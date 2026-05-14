# SGLang Kernel Reference

Repository: <https://github.com/sgl-project/sglang>

Use this when SGLang is the baseline, integration oracle, or source of the hot
kernel. Keep SGLang read-only unless the user explicitly asks for an in-place
patch.

## Read Order

1. Python call site and dispatch path.
2. `sgl-kernel/python/sgl_kernel/` wrapper.
3. `sgl-kernel/csrc/` kernel entry point and launch parameters.
4. Existing unit tests and benchmarks.
5. Similar kernels in vLLM, FlashInfer, TensorRT-LLM, CUTLASS, or PyTorch.

## Code Map

| Area | Paths to inspect |
| --- | --- |
| AOT CUDA extension | `sgl-kernel/csrc/`, `sgl-kernel/python/sgl_kernel/` |
| Attention | `sgl-kernel/csrc/attention/`, `python/sglang/srt/layers/attention/` |
| GEMM / quant GEMM | `sgl-kernel/csrc/gemm/`, `python/sglang/srt/layers/quantization/` |
| MoE | `sgl-kernel/csrc/moe/`, `python/sglang/srt/layers/moe/` |
| Elementwise / norm / RoPE | `sgl-kernel/csrc/elementwise/` |
| Sampling | `sgl-kernel/csrc/sampling/`, `python/sglang/srt/layers/sampler.py` |
| Spec decode | `sgl-kernel/csrc/spec_decode/`, EAGLE/tree decode call sites |
| Benchmarks | `python/sglang/bench_one_batch.py`, `python/sglang/bench_serving.py`, `sgl-kernel/benchmark/` |
| Tests | `sgl-kernel/tests/`, `test/`, kernel-specific pytest files |

## Search Patterns

Use these before choosing an edit:

```bash
rg -n "int8_scaled_mm|scaled_mm|cutlass|sm90|fp8|fp4|rmsnorm|paged|moe|sampling" \
  sgl-kernel python/sglang
rg -n "CUDA_VISIBLE_DEVICES|pytest|benchmark|bench_" sgl-kernel python/sglang test
rg -n "TORCH_LIBRARY|PYBIND11_MODULE|REGISTER|dispatch|backend" sgl-kernel python/sglang
```

## Baseline Extraction

- Identify the active dispatch path for the target GPU, dtype, and shape.
- Record the exact SGLang commit, build flags, CUDA version, driver, and GPU.
- Prefer existing SGLang tests/benchmarks for baseline parity before creating a
  standalone harness.
- When the SGLang benchmark is hard to import, copy only the minimal benchmark
  contract into a clean standalone repo and keep SGLang source read-only.

## Candidate Translation

Candidate kernels must not copy SGLang kernel bodies. Translate only:

- tensor shapes, strides, dtype contracts, scale layout, and output tolerance
- Python wrapper semantics and error handling expectations
- benchmark shapes and correctness cases
- profile-derived bottleneck hypotheses

Implement candidates as standalone naive CUDA C++ with PyTorch binding.

## NCU Focus

| Kernel family | First metrics |
| --- | --- |
| GEMM / int8 / fp8 | tensor pipe %, DRAM %, L2 bytes, active cycles, occupancy, long scoreboard |
| Norm / elementwise | DRAM %, L2 bytes, global-load sectors, issue stalls |
| Sampling / spec decode | branch divergence, long scoreboard, global-load coalescing |
| Paged attention | tensor pipe %, long scoreboard, L2 hit/traffic, shared bank conflicts |

## Useful Cross-Framework Priors

- vLLM for paged attention, cache layout, Marlin/Machete quant kernels.
- FlashInfer for paged/prefix attention wrappers and plan/run APIs.
- TensorRT-LLM for NVIDIA attention, MoE, and quantization routing.
- CUTLASS for GEMM tile, cluster, schedule, and epilogue prior art.
- PyTorch for correctness semantics and wide-shape behavior.

