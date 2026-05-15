# Topic: RoPE / Rotary Position Embeddings

## What it covers

Rotary position embedding kernels: standard RoPE, NeoX-style interleaved,
GPT-J-style paired, YaRN / NTK extensions, long-context variants.

## Per-framework references

| Framework | Where to look | What it teaches |
| --- | --- | --- |
| `sglang` | `sgl-kernel/csrc/elementwise/`, Python wrappers in `python/sglang/srt/layers/rotary_embedding.py` | Production RoPE variants for many models. |
| `vllm` | `csrc/pos_encoding_kernels.cu` | NeoX and GPT-J RoPE reference. |
| `tensorrt-llm` | `cpp/tensorrt_llm/kernels/unfusedAttentionKernels/*` (RoPE applied per token) | RoPE applied during the QKV projection prologue. |
| `flashinfer` | `include/flashinfer/pos_enc.cuh` | Fused RoPE inside the attention kernel. |
| `triton` | community implementations referenced from SGLang / vLLM Triton paths | Triton block-pointer RoPE templates. |

## Common optimization patterns

- Apply RoPE in-place on Q / K right before the attention kernel; avoids a
  second pass.
- Vectorized cos/sin LUT loads.
- Fuse RoPE with QK-norm when both are applied per head.
- For long-context (NTK / YaRN), precompute the frequency tensor once and
  index it by position.

## Common bottlenecks

- Memory-bound; check `dram__throughput`.
- Mismatched interleaving (NeoX vs GPT-J) is a frequent source of silent
  correctness drift; always test against `pytorch` reference.

## Recommended ncu metrics

- `dram__throughput.avg.pct_of_peak_sustained_elapsed`
- `smsp__inst_executed.avg.per_cycle_active`
- `l1tex__throughput.avg.pct_of_peak_sustained_elapsed`
