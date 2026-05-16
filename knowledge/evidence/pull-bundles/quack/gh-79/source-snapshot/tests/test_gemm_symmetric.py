import torch
import pytest

from quack.gemm_interface import gemm_symmetric


@pytest.mark.parametrize("dtype", [torch.float16, torch.bfloat16])
@pytest.mark.parametrize("L", [1, 3, 10])
@pytest.mark.parametrize("M", [128, 512, 1024, 4096])
@pytest.mark.parametrize("K", [128, 512, 2048])
@pytest.mark.parametrize("has_C", [False, True])
@pytest.mark.parametrize("alpha", [1.0, 2.5])
@pytest.mark.parametrize("beta", [1.0, 0.5])
def test_symmetric_gemm(dtype, L, M, K, has_C, alpha, beta):
    if not has_C and beta != 1.0:
        pytest.skip("beta only relevant with C")

    device = "cuda"
    torch.manual_seed(42)

    a = torch.empty_strided((L, M, K), (M * K, 1, M), dtype=dtype, device=device)
    a.uniform_(-2, 2)

    C = None
    if has_C:
        C = torch.randn(L, M, M, dtype=dtype, device=device)
        for l in range(L):
            C[l, :, :] = (C[l, :, :] + C[l, :, :].T) / 2

    a_ref = a.detach().clone().float()
    C_ref = C.detach().clone().float() if C is not None else None
    a_pt = a.detach().clone().to(dtype)
    C_pt = C.detach().clone().to(dtype) if C is not None else None

    out = gemm_symmetric(a, a.transpose(-2, -1), C=C, alpha=alpha, beta=beta)

    out_ref = torch.baddbmm(
        C_ref if C_ref is not None else torch.zeros(L, M, M, dtype=torch.float32, device=device),
        a_ref,
        a_ref.transpose(-2, -1),
        beta=beta if C_ref is not None else 0.0,
        alpha=alpha,
    )
    out_pt = torch.baddbmm(
        C_pt if C_pt is not None else torch.zeros(L, M, M, dtype=dtype, device=device),
        a_pt,
        a_pt.transpose(-2, -1),
        beta=beta if C_pt is not None else 0.0,
        alpha=alpha,
    )

    assert (out - out_ref).abs().max() < (out_pt - out_ref).abs().max() + 1e-6