// Extracted from sources/blogs/flashmla.md by scripts/extract_blog_code.py
// Heading: ## Key Code > ### Sparse-MLA KV-retrieval kernel (V3.2)
// Original fence language: cuda
// See evidence/blog-capsules/flashmla/code/ORIGIN.yaml for origin + license metadata.

// Sparse MLA selects top-k KV positions per query before running the dense
// MLA kernel on just those positions. Retrieval uses FP8 dot products with
// per-token scale factors.
__global__ void sparse_mla_topk(
    const __nv_fp8_e4m3* Q, const __nv_fp8_e4m3* K,
    const float* Q_scale, const float* K_scale,
    int* topk_idx, float* topk_score,
    int N, int K_DIM, int TOPK)
{
    int q_tile = blockIdx.x;
    float scores[N];
    for (int n = 0; n < N; n++) {
        float s = 0.f;
        for (int k = 0; k < K_DIM; k++) {
            s += decode_fp8(Q[q_tile * K_DIM + k]) * Q_scale[q_tile]
               * decode_fp8(K[n * K_DIM + k]) * K_scale[n];
        }
        scores[n] = s;
    }
    warp_topk_select(scores, N, topk_idx + q_tile * TOPK,
                     topk_score + q_tile * TOPK, TOPK);
}
