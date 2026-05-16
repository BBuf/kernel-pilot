// provenance: derived from blog-yue-nvfp4-hackathon, pr-vllm-16032, hw-nvfp4; not upstream code
// origin: wiki/kernels/nvfp4-gemv.md Phase 3 variant (copied from the extracted blog bundle)

// Extracted from sources/blogs/yue-nvfp4-hackathon.md by scripts/extract_blog_code.py
// Heading: # Blackwell NVFP4 Kernel Hackathon Journey (Yue Zhang) > ## Key Optimization Steps > ### Step 2: Coalesced Memory Access (~443us, then improved)
// Original fence language: cpp
// See evidence/blog-capsules/yue-nvfp4-hackathon/code/ORIGIN.yaml for origin + license metadata.

// Bad: each thread reads non-contiguous FP4 elements
// Good: threads in a warp read contiguous 128-byte chunks
// The FP4 packing (2 elements per byte) requires careful indexing
// to maintain coalesced access at the byte level
