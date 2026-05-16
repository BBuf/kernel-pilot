// Extracted from sources/blogs/tcgen05-tutorial.md by scripts/extract_blog_code.py
// Heading: ## Key Code > ### Pipelining + mbarrier phases (62% of peak)
// Original fence language: cuda
// See evidence/blog-capsules/tcgen05-tutorial/code/ORIGIN.yaml for origin + license metadata.

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
