# Simon Boehm SGEMM Worklog

Article: <https://siboehm.com/articles/22/CUDA-MMM>

Code: <https://github.com/siboehm/SGEMM_CUDA>

Use this source when the loop needs a clean CUDA C++ GEMM optimization ladder.

## Kernel Ladder

| Step | Code path | Optimization idea |
| --- | --- | --- |
| 1 | `src/kernels/1_naive.cuh` | one thread computes one C element |
| 2 | `src/kernels/2_kernel_global_mem_coalesce.cuh` | coalesced global memory access |
| 3 | `src/kernels/3_kernel_shared_mem_blocking.cuh` | shared-memory blocking |
| 4 | `src/kernels/4_kernel_1D_blocktiling.cuh` | 1D block tiling |
| 5 | `src/kernels/5_kernel_2D_blocktiling.cuh` | 2D block tiling |
| 6 | `src/kernels/6_kernel_vectorize.cuh` | vectorized memory access |
| 7 | `src/kernels/7_kernel_resolve_bank_conflicts.cuh` | shared-memory bank conflict fix |
| 8 | `src/kernels/8_kernel_bank_extra_col.cuh` | padded shared tile |
| 9 | `src/kernels/9_kernel_autotuned.cuh` | parameter autotuning |
| 10 | `src/kernels/10_kernel_warptiling.cuh` | warp tiling |
| 11 | `src/kernels/11_kernel_double_buffering.cuh` | double buffering |
| 12 | `src/kernels/12_kernel_double_buffering.cuh` | refined double buffering |

## Support Code

| Path | Use |
| --- | --- |
| `src/runner.cu` | dispatch, cuBLAS comparison, timing |
| `src/kernels.cuh` | kernel registration |
| `scripts/bank_calc.py` | bank conflict reasoning |
| `benchmark_results/` | reference result snapshots |

## Search Patterns

```bash
rg -n "sgemm|coalesce|shared|vector|bank|warptiling|double|BM|BN|BK|TM|TN" src scripts README.md
```

## Optimization Signals

- Early steps: DRAM throughput and global memory sectors.
- Shared-memory steps: bank conflicts and shared throughput.
- Warp tiling/double buffering: occupancy, register pressure, issue stalls,
  and compute pipe utilization.
