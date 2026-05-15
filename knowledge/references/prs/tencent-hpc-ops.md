# Tencent HPC Ops PR Knowledge Notes

Repository: <https://github.com/Tencent/hpc-ops>

This page is the production-PR layer for kernel-knowledge. It favors merged PRs that changed kernels, dispatch, JIT/runtime integration, tuning policy, tests, benchmarks, or profiling evidence. Release, CI-only, formatting, pure version-bump, and non-target-backend PRs are filtered out.

## Repository Source Scan

## Coverage Summary

| Category | CUDA-kernel PRs |
| --- | ---: |
| GEMM / Quantization | 1 |
| Attention / KV / Decode | 4 |
| MoE / Routing | 1 |
| Norm / Elementwise / Epilogue | 1 |
| Architecture / Pipeline | 1 |

## Pull Request Case Notes

### GEMM / Quantization

Use this section for: Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate.
NCU first look: Tensor pipe %, DRAM/L2 bytes, active cycles, register pressure, and scale-load traffic.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#13](https://github.com/Tencent/hpc-ops/pull/13) fix blockwise moe ep bug | 2026-01-28 | gemm_quant, moe_routing, benchmark_test | fix blockwise moe ep bug | kernel: `src/fuse_moe/fuse_moe.cu`<br>test: `tests/test_fuse_moe_blockwise.py` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |

### Attention / KV / Decode

Use this section for: Preserve page/KV/layout and plan-run contracts; profile memory traffic separately from math utilization.
NCU first look: Long scoreboard, L2/DRAM traffic, global-load sectors, tensor pipe %, and shared-memory bank conflicts.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#39](https://github.com/Tencent/hpc-ops/pull/39) Add rope_norm_store_kv fusion op | 2026-04-13 | attention_kv, norm_elementwise, benchmark_test, gemm_quant | This PR adds a fused CUDA operator that performs RoPE rotation, optional QK RMSNorm, and blocked KV-cache write in a single kernel. API \| API \| Input dtype \| Output \| Description \| \|-----\|-------------\|--------\|-------------\| \| `hpc.rope_norm_store_kv` \| BF16 \| `out_q`; K/V written in-place to KV ca... | test: `tests/test_rope.py`<br>wrapper: `hpc/rope.py`, `src/rope/entry.cc`, `src/rope/rope.h`<br>other: `src/rope/rope.cu` | Preserve page/KV/layout and plan-run contracts; profile memory traffic separately from math utilization. |
| [#38](https://github.com/Tencent/hpc-ops/pull/38) attn decode support mtp and refine code | 2026-04-10 | attention_kv, gemm_quant | 1. support mtp 1 and mtp 2 for bf16/fp8 decode attn 2. support num_heads_q / num_heads_kv == 8 3. refine attn decode code | kernel: `hpc/attention.py`, `src/attention/decode/decode.cc`, `src/attention/decode/decode.h`, `src/attention/decode/m64_dim128.cu`<br>test: `tests/test_attention_decode_bf16.py`, `tests/test_attention_decode_fp8.py`<br>other: `src/utils/utils.cuh` | Preserve page/KV/layout and plan-run contracts; profile memory traffic separately from math utilization. |
| [#40](https://github.com/Tencent/hpc-ops/pull/40) Add independent K scale support in FP8 prefill attention | 2026-04-10 | attention_kv, gemm_quant | Split the combined qkscale parameter into separate qscale and kscale in the FP8 prefill attention kernel, allowing Q and K to use different quantization granularities. Breaking Change: `qkscale: [num_batch, num_head_q, max_seqlens_q_pad], float32` is replaced by: `qscale: [num_batch, num_head_q, max... | kernel: `hpc/attention.py`, `src/attention/entry.cc`, `src/attention/prefill/config.h`, `src/attention/prefill/kernels.cuh`<br>test: `tests/test_attention_with_kvcache_prefill_fp8.py` | Preserve page/KV/layout and plan-run contracts; profile memory traffic separately from math utilization. |
| [#6](https://github.com/Tencent/hpc-ops/pull/6) fix multi kv head for attn splitk bf16 | 2026-01-26 | attention_kv, scheduler_autotune | Fix multi kv head bug for attn splitk bf16 decode. The main resason is forget use kv head stride for lse. | kernel: `src/attention/decode/smallm_splitk_kernels.cuh`<br>test: `tests/test_attention_decode_bf16.py` | Preserve page/KV/layout and plan-run contracts; profile memory traffic separately from math utilization. |

### MoE / Routing

Use this section for: Separate routing, permutation, top-k, and expert GEMM costs; keep tail-token and expert-layout tests attached to the idea.
NCU first look: Tensor pipe %, SM imbalance, branch divergence, L2 traffic, permutation traffic, and synchronization stalls.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#20](https://github.com/Tencent/hpc-ops/pull/20) fix num_tokens_per_group_avg use num_expert_total for ep  | 2026-02-03 | moe_routing | blockwise fused moe should use num_expert_total to calculate num_tokens_per_group_avg for tile select. | kernel: `src/fuse_moe/fuse_moe.cu` | Separate routing, permutation, top-k, and expert GEMM costs; keep tail-token and expert-layout tests attached to the idea. |

### Norm / Elementwise / Epilogue

Use this section for: Look for fusion, vectorization, dtype conversion, and store-traffic reductions before changing math.
NCU first look: DRAM %, L2 bytes, global load/store sectors, eligible warps, and long scoreboard.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#35](https://github.com/Tencent/hpc-ops/pull/35) add fused_rmsnorm_quant and fused_rmsnorm_rope op | 2026-04-09 | norm_elementwise, attention_kv, gemm_quant | add fused_rmsnorm_quant and fused_rmsnorm_rope op | kernel: `hpc/normalization.py`, `src/attention/decode/smallm_splitk_kernels.cuh`, `src/normalization/entry.cc`, `src/normalization/fused_rmsnorm_with_scale.cu`<br>test: `tests/test_normalization.py` | Look for fusion, vectorization, dtype conversion, and store-traffic reductions before changing math. |

### Architecture / Pipeline

Use this section for: Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages.
NCU first look: Tensor pipe %, memory pipe utilization, barrier stalls, wait groups, and occupancy.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#36](https://github.com/Tencent/hpc-ops/pull/36) update cutlass4.4.2 | 2026-04-09 | arch_pipeline, memory_primitives | update cutlass4.4.2 | kernel: `3rd/cutlass/include/cute/algorithm/axpby.hpp`, `3rd/cutlass/include/cute/algorithm/clear.hpp`, `3rd/cutlass/include/cute/algorithm/cooperative_copy.hpp`, `3rd/cutlass/include/cute/algorithm/cooperative_gemm.hpp` | Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages. |

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
