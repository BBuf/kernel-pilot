---
id: blog-k-search-kernel-generation
title: "K-Search: LLM Kernel Generation via Co-Evolving Intrinsic World Model"
author: Shiyi Cao et al.
url: https://arxiv.org/abs/2602.19128
source_category: community-note
architectures: [sm100, sm100a]
tags: [jit-compilation, gemm, attention, moe, mla, kernel-fusion]
retrieved_at: 2026-04-17
---

# K-Search: LLM Kernel Generation via Co-Evolving Intrinsic World Model

## Overview

K-Search (arXiv 2602.19128) introduces a paradigm shift in automated GPU kernel optimization by treating LLMs as world models rather than stochastic code generators. The system explicitly decouples high-level algorithmic planning from low-level program instantiation, enabling navigation of complex non-monotonic optimization paths. Evaluated on FlashInfer kernels (GQA, MLA, MoE), K-Search achieves an average 2.10x improvement over state-of-the-art evolutionary search, with up to 14.3x gains on complex MoE kernels. On the GPU Mode TriMul task, it achieves state-of-the-art 1030 us on H100.

## Core Problem

Existing automated kernel optimization approaches treat LLMs merely as stochastic code generators within heuristic-guided evolutionary loops. These methods struggle with complex kernels requiring coordinated, multi-step structural transformations because they:
- Lack explicit planning capabilities
- Frequently discard promising strategies due to inefficient intermediate implementations
- Cannot navigate non-monotonic optimization paths (where performance temporarily degrades before improving)

## K-Search Methodology

### Three-Phase Iterative Process

**Phase 1: Action Selection**
- Retrieves the highest-priority pending optimization from the search frontier
- Maintains an explicit search tree with "Closed nodes" (completed actions with attached programs) and "Open nodes" (pending optimization intents)

**Phase 2: Program Instantiation**
- Samples concrete implementations via stochastic policy
- Continues until stagnation (K consecutive failures)
- Separates the "what to optimize" from "how to implement it"

**Phase 3: World Model Co-Evolution**
- LLM analyzes execution trajectories from Phase 2
- Performs tree edits on the search frontier:
  - **Insert**: Add new optimization hypotheses
  - **Update**: Adjust priority scores based on observed results
  - **Prune**: Remove infeasible branches
- The world model improves as it observes more optimization trajectories

### Key Innovation: Decoupled Planning

Rather than searching directly in program space, K-Search maintains a separate optimization intent tree. This allows the system to:
- Keep promising optimization strategies alive even when initial implementations fail
- Compose multiple optimizations that individually degrade performance but jointly improve it
- Learn from failed implementations to refine future planning

## Experimental Results

### FlashInfer Kernel Benchmarks

| Kernel Type | vs OpenEvolve | vs ShinkaEvolve |
|---|---|---|
| Average across all | 2.10x | 2.21x |
| Complex MoE kernels | up to 14.3x | -- |
| MLA prefill tasks | 2.95-5.10x | -- |
| GQA paged decode | significant | -- |

### GPU Mode TriMul Competition
- **K-Search result**: 1030 us on H100
- Surpasses both prior automated solutions and human-designed kernels
- State-of-the-art on this benchmark

### Evaluated Kernel Types
- **GQA Paged Decode** (Hopper): Multi-head query fusion with vectorized memory access
- **MLA Paged Prefill/Decode** (Hopper): Causal attention with split KV handling
- **FP8 MoE** (Blackwell): Irregular routing with expert load balancing

## Case Study: MLA Optimization

The MLA case study demonstrates co-evolution effectiveness:
1. Initial fusion hypotheses are generated
2. Refinements like "register_resident_rescaling" are proposed through world model updates
3. Underperforming branches get pruned
4. By round 102, the world model proposes composable optimizations (split-K applied conditionally) that yield optimal performance
5. These insights would be impossible through direct program-space search alone

## Technical Advantages Over Evolutionary Search

1. **Resilience to transient bugs**: Failed implementations don't kill promising strategies
2. **Non-monotonic navigation**: Can traverse performance valleys to reach global optima
3. **Composable optimizations**: Discovers multi-step transformations that evolutionary methods miss
4. **Learning from failure**: World model improves from both successes and failures
5. **Explicit planning**: Separates "what" from "how", reducing the search space

## Significance for Blackwell Kernel Development

- Demonstrates that automated kernel generation can match or exceed human experts
- FP8 MoE kernel optimization on Blackwell is a key evaluation target
- The approach is complementary to manual kernel engineering -- it can discover non-obvious optimization compositions
- Code available at https://github.com/caoshiyi/K-Search
