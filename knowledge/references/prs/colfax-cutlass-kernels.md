# Colfax CUTLASS Kernels PR Knowledge Notes

Repository: <https://github.com/ColfaxResearch/cutlass-kernels>

This page is the production-PR layer for kernel-knowledge. It keeps merged PRs with CUDA/NVIDIA target evidence, real kernel/source changes, and an optimization/performance mechanism such as tuning, fusion, tensor-core paths, memory movement, scheduling, profiling, or benchmark-backed speed work. Release, CI-only, formatting, dependency-only, correctness-only, and non-target-backend PRs are filtered out.

## Repository Source Scan

## Coverage Summary

| Category | CUDA optimization PRs |
| --- | ---: |
| GEMM / Quantization | 2 |
| Architecture / Pipeline | 1 |

## Pull Request Case Notes

### GEMM / Quantization

Use this section for: Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate.
NCU first look: Tensor pipe %, DRAM/L2 bytes, active cycles, register pressure, and scale-load traffic.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#5](https://github.com/ColfaxResearch/cutlass-kernels/pull/5) FMHA Pure FP8 support | 2024-02-20 | gemm_quant, memory_primitives, norm_elementwise, scheduler_autotune | We add support for a 'pure' FP8 version through writing an efficient byte permute/shuffle method to match the register layout of the (FP8 downcasted) accumulator of GEMM-I to the desired register layout for operand A of FP8 GEMM-II. Note that FP8 GEMM-II still necessitates transposing the V matrix (... | kernel: `include/utils/fmha_cutlass.hpp`, `lib/gemm/copy_tensor.hpp`, `src/fmha-pipeline/fmha_consumer.h`, `src/fmha-pipeline/fmha_epilogue.h`<br>wrapper: `include/utils/cuda_launch.hpp`, `include/utils/random.hpp`<br>docs: `src/fmha-pipeline/README.md`<br>other: `src/fmha-pipeline/compile_H128.sh`, `src/fmha-pipeline/compile_H64.sh`, `src/fmha-pipeline/compile_run_all_config.sh` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |
| [#4](https://github.com/ColfaxResearch/cutlass-kernels/pull/4) FMHA Pipelined + WS + FP8 kernels | 2024-02-12 | gemm_quant, attention_kv, scheduler_autotune, arch_pipeline | Added pipelined + WS version of FMHA kernel to /src/fmha-pipeline. This supports both FP16 and FP8. | kernel: `include/utils/fmha_cutlass.hpp`, `lib/gemm/gemm_tensor.hpp`, `src/fmha-pipeline/fmha_consumer.h`, `src/fmha-pipeline/fmha_driver.h`<br>wrapper: `include/utils/cuda_launch.hpp`, `include/utils/random.hpp`<br>docs: `src/fmha-pipeline/README.md`<br>other: `src/fmha-pipeline/compile.sh`, `src/fmha-pipeline/compile_run_all_config.sh` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |

### Architecture / Pipeline

Use this section for: Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages.
NCU first look: Tensor pipe %, memory pipe utilization, barrier stalls, wait groups, and occupancy.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#3](https://github.com/ColfaxResearch/cutlass-kernels/pull/3) Streamlined barrier logic and use TMA store | 2024-02-07 | arch_pipeline, memory_primitives, gemm_quant, scheduler_autotune | We add some minor refinements to the fmha kernel, most notably writing out the result matrix using TMA store (in particular, thereby ensuring coalesced stores to global memory) and moving around some of the barrier logic (such as barrier initialize, which was being redundantly called with each copy... | kernel: `lib/gemm/copy_tensor.hpp`, `lib/gemm/gemm_tensor.hpp`, `src/fmha/fmha_forward.cu`<br>other: `src/fmha/compile.sh`, `src/fmha/compile_run_all_config.sh` | Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages. |

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
