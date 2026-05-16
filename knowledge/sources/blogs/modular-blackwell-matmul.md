---
id: blog-modular-blackwell
title: "Modular: Matrix Multiplication on Blackwell"
author: Modular
url: https://www.modular.com/blog/matrix-multiplication-on-nvidias-blackwell-part-1-introduction
source_category: community-note
architectures: [sm100, sm100a]
tags: [gemm, tcgen05, tmem, tma, 2sm-cooperative, pipeline-stages, tma-multicast, clc]
techniques: [pipeline-stages, tma-multicast, warp-specialization, double-buffering]
hardware_features: [tcgen05, tmem, tma, 2sm-cooperative, clc]
kernel_types: [gemm]
languages: [cuda-cpp]
retrieved_at: 2026-04-16
---

# Modular: Matrix Multiplication on Blackwell

## Overview

Multi-part blog series from Modular on building a high-performance GEMM kernel for Blackwell GPUs. The series provides a clear optimization progression, reaching 85% of SOTA performance with documented techniques at each step.

**Part 1**: [Introduction](https://www.modular.com/blog/matrix-multiplication-on-nvidias-blackwell-part-1-introduction)
**Part 3**: [The Optimizations Behind 85% of SOTA Performance](https://www.modular.com/blog/matrix-multiplication-on-nvidias-blackwell-part-3-the-optimizations-behind-85-of-sota-performance)

## Key Techniques

### TMA Multicasting

TMA can deliver the same data to multiple SMs in a cluster simultaneously:

```
// Without multicast: each SM loads its own copy of shared tiles
// With multicast: TMA loads once, broadcasts to N SMs

// Example: B matrix tile shared across M-dimension SMs
// If cluster has 4 SMs along M dimension:
// - Without multicast: 4 separate global memory reads
// - With multicast: 1 read, hardware broadcasts to 4 SMs
// 4x reduction in global memory bandwidth for B tiles
```

TMA multicasting is particularly effective for GEMM where the B matrix tile is shared across the M dimension of the output.

### 2-SM Cooperative MMA

Two SMs cooperate on a single m256 x n256 x k16 tile:

```
// Single SM: m128 x n256 x k16 = 128 * 256 * 16 * 2 = 1M FLOPs per MMA
// 2-SM:      m256 x n256 x k16 = 256 * 256 * 16 * 2 = 2M FLOPs per MMA

// Benefits:
// 1. Doubled M dimension -> better data reuse for A tile
// 2. Larger output tile -> fewer tiles needed for full GEMM
// 3. Both SMs share B tile (loaded once via TMA multicast)
```

### 5-Stage Circular Buffer Pipeline

Multi-stage software pipeline for overlapping TMA loads with compute:

```
// 5 SMEM buffer slots:
// Slot 0: being consumed by tcgen05.mma (current compute)
// Slot 1: data ready, waiting for compute
// Slot 2: TMA load in progress
// Slot 3: TMA load issued, waiting for completion
// Slot 4: free, ready for next TMA load

// Deeper pipeline (5 vs 2-3) hides more memory latency
// Critical for large K dimensions where many tiles must stream through
```

The 5-stage depth is deeper than the typical 2-3 stages used in simpler implementations, providing better latency hiding at the cost of more shared memory for buffers.

### Optimization Progression

The Modular blog documents a clear progression:

| Step | Technique | Approximate % SOTA |
|------|-----------|-------------------|
| 1 | Basic tcgen05.mma | ~20% |
| 2 | Swizzled SMEM layout | ~45% |
| 3 | TMA async pipeline (5-stage) | ~60% |
| 4 | Warp specialization | ~70% |
| 5 | 2-SM cooperative + TMA multicast | ~85% |

The remaining 15% gap to SOTA (cuBLAS / CUTLASS persistent) comes from:
- Persistent kernel with CLC scheduling
- Fine-tuned tile sizes for specific problem shapes
- Advanced register allocation and instruction scheduling

## Key Insights

1. **TMA multicast reduces bandwidth pressure**: For GEMM, the B matrix tile can be multicast to all SMs processing different M rows. This is a free bandwidth reduction that requires only cluster configuration.

2. **5-stage pipeline is optimal for B200**: The B200's 8 TB/s bandwidth and deep memory hierarchy benefit from deeper pipelines. Shallower pipelines (2-3 stages) leave performance on the table.

3. **85% without persistence**: Notably, 85% of SOTA is achievable without persistent kernels or CLC. This makes non-persistent kernels viable for many use cases where simplicity is preferred.

4. **Clear optimization ordering**: The series demonstrates that optimizations should be applied in order of impact: swizzling > pipelining > warp specialization > 2-SM cooperative. Attempting later optimizations without earlier ones yields minimal benefit.

## Sources

- [Part 1: Introduction](https://www.modular.com/blog/matrix-multiplication-on-nvidias-blackwell-part-1-introduction)
- [Part 3: 85% of SOTA](https://www.modular.com/blog/matrix-multiplication-on-nvidias-blackwell-part-3-the-optimizations-behind-85-of-sota-performance)
