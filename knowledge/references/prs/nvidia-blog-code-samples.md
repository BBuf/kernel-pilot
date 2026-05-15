# NVIDIA Developer Blog Code Samples PR Knowledge Notes

Repository: <https://github.com/NVIDIA-developer-blog/code-samples>

This page is the production-PR layer for kernel-knowledge. It favors merged PRs that changed kernels, dispatch, JIT/runtime integration, tuning policy, tests, benchmarks, or profiling evidence. Release, CI-only, formatting, pure version-bump, and non-target-backend PRs are filtered out.

## Repository Source Scan

## Coverage Summary

| Category | CUDA-kernel PRs |
| --- | ---: |
| GEMM / Quantization | 1 |
| Attention / KV / Decode | 2 |
| Memory / Primitives | 3 |
| Benchmark / Test Evidence | 6 |
| Other Kernel Cases | 4 |

## Pull Request Case Notes

### GEMM / Quantization

Use this section for: Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate.
NCU first look: Tensor pipe %, DRAM/L2 bytes, active cycles, register pressure, and scale-load traffic.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#51](https://github.com/NVIDIA-developer-blog/code-samples/pull/51) fix the output error check in tensor cores wmma sample | 2023-05-01 | gemm_quant | -- fix the output error check to use rel_error -- fix cublas time reporting issue due to startup time addition -- add option in makefile to specify arch at build time | kernel: `posts/tensor-cores/simpleTensorCoreGEMM.cu`<br>other: `posts/tensor-cores/Makefile` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |

### Attention / KV / Decode

