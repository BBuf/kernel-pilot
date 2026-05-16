---
id: doc-cutlass-clc
title: "CUTLASS Cluster Launch Control (CLC) Documentation"
url: https://docs.nvidia.com/cutlass/latest/media/docs/cpp/blackwell_cluster_launch_control.html
source_category: official-doc
architectures: [sm100, sm100a]
tags: [clc, cluster, tile-scheduling, persistent-kernel, mbarrier, 2sm-cooperative, pipeline-stages, gemm]
retrieved_at: 2026-04-17
---

# CUTLASS Cluster Launch Control (CLC) Documentation

## Overview

Cluster Launch Control (CLC) is a Blackwell hardware feature enabling dynamic tile scheduling for persistent GEMM kernels. Rather than static tile distribution where each thread block computes a predetermined output tile, CLC launches a grid of thread blocks and dynamically allocates work based on SM resource availability. Introduced in CUTLASS 3.8.0, CLC eliminates workload imbalance when SMs have uneven availability (e.g., partial SM allocation with Green Context or concurrent kernel execution).

## Core Mechanism

### Static vs Dynamic Scheduling

**Static Persistent Kernels (Hopper approach)**:
- Each thread block is pre-assigned a set of output tiles at launch
- Suffers from workload imbalance when SMs are occupied by other work
- Idle SM stalls reduce overall throughput

**CLC Dynamic Scheduling (Blackwell)**:
- Launches a grid containing as many thread blocks as there are output tiles
- Thread blocks query CLC to receive their next tile assignment at runtime
- Tiles are allocated only to available workers
- Prevents idle SM stalls from uneven workload distribution

### ClcID System

Grid coordinates are treated as ClcID identifiers. Each ClcID represents one output tile. The system guarantees that all coordinates are processed through one of two paths:
1. Direct worker launch (for the initial wave)
2. Scheduler query response (for subsequent tiles)

## Pipeline Architecture

### Key Configuration Parameters

| Parameter | Value | Description |
|---|---|---|
| Transaction size | 16 bytes | Size of CLC response stored in SMEM |
| Pipeline depth | 3 | Number of overlapped CLC operation waves |
| Producer arrival count | 1 | Single scheduler warp thread |
| Consumer arrival count | Total threads of consuming warps | All warps needing ClcIDs |
| Producer block ID | 0 | First CTA in cluster acts as scheduler |

### Pipeline Depth = 3

The CLC pipeline uses depth 3 to overlap CLC operations across multiple waves for latency hiding. This means up to 3 CLC queries can be in-flight simultaneously, with responses arriving asynchronously.

## Producer-Consumer Architecture

### Producer: Scheduler Warp
- Warp 1 of the 0th CTA in the cluster acts as the scheduler
- Issues CLC queries via `advance_to_next_work()`
- Produces ClcID responses into shared memory
- The scheduler warp is also its own consumer (to detect grid completion signals)

### Consumers: All Computation Warps
- MMA warps (tensor core computation)
- Mainloop load warps (TMA data fetching)
- Epilogue load warps
- Epilogue store warps
- All consume ClcID assignments via `get_current_work()`

### Asynchronous Pipeline Management

CLC queries are pipelined using `PipelineCLCFetchAsync`, which manages the producer-consumer relationship:
1. Producer issues query (stores response address in SMEM)
2. CLC hardware writes 16-byte response to specified SMEM address
3. Consumer warps wait on barrier for response availability
4. Consumer reads ClcID and begins processing the assigned tile
5. Producer can issue next query before consumers finish current tile

## Cluster Granularity

CLC operates on cluster granularity, not individual CTA granularity:
- A 2x2 persistent worker cluster consumes 2x2 = 4 ClcIDs per query
- This aligns with Blackwell's 2SM cooperative execution model
- Cluster shapes can be specified as preferred or fallback configurations

### Preferred and Fallback Cluster Shapes

The CLC API supports specifying:
- **Preferred cluster shape**: The optimal configuration (e.g., 2x1 for 2SM cooperative)
- **Fallback cluster shape**: Used when the preferred shape cannot be satisfied due to resource constraints

## Core CUTLASS Classes

### PipelineCLCFetchAsync
Manages the asynchronous CLC query pipeline with producer-consumer semantics. Key operations:
- Initialize pipeline with depth, transaction bytes, and arrival counts
- Producer phase: issue CLC queries and signal barriers
- Consumer phase: wait on barriers and read responses

### PersistentTileSchedulerSm100
Implements the tile scheduling logic:
- `advance_to_next_work()`: Issues the next CLC query (producer side)
- `get_current_work()`: Retrieves the current tile assignment (consumer side)
- Handles grid completion detection
- Manages stream-K decomposition for load balancing

## Integration with GEMM Kernels

CLC is used in CUTLASS Blackwell persistent GEMM kernels:
1. Kernel launches with grid size = number of output tiles
2. Initial tiles are assigned directly by CLC hardware
3. After processing a tile, each cluster queries for the next tile
4. Grid completes when all ClcIDs have been consumed and processed
5. Supports both tile-parallel and stream-K decomposition

## Comparison with Hopper Scheduling

| Aspect | Hopper (Static) | Blackwell (CLC) |
|---|---|---|
| Tile assignment | Pre-computed at launch | Dynamic at runtime |
| Load balancing | Fixed, may be uneven | Adaptive to SM availability |
| Overhead | Zero runtime overhead | CLC query latency (hidden by pipeline) |
| Green Context | Poor utilization | Efficient partial SM use |
| Stream-K | Software-managed | Hardware-assisted |
| Cluster support | Limited | Native preferred/fallback shapes |
