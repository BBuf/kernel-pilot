// provenance: derived from pr-flashinfer-1039, hw-tcgen05-mma, hw-tmem, technique-warp-specialization; not upstream code
// origin: wiki/techniques/warp-specialization.md Phase 3 variant; see ORIGIN.yaml in this directory
//
// Minimal three-role warp specialization skeleton for Blackwell SM100.
// Warp 0 = producer (TMA loads), warps 1-7 = MMA warpgroup (tcgen05.mma),
// warps 8-15 = epilogue. mbarrier phase is tracked by the pipeline class.
//
// This is a TEACHING skeleton, not a compilable kernel. See
// evidence/kernel-cases/warp-specialization/full/ for the canonical upstream
// implementation from FlashInfer PR-1039.

#include <cute/tensor.hpp>
#include <cutlass/pipeline/pipeline.hpp>

template <class Params, class SharedStorage, class Pipeline>
__device__ void warp_specialized_mainloop_skeleton(
    Params const& params,
    SharedStorage& storage,
    Pipeline& pipeline)
{
    int warp_idx = cute::canonical_warp_idx_sync();
    int lane_idx = threadIdx.x % 32;
    auto pipeline_state = cutlass::make_producer_pipeline_state(pipeline);

    if (warp_idx == 0) {
        // ---- Producer warp: drive TMA loads ----
        for (int k_tile = 0; k_tile < params.k_tile_count; ++k_tile) {
            pipeline.producer_acquire(pipeline_state);   // wait for empty slot
            if (lane_idx == 0) {
                // Issue TMA load for A and B tiles into the acquired stage's SMEM slot.
                // (Real code: cute::copy(tma_a, gA(_, _, k_tile), sA(_, _, pipeline_state.index()));)
            }
            pipeline.producer_commit(pipeline_state);    // mark stage ready
            ++pipeline_state;
        }
    } else if (warp_idx < 8) {
        // ---- MMA warpgroup: consume TMA loads and issue tcgen05.mma into TMEM ----
        auto consumer_state = cutlass::make_consumer_pipeline_state(pipeline);
        for (int k_tile = 0; k_tile < params.k_tile_count; ++k_tile) {
            pipeline.consumer_wait(consumer_state);      // wait for data-ready
            if (warp_idx == 1 && lane_idx == 0) {
                // Issue tcgen05.mma instruction; TMEM accumulator on storage.tmem_acc.
                // (Real code: tcgen05_mma(tmem_desc, sA(_, _, consumer_state.index()),
                //                          sB(_, _, consumer_state.index()));)
            }
            pipeline.consumer_release(consumer_state);   // release SMEM back to producer
            ++consumer_state;
        }
    } else {
        // ---- Epilogue warps: drain TMEM -> registers -> SMEM -> GMEM ----
        // Wait on the dedicated MMA-done mbarrier (separate from the load pipeline).
        // Then:
        //   - tcgen05.ld to pull accumulator fragments from TMEM into registers
        //   - apply scale/bias/activation in registers
        //   - tcgen05.st to push to SMEM, then TMA-store to GMEM
    }
}
