# kernel-knowledge References

This directory holds the detailed reference layer for KernelPilot. Keep
`knowledge/frameworks/*.md` and `knowledge/topics/*.md` as lightweight routing
pages; load files here only when the task needs the extra detail.

## Core Kernel Loop References

Read these for loop discipline, CUDA implementation, profiling, and architecture
specifics:

| Need | Read |
| --- | --- |
| Iteration loop, harness layout, validation gates | `ako4all/ako4all-kernel-loop.md` |
| CUDA C++ / PTX candidate work | `ako4all/cuda-cpp-kernel-reference.md`, `ako4all/cuda-cpp/cuda-cpp-overview.md` |
| CUTLASS / CuTe prior-art reading | `ako4all/cutlass-cpp-kernel-reference.md`, `ako4all/cutlass-cpp/cutlass-cpp-overview.md` |
| Nsight Compute / Nsight Systems evidence | `ako4all/profiling-debugging-reference.md` |
| Hopper H100 tuning | `ako4all/nvidia-architecture-reference.md`, `ako4all/architectures/sm90-optimization-guide.md` |
| Kernel templates and debugging | `ako4all/kernel-templates.md`, `ako4all/troubleshooting.md` |

The full copied AKO4ALL attribution is preserved in
`ako4all/source-attribution.md`.

## Framework Deep References

Read one of these when the target kernel or baseline comes from a specific
framework:

| Framework | Deep reference |
| --- | --- |
| SGLang | `frameworks/sglang.md` |
| vLLM | `frameworks/vllm.md` |
| TensorRT-LLM | `frameworks/tensorrt-llm.md` |
| PyTorch | `frameworks/pytorch.md` |
| FlashInfer | `frameworks/flashinfer.md` |
| CUTLASS / CuTe | `frameworks/cutlass.md` |

## Use Rules

- Prefer code, tests, benchmarks, and open PRs/issues before docs or blogs.
- Treat all framework kernels as prior art unless the user explicitly asks for
  an in-place framework patch.
- Candidate implementations stay naive hand-written CUDA C++ in `.cu` / `.cuh`.
- Log every source-derived idea with source path or URL, hypothesis, result, and
  a do-not-reread key.
