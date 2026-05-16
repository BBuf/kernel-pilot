---
id: doc-sm100-guide
title: "SM100 Blackwell Datacenter Optimization Guide"
url: https://github.com/BBuf/kernel-pilot/tree/main/knowledge/references
source_category: community-note
architectures: [sm100, sm100a]
tags: [tcgen05, tmem, tma, clc, 2sm-cooperative, nvfp4, fp8, fp4, block-scale, memory-hierarchy]
retrieved_at: 2026-05-16
description: "Distilled Blackwell datacenter tuning notes from the previous local reference tree."
---

# SM100 Blackwell Datacenter Optimization Guide

This page keeps the Blackwell architecture notes from the previous local tree.
Use official docs and PR evidence for final claims.

## Keep These Facts

- Datacenter Blackwell introduces the `tcgen05` tensor-core instruction family.
- TMEM moves large accumulator storage away from the register file.
- B200/GB200 class devices expose large L2 and high HBM bandwidth; coalescing still matters.
- CLC helps persistent kernels avoid tail effects and load imbalance.
- NVFP4/FP6/FP8 block-scaled paths are first-class tensor-core targets.

## Tuning Bias

- Use tcgen05/TMEM-capable libraries or DSLs for GEMM-like kernels.
- Prefer TMA for regular bulk movement and design for overlap with compute.
- Profile tensor pipe utilization, TMA throughput/stalls, L2 behavior, occupancy, and cross-die effects.
- Do not assume SM100 code ports to SM120 unchanged; desktop Blackwell lacks some datacenter assumptions.
