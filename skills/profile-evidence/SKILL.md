---
name: profile-evidence
description: Use when a GPU kernel optimization loop needs to turn Nsight Compute (ncu) metrics into a Profile Evidence Digest, classify bottlenecks, explain regressions, plateaus, or surprising wins, and choose one concrete next kernel edit.
---

# Profile Evidence Skill

**Purpose.** Turn fine-grained Nsight Compute (ncu) evidence into concrete
optimization guidance: identify stalls, bubbles, memory-bound vs compute-bound
behavior, occupancy issues, and other runtime bottlenecks, and emit a
ranked list of next actions tied to specific source / kernel features.

Invoke this skill whenever a candidate's benchmark result does not, by itself,
explain the bottleneck (regression, plateau, suspicious wins, or
correctness-only outcomes).

---

## When to invoke

Run the Profile Evidence Skill whenever **any** of the following are true:

1. The candidate is correct, but every case is within ±2% of the baseline.
2. The candidate is correct overall but regresses on one or more configured
   cases.
3. Two consecutive iterations have shown <1% geomean improvement over the
   prior best.
4. The candidate is much faster than expected and needs a "why is it faster"
   explanation before being recorded.
5. A reviewer asks for a Profile Evidence Digest.

Do **not** invoke the skill when correctness is failing; fix correctness first.

---

## How to collect data

Recommended `ncu` invocation for a quick triage:

```bash
ncu --set full --target-processes all --launch-skip 5 --launch-count 1 \
    --import-source on --section SourceCounters \
    -o ncu_<task>_<version> \
    python <benchmark or repro command>
```

Recommended `ncu` invocation for a focused kernel:

```bash
ncu --kernel-name regex:"<kernel-name-pattern>" \
    --set full \
    --import-source on \
    --metrics sm__inst_executed_pipe_tensor.avg.pct_of_peak_sustained_elapsed,\
dram__throughput.avg.pct_of_peak_sustained_elapsed,\
lts__t_bytes.avg.pct_of_peak_sustained_elapsed,\
sm__warps_active.avg.pct_of_peak_sustained_active,\
smsp__average_warp_latency_per_inst_executed,\
smsp__warp_issue_stalled_long_scoreboard.sum,\
smsp__warp_issue_stalled_short_scoreboard.sum,\
smsp__warp_issue_stalled_no_instruction.sum,\
smsp__warp_issue_stalled_imc_miss.sum,\
smsp__warp_issue_stalled_drain.sum,\
smsp__warp_issue_stalled_dispatch_stall.sum,\
l1tex__data_bank_conflicts_pipe_lsu.sum,\
sm__pipe_alu_cycles_active.avg.pct_of_peak_sustained_elapsed \
    -o ncu_<task>_<version> \
    python <benchmark>
```

Persist both the `.ncu-rep` and a CSV export:

```bash
ncu --import ncu_<task>_<version>.ncu-rep --csv > ncu_<task>_<version>.csv
```

The optimization loop should keep both artifact paths in the digest.

---

## Digest format

The skill emits one **Profile Evidence Digest** per kernel. Every digest must
contain the following sections:

```text
### Profile Evidence Digest: <kernel name> @ <version>

Environment
- GPU: <name + arch + driver + cuda>
- Shapes/dtypes: <list of cases captured>
- ncu report: <path to .ncu-rep>
- ncu csv: <path to .csv>

Headline
- Bottleneck class: [Memory-bound | Tensor-pipe-bound | ALU-bound | Latency-bound | Launch-overhead | Mixed]
- Most-stalled reason: <stall name>
- Confidence: [High | Medium | Low] (why)

Evidence
- <metric name>: <value> (<peak-percent>)  -> <interpretation>
- ... (one line per metric used in the conclusion)

Hypotheses (ranked)
1. <hypothesis>
   - Why: <which metric supports it>
   - Action: <specific code/kernel change>
   - Expected impact: <metric to move and by how much>
   - Risk / cost: <what could go wrong>
2. ...

Next concrete edit
- File: <path>
- Change: <one-sentence change>
- Validation: <which case to re-benchmark, which metric to re-check>
```

The digest must always end with a single, concrete next edit. "Try multiple
things" is not allowed.

---

## Stall-pattern rubric

Use the dominant stall reason to constrain the hypothesis ranking. Below are
the canonical patterns used by the Profile Evidence Skill.

### Long scoreboard stall (memory wait)

Signal:
- `smsp__warp_issue_stalled_long_scoreboard.sum` is the dominant stall.

Interpretation:
- Threads are waiting on a global / L2 load to return.

