// Extracted from sources/blogs/flash-attention-4.md by scripts/extract_blog_code.py
// Heading: ## Key Code > ### Software exp (Cody-Waite + Horner)
// Original fence language: cuda
// See evidence/blog-capsules/flash-attention-4/code/ORIGIN.yaml for origin + license metadata.

// Software-emulated exp2(x) using Cody-Waite range reduction and a
// Horner-scheme polynomial, Sollya-optimized coefficients. Lets FA-4
// overlap the exp path with tcgen05.mma because it stays off the SFU.
__device__ __forceinline__ float sw_exp2(float x) {
    // Range reduction: x = n + r, with n = round(x), r in [-0.5, 0.5]
    int n = __float2int_rn(x);
    float r = x - (float)n;
    // Horner-scheme polynomial for 2^r, r in [-0.5, 0.5]
    float p = 0x1.62e430p-1f;                // ~ ln(2)
    p = fmaf(p, r, 0x1.ebfc1ep-3f);
    p = fmaf(p, r, 0x1.c6af98p-5f);
    p = fmaf(p, r, 0x1.3b2c9cp-7f);
    p = fmaf(p, r, 0x1.62e43ap-10f);
    float y = fmaf(r, p, 1.0f);
    // Scale by 2^n via direct FP32 bit manipulation
    int bits = __float_as_int(y) + (n << 23);
    return __int_as_float(bits);
}
