// Extracted from sources/blogs/simon-nvfp4-gemv.md by scripts/extract_blog_code.py
// Heading: # NVFP4 GEMV and Improved NVFP4 GEMV (Simon Veitner) > ## Key Code > ### Reference core computation (Part 1)
// Original fence language: cpp
// See evidence/blog-capsules/simon-nvfp4-gemv/code/ORIGIN.yaml for origin + license metadata.

// NVFP4 GEMV: FP4 values are decoded to FP32 via their per-block FP8 scale,
// then multiplied against a decoded B element + its FP8 scale. Accumulation
// stays in FP32. Simon's reference kernel does this in a CuTe register tile:
for (int i = 0; i < TILES_K; i++) {
    float a = decode_nvfp4(tArA[i]) * decode_fp8(tArSFA[i]);
    float b = decode_nvfp4(tBrB[i]) * decode_fp8(tBrSFB[i]);
    res += a * b;                // FP32 accumulation
}
