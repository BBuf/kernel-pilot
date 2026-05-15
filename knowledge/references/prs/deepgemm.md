# DeepGEMM PR Knowledge Notes

Repository: <https://github.com/deepseek-ai/DeepGEMM>

This page is the production-PR layer for kernel-knowledge. It keeps merged PRs with CUDA/NVIDIA target evidence, real kernel/source changes, and an optimization/performance mechanism such as tuning, fusion, tensor-core paths, memory movement, scheduling, profiling, or benchmark-backed speed work. Release, CI-only, formatting, dependency-only, correctness-only, and non-target-backend PRs are filtered out.

## Repository Source Scan

Read these source regions before opening individual PR diffs:

- `csrc/apis`
- `csrc/jit`
- `csrc/jit_kernels/heuristics`
- `csrc/jit_kernels/impls`
- `deep_gemm/include/deep_gemm`
- `deep_gemm/testing`
- `tests`

## Coverage Summary

| Category | CUDA optimization PRs |
| --- | ---: |
| GEMM / Quantization | 12 |
| Scheduler / Autotune | 1 |
| Architecture / Pipeline | 4 |
| Benchmark / Test Evidence | 3 |

## Pull Request Case Notes

### GEMM / Quantization

Use this section for: Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate.
NCU first look: Tensor pipe %, DRAM/L2 bytes, active cycles, register pressure, and scale-load traffic.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#328](https://github.com/deepseek-ai/DeepGEMM/pull/328) Sync nv_dev with upstream #316 (Mega MoE optimizations & benchmarks) | 2026-05-08 | gemm_quant, benchmark_test, moe_routing, attention_kv, scheduler_autotune | Cherry-picks upstream `891d57b` (deepseek-ai PR 316: "Add various optimizations and Mega MoE benchmarks") onto `nv_dev` (currently at `c491439`, the merge of PR 314). Conflicts resolved against the NV-side commits from PR 314 (`f6d98f2`, `12cb7c0`, `a97b74d`): - **`deep_gemm/include/deep_gemm/schedu... | kernel: `csrc/apis/attention.hpp`, `csrc/apis/mega.hpp`, `csrc/jit_kernels/heuristics/mega_moe.hpp`, `csrc/jit_kernels/impls/sm100_fp8_fp4_mega_moe.hpp`<br>benchmark: `scripts/run_ncu_mega_moe.sh`<br>test: `tests/test_attention.py`, `tests/test_mega_moe.py`<br>wrapper: `scripts/quick_plot_pm.py`<br>docs: `README.md` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |
| [#198](https://github.com/deepseek-ai/DeepGEMM/pull/198) Make various updates and fixes | 2025-09-25 | gemm_quant, arch_pipeline, memory_primitives, scheduler_autotune, attention_kv | This PR is submitted by NVIDIA. Optimized some kernels on SM100 and added some kernels for DeepSeek V3 inference. | kernel: `csrc/apis/attention.hpp`, `csrc/apis/einsum.hpp`, `csrc/apis/gemm.hpp`, `csrc/apis/layout.hpp` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |
| [#112](https://github.com/deepseek-ai/DeepGEMM/pull/112) Add more GPU architectures support | 2025-07-18 | gemm_quant, memory_primitives, scheduler_autotune, arch_pipeline | Hi DeepGEMM Team, This PR is submitted by NVIDIA and introduces support for more GPU architectures. Key Points - MXFP8 support - Same 1x128 by 128x128 SF (scaling factor) recipe as original DeepGEMM, but using UE8M0 instead of FP32 for SF data format. - Same SF input layout as original DeepGEMM. - M... | kernel: `csrc/indexing/main.cu`, `csrc/jit/cache.hpp`, `csrc/jit/compiler.hpp`, `csrc/jit/device_runtime.hpp`<br>docs: `README.md`<br>other: `.gitmodules`, `CMakeLists.txt` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |
| [#88](https://github.com/deepseek-ai/DeepGEMM/pull/88) Support TMA multicast on B with m_grouped_gemm_contiguous. | 2025-04-21 | gemm_quant, moe_routing, arch_pipeline, scheduler_autotune, benchmark_test | Add function is_tma_multicast_valid() in scheduler.cuh to support TMA multicast on B with m_grouped_gemm_contiguous. Change test_m_grouped_gemm_contiguous in test_core.py to better simulate real-world usage. | kernel: `deep_gemm/include/deep_gemm/fp8_gemm.cuh`, `deep_gemm/include/deep_gemm/scheduler.cuh`, `deep_gemm/jit_kernels/gemm.py`<br>test: `tests/test_core.py`<br>docs: `README.md` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |
| [#103](https://github.com/deepseek-ai/DeepGEMM/pull/103) Grouped GEMM skip useless computation for unaligned Ms | 2025-05-27 | gemm_quant, moe_routing, benchmark_test, scheduler_autotune, compiler_runtime | Skip useless computation on M and reconstruct test_m_grouped_gemm_contiguous and test_m_grouped_gemm_masked'. In test_m_grouped_gemm_contiguous, there is a speedup of 0-15 TFLOPS (Due to the larger expected_m_per_group, the speedup effect is not very significant). In test_m_grouped_gemm_masked, ther... | kernel: `deep_gemm/include/deep_gemm/fp8_gemm.cuh`, `deep_gemm/include/deep_gemm/scheduler.cuh`, `deep_gemm/jit/compiler.py`<br>test: `tests/test_core.py`<br>docs: `README.md` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |
| [#95](https://github.com/deepseek-ai/DeepGEMM/pull/95) Weight gradient kernels for dense and MoE models | 2025-05-14 | gemm_quant, moe_routing, compiler_runtime, benchmark_test | This Pull Request introduces `deepgemm.wgrad_gemm_fp8_fp8_fp32_nt` and `k_grouped_wgrad_gemm_fp8_fp8_fp32_nt`, optimized weight gradient kernels for dense and MoE models. These kernels achieve a ~20% speedup compared to the internal CUTLASS implementation. For detailed usage, refer to the function d... | kernel: `deep_gemm/__init__.py`, `deep_gemm/include/deep_gemm/fp8_gemm.cuh`, `deep_gemm/include/deep_gemm/fp8_wgrad_gemm.cuh`, `deep_gemm/include/deep_gemm/mma_utils.cuh`<br>test: `tests/test_core.py`<br>docs: `README.md` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |
| [#168](https://github.com/deepseek-ai/DeepGEMM/pull/168) Fix performance issue of m-grouped contiguous GEMMs. | 2025-08-22 | gemm_quant, moe_routing, benchmark_test, scheduler_autotune | This PR fixed issue 160. On my H800, before fix: code block after fix: code block | kernel: `deep_gemm/include/deep_gemm/common/scheduler.cuh` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |
| [#74](https://github.com/deepseek-ai/DeepGEMM/pull/74) Performance: Larger BlockTile optimizations enable 1470+ TF FP8 on the "H800"-SXM | 2025-03-25 | gemm_quant, moe_routing, benchmark_test | By leveraging Large BlockTile optimization to alleviate **L2 cache pressure** and **maximize data reuse**, the H800-SXM achieves peak FP8 compute performance of 1470+ TFLOPS. @LyricZhao Normal GEMMs for dense models \| M \| N \| K \| Base BMxBN \| Computation \| Opti BMxBN \| Computation \| Speedup \| \|:----... | kernel: `deep_gemm/include/deep_gemm/fp8_gemm.cuh`, `deep_gemm/include/deep_gemm/mma_utils.cuh`, `deep_gemm/include/deep_gemm/scheduler.cuh`, `deep_gemm/include/deep_gemm/utils.cuh`<br>docs: `README.md` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |
| [#233](https://github.com/deepseek-ai/DeepGEMM/pull/233) support bf16 bias in deepgemm2 | 2025-11-25 | gemm_quant, arch_pipeline, benchmark_test | run tests on B200 with: tests/test_bf16.py tests/test_fp8.py | kernel: `csrc/apis/gemm.hpp`, `deep_gemm/include/deep_gemm/impls/sm100_fp8_gemm_1d1d.cuh`<br>test: `tests/generators.py` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |
| [#86](https://github.com/deepseek-ai/DeepGEMM/pull/86) Use swizzling instead of padding | 2025-04-14 | gemm_quant, moe_routing, compiler_runtime | - Remove performance report on README for maintenance simplicity - Peak TFLOPS 1503 -> 1519 TFLOPS, the original 1520 is on another "good" GPU - `(m= 4096, n=24576, k= 1536)`: 1212 -> 1270 TFLOPS - `(m= 4096, n=32768, k= 512)`: 775 -> 836 TFLOPS - `(m= 4096, n= 7168, k=16384)`: 1503 -> 1519 TFLOPS -... | kernel: `deep_gemm/include/deep_gemm/fp8_gemm.cuh`, `deep_gemm/jit/compiler.py`, `deep_gemm/jit_kernels/gemm.py`, `deep_gemm/jit_kernels/m_grouped_gemm.py`<br>docs: `README.md`<br>other: `indexing/main.cu` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |
| [#81](https://github.com/deepseek-ai/DeepGEMM/pull/81) Performance: BlockTile 256x128 optimizations enable 1500+ TF FP8 | 2025-04-09 | gemm_quant, benchmark_test | By resuing the Accumulator registers of Tensor Cores to implement a 256x128 BlockTile structure, this approach significantly increases data reuse, reduces the demand for L2 Cache and HBM memory accesses, and enhances the SM's computational frequency, ultimately achieving FP8 performance exceeding 1,... | kernel: `deep_gemm/include/deep_gemm/fp8_gemm.cuh`, `deep_gemm/jit_kernels/gemm.py`<br>docs: `README.md` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |
| [#227](https://github.com/deepseek-ai/DeepGEMM/pull/227) Use larger MMA shape to optimize sm100_fp8_mqa_logits | 2025-11-14 | gemm_quant, arch_pipeline | 10% speedup, it is now bounded by the cuda core and the number of registers. | kernel: `csrc/jit_kernels/impls/smxx_fp8_mqa_logits.hpp`, `deep_gemm/include/deep_gemm/impls/sm100_fp8_mqa_logits.cuh` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |

### Scheduler / Autotune

Use this section for: Treat scheduler/autotune configs as shape-specific evidence; replay benchmark shapes before generalizing.
NCU first look: SM occupancy, waves/SM, active cycles, tail effects, and load imbalance.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#158](https://github.com/deepseek-ai/DeepGEMM/pull/158) Fix inappropriate configs for some small shapes | 2025-08-14 | scheduler_autotune, compiler_runtime | This PR polishes get_best_configs modeling, to avoid picking inappropriate `(block_m, block_n)` for some shapes. Bad cases before this PR: \|\| (m, n, k) \| picked (block_m, block_n, block_k) \| expected best (block_m, block_n, block_k) \| kernel duration (on H20) \| \|:---\|:---\|:---\|:---\|:---\| \| sm90_fp8_... | kernel: `csrc/jit_kernels/heuristics/common.hpp` | Treat scheduler/autotune configs as shape-specific evidence; replay benchmark shapes before generalizing. |

### Architecture / Pipeline

Use this section for: Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages.
NCU first look: Tensor pipe %, memory pipe utilization, barrier stalls, wait groups, and occupancy.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#78](https://github.com/deepseek-ai/DeepGEMM/pull/78)  Solving bank conflict via padding and TMA 3D store | 2025-04-03 | arch_pipeline, gemm_quant, moe_routing, compiler_runtime | The optimization should make general cases 1% faster, cases with small Ks ~10% faster. | kernel: `deep_gemm/include/deep_gemm/fp8_gemm.cuh`, `deep_gemm/include/deep_gemm/tma_utils.cuh`, `deep_gemm/include/deep_gemm/utils.cuh`, `deep_gemm/jit/compiler.py`<br>docs: `README.md` | Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages. |
| [#193](https://github.com/deepseek-ai/DeepGEMM/pull/193) Fix multicast bug and optimize masked GEMM | 2025-09-12 | arch_pipeline, gemm_quant, scheduler_autotune, compiler_runtime | In the previous code, the variable used for determining whether to use multicast was incorrectly applied, the variable for judging A multicast capability was used to determine B multicast capability. Fortunately, this error does not affect correctness, and it also does not impact performance in the... | kernel: `csrc/jit_kernels/heuristics/common.hpp`, `csrc/jit_kernels/heuristics/sm100.hpp`, `csrc/jit_kernels/heuristics/sm90.hpp` | Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages. |
| [#83](https://github.com/deepseek-ai/DeepGEMM/pull/83) Use 1D TMA store instead of 3D | 2025-04-11 | arch_pipeline, gemm_quant, moe_routing, compiler_runtime | Use 1D TMA store instead of 3D | kernel: `deep_gemm/include/deep_gemm/fp8_gemm.cuh`, `deep_gemm/include/deep_gemm/tma_utils.cuh`, `deep_gemm/jit_kernels/gemm.py`, `deep_gemm/jit_kernels/m_grouped_gemm.py`<br>other: `indexing/main.cu` | Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages. |
| [#270](https://github.com/deepseek-ai/DeepGEMM/pull/270) fix: use SM90ArchSpec instead of SM100ArchSpec in sm90_bf16_k_grouped_gemm | 2026-01-06 | arch_pipeline, gemm_quant, moe_routing | This PR fixes a copy-paste error in `sm90_bf16_k_grouped_gemm` where `SM100ArchSpec` was incorrectly used instead of `SM90ArchSpec` for TMA descriptor block size calculations. Problem In `csrc/jit_kernels/impls/sm90_bf16_gemm.hpp`, the function `sm90_bf16_k_grouped_gemm` (lines 259-274) was using `S... | kernel: `csrc/jit_kernels/impls/sm90_bf16_gemm.hpp` | Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages. |

### Benchmark / Test Evidence

Use this section for: Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code.
NCU first look: Use the PR's benchmark/profile command as the first replay target.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#316](https://github.com/deepseek-ai/DeepGEMM/pull/316) Add various optimizations and Mega MoE benchmarks | 2026-04-24 | benchmark_test, moe_routing, gemm_quant, attention_kv, scheduler_autotune | We benchmarked Mega MoE on DeepSeek-V4-Flash and DeepSeek-V4-Pro under 8-way expert parallelism (EP8), testing at various batch sizes (i.e., the number of tokens per rank) to cover different serving scenarios. All values are averaged across 8 ranks. DeepSeek-V4-Flash DeepSeek-V4-Flash has 256 expert... | kernel: `csrc/apis/attention.hpp`, `csrc/apis/mega.hpp`, `csrc/jit_kernels/heuristics/mega_moe.hpp`, `csrc/jit_kernels/impls/sm100_fp8_fp4_mega_moe.hpp`<br>benchmark: `scripts/run_ncu_mega_moe.sh`<br>test: `tests/test_attention.py`, `tests/test_mega_moe.py`<br>wrapper: `scripts/quick_plot_pm.py`<br>docs: `README.md` | Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code. |
| [#42](https://github.com/deepseek-ai/DeepGEMM/pull/42) Performance: reducing the percentage of FFMA interleaving yields a sight performance gain, roughly 0.5% | 2025-03-05 | benchmark_test, gemm_quant, compiler_runtime | **Reducing** the percentage of FFMA interleaving yields a **sight performance gain**, roughly **0.5%**。 <img width="795" alt="image" src="https://github.com/user-attachments/assets/b8863a7d-34b1-439a-a7fe-fe2161daa530" /> Test on H100-SXM && CUDA 12.8. | kernel: `deep_gemm/jit/interleave_ffma.py` | Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code. |
| [#68](https://github.com/deepseek-ai/DeepGEMM/pull/68) Correctly flush L2 (+performance impact & upcoming optimization fork) | 2025-03-16 | benchmark_test, gemm_quant | Thank you for open sourcing this under a MIT license! I was working on optimized PTX matrix multiplications for H100 as you released this, and decided to continue working on it as a fork of your repo instead (not yet public). I've achieved very large performance gains (see below) and I plan to open... | kernel: `deep_gemm/utils.py`<br>test: `tests/test_core.py` | Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code. |

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
