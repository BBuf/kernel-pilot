---
id: doc-ako4all-profiling-debugging-reference
title: "AKO4ALL Profiling and Debugging Reference"
url: https://github.com/BBuf/kernel-pilot/tree/main/knowledge/references/ako4all
source_category: community-note
architectures: [sm90, sm100, sm120]
tags: [profiling, debugging, occupancy, register-budgeting, memory-hierarchy, shared-memory]
retrieved_at: 2026-05-16
description: "Distilled profiler/debugger workflow notes from the previous AKO4ALL reference tree."
---

# AKO4ALL Profiling and Debugging Reference

This source page captures the tool order and interpretation rules that should
sit beside PR-diff evidence during kernel optimization.

## Tool Order

1. Focused correctness reproducer.
2. `compute-sanitizer` or `cuda-gdb` for memory, race, and synchronization bugs.
3. `nsys` for timeline, launch gaps, CPU/GPU interaction, copies, and overlap.
4. `ncu` for per-kernel root cause.
5. PTX/SASS inspection when codegen or instruction selection is suspect.

## Useful Commands

```bash
compute-sanitizer --tool memcheck ./program
compute-sanitizer --tool racecheck ./program
nsys profile --trace=cuda,nvtx,osrt -o report ./program
ncu --set basic --kernel-name "kernel" ./program
ncu --section SpeedOfLight --section Occupancy --section LaunchStats --kernel-name "kernel" ./program
```

## Interpretation Rules

- SM high, memory low: likely compute-bound.
- Memory high, SM low: likely memory-bound.
- Both low: inspect latency, occupancy, scheduling, barriers, or launch gaps.
- Shape-specific failures in async kernels often point to predicate coverage, barrier lifetime, or shared-memory stage reuse.
- Any speedup claim needs device, dtype, shape, warmup, iterations, timing method, and one concrete next edit.
