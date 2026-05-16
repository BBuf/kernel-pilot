// provenance: derived from pr-cutlass-2161, pr-cutlass-2881, hw-clc, technique-persistent-kernels; not upstream code
// origin: wiki/techniques/persistent-kernels.md Phase 3 variant

// Persistent kernel with CLC (Cluster Launch Control). Each CTA loops,
// dynamically pulling a tile ID from the hardware queue until drained.

#include <cuda.h>

__global__ void persistent_gemm_with_clc(
    const half* A, const half* B, half* C,
    int M, int N, int K)
{
    __shared__ int current_tile_id;
    while (true) {
        if (threadIdx.x == 0) {
            // clusterlaunchcontrol.query_cancel returns next available tile id
            int tid;
            asm volatile("clusterlaunchcontrol.query_cancel.async.shared.b32 %0;"
                         : "=r"(tid));
            current_tile_id = tid;
        }
        __syncthreads();
        if (current_tile_id < 0) break;                 // queue drained
        // Grid-Dependent Control barrier lets successive launches overlap
        asm volatile("griddepcontrol.wait;");
        int tile_m = current_tile_id / ((N + 127) / 128);
        int tile_n = current_tile_id % ((N + 127) / 128);
        // ... MMA + epilogue on this tile ...
    }
}
