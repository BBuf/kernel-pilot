---
id: doc-sm90-guide
title: "SM90 Hopper Optimization Guide"
url: https://github.com/BBuf/kernel-pilot/tree/main/knowledge/references
source_category: community-note
architectures: [sm90, sm90a]
tags: [tma, wgmma, cluster, mbarrier, fp8, shared-memory-optimization, vectorized-loads]
retrieved_at: 2026-05-16
description: "Distilled Hopper tuning notes from the previous local reference tree."
---

# SM90 Hopper Optimization Guide

Hopper is the main comparison point for Blackwell migration.

## Keep These Facts

- 64 warps/SM and 2048 threads/SM.
- About 192 KB shared memory per SM.
- TMA, thread-block clusters, distributed shared memory, FP8 tensor cores.
- GEMM/attention kernels often center on WGMMA and warpgroup producer/consumer structure.
- H200 keeps the same SM architecture as H100 but raises memory bandwidth via HBM3e.

## Tuning Bias

- Use TMA to overlap global-to-shared movement with compute.
- Inspect WGMMA issue, TMA stalls, shared-memory bank conflicts, and register pressure together.
- Larger shared-memory tiles can help reuse but may reduce occupancy.
- For memory-bound kernels, vectorized loads and coalescing usually beat more arithmetic rearrangement.
