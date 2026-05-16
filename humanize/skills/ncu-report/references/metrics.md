# NCU Metrics Reference

Metric names differ across Nsight Compute versions and GPU architectures. Treat
the names below as preferred anchors, then verify availability on the target
machine:

```bash
ncu --list-sections
ncu --query-metrics | grep -E 'warp_issue_stalled|pipe_tensor|dram__|lts__|l1tex__|launch__'
```

## Collection Sections

| Section | Why it matters |
|---|---|
| `SpeedOfLight` | SM, tensor, memory, L2, and DRAM peak percentages. |
| `SchedulerStats` | Issue rate, eligible warps, scheduler pressure. |
| `WarpStateStats` | Dominant stall reasons. |
| `Occupancy` | Achieved occupancy and resource limiters. |
| `LaunchStats` | Launch geometry, waves, and block lifetime clues. |
| `MemoryWorkloadAnalysis` | Global, local, shared, L1/TEX, L2, and DRAM traffic. |
| `SourceCounters` | Source/SASS/PTX correlated counters and hotspots. |
| `PmSampling`, `PmSampling_WarpStates` when listed | Timeline evidence for localized bubbles and long-tail phases. |

## Runtime And Launch Identity

| Metric or field | Use |
|---|---|
| Kernel name / demangled name | Make sure the intended kernel was captured. |
| `gpu__time_duration.sum` | Kernel duration. Compare against benchmark timing. |
| `launch__grid_size` | Detect underfilled grids and tiny workloads. |
| `launch__block_size` | Confirm expected CTA shape. |
| `launch__registers_per_thread` | Register pressure and occupancy limiter. |
| `launch__shared_mem_per_block_static` | Static shared-memory budget. |
| `launch__shared_mem_per_block_dynamic` | Dynamic shared-memory budget. |
| `launch__occupancy_limit_registers` | Register-limited occupancy signal. |
| `launch__occupancy_limit_shared_mem` | Shared-memory-limited occupancy signal. |
| `launch__occupancy_limit_blocks` | Block limit or cluster limit signal. |

## Speed-Of-Light Counters

| Metric | Interpretation |
|---|---|
| `sm__throughput.avg.pct_of_peak_sustained_elapsed` | Overall SM pipeline pressure. |
| `sm__inst_executed_pipe_tensor.avg.pct_of_peak_sustained_elapsed` | Tensor-pipe utilization for MMA kernels. |
| `sm__pipe_alu_cycles_active.avg.pct_of_peak_sustained_elapsed` | ALU/SFU/epilogue pressure. |
| `dram__throughput.avg.pct_of_peak_sustained_elapsed` | HBM pressure. |
| `lts__t_bytes.avg.pct_of_peak_sustained_elapsed` | L2 traffic pressure. |
| `gpu__compute_memory_throughput.avg.pct_of_peak_sustained_elapsed` | Coarse compute/memory roofline clue when present. |

High tensor and low memory usually means compute/tensor bound. High memory and
low SM usually means bytes, layout, or coalescing. Both low means latency,
scheduling, occupancy, barriers, launch overhead, or tail effects.

## Scheduler And Warp State

| Metric | Interpretation |
|---|---|
| `smsp__warps_eligible.avg.per_cycle_active` | Low values mean scheduler often lacks ready warps. |
| `sm__warps_active.avg.pct_of_peak_sustained_active` | Achieved active warp occupancy. |
| `smsp__inst_executed.avg.per_cycle_active` | Issue rate. |
| `smsp__warp_issue_stalled_long_scoreboard.sum` | Waiting on global/L2/texture memory dependency. |
| `smsp__warp_issue_stalled_short_scoreboard.sum` | Waiting on shared-memory or MIO dependency. |
| `smsp__warp_issue_stalled_barrier.sum` | CTA barrier or named barrier pressure. |
| `smsp__warp_issue_stalled_membar.sum` | Memory barrier/order pressure. |
| `smsp__warp_issue_stalled_mio_throttle.sum` | MIO pipe saturated, often shared/TMA/ldmatrix adjacent. |
| `smsp__warp_issue_stalled_lg_throttle.sum` | LSU/global memory issue throttle. |
| `smsp__warp_issue_stalled_math_pipe_throttle.sum` | Math pipe unavailable. |
| `smsp__warp_issue_stalled_no_instruction.sum` | Front-end starvation, divergence, huge code, or I-cache. |
| `smsp__warp_issue_stalled_imc_miss.sum` | Instruction-cache miss. |
| `smsp__warp_issue_stalled_dispatch_stall.sum` | Dispatch or pipeline issue pressure. |
| `smsp__warp_issue_stalled_drain.sum` | Pipeline drain, often low ILP or phase ending. |
| `smsp__warp_issue_stalled_not_selected.sum` | Warps ready but not selected; may be healthy if many ready warps exist. |

Normalize all `smsp__warp_issue_stalled_*` metrics into percentages. The
largest stall is not automatically the root cause, but it constrains the next
hypotheses.

## Memory Path

