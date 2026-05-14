# Topic: Attention / FMHA / Paged

## What it covers

Fused multi-head attention (FMHA) on GPUs, including:

- prefill (context) FMHA, decode MMHA, append / extend attention,
- paged KV (vLLM / FlashInfer / SGLang block tables),
- MLA (DeepSeek latent attention),
- speculative / tree decode aware variants,
- backward attention.

## Per-framework references

| Framework | Where to look | What it teaches |
| --- | --- | --- |
| `flash-attention` | `csrc/flash_attn/src/flash_fwd_kernel.h`, `flash_attn/cute/`, `hopper/` | Online softmax, FA2 SM80, FA3 SM90 with TMA + WGMMA. |
| `flashinfer` | `include/flashinfer/`, `csrc/fmha_v2/fmha/hopper/`, `csrc/fmha_v2/fmha/warpspec/` | Paged KV, prefix-cache aware, MLA, warp-specialized FMHA. |
| `tensorrt-llm` | `cpp/tensorrt_llm/kernels/contextFusedMultiHeadAttention/`, `decoderMaskedMultiheadAttention/` | NVIDIA's context FMHA and decoder MMHA per arch. |
| `sglang` | `python/sglang/srt/layers/attention/`, `sgl-kernel/csrc/attention/` | Backend routing + production serving wrappers. |
| `vllm` | `csrc/attention/`, `vllm/attention/backends/` | Paged attention v1/v2, backend dispatcher. |
| `pytorch` | `aten/src/ATen/native/transformers/cuda/` | SDPA correctness oracle and arch dispatch. |
| `cutlass` | `examples/48_hopper_*`, `examples/60_*` | Hopper / Blackwell FMHA reference using CuTe. |
| `thunderkittens` | `examples/attn/` | Alternative tile-primitive view of FA. |

## Common optimization patterns

- Online softmax (FA-style rescaling on each KV block).
- KV-block tiling, head-major or seq-major orderings, depending on dtype.
- Causal masking via block coordinates (do not store the mask).
- TMA + WGMMA pipeline on Hopper; warp-specialized producer / consumer
  warpgroups.
- Split-K over the sequence axis for decode-style attention.
- Per-request KV gather using a block table; minimize indirect-load latency
  by coalescing accesses inside each block.

## Common bottlenecks

- HBM bandwidth dominates the small-batch decode case; tensor pipe under-
  utilized.
- Backward attention is L2-bound at long sequences; check `lts__t_bytes`.
- Warp-issue stalls in the masked / softmax phase; check
  `smsp__warp_issue_stalled_long_scoreboard`.

## Recommended ncu metrics

- `sm__inst_executed_pipe_tensor.avg.pct_of_peak_sustained_elapsed`
- `smsp__average_warp_latency_per_inst_executed`
- `l1tex__t_sectors_pipe_lsu_mem_global_op_ld.sum.per_second`
- `sm__warps_active.avg.pct_of_peak_sustained_active`
- `smsp__warp_issue_stalled_long_scoreboard.sum`

## Recommended micro-benchmarks to copy / adapt

- `flash-attention/benchmarks/benchmark_attn.py`
- `flash-attention/benchmarks/bench_sm90.py`
- `flashinfer/benchmarks/bench_blackwell_attention.py`
- `sglang/python/sglang/bench_one_batch.py` for end-to-end serving sanity.
