# ThunderKittens Deep Reference

Repository: <https://github.com/HazyResearch/ThunderKittens>

PR case notes: `../prs/thunderkittens.md`

Use this when the target benefits from warpgroup tile primitives, small
high-performance CUDA templates, attention, matmul, or reduction layouts.

## Read Order

1. `include/kittens.cuh`
2. `include/ops/`
3. `kernels/`
4. `examples/`
5. `tests/`

## Search Patterns

```bash
rg -n "warpgroup|mma|load|store|shared|tile|attention|matmul|softmax|norm" include kernels examples tests
```

## Candidate Use

- Use as baseline, prior art, or candidate seed only when the task allows it and
  license / attribution are handled.
- Record commit, copied files, tile primitive mapping, memory layout, and delta
  before mutating copied or adapted code.

## NCU Focus

- Warpgroup issue efficiency and tensor-core utilization.
- Shared-memory bank conflicts and register pressure.
- Tail-shape occupancy and waves-per-SM.
