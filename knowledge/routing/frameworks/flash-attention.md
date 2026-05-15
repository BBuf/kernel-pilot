# FlashAttention

Repository: <https://github.com/Dao-AILab/flash-attention>

Deep reference: `knowledge/references/source-guides/flash-attention.md`

FlashAttention is the canonical reference for **online-softmax attention** on
modern GPUs. FA2 covers SM80 (A100), FA3 covers SM90 (H100/H200) using TMA +
WGMMA, with CuTe-based kernel structure.

## Where the kernels live

| Directory | What you find there |
| --- | --- |
| `csrc/flash_attn/src/` | FA2 kernels (forward + backward) for SM80. |
| `csrc/flash_attn/src/flash_fwd_kernel.h` | Main FA2 forward kernel template. |
| `flash_attn/cute/` | CuTe-based FA3 kernel for SM90. |
| `hopper/` | Hopper-specific schedules (warpspecialization, TMA, WGMMA). |
| `benchmarks/benchmark_attn.py` | Sweep against PyTorch SDPA, FlashAttention, and xFormers. |
| `benchmarks/bench_sm90.py` | Hopper-specific microbenchmark for the FA3 path. |

## Optimization patterns documented here

- **Online softmax**: rescale the partial output by `exp(m_old - m_new)` on
  every block; the *canonical* trick for fused attention with constant smem.
- **Block-major tiling**: KV blocks of `kBlockN`, query blocks of `kBlockM`
  with a configurable head-dim split; the standard FA tile vocabulary.
- **Causal masking via diagonal blocks**: avoid storing the mask, derive it
  from block coordinates.
- **TMA + WGMMA pipeline (FA3)**: warpgroup-specialized producer / consumer
  with a swizzled smem layout. The reference for any Hopper FMHA design.
- **Backward kernel**: split into two passes (recompute and dQ, then dK + dV);
  reference for memory-bound backward attention.

## Common pitfalls

- FA2 has been heavily templated; the active specialization depends on head
  dim, causal flag, dropout, alibi, and softcap. Always pin the spec before
  benchmarking.
- The FA3 path requires CUTLASS + CuTe headers from a specific commit; do not
  mix with an older CUTLASS without re-pinning.
- Backward kernels are *much* more sensitive to head dim and seqlen
  divisibility than the forward; do not infer backward speed from forward
  speed.

## When to read this framework

- You are designing any kind of FMHA / attention forward or backward.
- You need a Hopper TMA + WGMMA warpgroup-specialized reference.
- You want a clean implementation of online softmax to compare against.

## Reuse / Copy Rules

- FlashAttention code may seed a candidate only when the user or baseline calls
  for that implementation family and license / attribution are handled.
- Record source path or URL, commit, copied files, and delta in the source
  ledger before mutating copied or adapted attention code.
- Otherwise use it as the primary hypothesis source for tile shapes, masking
  strategy, and softmax layout.

## Recommended ncu metrics for FlashAttention

- FA2: `sm__pipe_alu_cycles_active`, `smsp__inst_executed_pipe_tensor`,
  `lts__t_bytes`.
- FA3: `smsp__inst_executed_pipe_tensor.avg.pct_of_peak_sustained_elapsed`,
  `sm__cycles_active`, `dram__throughput`.
- Backward: `smsp__average_warp_latency_per_inst_executed`,
  `l1tex__data_bank_conflicts_pipe_lsu.sum`.
