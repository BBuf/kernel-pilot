# Veitner Blog And Code

Blog index: <https://veitner.bearblog.dev/blog/>

Primary code:

- <https://github.com/simveit/effective_transpose>
- <https://github.com/simveit/load_and_store>
- <https://gist.github.com/simveit>

Deep reference: `knowledge/references/source-guides/veitner-blog.md`

Use this source collection for hands-on Hopper / Blackwell kernel writeups,
especially CuTe DSL, QuACK, TMA, WGMMA, swizzling, transpose, reductions,
RMSNorm, SGEMM, persistent GEMM, block-scaled GEMM, NVFP4 GEMV, and GDN-style
sequence kernels.

## Where To Look First

| Source | What it teaches |
| --- | --- |
| `veitner.bearblog.dev/blog/` | Article index; route by topic and date. |
| `simveit/effective_transpose` | Native CUDA Hopper transpose progression with swizzling and TMA. |
| `simveit/load_and_store` | PTX `ldmatrix` / `stmatrix` learning code. |
| `gist.github.com/simveit` | Small kernels and experiments linked from posts. |

## High-Value Article Routes

- CuTe DSL: applied introduction, SGEMM, pipelining, WGMMA/TMA, epilogue,
  partitions, slicing, swizzles, numeric conversions.
- GEMM: persistent GEMM on Hopper, 2-CTA GEMM on B200, grouped block-scaled
  GEMM, block-scaled setup and host code.
- Memory movement: TMA intro, TMA without CUDA, matrix transpose on Hopper,
  L2 cache persistence, CUDA streams.
- Reductions and norms: simple reduction in CuTe DSL, RMSNorm, LayerNorm
  backward.
- Low precision: NVFP4 GEMV, scale tensor construction, numeric conversions.

## Reuse / Copy Rules

- Blog snippets and linked code may seed candidates when license / attribution
  are handled.
- Record article URL, code URL or gist ID, commit when available, copied files,
  and delta before mutating copied or adapted code.
- Prefer linked code over reconstructing long snippets from prose.
