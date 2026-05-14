# Topic: Activation / Element-wise Fusion

## What it covers

Fused activation kernels (silu, gelu, swiglu), fused-add-residual,
fused-dequant-activation. Almost always memory-bound; the value comes from
fusing them into a neighbor compute kernel.

## Per-framework references

| Framework | Where to look | What it teaches |
| --- | --- | --- |
| `sglang` | `sgl-kernel/csrc/elementwise/` | Fused silu_and_mul, swiglu, residual-add variants. |
| `vllm` | `csrc/activation_kernels.cu` | Reference silu / gelu / swiglu. |
| `tensorrt-llm` | `cpp/tensorrt_llm/kernels/preQuantScaleKernel/` | Pre-GEMM fused activation + quant. |
| `pytorch` | `aten/src/ATen/native/cuda/Activation.cu` | Correctness oracle. |
| `triton` | `python/tutorials/02-fused-softmax.py` style templates | Triton fused activation reference. |

## Common optimization patterns

- Always fuse into the preceding or following GEMM epilogue when possible.
- Vectorize loads / stores (`float4`, `bfloat162`, `half2`).
- For swiglu, fuse the two-projection `silu(x) * y` into one pass.

## Common bottlenecks

- Standalone activation kernels are pure-bandwidth and should be fused.
- Misaligned tail handling can degrade vectorization on the last tile.

## Recommended ncu metrics

- `dram__throughput.avg.pct_of_peak_sustained_elapsed`
- `smsp__inst_executed.avg.per_cycle_active`
- `l1tex__throughput.avg.pct_of_peak_sustained_elapsed`
