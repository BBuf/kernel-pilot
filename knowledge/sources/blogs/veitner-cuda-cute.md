---
id: blog-veitner-cuda-cute
title: "Veitner CUDA, CuTe DSL, PTX, and Sequence Kernel Notes"
author: Simon Veitner
url: https://veitner.bearblog.dev/blog/
source_category: community-note
architectures: [sm90, sm100]
tags: [tma, wgmma, tcgen05, nvfp4, block-scale, swizzling, bank-conflicts, ldmatrix, stmatrix, warp-specialization]
languages: [cuda-cpp, cute-dsl, ptx]
kernel_types: [gemm, gemv, gated-delta-net, fused-kernel]
retrieved_at: 2026-05-16
artifact_dir: evidence/blog-capsules/veitner-cuda-cute
description: "Practical Hopper/Blackwell blog and code map covering CuTe DSL, TMA/WGMMA, swizzling, PTX load/store, reductions, NVFP4, and GDN."
---

# Veitner CUDA, CuTe DSL, PTX, and Sequence Kernel Notes

Use this source for practical code-oriented Hopper/Blackwell posts that connect
CuTe DSL, TMA/WGMMA, PTX load/store fragments, swizzling, reductions, NVFP4, and
Gated Delta Net kernels.

## Companion Code

- `simveit/effective_transpose`
- `simveit/load_and_store`
- `gist.github.com/simveit`

Representative local artifact:

- `evidence/blog-capsules/veitner-cuda-cute/source-snapshot/effective_transpose/transpose_swizzle.cu`

## Search Patterns

```bash
grep -R -E -n "TMA|WGMMA|cp_async_bulk|mbarrier|swizzle|transpose|RMSNorm|NVFP4|blockscaled|GDN|ldmatrix|stmatrix" .
```
