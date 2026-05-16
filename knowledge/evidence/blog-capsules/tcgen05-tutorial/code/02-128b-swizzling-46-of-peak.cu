// Extracted from sources/blogs/tcgen05-tutorial.md by scripts/extract_blog_code.py
// Heading: ## Key Code > ### 128B swizzling (46% of peak)
// Original fence language: cuda
// See evidence/blog-capsules/tcgen05-tutorial/code/ORIGIN.yaml for origin + license metadata.

// XOR-swizzled SMEM layout eliminates bank conflicts on MMA load;
// 128-byte granularity gives 2.7x speedup on its own.
template <int N_K>
__device__ void swizzle_128b_store(half* smem, const half* gmem, int k_tile) {
    int tid = threadIdx.x;
    int col = (tid * 8) % N_K;
    int row = (tid * 8) / N_K;
    int swizzled = col ^ ((row & 0x7) << 4);      // 8-lane XOR swizzle
    *reinterpret_cast<uint4*>(&smem[row * N_K + swizzled]) =
        *reinterpret_cast<const uint4*>(&gmem[k_tile + row * N_K + col]);
}
