# Triton PR Knowledge Notes

Repository: <https://github.com/triton-lang/triton>

This page is the production-PR layer for kernel-knowledge. It keeps merged PRs with CUDA/NVIDIA target evidence, real kernel/source changes, and an optimization/performance mechanism such as tuning, fusion, tensor-core paths, memory movement, scheduling, profiling, or benchmark-backed speed work. Release, CI-only, formatting, dependency-only, correctness-only, and non-target-backend PRs are filtered out.

## Repository Source Scan

Read these source regions before opening individual PR diffs:

- `python/tutorials`
- `python/triton/language`
- `python/triton/runtime`
- `lib/Conversion`
- `test/TritonGPU`

## Coverage Summary

| Category | CUDA optimization PRs |
| --- | ---: |
| GEMM / Quantization | 1 |
| Norm / Elementwise / Epilogue | 1 |
| Architecture / Pipeline | 3 |
| Compiler / Runtime | 1 |
| Benchmark / Test Evidence | 1 |

## Pull Request Case Notes

### GEMM / Quantization

Use this section for: Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate.
NCU first look: Tensor pipe %, DRAM/L2 bytes, active cycles, register pressure, and scale-load traffic.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#10190](https://github.com/triton-lang/triton/pull/10190) [mxfp4] Fix Hopper scale padding mask | 2026-05-04 | gemm_quant, arch_pipeline | Why Hopper MXFP4 weight-scale swizzling can introduce padded scale bytes when the RHS K dimension does not fill the final scale tile. The regular RHS value load already masks invalid K-tail values, but the Hopper scale path was loading and unswizzling the full scale tile without clearing invalid K-s... | kernel: `python/triton_kernels/triton_kernels/matmul_details/_matmul.py`, `python/triton_kernels/triton_kernels/matmul_details/_p_matmul.py`<br>test: `python/triton_kernels/tests/test_matmul_details/test_opt_flags_nvidia.py` | Inspect scale layout, accumulator type, tile/schedule choice, epilogue fusion, and partial-tile guards before deriving a candidate. |

### Norm / Elementwise / Epilogue

Use this section for: Look for fusion, vectorization, dtype conversion, and store-traffic reductions before changing math.
NCU first look: DRAM %, L2 bytes, global load/store sectors, eligible warps, and long scoreboard.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#10060](https://github.com/triton-lang/triton/pull/10060) [BACKEND] Extend support for small MMAv2 FP64: single 8x8x4 instructions. | 2026-04-20 | norm_elementwise, compiler_runtime, benchmark_test, gemm_quant | The fp64 MMA path now operates at native `m8n8k4` granularity, supporting any shape that is a multiple of 8×8×4, including the minimal 8×8×4 case. This is an extension of https://github.com/triton-lang/triton/pull/7310 (The implementation was based on that PR) Tests passed on A100. Files Changed `li... | kernel: `lib/Dialect/TritonGPU/IR/Dialect.cpp`, `lib/Dialect/TritonGPU/IR/LinearLayoutConversions.cpp`, `lib/Dialect/TritonGPU/Transforms/Utility.cpp`, `third_party/nvidia/lib/TritonNVIDIAGPUToLLVM/DotOpToLLVM/MMAv2.cpp`<br>test: `python/test/unit/language/test_core.py`, `test/Conversion/tritongpu_to_llvm.mlir`, `test/TritonGPU/accelerate-matmul.mlir`<br>wrapper: `third_party/nvidia/backend/compiler.py` | Look for fusion, vectorization, dtype conversion, and store-traffic reductions before changing math. |

### Architecture / Pipeline

