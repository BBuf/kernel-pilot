# FlashInfer Kernel Reference

Repository: <https://github.com/flashinfer-ai/flashinfer>

PR case notes: `../prs/flashinfer.md`

Use FlashInfer as a baseline, candidate starting point, or prior for paged
attention, prefix-cache-aware attention, MLA, sampling, and plan/run Python
wrapper patterns.

## Read Order

1. Python wrapper and workspace planning API.
2. PyTorch extension binding.
3. Header-only kernel template and selected specialization.
4. Benchmarks and tests for the shape/dtype family.
5. SGLang/vLLM integration layer when FlashInfer is used through a framework.

## Code Map

| Area | Paths to inspect |
| --- | --- |
| Headers | `include/flashinfer/` |
| Extension bindings | `csrc/` |
| FMHA v2 | `csrc/fmha_v2/fmha/` |
| Hopper FMHA | `csrc/fmha_v2/fmha/hopper/`, `warpspec/` |
| Python wrappers | `python/flashinfer/` |
| Benchmarks | `benchmarks/`, especially attention/sampling benchmarks |
| Tests | `tests/` |

## Search Patterns

```bash
rg -n "BatchPrefill|BatchDecode|PagedKV|page_size|block_table|kv_indices|MLA|sampling|top_p|top_k" python include csrc tests benchmarks
rg -n "hopper|warpspec|tma|wgmma|sm90|workspace|plan|run" include csrc python
```

## Baseline Extraction

- Warm up wrapper planning and workspace allocation before timing kernels.
- Record page size, block-table representation, KV layout, head grouping, and
  causal/mask behavior.
- If comparing through SGLang or vLLM, record which wrapper path the framework
  selected.

## Candidate Translation

Translate:

- wrapper plan/run contract
- page-table and KV layout semantics
- shape families and workspace assumptions
- profile-derived memory-access hypotheses

If FlashInfer code is the requested starting point, copy/adapt it into the
standalone repo only with license/notice context, exact source path, commit, and
delta recorded. Otherwise translate the contracts and hypotheses above.

## NCU Focus

| Kernel family | First metrics |
| --- | --- |
| Paged attention | long scoreboard, L2 bytes, global load sectors, tensor pipe % |
| Prefix attention | redundant KV traffic, L2 hit rate, memory throughput |
| MLA | tensor pipe %, L2/DRAM traffic, epilogue ALU |
| Sampling | branch divergence, long scoreboard, global-load coalescing |

## Useful Cross-Framework Priors

- SGLang and vLLM for framework integration and production shape sets.
- FlashAttention for dense/prefill FMHA structure.
- CUTLASS for Hopper warp-specialized design vocabulary.
