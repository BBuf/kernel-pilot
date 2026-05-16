---
id: doc-triton-3.6-blackwell
title: "Triton 3.6.0 Release Notes — Blackwell (SM100) Lowering"
url: https://github.com/triton-lang/triton/releases/tag/v3.6.0
source_category: official-doc
architectures: [sm100, sm100a]
tags: [triton, tcgen05, tmem, 2sm-cooperative, block-scale, nvfp4, warp-specialization]
retrieved_at: 2026-04-27
---

# Triton 3.6.0 Release Notes — Blackwell Lowering

## Overview

Triton 3.6.0 (released `2026-01-21`, release commit `7c56a5e`) is the first Triton release with native NVIDIA Blackwell (SM100) lowering through `tcgen05.mma` plus tensor-memory (TMEM) accumulators. Prior to 3.6, the Triton compiler on Blackwell silently fell back to the Hopper `wgmma` path with register-resident accumulators, which is the framing recorded in the older `wiki/languages/triton-blackwell.md` page.

This doc page summarizes only the SM100-relevant items from the 3.6.0 release notes; per-pathway breakdown with verified-vs-needs-verification classification lives in `data/triton-3.6-evidence.md`.

## Blackwell-Relevant Items in the 3.6.0 Release Notes

### Tensor Memory (TMEM) infrastructure

The release adds TMEM allocation, copy, and layout primitives that the Blackwell backend lowers through `ttng.tmem_alloc`, `ttng.tmem_copy`, `ttng.tmem_load`, and `ttng.tmem_store`. Source PRs: `#8136`, `#8148`, `#8202`. After 3.6, accumulators on SM100 may live in TMEM rather than registers — the older blanket "accumulators stay in registers" claim is no longer correct as a universal statement.

### `tcgen05` lowering

Generic `tcgen05` load/store/copy lowering and `tcgen05.mma` generalization land via `#8225`, `#8421`, `#8495`, `#8102`, `#8338`, `#8386`. The dialect now exposes `ttng.tc_gen5_mma` and `ttng.tc_gen5_mma_scaled` with TMEM-token semantics.

### Warp specialization end-to-end

End-to-end aref-style warp specialization plumbing on the Blackwell path: `#8262`, `#7826`, `#8009`, `#8123`, `#8534`, `#8451`, `#8651`. The strongest user-visible surface is `tl.range(..., warp_specialize=True)` on top of descriptor / TMA matmul kernels, as documented in the Triton persistent matmul tutorial.

### Gluon front-end and 2-CTA support

Initial 2-CTA cluster support in the Gluon front-end (`#8644`, `#8653`), `num_ctas` plumbing (`#8645`), and Gluon-side `tcgen05 mma scaled` support (`#8393`). The Gluon path is the most explicit Blackwell-native surface; the release notes describe it as initial support.

### Block-scaled matmul (NVFP4 / MXFP)

Hardware-accelerated block-scaled matmul on Blackwell tensor cores via `tl.dot_scaled`. Backend exposes `ttng.tc_gen5_mma_scaled` (`#8393`); frontend fixes `#8564`, `#8658`. Format coverage centers on NVFP4 / MXFP per the official block-scaled matmul tutorial.

## Predecessor Release for Context

Triton 3.5.1 (released `2025-11-12`) is the last 3.5.x patch before the 3.6 Blackwell story. Pages with `version_sensitive` claims valid for `>=3.5,<3.6` should pin to 3.5.1.

## Subsequent 3.6.x Patches

As of `2026-04-27`, no 3.6.x patch release is visible on the official triton-lang/triton GitHub releases page; the next previous release shown there is 3.5.1. (`needs-verification` if this requires a machine-checked negative claim.)

## When To Cite This Page

Pages making claims about Triton's SM100 capabilities should add a `version_sensitive` block whose registry entry pins `last_verified_release: "3.6.0"` and lists `doc-triton-3.6-blackwell` (this page) as one of its `source_ids`. The companion downstream-code anchors are `pr-sglang-5390` and `pr-sglang-21595` — see `data/triton-3.6-evidence.md` for the per-pathway breakdown plus caveat anchors.

## Caveats

- The 3.6 release introduces native Blackwell lowering paths but does not by itself prove that every plain `tl.dot` matmul on SM100 lowers through TMEM-backed `tcgen05`. The strongest checked path is descriptor/TMA + `tl.range(warp_specialize=True)` + `tl.dot`, plus the Gluon multi-CTA / 2CTA path.
- Production-peak performance on Blackwell still favors hand-written CuTe-DSL / CUTLASS / FA-4 / TRT-LLM kernels for many compute-bound workloads. SGLang `pr-sglang-5390` reports a CUTLASS `tcgen05_mla` backend ~27% faster than the Triton MLA decode baseline; SGLang `pr-sglang-21595` changes Blackwell datacenter multimodal attention default away from `triton_attn` to FA4. A "first-class lane" framing for Triton on Blackwell is justified for supported lowering surfaces, but not as a blanket peak-performance equivalence claim.
