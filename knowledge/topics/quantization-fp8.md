# Topic: Quantization (FP8 / FP4 / INT8 / AWQ / GPTQ)

## What it covers

Low-precision GEMM, dequant-on-the-fly kernels, block-scaled FP8 / FP4
layouts, AWQ / GPTQ INT4 / INT8 weight-only kernels, SmoothQuant W8A8.

## Per-framework references

| Framework | Where to look | What it teaches |
| --- | --- | --- |
| `deepgemm` | `csrc/jit_kernels/impls/`, `deep_gemm/include/deep_gemm/` | Canonical FP8 block-scaled GEMM, grouped GEMM for MoE. |
| `tensorrt-llm` | `cpp/tensorrt_llm/kernels/quantization/`, `internal_cutlass_kernels/` | NVIDIA's FP8 / FP4 / INT8 GEMM and pre-quant kernels. |
| `cutlass` | `examples/54_hopper_fp8_*`, `examples/60_blackwell_*` | Reference Hopper / Blackwell FP8 / FP4 GEMM templates. |
| `vllm` | `csrc/quantization/` (`marlin`, `marlin_24`, `machete`, `awq`, `gptq`, `fp8`) | Multiple AWQ / GPTQ / FP8 design choices. |
| `sglang` | `python/sglang/srt/layers/quantization/`, `sgl-kernel/csrc/gemm/` | Production FP8 / FP4 / W8A8 wrappers. |

## Common optimization patterns

- **Block-scaled FP8**: 128x128 weight scale, 1x128 activation scale, scale
  tensors stored next to the data.
- **Per-channel + per-token scaling**: scales fused into the GEMM epilogue.
- **Weight-only INT4 (AWQ / GPTQ)**: dequant-on-the-fly into registers,
  matmul as FP16 / BF16. Skinny-batch decode is the common target.
- **Pre-quant fusion**: combine activation, quant, and scale into one kernel
  before the GEMM.

## Common bottlenecks

- Scale-tensor stride mismatch causes silent correctness drift.
- AWQ / GPTQ kernels are sensitive to the `group_size` / `M` ratio; benchmark
  across the full decode batch range.
- FP8 paths fall back to a slow path silently when alignment is missing.

## Recommended ncu metrics

- `sm__inst_executed_pipe_tensor.avg.pct_of_peak_sustained_elapsed`
- `dram__throughput.avg.pct_of_peak_sustained_elapsed`
- `lts__t_bytes.avg.pct_of_peak_sustained_elapsed`
- `smsp__inst_executed`
- `smsp__warp_issue_stalled_long_scoreboard.sum`
