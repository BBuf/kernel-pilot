# Kernel Source Catalog

This catalog lists repositories and documentation worth reading before proposing
GPU-kernel optimization ideas. Use it as reference material for Humanize-driven
kernel loops.

The machine-readable version is `kernel-source-catalog.json`.

## Reference Repositories

| Repository | Link | Read first |
| --- | --- | --- |
| `BBuf/AI-Infra-Auto-Driven-SKILLS` | https://github.com/BBuf/AI-Infra-Auto-Driven-SKILLS/tree/main/skills/gpu-kernel-ako4all/references | AKO loop discipline, CUDA C++, Triton, profiling, architecture notes |
| `NVIDIA/cutlass` | https://github.com/NVIDIA/cutlass | CUTLASS, CuTe C++, CuTe DSL, profiler, examples, tests |
| `NVIDIA/cuda-samples` | https://github.com/NVIDIA/cuda-samples | official CUDA samples, memory, streams, cooperative groups, CUDA Graphs |
| `NVIDIA/cccl` | https://github.com/NVIDIA/cccl | CUB, Thrust, libcu++, block/warp primitives, reductions, scans |
| `NVIDIA/CUDALibrarySamples` | https://github.com/NVIDIA/CUDALibrarySamples | cuBLAS, cuBLASLt, cuBLASDx, cuDNN, official library harnesses |
| `NVIDIA/cudnn-frontend` | https://github.com/NVIDIA/cudnn-frontend | cuDNN backend graph/frontend API, samples, attention and fused-op baselines |
| `NVIDIA/nvbench` | https://github.com/NVIDIA/nvbench | CUDA microbenchmark methodology and result reporting |
| `NVIDIA/cuda-tile` | https://github.com/NVIDIA/cuda-tile | tile IR, tensor core targeting, compiler scheduling ideas |
| `triton-lang/triton` | https://github.com/triton-lang/triton | Triton compiler, tutorials, language semantics, backend behavior |
| `tile-ai/tilelang` | https://github.com/tile-ai/tilelang | tile-level DSL schedules and generated kernels |
| `gpu-mode/reference-kernels` | https://github.com/gpu-mode/reference-kernels | GPU MODE leaderboard problem sets and reference kernels |
| `gpu-mode/kernelbot` | https://github.com/gpu-mode/kernelbot | AI-versus-human kernel competition workflow and harnesses |
| `gpu-mode/Triton-Puzzles` | https://github.com/gpu-mode/Triton-Puzzles | Triton puzzles for program ids, masks, reductions, and memory behavior |
| `HazyResearch/ThunderKittens` | https://github.com/HazyResearch/ThunderKittens | tile primitives, attention, matmul, and warpgroup-level CUDA patterns |
| `leimao/CUDA-GEMM-Optimization` | https://github.com/leimao/CUDA-GEMM-Optimization | stepwise CUDA GEMM optimization |
| `ColfaxResearch/cutlass-kernels` | https://github.com/ColfaxResearch/cutlass-kernels | CUTLASS and CuTe tutorial kernels |
| `moderngpu/moderngpu` | https://github.com/moderngpu/moderngpu | classic GPU primitives, scan, sort, merge, load balancing |
| `huggingface/kernels` | https://github.com/huggingface/kernels | reusable kernel packaging, tests, and benchmarks |
| `flashinfer-ai/flashinfer` | https://github.com/flashinfer-ai/flashinfer | `csrc`, `csrc/fmha_v2/fmha`, `csrc/fmha_v2/fmha/hopper`, `csrc/fmha_v2/fmha/warpspec`, `benchmarks/bench_blackwell_attention.py` |
| `Dao-AILab/flash-attention` | https://github.com/Dao-AILab/flash-attention | `csrc/flash_attn/src`, `flash_attn/cute`, `benchmarks/benchmark_attn.py`, `benchmarks/bench_sm90.py` |
| `Tencent/hpc-ops` | https://github.com/Tencent/hpc-ops | `hpc/attention.py`, `hpc/group_gemm.py`, `hpc/normalization.py`, `hpc/rope.py`, `src/attention`, `src/group_gemm`, `src/normalization`, `src/rope`, `tests/` |
| `deepseek-ai/DeepGEMM` | https://github.com/deepseek-ai/DeepGEMM | `csrc/apis`, `csrc/jit`, `csrc/jit_kernels/heuristics`, `csrc/jit_kernels/impls`, `deep_gemm/include/deep_gemm`, `deep_gemm/testing`, `tests/` |

## Official Docs And Expert Blogs

| Source | Link | Read first |
| --- | --- | --- |
| CUDA C++ Programming Guide | https://docs.nvidia.com/cuda/cuda-c-programming-guide/ | execution model, memory hierarchy, cooperative groups, async copy |
| CUDA C++ Best Practices Guide | https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/ | memory coalescing, shared memory, occupancy, metrics |
| PTX ISA | https://docs.nvidia.com/cuda/parallel-thread-execution/ | inline PTX, tensor core instructions, memory scopes |
| CUDA Binary Utilities | https://docs.nvidia.com/cuda/cuda-binary-utilities/ | cuobjdump, nvdisasm, SASS inspection |
| Nsight Compute Profiling Guide | https://docs.nvidia.com/nsight-compute/ProfilingGuide/ | roofline, memory workload, scheduler stats, source correlation |
| CUTLASS Documentation | https://docs.nvidia.com/cutlass/ | CUTLASS, CuTe, CuTe DSL, collectives, epilogues |
| Blackwell Tuning Guide | https://docs.nvidia.com/cuda/blackwell-tuning-guide/index.html | Blackwell SM behavior, shared memory, thread block clusters, B200 tuning |
| Hopper Tuning Guide | https://docs.nvidia.com/cuda/hopper-tuning-guide/index.html | Hopper SM behavior, TMA, thread block clusters, H100 tuning |
| Ampere Tuning Guide | https://docs.nvidia.com/cuda/ampere-tuning-guide/index.html | async copy, split barriers, warp reductions, A100 tuning |
| NVIDIA CUDA Blog | https://developer.nvidia.com/blog/tag/cuda/ | official CUDA optimization articles |
| NVIDIA CUTLASS Blog | https://developer.nvidia.com/blog/tag/cutlass/ | official CUTLASS and tensor core articles |
| Colfax Research | https://research.colfax-intl.com/ | human-expert CUTLASS, CuTe, GEMM, and warpgroup tutorials |
| Simon Boehm CUDA Matmul | https://siboehm.com/articles/22/CUDA-MMM | stepwise CUDA matmul optimization |
| Lei Mao CUDA Programming | https://leimao.github.io/blog/CUDA-Programming/ | CUDA GEMM, bank conflicts, reductions, transpose, benchmarking |
| Yifan Yang CUDA Matmul | https://yang-yifan.github.io/blogs/reg_tile/reg_tile.html | register tiling, roofline reasoning, matmul bottlenecks |

## Usage Rules

1. Read code first: production kernel paths, tests, benchmarks, and open
   PRs/issues have priority over official docs, expert blogs, and articles.
2. Do not copy external kernel code into a candidate.
3. Target-project code is used for APIs, tests, benchmark contracts,
   integration, and old-vs-new comparison.
4. Every source-derived idea must be logged with repository link, source path,
   exact hypothesis, and measured result. During plateau-driven research passes,
   also record a do-not-reread key.
