// provenance: derived from kernel-deepgemm, blog-deepgemm; not upstream code
// origin: wiki/kernels/deepgemm.md 'FP8 Accumulation with Nc=128 CUDA Core Promotion' section

// On Hopper SM90, the Tensor Core accumulator has limited precision (~FP22,
// not true FP32). DeepGEMM mitigates this by promoting partial sums to a
// separate FP32 accumulator on CUDA Cores every Nc=128 columns (4 consecutive
// WGMMA operations).
//
// On Blackwell SM100, tcgen05.mma with TMEM accumulation uses native UE8M0
// block scaling and does NOT need explicit CUDA-core promotion.

// SM90 path: WGMMA with Nc=128 CUDA Core promotion
// Every 4 WGMMAs, promote accumulated result to FP32 CUDA core accumulator
constexpr int Nc = 128;           // Promotion interval (4 WGMMAs of n=32 each)
constexpr int WGMMA_N = 32;

template <int TILE_M, int TILE_N, int WGMMA_K>
__device__ void fp8_accum_with_cuda_core_promotion(
    float (&cuda_core_acc)[TILE_M][TILE_N],
    const __nv_fp8_e4m3* A_smem,
    const __nv_fp8_e4m3* B_smem,
    const float* scale_a,
    const float* scale_b,
    int K)
{
    for (int k = 0; k < K; k += Nc) {
        // Run 4 consecutive WGMMAs with TC-limited precision accumulation
        __half2 tc_acc[TILE_M][WGMMA_N];
        memset(tc_acc, 0, sizeof(tc_acc));

        for (int sub_k = 0; sub_k < Nc; sub_k += WGMMA_K) {
            // wgmma_mma_async(tc_acc, A_smem + sub_k, B_smem + sub_k);
        }
        // wgmma_wait();

        // Promote: add TC result to CUDA Core FP32 accumulator
        // This prevents precision loss from repeated FP22 accumulation.
        for (int m = 0; m < TILE_M; m++) {
            for (int n = 0; n < TILE_N; n++) {
                cuda_core_acc[m][n] += (float)tc_acc[m][n] * scale_a[m] * scale_b[n];
            }
        }
    }
}

// SM100 path: tcgen05.mma with native block scaling — no explicit CUDA core
// promotion needed. Scaling factors packed as UE8M0 (4 values per uint32).
