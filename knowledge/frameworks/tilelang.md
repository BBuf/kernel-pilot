# TileLang

Repository: <https://github.com/tile-ai/tilelang>

TileLang is a tile-level DSL for GPU kernels with a Python-frontend schedule
language. It serves as a higher-level reference for "what schedule would I
write if I were optimizing this kernel by hand".

## Where the kernels live

| Path | What you find there |
| --- | --- |
| `examples/` | Matmul, attention, flash-attention, fused-MoE example schedules. |
| `python/tilelang/` | Frontend, schedule primitives, codegen entry points. |

## When to read this framework

- You want a quick schedule-language sketch of a candidate kernel before
  committing to Triton or CUDA C++.
- You are designing an autotuner-friendly Triton kernel and want a tile-DSL
  reference for the schedule space.

## When NOT to copy

- TileLang kernels are usable as **inspiration / hypothesis source**, not as
  direct candidate code unless license / attribution is handled.
