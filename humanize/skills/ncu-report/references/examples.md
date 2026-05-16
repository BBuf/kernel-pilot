# ncu-report Examples

All examples assume they run from the standalone optimization repo and write
under `profile-artifacts/<version>/`.

## Baseline Full Report

```bash
version=v000_baseline
out=profile-artifacts/$version
mkdir -p "$out"

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
    -o "$out/report" \
    python benchmarks/bench.py --impl baseline --shape "<shape>" --dtype "<dtype>"

ncu --import "$out/report.ncu-rep" --page raw --csv > "$out/raw.csv"
ncu --import "$out/report.ncu-rep" --page details > "$out/details.txt"
```

## Candidate Report With Same Harness

```bash
version=v001_candidate
out=profile-artifacts/$version
mkdir -p "$out"

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
    -o "$out/report" \
    python benchmarks/bench.py --impl candidate --shape "<shape>" --dtype "<dtype>"

ncu --import "$out/report.ncu-rep" --page raw --csv > "$out/raw.csv"
ncu --import "$out/report.ncu-rep" --page details > "$out/details.txt"
```

## Focused Metrics For A Fast Reprofile

Use this after a full baseline report exists and the next candidate only needs a
targeted check.

```bash
ncu --target-processes all \
    --kernel-name regex:"<kernel-name-pattern>" \
    --launch-skip 10 --launch-count 1 \
    --import-source on \
    --metrics sm__throughput.avg.pct_of_peak_sustained_elapsed,\
sm__inst_executed_pipe_tensor.avg.pct_of_peak_sustained_elapsed,\
dram__throughput.avg.pct_of_peak_sustained_elapsed,\
lts__t_bytes.avg.pct_of_peak_sustained_elapsed,\
sm__warps_active.avg.pct_of_peak_sustained_active,\
smsp__warps_eligible.avg.per_cycle_active,\
smsp__warp_issue_stalled_long_scoreboard.sum,\
smsp__warp_issue_stalled_short_scoreboard.sum,\
smsp__warp_issue_stalled_barrier.sum,\
smsp__warp_issue_stalled_membar.sum,\
smsp__warp_issue_stalled_mio_throttle.sum,\
smsp__warp_issue_stalled_no_instruction.sum,\
l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_ld.sum \
    -o profile-artifacts/v002_fast/report \
    python benchmarks/bench.py --impl candidate --shape "<shape>" --dtype "<dtype>"
```

If a metric name is unavailable, query the installed version and substitute the
closest section metric:

```bash
ncu --query-metrics | grep -E 'long_scoreboard|bank_conflict|pipe_tensor|throughput'
```

## PyTorch Extension Harness

```bash
CUDA_MODULE_LOADING=EAGER \
ncu --target-processes all \
    --kernel-name regex:"<extension_kernel_or_namespace>" \
    --launch-skip 5 --launch-count 1 \
    --set full --import-source on \
    -o profile-artifacts/v000_baseline/report \
    python -m pytest tests/test_kernel.py -q -s --profile-shape "<shape>"
```

For benchmark scripts, prefer a direct benchmark command over pytest so the
launch sequence is stable.

## PM Sampling And Source Hotspots

When aggregate metrics say "mixed" or "both low", preserve source and sampling
exports if supported:

```bash
ncu --list-sections | grep -E '^PmSampling'

# If the two PmSampling sections are listed, add these section flags to the
# capture command:
#   --section PmSampling --section PmSampling_WarpStates

ncu --import profile-artifacts/v001_candidate/report.ncu-rep \
    --page source --csv > profile-artifacts/v001_candidate/source.csv || true
ncu --import profile-artifacts/v001_candidate/report.ncu-rep \
    --page raw --csv | grep -Ei 'sampling|sample|stall|source' \
    > profile-artifacts/v001_candidate/sampling.csv || true
```

If `--page source` is unavailable, keep `details.txt` and cite the missing page
in the digest.

## PTX / SASS Hotspot Analysis

Use this when NCU source counters point at inline PTX, when `no_instruction` or
`imc_miss` suggests code-size/front-end pressure, or when the likely fix depends
on instruction selection.

Build with line information first:

```bash
# CUDA/C++ extension example; adapt flags to the local build system.
NVCC_FLAGS="-lineinfo -Xptxas=-v" python setup.py build_ext --inplace
```

Extract PTX and SASS when the build artifact is available:

```bash
version=v001_candidate
out=profile-artifacts/$version
mkdir -p "$out"

cuobjdump --dump-ptx build/<extension-or-binary> > "$out/kernel.ptx" || true
cuobjdump --dump-sass build/<extension-or-binary> > "$out/kernel.sass" || true
nvdisasm -g build/<kernel>.cubin > "$out/kernel.nvdisasm.sass" || true
```

Then align with NCU source evidence:

```bash
grep -E -n "<kernel-name>|tcgen05|wgmma|ldmatrix|cp.async|mbarrier|bar.sync|ld.global|st.global|cvt|selp|pred" "$out/kernel.ptx" "$out/kernel.sass"
grep -E -n "<hot-source-line>|<inline-ptx-mnemonic>" "$out/source.csv" "$out/details.txt" "$out/kernel.sass"
```

Common PTX/SASS conclusions:

- Scalarized loads: add vectorized load/store path, alignment assertion, or
  `__restrict__`.
- Unexpected `cvt`/promotion chain: fix dtype dispatch or accumulator type.
- Extra `bar.sync`/mbarrier instructions: simplify pipeline phase or barrier
  lifetime.
- Register spill/local memory access: reduce unroll, tile size, or register
  live range.
- Missing cache modifier or wrong global load form: add targeted inline PTX or
  use the framework's cache-policy primitive.
- Huge instruction window / `imc_miss`: split or specialize the kernel.

## Script-Assisted Digest And Comparison

```bash
python3 humanize/skills/ncu-report/scripts/ncu_report_digest.py \
    --csv profile-artifacts/v001_candidate/raw.csv \
    --baseline-csv profile-artifacts/v000_baseline/raw.csv \
    --kernel-regex "<kernel-name-pattern>" \
    --report profile-artifacts/v001_candidate/report.ncu-rep \
    --baseline-report profile-artifacts/v000_baseline/report.ncu-rep \
    --output profile-artifacts/v001_candidate/digest.md
```

Then manually inspect:

- `details.txt` for section warnings and occupancy limiters.
- `source.csv` or source page for source-correlated hotspots.
- PM-sampling rows for time-localized bubbles or tail waves.
- The actual kernel source before applying the suggested next edit.

## Blackwell Pipeline Bubble Check

Use this when tcgen05/TMA/TMEM kernels show lower than expected tensor pipe
utilization:

```bash
ncu --target-processes all \
    --kernel-name regex:"<blackwell_kernel>" \
    --launch-skip 5 --launch-count 1 \
    --set full --import-source on \
    --section SpeedOfLight \
    --section SchedulerStats \
    --section WarpStateStats \
    --section SourceCounters \
    -o profile-artifacts/v003_bw_pipeline/report \
    python benchmarks/bench.py --shape "<shape>" --dtype fp8

ncu --import profile-artifacts/v003_bw_pipeline/report.ncu-rep \
    --page raw --csv > profile-artifacts/v003_bw_pipeline/raw.csv
```

Look for:

- Tensor pipe below expectation while memory is not saturated.
- Barrier or mbarrier stalls near TMA wait code.
- Source samples concentrated on inline PTX `tcgen05`, `tcgen05.ld`,
  `tcgen05.cp`, `mbarrier`, or TMA wait/arrive sequences.
- PM-sampling timeline phases where TMA and MMA alternate instead of overlap.
