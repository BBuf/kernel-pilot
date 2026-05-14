# Topic: Normalization (RMSNorm / LayerNorm / QK-Norm)

## What it covers

Fused RMSNorm, LayerNorm, and their variants (QK-norm, fused-add-norm,
norm + quant). Almost always memory-bound.

## Per-framework references

| Framework | Where to look | What it teaches |
| --- | --- | --- |
| `sglang` | `sgl-kernel/csrc/elementwise/` | Fused RMSNorm + add + (optional) quant, QK-norm across heads. |
| `vllm` | `csrc/layernorm_kernels.cu`, `csrc/quantization/fp8/` | Fused RMSNorm + FP8 quant. |
| `tensorrt-llm` | `cpp/tensorrt_llm/kernels/rmsnormKernels.cu` | NVIDIA's fused RMSNorm + residual + quant. |
| `pytorch` | `aten/src/ATen/native/cuda/layer_norm_kernel.cu` | Correctness oracle. |
| `triton` | `python/tutorials/05-layer-norm.py` | Triton block-pointer norm reference. |
| `cccl-cub` | `cub/block/block_reduce.cuh` | Numerically-stable block reductions. |

## Common optimization patterns

- Per-row CTA with block reduction; vectorized loads (`float4`, `bfloat162`).
- Fuse `add(residual, x)` before the reduction to avoid a second pass.
- Fuse the post-norm quantization (FP8 / FP4) into the same kernel.
- QK-norm: a small reduction per head; can share warp-level reductions
  across heads if hidden dim is small.

## Common bottlenecks

- HBM bandwidth (always check `dram__throughput`).
- Bank conflicts in shared-memory reductions when using non-warp-friendly
  vector widths.
- Long-scoreboard stalls when the reduction is forced into multiple passes.

## Recommended ncu metrics

- `dram__throughput.avg.pct_of_peak_sustained_elapsed`
- `l1tex__throughput.avg.pct_of_peak_sustained_elapsed`
- `smsp__inst_executed.avg.per_cycle_active`
- `smsp__warp_issue_stalled_long_scoreboard.sum`
- `l1tex__data_bank_conflicts_pipe_lsu.sum`
