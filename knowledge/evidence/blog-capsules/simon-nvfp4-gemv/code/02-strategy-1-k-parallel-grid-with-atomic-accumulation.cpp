// Extracted from sources/blogs/simon-nvfp4-gemv.md by scripts/extract_blog_code.py
// Heading: # NVFP4 GEMV and Improved NVFP4 GEMV (Simon Veitner) > ## Key Code > ### Strategy 1 — K-parallel grid with atomic accumulation
// Original fence language: cpp
// See evidence/blog-capsules/simon-nvfp4-gemv/code/ORIGIN.yaml for origin + license metadata.

// Launch one CTA per (M-tile, K-tile); accumulate partial products into a
// global FP32 buffer via atomicAdd, then cast to FP16 in a second pass.
__global__ void nvfp4_gemv_k_parallel(
    const __nv_fp4_e2m1* A, const __nv_fp8_e4m3* SFA,
    const __nv_fp4_e2m1* B, const __nv_fp8_e4m3* SFB,
    float* accum_f32, int K_TILES)
{
    int m_tile = blockIdx.x;
    int k_tile = blockIdx.y;
    float partial = nvfp4_dot_product(A, SFA, B, SFB, m_tile, k_tile);
    atomicAdd(&accum_f32[m_tile], partial);
}
