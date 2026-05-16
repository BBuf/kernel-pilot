import math
import pytest
import torch

from quack.gemm_interface import (
    gemm,
    gemm_ref,
    gemm_act,
    gemm_relu_ref,
    gemm_dact,
    gemm_drelu_ref,
)

@pytest.mark.parametrize("input_dtype", [torch.bfloat16])
@pytest.mark.parametrize("n", [1504, 2048])
@pytest.mark.parametrize("k", [736, 4096])
def test_gemm(n, k, input_dtype):
    device = "cuda"
    torch.random.manual_seed(0)
    m = 1920
    x = torch.randn((m, k), device=device, dtype=input_dtype, requires_grad=True)
    x = x[::2]  # Testing non-contiguous
    w = (
        torch.randn((n, k), device=device, dtype=input_dtype)
        / math.sqrt(k)
    ).requires_grad_()
    out = gemm(x, w.mT)
    out_ref = gemm_ref(x.float(), w.float().mT)
    out_pt = gemm_ref(x, w.mT)
    assert out.shape == out_ref.shape, f"Output shape mismatch: {out.shape} vs {out_ref.shape}"
    assert out.shape == out_pt.shape, f"Output shape mismatch: {out.shape} vs {out_pt.shape}"
    assert (out - out_ref).abs().max() < 2 * (out_pt - out_ref).abs().max() + 1e-6


@pytest.mark.parametrize("input_dtype", [torch.bfloat16])
@pytest.mark.parametrize("n", [1504, 2048])
@pytest.mark.parametrize("k", [736, 4096])
def test_gemm_act(n, k, input_dtype):
    device = "cuda"
    torch.random.manual_seed(0)
    m = 1920
    A = torch.randn((m, k), device=device, dtype=input_dtype, requires_grad=True)
    B = (
        torch.randn((n, k), device=device, dtype=input_dtype) 
        / math.sqrt(k)
    ).requires_grad_()
    
    out_act, postact_act = gemm_act(A=A, B=B.mT, activation="relu")
    out_ref, postact_ref = gemm_relu_ref(A, B.mT)
    assert out_act.shape == out_ref.shape, f"Output shape mismatch: {out_act.shape} vs {out_ref.shape}"
    assert postact_act.shape == postact_ref.shape, f"PostAct shape mismatch: {postact_act.shape} vs {postact_ref.shape}"
    assert (out_act - out_ref).abs().max() < 1e-6, "Output value mismatch between gemm_act and ref"
    assert (postact_act - postact_ref).abs().max() < 1e-6, "PostAct value mismatch between gemm_act and ref"


# TODO: some bugs in gemm_dact
# @pytest.mark.parametrize("input_dtype", [torch.bfloat16])
# @pytest.mark.parametrize("n", [1504, 2048])
# @pytest.mark.parametrize("k", [736, 4096])
# def test_gemm_dact(n, k, input_dtype):
#     device = "cuda"
#     torch.random.manual_seed(0)
#     m = 1920
#     A = torch.randn((m, k), device=device, dtype=input_dtype, requires_grad=True)
#     B = (
#         torch.randn((n, k), device=device, dtype=input_dtype) 
#         / math.sqrt(k)
#     ).requires_grad_()
#     PreAct = torch.randn((m, n), device=device, dtype=input_dtype, requires_grad=True)
#     out_act, postact_act = gemm_dact(A=A, B=B.mT, PreAct=PreAct, activation="relu")
    
#     out_ref, postact_ref = gemm_drelu_ref(A, B.mT, PreAct)
    
#     assert out_act.shape == out_ref.shape, f"Output shape mismatch: {out_act.shape} vs {out_ref.shape}"
#     assert postact_act.shape == postact_ref.shape, f"PostAct shape mismatch: {postact_act.shape} vs {postact_ref.shape}"
#     assert (out_act - out_ref).abs().max() < 1e-6, "Output value mismatch between gemm_act and ref"
#     assert (postact_act - postact_ref).abs().max() < 1e-6, "PostAct value mismatch between gemm_act and ref"