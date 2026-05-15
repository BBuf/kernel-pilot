# cuDNN Frontend PR Knowledge Notes

Repository: <https://github.com/NVIDIA/cudnn-frontend>

This page is the production-PR layer for kernel-knowledge. It favors merged PRs that changed kernels, dispatch, JIT/runtime integration, tuning policy, tests, benchmarks, or profiling evidence. Release, CI-only, formatting, pure version-bump, and non-target-backend PRs are filtered out.

## Repository Source Scan

## Coverage Summary

| Category | CUDA-kernel PRs |
| --- | ---: |
| GEMM / Quantization | 5 |
| Attention / KV / Decode | 2 |
| Norm / Elementwise / Epilogue | 2 |
| Compiler / Runtime | 2 |
| Benchmark / Test Evidence | 1 |
| Other Kernel Cases | 2 |

## Pull Request Case Notes

### GEMM / Quantization

Use this section for: Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate.
NCU first look: Tensor pipe %, DRAM/L2 bytes, active cycles, register pressure, and scale-load traffic.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#179](https://github.com/NVIDIA/cudnn-frontend/pull/179) cuDNN Frontend v1.16.0 | 2025-11-07 | gemm_quant, benchmark_test, attention_kv, moe_routing, scheduler_autotune | cuDNN Frontend v1.16.0 is the recommended version for cuDNN 9.15.0 and later releases. This release introduces open-source implementations of commonly requested fused kernels for select architectures (Blackwell). These experimental kernels may require additional dependencies such as CuteDSL. The ini... | kernel: `include/cudnn_frontend/node/moe_grouped_matmul.h`, `include/cudnn_frontend/node/scaled_dot_product_flash_attention.h`, `python/cudnn/gemm_amax/__init__.py`, `python/cudnn/gemm_amax/api.py`<br>benchmark: `benchmark/sdpa_benchmark/benchmark_flash_attention.py`, `benchmark/sdpa_benchmark_training/README.md`, `benchmark/sdpa_benchmark_training/benchmark_single_sdpa.py`<br>wrapper: `include/cudnn_frontend/cudnn_interface.h`, `include/cudnn_frontend/graph_interface.h`, `include/cudnn_frontend/graph_properties.h`, `include/cudnn_frontend/node/sdpa_support_surface.h`<br>docs: `python/cudnn/README.md`<br>other: `CMakeLists.txt`, `dlpack_version.txt`, `pyproject.toml` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |
| [#126](https://github.com/NVIDIA/cudnn-frontend/pull/126) cudnn frontend v1.10 | 2025-01-28 | gemm_quant, attention_kv, norm_elementwise, benchmark_test | cudnn frontend v1.10 release notes cudnn frontend v1.10 is the preferred cudnn frontend to be used for cudnn backend 9.7.0 and later as it adds to the Blackwell specific features. New API - cudnn Frontend v1.10 introduces two new operators, block_scale_quantize and block_scale_dequantize to specify... | kernel: `include/cudnn_frontend/node/batchnorm.h`, `include/cudnn_frontend/node/batchnorm_inference.h`, `include/cudnn_frontend/node/block_scale_dequantize.h`, `include/cudnn_frontend/node/block_scale_quantize.h`<br>benchmark: `benchmark/Dockerfile`, `benchmark/benchmark_flash_attention.py`<br>wrapper: `include/cudnn_frontend/backend/backend_descriptor.h`, `include/cudnn_frontend/backend/plan_helpers.h`, `include/cudnn_frontend/context.h`, `include/cudnn_frontend/graph_interface.h`<br>docs: `README.FE.1.0.md`, `docs/cuda-graphs.md`, `docs/custom-execution-plan.md`, `docs/dynamic-kernel-cache.md`<br>other: `CMakeLists.txt` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |
| [#150](https://github.com/NVIDIA/cudnn-frontend/pull/150) cudnn frontend v1.13.0 | 2025-07-17 | gemm_quant, benchmark_test, attention_kv, arch_pipeline | cudnn frontend v1.13 release notes cudnn frontend v1.13 is the preferred cudnn frontend version for cudnn version 9.11.0 and above. New API Introduces device descriptor, which allows for device-less compilation of cudnn graph on a target GPU. See newly added sample and documentation. Improvements SD... | kernel: `include/cudnn_frontend/node/block_scale_dequantize.h`, `include/cudnn_frontend/node/scaled_dot_product_flash_attention.h`<br>benchmark: `benchmark/Llama-3.2-1B-Training/training_perf.py`, `benchmark/sdpa_benchmark/benchmark_flash_attention.py`, `benchmark/sdpa_benchmark_bf16_training/artifacts/sdpa_benchmark_results_NVIDIA_B200.csv`, `benchmark/sdpa_benchmark_bf16_training/artifacts/sdpa_benchmark_results_NVIDIA_B200.png`<br>wrapper: `include/cudnn_frontend.h`, `include/cudnn_frontend/backend/device_properties.h`, `include/cudnn_frontend/backend/plan_helpers.h`, `include/cudnn_frontend/cudnn_interface.h`<br>other: `CMakeLists.txt` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |
| [#174](https://github.com/NVIDIA/cudnn-frontend/pull/174) cudnn frontend v1.15.0 | 2025-10-10 | gemm_quant, benchmark_test, norm_elementwise, arch_pipeline | cudnn frontend v1.15 release notes cudnn frontend v1.15 is the preferred cudnn frontend version for cuDNN version 9.13.1 and above. New API - Introduced a new `cudnn.Graph` API that enables interoperability between `torch.tensors` and the cudnn frontend API. Sample code for performing a matmul with... | kernel: `include/cudnn_frontend/node/adaptive_layernorm.h`, `include/cudnn_frontend/node/batchnorm.h`, `include/cudnn_frontend/node/batchnorm_inference.h`, `include/cudnn_frontend/node/block_scale_dequantize.h`<br>benchmark: `benchmark/sdpa_benchmark_training/Dockerfile`, `benchmark/sdpa_benchmark_training/README.md`, `benchmark/sdpa_benchmark_training/artifacts/sample_b200_bf16_run.txt`, `benchmark/sdpa_benchmark_training/artifacts/sample_b200_fp8_run.txt`<br>wrapper: `include/cudnn_frontend/cudnn_interface.h`, `include/cudnn_frontend/graph_interface.h`, `include/cudnn_frontend/graph_properties.h`, `include/cudnn_frontend/node/bn_finalize.h`<br>other: `CMakeLists.txt` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |
| [#125](https://github.com/NVIDIA/cudnn-frontend/pull/125) cmake: install config with headers | 2025-05-22 | gemm_quant, attention_kv, norm_elementwise, scheduler_autotune | This PR contains a number of changes I made while packaging this repo for use with Nixpkgs. | kernel: `samples/cpp/norm/batchnorm.cpp`, `samples/cpp/norm/layernorm.cpp`, `samples/cpp/norm/rmsnorm.cpp`<br>wrapper: `samples/cpp/convolution/dgrads.cpp`, `samples/cpp/convolution/fp8_fprop.cpp`, `samples/cpp/convolution/fprop.cpp`, `samples/cpp/convolution/int8_fprop.cpp`<br>other: `CMakeLists.txt`, `cudnn_frontend-config.cmake.in`, `python/CMakeLists.txt`, `samples/cpp/CMakeLists.txt` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |

### Attention / KV / Decode

Use this section for: Preserve page/KV/layout and plan-run contracts; profile memory traffic separately from math utilization.
NCU first look: Long scoreboard, L2/DRAM traffic, global-load sectors, tensor pipe %, and shared-memory bank conflicts.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#194](https://github.com/NVIDIA/cudnn-frontend/pull/194) cudnn FE 1.17.0 | 2025-12-20 | attention_kv, arch_pipeline, benchmark_test, gemm_quant | cuDNN Frontend v1.17.0 Release Notes cuDNN Frontend v1.17.0 is the recommended version for cuDNN 9.17.0 and later releases. New Features 🚀 Open-Source Kernels - **Native Sparse Attention** : The Native Sparse Attention (NSA) module implements Native Sparse attention as described in the Native Sparse... | kernel: `include/cudnn_frontend/node/scaled_dot_product_flash_attention.h`<br>benchmark: `benchmark/sdpa_benchmark_training/Dockerfile`, `benchmark/sdpa_benchmark_training/README.md`, `benchmark/sdpa_benchmark_training/artifacts/sample_gb200_bf16_run.txt`, `benchmark/sdpa_benchmark_training/artifacts/sample_gb200_fp8_run.txt`<br>wrapper: `include/cudnn_frontend/cudnn_interface.h`, `include/cudnn_frontend/graph_helpers.h`, `include/cudnn_frontend/graph_interface.h`, `include/cudnn_frontend/graph_properties.h`<br>docs: `README.md`<br>other: `CMakeLists.txt` | Preserve page/KV/layout and plan-run contracts; profile memory traffic separately from math utilization. |
| [#240](https://github.com/NVIDIA/cudnn-frontend/pull/240) Add acknowledgements section to sparse_attention.md | 2026-05-08 | attention_kv | Added acknowledgements for the Native Sparse Attention fprop kernels implementation. | docs: `python/cudnn/native_sparse_attention/sparse_attention.md` | Preserve page/KV/layout and plan-run contracts; profile memory traffic separately from math utilization. |

### Norm / Elementwise / Epilogue

Use this section for: Look for fusion, vectorization, dtype conversion, and store-traffic reductions before changing math.
NCU first look: DRAM %, L2 bytes, global load/store sectors, eligible warps, and long scoreboard.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#216](https://github.com/NVIDIA/cudnn-frontend/pull/216) License update and fix broken link | 2026-04-06 | norm_elementwise, gemm_quant, moe_routing, scheduler_autotune, arch_pipeline | - Update License to MIT - Fix broken links in documentation | kernel: `include/cudnn_frontend/generated/rms_norm_silu/sm100/ln_fwd_silu_kernel.h`, `include/cudnn_frontend/generated/rms_norm_silu/sm100/ln_headers.h`, `include/cudnn_frontend/generated/sdpa/sm100/prefill/full_seqlens/d128_fprop_kernel.h`, `include/cudnn_frontend/generated/sdpa/sm100/prefill/full_seqlens/d64_fprop_kernel.h`<br>wrapper: `python/cudnn/api_base.py`<br>docs: `README.md` | Look for fusion, vectorization, dtype conversion, and store-traffic reductions before changing math. |
| [#92](https://github.com/NVIDIA/cudnn-frontend/pull/92) cudnn FE 1.6.0  | 2024-08-12 | norm_elementwise, gemm_quant, attention_kv | cudnn FE 1.6.0 Release notes: New API - Graph Slice Operation: Introduced the `graph.slice` operation for slicing input tensors. Refer to docs/operations/Slice.md for detailed documentation and` samples/cpp/misc/slice.cpp` for a C++ sample. Pybinds for this operation have also been added. - SM Carve... | kernel: `include/cudnn_frontend/node/batchnorm.h`, `include/cudnn_frontend/node/batchnorm_inference.h`, `include/cudnn_frontend/node/instancenorm.h`, `include/cudnn_frontend/node/layernorm.h`<br>wrapper: `include/cudnn_frontend.h`, `include/cudnn_frontend/context.h`, `include/cudnn_frontend/cudnn_interface.h`, `include/cudnn_frontend/graph_helpers.h`<br>docs: `README.FE.1.0.md`, `docs/operations/Slice.md`<br>other: `CMakeLists.txt` | Look for fusion, vectorization, dtype conversion, and store-traffic reductions before changing math. |

### Compiler / Runtime

Use this section for: Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests.
NCU first look: Generated kernel shape, launch overhead, occupancy, register pressure, and compile-time-selected schedule.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#5](https://github.com/NVIDIA/cudnn-frontend/pull/5) MR for quick fix for graceful exit | 2021-06-08 | compiler_runtime | - Adding status check on the cudnnBackendExecute during warm up. - Adding status check on json_handle when loading from a file | wrapper: `include/cudnn_frontend_Errata.h`, `include/cudnn_frontend_find_plan.h` | Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests. |
| [#183](https://github.com/NVIDIA/cudnn-frontend/pull/183) Fix issues in warmup function. | 2025-12-01 | compiler_runtime | - Make sure doing a cuda graph capture is not allowed when one is already in progress - Teardown the cuda graph to prevent future errors when execute fails | wrapper: `include/cudnn_frontend/graph_interface.h` | Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests. |

### Benchmark / Test Evidence

Use this section for: Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code.
NCU first look: Use the PR's benchmark/profile command as the first replay target.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#142](https://github.com/NVIDIA/cudnn-frontend/pull/142) cudnn benchmark and code cleanup | 2025-05-22 | benchmark_test, attention_kv | - Introduce new benchmark results for cuDNN on H200 and B200. Please refer to benchmark folder for more details. - Address code review comments on 1.12.0 release candidate. | kernel: `include/cudnn_frontend/backend/kernel_cache.h`, `python/pygraph/norm.cpp`<br>benchmark: `benchmark/Llama-3.2-1B-Training/Dockerfile`, `benchmark/Llama-3.2-1B-Training/README.md`, `benchmark/Llama-3.2-1B-Training/artifacts/b200_h200_speedup.png`, `benchmark/Llama-3.2-1B-Training/artifacts/b200_iteration_time.png`<br>wrapper: `include/cudnn_frontend/graph_interface.h`, `include/cudnn_frontend/graph_properties.h`, `python/properties.cpp`, `samples/cpp/misc/pointwise.cpp`<br>docs: `README.md`<br>other: `requirements.txt` | Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code. |

### Other Kernel Cases

Use this section for: Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea.
NCU first look: Choose metrics based on the changed kernel family after opening the diff.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#185](https://github.com/NVIDIA/cudnn-frontend/pull/185) Fix/cuda graph warmup | 2025-12-01 | kernel_other | Fix/cuda graph warmup | wrapper: `include/cudnn_frontend/graph_interface.h` | Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea. |
| [#208](https://github.com/NVIDIA/cudnn-frontend/pull/208) Restore the support for cuda 12.9 version | 2026-03-11 | kernel_other | Restore the support for cuda 12.9 version | wrapper: `include/cudnn_frontend_shim.h` | Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea. |

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
