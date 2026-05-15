# NVIDIA CUDA Developer Blog

CUDA blog index: <https://developer.nvidia.com/blog/tag/cuda/>

Companion code:

- <https://github.com/NVIDIA-developer-blog/code-samples>
- <https://github.com/NVIDIA/cuda-samples>

Use this source for official CUDA optimization patterns and small companion
kernels.

## Article / Code Map

| Kernel family | Article/source | Companion code |
| --- | --- | --- |
| Warp reductions | `Faster Parallel Reductions on Kepler` | `NVIDIA-developer-blog/code-samples/posts/parallel_reduction_with_shfl/` |
| Warp vote/shuffle atomics | `Voting and Shuffling to Optimize Atomic Operations` | search `posts/` for shuffle/vote examples |
| Tensor cores | CUDA tensor core blog/tutorials | `NVIDIA-developer-blog/code-samples/posts/tensor-cores/simpleTensorCoreGEMM.cu` |
| Mixed precision | mixed precision posts | `posts/mixed-precision/haxpy.cu`, `fp16_conversion.h` |
| NVTX / profiling | NVTX posts | `posts/nvtx/manual_nvtx.cu`, `compiler_inst_nvtx.cu` |
| Unified memory | UM posts | `posts/unified-memory/`, `posts/unified-memory-oversubscription/` |
| CUDA VMM | VMM posts | `posts/cuda-vmm/` |
| Official samples | CUDA samples | `NVIDIA/cuda-samples/Samples/*` |

## Companion Code Categories

| Repo/path | Kernel type | What to extract |
| --- | --- | --- |
| `posts/parallel_reduction_with_shfl/block_reduce.h` | block reduction | warp reductions plus block-level aggregation |
| `posts/parallel_reduction_with_shfl/warp_reduce.h` | warp reduction | `__shfl_down` reduction pattern |
| `posts/tensor-cores/simpleTensorCoreGEMM.cu` | WMMA GEMM | minimal tensor-core GEMM structure |
| `posts/mixed-precision/haxpy.cu` | vector op | half conversion and vector arithmetic |
| `posts/gups/gups.cu` | random access | memory system stress pattern |
| `posts/nvtx/*.cu` | profiling | NVTX annotation patterns |
| `NVIDIA/cuda-samples/Samples/2_Concepts_and_Techniques/` | primitives | scan, reduction, sorting, shared-memory examples |
| `NVIDIA/cuda-samples/Samples/3_CUDA_Features/` | features | cooperative groups, async copy, graph, surface/texture features |

## Search Patterns

```bash
rg -n "shfl|warp_reduce|block_reduce|wmma|mma|tensor core|shared|bank|coales|atomic|nvtx|cudaEvent" posts Samples
```

## Optimization Signals

- Reductions: issue stalls, synchronization stalls, shared conflicts, active
  cycles, global sectors.
- Tensor core examples: tensor pipe %, occupancy, register pressure, memory
  bandwidth.
- Profiling examples: use NVTX ranges to isolate candidate kernels in nsys/ncu.
