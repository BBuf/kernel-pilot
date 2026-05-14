# vLLM Kernel Reference

Repository: <https://github.com/vllm-project/vllm>

Use vLLM as a production prior for paged attention, quantized decode GEMM, KV
cache movement, and backend dispatch. Do not copy tuned kernel bodies.

## Read Order

1. Python operator or backend selector.
2. C++/CUDA binding and launch wrapper.
3. Kernel implementation plus shape guards.
4. Test and benchmark coverage.
5. Related upstream source, often FlashInfer, FlashAttention, CUTLASS, or
   PyTorch.

## Code Map

| Area | Paths to inspect |
| --- | --- |
| CUDA/C++ kernels | `csrc/` |
| Attention | `csrc/attention/`, `vllm/attention/`, `vllm/attention/backends/` |
| KV cache | `csrc/cache_kernels.cu`, cache/block-table utilities |
| MoE | `csrc/moe/`, `vllm/model_executor/layers/fused_moe/` |
| Quantization | `csrc/quantization/`, Marlin, Machete, AWQ, GPTQ, FP8 paths |
| CUTLASS glue | `csrc/cutlass_extensions/` |
| Python layer wrappers | `vllm/model_executor/layers/` |
| Tests/benchmarks | `tests/`, `benchmarks/` |

## Search Patterns

```bash
rg -n "paged_attention|block_table|cache_kernels|marlin|machete|awq|gptq|fp8|cutlass" csrc vllm tests benchmarks
rg -n "backend|dispatch|head_size|block_size|num_heads|kv_cache_dtype" vllm csrc
rg -n "benchmark|pytest|parametrize|CUDA_VISIBLE_DEVICES" tests benchmarks
```

## Baseline Extraction

- Confirm which backend is active for the hardware and shape. vLLM often keeps
  older kernels alive for specific decode paths.
- Capture block size, KV cache layout, group size, quant scales, and output
  tolerance before translating to a standalone harness.
- Separate framework overhead from kernel time. Prefer CUDA events or an
  existing microbench when available.

## Candidate Translation

Translate:

- block-table layout and shape contracts
- dequant scale layout and quant group semantics
- benchmark shape families
- backend-dispatch constraints

Do not copy Marlin, Machete, paged attention, or fused MoE kernel bodies.

## NCU Focus

| Kernel family | First metrics |
| --- | --- |
| Paged attention | long scoreboard, global load sectors, L2 bytes, occupancy |
| Quant decode GEMM | tensor pipe %, DRAM/L2 %, issue stalls, register pressure |
| KV cache movement | DRAM throughput, store/load coalescing, memory transactions |
| MoE routing/permutation | long scoreboard, branch divergence, shared bank conflicts |

## Useful Cross-Framework Priors

- FlashInfer for modern paged/prefix attention interfaces.
- SGLang for comparable serving dispatch and SGLang-specific hot paths.
- TensorRT-LLM for NVIDIA-style decode attention and quant GEMM.
- CUTLASS for GEMM tile/schedule/epilogue ideas.

