// Extracted from sources/blogs/colfax-cutlass-blackwell.md by scripts/extract_blog_code.py
// Heading: ## Key Code > ### TMEM load into registers for epilogue
// Original fence language: cuda
// See evidence/blog-capsules/colfax-cutlass-blackwell/code/ORIGIN.yaml for origin + license metadata.

// Epilogue warps drain TMEM → registers using tcgen05.ld
// Each warp loads 32 columns (=128 bytes) at a time.
float reg[4];
asm volatile(
    "tcgen05.ld.sync.aligned.32x32b.x4.b32 "
    "{%0, %1, %2, %3}, [%4];\n"
    : "=f"(reg[0]), "=f"(reg[1]), "=f"(reg[2]), "=f"(reg[3])
    : "r"(tmem_addr + warp_col_offset));
