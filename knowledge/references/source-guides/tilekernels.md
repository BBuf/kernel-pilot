# DeepSeek TileKernels Deep Reference

Repository: <https://github.com/deepseek-ai/TileKernels>

Source-only policy: do not query PR notes for this repository. Public PR
history is sparse; inspect `tile_kernels/`, `tests/`, and the current source
tree directly.

Use this when the target is a DeepSeek-style TileLang kernel, or when plateau
research needs production TileLang ideas for MoE routing, quantization,
transpose, fused SwiGLU+quantization, or Engram kernels.

## Read Order

1. README feature list and package constraints.
2. Operator implementation under `tile_kernels/`.
3. Matching tests under `tests/`.
4. TileLang runtime/lowering details in `tile-ai/tilelang` if the schedule is
   unclear.
5. Benchmark or profiling commands from the test harness.

## Code Map By Kernel Type

| Kernel type | Paths to inspect | What to extract |
| --- | --- |
| MoE routing/scoring | `tile_kernels/moe/{topk_gate_kernel.py,top2_sum_gate_kernel.py,topk_sum_and_topk_group_idx_kernel.py,scoring.py}`, `tests/moe/` | top-k routing, score normalization, grouped index construction |
| MoE movement/reduction | `tile_kernels/moe/{expand_to_fused_kernel.py,reduce_fused_kernel.py,get_fused_mapping_kernel.py,group_count_kernel.py,mask_indices_by_tp_kernel.py}`, matching tests | token expansion/reduction, expert grouping, TP masking |
| Quant casts | `tile_kernels/quant/{per_token_cast_kernel.py,per_channel_cast_kernel.py,per_block_cast_kernel.py,cast_back_kernel.py,cast_back_e5m6_kernel.py}`, `tests/quant/` | scale shape, e5m6/fp8 conversion, per-token/channel/block layout |
| Fused activation + quant | `tile_kernels/quant/swiglu_*_cast*_kernel.py`, `tile_kernels/torch/swiglu.py`, matching tests | fused SwiGLU forward/backward with cast and transpose |
| Transpose | `tile_kernels/transpose/batched_transpose_kernel.py`, `tests/transpose/test_transpose.py` | batched layout movement and validation |
| Engram kernels | `tile_kernels/engram/*_kernel.py`, `tests/engram/` | gate/hash/grad/fused-weight kernels |
| MHC kernels | `tile_kernels/mhc/*_kernel.py`, `tests/mhc/` | model-specific fused pre/post/norm/sinkhorn kernels |
| Torch wrappers | `tile_kernels/torch/*.py` | Python API contract and baseline semantics |
| Testing/bench | `tile_kernels/testing/{bench.py,generator.py,numeric.py,quant.py}`, `tests/pytest_*_plugin.py` | benchmark harness, random generators, numeric oracle |

## Search Patterns

```bash
rg -n "moe|routing|topk|quant|fp8|fp4|e5m6|swiglu|transpose|engram|rms|norm" tile_kernels tests
rg -n "TileLang|T\\.|pipeline|block|thread|shared|fragment|autotune" tile_kernels tests README.md
```

## Candidate Use

- TileKernels can seed standalone TileLang candidates when license /
  attribution are handled.
- Record exact commit, source path, copied files, TileLang schedule parameters,
  tests copied or adapted, and first delta.
- Prefer one operator at a time; TileKernels combines several LLM kernel
  families and can otherwise sprawl.

## NCU Focus

| Kernel family | First metrics |
| --- | --- |
| MoE routing | branch divergence, memory traffic, atomics, active cycles |
| Quantization | DRAM throughput, vectorization, global sectors, ALU pipe % |
| Transpose / data movement | coalescing, shared bank conflicts, L2/DRAM bytes |