| Metric | Interpretation |
|---|---|
| `dram__bytes_read.sum`, `dram__bytes_write.sum` | Actual HBM bytes. |
| `dram__throughput.avg.pct_of_peak_sustained_elapsed` | HBM utilization. |
| `lts__t_bytes.sum` | L2 bytes. Compare with DRAM to infer L2 reuse. |
| `lts__t_sectors_srcunit_tex_op_read.sum` | L2 read sectors from texture/L1 path. |
| `l1tex__t_sectors_pipe_lsu_mem_global_op_ld.sum` | Global-load sectors at L1/TEX. |
| `l1tex__t_sectors_pipe_lsu_mem_global_op_st.sum` | Global-store sectors at L1/TEX. |
| `l1tex__t_requests_pipe_lsu_mem_global_op_ld.sum` | Global load request count. |
| `smsp__sass_average_data_bytes_per_sector_mem_global_op_ld.pct` | Global-load sector utilization when available. |
| `l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_ld.sum` | Shared-memory load bank conflicts. |
| `l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_st.sum` | Shared-memory store bank conflicts. |

If exact bank-conflict metric names differ, query `bank_conflict` and use the
closest shared-memory load/store conflict counter.

## Tensor Core, TMA, And Architecture Signals

Metric names for Hopper WGMMA and Blackwell tcgen05/TMEM/TMA counters vary by
NCU version. Search first:

```bash
ncu --query-metrics | grep -E 'wgmma|tcgen05|tensor|tma|mbarrier|tmem|cluster'
```

Use these signals when available:

| Signal | Interpretation |
|---|---|
| Tensor pipe active below expectation | Wrong dtype path, tile too small, epilogue heavy, or pipeline bubble. |
| TMA/mbarrier wait hotspot | Stage count, phase tracking, arrive/wait lifetime, or producer/consumer split. |
| TMEM load/store source hotspot | Epilogue drain or accumulator movement dominates. |
| 2-SM cooperative imbalance | CTA pair scheduling or cluster shape mismatch. |
| CLC/tail-wave evidence | Static scheduling leaves final wave underfilled. |
| WGMMA wait group hotspots on Hopper | Pipeline depth, wait group placement, or smem visibility. |

## Source Counters And PM Sampling

Use source and sampling evidence when aggregate counters do not explain the
shape:

| Evidence | Use |
|---|---|
| Source line with high stall samples | Map the bottleneck to actual code. |
| Inline PTX line with high samples | Fix PTX sequence, register reuse, or instruction selection. |
| PM-sampling timeline shows late low occupancy | Tail effect or uneven block lifetime. |
| PM-sampling timeline shows alternating TMA/MMA idle phases | Pipeline bubble or bad producer/consumer split. |
| One source line dominates long scoreboard | Target that load for prefetch/coalescing/layout change. |

## PTX And SASS Analysis

Use PTX/SASS analysis when SourceCounters point at an inline PTX block, when
the hotspot is a generated instruction sequence rather than a clean source
line, or when aggregate counters suggest front-end/codegen pressure.

Useful command patterns:

```bash
cuobjdump --dump-ptx <binary-or-extension> > profile-artifacts/<version>/kernel.ptx
cuobjdump --dump-sass <binary-or-extension> > profile-artifacts/<version>/kernel.sass
nvdisasm -g <kernel>.cubin > profile-artifacts/<version>/kernel.nvdisasm.sass
```

| PTX/SASS signal | Likely mechanism | Edit family |
|---|---|---|
| scalar `ld.global` where vector load was expected | alignment or aliasing not proven | add vector path, alignment guard, `__restrict__` |
| low bytes/sector plus scalar loads | poor coalescing or scalarization | vectorize/coalesce layout |
| local memory load/store in SASS | register spill | reduce tile/unroll/live range |
| repeated `cvt` / pack / unpack | wrong dtype or epilogue path | fix dispatch, accumulator, or quant layout |
| extra `bar.sync` / mbarrier ops | over-synchronization | simplify barrier lifetime or pipeline stages |
| `tcgen05` / `wgmma` sparse or absent in tensor kernel | wrong lowering path | force tensor path or change kernel stack config |
| large instruction window with `imc_miss` | I-cache pressure | split/specialize kernel, reduce unroll |
| unexpected cache modifiers | wrong cache policy | use explicit cache-policy primitive or inline PTX |

PTX/SASS evidence should not replace NCU counters. It explains the mechanism
behind a measured hotspot and should still end in one code edit.

## Bottleneck To Edit Mapping

| Dominant signal | First edit family |
|---|---|
| Long scoreboard | Prefetch, coalesce, vectorize, reduce footprint, shared staging. |
| Short scoreboard + bank conflicts | Pad/switch shared layout, swizzle, reduce smem traffic. |
| Barrier/membar/mbarrier | Fix phase tracking, stage count, arrive/wait lifecycle, warp specialization. |
| Tensor pipe low | Increase tile, choose tensor path, reduce epilogue, deepen pipeline. |
| DRAM high, SM low | Reduce bytes, fuse, vectorize, improve layout. |
| L2 high, DRAM low | Improve reuse, persistent tiles, cache policy. |
| Both SM and memory low | Occupancy, divergence, launch overhead, tail waves, PM timeline. |
| I-cache/no-instruction | Reduce unroll/code size, specialize or split kernels. |
| Tail waves | Persistent scheduling, CLC, tile splitting, shape-aware routing. |
