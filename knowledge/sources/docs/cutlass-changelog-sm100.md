---
id: doc-cutlass-changelog-sm100
title: "CUTLASS Changelog: SM100/Blackwell Entries"
url: https://docs.nvidia.com/cutlass/latest/CHANGELOG.html
source_category: official-doc
architectures: [sm100, sm100a]
tags: [tcgen05, tmem, tma, clc, nvfp4, fp4, fp6, fp8, block-scale, warp-specialization, persistent-kernel, gemm, grouped-gemm, attention, moe, mla, 2sm-cooperative, tile-scheduling, cute-dsl, epilogue-fusion, sparse-attention]
retrieved_at: 2026-04-17
---

# CUTLASS Changelog: SM100/Blackwell Entries

## Overview

Comprehensive listing of all SM100 (Blackwell) related entries from the CUTLASS changelog, spanning from CUTLASS 3.8.0 (January 2025, first Blackwell support) through CUTLASS 4.5.0 (March 2026). The changelog tracks the rapid evolution of Blackwell kernel support including dense/sparse GEMM, blockscaled formats (NVFP4, MXFP4, MXFP6, MXFP8), MoE kernels, attention kernels, CuTe DSL, and the Cluster Launch Control scheduling system.

## CUTLASS 4.5.0 (2026-03-27)

- Added example 95 supporting "green context SM partition" enabling partial SM allocation for Blackwell kernels
- Fixed L2 capacity handling in Blackwell SM100/SM120 kernel templates
- Optimal code generation with CUDA toolkit 13.2

## CUTLASS 4.4.2 (2026-03-13)

- Fixed Hopper FMHA causal attention performance regression through mbarrier optimization
- Enabled SM120f compilation and NVFP4/MX Grouped GEMM in profiler

## CUTLASS 4.4.0 (2026-02-14)

- **GB300 support** via SM103 batched FP4 Ultra blockscaled GEMM kernel
- Introduced `cute.experimental` layer with fragment-free programming and automatic TMA descriptors
- Ahead of Time (AoT) compilation now available
- Added CopyDsmemStoreOp for distributed shared memory storage
- Support for customized epilogue fusion in persistent dense GEMM
- Multiple mixed input GEMM examples and performance improvements
- Fixed overlapping accumulator optimization for block tile N=256 in blockscaled GEMM

## CUTLASS 4.3.5 (2026-01-09)

- Fixed unexpected CPU overhead issue from previous release

## CUTLASS 4.3.4 (2025-12-22)

- Added PDL (Programmatic Dependent Launch) support via example kernel
- Fixed frame refcnt issue with cuda graph

## CUTLASS 4.3.1 (2025-11-26)

- Added SM103 support for CuTe DSL
- Merged multiple dependent DSOs into single DSO

## CUTLASS 4.3.0 (2025-11-21)

- Apache TVM-FFI support for reduced host runtime overhead
- FastDivmodDivisor with Python operator overloads and Cute dialect integration
- **L2 cache evict priority** for TMA operations
- Source location tracking for profiling/debugging correlation
- PTX and CUBIN code dumping capability
- Multiple Blackwell SM100 examples:
  - Persistent GEMM
  - Blockwise GEMM
  - Grouped GEMM variants
  - FMHA backward
  - Multi-head Latent Attention (MLA)
- Tutorial for Blackwell GEMM achieving **84% SOL performance with MNK 8K**
- Enhanced Blackwell SM100 Attention kernels with softmax skip correction
- Simplified MoE GEMM API with `MoEProblemShape` struct
- "GEMM_K = 0" support in grouped GEMM
- Blackwell SM100 convolution stream-K kernel support
- Blockscaled sparse kernel support in profiler

## CUTLASS 4.2.0 (2025-09-15)

