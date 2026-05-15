# Colfax Research Blog And Code Deep Reference

Article index: <https://research.colfax-intl.com/blog/>

Primary code:

- <https://github.com/ColfaxResearch/cfx-article-src>
- <https://github.com/ColfaxResearch/cutlass-kernels>

Use this reference when the loop needs CUTLASS / CuTe implementation detail
from articles with companion code.

Article-level map: `../blogs/colfax.md`

## Read Order By Topic

### Hopper CUTLASS / CuTe

1. `tutorial-hopper-tma`
2. `cutlass-tutorial-wgmma-hopper`
3. `cutlass-tutorial-design-of-a-gemm-kernel`
4. `cutlass-tutorial-persistent-kernels-and-stream-k`
5. `tutorial-matrix-transpose-in-cutlass`

### Blackwell CUTLASS

1. `cutlass-tutorial-writing-gemm-kernels-using-tensor-memory-for-nvidia-blackwell-gpus`
2. `cutlass-tutorial-gemm-with-thread-block-clusters-on-nvidia-blackwell-gpus`
3. `cutlass-tutorial-sub-byte-gemm-on-nvidia-blackwell-gpus`
4. `cutlass-tutorial-hardware-supported-block-scaling-with-nvidia-blackwell-gpus`

### Attention And Layouts

1. `flashattention-4-algorithm-and-kernel-pipelining-co-design-for-asymmetric-hardware-scaling`
2. `a-users-guide-to-flexattention-in-flashattention-cute-dsl`
3. `categorical-foundations-for-cute-layouts`
4. `cutlass-3-x-apis-orthogonal-reusable-and-composable-abstractions-for-gemm-kernel-design`

## Code Map By Kernel Type

| Kernel type | Source paths | What to extract |
| --- | --- |
| TMA copy | `cfx-article-src/tma/{main.cu,tma_copy.h,tma_copy_multicast.h,scale_tma_kernel.h,shared_storage.h}` | tensor-map construction, multicast, mbarrier, async copy lifecycle |
| Hopper pipeline GEMM | `cfx-article-src/pipeline-gemm/{sm90_gemm_multistage.cu,sm90_gemm_ws.cu,hopper-gemm-ws/*}` | warp-specialized producer/consumer split, mainloop, epilogue, kernel traits |
| Stream-K GEMM | `cfx-article-src/streamk/{streamk.cu,tile_scheduler.hpp,mainloop_sm90_tma_gmma_ws.hpp,epilogue_sm90_tma_ws.hpp}` | persistent tile scheduling, wave quantization, split work ownership |
| CuTe transpose | `cfx-article-src/transpose-cute/include/*`, `transpose-cute/main.cu`, `transpose-cute/python/*` | naive/smem/direct/TMA-store transpose variants and Python extension |
| EVT / fused epilogue | `cfx-article-src/evt/{evt_gemm_cute.cu,reference.h,node_types.md}` | epilogue visitor tree and reference checks |
| CUTLASS Python extension | `cfx-article-src/cutlass_gemm/cutlass_gemm/*`, `gemm.py` | minimal binding for standalone CUTLASS experiments |
| CUTLASS 3 GEMM | `cutlass-kernels/src/cutlass-gemm/gemm.cu` | CollectiveBuilder, TMA, warp-specialized schedule |
| Low-level CuTe GEMM | `cutlass-kernels/src/cute-gemm-tma-gma/gemm.cu` | CuTe tensor layouts, TMA/GMA setup |
| FMHA | `cutlass-kernels/src/fmha/{fmha_forward.cu,online_softmax.h}` | two-GEMM attention, online softmax, TMA load/store |
| Pipelined FMHA | `cutlass-kernels/src/fmha-pipeline/*` | producer/consumer pipeline, softmax, shared storage |
| Utilities | `include/utils/cuda_launch.hpp`, `include/utils/fmha_cutlass.hpp` | launch wrappers and reference helpers |

## Search Patterns

```bash
rg -n "TMA|WGMMA|StreamK|persistent|pipeline|mbarrier|cute|CUTE|CollectiveBuilder|Tensor Memory|block scaling|FlexAttention|FlashAttention|transpose" .
```

## Candidate Use

- Prefer `cfx-article-src` and `cutlass-kernels` over copying code from HTML.
- Record article URL, repo URL, commit, source path, copied files, schedule
  choice, and mutation delta.
- When adapting CUTLASS/CuTe code, also record CUTLASS version or commit and
  target SM architecture.

## NCU Focus

- GEMM: tensor pipe utilization, TMA bytes/stalls, scheduler issue efficiency,
  waves-per-SM, split/Stream-K tail balance.
- TMA and transpose: DRAM/L2 throughput, shared-memory bank conflicts, async
  barrier stalls.
- Attention: tensor pipe utilization, softmax/SFU pressure, shared-memory
  pressure, TMA wait stalls.