Use this section for: Preserve page/KV/layout and plan-run contracts; profile memory traffic separately from math utilization.
NCU first look: Long scoreboard, L2/DRAM traffic, global-load sectors, tensor pipe %, and shared-memory bank conflicts.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#30](https://github.com/NVIDIA-developer-blog/code-samples/pull/30) New Changes | 2020-04-08 | attention_kv | createCudaEngine function has been updated to work with TRT 7 and add profile to deal with dynamic shape Batch size. This has been updated in all simpleOnnx files. softmax funtion had been removed in all files because we did not need it. saveImageAsPGM is added to simpleOnnx_1.cpp to save the result... | wrapper: `posts/TensorRT-introduction/ioHelper.cpp`, `posts/TensorRT-introduction/simpleOnnx.cpp`, `posts/TensorRT-introduction/simpleOnnx_1.cpp`, `posts/TensorRT-introduction/simpleOnnx_2.cpp`<br>other: `posts/TensorRT-introduction/Makefile`, `posts/TensorRT-introduction/ioHelper.o` | Preserve page/KV/layout and plan-run contracts; profile memory traffic separately from math utilization. |
| [#31](https://github.com/NVIDIA-developer-blog/code-samples/pull/31) Updating TensorRT-introduction to work with TRT7 and Dynamic Shape | 2020-04-08 | attention_kv | createCudaEngine function has been updated to work with TRT 7 and add profile to deal with dynamic shape Batch size. This has been updated in all simpleOnnx files. softmax funtion had been removed in all files because we did not need it. saveImageAsPGM is added to simpleOnnx_1.cpp to save the result... | wrapper: `posts/TensorRT-introduction/ioHelper.cpp`, `posts/TensorRT-introduction/simpleOnnx.cpp`, `posts/TensorRT-introduction/simpleOnnx_1.cpp`, `posts/TensorRT-introduction/simpleOnnx_2.cpp`<br>other: `posts/TensorRT-introduction/Makefile`, `posts/TensorRT-introduction/ioHelper.o` | Preserve page/KV/layout and plan-run contracts; profile memory traffic separately from math utilization. |

### Memory / Primitives

Use this section for: Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract.
NCU first look: DRAM throughput, L2 hit rate, memory sectors, shared-memory conflicts, and synchronization overhead.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#25](https://github.com/NVIDIA-developer-blog/code-samples/pull/25) Code examples for blog on grCUDA | 2019-11-01 | memory_primitives, compiler_runtime | Code examples for blog on grCUDA | kernel: `posts/grcuda/kernel/saxpy.cu`, `posts/grcuda/kernel/saxpy.py`, `posts/grcuda/kernel/saxpy_nvrtc.py`<br>docs: `posts/grcuda/README.md`<br>other: `posts/grcuda/R/cuml_dbscan.R`, `posts/grcuda/R/run_r.sh`, `posts/grcuda/mandelbrot/app.js`, `posts/grcuda/mandelbrot/license.txt` | Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract. |
| [#1](https://github.com/NVIDIA-developer-blog/code-samples/pull/1) American Options Post | 2014-03-05 | memory_primitives | This Pull Request contains the code for the American Option post. | docs: `posts/american-options/Readme.md`<br>other: `.gitmodules`, `posts/american-options/LongstaffSchwartz_vs10.sln`, `posts/american-options/LongstaffSchwartz_vs11.sln`, `posts/american-options/Makefile` | Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract. |
| [#43](https://github.com/NVIDIA-developer-blog/code-samples/pull/43) Math Library Blog Samples | 2022-05-31 | memory_primitives | Openblas and cuBLAS examples for math library blog | kernel: `posts/math-libraries-intro/cublas-example.cu`<br>wrapper: `posts/math-libraries-intro/openblas-example.cpp`<br>docs: `posts/math-libraries-intro/README.md`<br>other: `posts/math-libraries-intro/Makefile` | Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract. |

### Benchmark / Test Evidence

Use this section for: Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code.
NCU first look: Use the PR's benchmark/profile command as the first replay target.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#49](https://github.com/NVIDIA-developer-blog/code-samples/pull/49) Add support for GUPS benchmark | 2023-03-02 | benchmark_test | This MR adds GUPS code to `code-samples`. Our version of GUPS is a GPU random access benchmark. It supports testing random access performance for both global memory and shared memory. The benchmark supports read, write, read_write, updates (with/without loops) access types. Besides the CUDA code for... | wrapper: `posts/gups/run.py`<br>docs: `posts/gups/README.md`<br>other: `posts/gups/LICENSE`, `posts/gups/LICENSE.gups.cu`, `posts/gups/Makefile`, `posts/gups/gups.cu` | Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code. |
| [#36](https://github.com/NVIDIA-developer-blog/code-samples/pull/36) Add Unified Memory oversubscription benchmark | 2021-08-03 | benchmark_test | Adding benchmark for Unified Memory oversubscription blog post. CC: @nsakharnykh | docs: `posts/unified-memory-oversubscription/README.md`<br>other: `posts/unified-memory-oversubscription/Makefile`, `posts/unified-memory-oversubscription/uvm_oversubs.cu` | Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code. |
| [#58](https://github.com/NVIDIA-developer-blog/code-samples/pull/58) Fix overflow in type cast for GUPS benchmark | 2025-09-18 | benchmark_test | This PR fixes an integer overflow bug in the GUPS benchmark that prevents running with problem size n = 2^31. Changes - Changed `size_t n = (size_t)(1 << logn)` to `size_t n = ((size_t)1) << logn` in `posts/gups/gups.cu:461` - The issue was that `1 << logn` performs left shift on an `int` (1) before... | other: `posts/gups/gups.cu` | Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code. |
| [#60](https://github.com/NVIDIA-developer-blog/code-samples/pull/60) Fix shared memory Table size and accesses reporting in GUPS benchmark | 2025-09-23 | benchmark_test | This PR fixes the incorrect Table size and accesses per thread reporting for shared memory tests in the GUPS benchmark, addressing the issues raised by @rkarim2 in 56. Problem Previously, when running shared memory tests, the benchmark incorrectly reported: - Table size showed the global memory work... | other: `posts/gups/gups.cu` | Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code. |
| [#35](https://github.com/NVIDIA-developer-blog/code-samples/pull/35) Fix vector example to work on systems without concurrent managed access | 2020-08-21 | benchmark_test | Prevent an error from occurring with the vector example on systems without concurrent managed access that do not support cuMemPrefetchAsync | wrapper: `posts/cuda-vmm/cuvector.cpp`, `posts/cuda-vmm/cuvector.h` | Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code. |
| [#52](https://github.com/NVIDIA-developer-blog/code-samples/pull/52) Printf-alternative blog files | 2023-05-10 | benchmark_test | Printf-alternative Often times users may be tempted to use `printf` to signal soft warnings; however the compiler may reserve extra registers for `printf` even if the warning rarely occurs. This in turn can affect performance. The `CASerror.h` header-only library implements a performant soft-warning... | wrapper: `posts/printf-alternative/CASerror.h`<br>docs: `posts/printf-alternative/README.md`<br>other: `posts/printf-alternative/CMakeLists.txt`, `posts/printf-alternative/main.cu` | Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code. |

### Other Kernel Cases

Use this section for: Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea.
NCU first look: Choose metrics based on the changed kernel family after opening the diff.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#16](https://github.com/NVIDIA-developer-blog/code-samples/pull/16) Add TensorRT introduction sample simpleOnnx | 2018-11-08 | kernel_other | Add TensorRT introduction sample simpleOnnx | wrapper: `posts/TensorRT-introduction/cudaWrapper.h`, `posts/TensorRT-introduction/ioHelper.cpp`, `posts/TensorRT-introduction/ioHelper.h`, `posts/TensorRT-introduction/simpleOnnx.cpp`<br>other: `posts/TensorRT-introduction/Makefile` | Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea. |
| [#26](https://github.com/NVIDIA-developer-blog/code-samples/pull/26) Add cuda-vmm examples | 2020-04-02 | kernel_other | This is to be referenced by a pending blog post. | wrapper: `posts/cuda-vmm/cuvector.cpp`, `posts/cuda-vmm/cuvector.h`, `posts/cuda-vmm/vector_main.cpp`<br>other: `posts/cuda-vmm/Makefile`, `posts/cuda-vmm/sync_main.cu` | Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea. |
| [#3](https://github.com/NVIDIA-developer-blog/code-samples/pull/3) double fix coalescing.cu | 2014-09-15 | kernel_other | Here: https://github.com/parallel-forall/code-samples/blob/master/series/cuda-cpp/coalescing-global/coalescing.cu lines 54 and 70 are passing a double for the second argument: code block This is not really sensible and may trigger compiler warnings like this: coalescing.cu:70: warning: passing âdoub... | other: `series/cuda-cpp/coalescing-global/coalescing.cu` | Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea. |
| [#15](https://github.com/NVIDIA-developer-blog/code-samples/pull/15) [Patch v3] jacobee: Allow compilation of code with cuda | 2018-09-18 | kernel_other | There is a bug in Makefile when specifying LD flags. Fixing the same in this patch. It also addresses CUDA 9 and Volta compatibility. Further, removing support for SM20 gencode from the makefile. This is because with the current combination there is no CUDA version with which SM20 works. If anyone h... | other: `posts/cuda-aware-mpi-example/src/Makefile` | Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea. |

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
