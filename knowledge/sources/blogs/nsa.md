---
id: blog-nsa
title: "Native Sparse Attention (NSA)"
author: DeepSeek AI
url: https://arxiv.org/abs/2502.11089
source_category: benchmark-blog
architectures: [sm90, sm100]
tags: [sparse-attention, attention, triton, chunk-parallelism]
retrieved_at: 2026-04-16
---

## Summary

DeepSeek's natively trainable sparse attention with three parallel paths.

## Architecture
1. Token compression via learnable MLP (coarse-grained)
2. Token selection using blockwise importance scores (top-n fine-grained blocks)
3. Sliding window (w=512) for local context

## Key Techniques
- Hardware-aligned blockwise memory access
- Group-centric loading: shares sparse KV blocks across GQA group heads
- Triton kernel: grid-based loop scheduling
- 9x forward speedup, 6x backward at 64K sequences vs FlashAttention-2
- Deployed in DeepSeek-V3.2-Exp
