---
id: doc-cuda-memory-occupancy
title: "CUDA Memory Hierarchy and Occupancy Notes"
url: https://github.com/BBuf/kernel-pilot/tree/main/knowledge/references
source_category: community-note
architectures: [sm90, sm100, sm120]
tags: [memory-hierarchy, l2-cache, shared-memory, occupancy, register-budgeting, coalescing, bank-conflicts]
retrieved_at: 2026-05-16
description: "Distilled CUDA memory and occupancy notes from the previous local reference cache."
---

# CUDA Memory Hierarchy and Occupancy Notes

This page distills only the kernel-relevant memory/occupancy pieces from the
old vendored CUDA docs. It is intentionally compact.

## Memory Rules

- Performance is best when data is resident in the memory closest to the processor accessing it.
- Coalesced global memory access and 128-byte alignment are still the first sanity checks for bandwidth-bound kernels.
- Shared memory can reduce global traffic, but bank conflicts and barrier placement can erase the gain.
- L2 reuse is workload- and architecture-sensitive; B200 has much more L2 than Hopper, but streaming accesses can still pollute cache.
- Unified memory and host memory features are useful for system behavior, but kernel optimization should first reason about device DRAM, L2, L1/shared, registers, and TMEM where available.

## Occupancy Rules

- Occupancy is active warps per SM divided by maximum possible active warps.
- Higher occupancy does not guarantee speed, but very low occupancy often prevents latency hiding.
- Registers, shared memory, block size, and launch bounds can each cap resident blocks.
- Use `--ptxas-options=-v`, Nsight Compute occupancy sections, and runtime occupancy APIs to connect resource use to active blocks.

## Practical Kernel Questions

1. Is memory access coalesced and vectorized?
2. Is the shared-memory layout introducing bank conflicts?
3. Is occupancy limited by registers, shared memory, block size, or launch bounds?
4. Did a tile-size change improve reuse while reducing active warps too far?
5. Would a cache policy or persistence hint help a reused stream without polluting L1/L2?
