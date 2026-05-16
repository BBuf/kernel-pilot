---
name: ncu-report
description: "Use when a GPU kernel optimization loop needs Nsight Compute driven profiling: build a focused harness, collect .ncu-rep reports, export metrics/source/PM-sampling evidence, compare baseline vs candidate reports, classify stalls, and produce one concrete next kernel edit."
type: flow
---

# ncu-report

Use this skill when benchmark numbers are not enough and the next CUDA,
Triton, CUTLASS/CuTe, CuTe DSL, or PTX kernel edit should be driven by Nsight
Compute evidence.

The rule is:

```text
profile first, diagnose second, optimize third
```

The output is not just "memory-bound" or "compute-bound". It must be an
inference chain from measured counters to a likely mechanism to one actionable
kernel edit.

## When To Invoke

Invoke `ncu-report` when any of these hold:

- A baseline benchmark has passed and no baseline report digest exists.
- A correct candidate is within +/-2% of baseline or the prior best.
- A correct candidate regresses on one or more important shapes.
- A candidate is much faster than expected and needs explanation.
- The next edit is unclear after benchmark results.
- A Humanize/RLCR reviewer asks for profile evidence.
- A Blackwell/Hopper kernel may involve pipeline bubbles, tail effects, uneven
  block lifetimes, inline PTX hotspots, TMA/mbarrier waits, tensor-core
  underuse, or source-correlated stalls.

Do not run NCU while correctness is failing unless the failure is a profiler
collection problem. Fix correctness first.

## Required Artifacts

Store artifacts under the standalone optimization repo:

```text
profile-artifacts/<version>/
  report.ncu-rep
  raw.csv
  details.txt
  source.csv                 # when source export is available
  sampling.csv               # when PM sampling export is available
  kernel.ptx                 # when PTX can be extracted
  kernel.sass                # when SASS can be extracted
  digest.md
```

When comparing a candidate, include the baseline or parent version path in the
digest.

## Workflow

1. Pick one representative shape first. Prefer the smallest shape that still
   exposes the regression, plateau, tail effect, or suspected bottleneck.
2. Build a focused harness with stable warmup, fixed dtype, fixed shape, fixed
   seed, and an explicit kernel-name pattern. Use the same command for baseline
   and candidate.
3. Capture an Nsight Compute report with SpeedOfLight, SchedulerStats,
   WarpStateStats, Occupancy, LaunchStats, MemoryWorkloadAnalysis, and
   SourceCounters. If `ncu --list-sections` shows `PmSampling` or
   `PmSampling_WarpStates`, add those PM-sampling sections for timeline stalls
   and long-tail evidence.
4. Export raw metrics and text details. Export source and sampling pages when
   the installed NCU supports them.
5. If the hotspot is source-correlated, inline PTX, codegen-sensitive, or
   instruction-selection-sensitive, extract PTX/SASS and align the hot source
   row with generated instructions before choosing the edit.
6. Compare candidate against baseline or parent, not only absolute metrics.
7. Diagnose using metric groups from [metrics.md](references/metrics.md).
8. Write `digest.md` using the template below. The final section must contain
   exactly one next edit.
9. Update the optimization loop ledger with the digest path, bottleneck class,
   and selected next edit.

## Hand Off To Kernel Knowledge

When the digest points to an edit family but the exact implementation is not
obvious, turn the measured symptom into a `kernel-knowledge` query. Use the
counter name, bottleneck class, target architecture, DSL, and operator as
search terms; then ground any borrowed implementation idea in PR/source
evidence before editing code.

Useful mappings:

| Digest signal | Knowledge query shape |
|---|---|
| Long scoreboard, poor bytes/sector | `memory-bound`, `vectorized-loads`, cache policy, layout/coalescing PRs |
| Shared bank conflicts or short scoreboard | `shared-memory`, `swizzling`, `bank-conflicts`, TMA/ldmatrix examples |
| Barrier, membar, mbarrier, TMA wait | `pipeline-stalls`, `mbarrier`, `pipeline-stages`, producer/consumer split |
| Low tensor pipe on GEMM/attention | `tcgen05` or `wgmma`, warp specialization, tile shape, epilogue fusion |
| Tail waves or uneven block lifetimes | `tail-effect`, persistent kernels, CLC, tile scheduling |
| I-cache, no-instruction, codegen pressure | PTX/SASS, inline PTX, specialization/splitting examples |

## Common Commands

Load [examples.md](references/examples.md) for copyable command variants:
baseline capture, focused regex capture, PyTorch extension profiling, PM
sampling/source export, PTX/SASS hotspot analysis, report comparison, and
script-assisted digest generation.

Minimal focused capture:

```bash
mkdir -p profile-artifacts/v000_baseline
ncu --target-processes all \
    --kernel-name regex:"<kernel-name-pattern>" \
    --launch-skip 5 --launch-count 1 \
    --set full --import-source on \
    --section SpeedOfLight \
    --section SchedulerStats \
    --section WarpStateStats \
    --section Occupancy \
    --section LaunchStats \
    --section MemoryWorkloadAnalysis \
    --section SourceCounters \
    -o profile-artifacts/v000_baseline/report \
    python benchmarks/<bench>.py --shape <shape> --dtype <dtype>

ncu --import profile-artifacts/v000_baseline/report.ncu-rep \
    --page raw --csv > profile-artifacts/v000_baseline/raw.csv
ncu --import profile-artifacts/v000_baseline/report.ncu-rep \
    --page details > profile-artifacts/v000_baseline/details.txt
```

