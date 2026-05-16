// provenance: derived from pr-cutlass-2139, kernel-nvfp4-gemm, hw-nvfp4; not upstream code
// origin: wiki/kernels/nvfp4-gemm.md Phase 3 variant

// Minimal NVFP4 GEMM skeleton. Packs 2x FP4 per byte; scale factors
// are UE8M0 per 16-element block. tcgen05.mma handles both.

#include <cuda_fp4.h>
#include <cuda_fp8.h>
#include <cstdint>

constexpr int BLOCK_SCALE = 16;  // NVFP4 scale granularity

template <int TILE_M, int TILE_N, int TILE_K>
__device__ void nvfp4_gemm_tile(
    uint32_t tmem_acc,
    const __nv_fp4_e2m1* A, const __nv_fp4_e2m1* B,
    const __nv_fp8_e4m3* SFA, const __nv_fp8_e4m3* SFB,
    int M, int N, int K)
{
    // Launch with tcgen05.mma.cta_group::1.kind::f8f6f4.block_scale
    // A descriptor encodes {A tile, SFA tile}; similarly for B.
    if (threadIdx.x == 0) {
        uint64_t desc_a = make_nvfp4_desc(A, SFA);
        uint64_t desc_b = make_nvfp4_desc(B, SFB);
        uint32_t sf_tmem = 0;  // SFA/SFB packed into dedicated TMEM rows
        asm volatile(
            "tcgen05.mma.cta_group::1.kind::f8f6f4.block_scale "
            "[%0], %1, %2, [%3], %4, 1;"
            :: "r"(tmem_acc), "l"(desc_a), "l"(desc_b), "r"(sf_tmem), "r"(0));
    }
}
