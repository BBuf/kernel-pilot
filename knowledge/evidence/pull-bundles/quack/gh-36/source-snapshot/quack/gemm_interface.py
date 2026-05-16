# Copyright (c) 2025, Tri Dao
from typing import Optional, Tuple

import torch
import torch.nn.functional as F
from torch import Tensor

from quack.gemm_config import GemmConfig, get_all_configs

from quack.autotuner import autotune, AutotuneConfig
from quack.dense_gemm_sm90 import gemm_sm90
from quack.gemm_act_sm90 import gemm_act_sm90
from quack.gemm_dact_sm90 import gemm_dact_sm90


def gemm_swiglu_out_ref(
    A: Tensor, B: Tensor, out: Optional[Tensor], store_preact: bool
) -> (Tensor, Tensor):
    preact = torch.mm(A, B)
    out_ = F.silu(preact[..., ::2]) * preact[..., 1::2]
    if out is not None:
        out.copy_(out_)
    else:
        out = out_
    if not store_preact:
        preact = None
    return out, preact


@autotune(
    configs=[AutotuneConfig(config=c) for c in get_all_configs()],
    key=["out_dtype", "dynamic_scheduler"],
)
def gemm_tuned(
    A: Tensor,  # (M, K)
    B: Tensor,  # (K, N)
    C: Optional[Tensor] = None,  # (M, N)
    out_dtype: Optional[torch.dtype] = None,
    dynamic_scheduler: bool = False,
    config: Optional[GemmConfig] = None,
) -> (Tensor, Optional[Tensor]):
    if config is None:
        config = GemmConfig(tile_m=128, tile_n=192, cluster_m=2, cluster_n=1, pingpong=True)
    A, B = A.unsqueeze(0), B.mT.unsqueeze(0)  # (1, M, K), (1, N, K)
    if C is not None:
        C = C.unsqueeze(0)  # (1, M, N)
    out_dtype = A.dtype if out_dtype is None else out_dtype
    D = torch.empty((1, A.shape[1], B.shape[1]), dtype=out_dtype, device=A.device)
    tile_count_semaphore = (
        torch.zeros(1, dtype=torch.int32, device=A.device) if dynamic_scheduler else None
    )
    gemm_sm90(
        A if not config.swap_ab else B,
        B if not config.swap_ab else A,
        D if not config.swap_ab else D.mT,
        (C if not config.swap_ab else C.mT) if C is not None else None,
        tile_count_semaphore,
        config.tile_m,
        config.tile_n,
        config.cluster_m,
        config.cluster_n,
        config.pingpong,
    )
    return D.squeeze(0)


@autotune(
    configs=[AutotuneConfig(config=c) for c in get_all_configs()],
    key=["activation", "out_dtype", "postact_dtype", "store_preact"],
)
def gemm_act_tuned(
    A: Tensor,  # (M, K)
    B: Tensor,  # (K, N)
    C: Optional[Tensor] = None,  # (M, N)
    activation: Optional[str] = None,  # None, "relu", "relu_sq", "gelu_tanh_approx"
    out_dtype: Optional[torch.dtype] = None,
    postact_dtype: Optional[torch.dtype] = None,
    store_preact: bool = True,
    config: Optional[GemmConfig] = None,
) -> (Tensor, Optional[Tensor]):
    if config is None:
        config = GemmConfig(tile_m=128, tile_n=192, cluster_m=2, cluster_n=1, pingpong=True)
    A, B = A.unsqueeze(0), B.mT.unsqueeze(0)  # (1, M, K), (1, N, K)
    if C is not None:
        C = C.unsqueeze(0)  # (1, M, N)
    out_dtype = A.dtype if out_dtype is None else out_dtype
    postact_dtype = A.dtype if postact_dtype is None else postact_dtype
    if store_preact:
        D = torch.empty((1, A.shape[1], B.shape[1]), dtype=out_dtype, device=A.device)
    else:
        D = None
    PostAct = torch.empty((1, A.shape[1], B.shape[1]), dtype=postact_dtype, device=A.device)
    gemm_act_sm90(
        A if not config.swap_ab else B,
        B if not config.swap_ab else A,
        (D if not config.swap_ab else D.mT) if D is not None else None,
        (C if not config.swap_ab else C.mT) if C is not None else None,
        PostAct if not config.swap_ab else PostAct.mT,
        activation,
        config.tile_m,
        config.tile_n,
        config.cluster_m,
        config.cluster_n,
        config.pingpong,
    )
    return D.squeeze(0), PostAct.squeeze(0)


