# PyTorch (ATen / Inductor)

Repository: <https://github.com/pytorch/pytorch>

Deep reference: `knowledge/references/source-guides/pytorch.md`

PyTorch is the **correctness oracle and integration backbone** for most LLM
kernel work. ATen native CUDA kernels are the reference for elementwise,
reduction, and SDPA semantics. Inductor is the reference for fused Triton
codegen patterns.

## Where the kernels live

| Directory | What you find there |
| --- | --- |
| `aten/src/ATen/native/cuda/` | CUDA implementation of `aten::*` ops: elementwise, reductions, embeddings, softmax, layernorm, RMSNorm-like. |
| `aten/src/ATen/native/transformers/cuda/` | SDPA implementations: FlashAttention-like, mem-efficient, math fallback, cuDNN. |
| `aten/src/ATen/native/cudnn/` | cuDNN attention / conv frontends, the reference for cuDNN-backed paths. |
| `torch/_inductor/` | TorchInductor Triton codegen, the reference for autotuned fused-kernel templates. |
| `torch/csrc/distributed/` | NCCL / Gloo / c10d, the reference for collective ops and process group semantics. |

## Optimization patterns documented here

- **Persistent-thread reductions**: `Reduce.cuh` and `BlockReduceSum.cuh` are
  the canonical block + warp reduction templates.
- **TensorIterator vectorization**: how ATen picks `vec4` / `vec8` and how it
  handles non-contiguous inputs. Always check before writing a "faster"
  elementwise kernel.
- **SDPA dispatch**: `transformers/cuda/sdp_utils.cpp` is the cleanest example
  of how to dispatch by head dim, dtype, mask shape, and arch.
- **Inductor templates**: see `torch/_inductor/kernel/` for autotuned Triton
  GEMM, flash-attention, and reduction templates with `do_bench`-driven
  configs.

## Common pitfalls

- ATen kernels handle a *much wider* shape / stride space than a serving
  kernel. Beating ATen on the LLM hot-path is fine; "beating ATen on every
  shape" is rarely the right goal.
- `cudnnFrontend` graphs are runtime-built; cuDNN often falls back to a slower
  config silently. Always compare against a fixed reference, not "the cuDNN
  default".
- Some `aten::*` ops are dispatched through Inductor at runtime; if you
  benchmark `torch.compile`d code you may be measuring an Inductor-generated
  kernel, not the ATen CUDA kernel.

## When to read this framework

- You need the **canonical correctness oracle** for an op (e.g. RMSNorm,
  SDPA, top-k).
- You need a **dispatch-pattern reference** for how to route by dtype / arch /
  shape.
- You want to compare against `torch.compile` / Inductor output as the
  "framework-default" baseline.

## Reuse / Copy Rules

- ATen / Inductor code may seed a candidate only when the user or baseline
  calls for that implementation family and license / attribution are handled.
- Record source path or URL, commit, copied files, and delta in the source
  ledger before mutating copied or adapted code.
- Otherwise use PyTorch as the canonical correctness reference and
  framework-default baseline.

## Recommended ncu metrics for PyTorch kernels

- ATen elementwise: `dram__throughput`, `smsp__inst_executed`.
- SDPA / FlashAttention path: `smsp__inst_executed_pipe_tensor`,
  `l1tex__t_sectors_pipe_lsu_mem_global_op_ld.sum.per_second`.
- cuDNN paths: capture by name with `--kernel-id ::kernel_name:1`, not by
  PyTorch op name.
