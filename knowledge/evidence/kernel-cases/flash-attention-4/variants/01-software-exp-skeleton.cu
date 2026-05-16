// provenance: derived from pr-cutlass-2466, technique-software-exp, kernel-flash-attention-4; not upstream code
// origin: wiki/kernels/flash-attention-4.md Phase 3 variant (software-emulated exponential skeleton)

// FlashAttention-4 software exp trick: exp2f(x * log2(e)) is emitted by
// the compiler as a fused ex2.approx.f32 instruction on SM100, which runs
// on the MUFU (Multi-Function Unit) path and overlaps with the MMA path.
// This avoids the Tensor Core saturation bottleneck that FA-2/FA-3 hit.

#include <cuda_fp16.h>
#include <cmath>

__device__ inline float fa4_rescale_exp(float x, float max_old, float max_new) {
    // Rescale accumulator when row maximum updates (online softmax).
    // exp2f(diff * log2(e)) fuses to ex2.approx.f32 on SM100.
    constexpr float LOG2E = 1.44269504088896340736f;
    return __expf((max_old - max_new) * 1.0f) * x;
    // Equivalent fused form:
    //   return exp2f((max_old - max_new) * LOG2E) * x;
}

// See full/ for the upstream FA4-MLA kernel. The ex2-based rescale lives
// inside that kernel's inner softmax loop (grep for 'exp2|ex2' in the
// mainloop collective file).
