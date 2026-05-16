---
id: blog-jax-pallas-blackwell-matmul
title: "Writing High-Performance Matrix Multiplication Kernels for Blackwell with JAX Pallas"
author: JAX Team (Google)
url: https://docs.jax.dev/en/latest/pallas/gpu/blackwell_matmul.html
source_category: community-note
architectures: [sm100]
tags: [gemm, warp-specialization, 2sm-cooperative, persistent-kernel, tma, tmem, pipeline-stages, swizzling, jax-pallas, tcgen05, double-buffering, epilogue-fusion]
retrieved_at: 2026-04-17
---

# Writing High-Performance Matrix Multiplication Kernels for Blackwell with JAX Pallas

## Overview

The official JAX Pallas tutorial for writing high-performance matrix multiplication kernels targeting NVIDIA Blackwell GPUs. The tutorial demonstrates incremental optimization from a basic 37.6% tensor core utilization kernel to a grid-tiled implementation achieving 109.6% of cuBLAS performance (69.4% absolute TC utilization). Six optimization stages are covered: warp specialization, tiled epilogue, collective 2CTA MMA, persistent kernels, dedicated epilogue warpgroups, and grid tiling. All benchmarks use float16 inputs with m=4096, k=4096, n=8192.

## Performance Progression

| Implementation | TC Utilization | vs cuBLAS |
|---|---|---|
| Basic single-CTA kernel | 37.62% | 59.4% |
| Warp specialization | 45.47% | 71.7% |
| Tiled epilogue | 55.82% | 88.1% |
| Collective 2CTA MMA | 59.41% | 93.7% |
| Persistent kernel | 61.46% | 97.0% |
| Dedicated epilogue warpgroup | 63.38% | 100.0% |
| Grid tiling | 69.44% | 109.6% |

## Pallas Programming Model

In Pallas (Mosaic GPU), one Pallas "thread" corresponds to one CUDA warpgroup (128 CUDA threads/lanes). Kernels are written in Python using JAX primitives, and the compiler handles lowering to GPU instructions.

Key abstractions:
- `ct.bid(0)` for block identifiers
- `ct.load()` / `ct.store()` for data movement
- Scratch shapes for shared memory and accumulator allocation
- Barrier objects for synchronization between pipeline stages

## Optimization Stages

### Stage 1: Basic Single-CTA Kernel
A single warpgroup handles everything: fetching data via TMA, issuing MMA operations, and storing results. The kernel uses tuning parameters: tile_m, tile_n, tile_k, and max_concurrent_steps for prefetch pipeline depth.

**Tile sizing guidance**: tile_k should ideally be 128 divided by the byte-width of the input element type (e.g., 64 for float16).

### Stage 2: Warp Specialization
Breaks the single warpgroup into specialized warps:
- **Memory warp**: Handles async TMA operations (loading MMA operands)
- **Compute warp**: Issues MMA instructions

This overlap reduces stalls by hiding memory latency behind compute. Uses 2 Pallas threads (warpgroups) with distinct roles.

### Stage 3: Tiled Epilogue
Rather than copying the full accumulated result to global memory at once, the epilogue loops through output columns in smaller chunks. This pipelines TMEM-to-SMEM transfers with SMEM-to-GMEM copies:
- Avoids waiting for the entire accumulator to be available
- Requires synchronization to prevent SMEM overwrites before previous copies complete
- Separate wait calls for successive transfers

### Stage 4: Collective 2CTA MMA (2SM Cooperative)
Leverages Blackwell's cluster capability by pairing two blocks on two separate SMs:
- Each block loads only half of each operand
- The MMA operation exchanges data from SMEM of each block as it runs
- Effectively doubles arithmetic intensity
- Uses a cluster of two CTAs with shared SMEM access
- Achieves ~5x speedup when combined with pipelining

### Stage 5: Persistent Kernel
The kernel launches a grid as large as the number of SMs (not the number of output tiles). Each SM processes multiple output tiles in a loop:
- 3 Pallas threads with warp specialization
- Eliminates kernel launch overhead for large problems
- Better amortizes setup costs across multiple tiles

### Stage 6: Dedicated Epilogue Warpgroup
Adds a separate warpgroup dedicated to epilogue operations, fully overlapping epilogue writes with the next tile's computation.

### Stage 7: Grid Tiling
Reorganizes the iteration order over output tiles to improve L2 cache locality, achieving 109.6% of cuBLAS performance (cuBLAS likely uses a different tile order).

## Key Implementation Details

### SMEM Transforms
Swizzle and tiling transforms ensure SMEM data format matches MMA instruction expectations. This is critical for avoiding bank conflicts and achieving maximum throughput.

### Pipeline Barrier Management
Barriers track data availability between load and compute phases. The kernel uses alternating barrier slots to prevent buffer overwrites before data consumption. The pattern:
1. Producer (memory warp) signals barrier when data is ready
2. Consumer (compute warp) waits on barrier before reading
3. Consumer signals completion so producer can reuse the buffer

### Benchmark Methodology
The tutorial emphasizes: "don't believe matmul benchmarks if they don't specify input data distribution." All measurements use arrays with iid normal float16 entries, which are one of the slower distributions for matmul.

## Significance

This tutorial is notable as the first comprehensive Blackwell kernel programming guide outside of CUDA C++/CUTLASS. It demonstrates that:
- JAX Pallas can achieve cuBLAS-competitive (and even superior) performance on Blackwell
- All major Blackwell features (TMA, TMEM, 2SM cooperative, warp specialization, persistent kernels) are accessible from Python
- The optimization progression mirrors the same techniques used in CUTLASS but expressed in a higher-level language
