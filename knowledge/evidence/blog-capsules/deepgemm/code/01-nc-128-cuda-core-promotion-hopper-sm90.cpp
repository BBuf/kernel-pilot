// Extracted from sources/blogs/deepgemm.md by scripts/extract_blog_code.py
// Heading: ## Key Code > ### Nc=128 CUDA-core promotion (Hopper SM90)
// Original fence language: cpp
// See evidence/blog-capsules/deepgemm/code/ORIGIN.yaml for origin + license metadata.

// On Hopper, the TC accumulator is only ~FP22-precise. DeepGEMM promotes
// the partial sum to an FP32 CUDA-core accumulator every Nc=128 columns
// (4 consecutive WGMMAs of n=32 each) to avoid precision drift.
constexpr int Nc = 128;
constexpr int WGMMA_N = 32;

float cuda_core_acc[TILE_M][TILE_N] = {0};

for (int k = 0; k < K; k += Nc) {
    __half2 tc_acc[TILE_M][WGMMA_N];
    memset(tc_acc, 0, sizeof(tc_acc));
    for (int sub_k = 0; sub_k < Nc; sub_k += WGMMA_K) {
        wgmma_mma_async(tc_acc, A_smem + sub_k, B_smem + sub_k);
    }
    wgmma_wait();
    for (int m = 0; m < TILE_M; m++)
        for (int n = 0; n < TILE_N; n++)
            cuda_core_acc[m][n] += (float)tc_acc[m][n] * scale_a[m] * scale_b[n];
}