@autotune(
    configs=[AutotuneConfig(config=c) for c in get_all_configs()],
    key=["activation", "out_dtype", "postact_dtype", "dynamic_scheduler"],
)
def gemm_dact_tuned(
    A: Tensor,  # (M, K)
    B: Tensor,  # (K, N)
    PreAct: Tensor,  # (M, N)
    activation: Optional[str] = None,  # None, "relu", "relu_sq", "gelu_tanh_approx"
    out_dtype: Optional[torch.dtype] = None,
    postact_dtype: Optional[torch.dtype] = None,
    dynamic_scheduler: bool = True,
    config: Optional[GemmConfig] = None,
) -> (Tensor, Optional[Tensor]):
    if config is None:
        config = GemmConfig(tile_m=128, tile_n=192, cluster_m=2, cluster_n=1, pingpong=True)
    A, B = A.unsqueeze(0), B.mT.unsqueeze(0)  # (1, M, K), (1, N, K)
    PreAct = PreAct.unsqueeze(0)  # (1, M, N)
    out_dtype = A.dtype if out_dtype is None else out_dtype
    postact_dtype = A.dtype if postact_dtype is None else postact_dtype
    D = torch.empty((1, A.shape[1], B.shape[1]), dtype=out_dtype, device=A.device)
    PostAct = torch.empty((1, A.shape[1], B.shape[1]), dtype=postact_dtype, device=A.device)
    tile_count_semaphore = (
        torch.zeros(1, dtype=torch.int32, device=A.device) if dynamic_scheduler else None
    )
    gemm_dact_sm90(
        A if not config.swap_ab else B,
        B if not config.swap_ab else A,
        D if not config.swap_ab else D.mT,
        PreAct if not config.swap_ab else PreAct.mT,
        PostAct if not config.swap_ab else PostAct.mT,
        tile_count_semaphore,
        activation,
        config.tile_m,
        config.tile_n,
        config.cluster_m,
        config.cluster_n,
        config.pingpong,
    )
    return D.squeeze(0), PostAct.squeeze(0)


@torch.library.custom_op("quack::gemm", mutates_args=(), device_types="cuda")
def gemm(
    A: Tensor, B: Tensor, out_dtype: Optional[torch.dtype] = None, dynamic_scheduler: bool = False
) -> Tensor:
    return gemm_tuned(A, B, None, out_dtype, dynamic_scheduler)


@torch.library.register_fake("quack::gemm")
def gemm_ref(
    A: Tensor, B: Tensor, out_dtype: Optional[torch.dtype] = None, dynamic_scheduler: bool = False
) -> Tensor:
    out_dtype = A.dtype if out_dtype is None else out_dtype
    return torch.mm(A, B).to(out_dtype)


@torch.library.custom_op("quack::gemm_add", mutates_args=(), device_types="cuda")
def gemm_add(
    A: Tensor,
    B: Tensor,
    C: Tensor,
    out_dtype: Optional[torch.dtype] = None,
    dynamic_scheduler: bool = False,
) -> Tensor:
    return gemm_tuned(A, B, C, out_dtype, dynamic_scheduler)


@torch.library.register_fake("quack::gemm_add")
def gemm_add_ref(
    A: Tensor,
    B: Tensor,
    C: Tensor,
    out_dtype: Optional[torch.dtype] = None,
    dynamic_scheduler: bool = False,
) -> Tensor:
    out_dtype = A.dtype if out_dtype is None else out_dtype
    return (C + torch.mm(A, B)).to(out_dtype)


@torch.library.custom_op("quack::gemm_add_t", mutates_args=(), device_types="cuda")
def gemm_t_add(A: Tensor, B: Tensor, C: Tensor) -> Tensor:
    return gemm_tuned(A, B.T, C)


