// provenance: derived from blog-yue-nvfp4-hackathon, pr-vllm-16032, hw-nvfp4; not upstream code
// origin: wiki/kernels/nvfp4-gemv.md Phase 3 variant (copied from the extracted blog bundle)

// Extracted from sources/blogs/yue-nvfp4-hackathon.md by scripts/extract_blog_code.py
// Heading: # Blackwell NVFP4 Kernel Hackathon Journey (Yue Zhang) > ## Key Optimization Steps > ### Step 3: Hardware Intrinsics (~39us)
// Original fence language: cpp
// See evidence/blog-capsules/yue-nvfp4-hackathon/code/ORIGIN.yaml for origin + license metadata.

// Generic: manual bit manipulation for FP4 -> FP16 conversion
// float val = decode_fp4_manual(packed_byte >> 4);  // slow

// Hardware intrinsic: single instruction for FP4 -> FP16x2
// __half2 result = __cvt_fp4x2_to_halfx2(packed_fp4);  // fast
