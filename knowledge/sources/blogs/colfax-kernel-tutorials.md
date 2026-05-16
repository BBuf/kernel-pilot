---
id: blog-colfax-kernel-tutorials
title: "Colfax Kernel Tutorial and Companion Code Map"
author: Colfax Research
url: https://research.colfax-intl.com/blog/
source_category: community-note
architectures: [sm90, sm100]
tags: [tma, wgmma, tcgen05, tmem, clc, block-scale, warp-specialization, persistent-kernel, tile-scheduling]
languages: [cuda-cpp, cute-dsl]
kernel_types: [gemm, attention, flash-attention]
retrieved_at: 2026-05-16
artifact_dir: evidence/blog-capsules/colfax-kernel-tutorials
description: "Article-to-code map for Colfax CUTLASS/CuTe tutorials; includes a small verbatim TMA code artifact."
---

# Colfax Kernel Tutorial and Companion Code Map

Use this source when an optimization question needs article-backed CUTLASS/CuTe
implementation detail.

## Read For

| Topic | Article family |
|---|---|
| Hopper TMA/WGMMA | TMA tutorial, WGMMA tutorial, pipelined GEMM, Stream-K |
| Blackwell GEMM | Tensor Memory GEMM, thread-block clusters, sub-byte GEMM, block scaling |
| Scheduling | Dynamic persistent tile scheduling with Cluster Launch Control |
| Attention | FlashAttention-4 and FlexAttention/CuTe DSL articles |

## Companion Code

Primary repos:

- `ColfaxResearch/cfx-article-src`
- `ColfaxResearch/cutlass-kernels`

Representative local artifact:

- `evidence/blog-capsules/colfax-kernel-tutorials/source-snapshot/cfx-article-src/tma/main.cu`

## Search Patterns

```bash
grep -R -E -n "TMA|WGMMA|StreamK|persistent|Cluster|CLC|mbarrier|CollectiveBuilder|Tensor Memory|block scaling|FlashAttention|FlexAttention" .
```
