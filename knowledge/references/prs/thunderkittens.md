# ThunderKittens PR Knowledge Notes

Repository: <https://github.com/HazyResearch/ThunderKittens>

This page is the production-PR layer for kernel-knowledge. It keeps merged PRs with CUDA/NVIDIA target evidence, real kernel/source changes, and an optimization/performance mechanism such as tuning, fusion, tensor-core paths, memory movement, scheduling, profiling, or benchmark-backed speed work. Release, CI-only, formatting, dependency-only, correctness-only, and non-target-backend PRs are filtered out.

## Repository Source Scan

Read these source regions before opening individual PR diffs:

- `include/kittens.cuh`
- `examples`

## Coverage Summary

| Category | CUDA optimization PRs |
| --- | ---: |
| GEMM / Quantization | 1 |
| Scheduler / Autotune | 1 |
| Architecture / Pipeline | 3 |
| Benchmark / Test Evidence | 1 |

## Pull Request Case Notes

### GEMM / Quantization

Use this section for: Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate.
NCU first look: Tensor pipe %, DRAM/L2 bytes, active cycles, register pressure, and scale-load traffic.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#84](https://github.com/HazyResearch/ThunderKittens/pull/84) WIP Blackwell fp8 support | 2025-01-28 | gemm_quant, arch_pipeline | WIP Blackwell fp8 support | kernel: `include/ops/warp/memory/tile/tensor_to_register.cuh`, `kernels/matmul/FP8_B200/matmul.cu`<br>other: `include/ops/warp/tensor/mma.cuh`, `kernels/matmul/FP8_B200/Makefile` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |

### Scheduler / Autotune

Use this section for: Treat scheduler/autotune configs as shape-specific evidence; replay benchmark shapes before generalizing.
NCU first look: SM occupancy, waves/SM, active cycles, tail effects, and load imbalance.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#186](https://github.com/HazyResearch/ThunderKittens/pull/186) Use persistent kernel for short sequence lengths (<=4096) in causal MHA | 2026-03-25 | scheduler_autotune, attention_kv, benchmark_test | Use persistent kernel for short sequence lengths (<=4096) in causal MHA | kernel: `kernels/attention/bf16_b300_mha_causal/bf16_b300_mha_causal.cu`<br>test: `kernels/attention/bf16_b300_mha_causal/test.py` | Treat scheduler/autotune configs as shape-specific evidence; replay benchmark shapes before generalizing. |

### Architecture / Pipeline

Use this section for: Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages.
NCU first look: Tensor pipe %, memory pipe utilization, barrier stalls, wait groups, and occupancy.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#1](https://github.com/HazyResearch/ThunderKittens/pull/1) TMA support + TMA/WGMMA integration testing | 2024-03-13 | arch_pipeline, benchmark_test | TMA support + TMA/WGMMA integration testing | kernel: `src/ops/warp/memory/tma.cuh`, `src/ops/warpgroup/wgmma/base/4x1.cuh`, `src/ops/warpgroup/wgmma/base/4x2.cuh`, `src/ops/warpgroup/wgmma/base/4x3.cuh`<br>test: `src/common/pyutils/__pycache__/test_build_utils.cpython-310.pyc`, `tests/Makefile`, `tests/block/dsmem.impl`, `tests/integration/wgmma_tma_tests.impl`<br>other: `src/common/util.cuh`, `src/ops/block/block.cuh`, `src/ops/warp/memory/memory.cuh`, `src/ops/warpgroup/warpgroup.cuh` | Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages. |
| [#29](https://github.com/HazyResearch/ThunderKittens/pull/29) added tma reductions | 2024-05-17 | arch_pipeline, benchmark_test | added tma reductions | kernel: `src/ops/warp/memory/tile/tma.cuh`, `src/ops/warp/memory/vec/tma.cuh`<br>test: `examples/attn/h100/test.py`<br>wrapper: `examples/attn_causal/gentests_causal.py`<br>other: `examples/attn/h100/h100_train.cu`, `examples/attn_causal/h100_train.cu` | Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages. |
| [#152](https://github.com/HazyResearch/ThunderKittens/pull/152) Educational Hopper Matmul level_07 Warp Specialization Fix | 2025-11-04 | arch_pipeline, gemm_quant | The current `level_07` kernel, which is meant to improve perf through work partitioning, regresses compared to `level_06`. `level_06` output: code block `level_07` output: code block The current warp specialization implementation only overlaps the next tile’s TMA load with the current tile’s MMA com... | kernel: `kernels/matmul/educational/level_07.cu` | Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages. |

### Benchmark / Test Evidence

Use this section for: Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code.
NCU first look: Use the PR's benchmark/profile command as the first replay target.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#98](https://github.com/HazyResearch/ThunderKittens/pull/98) Performance Parity for H100_mma_ABt and H100_mma Kernels | 2025-06-16 | benchmark_test, gemm_quant | This 4-line code change achieves performance parity between the transposed (`H100_mma_ABt`) and non-transposed (`H100_mma`) matmul kernels by dispatching the largest available tensor core instruction (`wgmma` of size `64x16x256`). Previously, the transposed kernel was approximately 75-80 TFLOPS slow... | kernel: `kernels/matmul/H100_mma_ABt/matmul.cu` | Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code. |

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
