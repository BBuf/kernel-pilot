---
id: blog-colfax-cutlass
title: 'Colfax CUTLASS Tutorial: GEMM Kernels Using Tensor Memory for Blackwell'
author: Colfax Research
url: https://research.colfax-intl.com/cutlass-tutorial-writing-gemm-kernels-using-tmem-for-nvidia-blackwell-gpus/
source_category: community-note
architectures:
- sm100
tags:
- tcgen05
- tmem
- cute-dsl
- warp-specialization
- 2sm-cooperative
retrieved_at: 2026-04-16
artifact_dir: evidence/blog-capsules/colfax-cutlass-blackwell/code
---

## Summary

Detailed tutorial on CUTLASS abstraction for Blackwell UMMA (tcgen05.mma) with sub-byte GEMM support.

## Key Content
- UMMA replaces WGMMA: register-free operation, single-thread launch, built-in block scaling
- TMEM: 512 columns × 128 rows of 32-bit cells (256KB/SM)
- 32-bit addressing: bits 31-16 = lane ID, bits 15-0 = column
- CUTLASS two-level abstraction: MMA_Atom (PTX wrapper) + MMA_Traits (CuTe layouts)
- Architectural progression: Volta → Hopper TMA → Blackwell TMEM+UMMA
- Sub-byte GEMM tutorial covering NVFP4, MXFP4, block scaling

## Key Code

### TMEM allocation + tcgen05.mma (single-thread launch)

```cuda
// UMMA on Blackwell: one thread drives the MMA for the whole CTA.
// Accumulator lives in TMEM, not registers.
__shared__ uint32_t tmem_addr;

if (threadIdx.x == 0) {
    // Allocate 128 rows × 256 cols of TMEM for the accumulator
    asm volatile("tcgen05.alloc.cta_group::1.sync.aligned.shared::cta.b32 [%0], 256;\n"
                 :: "r"(&tmem_addr));
}
__syncthreads();

// Issue UMMA: A and B live in SMEM, C accumulates into TMEM
if (threadIdx.x == 0) {
    asm volatile(
        "tcgen05.mma.cta_group::1.kind::f16 [%0], %1, %2, %3, 1;\n"
        :: "r"(tmem_addr), "l"(desc_a), "l"(desc_b), "r"(0));
}
```

### TMEM load into registers for epilogue

```cuda
// Epilogue warps drain TMEM → registers using tcgen05.ld
// Each warp loads 32 columns (=128 bytes) at a time.
float reg[4];
asm volatile(
    "tcgen05.ld.sync.aligned.32x32b.x4.b32 "
    "{%0, %1, %2, %3}, [%4];\n"
    : "=f"(reg[0]), "=f"(reg[1]), "=f"(reg[2]), "=f"(reg[3])
    : "r"(tmem_addr + warp_col_offset));
```

### CUTLASS MMA_Atom wrapping

```cpp
// The CUTLASS two-level abstraction: MMA_Atom wraps the PTX intrinsic,
// MMA_Traits maps logical MxNxK shapes to TMEM addressing.
using Atom = cute::MMA_Atom<cute::SM100_MMA_F16BF16_SS<
    cute::half_t, cute::half_t, float,     // A, B, C types
    128, 256,                               // MxN tile
    cute::UMMA::Major::K, cute::UMMA::Major::K
>>;
```
