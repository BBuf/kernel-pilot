# Colfax Research Blog And Code

Article index: <https://research.colfax-intl.com/blog/>

Primary code:

- <https://github.com/ColfaxResearch/cfx-article-src>
- <https://github.com/ColfaxResearch/cutlass-kernels>

Deep reference: `knowledge/references/source-guides/colfax-research.md`

Use this source collection for human-written CUTLASS / CuTe kernel tutorials
and companion code, especially Hopper TMA, WGMMA, pipeline GEMM, Stream-K,
matrix transpose, Blackwell Tensor Memory / UMMA, sub-byte GEMM, block scaling,
FlashAttention, FlexAttention, and CuTe layout algebra.

## Where To Look First

| Source | What it teaches |
| --- | --- |
| `research.colfax-intl.com/blog/` | Article index for CUTLASS, CuTe, Hopper, and Blackwell tutorials. |
| `ColfaxResearch/cfx-article-src` | Companion source for articles: `tma`, `pipeline-gemm`, `streamk`, `transpose-cute`, `cutlass_gemm`, `evt`. |
| `ColfaxResearch/cutlass-kernels` | LLM-focused CUTLASS kernels and experimental FlashAttention-3 variants. |

## High-Value Article Routes

- Hopper: TMA tutorial, WGMMA tutorial, GEMM kernel design and pipelining,
  Stream-K / persistent schedulers.
- Blackwell: Tensor Memory, 2-SM GEMM, sub-byte GEMM, hardware block scaling.
- Attention: FlashAttention-2 / FlashAttention-4, FlexAttention in CuTe DSL.
- CuTe: layout algebra, categorical foundations, CUTLASS 3.x API layers.

## Reuse / Copy Rules

- Companion code may seed candidates when license / attribution are handled.
- Record article URL, repository, source path, commit, copied files, and delta
  before mutating copied or adapted code.
- Prefer `cfx-article-src` code before retyping article snippets.
