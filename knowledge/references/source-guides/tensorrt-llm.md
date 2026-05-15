# TensorRT-LLM Kernel Reference

Repository: <https://github.com/NVIDIA/TensorRT-LLM>

PR case notes: `../prs/tensorrt-llm.md`

Use TensorRT-LLM as NVIDIA's public baseline, candidate starting point, or prior
for LLM attention, MoE, quantized GEMM, userbuffers, and Hopper/Blackwell
routing.

## Read Order

1. Plugin or layer dispatch path.
2. Kernel launch wrapper and template specialization.
3. Architecture-specific implementation.
4. Existing test, benchmark, or plugin validation.
5. CUTLASS/CuTe documentation for the selected collective or epilogue.

## Code Map

| Area | Paths to inspect |
| --- | --- |
| Kernel tree | `cpp/tensorrt_llm/kernels/` |
| Decoder attention | `cpp/tensorrt_llm/kernels/decoderMaskedMultiheadAttention/` |
| Context FMHA | `cpp/tensorrt_llm/kernels/contextFusedMultiHeadAttention/` |
| MoE | `cpp/tensorrt_llm/kernels/mixtureOfExperts/` |
| Quantization | `cpp/tensorrt_llm/kernels/quantization/` |
| CUTLASS kernels | `cpp/tensorrt_llm/kernels/cutlass_kernels/`, `internal_cutlass_kernels/` |
| Norm / sampling | `rmsnormKernels.cu`, `topkSampling*.cu` |
| Communication | `cpp/tensorrt_llm/kernels/userbuffers/` |
| Tests/benchmarks | `tests/`, `benchmarks/`, plugin tests under `cpp/tests/` |

## Search Patterns

```bash
rg -n "sm90|sm100|WGMMA|TMA|cutlass|fp8|fp4|int8|MoE|userbuffers|NVLS" cpp/tensorrt_llm
rg -n "decoderMasked|contextFused|multi_block|rmsnorm|topk|quant" cpp/tensorrt_llm/kernels
rg -n "TEST|benchmark|perf|plugin" cpp tests benchmarks
```

## Baseline Extraction

- Identify the exact template specialization selected at runtime.
- Record architecture guard, tile shape, cluster shape, schedule, stage count,
  scale-factor layout, and epilogue semantics.
- Be careful with internal CUTLASS paths; public names can hide the actual
  linked implementation.

## Candidate Translation

Translate:

- shape/dtype/scale contracts
- dispatch and guard logic
- benchmark cases and output tolerance
- NCU bottleneck hypotheses

If TensorRT-LLM code is the requested starting point, copy/adapt it into the
standalone repo only with license/notice context, exact source path, commit, and
delta recorded. Otherwise translate the contracts and hypotheses above.

## NCU Focus

| Kernel family | First metrics |
| --- | --- |
| FMHA / decoder attention | tensor pipe %, long scoreboard, L2/DRAM traffic, active cycles |
| Quant GEMM | tensor pipe %, scale-load traffic, epilogue ALU, register pressure |
| MoE | grouped-GEMM utilization, permutation traffic, shared memory conflicts |
| Userbuffers | DRAM/L2 traffic, synchronization stalls, overlap gaps via nsys |

## Useful Cross-Framework Priors

- CUTLASS for all GEMM, epilogue, TMA, WGMMA, and cluster-shape details.
- SGLang and vLLM for production serving wrappers and benchmark shapes.
- PyTorch for correctness reference and tolerance decisions.
