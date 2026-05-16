---
id: blog-qwen3-next-architecture
title: "Qwen3-Next: Hybrid GDN+MoE Architecture on NVIDIA Blackwell"
author: NVIDIA / Alibaba
url: https://developer.nvidia.com/blog/new-open-source-qwen3-next-models-preview-hybrid-moe-architecture-delivering-improved-accuracy-and-accelerated-parallel-processing-across-nvidia-platform/
source_category: community-note
architectures: [sm100, sm100a]
tags: [gated-delta-net, moe, linear-attention, attention, sparse-attention, cluster]
retrieved_at: 2026-04-17
---

# Qwen3-Next: Hybrid GDN+MoE Architecture on NVIDIA Blackwell

## Overview

NVIDIA and Alibaba's joint announcement of the Qwen3-Next model family, featuring a novel hybrid architecture combining Gated Delta Networks (GDN) with ultra-sparse Mixture of Experts (MoE). The 80B-parameter models activate only 3B parameters per token (3.7% activation ratio), using GDN for 75% of attention layers and GQA for the remaining 25%. This architecture is optimized for NVIDIA Blackwell, leveraging NVLink bandwidth for expert routing and supporting 260K+ token context lengths.

## Model Structure

### Parameter Efficiency
- **Total parameters**: 80B
- **Active per token**: 3B (3.7% activation ratio)
- **Variants**: Qwen3-Next 80B-A3B-Thinking, Qwen3-Next 80B-A3B-Instruct

### Expert Configuration
- 512 routed experts + 1 shared expert
- 10 experts activated per token
- Ultra-sparse design dramatically reduces per-token compute cost

## Hybrid Attention Mechanism

### Layer Design
The architecture uses a strategic alternating pattern across 48 layers:
- **75% of layers (36 layers)**: Gated DeltaNet (GDN) linear attention
- **25% of layers (12 layers)**: Every 4th layer uses standard GQA attention

### Gated DeltaNet (GDN) Integration
GDN, from NVIDIA Research and MIT, replaces standard softmax attention with a linear attention mechanism that:
- Processes sequences with memory and computation scaling almost linearly with sequence length
- Improves focus on relevant parts of long sequences without forgetting key information
- Enables efficient processing of 260K+ token contexts
- Eliminates the quadratic attention bottleneck for the majority of layers

The combination of GDN (efficient long-range) with periodic GQA layers (precise short-range) balances efficiency with the expressiveness of full attention.

## NVIDIA Blackwell Optimization

### NVLink Bandwidth for Expert Routing
Blackwell's 5th-generation NVLink provides 1.8 TB/s of direct GPU-to-GPU bandwidth, which is critical for:
- Minimizing latency during expert routing in the MoE layers
- All-to-all communication for dispatching tokens to expert-owning GPUs
- Directly translating to faster inference and higher token throughput

### Inference Framework Support
Deployment available through:
- NVIDIA NIM microservices
- SGLang
- vLLM

Models available for testing on build.NVIDIA.com and for download on Hugging Face.

## Architecture Significance

### Why Hybrid GDN+MoE Matters for Kernels
The architecture creates distinct kernel requirements:
1. **GDN layers**: Require efficient linear attention kernels (similar to Mamba/state-space models) that avoid materializing the full attention matrix
2. **GQA layers**: Standard grouped-query attention kernels (FlashAttention/FlashMLA compatible)
3. **MoE layers**: Expert-parallel GEMM kernels with efficient token routing
4. **Expert dispatch**: All-to-all communication kernels leveraging NVLink

### Context Length Scaling
The linear-time GDN layers enable 260K+ token processing without the quadratic memory/compute growth of full attention. Only the periodic GQA layers incur quadratic cost, and these can use sparse attention or sliding window techniques to manage long contexts.

## Comparison with Dense Models
- 80B total parameters but only 3B active: comparable inference cost to a 3B dense model
- 512 experts provide massive parameter capacity for knowledge storage
- GDN enables linear-time sequence processing for majority of layers
- Represents convergence of three efficiency techniques: sparse MoE, linear attention, and hardware-aware expert routing