Use this section for: Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages.
NCU first look: Tensor pipe %, memory pipe utilization, barrier stalls, wait groups, and occupancy.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#10148](https://github.com/triton-lang/triton/pull/10148) [Reland][NVIDIA] Support swizzle 0 TMA + MMA for Hopper and Blackwell | 2026-04-30 | arch_pipeline, norm_elementwise, compiler_runtime, benchmark_test | Compared to https://github.com/triton-lang/triton/pull/9931: * When looking for an equivalent LL in the loop https://github.com/masahi/triton/blob/62b3a08c1b205522991148b4d0b6d761e0ecb369/lib/Dialect/TritonNvidiaGPU/Transforms/OptimizeDescriptorEncoding.cppL69-L79, we are now guarding against an LL... | kernel: `include/triton/Dialect/TritonGPU/IR/LinearLayoutConversions.h`, `include/triton/Dialect/TritonGPU/Transforms/DescriptorMemoryLayouts.h`, `lib/Dialect/TritonGPU/IR/Dialect.cpp`, `lib/Dialect/TritonGPU/IR/LinearLayoutConversions.cpp`<br>test: `test/TritonGPU/dot-operands.mlir`, `test/TritonNvidiaGPU/optimize_descriptor_encoding.mlir` | Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages. |
| [#10275](https://github.com/triton-lang/triton/pull/10275) Support zero-sized Hopper MX scale layouts | 2026-05-11 | arch_pipeline, gemm_quant, compiler_runtime, benchmark_test | Fix Hopper MX scale layout conversion for zero-sized scale tensors. `torch.nn.functional.pad` rejects some valid zero-numel outputs. This shows up in Hopper scale swizzle after RHS transpose: for example, `(0, 64)` becomes `(64, 0)`, and row padding still leaves a zero-width output. The fix mirrors... | kernel: `python/triton_kernels/triton_kernels/tensor_details/layout_details/hopper_scale.py`, `python/triton_kernels/triton_kernels/tensor_details/layout_details/strided.py`<br>test: `python/triton_kernels/tests/test_tensor_details/test_layout_hopper.py` | Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages. |
| [#10196](https://github.com/triton-lang/triton/pull/10196) [MULTICTA] Fix multicast pattern for tcgen05_mma_scaled | 2026-05-04 | arch_pipeline, compiler_runtime, benchmark_test | The helper we had was missing the necessary `two_ctas` flag to compute the number of arrivals correctly for an mma that goes into a multicast TMA. I changed the API all across I think it would be much better if we just had a TTNG_InitMmaBarrierOp as proposed in https://github.com/triton-lang/triton/... | kernel: `lib/Dialect/TritonNvidiaGPU/IR/Ops.cpp`, `python/triton/experimental/gluon/language/nvidia/blackwell/__init__.py`<br>test: `python/test/gluon/test_consan.py`, `python/test/gluon/test_core.py`<br>wrapper: `python/examples/gluon/03-matmul-multicta.py`, `python/examples/gluon/04-2cta-block-scale-matmul.py`, `python/tutorials/gluon/14-multicta.py` | Extract the architecture assumption first: SM target, TMA/WGMMA/tcgen path, cluster use, and pipeline stages. |

### Compiler / Runtime

Use this section for: Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests.
NCU first look: Generated kernel shape, launch overhead, occupancy, register pressure, and compile-time-selected schedule.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#10059](https://github.com/triton-lang/triton/pull/10059) [TritonGPU] Coalesce integer atomics | 2026-04-19 | compiler_runtime, benchmark_test, norm_elementwise | Hello! The coalescing pass currently chooses `sizePerThread` for atomics using the same pointer alignment / contiguity heuristic as regular stores. For some atomic lowerings this is too optimistic: the pass will select a 128-bit per-thread layout even when the backend lowers the atomic as a narrower... | kernel: `lib/Dialect/TritonGPU/Transforms/Utility.cpp`<br>test: `test/TritonGPU/coalesce.mlir` | Treat compiler/runtime integration as part of the kernel: launch wrapper, cache/JIT behavior, generated code, and build flags need tests. |

### Benchmark / Test Evidence

Use this section for: Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code.
NCU first look: Use the PR's benchmark/profile command as the first replay target.

| PR | Merged | Signals | What changed | Evidence paths | Transfer note |
| --- | --- | --- | --- | --- | --- |
| [#10186](https://github.com/triton-lang/triton/pull/10186) [RUNTIME] Initialize profile scratch on stream 0 | 2026-05-01 | benchmark_test, compiler_runtime | Codex found an intersting one that was causing some consan failures (i.e., kernels that need an HBM scratch) to fail. This empirically fixes a race that was consistently reproduced in my multicta consan branch. Here's the post mortem Root cause: - Triton launches kernels on the current raw CUDA stre... | kernel: `python/triton/backends/driver.py`<br>test: `python/test/unit/runtime/test_driver.py` | Mine shape sets, tolerance rules, warmup logic, and profile commands before mutating code. |

## Per-PR Ledger Fields

When using an idea from this page, add one row to `artifacts/source-idea-ledger.md` with:

| Field | Value to record |
| --- | --- |
| Source key | `<repo>#<pr-number>` |
| Code evidence | Kernel, wrapper, benchmark, and test paths opened from the PR diff |
| Hypothesis | The concrete optimization idea derived from the PR |
| First experiment | Candidate version and benchmark shape set |
| Result | Correctness, geomean, best/worst cases, and NCU digest path |
| Do-not-reread key | Same as source key unless a single PR yields multiple independent ideas |

## How To Use This Page

- During the initial knowledge pass, read the category matching the target kernel and copy PR URL, changed paths, and hypothesis into the source idea ledger.
- During plateau expansion, choose PRs not already present in ledger do-not-reread keys; inspect the diff, linked issue, changed tests, and benchmark files before using the idea.
- Treat PR code as baseline/prior art unless the task and license allow copying or adapting it. When copied, record exact PR, commit, files, notice, and first delta.
