# Kernel Topics Index

A short cross-reference of all topic pages. During a Humanize loop, open the
topic page that matches the target operator and use it to choose code-first
sources to inspect.

| Topic | Page | Applies to |
| --- | --- | --- |
| Attention / FMHA / Paged | `routing/topics/attention.md` | sglang, vllm, tensorrt-llm, flash-attention, flashinfer, pytorch, thunderkittens, cutlass, triton, tilelang, cute-dsl, quack, veitner-blog, colfax-research |
| GEMM / Tensor-Core matmul | `routing/topics/matmul-gemm.md` | cutlass, deepgemm, tensorrt-llm, sglang, vllm, triton, thunderkittens, pytorch, tilelang, cute-dsl, quack, tilekernels, cuda-blog-kernels, veitner-blog, colfax-research |
| Mixture of Experts | `routing/topics/moe.md` | sglang, vllm, tensorrt-llm, deepgemm, triton, tilelang, tilekernels, cute-dsl, veitner-blog, colfax-research |
| Normalization (RMS / LN / QK-Norm) | `routing/topics/normalization.md` | sglang, vllm, tensorrt-llm, pytorch, triton, cccl-cub, tilelang, quack, cuda-blog-kernels, veitner-blog |
| RoPE | `routing/topics/rope.md` | sglang, vllm, tensorrt-llm, flashinfer, triton |
| Activation / element-wise fusion | `routing/topics/activation-fusion.md` | sglang, vllm, tensorrt-llm, pytorch, triton, tilelang, tilekernels, quack, veitner-blog |
| Sampling / speculative decode | `routing/topics/sampling.md` | sglang, vllm, tensorrt-llm, flashinfer |
| Quantization (FP8 / FP4 / INT8 / AWQ / GPTQ) | `routing/topics/quantization-fp8.md` | sglang, vllm, tensorrt-llm, deepgemm, cutlass, tilelang, tilekernels, cute-dsl, quack, veitner-blog, colfax-research |
| KV-cache / paged memory | `routing/topics/kv-cache.md` | sglang, vllm, tensorrt-llm, flashinfer |
| Communication / overlap | `routing/topics/communication.md` | pytorch, tensorrt-llm, sglang |
