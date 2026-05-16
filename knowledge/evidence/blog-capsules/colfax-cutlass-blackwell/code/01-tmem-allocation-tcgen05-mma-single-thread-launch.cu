// Extracted from sources/blogs/colfax-cutlass-blackwell.md by scripts/extract_blog_code.py
// Heading: ## Key Code > ### TMEM allocation + tcgen05.mma (single-thread launch)
// Original fence language: cuda
// See evidence/blog-capsules/colfax-cutlass-blackwell/code/ORIGIN.yaml for origin + license metadata.

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
