// Extracted from sources/blogs/tcgen05-tutorial.md by scripts/extract_blog_code.py
// Heading: ## Key Code > ### Basic tcgen05.mma kernel (17% of peak)
// Original fence language: cuda
// See evidence/blog-capsules/tcgen05-tutorial/code/ORIGIN.yaml for origin + license metadata.

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
