# Colfax Article Source PR Knowledge Notes

Repository: <https://github.com/ColfaxResearch/cfx-article-src>

This page is the production-PR layer for kernel-knowledge. It favors merged PRs that changed kernels, dispatch, JIT/runtime integration, tuning policy, tests, benchmarks, or profiling evidence. Release, CI-only, formatting, pure version-bump, and non-target-backend PRs are filtered out.

## Repository Source Scan

## Coverage Summary

| Category | CUDA-kernel PRs |
| --- | ---: |
| GEMM / Quantization | 1 |
| Scheduler / Autotune | 1 |
| Architecture / Pipeline | 2 |

## Pull Request Case Notes

### GEMM / Quantization

Use this section for: Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate.
NCU first look: Tensor pipe %, DRAM/L2 bytes, active cycles, register pressure, and scale-load traffic.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#8](https://github.com/ColfaxResearch/cfx-article-src/pull/8) Add code sample, makefile, and documentation on node types | 2024-10-25 | gemm_quant, compiler_runtime | Add code sample, makefile, and documentation on node types | kernel: `evt/evt_gemm_cute.cu`<br>wrapper: `evt/reference.h`<br>docs: `evt/node_types.md`<br>other: `evt/Makefile` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |

### Scheduler / Autotune

Use this section for: Treat scheduler/autotune configs as shape-specific evidence; replay benchmark shapes before generalizing.
NCU first look: SM occupancy, waves/SM, active cycles, tail effects, and load imbalance.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#9](https://github.com/ColfaxResearch/cfx-article-src/pull/9) Add code for Stream-K post | 2024-12-20 | scheduler_autotune, arch_pipeline, benchmark_test, gemm_quant, norm_elementwise | Add code for Stream-K post | kernel: `streamk/hopper_gemm_kernel.h`, `streamk/hopper_gemm_kernel_launch.h`, `streamk/kernel_traits.h`, `streamk/tile_scheduler.hpp`<br>benchmark: `streamk/cutlass_streamk/benchmark.cu`, `streamk/cutlass_streamk/profile.sh`<br>wrapper: `streamk/cli_options.h`, `streamk/convert_util.h`, `streamk/epilogue_sm90_tma_ws.hpp`, `streamk/mainloop_sm90_tma_gmma_ws.hpp`<br>docs: `streamk/README.md`<br>other: `streamk/Makefile`, `streamk/cutlass_streamk/Makefile`, `streamk/streamk.cu` | Treat scheduler/autotune configs as shape-specific evidence; replay benchmark shapes before generalizing. |

### Architecture / Pipeline

Use this section for: Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages.
NCU first look: Tensor pipe %, memory pipe utilization, barrier stalls, wait groups, and occupancy.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#7](https://github.com/ColfaxResearch/cfx-article-src/pull/7) Pipeline gemm example code | 2024-09-22 | arch_pipeline, gemm_quant, norm_elementwise, scheduler_autotune | Pipeline gemm example code | kernel: `pipeline-gemm/hopper-gemm-ws/convert_util.h`, `pipeline-gemm/hopper-gemm-ws/epilogue_sm90_tma_ws.hpp`, `pipeline-gemm/hopper-gemm-ws/hopper_gemm_kernel.h`, `pipeline-gemm/hopper-gemm-ws/hopper_gemm_kernel_launch.h`<br>docs: `pipeline-gemm/README.md`<br>other: `external/cutlass`, `pipeline-gemm/Makefile` | Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages. |
| [#1](https://github.com/ColfaxResearch/cfx-article-src/pull/1) Tma | 2024-06-24 | arch_pipeline, memory_primitives | Add TMA tutorial examples. | kernel: `tma/scale_tma_kernel.h`<br>wrapper: `tma/shared_storage.h`, `tma/smem_helper.hpp`, `tma/tma_copy.h`, `tma/tma_copy_multicast.h`<br>docs: `tma/README.md`<br>other: `tma/Makefile`, `tma/main.cu` | Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages. |

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
