# PyTorch Kernel Reference

Repository: <https://github.com/pytorch/pytorch>

Use PyTorch as correctness oracle, semantic reference, and broad-shape behavior
reference. PyTorch is rarely the candidate-code source for KernelPilot loops.

## Read Order

1. Python op schema and dispatch entry.
2. ATen native implementation or decomposition.
3. CUDA kernel and TensorIterator/reduction helpers.
4. Test coverage for semantics and edge cases.
5. Inductor or cuDNN path when the real baseline is `torch.compile` or cuDNN.

## Code Map

| Area | Paths to inspect |
| --- | --- |
| ATen native CUDA | `aten/src/ATen/native/cuda/` |
| TensorIterator | `aten/src/ATen/native/cuda/Loops.cuh`, TensorIterator helpers |
| Reductions | `aten/src/ATen/native/cuda/Reduce.cuh`, block/warp reduction helpers |
| Transformers / SDPA | `aten/src/ATen/native/transformers/cuda/` |
| cuDNN integration | `aten/src/ATen/native/cudnn/` |
| Inductor | `torch/_inductor/`, generated Triton templates and benchmarking utilities |
| Tests | `test/test_cuda.py`, `test/test_transformers.py`, op-specific tests |

## Search Patterns

```bash
rg -n "TORCH_IMPL_FUNC|REGISTER_DISPATCH|TensorIterator|gpu_kernel|Reduce|BlockReduce|sdpa|scaled_dot_product" aten torch test
rg -n "inductor|triton|do_bench|autotune|template" torch/_inductor test
rg -n "cuda|cudnn|flash|mem_efficient|math" aten/src/ATen/native/transformers
```

## Baseline Extraction

- Use PyTorch eager as semantic reference, not necessarily performance target.
- Record strides, broadcasting, type promotion, accumulation dtype, NaN/Inf
  behavior, rounding tolerance, and non-contiguous behavior.
- If comparing to `torch.compile`, save the generated kernel or at least the
  Inductor benchmark and config metadata.

## Candidate Translation

Translate:

- exact op semantics and edge cases
- output tolerance and dtype behavior
- representative shape generation
- decomposition of a composite op into tensors

Do not copy ATen, Inductor, cuDNN wrapper, or generated Triton kernel bodies.

## NCU Focus

| Kernel family | First metrics |
| --- | --- |
| Elementwise | DRAM throughput, global load/store sectors, vectorization, active cycles |
| Reduction / norm | long scoreboard, shared bank conflicts, occupancy, warp issue stalls |
| SDPA | tensor pipe %, L2/DRAM traffic, occupancy, branch divergence |
| Inductor-generated Triton | kernel count, launch overhead via nsys, tensor/DRAM utilization via ncu |

## Useful Cross-Framework Priors

- SGLang/vLLM for serving-specific narrowed shape contracts.
- CUTLASS/TensorRT-LLM for GEMM and quantized matmul prior art.
- FlashInfer/FlashAttention for attention-specific behavior.

