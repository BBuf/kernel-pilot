// Extracted from sources/blogs/colfax-cutlass-blackwell.md by scripts/extract_blog_code.py
// Heading: ## Key Code > ### CUTLASS MMA_Atom wrapping
// Original fence language: cpp
// See evidence/blog-capsules/colfax-cutlass-blackwell/code/ORIGIN.yaml for origin + license metadata.

// The CUTLASS two-level abstraction: MMA_Atom wraps the PTX intrinsic,
// MMA_Traits maps logical MxNxK shapes to TMEM addressing.
using Atom = cute::MMA_Atom<cute::SM100_MMA_F16BF16_SS<
    cute::half_t, cute::half_t, float,     // A, B, C types
    128, 256,                               // MxN tile
    cute::UMMA::Major::K, cute::UMMA::Major::K
>>;
