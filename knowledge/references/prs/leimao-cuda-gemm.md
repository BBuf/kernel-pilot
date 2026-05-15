# Lei Mao CUDA GEMM Optimization PR Knowledge Notes

Repository: <https://github.com/leimao/CUDA-GEMM-Optimization>

This page is the production-PR layer for kernel-knowledge. It keeps merged PRs with CUDA/NVIDIA target evidence, real kernel/source changes, and an optimization/performance mechanism such as tuning, fusion, tensor-core paths, memory movement, scheduling, profiling, or benchmark-backed speed work. Release, CI-only, formatting, dependency-only, correctness-only, and non-target-backend PRs are filtered out.

## Repository Source Scan

## Coverage Summary

| Category | CUDA optimization PRs |
| --- | ---: |
| GEMM / Quantization | 1 |

## Pull Request Case Notes

### GEMM / Quantization

Use this section for: Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate.
NCU first look: Tensor pipe %, DRAM/L2 bytes, active cycles, register pressure, and scale-load traffic.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#6](https://github.com/leimao/CUDA-GEMM-Optimization/pull/6) Improve WMMA GEMM | 2024-07-19 | gemm_quant, benchmark_test, memory_primitives, arch_pipeline | * Fixed a synchronization bug. * Created a few device helper functions. * Slightly improve the WMMA GEMM Performance. | kernel: `include/cuda_gemm.hpp`, `include/cuda_gemm_utils.cuh`, `src/05_2d_block_tiling_2d_thread_tiling_matrix_transpose.cu`, `src/05_2d_block_tiling_2d_thread_tiling_matrix_transpose_vectorized_memory_access.cu`<br>benchmark: `include/profile_utils.cuh`, `src/profile_cuda_gemm_fp16.cu`, `src/profile_cuda_gemm_fp32.cu`<br>docs: `README.md`<br>other: `CMakeLists.txt`, `docker/gemm-cuda.Dockerfile`, `src/02_2d_block_tiling.cu`, `src/02_2d_block_tiling_vectorized_memory_access.cu` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |

## Per-PR Ledger Fields

When using an idea from this page, add one row to `artifacts/source-idea-ledger.md` with:

| Field | Value to record |
| --- | --- |
| Source key | `<repo>#<pr-number>` |
| Code evidence | Kernel, wrapper, benchmark, and test paths opened from the PR diff |
| Hypothesis | The concrete optimization idea derived from the PR |
| First experiment | Candidate version and benchmark shape set |
| Result | Correctness, geomean, best/worst cases, and NCU digest path |
| Do-not-reread key | Same as source key unless a single PR yields multiple independent ideas |

## How To Use This Page

- During the initial knowledge pass, read the category matching the target kernel and copy PR URL, changed paths, and hypothesis into the source idea ledger.
- During plateau expansion, choose PRs not already present in ledger do-not-reread keys; inspect the diff, linked issue, changed tests, and benchmark files before using the idea.
- Treat PR code as baseline/prior art unless the task and license allow copying or adapting it. When copied, record exact PR, commit, files, notice, and first delta.
