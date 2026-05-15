# Tencent HPC Ops PR Knowledge Notes

Repository: <https://github.com/Tencent/hpc-ops>

This page is the production-PR layer for kernel-knowledge. It keeps merged PRs with CUDA/NVIDIA target evidence, real kernel/source changes, and an optimization/performance mechanism such as tuning, fusion, tensor-core paths, memory movement, scheduling, profiling, or benchmark-backed speed work. Release, CI-only, formatting, dependency-only, correctness-only, and non-target-backend PRs are filtered out.

## Repository Source Scan

## Coverage Summary

| Category | CUDA optimization PRs |
| --- | ---: |
| Attention / KV / Decode | 4 |
| Norm / Elementwise / Epilogue | 1 |

## Pull Request Case Notes

### Attention / KV / Decode

Use this section for: Preserve page/KV/layout and plan-run contracts; profile memory traffic separately from math utilization.
NCU first look: Long scoreboard, L2/DRAM traffic, global-load sectors, tensor pipe %, and shared-memory bank conflicts.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#39](https://github.com/Tencent/hpc-ops/pull/39) Add rope_norm_store_kv fusion op | 2026-04-13 | attention_kv, norm_elementwise, benchmark_test, gemm_quant | This PR adds a fused CUDA operator that performs RoPE rotation, optional QK RMSNorm, and blocked KV-cache write in a single kernel. API \| API \| Input dtype \| Output \| Description \| \|-----\|-------------\|--------\|-------------\| \| `hpc.rope_norm_store_kv` \| BF16 \| `out_q`; K/V written in-place to KV ca... | kernel: `hpc/rope.py`, `src/rope/entry.cc`, `src/rope/rope.cu`, `src/rope/rope.h`<br>test: `tests/test_rope.py` | Preserve page/KV/layout and plan-run contracts; profile memory traffic separately from math utilization. |
| [#38](https://github.com/Tencent/hpc-ops/pull/38) attn decode support mtp and refine code | 2026-04-10 | attention_kv, gemm_quant | 1. support mtp 1 and mtp 2 for bf16/fp8 decode attn 2. support num_heads_q / num_heads_kv == 8 3. refine attn decode code | kernel: `hpc/attention.py`, `src/attention/decode/decode.cc`, `src/attention/decode/decode.h`, `src/attention/decode/m64_dim128.cu`<br>test: `tests/test_attention_decode_bf16.py`, `tests/test_attention_decode_fp8.py`<br>other: `src/utils/utils.cuh` | Preserve page/KV/layout and plan-run contracts; profile memory traffic separately from math utilization. |
| [#40](https://github.com/Tencent/hpc-ops/pull/40) Add independent K scale support in FP8 prefill attention | 2026-04-10 | attention_kv, gemm_quant | Split the combined qkscale parameter into separate qscale and kscale in the FP8 prefill attention kernel, allowing Q and K to use different quantization granularities. Breaking Change: `qkscale: [num_batch, num_head_q, max_seqlens_q_pad], float32` is replaced by: `qscale: [num_batch, num_head_q, max... | kernel: `hpc/attention.py`, `src/attention/entry.cc`, `src/attention/prefill/config.h`, `src/attention/prefill/kernels.cuh`<br>test: `tests/test_attention_with_kvcache_prefill_fp8.py` | Preserve page/KV/layout and plan-run contracts; profile memory traffic separately from math utilization. |
| [#6](https://github.com/Tencent/hpc-ops/pull/6) fix multi kv head for attn splitk bf16 | 2026-01-26 | attention_kv, scheduler_autotune | Fix multi kv head bug for attn splitk bf16 decode. The main resason is forget use kv head stride for lse. | kernel: `src/attention/decode/smallm_splitk_kernels.cuh`<br>test: `tests/test_attention_decode_bf16.py` | Preserve page/KV/layout and plan-run contracts; profile memory traffic separately from math utilization. |

### Norm / Elementwise / Epilogue

Use this section for: Look for fusion, vectorization, dtype conversion, and store-traffic reductions before changing math.
NCU first look: DRAM %, L2 bytes, global load/store sectors, eligible warps, and long scoreboard.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#35](https://github.com/Tencent/hpc-ops/pull/35) add fused_rmsnorm_quant and fused_rmsnorm_rope op | 2026-04-09 | norm_elementwise, attention_kv, gemm_quant | add fused_rmsnorm_quant and fused_rmsnorm_rope op | kernel: `hpc/normalization.py`, `src/attention/decode/smallm_splitk_kernels.cuh`, `src/normalization/entry.cc`, `src/normalization/fused_rmsnorm_with_scale.cu`<br>test: `tests/test_normalization.py` | Look for fusion, vectorization, dtype conversion, and store-traffic reductions before changing math. |

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
