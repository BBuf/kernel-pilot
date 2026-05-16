import torch
import pytest

from quack.symmetric_dense_gemm_sm90 import symmetric_dense_gemm

class TestSymmetricGemm:
    """Unit tests for symmetric dense GEMM wrapper."""
    
    @pytest.fixture(params=[torch.float16, torch.bfloat16, torch.float32])
    def dtype(self, request):
        """Test different data types."""
        return request.param
    
    @property
    def default_shape(self):
        """Default shape for most tests (L, M, K)."""
        return (2, 1024, 512)
    
    def torch_reference(self, a, b=None, c=None, alpha=1.0, beta=1.0):
        """Reference implementation using PyTorch operations.
        
        Args:
            a: Input tensor A of shape (L, M, K)
            b: Input tensor B of shape (L, M, K) - if None, uses A (symmetric case)
            c: Optional bias tensor C of shape (L, M, M)
            alpha: Scaling factor for A @ B^T
            beta: Scaling factor for C
            
        Returns:
            Result tensor of shape (L, M, M)
        """
        if b is None:
            b = a
            
        # Use einsum for batched matrix multiplication: A @ B^T
        # a: (L, M, K), b: (L, M, K) -> result: (L, M, M)
        result = alpha * torch.einsum('lmk,lnk->lmn', a, b)
        
        if c is not None:
            result = result + beta * c
                
        return result
    
    def create_test_tensor(self, L, M, K, dtype, device, stride_pattern="m_major", seed=None):
        """Create test tensor with specified stride pattern.
        
        Args:
            L, M, K: Tensor dimensions
            dtype: Data type
            device: Device ('cuda' or 'cpu')
            stride_pattern: How to arrange strides - 'm_major' means M has stride 1, 'k_major' means K has stride 1
            seed: Random seed for reproducibility
        """
        if stride_pattern == "m_major":
            # M has stride 1: (L, M, K) with strides (M*K, 1, M)
            tensor = torch.empty_strided(
                (L, M, K), 
                (M*K, 1, M), 
                dtype=dtype, 
                device=device
            )
        elif stride_pattern == "k_major":
            # K has stride 1: (L, M, K) with strides (M*K, K, 1)
            tensor = torch.empty_strided(
                (L, M, K), 
                (M*K, K, 1), 
                dtype=dtype, 
                device=device
            )
        else:
            raise ValueError(f"Unsupported stride pattern: {stride_pattern}")
            
        # Fill with random data
        if seed is not None:
            torch.manual_seed(seed)
        tensor.uniform_(-2, 2)
        return tensor
    
    def create_symmetric_tensor(self, L, M, dtype, device, seed=None):
        """Create a symmetric tensor of shape (L, M, M)."""
        if seed is not None:
            torch.manual_seed(seed)
            
        tensor = torch.randn(L, M, M, dtype=dtype, device=device)
        
        for l in range(L):
            matrix = tensor[l, :, :]
            tensor[l, :, :] = (matrix + matrix.T) / 2
            
        return tensor
    
    def test_basic_symmetric_gemm(self, dtype):
        """Test basic symmetric GEMM without bias."""
        if not torch.cuda.is_available():
            pytest.skip("CUDA not available")
            
        L, M, K = self.default_shape
        device = 'cuda'
        
        # Create input tensor A with stride 1 along M dimension
        a = self.create_test_tensor(L, M, K, dtype, device, "m_major", seed=42)
        
        print(f"a.shape = {a.shape}, a.stride = {a.stride()}")
        
        # Test symmetric case (B = A)
        result_quack = symmetric_dense_gemm(a, a)
        result_torch = self.torch_reference(a, a)
        
        assert result_quack.shape == result_torch.shape == (L, M, M)

        if dtype == torch.float32:
            torch.testing.assert_close(result_quack, result_torch, atol=1e-4, rtol=1e-4)
        else:  # float16, bfloat16
            torch.testing.assert_close(result_quack, result_torch, atol=1e-2, rtol=1e-2)
    
    def test_symmetric_gemm_with_bias(self, dtype):
        """Test symmetric GEMM with bias tensor C."""
        if not torch.cuda.is_available():
            pytest.skip("CUDA not available")
            
        L, M, K = self.default_shape
        device = 'cuda'
        
        # Create input tensors
        a = self.create_test_tensor(L, M, K, dtype, device, "m_major", seed=42)
        c = self.create_symmetric_tensor(L, M, dtype, device, seed=123)
        
        # Compute with our wrapper
        result_quack = symmetric_dense_gemm(a, a, c=c)
        
        # Compute reference
        result_torch = self.torch_reference(a, a, c=c)
        
        # Check shapes match
        assert result_quack.shape == result_torch.shape == (L, M, M)
        
        # Check values match
        if dtype == torch.float32:
            torch.testing.assert_close(result_quack, result_torch, atol=1e-4, rtol=1e-4)
        else:
            torch.testing.assert_close(result_quack, result_torch, atol=1e-2, rtol=1e-2)
    
    def test_alpha_beta_scaling(self, dtype):
        """Test alpha and beta scaling factors."""
        if not torch.cuda.is_available():
            pytest.skip("CUDA not available")
            
        L, M, K = self.default_shape
        device = 'cuda'
        alpha, beta = 2.5, 0.5
        
        # Create input tensors
        a = self.create_test_tensor(L, M, K, dtype, device, "m_major", seed=42)
        c = self.create_symmetric_tensor(L, M, dtype, device, seed=123)
        
        # Compute with our wrapper
        result_quack = symmetric_dense_gemm(a, a, c=c, alpha=alpha, beta=beta)
        
        # Compute reference
        result_torch = self.torch_reference(a, a, c=c, alpha=alpha, beta=beta)
        
        # Check values match
        if dtype == torch.float32:
            torch.testing.assert_close(result_quack, result_torch, atol=1e-4, rtol=1e-4)
        else:
            torch.testing.assert_close(result_quack, result_torch, atol=1e-2, rtol=1e-2)
    
    def test_symmetry_property(self, dtype):
        """Test that output is actually symmetric (D = D^T)."""
        if not torch.cuda.is_available():
            pytest.skip("CUDA not available")
            
        L, M, K = self.default_shape
        device = 'cuda'
        
        # Create input tensor
        a = self.create_test_tensor(L, M, K, dtype, device, "m_major", seed=42)
      
        # Compute symmetric GEMM
        result = symmetric_dense_gemm(a, a)
        
        # Check symmetry for each batch
        for l in range(L):
            matrix = result[l, :, :]
            torch.testing.assert_close(matrix, matrix.T, atol=1e-6, rtol=1e-6)
    
    def test_different_sizes(self):
        """Test various matrix sizes to ensure robustness."""
        if not torch.cuda.is_available():
            pytest.skip("CUDA not available")
            
        device = 'cuda'
        dtype = torch.float16
        
        test_sizes = [
            (3, 128, 128),  
            (5, 256, 256),  
            (5, 1024, 1024), 
            (3, 2048, 2048),  
            (1, 4096, 4096),
        ]
        
        for L, M, K in test_sizes:
            a = self.create_test_tensor(L, M, K, dtype, device, "m_major", seed=42)
    
            result = symmetric_dense_gemm(a, a)
            expected = self.torch_reference(a, a)
            
            assert result.shape == (L, M, M)
            torch.testing.assert_close(result, expected, atol=1e-2, rtol=1e-2)
            
            # Verify symmetry
            for l in range(L):
                matrix = result[l, :, :]
                torch.testing.assert_close(matrix, matrix.T, atol=1e-6, rtol=1e-6)
    
    def test_different_stride_patterns(self, dtype):
        """Test symmetric GEMM with different stride patterns (m_major vs k_major)."""
        if not torch.cuda.is_available():
            pytest.skip("CUDA not available")
            
        L, M, K = self.default_shape
        device = 'cuda'
        
        a_m_major = self.create_test_tensor(L, M, K, dtype, device, "m_major", seed=42)
        
        data_contiguous = a_m_major.contiguous()
        a_k_major = torch.empty_strided(
            (L, M, K), 
            (M*K, K, 1), 
            dtype=dtype, 
            device=device
        )
        a_k_major.copy_(data_contiguous)
        
        assert torch.equal(a_m_major, a_k_major), "Input tensors should have identical values"
        assert a_m_major.stride() != a_k_major.stride(), "Stride patterns should be different"
        
        result_m_major = symmetric_dense_gemm(a_m_major, a_m_major)
        result_k_major = symmetric_dense_gemm(a_k_major, a_k_major)
        
        assert result_m_major.shape == result_k_major.shape == (L, M, M)
        
        if dtype == torch.float32:
            torch.testing.assert_close(result_m_major, result_k_major, atol=1e-6, rtol=1e-6)
        else: 
            torch.testing.assert_close(result_m_major, result_k_major, atol=1e-4, rtol=1e-4)
        
        expected = self.torch_reference(a_m_major, a_m_major)
        
        if dtype == torch.float32:
            torch.testing.assert_close(result_m_major, expected, atol=1e-4, rtol=1e-4)
            torch.testing.assert_close(result_k_major, expected, atol=1e-4, rtol=1e-4)
        else:
            torch.testing.assert_close(result_m_major, expected, atol=1e-2, rtol=1e-2)
            torch.testing.assert_close(result_k_major, expected, atol=1e-2, rtol=1e-2)

def run_tests():
    """Run all tests manually (for debugging)."""
    test_class = TestSymmetricGemm()
    
    try:
        # Test basic functionality
        print("Testing basic symmetric GEMM...")
        test_class.test_basic_symmetric_gemm(torch.float16)
        print("✓ Basic test passed")
        
        # Test with bias
        print("Testing with bias...")
        test_class.test_symmetric_gemm_with_bias(torch.float16)
        print("✓ Bias test passed")
        
        # Test scaling
        print("Testing alpha/beta scaling...")
        test_class.test_alpha_beta_scaling(torch.float16)
        print("✓ Scaling test passed")
        
        # Test symmetry
        print("Testing symmetry property...")
        test_class.test_symmetry_property(torch.float16)
        print("✓ Symmetry test passed")

        # Test different sizes
        print("Testing different sizes...")
        test_class.test_different_sizes()
        print("✓ Different sizes test passed")
        
        # Test different stride patterns
        print("Testing different stride patterns...")
        test_class.test_different_stride_patterns(torch.float16)
        print("✓ Different stride patterns test passed")
        
        print("\n🎉 All tests passed!")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    run_tests()