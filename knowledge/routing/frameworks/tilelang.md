# TileLang

Repository: <https://github.com/tile-ai/tilelang>

Deep reference: `knowledge/references/source-guides/tilelang.md`

TileLang is a tile-level DSL for GPU kernels with a Python-frontend schedule
language. It serves as a higher-level reference for "what schedule would I
write if I were optimizing this kernel by hand".

## Where the kernels live

| Path | What you find there |
| --- | --- |
| `examples/` | Matmul, attention, flash-attention, fused-MoE, MLA, and tutorial schedules. |
| `python/tilelang/` | Frontend, language, engine, schedule primitives, codegen entry points. |
| `tests/` | DSL behavior, lowering, and correctness tests. |
| `benchmark/` | Benchmark harnesses and sweep examples. |

## When to read this framework

- You want a quick schedule-language sketch of a candidate kernel before
  committing to Triton or CUDA C++.
- You are designing an autotuner-friendly Triton kernel and want a tile-DSL
  reference for the schedule space.

## Reuse / Copy Rules

- TileLang kernels are usable as direct candidate code when the user requests
  TileLang or the baseline is TileLang, provided license / attribution is
  handled.
- If copying or adapting a TileLang baseline, record the exact source, commit,
  copied files, and delta in the source ledger and lineage.
