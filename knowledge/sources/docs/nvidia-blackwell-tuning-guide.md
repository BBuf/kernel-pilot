---
id: doc-nvidia-tuning-guide
title: "NVIDIA Blackwell Tuning Guide"
url: https://docs.nvidia.com/cuda/blackwell-tuning-guide/
source_category: official-doc
architectures: [sm100, sm100a]
tags: [tcgen05, tmem, clc, tma, 2sm-cooperative, nvfp4, fp8, fp4, block-scale, pdl, gdc]
retrieved_at: 2026-04-16
---

# NVIDIA Blackwell Tuning Guide

## Overview

Official NVIDIA tuning guide for Blackwell (SM100/SM100a) GPU architectures. The primary reference for understanding Blackwell hardware features and their performance implications for kernel developers.

## Key Hardware Features

### tcgen05.mma (Tensor Core Generation 05)

Replaces Hopper's wgmma.mma_async. Fundamental changes:

- **Single-thread launch**: One thread issues the MMA instruction (vs warpgroup of 128 threads on Hopper)
- **CTA scope**: Operates at CTA level, not warpgroup level
- **Direct SMEM operand reads**: Operands read directly from shared memory -- no ldmatrix needed
- **TMEM accumulator output**: Results written to Tensor Memory, not registers
- **7 data type variants**: TF32, FP16/BF16, INT8, FP8 (E4M3/E5M2), FP6, FP4/NVFP4

Maximum MMA shapes:
| Configuration | Shape |
|---|---|
| 1-SM (1-CTA) | m128 x n256 x k16 (BF16) |
| 2-SM cooperative | m256 x n256 x k16 (BF16) |

7 variants: tf32, f16, i8, f8f6f4, mxf8f6f4.block_scale, mxf4.block_scale, mxf4nvf4.block_scale

### Tensor Memory (TMEM)

Dedicated 256KB per-SM memory for MMA accumulators:

- Layout: 128 rows x 512 columns x 32-bit elements
- Accessible only by the SM's tensor core unit
- Eliminates register pressure from large accumulator tiles
- 420 clock cycles end-to-end for cache-miss access (58% less than Hopper's 1000 cycles for register path)
- Best for multi-stage tensor pipelines with large working sets
- SMEM better for single-shot small-matrix operations
- Explicit alloc/dealloc lifecycle
- Power-of-2 column allocation (minimum 32)
- Data movement: tcgen05.st (reg->TMEM), tcgen05.ld (TMEM->reg), tcgen05.cp (SMEM->TMEM)

### Cluster Launch Control (CLC)

Hardware-level dynamic tile scheduling:

- Replaces static grid-based tile assignment
- Dynamically distributes tiles to available SMs
- Eliminates tail effects (last-wave underutilization)
- Enables persistent kernels without manual tile queue management
- `clusterlaunchcontrol.try_cancel` API for graceful termination
- Critical for grouped GEMM / MoE where group sizes vary

### TMA (Tensor Memory Accelerator)

Async bulk data movement engine (carried from Hopper, enhanced):

- Moves data from global -> shared memory without SM intervention
- 128-byte alignment requirement for descriptors
- Supports multicasting to multiple SMs in a cluster
- Pipelined with mbarrier for async producer-consumer

### 2-SM Cooperative MMA

Two SMs cooperate on a single larger MMA:

- Doubles effective M dimension (m256 vs m128)
- SMs share the output tile via TMEM
- Requires SMs to be in the same cluster
- Best for large GEMM tiles where single-SM MMA is not wide enough

### NVFP4 and Sub-Byte Data Types

Native tensor core support for narrow data types:

- **FP4 (E2M1)**: 4-bit float, representable values: 0, 0.5, 1, 1.5, 2, 3, 4, 6
- **FP6**: 6-bit float
- **FP8 (E4M3, E5M2)**: 8-bit float (carried from Hopper)
- **Block scaling**: Built into MMA instruction. Per-block UE8M0 scale factors.
- **NVFP4 block scale**: 16 FP4 elements share one FP8 E4M3 scale factor

### PDL (Programmatic Dependent Launch) / GDC (Grid Dependency Control)

- PDL enabled by default on Blackwell
- Overlaps dependent kernel launches
- GDC controls inter-kernel dependencies at grid level
- Reduces kernel launch gaps from ~5us to near-zero for dependent chains

## Hardware Specifications

| Feature | Value |
|---|---|
| Architecture | SM100a (B200) |
| SMs | 142 |
| Max warps/SM | 64 |
| 32-bit registers | 64K per SM |
| SMEM per SM | 228 KB |
| TMEM per SM | 256 KB (128 rows x 512 cols) |
| Max thread blocks/SM | 32 |
| Max cluster size | 8 (portable), 16 (opt-in) |
| L2 cache | 126 MB (B200) |
| HBM3e bandwidth | 8 TB/s |
| Peak FP16/BF16 tensor | ~2x Hopper |
| Peak FP4 tensor | ~4x Hopper |

## Performance Optimization Path

Demonstrated progression from the tcgen05 tutorial (Gau Nernst):

```
Naive (17% cuBLAS) -> 128B Swizzling (46%) -> Pipelining (62%)
-> Warp Specialization (80%) -> 2-SM MMA (86%)
-> Persistent Kernel + CLC (98% cuBLAS)
```

Each step addresses a specific bottleneck:
1. **Swizzling**: Eliminates shared memory bank conflicts
2. **Pipelining**: Overlaps TMA loads with compute
3. **Warp specialization**: Dedicated warps for TMA vs compute
4. **2-SM cooperative**: Larger effective tile for better reuse
5. **Persistent + CLC**: Eliminates tail effects and kernel launch overhead

## Hopper-to-Blackwell Migration Summary

| Aspect | Hopper (SM90) | Blackwell (SM100) |
|---|---|---|
| MMA instruction | wgmma.mma_async (warpgroup) | tcgen05.mma (single-thread, CTA) |
| MMA output | Registers | TMEM (256KB/SM) |
| Max BF16 MMA | m64n256k16 | m128n256k16 (1-CTA), m256n256k16 (2-CTA) |
| Matrix loading | ldmatrix to registers | Direct from SMEM |
| Synchronization | Warpgroup (4 warps) | Single thread, fully async |
| New data types | FP8 | FP4, FP6, FP8 with block scaling |
| Scaling | External (CUDA core promotion) | Native UE8M0 block scaling in MMA |
| Register pressure | High (accumulators in regs) | Low (accumulators in TMEM) |

## Sources

- [NVIDIA Blackwell Tuning Guide](https://docs.nvidia.com/cuda/blackwell-tuning-guide/)
- [Blackwell Architecture Whitepaper](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/)
