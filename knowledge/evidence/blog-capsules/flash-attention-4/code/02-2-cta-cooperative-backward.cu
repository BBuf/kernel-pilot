// Extracted from sources/blogs/flash-attention-4.md by scripts/extract_blog_code.py
// Heading: ## Key Code > ### 2-CTA cooperative backward
// Original fence language: cuda
// See evidence/blog-capsules/flash-attention-4/code/ORIGIN.yaml for origin + license metadata.

// 2-CTA cooperative backward: paired CTAs in a cluster share a single TMEM
// accumulator half, halving SMEM traffic for dK/dV accumulation.
asm volatile(
    "tcgen05.mma.cta_group::2.kind::f16 [%0], %1, %2, %3, 1;"
    : : "r"(tmem_acc_shared), "l"(desc_a), "l"(desc_b), "r"(0));
