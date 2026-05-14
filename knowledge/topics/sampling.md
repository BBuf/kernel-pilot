# Topic: Sampling / Speculative Decode

## What it covers

Logits processing (temperature, top-k, top-p, min-p, penalty), speculative /
tree decode bookkeeping (EAGLE / Medusa / draft-target verification), greedy
sampling.

## Per-framework references

| Framework | Where to look | What it teaches |
| --- | --- | --- |
| `sglang` | `python/sglang/srt/layers/sampler.py`, `sgl-kernel/csrc/spec_decode/` | Production logits processing + EAGLE / tree decode bookkeeping. |
| `flashinfer` | `include/flashinfer/sampling.cuh`, `python/flashinfer/sampling.py` | Top-k / top-p / min-p / temperature sampling primitives. |
| `vllm` | `csrc/sampler/`, `vllm/model_executor/layers/sampler.py` | Reference sampler integration with paged-attention scheduler. |
| `tensorrt-llm` | `cpp/tensorrt_llm/kernels/topkSampling*.cu` | NVIDIA's top-k sampling reference. |

## Common optimization patterns

- Two-pass top-k: warp-level partial top-k, then block-level merge.
- Fused top-k + softmax for top-p sampling.
- Tree-decode: gather logits via a per-branch index tensor, then verify with
  a small kernel that compares draft tokens to target tokens.
- For very-small vocab cases, prefer a one-pass radix-style top-k.

## Common bottlenecks

- `atomicAdd` contention on the candidate token buffer (avoid with warp
  reductions).
- Long-scoreboard stalls when reading the logits tensor without vectorized
  loads.
- Tree-decode gather is gather-heavy; consider sharded layouts.

## Recommended ncu metrics

- `smsp__warps_eligible.avg.per_cycle_active`
- `l1tex__t_sectors_pipe_lsu_mem_global_op_ld.sum`
- `smsp__inst_executed_op_global_atom.sum`
- `dram__throughput.avg.pct_of_peak_sustained_elapsed`
