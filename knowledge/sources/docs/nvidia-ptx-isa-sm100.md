---
id: doc-ptx-isa-sm100
title: "PTX ISA SM100 Instructions Reference"
url: https://docs.nvidia.com/cuda/parallel-thread-execution/
source_category: official-doc
architectures: [sm100, sm100a]
tags: [ptx, tcgen05, tmem, clc, tma, nvfp4, fp4, fp8, fp6, block-scale, mbarrier]
retrieved_at: 2026-04-16
---

# PTX ISA SM100 Instructions Reference

## Overview

PTX ISA 8.7+ introduces SM100-specific instructions for Blackwell's tensor core (tcgen05), tensor memory (TMEM), cluster launch control (CLC), and sub-byte data type conversions. This page summarizes the key new instructions relevant to kernel optimization.

## tcgen05.mma Instructions

### Syntax

```asm
tcgen05.mma.cta_group::{1|2}.kind::{dtype}
    [tmem_addr],        // Destination: TMEM address
    [smem_desc_a],      // Source A: SMEM descriptor
    [smem_desc_b];      // Source B: SMEM descriptor
```

### CTA Group Variants

| cta_group | Description | Max M |
|---|---|---|
| `cta_group::1` | Single-CTA (1-SM) operation | 128 |
| `cta_group::2` | Cooperative 2-CTA (2-SM) operation | 256 |

### Data Type Variants (kind)

| kind | A type | B type | Accumulator | Shape (1-CTA) |
|---|---|---|---|---|
| `kind::f16` | FP16/BF16 | FP16/BF16 | FP32 | m128n256k16 |
| `kind::tf32` | TF32 | TF32 | FP32 | m128n256k8 |
| `kind::i8` | INT8 | INT8 | INT32 | m128n256k32 |
| `kind::f8f6f4` | FP8/FP6/FP4 | FP8/FP6/FP4 | FP32 | m128n256k32+ |
| `kind::mxf8` | MX FP8 | MX FP8 | FP32 | m128n256k32 |
| `kind::mxf4nvf4` | NVFP4 | NVFP4 | FP32 | m128n256k64 |

### Key Differences from Hopper wgmma

```asm
// Hopper (SM90): warpgroup scope, register accumulators
wgmma.mma_async.sync.aligned.m64n256k16.f32.bf16.bf16
    {d0..d127},     // 128 register accumulators
    [desc_a],
    [desc_b];

// Blackwell (SM100): single-thread, TMEM accumulators
tcgen05.mma.cta_group::1.kind::f16
    [tmem_addr],    // TMEM accumulator (no register pressure)
    [smem_desc_a],
    [smem_desc_b];
```

## TMEM Instructions

### Allocation and Deallocation

```asm
// Allocate TMEM rows for a CTA group
tcgen05.alloc.cta_group::1 [tmem_base], num_rows;

// Deallocate TMEM rows
tcgen05.dealloc.cta_group::1 [tmem_base], num_rows;
```

### Load/Store (TMEM <-> Registers)

```asm
// Load from TMEM to registers (for epilogue)
tcgen05.ld.16x256b [reg_dest], [tmem_src];

// Store from registers to TMEM
tcgen05.st.16x256b [tmem_dest], [reg_src];
```

### TMEM Layout

```
TMEM per SM: 128 rows x 512 columns x 32-bit
Total: 128 * 512 * 4 bytes = 256 KB

Row addressing: tmem_base + row_offset
Column mapping: determined by MMA instruction variant
```

## CLC Instructions

### Dynamic Tile Scheduling

```asm
// Signal tile arrival (producer done loading data)
clc.arrive.group::1;

// Wait for tile assignment (consumer waits for work)
clc.wait.group::1;

// CLC replaces manual tile queues:
// - Hardware maintains work queue
// - Tiles assigned to SMs as they become available
// - Eliminates tail effects and load imbalance
```

