from typing import Optional
from functools import partial
from torch import Tensor
from quack.gemm_act import GemmActMixin, GemmActSm90, act_fn_map, gemm_act
from quack.gemm_sm90 import GemmSm90
from quack.gemm_sm100 import GemmSm100
from quack.tile_scheduler import TriangularTileScheduler
from quack.gemm_wrapper_utils import GemmWrapperBase
from quack.cute_dsl_utils import get_device_capacity, get_max_active_clusters
import cutlass
import cutlass.cute as cute
import cutlass.torch as cutlass_torch
from cutlass import Float32
from cutlass.cute.runtime import make_ptr

class GemmSymmetricMixin(GemmActMixin, GemmSm90):
    def get_scheduler_class(self, varlen_m: bool = False):
        return TriangularTileScheduler

class GemmSymmetricSm90(GemmSymmetricMixin, GemmSm90):
    pass

class GemmSymmetricSm100(GemmSymmetricMixin, GemmSm100):
    pass

def gemm_symmetric(
    A: Tensor,  # (l, m, k)
    B: Tensor,  # (l, m, k)
    D: Optional[Tensor],  # (l, m, m)
    C: Optional[Tensor],  # (l, m, m) 
    tile_count_semaphore: Optional[Tensor],  # (1,)
    activation: Optional[str],
    tile_M: int,
    tile_N: int,
    cluster_M: int,
    cluster_N: int,
    pingpong: bool = False,
    persistent: bool = True,
    max_swizzle_size: int = 8,
    alpha: float | Tensor = 1.0,
    beta: float | Tensor = 1.0,
) -> None:
    assert activation in act_fn_map, f"Unsupported activation {activation}"

    # Tranpose D so the "activation" is a write to the mirrored tile
    PostAct = D.mT

    L, M, K, N, tensor_infos = GemmWrapperBase.validate_and_prepare_tensors(
        A, B, D, C, additional_tensors={"PostAct": PostAct}
    )
    assert M == N, "M and N must be the same; symmetric gemm only supports square matrices"
    GemmWrapperBase.permute_tensors(tensor_infos)
    GemmWrapperBase.extract_dtypes(tensor_infos)
    major_configs = {
        "A": ("m", "k", "l"),
        "B": ("n", "k", "l"),
        "D": ("m", "n", "l"),
        "C": ("m", "n", "l"),
        "PostAct": ("m", "n", "l"),
    }
    GemmWrapperBase.determine_major_orders(tensor_infos, major_configs)

    device_capacity = get_device_capacity(A.device)
    assert device_capacity[0] in [9, 10], "Only SM90 and SM100 are supported"
    GemmCls = GemmSymmetricSm90 if device_capacity[0] == 9 else GemmSymmetricSm100
    # TODO: implement dynamic persistent
    if device_capacity[0] > 9:
        tile_count_semaphore = None

    acc_dtype = cutlass.Float32
    tile_shape_mn = (tile_M, tile_N)
    cluster_shape_mnk = (cluster_M, cluster_N, 1)
    if not GemmCls.is_valid_dtypes(
        tensor_infos["A"].dtype,
        tensor_infos["B"].dtype,
        acc_dtype,
        tensor_infos["D"].dtype,
        tensor_infos["A"].major,
        tensor_infos["B"].major,
    ):
        raise TypeError("Skipping due to unsupported combination of types and majors")

    max_active_clusters = get_max_active_clusters(cluster_M * cluster_N) if persistent else 0
    GemmWrapperBase.create_cute_tensors({k: v for k, v in tensor_infos.items()}, major_configs)

    def scalar_arg(scalar: float | Tensor):
        if isinstance(scalar, float):
            return Float32(scalar) if scalar != 1.0 else None
        else:
            assert isinstance(scalar, Tensor)
            return make_ptr(Float32, scalar.data_ptr(), cute.AddressSpace.gmem, assumed_align=4)

    act_fn = act_fn_map[activation]
    epi_args = GemmCls.EpilogueArguments(tensor_infos["PostAct"].cute_tensor, act_fn, scalar_arg(alpha), scalar_arg(beta))
    scheduler_args = GemmWrapperBase.create_scheduler_args(
        max_active_clusters, tile_count_semaphore, max_swizzle_size=max_swizzle_size
    )
    varlen_args = None

    current_stream = cutlass_torch.current_stream()
    compile_key = GemmWrapperBase.get_compile_key(
        tensor_infos,
        activation,
        tile_shape_mn,
        cluster_shape_mnk,
        pingpong,
        persistent,
        tile_count_semaphore is not None,
        device_capacity,
        max_swizzle_size,
        2 if isinstance(alpha, Tensor) else (1 if alpha == 1.0 else 0),
        2 if isinstance(beta, Tensor) else (1 if beta == 1.0 else 0),
        key_tensor_names=("A", "B", "D", "PostAct", "C"),
    )
    cache = gemm_act.compile_cache
    if compile_key not in cache:
        if device_capacity[0] == 9:
            GemmCls = partial(GemmCls, pingpong=pingpong, is_persistent=persistent)
        gemm_obj = GemmCls(
            acc_dtype,
            tensor_infos["A"].dtype,
            tile_shape_mn,
            cluster_shape_mnk,
            gather_A=False,
        )
        cache[compile_key] = cute.compile(
            gemm_obj,
            tensor_infos["A"].cute_tensor,
            tensor_infos["B"].cute_tensor,
            tensor_infos["D"].cute_tensor,
            tensor_infos["C"].cute_tensor,
            epi_args,
            scheduler_args,
            varlen_args,
            current_stream,
        )
    cache[compile_key](
        tensor_infos["A"].cute_tensor,
        tensor_infos["B"].cute_tensor,
        tensor_infos["D"].cute_tensor,
        tensor_infos["C"].cute_tensor,
        epi_args,
        scheduler_args,
        varlen_args,
        current_stream,
    )


gemm_act.compile_cache = {}
