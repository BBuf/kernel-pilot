---
id: doc-ako4all-cuda-kernel-reference
title: "AKO4ALL CUDA C++ and PTX Kernel Reference"
url: https://github.com/BBuf/kernel-pilot/tree/main/knowledge/references/ako4all
source_category: community-note
architectures: [sm90, sm100, sm120]
tags: [cuda-cpp, ptx, coalescing, vectorized-loads, shared-memory-optimization, bank-conflicts, tma, wgmma, tcgen05]
languages: [cuda-cpp, ptx]
retrieved_at: 2026-05-16
description: "Distilled CUDA C++/PTX workflow notes from the previous AKO4ALL reference tree."
---

# AKO4ALL CUDA C++ and PTX Kernel Reference

Use this page as background for handwritten CUDA C++/PTX kernels. It is a
workflow source, not a replacement for PR-diff evidence.

## Implementation Checklist

Before changing a kernel, pin down:

1. Shapes, dtypes, layouts, strides, and alignment.
2. Target SM architecture and shared-memory budget.
3. Bottleneck class: compute, memory, launch overhead, synchronization, layout conversion, or tail effect.
4. Correctness oracle and old-vs-new performance benchmark.
5. Which low-level rule must be preserved: memory coalescing, barrier coverage, tensor-map lifetime, PTX operand layout, or graph/stream ordering.

## CUDA C++ Patterns

- Elementwise: one thread per element, vectorized loads/stores when aligned.
- Row reductions: one block per row, warp shuffles plus shared-memory cross-warp reduction.
- Tiled GEMM/attention: cooperative global-to-shared staging, explicit barriers, register or TMEM accumulation depending on architecture.
- Stream overlap: pinned host memory and async copies across multiple streams.

## PTX Inspection Workflow

```bash
nvcc -O3 -lineinfo --ptxas-options=-v kernel.cu
cuobjdump -res-usage ./program
cuobjdump -ptx ./program > extracted.ptx
cuobjdump -sass ./program > extracted.sass
```

Use this when instruction selection or resource usage is part of the hypothesis:
`ldmatrix`, `stmatrix`, WGMMA, TMA, mbarrier, tensor memory, cache policy, or
inline PTX fragment layout.

## Common Failure Modes

- Adding async copy without enough independent work to hide the latency.
- Measuring pageable host transfers while expecting overlap.
- Increasing tile size until register pressure or shared-memory occupancy collapses.
- Changing several dimensions at once and losing causality.
- Reusing shared-memory stages without a predicate/barrier audit.
