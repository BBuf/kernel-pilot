# CUDA Samples PR Knowledge Notes

Repository: <https://github.com/NVIDIA/cuda-samples>

This page is the production-PR layer for kernel-knowledge. It favors merged PRs that changed kernels, dispatch, JIT/runtime integration, tuning policy, tests, benchmarks, or profiling evidence. Release, CI-only, formatting, pure version-bump, and non-target-backend PRs are filtered out.

## Repository Source Scan

## Coverage Summary

| Category | CUDA-kernel PRs |
| --- | ---: |
| Memory / Primitives | 5 |
| Architecture / Pipeline | 1 |
| Compiler / Runtime | 1 |
| Other Kernel Cases | 8 |

## Pull Request Case Notes

### Memory / Primitives

Use this section for: Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract.
NCU first look: DRAM throughput, L2 hit rate, memory sectors, shared-memory conflicts, and synchronization overhead.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#432](https://github.com/NVIDIA/cuda-samples/pull/432) CUDA 13.2 samples update | 2026-05-13 | memory_primitives, compiler_runtime, scheduler_autotune | - Added Python samples for CUDA Python 1.0 release - Renamed top-level `Samples` directory to `cpp` to accommodate Python samples. | wrapper: `Common/helper_string.h`<br>docs: `CHANGELOG.md`, `README.md`<br>other: `.pre-commit-config.yaml`, `CMakeLists.txt`, `Common/helper_nvJPEG.hxx`, `Samples/0_Introduction/UnifiedMemoryStreams/.vscode/launch.json` | Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract. |
| [#363](https://github.com/NVIDIA/cuda-samples/pull/363) fix bug in 6_Performance/transpose: copy sharedmem kernel | 2025-05-05 | memory_primitives, benchmark_test | I believe there is a bug in the copy sharedmem kernel that was hidden by the fact that in the host calling loop, the device output data was not reset before each loop iteration | other: `Samples/6_Performance/transpose/transpose.cu` | Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract. |
| [#332](https://github.com/NVIDIA/cuda-samples/pull/332) Fixing issue 175: changing TILE_DIM to 32 to fix bank conflicts | 2025-02-20 | memory_primitives, benchmark_test | Resolves 175 | other: `Samples/6_Performance/transpose/transpose.cu` | Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract. |
| [#368](https://github.com/NVIDIA/cuda-samples/pull/368) Update the vulkan headers include sequence and the transpose code format check | 2025-05-21 | memory_primitives, benchmark_test | Update the vulkan headers include sequence and the transpose code format check | wrapper: `Samples/5_Domain_Specific/simpleVulkan/VulkanBaseApp.h`, `Samples/5_Domain_Specific/simpleVulkanMMAP/VulkanBaseApp.h`<br>other: `Samples/5_Domain_Specific/vulkanImageCUDA/vulkanImageCUDA.cu`, `Samples/6_Performance/transpose/transpose.cu` | Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract. |
| [#330](https://github.com/NVIDIA/cuda-samples/pull/330) Remove unnecessary inheritance from `thrust::unary_function` | 2025-02-20 | memory_primitives | fixes https://github.com/NVIDIA/cuda-samples/issues/328 The need to inherit from `thrust::unary_function` was a hold-over from the pre-C++11 days. Nowadays, this isn't needed anymore and can just be removed. | kernel: `Samples/2_Concepts_and_Techniques/segmentationTreeThrust/kernels.cuh` | Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract. |

### Architecture / Pipeline

Use this section for: Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages.
NCU first look: Tensor pipe %, memory pipe utilization, barrier stalls, wait groups, and occupancy.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#327](https://github.com/NVIDIA/cuda-samples/pull/327) Fix compute performance calculation type casting in gpuGetMaxGflopsDe… | 2025-02-19 | arch_pipeline, benchmark_test | Fix `helper_cuda_drvapi.h` performance calculation in gpuGetMaxGflopsDeviceIdDRV() for 109 | wrapper: `Common/helper_cuda_drvapi.h` | Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages. |

### Compiler / Runtime

Use this section for: Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests.
NCU first look: Generated kernel shape, launch overhead, occupancy, register pressure, and compile-time-selected schedule.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#379](https://github.com/NVIDIA/cuda-samples/pull/379) Fix null pointer reference issue with cuda driver API function pointer… | 2025-09-05 | compiler_runtime | We see app crash when CuInit returns failure before initializing all the function pointers. Error path should not crash. PR for failsafe error path. | wrapper: `Samples/0_Introduction/matrixMulDynlinkJIT/helper_cuda_drvapi.h`<br>other: `Samples/0_Introduction/matrixMulDynlinkJIT/cuda_drvapi_dynlink.c` | Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests. |

### Other Kernel Cases

Use this section for: Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea.
NCU first look: Choose metrics based on the changed kernel family after opening the diff.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#320](https://github.com/NVIDIA/cuda-samples/pull/320) Update CUDA Samples for CTK 12.8 release and migrate build system to CMake | 2025-02-15 | kernel_other | This PR updates the samples repository for the CUDA Toolkit 12.8 release. We also update the build system to CMake to simplify builds across multiple architectures and targets. Please refer to the README documentation for updated build instructions. | wrapper: `Common/dynlink_d3d10.h`, `Common/helper_cuda.h`, `Common/helper_cuda_drvapi.h`, `Common/rendercheck_d3d10.cpp`<br>docs: `CHANGELOG.md`, `README.md`, `Samples/0_Introduction/README.md`, `Samples/0_Introduction/UnifiedMemoryStreams/README.md`<br>other: `.gitignore`, `CMakeLists.txt`, `Makefile`, `Samples/0_Introduction/CMakeLists.txt` | Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea. |
| [#182](https://github.com/NVIDIA/cuda-samples/pull/182) Fix cudaExtent.width set error. | 2023-03-28 | kernel_other | unit: 4_CUDA_Libraries/cudaNvSciNvMedia/cuda_consumer.cu Because of the change of padding size in NvSciBuf, the cudaExtent.width and cudaExtent.height should be change NvOnline Bug 3880762 | other: `Samples/4_CUDA_Libraries/cudaNvSciNvMedia/cuda_consumer.cu` | Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea. |
| [#344](https://github.com/NVIDIA/cuda-samples/pull/344) graphConditionalNodes: Add switch, while, if/else conditional examples and minor cleanup | 2025-03-04 | kernel_other | graphConditionalNodes: Add switch, while, if/else conditional examples and minor cleanup | other: `Samples/3_CUDA_Features/graphConditionalNodes/graphConditionalNodes.cu` | Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea. |
| [#331](https://github.com/NVIDIA/cuda-samples/pull/331) Enhancement for GLFW include and lib search | 2025-02-20 | kernel_other | Enhancement for GLFW include and lib search | docs: `README.md`<br>other: `Samples/5_Domain_Specific/simpleVulkan/CMakeLists.txt`, `Samples/5_Domain_Specific/simpleVulkanMMAP/CMakeLists.txt`, `Samples/5_Domain_Specific/smokeParticles/CMakeLists.txt`, `Samples/5_Domain_Specific/vulkanImageCUDA/CMakeLists.txt` | Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea. |
| [#329](https://github.com/NVIDIA/cuda-samples/pull/329) memMapIpc: Resolve build-time warnings and minor potential issues | 2025-02-19 | kernel_other | memMapIpc: Resolve build-time warnings and minor potential issues | wrapper: `Common/helper_cuda_drvapi.h`, `Samples/3_CUDA_Features/memMapIPCDrv/memMapIpc.cpp` | Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea. |
| [#334](https://github.com/NVIDIA/cuda-samples/pull/334) Fixing issue #321: A potential bug in memMapIPCDrv/memMapIpc.cpp | 2025-02-21 | kernel_other | Fixing issue 321: A potential bug in memMapIPCDrv/memMapIpc.cpp | wrapper: `Samples/3_CUDA_Features/memMapIPCDrv/memMapIpc.cpp` | Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea. |
| [#346](https://github.com/NVIDIA/cuda-samples/pull/346) graphConditionalNodes: Change launch dimension initialization for better cross-platform compatibility | 2025-03-05 | kernel_other | graphConditionalNodes: Change launch dimension initialization for better cross-platform compatibility | other: `Samples/3_CUDA_Features/graphConditionalNodes/graphConditionalNodes.cu` | Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea. |
| [#348](https://github.com/NVIDIA/cuda-samples/pull/348) graphConditionalNodes: Additional tweaks to launch dimension initialization | 2025-03-06 | kernel_other | graphConditionalNodes: Additional tweaks to launch dimension initialization | other: `Samples/3_CUDA_Features/graphConditionalNodes/graphConditionalNodes.cu` | Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea. |

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
