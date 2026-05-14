# Kernel Topics Index

A short cross-reference of all topic pages. During a Humanize loop, open the
topic page that matches the target operator and use it to choose code-first
sources to inspect.

| Topic | Page | Applies to |
| --- | --- | --- |
| Attention / FMHA / Paged | `topics/attention.md` | sglang, vllm, tensorrt-llm, flash-attention, flashinfer, pytorch, thunderkittens, cutlass |
| GEMM / Tensor-Core matmul | `topics/matmul-gemm.md` | cutlass, deepgemm, tensorrt-llm, sglang, vllm, triton, thunderkittens, pytorch |
| Mixture of Experts | `topics/moe.md` | sglang, vllm, tensorrt-llm, deepgemm, triton |
| Normalization (RMS / LN / QK-Norm) | `topics/normalization.md` | sglang, vllm, tensorrt-llm, pytorch, triton, cccl-cub |
| RoPE | `topics/rope.md` | sglang, vllm, tensorrt-llm, flashinfer, triton |
| Activation / element-wise fusion | `topics/activation-fusion.md` | sglang, vllm, tensorrt-llm, pytorch, triton |
| Sampling / speculative decode | `topics/sampling.md` | sglang, vllm, tensorrt-llm, flashinfer |
| Quantization (FP8 / FP4 / INT8 / AWQ / GPTQ) | `topics/quantization-fp8.md` | sglang, vllm, tensorrt-llm, deepgemm, cutlass |
| KV-cache / paged memory | `topics/kv-cache.md` | sglang, vllm, tensorrt-llm, flashinfer |
| Communication / overlap | `topics/communication.md` | pytorch, tensorrt-llm, sglang |
