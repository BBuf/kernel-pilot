---
id: hw-gpu-architecture-resource-model
title: "GPU Architecture Resource Model"
type: hardware
architectures: [sm90, sm100, sm120]
tags: [memory-hierarchy, tma, wgmma, tcgen05, tmem, nvfp4, fp8, fp4, cluster, occupancy]
confidence: source-reported
related: [hw-tcgen05-mma, hw-tmem, hw-tma, hw-clc, migration-wgmma-to-tcgen05, migration-register-to-tmem]
sources: [doc-ako4all-nvidia-architecture-reference, doc-ako4all-sm90-guide, doc-ako4all-sm100-guide, doc-nvidia-tuning-guide, blog-blackwell-microbenchmarking]
aliases: ["architecture resource model", "SM resource model", "Hopper vs Blackwell resources"]
blackwell_relevance: "This page explains which Hopper assumptions can carry to Blackwell and which must be re-validated for SM100/SM120."
---

# GPU Architecture Resource Model

Use this page before changing tile size, stage count, block size, or occupancy
assumptions. The key is to separate the physical resource that bottlenecks the
kernel from the programming interface used to reach it.

## Architecture Comparison

| Resource | SM90 Hopper | SM100 Blackwell datacenter | SM120 Blackwell desktop/workstation |
|---|---|---|---|
| Tensor-core path | WGMMA | tcgen05 | closer to register-fragment tensor-core paths |
| Accumulator storage | registers | TMEM | registers |
| Shared memory | large, TMA-friendly | larger, TMA/multicast-friendly | smaller than datacenter Blackwell |
| Scheduling tool | persistent kernels, Stream-K-like schedulers | CLC plus persistent kernels | persistent kernels without datacenter cluster/TMEM assumptions |
| Narrow precision | FP8 | FP4/FP6/FP8 block-scaled paths | FP4/FP6 exists but datacenter tcgen05/TMEM assumptions do not all carry |

## Decision Rules

- If the kernel is GEMM-like and targets SM100, first ask whether a tcgen05/TMEM path exists in CUTLASS, CuTe DSL, Triton 3.6+, or a tracked PR.
- If the kernel is memory-bound, architecture differences mostly change the bandwidth/L2/occupancy tradeoff; coalescing and vectorized loads remain first checks.
- If the kernel is tail-limited, SM100 CLC may be the right primitive; on SM90/SM120 use persistent scheduling or tile splitting.
- If porting from Hopper to Blackwell, do not just enlarge tiles. Re-check accumulator location, shared-memory usage, TMA overlap, and resident blocks.

## Profiling Questions

1. Is the limiting resource tensor pipe, DRAM, L2, shared memory, registers, TMEM, or launch/scheduling?
2. Did a larger tile improve reuse while lowering active warps too far?
3. Does the shape fill full waves of SMs, or is last-wave utilization the main loss?
4. Does the architecture actually support the feature being assumed: TMEM, CLC, clusters, or the target tensor-core instruction?
