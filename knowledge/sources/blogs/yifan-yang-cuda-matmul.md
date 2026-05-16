---
id: blog-yifan-yang-cuda-matmul
title: "Yifan Yang CUDA Matmul Roofline and Register Tiling Notes"
author: Yifan Yang
url: https://yang-yifan.github.io/blogs/reg_tile/reg_tile.html
source_category: community-note
architectures: [sm90, sm100, sm120]
tags: [roofline, register-reuse, occupancy, shared-memory-optimization, coalescing]
languages: [cuda-cpp]
kernel_types: [gemm]
retrieved_at: 2026-05-16
description: "Reasoning source for register tiling, throughput modeling, and roofline-style CUDA matmul analysis."
---

# Yifan Yang CUDA Matmul Roofline and Register Tiling Notes

Use this source for reasoning about why register tiling and throughput modeling
matter in hand-written CUDA matmul.

## Read For

| Question | What to extract |
|---|---|
| Why shared-memory tiling alone is insufficient | arithmetic intensity and memory-bandwidth argument |
| How to choose register tile size | per-thread work, register reuse, and occupancy tradeoff |
| How to use roofline thinking | target bandwidth/throughput and where the kernel falls short |
| When to stop optimizing naive CUDA GEMM | compare against tensor-core/CUTLASS paths and expected ceiling |

## Use With

- `blog-simon-boehm-sgemm` for the full code ladder.
- `blog-lei-mao-cuda-gemm` for staged CUDA C++ variants.
- CUTLASS/CuTe PR evidence when the target should move to tensor cores, TMA, or tcgen05.
