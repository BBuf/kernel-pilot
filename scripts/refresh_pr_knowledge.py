#!/usr/bin/env python3
"""Refresh the PR-driven kernel knowledge layer.

This script uses the GitHub CLI to collect merged and open pull requests from
kernel-heavy repositories, filters out release/CI/backend noise, and regenerates
human-readable PR notes plus machine-readable metadata.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_SINCE = "2024-05-15"


@dataclass(frozen=True)
class RepoConfig:
    display: str
    repo: str
    target: int
    queries: tuple[str, ...]


GENERIC_CUDA_QUERIES = (
    "CUDA kernel",
    "cuda kernel",
    "kernel optimization",
    "performance kernel",
    "optimize kernel",
    "faster kernel",
    "benchmark cuda",
    "ncu",
    "nsight compute",
    "gemm",
    "matmul",
    "attention",
    "reduction",
    "scan",
    "sort",
    "transpose",
    "shared memory",
    "coalescing",
    "tensor core",
    "wmma",
    "mma",
    "tma",
    "wgmma",
    "fp8",
    "fp4",
    "int8",
)


REPOS: dict[str, RepoConfig] = {
    "cutlass": RepoConfig(
        "CUTLASS / CuTe",
        "NVIDIA/cutlass",
        34,
        (
            "sm90",
            "sm100",
            "sm120",
            "hopper",
            "blackwell",
            "wgmma",
            "tma",
            "tcgen05",
            "warp specialization",
            "persistent gemm",
            "stream-k",
            "grouped gemm",
            "blockscaled",
            "block scaled",
            "fp8",
            "fp4",
            "mxfp4",
            "nvfp4",
            "int8",
            "epilogue",
            "EVT",
            "scheduler",
            "collective builder",
            "cute dsl",
            "MLA",
            "FMHA",
        ),
    ),
    "pytorch": RepoConfig(
        "PyTorch",
        "pytorch/pytorch",
        26,
        (
            "CUDA kernel",
            "Triton kernel",
            "scaled_dot_product attention cuda",
            "flex_attention GPU",
            "Inductor Triton heuristic",
            "persistent matmul",
            "max autotune",
            "cpp_wrapper_gpu",
            "aotinductor gpu",
            "cutlass backend",
            "cuda graph kernel",
            "template heuristic",
            "device-side TMA",
            "fp8 matmul",
            "block scaled",
            "benchmark cuda",
            "triton matmul",
        ),
    ),
    "sglang": RepoConfig(
        "SGLang",
        "sgl-project/sglang",
        34,
        (
            "sgl-kernel",
            "jit_kernel",
            "CUDA kernel",
            "csrc kernel",
            "sm90",
            "hopper",
            "blackwell",
            "int8 scaled_mm",
            "fp8",
            "fp4",
            "mxfp4",
            "nvfp4",
            "cutlass",
            "deepgemm",
            "flashinfer",
            "moe kernel",
            "fused moe",
            "attention kernel",
            "FlashMLA",
            "triton kernel",
            "fused norm",
            "sampling kernel",
            "PDL",
            "benchmark kernel",
        ),
    ),
    "vllm": RepoConfig(
        "vLLM",
        "vllm-project/vllm",
        34,
        (
            "CUDA kernel",
            "csrc kernel",
            "sm90",
            "sm100",
            "hopper",
            "blackwell",
            "int8 scaled_mm",
            "fp8",
            "fp4",
            "nvfp4",
            "mxfp4",
            "Marlin",
            "Machete",
            "paged attention",
            "FlashInfer",
            "MoE kernel",
            "fused moe",
            "topk",
            "GDN",
            "DeepGEMM",
            "quantization kernel",
            "cutlass",
            "benchmark kernel",
        ),
    ),
    "flashinfer": RepoConfig(
        "FlashInfer",
        "flashinfer-ai/flashinfer",
        34,
        (
            "hopper",
            "blackwell",
            "sm90",
            "sm100",
            "sm120",
            "cuda kernel",
            "cutlass",
            "cute dsl",
            "fp8",
            "fp4",
            "nvfp4",
            "mxfp4",
            "mla",
            "paged attention",
            "BatchDecode",
            "BatchPrefill",
            "GDN",
            "fused moe",
            "sampling",
            "topk",
            "varlen scheduler",
            "TMA",
            "warpspec",
            "benchmark",
        ),
    ),
    "deepgemm": RepoConfig(
        "DeepGEMM",
        "deepseek-ai/DeepGEMM",
        26,
        (
            "fp8",
            "fp4",
            "mxfp4",
            "nvfp4",
            "gemm",
            "grouped gemm",
            "moe",
            "Mega MoE",
            "hopper",
            "blackwell",
            "sm90",
            "sm100",
            "JIT",
            "TMA",
            "benchmark",
            "scheduler",
        ),
    ),
    "tensorrt-llm": RepoConfig(
        "TensorRT-LLM",
        "NVIDIA/TensorRT-LLM",
        34,
        (
            "cuda kernel",
            "hopper",
            "blackwell",
            "sm90",
            "sm100",
            "fp8",
            "fp4",
            "nvfp4",
            "mxfp4",
            "cutlass",
            "trtllmgen",
            "moe",
            "blockScaleMoe",
            "attention kernel",
            "MLA",
            "paged MQA",
            "DSA",
            "userbuffers",
            "allreduce",
            "routing",
            "cute dsl",
            "benchmark kernel",
        ),
    ),
    "flash-attention": RepoConfig(
        "FlashAttention",
        "Dao-AILab/flash-attention",
        24,
        (
            "hopper",
            "blackwell",
            "sm90",
            "sm100",
            "wgmma",
            "tma",
            "flash3",
            "FA3",
            "FA4",
            "cute",
            "cute dsl",
            "fp8",
            "varlen",
            "softcap",
            "head_dim",
            "MLA",
            "paged",
            "block sparse",
            "softmax",
        ),
    ),
    "triton": RepoConfig(
        "Triton",
        "triton-lang/triton",
        28,
        (
            "hopper",
            "blackwell",
            "sm90",
            "sm100",
            "tma",
            "wgmma",
            "warp specialize",
            "persistent matmul",
            "fp8",
            "fp4",
            "mxfp4",
            "tl.dot",
            "matmul",
            "attention",
            "tensor descriptor",
            "swizzle",
            "cuda backend",
            "proton",
            "Gluon",
            "autotune",
        ),
    ),
    "tilelang": RepoConfig(
        "TileLang",
        "tile-ai/tilelang",
        28,
        (
            "gemm",
            "matmul",
            "fp8",
            "fp4",
            "mxfp4",
            "blockscaled",
            "attention",
            "MLA",
            "moe",
            "TMA",
            "WGMMA",
            "tcgen",
            "hopper",
            "blackwell",
            "cuda backend",
            "copy lowering",
            "intrinsic",
            "benchmark",
        ),
    ),
    "quack": RepoConfig(
        "QuACK",
        "Dao-AILab/quack",
        28,
        (
            "gemm",
            "SM90",
            "SM100",
            "SM120",
            "hopper",
            "blackwell",
            "fp8",
            "fp4",
            "TMA",
            "RMSNorm",
            "softmax",
            "cross entropy",
            "epilogue",
            "MoE",
            "tile_K",
            "2CTA",
            "CLC",
            "autotune",
            "benchmark",
            "ncu",
        ),
    ),
    "tilekernels": RepoConfig(
        "DeepSeek TileKernels",
        "deepseek-ai/TileKernels",
        12,
        (
            "kernel",
            "moe",
            "gemm",
            "fp8",
            "quant",
            "transpose",
            "tilelang",
            "engram",
            "swiGLU",
            "benchmark",
        ),
    ),
    "thunderkittens": RepoConfig(
        "ThunderKittens",
        "HazyResearch/ThunderKittens",
        26,
        (
            "kernel",
            "attention",
            "gemm",
            "matmul",
            "hopper",
            "blackwell",
            "wgmma",
            "tma",
            "fp8",
            "MLA",
            "GQA",
            "ring attention",
            "FFTConv",
            "swizzle",
            "pybind",
            "benchmark",
            "educational b200",
        ),
    ),
    "cccl-cub": RepoConfig(
        "CCCL / CUB",
        "NVIDIA/cccl",
        28,
        (
            "CUB",
            "scan",
            "reduce",
            "segmented scan",
            "segmented reduce",
            "radix sort",
            "DeviceTopK",
            "topk",
            "warp reduce",
            "block reduce",
            "benchmark",
            "sm90",
            "sm100",
            "cuda.compute",
            "mdspan copy",
            "transpose",
            "warpspeed scan",
            "policy tuning",
        ),
    ),
    "cuda-samples": RepoConfig(
        "CUDA Samples",
        "NVIDIA/cuda-samples",
        9999,
        GENERIC_CUDA_QUERIES
        + (
            "cooperative groups",
            "cuda graphs",
            "transpose",
            "reduction",
            "matrixMul",
            "simpleCudaGraphs",
        ),
    ),
    "cuda-library-samples": RepoConfig(
        "CUDA Library Samples",
        "NVIDIA/CUDALibrarySamples",
        9999,
        GENERIC_CUDA_QUERIES
        + (
            "cuBLASLt",
            "cuBLASDx",
            "cuDNN",
            "GEMM sample",
            "matmul sample",
        ),
    ),
    "cudnn-frontend": RepoConfig(
        "cuDNN Frontend",
        "NVIDIA/cudnn-frontend",
        9999,
        GENERIC_CUDA_QUERIES
        + (
            "attention",
            "sdpa",
            "flash attention",
            "fusion",
            "graph",
        ),
    ),
    "nvbench": RepoConfig(
        "NVBench",
        "NVIDIA/nvbench",
        9999,
        GENERIC_CUDA_QUERIES
        + (
            "benchmark",
            "measure",
            "throughput",
            "timer",
        ),
    ),
    "cuda-tile": RepoConfig(
        "CUDA Tile",
        "NVIDIA/cuda-tile",
        9999,
        GENERIC_CUDA_QUERIES
        + (
            "tile",
            "tensor core",
            "schedule",
            "compiler",
        ),
    ),
    "gpu-mode-reference-kernels": RepoConfig(
        "GPU MODE Reference Kernels",
        "gpu-mode/reference-kernels",
        9999,
        GENERIC_CUDA_QUERIES
        + (
            "leaderboard",
            "competition",
            "reference kernel",
        ),
    ),
    "gpu-mode-kernelbot": RepoConfig(
        "GPU MODE KernelBot",
        "gpu-mode/kernelbot",
        9999,
        GENERIC_CUDA_QUERIES
        + (
            "submission",
            "benchmark",
            "cuda",
        ),
    ),
    "triton-puzzles": RepoConfig(
        "Triton Puzzles",
        "gpu-mode/Triton-Puzzles",
        9999,
        GENERIC_CUDA_QUERIES
        + (
            "triton",
            "puzzle",
            "program id",
            "mask",
        ),
    ),
    "nvidia-blog-code-samples": RepoConfig(
        "NVIDIA Developer Blog Code Samples",
        "NVIDIA-developer-blog/code-samples",
        9999,
        GENERIC_CUDA_QUERIES
        + (
            "parallel reduction",
            "tensor cores",
            "matrix transpose",
            "shared memory",
            "warp shuffle",
        ),
    ),
    "leimao-cuda-gemm": RepoConfig(
        "Lei Mao CUDA GEMM Optimization",
        "leimao/CUDA-GEMM-Optimization",
        9999,
        GENERIC_CUDA_QUERIES
        + (
            "gemm optimization",
            "wmma",
            "shared memory",
        ),
    ),
    "siboehm-sgemm": RepoConfig(
        "Simon Boehm SGEMM CUDA",
        "siboehm/SGEMM_CUDA",
        9999,
        GENERIC_CUDA_QUERIES
        + (
            "sgemm",
            "coalescing",
            "double buffering",
            "vectorize",
        ),
    ),
    "colfax-cutlass-kernels": RepoConfig(
        "Colfax CUTLASS Kernels",
        "ColfaxResearch/cutlass-kernels",
        9999,
        GENERIC_CUDA_QUERIES
        + (
            "cutlass",
            "cute",
            "fmha",
            "stream-k",
            "pipeline",
        ),
    ),
    "colfax-article-src": RepoConfig(
        "Colfax Article Source",
        "ColfaxResearch/cfx-article-src",
        9999,
        GENERIC_CUDA_QUERIES
        + (
            "tma",
            "pipeline-gemm",
            "streamk",
            "transpose-cute",
            "evt",
        ),
    ),
    "simveit-effective-transpose": RepoConfig(
        "Veitner Effective Transpose",
        "simveit/effective_transpose",
        9999,
        GENERIC_CUDA_QUERIES
        + (
            "transpose",
            "tma",
            "swizzle",
            "shared memory",
        ),
    ),
    "simveit-load-and-store": RepoConfig(
        "Veitner Load And Store",
        "simveit/load_and_store",
        9999,
        GENERIC_CUDA_QUERIES
        + (
            "ldmatrix",
            "stmatrix",
            "ptx",
            "load matrix",
            "store matrix",
        ),
    ),
    "moderngpu": RepoConfig(
        "ModernGPU",
        "moderngpu/moderngpu",
        9999,
        GENERIC_CUDA_QUERIES
        + (
            "scan",
            "sort",
            "merge",
            "load balancing",
            "reduce",
        ),
    ),
    "huggingface-kernels": RepoConfig(
        "Hugging Face Kernels",
        "huggingface/kernels",
        9999,
        GENERIC_CUDA_QUERIES
        + (
            "triton",
            "cuda",
            "benchmark",
            "kernel package",
        ),
    ),
    "tencent-hpc-ops": RepoConfig(
        "Tencent HPC Ops",
        "Tencent/hpc-ops",
        9999,
        GENERIC_CUDA_QUERIES
        + (
            "attention",
            "group gemm",
            "normalization",
            "rope",
        ),
    ),
}


CATEGORY_PROFILES: dict[str, dict[str, Any]] = {
    "gemm_quant": {
        "title": "GEMM / Quantization",
        "terms": (
            "gemm",
            "matmul",
            "scaled_mm",
            "fp8",
            "fp4",
            "mxfp4",
            "nvfp4",
            "int8",
            "marlin",
            "machete",
            "blockwise",
            "blockscaled",
            "dequant",
            "quant",
            "w4a16",
            "w8a8",
            "mx",
            "mxfp8",
        ),
        "recipe": "Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate.",
        "ncu": "Tensor pipe %, DRAM/L2 bytes, active cycles, register pressure, and scale-load traffic.",
        "questions": (
            "Which tile/schedule and scale layout made the PR worthwhile?",
            "Which shape family or tail case was protected by tests/benchmarks?",
        ),
    },
    "attention_kv": {
        "title": "Attention / KV / Decode",
        "terms": (
            "attention",
            "flash",
            "mla",
            "paged",
            "kv",
            "decode",
            "prefill",
            "gdn",
            "fa3",
            "fa4",
            "softmax",
            "head_dim",
            "batchdecode",
            "batchprefill",
            "xqa",
            "sageattention",
        ),
        "recipe": "Preserve page/KV/layout and plan-run contracts; profile memory traffic separately from math utilization.",
        "ncu": "Long scoreboard, L2/DRAM traffic, global-load sectors, tensor pipe %, and shared-memory bank conflicts.",
        "questions": (
            "Which KV/page/block-table invariant does the PR rely on?",
            "Is the measured win from memory coalescing, launch reduction, or tensor-core utilization?",
        ),
    },
    "moe_routing": {
        "title": "MoE / Routing",
        "terms": (
            "moe",
            "expert",
            "routing",
            "topk",
            "allreduce",
            "all-to-all",
            "alltoall",
            "permutation",
            "grouped",
            "mega moe",
        ),
        "recipe": "Separate routing, permutation, top-k, and expert GEMM costs; keep tail-token and expert-layout tests attached to the idea.",
        "ncu": "Tensor pipe %, SM imbalance, branch divergence, L2 traffic, permutation traffic, and synchronization stalls.",
        "questions": (
            "Does the PR optimize routing/permutation or the expert GEMM itself?",
            "Which expert-count, token-count, and group-size cases need replay?",
        ),
    },
    "norm_elementwise": {
        "title": "Norm / Elementwise / Epilogue",
        "terms": (
            "norm",
            "rms",
            "layernorm",
            "silu",
            "swiglu",
            "activation",
            "elementwise",
            "epilogue",
            "snake",
            "cross entropy",
            "hc kernel",
        ),
        "recipe": "Look for fusion, vectorization, dtype conversion, and store-traffic reductions before changing math.",
        "ncu": "DRAM %, L2 bytes, global load/store sectors, eligible warps, and long scoreboard.",
        "questions": (
            "Which loads/stores were eliminated or vectorized?",
            "Does the PR preserve dtype conversion and numerical tolerance?",
        ),
    },
    "memory_primitives": {
        "title": "Memory / Primitives",
        "terms": (
            "scan",
            "reduce",
            "sort",
            "radix",
            "copy",
            "transpose",
            "mdspan",
            "cub",
            "thrust",
            "cache",
            "gather",
            "scatter",
            "memcpy",
            "tma load",
            "d2d",
        ),
        "recipe": "Transfer primitive policy carefully: coalescing, shared-memory staging, partial tiles, and determinism are part of the contract.",
        "ncu": "DRAM throughput, L2 hit rate, memory sectors, shared-memory conflicts, and synchronization overhead.",
        "questions": (
            "Which primitive policy changed and how is it specialized by architecture?",
            "Are deterministic behavior and partial-tile behavior preserved?",
        ),
    },
    "scheduler_autotune": {
        "title": "Scheduler / Autotune",
        "terms": (
            "persistent",
            "streamk",
            "stream-k",
            "scheduler",
            "autotune",
            "tuning",
            "config",
            "heuristic",
            "2cta",
            "clc",
            "split",
            "varlen",
            "work stealing",
            "pdl",
        ),
        "recipe": "Treat scheduler/autotune configs as shape-specific evidence; replay benchmark shapes before generalizing.",
        "ncu": "SM occupancy, waves/SM, active cycles, tail effects, and load imbalance.",
        "questions": (
            "Which shape regime caused the scheduling change?",
            "Can the idea become a dispatcher rule rather than one monolithic kernel?",
        ),
    },
    "arch_pipeline": {
        "title": "Architecture / Pipeline",
        "terms": (
            "sm90",
            "sm100",
            "sm120",
            "sm121",
            "hopper",
            "blackwell",
            "b200",
            "gb200",
            "tma",
            "wgmma",
            "tcgen",
            "tcgen05",
            "warp",
            "warpspec",
            "cluster",
        ),
        "recipe": "Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages.",
        "ncu": "Tensor pipe %, memory pipe utilization, barrier stalls, wait groups, and occupancy.",
        "questions": (
            "Which architecture feature is essential rather than incidental?",
            "What fallback is needed for the current GPU target?",
        ),
    },
    "compiler_runtime": {
        "title": "Compiler / Runtime",
        "terms": (
            "inductor",
            "triton",
            "cute",
            "cutedsl",
            "cute dsl",
            "tilelang",
            "cuda backend",
            "cpp_wrapper",
            "jit",
            "aot",
            "proton",
            "gluon",
            "cutlass dsl",
            "nvrtc",
        ),
        "recipe": "Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests.",
        "ncu": "Generated kernel shape, launch overhead, occupancy, register pressure, and compile-time-selected schedule.",
        "questions": (
            "Which generated source or wrapper changed the runtime behavior?",
            "How should standalone candidates reproduce the same launch and cache contract?",
        ),
    },
    "benchmark_test": {
        "title": "Benchmark / Test Evidence",
        "terms": (
            "benchmark",
            "bench",
            "test",
            "ncu",
            "profile",
            "nsys",
            "perf",
            "throughput",
            "latency",
        ),
        "recipe": "Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code.",
        "ncu": "Use the PR's benchmark/profile command as the first replay target.",
        "questions": (
            "Which benchmark shape distribution did the PR validate?",
            "Which correctness/tolerance test should become part of the standalone harness?",
        ),
    },
    "kernel_other": {
        "title": "Other Kernel Cases",
        "terms": (),
        "recipe": "Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea.",
        "ncu": "Choose metrics based on the changed kernel family after opening the diff.",
        "questions": (
            "Which source paths actually changed kernel behavior?",
            "What evidence makes this more than integration churn?",
        ),
    },
}

CATEGORY_ORDER = tuple(CATEGORY_PROFILES)
PR_REFERENCE_ONLY_REPOS = {
    # These repositories are useful source/profiling references, but their PRs
    # mostly change tooling or service infrastructure rather than concrete CUDA
    # kernel optimizations.
    "nvbench",
    "gpu-mode-kernelbot",
}

SOURCE_FILE_RE = re.compile(
    r"(\.(cu|cuh|c|cc|cpp|cxx|h|hpp|inl|py)$|csrc/|sgl-kernel/|jit_kernel/|aten/src/|torch/_inductor/|"
    r"vllm/model_executor/|vllm/v1/|flashinfer/|include/|cpp/|quack/|"
    r"tile_kernels/|kernels/|src/|source/|samples/|Samples/|posts/|python/triton|examples/|benchmark/|"
    r"benchmarks/|microbenchmarks/|tests?/kernels|test/inductor|cub/|cudax/|cuda/|cuda-kernels/)",
    re.I,
)
KERNEL_SIGNAL_RE = re.compile(
    r"(kernel|cuda|csrc|sgl-kernel|jit_kernel|gemm|matmul|attention|mla|moe|"
    r"fp8|fp4|mxfp4|nvfp4|int8|cutlass|cute|triton|tilelang|deepgemm|"
    r"flashinfer|marlin|machete|tma|wgmma|tcgen|rms|norm|topk|paged|kv|"
    r"scan|reduce|sort|transpose|benchmark|profile|ncu|autotune|scheduler|"
    r"persistent|cub|thrust|epilogue|warpspec|blockscaled|optimization|optimize|"
    r"faster|speedup|coalesc|shared memory|tensor core|wmma|ldmatrix|stmatrix)",
    re.I,
)
REJECT_TITLE_RE = re.compile(
    r"(^v?\d+(?:\.\d+)+|\bv\d+(?:\.\d+)+.*update|dev update|release only|"
    r"\[release-only changes\]|branch cut for release|release triton to pypi|release notes?|"
    r"^\s*#?\s*.*frontend v\d+.*release|^release\b|\[rel/|tag release|tag update|"
    r"release update|version bump|bump .*version|"
    r"^\s*(\[.*\])?\s*bump\b|\bbump\b.*(acorn|cutedsl|version|dependency)|"
    r"bump pin|bump fbgemm|dependabot|cherry[-\s]*pick|\brevert\b|ruff|pre-commit|typo|"
    r"\[docs?\]|^\s*docs?:|\bdocs?\b|\breadme\b|\[documentation\]|"
    r"doc change|documentation only|documentation updates?|installation instructions|"
    r"document usage|workflow|kernels upload|set version|release workflow|"
    r"cookbook image|\bcookbook\b|ci:|\[ci\]|bump ci|nightly migration|"
    r"conditional split|split .*stage|migrate .*test/registered|pytest exit code|"
    r"release-whl|release-docker|\bMPS\b|\bROCm\b|\bAMD\b|\bMUSA\b|"
    r"\bAscend\b|\bNPU\b|\bXPU\b|\bSYCL\b|\boneAPI\b|\bIntel\b|\bCPU\b|\bHIP_VERSION\b|"
    r"\bMLX\b|\bAITER\b|\bDNNL\b|\bAVX2\b|"
    r"\bMetal\b|\bRVV\b|\bRISC\b|\briscv\b|"
    r"\bWindows\b|benchmark\] skip|skip .*benchmark|"
    r"SPDX|copyright header|copyright headers|\bMyPy\b|mypy|"
    r"test infrastructure|strict C\+\+ compiler warnings|"
    r"Fix example imports|Fix incorrect example paths|example paths|docstrings?|CUDA version checking|"
    r"Break up .*fbgemm_cuda_utils|torch\s+2\.11\s+upgrade|prep for torch|"
    r"bump\s+(flashinfer|nvidia|cutlass|docker|torch))",
    re.I,
)
BACKEND_NOISE_RE = re.compile(
    r"\b(MPS|ROCm|AMD|MUSA|Ascend|NPU|XPU|SYCL|oneAPI|Intel|CPU|Metal|RVV|"
    r"RISC-V|riscv|HIP|MLX|Apple|AITER|DNNL|AVX2|MI\d{3,4}X?)\b",
    re.I,
)
INFRA_NOISE_RE = re.compile(
    r"(dependency|nvidia-cutlass-dsl|upgrade to cutlass|unpin .*dependencies|"
    r"kernel-builder|nix|cargo|upload|trusted publishers|build-and-upload|"
    r"kernel-abi-check|kernels-data|cmake template|pyproject|workflow|web-ui|"
    r"api-url|wait time|timeout|updated_at|setup fixes|build scripts|"
    r"line info|debug/relwithdebinfo|unsupported architectures|vulnerabilities|"
    r"unused param|memory leak|check_cuda|rst to mdx|minor edits)",
    re.I,
)
PERF_ACTION_RE = re.compile(
    r"(optimi[sz]e|optimization|speedup|faster|\bperf\b|performance|benchmark|profile|ncu|"
    r"nsight|latency|throughput|bandwidth|dram|occupancy|tune|autotune|heuristic|"
    r"scheduler|persistent|stream-?k|split-?k|pipeline|prefetch|fusion|fuse|fused|"
    r"vectori[sz]|coalesc|shared memory|tensor core|warmup|dispatch|selection|"
    r"low latency|fast path|microbenchmark|blockwise|groupwise|blockscaled|parallelization)",
    re.I,
)
KERNEL_FAMILY_RE = re.compile(
    r"(gemm|matmul|attention|mla|moe|router|routing|norm|rmsnorm|layernorm|topk|top-k|"
    r"sampling|reduce|reduction|scan|sort|transpose|quant|dequant|epilogue|softmax|"
    r"mamba|selective[_ -]?state|allreduce|all-reduce|coalesc|bank conflict|gups|"
    r"copy|memcpy|d2d|kv|kvcache|gqa|decode|prefill|paged)",
    re.I,
)
KERNEL_SPECIALIZATION_RE = re.compile(
    r"(fp8|fp4|mxfp4|nvfp4|int8|int4|w4a|w8a|sm90|sm100|sm120|sm12x|hopper|"
    r"blackwell|b200|h100|h200|gb200|tma|wgmma|mma|tcgen|cute|cutlass|triton|"
    r"tilelang|deepgemm|flashinfer|flashmla|marlin|machete)",
    re.I,
)
KERNEL_ACTION_RE = re.compile(
    r"(add|support|implement|enable|port|migrate|replace|select|route|tune|"
    r"speciali[sz]e|integrate|use|default|switch)",
    re.I,
)
NOISE_TITLE_RE = re.compile(
    r"(pytest|unit tests?|test-only|tests? path|ci\b|nightly|est_time|expected accuracy|"
    r"tutorial|notebook|example|demo|comment|grammar|nit\b|minor|rename|cleanup|"
    r"refactor|restruct|migrate|build|compile|compilation|compatibility|import-time|link error|cmake|wheel|docker|"
    r"artifact|install|codeowners?|skills?|workflow|release|version|dependency|"
    r"metadata|license|upload|queue race|dead code|format|lint|warning|readme|docs?|"
    r"model support|support .*models?|onboard|re-onboard|modelopt .*support|"
    r"^\s*(\[.*\])?\s*chore\b|^\s*(\[.*\])?\s*\[.*infra.*\]|"
    r"\binfra\b|github pipeline|required changes|compressed archives?|"
    r"update .* from |review feedback|non-blocking review|add guard|"
    r"host-side cflags|aarch64|tvm_ffi|default disable|disable .*fusion|"
    r"unused variable|bad links?|coderabbit feedback|fallback guards?|"
    r"legacy .* path|declare .* scope|string truthiness|accuracy issue|"
    r"illegal memory|out[- ]?of[- ]?bounds|\boob\b|overflow|use-after-free|"
    r"kwarg mismatch|wrong order|invalid value|\bbug\b)",
    re.I,
)
STRONG_PERF_WORD_RE = re.compile(
    r"(optimi[sz]e|speedup|faster|\bperf\b|performance|latency|throughput|bandwidth|dram|"
    r"occupancy|profile|ncu|nsight|low latency|fast path)",
    re.I,
)
OPTIMIZATION_MECHANISM_RE = re.compile(
    r"(tma|wgmma|tcgen|mma|tensor core|warp speciali[sz]|producer-consumer|"
    r"persistent|stream-?k|split-?k|split kv|pipeline|prefetch|pdl|"
    r"autotun|heuristic|scheduler|dispatch|selection|tile|tiled_copy|"
    r"blockscaled|block-scaled|blockwise|groupwise|vectori[sz]|coalesc|"
    r"shared memory|ldg|stg|copy_optimized|copy_shared|"
    r"fp8|fp4|nvfp4|mxfp4|int8|int4|marlin|machete|deepgemm|"
    r"flashmla|pack-gqa|r2p|paged|kv cache compression|blocktopk)",
    re.I,
)
CUDA_TARGET_EVIDENCE_RE = re.compile(
    r"(\.(cu|cuh|ptx|cubin)\b|cuda|nvidia|cutlass|cute|sm\d+|hopper|blackwell|wgmma|tma|tcgen)",
    re.I,
)
CUDA_SOURCE_RE = re.compile(r"(\.(cu|cuh|cubin|ptx)$|cuda|csrc|cutlass|cute|triton|tilelang|gpu|kernel|kernels)", re.I)


def run_json(cmd: list[str], timeout: int = 80) -> Any:
    try:
        raw = subprocess.check_output(cmd, text=True, stderr=subprocess.PIPE, timeout=timeout)
        return json.loads(raw)
    except subprocess.CalledProcessError as exc:
        print(f"WARN command failed: {' '.join(cmd)}\n{exc.stderr}", file=sys.stderr)
    except Exception as exc:  # noqa: BLE001
        print(f"WARN command failed: {' '.join(cmd)}: {exc}", file=sys.stderr)
    return []


def clean_text(value: str | None, max_len: int = 360) -> str:
    text = re.sub(r"<!--.*?-->", " ", value or "", flags=re.S)
    text = re.sub(r"```.*?```", " code block ", text, flags=re.S)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"#+\s*", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(
        r"Thank you for your contribution!.*?community at https://slack\.sglang\.ai\.",
        "",
        text,
    )
    text = re.sub(r"Purpose\s+", "", text)
    text = re.sub(r"Summary\s+", "", text)
    if len(text) > max_len:
        return text[:max_len].rstrip() + "..."
    return text


def normalize_files(pr: dict[str, Any]) -> list[str]:
    files = pr.get("files") or pr.get("key_paths") or []
    out: list[str] = []
    for item in files:
        if isinstance(item, str):
            path = item
        else:
            path = item.get("path", "")
        if path:
            out.append(path)
    return out


def full_text(pr: dict[str, Any]) -> str:
    return " ".join(
        [
            pr.get("title") or "",
            pr.get("body_excerpt") or "",
            pr.get("what_changed") or "",
            " ".join(normalize_files(pr)),
        ]
    )


def category_scores(pr: dict[str, Any]) -> dict[str, int]:
    title = (pr.get("title") or "").lower()
    body = ((pr.get("body_excerpt") or pr.get("what_changed") or "")).lower()
    files = " ".join(normalize_files(pr)).lower()
    scores: dict[str, int] = {}
    for cat, profile in CATEGORY_PROFILES.items():
        if cat == "kernel_other":
            continue
        score = 0
        for term in profile["terms"]:
            needle = term.lower()
            if needle in title:
                score += 5
            if needle in files:
                score += 4
            if needle in body:
                score += 1
        if score:
            scores[cat] = score
    return scores


def classify(pr: dict[str, Any]) -> tuple[str, list[str]]:
    scores = category_scores(pr)
    if not scores:
        return "kernel_other", ["kernel_other"]
    ranked = sorted(scores.items(), key=lambda item: (-item[1], CATEGORY_ORDER.index(item[0])))
    primary = ranked[0][0]
    cats = [cat for cat, score in ranked if score >= max(2, ranked[0][1] // 3)]
    if primary not in cats:
        cats.insert(0, primary)
    return primary, cats[:5]


def path_buckets(files: list[str]) -> dict[str, list[str]]:
    buckets = {"kernel": [], "test": [], "benchmark": [], "wrapper": [], "docs": [], "other": []}
    for path in files:
        low = path.lower()
        if "bench" in low or "benchmark" in low or "profile" in low or "ncu" in low:
            buckets["benchmark"].append(path)
        elif "/test" in low or low.startswith("test") or "tests/" in low or "/testing/" in low or "__pycache__" in low:
            buckets["test"].append(path)
        elif low.endswith((".cu", ".cuh", ".h", ".hpp", ".cc", ".cpp", ".py")) and re.search(
            r"(csrc|kernel|kernels|cutlass|cute|triton|tile|flashinfer|cub|thrust|moe|"
            r"attention|gemm|quant|norm|transpose|coalesc|gups|shared|rope|kv|tma|"
            r"wgmma|fmha|fa3|flash|kvcache|allreduce|cudax|cuda\.compute|copy|"
            r"segmented_reduce|scan|reduce|sort|topk|sampling|softmax|fusion|fused)",
            low,
        ):
            buckets["kernel"].append(path)
        elif "docs" in low or low.endswith((".md", ".mdx", ".rst")):
            buckets["docs"].append(path)
        elif low.endswith((".py", ".cc", ".cpp", ".h", ".hpp")):
            buckets["wrapper"].append(path)
        else:
            buckets["other"].append(path)
    return {key: value[:12] for key, value in buckets.items() if value}


def has_cuda_optimization_evidence(pr: dict[str, Any]) -> bool:
    files = normalize_files(pr)
    text = full_text(pr)
    title = pr.get("title") or ""
    title_body = " ".join([pr.get("title") or "", pr.get("body_excerpt") or "", pr.get("what_changed") or ""])

    has_cuda_target = CUDA_TARGET_EVIDENCE_RE.search(text) or any(CUDA_TARGET_EVIDENCE_RE.search(path) for path in files)
    if not has_cuda_target:
        return False

    code_files = [
        path
        for path in files
        if not re.search(
            r"(^|/)(tests?|testing|benchmarks?|docs?|examples?|tutorials?)/|"
            r"(^|/)test_|benchmark|bench_|notebook|tutorial|__pycache__",
            path,
            re.I,
        )
    ]
    source_buckets = path_buckets(code_files)
    has_kernel_source = bool(source_buckets.get("kernel")) or any(
        path.lower().endswith((".cu", ".cuh", ".ptx", ".cubin"))
        and (
            KERNEL_FAMILY_RE.search(" ".join([path, title_body]))
            or KERNEL_SPECIALIZATION_RE.search(" ".join([path, title_body]))
        )
        for path in code_files
    )
    if not has_kernel_source:
        return False

    has_perf_action = PERF_ACTION_RE.search(title) or STRONG_PERF_WORD_RE.search(title_body)
    has_optimization_mechanism = OPTIMIZATION_MECHANISM_RE.search(title_body)
    has_kernel_family = KERNEL_FAMILY_RE.search(text)
    has_specialization = KERNEL_SPECIALIZATION_RE.search(text)
    has_kernel_action = KERNEL_ACTION_RE.search(title)

    # Tutorials, examples, CI/build work, and test-only PRs are useful context,
    # but they are not optimization evidence unless the title/body explicitly
    # carries a performance/profiling claim.
    if NOISE_TITLE_RE.search(title) and not STRONG_PERF_WORD_RE.search(title):
        return False

    if has_perf_action and (has_kernel_family or has_specialization or has_kernel_source):
        return True
    if has_kernel_source and has_kernel_family and has_specialization and has_kernel_action and has_optimization_mechanism:
        return True
    return False


def keep_pr(pr: dict[str, Any], *, open_watch: bool = False) -> bool:
    if pr.get("repo_id") in PR_REFERENCE_ONLY_REPOS:
        return False
    title = pr.get("title") or ""
    files = normalize_files(pr)
    text = full_text(pr)
    if INFRA_NOISE_RE.search(title) and not STRONG_PERF_WORD_RE.search(text):
        return False
    if BACKEND_NOISE_RE.search(title) and not (
        CUDA_TARGET_EVIDENCE_RE.search(text)
        or any(CUDA_TARGET_EVIDENCE_RE.search(path) for path in files)
    ):
        return False
    if REJECT_TITLE_RE.search(title):
        return False
    if not (CUDA_SOURCE_RE.search(text) or any(CUDA_SOURCE_RE.search(path) for path in files)):
        return False
    if not KERNEL_SIGNAL_RE.search(text):
        return False
    if not has_cuda_optimization_evidence(pr):
        return False
    if not any(SOURCE_FILE_RE.search(path) for path in files) and not re.search(
        r"(kernel|gemm|attention|moe|TMA|WGMMA|SM90|SM100|SM120|fp8|fp4|cutlass|triton|tilelang|cub|scan|reduce)",
        title,
        re.I,
    ):
        return False
    if open_watch and "release" in title.lower():
        return False
    return True


def score_pr(pr: dict[str, Any]) -> int:
    files = normalize_files(pr)
    primary, cats = classify(pr)
    score = 8 * len(cats)
    score += min(18, sum(1 for path in files if SOURCE_FILE_RE.search(path)))
    score += min(10, sum(category_scores(pr).values()) // 4)
    if any("bench" in path.lower() or "benchmark" in path.lower() for path in files):
        score += 4
    if any("test" in path.lower() for path in files):
        score += 3
    if re.search(r"\b(perf|optimi|support|add|implement|feat|fix|refactor|speed|faster)\b", pr.get("title") or "", re.I):
        score += 4
    if primary in {"benchmark_test", "kernel_other"}:
        score -= 2
    return score


def fetch_prs(repo_id: str, cfg: RepoConfig, state: str, since: str, limit_per_query: int) -> list[dict[str, Any]]:
    collected: dict[int, dict[str, Any]] = {}
    for query in cfg.queries:
        if state == "merged":
            search = f"merged:>={since} {query}"
            limit = limit_per_query
        else:
            search = f"updated:>={since} {query}"
            limit = max(10, limit_per_query // 2)
        arr = run_json(
            [
                "gh",
                "pr",
                "list",
                "--repo",
                cfg.repo,
                "--state",
                state,
                "--search",
                search,
                "--limit",
                str(limit),
                "--json",
                "number,title,url,body,mergedAt,createdAt,updatedAt,files,additions,deletions,author",
            ]
        )
        for pr in arr:
            number = pr["number"]
            files = normalize_files(pr)[:32]
            if number not in collected:
                pr["repo_id"] = repo_id
                pr["repo"] = cfg.repo
                pr["files"] = files
                pr["body_excerpt"] = clean_text(pr.get("body"), 900)
                pr["matched_queries"] = [query]
                pr.pop("body", None)
                collected[number] = pr
            else:
                collected[number]["matched_queries"].append(query)
        time.sleep(0.04)

    recent_limit = 180 if state == "merged" else 80
    recent = run_json(
        [
            "gh",
            "pr",
            "list",
            "--repo",
            cfg.repo,
            "--state",
            state,
            "--limit",
            str(recent_limit),
            "--json",
            "number,title,url,body,mergedAt,createdAt,updatedAt,files,additions,deletions,author",
        ]
    )
    for pr in recent:
        files = normalize_files(pr)[:32]
        text = " ".join([pr.get("title") or "", clean_text(pr.get("body"), 900), " ".join(files)])
        if not KERNEL_SIGNAL_RE.search(text):
            continue
        number = pr["number"]
        if number not in collected:
            pr["repo_id"] = repo_id
            pr["repo"] = cfg.repo
            pr["files"] = files
            pr["body_excerpt"] = clean_text(pr.get("body"), 900)
            pr["matched_queries"] = ["recent-kernel-path"]
            pr.pop("body", None)
            collected[number] = pr

    out = []
    for pr in collected.values():
        if keep_pr(pr, open_watch=state == "open"):
            primary, cats = classify(pr)
            pr["primary_category"] = primary
            pr["categories"] = cats
            pr["path_buckets"] = path_buckets(normalize_files(pr))
            pr["_score"] = score_pr(pr)
            pr["source_key"] = f"{cfg.repo}#{pr['number']}"
            out.append(pr)
    out.sort(key=lambda item: (item["_score"], item.get("mergedAt") or item.get("updatedAt") or ""), reverse=True)
    return out


def merge_prior(prs_by_repo: dict[str, dict[int, dict[str, Any]]], root: Path) -> None:
    old_path = root / "knowledge/references/prs/pr-index.json"
    if not old_path.exists():
        return
    try:
        old = json.loads(old_path.read_text())
    except json.JSONDecodeError:
        return
    for repo_entry in old.get("repositories", []):
        repo_id = repo_entry.get("id")
        if repo_id not in REPOS:
            continue
        cfg = REPOS[repo_id]
        for pr in repo_entry.get("pull_requests", []):
            normalized = {
                "repo_id": repo_id,
                "repo": cfg.repo,
                "number": pr["number"],
                "title": pr.get("title") or "",
                "url": pr.get("url") or f"https://github.com/{cfg.repo}/pull/{pr['number']}",
                "mergedAt": pr.get("merged_at") or pr.get("mergedAt"),
                "files": pr.get("key_paths") or pr.get("files") or [],
                "body_excerpt": pr.get("what_changed") or "",
                "matched_queries": ["prior-index"],
                "source_key": f"{cfg.repo}#{pr['number']}",
            }
            if keep_pr(normalized):
                primary, cats = classify(normalized)
                normalized["primary_category"] = primary
                normalized["categories"] = cats
                normalized["path_buckets"] = path_buckets(normalize_files(normalized))
                normalized["_score"] = score_pr(normalized)
                prs_by_repo[repo_id][normalized["number"]] = normalized


def select_diverse(prs: list[dict[str, Any]], target: int) -> list[dict[str, Any]]:
    # KernelPilot keeps every filtered CUDA optimization PR in the knowledge base.
    # The target field remains for historical/audit context but does not cap
    # repository coverage.
    return sorted(
        prs,
        key=lambda item: (
            CATEGORY_ORDER.index(item["primary_category"])
            if item["primary_category"] in CATEGORY_ORDER
            else 99,
            -item["_score"],
            item["number"],
        ),
    )


def format_paths(paths: list[str]) -> str:
    if not paths:
        return "See PR diff"
    return "<br>".join(f"`{path}`" for path in paths[:6])


def summarize_buckets(buckets: dict[str, list[str]]) -> str:
    if not buckets:
        return "Open PR diff and inspect changed kernel/test/benchmark paths."
    parts = []
    for key in ("kernel", "benchmark", "test", "wrapper", "docs", "other"):
        if key in buckets:
            parts.append(f"{key}: " + ", ".join(f"`{p}`" for p in buckets[key][:4]))
    return "<br>".join(parts)


def pr_record(pr: dict[str, Any], cfg: RepoConfig) -> dict[str, Any]:
    profile = CATEGORY_PROFILES[pr["primary_category"]]
    return {
        "number": pr["number"],
        "url": pr.get("url") or f"https://github.com/{cfg.repo}/pull/{pr['number']}",
        "title": pr.get("title"),
        "merged_at": pr.get("mergedAt"),
        "updated_at": pr.get("updatedAt"),
        "primary_category": pr["primary_category"],
        "categories": pr["categories"],
        "matched_queries": sorted(set(pr.get("matched_queries", []))),
        "score": pr.get("_score"),
        "what_changed": clean_text(pr.get("body_excerpt") or pr.get("title"), 320),
        "key_paths": normalize_files(pr)[:16],
        "path_buckets": pr.get("path_buckets") or path_buckets(normalize_files(pr)),
        "optimization_recipe": profile["recipe"],
        "ncu_hint": profile["ncu"],
        "source_key": pr["source_key"],
    }


def render_repo_page(root: Path, repo_id: str, cfg: RepoConfig, selected: list[dict[str, Any]], pool_count: int, framework_paths: list[str]) -> None:
    pr_dir = root / "knowledge/references/prs"
    lines: list[str] = []
    lines.append(f"# {cfg.display} PR Knowledge Notes\n")
    lines.append(f"Repository: <https://github.com/{cfg.repo}>\n")
    lines.append(
        "This page is the production-PR layer for kernel-knowledge. It keeps merged PRs with CUDA/NVIDIA target evidence, real kernel/source changes, and an optimization/performance mechanism such as tuning, fusion, tensor-core paths, memory movement, scheduling, profiling, or benchmark-backed speed work. Release, CI-only, formatting, dependency-only, correctness-only, and non-target-backend PRs are filtered out.\n"
    )
    if repo_id == "tilekernels" and len(selected) < 3:
        lines.append(
            "Note: this repository has little public PR history. Use the source guide and direct code scan as mandatory paired evidence, and treat this page as provenance when PRs exist.\n"
        )
    lines.append("## Repository Source Scan\n")
    if framework_paths:
        lines.append("Read these source regions before opening individual PR diffs:\n")
        lines.extend([f"- `{path}`" for path in framework_paths])
        lines.append("")
    lines.append("## Coverage Summary\n")
    counts = Counter(pr["primary_category"] for pr in selected)
    lines.append("| Category | CUDA optimization PRs |")
    lines.append("| --- | ---: |")
    for cat in CATEGORY_ORDER:
        if counts[cat]:
            lines.append(f"| {CATEGORY_PROFILES[cat]['title']} | {counts[cat]} |")
    lines.append("")
    lines.append("## Pull Request Case Notes\n")
    for cat in CATEGORY_ORDER:
        prs = [pr for pr in selected if pr["primary_category"] == cat]
        if not prs:
            continue
        profile = CATEGORY_PROFILES[cat]
        lines.append(f"### {profile['title']}\n")
        lines.append(f"Use this section for: {profile['recipe']}")
        lines.append(f"NCU first look: {profile['ncu']}\n")
        lines.append("| PR | Merged | Signals | What changed | Evidence paths | Transfer note |")
        lines.append("| --- | --- | --- | --- | --- | --- |")
        for pr in prs:
            title = (pr.get("title") or "").replace("|", "\\|")
            body = clean_text(pr.get("body_excerpt") or title, 300).replace("|", "\\|")
            merged = (pr.get("mergedAt") or "")[:10]
            signals = ", ".join(pr["categories"])
            evidence = summarize_buckets(pr.get("path_buckets") or {}).replace("|", "\\|")
            note = profile["recipe"].replace("|", "\\|")
            lines.append(
                f"| [#{pr['number']}](https://github.com/{cfg.repo}/pull/{pr['number']}) {title} | {merged} | {signals} | {body} | {evidence} | {note} |"
            )
        lines.append("")
    lines.append("## Per-PR Ledger Fields\n")
    lines.append("When using an idea from this page, add one row to `artifacts/source-idea-ledger.md` with:\n")
    lines.append("| Field | Value to record |")
    lines.append("| --- | --- |")
    lines.append("| Source key | `<repo>#<pr-number>` |")
    lines.append("| Code evidence | Kernel, wrapper, benchmark, and test paths opened from the PR diff |")
    lines.append("| Hypothesis | The concrete optimization idea derived from the PR |")
    lines.append("| First experiment | Candidate version and benchmark shape set |")
    lines.append("| Result | Correctness, geomean, best/worst cases, and NCU digest path |")
    lines.append("| Do-not-reread key | Same as source key unless a single PR yields multiple independent ideas |\n")
    lines.append("## How To Use This Page\n")
    lines.append("- During the initial knowledge pass, read the category matching the target kernel and copy PR URL, changed paths, and hypothesis into the source idea ledger.")
    lines.append("- During plateau expansion, choose PRs not already present in ledger do-not-reread keys; inspect the diff, linked issue, changed tests, and benchmark files before using the idea.")
    lines.append("- Treat PR code as baseline/prior art unless the task and license allow copying or adapting it. When copied, record exact PR, commit, files, notice, and first delta.\n")
    (pr_dir / f"{repo_id}.md").write_text("\n".join(lines), encoding="utf-8")


def render_by_topic_pages(root: Path, repo_records: list[dict[str, Any]]) -> None:
    topic_dir = root / "knowledge/references/prs/by-topic"
    topic_dir.mkdir(parents=True, exist_ok=True)
    by_cat: dict[str, list[tuple[dict[str, Any], dict[str, Any]]]] = defaultdict(list)
    for repo_entry in repo_records:
        for pr in repo_entry["pull_requests"]:
            by_cat[pr["primary_category"]].append((repo_entry, pr))
    index_lines = ["# Cross-Repository PR Topic Index\n"]
    index_lines.append("Use these pages when the bottleneck is known but the best source repository is not.\n")
    index_lines.append("| Topic | Page | PRs |")
    index_lines.append("| --- | --- | ---: |")
    for cat in CATEGORY_ORDER:
        items = by_cat.get(cat, [])
        if not items:
            continue
        page = f"{cat}.md"
        profile = CATEGORY_PROFILES[cat]
        index_lines.append(f"| {profile['title']} | [`{page}`]({page}) | {len(items)} |")
        lines = [f"# {profile['title']} PRs\n"]
        lines.append(f"Optimization recipe: {profile['recipe']}\n")
        lines.append(f"NCU first look: {profile['ncu']}\n")
        lines.append("## Inspection Questions\n")
        lines.extend(f"- {q}" for q in profile["questions"])
        lines.append("\n## PRs\n")
        lines.append("| Repo | PR | Merged | What to inspect | Ledger key |")
        lines.append("| --- | --- | --- | --- | --- |")
        for repo_entry, pr in sorted(items, key=lambda item: (item[0]["id"], item[1].get("merged_at") or ""), reverse=False):
            inspect = summarize_buckets(pr.get("path_buckets") or {}).replace("|", "\\|")
            merged = (pr.get("merged_at") or "")[:10]
            title = (pr.get("title") or "").replace("|", "\\|")
            lines.append(
                f"| `{repo_entry['repo']}` | [#{pr['number']}]({pr['url']}) {title} | {merged} | {inspect} | `{pr['source_key']}` |"
            )
        lines.append("")
        (topic_dir / page).write_text("\n".join(lines), encoding="utf-8")
    (topic_dir / "index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")


def render_index(root: Path, repo_records: list[dict[str, Any]], open_watch: list[dict[str, Any]], since: str) -> None:
    pr_dir = root / "knowledge/references/prs"
    idx: list[str] = []
    idx.append("# PR-Driven Kernel Knowledge\n")
    idx.append(
        "This layer follows the kernel-knowledge design implied by MIT Kernel Mafia: production pull requests are treated as first-class evidence because many real optimization recipes live in PR diffs, review threads, tests, benchmarks, and follow-up fixes rather than in official documentation.\n"
    )
    idx.append("## Paired PR + Source Read Order\n")
    idx.append("1. Start with the target topic and framework routing pages.")
    idx.append("2. Read the matching source guide under `knowledge/references/source-guides/` and the matching PR page below in the same knowledge pass.")
    idx.append("3. Use PRs for optimization history, review context, tests, and benchmark evidence; use source guides and direct source scans for the current implementation, wrappers, tests, benchmark entry points, and candidate code locations.")
    idx.append("4. If the bottleneck is known but the source repository is unclear, use `by-topic/index.md`, then open the matching source guide for each promising repository.")
    idx.append("5. Record each source-derived idea in the source idea ledger with repo, PR number when available, source path or symbol, hypothesis, measured result, and do-not-reread key.\n")
    idx.append("## Repository PR Pages\n")
    idx.append("| Repository | PR guide | CUDA optimization PRs | Filtered pool |")
    idx.append("| --- | --- | ---: | ---: |")
    for repo_entry in repo_records:
        idx.append(
            f"| `{repo_entry['repo']}` | [`{repo_entry['id']}.md`]({repo_entry['id']}.md) | {repo_entry['selected_count']} | {repo_entry['candidate_pool_after_filter']} |"
        )
    idx.append("\n## Cross-Repository Topic Pages\n")
    idx.append("Use [`by-topic/index.md`](by-topic/index.md) to inspect PRs by kernel family across all repositories.\n")
    idx.append("## Coverage Audit\n")
    idx.append("Use [`audit.md`](audit.md) to inspect scan methodology, filtering rules, repository coverage, and known gaps.\n")
    idx.append("## Open PR Watchlist\n")
    idx.append(
        "Use [`open-watchlist.md`](open-watchlist.md) for current open PRs. Re-run the refresh script before relying on these entries because open PRs move quickly.\n"
    )
    idx.append("## Categories\n")
    idx.append("| Category | Meaning |")
    idx.append("| --- | --- |")
    for cat, profile in CATEGORY_PROFILES.items():
        idx.append(f"| `{cat}` | {profile['title']} |")
    idx.append("\n## Expansion Rule\n")
    idx.append(
        "When two consecutive optimization rounds improve the best geomean by less than 1%, read paired PR/source evidence first. Read at least 50 new code-first sources before prose sources; a PR diff, source file, symbol, linked test, benchmark, or changed kernel file counts as a code-first source when it is recorded with a do-not-reread key.\n"
    )
    idx.append("## Refresh Command\n")
    idx.append("```bash")
    idx.append(f"python3 scripts/refresh_pr_knowledge.py --since {since}")
    idx.append("```\n")
    (pr_dir / "index.md").write_text("\n".join(idx), encoding="utf-8")

    lines = ["# Open Kernel PR Watchlist\n"]
    lines.append(
        "These PRs were open when the knowledge base was refreshed. Treat them as volatile idea sources and re-check GitHub before using code or benchmark claims.\n"
    )
    lines.append("| Repo | PR | Updated | Category | Evidence paths | Ledger key |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for pr in open_watch:
        evidence = summarize_buckets(pr.get("path_buckets") or {}).replace("|", "\\|")
        updated = (pr.get("updatedAt") or "")[:10]
        title = (pr.get("title") or "").replace("|", "\\|")
        lines.append(
            f"| `{pr['repo']}` | [#{pr['number']}]({pr['url']}) {title} | {updated} | {pr['primary_category']} | {evidence} | `{pr['source_key']}` |"
        )
    (pr_dir / "open-watchlist.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def render_audit(root: Path, repo_records: list[dict[str, Any]], open_watch: list[dict[str, Any]], since: str) -> None:
    pr_dir = root / "knowledge/references/prs"
    lines: list[str] = []
    lines.append("# PR Knowledge Coverage Audit\n")
    lines.append(f"Scan window: merged or updated since `{since}`.\n")
    lines.append("## What Was Scanned\n")
    lines.append("| Repository | Filtered merged pool | Knowledge merged PRs | Open watchlist entries |")
    lines.append("| --- | ---: | ---: | ---: |")
    open_counts = Counter(pr["repo"] for pr in open_watch)
    for entry in repo_records:
        lines.append(
            f"| `{entry['repo']}` | {entry['candidate_pool_after_filter']} | {entry['selected_count']} | {open_counts.get(entry['repo'], 0)} |"
        )
    lines.append("\n## Filter Policy\n")
    lines.append("- Keep PRs only when they have CUDA/NVIDIA target evidence, a real kernel/source change, and an optimization/performance mechanism.")
    lines.append("- Keep CUDA optimization PRs across the registered knowledge repositories, including implementation, runtime dispatch, tuning, benchmark-backed speed work, profiler evidence, and kernel-family feature additions.")
    lines.append("- Filter obvious non-CUDA backend work such as MPS, ROCm, AMD-only, MUSA, Ascend, Intel, CPU-only, Metal, RVV, and RISC-V PRs unless the same PR also carries CUDA/NVIDIA kernel evidence.")
    lines.append("- Filter release-only, CI-only, dependency-bump, formatting, copyright-header, MyPy, doc-only, cookbook-only, example-path-only, and correctness-only PRs.")
    lines.append("- Keep major release PRs only when their changed paths expose real kernel/API source files and the title/body points to kernel features.\n")
    lines.append("## Evidence Captured Per PR\n")
    lines.append("- PR URL and stable source key, for example `vllm-project/vllm#42236`.")
    lines.append("- Primary and secondary kernel categories.")
    lines.append("- Changed-path buckets: kernel, benchmark, test, wrapper, docs, other.")
    lines.append("- Short human-readable summary.")
    lines.append("- Transfer recipe and first NCU metrics to inspect.")
    lines.append("- Matched search queries in `pr-index.json` for traceability.\n")
    lines.append("## Retrieval Strategy\n")
    lines.append("1. Use the repository PR page and the matching source guide together when the baseline framework is known.")
    lines.append("2. Use `by-topic/index.md` when the bottleneck category is known but the best source repository is not, then open source guides for every promising repository.")
    lines.append("3. Use `open-watchlist.md` only for fresh ideas, and re-check GitHub plus the current source tree before trusting the code or benchmark claim.")
    lines.append("4. Log every source-derived idea in `artifacts/source-idea-ledger.md` with PR key when available, source path or symbol, opened tests/benchmarks, hypothesis, result, and do-not-reread key.\n")
    lines.append("## Known Gaps\n")
    lines.append("- DeepSeek TileKernels has little public PR history, so source-guide and direct code scan are mandatory paired evidence for that repo.")
    lines.append("- GitHub search can miss PRs whose titles and bodies use generic wording. When optimizing a specific kernel, still run path-based `gh pr list` or `gh search prs` for that exact file/function name and inspect current source paths.")
    lines.append("- Open PR entries are intentionally volatile and should not be treated as merged production evidence.")
    lines.append("- The corpus is intentionally CUDA-first. Non-CUDA backend PRs are filtered out unless they also contain CUDA/NVIDIA kernel evidence.\n")
    lines.append("## Refresh Command\n")
    lines.append("```bash")
    lines.append(f"python3 scripts/refresh_pr_knowledge.py --since {since}")
    lines.append("```")
    (pr_dir / "audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=Path(__file__).resolve().parents[1], type=Path)
    parser.add_argument("--since", default=DEFAULT_SINCE)
    parser.add_argument("--cache", default=None, type=Path)
    parser.add_argument("--use-cache", action="store_true")
    parser.add_argument("--limit-per-query", default=35, type=int)
    parser.add_argument("--skip-open", action="store_true")
    args = parser.parse_args()

    root = args.repo_root
    pr_dir = root / "knowledge/references/prs"
    pr_dir.mkdir(parents=True, exist_ok=True)
    index = json.loads((root / "knowledge/index.json").read_text())
    framework_paths = {fw["id"]: fw.get("kernel_paths", []) for fw in index.get("frameworks", [])}
    cache_path = args.cache or (pr_dir / "pr-scan-cache.json")

    if args.use_cache and cache_path.exists():
        cache = json.loads(cache_path.read_text())
        merged_by_repo = {
            repo_id: {int(pr["number"]): pr for pr in payload.get("merged", [])}
            for repo_id, payload in cache.get("repositories", {}).items()
        }
        open_by_repo = {
            repo_id: {int(pr["number"]): pr for pr in payload.get("open", [])}
            for repo_id, payload in cache.get("repositories", {}).items()
        }
    else:
        merged_by_repo: dict[str, dict[int, dict[str, Any]]] = defaultdict(dict)
        open_by_repo: dict[str, dict[int, dict[str, Any]]] = defaultdict(dict)
        merge_prior(merged_by_repo, root)
        for repo_id, cfg in REPOS.items():
            print(f"== scanning merged {cfg.repo}", file=sys.stderr)
            for pr in fetch_prs(repo_id, cfg, "merged", args.since, args.limit_per_query):
                merged_by_repo[repo_id][pr["number"]] = pr
            if not args.skip_open:
                print(f"== scanning open {cfg.repo}", file=sys.stderr)
                for pr in fetch_prs(repo_id, cfg, "open", args.since, max(12, args.limit_per_query // 2)):
                    open_by_repo[repo_id][pr["number"]] = pr
        cache = {
            "schema_version": 1,
            "scan_since": args.since,
            "repositories": {
                repo_id: {
                    "repo": REPOS[repo_id].repo,
                    "merged": list(merged_by_repo.get(repo_id, {}).values()),
                    "open": list(open_by_repo.get(repo_id, {}).values()),
                }
                for repo_id in REPOS
            },
        }
        cache_path.write_text(json.dumps(cache, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    repo_records: list[dict[str, Any]] = []
    open_watch: list[dict[str, Any]] = []
    for repo_id, cfg in REPOS.items():
        pool = list(merged_by_repo.get(repo_id, {}).values())
        pool = [pr for pr in pool if keep_pr(pr)]
        for pr in pool:
            primary, cats = classify(pr)
            pr["primary_category"] = primary
            pr["categories"] = cats
            pr["path_buckets"] = path_buckets(normalize_files(pr))
            pr["_score"] = score_pr(pr)
            pr["source_key"] = f"{cfg.repo}#{pr['number']}"
        pool.sort(key=lambda item: (item["_score"], item.get("mergedAt") or ""), reverse=True)
        selected = select_diverse(pool, cfg.target)
        render_repo_page(root, repo_id, cfg, selected, len(pool), framework_paths.get(repo_id, []))
        repo_records.append(
            {
                "id": repo_id,
                "name": cfg.display,
                "repo": cfg.repo,
                "pr_reference": f"knowledge/references/prs/{repo_id}.md",
                "scan_since": args.since,
                "selected_count": len(selected),
                "candidate_pool_after_filter": len(pool),
                "pull_requests": [pr_record(pr, cfg) for pr in selected],
            }
        )
        open_pool = list(open_by_repo.get(repo_id, {}).values())
        open_pool = [pr for pr in open_pool if keep_pr(pr, open_watch=True)]
        for pr in open_pool:
            primary, cats = classify(pr)
            pr["primary_category"] = primary
            pr["categories"] = cats
            pr["path_buckets"] = path_buckets(normalize_files(pr))
            pr["_score"] = score_pr(pr)
            pr["source_key"] = f"{cfg.repo}#{pr['number']}"
            pr["repo"] = cfg.repo
        open_pool.sort(key=lambda item: (item["_score"], item.get("updatedAt") or ""), reverse=True)
        open_watch.extend(open_pool)

    out_json = {
        "schema_version": 3,
        "generated_from": "GitHub PR scan by kernel family plus prior PR notes; all filtered CUDA optimization PRs are kept for source/runtime/tuning relevance.",
        "scan_since": args.since,
        "paper_alignment": "Production PRs are first-class evidence, with human summaries and machine metadata preserving traceability to PRs, changed code paths, tests, benchmarks, docs, and contest artifacts.",
        "categories": {key: {"title": value["title"], "recipe": value["recipe"], "ncu_hint": value["ncu"]} for key, value in CATEGORY_PROFILES.items()},
        "repositories": repo_records,
        "open_watchlist": [
            {
                "repo": pr["repo"],
                "number": pr["number"],
                "url": pr["url"],
                "title": pr.get("title"),
                "updated_at": pr.get("updatedAt"),
                "primary_category": pr["primary_category"],
                "categories": pr["categories"],
                "path_buckets": pr["path_buckets"],
                "source_key": pr["source_key"],
            }
            for pr in open_watch
        ],
    }
    (pr_dir / "pr-index.json").write_text(json.dumps(out_json, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    render_by_topic_pages(root, repo_records)
    render_index(root, repo_records, open_watch, args.since)
    render_audit(root, repo_records, open_watch, args.since)

    for repo in repo_records:
        print(f"{repo['id']}: selected={repo['selected_count']} pool={repo['candidate_pool_after_filter']}")
    print(f"open-watchlist: {len(open_watch)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
