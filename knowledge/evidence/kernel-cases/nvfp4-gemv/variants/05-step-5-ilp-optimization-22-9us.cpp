// provenance: derived from blog-yue-nvfp4-hackathon, pr-vllm-16032, hw-nvfp4; not upstream code
// origin: wiki/kernels/nvfp4-gemv.md Phase 3 variant (copied from the extracted blog bundle)

// Extracted from sources/blogs/yue-nvfp4-hackathon.md by scripts/extract_blog_code.py
// Heading: # Blackwell NVFP4 Kernel Hackathon Journey (Yue Zhang) > ## Key Optimization Steps > ### Step 5: ILP Optimization (~22.9us)
// Original fence language: cpp
// See evidence/blog-capsules/yue-nvfp4-hackathon/code/ORIGIN.yaml for origin + license metadata.

// Before: sequential FP4 decode + accumulate
for (int k = 0; k < K; k += 16) {
    decode_fp4(a[k:k+16]);
    accumulate(partial_sum);
}

// After: unrolled with interleaved decode + accumulate
// Decode batch[i+1] while accumulating batch[i]
// Multiple independent accumulator registers
