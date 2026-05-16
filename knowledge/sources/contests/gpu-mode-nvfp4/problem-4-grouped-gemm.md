---
id: contest-gpumode-p4
title: 'GPU Mode NVFP4 Hackathon - Problem 4: Grouped GEMM'
source_category: contest-report
architectures:
- sm100
- sm100a
tags:
- nvfp4
- grouped-gemm
- fp4
- block-scale
- tcgen05
- tmem
- tma
- moe
techniques:
- warp-specialization
- tile-scheduling
- pipeline-stages
- kernel-fusion
hardware_features:
- nvfp4
- fp4
- block-scale
- tcgen05
- tmem
- tma
- clc
kernel_types:
- grouped-gemm
- gemm
- moe
languages:
- cuda-cpp
- ptx
- cute-dsl
url: https://github.com/gpu-mode/reference-kernels
submissions:
- rank: 1
  participant: (reward hack - invalidated)
  score: 11.191us geomean (invalid)
  technique: 'Exploited eval harness: batched all 15 benchmark problems into first
    call, subsequent calls returned pre-computed results'
  submission_truth: unavailable
  code_unavailable_reason: Problem-4 rank-1 slot was invalidated after a reward-hacking
    incident; no legitimate kernel was archived, so there is no code to collect
- rank: 2
  participant: Simon (veitner)
  score: ~13.2us geomean
  technique: CLC dynamic tile scheduling, CUTLASS grouped GEMM with ptr-array interface,
    cross-group TMA prefetching
  submission_truth: unavailable
  code_unavailable_reason: Simon's grouped-GEMM submission posted in the GPU Mode
    Discord problem-4 thread; not republished publicly
- rank: 3
  participant: currybab
  score: ~13.5us geomean
  technique: Group packing for small-M experts, warp-specialized pipeline with group-boundary-aware
    scheduling
  submission_truth: unavailable
  code_unavailable_reason: currybab's grouped-GEMM submission posted in the GPU Mode
    Discord problem-4 thread; no public republish at collection time
---

# Problem 4: NVFP4 Grouped GEMM

## Problem Description

Multiple GEMMs with variable M dimensions but shared N and K, directly relevant to Mixture-of-Experts (MoE) inference on B200 GPUs:

```
for i in range(num_groups):
    C[i] = A[i] @ B[i]
    // A[i] shape: (M_i x K), variable M per group (tokens routed to expert i)
    // B[i] shape: (K x N), shared N and K across all groups
    // All in NVFP4 with block scaling
```

**Nature**: Compute-bound with load-balancing challenge. Variable M_i across groups means some experts receive many tokens while others receive few.

## Timeline

January 17 -- February 13, 2026. Final problem, weighted 40% (heaviest) for grand prize.

Grand Prize: Dell Pro Max with GB300 NVLink. Weighted scoring across all 4 problems: 10% / 20% / 30% / 40%.

## MoE Relevance

Grouped GEMM is the core compute kernel for MoE inference:
- DeepSeek-V3: 256 experts, tokens routed to 8 experts each
- Qwen3-Next: 512 experts, ~19 active per token
- Each expert's forward pass is a grouped GEMM where M_i = number of tokens routed to expert i

The variable M dimension creates significant load imbalance challenges. Some experts may receive hundreds of tokens while others receive zero.

## Optimization Techniques

### Dynamic Tile Scheduling with CLC

Cluster Launch Control (CLC) enables hardware-level dynamic work distribution:

```
// CLC dynamically assigns tiles to SMs based on availability
// Critical for grouped GEMM where groups have vastly different sizes
// Small groups (M_i < tile_M) waste compute with static scheduling
// CLC balances load across SMs at hardware speed
```

Without CLC, static tile assignment leaves SMs idle when their assigned group finishes early. CLC redistributes remaining tiles to available SMs.

### Group Packing and Scheduling

Multiple small groups can be packed into shared tile grids:

```
// Naive: one kernel launch per group (high launch overhead)
// Better: single kernel, all groups in one grid
// Best: tile scheduler that packs small groups efficiently

// For groups with M_i < tile_M (e.g., M_i=3, tile_M=128):
// Pack multiple small groups into shared tiles
// or use specialized small-M kernels
```

### Warp Specialization for Variable Workloads

The warp specialization pattern adapts to variable group sizes:

- **TMA warps**: Prefetch tiles for the next group while current group computes
- **Compute warps**: Execute tcgen05.mma on current tiles
- **Scheduling warps**: Track group boundaries and manage tile assignment

### CUTLASS Grouped GEMM Schedule

```cpp
// CUTLASS 4.x grouped GEMM for NVFP4 on SM100
using KernelSchedule = cutlass::gemm::KernelPtrArrayTmaWarpSpecialized1SmNvf4Sm100;

// Ptr-array interface: each group has its own A, B, C pointers
// M array specifies per-group row count
// N and K shared across all groups
using GemmKernel = cutlass::gemm::kernel::GemmUniversal<
    ProblemShape,         // GroupedGemmProblemShape
    CollectiveMainloop,
    CollectiveEpilogue
>;
```

### Pipeline Overlap Across Groups

When processing multiple groups sequentially within a CTA:

```
// While computing group[i] tiles:
//   TMA prefetches group[i+1] weight tiles
//   Previous group[i-1] epilogue writes complete
// This hides group-transition latency
```

## The Reward Hack

A notable submission to Problem 4 reported 11.191us (~2us ahead of the next competitor):

**Mechanism**:
1. **Correctness phase**: The evaluation harness clones data objects, so the real kernel runs correctly on fresh data
2. **Timing phase**: The harness reuses the same data objects. The exploit detects first call, fires a single fused super-batch covering all 15 benchmark problems (all 120 groups across all configs). Subsequent calls 2-15 detect pre-computed results and return immediately

**Impact**: Led to improvements in the FlashInfer-Bench evaluation methodology for the MLSys 2026 contest. The incident demonstrated that kernel benchmarking harnesses must isolate timing runs from state carried across invocations.

## Performance Data

| Approach | Approximate Time |
|----------|-----------------|
| Reward hack submission | 11.191us (invalid) |
| Legitimate top performers | ~13-14us range |
| CUTLASS baseline | ~15us range |

Exact legitimate leaderboard data not fully published due to the hack incident.

## Key Challenges

1. **Load imbalance**: Expert routing creates highly variable M_i values. Some groups may have M_i=0 (no tokens routed)
2. **Small-group efficiency**: Groups with M_i < tile_M waste compute on padding
3. **Group-transition overhead**: Switching between groups incurs pointer arithmetic and descriptor updates
4. **TMA alignment**: Each group's A matrix must be 128-byte aligned for TMA, requiring careful memory layout
5. **TMEM reuse**: Accumulator tiles in TMEM must be cleared between groups

## Sources

- [gpu-mode/reference-kernels](https://github.com/gpu-mode/reference-kernels) (`/problems/nvidia/nvfp4_group_gemm/`)
- [Reward Hack Writeup](https://www.gpumode.com/news/reward-hacking-nvfp4)
- [GPU MODE Hackathon (Luma)](https://luma.com/9n27uem4)
- [NVIDIA Forums Announcement](https://forums.developer.nvidia.com/t/join-us-for-the-blackwell-nvfp4-kernel-hackathon-with-nvidia-and-gpu-mode/350092)