- Support for Blackwell SM103 kernels for B300 GPUs with blockscaled datatypes
- New dispatch policies for collectives and kernel layers
- Blockscaled ultra FP4 dense and grouped GEMM examples
- Blackwell SM121 support for DGX Spark GPUs
- Further enhancement of SM100 Attention kernels
- **Blackwell SM100 fp4 GEMV kernel** support
- Blackwell SM100 legacy mixed input GEMM kernels
- Blackwell SM100 cpasync kernel support
- Mixed input blockscaled grouped GEMM on SM120
- Instantiation level support for SM100/SM103 kernels
- Fixed SM100/SM103 group GEMM kernel race check

## CUTLASS 4.1.0 (2025-07-16)

- Added aarch64 support for pip installation
- **Blackwell SM100 persistent dense blockscaled GEMM with static scheduling** example
- Blackwell Mamba2 SSD (State Space Decomposition) example

## CUTLASS 4.0.0 (2025-06-03)

- **CuTe DSL Python layer** centered around CuTe abstractions (major new feature)
- Blackwell SM100 persistent dense GEMM with static scheduling example
- Blackwell SM100 grouped GEMM example
- **Blackwell SM100 fused multi-head attention forward pass** example
- Support for Family Specific Architecture Features (100f, 101f, 120f)
- Improved blockwise and groupwise GEMMs on Hopper and Blackwell
- Blackwell SM100 SIMT packed fp32x2 kernels

## CUTLASS 3.9.0 (2025-04-24)

- Blackwell SM120 kernel support for GeForce GPUs
- Blockscaled GEMM with NVFP4 and mixed input examples
- Sparse blockscaled GEMM examples
- **Multi-head Latent Attention (MLA) for SM100** in FMHA example
- FMHA Backward kernel for SM100
- **Distributed GEMM** example for SM100 Blackwell
- Blockwise and groupwise GEMM support for Blackwell
- Grouped GEMM with blockwise/groupwise scaling for Blackwell

## CUTLASS 3.8.0 (2025-01-25) -- First Blackwell Release

- **5th generation Blackwell Tensor Core instructions (TCGen05)** via CuTe MMA atoms
- **Tensor Memory Accelerator (TMA)** extensions for Blackwell
- Exposure of **tmem** (tensor memory) as first-class data locale
- tmem<->rmem, rmem<->tmem, and smem<->tmem data movement instructions
- New narrow precision formats: FP4, FP6, FP8 and blockscaled variants NVFP4, MXFP4, MXFP6, MXFP8
- Blackwell-specific synchronization pipelines
- **Cluster Launch Control (CLC) API** supporting preferred and fallback cluster shapes
- Tile schedulers using CLC for dynamic persistence scheduling
- Full CUTLASS 3.x API support for SM100 kernels
- Five SM100 example categories demonstrating collective builders
- Mixed input GEMM kernel support for Hopper
- Grouped GEMM version 3.x for Hopper and Blackwell

## Key SM100 Examples by Number

| Example | Description |
|---------|-------------|
| 77 | Blackwell SM100 Attention kernels (enhanced multiple times) |
| 78 | Emulated BF16x9 GEMM |
| 82 | Distributed GEMM for SM100 |
| 83 | Sparse GEMM |
| 92 | MoE kernels for low-latency inference |
| 95 | Green context SM partition |
| 112 | State Space Decomposition (SSD) |

## Timeline Summary

- **Jan 2025** (3.8.0): First SM100 support, tcgen05, TMEM, CLC, FP4/FP6 formats
- **Apr 2025** (3.9.0): MLA, distributed GEMM, NVFP4, sparse blockscaled
- **Jun 2025** (4.0.0): CuTe DSL Python, persistent GEMM, FMHA
- **Jul 2025** (4.1.0): Blockscaled GEMM with static scheduling, Mamba2 SSD
- **Sep 2025** (4.2.0): SM103 (B300), GEMV, cpasync, SM121 (DGX Spark)
- **Nov 2025** (4.3.0): MoE API, stream-K convolution, 84% SOL tutorial
- **Feb 2026** (4.4.0): GB300, AoT compilation, cute.experimental, epilogue fusion
- **Mar 2026** (4.5.0): Green context, L2 fixes, CUDA 13.2 optimization
