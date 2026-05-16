---
id: blog-vllm-deepseek-v3-sparse
title: "DeepSeek-V3.2-Exp in vLLM: Fine-Grained Sparse Attention in Action"
author: vLLM Team
url: https://blog.vllm.ai/2025/09/29/deepseek-v3-2.html
source_category: community-note
architectures: [sm100, sm100a]
tags: [sparse-attention, mla, attention, flash-attention, decode, prefill, fp8, quantization, kernel-fusion]
retrieved_at: 2026-04-17
---

# DeepSeek-V3.2-Exp in vLLM: Fine-Grained Sparse Attention in Action

## Overview

The vLLM team's Day 0 support blog for DeepSeek-V3.2-Exp, the first major model to deploy DeepSeek Sparse Attention (DSA) -- a two-stage sparse attention mechanism that selects only the top 2,048 most relevant tokens per query position rather than attending to full context. The blog details the vLLM implementation including the lightning indexer, FP8 KV cache quantization, and deployment configurations across Hopper and Blackwell hardware.

## Sparse Attention Architecture: DeepSeek Sparse Attention (DSA)

DSA implements a two-stage process for long-context efficiency:

### Stage 1: Lightning Indexer
- Computes relevance logits between query tokens and cached context
- Applies per-head weighting to logits
- Performs row-wise top-K selection to identify the 2,048 most relevant positions
- Maintains separate K-cache buffers specifically for indexing operations
- Operates independently during prefill vs decode phases due to different batching requirements

### Stage 2: Fine-Grained Token Selection
- Selected tokens are fed to the standard MLA attention kernel
- Only attends to the top-2,048 tokens instead of full context
- Dramatically reduces compute for long sequences while maintaining accuracy

## KV Cache Structure and Quantization

The implementation uses FP8 quantization for the KV cache:

- **MLA cache**: 656 bytes per token
  - 512 bytes quantized content
  - 16 bytes scales
  - 128 bytes unquantized RoPE component
- **Indexer cache**: Per-block storage with interleaved values and scaling factors
- **Block size**: Fixed at 64 tokens (required for FlashMLA kernel compatibility)

## Hardware Requirements

Minimum supported configurations:
- 16x H100 GPUs
- 8x H200 GPUs
- 8x B200 GPUs (Blackwell architecture -- Day 0 support)

Out-of-the-box Blackwell support enables direct execution on B200 and GB200 accelerators.

## Deployment Configuration

Recommended deployment uses expert parallelism / data parallelism mode:
```
DP=8, EP=8, TP=1
```

Kernels are primarily optimized for TP=1, so EP/DP mode is preferred over tensor parallelism for this model.

Basic launch command:
```
vllm serve deepseek-ai/DeepSeek-V3.2-Exp --tensor-parallel-size 8
```

## Implementation Details

### Kernel Integration
- Fused top-K kernels leveraging TileLang references for the lightning indexer
- DeepGEMM CUDA kernels for indexer compute operations
- FlashMLA sparse attention kernel for the actual attention computation
- FP8 quantization applied during cache writes to vLLM's page table system

### Accuracy Validation
- Validated against official results on GSM8K and GPQA-Diamond benchmarks
- Matched V3.1-Terminus performance on standard benchmarks
- Hadamard transforms removed with no observed accuracy impact

## Known Limitations

- Block size restricted to 64 tokens
- Expert parallelism temporarily disabled (unresolved bugs)
- Logits tensor materialization issues at high batch sizes with extended contexts
- Currently limited to NVIDIA Hopper and Blackwell datacenter GPUs

## Significance

This deployment demonstrates that sparse attention can be practically integrated into production serving frameworks. The reduction from full-context to top-2,048 attention enables up to 50% cost reduction for long-context API calls while maintaining model quality. Blackwell's higher memory bandwidth (8 TB/s on B200) particularly benefits the indexer phase which is memory-bound.
