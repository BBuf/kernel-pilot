# CUDA Blog Companion Kernel Reference

Use this when plateau research needs classic CUDA optimization examples with
both prose and code. Prefer these for memory coalescing, shared-memory bank
conflicts, reductions, transpose, and stepwise GEMM reasoning.

Source-only policy: do not query PR notes for these companion repositories.
Inspect the source paths, blog map, and current code directly.

## Primary Sources

| Source | Use for |
| --- | --- |
| `NVIDIA-developer-blog/code-samples` | Parallel Forall / NVIDIA blog companion kernels. |
| `NVIDIA/cuda-samples` | Official CUDA sample kernels and harnesses. |
| `leimao/CUDA-GEMM-Optimization` | Stepwise GEMM optimization and Nsight-friendly harness. |
| `siboehm/SGEMM_CUDA` | Worklog-style SGEMM progression from simple to optimized kernels. |
| `ColfaxResearch/cutlass-kernels` | CUTLASS/CuTe tutorial companion kernels. |

Detailed blog maps live in `../blogs/`:

- `../blogs/nvidia-cuda.md`
- `../blogs/simon-boehm-sgemm.md`
- `../blogs/lei-mao-cuda.md`
- `../blogs/yifan-yang-matmul.md`
- `../blogs/colfax.md`

## Code Map By Kernel Type

| Kernel type | Repos / paths | What to extract |
| --- | --- | --- |
| Warp/block reductions | `NVIDIA-developer-blog/code-samples/posts/parallel_reduction_with_shfl/{warp_reduce.h,block_reduce.h,device_reduce_*.h,main.cu}` | warp shuffle reduction, block aggregation, atomic variants |
| WMMA / tensor-core GEMM | `NVIDIA-developer-blog/code-samples/posts/tensor-cores/simpleTensorCoreGEMM.cu` | minimal WMMA load/mma/store and correctness harness |
| Classic SGEMM ladder | `siboehm/SGEMM_CUDA/src/kernels/{1_naive.cuh..12_kernel_double_buffering.cuh}` | coalescing, smem tiling, vectorization, bank fixes, warp tiling, double buffering |
| CUDA GEMM ladder | `leimao/CUDA-GEMM-Optimization/src/{00_*,01_*,02_*,03_*,04_*,05_*,06_*,07_*}` | non-coalesced to WMMA progression with profile harnesses |
| Transpose / memory movement | `ColfaxResearch/cfx-article-src/transpose-cute/`, `simveit/effective_transpose/` | shared-memory transpose, swizzle, TMA store/load, profiling variants |
| Mixed precision vector ops | `NVIDIA-developer-blog/code-samples/posts/mixed-precision/` | half conversion and simple low-precision arithmetic |
| Profiling instrumentation | `NVIDIA-developer-blog/code-samples/posts/nvtx/` | NVTX ranges and compiler/manual instrumentation |

## Search Patterns

```bash
rg -n "transpose|coalesc|bank|shared|TILE_DIM|BLOCK_ROWS|wmma|tensor core|gemm|reduction|scan" .
rg -n "ncu|nvprof|cudaEvent|GB/s|TFLOP|occupancy|profile" .
```

## Candidate Use

- Treat blog companion kernels as simple, readable baselines or hypothesis
  sources.
- If copying/adapting code, check the repo license and record source, commit,
  copied files, and first delta.
- Prefer translating one pattern at a time: coalesced load, padded shared tile,
  vectorized access, warp reduction, cp.async, or WMMA.

## NCU Focus

| Pattern | First metrics |
| --- | --- |
| Coalescing / transpose | global sectors, DRAM throughput, shared bank conflicts |
| GEMM | tensor pipe %, L2/DRAM bytes, shared-memory throughput, occupancy |
| Reductions | issue stalls, active cycles, global load/store sectors |
