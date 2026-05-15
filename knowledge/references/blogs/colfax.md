# Colfax Research Blog

Index: <https://research.colfax-intl.com/blog/>

Companion code:

- <https://github.com/ColfaxResearch/cfx-article-src>
- <https://github.com/ColfaxResearch/cutlass-kernels>

Use this source for CUTLASS/CuTe tutorial kernels with article-backed
implementation detail.

## Article Map

| Kernel family | Articles to read |
| --- | --- |
| Hopper TMA/WGMMA | `CUTLASS Tutorial: Mastering the NVIDIA Tensor Memory Accelerator`, `CUTLASS Tutorial: Fast Matrix-Multiplication with WGMMA on NVIDIA Hopper GPUs` |
| Hopper GEMM pipeline | `CUTLASS Tutorial: Efficient GEMM kernel designs with Pipelining`, `CUTLASS Tutorial: Persistent Kernels and Stream-K` |
| Hopper transpose | `CUTLASS Tutorial: Matrix Transpose in CuTe/CUTLASS` |
| Blackwell GEMM | `Writing GEMM Kernels Using Tensor Memory for NVIDIA Blackwell GPUs`, `GEMM with Thread Block Clusters on NVIDIA Blackwell GPUs`, `Sub-byte GEMM on NVIDIA Blackwell GPUs`, `Hardware-supported Block-scaling with NVIDIA Blackwell GPUs` |
| Blackwell scheduling | `Dynamic persistent tile scheduling with Cluster Launch Control (CLC) on NVIDIA Blackwell GPUs` |
| Attention | `FlashAttention-4: Algorithm and Kernel Pipelining Co-Design`, `A User's Guide to FlexAttention in FlashAttention CuTe DSL`, `FlexAttention + FlashAttention-4` |
| CuTe layouts / APIs | `Categorical Foundations for CuTe Layouts`, `CUTLASS 3.x APIs: Orthogonal, Reusable, and Composable Abstractions for GEMM Kernel Design` |

## Companion Code Map

| Repo/path | Kernel type | What to extract |
| --- | --- | --- |
| `cfx-article-src/tma/main.cu` | Hopper TMA copy | load/store/multicast setup, tensor maps, barriers |
| `cfx-article-src/tma/tma_copy*.h` | TMA helper | copy atom setup and multicast variants |
| `cfx-article-src/pipeline-gemm/sm90_gemm_multistage.cu` | Hopper GEMM | multistage non-warp-specialized baseline |
| `cfx-article-src/pipeline-gemm/sm90_gemm_ws.cu` | warp-specialized GEMM | producer/consumer split and pipeline shape |
| `cfx-article-src/pipeline-gemm/hopper-gemm-ws/*` | custom GEMM kernel | mainloop, epilogue, tile scheduler, kernel traits |
| `cfx-article-src/streamk/streamk.cu` | Stream-K GEMM | persistent tile scheduling and split-K comparison |
| `cfx-article-src/streamk/tile_scheduler.hpp` | scheduling | Stream-K scheduler details and wave quantization handling |
| `cfx-article-src/transpose-cute/include/*` | transpose/copy | naive, shared-memory, direct copy, TMA-store vectorized variants |
| `cfx-article-src/evt/evt_gemm_cute.cu` | epilogue visitor tree | composable epilogue and reference checks |
| `cfx-article-src/cutlass_gemm/cutlass_gemm/*` | Python extension | minimal CUTLASS GEMM binding structure |
| `cutlass-kernels/src/cutlass-gemm/gemm.cu` | CUTLASS 3 GEMM | CollectiveBuilder, TMA, warp-specialized GEMM |
| `cutlass-kernels/src/cute-gemm-tma-gma/gemm.cu` | CuTe GEMM | lower-level CuTe TMA/GMA example |
| `cutlass-kernels/src/fmha/fmha_forward.cu` | FMHA | online softmax, two GEMMs, TMA load/store |
| `cutlass-kernels/src/fmha-pipeline/*` | pipelined FMHA | producer/consumer split, pipelined softmax path |

## Search Patterns

```bash
rg -n "TMA|WGMMA|StreamK|persistent|Cluster|CLC|mbarrier|CollectiveBuilder|Tensor Memory|block scaling|FlashAttention|FlexAttention|transpose" .
```

## Optimization Signals

- GEMM: tensor pipe %, TMA bytes/stalls, active cycles, register pressure,
  waves-per-SM, and Stream-K tail utilization.
- Attention: tensor pipe %, SFU pressure, softmax dependencies, TMA waits, and
  shared-memory pressure.
- Transpose/TMA: DRAM bandwidth, shared-memory bank conflicts, L2 bytes, and
  async barrier stalls.
