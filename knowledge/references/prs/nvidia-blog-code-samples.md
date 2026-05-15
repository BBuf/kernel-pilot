# NVIDIA Developer Blog Code Samples PR Knowledge Notes

Repository: <https://github.com/NVIDIA-developer-blog/code-samples>

This page is the production-PR layer for kernel-knowledge. It keeps merged PRs with CUDA/NVIDIA target evidence, real kernel/source changes, and an optimization/performance mechanism such as tuning, fusion, tensor-core paths, memory movement, scheduling, profiling, or benchmark-backed speed work. Release, CI-only, formatting, dependency-only, correctness-only, and non-target-backend PRs are filtered out.

## Repository Source Scan

## Coverage Summary

| Category | CUDA optimization PRs |
| --- | ---: |
| GEMM / Quantization | 1 |
| Benchmark / Test Evidence | 2 |
| Other Kernel Cases | 1 |

## Pull Request Case Notes

### GEMM / Quantization

Use this section for: Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate.
NCU first look: Tensor pipe %, DRAM/L2 bytes, active cycles, register pressure, and scale-load traffic.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#51](https://github.com/NVIDIA-developer-blog/code-samples/pull/51) fix the output error check in tensor cores wmma sample | 2023-05-01 | gemm_quant | -- fix the output error check to use rel_error -- fix cublas time reporting issue due to startup time addition -- add option in makefile to specify arch at build time | kernel: `posts/tensor-cores/simpleTensorCoreGEMM.cu`<br>other: `posts/tensor-cores/Makefile` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |

### Benchmark / Test Evidence

Use this section for: Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code.
NCU first look: Use the PR's benchmark/profile command as the first replay target.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#49](https://github.com/NVIDIA-developer-blog/code-samples/pull/49) Add support for GUPS benchmark | 2023-03-02 | benchmark_test | This MR adds GUPS code to `code-samples`. Our version of GUPS is a GPU random access benchmark. It supports testing random access performance for both global memory and shared memory. The benchmark supports read, write, read_write, updates (with/without loops) access types. Besides the CUDA code for... | kernel: `posts/gups/LICENSE.gups.cu`, `posts/gups/gups.cu`, `posts/gups/run.py`<br>docs: `posts/gups/README.md`<br>other: `posts/gups/LICENSE`, `posts/gups/Makefile` | Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code. |
| [#60](https://github.com/NVIDIA-developer-blog/code-samples/pull/60) Fix shared memory Table size and accesses reporting in GUPS benchmark | 2025-09-23 | benchmark_test | This PR fixes the incorrect Table size and accesses per thread reporting for shared memory tests in the GUPS benchmark, addressing the issues raised by @rkarim2 in 56. Problem Previously, when running shared memory tests, the benchmark incorrectly reported: - Table size showed the global memory work... | kernel: `posts/gups/gups.cu` | Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code. |

### Other Kernel Cases

Use this section for: Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea.
NCU first look: Choose metrics based on the changed kernel family after opening the diff.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#3](https://github.com/NVIDIA-developer-blog/code-samples/pull/3) double fix coalescing.cu | 2014-09-15 | kernel_other | Here: https://github.com/parallel-forall/code-samples/blob/master/series/cuda-cpp/coalescing-global/coalescing.cu lines 54 and 70 are passing a double for the second argument: code block This is not really sensible and may trigger compiler warnings like this: coalescing.cu:70: warning: passing âdoub... | kernel: `series/cuda-cpp/coalescing-global/coalescing.cu` | Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea. |

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
