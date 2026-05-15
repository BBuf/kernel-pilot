# Veitner / Simon's Blog

Index: <https://veitner.bearblog.dev/blog/>

Companion code:

- <https://github.com/simveit/effective_transpose>
- <https://github.com/simveit/load_and_store>
- <https://gist.github.com/simveit>

Use this source for practical Hopper / Blackwell kernels that connect CuTe DSL,
QuACK, TMA/WGMMA, swizzling, reductions, GEMM, and sequence kernels.

## Article Map

| Kernel family | Articles to read |
| --- | --- |
| CuTe DSL basics | `An applied introduction to CuTeDSL`, `SGEMM in CuTeDSL`, `Thread Value Layouts in CuTe`, `Tensors Slicing in CuTe`, `CuTe partitions`, `Layout Gymnastics`, `MMA Atoms in CuTe` |
| Hopper CuTe DSL GEMM | `CuTeDSL on Hopper - WGMMA and TMA intro`, `CuTeDSL on Hopper - Pipelining`, `Consumer-Producer pattern on H100 in CuTeDSL`, `Persistent GEMM in CuTeDSL on Hopper`, `Persistent Float8 Dense Gemm on Hopper`, `Epilogue in CuTeDSL H100 kernels`, `Warp Specialisation in CuTeDSL` |
| Blackwell GEMM / low precision | `2 CTA GEMM on B200`, `Blackwell Pipelining with CuTeDSL`, `B200 Blockscaled GEMM - The setup`, `Scale Tensor construction in CuTeDSL`, `Grouped Block scaled Gemm - Intro`, `Grouped Blockscaled Gemm - Host code`, `Grouped Blockscaled Gemm - Kernel`, `NVFP4 GEMV`, `NVFP4 GEMV improved` |
| Memory movement | `TMA introduction`, `Use TMA without CUDA`, `Making matrix transpose really fast on Hopper GPUs`, `Swizzles and their usage in CuTeDSL Kernels`, `Understanding CuTe Swizzling`, `GPU L2 Cache Persistence`, `Cuda streams` |
| PTX / SASS | `Load and store matrices efficiently with PTX instructions`, `Use PTX instructions in Mojo`, `Analyze CUDA programs by looking at GPU assembly` |
| Norm / reduction | `Making vector sum really fast`, `Making prefix sum really fast`, `Making RMSNorm really fast`, `Backprop through RMSNorm`, `Backprob through Layernorm`, `Simple reduction in CuTeDSL` |
| Sequence kernels | `Gated Delta Net Decoding`, `Chunkwise Gated Delta Rule`, `Simple math to speed up GDN prefill` |
| QuACK | `Outperform compiled PyTorch code using QuACK`, `PingPong in the CuTeDSL with QuACK` |

## Companion Code Map

| Repo/path | Kernel type | What to extract |
| --- | --- | --- |
| `simveit/effective_transpose/transpose_naive.cu` | transpose baseline | baseline indexing and CUDA event harness |
| `simveit/effective_transpose/transpose_swizzle.cu` | transpose + swizzle | bank-conflict reduction through row/column swizzles |
| `simveit/effective_transpose/transpose_swizzle_batched.cu` | batched transpose | more work per CTA and higher DRAM utilization |
| `simveit/effective_transpose/transpose_swizzle_batched_for_profile.cu` | profiling variant | Nsight-friendly stable variant |
| `simveit/effective_transpose/swizzle.cu` | swizzle microbench | isolated swizzle math and TMA store/load |
| `simveit/load_and_store/ld_matrix_x{1,2,4}.cu` | PTX load | `ldmatrix` forms and register fragments |
| `simveit/load_and_store/st_matrix_x{1,2,4}.cu` | PTX store | `stmatrix` forms and shared-memory addressing |
| `gist.github.com/simveit` | small kernels | one-off CuTe DSL/CUDA snippets linked from posts |

## Search Patterns

```bash
rg -n "TMA|WGMMA|cp_async_bulk|mbarrier|swizzle|transpose|RMSNorm|NVFP4|blockscaled|GDN|ldmatrix|stmatrix" .
```

## Optimization Signals

- Transpose/TMA: check DRAM throughput, L2 bytes, bank conflicts, TMA wait
  stalls, and global sectors.
- GEMM: check tensor pipe %, register pressure, TMA bytes/stalls, occupancy,
  and waves-per-SM.
- Norm/reduction: check HBM throughput, shared-memory conflicts, long
  scoreboard, and warp issue stalls.