## TMA Instructions (SM100 Enhanced)

### Async Bulk Copy

```asm
// TMA load: global -> shared memory
cp.async.bulk.tensor.2d.dst_shared::cta.src_global.tile.mbarrier::complete_tx::bytes
    [smem_addr], [tma_desc, {coord_x, coord_y}], [mbarrier];

// TMA store: shared memory -> global
cp.async.bulk.tensor.2d.dst_global.src_shared::cta.tile
    [tma_desc, {coord_x, coord_y}], [smem_addr];
```

### TMA Multicast

```asm
// Multicast TMA load to multiple CTAs in cluster
cp.async.bulk.tensor.2d.dst_shared::cluster.src_global.tile.mbarrier::complete_tx::bytes
    [smem_addr], [tma_desc, {coord_x, coord_y}], [mbarrier], multicast_mask;
```

### Alignment Requirements

- TMA descriptors: 128-byte aligned base address
- Shared memory buffers: 128-byte aligned for TMA targets
- Global memory source: 128-byte aligned

## FP4/FP8 Conversion Instructions

### FP4 (E2M1) Conversions

```asm
// Pack two FP16 values into FP4x2
cvt.rn.e2m1x2.f16x2 %fp4_packed, %f16x2_val;

// Unpack FP4x2 to two FP16 values
cvt.rn.f16x2.e2m1x2 %f16x2_result, %fp4_packed;
```

### Byte Unpacking for FP4

```asm
// Efficient byte unpacking (faster than bitwise extraction)
mov.b32 {tmp0, tmp1, tmp2, tmp3}, %packed_word;
// Splits 32-bit word into 4 bytes without shift/mask overhead
// Critical for FP4 decoding performance
```

### FP8 Conversions

```asm
// FP8 E4M3 to FP16
cvt.rn.f16.e4m3 %f16_result, %fp8_val;

// FP16 to FP8 E4M3
cvt.rn.e4m3.f16 %fp8_result, %f16_val;

// FP8 E5M2 conversions (similar syntax)
cvt.rn.f16.e5m2 %f16_result, %fp8_val;
```

## Cache Control Instructions

### Load Qualifiers (Critical for Memory-Bound Kernels)

```asm
// Default: normal caching
ld.global %val, [addr];

// L1 no-allocate: bypass L1 for streaming data
ld.global.L1::no_allocate %val, [addr];

// L1 evict-last: keep in L1 as long as possible (for reused data)
ld.global.L1::evict_last %val, [addr];

// Non-coherent read-only (used by DeepEP for communication)
ld.global.nc.L1::no_allocate.L2::256B %val, [addr];
```

### Vectorized Loads

```asm
// 64-bit vector load
ld.global.v2.u32 {r0, r1}, [addr];

// 128-bit vector load
ld.global.v2.u64 {r0, r1}, [addr];

// 256-bit vector load
ld.global.v4.u64 {r0, r1, r2, r3}, [addr];
```

## Synchronization Primitives

### mbarrier (Memory Barrier)

```asm
// Initialize mbarrier
mbarrier.init.shared.b64 [mbar], thread_count;

// Arrive at mbarrier (producer signals completion)
mbarrier.arrive.shared.b64 %phase, [mbar];

// Wait on mbarrier (consumer waits for data)
mbarrier.try_wait.shared.b64 %pred, [mbar], %phase;
```

### Async Pipeline Coordination

```asm
// TMA + mbarrier pipeline pattern:
// 1. Producer issues TMA load with mbarrier
// 2. Consumer waits on mbarrier
// 3. Consumer processes data while producer issues next load
// 4. Repeat for multi-stage pipeline
```

## Sources

- [PTX ISA Reference](https://docs.nvidia.com/cuda/parallel-thread-execution/)
- [CUDA 13.0 Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/)
- [NVIDIA Blackwell Tuning Guide](https://docs.nvidia.com/cuda/blackwell-tuning-guide/)
