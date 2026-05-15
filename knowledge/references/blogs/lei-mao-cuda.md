# Lei Mao CUDA Programming

Index: <https://leimao.github.io/blog/CUDA-Programming/>

Code: <https://github.com/leimao/CUDA-GEMM-Optimization>

Use this source for educational CUDA kernels with explicit optimization stages,
especially GEMM, bank conflicts, reductions, transpose, and profiling.

## Code Map

| Kernel family | Paths | What to extract |
| --- | --- | --- |
| GEMM v00-v01 | `src/00_non_coalesced_global_memory_access.cu`, `src/01_coalesced_global_memory_access.cu` | coalescing delta and baseline harness |
| 2D block tiling | `src/02_2d_block_tiling*.cu` | shared-memory tiling |
| 1D/2D thread tiling | `src/03_*`, `src/04_*` | per-thread work granularity |
| Matrix-transposed tiles | `src/05_*`, `src/06_*` | shared-memory layout and bank-conflict mitigation |
| Warp tiling | `src/06_2d_block_tiling_2d_warp_tiling*` | warp-level partitioning |
| WMMA | `src/07_*wmma*.cu` | tensor-core transition point |
| Benchmark harness | `src/profile_cuda_gemm_fp16.cu`, `src/profile_cuda_gemm_fp32.cu` | shape sweep and timing |
| Utilities | `include/cuda_gemm_utils.cuh`, `include/profile_utils.cuh` | launch/timing helpers |

## Search Patterns

```bash
rg -n "coalesced|vectorized|thread_tiling|warp_tiling|matrix_transpose|wmma|BLOCK_TILE|THREAD_TILE|profile" src include
```

## Optimization Signals

- Compare each ladder step with one profiler question: coalescing, shared tile,
  vectorization, bank conflicts, warp tiling, double buffering, or WMMA.
- Use when a production kernel needs a simple CUDA C++ sanity candidate before
  moving to CUTLASS/CuTe/Triton/TileLang.
