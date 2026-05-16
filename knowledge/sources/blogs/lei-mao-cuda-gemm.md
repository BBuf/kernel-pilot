---
id: blog-lei-mao-cuda-gemm
title: "Lei Mao CUDA GEMM Optimization Code Map"
author: Lei Mao
url: https://leimao.github.io/blog/CUDA-Programming/
source_category: community-note
architectures: [sm90, sm100, sm120]
tags: [coalescing, vectorized-loads, shared-memory-optimization, bank-conflicts, register-reuse, occupancy]
languages: [cuda-cpp]
kernel_types: [gemm]
retrieved_at: 2026-05-16
artifact_dir: evidence/blog-capsules/lei-mao-cuda-gemm
description: "Educational CUDA GEMM ladder with explicit kernel variants and benchmark helpers."
---

# Lei Mao CUDA GEMM Optimization Code Map

Use this source for staged CUDA C++ GEMM variants: coalescing, block tiling,
thread tiling, matrix-transposed tiles, warp tiling, WMMA, and benchmark
helpers.

## Companion Code

Repo: `leimao/CUDA-GEMM-Optimization`

Representative local artifact:

- `evidence/blog-capsules/lei-mao-cuda-gemm/source-snapshot/src/00_non_coalesced_global_memory_access.cu`

## Extraction Targets

| Kernel family | What to extract |
|---|---|
| v00/v01 | non-coalesced vs coalesced global access |
| 2D block tiling | shared-memory tiling and barrier placement |
| thread/warp tiling | per-thread reuse and register pressure tradeoff |
| transposed tiles | shared-memory layout and bank-conflict mitigation |
| WMMA | transition from scalar CUDA cores to tensor cores |

## Search Patterns

```bash
grep -R -E -n "coalesced|thread_tiling|warp_tiling|matrix_transpose|wmma|BLOCK_TILE|THREAD_TILE|profile" src include
```
