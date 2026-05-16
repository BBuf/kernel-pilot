---
id: doc-tfla
title: "Tiled Flash Linear Attention (TFLA)"
url: https://arxiv.org/abs/2503.14376
source_category: paper
architectures: [sm100, sm90]
tags: [linear-attention, gated-delta-net, chunk-parallelism, tcgen05, wgmma]
retrieved_at: 2026-04-16
---

## Summary

Paper on Tiled Flash Linear Attention enabling arbitrarily large chunk sizes for linear attention.

## Key Techniques
- Two levels of sequence parallelism: standard chunkwise + tiling within chunks
- Prevents materialization of intermediate memory states
- Matmuls emitted as inline PTX: WGMMA on Hopper, tcgen05 on Blackwell
- Improves arithmetic intensity for linear attention variants including GatedDeltaNet