@torch.library.register_fake("quack::gemm_add_t")
def gemm_t_add_ref(A: Tensor, B: Tensor, C: Tensor) -> Tensor:
    return gemm_add_ref(A, B.T, C)


# Specifying the schema manually here since torch.library._infer_schema doesn't work when return
# type is a tuple of Tensor
@torch.library.custom_op(
    "quack::gemm_act",
    mutates_args=(),
    device_types="cuda",
    schema="(Tensor A, Tensor B, Tensor? C=None, str? activation=None, ScalarType? out_dtype=None, ScalarType? postact_dtype=None, bool store_preact=True) -> (Tensor?, Tensor)",
)
def gemm_act(
    A: Tensor,
    B: Tensor,
    C: Optional[Tensor] = None,
    activation: Optional[str] = None,
    out_dtype: Optional[torch.dtype] = None,
    postact_dtype: Optional[torch.dtype] = None,
    store_preact: bool = True,
) -> Tuple[Tensor, Tensor]:
    return gemm_act_tuned(A, B, C, activation, out_dtype, postact_dtype, store_preact)


@torch.library.register_fake("quack::gemm_act")
def gemm_act_ref(
    A: Tensor,
    B: Tensor,
    C: Optional[Tensor] = None,
    activation: Optional[str] = None,
    out_dtype: Optional[torch.dtype] = None,
    postact_dtype: Optional[torch.dtype] = None,
) -> Tuple[Tensor, Tensor]:
    out_dtype = A.dtype if out_dtype is None else out_dtype
    postact_dtype = A.dtype if postact_dtype is None else postact_dtype
    if C is None:
        out = torch.mm(A, B).to(out_dtype)
    else:
        out = (C + torch.mm(A, B)).to(out_dtype)
    postact = out.to(postact_dtype)
    return out, postact


def gemm_relu_ref(A: Tensor, B: Tensor) -> Tensor:
    # A: (M, K), B: (K, N)
    out = torch.mm(A, B)
    postact = torch.clamp(out, min=0.0)
    return out, postact


# Specifying the schema manually here since torch.library._infer_schema doesn't work when return
# type is a tuple of Tensor
@torch.library.custom_op(
    "quack::gemm_dact",
    mutates_args=(),
    device_types="cuda",
    schema="(Tensor A, Tensor B, Tensor PreAct, str? activation=None, ScalarType? out_dtype=None, ScalarType? postact_dtype=None, bool dynamic_scheduler=True) -> (Tensor, Tensor)",
)
def gemm_dact(
    A: Tensor,
    B: Tensor,
    PreAct: Tensor,
    activation: Optional[str] = None,
    out_dtype: Optional[torch.dtype] = None,
    postact_dtype: Optional[torch.dtype] = None,
    dynamic_scheduler: bool = True,
) -> Tuple[Tensor, Tensor]:
    return gemm_dact_tuned(A, B, PreAct, activation, out_dtype, postact_dtype, dynamic_scheduler)


def gemm_drelu_ref(A: Tensor, B: Tensor, preact: Tensor) -> (Tensor, Tensor):
    # A: (M, K), B: (K, N), preact: (M, N)
    dout = torch.mm(A, B)
    dx = torch.where(preact > 0, dout, torch.zeros_like(dout))
    postact = torch.clamp(preact, min=0.0)
    return dx, postact


def gemm_dswiglu_ref(A: Tensor, B: Tensor, preact: Tensor) -> (Tensor, Tensor):
    # A: (M, K), B: (K, N), preact: (M, 2 * N)
    dout = torch.mm(A, B)
    p0, p1 = preact[..., ::2], preact[..., 1::2]
    sigmoid = torch.sigmoid(p0)
    silu = F.silu(p0)
    postact = silu * p1
    d0 = sigmoid * (1 + p0 * (1 - sigmoid)) * p1 * dout
    d1 = F.silu(p0) * dout
    out = torch.stack([d0, d1], dim=-1).reshape(d0.shape[:-1] + (2 * d0.shape[-1],))
    return out, postact
