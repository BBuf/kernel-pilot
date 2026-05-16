// provenance: derived from pr-vllm-16032, blog-colfax-cutlass, technique-epilogue-fusion, hw-tmem; not upstream code
// origin: wiki/techniques/epilogue-fusion.md Phase 3 variant

// Double-buffered TMEM epilogue skeleton. The MMA warp writes into one
// half of TMEM while the epilogue warp drains the other half. Two
// mbarriers coordinate the hand-off.

constexpr int TMEM_HALF = 128;  // each half holds a 128x128 FP32 accumulator

template <class Params>
__device__ void double_buffered_tmem_epilogue(
    Params const& params, int num_tiles)
{
    __shared__ uint64_t mbar_mma_done[2];
    __shared__ uint64_t mbar_epi_done[2];
    int warp = threadIdx.x / 32;

    if (warp == 1) {
        // MMA warp: alternates between two halves
        for (int t = 0; t < num_tiles; ++t) {
            int buf = t & 1;
            if (t >= 2) mbarrier_wait(&mbar_epi_done[buf]);
            tcgen05_mma_into_half(buf);
            mbarrier_arrive(&mbar_mma_done[buf]);
        }
    } else if (warp >= 2) {
        // Epilogue warp: drains TMEM -> registers -> SMEM -> GMEM
        for (int t = 0; t < num_tiles; ++t) {
            int buf = t & 1;
            mbarrier_wait(&mbar_mma_done[buf]);
            drain_tmem_half_to_gmem(buf);
            mbarrier_arrive(&mbar_epi_done[buf]);
        }
    }
}
