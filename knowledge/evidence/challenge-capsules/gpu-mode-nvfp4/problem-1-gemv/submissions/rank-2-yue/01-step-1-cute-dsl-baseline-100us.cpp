// Extracted from sources/blogs/yue-nvfp4-hackathon.md by scripts/extract_blog_code.py
// Heading: # Blackwell NVFP4 Kernel Hackathon Journey (Yue Zhang) > ## Key Optimization Steps > ### Step 1: CuTe DSL Baseline (~100us)
// Original fence language: cpp
// See evidence/blog-capsules/yue-nvfp4-hackathon/code/ORIGIN.yaml for origin + license metadata.

// CuTe DSL approach:
// - Automatic partition/copy for NVFP4 data
// - Handles packing/unpacking of FP4 values
// - Reasonable but not optimal memory access patterns
// Result: ~100us -- decent starting point
