# Topic: Communication (NCCL / NVLS / userbuffers)

## What it covers

Collective ops (all-reduce, all-gather, reduce-scatter, all-to-all),
NVLink-multicast (NVLS) primitives, NVIDIA userbuffers for TP overlap,
comm-overlap GEMM patterns.

## Per-framework references

| Framework | Where to look | What it teaches |
| --- | --- | --- |
| `tensorrt-llm` | `cpp/tensorrt_llm/kernels/userbuffers/` | Registered host buffers + `multimem` PTX for cluster-wide reductions. |
| `pytorch` | `torch/csrc/distributed/`, NCCL bindings | Reference for NCCL process group / collective semantics. |
| `sglang` | `sgl-kernel/csrc/allreduce_*`, `python/sglang/srt/distributed/` | Production all-reduce + comm-overlap GEMM glue. |

## Common optimization patterns

- NVLS one-shot all-reduce with `multimem.ld.reduce` + `multimem.st`.
- Userbuffers: pre-registered buffers shared across ranks; avoids stage-and-
  copy on every collective.
- Comm-overlap GEMM: pipeline the comm chunk-by-chunk with the GEMM that
  produces / consumes its outputs.

## Common bottlenecks

- NCCL `allreduce` for small messages is latency-bound; check the NVLS or
  userbuffers path instead.
- Cluster-wide reductions can starve SMs on the "consumer" side; check
  `smsp__cycles_active` per rank.

## Recommended ncu metrics

- `smsp__cycles_active.avg.pct_of_peak_sustained_elapsed`
- `dram__throughput.avg.pct_of_peak_sustained_elapsed`
- `lts__t_bytes.avg.pct_of_peak_sustained_elapsed`
