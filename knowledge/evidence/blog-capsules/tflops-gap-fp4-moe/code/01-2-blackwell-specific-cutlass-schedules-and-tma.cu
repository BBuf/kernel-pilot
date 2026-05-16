// Extracted from sources/blogs/tflops-gap-fp4-moe.md by scripts/extract_blog_code.py
// Heading: # TFLOPS Gap: Why FP4 MoE Kernel Engineering Matters on Blackwell > ## Three Key Optimization Techniques > ### 2. Blackwell-Specific CUTLASS Schedules and TMA
// Original fence language: cuda
// See evidence/blog-capsules/tflops-gap-fp4-moe/code/ORIGIN.yaml for origin + license metadata.

blockscale_offsets[expert_id + 1] = (expert_offsets[expert_id + 1] + 127) / 128 * 128;