Recommended hypotheses (rank in order):
1. **Increase MLIO** (memory-level instruction overlap). Use `cp.async`,
   `cuda::pipeline`, manual prefetch, or loop unrolling in native CUDA to issue
   more loads before the first one is consumed.
2. **Coalesce / vectorize loads**. Check `smsp__sass_average_data_bytes_per_sector_mem_global_op_ld`.
3. **Reduce footprint**. If working set exceeds L2, either tile smaller or
   pre-fetch into shared memory.
4. **Pre-stage indirection**. Indirect KV loads through a block table benefit
   from gathering once into shared memory.

### Short scoreboard stall (shared-memory wait)

Signal:
- `smsp__warp_issue_stalled_short_scoreboard.sum` is dominant.
- `l1tex__data_bank_conflicts_pipe_lsu.sum` is non-trivial.

Interpretation:
- Threads are waiting on a shared-memory access; usually bank conflicts.

Recommended hypotheses:
1. **Resolve bank conflicts**. Pad shared-memory tile or use a swizzle.
2. **Use ldmatrix / TMA** to bulk-load tiles into shared memory.
3. **Reduce smem traffic**. Reuse a tile across more compute.

### `no_instruction` stall (front-end starvation)

Signal:
- `smsp__warp_issue_stalled_no_instruction.sum` dominant.

Interpretation:
- The scheduler has no instructions ready (could be control flow, predicated
  paths, or branch divergence).

Recommended hypotheses:
1. **Reduce branch divergence**; reorganize the kernel so warps execute the
   same predicate.
2. **Inline / unroll** the inner loop.
3. **Check ICache misses** via `smsp__warp_issue_stalled_imc_miss.sum`.

### `imc_miss` stall (ICache miss)

Signal:
- `smsp__warp_issue_stalled_imc_miss.sum` dominant.

Recommended hypotheses:
1. **Reduce kernel size**: split into specialized kernels or templated paths.
2. **Avoid huge unrolls** that blow the ICache.

### `drain` / `dispatch_stall` (pipeline drain)

Signal:
- `smsp__warp_issue_stalled_drain.sum` or `smsp__warp_issue_stalled_dispatch_stall.sum`
  dominant.

Recommended hypotheses:
1. **Insufficient ILP**; mix independent FMAs / tensor-pipe instructions.
2. **Producer / consumer imbalance** in warp-specialized Hopper kernels.

### Tensor pipe under-utilized

Signal:
- `sm__inst_executed_pipe_tensor.avg.pct_of_peak_sustained_elapsed` is low
  even though the operator is supposed to be compute-bound.

Recommended hypotheses:
1. **Tile shape too small**; increase `kBlockM` / `kBlockN` if smem allows.
2. **Epilogue heavy**; check `sm__pipe_alu_cycles_active`; fuse the epilogue
   or split into a separate kernel.
3. **Wrong dtype path**; verify FP8 / FP4 dispatch is actually selected.

### HBM-bound but achieved BW low

Signal:
- `dram__throughput` is the dominant percent but **< 70 %** of peak.

Recommended hypotheses:
1. **Coalesce / vectorize**; check sector size.
2. **Avoid non-contiguous strides**; rewrite the layout if possible.
3. **Use TMA** on Hopper / Blackwell for bulk loads.

### L2-bound

Signal:
- `lts__t_bytes` high, `dram__throughput` low or moderate.

Recommended hypotheses:
1. **Smaller tile, larger reuse**; the working set fits in L2 but the kernel
   does not reuse it.
2. **Persistent kernel** to amortize tile fetches across multiple outputs.

### Launch-overhead bound

Signal:
- Kernel runtime is in the microsecond range; `sm__cycles_active` low for the
  whole grid.

Recommended hypotheses:
1. **Persistent kernel** loop over tiles instead of relaunching.
2. **Capture into CUDA Graph** when the kernel is called many times with the
   same shape.
3. **Fuse with neighbor kernel** to amortize launch cost.

---

## Producing the digest from CSV

A minimal extraction loop:

1. Parse the CSV row corresponding to the kernel of interest.
2. Compute the stall composition (sum of `smsp__warp_issue_stalled_*` columns
   normalized to 100 %).
3. Classify the bottleneck using the rubric above.
4. Compose the digest from the rubric template.

The python module accepts either a hand-written summary dictionary (already
parsed from `ncu --csv`) or a small CSV file with one row per metric.

---

## Output rules

- One concrete next edit. No optionality.
- Cite the metric value that supports each hypothesis.
- If the kernel is already at >85 % tensor pipe peak (or >85 % DRAM peak) and
  correct, declare "no further low-effort optimization" and stop.
- Always store the digest under the task run directory (`runs/<task>/<version>/digest.md`).
