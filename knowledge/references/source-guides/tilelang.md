# TileLang Deep Reference

Repository: <https://github.com/tile-ai/tilelang>

PR case notes: `../prs/tilelang.md`

Use this when a user asks for TileLang, when the baseline is TileLang, or when a
CUDA/Triton/CuTe candidate needs a tile-schedule sketch before implementation.

## Read Order

1. Example closest to the operator.
2. Language primitives and schedule annotations.
3. Autotune / benchmark utilities.
4. Generated CUDA or lowered IR if available.
5. Tests covering the same layout and dtype.

## Code Map By Kernel Type

| Kernel type | Paths to inspect | What to extract |
| --- | --- |
| GEMM | `examples/gemm/`, `examples/gemm_fp8/`, `examples/gemm_int4/`, `examples/gemm_sm100/`, `examples/gemm_splitk/`, `examples/gemm_streamk/`, `benchmark/matmul/`, `benchmark/matmul_fp8/` | dense/low-precision/split-K/Stream-K schedule examples and sweep harnesses |
| Block-scaled / dequant GEMM | `examples/blockscaled_gemm_sm100/`, `examples/dequantize_gemm/`, `examples/deepseek_deepgemm/` | MXFP8/MXFP4/block-scale layouts and dequantized matmul |
| Attention / decode | `examples/flash_attention/`, `examples/flash_attention_sm100/`, `examples/flash_decoding/`, `examples/blocksparse_attention/`, `benchmark/blocksparse_attention/` | dense/sparse attention, decode variants, Triton comparison harnesses |
| DeepSeek attention | `examples/deepseek_mla/`, `examples/deepseek_nsa/`, `examples/deepseek_v32/`, `examples/deepseek_v4/` | MLA/NSA/sparse attention and DeepSeek-specific shape contracts |
| MoE / fused ops | `examples/fusedmoe/`, `examples/grouped_gemm/`, `examples/topk/`, `examples/cast/` | grouped GEMM, routing/top-k, cast/quant schedule |
| Norm / elementwise | `examples/norm/`, `examples/elementwise/`, `examples/hadamard_transform/`, `examples/online_softmax/` | memory-bound fused ops and reductions |
| Sequence kernels | `examples/gdn/`, `examples/linear_attention/`, `examples/mamba2/`, `benchmark/mamba2/` | recurrent/linear attention style schedule references |
| Language/compiler | `python/tilelang/`, `docs/programming_guides/`, `docs/compiler_internals/`, `docs/runtime_internals/` | primitives, lowering behavior, autotune, debug/profiling knobs |
| Tests/benchmarks | `tests/`, example `test_*.py`, `benchmark/` | correctness coverage and performance harnesses |

## Search Patterns

```bash
rg -n "GEMM|matmul|attention|flash|moe|rms|norm|quant|transpose|pipeline|swizzle|autotune" examples python tests
rg -n "T\\.copy|T\\.gemm|T\\.alloc|thread_binding|shared|fragment|num_stages|block_M|block_N|block_K" examples python tests
```

## Candidate Use

- TileLang kernels may be copied/adapted into the standalone repo when license /
  attribution are handled.
- Record Python package version or commit, source path, schedule parameters,
  generated backend if inspected, and deltas.
- Keep a baseline-vs-candidate harness because TileLang performance depends on
  lowering, autotune, and runtime environment.

## NCU Focus

| Kernel family | First metrics |
| --- | --- |
| GEMM / attention | tensor pipe %, L2/DRAM bytes, shared-memory pressure, occupancy |
| Memory-bound fused ops | DRAM throughput, global sectors, bank conflicts, issue stalls |
| Autotuned variants | chosen config, compile time, p50 latency, occupancy/register tradeoff |
