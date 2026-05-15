# DeepSeek TileKernels

Repository: <https://github.com/deepseek-ai/TileKernels>

Deep reference: `knowledge/references/source-guides/tilekernels.md`

TileKernels is DeepSeek's TileLang kernel library for LLM training and
inference operators such as MoE routing, quantization, transpose, fused
SwiGLU+quantization, and Engram kernels.

## Where the kernels live

| Directory | What you find there |
| --- | --- |
| `tile_kernels/` | TileLang kernel implementations. |
| `tests/` | Operator correctness and performance checks. |
| `README.md` | Feature list, supported operators, and packaging notes. |

## When to read this framework

- The user asks for DeepSeek TileLang / TileKernels.
- You need production-shaped TileLang examples for MoE routing, FP8/FP4
  quantization, transpose, or fused activation+quantization kernels.
- Two optimization rounds plateau and the next idea should come from a
  production TileLang codebase rather than generic tutorials.

## Reuse / Copy Rules

- TileKernels may seed a standalone TileLang candidate when license /
  attribution are handled.
- Record exact source path, commit, copied files, TileLang schedule parameters,
  and delta in the source ledger and lineage.
