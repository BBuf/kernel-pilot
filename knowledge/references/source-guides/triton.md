# Triton Deep Reference

Repository: <https://github.com/triton-lang/triton>

PR case notes: `../prs/triton.md`

Use this when the user asks for Triton, the baseline is Triton or Inductor
generated code, or the target framework's hot kernel is written in Triton.

## Read Order

1. Tutorial closest to the operator.
2. Target framework's Triton kernel and wrapper.
3. Autotune key/config definitions.
4. Lowering/backend tests when SASS or scheduling is surprising.
5. Benchmark harness and p50/p90 reporting.

## Code Map

| Area | Paths to inspect |
| --- | --- |
| Tutorials | `python/tutorials/` |
| Language primitives | `python/triton/language/` |
| Runtime / autotune | `python/triton/runtime/` |
| Compiler lowering | `lib/`, `third_party/nvidia/` |
| Backend tests | `test/TritonGPU/`, `test/` |

## Search Patterns

```bash
rg -n "tl\\.dot|tl\\.load|tl\\.store|block_ptr|make_block_ptr|program_id|num_warps|num_stages|autotune|Config" python test
rg -n "TMA|warp_specialize|persistent|split_k|matmul|softmax|layer_norm|attention|moe" python test lib third_party/nvidia
```

## Candidate Use

- Triton code can seed candidates when the user or baseline calls for Triton.
- Record source path, commit, autotune config, compile flags, and first delta.
- Always include warmup and compile-time notes because Triton JIT effects can
  hide true kernel latency.

## NCU Focus

| Kernel family | First metrics |
| --- | --- |
| Matmul / attention | tensor pipe %, L2/DRAM bytes, occupancy, register pressure |
| Softmax / norm | DRAM throughput, global sectors, issue stalls |
| Persistent kernels | active cycles, load imbalance, launch/grid size, long scoreboard |
