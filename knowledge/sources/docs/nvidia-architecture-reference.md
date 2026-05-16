---
id: doc-nvidia-architecture-reference
title: "NVIDIA Architecture Reference"
url: https://github.com/BBuf/kernel-pilot/tree/main/knowledge/references
source_category: community-note
architectures: [sm90, sm100, sm120]
tags: [memory-hierarchy, tma, wgmma, tcgen05, tmem, nvfp4, fp8, fp4, cluster]
retrieved_at: 2026-05-16
description: "Distilled local architecture notes from the previous reference tree; used as background knowledge, not primary PR evidence."
---

# NVIDIA Architecture Reference

This source page preserves the useful architecture layer from the previous
local reference tree without restoring the old document dump.

## Architecture Facts To Keep

| Architecture | Examples | Kernel tuning bias |
|---|---|---|
| SM90 | H100, H200 | Larger shared-memory tiles, TMA overlap, WGMMA/warpgroup programming, thread-block clusters, distributed shared memory |
| SM100 | B200, GB200 | tcgen05/TMEM paths for GEMM-like kernels, larger shared-memory tiles than Hopper, Blackwell TMA/multicast, CLC for persistent tile scheduling |
| SM120 | RTX 5090 class | GDDR bandwidth and register pressure matter more; no datacenter TMEM/tcgen05 assumptions; reduce SM100 tile and cluster assumptions |

## Cross-Architecture Rules

- Query device properties at runtime; do not bake SM count, shared-memory budget, or cluster size into a generic kernel.
- Treat every performance conclusion as architecture-specific until measured on the target SKU.
- Prefer source pages backed by merged PR diffs for concrete implementation choices; use this architecture page to explain why a choice might work.
- For Hopper-to-Blackwell migration, separate three concerns: tensor-core instruction path, accumulator storage, and scheduling/tail behavior.

## Provenance Note

This page is a compact rewrite of prior local architecture notes. Treat it as
orientation material and use PR/source artifacts for concrete implementation
details.
