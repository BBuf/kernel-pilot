// Extracted from sources/blogs/deepgemm.md by scripts/extract_blog_code.py
// Heading: ## Key Code > ### SM100 path — tcgen05.mma with UE8M0 block scaling
// Original fence language: cpp
// See evidence/blog-capsules/deepgemm/code/ORIGIN.yaml for origin + license metadata.

// On Blackwell, tcgen05.mma consumes UE8M0 scale factors directly.
// 4 UE8M0 values pack into a single uint32; TMEM accumulates in full FP32
// precision so no CUDA-core promotion is needed.
uint32_t packed_scales = pack_ue8m0(sf[0], sf[1], sf[2], sf[3]);
asm volatile(
    "tcgen05.mma.cta_group::1.kind::f8f6f4.block_scale "
    "[%0], %1, %2, [%3], %4, 1;\n"
    :: "r"(tmem_acc), "l"(desc_a), "l"(desc_b),
       "r"(sf_tmem_addr), "r"(0));