If a section or page is unavailable on the installed NCU version, record that
in the digest and continue with the available sections.

Optional helper:

```bash
python3 <skill-root>/scripts/ncu_report_digest.py \
    --csv profile-artifacts/v001_candidate/raw.csv \
    --baseline-csv profile-artifacts/v000_baseline/raw.csv \
    --kernel-regex "<kernel-name-pattern>" \
    --output profile-artifacts/v001_candidate/digest.md
```

The helper is a first pass only. Inspect the report and source/sampling evidence
before treating the next edit as final.

## Metrics To Inspect

Start with these groups, then load [metrics.md](references/metrics.md) for the
full list and interpretation rules:

- Runtime and identity: kernel name, duration, launch count, grid/block shape.
- Speed-of-light: SM throughput, tensor pipe throughput, DRAM throughput, L2
  throughput.
- Scheduler and warp state: eligible warps, active warps, issue rate, dominant
  `smsp__warp_issue_stalled_*` reason.
- Occupancy and resources: achieved occupancy, registers/thread, shared memory,
  occupancy limiters.
- Memory path: global load/store sectors, bytes per sector, L1/TEX, L2, DRAM,
  shared-memory bank conflicts.
- Source evidence: source-correlated stall rows, SASS/PTX line hotspots, inline
  PTX hotspots.
- PTX/SASS evidence: generated instruction sequence, register reuse, predicate
  pressure, vector width, cache modifiers, barrier instructions, and inline PTX
  line mappings.
- PM sampling: time-localized stalls, pipeline bubbles, long tail waves,
  producer/consumer imbalance.
- Blackwell/Hopper specifics: TMA waits, mbarrier waits, tcgen05/wgmma tensor
  pipe utilization, TMEM lifecycle, CLC/tail effect, 2-SM cooperative imbalance.

Validate exact metric names on the target machine:

```bash
ncu --list-sections
ncu --query-metrics | grep -E 'warp_issue_stalled|pipe_tensor|dram__|lts__|bank_conflict|launch__'
```

## Digest Template

```markdown
### NCU Report Digest: <kernel> @ <version>

Environment
- GPU / arch:
- Driver / CUDA / NCU:
- Repo commit:
- Benchmark command:
- Shape / dtype:
- Baseline or parent report:
- Candidate report:
- Raw CSV:
- Source / sampling exports:
- PTX / SASS dumps:

Headline
- Bottleneck class:
- Dominant stall or hotspot:
- Confidence: High | Medium | Low
- Why this report is valid:

Evidence
| Metric | Baseline | Candidate | Delta | Interpretation |
|---|---:|---:|---:|---|
| <metric> | <value> | <value> | <delta> | <meaning> |

Source / PM-Sampling Hotspots
- <source/PTX/SASS line or phase>: <counter/timeline signal> -> <meaning>

PTX / SASS Analysis
- Hot instruction window:
- Suspected codegen or inline PTX issue:
- Instruction-level edit:

Inference Chain
1. Measured counter:
2. Likely mechanism:
3. Why other hypotheses are weaker:
4. Risk:

Next Concrete Edit
- File:
- Change:
- Validation:
- Expected metric movement:
```

## Diagnosis Rubric

- Long scoreboard dominant: global/L2 load latency. Prefer prefetch, more MLIO,
  coalescing/vectorization, smaller footprint, or shared staging.
- Short scoreboard plus bank conflicts: shared-memory wait. Prefer padding,
  swizzle, layout change, or fewer shared-memory round trips.
- Barrier or mbarrier stalls: pipeline synchronization issue. Check phase
  tracking, TMA arrive/wait lifecycle, stage count, and producer/consumer split.
- Tensor pipe low on a tensor-core kernel: wrong path, tile too small, epilogue
  too heavy, insufficient pipeline depth, or scheduler bubbles.
- DRAM high and SM low: reduce bytes, improve coalescing, vectorize, fuse, or
  change layout.
- L2 high and DRAM low/moderate: reuse exists but may be inefficient. Consider
  tile shape, persistent scheduling, or cache policy.
- Both SM and memory low: check occupancy, eligible warps, launch overhead,
  branch divergence, barriers, and PM-sampling timeline.
- Tail waves or uneven block lifetimes: consider persistent scheduling, CLC on
  Blackwell, tile splitting, or shape-aware routing.
- Inline PTX hotspot: inspect source-correlated SASS/PTX before changing
  high-level code.
- PTX/SASS mismatch: if high-level source looks correct but generated code shows
  scalarized loads, unexpected conversions, missing cache modifiers, excessive
  predicate moves, register spills, or extra barriers, choose a codegen-facing
  edit such as explicit vectorization, `__restrict__`, alignment assertions,
  launch bounds, narrower unroll, or a targeted inline PTX sequence.

## Output Rules

- End with exactly one next edit. Do not end with "try several things".
- Cite the metric values that support the diagnosis.
- Compare against baseline or parent whenever a comparable report exists.
- If a key metric is missing, say it is missing and use the closest available
  section. Do not invent metric values.
- If the kernel is already beyond about 85% of relevant tensor, SM, or DRAM
  peak and no low-effort edit remains, say that and route effort to shape
  routing, fusion, launch overhead, or stopping criteria.
- Keep `.ncu-rep`, CSV exports, and digest paths in the attempt ledger.
