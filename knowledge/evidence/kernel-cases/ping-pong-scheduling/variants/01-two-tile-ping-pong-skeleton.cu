// provenance: derived from pr-cutlass-2466, blog-flash-attention-4, technique-ping-pong-scheduling; not upstream code
// origin: wiki/techniques/ping-pong-scheduling.md Phase 3 variant

// Minimal two-tile ping-pong: while tile A runs softmax+rescale on the
// SFU path, tile B issues tcgen05.mma on the tensor-core path. The two
// overlap because they use disjoint hardware units.

template <class Acc>
__device__ void ping_pong_mainloop(
    Acc& acc_a, Acc& acc_b,
    const half* K_block, const half* V_block,
    int num_kv_tiles)
{
    for (int t = 0; t < num_kv_tiles; t += 2) {
        issue_mma(acc_a, K_block + t * K_TILE);         // tensor-core
        wait_mma();
        softmax_and_rescale(acc_a);                     // SFU/MUFU

        issue_mma(acc_b, K_block + (t + 1) * K_TILE);   // overlaps with softmax_and_rescale above
        wait_mma();
        softmax_and_rescale(acc_b);
    }
}
