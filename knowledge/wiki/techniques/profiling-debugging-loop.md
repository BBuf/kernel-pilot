---
id: technique-profiling-debugging-loop
title: "Profiling and Debugging Loop"
type: technique
architectures: [sm90, sm100, sm120]
tags: [profiling, debugging, occupancy, register-budgeting, memory-hierarchy, shared-memory]
confidence: source-reported
reproducibility: snippet
prerequisites: []
related: [pattern-memory-bound, pattern-compute-bound, pattern-register-pressure, pattern-low-sm-utilization, hw-cuda-memory-hierarchy]
sources: [doc-ako4all-profiling-debugging-reference, doc-ako4all-cuda-kernel-reference, doc-ako4all-cuda-memory-occupancy]
blackwell_relevance: "The loop is architecture-independent, but Blackwell profiles must explicitly distinguish TMEM/tcgen05/TMA/CLC effects from register, shared-memory, and scheduling effects."
---

# Profiling and Debugging Loop

Use this page to turn a profiler result into one concrete next edit.

## Order

1. Reproduce correctness with the smallest shape that still fails or regresses.
2. Run sanitizer/debugger for memory, race, and synchronization bugs.
3. Use `nsys` for timeline and launch gaps.
4. Use `ncu` for root cause of the specific kernel.
5. Inspect PTX/SASS only when the hypothesis is about codegen or instruction selection.

## Command Skeleton

```bash
compute-sanitizer --tool memcheck ./bench
compute-sanitizer --tool racecheck ./bench
nsys profile --trace=cuda,nvtx,osrt -o report ./bench
ncu --section SpeedOfLight --section Occupancy --section MemoryWorkloadAnalysis --kernel-name "kernel" ./bench
cuobjdump -res-usage ./bench
```

## Digest Rule

Every profile digest should end with exactly one next edit:

| Observation | Next edit type |
|---|---|
| high DRAM, low SM | reduce bytes, vectorize, coalesce, fuse |
| low occupancy from registers | reduce register tile, add launch bounds, or move accumulator to TMEM path on SM100 |
| shared bank conflicts | pad/swizzle shared layout |
| TMA wait dominates | adjust stage count, producer/consumer split, or barrier lifetime |
| last wave dominates | persistent scheduling, CLC on SM100, or tile splitting |

Avoid "profile more" as the final action unless the current measurement is invalid.
