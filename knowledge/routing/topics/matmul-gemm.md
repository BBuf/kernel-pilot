# Topic: GEMM / Tensor-Core matmul

## What it covers

Dense matmul kernels including dense FP16 / BF16 GEMM, FP8 / FP4 GEMM,
block-scaled GEMM, grouped GEMM, GEMV (skinny matmul), Stream-K / Split-K,
fused epilogues (bias, residual, activation, dequant).

## Per-framework references

| Framework | Where to look | What it teaches |
| --- | --- | --- |
| `cutlass` | `include/cutlass/gemm/`, `examples/48_hopper_*`, `examples/60_*`, `tools/profiler/` | The canonical Hopper / Blackwell GEMM templates with TMA + WGMMA. |
| `deepgemm` | `csrc/jit_kernels/impls/`, `deep_gemm/include/deep_gemm/` | FP8 block-scaled GEMM, grouped GEMM, JIT heuristics. |
| `tensorrt-llm` | `cpp/tensorrt_llm/kernels/cutlass_kernels/`, `internal_cutlass_kernels/` | NVIDIA's CUTLASS variants for FP8 / FP4 / INT8. |
| `triton` | `python/tutorials/03-matrix-multiplication.py`, `python/tutorials/09-persistent-matmul.py` | Block-pointer + autotune matmul reference. |
| `tilelang` | `examples/`, `examples/deepseek_mla/`, `benchmark/` | Tile-level GEMM and attention schedules that are easy to mutate. |
| `cute-dsl` | `cutlass/python/`, `examples/48_hopper_*`, `examples/60_*` | Python CuTe DSL scheduling and generated kernel structure. |
| `quack` | `quack/`, `benchmarks/`, `microbenchmarks/` | Tri Dao CuTe DSL GEMM and microbenchmark patterns. |
| `tilekernels` | `tile_kernels/`, `tests/` | DeepSeek TileLang kernels for quantization, transpose, MoE movement, and fused ops. |
| `cuda-blog-kernels` | `NVIDIA-developer-blog/code-samples`, `siboehm/SGEMM_CUDA`, `leimao/CUDA-GEMM-Optimization` | Classic CUDA blog-to-code optimization ladders. |
| `veitner-blog` | `veitner.bearblog.dev/blog/`, `simveit/effective_transpose` | CuTe DSL SGEMM, persistent GEMM, block-scaled GEMM, TMA/swizzle experiments. |
| `colfax-research` | `research.colfax-intl.com/blog/`, `ColfaxResearch/cfx-article-src`, `ColfaxResearch/cutlass-kernels` | CUTLASS/CuTe Hopper and Blackwell GEMM tutorials with companion code. |
| `sglang` | `sgl-kernel/csrc/gemm/` | Production FP8 / FP4 GEMM wrappers. |
| `vllm` | `csrc/quantization/` (marlin / machete) | Skinny-K decode GEMM for AWQ / GPTQ. |
| `pytorch` | `aten/src/ATen/native/cuda/Blas.cpp`, `torch/_inductor/kernel/mm.py` | cuBLAS / Inductor matmul as a baseline. |
| `thunderkittens` | `examples/matmul/` | Tile-primitive warpgroup matmul. |

## Common optimization patterns

- Hopper TMA loads with warpgroup-specialized producer / consumer.
- Persistent kernel grid (one CTA per SM, loops over output tiles).
- Stream-K for low-batch or skinny-K shapes.
- Fused epilogue: bias + activation + residual + dequant in one pass.
- Block-scaled FP8: 128x128 weight scale, 1x128 activation scale (Hopper).
- Cluster-launched cooperative GEMM on Hopper / Blackwell.

## Common bottlenecks

- Skinny-K decode is memory-bound; tensor pipe underutilized.
- Tail batches in grouped GEMM cause SM imbalance; use Stream-K or padding.
- Epilogue dominates total time when activation / dequant is heavy; fuse it.

## Recommended ncu metrics

- `sm__inst_executed_pipe_tensor.avg.pct_of_peak_sustained_elapsed`
- `dram__throughput.avg.pct_of_peak_sustained_elapsed`
- `lts__t_bytes.avg.pct_of_peak_sustained_elapsed`
- `smsp__sass_average_data_bytes_per_sector_mem_global_op_ld.pct_of_peak_sustained_elapsed`
- `sm__cycles_active.avg.pct_of_peak_sustained_elapsed`
