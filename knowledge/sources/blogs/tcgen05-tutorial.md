---
id: blog-tcgen05-tutorial
title: tcgen05 for dummies
author: Gau Nernst
url: https://gau-nernst.github.io/tcgen05/
source_category: community-note
architectures:
- sm100
tags:
- tcgen05
- tmem
- swizzling
- pipeline-stages
- persistent-kernel
- warp-specialization
- mbarrier
- cuda-cpp
- ptx
retrieved_at: 2026-04-16
artifact_dir: evidence/blog-capsules/tcgen05-tutorial/code
---

## Summary

Step-by-step tutorial building a Blackwell GEMM kernel from scratch in plain CUDA C++ with PTX, achieving 98% of cuBLAS performance.

## Performance Progression
- Basic kernel: 255 TFLOPS (17%)
- 128B swizzling: 695 TFLOPS (46%)
- Pipelining: 940 TFLOPS (62%)
- Warp specialization: ~1200 TFLOPS (80%)
- Persistent kernel: 1476 TFLOPS (98%) vs 1507 cuBLAS

## Key Findings
- tcgen05.mma operates directly on shared memory — no ldmatrix needed
- TMEM: 128×512 capacity, 32-bit elements, must alloc/dealloc
- mbarrier synchronization with phases and parity bits
- "Tensor Core programming on Blackwell is easier than previous generations"
- 128B swizzling alone gives 2.7× speedup

## Key Code

### Basic tcgen05.mma kernel (17% of peak)

```cuda
// The naive building block: one-thread-launched tcgen05.mma into TMEM.
// ~255 TFLOPS on B200 (17% of peak).
__shared__ uint32_t tmem;
if (threadIdx.x == 0) {
    asm volatile("tcgen05.alloc.cta_group::1.sync.aligned.shared::cta.b32 [%0], 256;\n"
                 :: "r"(&tmem));
}
__syncthreads();

for (int k = 0; k < K; k += K_TILE) {
    cp_async(smem_a, A + k);
    cp_async(smem_b, B + k);
    cp_async_commit();
    cp_async_wait<0>();
    __syncthreads();
    if (threadIdx.x == 0) {
        asm volatile("tcgen05.mma.cta_group::1.kind::f16 [%0], %1, %2, %3, 1;\n"
                     :: "r"(tmem), "l"(desc_a), "l"(desc_b), "r"(0));
    }
}
```

### 128B swizzling (46% of peak)

```cuda
// XOR-swizzled SMEM layout eliminates bank conflicts on MMA load;
// 128-byte granularity gives 2.7x speedup on its own.
template <int N_K>
__device__ void swizzle_128b_store(half* smem, const half* gmem, int k_tile) {
    int tid = threadIdx.x;
    int col = (tid * 8) % N_K;
    int row = (tid * 8) / N_K;
    int swizzled = col ^ ((row & 0x7) << 4);      // 8-lane XOR swizzle
    *reinterpret_cast<uint4*>(&smem[row * N_K + swizzled]) =
        *reinterpret_cast<const uint4*>(&gmem[k_tile + row * N_K + col]);
}
```

### Pipelining + mbarrier phases (62% of peak)

```cuda
// Multi-stage TMA load pipeline. mbarrier phase bits toggle every STAGES
// arrivals so try_wait.parity can distinguish consecutive rounds without a
// counter rollover.
constexpr int STAGES = 4;
__shared__ uint64_t mbar_full[STAGES];
__shared__ uint64_t mbar_empty[STAGES];

if (threadIdx.x == 0) {
    for (int i = 0; i < STAGES; i++) {
        asm volatile("mbarrier.init.shared::cta.b64 [%0], 1;\n" :: "r"(&mbar_full[i]));
        asm volatile("mbarrier.init.shared::cta.b64 [%0], 1;\n" :: "r"(&mbar_empty[i]));
    }
}
__syncthreads();

int phase = 0;
for (int k = 0; k < K_TILES; k++) {
    int stage = k % STAGES;
    if (k >= STAGES) {
        asm volatile("mbarrier.try_wait.parity.shared::cta.b64 _, [%0], %1;\n"
                     :: "r"(&mbar_empty[stage]), "r"(phase));
    }
    tma_load(smem_a[stage], gmem_a, k);
    asm volatile("mbarrier.arrive.shared::cta.b64 _, [%0];\n"
                 :: "r"(&mbar_full[stage]));
    if ((k + 1) % STAGES == 0) phase ^= 1;
}
```
