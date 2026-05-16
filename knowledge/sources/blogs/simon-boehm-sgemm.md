---
id: blog-simon-boehm-sgemm
title: "Simon Boehm SGEMM Optimization Ladder"
author: Simon Boehm
url: https://siboehm.com/articles/22/CUDA-MMM
source_category: benchmark-blog
architectures: [sm90, sm100, sm120]
tags: [coalescing, vectorized-loads, shared-memory-optimization, bank-conflicts, double-buffering, register-reuse, roofline]
languages: [cuda-cpp]
kernel_types: [gemm]
retrieved_at: 2026-05-16
artifact_dir: evidence/blog-capsules/simon-boehm-sgemm
description: "Stepwise CUDA SGEMM optimization ladder with representative verbatim kernel artifacts."
---

# Simon Boehm SGEMM Optimization Ladder

Use this source when the agent needs a clean CUDA C++ GEMM optimization ladder
before moving to CUTLASS, CuTe, Triton, or TileLang.

## Local Artifacts

- `evidence/blog-capsules/simon-boehm-sgemm/source-snapshot/src/kernels/1_naive.cuh`
- `evidence/blog-capsules/simon-boehm-sgemm/source-snapshot/src/kernels/6_kernel_vectorize.cuh`
- `evidence/blog-capsules/simon-boehm-sgemm/source-snapshot/src/kernels/12_kernel_double_buffering.cuh`

## Ladder

| Step | Idea |
|---|---|
| 1 | naive one thread per C element |
| 2 | coalesced global memory access |
| 3 | shared-memory blocking |
| 4-5 | 1D/2D block tiling |
| 6 | vectorized memory access |
| 7-8 | bank-conflict mitigation and padded shared tile |
| 9 | autotuned parameters |
| 10 | warp tiling |
| 11-12 | double buffering |

## Search Patterns

```bash
grep -R -E -n "sgemm|coalesce|shared|vector|bank|warptiling|double|BM|BN|BK|TM|TN" src scripts README.md
```
