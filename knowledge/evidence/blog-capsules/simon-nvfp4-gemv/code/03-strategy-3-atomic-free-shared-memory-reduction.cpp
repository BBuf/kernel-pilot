// Extracted from sources/blogs/simon-nvfp4-gemv.md by scripts/extract_blog_code.py
// Heading: # NVFP4 GEMV and Improved NVFP4 GEMV (Simon Veitner) > ## Key Code > ### Strategy 3 — Atomic-free shared-memory reduction
// Original fence language: cpp
// See evidence/blog-capsules/simon-nvfp4-gemv/code/ORIGIN.yaml for origin + license metadata.

// Each thread pair stores an intermediate product; after __syncthreads()
// the CTA reduces along K-major in shared memory without atomics.
__shared__ float smem[THREADS_PER_M][THREADS_PER_K];
smem[tid_m][tid_k] = thread_partial;
__syncthreads();

// Warp-wide parallel reduction along the K axis
for (int s = THREADS_PER_K / 2; s > 0; s >>= 1) {
    if (tid_k < s) smem[tid_m][tid_k] += smem[tid_m][tid_k + s];
    __syncthreads();
}
if (tid_k == 0) C[m_base + tid_m] = __float2half(smem[tid_m][0]);
