# Veitner Blog And Code Deep Reference

Blog index: <https://veitner.bearblog.dev/blog/>

Primary code:

- <https://github.com/simveit/effective_transpose>
- <https://github.com/simveit/load_and_store>
- <https://gist.github.com/simveit>

Use this reference when the optimization loop needs practical Hopper /
Blackwell examples that explain both the idea and a small implementation.

Article-level map: `../blogs/veitner.md`

## Read Order By Topic

### CuTe DSL / QuACK

1. `an-applied-introduction-to-cutedsl`
2. `sgemm-in-cutedsl`
3. `cutedsl-on-hopper-wgmma-and-tma-intro`
4. `cutedsl-on-hopper-pipelining`
5. `consumer-producer-pattern-on-h100-in-cutedsl`
6. `persistent-gemm-in-cutedsl-on-hopper`
7. `pingpong-in-the-cutedsl-with-quack`
8. `warp-specialisation-in-cutedsl`

### GEMM / Low Precision

1. `persistent-float8-dense-gemm-on-hopper`
2. `b200-blockscaled-gemm-the-setup`
3. `scale-tensor-construction-in-cutedsl`
4. `grouped-block-scaled-gemm-intro`
5. `grouped-blockscaled-gemm-host-code`
6. `grouped-blockscaled-gemm-kernel`
7. `nvfp4-gemv`
8. `nvfp4-gemv-improved`

### Memory Movement / TMA

1. `tma-introduction`
2. `making-matrix-transpose-really-fast-on-hopper-gpus`
3. `use-tma-without-cuda`
4. `highly-efficient-matrix-transpose-in-mojo`
5. `gpu-l2-cache-persistence`
6. `swizzles-and-their-usage-in-cutedsl-kernels`

### Norm / Reduction / Sequence Kernels

1. `making-rmsnorm-really-fast`
2. `simple-reduction-in-cutedsl`
3. `backprop-through-rmsnorm`
4. `backprob-through-layernorm`
5. `gated-delta-net-decoding`
6. `chunkwise-gated-delta-rule`
7. `simple-math-to-speed-up-gdn-prefill`

## Code Map By Kernel Type

| Kernel type | Source paths | What to extract |
| --- | --- |
| TMA transpose baseline | `simveit/effective_transpose/transpose_naive.cu` | baseline indexing, TMA tensor-map setup, event timing |
| TMA transpose + swizzle | `transpose_swizzle.cu`, `swizzle.cu` | row/column swizzle helpers and bank-conflict reduction |
| Batched TMA transpose | `transpose_swizzle_batched.cu`, `transpose_swizzle_batched_for_profile.cu` | more CTAs/work per launch and stable profiling variant |
| Shared-memory / tensor-map helpers | `effective_transpose/utils.h` | CUDA 12+ tensor-map boilerplate and validation helpers |
| PTX load matrix | `simveit/load_and_store/ld_matrix_x1.cu`, `ld_matrix_x2.cu`, `ld_matrix_x4.cu` | `ldmatrix.sync.aligned` fragments and address conversion |
| PTX store matrix | `st_matrix_x1.cu`, `st_matrix_x2.cu`, `st_matrix_x4.cu` | `stmatrix.sync.aligned` forms and fragment layout |
| Blog-linked snippets | `gist.github.com/simveit` | source with gist URL/revision as provenance key |

## Search Patterns

```bash
rg -n "TMA|WGMMA|CuTeDSL|QuACK|swizzle|persistent|blockscaled|NVFP4|RMSNorm|GDN|transpose|mbarrier|ldmatrix|stmatrix" .
```

## Candidate Use

- Use blog posts for hypotheses and linked code for candidate seeds.
- Record article URL plus code URL, commit or gist revision when available,
  copied files, and mutation delta.
- If no linked code exists, summarize the idea in `source-idea-ledger.md`
  instead of copying prose-derived snippets.

## NCU Focus

- TMA transpose and swizzling: DRAM bandwidth, L2 bytes, shared-memory bank
  conflicts, long scoreboard.
- CuTe DSL GEMM: tensor pipe utilization, waves-per-SM, shared-memory pressure,
  register pressure, TMA wait stalls.
- Norm/reduction: HBM throughput, shared-memory conflicts, warp issue stalls.
