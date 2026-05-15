# QuACK PR Knowledge Notes

Repository: <https://github.com/Dao-AILab/quack>

This page is the production-PR layer for kernel-knowledge. It favors merged PRs that changed kernels, dispatch, JIT/runtime integration, tuning policy, tests, benchmarks, or profiling evidence. Release, CI-only, formatting, pure version-bump, and non-target-backend PRs are filtered out.

## Repository Source Scan

Read these source regions before opening individual PR diffs:

- `quack`
- `benchmarks`
- `microbenchmarks`
- `examples`
- `tests`
- `docs`

## Coverage Summary

| Category | CUDA-kernel PRs |
| --- | ---: |
| GEMM / Quantization | 2 |
| Norm / Elementwise / Epilogue | 7 |
| Memory / Primitives | 5 |
| Scheduler / Autotune | 4 |
| Architecture / Pipeline | 3 |
| Compiler / Runtime | 4 |
| Benchmark / Test Evidence | 1 |

## Pull Request Case Notes

### GEMM / Quantization

Use this section for: Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate.
NCU first look: Tensor pipe %, DRAM/L2 bytes, active cycles, register pressure, and scale-load traffic.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#82](https://github.com/Dao-AILab/quack/pull/82) Add stochastic rounding support for GEMM epilogue | 2026-03-16 | gemm_quant, arch_pipeline, norm_elementwise, benchmark_test, memory_primitives | Implements a generic rounding mode mechanism for Quack GEMM epilogues that configures how the accumulator (FP32) is downconverted to the output dtype (e.g., BF16) before storing to gmem. Stochastic rounding (RS) uses the hardware `cvt.rs.satfinite.bf16x2.f32` PTX instruction and is only supported on... | kernel: `quack/gemm.py`, `quack/gemm_act.py`, `quack/gemm_dact.py`, `quack/gemm_default_epi.py`<br>test: `tests/test_linear.py`<br>wrapper: `quack/__init__.py`, `quack/copy_utils.py`, `quack/rounding.py`, `quack/utils.py` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |
| [#28](https://github.com/Dao-AILab/quack/pull/28) Speedup Torch Wrapper for Symm Matmul | 2025-08-11 | gemm_quant, arch_pipeline | Previously: 1) We extraneously cast to cpu explicitly and then back to gpu via `convert_cute_tensor`: https://github.com/NVIDIA/cutlass/blob/19772cd63ecccc07a5cf5da852b15cd3ccecf63b/python/CuTeDSL/cutlass/torch.pyL143. 2) We didn't cache code block which is fairly expensive. | kernel: `quack/symmetric_dense_gemm_sm90.py` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |

### Norm / Elementwise / Epilogue

Use this section for: Look for fusion, vectorization, dtype conversion, and store-traffic reductions before changing math.
NCU first look: DRAM %, L2 bytes, global load/store sectors, eligible warps, and long scoreboard.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#118](https://github.com/Dao-AILab/quack/pull/118) Add remaining SM120 / RTX 50 support for GEMM epilogues and RMS paths | 2026-04-25 | norm_elementwise, benchmark_test, gemm_quant, arch_pipeline | Author: Alecco (& Codex) for Ologan Add SM120 support for RTX 50 GPUs across missing GEMM epilogue paths and dependent wrappers. This PR enables and validates: - gemm_dgated - non-gated gemm_act - non-gated gemm_dact - gemm_sq_reduce - gemm_rms - gemm_rms_then_norm_act - non-gated MLP eager and torc... | kernel: `quack/gemm_act.py`, `quack/gemm_dact.py`, `quack/gemm_sq_reduce.py`<br>benchmark: `benchmarks/benchmark_gemm_epilogues.py`, `docs/sm120_ncu_profiling.md`<br>test: `tests/test_linear.py`, `tests/test_linear_varlen_m.py`, `tests/test_mlp.py`<br>wrapper: `quack/epi_ops.py`<br>docs: `README.md`<br>other: `pyproject.toml` | Look for fusion, vectorization, dtype conversion, and store-traffic reductions before changing math. |
| [#132](https://github.com/Dao-AILab/quack/pull/132) RMS Norm Bwd: Optimize for GB200 w/ TMA loads, reload_x, separate output dtype, new launch configs | 2026-05-14 | norm_elementwise, arch_pipeline, scheduler_autotune, memory_primitives | Various optimizations and enhancements to RMSNormBwd kernel for GB200 Kernel additions - TMA 1D or 2D loads for X / dY load path depending on the CTA tilers. Helps reduce register pressure for larger reduction dims without having to bump up the cluster shapes. - Refactored persistent-loop loads: ref... | kernel: `quack/rmsnorm.py`, `quack/rmsnorm_config.py` | Look for fusion, vectorization, dtype conversion, and store-traffic reductions before changing math. |
| [#19](https://github.com/Dao-AILab/quack/pull/19) add PyTorch focused benchmarking for quack rmsnorm | 2025-07-17 | norm_elementwise, benchmark_test | This PR adds two new benchmarking files that compares a - Pytorch nn.RMSNorm b - TorchCompile RMSNorm c - Quack RMSNorm For both forward and backward passes. Uses triton.do_bench with timing based benchmarking rather than num iters. This clears the L2 cache, and in theory provides more accurate resu... | benchmark: `benchmarks/pytorch_benchmark_rmsnorm.py`, `benchmarks/pytorch_benchmark_rmsnorm_backward.py`, `benchmarks/visual_outputs/quack_vs_pytorch_backward_speedup.png`, `benchmarks/visual_outputs/quack_vs_pytorch_speedup.png` | Look for fusion, vectorization, dtype conversion, and store-traffic reductions before changing math. |
| [#126](https://github.com/Dao-AILab/quack/pull/126) feat: add `weight` to cross entropy | 2026-05-01 | norm_elementwise, benchmark_test | Add per-class weight support to cross entropy kernel This PR adds optional per-class `weight` support to the fused cross entropy forward and backward kernels, matching the semantics of `torch.nn.functional.cross_entropy(weight=...)`. When a weight tensor is provided, the per-sample loss becomes `w[t... | test: `tests/test_cross_entropy.py`<br>wrapper: `quack/cross_entropy.py`, `quack/linear_cross_entropy.py` | Look for fusion, vectorization, dtype conversion, and store-traffic reductions before changing math. |
| [#13](https://github.com/Dao-AILab/quack/pull/13) Add support for 3D Inputs for Quack.RMSNorm (support real world training usage) | 2025-07-15 | norm_elementwise | This PR: 1 - updates the forward and backward to support 3D inputs. For most training scenarios, the inputs to RMSNorm will not be 2D but rather batched and thus 3D. Hence, only supporting 2D is a limiting factor for real world usage. The changes are really in the external aspects and not to the ker... | kernel: `quack/rmsnorm.py`<br>test: `tests/test_rmsnorm.py` | Look for fusion, vectorization, dtype conversion, and store-traffic reductions before changing math. |
| [#11](https://github.com/Dao-AILab/quack/pull/11) clearer _calculate_threads_per_row and _set_cluster_n  (if-elif-else rather than nested ternaries) | 2025-07-15 | norm_elementwise, arch_pipeline | Fantastic kernels here! This PR: 1 - improves readability and hopefully maintainability of ~~~ _calculate_threads_per_row ~~~ and ~~~ _set_cluster_n ~~~ by moving them to if-elif-else blocks rather than the current nested ternaries. I found the nested ternaries hard to follow/read, and figure others... | kernel: `quack/rmsnorm.py` | Look for fusion, vectorization, dtype conversion, and store-traffic reductions before changing math. |
| [#57](https://github.com/Dao-AILab/quack/pull/57) Swap order of decorators | 2025-11-21 | norm_elementwise, compiler_runtime | To prevent ambiguous about jitted function, the upcoming cute dsl will require `jit` and `kernel` decorator to be the inner most decorator. Swapping decorators order to prevent error when upgrading. | wrapper: `quack/activation.py` | Look for fusion, vectorization, dtype conversion, and store-traffic reductions before changing math. |

### Memory / Primitives

Use this section for: Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract.
NCU first look: DRAM throughput, L2 hit rate, memory sectors, shared-memory conflicts, and synchronization overhead.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#120](https://github.com/Dao-AILab/quack/pull/120) Fix ColVecReduce shared-memory staging | 2026-04-26 | memory_primitives, gemm_quant, arch_pipeline, benchmark_test | My https://github.com/Dao-AILab/quack/pull/118 added shared-memory staging to ColVecReduce so SM120 epilogues with warps_in_N > 1 can reduce partial row sums across N-warps. This PR fixes two issues: 1. The staging buffer was allocated for all architectures, even though SM90/SM100/SM110 use the orig... | kernel: `quack/gemm_sq_reduce.py`<br>test: `tests/test_epi_ops.py`<br>wrapper: `quack/epi_ops.py` | Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract. |
| [#29](https://github.com/Dao-AILab/quack/pull/29) Fix Symmetric Compile Cache | 2025-08-20 | memory_primitives, gemm_quant, arch_pipeline, benchmark_test | We need to add strides to the cute compile cache, otherwise tensors with the same values but different strides will have different values when multiplied. | kernel: `quack/symmetric_dense_gemm_sm90.py`<br>test: `tests/test_symmetric_dense_gemm_sm90.py` | Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract. |
| [#74](https://github.com/Dao-AILab/quack/pull/74) Fix gather fusion in SM100 | 2026-02-11 | memory_primitives, arch_pipeline, gemm_quant | This can pass all unit tests on B300 GPUs. | kernel: `quack/gemm_interface.py` | Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract. |
| [#98](https://github.com/Dao-AILab/quack/pull/98) Remove asm_dialect=AD_ATT from inline PTX assembly calls | 2026-04-06 | memory_primitives, norm_elementwise | - Remove `asm_dialect=llvm.AsmDialect.AD_ATT` from all 12 `llvm.inline_asm` call sites across 5 files - Fixes ptxas parse errors when inline PTX contains `{}` register grouping braces Problem `AD_ATT` tells LLVM to interpret the asm string as AT&T syntax, where `{` has special meaning as a group del... | wrapper: `quack/activation.py`, `quack/copy_utils.py`, `quack/rounding.py`, `quack/tensormap_manager.py` | Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract. |
| [#102](https://github.com/Dao-AILab/quack/pull/102) Prevent `get_device_capacity` LRU cache from extending `torch.tensor` lifetimes | 2026-04-08 | memory_primitives, compiler_runtime | 2f88de6aeaac68389255350c24b8cd7f9862cde1 does something similar, but its a spot fix only at the call sites of `get_device_capacity`. This PR adds a principled fix for other callers too so that this does not happen again in consumer code that calls the function directly either. | kernel: `quack/cute_dsl_utils.py` | Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract. |

### Scheduler / Autotune

Use this section for: Treat scheduler/autotune configs as shape-specific evidence; replay benchmark shapes before generalizing.
NCU first look: SM occupancy, waves/SM, active cycles, tail effects, and load imbalance.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#79](https://github.com/Dao-AILab/quack/pull/79) Fix Triangular Scheduler | 2026-03-09 | scheduler_autotune, benchmark_test, gemm_quant | 1) `cute.FastDivmodDivisor`'s __rdivmod__ returns IntValue (https://github.com/NVIDIA/cutlass/blob/main/python/CuTeDSL/cutlass/cute/core.pyL4588), so math like ` (utils.sqrt(2 * cluster_id_in_problem + 2.25) - 0.5) * params.group_size_inv_f32` breaks. I cast cluster_id_in_problem to In532 2) Fixed n... | kernel: `quack/tile_scheduler.py`<br>test: `tests/test_gemm_symmetric.py`, `tests/test_symmetric_gemm.py` | Treat scheduler/autotune configs as shape-specific evidence; replay benchmark shapes before generalizing. |
| [#75](https://github.com/Dao-AILab/quack/pull/75) Better gemm configs that reduce 80% autotuning time | 2026-02-25 | scheduler_autotune, gemm_quant, memory_primitives | I benchmarked 18 different MoE configs on H100 and B300 GPU and checked all autotuning logs in quack. The new configs can match the original throughput while reducing 80% autotuning time. | kernel: `quack/gemm_config.py` | Treat scheduler/autotune configs as shape-specific evidence; replay benchmark shapes before generalizing. |
| [#85](https://github.com/Dao-AILab/quack/pull/85) Avoid CUDA context initialization at import time | 2026-03-18 | scheduler_autotune, gemm_quant, arch_pipeline | Previously, `import quack.gemm_interface` called `get_device_capacity(torch.device("cuda"))` at module level to determine which autotuning configs to generate. This eagerly initialized a CUDA context. In our use case, sometimes we do it in a CPU only environment. Fix: generate configs for all suppor... | kernel: `quack/gemm_config.py`, `quack/gemm_interface.py` | Treat scheduler/autotune configs as shape-specific evidence; replay benchmark shapes before generalizing. |
| [#104](https://github.com/Dao-AILab/quack/pull/104) Fix autotuner worker device affinity | 2026-04-13 | scheduler_autotune | I observed the following issue when using quack in combination with fsdp on 8 B200s. All 8 GPUs run quack autotuning simultaneously, in a subprocesses. It seems that all these subprocesses run on cuda:0, the first GPU. They also all take up memory. Unfortunately, this causes an OOM. The other GPUs w... | wrapper: `quack/autotuner.py` | Treat scheduler/autotune configs as shape-specific evidence; replay benchmark shapes before generalizing. |

### Architecture / Pipeline

Use this section for: Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages.
NCU first look: Tensor pipe %, memory pipe utilization, barrier stalls, wait groups, and occupancy.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#94](https://github.com/Dao-AILab/quack/pull/94) [Gemm] fix sm120 gemm kernel invocation error | 2026-04-02 | arch_pipeline, benchmark_test, gemm_quant | Currently the `GemmSm120` does not work and will throw the following error: code block This is because its parent class `GemmSm90` calls the `kernel` with the following parameters: https://github.com/Dao-AILab/quack/blob/a24e4aa1861ccce0419ba41e3cbe9433e192b5ac/quack/gemm_sm90.pyL526-L547 But `GemmS... | kernel: `quack/gemm_sm120.py`<br>benchmark: `benchmarks/benchmark_gemm.py` | Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages. |
| [#99](https://github.com/Dao-AILab/quack/pull/99) add _get_mma_inst_tile_k() virtual method to GemmSm100 | 2026-04-14 | arch_pipeline, gemm_quant, moe_routing | Problem: Subclassing GemmSm100 for specialized GEMM variants (e.g., MoE grouped GEMM) requires overriding the MMA K-tile depth. Currently mma_inst_tile_k = 4 is hardcoded inside _setup_attributes, which feeds into downstream SMEM layout, pipeline stage, and cluster shape calculations. In the MoE ker... | kernel: `quack/gemm_sm100.py` | Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages. |
| [#76](https://github.com/Dao-AILab/quack/pull/76) Support to only store mPostAct | 2026-03-03 | arch_pipeline, gemm_quant | During inference, we can only store mPostAct and do not store pre activation results. This PR fix an assertion error raised in this case. code block Test cases are passed in both Hopper and Blackwell GPUs. | kernel: `quack/gemm_sm100.py`, `quack/gemm_sm90.py` | Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages. |

### Compiler / Runtime

Use this section for: Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests.
NCU first look: Generated kernel shape, launch overhead, occupancy, register pressure, and compile-time-selected schedule.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#123](https://github.com/Dao-AILab/quack/pull/123) Fix cute dsl arch import | 2026-04-29 | compiler_runtime, norm_elementwise, attention_kv, memory_primitives, arch_pipeline | Fix the issue: ImportError: cannot import name 'Arch' from 'cutlass.base_dsl' | kernel: `quack/rmsnorm.py`<br>wrapper: `quack/copy_utils.py`, `quack/cross_entropy.py`, `quack/softmax.py` | Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests. |
| [#83](https://github.com/Dao-AILab/quack/pull/83) Allow for patching tvm-ffi | 2026-03-13 | compiler_runtime, attention_kv | update patcher code block We should just centralize here and remove: https://github.com/Dao-AILab/flash-attention/blob/main/flash_attn/cute/cute_dsl_ptxas.py | kernel: `quack/cute_dsl_ptxas.py` | Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests. |
| [#67](https://github.com/Dao-AILab/quack/pull/67) Add loc info & Fix api changes for CuTeDSL 4.4 | 2026-01-31 | compiler_runtime | Add loc info & Fix api changes for CuTeDSL 4.4 Note: should merge this PR once the repo's dependency updates CuTeDSL version to 4.4. | wrapper: `quack/pipeline.py` | Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests. |
| [#78](https://github.com/Dao-AILab/quack/pull/78) new nvvm.fmin signature | 2026-03-07 | compiler_runtime | https://github.com/NVIDIA/cutlass/blob/49e54f2b2314bf2277c5f56ba9beb33165848793/python/CuTeDSL/cutlass/cute/arch/nvvm_wrappers.pyL963-L972 this fails with cutedsl==4.4.1. Helps fixing this | wrapper: `quack/utils.py`<br>other: `pyproject.toml` | Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests. |

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
