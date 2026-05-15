# CuTe DSL Deep Reference

Repository: <https://github.com/NVIDIA/cutlass>

PR case notes: `../prs/cutlass.md`

Use this when the candidate language is CuTe DSL, when the baseline is QuACK or
another CuTe DSL kernel, or when CUTLASS/CuTe layout algebra is needed for
Hopper / Blackwell kernels.

## Required Companion References

- `../ako4all/cute-dsl-kernel-reference.md`
- `../ako4all/cute-dsl/cute-dsl-overview.md`
- `../ako4all/cutlass-cpp-kernel-reference.md`
- `../ako4all/architectures/sm90-optimization-guide.md` for H100
- `../ako4all/cute-dsl/sm100-optimization-guide.md` for B200/B300

## Read Order

1. CuTe DSL example closest to the operator.
2. Layout and tensor algebra docs.
3. Copy / TMA / MMA primitives.
4. Epilogue and scale/bias handling.
5. Tests or examples for the same architecture and dtype.

## Code Map

| Area | Paths to inspect |
| --- | --- |
| CuTe DSL package | `python/` |
| C++ layout vocabulary | `include/cute/` |
| Hopper / Blackwell examples | `examples/48_hopper_*`, `examples/50_blackwell_*`, `examples/60_*` |
| Unit tests | `test/unit/` |
| Docs | `media/docs/`, `docs.nvidia.com/cutlass/` |

## Search Patterns

```bash
rg -n "cute|Layout|Tensor|TiledCopy|TiledMma|CopyAtom|MmaAtom|TMA|WGMMA|tcgen05|epilogue|visitor" python include examples test
rg -n "sm90|sm100|blackwell|hopper|block_scaled|fp8|fp4|int8|scale" python include examples test
```

## Candidate Use

- CuTe DSL code may seed a standalone candidate when license / attribution are
  handled.
- Record exact source, commit, tile/layout config, selected MMA/copy atoms,
  generated code if inspected, and delta.
- For baseline-derived work, keep the first candidate close to the baseline so
  the first measured delta isolates one schedule/layout change.

## NCU Focus

| Kernel family | First metrics |
| --- | --- |
| GEMM / attention | tensor pipe %, TMA traffic, L2/DRAM bytes, active cycles |
| Memory-bound fused ops | DRAM throughput, global sectors, shared bank conflicts |
| Epilogue fusion | tensor vs ALU pipe %, store traffic, scale/bias load traffic |
