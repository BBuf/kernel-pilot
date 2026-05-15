# QuACK PR Knowledge Notes

Repository: <https://github.com/Dao-AILab/quack>

This page is the production-PR layer for kernel-knowledge. It keeps merged PRs with CUDA/NVIDIA target evidence, real kernel/source changes, and an optimization/performance mechanism such as tuning, fusion, tensor-core paths, memory movement, scheduling, profiling, or benchmark-backed speed work. Release, CI-only, formatting, dependency-only, correctness-only, and non-target-backend PRs are filtered out.

## Repository Source Scan

Read these source regions before opening individual PR diffs:

- `quack`
- `benchmarks`
- `microbenchmarks`
- `examples`
- `tests`
- `docs`

## Coverage Summary

| Category | CUDA optimization PRs |
| --- | ---: |
| GEMM / Quantization | 2 |
| Norm / Elementwise / Epilogue | 1 |
| Memory / Primitives | 1 |
| Scheduler / Autotune | 2 |
| Architecture / Pipeline | 2 |
| Benchmark / Test Evidence | 1 |

## Pull Request Case Notes

### GEMM / Quantization

Use this section for: Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate.
NCU first look: Tensor pipe %, DRAM/L2 bytes, active cycles, register pressure, and scale-load traffic.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#82](https://github.com/Dao-AILab/quack/pull/82) Add stochastic rounding support for GEMM epilogue | 2026-03-16 | gemm_quant, arch_pipeline, norm_elementwise, benchmark_test, memory_primitives | Implements a generic rounding mode mechanism for Quack GEMM epilogues that configures how the accumulator (FP32) is downconverted to the output dtype (e.g., BF16) before storing to gmem. Stochastic rounding (RS) uses the hardware `cvt.rs.satfinite.bf16x2.f32` PTX instruction and is only supported on... | kernel: `quack/copy_utils.py`, `quack/gemm.py`, `quack/gemm_act.py`, `quack/gemm_dact.py`<br>test: `tests/test_linear.py`<br>wrapper: `quack/__init__.py`, `quack/rounding.py`, `quack/utils.py` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |
| [#28](https://github.com/Dao-AILab/quack/pull/28) Speedup Torch Wrapper for Symm Matmul | 2025-08-11 | gemm_quant, arch_pipeline | Previously: 1) We extraneously cast to cpu explicitly and then back to gpu via `convert_cute_tensor`: https://github.com/NVIDIA/cutlass/blob/19772cd63ecccc07a5cf5da852b15cd3ccecf63b/python/CuTeDSL/cutlass/torch.pyL143. 2) We didn't cache code block which is fairly expensive. | kernel: `quack/symmetric_dense_gemm_sm90.py` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |

### Norm / Elementwise / Epilogue

Use this section for: Look for fusion, vectorization, dtype conversion, and store-traffic reductions before changing math.
NCU first look: DRAM %, L2 bytes, global load/store sectors, eligible warps, and long scoreboard.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#132](https://github.com/Dao-AILab/quack/pull/132) RMS Norm Bwd: Optimize for GB200 w/ TMA loads, reload_x, separate output dtype, new launch configs | 2026-05-14 | norm_elementwise, arch_pipeline, scheduler_autotune, memory_primitives | Various optimizations and enhancements to RMSNormBwd kernel for GB200 Kernel additions - TMA 1D or 2D loads for X / dY load path depending on the CTA tilers. Helps reduce register pressure for larger reduction dims without having to bump up the cluster shapes. - Refactored persistent-loop loads: ref... | kernel: `quack/rmsnorm.py`, `quack/rmsnorm_config.py` | Look for fusion, vectorization, dtype conversion, and store-traffic reductions before changing math. |

### Memory / Primitives

Use this section for: Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract.
NCU first look: DRAM throughput, L2 hit rate, memory sectors, shared-memory conflicts, and synchronization overhead.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#74](https://github.com/Dao-AILab/quack/pull/74) Fix gather fusion in SM100 | 2026-02-11 | memory_primitives, arch_pipeline, gemm_quant | This can pass all unit tests on B300 GPUs. | kernel: `quack/gemm_interface.py` | Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract. |

### Scheduler / Autotune

Use this section for: Treat scheduler/autotune configs as shape-specific evidence; replay benchmark shapes before generalizing.
NCU first look: SM occupancy, waves/SM, active cycles, tail effects, and load imbalance.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#79](https://github.com/Dao-AILab/quack/pull/79) Fix Triangular Scheduler | 2026-03-09 | scheduler_autotune, benchmark_test, gemm_quant | 1) `cute.FastDivmodDivisor`'s __rdivmod__ returns IntValue (https://github.com/NVIDIA/cutlass/blob/main/python/CuTeDSL/cutlass/cute/core.pyL4588), so math like ` (utils.sqrt(2 * cluster_id_in_problem + 2.25) - 0.5) * params.group_size_inv_f32` breaks. I cast cluster_id_in_problem to In532 2) Fixed n... | kernel: `quack/tile_scheduler.py`<br>test: `tests/test_gemm_symmetric.py`, `tests/test_symmetric_gemm.py` | Treat scheduler/autotune configs as shape-specific evidence; replay benchmark shapes before generalizing. |
| [#85](https://github.com/Dao-AILab/quack/pull/85) Avoid CUDA context initialization at import time | 2026-03-18 | scheduler_autotune, gemm_quant, arch_pipeline | Previously, `import quack.gemm_interface` called `get_device_capacity(torch.device("cuda"))` at module level to determine which autotuning configs to generate. This eagerly initialized a CUDA context. In our use case, sometimes we do it in a CPU only environment. Fix: generate configs for all suppor... | kernel: `quack/gemm_config.py`, `quack/gemm_interface.py` | Treat scheduler/autotune configs as shape-specific evidence; replay benchmark shapes before generalizing. |

### Architecture / Pipeline

Use this section for: Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages.
NCU first look: Tensor pipe %, memory pipe utilization, barrier stalls, wait groups, and occupancy.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#94](https://github.com/Dao-AILab/quack/pull/94) [Gemm] fix sm120 gemm kernel invocation error | 2026-04-02 | arch_pipeline, benchmark_test, gemm_quant | Currently the `GemmSm120` does not work and will throw the following error: code block This is because its parent class `GemmSm90` calls the `kernel` with the following parameters: https://github.com/Dao-AILab/quack/blob/a24e4aa1861ccce0419ba41e3cbe9433e192b5ac/quack/gemm_sm90.pyL526-L547 But `GemmS... | kernel: `quack/gemm_sm120.py`<br>benchmark: `benchmarks/benchmark_gemm.py` | Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages. |
| [#99](https://github.com/Dao-AILab/quack/pull/99) add _get_mma_inst_tile_k() virtual method to GemmSm100 | 2026-04-14 | arch_pipeline, gemm_quant, moe_routing | Problem: Subclassing GemmSm100 for specialized GEMM variants (e.g., MoE grouped GEMM) requires overriding the MMA K-tile depth. Currently mma_inst_tile_k = 4 is hardcoded inside _setup_attributes, which feeds into downstream SMEM layout, pipeline stage, and cluster shape calculations. In the MoE ker... | kernel: `quack/gemm_sm100.py` | Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages. |

### Benchmark / Test Evidence

Use this section for: Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code.
NCU first look: Use the PR's benchmark/profile command as the first replay target.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#95](https://github.com/Dao-AILab/quack/pull/95) [Gemm] Fix `gemm_symmetric` on SM120 + add benchmark | 2026-04-03 | benchmark_test, gemm_quant, arch_pipeline | This PR is a follow-up of 94. - Fix `gemm_symmetric` kernel hang and incorrect triangular scheduling on SM120 (RTX 5090) - Add `benchmarks/benchmark_gemm_symmetric.py` comparing against cuBLAS Problem `gemm_symmetric` was broken on SM120 with two compounding bugs: 1. **Kernel deadlock with `cluster_... | kernel: `quack/gemm_interface.py`<br>benchmark: `benchmarks/benchmark_gemm_symmetric.py` | Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code. |

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
