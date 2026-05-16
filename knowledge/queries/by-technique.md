# Technique Index

<a id="async-copy"></a>
## async-copy

132 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-cccl-cub-5061` | upstream-code | [`sources/prs/cccl-cub/PR-5061.md`](../sources/prs/cccl-cub/PR-5061.md) | Replace CG by TMA copy in bulk copy fallback path |
| `pr-cccl-cub-5414` | upstream-code | [`sources/prs/cccl-cub/PR-5414.md`](../sources/prs/cccl-cub/PR-5414.md) | Move TMA barrier in DeviceTransform into dynamic SMEM |
| `pr-cccl-cub-6329` | upstream-code | [`sources/prs/cccl-cub/PR-6329.md`](../sources/prs/cccl-cub/PR-6329.md) | Improve `cuda::barrier` TMA examples and `elect_one` in `DeviceTransform` |
| `pr-cutlass-1661` | upstream-code | [`sources/prs/cutlass/PR-1661.md`](../sources/prs/cutlass/PR-1661.md) | Skip void-C kernels in the profiler when beta is non zero |
| `pr-cutlass-1795` | upstream-code | [`sources/prs/cutlass/PR-1795.md`](../sources/prs/cutlass/PR-1795.md) | Support for TMA Epilogue for Group Gemm and add pingpong ptr array & Group Gemm |
| `pr-cutlass-1883` | upstream-code | [`sources/prs/cutlass/PR-1883.md`](../sources/prs/cutlass/PR-1883.md) | Improve sm90 mixed dtype kernel |
| `pr-cutlass-1932` | upstream-code | [`sources/prs/cutlass/PR-1932.md`](../sources/prs/cutlass/PR-1932.md) | Blockwise Scaling for FP8 |
| `pr-cutlass-2095` | upstream-code | [`sources/prs/cutlass/PR-2095.md`](../sources/prs/cutlass/PR-2095.md) | Improvements for: Groupwise scaling along M for FP8 gemm |
| `pr-cutlass-2123` | upstream-code | [`sources/prs/cutlass/PR-2123.md`](../sources/prs/cutlass/PR-2123.md) | Hopper Grouped GEMM support for FP8 Accum |
| `pr-cutlass-2172` | upstream-code | [`sources/prs/cutlass/PR-2172.md`](../sources/prs/cutlass/PR-2172.md) | Fix SM90 beta=1 hang and stream-K launch errors |
| `pr-cutlass-2270` | upstream-code | [`sources/prs/cutlass/PR-2270.md`](../sources/prs/cutlass/PR-2270.md) | hopper-blockwise-generalization-optimization |
| `pr-cutlass-2790` | upstream-code | [`sources/prs/cutlass/PR-2790.md`](../sources/prs/cutlass/PR-2790.md) | Blockscaled Ragged Contiguous Grouped Gemm for MoEs |
| `pr-cutlass-3055` | upstream-code | [`sources/prs/cutlass/PR-3055.md`](../sources/prs/cutlass/PR-3055.md) | Replace std::min with cute::min in sm120 blockwise scaling device functions |
| `pr-cutlass-3176` | upstream-code | [`sources/prs/cutlass/PR-3176.md`](../sources/prs/cutlass/PR-3176.md) | Small Tile N BlockScaled GEMM + Grouped GEMM on SM12x |
| `pr-deepgemm-103` | upstream-code | [`sources/prs/deepgemm/PR-103.md`](../sources/prs/deepgemm/PR-103.md) | Grouped GEMM skip useless computation for unaligned Ms |
| `pr-deepgemm-112` | upstream-code | [`sources/prs/deepgemm/PR-112.md`](../sources/prs/deepgemm/PR-112.md) | Add more GPU architectures support |
| `pr-deepgemm-270` | upstream-code | [`sources/prs/deepgemm/PR-270.md`](../sources/prs/deepgemm/PR-270.md) | fix: use SM90ArchSpec instead of SM100ArchSpec in sm90_bf16_k_grouped_gemm |
| `pr-deepgemm-328` | upstream-code | [`sources/prs/deepgemm/PR-328.md`](../sources/prs/deepgemm/PR-328.md) | Sync nv_dev with upstream #316 (Mega MoE optimizations & benchmarks) |
| `pr-deepgemm-68` | upstream-code | [`sources/prs/deepgemm/PR-68.md`](../sources/prs/deepgemm/PR-68.md) | Correctly flush L2 (+performance impact & upcoming optimization fork) |
| `pr-deepgemm-74` | upstream-code | [`sources/prs/deepgemm/PR-74.md`](../sources/prs/deepgemm/PR-74.md) | Performance: Larger BlockTile optimizations enable 1470+ TF FP8 on the "H800"-SXM |
| `pr-deepgemm-78` | upstream-code | [`sources/prs/deepgemm/PR-78.md`](../sources/prs/deepgemm/PR-78.md) |  Solving bank conflict via padding and TMA 3D store |
| `pr-deepgemm-83` | upstream-code | [`sources/prs/deepgemm/PR-83.md`](../sources/prs/deepgemm/PR-83.md) | Use 1D TMA store instead of 3D |
| `pr-deepgemm-88` | upstream-code | [`sources/prs/deepgemm/PR-88.md`](../sources/prs/deepgemm/PR-88.md) | Support TMA multicast on B with m_grouped_gemm_contiguous. |
| `pr-flash-attention-1072` | upstream-code | [`sources/prs/flash-attention/PR-1072.md`](../sources/prs/flash-attention/PR-1072.md) | Add var-seq-len to FA3 fp16 / bf16 fwd |
| `pr-flash-attention-1100` | upstream-code | [`sources/prs/flash-attention/PR-1100.md`](../sources/prs/flash-attention/PR-1100.md) | Fp8 kernel with "in-kernel" transpose of V in producer |
| `pr-flash-attention-1173` | upstream-code | [`sources/prs/flash-attention/PR-1173.md`](../sources/prs/flash-attention/PR-1173.md) | FA3 FP8 qkv descales + restore max offset for h128 causal + added sync for producer WG |
| `pr-flash-attention-1180` | upstream-code | [`sources/prs/flash-attention/PR-1180.md`](../sources/prs/flash-attention/PR-1180.md) | Add ArchTag to pre/postprocess bwd kernels |
| `pr-flash-attention-1182` | upstream-code | [`sources/prs/flash-attention/PR-1182.md`](../sources/prs/flash-attention/PR-1182.md) | Add seqused_q in fwd / bwd and seqused_k in bwd in hopper FA. |
| `pr-flash-attention-1233` | upstream-code | [`sources/prs/flash-attention/PR-1233.md`](../sources/prs/flash-attention/PR-1233.md) | Add local attention in Hopper FAv3 |
| `pr-flash-attention-1236` | upstream-code | [`sources/prs/flash-attention/PR-1236.md`](../sources/prs/flash-attention/PR-1236.md) | FA3 kvcache + split kv + gqa parallelization |
| `pr-flash-attention-1268` | upstream-code | [`sources/prs/flash-attention/PR-1268.md`](../sources/prs/flash-attention/PR-1268.md) | Paged Attention support for FA3 |
| `pr-flash-attention-1331` | upstream-code | [`sources/prs/flash-attention/PR-1331.md`](../sources/prs/flash-attention/PR-1331.md) | FA3 paged attention: Readiness for Cutlass 3.6 / default value for block_table |
| `pr-flash-attention-1361` | upstream-code | [`sources/prs/flash-attention/PR-1361.md`](../sources/prs/flash-attention/PR-1361.md) | Fix FA3 Varlen Performance regression |
| `pr-flash-attention-1511` | upstream-code | [`sources/prs/flash-attention/PR-1511.md`](../sources/prs/flash-attention/PR-1511.md) | Fix CUDA 12.1 build |
| `pr-flash-attention-1604` | upstream-code | [`sources/prs/flash-attention/PR-1604.md`](../sources/prs/flash-attention/PR-1604.md) | Support hdimQK != hdimV backward |
| `pr-flash-attention-1868` | upstream-code | [`sources/prs/flash-attention/PR-1868.md`](../sources/prs/flash-attention/PR-1868.md) | flash-attn-cute bwd sm90 |
| `pr-flash-attention-1893` | upstream-code | [`sources/prs/flash-attention/PR-1893.md`](../sources/prs/flash-attention/PR-1893.md) | Improve causal backward determinism perf with SPT schedule |
| `pr-flash-attention-1924` | upstream-code | [`sources/prs/flash-attention/PR-1924.md`](../sources/prs/flash-attention/PR-1924.md) | Remove self refs in softmax for-loop |
| `pr-flash-attention-1940` | upstream-code | [`sources/prs/flash-attention/PR-1940.md`](../sources/prs/flash-attention/PR-1940.md) | [Cute,Fwd,Sm100] Implement SplitKV |
| `pr-flash-attention-1985` | upstream-code | [`sources/prs/flash-attention/PR-1985.md`](../sources/prs/flash-attention/PR-1985.md) | [Cute] Block sparse support Sm100 |
| `pr-flash-attention-1993` | upstream-code | [`sources/prs/flash-attention/PR-1993.md`](../sources/prs/flash-attention/PR-1993.md) | [Cute,Fwd,Sm100] Support `q_stage=1` for inference |
| `pr-flash-attention-1999` | upstream-code | [`sources/prs/flash-attention/PR-1999.md`](../sources/prs/flash-attention/PR-1999.md) | [Cute,Fwd,Sm100] Support paged attention |
| `pr-flash-attention-2014` | upstream-code | [`sources/prs/flash-attention/PR-2014.md`](../sources/prs/flash-attention/PR-2014.md) | [Cute,Sm100,Fwd] use correction warps for epi when not using TMA |
| `pr-flash-attention-2026` | upstream-code | [`sources/prs/flash-attention/PR-2026.md`](../sources/prs/flash-attention/PR-2026.md) | [Cute,Fwd,Sm100] don't pass mask_fn to softmax_step generically |
| `pr-flash-attention-2043` | upstream-code | [`sources/prs/flash-attention/PR-2043.md`](../sources/prs/flash-attention/PR-2043.md) | [Cute,Fwd] Extend score_mod to variable sequence length |
| `pr-flash-attention-2070` | upstream-code | [`sources/prs/flash-attention/PR-2070.md`](../sources/prs/flash-attention/PR-2070.md) | Add score-mod bwd support  |
| `pr-flash-attention-2085` | upstream-code | [`sources/prs/flash-attention/PR-2085.md`](../sources/prs/flash-attention/PR-2085.md) | Add blocksparse support for bwd on blackwell |
| `pr-flash-attention-2109` | upstream-code | [`sources/prs/flash-attention/PR-2109.md`](../sources/prs/flash-attention/PR-2109.md) | [Cute,Fwd,Sm100] fp8 e4m3 and e5m2 support |
| `pr-flash-attention-2150` | upstream-code | [`sources/prs/flash-attention/PR-2150.md`](../sources/prs/flash-attention/PR-2150.md) | [Cute, Bwd, Sm100] Add varlen for sm100 bwd |
| `pr-flash-attention-2174` | upstream-code | [`sources/prs/flash-attention/PR-2174.md`](../sources/prs/flash-attention/PR-2174.md) | [Cute] update row_max before safe overwrite for online_softmax |
| `pr-flash-attention-2301` | upstream-code | [`sources/prs/flash-attention/PR-2301.md`](../sources/prs/flash-attention/PR-2301.md) | Fix GQA crash in cute FLASH backend: init load_Q before conditional |
| `pr-flash-attention-2303` | upstream-code | [`sources/prs/flash-attention/PR-2303.md`](../sources/prs/flash-attention/PR-2303.md) | [Cute,Fwd,Sm100] fix paged kv |
| `pr-flash-attention-2329` | upstream-code | [`sources/prs/flash-attention/PR-2329.md`](../sources/prs/flash-attention/PR-2329.md) | SM120 forward pass (Blackwell GeForce / DGX Spark) |
| `pr-flash-attention-2360` | upstream-code | [`sources/prs/flash-attention/PR-2360.md`](../sources/prs/flash-attention/PR-2360.md) | [Fwd,Sm90] Add paged KV attention support (tma and cp.async) |
| `pr-flash-attention-2368` | upstream-code | [`sources/prs/flash-attention/PR-2368.md`](../sources/prs/flash-attention/PR-2368.md) | [Cute] fix: FA4 paged attention kv load for DeepSeek (192,128) on SM100 |
| `pr-flash-attention-2412` | upstream-code | [`sources/prs/flash-attention/PR-2412.md`](../sources/prs/flash-attention/PR-2412.md) | Feat([FA4][CUTE DSL]) Add head_dim=256 support (forward + backward) |
| `pr-flash-attention-2441` | upstream-code | [`sources/prs/flash-attention/PR-2441.md`](../sources/prs/flash-attention/PR-2441.md) | [Cute,Sm100,Fwd] add MLA 64/512 with topk sparsity for MQA 128 heads |
| `pr-flash-attention-2470` | upstream-code | [`sources/prs/flash-attention/PR-2470.md`](../sources/prs/flash-attention/PR-2470.md) | [Cute,Fwd,Sm100] Fix the crash when seqlen_k=0 |
| `pr-flash-attention-2488` | upstream-code | [`sources/prs/flash-attention/PR-2488.md`](../sources/prs/flash-attention/PR-2488.md) | [hd256] Improve forward kernel with exp2 FMA emulation (3% to 9% performance gain) |
| `pr-flash-attention-2489` | upstream-code | [`sources/prs/flash-attention/PR-2489.md`](../sources/prs/flash-attention/PR-2489.md) | [hd256] Add TMA paged KV support to SM100 2CTA forward kernel |
| `pr-flash-attention-2497` | upstream-code | [`sources/prs/flash-attention/PR-2497.md`](../sources/prs/flash-attention/PR-2497.md) | [FA4][hd256] Backward TMA bulk-store epilogue + LSE/dpsum coalesce |
| `pr-flash-attention-2504` | upstream-code | [`sources/prs/flash-attention/PR-2504.md`](../sources/prs/flash-attention/PR-2504.md) | [SM100] Guard gO None in empty-tile correction |
| `pr-flashinfer-2630` | upstream-code | [`sources/prs/flashinfer/PR-2630.md`](../sources/prs/flashinfer/PR-2630.md) | Add parallel attention |
| `pr-flashinfer-2711` | upstream-code | [`sources/prs/flashinfer/PR-2711.md`](../sources/prs/flashinfer/PR-2711.md) | feat: Add DiT-oriented kernels where Qk (Bmm1) type can be reinterpreted into Int8 or BFloat16 |
| `pr-flashinfer-2726` | upstream-code | [`sources/prs/flashinfer/PR-2726.md`](../sources/prs/flashinfer/PR-2726.md) | Added missing padding |
| `pr-flashinfer-2799` | upstream-code | [`sources/prs/flashinfer/PR-2799.md`](../sources/prs/flashinfer/PR-2799.md) | [fmha-v2] Support HND and NHD paged KV cache layouts with conditional stride handling |
| `pr-flashinfer-2841` | upstream-code | [`sources/prs/flashinfer/PR-2841.md`](../sources/prs/flashinfer/PR-2841.md) | [Perf] Add FMHAv2 to flashinfer_benchmark.py and eliminate unnecessary H2D |
| `pr-flashinfer-2944` | upstream-code | [`sources/prs/flashinfer/PR-2944.md`](../sources/prs/flashinfer/PR-2944.md) | feat: Add CuTe DSL grouped-gemm + combine fusion support |
| `pr-flashinfer-2959` | upstream-code | [`sources/prs/flashinfer/PR-2959.md`](../sources/prs/flashinfer/PR-2959.md) | [Fmha] Add head_dim=512 support for trtllm attention kernels |
| `pr-flashinfer-2962` | upstream-code | [`sources/prs/flashinfer/PR-2962.md`](../sources/prs/flashinfer/PR-2962.md) | Improved `simple` mamba SSU kernel  |
| `pr-flashinfer-3039` | upstream-code | [`sources/prs/flashinfer/PR-3039.md`](../sources/prs/flashinfer/PR-3039.md) | feat: Integrate CuTe DSL FMHA prefill kernels by loading cubin |
| `pr-flashinfer-3059` | upstream-code | [`sources/prs/flashinfer/PR-3059.md`](../sources/prs/flashinfer/PR-3059.md) | Support Allreduce + Norm + Per-token Group Fp8 Quant Fusion |
| `pr-flashinfer-3080` | upstream-code | [`sources/prs/flashinfer/PR-3080.md`](../sources/prs/flashinfer/PR-3080.md) | feat: Add b12x_fused_moe / B12xMoEWrapper SM120 APIs with micro kernel and ReLU2 |
| `pr-flashinfer-3084` | upstream-code | [`sources/prs/flashinfer/PR-3084.md`](../sources/prs/flashinfer/PR-3084.md) | perf: optimize MXFP4xBF16 & INT4xFP8 CUTLASS MoE backend for SM90 |
| `pr-flashinfer-3132` | upstream-code | [`sources/prs/flashinfer/PR-3132.md`](../sources/prs/flashinfer/PR-3132.md) | [CuTe DSL] Fix FP8 MLA persistent perf regression and ProxyKind cu13 wheel breakage |
| `pr-flashinfer-3152` | upstream-code | [`sources/prs/flashinfer/PR-3152.md`](../sources/prs/flashinfer/PR-3152.md) | Integrate CUTLASS Small Tile N Blockscaled GEMMs/Grouped GEMMs for SM120 and SM121 |
| `pr-flashinfer-3185` | upstream-code | [`sources/prs/flashinfer/PR-3185.md`](../sources/prs/flashinfer/PR-3185.md) | feat: enable glm5 router gemm |
| `pr-flashinfer-3276` | upstream-code | [`sources/prs/flashinfer/PR-3276.md`](../sources/prs/flashinfer/PR-3276.md) | fix(fmha_v2): fix FP8 V-scratch pipeline and varlen scheduler on SM90 |
| `pr-quack-100` | upstream-code | [`sources/prs/quack/PR-100.md`](../sources/prs/quack/PR-100.md) | Autotune between tma gather and cp.async in SM100 |
| `pr-quack-126` | upstream-code | [`sources/prs/quack/PR-126.md`](../sources/prs/quack/PR-126.md) | feat: add `weight` to cross entropy |
| `pr-quack-132` | upstream-code | [`sources/prs/quack/PR-132.md`](../sources/prs/quack/PR-132.md) | RMS Norm Bwd: Optimize for GB200 w/ TMA loads, reload_x, separate output dtype, new launch configs |
| `pr-quack-96` | upstream-code | [`sources/prs/quack/PR-96.md`](../sources/prs/quack/PR-96.md) | Add SM120 (consumer Blackwell) support |
| `pr-sglang-23965` | upstream-code | [`sources/prs/sglang/PR-23965.md`](../sources/prs/sglang/PR-23965.md) | Enable PDL for various kernels in DSV32/GLM5 |
| `pr-tensorrt-llm-10042` | upstream-code | [`sources/prs/tensorrt-llm/PR-10042.md`](../sources/prs/tensorrt-llm/PR-10042.md) | [None][perf] Add more optimization options for MOE CuteDSL finalized kernel |
| `pr-tensorrt-llm-10264` | upstream-code | [`sources/prs/tensorrt-llm/PR-10264.md`](../sources/prs/tensorrt-llm/PR-10264.md) | [TRTLLM-10022][feat] Add hopper xqa decode support for skip softmax attention |
| `pr-tensorrt-llm-10742` | upstream-code | [`sources/prs/tensorrt-llm/PR-10742.md`](../sources/prs/tensorrt-llm/PR-10742.md) | [https://nvbugs/5669671][fix] Support GuidedDecoder with sharded logits (pick #10698) |
| `pr-tensorrt-llm-10987` | upstream-code | [`sources/prs/tensorrt-llm/PR-10987.md`](../sources/prs/tensorrt-llm/PR-10987.md) | [TRTLLM-9831][perf] Use TMA.RED to improve effective memory bandwidth |
| `pr-tensorrt-llm-12440` | upstream-code | [`sources/prs/tensorrt-llm/PR-12440.md`](../sources/prs/tensorrt-llm/PR-12440.md) | [None][feat] Update TRTLLM MoE cubins |
| `pr-tensorrt-llm-12866` | upstream-code | [`sources/prs/tensorrt-llm/PR-12866.md`](../sources/prs/tensorrt-llm/PR-12866.md) | [None][feat] AutoDeploy: Onboard google/gemma-4-31B-it dense model, including nvfp4 |
| `pr-tensorrt-llm-13120` | upstream-code | [`sources/prs/tensorrt-llm/PR-13120.md`](../sources/prs/tensorrt-llm/PR-13120.md) | [None][bug] fix SM90 full-mask skip-softmax dispatch |
| `pr-tensorrt-llm-13157` | upstream-code | [`sources/prs/tensorrt-llm/PR-13157.md`](../sources/prs/tensorrt-llm/PR-13157.md) | [https://nvbugs/6086538][fix] suppress misleading skip-softmax FMHA warning in generation |
| `pr-tensorrt-llm-13433` | upstream-code | [`sources/prs/tensorrt-llm/PR-13433.md`](../sources/prs/tensorrt-llm/PR-13433.md) | [None][perf] Extend customMoeRouting kernel to support Qwen3.5 |
| `pr-tensorrt-llm-13628` | upstream-code | [`sources/prs/tensorrt-llm/PR-13628.md`](../sources/prs/tensorrt-llm/PR-13628.md) | [None][feat] Fuse FP8 1x128 quantize + UE8M0 scale pack on SM100 |
| `pr-tensorrt-llm-13945` | upstream-code | [`sources/prs/tensorrt-llm/PR-13945.md`](../sources/prs/tensorrt-llm/PR-13945.md) | [https://nvbugs/6100102][fix] Fix cutlass grouped gemm launcher EpilogueScalars construction |
| `pr-tensorrt-llm-6538` | upstream-code | [`sources/prs/tensorrt-llm/PR-6538.md`](../sources/prs/tensorrt-llm/PR-6538.md) | [None][feat] Use Separate QKV Input Layout for Context MLA |
| `pr-tensorrt-llm-6809` | upstream-code | [`sources/prs/tensorrt-llm/PR-6809.md`](../sources/prs/tensorrt-llm/PR-6809.md) | [OMNIML-2336][feat] Add NVFP4 x FP8 |
| `pr-tensorrt-llm-9025` | upstream-code | [`sources/prs/tensorrt-llm/PR-9025.md`](../sources/prs/tensorrt-llm/PR-9025.md) | [None][feat] Update TRTLLM MoE cubins; reduce mxfp4 weight padding requirement; tighten TMA bound |
| `pr-tensorrt-llm-9838` | upstream-code | [`sources/prs/tensorrt-llm/PR-9838.md`](../sources/prs/tensorrt-llm/PR-9838.md) | [https://nvbugs/5726962][feat] Apply fusion for W4AFP8_AWQ MoE |
| `pr-tilelang-1667` | upstream-code | [`sources/prs/tilelang/PR-1667.md`](../sources/prs/tilelang/PR-1667.md) | [Feature] Support `cp.reduce.async.bulk.tensor` |
| `pr-tilelang-1840` | upstream-code | [`sources/prs/tilelang/PR-1840.md`](../sources/prs/tilelang/PR-1840.md) | [BugFix] Fix Hopper TMA lowering without warp specialization |
| `pr-tilelang-1882` | upstream-code | [`sources/prs/tilelang/PR-1882.md`](../sources/prs/tilelang/PR-1882.md) | [Feature] 2-SM support for TMA, TMEM and TCGEN5MMA on Blackwell |
| `pr-tilelang-1909` | upstream-code | [`sources/prs/tilelang/PR-1909.md`](../sources/prs/tilelang/PR-1909.md) | [Feature] Add Producer-Consumer Warp Specialization and T.tma_copy() API |
| `pr-tilelang-1931` | upstream-code | [`sources/prs/tilelang/PR-1931.md`](../sources/prs/tilelang/PR-1931.md) | [Runtime] Improve TMA descriptor diagnostics |
| `pr-tilelang-1946` | upstream-code | [`sources/prs/tilelang/PR-1946.md`](../sources/prs/tilelang/PR-1946.md) | [BugFix] Update usage of tma load in SM100 manual warp-specialized examples |
| `pr-tilelang-1953` | upstream-code | [`sources/prs/tilelang/PR-1953.md`](../sources/prs/tilelang/PR-1953.md) | [PIpeline] Enable software pipelining when warp specialization is unavailable |
| `pr-tilelang-1962` | upstream-code | [`sources/prs/tilelang/PR-1962.md`](../sources/prs/tilelang/PR-1962.md) | [Bugfix] Fix double buffer versioning when TMA is used without warp specialization |
| `pr-tilelang-1975` | upstream-code | [`sources/prs/tilelang/PR-1975.md`](../sources/prs/tilelang/PR-1975.md) | Fix wrapped pre-loop TMA prefixes in producer-consumer WS |
| `pr-tilelang-1981` | upstream-code | [`sources/prs/tilelang/PR-1981.md`](../sources/prs/tilelang/PR-1981.md) | [Feature] Support TMA store in T.tma_copy() |
| `pr-tilelang-1989` | upstream-code | [`sources/prs/tilelang/PR-1989.md`](../sources/prs/tilelang/PR-1989.md) | Add regression test for 1D TMA load compilation and execution |
| `pr-tilelang-1995` | upstream-code | [`sources/prs/tilelang/PR-1995.md`](../sources/prs/tilelang/PR-1995.md) | [BugFix] Fix missing barrier init attrs when TMA is disabled |
| `pr-tilelang-2024` | upstream-code | [`sources/prs/tilelang/PR-2024.md`](../sources/prs/tilelang/PR-2024.md) | Re-enable deprecated `TL_DISABLE_TMA_LOWER` pass config for TMA store |
| `pr-tilelang-2052` | upstream-code | [`sources/prs/tilelang/PR-2052.md`](../sources/prs/tilelang/PR-2052.md) | [Bugfix] Use shared::cta instead of shared::cluster for non-cluster T… |
| `pr-tilelang-2087` | upstream-code | [`sources/prs/tilelang/PR-2087.md`](../sources/prs/tilelang/PR-2087.md) | [Bugfix] Enable `.shared::cta` in TMA copy paths only on CUDA 12.8+ |
| `pr-tilelang-2107` | upstream-code | [`sources/prs/tilelang/PR-2107.md`](../sources/prs/tilelang/PR-2107.md) | [TMA] Support FP4 TensorMap TMA copies |
| `pr-tilelang-2134` | upstream-code | [`sources/prs/tilelang/PR-2134.md`](../sources/prs/tilelang/PR-2134.md) | fix: TMA alignment to 1024 bytes on Blackwell |
| `pr-tilelang-2151` | upstream-code | [`sources/prs/tilelang/PR-2151.md`](../sources/prs/tilelang/PR-2151.md) | [TMA] Fix TMA descriptor init placement |
| `pr-tilelang-2166` | upstream-code | [`sources/prs/tilelang/PR-2166.md`](../sources/prs/tilelang/PR-2166.md) | [BugFix] Consider non-local store in external call and SIMT producer for warp specialize |
| `pr-triton-10042` | upstream-code | [`sources/prs/triton/PR-10042.md`](../sources/prs/triton/PR-10042.md) | [Triton] Fix LLVMDILocalVariable pass crash with LLVM_EXTRACT_DI_LOCAL_VARIABLES |
| `pr-triton-10148` | upstream-code | [`sources/prs/triton/PR-10148.md`](../sources/prs/triton/PR-10148.md) | [Reland][NVIDIA] Support swizzle 0 TMA + MMA for Hopper and Blackwell |
| `pr-triton-10157` | upstream-code | [`sources/prs/triton/PR-10157.md`](../sources/prs/triton/PR-10157.md) | [AMD] Add Triton-level tt.descriptor_gather and tt.descriptor_scatter support for gfx1250 |
| `pr-triton-10167` | upstream-code | [`sources/prs/triton/PR-10167.md`](../sources/prs/triton/PR-10167.md) | [CONSAN] Add read before any write check |
| `pr-triton-10172` | upstream-code | [`sources/prs/triton/PR-10172.md`](../sources/prs/triton/PR-10172.md) | [AMD][TDM] Pipeline tt.descriptor_gather through the TDM async chain |
| `pr-triton-10190` | upstream-code | [`sources/prs/triton/PR-10190.md`](../sources/prs/triton/PR-10190.md) | [mxfp4] Fix Hopper scale padding mask |
| `pr-triton-10196` | upstream-code | [`sources/prs/triton/PR-10196.md`](../sources/prs/triton/PR-10196.md) | [MULTICTA] Fix multicast pattern for tcgen05_mma_scaled |
| `pr-triton-10212` | upstream-code | [`sources/prs/triton/PR-10212.md`](../sources/prs/triton/PR-10212.md) | [CONSAN] Multi CTA model v2 |
| `pr-triton-10242` | upstream-code | [`sources/prs/triton/PR-10242.md`](../sources/prs/triton/PR-10242.md) | Fix convert_layout lowering for CGA + slice layouts. |
| `pr-triton-10324` | upstream-code | [`sources/prs/triton/PR-10324.md`](../sources/prs/triton/PR-10324.md) | [BACKEND] Allow two_ctas=False barriers in TMA ops in a 2CTA kernel |
| `pr-vllm-32195` | upstream-code | [`sources/prs/vllm/PR-32195.md`](../sources/prs/vllm/PR-32195.md) | Add TMA support to fused_moe_lora kernel |
| `pr-vllm-32619` | upstream-code | [`sources/prs/vllm/PR-32619.md`](../sources/prs/vllm/PR-32619.md) | [Perf] Create TMA-aligned input scale tensor for DeepGemm on Hopper |
| `pr-vllm-33255` | upstream-code | [`sources/prs/vllm/PR-33255.md`](../sources/prs/vllm/PR-33255.md) | [Bugfix] Fix quant RMS norm fusion for quantization with TMA-aligned scales |
| `pr-vllm-38504` | upstream-code | [`sources/prs/vllm/PR-38504.md`](../sources/prs/vllm/PR-38504.md) | [Kernels][MoE] Fix legacy_routing to use bitmatrix-based routing path |
| `pr-vllm-39391` | upstream-code | [`sources/prs/vllm/PR-39391.md`](../sources/prs/vllm/PR-39391.md) | fix: clamp NaN/Inf in topk_softmax to prevent duplicate expert IDs |

<a id="autotuning"></a>
## autotuning

125 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-cccl-cub-3236` | upstream-code | [`sources/prs/cccl-cub/PR-3236.md`](../sources/prs/cccl-cub/PR-3236.md) | Fix scan / sm90 perf regression  |
| `pr-cccl-cub-3559` | upstream-code | [`sources/prs/cccl-cub/PR-3559.md`](../sources/prs/cccl-cub/PR-3559.md) | Add b200 tunings for scan.exclusive.sum |
| `pr-cccl-cub-3691` | upstream-code | [`sources/prs/cccl-cub/PR-3691.md`](../sources/prs/cccl-cub/PR-3691.md) | Fix SM100 histogram tunings |
| `pr-cccl-cub-4961` | upstream-code | [`sources/prs/cccl-cub/PR-4961.md`](../sources/prs/cccl-cub/PR-4961.md) | Add nondeterministic reduce that uses atomics |
| `pr-cccl-cub-5314` | upstream-code | [`sources/prs/cccl-cub/PR-5314.md`](../sources/prs/cccl-cub/PR-5314.md) | CUB - Add internal integer utils and tests (Split `WarpReduce` PR) |
| `pr-cccl-cub-6077` | upstream-code | [`sources/prs/cccl-cub/PR-6077.md`](../sources/prs/cccl-cub/PR-6077.md) | [CUB] Use `BlockLoadToShared` in `DeviceMerge` |
| `pr-cccl-cub-6597` | upstream-code | [`sources/prs/cccl-cub/PR-6597.md`](../sources/prs/cccl-cub/PR-6597.md) | Split fixed-size segmented reduce dispatch header |
| `pr-cccl-cub-6811` | upstream-code | [`sources/prs/cccl-cub/PR-6811.md`](../sources/prs/cccl-cub/PR-6811.md) | Integrate decoupled lookahead warpspeed scan |
| `pr-cccl-cub-7093` | upstream-code | [`sources/prs/cccl-cub/PR-7093.md`](../sources/prs/cccl-cub/PR-7093.md) | Implement new tuning API arch dispatching |
| `pr-cccl-cub-7346` | upstream-code | [`sources/prs/cccl-cub/PR-7346.md`](../sources/prs/cccl-cub/PR-7346.md) | Implement the new tuning API for deterministic (rfa) reduce dispatch |
| `pr-cccl-cub-7669` | upstream-code | [`sources/prs/cccl-cub/PR-7669.md`](../sources/prs/cccl-cub/PR-7669.md) | Implement the new tuning API for `DeviceRleDispatch` |
| `pr-cccl-cub-7718` | upstream-code | [`sources/prs/cccl-cub/PR-7718.md`](../sources/prs/cccl-cub/PR-7718.md) | Optimize non fixed size segmented reduce for small segments using max_segment_size |
| `pr-cccl-cub-7805` | upstream-code | [`sources/prs/cccl-cub/PR-7805.md`](../sources/prs/cccl-cub/PR-7805.md) | Forward policy hub from `dispatch_streaming_arg_reduce_t` to `reduce::dispatch` |
| `pr-cccl-cub-7807` | upstream-code | [`sources/prs/cccl-cub/PR-7807.md`](../sources/prs/cccl-cub/PR-7807.md) | Implement the new tuning API for `detail::reduce::dispatch_streaming_arg_reduce_t` |
| `pr-cccl-cub-7810` | upstream-code | [`sources/prs/cccl-cub/PR-7810.md`](../sources/prs/cccl-cub/PR-7810.md) | Use the new tuning API internally for `detail::transform::dispatch` |
| `pr-cccl-cub-7814` | upstream-code | [`sources/prs/cccl-cub/PR-7814.md`](../sources/prs/cccl-cub/PR-7814.md) | [Backport branch/3.3.x] Forward policy hub from `dispatch_streaming_arg_reduce_t` to `reduce::dispatch` |
| `pr-cccl-cub-7844` | upstream-code | [`sources/prs/cccl-cub/PR-7844.md`](../sources/prs/cccl-cub/PR-7844.md) | Implement the new tuning API for `DispatchSegmentedRadixSort` |
| `pr-cccl-cub-7874` | upstream-code | [`sources/prs/cccl-cub/PR-7874.md`](../sources/prs/cccl-cub/PR-7874.md) | Implement the new tuning API for `DispatchSegmentedSort` |
| `pr-cccl-cub-7928` | upstream-code | [`sources/prs/cccl-cub/PR-7928.md`](../sources/prs/cccl-cub/PR-7928.md) | Implement the new tuning API for `DispatchTopK` |
| `pr-cccl-cub-8311` | upstream-code | [`sources/prs/cccl-cub/PR-8311.md`](../sources/prs/cccl-cub/PR-8311.md) | Implement the new tuning API for `DispatchSelectIf` |
| `pr-cccl-cub-8332` | upstream-code | [`sources/prs/cccl-cub/PR-8332.md`](../sources/prs/cccl-cub/PR-8332.md) | simplify dispatch segmented reduce to use latest dispatch and new tunings API |
| `pr-cccl-cub-8352` | upstream-code | [`sources/prs/cccl-cub/PR-8352.md`](../sources/prs/cccl-cub/PR-8352.md) | Apply some random warpspeed tunings |
| `pr-cccl-cub-8538` | upstream-code | [`sources/prs/cccl-cub/PR-8538.md`](../sources/prs/cccl-cub/PR-8538.md) | Implement the new tuning API for `detail::batched_topk::dispatch_batched_topk` |
| `pr-cccl-cub-8742` | upstream-code | [`sources/prs/cccl-cub/PR-8742.md`](../sources/prs/cccl-cub/PR-8742.md) | Use the new tuning API internally for `detail::topk::dispatch` |
| `pr-cccl-cub-8826` | upstream-code | [`sources/prs/cccl-cub/PR-8826.md`](../sources/prs/cccl-cub/PR-8826.md) | Use the new tuning API internally for `detail::reduce[_nd]::dispatch[_nd]` |
| `pr-cutlass-1350` | upstream-code | [`sources/prs/cutlass/PR-1350.md`](../sources/prs/cutlass/PR-1350.md) | Add couple configs into generator.py for mixed input MM |
| `pr-cutlass-2172` | upstream-code | [`sources/prs/cutlass/PR-2172.md`](../sources/prs/cutlass/PR-2172.md) | Fix SM90 beta=1 hang and stream-K launch errors |
| `pr-cutlass-2596` | upstream-code | [`sources/prs/cutlass/PR-2596.md`](../sources/prs/cutlass/PR-2596.md) | Fix broken imports in heuristics_provider.py |
| `pr-deepgemm-103` | upstream-code | [`sources/prs/deepgemm/PR-103.md`](../sources/prs/deepgemm/PR-103.md) | Grouped GEMM skip useless computation for unaligned Ms |
| `pr-deepgemm-112` | upstream-code | [`sources/prs/deepgemm/PR-112.md`](../sources/prs/deepgemm/PR-112.md) | Add more GPU architectures support |
| `pr-deepgemm-158` | upstream-code | [`sources/prs/deepgemm/PR-158.md`](../sources/prs/deepgemm/PR-158.md) | Fix inappropriate configs for some small shapes |
| `pr-deepgemm-168` | upstream-code | [`sources/prs/deepgemm/PR-168.md`](../sources/prs/deepgemm/PR-168.md) | Fix performance issue of m-grouped contiguous GEMMs. |
| `pr-deepgemm-193` | upstream-code | [`sources/prs/deepgemm/PR-193.md`](../sources/prs/deepgemm/PR-193.md) | Fix multicast bug and optimize masked GEMM |
| `pr-deepgemm-198` | upstream-code | [`sources/prs/deepgemm/PR-198.md`](../sources/prs/deepgemm/PR-198.md) | Make various updates and fixes |
| `pr-deepgemm-316` | upstream-code | [`sources/prs/deepgemm/PR-316.md`](../sources/prs/deepgemm/PR-316.md) | Add various optimizations and Mega MoE benchmarks |
| `pr-deepgemm-328` | upstream-code | [`sources/prs/deepgemm/PR-328.md`](../sources/prs/deepgemm/PR-328.md) | Sync nv_dev with upstream #316 (Mega MoE optimizations & benchmarks) |
| `pr-deepgemm-88` | upstream-code | [`sources/prs/deepgemm/PR-88.md`](../sources/prs/deepgemm/PR-88.md) | Support TMA multicast on B with m_grouped_gemm_contiguous. |
| `pr-flash-attention-1236` | upstream-code | [`sources/prs/flash-attention/PR-1236.md`](../sources/prs/flash-attention/PR-1236.md) | FA3 kvcache + split kv + gqa parallelization |
| `pr-flash-attention-1361` | upstream-code | [`sources/prs/flash-attention/PR-1361.md`](../sources/prs/flash-attention/PR-1361.md) | Fix FA3 Varlen Performance regression |
| `pr-flash-attention-1823` | upstream-code | [`sources/prs/flash-attention/PR-1823.md`](../sources/prs/flash-attention/PR-1823.md) | Add sorting and head swizzle to varlen scheduler |
| `pr-flash-attention-1893` | upstream-code | [`sources/prs/flash-attention/PR-1893.md`](../sources/prs/flash-attention/PR-1893.md) | Improve causal backward determinism perf with SPT schedule |
| `pr-flash-attention-1934` | upstream-code | [`sources/prs/flash-attention/PR-1934.md`](../sources/prs/flash-attention/PR-1934.md) | feat: Adding varlen support to cute-dsl sm80 bwd |
| `pr-flash-attention-1940` | upstream-code | [`sources/prs/flash-attention/PR-1940.md`](../sources/prs/flash-attention/PR-1940.md) | [Cute,Fwd,Sm100] Implement SplitKV |
| `pr-flash-attention-2033` | upstream-code | [`sources/prs/flash-attention/PR-2033.md`](../sources/prs/flash-attention/PR-2033.md) | [Cute,Bwd,Sm100] enable deterministic mode for sm100 bwd and fix race conditions |
| `pr-flash-attention-2043` | upstream-code | [`sources/prs/flash-attention/PR-2043.md`](../sources/prs/flash-attention/PR-2043.md) | [Cute,Fwd] Extend score_mod to variable sequence length |
| `pr-flash-attention-2218` | upstream-code | [`sources/prs/flash-attention/PR-2218.md`](../sources/prs/flash-attention/PR-2218.md) | [Ai-assisted] CLC work stealing |
| `pr-flash-attention-2236` | upstream-code | [`sources/prs/flash-attention/PR-2236.md`](../sources/prs/flash-attention/PR-2236.md) | [Cute,Flex,Fwd] Allow vectorized score_mod definitions |
| `pr-flash-attention-2333` | upstream-code | [`sources/prs/flash-attention/PR-2333.md`](../sources/prs/flash-attention/PR-2333.md) | Add SM120 varlen attention support |
| `pr-flash-attention-2390` | upstream-code | [`sources/prs/flash-attention/PR-2390.md`](../sources/prs/flash-attention/PR-2390.md) | [Cute,Sm100,Bwd] refine bwd swizzle for deterministic |
| `pr-flash-attention-2412` | upstream-code | [`sources/prs/flash-attention/PR-2412.md`](../sources/prs/flash-attention/PR-2412.md) | Feat([FA4][CUTE DSL]) Add head_dim=256 support (forward + backward) |
| `pr-flash-attention-2441` | upstream-code | [`sources/prs/flash-attention/PR-2441.md`](../sources/prs/flash-attention/PR-2441.md) | [Cute,Sm100,Fwd] add MLA 64/512 with topk sparsity for MQA 128 heads |
| `pr-flash-attention-2455` | upstream-code | [`sources/prs/flash-attention/PR-2455.md`](../sources/prs/flash-attention/PR-2455.md) | Add CLC scheduler heuristic |
| `pr-flash-attention-2488` | upstream-code | [`sources/prs/flash-attention/PR-2488.md`](../sources/prs/flash-attention/PR-2488.md) | [hd256] Improve forward kernel with exp2 FMA emulation (3% to 9% performance gain) |
| `pr-flash-attention-2489` | upstream-code | [`sources/prs/flash-attention/PR-2489.md`](../sources/prs/flash-attention/PR-2489.md) | [hd256] Add TMA paged KV support to SM100 2CTA forward kernel |
| `pr-flash-attention-2497` | upstream-code | [`sources/prs/flash-attention/PR-2497.md`](../sources/prs/flash-attention/PR-2497.md) | [FA4][hd256] Backward TMA bulk-store epilogue + LSE/dpsum coalesce |
| `pr-flash-attention-2515` | upstream-code | [`sources/prs/flash-attention/PR-2515.md`](../sources/prs/flash-attention/PR-2515.md) | Fix ZeroDivisionError in num_splits_heuristic for empty Q workloads |
| `pr-flashinfer-2557` | upstream-code | [`sources/prs/flashinfer/PR-2557.md`](../sources/prs/flashinfer/PR-2557.md) | [Bugfix][comm] Fix FP4 one-shot launch config instability in trtllm_allreduce_fusion |
| `pr-flashinfer-2630` | upstream-code | [`sources/prs/flashinfer/PR-2630.md`](../sources/prs/flashinfer/PR-2630.md) | Add parallel attention |
| `pr-flashinfer-2914` | upstream-code | [`sources/prs/flashinfer/PR-2914.md`](../sources/prs/flashinfer/PR-2914.md) | feat: Add cuBLASLt backend for `mm_bf16` and enable multi-tactic autotuning for FP8/MXFP8 runners |
| `pr-flashinfer-2928` | upstream-code | [`sources/prs/flashinfer/PR-2928.md`](../sources/prs/flashinfer/PR-2928.md) | fix: clamp enable_pdl=True to False on SM < 90 to prevent PDL PTX on Ampere |
| `pr-flashinfer-3115` | upstream-code | [`sources/prs/flashinfer/PR-3115.md`](../sources/prs/flashinfer/PR-3115.md) | perf(autotuner): replace power-of-2 token buckets with hybrid spacing & fix missing routing_replay_out arg |
| `pr-flashinfer-3155` | upstream-code | [`sources/prs/flashinfer/PR-3155.md`](../sources/prs/flashinfer/PR-3155.md) | fix(gdn): use physical SM count for SM100 persistent prefill kernel |
| `pr-flashinfer-3203` | upstream-code | [`sources/prs/flashinfer/PR-3203.md`](../sources/prs/flashinfer/PR-3203.md) | Include TinyGEMM into BF16 autotuner |
| `pr-flashinfer-3216` | upstream-code | [`sources/prs/flashinfer/PR-3216.md`](../sources/prs/flashinfer/PR-3216.md) | fix(cute_dsl/moe): make autotuner bucket configuration adapt to runtime input |
| `pr-flashinfer-3227` | upstream-code | [`sources/prs/flashinfer/PR-3227.md`](../sources/prs/flashinfer/PR-3227.md) | [Bugfix] Fix fused MoE autotuning correctness issues by filtering clusterDimZ |
| `pr-flashinfer-3235` | upstream-code | [`sources/prs/flashinfer/PR-3235.md`](../sources/prs/flashinfer/PR-3235.md) | Support Kimi K2.5 H64 CuTe DSL MLA decode |
| `pr-flashinfer-3252` | upstream-code | [`sources/prs/flashinfer/PR-3252.md`](../sources/prs/flashinfer/PR-3252.md) | fix(cute_dsl/moe): unbias autotuner profiling for tile_size enumeration |
| `pr-flashinfer-3276` | upstream-code | [`sources/prs/flashinfer/PR-3276.md`](../sources/prs/flashinfer/PR-3276.md) | fix(fmha_v2): fix FP8 V-scratch pipeline and varlen scheduler on SM90 |
| `pr-quack-100` | upstream-code | [`sources/prs/quack/PR-100.md`](../sources/prs/quack/PR-100.md) | Autotune between tma gather and cp.async in SM100 |
| `pr-quack-104` | upstream-code | [`sources/prs/quack/PR-104.md`](../sources/prs/quack/PR-104.md) | Fix autotuner worker device affinity |
| `pr-sglang-18639` | upstream-code | [`sources/prs/sglang/PR-18639.md`](../sources/prs/sglang/PR-18639.md) | [sglang-miles] True on-policy training support for FSDP2 |
| `pr-sglang-18801` | upstream-code | [`sources/prs/sglang/PR-18801.md`](../sources/prs/sglang/PR-18801.md) | Support CuteDSL `mm_fp4` backend |
| `pr-sglang-21104` | upstream-code | [`sources/prs/sglang/PR-21104.md`](../sources/prs/sglang/PR-21104.md) | perf: precompute FA3 scheduler_metadata to eliminate per-layer prepare_varlen_num_blocks |
| `pr-sglang-23965` | upstream-code | [`sources/prs/sglang/PR-23965.md`](../sources/prs/sglang/PR-23965.md) | Enable PDL for various kernels in DSV32/GLM5 |
| `pr-sglang-24197` | upstream-code | [`sources/prs/sglang/PR-24197.md`](../sources/prs/sglang/PR-24197.md) | Refactor device timer, clean up metrics collector, and add fwd occupancy metric |
| `pr-sglang-24411` | upstream-code | [`sources/prs/sglang/PR-24411.md`](../sources/prs/sglang/PR-24411.md) | [diffusion] Fuse LTX2 split rotary embedding |
| `pr-sglang-24562` | upstream-code | [`sources/prs/sglang/PR-24562.md`](../sources/prs/sglang/PR-24562.md) | Fix performance regression on Deepseek V3 on `moe-runner-backend=triton` on SM90 |
| `pr-tensorrt-llm-10043` | upstream-code | [`sources/prs/tensorrt-llm/PR-10043.md`](../sources/prs/tensorrt-llm/PR-10043.md) | [TRTLLM-9992][perf] Enable PDL for CuteDSL kernels and overlap MoeOutputMemset |
| `pr-tensorrt-llm-10190` | upstream-code | [`sources/prs/tensorrt-llm/PR-10190.md`](../sources/prs/tensorrt-llm/PR-10190.md) | [None][feat] sm100 weight-only kernel |
| `pr-tensorrt-llm-10201` | upstream-code | [`sources/prs/tensorrt-llm/PR-10201.md`](../sources/prs/tensorrt-llm/PR-10201.md) | [TRTLLM-9831][perf] Enable 2CTA with autotune for CuteDSL MoE and Grouped GEMM optimizations |
| `pr-tensorrt-llm-10279` | upstream-code | [`sources/prs/tensorrt-llm/PR-10279.md`](../sources/prs/tensorrt-llm/PR-10279.md) | [TRTLLM-10147][perf] Balanced random MoE workload generator for CuteDSL kernel UT, autotuner and layerwise benchmark |
| `pr-tensorrt-llm-10339` | upstream-code | [`sources/prs/tensorrt-llm/PR-10339.md`](../sources/prs/tensorrt-llm/PR-10339.md) | [TRTLLM-9661][chore] Further reduce tuning time for cuteDSL nvFP4 dense gemm. |
| `pr-tensorrt-llm-11589` | upstream-code | [`sources/prs/tensorrt-llm/PR-11589.md`](../sources/prs/tensorrt-llm/PR-11589.md) | [TRTLLM-10004][feat] Enable GEMM -> AR with GEMM output in registered buffers |
| `pr-tensorrt-llm-11652` | upstream-code | [`sources/prs/tensorrt-llm/PR-11652.md`](../sources/prs/tensorrt-llm/PR-11652.md) | [None][feat] NVFP4 TRTLLM-Gen MoE for AutoDeploy (Nemotron Super) |
| `pr-tensorrt-llm-11900` | upstream-code | [`sources/prs/tensorrt-llm/PR-11900.md`](../sources/prs/tensorrt-llm/PR-11900.md) | [TRTLLM-10407][feat] Integrate CuTE DSL top-k kernel for Blackwell |
| `pr-tensorrt-llm-11990` | upstream-code | [`sources/prs/tensorrt-llm/PR-11990.md`](../sources/prs/tensorrt-llm/PR-11990.md) | [None][feat] GLM 5 support and DSA MTP fixes |
| `pr-tensorrt-llm-11993` | upstream-code | [`sources/prs/tensorrt-llm/PR-11993.md`](../sources/prs/tensorrt-llm/PR-11993.md) | [#11694][feat] AutoDeploy: Improve the piecewise CG memory usage |
| `pr-tensorrt-llm-12046` | upstream-code | [`sources/prs/tensorrt-llm/PR-12046.md`](../sources/prs/tensorrt-llm/PR-12046.md) | [https://nvbugs/5955188][fix] Fix harmony parsers and WAR routing PDL for agentic coding use cases |
| `pr-tensorrt-llm-12074` | upstream-code | [`sources/prs/tensorrt-llm/PR-12074.md`](../sources/prs/tensorrt-llm/PR-12074.md) | [TRTLLM-11289][feat] Integrate CuteDSL's bf16 dense GEMMs |
| `pr-tensorrt-llm-12236` | upstream-code | [`sources/prs/tensorrt-llm/PR-12236.md`](../sources/prs/tensorrt-llm/PR-12236.md) | [TRTLLM-10407][perf] Enable CuteDSL indexer_top_k in model |
| `pr-tensorrt-llm-12385` | upstream-code | [`sources/prs/tensorrt-llm/PR-12385.md`](../sources/prs/tensorrt-llm/PR-12385.md) | [None][feat] Temporally-Correlated Heuristic-guided Indexer TopK for Sparse Attention |
| `pr-tensorrt-llm-12503` | upstream-code | [`sources/prs/tensorrt-llm/PR-12503.md`](../sources/prs/tensorrt-llm/PR-12503.md) | [https://nvbugs/5983390][perf] Split MLA DSA custom op for piecewise CUDA graph capture |
| `pr-tensorrt-llm-12506` | upstream-code | [`sources/prs/tensorrt-llm/PR-12506.md`](../sources/prs/tensorrt-llm/PR-12506.md) | [None][feat] Add PDL support to CuTE DSL top-k kernels |
| `pr-tensorrt-llm-12612` | upstream-code | [`sources/prs/tensorrt-llm/PR-12612.md`](../sources/prs/tensorrt-llm/PR-12612.md) | [None][feat] Trtllm-gen FMHA JIT support |
| `pr-tensorrt-llm-12738` | upstream-code | [`sources/prs/tensorrt-llm/PR-12738.md`](../sources/prs/tensorrt-llm/PR-12738.md) | [None][feat] Add bf16 trtllm-gen moe support through flashinfer. |
| `pr-tensorrt-llm-13219` | upstream-code | [`sources/prs/tensorrt-llm/PR-13219.md`](../sources/prs/tensorrt-llm/PR-13219.md) | [TRTLLM-34871][feat] Add cute dsl FP8 paged MQA logits decode kernel |
| `pr-tensorrt-llm-13340` | upstream-code | [`sources/prs/tensorrt-llm/PR-13340.md`](../sources/prs/tensorrt-llm/PR-13340.md) | [None][feat] Integrate FP4 indexer for DSA on Blackwell |
| `pr-tensorrt-llm-13477` | upstream-code | [`sources/prs/tensorrt-llm/PR-13477.md`](../sources/prs/tensorrt-llm/PR-13477.md) | [None][perf] Scheme X L2-aware dispatcher and PDL launchers for sparse-attention GVR Top-K |
| `pr-tensorrt-llm-13570` | upstream-code | [`sources/prs/tensorrt-llm/PR-13570.md`](../sources/prs/tensorrt-llm/PR-13570.md) | [TRTLLM-12128][feat] enable SageAttention for Wan/FLUX (new commits) |
| `pr-tensorrt-llm-13658` | upstream-code | [`sources/prs/tensorrt-llm/PR-13658.md`](../sources/prs/tensorrt-llm/PR-13658.md) | [None][test] add Nemotron Ultra V3 AutoDeploy accuracy test |
| `pr-tensorrt-llm-13667` | upstream-code | [`sources/prs/tensorrt-llm/PR-13667.md`](../sources/prs/tensorrt-llm/PR-13667.md) | [None][perf] Improve TRTLLM MoE autotune in DEP |
| `pr-tensorrt-llm-13802` | upstream-code | [`sources/prs/tensorrt-llm/PR-13802.md`](../sources/prs/tensorrt-llm/PR-13802.md) | [None][fix] Use compressed lengths for DeepSeek-V4 indexer |
| `pr-tensorrt-llm-13873` | upstream-code | [`sources/prs/tensorrt-llm/PR-13873.md`](../sources/prs/tensorrt-llm/PR-13873.md) | [TRTLLM-12503][feat] Parallel VAE independent scaling and fix arg passing |
| `pr-tensorrt-llm-13971` | upstream-code | [`sources/prs/tensorrt-llm/PR-13971.md`](../sources/prs/tensorrt-llm/PR-13971.md) | [None][perf] Follow-up patch for "Improve TRTLLM MoE autotune in DEP (#13667)" |
| `pr-tensorrt-llm-13997` | upstream-code | [`sources/prs/tensorrt-llm/PR-13997.md`](../sources/prs/tensorrt-llm/PR-13997.md) | [None][feat] enable TRTLLM-Gen internal routing |
| `pr-tensorrt-llm-9087` | upstream-code | [`sources/prs/tensorrt-llm/PR-9087.md`](../sources/prs/tensorrt-llm/PR-9087.md) | [None][fix] support topk autotuner input for expert slot per group larger than 32 |
| `pr-tensorrt-llm-9486` | upstream-code | [`sources/prs/tensorrt-llm/PR-9486.md`](../sources/prs/tensorrt-llm/PR-9486.md) | [TRTLLM-8958][feat] and [TRTLLM-8960]: create ConfigurableMoE and support TRTLLMGenFusedMoE as backend |
| `pr-tilelang-1658` | upstream-code | [`sources/prs/tilelang/PR-1658.md`](../sources/prs/tilelang/PR-1658.md) | [Feat] profiler support cudagraph backend |
| `pr-tilelang-1667` | upstream-code | [`sources/prs/tilelang/PR-1667.md`](../sources/prs/tilelang/PR-1667.md) | [Feature] Support `cp.reduce.async.bulk.tensor` |
| `pr-tilelang-1717` | upstream-code | [`sources/prs/tilelang/PR-1717.md`](../sources/prs/tilelang/PR-1717.md) | [Enhancement] Add explicit global memory load/store intrinsics (ldg/stg 32/64/128) |
| `pr-tilelang-1874` | upstream-code | [`sources/prs/tilelang/PR-1874.md`](../sources/prs/tilelang/PR-1874.md) | [Feature] Support cluster launch, query, synchronization and barrier operations |
| `pr-tilelang-1906` | upstream-code | [`sources/prs/tilelang/PR-1906.md`](../sources/prs/tilelang/PR-1906.md) | [Enhancement] Add eager-mode support for tilelang.autotune |
| `pr-tilelang-1972` | upstream-code | [`sources/prs/tilelang/PR-1972.md`](../sources/prs/tilelang/PR-1972.md) | [Bugfix] Fix CuTeDSL autotune cache invalid ELF header (#1967) |
| `pr-tilelang-2024` | upstream-code | [`sources/prs/tilelang/PR-2024.md`](../sources/prs/tilelang/PR-2024.md) | Re-enable deprecated `TL_DISABLE_TMA_LOWER` pass config for TMA store |
| `pr-tilelang-2153` | upstream-code | [`sources/prs/tilelang/PR-2153.md`](../sources/prs/tilelang/PR-2153.md) | [codex] Split GEMM implementations by backend |
| `pr-tilelang-2159` | upstream-code | [`sources/prs/tilelang/PR-2159.md`](../sources/prs/tilelang/PR-2159.md) | [Autotune] Add pipeline, grouped compilation, and multi-GPU benchmark support |
| `pr-triton-10125` | upstream-code | [`sources/prs/triton/PR-10125.md`](../sources/prs/triton/PR-10125.md) | Add AutotuneListener hook to triton knobs |
| `pr-triton-10249` | upstream-code | [`sources/prs/triton/PR-10249.md`](../sources/prs/triton/PR-10249.md) | [triton_kernels] nvfp4 x nvfp4 tuning |
| `pr-triton-10295` | upstream-code | [`sources/prs/triton/PR-10295.md`](../sources/prs/triton/PR-10295.md) | [runtime] Skip None args in autotune restore_value/reset_to_zero hooks |
| `pr-vllm-34260` | upstream-code | [`sources/prs/vllm/PR-34260.md`](../sources/prs/vllm/PR-34260.md) | [Model Bash]: Improve FP8 Oracle for Config Specific Kernel Selection |
| `pr-vllm-39917` | upstream-code | [`sources/prs/vllm/PR-39917.md`](../sources/prs/vllm/PR-39917.md) | [Core] Replace routing replay with device cache and async D2H pipeline |
| `pr-vllm-40850` | upstream-code | [`sources/prs/vllm/PR-40850.md`](../sources/prs/vllm/PR-40850.md) | [Kernel][Helion] Optimize Helion config parsing latency |
| `pr-vllm-41189` | upstream-code | [`sources/prs/vllm/PR-41189.md`](../sources/prs/vllm/PR-41189.md) | [Bugfix] Fix persistent_topk cooperative deadlock at TopK=1024 |
| `pr-vllm-41665` | upstream-code | [`sources/prs/vllm/PR-41665.md`](../sources/prs/vllm/PR-41665.md) | [Bugfix] Fix condition to clear persistent topk so that it can be captured regardless |
| `pr-vllm-41745` | upstream-code | [`sources/prs/vllm/PR-41745.md`](../sources/prs/vllm/PR-41745.md) | [Spec Decode] Add Gemma4 MTP speculative decoding support |

<a id="cache-policy"></a>
## cache-policy

54 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `blog-amandeep-nvfp4` | community-note | [`sources/blogs/amandeep-nvfp4-attempts.md`](../sources/blogs/amandeep-nvfp4-attempts.md) | Twelve Attempts at NVFP4 Batched GEMV |
| `blog-yue-nvfp4` | community-note | [`sources/blogs/yue-nvfp4-hackathon.md`](../sources/blogs/yue-nvfp4-hackathon.md) | Blackwell NVFP4 Kernel Hackathon Journey |
| `contest-gpumode-p1` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-1-gemv.md`](../sources/contests/gpu-mode-nvfp4/problem-1-gemv.md) | GPU Mode NVFP4 Hackathon - Problem 1: Batched GEMV |
| `pr-cccl-cub-4618` | upstream-code | [`sources/prs/cccl-cub/PR-4618.md`](../sources/prs/cccl-cub/PR-4618.md) | Pass `cached_segment` by `span` |
| `pr-deepgemm-112` | upstream-code | [`sources/prs/deepgemm/PR-112.md`](../sources/prs/deepgemm/PR-112.md) | Add more GPU architectures support |
| `pr-deepgemm-74` | upstream-code | [`sources/prs/deepgemm/PR-74.md`](../sources/prs/deepgemm/PR-74.md) | Performance: Larger BlockTile optimizations enable 1470+ TF FP8 on the "H800"-SXM |
| `pr-deepgemm-81` | upstream-code | [`sources/prs/deepgemm/PR-81.md`](../sources/prs/deepgemm/PR-81.md) | Performance: BlockTile 256x128 optimizations enable 1500+ TF FP8 |
| `pr-flash-attention-1236` | upstream-code | [`sources/prs/flash-attention/PR-1236.md`](../sources/prs/flash-attention/PR-1236.md) | FA3 kvcache + split kv + gqa parallelization |
| `pr-flash-attention-1331` | upstream-code | [`sources/prs/flash-attention/PR-1331.md`](../sources/prs/flash-attention/PR-1331.md) | FA3 paged attention: Readiness for Cutlass 3.6 / default value for block_table |
| `pr-flash-attention-2218` | upstream-code | [`sources/prs/flash-attention/PR-2218.md`](../sources/prs/flash-attention/PR-2218.md) | [Ai-assisted] CLC work stealing |
| `pr-flash-attention-2298` | upstream-code | [`sources/prs/flash-attention/PR-2298.md`](../sources/prs/flash-attention/PR-2298.md) | [CuTe] Include broadcast dims in backward compile cache keys |
| `pr-flash-attention-2304` | upstream-code | [`sources/prs/flash-attention/PR-2304.md`](../sources/prs/flash-attention/PR-2304.md) | [Cute][Testing] Add persistent compile cache for cutedsl AOT compilation |
| `pr-flash-attention-2360` | upstream-code | [`sources/prs/flash-attention/PR-2360.md`](../sources/prs/flash-attention/PR-2360.md) | [Fwd,Sm90] Add paged KV attention support (tma and cp.async) |
| `pr-flash-attention-2370` | upstream-code | [`sources/prs/flash-attention/PR-2370.md`](../sources/prs/flash-attention/PR-2370.md) | [Cute, Testing] Bump cutedsl to 4.4.2 and remove prior aot cache management workarounds |
| `pr-flash-attention-2402` | upstream-code | [`sources/prs/flash-attention/PR-2402.md`](../sources/prs/flash-attention/PR-2402.md) | feat(cute): implement softcap backward pass, correct math formula, and resolve JIT cache bug |
| `pr-flashinfer-2799` | upstream-code | [`sources/prs/flashinfer/PR-2799.md`](../sources/prs/flashinfer/PR-2799.md) | [fmha-v2] Support HND and NHD paged KV cache layouts with conditional stride handling |
| `pr-flashinfer-2841` | upstream-code | [`sources/prs/flashinfer/PR-2841.md`](../sources/prs/flashinfer/PR-2841.md) | [Perf] Add FMHAv2 to flashinfer_benchmark.py and eliminate unnecessary H2D |
| `pr-flashinfer-2951` | upstream-code | [`sources/prs/flashinfer/PR-2951.md`](../sources/prs/flashinfer/PR-2951.md) | feat: Add DCP All-to-All kernel for context-parallel attention reduction |
| `pr-quack-29` | upstream-code | [`sources/prs/quack/PR-29.md`](../sources/prs/quack/PR-29.md) | Fix Symmetric Compile Cache |
| `pr-sglang-19148` | upstream-code | [`sources/prs/sglang/PR-19148.md`](../sources/prs/sglang/PR-19148.md) | [DeepSeek-V3.2][JIT-kernel] Support nsa fuse store indexer k cache |
| `pr-sglang-20479` | upstream-code | [`sources/prs/sglang/PR-20479.md`](../sources/prs/sglang/PR-20479.md) | Support Triton MLA FP8 KV cache |
| `pr-sglang-21104` | upstream-code | [`sources/prs/sglang/PR-21104.md`](../sources/prs/sglang/PR-21104.md) | perf: precompute FA3 scheduler_metadata to eliminate per-layer prepare_varlen_num_blocks |
| `pr-sglang-23965` | upstream-code | [`sources/prs/sglang/PR-23965.md`](../sources/prs/sglang/PR-23965.md) | Enable PDL for various kernels in DSV32/GLM5 |
| `pr-sglang-24925` | upstream-code | [`sources/prs/sglang/PR-24925.md`](../sources/prs/sglang/PR-24925.md) | [attn backend] Integrate tokenspeed_mla prefill/decode kernels (fp8 kv cache, blackwell) |
| `pr-tensorrt-llm-11273` | upstream-code | [`sources/prs/tensorrt-llm/PR-11273.md`](../sources/prs/tensorrt-llm/PR-11273.md) | [None][feat] Optimize super-v3 nvfp4 for better perf |
| `pr-tensorrt-llm-11990` | upstream-code | [`sources/prs/tensorrt-llm/PR-11990.md`](../sources/prs/tensorrt-llm/PR-11990.md) | [None][feat] GLM 5 support and DSA MTP fixes |
| `pr-tensorrt-llm-12062` | upstream-code | [`sources/prs/tensorrt-llm/PR-12062.md`](../sources/prs/tensorrt-llm/PR-12062.md) | [TRTLLM-11540][feat] Add EAGLE3 dynamic tree speculative decoding support |
| `pr-tensorrt-llm-12322` | upstream-code | [`sources/prs/tensorrt-llm/PR-12322.md`](../sources/prs/tensorrt-llm/PR-12322.md) | [https://nvbugs/5983390][perf] Kernel fusions in _gather_k_cache_for_chunk of Indexer in DSA |
| `pr-tensorrt-llm-12503` | upstream-code | [`sources/prs/tensorrt-llm/PR-12503.md`](../sources/prs/tensorrt-llm/PR-12503.md) | [https://nvbugs/5983390][perf] Split MLA DSA custom op for piecewise CUDA graph capture |
| `pr-tensorrt-llm-12519` | upstream-code | [`sources/prs/tensorrt-llm/PR-12519.md`](../sources/prs/tensorrt-llm/PR-12519.md) | [#12634][feat] AutoDeploy: Support rank 256 MLA in flashinfer_mla |
| `pr-tensorrt-llm-12537` | upstream-code | [`sources/prs/tensorrt-llm/PR-12537.md`](../sources/prs/tensorrt-llm/PR-12537.md) | [None][feat] Add Mamba2 MTP SSM cache CUDA kernel for tree-based speculative decoding |
| `pr-tensorrt-llm-12581` | upstream-code | [`sources/prs/tensorrt-llm/PR-12581.md`](../sources/prs/tensorrt-llm/PR-12581.md) | [https://nvbugs/5983390][perf] Multiple host perf optimizations for DSA part |
| `pr-tensorrt-llm-13169` | upstream-code | [`sources/prs/tensorrt-llm/PR-13169.md`](../sources/prs/tensorrt-llm/PR-13169.md) | [https://nvbugs/5945047][fix] Fix cluster launch enablement for SM120 GPUs in allReduce fusion |
| `pr-tensorrt-llm-13268` | upstream-code | [`sources/prs/tensorrt-llm/PR-13268.md`](../sources/prs/tensorrt-llm/PR-13268.md) | [https://nvbugs/6095953][fix] Fix cache memory estimation for Qwen3 hybrid models in trtllm-bench |
| `pr-tensorrt-llm-13340` | upstream-code | [`sources/prs/tensorrt-llm/PR-13340.md`](../sources/prs/tensorrt-llm/PR-13340.md) | [None][feat] Integrate FP4 indexer for DSA on Blackwell |
| `pr-tensorrt-llm-13652` | upstream-code | [`sources/prs/tensorrt-llm/PR-13652.md`](../sources/prs/tensorrt-llm/PR-13652.md) | [None][feat] Add DeepSeekV4 attention kernels |
| `pr-tensorrt-llm-13802` | upstream-code | [`sources/prs/tensorrt-llm/PR-13802.md`](../sources/prs/tensorrt-llm/PR-13802.md) | [None][fix] Use compressed lengths for DeepSeek-V4 indexer |
| `pr-tensorrt-llm-14070` | upstream-code | [`sources/prs/tensorrt-llm/PR-14070.md`](../sources/prs/tensorrt-llm/PR-14070.md) | [None][perf] Speed up model init: cache support_nvlink() |
| `pr-tensorrt-llm-4867` | upstream-code | [`sources/prs/tensorrt-llm/PR-4867.md`](../sources/prs/tensorrt-llm/PR-4867.md) | feat: Add w4a8_mxfp4_fp8 quantization recipe. |
| `pr-tensorrt-llm-6538` | upstream-code | [`sources/prs/tensorrt-llm/PR-6538.md`](../sources/prs/tensorrt-llm/PR-6538.md) | [None][feat] Use Separate QKV Input Layout for Context MLA |
| `pr-tensorrt-llm-8405` | upstream-code | [`sources/prs/tensorrt-llm/PR-8405.md`](../sources/prs/tensorrt-llm/PR-8405.md) | [TRTLLM-8535][feat] Support DeepSeek V3.2 with FP8 + BF16 KV cache/NVFP4 + BF16 KV cache |
| `pr-tilelang-1414` | upstream-code | [`sources/prs/tilelang/PR-1414.md`](../sources/prs/tilelang/PR-1414.md) | [Enhancement] Introduce `T.__ldg` |
| `pr-tilelang-1972` | upstream-code | [`sources/prs/tilelang/PR-1972.md`](../sources/prs/tilelang/PR-1972.md) | [Bugfix] Fix CuTeDSL autotune cache invalid ELF header (#1967) |
| `pr-tilelang-1982` | upstream-code | [`sources/prs/tilelang/PR-1982.md`](../sources/prs/tilelang/PR-1982.md) | [Enhancement] Use atomic directory rename for cache writes |
| `pr-vllm-37332` | upstream-code | [`sources/prs/vllm/PR-37332.md`](../sources/prs/vllm/PR-37332.md) | Add nvfp4 support to reshape_and_cache_flash |
| `pr-vllm-39306` | upstream-code | [`sources/prs/vllm/PR-39306.md`](../sources/prs/vllm/PR-39306.md) | Use CU_MEMCPY_SRC_ACCESS_ORDER_ANY for batch KV cache swaps |
| `pr-vllm-39917` | upstream-code | [`sources/prs/vllm/PR-39917.md`](../sources/prs/vllm/PR-39917.md) | [Core] Replace routing replay with device cache and async D2H pipeline |
| `pr-vllm-40045` | upstream-code | [`sources/prs/vllm/PR-40045.md`](../sources/prs/vllm/PR-40045.md) | [Attention] use diff kv backend for mimo v2 flash |
| `pr-vllm-40177` | upstream-code | [`sources/prs/vllm/PR-40177.md`](../sources/prs/vllm/PR-40177.md) | Add nvfp4 kv cache support |
| `pr-vllm-40392` | upstream-code | [`sources/prs/vllm/PR-40392.md`](../sources/prs/vllm/PR-40392.md) | [Performance][DSR1]: Fused RoPE+KVCache+q_concat for MLA |
| `pr-vllm-40850` | upstream-code | [`sources/prs/vllm/PR-40850.md`](../sources/prs/vllm/PR-40850.md) | [Kernel][Helion] Optimize Helion config parsing latency |
| `pr-vllm-40941` | upstream-code | [`sources/prs/vllm/PR-40941.md`](../sources/prs/vllm/PR-40941.md) | [Attention][TurboQuant] Share dequant buffers, eliminate float16_copy |
| `pr-vllm-41778` | upstream-code | [`sources/prs/vllm/PR-41778.md`](../sources/prs/vllm/PR-41778.md) | [MLA Attention Backend] Add TOKENSPEED_MLA backend for DSR1/Kimi K25 prefill + decode on Blackwell |
| `pr-vllm-42236` | upstream-code | [`sources/prs/vllm/PR-42236.md`](../sources/prs/vllm/PR-42236.md) | [DSv4] Improved dequant gather K cache kernel |

<a id="chunk-parallelism"></a>
## chunk-parallelism

1 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `contest-flashinfer-track-c` | contest-report | [`sources/contests/flashinfer-mlsys26/track-c-gated-delta-net.md`](../sources/contests/flashinfer-mlsys26/track-c-gated-delta-net.md) | FlashInfer MLSys 2026 - Track C: Gated Delta Net |

<a id="communication-overlap"></a>
## communication-overlap

1 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-deepgemm-304` | upstream-code | [`sources/prs/deepgemm/PR-304.md`](../sources/prs/deepgemm/PR-304.md) | [Public release 26/04] Introducing Mega MoE, FP4 Indexer and other features/fixes |

<a id="data-reuse"></a>
## data-reuse

2 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `blog-amandeep-nvfp4` | community-note | [`sources/blogs/amandeep-nvfp4-attempts.md`](../sources/blogs/amandeep-nvfp4-attempts.md) | Twelve Attempts at NVFP4 Batched GEMV |
| `contest-gpumode-p1` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-1-gemv.md`](../sources/contests/gpu-mode-nvfp4/problem-1-gemv.md) | GPU Mode NVFP4 Hackathon - Problem 1: Batched GEMV |

<a id="double-buffering"></a>
## double-buffering

5 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `blog-modular-blackwell` | community-note | [`sources/blogs/modular-blackwell-matmul.md`](../sources/blogs/modular-blackwell-matmul.md) | Modular: Matrix Multiplication on Blackwell |
| `pr-cutlass-2466` | upstream-code | [`sources/prs/cutlass/PR-2466.md`](../sources/prs/cutlass/PR-2466.md) | Example 77 add blackwell fmha bwd for MLA shape |
| `pr-cutlass-2472` | upstream-code | [`sources/prs/cutlass/PR-2472.md`](../sources/prs/cutlass/PR-2472.md) | Add Blackwell MLA forward (shape: d=192, dv=128) implementation |
| `pr-cutlass-2995` | upstream-code | [`sources/prs/cutlass/PR-2995.md`](../sources/prs/cutlass/PR-2995.md) | [CuTeDSL] Fix: SM100 block-scale gemm overlapping accumulator |
| `pr-flashinfer-2387` | upstream-code | [`sources/prs/flashinfer/PR-2387.md`](../sources/prs/flashinfer/PR-2387.md) | A Blackwell-optimized version of selective_state_update (mamba) |

<a id="epilogue-fusion"></a>
## epilogue-fusion

57 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `contest-gpumode-p3` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-3-gated-dual-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-3-gated-dual-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 3: Gated Dual GEMM |
| `pr-cutlass-1350` | upstream-code | [`sources/prs/cutlass/PR-1350.md`](../sources/prs/cutlass/PR-1350.md) | Add couple configs into generator.py for mixed input MM |
| `pr-cutlass-1661` | upstream-code | [`sources/prs/cutlass/PR-1661.md`](../sources/prs/cutlass/PR-1661.md) | Skip void-C kernels in the profiler when beta is non zero |
| `pr-cutlass-1753` | upstream-code | [`sources/prs/cutlass/PR-1753.md`](../sources/prs/cutlass/PR-1753.md) | Fix EVT for cutlass::gemm::kernel::DefaultGemmWithVisitor's behavior when constructing GemmUniversalAdapter |
| `pr-cutlass-1795` | upstream-code | [`sources/prs/cutlass/PR-1795.md`](../sources/prs/cutlass/PR-1795.md) | Support for TMA Epilogue for Group Gemm and add pingpong ptr array & Group Gemm |
| `pr-cutlass-1883` | upstream-code | [`sources/prs/cutlass/PR-1883.md`](../sources/prs/cutlass/PR-1883.md) | Improve sm90 mixed dtype kernel |
| `pr-cutlass-1932` | upstream-code | [`sources/prs/cutlass/PR-1932.md`](../sources/prs/cutlass/PR-1932.md) | Blockwise Scaling for FP8 |
| `pr-cutlass-2033` | upstream-code | [`sources/prs/cutlass/PR-2033.md`](../sources/prs/cutlass/PR-2033.md) | [EVT] Add support for Row/Col broadcast PtrArray |
| `pr-cutlass-2220` | upstream-code | [`sources/prs/cutlass/PR-2220.md`](../sources/prs/cutlass/PR-2220.md) | Set EpiTile correctly when TileN is not divisible by 32 |
| `pr-cutlass-2333` | upstream-code | [`sources/prs/cutlass/PR-2333.md`](../sources/prs/cutlass/PR-2333.md) | Fix epilogue::thread::Convert cannot be used with DefaultEpilogue |
| `pr-cutlass-2366` | upstream-code | [`sources/prs/cutlass/PR-2366.md`](../sources/prs/cutlass/PR-2366.md) | [ex77] fix mla split; add fwd lse; add bwd varlen |
| `pr-cutlass-2946` | upstream-code | [`sources/prs/cutlass/PR-2946.md`](../sources/prs/cutlass/PR-2946.md) | [Cutlass profiler] Fix SM100 FP8 nosmem epilogue shape_div “Divisibility Condition” for non‑multiple‑of‑64 N tiles |
| `pr-cutlass-2995` | upstream-code | [`sources/prs/cutlass/PR-2995.md`](../sources/prs/cutlass/PR-2995.md) | [CuTeDSL] Fix: SM100 block-scale gemm overlapping accumulator |
| `pr-cutlass-3184` | upstream-code | [`sources/prs/cutlass/PR-3184.md`](../sources/prs/cutlass/PR-3184.md) | Add Snake activation functor for EVT |
| `pr-deepgemm-198` | upstream-code | [`sources/prs/deepgemm/PR-198.md`](../sources/prs/deepgemm/PR-198.md) | Make various updates and fixes |
| `pr-flash-attention-1072` | upstream-code | [`sources/prs/flash-attention/PR-1072.md`](../sources/prs/flash-attention/PR-1072.md) | Add var-seq-len to FA3 fp16 / bf16 fwd |
| `pr-flash-attention-1100` | upstream-code | [`sources/prs/flash-attention/PR-1100.md`](../sources/prs/flash-attention/PR-1100.md) | Fp8 kernel with "in-kernel" transpose of V in producer |
| `pr-flash-attention-1182` | upstream-code | [`sources/prs/flash-attention/PR-1182.md`](../sources/prs/flash-attention/PR-1182.md) | Add seqused_q in fwd / bwd and seqused_k in bwd in hopper FA. |
| `pr-flash-attention-1236` | upstream-code | [`sources/prs/flash-attention/PR-1236.md`](../sources/prs/flash-attention/PR-1236.md) | FA3 kvcache + split kv + gqa parallelization |
| `pr-flash-attention-1604` | upstream-code | [`sources/prs/flash-attention/PR-1604.md`](../sources/prs/flash-attention/PR-1604.md) | Support hdimQK != hdimV backward |
| `pr-flash-attention-1723` | upstream-code | [`sources/prs/flash-attention/PR-1723.md`](../sources/prs/flash-attention/PR-1723.md) | Fix(hopper): Correct C++ syntax in epilogue_fwd.hpp |
| `pr-flash-attention-1893` | upstream-code | [`sources/prs/flash-attention/PR-1893.md`](../sources/prs/flash-attention/PR-1893.md) | Improve causal backward determinism perf with SPT schedule |
| `pr-flash-attention-2014` | upstream-code | [`sources/prs/flash-attention/PR-2014.md`](../sources/prs/flash-attention/PR-2014.md) | [Cute,Sm100,Fwd] use correction warps for epi when not using TMA |
| `pr-flash-attention-2497` | upstream-code | [`sources/prs/flash-attention/PR-2497.md`](../sources/prs/flash-attention/PR-2497.md) | [FA4][hd256] Backward TMA bulk-store epilogue + LSE/dpsum coalesce |
| `pr-flashinfer-1015` | upstream-code | [`sources/prs/flashinfer/PR-1015.md`](../sources/prs/flashinfer/PR-1015.md) | add multi-item scoring |
| `pr-flashinfer-1033` | upstream-code | [`sources/prs/flashinfer/PR-1033.md`](../sources/prs/flashinfer/PR-1033.md) | feat: add functional per-head FP8 quantization for FA3 |
| `pr-flashinfer-1039` | upstream-code | [`sources/prs/flashinfer/PR-1039.md`](../sources/prs/flashinfer/PR-1039.md) | [nvidia] initial support for blackwell kernels |
| `pr-flashinfer-1071` | upstream-code | [`sources/prs/flashinfer/PR-1071.md`](../sources/prs/flashinfer/PR-1071.md) | bugfix: adding lse output to blackwell fmha kernels |
| `pr-flashinfer-1106` | upstream-code | [`sources/prs/flashinfer/PR-1106.md`](../sources/prs/flashinfer/PR-1106.md) | bugfix: host-precomuted plan function for blackwell fmha |
| `pr-flashinfer-1113` | upstream-code | [`sources/prs/flashinfer/PR-1113.md`](../sources/prs/flashinfer/PR-1113.md) | Add CUTLASS fused moe kernels from TensorRT-LLM. |
| `pr-flashinfer-1114` | upstream-code | [`sources/prs/flashinfer/PR-1114.md`](../sources/prs/flashinfer/PR-1114.md) | bugfix: Fix test and output shape of fp4 quantize |
| `pr-flashinfer-1198` | upstream-code | [`sources/prs/flashinfer/PR-1198.md`](../sources/prs/flashinfer/PR-1198.md) | bugfix: fix blackwell fmha hanging issue for empty kv_len |
| `pr-flashinfer-1498` | upstream-code | [`sources/prs/flashinfer/PR-1498.md`](../sources/prs/flashinfer/PR-1498.md) | feat: scaling at fp4 gemm epilogue |
| `pr-flashinfer-1954` | upstream-code | [`sources/prs/flashinfer/PR-1954.md`](../sources/prs/flashinfer/PR-1954.md) | Feature: Support Relu2 activation in fused MoE |
| `pr-flashinfer-2020` | upstream-code | [`sources/prs/flashinfer/PR-2020.md`](../sources/prs/flashinfer/PR-2020.md) | update trtllm cutlass moe  |
| `pr-flashinfer-2111` | upstream-code | [`sources/prs/flashinfer/PR-2111.md`](../sources/prs/flashinfer/PR-2111.md) | refactor: update fa3 codebase and fix hopper unittest [part 1] |
| `pr-flashinfer-2142` | upstream-code | [`sources/prs/flashinfer/PR-2142.md`](../sources/prs/flashinfer/PR-2142.md) | feat: TRTLLM FMHAv2 backend for ctx attention |
| `pr-flashinfer-2446` | upstream-code | [`sources/prs/flashinfer/PR-2446.md`](../sources/prs/flashinfer/PR-2446.md) | feat: Add TRTLLM fmha_v2 library for SM90 attention with Skip-Softmax  |
| `pr-flashinfer-2805` | upstream-code | [`sources/prs/flashinfer/PR-2805.md`](../sources/prs/flashinfer/PR-2805.md) | [CuTe DSL] Add modular FMHA prefill and MLA decode attention kernels |
| `pr-flashinfer-2841` | upstream-code | [`sources/prs/flashinfer/PR-2841.md`](../sources/prs/flashinfer/PR-2841.md) | [Perf] Add FMHAv2 to flashinfer_benchmark.py and eliminate unnecessary H2D |
| `pr-flashinfer-2926` | upstream-code | [`sources/prs/flashinfer/PR-2926.md`](../sources/prs/flashinfer/PR-2926.md) | feat: add Relu2 (squared ReLU) activation support in CUTLASS MoE backend |
| `pr-flashinfer-2944` | upstream-code | [`sources/prs/flashinfer/PR-2944.md`](../sources/prs/flashinfer/PR-2944.md) | feat: Add CuTe DSL grouped-gemm + combine fusion support |
| `pr-flashinfer-765` | upstream-code | [`sources/prs/flashinfer/PR-765.md`](../sources/prs/flashinfer/PR-765.md) | feat: support deepseek prefill attention shape |
| `pr-flashinfer-869` | upstream-code | [`sources/prs/flashinfer/PR-869.md`](../sources/prs/flashinfer/PR-869.md) | Naive Support for Hopper FP8 Prefill Kernel with Per-Head Quantization |
| `pr-flashinfer-887` | upstream-code | [`sources/prs/flashinfer/PR-887.md`](../sources/prs/flashinfer/PR-887.md) | perf: FlashAttention-3 style MLA PageAttention |
| `pr-quack-118` | upstream-code | [`sources/prs/quack/PR-118.md`](../sources/prs/quack/PR-118.md) | Add remaining SM120 / RTX 50 support for GEMM epilogues and RMS paths |
| `pr-quack-35` | upstream-code | [`sources/prs/quack/PR-35.md`](../sources/prs/quack/PR-35.md) | Add optional epilogue args |
| `pr-quack-82` | upstream-code | [`sources/prs/quack/PR-82.md`](../sources/prs/quack/PR-82.md) | Add stochastic rounding support for GEMM epilogue |
| `pr-sglang-2752` | upstream-code | [`sources/prs/sglang/PR-2752.md`](../sources/prs/sglang/PR-2752.md) | Support cutlass Int8 gemm |
| `pr-sglang-3216` | upstream-code | [`sources/prs/sglang/PR-3216.md`](../sources/prs/sglang/PR-3216.md) | add tensorrt_llm common and cutlass_extensions as 3rdparty |
| `pr-tensorrt-llm-13945` | upstream-code | [`sources/prs/tensorrt-llm/PR-13945.md`](../sources/prs/tensorrt-llm/PR-13945.md) | [https://nvbugs/6100102][fix] Fix cutlass grouped gemm launcher EpilogueScalars construction |
| `pr-tensorrt-llm-6809` | upstream-code | [`sources/prs/tensorrt-llm/PR-6809.md`](../sources/prs/tensorrt-llm/PR-6809.md) | [OMNIML-2336][feat] Add NVFP4 x FP8 |
| `pr-tensorrt-llm-9838` | upstream-code | [`sources/prs/tensorrt-llm/PR-9838.md`](../sources/prs/tensorrt-llm/PR-9838.md) | [https://nvbugs/5726962][feat] Apply fusion for W4AFP8_AWQ MoE |
| `pr-vllm-10995` | upstream-code | [`sources/prs/vllm/PR-10995.md`](../sources/prs/vllm/PR-10995.md) | [Kernel]: Cutlass 2:4 Sparsity + FP8/Int8 Quant Support |
| `pr-vllm-13972` | upstream-code | [`sources/prs/vllm/PR-13972.md`](../sources/prs/vllm/PR-13972.md) | [Kernel] CUTLASS grouped gemm fp8 MoE kernel |
| `pr-vllm-20142` | upstream-code | [`sources/prs/vllm/PR-20142.md`](../sources/prs/vllm/PR-20142.md) | Replace `multiply_add` with `homogeneous_multiply_add` to Address Clang Template Parameter Issue |
| `pr-vllm-37503` | upstream-code | [`sources/prs/vllm/PR-37503.md`](../sources/prs/vllm/PR-37503.md) | [4/n] Migrate FP4/W4A8 CUTLASS kernels to torch stable ABI |

<a id="fine-grained-quantization"></a>
## fine-grained-quantization

222 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `contest-flashinfer-track-a` | contest-report | [`sources/contests/flashinfer-mlsys26/track-a-fused-moe.md`](../sources/contests/flashinfer-mlsys26/track-a-fused-moe.md) | FlashInfer MLSys 2026 - Track A: Fused MoE FP8 |
| `contest-flashinfer-track-b` | contest-report | [`sources/contests/flashinfer-mlsys26/track-b-sparse-attention.md`](../sources/contests/flashinfer-mlsys26/track-b-sparse-attention.md) | FlashInfer MLSys 2026 - Track B: DeepSeek V3.2 Sparse Attention |
| `pr-cutlass-1350` | upstream-code | [`sources/prs/cutlass/PR-1350.md`](../sources/prs/cutlass/PR-1350.md) | Add couple configs into generator.py for mixed input MM |
| `pr-cutlass-1753` | upstream-code | [`sources/prs/cutlass/PR-1753.md`](../sources/prs/cutlass/PR-1753.md) | Fix EVT for cutlass::gemm::kernel::DefaultGemmWithVisitor's behavior when constructing GemmUniversalAdapter |
| `pr-cutlass-1795` | upstream-code | [`sources/prs/cutlass/PR-1795.md`](../sources/prs/cutlass/PR-1795.md) | Support for TMA Epilogue for Group Gemm and add pingpong ptr array & Group Gemm |
| `pr-cutlass-1883` | upstream-code | [`sources/prs/cutlass/PR-1883.md`](../sources/prs/cutlass/PR-1883.md) | Improve sm90 mixed dtype kernel |
| `pr-cutlass-1932` | upstream-code | [`sources/prs/cutlass/PR-1932.md`](../sources/prs/cutlass/PR-1932.md) | Blockwise Scaling for FP8 |
| `pr-cutlass-2095` | upstream-code | [`sources/prs/cutlass/PR-2095.md`](../sources/prs/cutlass/PR-2095.md) | Improvements for: Groupwise scaling along M for FP8 gemm |
| `pr-cutlass-2123` | upstream-code | [`sources/prs/cutlass/PR-2123.md`](../sources/prs/cutlass/PR-2123.md) | Hopper Grouped GEMM support for FP8 Accum |
| `pr-cutlass-2139` | upstream-code | [`sources/prs/cutlass/PR-2139.md`](../sources/prs/cutlass/PR-2139.md) | Blockwise and Groupwise GEMM for Blackwell and Improvements for Hopper |
| `pr-cutlass-2256` | upstream-code | [`sources/prs/cutlass/PR-2256.md`](../sources/prs/cutlass/PR-2256.md) | Use cudaMemcpyAsync in gemm grouped with kRequiresPrecomputation sche… |
| `pr-cutlass-2270` | upstream-code | [`sources/prs/cutlass/PR-2270.md`](../sources/prs/cutlass/PR-2270.md) | hopper-blockwise-generalization-optimization |
| `pr-cutlass-2790` | upstream-code | [`sources/prs/cutlass/PR-2790.md`](../sources/prs/cutlass/PR-2790.md) | Blockscaled Ragged Contiguous Grouped Gemm for MoEs |
| `pr-cutlass-3055` | upstream-code | [`sources/prs/cutlass/PR-3055.md`](../sources/prs/cutlass/PR-3055.md) | Replace std::min with cute::min in sm120 blockwise scaling device functions |
| `pr-cutlass-3092` | upstream-code | [`sources/prs/cutlass/PR-3092.md`](../sources/prs/cutlass/PR-3092.md) | Support for Group GEMM in CUTLASS Profiler for GeForce and Spark |
| `pr-cutlass-3176` | upstream-code | [`sources/prs/cutlass/PR-3176.md`](../sources/prs/cutlass/PR-3176.md) | Small Tile N BlockScaled GEMM + Grouped GEMM on SM12x |
| `pr-deepgemm-103` | upstream-code | [`sources/prs/deepgemm/PR-103.md`](../sources/prs/deepgemm/PR-103.md) | Grouped GEMM skip useless computation for unaligned Ms |
| `pr-deepgemm-112` | upstream-code | [`sources/prs/deepgemm/PR-112.md`](../sources/prs/deepgemm/PR-112.md) | Add more GPU architectures support |
| `pr-deepgemm-168` | upstream-code | [`sources/prs/deepgemm/PR-168.md`](../sources/prs/deepgemm/PR-168.md) | Fix performance issue of m-grouped contiguous GEMMs. |
| `pr-deepgemm-193` | upstream-code | [`sources/prs/deepgemm/PR-193.md`](../sources/prs/deepgemm/PR-193.md) | Fix multicast bug and optimize masked GEMM |
| `pr-deepgemm-198` | upstream-code | [`sources/prs/deepgemm/PR-198.md`](../sources/prs/deepgemm/PR-198.md) | Make various updates and fixes |
| `pr-deepgemm-227` | upstream-code | [`sources/prs/deepgemm/PR-227.md`](../sources/prs/deepgemm/PR-227.md) | Use larger MMA shape to optimize sm100_fp8_mqa_logits |
| `pr-deepgemm-233` | upstream-code | [`sources/prs/deepgemm/PR-233.md`](../sources/prs/deepgemm/PR-233.md) | support bf16 bias in deepgemm2 |
| `pr-deepgemm-270` | upstream-code | [`sources/prs/deepgemm/PR-270.md`](../sources/prs/deepgemm/PR-270.md) | fix: use SM90ArchSpec instead of SM100ArchSpec in sm90_bf16_k_grouped_gemm |
| `pr-deepgemm-304` | upstream-code | [`sources/prs/deepgemm/PR-304.md`](../sources/prs/deepgemm/PR-304.md) | [Public release 26/04] Introducing Mega MoE, FP4 Indexer and other features/fixes |
| `pr-deepgemm-316` | upstream-code | [`sources/prs/deepgemm/PR-316.md`](../sources/prs/deepgemm/PR-316.md) | Add various optimizations and Mega MoE benchmarks |
| `pr-deepgemm-328` | upstream-code | [`sources/prs/deepgemm/PR-328.md`](../sources/prs/deepgemm/PR-328.md) | Sync nv_dev with upstream #316 (Mega MoE optimizations & benchmarks) |
| `pr-deepgemm-42` | upstream-code | [`sources/prs/deepgemm/PR-42.md`](../sources/prs/deepgemm/PR-42.md) | Performance: reducing the percentage of FFMA interleaving yields a sight performance gain, roughly 0.5% |
| `pr-deepgemm-68` | upstream-code | [`sources/prs/deepgemm/PR-68.md`](../sources/prs/deepgemm/PR-68.md) | Correctly flush L2 (+performance impact & upcoming optimization fork) |
| `pr-deepgemm-74` | upstream-code | [`sources/prs/deepgemm/PR-74.md`](../sources/prs/deepgemm/PR-74.md) | Performance: Larger BlockTile optimizations enable 1470+ TF FP8 on the "H800"-SXM |
| `pr-deepgemm-78` | upstream-code | [`sources/prs/deepgemm/PR-78.md`](../sources/prs/deepgemm/PR-78.md) |  Solving bank conflict via padding and TMA 3D store |
| `pr-deepgemm-81` | upstream-code | [`sources/prs/deepgemm/PR-81.md`](../sources/prs/deepgemm/PR-81.md) | Performance: BlockTile 256x128 optimizations enable 1500+ TF FP8 |
| `pr-deepgemm-83` | upstream-code | [`sources/prs/deepgemm/PR-83.md`](../sources/prs/deepgemm/PR-83.md) | Use 1D TMA store instead of 3D |
| `pr-deepgemm-86` | upstream-code | [`sources/prs/deepgemm/PR-86.md`](../sources/prs/deepgemm/PR-86.md) | Use swizzling instead of padding |
| `pr-deepgemm-88` | upstream-code | [`sources/prs/deepgemm/PR-88.md`](../sources/prs/deepgemm/PR-88.md) | Support TMA multicast on B with m_grouped_gemm_contiguous. |
| `pr-deepgemm-95` | upstream-code | [`sources/prs/deepgemm/PR-95.md`](../sources/prs/deepgemm/PR-95.md) | Weight gradient kernels for dense and MoE models |
| `pr-flash-attention-1100` | upstream-code | [`sources/prs/flash-attention/PR-1100.md`](../sources/prs/flash-attention/PR-1100.md) | Fp8 kernel with "in-kernel" transpose of V in producer |
| `pr-flash-attention-1173` | upstream-code | [`sources/prs/flash-attention/PR-1173.md`](../sources/prs/flash-attention/PR-1173.md) | FA3 FP8 qkv descales + restore max offset for h128 causal + added sync for producer WG |
| `pr-flash-attention-2109` | upstream-code | [`sources/prs/flash-attention/PR-2109.md`](../sources/prs/flash-attention/PR-2109.md) | [Cute,Fwd,Sm100] fp8 e4m3 and e5m2 support |
| `pr-flashinfer-1548` | upstream-code | [`sources/prs/flashinfer/PR-1548.md`](../sources/prs/flashinfer/PR-1548.md) | perf: Enable SplitK and fix autotuner for trtllm fp4 fused moe |
| `pr-flashinfer-2534` | upstream-code | [`sources/prs/flashinfer/PR-2534.md`](../sources/prs/flashinfer/PR-2534.md) | fix: support fp32 logits for fp8_per_tensor and fp8_block |
| `pr-flashinfer-2557` | upstream-code | [`sources/prs/flashinfer/PR-2557.md`](../sources/prs/flashinfer/PR-2557.md) | [Bugfix][comm] Fix FP4 one-shot launch config instability in trtllm_allreduce_fusion |
| `pr-flashinfer-2711` | upstream-code | [`sources/prs/flashinfer/PR-2711.md`](../sources/prs/flashinfer/PR-2711.md) | feat: Add DiT-oriented kernels where Qk (Bmm1) type can be reinterpreted into Int8 or BFloat16 |
| `pr-flashinfer-2726` | upstream-code | [`sources/prs/flashinfer/PR-2726.md`](../sources/prs/flashinfer/PR-2726.md) | Added missing padding |
| `pr-flashinfer-2779` | upstream-code | [`sources/prs/flashinfer/PR-2779.md`](../sources/prs/flashinfer/PR-2779.md) | feat: FP8 output support for CUTLASS MLA paged attention |
| `pr-flashinfer-2870` | upstream-code | [`sources/prs/flashinfer/PR-2870.md`](../sources/prs/flashinfer/PR-2870.md) | fix: fix cute dsl swap_ab tactic failure |
| `pr-flashinfer-2914` | upstream-code | [`sources/prs/flashinfer/PR-2914.md`](../sources/prs/flashinfer/PR-2914.md) | feat: Add cuBLASLt backend for `mm_bf16` and enable multi-tactic autotuning for FP8/MXFP8 runners |
| `pr-flashinfer-2928` | upstream-code | [`sources/prs/flashinfer/PR-2928.md`](../sources/prs/flashinfer/PR-2928.md) | fix: clamp enable_pdl=True to False on SM < 90 to prevent PDL PTX on Ampere |
| `pr-flashinfer-2944` | upstream-code | [`sources/prs/flashinfer/PR-2944.md`](../sources/prs/flashinfer/PR-2944.md) | feat: Add CuTe DSL grouped-gemm + combine fusion support |
| `pr-flashinfer-3027` | upstream-code | [`sources/prs/flashinfer/PR-3027.md`](../sources/prs/flashinfer/PR-3027.md) | [feat] Trtllm-gen Per-token Nvfp4 MoE |
| `pr-flashinfer-3059` | upstream-code | [`sources/prs/flashinfer/PR-3059.md`](../sources/prs/flashinfer/PR-3059.md) | Support Allreduce + Norm + Per-token Group Fp8 Quant Fusion |
| `pr-flashinfer-3080` | upstream-code | [`sources/prs/flashinfer/PR-3080.md`](../sources/prs/flashinfer/PR-3080.md) | feat: Add b12x_fused_moe / B12xMoEWrapper SM120 APIs with micro kernel and ReLU2 |
| `pr-flashinfer-3084` | upstream-code | [`sources/prs/flashinfer/PR-3084.md`](../sources/prs/flashinfer/PR-3084.md) | perf: optimize MXFP4xBF16 & INT4xFP8 CUTLASS MoE backend for SM90 |
| `pr-flashinfer-3097` | upstream-code | [`sources/prs/flashinfer/PR-3097.md`](../sources/prs/flashinfer/PR-3097.md) | Support NVFP4 KV for prefill and batch attention kernels |
| `pr-flashinfer-3113` | upstream-code | [`sources/prs/flashinfer/PR-3113.md`](../sources/prs/flashinfer/PR-3113.md) | Fix: Extend b12x FP4 GEMM support to SM121 (GB10/DGX Spark) |
| `pr-flashinfer-3115` | upstream-code | [`sources/prs/flashinfer/PR-3115.md`](../sources/prs/flashinfer/PR-3115.md) | perf(autotuner): replace power-of-2 token buckets with hybrid spacing & fix missing routing_replay_out arg |
| `pr-flashinfer-3129` | upstream-code | [`sources/prs/flashinfer/PR-3129.md`](../sources/prs/flashinfer/PR-3129.md) | feat: Enable FP8 (E4M3/E5M2) in concat_mla_k for optimize long-context prefill performance and refactor type dispatch for BF16/FP16 |
| `pr-flashinfer-3151` | upstream-code | [`sources/prs/flashinfer/PR-3151.md`](../sources/prs/flashinfer/PR-3151.md) | perf: Add no-bias path for tinygemm_bf16 |
| `pr-flashinfer-3152` | upstream-code | [`sources/prs/flashinfer/PR-3152.md`](../sources/prs/flashinfer/PR-3152.md) | Integrate CUTLASS Small Tile N Blockscaled GEMMs/Grouped GEMMs for SM120 and SM121 |
| `pr-flashinfer-3157` | upstream-code | [`sources/prs/flashinfer/PR-3157.md`](../sources/prs/flashinfer/PR-3157.md) | feat: DiT layer norm fusions for WAN: flashinfer.diffusion_ops |
| `pr-flashinfer-3185` | upstream-code | [`sources/prs/flashinfer/PR-3185.md`](../sources/prs/flashinfer/PR-3185.md) | feat: enable glm5 router gemm |
| `pr-flashinfer-3203` | upstream-code | [`sources/prs/flashinfer/PR-3203.md`](../sources/prs/flashinfer/PR-3203.md) | Include TinyGEMM into BF16 autotuner |
| `pr-flashinfer-3227` | upstream-code | [`sources/prs/flashinfer/PR-3227.md`](../sources/prs/flashinfer/PR-3227.md) | [Bugfix] Fix fused MoE autotuning correctness issues by filtering clusterDimZ |
| `pr-flashinfer-3237` | upstream-code | [`sources/prs/flashinfer/PR-3237.md`](../sources/prs/flashinfer/PR-3237.md) | perf: optimize per-token nvfp4 quantization kernel. |
| `pr-flashinfer-3239` | upstream-code | [`sources/prs/flashinfer/PR-3239.md`](../sources/prs/flashinfer/PR-3239.md) | Update moe gemm |
| `pr-flashinfer-3271` | upstream-code | [`sources/prs/flashinfer/PR-3271.md`](../sources/prs/flashinfer/PR-3271.md) | feat(moe): add SM120 W4A16 b12x kernels |
| `pr-flashinfer-3276` | upstream-code | [`sources/prs/flashinfer/PR-3276.md`](../sources/prs/flashinfer/PR-3276.md) | fix(fmha_v2): fix FP8 V-scratch pipeline and varlen scheduler on SM90 |
| `pr-sglang-15471` | upstream-code | [`sources/prs/sglang/PR-15471.md`](../sources/prs/sglang/PR-15471.md) | [sgl-kernel][6/7]Support Expert Specialization Grouped GEMM |
| `pr-sglang-18639` | upstream-code | [`sources/prs/sglang/PR-18639.md`](../sources/prs/sglang/PR-18639.md) | [sglang-miles] True on-policy training support for FSDP2 |
| `pr-sglang-18750` | upstream-code | [`sources/prs/sglang/PR-18750.md`](../sources/prs/sglang/PR-18750.md) | fix(sgl-kernel): use >= 120 for SM12x CUDA kernel dispatch |
| `pr-sglang-18801` | upstream-code | [`sources/prs/sglang/PR-18801.md`](../sources/prs/sglang/PR-18801.md) | Support CuteDSL `mm_fp4` backend |
| `pr-sglang-19148` | upstream-code | [`sources/prs/sglang/PR-19148.md`](../sources/prs/sglang/PR-19148.md) | [DeepSeek-V3.2][JIT-kernel] Support nsa fuse store indexer k cache |
| `pr-sglang-19880` | upstream-code | [`sources/prs/sglang/PR-19880.md`](../sources/prs/sglang/PR-19880.md) | [JIT Kernel][Feature] Support JIT custom all reduce (rewrite as v2) |
| `pr-sglang-20047` | upstream-code | [`sources/prs/sglang/PR-20047.md`](../sources/prs/sglang/PR-20047.md) | fix: default FP4 GEMM backend to flashinfer_cudnn on SM120 (Blackwell) |
| `pr-sglang-21321` | upstream-code | [`sources/prs/sglang/PR-21321.md`](../sources/prs/sglang/PR-21321.md) | [Kernel] Support FlashInfer TRTLLM-Gen fused MoE for non-gated FP4 & FP8 (Nemotron) |
| `pr-sglang-21734` | upstream-code | [`sources/prs/sglang/PR-21734.md`](../sources/prs/sglang/PR-21734.md) | perf: optimize PCG inductor path for FP8 models |
| `pr-sglang-22717` | upstream-code | [`sources/prs/sglang/PR-22717.md`](../sources/prs/sglang/PR-22717.md) | [codex] Add flashinfer TRTLLM backend for diffusion NVFP4 |
| `pr-sglang-23590` | upstream-code | [`sources/prs/sglang/PR-23590.md`](../sources/prs/sglang/PR-23590.md) | Reland Cute-DSL FP4 dense GEMM |
| `pr-sglang-23686` | upstream-code | [`sources/prs/sglang/PR-23686.md`](../sources/prs/sglang/PR-23686.md) | Deepseek_v4 support w4(mxfp4)a16 on hopper |
| `pr-sglang-23745` | upstream-code | [`sources/prs/sglang/PR-23745.md`](../sources/prs/sglang/PR-23745.md) | Use Cute-DSL NVFP4 quantization kernels |
| `pr-sglang-23756` | upstream-code | [`sources/prs/sglang/PR-23756.md`](../sources/prs/sglang/PR-23756.md) | feat: port SGLANG_JIT_DEEPGEMM_FAST_WARMUP to deepseek_v4 branch |
| `pr-sglang-23965` | upstream-code | [`sources/prs/sglang/PR-23965.md`](../sources/prs/sglang/PR-23965.md) | Enable PDL for various kernels in DSV32/GLM5 |
| `pr-sglang-24048` | upstream-code | [`sources/prs/sglang/PR-24048.md`](../sources/prs/sglang/PR-24048.md) | [VLM] Optimize Gemma4 VLM with PCG and fuse RMSNorm + residual add + scalar |
| `pr-sglang-24197` | upstream-code | [`sources/prs/sglang/PR-24197.md`](../sources/prs/sglang/PR-24197.md) | Refactor device timer, clean up metrics collector, and add fwd occupancy metric |
| `pr-sglang-24490` | upstream-code | [`sources/prs/sglang/PR-24490.md`](../sources/prs/sglang/PR-24490.md) | Port MXFP4 Marlin MoE support to JIT kernel path |
| `pr-sglang-24696` | upstream-code | [`sources/prs/sglang/PR-24696.md`](../sources/prs/sglang/PR-24696.md) | [Gemma4] Optimize Gemm4 with fused Q/K/V RMSNorm + per-expert FP8 ckpt loader |
| `pr-sglang-24816` | upstream-code | [`sources/prs/sglang/PR-24816.md`](../sources/prs/sglang/PR-24816.md) | Add FlashInfer SM90 cutlass MXFP4 MoE backend (W4A16) for GPT-OSS + DeepSeek-V4 |
| `pr-sglang-24986` | upstream-code | [`sources/prs/sglang/PR-24986.md`](../sources/prs/sglang/PR-24986.md) | [rebase]Deepseek_v4 support w4(mxfp4)a16 on hopper |
| `pr-sglang-25107` | upstream-code | [`sources/prs/sglang/PR-25107.md`](../sources/prs/sglang/PR-25107.md) | perf(nvfp4): free unused source scales after weight processing |
| `pr-sglang-3056` | upstream-code | [`sources/prs/sglang/PR-3056.md`](../sources/prs/sglang/PR-3056.md) | feat: integrate bmm_fp8 kernel into sgl-kernel |
| `pr-sglang-3529` | upstream-code | [`sources/prs/sglang/PR-3529.md`](../sources/prs/sglang/PR-3529.md) | integrate blockwise fp8 kernel |
| `pr-sglang-4165` | upstream-code | [`sources/prs/sglang/PR-4165.md`](../sources/prs/sglang/PR-4165.md) | DeepGemm integrate to sgl-kernel |
| `pr-sglang-5432` | upstream-code | [`sources/prs/sglang/PR-5432.md`](../sources/prs/sglang/PR-5432.md) | [perf] introduce deep gemm group_gemm_masked as bmm |
| `pr-sglang-7627` | upstream-code | [`sources/prs/sglang/PR-7627.md`](../sources/prs/sglang/PR-7627.md) | Add dsv3 router gemm kernel |
| `pr-sglang-7630` | upstream-code | [`sources/prs/sglang/PR-7630.md`](../sources/prs/sglang/PR-7630.md) | Add dsv3 fused a gemm to sgl-kernel |
| `pr-tensorrt-llm-10042` | upstream-code | [`sources/prs/tensorrt-llm/PR-10042.md`](../sources/prs/tensorrt-llm/PR-10042.md) | [None][perf] Add more optimization options for MOE CuteDSL finalized kernel |
| `pr-tensorrt-llm-10043` | upstream-code | [`sources/prs/tensorrt-llm/PR-10043.md`](../sources/prs/tensorrt-llm/PR-10043.md) | [TRTLLM-9992][perf] Enable PDL for CuteDSL kernels and overlap MoeOutputMemset |
| `pr-tensorrt-llm-10088` | upstream-code | [`sources/prs/tensorrt-llm/PR-10088.md`](../sources/prs/tensorrt-llm/PR-10088.md) | [None][feat] CuteDSL MOE FC1 Enhancement |
| `pr-tensorrt-llm-10130` | upstream-code | [`sources/prs/tensorrt-llm/PR-10130.md`](../sources/prs/tensorrt-llm/PR-10130.md) | [TRTLLM-9457][feat] Add cute dsl fp8 gemm for Blackwell |
| `pr-tensorrt-llm-10190` | upstream-code | [`sources/prs/tensorrt-llm/PR-10190.md`](../sources/prs/tensorrt-llm/PR-10190.md) | [None][feat] sm100 weight-only kernel |
| `pr-tensorrt-llm-10201` | upstream-code | [`sources/prs/tensorrt-llm/PR-10201.md`](../sources/prs/tensorrt-llm/PR-10201.md) | [TRTLLM-9831][perf] Enable 2CTA with autotune for CuteDSL MoE and Grouped GEMM optimizations |
| `pr-tensorrt-llm-10226` | upstream-code | [`sources/prs/tensorrt-llm/PR-10226.md`](../sources/prs/tensorrt-llm/PR-10226.md) | [TRTLLM-9798][feat] Change to use new DeepGEMM MQA sm100 kernel for MTP-3 |
| `pr-tensorrt-llm-10327` | upstream-code | [`sources/prs/tensorrt-llm/PR-10327.md`](../sources/prs/tensorrt-llm/PR-10327.md) | [None][fix] impl fused triton kernel for e8m0 resmooth to reduce memory footprint |
| `pr-tensorrt-llm-10339` | upstream-code | [`sources/prs/tensorrt-llm/PR-10339.md`](../sources/prs/tensorrt-llm/PR-10339.md) | [TRTLLM-9661][chore] Further reduce tuning time for cuteDSL nvFP4 dense gemm. |
| `pr-tensorrt-llm-10429` | upstream-code | [`sources/prs/tensorrt-llm/PR-10429.md`](../sources/prs/tensorrt-llm/PR-10429.md) | [None] [feat] Add test script and raster M for gather fc1 kernel |
| `pr-tensorrt-llm-10479` | upstream-code | [`sources/prs/tensorrt-llm/PR-10479.md`](../sources/prs/tensorrt-llm/PR-10479.md) | [None] [feat] Add densegemm backend for MoE |
| `pr-tensorrt-llm-10532` | upstream-code | [`sources/prs/tensorrt-llm/PR-10532.md`](../sources/prs/tensorrt-llm/PR-10532.md) | [None][feat] MiniMax M2 support |
| `pr-tensorrt-llm-10987` | upstream-code | [`sources/prs/tensorrt-llm/PR-10987.md`](../sources/prs/tensorrt-llm/PR-10987.md) | [TRTLLM-9831][perf] Use TMA.RED to improve effective memory bandwidth |
| `pr-tensorrt-llm-11143` | upstream-code | [`sources/prs/tensorrt-llm/PR-11143.md`](../sources/prs/tensorrt-llm/PR-11143.md) | [None][feat] fuse shared to sparse experts in TRT-LLM Gen MoE |
| `pr-tensorrt-llm-11165` | upstream-code | [`sources/prs/tensorrt-llm/PR-11165.md`](../sources/prs/tensorrt-llm/PR-11165.md) | [https://nvbugs/5799917][fix] Recover from CUTLASS MoE doActivation perf regression for MXFP4/NVFP4 dtype |
| `pr-tensorrt-llm-11273` | upstream-code | [`sources/prs/tensorrt-llm/PR-11273.md`](../sources/prs/tensorrt-llm/PR-11273.md) | [None][feat] Optimize super-v3 nvfp4 for better perf |
| `pr-tensorrt-llm-11473` | upstream-code | [`sources/prs/tensorrt-llm/PR-11473.md`](../sources/prs/tensorrt-llm/PR-11473.md) | [None][feat] Optimize by fuse nvfp4_quant to layernorm_gated for mamba2_mixer |
| `pr-tensorrt-llm-11510` | upstream-code | [`sources/prs/tensorrt-llm/PR-11510.md`](../sources/prs/tensorrt-llm/PR-11510.md) | [None][feat] Add support for expert_number<=2048 and K<=32 |
| `pr-tensorrt-llm-11589` | upstream-code | [`sources/prs/tensorrt-llm/PR-11589.md`](../sources/prs/tensorrt-llm/PR-11589.md) | [TRTLLM-10004][feat] Enable GEMM -> AR with GEMM output in registered buffers |
| `pr-tensorrt-llm-11652` | upstream-code | [`sources/prs/tensorrt-llm/PR-11652.md`](../sources/prs/tensorrt-llm/PR-11652.md) | [None][feat] NVFP4 TRTLLM-Gen MoE for AutoDeploy (Nemotron Super) |
| `pr-tensorrt-llm-11718` | upstream-code | [`sources/prs/tensorrt-llm/PR-11718.md`](../sources/prs/tensorrt-llm/PR-11718.md) | [TRTLLM-11119][feat] Blackwell SageAttention, Integrate into AttentionOp API |
| `pr-tensorrt-llm-11733` | upstream-code | [`sources/prs/tensorrt-llm/PR-11733.md`](../sources/prs/tensorrt-llm/PR-11733.md) | [https://nvbugs/5799917][fix] Recover from CUTLASS MoE doActivation perf regression for MXFP4/NVFP4 dtype |
| `pr-tensorrt-llm-11769` | upstream-code | [`sources/prs/tensorrt-llm/PR-11769.md`](../sources/prs/tensorrt-llm/PR-11769.md) | [https://nvbugs/5885070][fix] fix deepeplowlatency with cutedsl moe backend |
| `pr-tensorrt-llm-11774` | upstream-code | [`sources/prs/tensorrt-llm/PR-11774.md`](../sources/prs/tensorrt-llm/PR-11774.md) | [None][fix] Fix SM120 issue for rms_norm with nvfp4_quant_fusion |
| `pr-tensorrt-llm-11897` | upstream-code | [`sources/prs/tensorrt-llm/PR-11897.md`](../sources/prs/tensorrt-llm/PR-11897.md) | [TRTLLM-10990][feat] Fuse SwiGLU and quant into shared expert |
| `pr-tensorrt-llm-11899` | upstream-code | [`sources/prs/tensorrt-llm/PR-11899.md`](../sources/prs/tensorrt-llm/PR-11899.md) | [TRTLLM-10421][perf] Add fused cat+fp8_quantize CUDA kernel for DSA indexer |
| `pr-tensorrt-llm-11990` | upstream-code | [`sources/prs/tensorrt-llm/PR-11990.md`](../sources/prs/tensorrt-llm/PR-11990.md) | [None][feat] GLM 5 support and DSA MTP fixes |
| `pr-tensorrt-llm-11993` | upstream-code | [`sources/prs/tensorrt-llm/PR-11993.md`](../sources/prs/tensorrt-llm/PR-11993.md) | [#11694][feat] AutoDeploy: Improve the piecewise CG memory usage |
| `pr-tensorrt-llm-12055` | upstream-code | [`sources/prs/tensorrt-llm/PR-12055.md`](../sources/prs/tensorrt-llm/PR-12055.md) | [TRTLLM-11285][feat] Fuse indexer wk + weights_proj into single GEMM in TF32 for DS-V3.2 |
| `pr-tensorrt-llm-12074` | upstream-code | [`sources/prs/tensorrt-llm/PR-12074.md`](../sources/prs/tensorrt-llm/PR-12074.md) | [TRTLLM-11289][feat] Integrate CuteDSL's bf16 dense GEMMs |
| `pr-tensorrt-llm-12079` | upstream-code | [`sources/prs/tensorrt-llm/PR-12079.md`](../sources/prs/tensorrt-llm/PR-12079.md) | [None][feat] CuteDSL MOE: Add raster along M/N support for blockscaled contiguous backbone kernel |
| `pr-tensorrt-llm-12136` | upstream-code | [`sources/prs/tensorrt-llm/PR-12136.md`](../sources/prs/tensorrt-llm/PR-12136.md) | [None][feat] Add DWDP (Distributed Weight Data Parallelism) support for MoE inference |
| `pr-tensorrt-llm-12320` | upstream-code | [`sources/prs/tensorrt-llm/PR-12320.md`](../sources/prs/tensorrt-llm/PR-12320.md) | [None][feat] Support update weight for nvfp4 |
| `pr-tensorrt-llm-12503` | upstream-code | [`sources/prs/tensorrt-llm/PR-12503.md`](../sources/prs/tensorrt-llm/PR-12503.md) | [https://nvbugs/5983390][perf] Split MLA DSA custom op for piecewise CUDA graph capture |
| `pr-tensorrt-llm-12507` | upstream-code | [`sources/prs/tensorrt-llm/PR-12507.md`](../sources/prs/tensorrt-llm/PR-12507.md) | [#4674][feat] optimize llama8B decode: trtllm silu_mul backend, quant+silu_mul, QKV passthrough to attention |
| `pr-tensorrt-llm-12738` | upstream-code | [`sources/prs/tensorrt-llm/PR-12738.md`](../sources/prs/tensorrt-llm/PR-12738.md) | [None][feat] Add bf16 trtllm-gen moe support through flashinfer. |
| `pr-tensorrt-llm-12884` | upstream-code | [`sources/prs/tensorrt-llm/PR-12884.md`](../sources/prs/tensorrt-llm/PR-12884.md) | [TRTLLM-11585][feat] Add CUTEDSL moe backend for nemotron-h |
| `pr-tensorrt-llm-12937` | upstream-code | [`sources/prs/tensorrt-llm/PR-12937.md`](../sources/prs/tensorrt-llm/PR-12937.md) | [TRTLLM-11485][feat] Feature rework: Add SageAttention refreshed kernels (attentionOp only) |
| `pr-tensorrt-llm-12946` | upstream-code | [`sources/prs/tensorrt-llm/PR-12946.md`](../sources/prs/tensorrt-llm/PR-12946.md) | [#12784][feat] AutoDeploy: Optimize DeepSeek-R1 model performance |
| `pr-tensorrt-llm-13033` | upstream-code | [`sources/prs/tensorrt-llm/PR-13033.md`](../sources/prs/tensorrt-llm/PR-13033.md) | [None][feat] Update rms_norm + fp4_qaunt kernel supporting more dim |
| `pr-tensorrt-llm-13117` | upstream-code | [`sources/prs/tensorrt-llm/PR-13117.md`](../sources/prs/tensorrt-llm/PR-13117.md) | [None][feat] Add FP4 residual quantization kernel without channel reo… |
| `pr-tensorrt-llm-13207` | upstream-code | [`sources/prs/tensorrt-llm/PR-13207.md`](../sources/prs/tensorrt-llm/PR-13207.md) | [None][fix] Propagate init_load_balancer to DeepGemmFusedMoE in create_moe_backend |
| `pr-tensorrt-llm-13219` | upstream-code | [`sources/prs/tensorrt-llm/PR-13219.md`](../sources/prs/tensorrt-llm/PR-13219.md) | [TRTLLM-34871][feat] Add cute dsl FP8 paged MQA logits decode kernel |
| `pr-tensorrt-llm-13340` | upstream-code | [`sources/prs/tensorrt-llm/PR-13340.md`](../sources/prs/tensorrt-llm/PR-13340.md) | [None][feat] Integrate FP4 indexer for DSA on Blackwell |
| `pr-tensorrt-llm-13452` | upstream-code | [`sources/prs/tensorrt-llm/PR-13452.md`](../sources/prs/tensorrt-llm/PR-13452.md) | [TRTLLM-11285][perf] Force enable TF32 tensor cores for DSA indexer fused GEMM |
| `pr-tensorrt-llm-13595` | upstream-code | [`sources/prs/tensorrt-llm/PR-13595.md`](../sources/prs/tensorrt-llm/PR-13595.md) | [None][feat] Enable EPLB for DeepSeek-V4 |
| `pr-tensorrt-llm-13628` | upstream-code | [`sources/prs/tensorrt-llm/PR-13628.md`](../sources/prs/tensorrt-llm/PR-13628.md) | [None][feat] Fuse FP8 1x128 quantize + UE8M0 scale pack on SM100 |
| `pr-tensorrt-llm-13740` | upstream-code | [`sources/prs/tensorrt-llm/PR-13740.md`](../sources/prs/tensorrt-llm/PR-13740.md) | [https://nvbugs/6108841][fix] add hidden_dim=6144 router GEMM instantiation for GLM-5 |
| `pr-tensorrt-llm-13767` | upstream-code | [`sources/prs/tensorrt-llm/PR-13767.md`](../sources/prs/tensorrt-llm/PR-13767.md) | [None][fix] Plumb swiglu_limit through DeepGEMM and TRTLLMGen FP8 fused MoE |
| `pr-tensorrt-llm-13873` | upstream-code | [`sources/prs/tensorrt-llm/PR-13873.md`](../sources/prs/tensorrt-llm/PR-13873.md) | [TRTLLM-12503][feat] Parallel VAE independent scaling and fix arg passing |
| `pr-tensorrt-llm-13929` | upstream-code | [`sources/prs/tensorrt-llm/PR-13929.md`](../sources/prs/tensorrt-llm/PR-13929.md) | [TRTLLM-35237][feat] Add cute dsl FP4 paged MQA logits decode kernel |
| `pr-tensorrt-llm-13938` | upstream-code | [`sources/prs/tensorrt-llm/PR-13938.md`](../sources/prs/tensorrt-llm/PR-13938.md) | [None][feat] Keep DSv4 o_a_proj as FP8, and port vLLM's fused_inv_rope_fp8_quant |
| `pr-tensorrt-llm-4867` | upstream-code | [`sources/prs/tensorrt-llm/PR-4867.md`](../sources/prs/tensorrt-llm/PR-4867.md) | feat: Add w4a8_mxfp4_fp8 quantization recipe. |
| `pr-tensorrt-llm-6809` | upstream-code | [`sources/prs/tensorrt-llm/PR-6809.md`](../sources/prs/tensorrt-llm/PR-6809.md) | [OMNIML-2336][feat] Add NVFP4 x FP8 |
| `pr-tensorrt-llm-7524` | upstream-code | [`sources/prs/tensorrt-llm/PR-7524.md`](../sources/prs/tensorrt-llm/PR-7524.md) | [None][chore] Fix kernel launch param and add TRTLLM MoE backend test |
| `pr-tensorrt-llm-7761` | upstream-code | [`sources/prs/tensorrt-llm/PR-7761.md`](../sources/prs/tensorrt-llm/PR-7761.md) | [TRTLLM-8637][feat] Optimize the routing kernel for DeepseekV3 (MoE CUTLASS backend); Add support for 384 experts (MoE TRTLLM backend) |
| `pr-tensorrt-llm-7937` | upstream-code | [`sources/prs/tensorrt-llm/PR-7937.md`](../sources/prs/tensorrt-llm/PR-7937.md) | [None][feat] GPT-OSS Sm120/Sm121 Support |
| `pr-tensorrt-llm-8405` | upstream-code | [`sources/prs/tensorrt-llm/PR-8405.md`](../sources/prs/tensorrt-llm/PR-8405.md) | [TRTLLM-8535][feat] Support DeepSeek V3.2 with FP8 + BF16 KV cache/NVFP4 + BF16 KV cache |
| `pr-tensorrt-llm-8501` | upstream-code | [`sources/prs/tensorrt-llm/PR-8501.md`](../sources/prs/tensorrt-llm/PR-8501.md) | [None][fix] Fix the performance issue of FP8 blockwise grouped GEMM when using attention DP |
| `pr-tensorrt-llm-8620` | upstream-code | [`sources/prs/tensorrt-llm/PR-8620.md`](../sources/prs/tensorrt-llm/PR-8620.md) | [None][feat] Enable nvfp4 cuda core for sm120 |
| `pr-tensorrt-llm-8886` | upstream-code | [`sources/prs/tensorrt-llm/PR-8886.md`](../sources/prs/tensorrt-llm/PR-8886.md) | [None][feat] Enable EPLB for trtllm-gen and cutlass backend |
| `pr-tensorrt-llm-9025` | upstream-code | [`sources/prs/tensorrt-llm/PR-9025.md`](../sources/prs/tensorrt-llm/PR-9025.md) | [None][feat] Update TRTLLM MoE cubins; reduce mxfp4 weight padding requirement; tighten TMA bound |
| `pr-tensorrt-llm-9175` | upstream-code | [`sources/prs/tensorrt-llm/PR-9175.md`](../sources/prs/tensorrt-llm/PR-9175.md) | [None][feat] TRT-LLM Gen MoE optimize DeepSeek Fp8 activation kernel |
| `pr-tensorrt-llm-9486` | upstream-code | [`sources/prs/tensorrt-llm/PR-9486.md`](../sources/prs/tensorrt-llm/PR-9486.md) | [TRTLLM-8958][feat] and [TRTLLM-8960]: create ConfigurableMoE and support TRTLLMGenFusedMoE as backend |
| `pr-tensorrt-llm-9618` | upstream-code | [`sources/prs/tensorrt-llm/PR-9618.md`](../sources/prs/tensorrt-llm/PR-9618.md) | [TRTLLM-9685] [feat] Add gather fc1 kernel by cuteDSL |
| `pr-tensorrt-llm-9729` | upstream-code | [`sources/prs/tensorrt-llm/PR-9729.md`](../sources/prs/tensorrt-llm/PR-9729.md) | [None][feat] add fp4 gemm + allreduce |
| `pr-tensorrt-llm-9838` | upstream-code | [`sources/prs/tensorrt-llm/PR-9838.md`](../sources/prs/tensorrt-llm/PR-9838.md) | [https://nvbugs/5726962][feat] Apply fusion for W4AFP8_AWQ MoE |
| `pr-tensorrt-llm-9854` | upstream-code | [`sources/prs/tensorrt-llm/PR-9854.md`](../sources/prs/tensorrt-llm/PR-9854.md) | [None][feat] Port fp4 quantization kernel optimization from FlashInfer |
| `pr-tensorrt-llm-9905` | upstream-code | [`sources/prs/tensorrt-llm/PR-9905.md`](../sources/prs/tensorrt-llm/PR-9905.md) | [None][feat] Adding torch ext API for FusedAddRMSNormQuant kernel |
| `pr-tilelang-1229` | upstream-code | [`sources/prs/tilelang/PR-1229.md`](../sources/prs/tilelang/PR-1229.md) | [WIP] support more dtypes for tcgen05 |
| `pr-tilelang-1327` | upstream-code | [`sources/prs/tilelang/PR-1327.md`](../sources/prs/tilelang/PR-1327.md) | [Enhancement] add more dtype and fix mma.ws for fp16 for tcgen05 |
| `pr-tilelang-1736` | upstream-code | [`sources/prs/tilelang/PR-1736.md`](../sources/prs/tilelang/PR-1736.md) | Add swizzle layout detection and automatic merging for layout conflicts |
| `pr-tilelang-1764` | upstream-code | [`sources/prs/tilelang/PR-1764.md`](../sources/prs/tilelang/PR-1764.md) | [Feature] Support tcgen5mma lowering for `.kind::i8` |
| `pr-tilelang-1866` | upstream-code | [`sources/prs/tilelang/PR-1866.md`](../sources/prs/tilelang/PR-1866.md) | [CUDA] Support tcgen5mma gemm ts |
| `pr-tilelang-1909` | upstream-code | [`sources/prs/tilelang/PR-1909.md`](../sources/prs/tilelang/PR-1909.md) | [Feature] Add Producer-Consumer Warp Specialization and T.tma_copy() API |
| `pr-tilelang-1945` | upstream-code | [`sources/prs/tilelang/PR-1945.md`](../sources/prs/tilelang/PR-1945.md) | [Feature] Block-scaled GEMM support for MXFP8 on Blackwell |
| `pr-tilelang-2013` | upstream-code | [`sources/prs/tilelang/PR-2013.md`](../sources/prs/tilelang/PR-2013.md) | [CI] Remove legacy dequantize gemm test |
| `pr-tilelang-2063` | upstream-code | [`sources/prs/tilelang/PR-2063.md`](../sources/prs/tilelang/PR-2063.md) | [CUDA] Support int4 `T.gemm` |
| `pr-tilelang-2073` | upstream-code | [`sources/prs/tilelang/PR-2073.md`](../sources/prs/tilelang/PR-2073.md) | [CUDA] Improve int4 GEMM lowering and packed codegen support |
| `pr-tilelang-2107` | upstream-code | [`sources/prs/tilelang/PR-2107.md`](../sources/prs/tilelang/PR-2107.md) | [TMA] Support FP4 TensorMap TMA copies |
| `pr-tilelang-2153` | upstream-code | [`sources/prs/tilelang/PR-2153.md`](../sources/prs/tilelang/PR-2153.md) | [codex] Split GEMM implementations by backend |
| `pr-vllm-10995` | upstream-code | [`sources/prs/vllm/PR-10995.md`](../sources/prs/vllm/PR-10995.md) | [Kernel]: Cutlass 2:4 Sparsity + FP8/Int8 Quant Support |
| `pr-vllm-12931` | upstream-code | [`sources/prs/vllm/PR-12931.md`](../sources/prs/vllm/PR-12931.md) | [Misc][Kernel]: Add GPTQAllSpark Quantization |
| `pr-vllm-13571` | upstream-code | [`sources/prs/vllm/PR-13571.md`](../sources/prs/vllm/PR-13571.md) | [NVIDIA] Support nvfp4 cutlass gemm |
| `pr-vllm-21556` | upstream-code | [`sources/prs/vllm/PR-21556.md`](../sources/prs/vllm/PR-21556.md) | [Kernel] Improve machete memory bound perf |
| `pr-vllm-23696` | upstream-code | [`sources/prs/vllm/PR-23696.md`](../sources/prs/vllm/PR-23696.md) | [Kernel][B200] `mxfp4` fused cutlass moe |
| `pr-vllm-27134` | upstream-code | [`sources/prs/vllm/PR-27134.md`](../sources/prs/vllm/PR-27134.md) | [Kernels] Enable FlashInfer FP8 Blockscale on SM90 (for TEP DSR1) |
| `pr-vllm-32619` | upstream-code | [`sources/prs/vllm/PR-32619.md`](../sources/prs/vllm/PR-32619.md) | [Perf] Create TMA-aligned input scale tensor for DeepGemm on Hopper |
| `pr-vllm-33255` | upstream-code | [`sources/prs/vllm/PR-33255.md`](../sources/prs/vllm/PR-33255.md) | [Bugfix] Fix quant RMS norm fusion for quantization with TMA-aligned scales |
| `pr-vllm-33568` | upstream-code | [`sources/prs/vllm/PR-33568.md`](../sources/prs/vllm/PR-33568.md) | [Perf] Disable clean_logits in deepgemm fp8_mqa_logits kernel |
| `pr-vllm-34260` | upstream-code | [`sources/prs/vllm/PR-34260.md`](../sources/prs/vllm/PR-34260.md) | [Model Bash]: Improve FP8 Oracle for Config Specific Kernel Selection |
| `pr-vllm-34389` | upstream-code | [`sources/prs/vllm/PR-34389.md`](../sources/prs/vllm/PR-34389.md) | [Custom Ops] Add functional + out variant for scaled_fp4_quant |
| `pr-vllm-34556` | upstream-code | [`sources/prs/vllm/PR-34556.md`](../sources/prs/vllm/PR-34556.md) | [Quantization] add humming quantization kernel |
| `pr-vllm-34758` | upstream-code | [`sources/prs/vllm/PR-34758.md`](../sources/prs/vllm/PR-34758.md) | [Model Bash] DeepSeek R1 BF16 Min Latency QKV A GEMM (0.5% E2E Speedup) |
| `pr-vllm-35271` | upstream-code | [`sources/prs/vllm/PR-35271.md`](../sources/prs/vllm/PR-35271.md) | [Feat] Add CUDA torch fallbacks for fp8_mqa_logits/fp8_paged_mqa_logits_torch function |
| `pr-vllm-35382` | upstream-code | [`sources/prs/vllm/PR-35382.md`](../sources/prs/vllm/PR-35382.md) | fix(mxfp4): return is_monolithic=False when LoRA is enabled for Triton backend |
| `pr-vllm-37332` | upstream-code | [`sources/prs/vllm/PR-37332.md`](../sources/prs/vllm/PR-37332.md) | Add nvfp4 support to reshape_and_cache_flash |
| `pr-vllm-37463` | upstream-code | [`sources/prs/vllm/PR-37463.md`](../sources/prs/vllm/PR-37463.md) | [Kernel] Add MXFP4 W4A4 CUTLASS MoE kernel for SM100 |
| `pr-vllm-37970` | upstream-code | [`sources/prs/vllm/PR-37970.md`](../sources/prs/vllm/PR-37970.md) | [Kernel] Optimize SM120 CUTLASS blockwise FP8 GEMM |
| `pr-vllm-38065` | upstream-code | [`sources/prs/vllm/PR-38065.md`](../sources/prs/vllm/PR-38065.md) | [Perf] FP8 FlashInfer Attn for ViT |
| `pr-vllm-38504` | upstream-code | [`sources/prs/vllm/PR-38504.md`](../sources/prs/vllm/PR-38504.md) | [Kernels][MoE] Fix legacy_routing to use bitmatrix-based routing path |
| `pr-vllm-38670` | upstream-code | [`sources/prs/vllm/PR-38670.md`](../sources/prs/vllm/PR-38670.md) | [Bugfix] Fix AWQ models batch invariance issues |
| `pr-vllm-39547` | upstream-code | [`sources/prs/vllm/PR-39547.md`](../sources/prs/vllm/PR-39547.md) | [Perf] Fuse Zero Initializer for FP8 DeepGemm Block Quant Kernel |
| `pr-vllm-40105` | upstream-code | [`sources/prs/vllm/PR-40105.md`](../sources/prs/vllm/PR-40105.md) | [Bugfix] Add Marlin kernel in block scaled mm kernel selection. |
| `pr-vllm-40177` | upstream-code | [`sources/prs/vllm/PR-40177.md`](../sources/prs/vllm/PR-40177.md) | Add nvfp4 kv cache support |
| `pr-vllm-40191` | upstream-code | [`sources/prs/vllm/PR-40191.md`](../sources/prs/vllm/PR-40191.md) | [Bugfix] Guard mxfp4_experts_quant bindings on ENABLE_NVFP4_SM100 |
| `pr-vllm-40273` | upstream-code | [`sources/prs/vllm/PR-40273.md`](../sources/prs/vllm/PR-40273.md) | Fix MoE backend selection for LoRA (unquantized MoE) |
| `pr-vllm-40408` | upstream-code | [`sources/prs/vllm/PR-40408.md`](../sources/prs/vllm/PR-40408.md) | [Perf] Batch invariance with Cutlass fp8 support, 28.9% E2E latency improvement |
| `pr-vllm-40574` | upstream-code | [`sources/prs/vllm/PR-40574.md`](../sources/prs/vllm/PR-40574.md) | [MoE] Move cutlass moe to fused_moe/experts/ |
| `pr-vllm-40850` | upstream-code | [`sources/prs/vllm/PR-40850.md`](../sources/prs/vllm/PR-40850.md) | [Kernel][Helion] Optimize Helion config parsing latency |
| `pr-vllm-40941` | upstream-code | [`sources/prs/vllm/PR-40941.md`](../sources/prs/vllm/PR-40941.md) | [Attention][TurboQuant] Share dequant buffers, eliminate float16_copy |
| `pr-vllm-40960` | upstream-code | [`sources/prs/vllm/PR-40960.md`](../sources/prs/vllm/PR-40960.md) | [DSV4] Add BF16 and MXFP8 A2A support for flashinfer a2a one sided |
| `pr-vllm-41050` | upstream-code | [`sources/prs/vllm/PR-41050.md`](../sources/prs/vllm/PR-41050.md) | [Kernel][MoE] Support GELU on TRT-LLM NvFP4 fused MoE for Gemma4 |
| `pr-vllm-41326` | upstream-code | [`sources/prs/vllm/PR-41326.md`](../sources/prs/vllm/PR-41326.md) | Faster per-token fp8 group quant packed kernel for blackwell |
| `pr-vllm-41428` | upstream-code | [`sources/prs/vllm/PR-41428.md`](../sources/prs/vllm/PR-41428.md) | [DSv4] Improved fused Indexer Q quant kernel |
| `pr-vllm-41566` | upstream-code | [`sources/prs/vllm/PR-41566.md`](../sources/prs/vllm/PR-41566.md) | [Quantization] Rework quantization_config to use QuantKey and allow for activation override |
| `pr-vllm-41664` | upstream-code | [`sources/prs/vllm/PR-41664.md`](../sources/prs/vllm/PR-41664.md) | [MXFP4] Support for linear layers + compressed-tensors integration |
| `pr-vllm-41745` | upstream-code | [`sources/prs/vllm/PR-41745.md`](../sources/prs/vllm/PR-41745.md) | [Spec Decode] Add Gemma4 MTP speculative decoding support |
| `pr-vllm-41868` | upstream-code | [`sources/prs/vllm/PR-41868.md`](../sources/prs/vllm/PR-41868.md) | [CUDA][CUTLASS] Enable cutlass scaled mm for non-compatible sizes  |
| `pr-vllm-41882` | upstream-code | [`sources/prs/vllm/PR-41882.md`](../sources/prs/vllm/PR-41882.md) | Add NVFP4 all-gather GEMM fusion for AsyncTP |
| `pr-vllm-41979` | upstream-code | [`sources/prs/vllm/PR-41979.md`](../sources/prs/vllm/PR-41979.md) | [MoE] Move various experts classes to fused_moe/experts/ |
| `pr-vllm-41986` | upstream-code | [`sources/prs/vllm/PR-41986.md`](../sources/prs/vllm/PR-41986.md) | [Bugfix] Add swiglu limits to deepgemm fp8 methods |
| `pr-vllm-42153` | upstream-code | [`sources/prs/vllm/PR-42153.md`](../sources/prs/vllm/PR-42153.md) | [Perf] Use 2D-grid to eliminate divmod in W8W8 group quant |
| `pr-vllm-42236` | upstream-code | [`sources/prs/vllm/PR-42236.md`](../sources/prs/vllm/PR-42236.md) | [DSv4] Improved dequant gather K cache kernel |
| `pr-vllm-7174` | upstream-code | [`sources/prs/vllm/PR-7174.md`](../sources/prs/vllm/PR-7174.md) | [Kernel] (1/N) Machete - Hopper Optimized Mixed Precision Linear Kernel  |
| `pr-vllm-7701` | upstream-code | [`sources/prs/vllm/PR-7701.md`](../sources/prs/vllm/PR-7701.md) | [Kernel] (2/N) Machete - Integrate into CompressedTensorsWNA16 and GPTQMarlin |
| `pr-vllm-9218` | upstream-code | [`sources/prs/vllm/PR-9218.md`](../sources/prs/vllm/PR-9218.md) | [Bugfix] Fix Machete unittests failing with `NotImplementedError` |

<a id="jit-compilation"></a>
## jit-compilation

1 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-sglang-4165` | upstream-code | [`sources/prs/sglang/PR-4165.md`](../sources/prs/sglang/PR-4165.md) | DeepGemm integrate to sgl-kernel |

<a id="kernel-fusion"></a>
## kernel-fusion

683 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `contest-flashinfer-track-a` | contest-report | [`sources/contests/flashinfer-mlsys26/track-a-fused-moe.md`](../sources/contests/flashinfer-mlsys26/track-a-fused-moe.md) | FlashInfer MLSys 2026 - Track A: Fused MoE FP8 |
| `contest-flashinfer-track-b` | contest-report | [`sources/contests/flashinfer-mlsys26/track-b-sparse-attention.md`](../sources/contests/flashinfer-mlsys26/track-b-sparse-attention.md) | FlashInfer MLSys 2026 - Track B: DeepSeek V3.2 Sparse Attention |
| `contest-flashinfer-track-c` | contest-report | [`sources/contests/flashinfer-mlsys26/track-c-gated-delta-net.md`](../sources/contests/flashinfer-mlsys26/track-c-gated-delta-net.md) | FlashInfer MLSys 2026 - Track C: Gated Delta Net |
| `contest-gpumode-p3` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-3-gated-dual-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-3-gated-dual-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 3: Gated Dual GEMM |
| `contest-gpumode-p4` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 4: Grouped GEMM |
| `pr-cutlass-1795` | upstream-code | [`sources/prs/cutlass/PR-1795.md`](../sources/prs/cutlass/PR-1795.md) | Support for TMA Epilogue for Group Gemm and add pingpong ptr array & Group Gemm |
| `pr-cutlass-2033` | upstream-code | [`sources/prs/cutlass/PR-2033.md`](../sources/prs/cutlass/PR-2033.md) | [EVT] Add support for Row/Col broadcast PtrArray |
| `pr-cutlass-2292` | upstream-code | [`sources/prs/cutlass/PR-2292.md`](../sources/prs/cutlass/PR-2292.md) | Handle get_masked_trip_count for small length in fmha example |
| `pr-cutlass-2366` | upstream-code | [`sources/prs/cutlass/PR-2366.md`](../sources/prs/cutlass/PR-2366.md) | [ex77] fix mla split; add fwd lse; add bwd varlen |
| `pr-cutlass-3176` | upstream-code | [`sources/prs/cutlass/PR-3176.md`](../sources/prs/cutlass/PR-3176.md) | Small Tile N BlockScaled GEMM + Grouped GEMM on SM12x |
| `pr-deepgemm-304` | upstream-code | [`sources/prs/deepgemm/PR-304.md`](../sources/prs/deepgemm/PR-304.md) | [Public release 26/04] Introducing Mega MoE, FP4 Indexer and other features/fixes |
| `pr-flashinfer-1039` | upstream-code | [`sources/prs/flashinfer/PR-1039.md`](../sources/prs/flashinfer/PR-1039.md) | [nvidia] initial support for blackwell kernels |
| `pr-flashinfer-1106` | upstream-code | [`sources/prs/flashinfer/PR-1106.md`](../sources/prs/flashinfer/PR-1106.md) | bugfix: host-precomuted plan function for blackwell fmha |
| `pr-flashinfer-1108` | upstream-code | [`sources/prs/flashinfer/PR-1108.md`](../sources/prs/flashinfer/PR-1108.md) | feat: add trtllm moe_allreduce_fusion |
| `pr-flashinfer-1113` | upstream-code | [`sources/prs/flashinfer/PR-1113.md`](../sources/prs/flashinfer/PR-1113.md) | Add CUTLASS fused moe kernels from TensorRT-LLM. |
| `pr-flashinfer-1114` | upstream-code | [`sources/prs/flashinfer/PR-1114.md`](../sources/prs/flashinfer/PR-1114.md) | bugfix: Fix test and output shape of fp4 quantize |
| `pr-flashinfer-1131` | upstream-code | [`sources/prs/flashinfer/PR-1131.md`](../sources/prs/flashinfer/PR-1131.md) | feat: add trtllm all-reduce fusion |
| `pr-flashinfer-1153` | upstream-code | [`sources/prs/flashinfer/PR-1153.md`](../sources/prs/flashinfer/PR-1153.md) | feat: Fused temperature online softmax kernel |
| `pr-flashinfer-1159` | upstream-code | [`sources/prs/flashinfer/PR-1159.md`](../sources/prs/flashinfer/PR-1159.md) | feat: add finalize_moe_allreduce from trtllm |
| `pr-flashinfer-1161` | upstream-code | [`sources/prs/flashinfer/PR-1161.md`](../sources/prs/flashinfer/PR-1161.md) | feat: update non-fused moe |
| `pr-flashinfer-1164` | upstream-code | [`sources/prs/flashinfer/PR-1164.md`](../sources/prs/flashinfer/PR-1164.md) | feat: enable and update all-reduce fused quantization |
| `pr-flashinfer-1170` | upstream-code | [`sources/prs/flashinfer/PR-1170.md`](../sources/prs/flashinfer/PR-1170.md) | feat: logits processor fustion rule for temperature softmax |
| `pr-flashinfer-1212` | upstream-code | [`sources/prs/flashinfer/PR-1212.md`](../sources/prs/flashinfer/PR-1212.md) | feat: trtllm-gen fp8 moe kernels |
| `pr-flashinfer-1214` | upstream-code | [`sources/prs/flashinfer/PR-1214.md`](../sources/prs/flashinfer/PR-1214.md) | Feature/sm100 low latency nvfp4 kernels |
| `pr-flashinfer-1240` | upstream-code | [`sources/prs/flashinfer/PR-1240.md`](../sources/prs/flashinfer/PR-1240.md) | Patch fp8 cubin availability |
| `pr-flashinfer-1249` | upstream-code | [`sources/prs/flashinfer/PR-1249.md`](../sources/prs/flashinfer/PR-1249.md) | Remove sm100+ requirment for trtllm allreduce kernels |
| `pr-flashinfer-1255` | upstream-code | [`sources/prs/flashinfer/PR-1255.md`](../sources/prs/flashinfer/PR-1255.md) | TRT-LLM's Multi-Node NVLink AR + fused RMSNorm kernel |
| `pr-flashinfer-1272` | upstream-code | [`sources/prs/flashinfer/PR-1272.md`](../sources/prs/flashinfer/PR-1272.md) | Add shuffle matrix flag |
| `pr-flashinfer-1284` | upstream-code | [`sources/prs/flashinfer/PR-1284.md`](../sources/prs/flashinfer/PR-1284.md) | Convert scale_factor from scalar to Tensor in trt_allreduce_fusion |
| `pr-flashinfer-1287` | upstream-code | [`sources/prs/flashinfer/PR-1287.md`](../sources/prs/flashinfer/PR-1287.md) | Bug fix: guard fp8 e8m0 and e2m1 compile  |
| `pr-flashinfer-1291` | upstream-code | [`sources/prs/flashinfer/PR-1291.md`](../sources/prs/flashinfer/PR-1291.md) | Remove FAST_BUILD FLAG for MOE |
| `pr-flashinfer-1294` | upstream-code | [`sources/prs/flashinfer/PR-1294.md`](../sources/prs/flashinfer/PR-1294.md) | Update cutlass fp4 moe kernels |
| `pr-flashinfer-1297` | upstream-code | [`sources/prs/flashinfer/PR-1297.md`](../sources/prs/flashinfer/PR-1297.md) | feat: Add weight layout option for trtllm-gen fused moe |
| `pr-flashinfer-1298` | upstream-code | [`sources/prs/flashinfer/PR-1298.md`](../sources/prs/flashinfer/PR-1298.md) | perfix: use lightweight API to query device property |
| `pr-flashinfer-1309` | upstream-code | [`sources/prs/flashinfer/PR-1309.md`](../sources/prs/flashinfer/PR-1309.md) | Refactor Fused Moe Module |
| `pr-flashinfer-1310` | upstream-code | [`sources/prs/flashinfer/PR-1310.md`](../sources/prs/flashinfer/PR-1310.md) | Support loading autotuned results from json for cutlass fp4 moe backends |
| `pr-flashinfer-1319` | upstream-code | [`sources/prs/flashinfer/PR-1319.md`](../sources/prs/flashinfer/PR-1319.md) | Make Fp8 MoE routing_bias optional |
| `pr-flashinfer-1328` | upstream-code | [`sources/prs/flashinfer/PR-1328.md`](../sources/prs/flashinfer/PR-1328.md) | refactor: Improved metainfo for trtllm-gen kernels |
| `pr-flashinfer-1339` | upstream-code | [`sources/prs/flashinfer/PR-1339.md`](../sources/prs/flashinfer/PR-1339.md) | feat: Fused rope fp8 quantize kernel for MLA |
| `pr-flashinfer-1355` | upstream-code | [`sources/prs/flashinfer/PR-1355.md`](../sources/prs/flashinfer/PR-1355.md) | feature: add fp4 mm using trtllm backend |
| `pr-flashinfer-1361` | upstream-code | [`sources/prs/flashinfer/PR-1361.md`](../sources/prs/flashinfer/PR-1361.md) | Update autotune results for the nvfp4 cutlass moe backends for v0.2.9 |
| `pr-flashinfer-1371` | upstream-code | [`sources/prs/flashinfer/PR-1371.md`](../sources/prs/flashinfer/PR-1371.md) | bugfix: fixed cutlass fused moe usage of FP4QuantizationSFLayout::SWIZZLED |
| `pr-flashinfer-1389` | upstream-code | [`sources/prs/flashinfer/PR-1389.md`](../sources/prs/flashinfer/PR-1389.md) | GPT-OSS Support: Add Blackwell MoE mxfp4 implementation from TRTLLM and Attention Sink |
| `pr-flashinfer-1396` | upstream-code | [`sources/prs/flashinfer/PR-1396.md`](../sources/prs/flashinfer/PR-1396.md) | gpt-oss: Add MXFP8 x MXFP4 CUTLASS MOE for SM100 and BF16 x MXFP4 CUTLASS for SM90 + SwigluBias Activation |
| `pr-flashinfer-1398` | upstream-code | [`sources/prs/flashinfer/PR-1398.md`](../sources/prs/flashinfer/PR-1398.md) | Fix trtllm moe launcher local_num_experts |
| `pr-flashinfer-1410` | upstream-code | [`sources/prs/flashinfer/PR-1410.md`](../sources/prs/flashinfer/PR-1410.md) | [bugfix] Fix compilation failure when compiling csrc/trtllm_moe_allreduce_fusion.cu |
| `pr-flashinfer-1412` | upstream-code | [`sources/prs/flashinfer/PR-1412.md`](../sources/prs/flashinfer/PR-1412.md) | Faster weight processing (moe nvfp4) |
| `pr-flashinfer-1428` | upstream-code | [`sources/prs/flashinfer/PR-1428.md`](../sources/prs/flashinfer/PR-1428.md) | Fix redundant kernels in moe |
| `pr-flashinfer-1446` | upstream-code | [`sources/prs/flashinfer/PR-1446.md`](../sources/prs/flashinfer/PR-1446.md) | Remove getEnvEnablePDL in favor of enable_pdl parameter |
| `pr-flashinfer-1469` | upstream-code | [`sources/prs/flashinfer/PR-1469.md`](../sources/prs/flashinfer/PR-1469.md) | bugfix: Verify num_experts greater or equal to local_experts + offset |
| `pr-flashinfer-1472` | upstream-code | [`sources/prs/flashinfer/PR-1472.md`](../sources/prs/flashinfer/PR-1472.md) | feat: Enable multiple fused-moe backends |
| `pr-flashinfer-1475` | upstream-code | [`sources/prs/flashinfer/PR-1475.md`](../sources/prs/flashinfer/PR-1475.md) | tuner: Trtllm-gen Fp4 MoE Autotunner |
| `pr-flashinfer-1480` | upstream-code | [`sources/prs/flashinfer/PR-1480.md`](../sources/prs/flashinfer/PR-1480.md) | fix missing enable_pdl argument in trtllm-gen fp4 moe |
| `pr-flashinfer-1490` | upstream-code | [`sources/prs/flashinfer/PR-1490.md`](../sources/prs/flashinfer/PR-1490.md) | feat: Support fp8 qkv, fp16/bf16 out MHA for trtllm-gen. |
| `pr-flashinfer-1507` | upstream-code | [`sources/prs/flashinfer/PR-1507.md`](../sources/prs/flashinfer/PR-1507.md) | update allreduce to match trtllm |
| `pr-flashinfer-1508` | upstream-code | [`sources/prs/flashinfer/PR-1508.md`](../sources/prs/flashinfer/PR-1508.md) | Support cuda<12.8 built for trtllm_allreduce_fusion. |
| `pr-flashinfer-1525` | upstream-code | [`sources/prs/flashinfer/PR-1525.md`](../sources/prs/flashinfer/PR-1525.md) | Add GeGLU support to trtllm-gen NVFP4 Fused MoE Kernel |
| `pr-flashinfer-1530` | upstream-code | [`sources/prs/flashinfer/PR-1530.md`](../sources/prs/flashinfer/PR-1530.md) | bugfix: Fix compile error for undefined swizzle enum. |
| `pr-flashinfer-1540` | upstream-code | [`sources/prs/flashinfer/PR-1540.md`](../sources/prs/flashinfer/PR-1540.md) | feat: Add fp8-qkv, fp16/bf16 output MHA |
| `pr-flashinfer-1545` | upstream-code | [`sources/prs/flashinfer/PR-1545.md`](../sources/prs/flashinfer/PR-1545.md) | fix trtllm_allreduce_fusion twoshot register problem. |
| `pr-flashinfer-1547` | upstream-code | [`sources/prs/flashinfer/PR-1547.md`](../sources/prs/flashinfer/PR-1547.md) | perf: replace cudaGetDeviceProperties with cudaDeviceGetAttribute |
| `pr-flashinfer-1565` | upstream-code | [`sources/prs/flashinfer/PR-1565.md`](../sources/prs/flashinfer/PR-1565.md) | fix: separate out fp4 lib into sm90 and sm100 versions, add oob checking in fused moe |
| `pr-flashinfer-1571` | upstream-code | [`sources/prs/flashinfer/PR-1571.md`](../sources/prs/flashinfer/PR-1571.md) | bugfix: fix cuda version guard macros |
| `pr-flashinfer-1573` | upstream-code | [`sources/prs/flashinfer/PR-1573.md`](../sources/prs/flashinfer/PR-1573.md) | update trtllm-gen fp4 autotuner and routing |
| `pr-flashinfer-1581` | upstream-code | [`sources/prs/flashinfer/PR-1581.md`](../sources/prs/flashinfer/PR-1581.md) | refactor: Expose calculate_tile_tokens_dim function |
| `pr-flashinfer-1582` | upstream-code | [`sources/prs/flashinfer/PR-1582.md`](../sources/prs/flashinfer/PR-1582.md) | bugfix: Fix arg passing to TORCH_CHECK and TORCH_WARN macros |
| `pr-flashinfer-1596` | upstream-code | [`sources/prs/flashinfer/PR-1596.md`](../sources/prs/flashinfer/PR-1596.md) | bugfix: fix fused-temperature softmax IMA issue |
| `pr-flashinfer-1608` | upstream-code | [`sources/prs/flashinfer/PR-1608.md`](../sources/prs/flashinfer/PR-1608.md) | feat: initial support for SM103, SM110, SM120, SM121 |
| `pr-flashinfer-1622` | upstream-code | [`sources/prs/flashinfer/PR-1622.md`](../sources/prs/flashinfer/PR-1622.md) | bugfix: collect all modules to aot |
| `pr-flashinfer-1695` | upstream-code | [`sources/prs/flashinfer/PR-1695.md`](../sources/prs/flashinfer/PR-1695.md) | [cute_dsl] add gemm + all reduce (two_shot)  |
| `pr-flashinfer-1696` | upstream-code | [`sources/prs/flashinfer/PR-1696.md`](../sources/prs/flashinfer/PR-1696.md) | Support Kimi-K2 for TRT: templatize number of experts |
| `pr-flashinfer-1710` | upstream-code | [`sources/prs/flashinfer/PR-1710.md`](../sources/prs/flashinfer/PR-1710.md) | test: skip the unsupported test cases for sm120/121 |
| `pr-flashinfer-1716` | upstream-code | [`sources/prs/flashinfer/PR-1716.md`](../sources/prs/flashinfer/PR-1716.md) | perf: Add tuning config for cutlass moe for a hardware |
| `pr-flashinfer-1723` | upstream-code | [`sources/prs/flashinfer/PR-1723.md`](../sources/prs/flashinfer/PR-1723.md) | Fix DeepSeek quality for TRTLLM fused MoE routing |
| `pr-flashinfer-1724` | upstream-code | [`sources/prs/flashinfer/PR-1724.md`](../sources/prs/flashinfer/PR-1724.md) | bugfix: partially fix tests/test_trtllm_gen_fused_moe.py unit test failure |
| `pr-flashinfer-1817` | upstream-code | [`sources/prs/flashinfer/PR-1817.md`](../sources/prs/flashinfer/PR-1817.md) | fix: fp4 moe on sm120 |
| `pr-flashinfer-1819` | upstream-code | [`sources/prs/flashinfer/PR-1819.md`](../sources/prs/flashinfer/PR-1819.md) | feat:enable fp8 blockscale moe for fused cultass for sm90 |
| `pr-flashinfer-1829` | upstream-code | [`sources/prs/flashinfer/PR-1829.md`](../sources/prs/flashinfer/PR-1829.md) | feat: trtrllm-gen global scaled FP8 GEMMs |
| `pr-flashinfer-1831` | upstream-code | [`sources/prs/flashinfer/PR-1831.md`](../sources/prs/flashinfer/PR-1831.md) | Update the routing for TRTLLMGEN to support kimi k2 and qwen |
| `pr-flashinfer-1882` | upstream-code | [`sources/prs/flashinfer/PR-1882.md`](../sources/prs/flashinfer/PR-1882.md) | feat: Add FP4 TRTLLM-Gen throughput MOE batched gemms |
| `pr-flashinfer-1924` | upstream-code | [`sources/prs/flashinfer/PR-1924.md`](../sources/prs/flashinfer/PR-1924.md) | MLA RoPE + quantization fused kernel: shape generalization for MHA / GQA |
| `pr-flashinfer-1927` | upstream-code | [`sources/prs/flashinfer/PR-1927.md`](../sources/prs/flashinfer/PR-1927.md) | silu_and_mul nvfp4 quanization fusion rework |
| `pr-flashinfer-1954` | upstream-code | [`sources/prs/flashinfer/PR-1954.md`](../sources/prs/flashinfer/PR-1954.md) | Feature: Support Relu2 activation in fused MoE |
| `pr-flashinfer-1955` | upstream-code | [`sources/prs/flashinfer/PR-1955.md`](../sources/prs/flashinfer/PR-1955.md) | Update trtllm-gen fused moe routing kernel and add more kernels |
| `pr-flashinfer-1961` | upstream-code | [`sources/prs/flashinfer/PR-1961.md`](../sources/prs/flashinfer/PR-1961.md) | Fix: Verify scales are not None for Cutlass FP8 FusedMoE |
| `pr-flashinfer-1973` | upstream-code | [`sources/prs/flashinfer/PR-1973.md`](../sources/prs/flashinfer/PR-1973.md) | Feature: Add support for L40 FusedMoE in cutlass path |
| `pr-flashinfer-1980` | upstream-code | [`sources/prs/flashinfer/PR-1980.md`](../sources/prs/flashinfer/PR-1980.md) | feat: autotune tile_tokens_dim in trtllm-gen MOE |
| `pr-flashinfer-1995` | upstream-code | [`sources/prs/flashinfer/PR-1995.md`](../sources/prs/flashinfer/PR-1995.md) | Bugfix: Change get() -> GetDLTensorPtr() in cutlass FusedMoE validations |
| `pr-flashinfer-2011` | upstream-code | [`sources/prs/flashinfer/PR-2011.md`](../sources/prs/flashinfer/PR-2011.md) | Feature: Support non-gated activation in cutlass fused MoE nvfp4 |
| `pr-flashinfer-2014` | upstream-code | [`sources/prs/flashinfer/PR-2014.md`](../sources/prs/flashinfer/PR-2014.md) | [feat] Refactor trtllmgen MOE and add Bf16 trtllmgen moe |
| `pr-flashinfer-2020` | upstream-code | [`sources/prs/flashinfer/PR-2020.md`](../sources/prs/flashinfer/PR-2020.md) | update trtllm cutlass moe  |
| `pr-flashinfer-2030` | upstream-code | [`sources/prs/flashinfer/PR-2030.md`](../sources/prs/flashinfer/PR-2030.md) | Enable renormalize(naive) routing for fp8 per-tensor |
| `pr-flashinfer-2037` | upstream-code | [`sources/prs/flashinfer/PR-2037.md`](../sources/prs/flashinfer/PR-2037.md) | feat: Add flashinfer.rope.rope_quantize_fp8_append_paged_kv_cache (fused RoPE + Q + KV cache, supports MLA/GQA/MHA)  |
| `pr-flashinfer-2049` | upstream-code | [`sources/prs/flashinfer/PR-2049.md`](../sources/prs/flashinfer/PR-2049.md) | [BUG] Fix trtllm-gen fp4 moe renormalize routing |
| `pr-flashinfer-2051` | upstream-code | [`sources/prs/flashinfer/PR-2051.md`](../sources/prs/flashinfer/PR-2051.md) | Add support for topkPacked input in block-level renormalize |
| `pr-flashinfer-2063` | upstream-code | [`sources/prs/flashinfer/PR-2063.md`](../sources/prs/flashinfer/PR-2063.md) | perf: TRT-LLM MoE Block-FP8 activation optimization |
| `pr-flashinfer-2082` | upstream-code | [`sources/prs/flashinfer/PR-2082.md`](../sources/prs/flashinfer/PR-2082.md) | Patch sm103 for 3xfp4 moe generation |
| `pr-flashinfer-2090` | upstream-code | [`sources/prs/flashinfer/PR-2090.md`](../sources/prs/flashinfer/PR-2090.md) | refactor: pass hopper deepgemm include directory through python |
| `pr-flashinfer-2092` | upstream-code | [`sources/prs/flashinfer/PR-2092.md`](../sources/prs/flashinfer/PR-2092.md) | perf: TRT-LLM Gen finalize kernel optimization |
| `pr-flashinfer-2099` | upstream-code | [`sources/prs/flashinfer/PR-2099.md`](../sources/prs/flashinfer/PR-2099.md) | [DSV3] Optimized routing kernels dsv3 |
| `pr-flashinfer-2130` | upstream-code | [`sources/prs/flashinfer/PR-2130.md`](../sources/prs/flashinfer/PR-2130.md) | A unified API for the MNNVL and single-node/multi-GPU AllReduce kernels. |
| `pr-flashinfer-2142` | upstream-code | [`sources/prs/flashinfer/PR-2142.md`](../sources/prs/flashinfer/PR-2142.md) | feat: TRTLLM FMHAv2 backend for ctx attention |
| `pr-flashinfer-2159` | upstream-code | [`sources/prs/flashinfer/PR-2159.md`](../sources/prs/flashinfer/PR-2159.md) | feat: MxInt4 x Bf16 TRT-LLM Gen MoE support |
| `pr-flashinfer-2165` | upstream-code | [`sources/prs/flashinfer/PR-2165.md`](../sources/prs/flashinfer/PR-2165.md) | Add data type check for deepseek fp4 moe |
| `pr-flashinfer-2181` | upstream-code | [`sources/prs/flashinfer/PR-2181.md`](../sources/prs/flashinfer/PR-2181.md) | Rename noauxtc to fused_topk_deepseek |
| `pr-flashinfer-2193` | upstream-code | [`sources/prs/flashinfer/PR-2193.md`](../sources/prs/flashinfer/PR-2193.md) | feat: unit-test and api change, w4a8 grouped-gemm fused MoE for SM90 |
| `pr-flashinfer-2215` | upstream-code | [`sources/prs/flashinfer/PR-2215.md`](../sources/prs/flashinfer/PR-2215.md) | feat: further optimize top-k and add fused top-k page construction kernels for DSA |
| `pr-flashinfer-2217` | upstream-code | [`sources/prs/flashinfer/PR-2217.md`](../sources/prs/flashinfer/PR-2217.md) | feat: Support unpadded output hidden size for trtllm_fp4_block_scale_moe |
| `pr-flashinfer-2233` | upstream-code | [`sources/prs/flashinfer/PR-2233.md`](../sources/prs/flashinfer/PR-2233.md) | feat: Fused RMSNorm + FP4 Quantization Kernels in CuTe-DSL |
| `pr-flashinfer-2234` | upstream-code | [`sources/prs/flashinfer/PR-2234.md`](../sources/prs/flashinfer/PR-2234.md) | fix: add DeepSeek routing for Bf16xBf16 and MxIntxBf16 TRT-LLM Gen MoE |
| `pr-flashinfer-2235` | upstream-code | [`sources/prs/flashinfer/PR-2235.md`](../sources/prs/flashinfer/PR-2235.md) | refactor: pull trtllm-gen batch-gemm/gemm headers from artifactory; update tma descriptor shape init |
| `pr-flashinfer-2243` | upstream-code | [`sources/prs/flashinfer/PR-2243.md`](../sources/prs/flashinfer/PR-2243.md) | feat: RMSNorm/Fused RMSNorm + FP8 Quantization kernels |
| `pr-flashinfer-2260` | upstream-code | [`sources/prs/flashinfer/PR-2260.md`](../sources/prs/flashinfer/PR-2260.md) | fix: Add global scale support and optional output allocation for RMSNorm+FP4Quant fusion kernels |
| `pr-flashinfer-2268` | upstream-code | [`sources/prs/flashinfer/PR-2268.md`](../sources/prs/flashinfer/PR-2268.md) | [performance]optimize for nvfp4 |
| `pr-flashinfer-2304` | upstream-code | [`sources/prs/flashinfer/PR-2304.md`](../sources/prs/flashinfer/PR-2304.md) | feat: Support Fused MoE non gated Relu2 NVFP4 & FP8 and support Nemotron |
| `pr-flashinfer-2330` | upstream-code | [`sources/prs/flashinfer/PR-2330.md`](../sources/prs/flashinfer/PR-2330.md) | feat: expose swizzled_input_sf parameter for CUTLASS fused MOE |
| `pr-flashinfer-2343` | upstream-code | [`sources/prs/flashinfer/PR-2343.md`](../sources/prs/flashinfer/PR-2343.md) | Optimize quantization function in large problem size |
| `pr-flashinfer-2398` | upstream-code | [`sources/prs/flashinfer/PR-2398.md`](../sources/prs/flashinfer/PR-2398.md) | feat: cuteDSL fp4 moe for better DSR1 performance. |
| `pr-flashinfer-2428` | upstream-code | [`sources/prs/flashinfer/PR-2428.md`](../sources/prs/flashinfer/PR-2428.md) | refactor: refactoring cuda code to cute-dsl (part 1) |
| `pr-flashinfer-2445` | upstream-code | [`sources/prs/flashinfer/PR-2445.md`](../sources/prs/flashinfer/PR-2445.md) | bugfix: fix stub generation directory in fused_moe module |
| `pr-flashinfer-2446` | upstream-code | [`sources/prs/flashinfer/PR-2446.md`](../sources/prs/flashinfer/PR-2446.md) | feat: Add TRTLLM fmha_v2 library for SM90 attention with Skip-Softmax  |
| `pr-flashinfer-2462` | upstream-code | [`sources/prs/flashinfer/PR-2462.md`](../sources/prs/flashinfer/PR-2462.md) | feat: Support Fused MoE non gated Relu2 NVFP4 & FP8 and support Nemotron, fixed |
| `pr-flashinfer-2505` | upstream-code | [`sources/prs/flashinfer/PR-2505.md`](../sources/prs/flashinfer/PR-2505.md) | Feat: Trtllm-gen MxFP8 MoE integration |
| `pr-flashinfer-2534` | upstream-code | [`sources/prs/flashinfer/PR-2534.md`](../sources/prs/flashinfer/PR-2534.md) | fix: support fp32 logits for fp8_per_tensor and fp8_block |
| `pr-flashinfer-2557` | upstream-code | [`sources/prs/flashinfer/PR-2557.md`](../sources/prs/flashinfer/PR-2557.md) | [Bugfix][comm] Fix FP4 one-shot launch config instability in trtllm_allreduce_fusion |
| `pr-flashinfer-2564` | upstream-code | [`sources/prs/flashinfer/PR-2564.md`](../sources/prs/flashinfer/PR-2564.md) | fix: W4A8 autotune crash in cutlass_fused_moe profiler workspace |
| `pr-flashinfer-2581` | upstream-code | [`sources/prs/flashinfer/PR-2581.md`](../sources/prs/flashinfer/PR-2581.md) | Implement `cutlass_fused_moe` mxfp8 |
| `pr-flashinfer-2629` | upstream-code | [`sources/prs/flashinfer/PR-2629.md`](../sources/prs/flashinfer/PR-2629.md) | fix: cute dsl nvfp4 moe routing index error |
| `pr-flashinfer-2631` | upstream-code | [`sources/prs/flashinfer/PR-2631.md`](../sources/prs/flashinfer/PR-2631.md) | fix: add SM121 support to SM120 version guards |
| `pr-flashinfer-2642` | upstream-code | [`sources/prs/flashinfer/PR-2642.md`](../sources/prs/flashinfer/PR-2642.md) | [fp8_blockwise]Fix int32 overflow in TRTLLM fused MoE activation kernel |
| `pr-flashinfer-2653` | upstream-code | [`sources/prs/flashinfer/PR-2653.md`](../sources/prs/flashinfer/PR-2653.md) | [feat] trtllm-gen mxfp8 gemm |
| `pr-flashinfer-2654` | upstream-code | [`sources/prs/flashinfer/PR-2654.md`](../sources/prs/flashinfer/PR-2654.md) | fix: Add fused MOE and GEMM AOT modules for SM121 |
| `pr-flashinfer-2707` | upstream-code | [`sources/prs/flashinfer/PR-2707.md`](../sources/prs/flashinfer/PR-2707.md) | feat: Add support for TRTLLM MXFP8 non-gated MoE with ReLU2 |
| `pr-flashinfer-2725` | upstream-code | [`sources/prs/flashinfer/PR-2725.md`](../sources/prs/flashinfer/PR-2725.md) | fix: Add SM120 (RTX Blackwell desktop) support for NVFP4 MoE kernels |
| `pr-flashinfer-2739` | upstream-code | [`sources/prs/flashinfer/PR-2739.md`](../sources/prs/flashinfer/PR-2739.md) | Support in-place update for `trtllm_fp8_block_scale_moe` |
| `pr-flashinfer-2740` | upstream-code | [`sources/prs/flashinfer/PR-2740.md`](../sources/prs/flashinfer/PR-2740.md) | misc: Update gemm/batched gemm cubins from trtllm-gen, gemm header refactor |
| `pr-flashinfer-2744` | upstream-code | [`sources/prs/flashinfer/PR-2744.md`](../sources/prs/flashinfer/PR-2744.md) | [feat] Add 2048 experts and 32 Top K  |
| `pr-flashinfer-2777` | upstream-code | [`sources/prs/flashinfer/PR-2777.md`](../sources/prs/flashinfer/PR-2777.md) | perf: Performance tune cute dsl RMSNorm variants |
| `pr-flashinfer-2792` | upstream-code | [`sources/prs/flashinfer/PR-2792.md`](../sources/prs/flashinfer/PR-2792.md) | feat: Support padding tokens with seqlen=0 for rope+quant+kv cache update fusion kernel |
| `pr-flashinfer-2799` | upstream-code | [`sources/prs/flashinfer/PR-2799.md`](../sources/prs/flashinfer/PR-2799.md) | [fmha-v2] Support HND and NHD paged KV cache layouts with conditional stride handling |
| `pr-flashinfer-2805` | upstream-code | [`sources/prs/flashinfer/PR-2805.md`](../sources/prs/flashinfer/PR-2805.md) | [CuTe DSL] Add modular FMHA prefill and MLA decode attention kernels |
| `pr-flashinfer-2811` | upstream-code | [`sources/prs/flashinfer/PR-2811.md`](../sources/prs/flashinfer/PR-2811.md) | CuteDSL MoE fix redundant output buffer zeroing |
| `pr-flashinfer-2821` | upstream-code | [`sources/prs/flashinfer/PR-2821.md`](../sources/prs/flashinfer/PR-2821.md) | fix: Autotuner _find_nearest_profile non-power-of-2 num_tokens, create launchers for all supported tileN in trtllm fused MoE |
| `pr-flashinfer-2853` | upstream-code | [`sources/prs/flashinfer/PR-2853.md`](../sources/prs/flashinfer/PR-2853.md) | fix: int32 overflow in `trtllm_fp4_block_scale_moe` causing "Unsupported hidden state scale shape" for EP32+ configs |
| `pr-flashinfer-2864` | upstream-code | [`sources/prs/flashinfer/PR-2864.md`](../sources/prs/flashinfer/PR-2864.md) | Add support for Relu2 in BF16 fused MoE |
| `pr-flashinfer-2882` | upstream-code | [`sources/prs/flashinfer/PR-2882.md`](../sources/prs/flashinfer/PR-2882.md) | Fix silent bug with FP8 per tensor non-gated MoE |
| `pr-flashinfer-2898` | upstream-code | [`sources/prs/flashinfer/PR-2898.md`](../sources/prs/flashinfer/PR-2898.md) | fix: snap weight_scale_vec_size to handle block_scale_interleave padding for SM120 |
| `pr-flashinfer-2913` | upstream-code | [`sources/prs/flashinfer/PR-2913.md`](../sources/prs/flashinfer/PR-2913.md) | [NVIDIA] fix(jit): enable GDC for CUTLASS fused MoE PDL — prevent random crashes on SM12x |
| `pr-flashinfer-2916` | upstream-code | [`sources/prs/flashinfer/PR-2916.md`](../sources/prs/flashinfer/PR-2916.md) | fix: Fix autotuner crash on meta-device tensor in trtllm_fp4_block_scale_routed_moe |
| `pr-flashinfer-2942` | upstream-code | [`sources/prs/flashinfer/PR-2942.md`](../sources/prs/flashinfer/PR-2942.md) | [Perf] Refactor MoE autotuning to set valid topk ids in routed MoE tuning |
| `pr-flashinfer-2944` | upstream-code | [`sources/prs/flashinfer/PR-2944.md`](../sources/prs/flashinfer/PR-2944.md) | feat: Add CuTe DSL grouped-gemm + combine fusion support |
| `pr-flashinfer-2965` | upstream-code | [`sources/prs/flashinfer/PR-2965.md`](../sources/prs/flashinfer/PR-2965.md) | Add flashinfer.fused_rmsnorm_silu() with native kernel backend |
| `pr-flashinfer-2966` | upstream-code | [`sources/prs/flashinfer/PR-2966.md`](../sources/prs/flashinfer/PR-2966.md) | Fused moe all-reduce routed scaling factor + quant support |
| `pr-flashinfer-2982` | upstream-code | [`sources/prs/flashinfer/PR-2982.md`](../sources/prs/flashinfer/PR-2982.md) | feat(comm): add MOE Finalize/Reduction patterns to unified allreduce_fusion API |
| `pr-flashinfer-2984` | upstream-code | [`sources/prs/flashinfer/PR-2984.md`](../sources/prs/flashinfer/PR-2984.md) | fix: restore SM120 CUTLASS MoE tile candidate removed by #2927 (test_trtllm_cutlass_fused_moe.py) |
| `pr-flashinfer-3007` | upstream-code | [`sources/prs/flashinfer/PR-3007.md`](../sources/prs/flashinfer/PR-3007.md) | fix: use sym_int64 for strides in rmsnorm CuTe DSL kernels to prevent int32 overflow |
| `pr-flashinfer-3014` | upstream-code | [`sources/prs/flashinfer/PR-3014.md`](../sources/prs/flashinfer/PR-3014.md) | perf: Optimize CUTLASS MoE helper kernels for small-batch decode workloads |
| `pr-flashinfer-3024` | upstream-code | [`sources/prs/flashinfer/PR-3024.md`](../sources/prs/flashinfer/PR-3024.md) | [feat] Add routing_replay_out support to MoE kernels and Python API |
| `pr-flashinfer-3025` | upstream-code | [`sources/prs/flashinfer/PR-3025.md`](../sources/prs/flashinfer/PR-3025.md) | Prevent MoE autotuner buffer overflow on large token buckets |
| `pr-flashinfer-3027` | upstream-code | [`sources/prs/flashinfer/PR-3027.md`](../sources/prs/flashinfer/PR-3027.md) | [feat] Trtllm-gen Per-token Nvfp4 MoE |
| `pr-flashinfer-3032` | upstream-code | [`sources/prs/flashinfer/PR-3032.md`](../sources/prs/flashinfer/PR-3032.md) | fused_moe: pre-filter SM89 tactics with zero occupancy on SM120 Blackwell (fix review feedback on #2764) |
| `pr-flashinfer-3059` | upstream-code | [`sources/prs/flashinfer/PR-3059.md`](../sources/prs/flashinfer/PR-3059.md) | Support Allreduce + Norm + Per-token Group Fp8 Quant Fusion |
| `pr-flashinfer-3066` | upstream-code | [`sources/prs/flashinfer/PR-3066.md`](../sources/prs/flashinfer/PR-3066.md) | feat: Add b12x CuTe DSL fused MoE for SM120 |
| `pr-flashinfer-3080` | upstream-code | [`sources/prs/flashinfer/PR-3080.md`](../sources/prs/flashinfer/PR-3080.md) | feat: Add b12x_fused_moe / B12xMoEWrapper SM120 APIs with micro kernel and ReLU2 |
| `pr-flashinfer-3084` | upstream-code | [`sources/prs/flashinfer/PR-3084.md`](../sources/prs/flashinfer/PR-3084.md) | perf: optimize MXFP4xBF16 & INT4xFP8 CUTLASS MoE backend for SM90 |
| `pr-flashinfer-3115` | upstream-code | [`sources/prs/flashinfer/PR-3115.md`](../sources/prs/flashinfer/PR-3115.md) | perf(autotuner): replace power-of-2 token buckets with hybrid spacing & fix missing routing_replay_out arg |
| `pr-flashinfer-3157` | upstream-code | [`sources/prs/flashinfer/PR-3157.md`](../sources/prs/flashinfer/PR-3157.md) | feat: DiT layer norm fusions for WAN: flashinfer.diffusion_ops |
| `pr-flashinfer-3185` | upstream-code | [`sources/prs/flashinfer/PR-3185.md`](../sources/prs/flashinfer/PR-3185.md) | feat: enable glm5 router gemm |
| `pr-flashinfer-3191` | upstream-code | [`sources/prs/flashinfer/PR-3191.md`](../sources/prs/flashinfer/PR-3191.md) | fix(sm12x): fix micro-kernel workspace sizing when routed_rows > num_local_experts |
| `pr-flashinfer-3193` | upstream-code | [`sources/prs/flashinfer/PR-3193.md`](../sources/prs/flashinfer/PR-3193.md) | perf(moe): optimize SM120 b12x MoE short decode |
| `pr-flashinfer-3216` | upstream-code | [`sources/prs/flashinfer/PR-3216.md`](../sources/prs/flashinfer/PR-3216.md) | fix(cute_dsl/moe): make autotuner bucket configuration adapt to runtime input |
| `pr-flashinfer-3227` | upstream-code | [`sources/prs/flashinfer/PR-3227.md`](../sources/prs/flashinfer/PR-3227.md) | [Bugfix] Fix fused MoE autotuning correctness issues by filtering clusterDimZ |
| `pr-flashinfer-3252` | upstream-code | [`sources/prs/flashinfer/PR-3252.md`](../sources/prs/flashinfer/PR-3252.md) | fix(cute_dsl/moe): unbias autotuner profiling for tile_size enumeration |
| `pr-flashinfer-3271` | upstream-code | [`sources/prs/flashinfer/PR-3271.md`](../sources/prs/flashinfer/PR-3271.md) | feat(moe): add SM120 W4A16 b12x kernels |
| `pr-flashinfer-718` | upstream-code | [`sources/prs/flashinfer/PR-718.md`](../sources/prs/flashinfer/PR-718.md) | bugfix: FusedAddRMSNorm kernels might require more than 48KB shared memory when d is large. |
| `pr-flashinfer-804` | upstream-code | [`sources/prs/flashinfer/PR-804.md`](../sources/prs/flashinfer/PR-804.md) | perf: memory efficient deepseek mla fused page-attention kernel |
| `pr-pytorch-150145` | upstream-code | [`sources/prs/pytorch/PR-150145.md`](../sources/prs/pytorch/PR-150145.md) | Dont exclude constant_pad_nd in prologue fusion |
| `pr-pytorch-176410` | upstream-code | [`sources/prs/pytorch/PR-176410.md`](../sources/prs/pytorch/PR-176410.md) | [Inductor] Reject non-contiguous subnode fusion in mix-order reduction. |
| `pr-quack-74` | upstream-code | [`sources/prs/quack/PR-74.md`](../sources/prs/quack/PR-74.md) | Fix gather fusion in SM100 |
| `pr-sglang-10275` | upstream-code | [`sources/prs/sglang/PR-10275.md`](../sources/prs/sglang/PR-10275.md) | Add support for bf16 x bf16 cutlass fused MoE |
| `pr-sglang-10426` | upstream-code | [`sources/prs/sglang/PR-10426.md`](../sources/prs/sglang/PR-10426.md) | Fix correction bias undefined behavior for nvfp4 models |
| `pr-sglang-10758` | upstream-code | [`sources/prs/sglang/PR-10758.md`](../sources/prs/sglang/PR-10758.md) | Fix MTP MoE weight loading with NVFP4 target model. |
| `pr-sglang-11081` | upstream-code | [`sources/prs/sglang/PR-11081.md`](../sources/prs/sglang/PR-11081.md) | Fix DSR1 accuracy for flashinfer_trtllm MoE with FP8 quantization |
| `pr-sglang-11611` | upstream-code | [`sources/prs/sglang/PR-11611.md`](../sources/prs/sglang/PR-11611.md) | Support shared experts overlap in cutlass moe |
| `pr-sglang-12078` | upstream-code | [`sources/prs/sglang/PR-12078.md`](../sources/prs/sglang/PR-12078.md) | [Ascend] qwen optimization |
| `pr-sglang-12543` | upstream-code | [`sources/prs/sglang/PR-12543.md`](../sources/prs/sglang/PR-12543.md) | Enable Flashinfer TRTLLM-GEN-MoE FP8 blockwise kernel for Qwen3-Next on Blackwell |
| `pr-sglang-12758` | upstream-code | [`sources/prs/sglang/PR-12758.md`](../sources/prs/sglang/PR-12758.md) | [Bugfix] Fix illegal memory access |
| `pr-sglang-12787` | upstream-code | [`sources/prs/sglang/PR-12787.md`](../sources/prs/sglang/PR-12787.md) | [Nvidia] Add trtllm mnnvl allreduce with unified flashinfer allreduce fusion api |
| `pr-sglang-12888` | upstream-code | [`sources/prs/sglang/PR-12888.md`](../sources/prs/sglang/PR-12888.md) | Apply moe_reduce_sum kernel for fused_marlin_moe |
| `pr-sglang-13158` | upstream-code | [`sources/prs/sglang/PR-13158.md`](../sources/prs/sglang/PR-13158.md) | [NPU]Optimization of `forward_npu` for `UnquantizedFusedMoEMethod` |
| `pr-sglang-13162` | upstream-code | [`sources/prs/sglang/PR-13162.md`](../sources/prs/sglang/PR-13162.md) | Fix nan in global scaling factor for large scale nvfp4 EP |
| `pr-sglang-13263` | upstream-code | [`sources/prs/sglang/PR-13263.md`](../sources/prs/sglang/PR-13263.md) | diffusion: enable fa4 for blackwell |
| `pr-sglang-13617` | upstream-code | [`sources/prs/sglang/PR-13617.md`](../sources/prs/sglang/PR-13617.md) | [ROCM] Optimized deepseek-r1 fp8 model with + triton_gemm_a8w8 + batch_gemm_a8w8 + fused set_mla_kv_buffer kernel |
| `pr-sglang-13747` | upstream-code | [`sources/prs/sglang/PR-13747.md`](../sources/prs/sglang/PR-13747.md) | [AMD] Support --enable-aiter-allreduce-fusion on AMD GPUs |
| `pr-sglang-13761` | upstream-code | [`sources/prs/sglang/PR-13761.md`](../sources/prs/sglang/PR-13761.md) | [Feat][NVFP4] Enable NVFP4 MoE for Qwen series models (eg. Qwen3-Next) #13761 |
| `pr-sglang-13794` | upstream-code | [`sources/prs/sglang/PR-13794.md`](../sources/prs/sglang/PR-13794.md) | Support fp4 fp8 non gated moe |
| `pr-sglang-13798` | upstream-code | [`sources/prs/sglang/PR-13798.md`](../sources/prs/sglang/PR-13798.md) | [NVIDIA] Enable TRTLLM BF16 MoE on Blackwell GPUs |
| `pr-sglang-13864` | upstream-code | [`sources/prs/sglang/PR-13864.md`](../sources/prs/sglang/PR-13864.md) | [BugFix] fix outplace_fused_experts missing is_gated |
| `pr-sglang-13873` | upstream-code | [`sources/prs/sglang/PR-13873.md`](../sources/prs/sglang/PR-13873.md) | Feat: GLM-4.6 supports shared experts fusion |
| `pr-sglang-13959` | upstream-code | [`sources/prs/sglang/PR-13959.md`](../sources/prs/sglang/PR-13959.md) | [DeepSeek v3.2] opt Context Parallelism: support fused moe, multi batch and fp8 kvcache |
| `pr-sglang-14105` | upstream-code | [`sources/prs/sglang/PR-14105.md`](../sources/prs/sglang/PR-14105.md) | [LoRA][III] Add LoRA support for MoE layers and enable TP |
| `pr-sglang-14122` | upstream-code | [`sources/prs/sglang/PR-14122.md`](../sources/prs/sglang/PR-14122.md) | Add new moe wna16 marlin gemm |
| `pr-sglang-14125` | upstream-code | [`sources/prs/sglang/PR-14125.md`](../sources/prs/sglang/PR-14125.md) | Apply new moe wna16 marlin gemm |
| `pr-sglang-14134` | upstream-code | [`sources/prs/sglang/PR-14134.md`](../sources/prs/sglang/PR-14134.md) | Apply new moe align block size kernel |
| `pr-sglang-14213` | upstream-code | [`sources/prs/sglang/PR-14213.md`](../sources/prs/sglang/PR-14213.md) | Add Mistral Large 3 support. |
| `pr-sglang-14350` | upstream-code | [`sources/prs/sglang/PR-14350.md`](../sources/prs/sglang/PR-14350.md) | [FIX] trtllm-moe-fp4-renorm for Qwen series models |
| `pr-sglang-14423` | upstream-code | [`sources/prs/sglang/PR-14423.md`](../sources/prs/sglang/PR-14423.md) | [NPU] perf update with kvcache nz & w4a8 quant |
| `pr-sglang-14717` | upstream-code | [`sources/prs/sglang/PR-14717.md`](../sources/prs/sglang/PR-14717.md) | [diffusion] kernel fusion: gated residual layernorm scale shift and layernorm scale shift kernel fusion for Qwen-Image, WAN and HunyuanVideo |
| `pr-sglang-14829` | upstream-code | [`sources/prs/sglang/PR-14829.md`](../sources/prs/sglang/PR-14829.md) | Apply back moe_sum_reduce for fused_marlin_moe |
| `pr-sglang-15049` | upstream-code | [`sources/prs/sglang/PR-15049.md`](../sources/prs/sglang/PR-15049.md) | Mistral Large 3 NVFP4 TRTLLM MoE support |
| `pr-sglang-15141` | upstream-code | [`sources/prs/sglang/PR-15141.md`](../sources/prs/sglang/PR-15141.md) | [sgl-kernel][1/2] Fused qk_norm_rope for GLM4.6 |
| `pr-sglang-15306` | upstream-code | [`sources/prs/sglang/PR-15306.md`](../sources/prs/sglang/PR-15306.md) | Fix warp illegal instruction in kimi k2 thinking PCG |
| `pr-sglang-15382` | upstream-code | [`sources/prs/sglang/PR-15382.md`](../sources/prs/sglang/PR-15382.md) | [diffusion] Add Sage Attention 3 Support for sm 120 (RTX5090) |
| `pr-sglang-15539` | upstream-code | [`sources/prs/sglang/PR-15539.md`](../sources/prs/sglang/PR-15539.md) | MoE: Skip SiLU/GELU activation for masked experts |
| `pr-sglang-15551` | upstream-code | [`sources/prs/sglang/PR-15551.md`](../sources/prs/sglang/PR-15551.md) | Update flashinfer to 0.6.1 |
| `pr-sglang-15712` | upstream-code | [`sources/prs/sglang/PR-15712.md`](../sources/prs/sglang/PR-15712.md) | Add SwapAB Optimization for triton fused_moe_kernel on SM90. |
| `pr-sglang-15835` | upstream-code | [`sources/prs/sglang/PR-15835.md`](../sources/prs/sglang/PR-15835.md) | [Feature] JIT Fused QK norm + qk norm clean up |
| `pr-sglang-15888` | upstream-code | [`sources/prs/sglang/PR-15888.md`](../sources/prs/sglang/PR-15888.md) | [diffusion] model: support TurboWan2.1-T2V-1.3B/14B SLA |
| `pr-sglang-15904` | upstream-code | [`sources/prs/sglang/PR-15904.md`](../sources/prs/sglang/PR-15904.md) | [NPU] NZ for non-quantized MOE, Qwen3 MOE double memory consumption fix |
| `pr-sglang-15948` | upstream-code | [`sources/prs/sglang/PR-15948.md`](../sources/prs/sglang/PR-15948.md) |  Add tuned triton==3.5.1 h200 tp2, tp4 for qwen 3 next |
| `pr-sglang-16084` | upstream-code | [`sources/prs/sglang/PR-16084.md`](../sources/prs/sglang/PR-16084.md) | fix layer intermediate size |
| `pr-sglang-16227` | upstream-code | [`sources/prs/sglang/PR-16227.md`](../sources/prs/sglang/PR-16227.md) | [NemotronH] Add latent MoE support |
| `pr-sglang-16335` | upstream-code | [`sources/prs/sglang/PR-16335.md`](../sources/prs/sglang/PR-16335.md) | [diffusion] Fix RuntimeError in SageAttention3 on Nvidia Blackwell with Qwen-Image |
| `pr-sglang-16382` | upstream-code | [`sources/prs/sglang/PR-16382.md`](../sources/prs/sglang/PR-16382.md) | [Fix]Fix FA3 Performance in Diffusion Model  |
| `pr-sglang-16723` | upstream-code | [`sources/prs/sglang/PR-16723.md`](../sources/prs/sglang/PR-16723.md) | [Rework] Add SwapAB Optimization for triton fused_moe_kernel on SM90. |
| `pr-sglang-16824` | upstream-code | [`sources/prs/sglang/PR-16824.md`](../sources/prs/sglang/PR-16824.md) | [Fix] `flashinfer_trtllm` `intermediate_size` assertion with Qwen3 + TP=8 |
| `pr-sglang-16892` | upstream-code | [`sources/prs/sglang/PR-16892.md`](../sources/prs/sglang/PR-16892.md) | Support mxint4 flashinfer_trtllm moe gemm |
| `pr-sglang-17094` | upstream-code | [`sources/prs/sglang/PR-17094.md`](../sources/prs/sglang/PR-17094.md) | Optimize GDN decode for Qwen3 Next |
| `pr-sglang-17111` | upstream-code | [`sources/prs/sglang/PR-17111.md`](../sources/prs/sglang/PR-17111.md) | [diffusion] fix: fix using upstream flash_attn on blackwell |
| `pr-sglang-17235` | upstream-code | [`sources/prs/sglang/PR-17235.md`](../sources/prs/sglang/PR-17235.md) | [GLM 4.7] Add RTX 6000 Pro aka sm120 |
| `pr-sglang-17554` | upstream-code | [`sources/prs/sglang/PR-17554.md`](../sources/prs/sglang/PR-17554.md) | Kernel: optimize decoding metadata in NSA multi-spec backend with fused kernels |
| `pr-sglang-18233` | upstream-code | [`sources/prs/sglang/PR-18233.md`](../sources/prs/sglang/PR-18233.md) | Support Qwen3 MoE context parallel |
| `pr-sglang-18639` | upstream-code | [`sources/prs/sglang/PR-18639.md`](../sources/prs/sglang/PR-18639.md) | [sglang-miles] True on-policy training support for FSDP2 |
| `pr-sglang-18762` | upstream-code | [`sources/prs/sglang/PR-18762.md`](../sources/prs/sglang/PR-18762.md) | [diffusion] Diffusion norm fusion for z-image |
| `pr-sglang-19059` | upstream-code | [`sources/prs/sglang/PR-19059.md`](../sources/prs/sglang/PR-19059.md) | [jit_kernel] Add fused_qknorm_rope JIT kernel |
| `pr-sglang-19148` | upstream-code | [`sources/prs/sglang/PR-19148.md`](../sources/prs/sglang/PR-19148.md) | [DeepSeek-V3.2][JIT-kernel] Support nsa fuse store indexer k cache |
| `pr-sglang-19174` | upstream-code | [`sources/prs/sglang/PR-19174.md`](../sources/prs/sglang/PR-19174.md) | Adjust padding size to improve triton_kernels moe performance |
| `pr-sglang-19433` | upstream-code | [`sources/prs/sglang/PR-19433.md`](../sources/prs/sglang/PR-19433.md) | Fix/nemotron mtp quantaized |
| `pr-sglang-19537` | upstream-code | [`sources/prs/sglang/PR-19537.md`](../sources/prs/sglang/PR-19537.md) | [FlashInfer v0.6.4] [RL] Integrate FlashInfer mxfp8 gemm, MoE, and routed MoE |
| `pr-sglang-19549` | upstream-code | [`sources/prs/sglang/PR-19549.md`](../sources/prs/sglang/PR-19549.md) | [diffusion][llm] macOS support |
| `pr-sglang-19652` | upstream-code | [`sources/prs/sglang/PR-19652.md`](../sources/prs/sglang/PR-19652.md) | [Feature] NVFP4 Marlin fallback for non-Blackwell GPUs (SM75+) |
| `pr-sglang-19725` | upstream-code | [`sources/prs/sglang/PR-19725.md`](../sources/prs/sglang/PR-19725.md) | [SGLang-Diffusion] Fix custom op fake impl missing eps default for torch.compile |
| `pr-sglang-19794` | upstream-code | [`sources/prs/sglang/PR-19794.md`](../sources/prs/sglang/PR-19794.md) | Add compile-time 256-bit vector guard for pre-Blackwell |
| `pr-sglang-20039` | upstream-code | [`sources/prs/sglang/PR-20039.md`](../sources/prs/sglang/PR-20039.md) | [Bugfix] Work around FlashInfer unified transport issue on GB |
| `pr-sglang-20094` | upstream-code | [`sources/prs/sglang/PR-20094.md`](../sources/prs/sglang/PR-20094.md) | [diffusion] fix bug of copy_if |
| `pr-sglang-20137` | upstream-code | [`sources/prs/sglang/PR-20137.md`](../sources/prs/sglang/PR-20137.md) | [diffusion] Support nvfp4 for Flux.2 |
| `pr-sglang-20268` | upstream-code | [`sources/prs/sglang/PR-20268.md`](../sources/prs/sglang/PR-20268.md) | [4/n jit_kernel restruct] speed up CI tests and add benchmark workflow |
| `pr-sglang-20305` | upstream-code | [`sources/prs/sglang/PR-20305.md`](../sources/prs/sglang/PR-20305.md) | [Benchmark] use flashinfer bench_gpu_time instead of triton do_bench |
| `pr-sglang-20384` | upstream-code | [`sources/prs/sglang/PR-20384.md`](../sources/prs/sglang/PR-20384.md) | [Fix] Add fallback for flashinfer allreduce fusion |
| `pr-sglang-20501` | upstream-code | [`sources/prs/sglang/PR-20501.md`](../sources/prs/sglang/PR-20501.md) | [Kernel] Fuse temperature + softmax in sampling for decode speedup |
| `pr-sglang-20576` | upstream-code | [`sources/prs/sglang/PR-20576.md`](../sources/prs/sglang/PR-20576.md) | [Diffusion] Clean upstream fa3 in hopper |
| `pr-sglang-20632` | upstream-code | [`sources/prs/sglang/PR-20632.md`](../sources/prs/sglang/PR-20632.md) | [Diffusion] Add a benchmark for rmsnorm/fuse_add_rmsnorm |
| `pr-sglang-20673` | upstream-code | [`sources/prs/sglang/PR-20673.md`](../sources/prs/sglang/PR-20673.md) | [Feature][JIT Kernel] Fused TP QK norm For Minimax |
| `pr-sglang-20910` | upstream-code | [`sources/prs/sglang/PR-20910.md`](../sources/prs/sglang/PR-20910.md) | Add SGLang CUDA crash API logging inspired by FlashInfer |
| `pr-sglang-20988` | upstream-code | [`sources/prs/sglang/PR-20988.md`](../sources/prs/sglang/PR-20988.md) | ci: run Stage A CUDA tests as stage-a-test-small-1-gpu on 5090 |
| `pr-sglang-21019` | upstream-code | [`sources/prs/sglang/PR-21019.md`](../sources/prs/sglang/PR-21019.md) | [Qwen3.5] Fuse split/reshape/cat ops in GDN projection with Triton kernel |
| `pr-sglang-21233` | upstream-code | [`sources/prs/sglang/PR-21233.md`](../sources/prs/sglang/PR-21233.md) | [refactor] Clean up duplicate flashinfer trtllm moe code |
| `pr-sglang-21239` | upstream-code | [`sources/prs/sglang/PR-21239.md`](../sources/prs/sglang/PR-21239.md) | Refactor JIT kernel CI to use run_suite.py registration system |
| `pr-sglang-21280` | upstream-code | [`sources/prs/sglang/PR-21280.md`](../sources/prs/sglang/PR-21280.md) | [RL] Support mxfp8 DeepSeek V3 |
| `pr-sglang-21321` | upstream-code | [`sources/prs/sglang/PR-21321.md`](../sources/prs/sglang/PR-21321.md) | [Kernel] Support FlashInfer TRTLLM-Gen fused MoE for non-gated FP4 & FP8 (Nemotron) |
| `pr-sglang-21325` | upstream-code | [`sources/prs/sglang/PR-21325.md`](../sources/prs/sglang/PR-21325.md) | [misc] clean up kernel API |
| `pr-sglang-21411` | upstream-code | [`sources/prs/sglang/PR-21411.md`](../sources/prs/sglang/PR-21411.md) | [GDN] Fuse GDN kkt + solve_tril into one kernel |
| `pr-sglang-21440` | upstream-code | [`sources/prs/sglang/PR-21440.md`](../sources/prs/sglang/PR-21440.md) | [Diffusion] Add qknorm rope fuse kernel |
| `pr-sglang-21654` | upstream-code | [`sources/prs/sglang/PR-21654.md`](../sources/prs/sglang/PR-21654.md) | [jit_kernel] Optimize fused_qknorm_rope: deduplicate sincosf for interleave RoPE  |
| `pr-sglang-21734` | upstream-code | [`sources/prs/sglang/PR-21734.md`](../sources/prs/sglang/PR-21734.md) | perf: optimize PCG inductor path for FP8 models |
| `pr-sglang-21834` | upstream-code | [`sources/prs/sglang/PR-21834.md`](../sources/prs/sglang/PR-21834.md) | [Feature] JIT rmsnorm update (with claude) |
| `pr-sglang-22024` | upstream-code | [`sources/prs/sglang/PR-22024.md`](../sources/prs/sglang/PR-22024.md) | [NPU] enable mla prepare fused kernel only when being mla attn |
| `pr-sglang-22064` | upstream-code | [`sources/prs/sglang/PR-22064.md`](../sources/prs/sglang/PR-22064.md) | [Diffusion] Fix weight scale swizzle and add large-M kernel config for FLUX.2-dev-NVFP4 |
| `pr-sglang-22091` | upstream-code | [`sources/prs/sglang/PR-22091.md`](../sources/prs/sglang/PR-22091.md) | [diffusion] Default NVFP4 to CUTLASS and add all-model shape benchmarks |
| `pr-sglang-22127` | upstream-code | [`sources/prs/sglang/PR-22127.md`](../sources/prs/sglang/PR-22127.md) | [Diffusion] Add diffusion NVFP4 scaled-mm correctness test |
| `pr-sglang-22365` | upstream-code | [`sources/prs/sglang/PR-22365.md`](../sources/prs/sglang/PR-22365.md) | [Diffusion] modelopt diffusion fp8 support for flux1/flux2 and wan2.2 |
| `pr-sglang-22574` | upstream-code | [`sources/prs/sglang/PR-22574.md`](../sources/prs/sglang/PR-22574.md) | [Diffusion] Add FLUX.1-dev ModelOpt NVFP4 support |
| `pr-sglang-22594` | upstream-code | [`sources/prs/sglang/PR-22594.md`](../sources/prs/sglang/PR-22594.md) | diffusion: fix layerwise offload for ModelOpt quantized DiTs |
| `pr-sglang-22672` | upstream-code | [`sources/prs/sglang/PR-22672.md`](../sources/prs/sglang/PR-22672.md) | reland [Diffusion] Add FLUX.1-dev ModelOpt NVFP4 support |
| `pr-sglang-22681` | upstream-code | [`sources/prs/sglang/PR-22681.md`](../sources/prs/sglang/PR-22681.md) | [Diffusion] Add Wan2.2 ModelOpt NVFP4 support |
| `pr-sglang-22717` | upstream-code | [`sources/prs/sglang/PR-22717.md`](../sources/prs/sglang/PR-22717.md) | [codex] Add flashinfer TRTLLM backend for diffusion NVFP4 |
| `pr-sglang-22814` | upstream-code | [`sources/prs/sglang/PR-22814.md`](../sources/prs/sglang/PR-22814.md) | diffusion: add HunyuanVideo GroupNorm+SiLU fast path |
| `pr-sglang-22869` | upstream-code | [`sources/prs/sglang/PR-22869.md`](../sources/prs/sglang/PR-22869.md) | [diffusion] feat: introduce ltx-2-two-stage device manager |
| `pr-sglang-23148` | upstream-code | [`sources/prs/sglang/PR-23148.md`](../sources/prs/sglang/PR-23148.md) | [codex] diffusion: enable group norm silu fuse by default |
| `pr-sglang-23686` | upstream-code | [`sources/prs/sglang/PR-23686.md`](../sources/prs/sglang/PR-23686.md) | Deepseek_v4 support w4(mxfp4)a16 on hopper |
| `pr-sglang-23707` | upstream-code | [`sources/prs/sglang/PR-23707.md`](../sources/prs/sglang/PR-23707.md) | [MoE] Deprecate act_and_mul_triton; fold filter_expert into JIT silu/gelu_and_mul |
| `pr-sglang-23938` | upstream-code | [`sources/prs/sglang/PR-23938.md`](../sources/prs/sglang/PR-23938.md) | Optimize large GroupNorm SiLU apply |
| `pr-sglang-23965` | upstream-code | [`sources/prs/sglang/PR-23965.md`](../sources/prs/sglang/PR-23965.md) | Enable PDL for various kernels in DSV32/GLM5 |
| `pr-sglang-24048` | upstream-code | [`sources/prs/sglang/PR-24048.md`](../sources/prs/sglang/PR-24048.md) | [VLM] Optimize Gemma4 VLM with PCG and fuse RMSNorm + residual add + scalar |
| `pr-sglang-24411` | upstream-code | [`sources/prs/sglang/PR-24411.md`](../sources/prs/sglang/PR-24411.md) | [diffusion] Fuse LTX2 split rotary embedding |
| `pr-sglang-24490` | upstream-code | [`sources/prs/sglang/PR-24490.md`](../sources/prs/sglang/PR-24490.md) | Port MXFP4 Marlin MoE support to JIT kernel path |
| `pr-sglang-24562` | upstream-code | [`sources/prs/sglang/PR-24562.md`](../sources/prs/sglang/PR-24562.md) | Fix performance regression on Deepseek V3 on `moe-runner-backend=triton` on SM90 |
| `pr-sglang-24696` | upstream-code | [`sources/prs/sglang/PR-24696.md`](../sources/prs/sglang/PR-24696.md) | [Gemma4] Optimize Gemm4 with fused Q/K/V RMSNorm + per-expert FP8 ckpt loader |
| `pr-sglang-24816` | upstream-code | [`sources/prs/sglang/PR-24816.md`](../sources/prs/sglang/PR-24816.md) | Add FlashInfer SM90 cutlass MXFP4 MoE backend (W4A16) for GPT-OSS + DeepSeek-V4 |
| `pr-sglang-24986` | upstream-code | [`sources/prs/sglang/PR-24986.md`](../sources/prs/sglang/PR-24986.md) | [rebase]Deepseek_v4 support w4(mxfp4)a16 on hopper |
| `pr-sglang-25107` | upstream-code | [`sources/prs/sglang/PR-25107.md`](../sources/prs/sglang/PR-25107.md) | perf(nvfp4): free unused source scales after weight processing |
| `pr-sglang-3216` | upstream-code | [`sources/prs/sglang/PR-3216.md`](../sources/prs/sglang/PR-3216.md) | add tensorrt_llm common and cutlass_extensions as 3rdparty |
| `pr-sglang-3730` | upstream-code | [`sources/prs/sglang/PR-3730.md`](../sources/prs/sglang/PR-3730.md) | Feature DeepSeek V3/R1 INT8 Quantization (block-wise) |
| `pr-sglang-3888` | upstream-code | [`sources/prs/sglang/PR-3888.md`](../sources/prs/sglang/PR-3888.md) | [Feature] DeepSeek V3/R1 INT8 Quantization (channel-wise)  |
| `pr-sglang-4215` | upstream-code | [`sources/prs/sglang/PR-4215.md`](../sources/prs/sglang/PR-4215.md) | Accelerate FP8 CUDA Kernel by 20-28% |
| `pr-sglang-4530` | upstream-code | [`sources/prs/sglang/PR-4530.md`](../sources/prs/sglang/PR-4530.md) | Add deepseek style fused moe group gate selection kernel |
| `pr-sglang-4918` | upstream-code | [`sources/prs/sglang/PR-4918.md`](../sources/prs/sglang/PR-4918.md) | Add DeepSeek V3/R1 shared experts fusion |
| `pr-sglang-5086` | upstream-code | [`sources/prs/sglang/PR-5086.md`](../sources/prs/sglang/PR-5086.md) | reduce moe_align_block_size_kernel small batch mode overhead |
| `pr-sglang-5371` | upstream-code | [`sources/prs/sglang/PR-5371.md`](../sources/prs/sglang/PR-5371.md) | apply fused moe gate in ds v3/r1 |
| `pr-sglang-5432` | upstream-code | [`sources/prs/sglang/PR-5432.md`](../sources/prs/sglang/PR-5432.md) | [perf] introduce deep gemm group_gemm_masked as bmm |
| `pr-sglang-6042` | upstream-code | [`sources/prs/sglang/PR-6042.md`](../sources/prs/sglang/PR-6042.md) | Support tuning moe for llama 4 model |
| `pr-sglang-6093` | upstream-code | [`sources/prs/sglang/PR-6093.md`](../sources/prs/sglang/PR-6093.md) | [1/2] Add Kernel support for Cutlass based Fused FP4 MoE |
| `pr-sglang-6226` | upstream-code | [`sources/prs/sglang/PR-6226.md`](../sources/prs/sglang/PR-6226.md) | enable auto-round quantization model |
| `pr-sglang-6295` | upstream-code | [`sources/prs/sglang/PR-6295.md`](../sources/prs/sglang/PR-6295.md) | fix: enable multi-GPU Triton fused MoE tuning |
| `pr-sglang-6369` | upstream-code | [`sources/prs/sglang/PR-6369.md`](../sources/prs/sglang/PR-6369.md) | reduce torch.zeros overhead in moe align block size kernel |
| `pr-sglang-6404` | upstream-code | [`sources/prs/sglang/PR-6404.md`](../sources/prs/sglang/PR-6404.md) | Add fp8 fused_experts kernel for CPU in sgl-kernel and add UT |
| `pr-sglang-6627` | upstream-code | [`sources/prs/sglang/PR-6627.md`](../sources/prs/sglang/PR-6627.md) | Refine pre_reorder_triton_kernel slightly to improve performance |
| `pr-sglang-6641` | upstream-code | [`sources/prs/sglang/PR-6641.md`](../sources/prs/sglang/PR-6641.md) | [CPU] [BF16] Call fused_experts_cpu, weight_packed_linear and bmm_cpu kernel in DeepSeek model |
| `pr-sglang-6736` | upstream-code | [`sources/prs/sglang/PR-6736.md`](../sources/prs/sglang/PR-6736.md) | Set `num_fused_shared_experts` as `num_shared_experts` when shared_experts fusion is not disabled |
| `pr-sglang-6769` | upstream-code | [`sources/prs/sglang/PR-6769.md`](../sources/prs/sglang/PR-6769.md) | [CPU] add optimizations for INT8 and FP8 DeepSeek |
| `pr-sglang-6771` | upstream-code | [`sources/prs/sglang/PR-6771.md`](../sources/prs/sglang/PR-6771.md) | [CPU] support the case where num_attention_heads or intermediate_size is not divisible by the TP size |
| `pr-sglang-6853` | upstream-code | [`sources/prs/sglang/PR-6853.md`](../sources/prs/sglang/PR-6853.md) | [DeepseekR1-FP4] Add Support for nvidia/DeepSeekR1-FP4 model |
| `pr-sglang-6890` | upstream-code | [`sources/prs/sglang/PR-6890.md`](../sources/prs/sglang/PR-6890.md) | Use deepgemm instead of triton for fused_qkv_a_proj_with_mqa |
| `pr-sglang-6958` | upstream-code | [`sources/prs/sglang/PR-6958.md`](../sources/prs/sglang/PR-6958.md) | chore: upgrade flashinfer v0.2.6.post1 jit |
| `pr-sglang-6970` | upstream-code | [`sources/prs/sglang/PR-6970.md`](../sources/prs/sglang/PR-6970.md) | Fuse routed scaling factor in deepseek |
| `pr-sglang-7023` | upstream-code | [`sources/prs/sglang/PR-7023.md`](../sources/prs/sglang/PR-7023.md) | Update default settings for blackwell |
| `pr-sglang-7093` | upstream-code | [`sources/prs/sglang/PR-7093.md`](../sources/prs/sglang/PR-7093.md) | Fix positional argument |
| `pr-sglang-7129` | upstream-code | [`sources/prs/sglang/PR-7129.md`](../sources/prs/sglang/PR-7129.md) | Enable ModelOpt Llama4 fp8 checkpoint deployment in SGLang |
| `pr-sglang-7172` | upstream-code | [`sources/prs/sglang/PR-7172.md`](../sources/prs/sglang/PR-7172.md) | Support new DeepGEMM |
| `pr-sglang-7268` | upstream-code | [`sources/prs/sglang/PR-7268.md`](../sources/prs/sglang/PR-7268.md) | [AMD] add aiter fused moe in DeepEP path |
| `pr-sglang-7327` | upstream-code | [`sources/prs/sglang/PR-7327.md`](../sources/prs/sglang/PR-7327.md) | FlashInfer NVFP4 MoE with EP & 2-stream shared expert |
| `pr-sglang-7376` | upstream-code | [`sources/prs/sglang/PR-7376.md`](../sources/prs/sglang/PR-7376.md) | Fix MTP with Deepseek R1 Fp4 |
| `pr-sglang-7391` | upstream-code | [`sources/prs/sglang/PR-7391.md`](../sources/prs/sglang/PR-7391.md) | Fix torch compile run |
| `pr-sglang-7621` | upstream-code | [`sources/prs/sglang/PR-7621.md`](../sources/prs/sglang/PR-7621.md) | [b200] support trt-llm allreduce fuse rms_norm_add kernel |
| `pr-sglang-7630` | upstream-code | [`sources/prs/sglang/PR-7630.md`](../sources/prs/sglang/PR-7630.md) | Add dsv3 fused a gemm to sgl-kernel |
| `pr-sglang-7667` | upstream-code | [`sources/prs/sglang/PR-7667.md`](../sources/prs/sglang/PR-7667.md) | Add fp4 quantize before all-gather for Flashinfer cutlass MoE DP (max throughput) |
| `pr-sglang-7689` | upstream-code | [`sources/prs/sglang/PR-7689.md`](../sources/prs/sglang/PR-7689.md) | Integrate triton moe kernel |
| `pr-sglang-8118` | upstream-code | [`sources/prs/sglang/PR-8118.md`](../sources/prs/sglang/PR-8118.md) | [feat] Support tp mode for DeepSeek-R1-W4AFP8 |
| `pr-sglang-8258` | upstream-code | [`sources/prs/sglang/PR-8258.md`](../sources/prs/sglang/PR-8258.md) | Support triton kernels v3.4.0 for fused_moe |
| `pr-sglang-8552` | upstream-code | [`sources/prs/sglang/PR-8552.md`](../sources/prs/sglang/PR-8552.md) | [NVIDIA] Add Low Latency NVFP4 decode kernels from Flashinfer |
| `pr-sglang-8678` | upstream-code | [`sources/prs/sglang/PR-8678.md`](../sources/prs/sglang/PR-8678.md) | feat: support cutlass_moe_fp8 kernel for fusedmoe in sm90 |
| `pr-sglang-8731` | upstream-code | [`sources/prs/sglang/PR-8731.md`](../sources/prs/sglang/PR-8731.md) | fuse allreduce and residual_rmsnorm |
| `pr-sglang-8898` | upstream-code | [`sources/prs/sglang/PR-8898.md`](../sources/prs/sglang/PR-8898.md) | [Perf] Auto enable best flashinfer mxfp4  kernel in b200 |
| `pr-sglang-9339` | upstream-code | [`sources/prs/sglang/PR-9339.md`](../sources/prs/sglang/PR-9339.md) | Support trtllm_allreduce_fusion in flashinfer for cuda<12.8 |
| `pr-sglang-9473` | upstream-code | [`sources/prs/sglang/PR-9473.md`](../sources/prs/sglang/PR-9473.md) | [fix] Fix mxfp4 triton MoE tp bug |
| `pr-sglang-9477` | upstream-code | [`sources/prs/sglang/PR-9477.md`](../sources/prs/sglang/PR-9477.md) | Optimize moe_sum_reduce_kernel |
| `pr-sglang-9660` | upstream-code | [`sources/prs/sglang/PR-9660.md`](../sources/prs/sglang/PR-9660.md) | Single Batch Overlap for MoE Models |
| `pr-sglang-9744` | upstream-code | [`sources/prs/sglang/PR-9744.md`](../sources/prs/sglang/PR-9744.md) | [CPU] Add FP8 Bmm support |
| `pr-tensorrt-llm-10042` | upstream-code | [`sources/prs/tensorrt-llm/PR-10042.md`](../sources/prs/tensorrt-llm/PR-10042.md) | [None][perf] Add more optimization options for MOE CuteDSL finalized kernel |
| `pr-tensorrt-llm-10043` | upstream-code | [`sources/prs/tensorrt-llm/PR-10043.md`](../sources/prs/tensorrt-llm/PR-10043.md) | [TRTLLM-9992][perf] Enable PDL for CuteDSL kernels and overlap MoeOutputMemset |
| `pr-tensorrt-llm-10088` | upstream-code | [`sources/prs/tensorrt-llm/PR-10088.md`](../sources/prs/tensorrt-llm/PR-10088.md) | [None][feat] CuteDSL MOE FC1 Enhancement |
| `pr-tensorrt-llm-10201` | upstream-code | [`sources/prs/tensorrt-llm/PR-10201.md`](../sources/prs/tensorrt-llm/PR-10201.md) | [TRTLLM-9831][perf] Enable 2CTA with autotune for CuteDSL MoE and Grouped GEMM optimizations |
| `pr-tensorrt-llm-10279` | upstream-code | [`sources/prs/tensorrt-llm/PR-10279.md`](../sources/prs/tensorrt-llm/PR-10279.md) | [TRTLLM-10147][perf] Balanced random MoE workload generator for CuteDSL kernel UT, autotuner and layerwise benchmark |
| `pr-tensorrt-llm-10327` | upstream-code | [`sources/prs/tensorrt-llm/PR-10327.md`](../sources/prs/tensorrt-llm/PR-10327.md) | [None][fix] impl fused triton kernel for e8m0 resmooth to reduce memory footprint |
| `pr-tensorrt-llm-10429` | upstream-code | [`sources/prs/tensorrt-llm/PR-10429.md`](../sources/prs/tensorrt-llm/PR-10429.md) | [None] [feat] Add test script and raster M for gather fc1 kernel |
| `pr-tensorrt-llm-10479` | upstream-code | [`sources/prs/tensorrt-llm/PR-10479.md`](../sources/prs/tensorrt-llm/PR-10479.md) | [None] [feat] Add densegemm backend for MoE |
| `pr-tensorrt-llm-10532` | upstream-code | [`sources/prs/tensorrt-llm/PR-10532.md`](../sources/prs/tensorrt-llm/PR-10532.md) | [None][feat] MiniMax M2 support |
| `pr-tensorrt-llm-10987` | upstream-code | [`sources/prs/tensorrt-llm/PR-10987.md`](../sources/prs/tensorrt-llm/PR-10987.md) | [TRTLLM-9831][perf] Use TMA.RED to improve effective memory bandwidth |
| `pr-tensorrt-llm-11143` | upstream-code | [`sources/prs/tensorrt-llm/PR-11143.md`](../sources/prs/tensorrt-llm/PR-11143.md) | [None][feat] fuse shared to sparse experts in TRT-LLM Gen MoE |
| `pr-tensorrt-llm-11273` | upstream-code | [`sources/prs/tensorrt-llm/PR-11273.md`](../sources/prs/tensorrt-llm/PR-11273.md) | [None][feat] Optimize super-v3 nvfp4 for better perf |
| `pr-tensorrt-llm-11381` | upstream-code | [`sources/prs/tensorrt-llm/PR-11381.md`](../sources/prs/tensorrt-llm/PR-11381.md) | [None][feat] Remove non flash attetnion style fmha_v2 kernel for hopper |
| `pr-tensorrt-llm-11473` | upstream-code | [`sources/prs/tensorrt-llm/PR-11473.md`](../sources/prs/tensorrt-llm/PR-11473.md) | [None][feat] Optimize by fuse nvfp4_quant to layernorm_gated for mamba2_mixer |
| `pr-tensorrt-llm-11589` | upstream-code | [`sources/prs/tensorrt-llm/PR-11589.md`](../sources/prs/tensorrt-llm/PR-11589.md) | [TRTLLM-10004][feat] Enable GEMM -> AR with GEMM output in registered buffers |
| `pr-tensorrt-llm-11652` | upstream-code | [`sources/prs/tensorrt-llm/PR-11652.md`](../sources/prs/tensorrt-llm/PR-11652.md) | [None][feat] NVFP4 TRTLLM-Gen MoE for AutoDeploy (Nemotron Super) |
| `pr-tensorrt-llm-11718` | upstream-code | [`sources/prs/tensorrt-llm/PR-11718.md`](../sources/prs/tensorrt-llm/PR-11718.md) | [TRTLLM-11119][feat] Blackwell SageAttention, Integrate into AttentionOp API |
| `pr-tensorrt-llm-11769` | upstream-code | [`sources/prs/tensorrt-llm/PR-11769.md`](../sources/prs/tensorrt-llm/PR-11769.md) | [https://nvbugs/5885070][fix] fix deepeplowlatency with cutedsl moe backend |
| `pr-tensorrt-llm-11774` | upstream-code | [`sources/prs/tensorrt-llm/PR-11774.md`](../sources/prs/tensorrt-llm/PR-11774.md) | [None][fix] Fix SM120 issue for rms_norm with nvfp4_quant_fusion |
| `pr-tensorrt-llm-11869` | upstream-code | [`sources/prs/tensorrt-llm/PR-11869.md`](../sources/prs/tensorrt-llm/PR-11869.md) | [None][feat] Add fused DiT QK Norm + RoPE CUDA kernel for FLUX |
| `pr-tensorrt-llm-11897` | upstream-code | [`sources/prs/tensorrt-llm/PR-11897.md`](../sources/prs/tensorrt-llm/PR-11897.md) | [TRTLLM-10990][feat] Fuse SwiGLU and quant into shared expert |
| `pr-tensorrt-llm-11899` | upstream-code | [`sources/prs/tensorrt-llm/PR-11899.md`](../sources/prs/tensorrt-llm/PR-11899.md) | [TRTLLM-10421][perf] Add fused cat+fp8_quantize CUDA kernel for DSA indexer |
| `pr-tensorrt-llm-11993` | upstream-code | [`sources/prs/tensorrt-llm/PR-11993.md`](../sources/prs/tensorrt-llm/PR-11993.md) | [#11694][feat] AutoDeploy: Improve the piecewise CG memory usage |
| `pr-tensorrt-llm-12055` | upstream-code | [`sources/prs/tensorrt-llm/PR-12055.md`](../sources/prs/tensorrt-llm/PR-12055.md) | [TRTLLM-11285][feat] Fuse indexer wk + weights_proj into single GEMM in TF32 for DS-V3.2 |
| `pr-tensorrt-llm-12079` | upstream-code | [`sources/prs/tensorrt-llm/PR-12079.md`](../sources/prs/tensorrt-llm/PR-12079.md) | [None][feat] CuteDSL MOE: Add raster along M/N support for blockscaled contiguous backbone kernel |
| `pr-tensorrt-llm-12136` | upstream-code | [`sources/prs/tensorrt-llm/PR-12136.md`](../sources/prs/tensorrt-llm/PR-12136.md) | [None][feat] Add DWDP (Distributed Weight Data Parallelism) support for MoE inference |
| `pr-tensorrt-llm-12201` | upstream-code | [`sources/prs/tensorrt-llm/PR-12201.md`](../sources/prs/tensorrt-llm/PR-12201.md) | [None][feat] Add fused allreduce+RMSNorm op and optional residual in … |
| `pr-tensorrt-llm-12320` | upstream-code | [`sources/prs/tensorrt-llm/PR-12320.md`](../sources/prs/tensorrt-llm/PR-12320.md) | [None][feat] Support update weight for nvfp4 |
| `pr-tensorrt-llm-12322` | upstream-code | [`sources/prs/tensorrt-llm/PR-12322.md`](../sources/prs/tensorrt-llm/PR-12322.md) | [https://nvbugs/5983390][perf] Kernel fusions in _gather_k_cache_for_chunk of Indexer in DSA |
| `pr-tensorrt-llm-12427` | upstream-code | [`sources/prs/tensorrt-llm/PR-12427.md`](../sources/prs/tensorrt-llm/PR-12427.md) | [None][feat] MLIR-based auto-generated elementwise fusion for AutoDeploy |
| `pr-tensorrt-llm-12470` | upstream-code | [`sources/prs/tensorrt-llm/PR-12470.md`](../sources/prs/tensorrt-llm/PR-12470.md) | [None][feat] Support sparse mqa/gqa attention |
| `pr-tensorrt-llm-12738` | upstream-code | [`sources/prs/tensorrt-llm/PR-12738.md`](../sources/prs/tensorrt-llm/PR-12738.md) | [None][feat] Add bf16 trtllm-gen moe support through flashinfer. |
| `pr-tensorrt-llm-12799` | upstream-code | [`sources/prs/tensorrt-llm/PR-12799.md`](../sources/prs/tensorrt-llm/PR-12799.md) | [TRTLLM-11797][feat] Add cutedsl moe backend supporting for qwen3.5. |
| `pr-tensorrt-llm-12884` | upstream-code | [`sources/prs/tensorrt-llm/PR-12884.md`](../sources/prs/tensorrt-llm/PR-12884.md) | [TRTLLM-11585][feat] Add CUTEDSL moe backend for nemotron-h |
| `pr-tensorrt-llm-12946` | upstream-code | [`sources/prs/tensorrt-llm/PR-12946.md`](../sources/prs/tensorrt-llm/PR-12946.md) | [#12784][feat] AutoDeploy: Optimize DeepSeek-R1 model performance |
| `pr-tensorrt-llm-13033` | upstream-code | [`sources/prs/tensorrt-llm/PR-13033.md`](../sources/prs/tensorrt-llm/PR-13033.md) | [None][feat] Update rms_norm + fp4_qaunt kernel supporting more dim |
| `pr-tensorrt-llm-13052` | upstream-code | [`sources/prs/tensorrt-llm/PR-13052.md`](../sources/prs/tensorrt-llm/PR-13052.md) | [#12716][feat] Fused cross-head QK Norm + RoPE kernel for WAN |
| `pr-tensorrt-llm-13169` | upstream-code | [`sources/prs/tensorrt-llm/PR-13169.md`](../sources/prs/tensorrt-llm/PR-13169.md) | [https://nvbugs/5945047][fix] Fix cluster launch enablement for SM120 GPUs in allReduce fusion |
| `pr-tensorrt-llm-13207` | upstream-code | [`sources/prs/tensorrt-llm/PR-13207.md`](../sources/prs/tensorrt-llm/PR-13207.md) | [None][fix] Propagate init_load_balancer to DeepGemmFusedMoE in create_moe_backend |
| `pr-tensorrt-llm-13340` | upstream-code | [`sources/prs/tensorrt-llm/PR-13340.md`](../sources/prs/tensorrt-llm/PR-13340.md) | [None][feat] Integrate FP4 indexer for DSA on Blackwell |
| `pr-tensorrt-llm-13384` | upstream-code | [`sources/prs/tensorrt-llm/PR-13384.md`](../sources/prs/tensorrt-llm/PR-13384.md) | [None][feat] Add MegaMoEDeepGemmFusedMoE backend wrapping DeepGEMM fp8_fp4_mega_moe |
| `pr-tensorrt-llm-13433` | upstream-code | [`sources/prs/tensorrt-llm/PR-13433.md`](../sources/prs/tensorrt-llm/PR-13433.md) | [None][perf] Extend customMoeRouting kernel to support Qwen3.5 |
| `pr-tensorrt-llm-13452` | upstream-code | [`sources/prs/tensorrt-llm/PR-13452.md`](../sources/prs/tensorrt-llm/PR-13452.md) | [TRTLLM-11285][perf] Force enable TF32 tensor cores for DSA indexer fused GEMM |
| `pr-tensorrt-llm-13454` | upstream-code | [`sources/prs/tensorrt-llm/PR-13454.md`](../sources/prs/tensorrt-llm/PR-13454.md) | [None][fix] Split TRT-LLM-only rope fusion out of standalone auto_deploy |
| `pr-tensorrt-llm-13595` | upstream-code | [`sources/prs/tensorrt-llm/PR-13595.md`](../sources/prs/tensorrt-llm/PR-13595.md) | [None][feat] Enable EPLB for DeepSeek-V4 |
| `pr-tensorrt-llm-13628` | upstream-code | [`sources/prs/tensorrt-llm/PR-13628.md`](../sources/prs/tensorrt-llm/PR-13628.md) | [None][feat] Fuse FP8 1x128 quantize + UE8M0 scale pack on SM100 |
| `pr-tensorrt-llm-13767` | upstream-code | [`sources/prs/tensorrt-llm/PR-13767.md`](../sources/prs/tensorrt-llm/PR-13767.md) | [None][fix] Plumb swiglu_limit through DeepGEMM and TRTLLMGen FP8 fused MoE |
| `pr-tensorrt-llm-13771` | upstream-code | [`sources/prs/tensorrt-llm/PR-13771.md`](../sources/prs/tensorrt-llm/PR-13771.md) | [None][fix] Fix fused MHC for DeepSeek-V4-Pro hidden size |
| `pr-tensorrt-llm-13892` | upstream-code | [`sources/prs/tensorrt-llm/PR-13892.md`](../sources/prs/tensorrt-llm/PR-13892.md) | [None][perf] mHC fused_hc kernel optimizations + DS-V4 entry-boundary RMSNorm fold-in |
| `pr-tensorrt-llm-13938` | upstream-code | [`sources/prs/tensorrt-llm/PR-13938.md`](../sources/prs/tensorrt-llm/PR-13938.md) | [None][feat] Keep DSv4 o_a_proj as FP8, and port vLLM's fused_inv_rope_fp8_quant |
| `pr-tensorrt-llm-13997` | upstream-code | [`sources/prs/tensorrt-llm/PR-13997.md`](../sources/prs/tensorrt-llm/PR-13997.md) | [None][feat] enable TRTLLM-Gen internal routing |
| `pr-tensorrt-llm-6538` | upstream-code | [`sources/prs/tensorrt-llm/PR-6538.md`](../sources/prs/tensorrt-llm/PR-6538.md) | [None][feat] Use Separate QKV Input Layout for Context MLA |
| `pr-tensorrt-llm-7937` | upstream-code | [`sources/prs/tensorrt-llm/PR-7937.md`](../sources/prs/tensorrt-llm/PR-7937.md) | [None][feat] GPT-OSS Sm120/Sm121 Support |
| `pr-tensorrt-llm-8501` | upstream-code | [`sources/prs/tensorrt-llm/PR-8501.md`](../sources/prs/tensorrt-llm/PR-8501.md) | [None][fix] Fix the performance issue of FP8 blockwise grouped GEMM when using attention DP |
| `pr-tensorrt-llm-8675` | upstream-code | [`sources/prs/tensorrt-llm/PR-8675.md`](../sources/prs/tensorrt-llm/PR-8675.md) | [TRTLLM-8827] [feat] Enable low precision alltoall for Cutlass and TRTLLMGen backends |
| `pr-tensorrt-llm-8886` | upstream-code | [`sources/prs/tensorrt-llm/PR-8886.md`](../sources/prs/tensorrt-llm/PR-8886.md) | [None][feat] Enable EPLB for trtllm-gen and cutlass backend |
| `pr-tensorrt-llm-9486` | upstream-code | [`sources/prs/tensorrt-llm/PR-9486.md`](../sources/prs/tensorrt-llm/PR-9486.md) | [TRTLLM-8958][feat] and [TRTLLM-8960]: create ConfigurableMoE and support TRTLLMGenFusedMoE as backend |
| `pr-tensorrt-llm-9618` | upstream-code | [`sources/prs/tensorrt-llm/PR-9618.md`](../sources/prs/tensorrt-llm/PR-9618.md) | [TRTLLM-9685] [feat] Add gather fc1 kernel by cuteDSL |
| `pr-tensorrt-llm-9729` | upstream-code | [`sources/prs/tensorrt-llm/PR-9729.md`](../sources/prs/tensorrt-llm/PR-9729.md) | [None][feat] add fp4 gemm + allreduce |
| `pr-tensorrt-llm-9838` | upstream-code | [`sources/prs/tensorrt-llm/PR-9838.md`](../sources/prs/tensorrt-llm/PR-9838.md) | [https://nvbugs/5726962][feat] Apply fusion for W4AFP8_AWQ MoE |
| `pr-tensorrt-llm-9852` | upstream-code | [`sources/prs/tensorrt-llm/PR-9852.md`](../sources/prs/tensorrt-llm/PR-9852.md) | [None][feat] Fused kernels (qknormrope + moe routing) and two-model MTP support for glm4moe |
| `pr-tensorrt-llm-9905` | upstream-code | [`sources/prs/tensorrt-llm/PR-9905.md`](../sources/prs/tensorrt-llm/PR-9905.md) | [None][feat] Adding torch ext API for FusedAddRMSNormQuant kernel |
| `pr-tensorrt-llm-9924` | upstream-code | [`sources/prs/tensorrt-llm/PR-9924.md`](../sources/prs/tensorrt-llm/PR-9924.md) | [TRTLLM-9493][feat] Add helixPostProcessNative kernel for cp_dim=2 |
| `pr-tilelang-1200` | upstream-code | [`sources/prs/tilelang/PR-1200.md`](../sources/prs/tilelang/PR-1200.md) | [Refactor] Add kernel selection option for GEMM v1 in environment settings |
| `pr-tilelang-1221` | upstream-code | [`sources/prs/tilelang/PR-1221.md`](../sources/prs/tilelang/PR-1221.md) |  [Enhancement] Improve iterator handling in layout utilities and parallel operations |
| `pr-tilelang-1338` | upstream-code | [`sources/prs/tilelang/PR-1338.md`](../sources/prs/tilelang/PR-1338.md) | [Language][UX] Semantic check for parallel fragment access |
| `pr-tilelang-1421` | upstream-code | [`sources/prs/tilelang/PR-1421.md`](../sources/prs/tilelang/PR-1421.md) | feat(cutedsl): add CuTeDSL backend |
| `pr-tilelang-1533` | upstream-code | [`sources/prs/tilelang/PR-1533.md`](../sources/prs/tilelang/PR-1533.md) | [Fix] Add support for non-var complement arithmetic computation (#1374) |
| `pr-tilelang-1579` | upstream-code | [`sources/prs/tilelang/PR-1579.md`](../sources/prs/tilelang/PR-1579.md) | [Layout] Support annotating loop layout in frontend |
| `pr-tilelang-1660` | upstream-code | [`sources/prs/tilelang/PR-1660.md`](../sources/prs/tilelang/PR-1660.md) | [Example] Add KDA algorithm implementation in tilelang |
| `pr-tilelang-1672` | upstream-code | [`sources/prs/tilelang/PR-1672.md`](../sources/prs/tilelang/PR-1672.md) | [Clean][Refactor] Phaseout Legacy Pass `ParallelLoopTransformer` |
| `pr-tilelang-1676` | upstream-code | [`sources/prs/tilelang/PR-1676.md`](../sources/prs/tilelang/PR-1676.md) | [Feature] Atomic Reduction Operations and Vectorization Enhancement |
| `pr-tilelang-1801` | upstream-code | [`sources/prs/tilelang/PR-1801.md`](../sources/prs/tilelang/PR-1801.md) | [BugFix] Missing Recursive Loop Var Checking in Loop Unswitching |
| `pr-tilelang-1820` | upstream-code | [`sources/prs/tilelang/PR-1820.md`](../sources/prs/tilelang/PR-1820.md) | [Bugfix] Remove mistaken coalesced_width parameter in regression test of fusedmoe kernel |
| `pr-tilelang-1827` | upstream-code | [`sources/prs/tilelang/PR-1827.md`](../sources/prs/tilelang/PR-1827.md) | [Refactor] Introduce `T.access_of` to combine `T.address_of` and `access_ptr` |
| `pr-tilelang-1839` | upstream-code | [`sources/prs/tilelang/PR-1839.md`](../sources/prs/tilelang/PR-1839.md) | [CUDA][Feature] Add packed FP32x2 math intrinsics and auto vectorized support |
| `pr-tilelang-1884` | upstream-code | [`sources/prs/tilelang/PR-1884.md`](../sources/prs/tilelang/PR-1884.md) | [Analysis] Refactor FragmentLoopChecker visiting style |
| `pr-tilelang-1962` | upstream-code | [`sources/prs/tilelang/PR-1962.md`](../sources/prs/tilelang/PR-1962.md) | [Bugfix] Fix double buffer versioning when TMA is used without warp specialization |
| `pr-tilelang-1978` | upstream-code | [`sources/prs/tilelang/PR-1978.md`](../sources/prs/tilelang/PR-1978.md) | Unified packed x2 intrinsics with multi-dtype support and bug fixes |
| `pr-tilelang-2138` | upstream-code | [`sources/prs/tilelang/PR-2138.md`](../sources/prs/tilelang/PR-2138.md) | [Refactor][Backend] Split tl.copy lowering by backend |
| `pr-tilelang-2156` | upstream-code | [`sources/prs/tilelang/PR-2156.md`](../sources/prs/tilelang/PR-2156.md) | [Refactor][Backend] Split remaining TileOps by backend |
| `pr-tilelang-2163` | upstream-code | [`sources/prs/tilelang/PR-2163.md`](../sources/prs/tilelang/PR-2163.md) | [Backend] Share common GPU tile op lowerers |
| `pr-vllm-12185` | upstream-code | [`sources/prs/vllm/PR-12185.md`](../sources/prs/vllm/PR-12185.md) | [Kernel] add triton fused moe kernel for gptq/awq |
| `pr-vllm-12303` | upstream-code | [`sources/prs/vllm/PR-12303.md`](../sources/prs/vllm/PR-12303.md) | [Hardware][Gaudi][Feature] Enable Dynamic MoE for Mixtral |
| `pr-vllm-12574` | upstream-code | [`sources/prs/vllm/PR-12574.md`](../sources/prs/vllm/PR-12574.md) | [Kernel] port sgl moe_align_block_size kernels |
| `pr-vllm-12583` | upstream-code | [`sources/prs/vllm/PR-12583.md`](../sources/prs/vllm/PR-12583.md) | Expert Parallelism (EP) Support for DeepSeek Models |
| `pr-vllm-12637` | upstream-code | [`sources/prs/vllm/PR-12637.md`](../sources/prs/vllm/PR-12637.md) | Apply torch.compile to fused_moe/grouped_topk |
| `pr-vllm-12757` | upstream-code | [`sources/prs/vllm/PR-12757.md`](../sources/prs/vllm/PR-12757.md) | [Misc] Update w2 scale loading for GPTQMarlinMoE |
| `pr-vllm-12850` | upstream-code | [`sources/prs/vllm/PR-12850.md`](../sources/prs/vllm/PR-12850.md) | Optimize moe_align_block_size for deepseek_v3 |
| `pr-vllm-13167` | upstream-code | [`sources/prs/vllm/PR-13167.md`](../sources/prs/vllm/PR-13167.md) | [Model] Deepseek GGUF support  |
| `pr-vllm-13321` | upstream-code | [`sources/prs/vllm/PR-13321.md`](../sources/prs/vllm/PR-13321.md) | [Kernel] moe wna16 cuda kernel |
| `pr-vllm-13625` | upstream-code | [`sources/prs/vllm/PR-13625.md`](../sources/prs/vllm/PR-13625.md) | [Kernel] Optimize moe intermediate_cache usage |
| `pr-vllm-13693` | upstream-code | [`sources/prs/vllm/PR-13693.md`](../sources/prs/vllm/PR-13693.md) | [BugFix]  Illegal memory access for MoE On H20 |
| `pr-vllm-13718` | upstream-code | [`sources/prs/vllm/PR-13718.md`](../sources/prs/vllm/PR-13718.md) | [core] Perf improvement for DSv3 on AMD GPUs |
| `pr-vllm-13772` | upstream-code | [`sources/prs/vllm/PR-13772.md`](../sources/prs/vllm/PR-13772.md) | Fix precommit fail in fused_moe intermediate_cache2 chunking |
| `pr-vllm-13784` | upstream-code | [`sources/prs/vllm/PR-13784.md`](../sources/prs/vllm/PR-13784.md) | [Bugfix][Quantization] Fix FP8 + EP |
| `pr-vllm-13931` | upstream-code | [`sources/prs/vllm/PR-13931.md`](../sources/prs/vllm/PR-13931.md) | [V1] EP/TP MoE + DP Attention |
| `pr-vllm-13972` | upstream-code | [`sources/prs/vllm/PR-13972.md`](../sources/prs/vllm/PR-13972.md) | [Kernel] CUTLASS grouped gemm fp8 MoE kernel |
| `pr-vllm-13974` | upstream-code | [`sources/prs/vllm/PR-13974.md`](../sources/prs/vllm/PR-13974.md) | [Misc] Print FusedMoE detail info |
| `pr-vllm-14068` | upstream-code | [`sources/prs/vllm/PR-14068.md`](../sources/prs/vllm/PR-14068.md) | [core] moe fp8 block quant tuning support |
| `pr-vllm-14245` | upstream-code | [`sources/prs/vllm/PR-14245.md`](../sources/prs/vllm/PR-14245.md) | dynamic distpatch of fp8 kernels |
| `pr-vllm-14447` | upstream-code | [`sources/prs/vllm/PR-14447.md`](../sources/prs/vllm/PR-14447.md) | [Kernel] moe wna16 marlin kernel |
| `pr-vllm-14454` | upstream-code | [`sources/prs/vllm/PR-14454.md`](../sources/prs/vllm/PR-14454.md) | [ROCm][Kernel] MoE weights padding |
| `pr-vllm-14568` | upstream-code | [`sources/prs/vllm/PR-14568.md`](../sources/prs/vllm/PR-14568.md) | permute/unpermute kernel for moe optimization |
| `pr-vllm-14681` | upstream-code | [`sources/prs/vllm/PR-14681.md`](../sources/prs/vllm/PR-14681.md) | [Bugfix][IPEX] Add `VLLM_CPU_MOE_PREPACK` to allow disabling MoE prepack when CPU does not support it |
| `pr-vllm-14967` | upstream-code | [`sources/prs/vllm/PR-14967.md`](../sources/prs/vllm/PR-14967.md) | [FEAT][ROCm] Integrate Fused MoE Kernels from AITER |
| `pr-vllm-15511` | upstream-code | [`sources/prs/vllm/PR-15511.md`](../sources/prs/vllm/PR-15511.md) | Use Cache Hinting for fused_moe kernel |
| `pr-vllm-15515` | upstream-code | [`sources/prs/vllm/PR-15515.md`](../sources/prs/vllm/PR-15515.md) | [moe][quant] add weight name case for offset |
| `pr-vllm-15587` | upstream-code | [`sources/prs/vllm/PR-15587.md`](../sources/prs/vllm/PR-15587.md) | [Quantization] Fp8 Channelwise Dynamic Per Token GroupedGEMM |
| `pr-vllm-15834` | upstream-code | [`sources/prs/vllm/PR-15834.md`](../sources/prs/vllm/PR-15834.md) | [V1] TPU - Fix fused MOE |
| `pr-vllm-15945` | upstream-code | [`sources/prs/vllm/PR-15945.md`](../sources/prs/vllm/PR-15945.md) | [Hardware][Gaudi][BugFix] fix arguments of hpu fused moe |
| `pr-vllm-15956` | upstream-code | [`sources/prs/vllm/PR-15956.md`](../sources/prs/vllm/PR-15956.md) | Modularize fused experts and integrate PPLX kernels |
| `pr-vllm-16038` | upstream-code | [`sources/prs/vllm/PR-16038.md`](../sources/prs/vllm/PR-16038.md) | [Kernel] Use moe_wna16 kernel for compressed tensors wna16 moe models |
| `pr-vllm-16071` | upstream-code | [`sources/prs/vllm/PR-16071.md`](../sources/prs/vllm/PR-16071.md) | [Kernel][Bugfix] Re-fuse triton moe weight application |
| `pr-vllm-16113` | upstream-code | [`sources/prs/vllm/PR-16113.md`](../sources/prs/vllm/PR-16113.md) | Upstream Llama4 Support to Main |
| `pr-vllm-16198` | upstream-code | [`sources/prs/vllm/PR-16198.md`](../sources/prs/vllm/PR-16198.md) | [Bug] [ROCm] Fix Llama 4 Enablement Bug on ROCm: V0 ROCmFlashAttentionImpl and Triton Fused MoE bugs |
| `pr-vllm-16263` | upstream-code | [`sources/prs/vllm/PR-16263.md`](../sources/prs/vllm/PR-16263.md) | [Hardware][AMD] Improve OAM device ID + llama4 Maverick MOE tuning |
| `pr-vllm-16362` | upstream-code | [`sources/prs/vllm/PR-16362.md`](../sources/prs/vllm/PR-16362.md) | [Hardware/NVIDIA/Kernel] [Functional Enablement] [1/N] Enable nvidia/DeepSeek-R1-FP4 Model |
| `pr-vllm-16366` | upstream-code | [`sources/prs/vllm/PR-16366.md`](../sources/prs/vllm/PR-16366.md) | [Kernel] Support W8A8 channel-wise weights and per-token activations in triton fused_moe_kernel |
| `pr-vllm-16537` | upstream-code | [`sources/prs/vllm/PR-16537.md`](../sources/prs/vllm/PR-16537.md) | Enable PTPC FP8 for CompressedTensorsW8A8Fp8MoEMethod (triton fused_moe) |
| `pr-vllm-16674` | upstream-code | [`sources/prs/vllm/PR-16674.md`](../sources/prs/vllm/PR-16674.md) | [ROCM] enable aiter fused moe kernel for llama4 bf16 checkpoints |
| `pr-vllm-16727` | upstream-code | [`sources/prs/vllm/PR-16727.md`](../sources/prs/vllm/PR-16727.md) | [ROCm] Add aiter tkw1 kernel for Llama4 fp8 |
| `pr-vllm-16752` | upstream-code | [`sources/prs/vllm/PR-16752.md`](../sources/prs/vllm/PR-16752.md) | [FEAT] [ROCm]: AITER Fused MOE V1 Support |
| `pr-vllm-16756` | upstream-code | [`sources/prs/vllm/PR-16756.md`](../sources/prs/vllm/PR-16756.md) | [torch.compile][ROCm] Fuse quantization onto attention using a torch.compile pass |
| `pr-vllm-16801` | upstream-code | [`sources/prs/vllm/PR-16801.md`](../sources/prs/vllm/PR-16801.md) | [BugFix] Accuracy fix for llama4 int4 - improperly casted scales |
| `pr-vllm-16850` | upstream-code | [`sources/prs/vllm/PR-16850.md`](../sources/prs/vllm/PR-16850.md) | [Kernel] some optimizations for dense marlin and moe marlin |
| `pr-vllm-16854` | upstream-code | [`sources/prs/vllm/PR-16854.md`](../sources/prs/vllm/PR-16854.md) | [Bugfix] Fix moe weight losing all extra attrs after `process_weights_after_loading`. |
| `pr-vllm-16861` | upstream-code | [`sources/prs/vllm/PR-16861.md`](../sources/prs/vllm/PR-16861.md) | [Kernel] Add expert_map support to Cutlass FP8 MOE |
| `pr-vllm-17110` | upstream-code | [`sources/prs/vllm/PR-17110.md`](../sources/prs/vllm/PR-17110.md) | [FEAT] [ROCm]: Add AITER CK 2 Stages MoE support |
| `pr-vllm-17139` | upstream-code | [`sources/prs/vllm/PR-17139.md`](../sources/prs/vllm/PR-17139.md) | [ROCm][FP8][Kernel] FP8 quantization fused into Custom Paged Attention |
| `pr-vllm-17523` | upstream-code | [`sources/prs/vllm/PR-17523.md`](../sources/prs/vllm/PR-17523.md) | [FEAT][ROCm]: Support AITER MLA on V1 Engine |
| `pr-vllm-17687` | upstream-code | [`sources/prs/vllm/PR-17687.md`](../sources/prs/vllm/PR-17687.md) | [Kernel] fp4 marlin kernel |
| `pr-vllm-17912` | upstream-code | [`sources/prs/vllm/PR-17912.md`](../sources/prs/vllm/PR-17912.md) | [BugFix][AMD] Compatible patch for AITER lib after 04/20 |
| `pr-vllm-18321` | upstream-code | [`sources/prs/vllm/PR-18321.md`](../sources/prs/vllm/PR-18321.md) | [Model]: Fused MoE for nomic-embed-text-v2-moe |
| `pr-vllm-18343` | upstream-code | [`sources/prs/vllm/PR-18343.md`](../sources/prs/vllm/PR-18343.md) | [Feature] Expert Parallelism Load Balancer (EPLB) |
| `pr-vllm-18762` | upstream-code | [`sources/prs/vllm/PR-18762.md`](../sources/prs/vllm/PR-18762.md) | [Kernel] Integrate CUTLASS MoE kernel with PPLX |
| `pr-vllm-18864` | upstream-code | [`sources/prs/vllm/PR-18864.md`](../sources/prs/vllm/PR-18864.md) | [Kernel] Enable fp8 support for pplx and BatchedTritonExperts. |
| `pr-vllm-18990` | upstream-code | [`sources/prs/vllm/PR-18990.md`](../sources/prs/vllm/PR-18990.md) | [ROCm] [AITER] [Bugfix] Patch for AITER commit `648764942e552a8bb5fe16026703716a81f05374` |
| `pr-vllm-19110` | upstream-code | [`sources/prs/vllm/PR-19110.md`](../sources/prs/vllm/PR-19110.md) | [Hardware][NVIDIA] FP4 MoE kernel optimization |
| `pr-vllm-19168` | upstream-code | [`sources/prs/vllm/PR-19168.md`](../sources/prs/vllm/PR-19168.md) | [Kernels] Add activation chunking logic to FusedMoEModularKernel |
| `pr-vllm-19346` | upstream-code | [`sources/prs/vllm/PR-19346.md`](../sources/prs/vllm/PR-19346.md) | [Kernel] Apply torch.Tag.needs_fixed_stride_order only for torch==2.6.0 |
| `pr-vllm-19667` | upstream-code | [`sources/prs/vllm/PR-19667.md`](../sources/prs/vllm/PR-19667.md) | [Kernels] Use empty for modular MoE workspaces |
| `pr-vllm-19757` | upstream-code | [`sources/prs/vllm/PR-19757.md`](../sources/prs/vllm/PR-19757.md) | [feat]: CUTLASS block scaled group gemm for SM100 |
| `pr-vllm-19820` | upstream-code | [`sources/prs/vllm/PR-19820.md`](../sources/prs/vllm/PR-19820.md) | [Feature] Integrate new deepgemm |
| `pr-vllm-19990` | upstream-code | [`sources/prs/vllm/PR-19990.md`](../sources/prs/vllm/PR-19990.md) | [Quantization] Add compressed-tensors NVFP4 MoE Support |
| `pr-vllm-20087` | upstream-code | [`sources/prs/vllm/PR-20087.md`](../sources/prs/vllm/PR-20087.md) |  [Feature] Integrate SM100 DeepGEMM support |
| `pr-vllm-20152` | upstream-code | [`sources/prs/vllm/PR-20152.md`](../sources/prs/vllm/PR-20152.md) | [Bugfix] Mark 'hidden_states' as mutable in moe_forward registration. |
| `pr-vllm-20166` | upstream-code | [`sources/prs/vllm/PR-20166.md`](../sources/prs/vllm/PR-20166.md) | [Bugfix] Fix topk_ids indices_type for CUTLASS w8a8 FP8 MoE |
| `pr-vllm-20167` | upstream-code | [`sources/prs/vllm/PR-20167.md`](../sources/prs/vllm/PR-20167.md) | [Bugfix] Fix Maverick correctness by filling zero to cache space in cutlass_moe |
| `pr-vllm-20270` | upstream-code | [`sources/prs/vllm/PR-20270.md`](../sources/prs/vllm/PR-20270.md) | [V1] [ROCm] Enable EP with AITER Fused MoE |
| `pr-vllm-20332` | upstream-code | [`sources/prs/vllm/PR-20332.md`](../sources/prs/vllm/PR-20332.md) | [Misc] DP : Add ExpertTokensMetadata |
| `pr-vllm-20453` | upstream-code | [`sources/prs/vllm/PR-20453.md`](../sources/prs/vllm/PR-20453.md) | Support Llama 4 for cutlass_moe_fp4 |
| `pr-vllm-20457` | upstream-code | [`sources/prs/vllm/PR-20457.md`](../sources/prs/vllm/PR-20457.md) | Support Llama 4 for fused_marlin_moe |
| `pr-vllm-20509` | upstream-code | [`sources/prs/vllm/PR-20509.md`](../sources/prs/vllm/PR-20509.md) | [Bugfix] Fix missing per_act_token parameter in compressed_tensors_moe |
| `pr-vllm-20640` | upstream-code | [`sources/prs/vllm/PR-20640.md`](../sources/prs/vllm/PR-20640.md) | [feat] enable SM100 CUTLASS block scaled group gemm for smaller batch sizes |
| `pr-vllm-20762` | upstream-code | [`sources/prs/vllm/PR-20762.md`](../sources/prs/vllm/PR-20762.md) | [Performance] Performance improvements in non-blockwise fp8 CUTLASS MoE |
| `pr-vllm-20781` | upstream-code | [`sources/prs/vllm/PR-20781.md`](../sources/prs/vllm/PR-20781.md) | [fix]: disable cutlass block scaled group gemm for EP |
| `pr-vllm-20825` | upstream-code | [`sources/prs/vllm/PR-20825.md`](../sources/prs/vllm/PR-20825.md) | [Bugfix] Fix a couple PPLX+CUTLASS MoE bugs |
| `pr-vllm-20833` | upstream-code | [`sources/prs/vllm/PR-20833.md`](../sources/prs/vllm/PR-20833.md) | [Bug] Fix DeepGemm for EP low latency case |
| `pr-vllm-20841` | upstream-code | [`sources/prs/vllm/PR-20841.md`](../sources/prs/vllm/PR-20841.md) | [Perf] Use Triton instead of Torch for DeepGEMM Per Token Group Quant |
| `pr-vllm-20903` | upstream-code | [`sources/prs/vllm/PR-20903.md`](../sources/prs/vllm/PR-20903.md) | [Kernel] DeepGemm MoE : Integrate triton permute / unpermute kernels  |
| `pr-vllm-21003` | upstream-code | [`sources/prs/vllm/PR-21003.md`](../sources/prs/vllm/PR-21003.md) | Support mnnvl all2allv from Flashinfer |
| `pr-vllm-21116` | upstream-code | [`sources/prs/vllm/PR-21116.md`](../sources/prs/vllm/PR-21116.md) | [perf] Add fused MLA QKV + strided layernorm |
| `pr-vllm-21121` | upstream-code | [`sources/prs/vllm/PR-21121.md`](../sources/prs/vllm/PR-21121.md) | [Bugfix] Allocate less memory in non-batched CUTLASS MoE |
| `pr-vllm-21166` | upstream-code | [`sources/prs/vllm/PR-21166.md`](../sources/prs/vllm/PR-21166.md) | [Feature][OCP MX] Support mxfp6 and mixed mxfp6-mxfp4 |
| `pr-vllm-21229` | upstream-code | [`sources/prs/vllm/PR-21229.md`](../sources/prs/vllm/PR-21229.md) | [Feature][Kernel]FusedMoE LoRA |
| `pr-vllm-21331` | upstream-code | [`sources/prs/vllm/PR-21331.md`](../sources/prs/vllm/PR-21331.md) | Support Tensorrt-LLM MoE fp4 for low-latency |
| `pr-vllm-21340` | upstream-code | [`sources/prs/vllm/PR-21340.md`](../sources/prs/vllm/PR-21340.md) | [TPU][Bugfix] fix moe layer |
| `pr-vllm-21408` | upstream-code | [`sources/prs/vllm/PR-21408.md`](../sources/prs/vllm/PR-21408.md) | Update flashinfer CUTLASS NVFP4 MoE Kernel to use per expert global scaling factor |
| `pr-vllm-21411` | upstream-code | [`sources/prs/vllm/PR-21411.md`](../sources/prs/vllm/PR-21411.md) | [NVIDIA] Explicitly disable shuffled weights for flashinfer blockscale moe fp8 kernels |
| `pr-vllm-21497` | upstream-code | [`sources/prs/vllm/PR-21497.md`](../sources/prs/vllm/PR-21497.md) | [MoE] More balanced expert sharding |
| `pr-vllm-21499` | upstream-code | [`sources/prs/vllm/PR-21499.md`](../sources/prs/vllm/PR-21499.md) | [NVIDIA] Fix Llama4 Scout FP4 functionality issues |
| `pr-vllm-21643` | upstream-code | [`sources/prs/vllm/PR-21643.md`](../sources/prs/vllm/PR-21643.md) | [xpu]support moe models on XPU platform |
| `pr-vllm-21716` | upstream-code | [`sources/prs/vllm/PR-21716.md`](../sources/prs/vllm/PR-21716.md) | [NVIDIA] Support Flashinfer TRTLLM FP8-q/kv/out Attention Kernel |
| `pr-vllm-21733` | upstream-code | [`sources/prs/vllm/PR-21733.md`](../sources/prs/vllm/PR-21733.md) | feat: Add Support GPTQ Quantization MOE on ROCM vllm serve |
| `pr-vllm-21963` | upstream-code | [`sources/prs/vllm/PR-21963.md`](../sources/prs/vllm/PR-21963.md) | Fix Flashinfer CUTLASS MOE Allgather |
| `pr-vllm-22339` | upstream-code | [`sources/prs/vllm/PR-22339.md`](../sources/prs/vllm/PR-22339.md) | [gpt-oss] flashinfer mxfp4 |
| `pr-vllm-22421` | upstream-code | [`sources/prs/vllm/PR-22421.md`](../sources/prs/vllm/PR-22421.md) | [gpt-oss] triton kernel mxfp4 |
| `pr-vllm-22511` | upstream-code | [`sources/prs/vllm/PR-22511.md`](../sources/prs/vllm/PR-22511.md) | Fix Llama4 FlashInfer FP4 MoE issues |
| `pr-vllm-22535` | upstream-code | [`sources/prs/vllm/PR-22535.md`](../sources/prs/vllm/PR-22535.md) | Fix torch version check for SM100 mxfp4  |
| `pr-vllm-22703` | upstream-code | [`sources/prs/vllm/PR-22703.md`](../sources/prs/vllm/PR-22703.md) | [NVIDIA] Support Flashinfer TRTLLM FP8-q/kv NVFP4-out Attention Kernel |
| `pr-vllm-22887` | upstream-code | [`sources/prs/vllm/PR-22887.md`](../sources/prs/vllm/PR-22887.md) | [XPU] support data parallel for MoE models on XPU |
| `pr-vllm-22895` | upstream-code | [`sources/prs/vllm/PR-22895.md`](../sources/prs/vllm/PR-22895.md) | [Kernel] Added flashinfer fp8 per-tensor gemms |
| `pr-vllm-23008` | upstream-code | [`sources/prs/vllm/PR-23008.md`](../sources/prs/vllm/PR-23008.md) | Use Blackwell FlashInfer MXFP4 MoE by default if available  |
| `pr-vllm-23045` | upstream-code | [`sources/prs/vllm/PR-23045.md`](../sources/prs/vllm/PR-23045.md) | [Kernel] CUTLASS MoE FP8: Integrate cuda moe permute/unpermute |
| `pr-vllm-23123` | upstream-code | [`sources/prs/vllm/PR-23123.md`](../sources/prs/vllm/PR-23123.md) | Add routed_scaling_factor to MoE grouped topk |
| `pr-vllm-23125` | upstream-code | [`sources/prs/vllm/PR-23125.md`](../sources/prs/vllm/PR-23125.md) | [Bugfix] Fix accuracy issue when using flashinfer cutlass moe, TP=1 and modelopt. |
| `pr-vllm-23146` | upstream-code | [`sources/prs/vllm/PR-23146.md`](../sources/prs/vllm/PR-23146.md) | [CPU] add cpu fused moe pytorch native implementation |
| `pr-vllm-23265` | upstream-code | [`sources/prs/vllm/PR-23265.md`](../sources/prs/vllm/PR-23265.md) | [Perf] Small optimizations for silu_mul_fp8_quant_deep_gemm |
| `pr-vllm-23273` | upstream-code | [`sources/prs/vllm/PR-23273.md`](../sources/prs/vllm/PR-23273.md) | [Kernels] Overlap shared experts with send/recv |
| `pr-vllm-23274` | upstream-code | [`sources/prs/vllm/PR-23274.md`](../sources/prs/vllm/PR-23274.md) | [Kernel] Add fused grouped_topk kernel for MoE |
| `pr-vllm-23537` | upstream-code | [`sources/prs/vllm/PR-23537.md`](../sources/prs/vllm/PR-23537.md) | Update Flashinfer to  0.2.14.post1 |
| `pr-vllm-23608` | upstream-code | [`sources/prs/vllm/PR-23608.md`](../sources/prs/vllm/PR-23608.md) | DP/EP Support for gpt-oss with deepep-ht comm kernel on SM100 |
| `pr-vllm-23647` | upstream-code | [`sources/prs/vllm/PR-23647.md`](../sources/prs/vllm/PR-23647.md) | [Flashinfer] Support Flashinfer TRTLLM FP8-qkv BF16/FP16-out Attention Kernel |
| `pr-vllm-23666` | upstream-code | [`sources/prs/vllm/PR-23666.md`](../sources/prs/vllm/PR-23666.md) | [Feature] Add Hopper DeepGEMM E8M0 for DeepSeekV3.1 scale_fmt |
| `pr-vllm-23671` | upstream-code | [`sources/prs/vllm/PR-23671.md`](../sources/prs/vllm/PR-23671.md) | [NVIDIA] Support SiluMul + NVFP4 quant fusion |
| `pr-vllm-23693` | upstream-code | [`sources/prs/vllm/PR-23693.md`](../sources/prs/vllm/PR-23693.md) | [Core/DBO][1/N] Add Dual-Batch Overlap mechanism to VLLM |
| `pr-vllm-23696` | upstream-code | [`sources/prs/vllm/PR-23696.md`](../sources/prs/vllm/PR-23696.md) | [Kernel][B200] `mxfp4` fused cutlass moe |
| `pr-vllm-23727` | upstream-code | [`sources/prs/vllm/PR-23727.md`](../sources/prs/vllm/PR-23727.md) | [Bugfix][Misc] Fix silu_and_mul_nvfp4_quant issue and extract common utils for nvfp4 kernel source files |
| `pr-vllm-23745` | upstream-code | [`sources/prs/vllm/PR-23745.md`](../sources/prs/vllm/PR-23745.md) | [Feat][EPLB] A novel static EPLB placement strategy for MoE models. |
| `pr-vllm-23809` | upstream-code | [`sources/prs/vllm/PR-23809.md`](../sources/prs/vllm/PR-23809.md) | [fix]: add Arm 4bit fused moe support |
| `pr-vllm-23819` | upstream-code | [`sources/prs/vllm/PR-23819.md`](../sources/prs/vllm/PR-23819.md) | [Model][gpt-oss] Support DP+EP for GPT-OSS with FlashInfer trtllm-gen MoE |
| `pr-vllm-23991` | upstream-code | [`sources/prs/vllm/PR-23991.md`](../sources/prs/vllm/PR-23991.md) | [Model] Add LongCat-Flash  |
| `pr-vllm-24248` | upstream-code | [`sources/prs/vllm/PR-24248.md`](../sources/prs/vllm/PR-24248.md) | [PERF] Allreduce fusion. Support torch native matching. Tuning of the thresholds |
| `pr-vllm-24722` | upstream-code | [`sources/prs/vllm/PR-24722.md`](../sources/prs/vllm/PR-24722.md) | [Kernel][Quantization] add w4a8 support for marlin kernel |
| `pr-vllm-24833` | upstream-code | [`sources/prs/vllm/PR-24833.md`](../sources/prs/vllm/PR-24833.md) | [Bugfix] Fix accuracy issue for silu_mul + nvfp4 quant fusion kernel |
| `pr-vllm-25193` | upstream-code | [`sources/prs/vllm/PR-25193.md`](../sources/prs/vllm/PR-25193.md) | [Compile] Fix Compile Warning for Ignoring `MIN_BLOCK_PER_SM` |
| `pr-vllm-25503` | upstream-code | [`sources/prs/vllm/PR-25503.md`](../sources/prs/vllm/PR-25503.md) | feat: BF16 FlashInfer Fused Cutlass MOE for Hopper and Blackwell Expert Parallel |
| `pr-vllm-25774` | upstream-code | [`sources/prs/vllm/PR-25774.md`](../sources/prs/vllm/PR-25774.md) | Fuse RoPE and MLA KV-cache write |
| `pr-vllm-25987` | upstream-code | [`sources/prs/vllm/PR-25987.md`](../sources/prs/vllm/PR-25987.md) | [Bugfix] Allow skipping MoE in NVFP4 (fix for MTP) |
| `pr-vllm-25990` | upstream-code | [`sources/prs/vllm/PR-25990.md`](../sources/prs/vllm/PR-25990.md) | [MoE] Nvfp4 Masked Gemm: Add flashinfer grouped_gemm_nt_masked |
| `pr-vllm-26135` | upstream-code | [`sources/prs/vllm/PR-26135.md`](../sources/prs/vllm/PR-26135.md) | [ModelOpt] Load w13/w2_input_scale for all experts, nvfp4 |
| `pr-vllm-26322` | upstream-code | [`sources/prs/vllm/PR-26322.md`](../sources/prs/vllm/PR-26322.md) | [Bug] Fix Shape Validation for Fallback while Enabling E8M0 for DeepGEMM |
| `pr-vllm-26440` | upstream-code | [`sources/prs/vllm/PR-26440.md`](../sources/prs/vllm/PR-26440.md) | [Performance] Dual stream execution of "shared_experts" and "selected_experts" inside FusedMoE |
| `pr-vllm-26534` | upstream-code | [`sources/prs/vllm/PR-26534.md`](../sources/prs/vllm/PR-26534.md) | Move query quantization to attention layer for Flashinfer & Triton. |
| `pr-vllm-26545` | upstream-code | [`sources/prs/vllm/PR-26545.md`](../sources/prs/vllm/PR-26545.md) | [ROCM] MoE fp4 CK kernel |
| `pr-vllm-26714` | upstream-code | [`sources/prs/vllm/PR-26714.md`](../sources/prs/vllm/PR-26714.md) | [NVIDIA] [Perf] Update to leverage flashinfer trtllm FP4 MOE throughput kernel |
| `pr-vllm-26729` | upstream-code | [`sources/prs/vllm/PR-26729.md`](../sources/prs/vllm/PR-26729.md) | [Bugfix] Fix gpt-oss w4a8 DP/EP on B200 |
| `pr-vllm-27134` | upstream-code | [`sources/prs/vllm/PR-27134.md`](../sources/prs/vllm/PR-27134.md) | [Kernels] Enable FlashInfer FP8 Blockscale on SM90 (for TEP DSR1) |
| `pr-vllm-27146` | upstream-code | [`sources/prs/vllm/PR-27146.md`](../sources/prs/vllm/PR-27146.md) | [torch.compile] Enable silu_mul_fp8_quant fusion without custom ops enabled |
| `pr-vllm-27223` | upstream-code | [`sources/prs/vllm/PR-27223.md`](../sources/prs/vllm/PR-27223.md) | Flashinfer_CUTLASS_MOE fuses quantization for TP |
| `pr-vllm-27255` | upstream-code | [`sources/prs/vllm/PR-27255.md`](../sources/prs/vllm/PR-27255.md) | Bugfix: Cutlass FP8 FusedMoE bad scaling factors |
| `pr-vllm-27261` | upstream-code | [`sources/prs/vllm/PR-27261.md`](../sources/prs/vllm/PR-27261.md) | Feature: Support Relu2 in FusedMoE fp8 cutlass path |
| `pr-vllm-27492` | upstream-code | [`sources/prs/vllm/PR-27492.md`](../sources/prs/vllm/PR-27492.md) | [Performance] Support FP8 flashinfer TRTLLM MOE on Qwen3 and Qwen-3next |
| `pr-vllm-27532` | upstream-code | [`sources/prs/vllm/PR-27532.md`](../sources/prs/vllm/PR-27532.md) | [Attention] Use sparse prefill kernel for fp8 kv-cache in DeepSeek-v3.2 |
| `pr-vllm-27883` | upstream-code | [`sources/prs/vllm/PR-27883.md`](../sources/prs/vllm/PR-27883.md) | [Performance] Fused blockwise quant RMS norm |
| `pr-vllm-27897` | upstream-code | [`sources/prs/vllm/PR-27897.md`](../sources/prs/vllm/PR-27897.md) | [Performance][B200] Fix deepgemm prologue |
| `pr-vllm-28124` | upstream-code | [`sources/prs/vllm/PR-28124.md`](../sources/prs/vllm/PR-28124.md) | [Perf][DeepSeek] Add sigmoid+bias fusion to fused_grouped_topk from TRTLLM |
| `pr-vllm-28166` | upstream-code | [`sources/prs/vllm/PR-28166.md`](../sources/prs/vllm/PR-28166.md) | [flashinfer] fix FI all2all with FI cutlass moe |
| `pr-vllm-28284` | upstream-code | [`sources/prs/vllm/PR-28284.md`](../sources/prs/vllm/PR-28284.md) | [Feature] Support recording expert indices for rollout router replay |
| `pr-vllm-28358` | upstream-code | [`sources/prs/vllm/PR-28358.md`](../sources/prs/vllm/PR-28358.md) | [Performance][B200] silu_mul_quant: pack scales in int32 |
| `pr-vllm-28377` | upstream-code | [`sources/prs/vllm/PR-28377.md`](../sources/prs/vllm/PR-28377.md) | [Bugfix][EPLB] Disabled shared expert overlap when EPLB is enabled |
| `pr-vllm-28718` | upstream-code | [`sources/prs/vllm/PR-28718.md`](../sources/prs/vllm/PR-28718.md) | [Feature] Prefill Context Parallel (PCP) basic support |
| `pr-vllm-28841` | upstream-code | [`sources/prs/vllm/PR-28841.md`](../sources/prs/vllm/PR-28841.md) | [Bugfix] Fix GPT-OSS AR+NORM fusion |
| `pr-vllm-28878` | upstream-code | [`sources/prs/vllm/PR-28878.md`](../sources/prs/vllm/PR-28878.md) | [Bugfix] Make compressed-tensors MoEs respect ignored layers |
| `pr-vllm-29004` | upstream-code | [`sources/prs/vllm/PR-29004.md`](../sources/prs/vllm/PR-29004.md) | [Feat] Support non-gated activations in NVFP4 modelopt path |
| `pr-vllm-29222` | upstream-code | [`sources/prs/vllm/PR-29222.md`](../sources/prs/vllm/PR-29222.md) | [LoRA] Optimize 3D MoE logic |
| `pr-vllm-29354` | upstream-code | [`sources/prs/vllm/PR-29354.md`](../sources/prs/vllm/PR-29354.md) | Add unpermute-aware fused MoE path and small-batch fallback |
| `pr-vllm-29439` | upstream-code | [`sources/prs/vllm/PR-29439.md`](../sources/prs/vllm/PR-29439.md) | [Bugfix] Fix grouped_topk pytorch impl when num_experts can't be grouped properly |
| `pr-vllm-29642` | upstream-code | [`sources/prs/vllm/PR-29642.md`](../sources/prs/vllm/PR-29642.md) | [Kernel][MoE] optimize `moe_align_block_size` |
| `pr-vllm-29691` | upstream-code | [`sources/prs/vllm/PR-29691.md`](../sources/prs/vllm/PR-29691.md) | [Kernel]Support W4A8 Grouped GEMM on Hopper |
| `pr-vllm-29757` | upstream-code | [`sources/prs/vllm/PR-29757.md`](../sources/prs/vllm/PR-29757.md) | Add Mistral Large 3 and Ministral 3 |
| `pr-vllm-29773` | upstream-code | [`sources/prs/vllm/PR-29773.md`](../sources/prs/vllm/PR-29773.md) | [ROCm] [Fused Moe EP] Use binary expert mask for aiter fused moe kernel |
| `pr-vllm-29775` | upstream-code | [`sources/prs/vllm/PR-29775.md`](../sources/prs/vllm/PR-29775.md) | [ROCm][MXFP4] Infer w4a4 quant method in rocm aiter fused moe |
| `pr-vllm-29804` | upstream-code | [`sources/prs/vllm/PR-29804.md`](../sources/prs/vllm/PR-29804.md) | [EPLB] Support EPLB w/ NVFP4 |
| `pr-vllm-29935` | upstream-code | [`sources/prs/vllm/PR-29935.md`](../sources/prs/vllm/PR-29935.md) | [moe] Use enable_chunking func (to support disabling chunking) |
| `pr-vllm-29936` | upstream-code | [`sources/prs/vllm/PR-29936.md`](../sources/prs/vllm/PR-29936.md) | [moe] Allow disabling DP chunking |
| `pr-vllm-30014` | upstream-code | [`sources/prs/vllm/PR-30014.md`](../sources/prs/vllm/PR-30014.md) | [Perf] Do FP4 quant before All gather on flashinfer trtllmgen MOE  |
| `pr-vllm-30210` | upstream-code | [`sources/prs/vllm/PR-30210.md`](../sources/prs/vllm/PR-30210.md) | [Bugfix]: Fix glm46 awq marlin moe wna16 compatibility |
| `pr-vllm-30254` | upstream-code | [`sources/prs/vllm/PR-30254.md`](../sources/prs/vllm/PR-30254.md) | gptq marlin quantization support for fused moe with lora |
| `pr-vllm-30286` | upstream-code | [`sources/prs/vllm/PR-30286.md`](../sources/prs/vllm/PR-30286.md) | [LoRA] Support Quantized Adapters |
| `pr-vllm-30357` | upstream-code | [`sources/prs/vllm/PR-30357.md`](../sources/prs/vllm/PR-30357.md) | [ROCm][Quantization] GPT OSS Upstream MoE wmxfp4_afp8 with static scales |
| `pr-vllm-30484` | upstream-code | [`sources/prs/vllm/PR-30484.md`](../sources/prs/vllm/PR-30484.md) | [Feature] Add SM103 (Blackwell Ultra) Support to vLLM |
| `pr-vllm-30585` | upstream-code | [`sources/prs/vllm/PR-30585.md`](../sources/prs/vllm/PR-30585.md) | [Bugfix] Fix Triton FusedMoE LoRA |
| `pr-vllm-30647` | upstream-code | [`sources/prs/vllm/PR-30647.md`](../sources/prs/vllm/PR-30647.md) | [Perf] Eliminate padding and slicing op for GPT-OSS with Flashinfer MXFP4 MXFP8 MoE |
| `pr-vllm-30716` | upstream-code | [`sources/prs/vllm/PR-30716.md`](../sources/prs/vllm/PR-30716.md) | fused_moe_lora PDL improvements |
| `pr-vllm-30802` | upstream-code | [`sources/prs/vllm/PR-30802.md`](../sources/prs/vllm/PR-30802.md) | Add support for LoRA adapters in Nemotron-H models |
| `pr-vllm-30897` | upstream-code | [`sources/prs/vllm/PR-30897.md`](../sources/prs/vllm/PR-30897.md) | [NVFP4][Perf] Tune NVFP4 input quant kernel for small batch size |
| `pr-vllm-31003` | upstream-code | [`sources/prs/vllm/PR-31003.md`](../sources/prs/vllm/PR-31003.md) | [Mics] add pcp basic support to MoE model |
| `pr-vllm-31055` | upstream-code | [`sources/prs/vllm/PR-31055.md`](../sources/prs/vllm/PR-31055.md) | [Bugfix] Fix GLM-4 MoE router logits dtype for data parallel chunking |
| `pr-vllm-31104` | upstream-code | [`sources/prs/vllm/PR-31104.md`](../sources/prs/vllm/PR-31104.md) | [BugFix] LoRA: Support loading base_layer of experts |
| `pr-vllm-31246` | upstream-code | [`sources/prs/vllm/PR-31246.md`](../sources/prs/vllm/PR-31246.md) | [Kernel] Add topk_sigmoid kernel |
| `pr-vllm-31317` | upstream-code | [`sources/prs/vllm/PR-31317.md`](../sources/prs/vllm/PR-31317.md) | pin lora_b moe weights on cpu |
| `pr-vllm-31502` | upstream-code | [`sources/prs/vllm/PR-31502.md`](../sources/prs/vllm/PR-31502.md) | [Bugfix][ROCm] Fix Static Quant Issue |
| `pr-vllm-31528` | upstream-code | [`sources/prs/vllm/PR-31528.md`](../sources/prs/vllm/PR-31528.md) | [FIX] Add NO_MUL activation support for modular kernel path |
| `pr-vllm-31531` | upstream-code | [`sources/prs/vllm/PR-31531.md`](../sources/prs/vllm/PR-31531.md) | Use the same memory for workspace13 and fused_output. |
| `pr-vllm-31534` | upstream-code | [`sources/prs/vllm/PR-31534.md`](../sources/prs/vllm/PR-31534.md) | [Fix] Align fused moe lora_b shape with peft |
| `pr-vllm-31742` | upstream-code | [`sources/prs/vllm/PR-31742.md`](../sources/prs/vllm/PR-31742.md) | [Bugfix] Fix Broken ModelOpt NVFP4 MoE |
| `pr-vllm-31777` | upstream-code | [`sources/prs/vllm/PR-31777.md`](../sources/prs/vllm/PR-31777.md) | [LoRA]Disable linear LoRA  kernel PDL |
| `pr-vllm-31916` | upstream-code | [`sources/prs/vllm/PR-31916.md`](../sources/prs/vllm/PR-31916.md) | [1/N][Attention] Restructure attention: move files |
| `pr-vllm-32064` | upstream-code | [`sources/prs/vllm/PR-32064.md`](../sources/prs/vllm/PR-32064.md) | [5/N][Attention] Finish eliminating `vllm/attention` folder |
| `pr-vllm-32195` | upstream-code | [`sources/prs/vllm/PR-32195.md`](../sources/prs/vllm/PR-32195.md) | Add TMA support to fused_moe_lora kernel |
| `pr-vllm-32437` | upstream-code | [`sources/prs/vllm/PR-32437.md`](../sources/prs/vllm/PR-32437.md) | [Hardware][SM100] Add TRTLLM Kernel for INT4 W4A16 Kernel. |
| `pr-vllm-32520` | upstream-code | [`sources/prs/vllm/PR-32520.md`](../sources/prs/vllm/PR-32520.md) | [Perf][Kernel] Optimize FP4 quantization kernels (SM100F) |
| `pr-vllm-32954` | upstream-code | [`sources/prs/vllm/PR-32954.md`](../sources/prs/vllm/PR-32954.md) | [NVIDIA] [feat] Integrate flashinfer Trtllmgen bf16 moe |
| `pr-vllm-33174` | upstream-code | [`sources/prs/vllm/PR-33174.md`](../sources/prs/vllm/PR-33174.md) | Add support for Mistral Large 3 inference with Flashinfer MoE |
| `pr-vllm-33255` | upstream-code | [`sources/prs/vllm/PR-33255.md`](../sources/prs/vllm/PR-33255.md) | [Bugfix] Fix quant RMS norm fusion for quantization with TMA-aligned scales |
| `pr-vllm-33417` | upstream-code | [`sources/prs/vllm/PR-33417.md`](../sources/prs/vllm/PR-33417.md) | fix: Add SM120 (RTX Blackwell) support for FlashInfer CUTLASS NVFP4 MoE kernels |
| `pr-vllm-33506` | upstream-code | [`sources/prs/vllm/PR-33506.md`](../sources/prs/vllm/PR-33506.md) | [Kernel] Support Flashinfer trtllm fused MoE non gated FP8 & NVFP4 |
| `pr-vllm-34260` | upstream-code | [`sources/prs/vllm/PR-34260.md`](../sources/prs/vllm/PR-34260.md) | [Model Bash]: Improve FP8 Oracle for Config Specific Kernel Selection |
| `pr-vllm-34389` | upstream-code | [`sources/prs/vllm/PR-34389.md`](../sources/prs/vllm/PR-34389.md) | [Custom Ops] Add functional + out variant for scaled_fp4_quant |
| `pr-vllm-34478` | upstream-code | [`sources/prs/vllm/PR-34478.md`](../sources/prs/vllm/PR-34478.md) | [Model] Add NVFP4 quantization support for Step3.5-Flash |
| `pr-vllm-34494` | upstream-code | [`sources/prs/vllm/PR-34494.md`](../sources/prs/vllm/PR-34494.md) | [Bugfix] Handle num_expert_group=None in flashinfer block-scale FP8 MoE |
| `pr-vllm-34556` | upstream-code | [`sources/prs/vllm/PR-34556.md`](../sources/prs/vllm/PR-34556.md) | [Quantization] add humming quantization kernel |
| `pr-vllm-34758` | upstream-code | [`sources/prs/vllm/PR-34758.md`](../sources/prs/vllm/PR-34758.md) | [Model Bash] DeepSeek R1 BF16 Min Latency QKV A GEMM (0.5% E2E Speedup) |
| `pr-vllm-34924` | upstream-code | [`sources/prs/vllm/PR-34924.md`](../sources/prs/vllm/PR-34924.md) | [Perf] Enable FlashInfer DeepGEMM swapAB on SM90 by default |
| `pr-vllm-35121` | upstream-code | [`sources/prs/vllm/PR-35121.md`](../sources/prs/vllm/PR-35121.md) | [Performance] Cublas Bf16 Gate with Fp32 Output |
| `pr-vllm-35123` | upstream-code | [`sources/prs/vllm/PR-35123.md`](../sources/prs/vllm/PR-35123.md) | [Bugfix] Fix DSV3 kernels breaking _C and _moe_C on unsupported arches |
| `pr-vllm-35161` | upstream-code | [`sources/prs/vllm/PR-35161.md`](../sources/prs/vllm/PR-35161.md) | [Bugfix] Fix expert_ids padding values in moe_align_block_size kernel |
| `pr-vllm-35210` | upstream-code | [`sources/prs/vllm/PR-35210.md`](../sources/prs/vllm/PR-35210.md) | [BugFix] Fix fp4 quant kernel on CUDA 12.8 |
| `pr-vllm-35382` | upstream-code | [`sources/prs/vllm/PR-35382.md`](../sources/prs/vllm/PR-35382.md) | fix(mxfp4): return is_monolithic=False when LoRA is enabled for Triton backend |
| `pr-vllm-35448` | upstream-code | [`sources/prs/vllm/PR-35448.md`](../sources/prs/vllm/PR-35448.md) | [Quant][Feature] Support online MXFP8 quantization for MoE and dense models |
| `pr-vllm-35777` | upstream-code | [`sources/prs/vllm/PR-35777.md`](../sources/prs/vllm/PR-35777.md) | [Kernel] Add fused_sigmoid_gating_delta_rule_update kernel for Qwen3 Next |
| `pr-vllm-35927` | upstream-code | [`sources/prs/vllm/PR-35927.md`](../sources/prs/vllm/PR-35927.md) | [MoE] Move PF Methods to Folder |
| `pr-vllm-35986` | upstream-code | [`sources/prs/vllm/PR-35986.md`](../sources/prs/vllm/PR-35986.md) | Add support for ModelOpt MXFP8 MoE models |
| `pr-vllm-36017` | upstream-code | [`sources/prs/vllm/PR-36017.md`](../sources/prs/vllm/PR-36017.md) | [Bugfix] Fix passing of activation_type to trtllm fused MoE NVFP4 and FP8 |
| `pr-vllm-36022` | upstream-code | [`sources/prs/vllm/PR-36022.md`](../sources/prs/vllm/PR-36022.md) | [Kernel] Add FlashInfer MoE A2A Kernel |
| `pr-vllm-36146` | upstream-code | [`sources/prs/vllm/PR-36146.md`](../sources/prs/vllm/PR-36146.md) | [Bugfix] Disable FlashInfer TRTLLM BF16 path for non-gated MoE |
| `pr-vllm-36205` | upstream-code | [`sources/prs/vllm/PR-36205.md`](../sources/prs/vllm/PR-36205.md) | [mla] Support fused FP8/NVFP4 output quantization in MLA attention (#35792) |
| `pr-vllm-36307` | upstream-code | [`sources/prs/vllm/PR-36307.md`](../sources/prs/vllm/PR-36307.md) | [Perf] Add TRTLLM FP8 MoE Modular Kernel |
| `pr-vllm-36458` | upstream-code | [`sources/prs/vllm/PR-36458.md`](../sources/prs/vllm/PR-36458.md) | [XPU] Support block fp8 moe by fallback to TritonExpert on XPU |
| `pr-vllm-36518` | upstream-code | [`sources/prs/vllm/PR-36518.md`](../sources/prs/vllm/PR-36518.md) | [Kernel] Fuse FP8 output quantization into merge_attn_states |
| `pr-vllm-36725` | upstream-code | [`sources/prs/vllm/PR-36725.md`](../sources/prs/vllm/PR-36725.md) | [Bug][MoE] Fix TRTLLM NVFP4 Routing Kernel Precision |
| `pr-vllm-36728` | upstream-code | [`sources/prs/vllm/PR-36728.md`](../sources/prs/vllm/PR-36728.md) | [Bug][MoE] Strengthen _supports_current_device() checks in the TRTLLM FP8, NVFP4, and FlashInfer CuteDSL MoE experts |
| `pr-vllm-37128` | upstream-code | [`sources/prs/vllm/PR-37128.md`](../sources/prs/vllm/PR-37128.md) | [MoE Refactor] Mxfp4 oracle rebased |
| `pr-vllm-37205` | upstream-code | [`sources/prs/vllm/PR-37205.md`](../sources/prs/vllm/PR-37205.md) | [Kernel] Add gpt-oss Router GEMM kernel |
| `pr-vllm-37217` | upstream-code | [`sources/prs/vllm/PR-37217.md`](../sources/prs/vllm/PR-37217.md) | [MoE/EPLB] Fix FlashInfer nvfp4 experts + EPLB correctness |
| `pr-vllm-37320` | upstream-code | [`sources/prs/vllm/PR-37320.md`](../sources/prs/vllm/PR-37320.md) | [Kernel] Add non-gated support for NVFP4 CUTLASS MoE |
| `pr-vllm-37373` | upstream-code | [`sources/prs/vllm/PR-37373.md`](../sources/prs/vllm/PR-37373.md) | [torch.compile] Refactor Attention Quant Fusion Pass and Remove Boilerplate |
| `pr-vllm-37463` | upstream-code | [`sources/prs/vllm/PR-37463.md`](../sources/prs/vllm/PR-37463.md) | [Kernel] Add MXFP4 W4A4 CUTLASS MoE kernel for SM100 |
| `pr-vllm-37503` | upstream-code | [`sources/prs/vllm/PR-37503.md`](../sources/prs/vllm/PR-37503.md) | [4/n] Migrate FP4/W4A8 CUTLASS kernels to torch stable ABI |
| `pr-vllm-37605` | upstream-code | [`sources/prs/vllm/PR-37605.md`](../sources/prs/vllm/PR-37605.md) | [Bugfix] Disable monolithic TRTLLM MoE for Renormalize routing (#37591) |
| `pr-vllm-37695` | upstream-code | [`sources/prs/vllm/PR-37695.md`](../sources/prs/vllm/PR-37695.md) | [Perf] Use torch compile to fuse pack topk in trtllm moe |
| `pr-vllm-37759` | upstream-code | [`sources/prs/vllm/PR-37759.md`](../sources/prs/vllm/PR-37759.md) | [MoE] Move FlashInfer CuteDSL experts into fused_moe/experts/ |
| `pr-vllm-38050` | upstream-code | [`sources/prs/vllm/PR-38050.md`](../sources/prs/vllm/PR-38050.md) | [MoE Kernel] Flashinfer nvfp4 cutedsl moe kernel integration |
| `pr-vllm-38251` | upstream-code | [`sources/prs/vllm/PR-38251.md`](../sources/prs/vllm/PR-38251.md) | [Quantization] Add FlashInfer CuteDSL batched experts backend for NVFP4 MoE |
| `pr-vllm-38329` | upstream-code | [`sources/prs/vllm/PR-38329.md`](../sources/prs/vllm/PR-38329.md) | [MoE] Add RoutingMethodType.Simulated to TRT-LLM FP8/NVFP4 kernel allowlists |
| `pr-vllm-38423` | upstream-code | [`sources/prs/vllm/PR-38423.md`](../sources/prs/vllm/PR-38423.md) | [NVIDIA] Bugfix NVFP4 DGX Spark and RTX50 |
| `pr-vllm-38504` | upstream-code | [`sources/prs/vllm/PR-38504.md`](../sources/prs/vllm/PR-38504.md) | [Kernels][MoE] Fix legacy_routing to use bitmatrix-based routing path |
| `pr-vllm-38859` | upstream-code | [`sources/prs/vllm/PR-38859.md`](../sources/prs/vllm/PR-38859.md) | [Bugfix] Re-enable Renormalize routing for TRT-LLM MoE experts |
| `pr-vllm-38989` | upstream-code | [`sources/prs/vllm/PR-38989.md`](../sources/prs/vllm/PR-38989.md) | [Bug] Fix routing bias dtype for trtllm per-block fp8 moe |
| `pr-vllm-38990` | upstream-code | [`sources/prs/vllm/PR-38990.md`](../sources/prs/vllm/PR-38990.md) | [Bugfix][MoE] Fix 6-8% decode regression: prefer multi-stream shared expert overlap |
| `pr-vllm-38993` | upstream-code | [`sources/prs/vllm/PR-38993.md`](../sources/prs/vllm/PR-38993.md) | [Perf] Change Trtllm fp8 MoE to use Shuffled Weights and BlockMajorK Layout |
| `pr-vllm-39002` | upstream-code | [`sources/prs/vllm/PR-39002.md`](../sources/prs/vllm/PR-39002.md) | [Bugfix] Fix FlashInfer crash with kv_cache_dtype_skip_layers |
| `pr-vllm-39007` | upstream-code | [`sources/prs/vllm/PR-39007.md`](../sources/prs/vllm/PR-39007.md) | [MoE] Move GPT OSS Triton kernel experts into fused_moe/experts/ |
| `pr-vllm-39088` | upstream-code | [`sources/prs/vllm/PR-39088.md`](../sources/prs/vllm/PR-39088.md) | [XPU] Quick fix for TritonMLA to remove cuda hardcode |
| `pr-vllm-39391` | upstream-code | [`sources/prs/vllm/PR-39391.md`](../sources/prs/vllm/PR-39391.md) | fix: clamp NaN/Inf in topk_softmax to prevent duplicate expert IDs |
| `pr-vllm-39510` | upstream-code | [`sources/prs/vllm/PR-39510.md`](../sources/prs/vllm/PR-39510.md) | [Kernel] Support TRTLLM GEN NVFP4 MoE for non-512-aligned hidden dims via weight padding |
| `pr-vllm-39717` | upstream-code | [`sources/prs/vllm/PR-39717.md`](../sources/prs/vllm/PR-39717.md) | [Bugfix] Reject non-nvfp4 dtypes when using the flashinfer_nvlink_one_sided all2all backend |
| `pr-vllm-39825` | upstream-code | [`sources/prs/vllm/PR-39825.md`](../sources/prs/vllm/PR-39825.md) | [Bugfix] Disable FlashInfer CUTLASS MoE on SM121 (DGX Spark) |
| `pr-vllm-39917` | upstream-code | [`sources/prs/vllm/PR-39917.md`](../sources/prs/vllm/PR-39917.md) | [Core] Replace routing replay with device cache and async D2H pipeline |
| `pr-vllm-40191` | upstream-code | [`sources/prs/vllm/PR-40191.md`](../sources/prs/vllm/PR-40191.md) | [Bugfix] Guard mxfp4_experts_quant bindings on ENABLE_NVFP4_SM100 |
| `pr-vllm-40273` | upstream-code | [`sources/prs/vllm/PR-40273.md`](../sources/prs/vllm/PR-40273.md) | Fix MoE backend selection for LoRA (unquantized MoE) |
| `pr-vllm-40392` | upstream-code | [`sources/prs/vllm/PR-40392.md`](../sources/prs/vllm/PR-40392.md) | [Performance][DSR1]: Fused RoPE+KVCache+q_concat for MLA |
| `pr-vllm-40574` | upstream-code | [`sources/prs/vllm/PR-40574.md`](../sources/prs/vllm/PR-40574.md) | [MoE] Move cutlass moe to fused_moe/experts/ |
| `pr-vllm-40950` | upstream-code | [`sources/prs/vllm/PR-40950.md`](../sources/prs/vllm/PR-40950.md) | [DSV4] Add silu clamp limit to shared expert |
| `pr-vllm-40960` | upstream-code | [`sources/prs/vllm/PR-40960.md`](../sources/prs/vllm/PR-40960.md) | [DSV4] Add BF16 and MXFP8 A2A support for flashinfer a2a one sided |
| `pr-vllm-41050` | upstream-code | [`sources/prs/vllm/PR-41050.md`](../sources/prs/vllm/PR-41050.md) | [Kernel][MoE] Support GELU on TRT-LLM NvFP4 fused MoE for Gemma4 |
| `pr-vllm-41263` | upstream-code | [`sources/prs/vllm/PR-41263.md`](../sources/prs/vllm/PR-41263.md) | [DSV4]   Fuse norm and router for low latency scenario |
| `pr-vllm-41428` | upstream-code | [`sources/prs/vllm/PR-41428.md`](../sources/prs/vllm/PR-41428.md) | [DSv4] Improved fused Indexer Q quant kernel |
| `pr-vllm-41566` | upstream-code | [`sources/prs/vllm/PR-41566.md`](../sources/prs/vllm/PR-41566.md) | [Quantization] Rework quantization_config to use QuantKey and allow for activation override |
| `pr-vllm-41882` | upstream-code | [`sources/prs/vllm/PR-41882.md`](../sources/prs/vllm/PR-41882.md) | Add NVFP4 all-gather GEMM fusion for AsyncTP |
| `pr-vllm-41979` | upstream-code | [`sources/prs/vllm/PR-41979.md`](../sources/prs/vllm/PR-41979.md) | [MoE] Move various experts classes to fused_moe/experts/ |
| `pr-vllm-41986` | upstream-code | [`sources/prs/vllm/PR-41986.md`](../sources/prs/vllm/PR-41986.md) | [Bugfix] Add swiglu limits to deepgemm fp8 methods |
| `pr-vllm-42236` | upstream-code | [`sources/prs/vllm/PR-42236.md`](../sources/prs/vllm/PR-42236.md) | [DSv4] Improved dequant gather K cache kernel |

<a id="loop-unrolling"></a>
## loop-unrolling

2 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `blog-yue-nvfp4` | community-note | [`sources/blogs/yue-nvfp4-hackathon.md`](../sources/blogs/yue-nvfp4-hackathon.md) | Blackwell NVFP4 Kernel Hackathon Journey |
| `contest-gpumode-p1` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-1-gemv.md`](../sources/contests/gpu-mode-nvfp4/problem-1-gemv.md) | GPU Mode NVFP4 Hackathon - Problem 1: Batched GEMV |

<a id="per-k-specialization"></a>
## per-k-specialization

2 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `blog-amandeep-nvfp4` | community-note | [`sources/blogs/amandeep-nvfp4-attempts.md`](../sources/blogs/amandeep-nvfp4-attempts.md) | Twelve Attempts at NVFP4 Batched GEMV |
| `contest-gpumode-p1` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-1-gemv.md`](../sources/contests/gpu-mode-nvfp4/problem-1-gemv.md) | GPU Mode NVFP4 Hackathon - Problem 1: Batched GEMV |

<a id="persistent-kernel"></a>
## persistent-kernel

25 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-cutlass-2161` | upstream-code | [`sources/prs/cutlass/PR-2161.md`](../sources/prs/cutlass/PR-2161.md) | Blockwise Improvement and Programmatic Dependent Launch |
| `pr-cutlass-2746` | upstream-code | [`sources/prs/cutlass/PR-2746.md`](../sources/prs/cutlass/PR-2746.md) | Support for GEMM-K=0 for Blackwell Grouped GEMMs |
| `pr-cutlass-2881` | upstream-code | [`sources/prs/cutlass/PR-2881.md`](../sources/prs/cutlass/PR-2881.md) | new example with TMA prefetch feature targeting for DRAM latency boun… |
| `pr-cutlass-3130` | upstream-code | [`sources/prs/cutlass/PR-3130.md`](../sources/prs/cutlass/PR-3130.md) | Update blackwell tutorial to be compatible with 4.5-dev version |
| `pr-flashinfer-1137` | upstream-code | [`sources/prs/flashinfer/PR-1137.md`](../sources/prs/flashinfer/PR-1137.md) | [feat] add unified batch attention w/ correctness tests. |
| `pr-flashinfer-1200` | upstream-code | [`sources/prs/flashinfer/PR-1200.md`](../sources/prs/flashinfer/PR-1200.md) | [feat] optimize persistent batch attention perf. |
| `pr-flashinfer-1322` | upstream-code | [`sources/prs/flashinfer/PR-1322.md`](../sources/prs/flashinfer/PR-1322.md) | feat: Add k_scale and v_scale to persistent attention  |
| `pr-flashinfer-1324` | upstream-code | [`sources/prs/flashinfer/PR-1324.md`](../sources/prs/flashinfer/PR-1324.md) | feat: Support logits_soft_cap for Persistent attn; fix kv split limit |
| `pr-flashinfer-1533` | upstream-code | [`sources/prs/flashinfer/PR-1533.md`](../sources/prs/flashinfer/PR-1533.md) | bugfix: Fix Persistent kernel precision for masked output  |
| `pr-flashinfer-1559` | upstream-code | [`sources/prs/flashinfer/PR-1559.md`](../sources/prs/flashinfer/PR-1559.md) | bugfix: fix persistent attention kernel correctness on blackwell |
| `pr-flashinfer-1614` | upstream-code | [`sources/prs/flashinfer/PR-1614.md`](../sources/prs/flashinfer/PR-1614.md) | bugfix: fix merge_attention_state in BatchAttention w/ gqa-group-size in Qwen family |
| `pr-flashinfer-1668` | upstream-code | [`sources/prs/flashinfer/PR-1668.md`](../sources/prs/flashinfer/PR-1668.md) | TGV GEMM as a BF16 backend alternative to cuBLAS |
| `pr-flashinfer-1681` | upstream-code | [`sources/prs/flashinfer/PR-1681.md`](../sources/prs/flashinfer/PR-1681.md) | perf: improve performance of cutlass fmha |
| `pr-flashinfer-1826` | upstream-code | [`sources/prs/flashinfer/PR-1826.md`](../sources/prs/flashinfer/PR-1826.md) | Bugfix: Fix data hazard in persistent reduce |
| `pr-flashinfer-1850` | upstream-code | [`sources/prs/flashinfer/PR-1850.md`](../sources/prs/flashinfer/PR-1850.md) | Add head_dim=64 for blackwell cutlass fmha implementation |
| `pr-flashinfer-1865` | upstream-code | [`sources/prs/flashinfer/PR-1865.md`](../sources/prs/flashinfer/PR-1865.md) | Bugfix: fix o_strides in persistent kernel  |
| `pr-flashinfer-1942` | upstream-code | [`sources/prs/flashinfer/PR-1942.md`](../sources/prs/flashinfer/PR-1942.md) | Add realistic bench for persistent kernel  |
| `pr-flashinfer-2805` | upstream-code | [`sources/prs/flashinfer/PR-2805.md`](../sources/prs/flashinfer/PR-2805.md) | [CuTe DSL] Add modular FMHA prefill and MLA decode attention kernels |
| `pr-flashinfer-982` | upstream-code | [`sources/prs/flashinfer/PR-982.md`](../sources/prs/flashinfer/PR-982.md) | SM-constraint-GEMM by triton persistent kernel |
| `pr-sglang-17327` | upstream-code | [`sources/prs/sglang/PR-17327.md`](../sources/prs/sglang/PR-17327.md) | Disable mla persistent kernel when not using fp8 kv_cache |
| `pr-sglang-5390` | upstream-code | [`sources/prs/sglang/PR-5390.md`](../sources/prs/sglang/PR-5390.md) | Add Cutlass MLA attention backend |
| `pr-vllm-16032` | upstream-code | [`sources/prs/vllm/PR-16032.md`](../sources/prs/vllm/PR-16032.md) | [NVIDIA] Support Cutlass MLA for Blackwell GPUs |
| `pr-vllm-36574` | upstream-code | [`sources/prs/vllm/PR-36574.md`](../sources/prs/vllm/PR-36574.md) | [ROCm] Utilize persistent MLA kernel from AITER |
| `pr-vllm-37421` | upstream-code | [`sources/prs/vllm/PR-37421.md`](../sources/prs/vllm/PR-37421.md) | [Perf][Kernel] Persistent TopK scheduler: unified CUDAGraph-safe kernel with dynamic per-row dispatch - DeepSeek-V3.2 DSA decode |
| `pr-vllm-38615` | upstream-code | [`sources/prs/vllm/PR-38615.md`](../sources/prs/vllm/PR-38615.md) | [ROCm] Fix aiter persistent mode mla with q/o nhead<16 for kimi-k2.5 tp8 |

<a id="persistent-kernels"></a>
## persistent-kernels

19 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-flash-attention-2304` | upstream-code | [`sources/prs/flash-attention/PR-2304.md`](../sources/prs/flash-attention/PR-2304.md) | [Cute][Testing] Add persistent compile cache for cutedsl AOT compilation |
| `pr-flash-attention-2441` | upstream-code | [`sources/prs/flash-attention/PR-2441.md`](../sources/prs/flash-attention/PR-2441.md) | [Cute,Sm100,Fwd] add MLA 64/512 with topk sparsity for MQA 128 heads |
| `pr-flashinfer-3097` | upstream-code | [`sources/prs/flashinfer/PR-3097.md`](../sources/prs/flashinfer/PR-3097.md) | Support NVFP4 KV for prefill and batch attention kernels |
| `pr-flashinfer-3132` | upstream-code | [`sources/prs/flashinfer/PR-3132.md`](../sources/prs/flashinfer/PR-3132.md) | [CuTe DSL] Fix FP8 MLA persistent perf regression and ProxyKind cu13 wheel breakage |
| `pr-flashinfer-3155` | upstream-code | [`sources/prs/flashinfer/PR-3155.md`](../sources/prs/flashinfer/PR-3155.md) | fix(gdn): use physical SM count for SM100 persistent prefill kernel |
| `pr-flashinfer-3235` | upstream-code | [`sources/prs/flashinfer/PR-3235.md`](../sources/prs/flashinfer/PR-3235.md) | Support Kimi K2.5 H64 CuTe DSL MLA decode |
| `pr-tensorrt-llm-10043` | upstream-code | [`sources/prs/tensorrt-llm/PR-10043.md`](../sources/prs/tensorrt-llm/PR-10043.md) | [TRTLLM-9992][perf] Enable PDL for CuteDSL kernels and overlap MoeOutputMemset |
| `pr-tensorrt-llm-11718` | upstream-code | [`sources/prs/tensorrt-llm/PR-11718.md`](../sources/prs/tensorrt-llm/PR-11718.md) | [TRTLLM-11119][feat] Blackwell SageAttention, Integrate into AttentionOp API |
| `pr-tensorrt-llm-12074` | upstream-code | [`sources/prs/tensorrt-llm/PR-12074.md`](../sources/prs/tensorrt-llm/PR-12074.md) | [TRTLLM-11289][feat] Integrate CuteDSL's bf16 dense GEMMs |
| `pr-tensorrt-llm-12470` | upstream-code | [`sources/prs/tensorrt-llm/PR-12470.md`](../sources/prs/tensorrt-llm/PR-12470.md) | [None][feat] Support sparse mqa/gqa attention |
| `pr-tensorrt-llm-12612` | upstream-code | [`sources/prs/tensorrt-llm/PR-12612.md`](../sources/prs/tensorrt-llm/PR-12612.md) | [None][feat] Trtllm-gen FMHA JIT support |
| `pr-tensorrt-llm-12937` | upstream-code | [`sources/prs/tensorrt-llm/PR-12937.md`](../sources/prs/tensorrt-llm/PR-12937.md) | [TRTLLM-11485][feat] Feature rework: Add SageAttention refreshed kernels (attentionOp only) |
| `pr-tensorrt-llm-13505` | upstream-code | [`sources/prs/tensorrt-llm/PR-13505.md`](../sources/prs/tensorrt-llm/PR-13505.md) | [None][perf] Drop cubin and Eliminate ~6s FMHA JIT recompile in eager generation by aligning kernel selection with CUDA graph warmup |
| `pr-tensorrt-llm-13652` | upstream-code | [`sources/prs/tensorrt-llm/PR-13652.md`](../sources/prs/tensorrt-llm/PR-13652.md) | [None][feat] Add DeepSeekV4 attention kernels |
| `pr-tilelang-1874` | upstream-code | [`sources/prs/tilelang/PR-1874.md`](../sources/prs/tilelang/PR-1874.md) | [Feature] Support cluster launch, query, synchronization and barrier operations |
| `pr-tilelang-1882` | upstream-code | [`sources/prs/tilelang/PR-1882.md`](../sources/prs/tilelang/PR-1882.md) | [Feature] 2-SM support for TMA, TMEM and TCGEN5MMA on Blackwell |
| `pr-tilelang-2003` | upstream-code | [`sources/prs/tilelang/PR-2003.md`](../sources/prs/tilelang/PR-2003.md) | [Transform] Add InjectTcgen05Fence pass |
| `pr-vllm-41189` | upstream-code | [`sources/prs/vllm/PR-41189.md`](../sources/prs/vllm/PR-41189.md) | [Bugfix] Fix persistent_topk cooperative deadlock at TopK=1024 |
| `pr-vllm-41665` | upstream-code | [`sources/prs/vllm/PR-41665.md`](../sources/prs/vllm/PR-41665.md) | [Bugfix] Fix condition to clear persistent topk so that it can be captured regardless |

<a id="pipeline-stages"></a>
## pipeline-stages

230 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `blog-modular-blackwell` | community-note | [`sources/blogs/modular-blackwell-matmul.md`](../sources/blogs/modular-blackwell-matmul.md) | Modular: Matrix Multiplication on Blackwell |
| `contest-flashinfer-track-a` | contest-report | [`sources/contests/flashinfer-mlsys26/track-a-fused-moe.md`](../sources/contests/flashinfer-mlsys26/track-a-fused-moe.md) | FlashInfer MLSys 2026 - Track A: Fused MoE FP8 |
| `contest-flashinfer-track-b` | contest-report | [`sources/contests/flashinfer-mlsys26/track-b-sparse-attention.md`](../sources/contests/flashinfer-mlsys26/track-b-sparse-attention.md) | FlashInfer MLSys 2026 - Track B: DeepSeek V3.2 Sparse Attention |
| `contest-flashinfer-track-c` | contest-report | [`sources/contests/flashinfer-mlsys26/track-c-gated-delta-net.md`](../sources/contests/flashinfer-mlsys26/track-c-gated-delta-net.md) | FlashInfer MLSys 2026 - Track C: Gated Delta Net |
| `contest-gpumode-p2` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-2-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-2-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 2: NVFP4 GEMM |
| `contest-gpumode-p3` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-3-gated-dual-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-3-gated-dual-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 3: Gated Dual GEMM |
| `contest-gpumode-p4` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 4: Grouped GEMM |
| `pr-cccl-cub-3236` | upstream-code | [`sources/prs/cccl-cub/PR-3236.md`](../sources/prs/cccl-cub/PR-3236.md) | Fix scan / sm90 perf regression  |
| `pr-cccl-cub-3559` | upstream-code | [`sources/prs/cccl-cub/PR-3559.md`](../sources/prs/cccl-cub/PR-3559.md) | Add b200 tunings for scan.exclusive.sum |
| `pr-cccl-cub-3691` | upstream-code | [`sources/prs/cccl-cub/PR-3691.md`](../sources/prs/cccl-cub/PR-3691.md) | Fix SM100 histogram tunings |
| `pr-cccl-cub-4961` | upstream-code | [`sources/prs/cccl-cub/PR-4961.md`](../sources/prs/cccl-cub/PR-4961.md) | Add nondeterministic reduce that uses atomics |
| `pr-cccl-cub-5314` | upstream-code | [`sources/prs/cccl-cub/PR-5314.md`](../sources/prs/cccl-cub/PR-5314.md) | CUB - Add internal integer utils and tests (Split `WarpReduce` PR) |
| `pr-cccl-cub-5408` | upstream-code | [`sources/prs/cccl-cub/PR-5408.md`](../sources/prs/cccl-cub/PR-5408.md) | Combine `block_reduce_warp_reduction_nondeterministic.cuh` specialization with original deterministic one  |
| `pr-cccl-cub-6811` | upstream-code | [`sources/prs/cccl-cub/PR-6811.md`](../sources/prs/cccl-cub/PR-6811.md) | Integrate decoupled lookahead warpspeed scan |
| `pr-cccl-cub-6819` | upstream-code | [`sources/prs/cccl-cub/PR-6819.md`](../sources/prs/cccl-cub/PR-6819.md) | Use integer promotion for `warp_reduce` |
| `pr-cccl-cub-8352` | upstream-code | [`sources/prs/cccl-cub/PR-8352.md`](../sources/prs/cccl-cub/PR-8352.md) | Apply some random warpspeed tunings |
| `pr-cccl-cub-8423` | upstream-code | [`sources/prs/cccl-cub/PR-8423.md`](../sources/prs/cccl-cub/PR-8423.md) | Vectorize mbarrier initialization in warpspeed scan |
| `pr-cccl-cub-8839` | upstream-code | [`sources/prs/cccl-cub/PR-8839.md`](../sources/prs/cccl-cub/PR-8839.md) | Fix Warpspeed scan shifted output store |
| `pr-cutlass-1661` | upstream-code | [`sources/prs/cutlass/PR-1661.md`](../sources/prs/cutlass/PR-1661.md) | Skip void-C kernels in the profiler when beta is non zero |
| `pr-cutlass-1795` | upstream-code | [`sources/prs/cutlass/PR-1795.md`](../sources/prs/cutlass/PR-1795.md) | Support for TMA Epilogue for Group Gemm and add pingpong ptr array & Group Gemm |
| `pr-cutlass-1883` | upstream-code | [`sources/prs/cutlass/PR-1883.md`](../sources/prs/cutlass/PR-1883.md) | Improve sm90 mixed dtype kernel |
| `pr-cutlass-1932` | upstream-code | [`sources/prs/cutlass/PR-1932.md`](../sources/prs/cutlass/PR-1932.md) | Blockwise Scaling for FP8 |
| `pr-cutlass-2095` | upstream-code | [`sources/prs/cutlass/PR-2095.md`](../sources/prs/cutlass/PR-2095.md) | Improvements for: Groupwise scaling along M for FP8 gemm |
| `pr-cutlass-2123` | upstream-code | [`sources/prs/cutlass/PR-2123.md`](../sources/prs/cutlass/PR-2123.md) | Hopper Grouped GEMM support for FP8 Accum |
| `pr-cutlass-2172` | upstream-code | [`sources/prs/cutlass/PR-2172.md`](../sources/prs/cutlass/PR-2172.md) | Fix SM90 beta=1 hang and stream-K launch errors |
| `pr-cutlass-2270` | upstream-code | [`sources/prs/cutlass/PR-2270.md`](../sources/prs/cutlass/PR-2270.md) | hopper-blockwise-generalization-optimization |
| `pr-cutlass-2466` | upstream-code | [`sources/prs/cutlass/PR-2466.md`](../sources/prs/cutlass/PR-2466.md) | Example 77 add blackwell fmha bwd for MLA shape |
| `pr-cutlass-2472` | upstream-code | [`sources/prs/cutlass/PR-2472.md`](../sources/prs/cutlass/PR-2472.md) | Add Blackwell MLA forward (shape: d=192, dv=128) implementation |
| `pr-cutlass-2746` | upstream-code | [`sources/prs/cutlass/PR-2746.md`](../sources/prs/cutlass/PR-2746.md) | Support for GEMM-K=0 for Blackwell Grouped GEMMs |
| `pr-cutlass-2790` | upstream-code | [`sources/prs/cutlass/PR-2790.md`](../sources/prs/cutlass/PR-2790.md) | Blockscaled Ragged Contiguous Grouped Gemm for MoEs |
| `pr-cutlass-2995` | upstream-code | [`sources/prs/cutlass/PR-2995.md`](../sources/prs/cutlass/PR-2995.md) | [CuTeDSL] Fix: SM100 block-scale gemm overlapping accumulator |
| `pr-cutlass-3055` | upstream-code | [`sources/prs/cutlass/PR-3055.md`](../sources/prs/cutlass/PR-3055.md) | Replace std::min with cute::min in sm120 blockwise scaling device functions |
| `pr-cutlass-3092` | upstream-code | [`sources/prs/cutlass/PR-3092.md`](../sources/prs/cutlass/PR-3092.md) | Support for Group GEMM in CUTLASS Profiler for GeForce and Spark |
| `pr-cutlass-3176` | upstream-code | [`sources/prs/cutlass/PR-3176.md`](../sources/prs/cutlass/PR-3176.md) | Small Tile N BlockScaled GEMM + Grouped GEMM on SM12x |
| `pr-deepgemm-112` | upstream-code | [`sources/prs/deepgemm/PR-112.md`](../sources/prs/deepgemm/PR-112.md) | Add more GPU architectures support |
| `pr-deepgemm-193` | upstream-code | [`sources/prs/deepgemm/PR-193.md`](../sources/prs/deepgemm/PR-193.md) | Fix multicast bug and optimize masked GEMM |
| `pr-deepgemm-198` | upstream-code | [`sources/prs/deepgemm/PR-198.md`](../sources/prs/deepgemm/PR-198.md) | Make various updates and fixes |
| `pr-deepgemm-227` | upstream-code | [`sources/prs/deepgemm/PR-227.md`](../sources/prs/deepgemm/PR-227.md) | Use larger MMA shape to optimize sm100_fp8_mqa_logits |
| `pr-deepgemm-233` | upstream-code | [`sources/prs/deepgemm/PR-233.md`](../sources/prs/deepgemm/PR-233.md) | support bf16 bias in deepgemm2 |
| `pr-deepgemm-270` | upstream-code | [`sources/prs/deepgemm/PR-270.md`](../sources/prs/deepgemm/PR-270.md) | fix: use SM90ArchSpec instead of SM100ArchSpec in sm90_bf16_k_grouped_gemm |
| `pr-deepgemm-78` | upstream-code | [`sources/prs/deepgemm/PR-78.md`](../sources/prs/deepgemm/PR-78.md) |  Solving bank conflict via padding and TMA 3D store |
| `pr-deepgemm-83` | upstream-code | [`sources/prs/deepgemm/PR-83.md`](../sources/prs/deepgemm/PR-83.md) | Use 1D TMA store instead of 3D |
| `pr-deepgemm-88` | upstream-code | [`sources/prs/deepgemm/PR-88.md`](../sources/prs/deepgemm/PR-88.md) | Support TMA multicast on B with m_grouped_gemm_contiguous. |
| `pr-flash-attention-1072` | upstream-code | [`sources/prs/flash-attention/PR-1072.md`](../sources/prs/flash-attention/PR-1072.md) | Add var-seq-len to FA3 fp16 / bf16 fwd |
| `pr-flash-attention-1100` | upstream-code | [`sources/prs/flash-attention/PR-1100.md`](../sources/prs/flash-attention/PR-1100.md) | Fp8 kernel with "in-kernel" transpose of V in producer |
| `pr-flash-attention-1173` | upstream-code | [`sources/prs/flash-attention/PR-1173.md`](../sources/prs/flash-attention/PR-1173.md) | FA3 FP8 qkv descales + restore max offset for h128 causal + added sync for producer WG |
| `pr-flash-attention-1182` | upstream-code | [`sources/prs/flash-attention/PR-1182.md`](../sources/prs/flash-attention/PR-1182.md) | Add seqused_q in fwd / bwd and seqused_k in bwd in hopper FA. |
| `pr-flash-attention-1233` | upstream-code | [`sources/prs/flash-attention/PR-1233.md`](../sources/prs/flash-attention/PR-1233.md) | Add local attention in Hopper FAv3 |
| `pr-flash-attention-1236` | upstream-code | [`sources/prs/flash-attention/PR-1236.md`](../sources/prs/flash-attention/PR-1236.md) | FA3 kvcache + split kv + gqa parallelization |
| `pr-flash-attention-1268` | upstream-code | [`sources/prs/flash-attention/PR-1268.md`](../sources/prs/flash-attention/PR-1268.md) | Paged Attention support for FA3 |
| `pr-flash-attention-1331` | upstream-code | [`sources/prs/flash-attention/PR-1331.md`](../sources/prs/flash-attention/PR-1331.md) | FA3 paged attention: Readiness for Cutlass 3.6 / default value for block_table |
| `pr-flash-attention-1361` | upstream-code | [`sources/prs/flash-attention/PR-1361.md`](../sources/prs/flash-attention/PR-1361.md) | Fix FA3 Varlen Performance regression |
| `pr-flash-attention-1604` | upstream-code | [`sources/prs/flash-attention/PR-1604.md`](../sources/prs/flash-attention/PR-1604.md) | Support hdimQK != hdimV backward |
| `pr-flash-attention-1823` | upstream-code | [`sources/prs/flash-attention/PR-1823.md`](../sources/prs/flash-attention/PR-1823.md) | Add sorting and head swizzle to varlen scheduler |
| `pr-flash-attention-1893` | upstream-code | [`sources/prs/flash-attention/PR-1893.md`](../sources/prs/flash-attention/PR-1893.md) | Improve causal backward determinism perf with SPT schedule |
| `pr-flash-attention-1940` | upstream-code | [`sources/prs/flash-attention/PR-1940.md`](../sources/prs/flash-attention/PR-1940.md) | [Cute,Fwd,Sm100] Implement SplitKV |
| `pr-flash-attention-1945` | upstream-code | [`sources/prs/flash-attention/PR-1945.md`](../sources/prs/flash-attention/PR-1945.md) | Blackwell FlashAttention-BWD (v1.0) |
| `pr-flash-attention-1985` | upstream-code | [`sources/prs/flash-attention/PR-1985.md`](../sources/prs/flash-attention/PR-1985.md) | [Cute] Block sparse support Sm100 |
| `pr-flash-attention-1993` | upstream-code | [`sources/prs/flash-attention/PR-1993.md`](../sources/prs/flash-attention/PR-1993.md) | [Cute,Fwd,Sm100] Support `q_stage=1` for inference |
| `pr-flash-attention-1999` | upstream-code | [`sources/prs/flash-attention/PR-1999.md`](../sources/prs/flash-attention/PR-1999.md) | [Cute,Fwd,Sm100] Support paged attention |
| `pr-flash-attention-2014` | upstream-code | [`sources/prs/flash-attention/PR-2014.md`](../sources/prs/flash-attention/PR-2014.md) | [Cute,Sm100,Fwd] use correction warps for epi when not using TMA |
| `pr-flash-attention-2026` | upstream-code | [`sources/prs/flash-attention/PR-2026.md`](../sources/prs/flash-attention/PR-2026.md) | [Cute,Fwd,Sm100] don't pass mask_fn to softmax_step generically |
| `pr-flash-attention-2033` | upstream-code | [`sources/prs/flash-attention/PR-2033.md`](../sources/prs/flash-attention/PR-2033.md) | [Cute,Bwd,Sm100] enable deterministic mode for sm100 bwd and fix race conditions |
| `pr-flash-attention-2043` | upstream-code | [`sources/prs/flash-attention/PR-2043.md`](../sources/prs/flash-attention/PR-2043.md) | [Cute,Fwd] Extend score_mod to variable sequence length |
| `pr-flash-attention-2070` | upstream-code | [`sources/prs/flash-attention/PR-2070.md`](../sources/prs/flash-attention/PR-2070.md) | Add score-mod bwd support  |
| `pr-flash-attention-2085` | upstream-code | [`sources/prs/flash-attention/PR-2085.md`](../sources/prs/flash-attention/PR-2085.md) | Add blocksparse support for bwd on blackwell |
| `pr-flash-attention-2091` | upstream-code | [`sources/prs/flash-attention/PR-2091.md`](../sources/prs/flash-attention/PR-2091.md) | Fix IMA in fwd on m boundary |
| `pr-flash-attention-2098` | upstream-code | [`sources/prs/flash-attention/PR-2098.md`](../sources/prs/flash-attention/PR-2098.md) | Add pack-gqa fwd support for sparse impl w/ broadcasted H dim |
| `pr-flash-attention-2104` | upstream-code | [`sources/prs/flash-attention/PR-2104.md`](../sources/prs/flash-attention/PR-2104.md) | [Cute,Fwd,Sm100] distributed offset calculation for paged KV |
| `pr-flash-attention-2108` | upstream-code | [`sources/prs/flash-attention/PR-2108.md`](../sources/prs/flash-attention/PR-2108.md) | [NVIDIA] Enable Jetson Thor FA4 |
| `pr-flash-attention-2109` | upstream-code | [`sources/prs/flash-attention/PR-2109.md`](../sources/prs/flash-attention/PR-2109.md) | [Cute,Fwd,Sm100] fp8 e4m3 and e5m2 support |
| `pr-flash-attention-2145` | upstream-code | [`sources/prs/flash-attention/PR-2145.md`](../sources/prs/flash-attention/PR-2145.md) | [CUTE][SM90]Enable pack-gqa with broadcasted maskmods |
| `pr-flash-attention-2180` | upstream-code | [`sources/prs/flash-attention/PR-2180.md`](../sources/prs/flash-attention/PR-2180.md) | [Cute][Flex]Add pack-gqa divmod |
| `pr-flash-attention-2186` | upstream-code | [`sources/prs/flash-attention/PR-2186.md`](../sources/prs/flash-attention/PR-2186.md) | [Cute,Fwd,Sm100] support irregular qhead / kvhead ratios |
| `pr-flash-attention-2236` | upstream-code | [`sources/prs/flash-attention/PR-2236.md`](../sources/prs/flash-attention/PR-2236.md) | [Cute,Flex,Fwd] Allow vectorized score_mod definitions |
| `pr-flash-attention-2330` | upstream-code | [`sources/prs/flash-attention/PR-2330.md`](../sources/prs/flash-attention/PR-2330.md) | [Bwd,Sm120] Add SM120 backward pass support |
| `pr-flash-attention-2333` | upstream-code | [`sources/prs/flash-attention/PR-2333.md`](../sources/prs/flash-attention/PR-2333.md) | Add SM120 varlen attention support |
| `pr-flash-attention-2360` | upstream-code | [`sources/prs/flash-attention/PR-2360.md`](../sources/prs/flash-attention/PR-2360.md) | [Fwd,Sm90] Add paged KV attention support (tma and cp.async) |
| `pr-flash-attention-2388` | upstream-code | [`sources/prs/flash-attention/PR-2388.md`](../sources/prs/flash-attention/PR-2388.md) | fix: use LSE accum strides from params instead of hardcoded ones |
| `pr-flash-attention-2390` | upstream-code | [`sources/prs/flash-attention/PR-2390.md`](../sources/prs/flash-attention/PR-2390.md) | [Cute,Sm100,Bwd] refine bwd swizzle for deterministic |
| `pr-flash-attention-2441` | upstream-code | [`sources/prs/flash-attention/PR-2441.md`](../sources/prs/flash-attention/PR-2441.md) | [Cute,Sm100,Fwd] add MLA 64/512 with topk sparsity for MQA 128 heads |
| `pr-flash-attention-2488` | upstream-code | [`sources/prs/flash-attention/PR-2488.md`](../sources/prs/flash-attention/PR-2488.md) | [hd256] Improve forward kernel with exp2 FMA emulation (3% to 9% performance gain) |
| `pr-flash-attention-2489` | upstream-code | [`sources/prs/flash-attention/PR-2489.md`](../sources/prs/flash-attention/PR-2489.md) | [hd256] Add TMA paged KV support to SM100 2CTA forward kernel |
| `pr-flash-attention-2497` | upstream-code | [`sources/prs/flash-attention/PR-2497.md`](../sources/prs/flash-attention/PR-2497.md) | [FA4][hd256] Backward TMA bulk-store epilogue + LSE/dpsum coalesce |
| `pr-flashinfer-1113` | upstream-code | [`sources/prs/flashinfer/PR-1113.md`](../sources/prs/flashinfer/PR-1113.md) | Add CUTLASS fused moe kernels from TensorRT-LLM. |
| `pr-flashinfer-1850` | upstream-code | [`sources/prs/flashinfer/PR-1850.md`](../sources/prs/flashinfer/PR-1850.md) | Add head_dim=64 for blackwell cutlass fmha implementation |
| `pr-flashinfer-2387` | upstream-code | [`sources/prs/flashinfer/PR-2387.md`](../sources/prs/flashinfer/PR-2387.md) | A Blackwell-optimized version of selective_state_update (mamba) |
| `pr-flashinfer-2398` | upstream-code | [`sources/prs/flashinfer/PR-2398.md`](../sources/prs/flashinfer/PR-2398.md) | feat: cuteDSL fp4 moe for better DSR1 performance. |
| `pr-flashinfer-2439` | upstream-code | [`sources/prs/flashinfer/PR-2439.md`](../sources/prs/flashinfer/PR-2439.md) | Add sm90 guard to fence ptx |
| `pr-flashinfer-2805` | upstream-code | [`sources/prs/flashinfer/PR-2805.md`](../sources/prs/flashinfer/PR-2805.md) | [CuTe DSL] Add modular FMHA prefill and MLA decode attention kernels |
| `pr-flashinfer-2841` | upstream-code | [`sources/prs/flashinfer/PR-2841.md`](../sources/prs/flashinfer/PR-2841.md) | [Perf] Add FMHAv2 to flashinfer_benchmark.py and eliminate unnecessary H2D |
| `pr-flashinfer-3009` | upstream-code | [`sources/prs/flashinfer/PR-3009.md`](../sources/prs/flashinfer/PR-3009.md) | [feat] Faster topk algorithm |
| `pr-flashinfer-3080` | upstream-code | [`sources/prs/flashinfer/PR-3080.md`](../sources/prs/flashinfer/PR-3080.md) | feat: Add b12x_fused_moe / B12xMoEWrapper SM120 APIs with micro kernel and ReLU2 |
| `pr-flashinfer-3084` | upstream-code | [`sources/prs/flashinfer/PR-3084.md`](../sources/prs/flashinfer/PR-3084.md) | perf: optimize MXFP4xBF16 & INT4xFP8 CUTLASS MoE backend for SM90 |
| `pr-flashinfer-3113` | upstream-code | [`sources/prs/flashinfer/PR-3113.md`](../sources/prs/flashinfer/PR-3113.md) | Fix: Extend b12x FP4 GEMM support to SM121 (GB10/DGX Spark) |
| `pr-flashinfer-3152` | upstream-code | [`sources/prs/flashinfer/PR-3152.md`](../sources/prs/flashinfer/PR-3152.md) | Integrate CUTLASS Small Tile N Blockscaled GEMMs/Grouped GEMMs for SM120 and SM121 |
| `pr-flashinfer-3155` | upstream-code | [`sources/prs/flashinfer/PR-3155.md`](../sources/prs/flashinfer/PR-3155.md) | fix(gdn): use physical SM count for SM100 persistent prefill kernel |
| `pr-flashinfer-3191` | upstream-code | [`sources/prs/flashinfer/PR-3191.md`](../sources/prs/flashinfer/PR-3191.md) | fix(sm12x): fix micro-kernel workspace sizing when routed_rows > num_local_experts |
| `pr-flashinfer-3193` | upstream-code | [`sources/prs/flashinfer/PR-3193.md`](../sources/prs/flashinfer/PR-3193.md) | perf(moe): optimize SM120 b12x MoE short decode |
| `pr-flashinfer-3227` | upstream-code | [`sources/prs/flashinfer/PR-3227.md`](../sources/prs/flashinfer/PR-3227.md) | [Bugfix] Fix fused MoE autotuning correctness issues by filtering clusterDimZ |
| `pr-flashinfer-3259` | upstream-code | [`sources/prs/flashinfer/PR-3259.md`](../sources/prs/flashinfer/PR-3259.md) | Add dynamic tokens-per-page TRTLLM-GEN GQA kernels |
| `pr-flashinfer-3271` | upstream-code | [`sources/prs/flashinfer/PR-3271.md`](../sources/prs/flashinfer/PR-3271.md) | feat(moe): add SM120 W4A16 b12x kernels |
| `pr-flashinfer-3276` | upstream-code | [`sources/prs/flashinfer/PR-3276.md`](../sources/prs/flashinfer/PR-3276.md) | fix(fmha_v2): fix FP8 V-scratch pipeline and varlen scheduler on SM90 |
| `pr-flashinfer-901` | upstream-code | [`sources/prs/flashinfer/PR-901.md`](../sources/prs/flashinfer/PR-901.md) | perf: tweak the pipeline design of mla kernel |
| `pr-flashinfer-952` | upstream-code | [`sources/prs/flashinfer/PR-952.md`](../sources/prs/flashinfer/PR-952.md) | perf: Use 2WG pipeline design for MLA implementation on Hopper |
| `pr-sglang-13263` | upstream-code | [`sources/prs/sglang/PR-13263.md`](../sources/prs/sglang/PR-13263.md) | diffusion: enable fa4 for blackwell |
| `pr-sglang-15382` | upstream-code | [`sources/prs/sglang/PR-15382.md`](../sources/prs/sglang/PR-15382.md) | [diffusion] Add Sage Attention 3 Support for sm 120 (RTX5090) |
| `pr-sglang-15888` | upstream-code | [`sources/prs/sglang/PR-15888.md`](../sources/prs/sglang/PR-15888.md) | [diffusion] model: support TurboWan2.1-T2V-1.3B/14B SLA |
| `pr-sglang-16723` | upstream-code | [`sources/prs/sglang/PR-16723.md`](../sources/prs/sglang/PR-16723.md) | [Rework] Add SwapAB Optimization for triton fused_moe_kernel on SM90. |
| `pr-sglang-17353` | upstream-code | [`sources/prs/sglang/PR-17353.md`](../sources/prs/sglang/PR-17353.md) | Move fa4 from sgl-kernel to jit kernel |
| `pr-sglang-17784` | upstream-code | [`sources/prs/sglang/PR-17784.md`](../sources/prs/sglang/PR-17784.md) | Upgrade transformers==5.3.0 |
| `pr-sglang-19549` | upstream-code | [`sources/prs/sglang/PR-19549.md`](../sources/prs/sglang/PR-19549.md) | [diffusion][llm] macOS support |
| `pr-sglang-20047` | upstream-code | [`sources/prs/sglang/PR-20047.md`](../sources/prs/sglang/PR-20047.md) | fix: default FP4 GEMM backend to flashinfer_cudnn on SM120 (Blackwell) |
| `pr-sglang-20137` | upstream-code | [`sources/prs/sglang/PR-20137.md`](../sources/prs/sglang/PR-20137.md) | [diffusion] Support nvfp4 for Flux.2 |
| `pr-sglang-20576` | upstream-code | [`sources/prs/sglang/PR-20576.md`](../sources/prs/sglang/PR-20576.md) | [Diffusion] Clean upstream fa3 in hopper |
| `pr-sglang-22574` | upstream-code | [`sources/prs/sglang/PR-22574.md`](../sources/prs/sglang/PR-22574.md) | [Diffusion] Add FLUX.1-dev ModelOpt NVFP4 support |
| `pr-sglang-22672` | upstream-code | [`sources/prs/sglang/PR-22672.md`](../sources/prs/sglang/PR-22672.md) | reland [Diffusion] Add FLUX.1-dev ModelOpt NVFP4 support |
| `pr-sglang-22869` | upstream-code | [`sources/prs/sglang/PR-22869.md`](../sources/prs/sglang/PR-22869.md) | [diffusion] feat: introduce ltx-2-two-stage device manager |
| `pr-sglang-24562` | upstream-code | [`sources/prs/sglang/PR-24562.md`](../sources/prs/sglang/PR-24562.md) | Fix performance regression on Deepseek V3 on `moe-runner-backend=triton` on SM90 |
| `pr-sglang-3216` | upstream-code | [`sources/prs/sglang/PR-3216.md`](../sources/prs/sglang/PR-3216.md) | add tensorrt_llm common and cutlass_extensions as 3rdparty |
| `pr-sglang-5724` | upstream-code | [`sources/prs/sglang/PR-5724.md`](../sources/prs/sglang/PR-5724.md) | [PP] Add pipeline parallelism |
| `pr-tensorrt-llm-10042` | upstream-code | [`sources/prs/tensorrt-llm/PR-10042.md`](../sources/prs/tensorrt-llm/PR-10042.md) | [None][perf] Add more optimization options for MOE CuteDSL finalized kernel |
| `pr-tensorrt-llm-10088` | upstream-code | [`sources/prs/tensorrt-llm/PR-10088.md`](../sources/prs/tensorrt-llm/PR-10088.md) | [None][feat] CuteDSL MOE FC1 Enhancement |
| `pr-tensorrt-llm-10130` | upstream-code | [`sources/prs/tensorrt-llm/PR-10130.md`](../sources/prs/tensorrt-llm/PR-10130.md) | [TRTLLM-9457][feat] Add cute dsl fp8 gemm for Blackwell |
| `pr-tensorrt-llm-10190` | upstream-code | [`sources/prs/tensorrt-llm/PR-10190.md`](../sources/prs/tensorrt-llm/PR-10190.md) | [None][feat] sm100 weight-only kernel |
| `pr-tensorrt-llm-10226` | upstream-code | [`sources/prs/tensorrt-llm/PR-10226.md`](../sources/prs/tensorrt-llm/PR-10226.md) | [TRTLLM-9798][feat] Change to use new DeepGEMM MQA sm100 kernel for MTP-3 |
| `pr-tensorrt-llm-10264` | upstream-code | [`sources/prs/tensorrt-llm/PR-10264.md`](../sources/prs/tensorrt-llm/PR-10264.md) | [TRTLLM-10022][feat] Add hopper xqa decode support for skip softmax attention |
| `pr-tensorrt-llm-10479` | upstream-code | [`sources/prs/tensorrt-llm/PR-10479.md`](../sources/prs/tensorrt-llm/PR-10479.md) | [None] [feat] Add densegemm backend for MoE |
| `pr-tensorrt-llm-10532` | upstream-code | [`sources/prs/tensorrt-llm/PR-10532.md`](../sources/prs/tensorrt-llm/PR-10532.md) | [None][feat] MiniMax M2 support |
| `pr-tensorrt-llm-10742` | upstream-code | [`sources/prs/tensorrt-llm/PR-10742.md`](../sources/prs/tensorrt-llm/PR-10742.md) | [https://nvbugs/5669671][fix] Support GuidedDecoder with sharded logits (pick #10698) |
| `pr-tensorrt-llm-10987` | upstream-code | [`sources/prs/tensorrt-llm/PR-10987.md`](../sources/prs/tensorrt-llm/PR-10987.md) | [TRTLLM-9831][perf] Use TMA.RED to improve effective memory bandwidth |
| `pr-tensorrt-llm-11181` | upstream-code | [`sources/prs/tensorrt-llm/PR-11181.md`](../sources/prs/tensorrt-llm/PR-11181.md) | [https://nvbugs/5854860][fix] Fix cutedsl argmax on sm120 |
| `pr-tensorrt-llm-11381` | upstream-code | [`sources/prs/tensorrt-llm/PR-11381.md`](../sources/prs/tensorrt-llm/PR-11381.md) | [None][feat] Remove non flash attetnion style fmha_v2 kernel for hopper |
| `pr-tensorrt-llm-11697` | upstream-code | [`sources/prs/tensorrt-llm/PR-11697.md`](../sources/prs/tensorrt-llm/PR-11697.md) | [TRTLLM-11092][feat] add support for visual gen FA4 attention backend |
| `pr-tensorrt-llm-11718` | upstream-code | [`sources/prs/tensorrt-llm/PR-11718.md`](../sources/prs/tensorrt-llm/PR-11718.md) | [TRTLLM-11119][feat] Blackwell SageAttention, Integrate into AttentionOp API |
| `pr-tensorrt-llm-11897` | upstream-code | [`sources/prs/tensorrt-llm/PR-11897.md`](../sources/prs/tensorrt-llm/PR-11897.md) | [TRTLLM-10990][feat] Fuse SwiGLU and quant into shared expert |
| `pr-tensorrt-llm-11900` | upstream-code | [`sources/prs/tensorrt-llm/PR-11900.md`](../sources/prs/tensorrt-llm/PR-11900.md) | [TRTLLM-10407][feat] Integrate CuTE DSL top-k kernel for Blackwell |
| `pr-tensorrt-llm-12074` | upstream-code | [`sources/prs/tensorrt-llm/PR-12074.md`](../sources/prs/tensorrt-llm/PR-12074.md) | [TRTLLM-11289][feat] Integrate CuteDSL's bf16 dense GEMMs |
| `pr-tensorrt-llm-12079` | upstream-code | [`sources/prs/tensorrt-llm/PR-12079.md`](../sources/prs/tensorrt-llm/PR-12079.md) | [None][feat] CuteDSL MOE: Add raster along M/N support for blockscaled contiguous backbone kernel |
| `pr-tensorrt-llm-12136` | upstream-code | [`sources/prs/tensorrt-llm/PR-12136.md`](../sources/prs/tensorrt-llm/PR-12136.md) | [None][feat] Add DWDP (Distributed Weight Data Parallelism) support for MoE inference |
| `pr-tensorrt-llm-12354` | upstream-code | [`sources/prs/tensorrt-llm/PR-12354.md`](../sources/prs/tensorrt-llm/PR-12354.md) | [TRTLLM-10407][perf] Add cute dsl single pass multi cta cluster topk |
| `pr-tensorrt-llm-12506` | upstream-code | [`sources/prs/tensorrt-llm/PR-12506.md`](../sources/prs/tensorrt-llm/PR-12506.md) | [None][feat] Add PDL support to CuTE DSL top-k kernels |
| `pr-tensorrt-llm-12799` | upstream-code | [`sources/prs/tensorrt-llm/PR-12799.md`](../sources/prs/tensorrt-llm/PR-12799.md) | [TRTLLM-11797][feat] Add cutedsl moe backend supporting for qwen3.5. |
| `pr-tensorrt-llm-12884` | upstream-code | [`sources/prs/tensorrt-llm/PR-12884.md`](../sources/prs/tensorrt-llm/PR-12884.md) | [TRTLLM-11585][feat] Add CUTEDSL moe backend for nemotron-h |
| `pr-tensorrt-llm-13169` | upstream-code | [`sources/prs/tensorrt-llm/PR-13169.md`](../sources/prs/tensorrt-llm/PR-13169.md) | [https://nvbugs/5945047][fix] Fix cluster launch enablement for SM120 GPUs in allReduce fusion |
| `pr-tensorrt-llm-13219` | upstream-code | [`sources/prs/tensorrt-llm/PR-13219.md`](../sources/prs/tensorrt-llm/PR-13219.md) | [TRTLLM-34871][feat] Add cute dsl FP8 paged MQA logits decode kernel |
| `pr-tensorrt-llm-13340` | upstream-code | [`sources/prs/tensorrt-llm/PR-13340.md`](../sources/prs/tensorrt-llm/PR-13340.md) | [None][feat] Integrate FP4 indexer for DSA on Blackwell |
| `pr-tensorrt-llm-13570` | upstream-code | [`sources/prs/tensorrt-llm/PR-13570.md`](../sources/prs/tensorrt-llm/PR-13570.md) | [TRTLLM-12128][feat] enable SageAttention for Wan/FLUX (new commits) |
| `pr-tensorrt-llm-13595` | upstream-code | [`sources/prs/tensorrt-llm/PR-13595.md`](../sources/prs/tensorrt-llm/PR-13595.md) | [None][feat] Enable EPLB for DeepSeek-V4 |
| `pr-tensorrt-llm-13628` | upstream-code | [`sources/prs/tensorrt-llm/PR-13628.md`](../sources/prs/tensorrt-llm/PR-13628.md) | [None][feat] Fuse FP8 1x128 quantize + UE8M0 scale pack on SM100 |
| `pr-tensorrt-llm-13658` | upstream-code | [`sources/prs/tensorrt-llm/PR-13658.md`](../sources/prs/tensorrt-llm/PR-13658.md) | [None][test] add Nemotron Ultra V3 AutoDeploy accuracy test |
| `pr-tensorrt-llm-13873` | upstream-code | [`sources/prs/tensorrt-llm/PR-13873.md`](../sources/prs/tensorrt-llm/PR-13873.md) | [TRTLLM-12503][feat] Parallel VAE independent scaling and fix arg passing |
| `pr-tensorrt-llm-13929` | upstream-code | [`sources/prs/tensorrt-llm/PR-13929.md`](../sources/prs/tensorrt-llm/PR-13929.md) | [TRTLLM-35237][feat] Add cute dsl FP4 paged MQA logits decode kernel |
| `pr-tensorrt-llm-6538` | upstream-code | [`sources/prs/tensorrt-llm/PR-6538.md`](../sources/prs/tensorrt-llm/PR-6538.md) | [None][feat] Use Separate QKV Input Layout for Context MLA |
| `pr-tensorrt-llm-6809` | upstream-code | [`sources/prs/tensorrt-llm/PR-6809.md`](../sources/prs/tensorrt-llm/PR-6809.md) | [OMNIML-2336][feat] Add NVFP4 x FP8 |
| `pr-tensorrt-llm-7524` | upstream-code | [`sources/prs/tensorrt-llm/PR-7524.md`](../sources/prs/tensorrt-llm/PR-7524.md) | [None][chore] Fix kernel launch param and add TRTLLM MoE backend test |
| `pr-tensorrt-llm-7755` | upstream-code | [`sources/prs/tensorrt-llm/PR-7755.md`](../sources/prs/tensorrt-llm/PR-7755.md) | [None][fix] Fix and add test for TRTLLM MoE backend |
| `pr-tensorrt-llm-7937` | upstream-code | [`sources/prs/tensorrt-llm/PR-7937.md`](../sources/prs/tensorrt-llm/PR-7937.md) | [None][feat] GPT-OSS Sm120/Sm121 Support |
| `pr-tensorrt-llm-8886` | upstream-code | [`sources/prs/tensorrt-llm/PR-8886.md`](../sources/prs/tensorrt-llm/PR-8886.md) | [None][feat] Enable EPLB for trtllm-gen and cutlass backend |
| `pr-tensorrt-llm-9025` | upstream-code | [`sources/prs/tensorrt-llm/PR-9025.md`](../sources/prs/tensorrt-llm/PR-9025.md) | [None][feat] Update TRTLLM MoE cubins; reduce mxfp4 weight padding requirement; tighten TMA bound |
| `pr-tensorrt-llm-9618` | upstream-code | [`sources/prs/tensorrt-llm/PR-9618.md`](../sources/prs/tensorrt-llm/PR-9618.md) | [TRTLLM-9685] [feat] Add gather fc1 kernel by cuteDSL |
| `pr-tilelang-1229` | upstream-code | [`sources/prs/tilelang/PR-1229.md`](../sources/prs/tilelang/PR-1229.md) | [WIP] support more dtypes for tcgen05 |
| `pr-tilelang-1327` | upstream-code | [`sources/prs/tilelang/PR-1327.md`](../sources/prs/tilelang/PR-1327.md) | [Enhancement] add more dtype and fix mma.ws for fp16 for tcgen05 |
| `pr-tilelang-1399` | upstream-code | [`sources/prs/tilelang/PR-1399.md`](../sources/prs/tilelang/PR-1399.md) | [Enhancement] Refactor inflight computing to support dynamic pipeline extents |
| `pr-tilelang-1647` | upstream-code | [`sources/prs/tilelang/PR-1647.md`](../sources/prs/tilelang/PR-1647.md) | [Feat] Allow dangling producer in wasp pipeline planning (#1263) |
| `pr-tilelang-1667` | upstream-code | [`sources/prs/tilelang/PR-1667.md`](../sources/prs/tilelang/PR-1667.md) | [Feature] Support `cp.reduce.async.bulk.tensor` |
| `pr-tilelang-1717` | upstream-code | [`sources/prs/tilelang/PR-1717.md`](../sources/prs/tilelang/PR-1717.md) | [Enhancement] Add explicit global memory load/store intrinsics (ldg/stg 32/64/128) |
| `pr-tilelang-1736` | upstream-code | [`sources/prs/tilelang/PR-1736.md`](../sources/prs/tilelang/PR-1736.md) | Add swizzle layout detection and automatic merging for layout conflicts |
| `pr-tilelang-1762` | upstream-code | [`sources/prs/tilelang/PR-1762.md`](../sources/prs/tilelang/PR-1762.md) | [Feature] Hierarchical reduction and warp reduction intrinsics support |
| `pr-tilelang-1764` | upstream-code | [`sources/prs/tilelang/PR-1764.md`](../sources/prs/tilelang/PR-1764.md) | [Feature] Support tcgen5mma lowering for `.kind::i8` |
| `pr-tilelang-1840` | upstream-code | [`sources/prs/tilelang/PR-1840.md`](../sources/prs/tilelang/PR-1840.md) | [BugFix] Fix Hopper TMA lowering without warp specialization |
| `pr-tilelang-1858` | upstream-code | [`sources/prs/tilelang/PR-1858.md`](../sources/prs/tilelang/PR-1858.md) | [Feature] Add TIR builtins for warp-level vote and block-level predicate sync |
| `pr-tilelang-1866` | upstream-code | [`sources/prs/tilelang/PR-1866.md`](../sources/prs/tilelang/PR-1866.md) | [CUDA] Support tcgen5mma gemm ts |
| `pr-tilelang-1874` | upstream-code | [`sources/prs/tilelang/PR-1874.md`](../sources/prs/tilelang/PR-1874.md) | [Feature] Support cluster launch, query, synchronization and barrier operations |
| `pr-tilelang-1882` | upstream-code | [`sources/prs/tilelang/PR-1882.md`](../sources/prs/tilelang/PR-1882.md) | [Feature] 2-SM support for TMA, TMEM and TCGEN5MMA on Blackwell |
| `pr-tilelang-1909` | upstream-code | [`sources/prs/tilelang/PR-1909.md`](../sources/prs/tilelang/PR-1909.md) | [Feature] Add Producer-Consumer Warp Specialization and T.tma_copy() API |
| `pr-tilelang-1937` | upstream-code | [`sources/prs/tilelang/PR-1937.md`](../sources/prs/tilelang/PR-1937.md) | Fix predicated cp.async pipeline scheduling |
| `pr-tilelang-1945` | upstream-code | [`sources/prs/tilelang/PR-1945.md`](../sources/prs/tilelang/PR-1945.md) | [Feature] Block-scaled GEMM support for MXFP8 on Blackwell |
| `pr-tilelang-1953` | upstream-code | [`sources/prs/tilelang/PR-1953.md`](../sources/prs/tilelang/PR-1953.md) | [PIpeline] Enable software pipelining when warp specialization is unavailable |
| `pr-tilelang-1981` | upstream-code | [`sources/prs/tilelang/PR-1981.md`](../sources/prs/tilelang/PR-1981.md) | [Feature] Support TMA store in T.tma_copy() |
| `pr-tilelang-2002` | upstream-code | [`sources/prs/tilelang/PR-2002.md`](../sources/prs/tilelang/PR-2002.md) | [Refactor][Pipeline] Run pipeline rewriting before layout inference and stabilize tiled WS |
| `pr-tilelang-2003` | upstream-code | [`sources/prs/tilelang/PR-2003.md`](../sources/prs/tilelang/PR-2003.md) | [Transform] Add InjectTcgen05Fence pass |
| `pr-tilelang-2024` | upstream-code | [`sources/prs/tilelang/PR-2024.md`](../sources/prs/tilelang/PR-2024.md) | Re-enable deprecated `TL_DISABLE_TMA_LOWER` pass config for TMA store |
| `pr-tilelang-2052` | upstream-code | [`sources/prs/tilelang/PR-2052.md`](../sources/prs/tilelang/PR-2052.md) | [Bugfix] Use shared::cta instead of shared::cluster for non-cluster T… |
| `pr-tilelang-2063` | upstream-code | [`sources/prs/tilelang/PR-2063.md`](../sources/prs/tilelang/PR-2063.md) | [CUDA] Support int4 `T.gemm` |
| `pr-tilelang-2087` | upstream-code | [`sources/prs/tilelang/PR-2087.md`](../sources/prs/tilelang/PR-2087.md) | [Bugfix] Enable `.shared::cta` in TMA copy paths only on CUDA 12.8+ |
| `pr-tilelang-2092` | upstream-code | [`sources/prs/tilelang/PR-2092.md`](../sources/prs/tilelang/PR-2092.md) | [BugFix] Relax loop wait and adjust trailing drain behavior in async pipeline tests |
| `pr-tilelang-2107` | upstream-code | [`sources/prs/tilelang/PR-2107.md`](../sources/prs/tilelang/PR-2107.md) | [TMA] Support FP4 TensorMap TMA copies |
| `pr-tilelang-2153` | upstream-code | [`sources/prs/tilelang/PR-2153.md`](../sources/prs/tilelang/PR-2153.md) | [codex] Split GEMM implementations by backend |
| `pr-tilelang-2159` | upstream-code | [`sources/prs/tilelang/PR-2159.md`](../sources/prs/tilelang/PR-2159.md) | [Autotune] Add pipeline, grouped compilation, and multi-GPU benchmark support |
| `pr-tilelang-2166` | upstream-code | [`sources/prs/tilelang/PR-2166.md`](../sources/prs/tilelang/PR-2166.md) | [BugFix] Consider non-local store in external call and SIMT producer for warp specialize |
| `pr-triton-10172` | upstream-code | [`sources/prs/triton/PR-10172.md`](../sources/prs/triton/PR-10172.md) | [AMD][TDM] Pipeline tt.descriptor_gather through the TDM async chain |
| `pr-triton-9666` | upstream-code | [`sources/prs/triton/PR-9666.md`](../sources/prs/triton/PR-9666.md) | [AMD] Enable loop unrolling for Gluon warp-pipelined kernels |
| `pr-vllm-11743` | upstream-code | [`sources/prs/vllm/PR-11743.md`](../sources/prs/vllm/PR-11743.md) | [Core] Support fully transparent sleep mode |
| `pr-vllm-13726` | upstream-code | [`sources/prs/vllm/PR-13726.md`](../sources/prs/vllm/PR-13726.md) | [V1] V1 Enablement Oracle  |
| `pr-vllm-16113` | upstream-code | [`sources/prs/vllm/PR-16113.md`](../sources/prs/vllm/PR-16113.md) | Upstream Llama4 Support to Main |
| `pr-vllm-16756` | upstream-code | [`sources/prs/vllm/PR-16756.md`](../sources/prs/vllm/PR-16756.md) | [torch.compile][ROCm] Fuse quantization onto attention using a torch.compile pass |
| `pr-vllm-16859` | upstream-code | [`sources/prs/vllm/PR-16859.md`](../sources/prs/vllm/PR-16859.md) | Update PyTorch to 2.7.0 |
| `pr-vllm-18343` | upstream-code | [`sources/prs/vllm/PR-18343.md`](../sources/prs/vllm/PR-18343.md) | [Feature] Expert Parallelism Load Balancer (EPLB) |
| `pr-vllm-20358` | upstream-code | [`sources/prs/vllm/PR-20358.md`](../sources/prs/vllm/PR-20358.md) | Update PyTorch to 2.8.0 |
| `pr-vllm-21078` | upstream-code | [`sources/prs/vllm/PR-21078.md`](../sources/prs/vllm/PR-21078.md) | [Kernel] Flashinfer MLA (trtllm-gen) decode kernel integration |
| `pr-vllm-21088` | upstream-code | [`sources/prs/vllm/PR-21088.md`](../sources/prs/vllm/PR-21088.md) | [v1] Add Whisper model support (encoder-decoder) |
| `pr-vllm-21229` | upstream-code | [`sources/prs/vllm/PR-21229.md`](../sources/prs/vllm/PR-21229.md) | [Feature][Kernel]FusedMoE LoRA |
| `pr-vllm-21716` | upstream-code | [`sources/prs/vllm/PR-21716.md`](../sources/prs/vllm/PR-21716.md) | [NVIDIA] Support Flashinfer TRTLLM FP8-q/kv/out Attention Kernel |
| `pr-vllm-22095` | upstream-code | [`sources/prs/vllm/PR-22095.md`](../sources/prs/vllm/PR-22095.md) | [NVIDIA] Support Flashinfer TRT-LLM Prefill Attention Kernel |
| `pr-vllm-22895` | upstream-code | [`sources/prs/vllm/PR-22895.md`](../sources/prs/vllm/PR-22895.md) | [Kernel] Added flashinfer fp8 per-tensor gemms |
| `pr-vllm-23671` | upstream-code | [`sources/prs/vllm/PR-23671.md`](../sources/prs/vllm/PR-23671.md) | [NVIDIA] Support SiluMul + NVFP4 quant fusion |
| `pr-vllm-23727` | upstream-code | [`sources/prs/vllm/PR-23727.md`](../sources/prs/vllm/PR-23727.md) | [Bugfix][Misc] Fix silu_and_mul_nvfp4_quant issue and extract common utils for nvfp4 kernel source files |
| `pr-vllm-23734` | upstream-code | [`sources/prs/vllm/PR-23734.md`](../sources/prs/vllm/PR-23734.md) | [Feature] Support Decode Context Parallel (DCP) for MLA |
| `pr-vllm-24248` | upstream-code | [`sources/prs/vllm/PR-24248.md`](../sources/prs/vllm/PR-24248.md) | [PERF] Allreduce fusion. Support torch native matching. Tuning of the thresholds |
| `pr-vllm-24440` | upstream-code | [`sources/prs/vllm/PR-24440.md`](../sources/prs/vllm/PR-24440.md) | [Transform] [Quantization] Add QuTLASS support to vLLM |
| `pr-vllm-24833` | upstream-code | [`sources/prs/vllm/PR-24833.md`](../sources/prs/vllm/PR-24833.md) | [Bugfix] Fix accuracy issue for silu_mul + nvfp4 quant fusion kernel |
| `pr-vllm-25990` | upstream-code | [`sources/prs/vllm/PR-25990.md`](../sources/prs/vllm/PR-25990.md) | [MoE] Nvfp4 Masked Gemm: Add flashinfer grouped_gemm_nt_masked |
| `pr-vllm-27134` | upstream-code | [`sources/prs/vllm/PR-27134.md`](../sources/prs/vllm/PR-27134.md) | [Kernels] Enable FlashInfer FP8 Blockscale on SM90 (for TEP DSR1) |
| `pr-vllm-27232` | upstream-code | [`sources/prs/vllm/PR-27232.md`](../sources/prs/vllm/PR-27232.md) | [Bugfix] Ensure calculated KV scales are applied in attention. |
| `pr-vllm-28687` | upstream-code | [`sources/prs/vllm/PR-28687.md`](../sources/prs/vllm/PR-28687.md) | [Performance] Reduce DeepGEMM N dim restriction from 128 to 64 multiplier  |
| `pr-vllm-28841` | upstream-code | [`sources/prs/vllm/PR-28841.md`](../sources/prs/vllm/PR-28841.md) | [Bugfix] Fix GPT-OSS AR+NORM fusion |
| `pr-vllm-28878` | upstream-code | [`sources/prs/vllm/PR-28878.md`](../sources/prs/vllm/PR-28878.md) | [Bugfix] Make compressed-tensors MoEs respect ignored layers |
| `pr-vllm-30885` | upstream-code | [`sources/prs/vllm/PR-30885.md`](../sources/prs/vllm/PR-30885.md) | [Kernel][Performance] Enable smaller Scaling Factor tiling for NVFP4 small-batch decoding |
| `pr-vllm-31916` | upstream-code | [`sources/prs/vllm/PR-31916.md`](../sources/prs/vllm/PR-31916.md) | [1/N][Attention] Restructure attention: move files |
| `pr-vllm-32064` | upstream-code | [`sources/prs/vllm/PR-32064.md`](../sources/prs/vllm/PR-32064.md) | [5/N][Attention] Finish eliminating `vllm/attention` folder |
| `pr-vllm-32195` | upstream-code | [`sources/prs/vllm/PR-32195.md`](../sources/prs/vllm/PR-32195.md) | Add TMA support to fused_moe_lora kernel |
| `pr-vllm-32619` | upstream-code | [`sources/prs/vllm/PR-32619.md`](../sources/prs/vllm/PR-32619.md) | [Perf] Create TMA-aligned input scale tensor for DeepGemm on Hopper |
| `pr-vllm-34260` | upstream-code | [`sources/prs/vllm/PR-34260.md`](../sources/prs/vllm/PR-34260.md) | [Model Bash]: Improve FP8 Oracle for Config Specific Kernel Selection |
| `pr-vllm-37970` | upstream-code | [`sources/prs/vllm/PR-37970.md`](../sources/prs/vllm/PR-37970.md) | [Kernel] Optimize SM120 CUTLASS blockwise FP8 GEMM |
| `pr-vllm-39306` | upstream-code | [`sources/prs/vllm/PR-39306.md`](../sources/prs/vllm/PR-39306.md) | Use CU_MEMCPY_SRC_ACCESS_ORDER_ANY for batch KV cache swaps |
| `pr-vllm-39391` | upstream-code | [`sources/prs/vllm/PR-39391.md`](../sources/prs/vllm/PR-39391.md) | fix: clamp NaN/Inf in topk_softmax to prevent duplicate expert IDs |
| `pr-vllm-39917` | upstream-code | [`sources/prs/vllm/PR-39917.md`](../sources/prs/vllm/PR-39917.md) | [Core] Replace routing replay with device cache and async D2H pipeline |
| `pr-vllm-40408` | upstream-code | [`sources/prs/vllm/PR-40408.md`](../sources/prs/vllm/PR-40408.md) | [Perf] Batch invariance with Cutlass fp8 support, 28.9% E2E latency improvement |
| `pr-vllm-7174` | upstream-code | [`sources/prs/vllm/PR-7174.md`](../sources/prs/vllm/PR-7174.md) | [Kernel] (1/N) Machete - Hopper Optimized Mixed Precision Linear Kernel  |

<a id="register-budgeting"></a>
## register-budgeting

2 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `blog-amandeep-nvfp4` | community-note | [`sources/blogs/amandeep-nvfp4-attempts.md`](../sources/blogs/amandeep-nvfp4-attempts.md) | Twelve Attempts at NVFP4 Batched GEMV |
| `contest-gpumode-p1` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-1-gemv.md`](../sources/contests/gpu-mode-nvfp4/problem-1-gemv.md) | GPU Mode NVFP4 Hackathon - Problem 1: Batched GEMV |

<a id="register-reuse"></a>
## register-reuse

3 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `blog-yue-nvfp4` | community-note | [`sources/blogs/yue-nvfp4-hackathon.md`](../sources/blogs/yue-nvfp4-hackathon.md) | Blackwell NVFP4 Kernel Hackathon Journey |
| `contest-gpumode-p1` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-1-gemv.md`](../sources/contests/gpu-mode-nvfp4/problem-1-gemv.md) | GPU Mode NVFP4 Hackathon - Problem 1: Batched GEMV |
| `contest-gpumode-p2` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-2-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-2-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 2: NVFP4 GEMM |

<a id="swizzling"></a>
## swizzling

27 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `contest-gpumode-p2` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-2-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-2-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 2: NVFP4 GEMM |
| `pr-cutlass-1753` | upstream-code | [`sources/prs/cutlass/PR-1753.md`](../sources/prs/cutlass/PR-1753.md) | Fix EVT for cutlass::gemm::kernel::DefaultGemmWithVisitor's behavior when constructing GemmUniversalAdapter |
| `pr-flash-attention-1823` | upstream-code | [`sources/prs/flash-attention/PR-1823.md`](../sources/prs/flash-attention/PR-1823.md) | Add sorting and head swizzle to varlen scheduler |
| `pr-flash-attention-2390` | upstream-code | [`sources/prs/flash-attention/PR-2390.md`](../sources/prs/flash-attention/PR-2390.md) | [Cute,Sm100,Bwd] refine bwd swizzle for deterministic |
| `pr-flashinfer-1176` | upstream-code | [`sources/prs/flashinfer/PR-1176.md`](../sources/prs/flashinfer/PR-1176.md) | Expose fp4 blockscale swizzling kernel |
| `pr-flashinfer-1371` | upstream-code | [`sources/prs/flashinfer/PR-1371.md`](../sources/prs/flashinfer/PR-1371.md) | bugfix: fixed cutlass fused moe usage of FP4QuantizationSFLayout::SWIZZLED |
| `pr-flashinfer-1530` | upstream-code | [`sources/prs/flashinfer/PR-1530.md`](../sources/prs/flashinfer/PR-1530.md) | bugfix: Fix compile error for undefined swizzle enum. |
| `pr-flashinfer-2025` | upstream-code | [`sources/prs/flashinfer/PR-2025.md`](../sources/prs/flashinfer/PR-2025.md) | perf: Speed up fp4 quantization for small batch with swizzling for cutlass MoE |
| `pr-flashinfer-2330` | upstream-code | [`sources/prs/flashinfer/PR-2330.md`](../sources/prs/flashinfer/PR-2330.md) | feat: expose swizzled_input_sf parameter for CUTLASS fused MOE |
| `pr-flashinfer-2954` | upstream-code | [`sources/prs/flashinfer/PR-2954.md`](../sources/prs/flashinfer/PR-2954.md) | Only swizzle on v block scale; rename kv_block_scales to kv_cache_sf |
| `pr-flashinfer-3097` | upstream-code | [`sources/prs/flashinfer/PR-3097.md`](../sources/prs/flashinfer/PR-3097.md) | Support NVFP4 KV for prefill and batch attention kernels |
| `pr-sglang-22064` | upstream-code | [`sources/prs/sglang/PR-22064.md`](../sources/prs/sglang/PR-22064.md) | [Diffusion] Fix weight scale swizzle and add large-M kernel config for FLUX.2-dev-NVFP4 |
| `pr-sglang-22204` | upstream-code | [`sources/prs/sglang/PR-22204.md`](../sources/prs/sglang/PR-22204.md) | [RL] Refactor NVFP4 shuffling/swizzling to in-place replacement |
| `pr-tensorrt-llm-13708` | upstream-code | [`sources/prs/tensorrt-llm/PR-13708.md`](../sources/prs/tensorrt-llm/PR-13708.md) | [https://nvbugs/6094072][fix] swizzle GPT-OSS dummy MXFP4 weights |
| `pr-tensorrt-llm-14054` | upstream-code | [`sources/prs/tensorrt-llm/PR-14054.md`](../sources/prs/tensorrt-llm/PR-14054.md) | [https://nvbugs/6162323][fix] Make mxfp4 H20 swizzle WAR more robust |
| `pr-tensorrt-llm-9618` | upstream-code | [`sources/prs/tensorrt-llm/PR-9618.md`](../sources/prs/tensorrt-llm/PR-9618.md) | [TRTLLM-9685] [feat] Add gather fc1 kernel by cuteDSL |
| `pr-tensorrt-llm-9854` | upstream-code | [`sources/prs/tensorrt-llm/PR-9854.md`](../sources/prs/tensorrt-llm/PR-9854.md) | [None][feat] Port fp4 quantization kernel optimization from FlashInfer |
| `pr-tilelang-1667` | upstream-code | [`sources/prs/tilelang/PR-1667.md`](../sources/prs/tilelang/PR-1667.md) | [Feature] Support `cp.reduce.async.bulk.tensor` |
| `pr-tilelang-1736` | upstream-code | [`sources/prs/tilelang/PR-1736.md`](../sources/prs/tilelang/PR-1736.md) | Add swizzle layout detection and automatic merging for layout conflicts |
| `pr-tilelang-1874` | upstream-code | [`sources/prs/tilelang/PR-1874.md`](../sources/prs/tilelang/PR-1874.md) | [Feature] Support cluster launch, query, synchronization and barrier operations |
| `pr-tilelang-1882` | upstream-code | [`sources/prs/tilelang/PR-1882.md`](../sources/prs/tilelang/PR-1882.md) | [Feature] 2-SM support for TMA, TMEM and TCGEN5MMA on Blackwell |
| `pr-triton-10148` | upstream-code | [`sources/prs/triton/PR-10148.md`](../sources/prs/triton/PR-10148.md) | [Reland][NVIDIA] Support swizzle 0 TMA + MMA for Hopper and Blackwell |
| `pr-triton-10214` | upstream-code | [`sources/prs/triton/PR-10214.md`](../sources/prs/triton/PR-10214.md) | Allow MXFP8 LHS with Hopper-swizzled MXFP4 RHS |
| `pr-vllm-23140` | upstream-code | [`sources/prs/vllm/PR-23140.md`](../sources/prs/vllm/PR-23140.md) | Fix nvfp4 swizzling |
| `pr-vllm-23465` | upstream-code | [`sources/prs/vllm/PR-23465.md`](../sources/prs/vllm/PR-23465.md) | [Attention][FA3] Update FA3 to include new swizzle optimization |
| `pr-vllm-34043` | upstream-code | [`sources/prs/vllm/PR-34043.md`](../sources/prs/vllm/PR-34043.md) | Reapply [Attention][FA3] Update FA3 to include new swizzle optimization |
| `pr-vllm-34389` | upstream-code | [`sources/prs/vllm/PR-34389.md`](../sources/prs/vllm/PR-34389.md) | [Custom Ops] Add functional + out variant for scaled_fp4_quant |

<a id="tile-scheduling"></a>
## tile-scheduling

145 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `contest-flashinfer-track-a` | contest-report | [`sources/contests/flashinfer-mlsys26/track-a-fused-moe.md`](../sources/contests/flashinfer-mlsys26/track-a-fused-moe.md) | FlashInfer MLSys 2026 - Track A: Fused MoE FP8 |
| `contest-gpumode-p4` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 4: Grouped GEMM |
| `pr-cccl-cub-3236` | upstream-code | [`sources/prs/cccl-cub/PR-3236.md`](../sources/prs/cccl-cub/PR-3236.md) | Fix scan / sm90 perf regression  |
| `pr-cccl-cub-3559` | upstream-code | [`sources/prs/cccl-cub/PR-3559.md`](../sources/prs/cccl-cub/PR-3559.md) | Add b200 tunings for scan.exclusive.sum |
| `pr-cccl-cub-3691` | upstream-code | [`sources/prs/cccl-cub/PR-3691.md`](../sources/prs/cccl-cub/PR-3691.md) | Fix SM100 histogram tunings |
| `pr-cccl-cub-4961` | upstream-code | [`sources/prs/cccl-cub/PR-4961.md`](../sources/prs/cccl-cub/PR-4961.md) | Add nondeterministic reduce that uses atomics |
| `pr-cccl-cub-5314` | upstream-code | [`sources/prs/cccl-cub/PR-5314.md`](../sources/prs/cccl-cub/PR-5314.md) | CUB - Add internal integer utils and tests (Split `WarpReduce` PR) |
| `pr-cccl-cub-6077` | upstream-code | [`sources/prs/cccl-cub/PR-6077.md`](../sources/prs/cccl-cub/PR-6077.md) | [CUB] Use `BlockLoadToShared` in `DeviceMerge` |
| `pr-cccl-cub-6597` | upstream-code | [`sources/prs/cccl-cub/PR-6597.md`](../sources/prs/cccl-cub/PR-6597.md) | Split fixed-size segmented reduce dispatch header |
| `pr-cccl-cub-6811` | upstream-code | [`sources/prs/cccl-cub/PR-6811.md`](../sources/prs/cccl-cub/PR-6811.md) | Integrate decoupled lookahead warpspeed scan |
| `pr-cccl-cub-7093` | upstream-code | [`sources/prs/cccl-cub/PR-7093.md`](../sources/prs/cccl-cub/PR-7093.md) | Implement new tuning API arch dispatching |
| `pr-cccl-cub-7346` | upstream-code | [`sources/prs/cccl-cub/PR-7346.md`](../sources/prs/cccl-cub/PR-7346.md) | Implement the new tuning API for deterministic (rfa) reduce dispatch |
| `pr-cccl-cub-7669` | upstream-code | [`sources/prs/cccl-cub/PR-7669.md`](../sources/prs/cccl-cub/PR-7669.md) | Implement the new tuning API for `DeviceRleDispatch` |
| `pr-cccl-cub-7718` | upstream-code | [`sources/prs/cccl-cub/PR-7718.md`](../sources/prs/cccl-cub/PR-7718.md) | Optimize non fixed size segmented reduce for small segments using max_segment_size |
| `pr-cccl-cub-7805` | upstream-code | [`sources/prs/cccl-cub/PR-7805.md`](../sources/prs/cccl-cub/PR-7805.md) | Forward policy hub from `dispatch_streaming_arg_reduce_t` to `reduce::dispatch` |
| `pr-cccl-cub-7807` | upstream-code | [`sources/prs/cccl-cub/PR-7807.md`](../sources/prs/cccl-cub/PR-7807.md) | Implement the new tuning API for `detail::reduce::dispatch_streaming_arg_reduce_t` |
| `pr-cccl-cub-7810` | upstream-code | [`sources/prs/cccl-cub/PR-7810.md`](../sources/prs/cccl-cub/PR-7810.md) | Use the new tuning API internally for `detail::transform::dispatch` |
| `pr-cccl-cub-7814` | upstream-code | [`sources/prs/cccl-cub/PR-7814.md`](../sources/prs/cccl-cub/PR-7814.md) | [Backport branch/3.3.x] Forward policy hub from `dispatch_streaming_arg_reduce_t` to `reduce::dispatch` |
| `pr-cccl-cub-7844` | upstream-code | [`sources/prs/cccl-cub/PR-7844.md`](../sources/prs/cccl-cub/PR-7844.md) | Implement the new tuning API for `DispatchSegmentedRadixSort` |
| `pr-cccl-cub-7874` | upstream-code | [`sources/prs/cccl-cub/PR-7874.md`](../sources/prs/cccl-cub/PR-7874.md) | Implement the new tuning API for `DispatchSegmentedSort` |
| `pr-cccl-cub-7928` | upstream-code | [`sources/prs/cccl-cub/PR-7928.md`](../sources/prs/cccl-cub/PR-7928.md) | Implement the new tuning API for `DispatchTopK` |
| `pr-cccl-cub-8311` | upstream-code | [`sources/prs/cccl-cub/PR-8311.md`](../sources/prs/cccl-cub/PR-8311.md) | Implement the new tuning API for `DispatchSelectIf` |
| `pr-cccl-cub-8332` | upstream-code | [`sources/prs/cccl-cub/PR-8332.md`](../sources/prs/cccl-cub/PR-8332.md) | simplify dispatch segmented reduce to use latest dispatch and new tunings API |
| `pr-cccl-cub-8352` | upstream-code | [`sources/prs/cccl-cub/PR-8352.md`](../sources/prs/cccl-cub/PR-8352.md) | Apply some random warpspeed tunings |
| `pr-cccl-cub-8538` | upstream-code | [`sources/prs/cccl-cub/PR-8538.md`](../sources/prs/cccl-cub/PR-8538.md) | Implement the new tuning API for `detail::batched_topk::dispatch_batched_topk` |
| `pr-cccl-cub-8742` | upstream-code | [`sources/prs/cccl-cub/PR-8742.md`](../sources/prs/cccl-cub/PR-8742.md) | Use the new tuning API internally for `detail::topk::dispatch` |
| `pr-cccl-cub-8826` | upstream-code | [`sources/prs/cccl-cub/PR-8826.md`](../sources/prs/cccl-cub/PR-8826.md) | Use the new tuning API internally for `detail::reduce[_nd]::dispatch[_nd]` |
| `pr-cutlass-1350` | upstream-code | [`sources/prs/cutlass/PR-1350.md`](../sources/prs/cutlass/PR-1350.md) | Add couple configs into generator.py for mixed input MM |
| `pr-cutlass-2161` | upstream-code | [`sources/prs/cutlass/PR-2161.md`](../sources/prs/cutlass/PR-2161.md) | Blockwise Improvement and Programmatic Dependent Launch |
| `pr-cutlass-2172` | upstream-code | [`sources/prs/cutlass/PR-2172.md`](../sources/prs/cutlass/PR-2172.md) | Fix SM90 beta=1 hang and stream-K launch errors |
| `pr-cutlass-2267` | upstream-code | [`sources/prs/cutlass/PR-2267.md`](../sources/prs/cutlass/PR-2267.md) | war to fix blackwell grouped groupwise hang |
| `pr-cutlass-2291` | upstream-code | [`sources/prs/cutlass/PR-2291.md`](../sources/prs/cutlass/PR-2291.md) | Correct divmod order in example 77 (blackwell fmha) |
| `pr-cutlass-2366` | upstream-code | [`sources/prs/cutlass/PR-2366.md`](../sources/prs/cutlass/PR-2366.md) | [ex77] fix mla split; add fwd lse; add bwd varlen |
| `pr-cutlass-2596` | upstream-code | [`sources/prs/cutlass/PR-2596.md`](../sources/prs/cutlass/PR-2596.md) | Fix broken imports in heuristics_provider.py |
| `pr-deepgemm-103` | upstream-code | [`sources/prs/deepgemm/PR-103.md`](../sources/prs/deepgemm/PR-103.md) | Grouped GEMM skip useless computation for unaligned Ms |
| `pr-deepgemm-112` | upstream-code | [`sources/prs/deepgemm/PR-112.md`](../sources/prs/deepgemm/PR-112.md) | Add more GPU architectures support |
| `pr-deepgemm-158` | upstream-code | [`sources/prs/deepgemm/PR-158.md`](../sources/prs/deepgemm/PR-158.md) | Fix inappropriate configs for some small shapes |
| `pr-deepgemm-168` | upstream-code | [`sources/prs/deepgemm/PR-168.md`](../sources/prs/deepgemm/PR-168.md) | Fix performance issue of m-grouped contiguous GEMMs. |
| `pr-deepgemm-193` | upstream-code | [`sources/prs/deepgemm/PR-193.md`](../sources/prs/deepgemm/PR-193.md) | Fix multicast bug and optimize masked GEMM |
| `pr-deepgemm-198` | upstream-code | [`sources/prs/deepgemm/PR-198.md`](../sources/prs/deepgemm/PR-198.md) | Make various updates and fixes |
| `pr-deepgemm-316` | upstream-code | [`sources/prs/deepgemm/PR-316.md`](../sources/prs/deepgemm/PR-316.md) | Add various optimizations and Mega MoE benchmarks |
| `pr-deepgemm-328` | upstream-code | [`sources/prs/deepgemm/PR-328.md`](../sources/prs/deepgemm/PR-328.md) | Sync nv_dev with upstream #316 (Mega MoE optimizations & benchmarks) |
| `pr-deepgemm-74` | upstream-code | [`sources/prs/deepgemm/PR-74.md`](../sources/prs/deepgemm/PR-74.md) | Performance: Larger BlockTile optimizations enable 1470+ TF FP8 on the "H800"-SXM |
| `pr-deepgemm-88` | upstream-code | [`sources/prs/deepgemm/PR-88.md`](../sources/prs/deepgemm/PR-88.md) | Support TMA multicast on B with m_grouped_gemm_contiguous. |
| `pr-flash-attention-1100` | upstream-code | [`sources/prs/flash-attention/PR-1100.md`](../sources/prs/flash-attention/PR-1100.md) | Fp8 kernel with "in-kernel" transpose of V in producer |
| `pr-flash-attention-1233` | upstream-code | [`sources/prs/flash-attention/PR-1233.md`](../sources/prs/flash-attention/PR-1233.md) | Add local attention in Hopper FAv3 |
| `pr-flash-attention-1236` | upstream-code | [`sources/prs/flash-attention/PR-1236.md`](../sources/prs/flash-attention/PR-1236.md) | FA3 kvcache + split kv + gqa parallelization |
| `pr-flash-attention-1361` | upstream-code | [`sources/prs/flash-attention/PR-1361.md`](../sources/prs/flash-attention/PR-1361.md) | Fix FA3 Varlen Performance regression |
| `pr-flash-attention-1823` | upstream-code | [`sources/prs/flash-attention/PR-1823.md`](../sources/prs/flash-attention/PR-1823.md) | Add sorting and head swizzle to varlen scheduler |
| `pr-flash-attention-1893` | upstream-code | [`sources/prs/flash-attention/PR-1893.md`](../sources/prs/flash-attention/PR-1893.md) | Improve causal backward determinism perf with SPT schedule |
| `pr-flash-attention-1934` | upstream-code | [`sources/prs/flash-attention/PR-1934.md`](../sources/prs/flash-attention/PR-1934.md) | feat: Adding varlen support to cute-dsl sm80 bwd |
| `pr-flash-attention-1940` | upstream-code | [`sources/prs/flash-attention/PR-1940.md`](../sources/prs/flash-attention/PR-1940.md) | [Cute,Fwd,Sm100] Implement SplitKV |
| `pr-flash-attention-2033` | upstream-code | [`sources/prs/flash-attention/PR-2033.md`](../sources/prs/flash-attention/PR-2033.md) | [Cute,Bwd,Sm100] enable deterministic mode for sm100 bwd and fix race conditions |
| `pr-flash-attention-2043` | upstream-code | [`sources/prs/flash-attention/PR-2043.md`](../sources/prs/flash-attention/PR-2043.md) | [Cute,Fwd] Extend score_mod to variable sequence length |
| `pr-flash-attention-2218` | upstream-code | [`sources/prs/flash-attention/PR-2218.md`](../sources/prs/flash-attention/PR-2218.md) | [Ai-assisted] CLC work stealing |
| `pr-flash-attention-2236` | upstream-code | [`sources/prs/flash-attention/PR-2236.md`](../sources/prs/flash-attention/PR-2236.md) | [Cute,Flex,Fwd] Allow vectorized score_mod definitions |
| `pr-flash-attention-2333` | upstream-code | [`sources/prs/flash-attention/PR-2333.md`](../sources/prs/flash-attention/PR-2333.md) | Add SM120 varlen attention support |
| `pr-flash-attention-2390` | upstream-code | [`sources/prs/flash-attention/PR-2390.md`](../sources/prs/flash-attention/PR-2390.md) | [Cute,Sm100,Bwd] refine bwd swizzle for deterministic |
| `pr-flash-attention-2412` | upstream-code | [`sources/prs/flash-attention/PR-2412.md`](../sources/prs/flash-attention/PR-2412.md) | Feat([FA4][CUTE DSL]) Add head_dim=256 support (forward + backward) |
| `pr-flash-attention-2441` | upstream-code | [`sources/prs/flash-attention/PR-2441.md`](../sources/prs/flash-attention/PR-2441.md) | [Cute,Sm100,Fwd] add MLA 64/512 with topk sparsity for MQA 128 heads |
| `pr-flash-attention-2455` | upstream-code | [`sources/prs/flash-attention/PR-2455.md`](../sources/prs/flash-attention/PR-2455.md) | Add CLC scheduler heuristic |
| `pr-flash-attention-2488` | upstream-code | [`sources/prs/flash-attention/PR-2488.md`](../sources/prs/flash-attention/PR-2488.md) | [hd256] Improve forward kernel with exp2 FMA emulation (3% to 9% performance gain) |
| `pr-flash-attention-2489` | upstream-code | [`sources/prs/flash-attention/PR-2489.md`](../sources/prs/flash-attention/PR-2489.md) | [hd256] Add TMA paged KV support to SM100 2CTA forward kernel |
| `pr-flash-attention-2497` | upstream-code | [`sources/prs/flash-attention/PR-2497.md`](../sources/prs/flash-attention/PR-2497.md) | [FA4][hd256] Backward TMA bulk-store epilogue + LSE/dpsum coalesce |
| `pr-flash-attention-2515` | upstream-code | [`sources/prs/flash-attention/PR-2515.md`](../sources/prs/flash-attention/PR-2515.md) | Fix ZeroDivisionError in num_splits_heuristic for empty Q workloads |
| `pr-flashinfer-1015` | upstream-code | [`sources/prs/flashinfer/PR-1015.md`](../sources/prs/flashinfer/PR-1015.md) | add multi-item scoring |
| `pr-flashinfer-1039` | upstream-code | [`sources/prs/flashinfer/PR-1039.md`](../sources/prs/flashinfer/PR-1039.md) | [nvidia] initial support for blackwell kernels |
| `pr-flashinfer-1106` | upstream-code | [`sources/prs/flashinfer/PR-1106.md`](../sources/prs/flashinfer/PR-1106.md) | bugfix: host-precomuted plan function for blackwell fmha |
| `pr-flashinfer-1548` | upstream-code | [`sources/prs/flashinfer/PR-1548.md`](../sources/prs/flashinfer/PR-1548.md) | perf: Enable SplitK and fix autotuner for trtllm fp4 fused moe |
| `pr-flashinfer-1668` | upstream-code | [`sources/prs/flashinfer/PR-1668.md`](../sources/prs/flashinfer/PR-1668.md) | TGV GEMM as a BF16 backend alternative to cuBLAS |
| `pr-flashinfer-2276` | upstream-code | [`sources/prs/flashinfer/PR-2276.md`](../sources/prs/flashinfer/PR-2276.md) | feat: add GDN Attention |
| `pr-flashinfer-2422` | upstream-code | [`sources/prs/flashinfer/PR-2422.md`](../sources/prs/flashinfer/PR-2422.md) | refactor: reduce hopper's gdn prefill compilation time and fix docstring. |
| `pr-flashinfer-2557` | upstream-code | [`sources/prs/flashinfer/PR-2557.md`](../sources/prs/flashinfer/PR-2557.md) | [Bugfix][comm] Fix FP4 one-shot launch config instability in trtllm_allreduce_fusion |
| `pr-flashinfer-2630` | upstream-code | [`sources/prs/flashinfer/PR-2630.md`](../sources/prs/flashinfer/PR-2630.md) | Add parallel attention |
| `pr-flashinfer-2709` | upstream-code | [`sources/prs/flashinfer/PR-2709.md`](../sources/prs/flashinfer/PR-2709.md) | Mamba2 SSD Combined Forward Pass (Blackwell CuTe DSL Kernel) |
| `pr-flashinfer-2914` | upstream-code | [`sources/prs/flashinfer/PR-2914.md`](../sources/prs/flashinfer/PR-2914.md) | feat: Add cuBLASLt backend for `mm_bf16` and enable multi-tactic autotuning for FP8/MXFP8 runners |
| `pr-flashinfer-2928` | upstream-code | [`sources/prs/flashinfer/PR-2928.md`](../sources/prs/flashinfer/PR-2928.md) | fix: clamp enable_pdl=True to False on SM < 90 to prevent PDL PTX on Ampere |
| `pr-flashinfer-3001` | upstream-code | [`sources/prs/flashinfer/PR-3001.md`](../sources/prs/flashinfer/PR-3001.md) | [feat] Add blackwell GDN prefill kernel |
| `pr-flashinfer-3115` | upstream-code | [`sources/prs/flashinfer/PR-3115.md`](../sources/prs/flashinfer/PR-3115.md) | perf(autotuner): replace power-of-2 token buckets with hybrid spacing & fix missing routing_replay_out arg |
| `pr-flashinfer-3155` | upstream-code | [`sources/prs/flashinfer/PR-3155.md`](../sources/prs/flashinfer/PR-3155.md) | fix(gdn): use physical SM count for SM100 persistent prefill kernel |
| `pr-flashinfer-3203` | upstream-code | [`sources/prs/flashinfer/PR-3203.md`](../sources/prs/flashinfer/PR-3203.md) | Include TinyGEMM into BF16 autotuner |
| `pr-flashinfer-3216` | upstream-code | [`sources/prs/flashinfer/PR-3216.md`](../sources/prs/flashinfer/PR-3216.md) | fix(cute_dsl/moe): make autotuner bucket configuration adapt to runtime input |
| `pr-flashinfer-3227` | upstream-code | [`sources/prs/flashinfer/PR-3227.md`](../sources/prs/flashinfer/PR-3227.md) | [Bugfix] Fix fused MoE autotuning correctness issues by filtering clusterDimZ |
| `pr-flashinfer-3235` | upstream-code | [`sources/prs/flashinfer/PR-3235.md`](../sources/prs/flashinfer/PR-3235.md) | Support Kimi K2.5 H64 CuTe DSL MLA decode |
| `pr-flashinfer-3252` | upstream-code | [`sources/prs/flashinfer/PR-3252.md`](../sources/prs/flashinfer/PR-3252.md) | fix(cute_dsl/moe): unbias autotuner profiling for tile_size enumeration |
| `pr-flashinfer-3276` | upstream-code | [`sources/prs/flashinfer/PR-3276.md`](../sources/prs/flashinfer/PR-3276.md) | fix(fmha_v2): fix FP8 V-scratch pipeline and varlen scheduler on SM90 |
| `pr-quack-31` | upstream-code | [`sources/prs/quack/PR-31.md`](../sources/prs/quack/PR-31.md) | Add missing default value for `is_scheduler_warp` |
| `pr-quack-79` | upstream-code | [`sources/prs/quack/PR-79.md`](../sources/prs/quack/PR-79.md) | Fix Triangular Scheduler |
| `pr-quack-81` | upstream-code | [`sources/prs/quack/PR-81.md`](../sources/prs/quack/PR-81.md) | [SM100] fix CLC persistence for varlen-M tile scheduler |
| `pr-sglang-17353` | upstream-code | [`sources/prs/sglang/PR-17353.md`](../sources/prs/sglang/PR-17353.md) | Move fa4 from sgl-kernel to jit kernel |
| `pr-sglang-18639` | upstream-code | [`sources/prs/sglang/PR-18639.md`](../sources/prs/sglang/PR-18639.md) | [sglang-miles] True on-policy training support for FSDP2 |
| `pr-sglang-21104` | upstream-code | [`sources/prs/sglang/PR-21104.md`](../sources/prs/sglang/PR-21104.md) | perf: precompute FA3 scheduler_metadata to eliminate per-layer prepare_varlen_num_blocks |
| `pr-sglang-23965` | upstream-code | [`sources/prs/sglang/PR-23965.md`](../sources/prs/sglang/PR-23965.md) | Enable PDL for various kernels in DSV32/GLM5 |
| `pr-sglang-24197` | upstream-code | [`sources/prs/sglang/PR-24197.md`](../sources/prs/sglang/PR-24197.md) | Refactor device timer, clean up metrics collector, and add fwd occupancy metric |
| `pr-sglang-24411` | upstream-code | [`sources/prs/sglang/PR-24411.md`](../sources/prs/sglang/PR-24411.md) | [diffusion] Fuse LTX2 split rotary embedding |
| `pr-sglang-24562` | upstream-code | [`sources/prs/sglang/PR-24562.md`](../sources/prs/sglang/PR-24562.md) | Fix performance regression on Deepseek V3 on `moe-runner-backend=triton` on SM90 |
| `pr-sglang-5390` | upstream-code | [`sources/prs/sglang/PR-5390.md`](../sources/prs/sglang/PR-5390.md) | Add Cutlass MLA attention backend |
| `pr-sglang-6929` | upstream-code | [`sources/prs/sglang/PR-6929.md`](../sources/prs/sglang/PR-6929.md) | [perf][sgl-kernel] extend cutlass_mla_decode to support num_head < 128 |
| `pr-tensorrt-llm-10042` | upstream-code | [`sources/prs/tensorrt-llm/PR-10042.md`](../sources/prs/tensorrt-llm/PR-10042.md) | [None][perf] Add more optimization options for MOE CuteDSL finalized kernel |
| `pr-tensorrt-llm-10043` | upstream-code | [`sources/prs/tensorrt-llm/PR-10043.md`](../sources/prs/tensorrt-llm/PR-10043.md) | [TRTLLM-9992][perf] Enable PDL for CuteDSL kernels and overlap MoeOutputMemset |
| `pr-tensorrt-llm-10190` | upstream-code | [`sources/prs/tensorrt-llm/PR-10190.md`](../sources/prs/tensorrt-llm/PR-10190.md) | [None][feat] sm100 weight-only kernel |
| `pr-tensorrt-llm-10201` | upstream-code | [`sources/prs/tensorrt-llm/PR-10201.md`](../sources/prs/tensorrt-llm/PR-10201.md) | [TRTLLM-9831][perf] Enable 2CTA with autotune for CuteDSL MoE and Grouped GEMM optimizations |
| `pr-tensorrt-llm-10339` | upstream-code | [`sources/prs/tensorrt-llm/PR-10339.md`](../sources/prs/tensorrt-llm/PR-10339.md) | [TRTLLM-9661][chore] Further reduce tuning time for cuteDSL nvFP4 dense gemm. |
| `pr-tensorrt-llm-11652` | upstream-code | [`sources/prs/tensorrt-llm/PR-11652.md`](../sources/prs/tensorrt-llm/PR-11652.md) | [None][feat] NVFP4 TRTLLM-Gen MoE for AutoDeploy (Nemotron Super) |
| `pr-tensorrt-llm-11900` | upstream-code | [`sources/prs/tensorrt-llm/PR-11900.md`](../sources/prs/tensorrt-llm/PR-11900.md) | [TRTLLM-10407][feat] Integrate CuTE DSL top-k kernel for Blackwell |
| `pr-tensorrt-llm-11990` | upstream-code | [`sources/prs/tensorrt-llm/PR-11990.md`](../sources/prs/tensorrt-llm/PR-11990.md) | [None][feat] GLM 5 support and DSA MTP fixes |
| `pr-tensorrt-llm-11993` | upstream-code | [`sources/prs/tensorrt-llm/PR-11993.md`](../sources/prs/tensorrt-llm/PR-11993.md) | [#11694][feat] AutoDeploy: Improve the piecewise CG memory usage |
| `pr-tensorrt-llm-12046` | upstream-code | [`sources/prs/tensorrt-llm/PR-12046.md`](../sources/prs/tensorrt-llm/PR-12046.md) | [https://nvbugs/5955188][fix] Fix harmony parsers and WAR routing PDL for agentic coding use cases |
| `pr-tensorrt-llm-12074` | upstream-code | [`sources/prs/tensorrt-llm/PR-12074.md`](../sources/prs/tensorrt-llm/PR-12074.md) | [TRTLLM-11289][feat] Integrate CuteDSL's bf16 dense GEMMs |
| `pr-tensorrt-llm-12079` | upstream-code | [`sources/prs/tensorrt-llm/PR-12079.md`](../sources/prs/tensorrt-llm/PR-12079.md) | [None][feat] CuteDSL MOE: Add raster along M/N support for blockscaled contiguous backbone kernel |
| `pr-tensorrt-llm-12236` | upstream-code | [`sources/prs/tensorrt-llm/PR-12236.md`](../sources/prs/tensorrt-llm/PR-12236.md) | [TRTLLM-10407][perf] Enable CuteDSL indexer_top_k in model |
| `pr-tensorrt-llm-12385` | upstream-code | [`sources/prs/tensorrt-llm/PR-12385.md`](../sources/prs/tensorrt-llm/PR-12385.md) | [None][feat] Temporally-Correlated Heuristic-guided Indexer TopK for Sparse Attention |
| `pr-tensorrt-llm-12503` | upstream-code | [`sources/prs/tensorrt-llm/PR-12503.md`](../sources/prs/tensorrt-llm/PR-12503.md) | [https://nvbugs/5983390][perf] Split MLA DSA custom op for piecewise CUDA graph capture |
| `pr-tensorrt-llm-12506` | upstream-code | [`sources/prs/tensorrt-llm/PR-12506.md`](../sources/prs/tensorrt-llm/PR-12506.md) | [None][feat] Add PDL support to CuTE DSL top-k kernels |
| `pr-tensorrt-llm-12612` | upstream-code | [`sources/prs/tensorrt-llm/PR-12612.md`](../sources/prs/tensorrt-llm/PR-12612.md) | [None][feat] Trtllm-gen FMHA JIT support |
| `pr-tensorrt-llm-12738` | upstream-code | [`sources/prs/tensorrt-llm/PR-12738.md`](../sources/prs/tensorrt-llm/PR-12738.md) | [None][feat] Add bf16 trtllm-gen moe support through flashinfer. |
| `pr-tensorrt-llm-13169` | upstream-code | [`sources/prs/tensorrt-llm/PR-13169.md`](../sources/prs/tensorrt-llm/PR-13169.md) | [https://nvbugs/5945047][fix] Fix cluster launch enablement for SM120 GPUs in allReduce fusion |
| `pr-tensorrt-llm-13219` | upstream-code | [`sources/prs/tensorrt-llm/PR-13219.md`](../sources/prs/tensorrt-llm/PR-13219.md) | [TRTLLM-34871][feat] Add cute dsl FP8 paged MQA logits decode kernel |
| `pr-tensorrt-llm-13340` | upstream-code | [`sources/prs/tensorrt-llm/PR-13340.md`](../sources/prs/tensorrt-llm/PR-13340.md) | [None][feat] Integrate FP4 indexer for DSA on Blackwell |
| `pr-tensorrt-llm-13477` | upstream-code | [`sources/prs/tensorrt-llm/PR-13477.md`](../sources/prs/tensorrt-llm/PR-13477.md) | [None][perf] Scheme X L2-aware dispatcher and PDL launchers for sparse-attention GVR Top-K |
| `pr-tensorrt-llm-13570` | upstream-code | [`sources/prs/tensorrt-llm/PR-13570.md`](../sources/prs/tensorrt-llm/PR-13570.md) | [TRTLLM-12128][feat] enable SageAttention for Wan/FLUX (new commits) |
| `pr-tensorrt-llm-13658` | upstream-code | [`sources/prs/tensorrt-llm/PR-13658.md`](../sources/prs/tensorrt-llm/PR-13658.md) | [None][test] add Nemotron Ultra V3 AutoDeploy accuracy test |
| `pr-tensorrt-llm-13802` | upstream-code | [`sources/prs/tensorrt-llm/PR-13802.md`](../sources/prs/tensorrt-llm/PR-13802.md) | [None][fix] Use compressed lengths for DeepSeek-V4 indexer |
| `pr-tensorrt-llm-13873` | upstream-code | [`sources/prs/tensorrt-llm/PR-13873.md`](../sources/prs/tensorrt-llm/PR-13873.md) | [TRTLLM-12503][feat] Parallel VAE independent scaling and fix arg passing |
| `pr-tensorrt-llm-13908` | upstream-code | [`sources/prs/tensorrt-llm/PR-13908.md`](../sources/prs/tensorrt-llm/PR-13908.md) | [None][refactor] MoEScheduler split + MegaMoE EPLB / multi-chunk / CI integration |
| `pr-tensorrt-llm-13997` | upstream-code | [`sources/prs/tensorrt-llm/PR-13997.md`](../sources/prs/tensorrt-llm/PR-13997.md) | [None][feat] enable TRTLLM-Gen internal routing |
| `pr-tensorrt-llm-9087` | upstream-code | [`sources/prs/tensorrt-llm/PR-9087.md`](../sources/prs/tensorrt-llm/PR-9087.md) | [None][fix] support topk autotuner input for expert slot per group larger than 32 |
| `pr-tensorrt-llm-9486` | upstream-code | [`sources/prs/tensorrt-llm/PR-9486.md`](../sources/prs/tensorrt-llm/PR-9486.md) | [TRTLLM-8958][feat] and [TRTLLM-8960]: create ConfigurableMoE and support TRTLLMGenFusedMoE as backend |
| `pr-tilelang-1584` | upstream-code | [`sources/prs/tilelang/PR-1584.md`](../sources/prs/tilelang/PR-1584.md) | [CI] Add CUDA-aware pytest scheduler + auto workers |
| `pr-tilelang-1658` | upstream-code | [`sources/prs/tilelang/PR-1658.md`](../sources/prs/tilelang/PR-1658.md) | [Feat] profiler support cudagraph backend |
| `pr-tilelang-1667` | upstream-code | [`sources/prs/tilelang/PR-1667.md`](../sources/prs/tilelang/PR-1667.md) | [Feature] Support `cp.reduce.async.bulk.tensor` |
| `pr-tilelang-1717` | upstream-code | [`sources/prs/tilelang/PR-1717.md`](../sources/prs/tilelang/PR-1717.md) | [Enhancement] Add explicit global memory load/store intrinsics (ldg/stg 32/64/128) |
| `pr-tilelang-1874` | upstream-code | [`sources/prs/tilelang/PR-1874.md`](../sources/prs/tilelang/PR-1874.md) | [Feature] Support cluster launch, query, synchronization and barrier operations |
| `pr-tilelang-1972` | upstream-code | [`sources/prs/tilelang/PR-1972.md`](../sources/prs/tilelang/PR-1972.md) | [Bugfix] Fix CuTeDSL autotune cache invalid ELF header (#1967) |
| `pr-tilelang-2024` | upstream-code | [`sources/prs/tilelang/PR-2024.md`](../sources/prs/tilelang/PR-2024.md) | Re-enable deprecated `TL_DISABLE_TMA_LOWER` pass config for TMA store |
| `pr-tilelang-2153` | upstream-code | [`sources/prs/tilelang/PR-2153.md`](../sources/prs/tilelang/PR-2153.md) | [codex] Split GEMM implementations by backend |
| `pr-vllm-13798` | upstream-code | [`sources/prs/vllm/PR-13798.md`](../sources/prs/vllm/PR-13798.md) | add cutlass support for blackwell fp8 gemm |
| `pr-vllm-19566` | upstream-code | [`sources/prs/vllm/PR-19566.md`](../sources/prs/vllm/PR-19566.md) | [Perf] Further tunings for SM100 FP8 CUTLASS kernel |
| `pr-vllm-20769` | upstream-code | [`sources/prs/vllm/PR-20769.md`](../sources/prs/vllm/PR-20769.md) | SM100 Cutlass MLA decode with unrestricted num_heads (< 128) for DeepSeek TP |
| `pr-vllm-34260` | upstream-code | [`sources/prs/vllm/PR-34260.md`](../sources/prs/vllm/PR-34260.md) | [Model Bash]: Improve FP8 Oracle for Config Specific Kernel Selection |
| `pr-vllm-39917` | upstream-code | [`sources/prs/vllm/PR-39917.md`](../sources/prs/vllm/PR-39917.md) | [Core] Replace routing replay with device cache and async D2H pipeline |
| `pr-vllm-40850` | upstream-code | [`sources/prs/vllm/PR-40850.md`](../sources/prs/vllm/PR-40850.md) | [Kernel][Helion] Optimize Helion config parsing latency |
| `pr-vllm-41189` | upstream-code | [`sources/prs/vllm/PR-41189.md`](../sources/prs/vllm/PR-41189.md) | [Bugfix] Fix persistent_topk cooperative deadlock at TopK=1024 |
| `pr-vllm-41665` | upstream-code | [`sources/prs/vllm/PR-41665.md`](../sources/prs/vllm/PR-41665.md) | [Bugfix] Fix condition to clear persistent topk so that it can be captured regardless |
| `pr-vllm-41745` | upstream-code | [`sources/prs/vllm/PR-41745.md`](../sources/prs/vllm/PR-41745.md) | [Spec Decode] Add Gemma4 MTP speculative decoding support |

<a id="tma-multicast"></a>
## tma-multicast

3 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `blog-modular-blackwell` | community-note | [`sources/blogs/modular-blackwell-matmul.md`](../sources/blogs/modular-blackwell-matmul.md) | Modular: Matrix Multiplication on Blackwell |
| `pr-cutlass-2472` | upstream-code | [`sources/prs/cutlass/PR-2472.md`](../sources/prs/cutlass/PR-2472.md) | Add Blackwell MLA forward (shape: d=192, dv=128) implementation |
| `pr-flashinfer-1695` | upstream-code | [`sources/prs/flashinfer/PR-1695.md`](../sources/prs/flashinfer/PR-1695.md) | [cute_dsl] add gemm + all reduce (two_shot)  |

<a id="vectorized-loads"></a>
## vectorized-loads

29 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `blog-amandeep-nvfp4` | community-note | [`sources/blogs/amandeep-nvfp4-attempts.md`](../sources/blogs/amandeep-nvfp4-attempts.md) | Twelve Attempts at NVFP4 Batched GEMV |
| `blog-yue-nvfp4` | community-note | [`sources/blogs/yue-nvfp4-hackathon.md`](../sources/blogs/yue-nvfp4-hackathon.md) | Blackwell NVFP4 Kernel Hackathon Journey |
| `contest-gpumode-p1` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-1-gemv.md`](../sources/contests/gpu-mode-nvfp4/problem-1-gemv.md) | GPU Mode NVFP4 Hackathon - Problem 1: Batched GEMV |
| `pr-cccl-cub-3517` | upstream-code | [`sources/prs/cccl-cub/PR-3517.md`](../sources/prs/cccl-cub/PR-3517.md) | Fix the vectorized loading of BlockLoad |
| `pr-cccl-cub-6921` | upstream-code | [`sources/prs/cccl-cub/PR-6921.md`](../sources/prs/cccl-cub/PR-6921.md) | Use vectorized transform kernel for sizeof(T) < 4 workloads of arity >1 on Hopper |
| `pr-cccl-cub-7571` | upstream-code | [`sources/prs/cccl-cub/PR-7571.md`](../sources/prs/cccl-cub/PR-7571.md) | Vectorize reduction also for trivially relocatable types |
| `pr-cccl-cub-7823` | upstream-code | [`sources/prs/cccl-cub/PR-7823.md`](../sources/prs/cccl-cub/PR-7823.md) | Optimized Device-to-Device Tensor Copy (`cudax`) |
| `pr-cccl-cub-8351` | upstream-code | [`sources/prs/cccl-cub/PR-8351.md`](../sources/prs/cccl-cub/PR-8351.md) | Fix and improve vector type traits |
| `pr-cccl-cub-8423` | upstream-code | [`sources/prs/cccl-cub/PR-8423.md`](../sources/prs/cccl-cub/PR-8423.md) | Vectorize mbarrier initialization in warpspeed scan |
| `pr-flash-attention-2236` | upstream-code | [`sources/prs/flash-attention/PR-2236.md`](../sources/prs/flash-attention/PR-2236.md) | [Cute,Flex,Fwd] Allow vectorized score_mod definitions |
| `pr-flashinfer-2962` | upstream-code | [`sources/prs/flashinfer/PR-2962.md`](../sources/prs/flashinfer/PR-2962.md) | Improved `simple` mamba SSU kernel  |
| `pr-flashinfer-3027` | upstream-code | [`sources/prs/flashinfer/PR-3027.md`](../sources/prs/flashinfer/PR-3027.md) | [feat] Trtllm-gen Per-token Nvfp4 MoE |
| `pr-pytorch-150705` | upstream-code | [`sources/prs/pytorch/PR-150705.md`](../sources/prs/pytorch/PR-150705.md) | [CUDA] Only use vec128 if CUDA version is newer than 12.8 |
| `pr-sglang-23938` | upstream-code | [`sources/prs/sglang/PR-23938.md`](../sources/prs/sglang/PR-23938.md) | Optimize large GroupNorm SiLU apply |
| `pr-tensorrt-llm-9175` | upstream-code | [`sources/prs/tensorrt-llm/PR-9175.md`](../sources/prs/tensorrt-llm/PR-9175.md) | [None][feat] TRT-LLM Gen MoE optimize DeepSeek Fp8 activation kernel |
| `pr-tilelang-1582` | upstream-code | [`sources/prs/tilelang/PR-1582.md`](../sources/prs/tilelang/PR-1582.md) | [Feature] Add more curand operations & support vectorization |
| `pr-tilelang-1644` | upstream-code | [`sources/prs/tilelang/PR-1644.md`](../sources/prs/tilelang/PR-1644.md) | [Feature] Introduce DecoupleTypeCast pass for mixed-precision vectorization |
| `pr-tilelang-1676` | upstream-code | [`sources/prs/tilelang/PR-1676.md`](../sources/prs/tilelang/PR-1676.md) | [Feature] Atomic Reduction Operations and Vectorization Enhancement |
| `pr-tilelang-1677` | upstream-code | [`sources/prs/tilelang/PR-1677.md`](../sources/prs/tilelang/PR-1677.md) | [Refactor] Move AtomicAdd Vectorization to VectorizeLoop Pass |
| `pr-tilelang-1717` | upstream-code | [`sources/prs/tilelang/PR-1717.md`](../sources/prs/tilelang/PR-1717.md) | [Enhancement] Add explicit global memory load/store intrinsics (ldg/stg 32/64/128) |
| `pr-tilelang-1722` | upstream-code | [`sources/prs/tilelang/PR-1722.md`](../sources/prs/tilelang/PR-1722.md) | [Refactor] re-implement vector subtype and its access method |
| `pr-tilelang-1726` | upstream-code | [`sources/prs/tilelang/PR-1726.md`](../sources/prs/tilelang/PR-1726.md) | [Bugfix] Fix incorrect alignment of vectorized subtype |
| `pr-tilelang-1741` | upstream-code | [`sources/prs/tilelang/PR-1741.md`](../sources/prs/tilelang/PR-1741.md) | [BugFix] Fix FP4 related vectorized cast |
| `pr-tilelang-1839` | upstream-code | [`sources/prs/tilelang/PR-1839.md`](../sources/prs/tilelang/PR-1839.md) | [CUDA][Feature] Add packed FP32x2 math intrinsics and auto vectorized support |
| `pr-tilelang-1901` | upstream-code | [`sources/prs/tilelang/PR-1901.md`](../sources/prs/tilelang/PR-1901.md) | [BugFix] Add vector type definitions to common.h for CPU codegen |
| `pr-tilelang-2004` | upstream-code | [`sources/prs/tilelang/PR-2004.md`](../sources/prs/tilelang/PR-2004.md) | fix: fix copy+cast vectorize loop to use wider vector load/store instrcution |
| `pr-tilelang-2015` | upstream-code | [`sources/prs/tilelang/PR-2015.md`](../sources/prs/tilelang/PR-2015.md) | [BugFix] Enhance CUDA vectorization for binary operations |
| `pr-tilelang-2063` | upstream-code | [`sources/prs/tilelang/PR-2063.md`](../sources/prs/tilelang/PR-2063.md) | [CUDA] Support int4 `T.gemm` |
| `pr-tilelang-2117` | upstream-code | [`sources/prs/tilelang/PR-2117.md`](../sources/prs/tilelang/PR-2117.md) | [Enhancement][CUDA][SM100] Report unsupported FP6 vector types earlier |

<a id="warp-specialization"></a>
## warp-specialization

122 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `blog-modular-blackwell` | community-note | [`sources/blogs/modular-blackwell-matmul.md`](../sources/blogs/modular-blackwell-matmul.md) | Modular: Matrix Multiplication on Blackwell |
| `contest-flashinfer-track-a` | contest-report | [`sources/contests/flashinfer-mlsys26/track-a-fused-moe.md`](../sources/contests/flashinfer-mlsys26/track-a-fused-moe.md) | FlashInfer MLSys 2026 - Track A: Fused MoE FP8 |
| `contest-flashinfer-track-b` | contest-report | [`sources/contests/flashinfer-mlsys26/track-b-sparse-attention.md`](../sources/contests/flashinfer-mlsys26/track-b-sparse-attention.md) | FlashInfer MLSys 2026 - Track B: DeepSeek V3.2 Sparse Attention |
| `contest-flashinfer-track-c` | contest-report | [`sources/contests/flashinfer-mlsys26/track-c-gated-delta-net.md`](../sources/contests/flashinfer-mlsys26/track-c-gated-delta-net.md) | FlashInfer MLSys 2026 - Track C: Gated Delta Net |
| `contest-gpumode-p2` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-2-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-2-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 2: NVFP4 GEMM |
| `contest-gpumode-p3` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-3-gated-dual-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-3-gated-dual-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 3: Gated Dual GEMM |
| `contest-gpumode-p4` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 4: Grouped GEMM |
| `pr-cccl-cub-1973` | upstream-code | [`sources/prs/cccl-cub/PR-1973.md`](../sources/prs/cccl-cub/PR-1973.md) | Experimental Python cooperative algorithms |
| `pr-cccl-cub-3218` | upstream-code | [`sources/prs/cccl-cub/PR-3218.md`](../sources/prs/cccl-cub/PR-3218.md) | cuda.parallel: Support structured types as algorithm inputs |
| `pr-cccl-cub-3517` | upstream-code | [`sources/prs/cccl-cub/PR-3517.md`](../sources/prs/cccl-cub/PR-3517.md) | Fix the vectorized loading of BlockLoad |
| `pr-cccl-cub-4000` | upstream-code | [`sources/prs/cccl-cub/PR-4000.md`](../sources/prs/cccl-cub/PR-4000.md) | Drop CUB_MIN|MAX in warp_scan_shfl |
| `pr-cccl-cub-4716` | upstream-code | [`sources/prs/cccl-cub/PR-4716.md`](../sources/prs/cccl-cub/PR-4716.md) | Split Optimize Warp Reduce PR - CUB part |
| `pr-cccl-cub-4961` | upstream-code | [`sources/prs/cccl-cub/PR-4961.md`](../sources/prs/cccl-cub/PR-4961.md) | Add nondeterministic reduce that uses atomics |
| `pr-cccl-cub-5314` | upstream-code | [`sources/prs/cccl-cub/PR-5314.md`](../sources/prs/cccl-cub/PR-5314.md) | CUB - Add internal integer utils and tests (Split `WarpReduce` PR) |
| `pr-cccl-cub-5408` | upstream-code | [`sources/prs/cccl-cub/PR-5408.md`](../sources/prs/cccl-cub/PR-5408.md) | Combine `block_reduce_warp_reduction_nondeterministic.cuh` specialization with original deterministic one  |
| `pr-cccl-cub-6069` | upstream-code | [`sources/prs/cccl-cub/PR-6069.md`](../sources/prs/cccl-cub/PR-6069.md) | Add dynamic CUB dispatch for segmented_sort |
| `pr-cccl-cub-6202` | upstream-code | [`sources/prs/cccl-cub/PR-6202.md`](../sources/prs/cccl-cub/PR-6202.md) | [Backport 3.1]: [CUB] Replace several direct uses of `__clz` (#6099) |
| `pr-cccl-cub-6484` | upstream-code | [`sources/prs/cccl-cub/PR-6484.md`](../sources/prs/cccl-cub/PR-6484.md) | Avoid potentially ambiguous overload in `warp_excahnge_shfl` |
| `pr-cccl-cub-6811` | upstream-code | [`sources/prs/cccl-cub/PR-6811.md`](../sources/prs/cccl-cub/PR-6811.md) | Integrate decoupled lookahead warpspeed scan |
| `pr-cccl-cub-6814` | upstream-code | [`sources/prs/cccl-cub/PR-6814.md`](../sources/prs/cccl-cub/PR-6814.md) | Improve our `WarpReduce` implementation |
| `pr-cccl-cub-6819` | upstream-code | [`sources/prs/cccl-cub/PR-6819.md`](../sources/prs/cccl-cub/PR-6819.md) | Use integer promotion for `warp_reduce` |
| `pr-cccl-cub-6846` | upstream-code | [`sources/prs/cccl-cub/PR-6846.md`](../sources/prs/cccl-cub/PR-6846.md) | [cuda.coop]: add device-side `coop.warp.sum` benchmark with pynvbench |
| `pr-cccl-cub-7692` | upstream-code | [`sources/prs/cccl-cub/PR-7692.md`](../sources/prs/cccl-cub/PR-7692.md) | Implement `WarpReduceBatched` |
| `pr-cccl-cub-7718` | upstream-code | [`sources/prs/cccl-cub/PR-7718.md`](../sources/prs/cccl-cub/PR-7718.md) | Optimize non fixed size segmented reduce for small segments using max_segment_size |
| `pr-cccl-cub-7861` | upstream-code | [`sources/prs/cccl-cub/PR-7861.md`](../sources/prs/cccl-cub/PR-7861.md) | Improve warpspeed scan tuning for sm120 |
| `pr-cccl-cub-7874` | upstream-code | [`sources/prs/cccl-cub/PR-7874.md`](../sources/prs/cccl-cub/PR-7874.md) | Implement the new tuning API for `DispatchSegmentedSort` |
| `pr-cccl-cub-7892` | upstream-code | [`sources/prs/cccl-cub/PR-7892.md`](../sources/prs/cccl-cub/PR-7892.md) | Reduce warpspeed scan to 256 threads/block on NVHPC |
| `pr-cccl-cub-8008` | upstream-code | [`sources/prs/cccl-cub/PR-8008.md`](../sources/prs/cccl-cub/PR-8008.md) | Make warpspeed scan tunable |
| `pr-cccl-cub-8125` | upstream-code | [`sources/prs/cccl-cub/PR-8125.md`](../sources/prs/cccl-cub/PR-8125.md) | Optimized Device-to-Device Tensor Copy (cudax) - Transpose Case |
| `pr-cccl-cub-8145` | upstream-code | [`sources/prs/cccl-cub/PR-8145.md`](../sources/prs/cccl-cub/PR-8145.md) | Refactor warpspeed scan tuning |
| `pr-cccl-cub-8158` | upstream-code | [`sources/prs/cccl-cub/PR-8158.md`](../sources/prs/cccl-cub/PR-8158.md) | Let scan tuning policy choose warpspeed or not |
| `pr-cccl-cub-8169` | upstream-code | [`sources/prs/cccl-cub/PR-8169.md`](../sources/prs/cccl-cub/PR-8169.md) | Fix UB in `cuda::device::warp_match_all` |
| `pr-cccl-cub-8184` | upstream-code | [`sources/prs/cccl-cub/PR-8184.md`](../sources/prs/cccl-cub/PR-8184.md) | Avoid passing uninitialized values to scan_op |
| `pr-cccl-cub-8210` | upstream-code | [`sources/prs/cccl-cub/PR-8210.md`](../sources/prs/cccl-cub/PR-8210.md) | Add warp shuffle constraints |
| `pr-cccl-cub-8222` | upstream-code | [`sources/prs/cccl-cub/PR-8222.md`](../sources/prs/cccl-cub/PR-8222.md) | Small warpspeed scan improvements |
| `pr-cccl-cub-8236` | upstream-code | [`sources/prs/cccl-cub/PR-8236.md`](../sources/prs/cccl-cub/PR-8236.md) | Prevent ADL from finding user-namespace functions in `kernel_scan_warp` |
| `pr-cccl-cub-8254` | upstream-code | [`sources/prs/cccl-cub/PR-8254.md`](../sources/prs/cccl-cub/PR-8254.md) | Recover `warp_shuffle` original behavior (revert #8210) |
| `pr-cccl-cub-8270` | upstream-code | [`sources/prs/cccl-cub/PR-8270.md`](../sources/prs/cccl-cub/PR-8270.md) | `cuda::is_bitwise_comparable` |
| `pr-cccl-cub-8332` | upstream-code | [`sources/prs/cccl-cub/PR-8332.md`](../sources/prs/cccl-cub/PR-8332.md) | simplify dispatch segmented reduce to use latest dispatch and new tunings API |
| `pr-cccl-cub-8342` | upstream-code | [`sources/prs/cccl-cub/PR-8342.md`](../sources/prs/cccl-cub/PR-8342.md) | Make warpspeed scan tunable |
| `pr-cccl-cub-8352` | upstream-code | [`sources/prs/cccl-cub/PR-8352.md`](../sources/prs/cccl-cub/PR-8352.md) | Apply some random warpspeed tunings |
| `pr-cccl-cub-8394` | upstream-code | [`sources/prs/cccl-cub/PR-8394.md`](../sources/prs/cccl-cub/PR-8394.md) | Refactor and improve `extents_as` queries |
| `pr-cccl-cub-8395` | upstream-code | [`sources/prs/cccl-cub/PR-8395.md`](../sources/prs/cccl-cub/PR-8395.md) | [CUB] Replace `Shuffle(Up|Down|Index)` with cuda::device::warp_shuffle - RadixSort only |
| `pr-cccl-cub-8407` | upstream-code | [`sources/prs/cccl-cub/PR-8407.md`](../sources/prs/cccl-cub/PR-8407.md) | Workaround nvc++ crash in warpspeed scan |
| `pr-cccl-cub-8423` | upstream-code | [`sources/prs/cccl-cub/PR-8423.md`](../sources/prs/cccl-cub/PR-8423.md) | Vectorize mbarrier initialization in warpspeed scan |
| `pr-cccl-cub-8440` | upstream-code | [`sources/prs/cccl-cub/PR-8440.md`](../sources/prs/cccl-cub/PR-8440.md) | Swap the `load_modifier` and `store_algorithm` in `sub_warp_merge_sort_policy` |
| `pr-cccl-cub-8441` | upstream-code | [`sources/prs/cccl-cub/PR-8441.md`](../sources/prs/cccl-cub/PR-8441.md) | Rename `agent_warp_reduce_policy` to `warp_reduce_policy` |
| `pr-cccl-cub-8487` | upstream-code | [`sources/prs/cccl-cub/PR-8487.md`](../sources/prs/cccl-cub/PR-8487.md) | Enable hierarchy query tests for nvrtc |
| `pr-cccl-cub-8495` | upstream-code | [`sources/prs/cccl-cub/PR-8495.md`](../sources/prs/cccl-cub/PR-8495.md) | Replace `detail::scan::dispatch` by CUB's public API |
| `pr-cccl-cub-8522` | upstream-code | [`sources/prs/cccl-cub/PR-8522.md`](../sources/prs/cccl-cub/PR-8522.md) | [CUB] Delegate large segments to Multi-CTA Implementation in `DeviceSegmentedTopK` |
| `pr-cccl-cub-8523` | upstream-code | [`sources/prs/cccl-cub/PR-8523.md`](../sources/prs/cccl-cub/PR-8523.md) | [cudax] Implement public groups synchronizers |
| `pr-cccl-cub-8527` | upstream-code | [`sources/prs/cccl-cub/PR-8527.md`](../sources/prs/cccl-cub/PR-8527.md) | [cudax] Make groups constructible from other groups |
| `pr-cccl-cub-8529` | upstream-code | [`sources/prs/cccl-cub/PR-8529.md`](../sources/prs/cccl-cub/PR-8529.md) | Prefer the term warpspeed over lookahead |
| `pr-cccl-cub-8611` | upstream-code | [`sources/prs/cccl-cub/PR-8611.md`](../sources/prs/cccl-cub/PR-8611.md) | Add B200 tuning for warpspeed_scan  |
| `pr-cccl-cub-8639` | upstream-code | [`sources/prs/cccl-cub/PR-8639.md`](../sources/prs/cccl-cub/PR-8639.md) | Segmented scan multisegment part 1 |
| `pr-cccl-cub-8657` | upstream-code | [`sources/prs/cccl-cub/PR-8657.md`](../sources/prs/cccl-cub/PR-8657.md) | Add a killswitch for warpspeed scan |
| `pr-cccl-cub-8689` | upstream-code | [`sources/prs/cccl-cub/PR-8689.md`](../sources/prs/cccl-cub/PR-8689.md) | Revert I8 tunings for warpspeed scan |
| `pr-cccl-cub-8755` | upstream-code | [`sources/prs/cccl-cub/PR-8755.md`](../sources/prs/cccl-cub/PR-8755.md) | [cudax] Change the group mapping application logic |
| `pr-cccl-cub-8766` | upstream-code | [`sources/prs/cccl-cub/PR-8766.md`](../sources/prs/cccl-cub/PR-8766.md) | [cudax] Implement `composite_mapping` for groups |
| `pr-cccl-cub-8788` | upstream-code | [`sources/prs/cccl-cub/PR-8788.md`](../sources/prs/cccl-cub/PR-8788.md) | Rename cuda.coop backend to cuda.coop._experimental |
| `pr-cccl-cub-8836` | upstream-code | [`sources/prs/cccl-cub/PR-8836.md`](../sources/prs/cccl-cub/PR-8836.md) | Rename `block_threads` -> `threads_per_block` |
| `pr-cccl-cub-8839` | upstream-code | [`sources/prs/cccl-cub/PR-8839.md`](../sources/prs/cccl-cub/PR-8839.md) | Fix Warpspeed scan shifted output store |
| `pr-cccl-cub-8922` | upstream-code | [`sources/prs/cccl-cub/PR-8922.md`](../sources/prs/cccl-cub/PR-8922.md) | Disable warpspeed scan on sm120 with nvcc < 13.4 |
| `pr-cccl-cub-8967` | upstream-code | [`sources/prs/cccl-cub/PR-8967.md`](../sources/prs/cccl-cub/PR-8967.md) | Also disable warpspeed scan below NVRTC 13.4 |
| `pr-cutlass-1661` | upstream-code | [`sources/prs/cutlass/PR-1661.md`](../sources/prs/cutlass/PR-1661.md) | Skip void-C kernels in the profiler when beta is non zero |
| `pr-cutlass-1795` | upstream-code | [`sources/prs/cutlass/PR-1795.md`](../sources/prs/cutlass/PR-1795.md) | Support for TMA Epilogue for Group Gemm and add pingpong ptr array & Group Gemm |
| `pr-cutlass-1883` | upstream-code | [`sources/prs/cutlass/PR-1883.md`](../sources/prs/cutlass/PR-1883.md) | Improve sm90 mixed dtype kernel |
| `pr-cutlass-1932` | upstream-code | [`sources/prs/cutlass/PR-1932.md`](../sources/prs/cutlass/PR-1932.md) | Blockwise Scaling for FP8 |
| `pr-cutlass-2037` | upstream-code | [`sources/prs/cutlass/PR-2037.md`](../sources/prs/cutlass/PR-2037.md) | Groupwise scaling along M for FP8 gemm |
| `pr-cutlass-2095` | upstream-code | [`sources/prs/cutlass/PR-2095.md`](../sources/prs/cutlass/PR-2095.md) | Improvements for: Groupwise scaling along M for FP8 gemm |
| `pr-cutlass-2123` | upstream-code | [`sources/prs/cutlass/PR-2123.md`](../sources/prs/cutlass/PR-2123.md) | Hopper Grouped GEMM support for FP8 Accum |
| `pr-cutlass-2139` | upstream-code | [`sources/prs/cutlass/PR-2139.md`](../sources/prs/cutlass/PR-2139.md) | Blockwise and Groupwise GEMM for Blackwell and Improvements for Hopper |
| `pr-cutlass-2172` | upstream-code | [`sources/prs/cutlass/PR-2172.md`](../sources/prs/cutlass/PR-2172.md) | Fix SM90 beta=1 hang and stream-K launch errors |
| `pr-cutlass-2270` | upstream-code | [`sources/prs/cutlass/PR-2270.md`](../sources/prs/cutlass/PR-2270.md) | hopper-blockwise-generalization-optimization |
| `pr-cutlass-2466` | upstream-code | [`sources/prs/cutlass/PR-2466.md`](../sources/prs/cutlass/PR-2466.md) | Example 77 add blackwell fmha bwd for MLA shape |
| `pr-cutlass-2472` | upstream-code | [`sources/prs/cutlass/PR-2472.md`](../sources/prs/cutlass/PR-2472.md) | Add Blackwell MLA forward (shape: d=192, dv=128) implementation |
| `pr-cutlass-2746` | upstream-code | [`sources/prs/cutlass/PR-2746.md`](../sources/prs/cutlass/PR-2746.md) | Support for GEMM-K=0 for Blackwell Grouped GEMMs |
| `pr-cutlass-2790` | upstream-code | [`sources/prs/cutlass/PR-2790.md`](../sources/prs/cutlass/PR-2790.md) | Blockscaled Ragged Contiguous Grouped Gemm for MoEs |
| `pr-cutlass-3176` | upstream-code | [`sources/prs/cutlass/PR-3176.md`](../sources/prs/cutlass/PR-3176.md) | Small Tile N BlockScaled GEMM + Grouped GEMM on SM12x |
| `pr-flash-attention-1100` | upstream-code | [`sources/prs/flash-attention/PR-1100.md`](../sources/prs/flash-attention/PR-1100.md) | Fp8 kernel with "in-kernel" transpose of V in producer |
| `pr-flash-attention-1173` | upstream-code | [`sources/prs/flash-attention/PR-1173.md`](../sources/prs/flash-attention/PR-1173.md) | FA3 FP8 qkv descales + restore max offset for h128 causal + added sync for producer WG |
| `pr-flash-attention-1993` | upstream-code | [`sources/prs/flash-attention/PR-1993.md`](../sources/prs/flash-attention/PR-1993.md) | [Cute,Fwd,Sm100] Support `q_stage=1` for inference |
| `pr-flash-attention-1999` | upstream-code | [`sources/prs/flash-attention/PR-1999.md`](../sources/prs/flash-attention/PR-1999.md) | [Cute,Fwd,Sm100] Support paged attention |
| `pr-flash-attention-2014` | upstream-code | [`sources/prs/flash-attention/PR-2014.md`](../sources/prs/flash-attention/PR-2014.md) | [Cute,Sm100,Fwd] use correction warps for epi when not using TMA |
| `pr-flash-attention-2033` | upstream-code | [`sources/prs/flash-attention/PR-2033.md`](../sources/prs/flash-attention/PR-2033.md) | [Cute,Bwd,Sm100] enable deterministic mode for sm100 bwd and fix race conditions |
| `pr-flash-attention-2104` | upstream-code | [`sources/prs/flash-attention/PR-2104.md`](../sources/prs/flash-attention/PR-2104.md) | [Cute,Fwd,Sm100] distributed offset calculation for paged KV |
| `pr-flash-attention-2497` | upstream-code | [`sources/prs/flash-attention/PR-2497.md`](../sources/prs/flash-attention/PR-2497.md) | [FA4][hd256] Backward TMA bulk-store epilogue + LSE/dpsum coalesce |
| `pr-flashinfer-1294` | upstream-code | [`sources/prs/flashinfer/PR-1294.md`](../sources/prs/flashinfer/PR-1294.md) | Update cutlass fp4 moe kernels |
| `pr-flashinfer-1396` | upstream-code | [`sources/prs/flashinfer/PR-1396.md`](../sources/prs/flashinfer/PR-1396.md) | gpt-oss: Add MXFP8 x MXFP4 CUTLASS MOE for SM100 and BF16 x MXFP4 CUTLASS for SM90 + SwigluBias Activation |
| `pr-flashinfer-1681` | upstream-code | [`sources/prs/flashinfer/PR-1681.md`](../sources/prs/flashinfer/PR-1681.md) | perf: improve performance of cutlass fmha |
| `pr-flashinfer-1850` | upstream-code | [`sources/prs/flashinfer/PR-1850.md`](../sources/prs/flashinfer/PR-1850.md) | Add head_dim=64 for blackwell cutlass fmha implementation |
| `pr-flashinfer-1973` | upstream-code | [`sources/prs/flashinfer/PR-1973.md`](../sources/prs/flashinfer/PR-1973.md) | Feature: Add support for L40 FusedMoE in cutlass path |
| `pr-flashinfer-2020` | upstream-code | [`sources/prs/flashinfer/PR-2020.md`](../sources/prs/flashinfer/PR-2020.md) | update trtllm cutlass moe  |
| `pr-flashinfer-2387` | upstream-code | [`sources/prs/flashinfer/PR-2387.md`](../sources/prs/flashinfer/PR-2387.md) | A Blackwell-optimized version of selective_state_update (mamba) |
| `pr-flashinfer-2799` | upstream-code | [`sources/prs/flashinfer/PR-2799.md`](../sources/prs/flashinfer/PR-2799.md) | [fmha-v2] Support HND and NHD paged KV cache layouts with conditional stride handling |
| `pr-flashinfer-2841` | upstream-code | [`sources/prs/flashinfer/PR-2841.md`](../sources/prs/flashinfer/PR-2841.md) | [Perf] Add FMHAv2 to flashinfer_benchmark.py and eliminate unnecessary H2D |
| `pr-flashinfer-3027` | upstream-code | [`sources/prs/flashinfer/PR-3027.md`](../sources/prs/flashinfer/PR-3027.md) | [feat] Trtllm-gen Per-token Nvfp4 MoE |
| `pr-flashinfer-3084` | upstream-code | [`sources/prs/flashinfer/PR-3084.md`](../sources/prs/flashinfer/PR-3084.md) | perf: optimize MXFP4xBF16 & INT4xFP8 CUTLASS MoE backend for SM90 |
| `pr-flashinfer-3113` | upstream-code | [`sources/prs/flashinfer/PR-3113.md`](../sources/prs/flashinfer/PR-3113.md) | Fix: Extend b12x FP4 GEMM support to SM121 (GB10/DGX Spark) |
| `pr-flashinfer-3276` | upstream-code | [`sources/prs/flashinfer/PR-3276.md`](../sources/prs/flashinfer/PR-3276.md) | fix(fmha_v2): fix FP8 V-scratch pipeline and varlen scheduler on SM90 |
| `pr-quack-31` | upstream-code | [`sources/prs/quack/PR-31.md`](../sources/prs/quack/PR-31.md) | Add missing default value for `is_scheduler_warp` |
| `pr-quack-97` | upstream-code | [`sources/prs/quack/PR-97.md`](../sources/prs/quack/PR-97.md) | [BugFix] Fix `_is_warp_leader` in `TraceContext`  |
| `pr-sglang-15835` | upstream-code | [`sources/prs/sglang/PR-15835.md`](../sources/prs/sglang/PR-15835.md) | [Feature] JIT Fused QK norm + qk norm clean up |
| `pr-sglang-20673` | upstream-code | [`sources/prs/sglang/PR-20673.md`](../sources/prs/sglang/PR-20673.md) | [Feature][JIT Kernel] Fused TP QK norm For Minimax |
| `pr-sglang-5390` | upstream-code | [`sources/prs/sglang/PR-5390.md`](../sources/prs/sglang/PR-5390.md) | Add Cutlass MLA attention backend |
| `pr-tensorrt-llm-10190` | upstream-code | [`sources/prs/tensorrt-llm/PR-10190.md`](../sources/prs/tensorrt-llm/PR-10190.md) | [None][feat] sm100 weight-only kernel |
| `pr-thunderkittens-152` | upstream-code | [`sources/prs/thunderkittens/PR-152.md`](../sources/prs/thunderkittens/PR-152.md) | Educational Hopper Matmul level_07 Warp Specialization Fix |
| `pr-tilelang-1762` | upstream-code | [`sources/prs/tilelang/PR-1762.md`](../sources/prs/tilelang/PR-1762.md) | [Feature] Hierarchical reduction and warp reduction intrinsics support |
| `pr-tilelang-1840` | upstream-code | [`sources/prs/tilelang/PR-1840.md`](../sources/prs/tilelang/PR-1840.md) | [BugFix] Fix Hopper TMA lowering without warp specialization |
| `pr-tilelang-1858` | upstream-code | [`sources/prs/tilelang/PR-1858.md`](../sources/prs/tilelang/PR-1858.md) | [Feature] Add TIR builtins for warp-level vote and block-level predicate sync |
| `pr-tilelang-1882` | upstream-code | [`sources/prs/tilelang/PR-1882.md`](../sources/prs/tilelang/PR-1882.md) | [Feature] 2-SM support for TMA, TMEM and TCGEN5MMA on Blackwell |
| `pr-tilelang-1909` | upstream-code | [`sources/prs/tilelang/PR-1909.md`](../sources/prs/tilelang/PR-1909.md) | [Feature] Add Producer-Consumer Warp Specialization and T.tma_copy() API |
| `pr-tilelang-1946` | upstream-code | [`sources/prs/tilelang/PR-1946.md`](../sources/prs/tilelang/PR-1946.md) | [BugFix] Update usage of tma load in SM100 manual warp-specialized examples |
| `pr-tilelang-1953` | upstream-code | [`sources/prs/tilelang/PR-1953.md`](../sources/prs/tilelang/PR-1953.md) | [PIpeline] Enable software pipelining when warp specialization is unavailable |
| `pr-tilelang-1962` | upstream-code | [`sources/prs/tilelang/PR-1962.md`](../sources/prs/tilelang/PR-1962.md) | [Bugfix] Fix double buffer versioning when TMA is used without warp specialization |
| `pr-tilelang-1976` | upstream-code | [`sources/prs/tilelang/PR-1976.md`](../sources/prs/tilelang/PR-1976.md) | [Feature] Batched AllReduce for better T.reduce performance |
| `pr-tilelang-2039` | upstream-code | [`sources/prs/tilelang/PR-2039.md`](../sources/prs/tilelang/PR-2039.md) | [API] Default warp-lane mask to 0xFFFFFFFF for warp-sync builtins |
| `pr-tilelang-2166` | upstream-code | [`sources/prs/tilelang/PR-2166.md`](../sources/prs/tilelang/PR-2166.md) | [BugFix] Consider non-local store in external call and SIMT producer for warp specialize |
| `pr-triton-10056` | upstream-code | [`sources/prs/triton/PR-10056.md`](../sources/prs/triton/PR-10056.md) | [AMD][gfx1250] Support warp usage hints in TDM copy |
| `pr-triton-10217` | upstream-code | [`sources/prs/triton/PR-10217.md`](../sources/prs/triton/PR-10217.md) | [ConSan] Fix missing captureBytes argument in passToWarpSpecialize call |
| `pr-triton-9666` | upstream-code | [`sources/prs/triton/PR-9666.md`](../sources/prs/triton/PR-9666.md) | [AMD] Enable loop unrolling for Gluon warp-pipelined kernels |
| `pr-vllm-16032` | upstream-code | [`sources/prs/vllm/PR-16032.md`](../sources/prs/vllm/PR-16032.md) | [NVIDIA] Support Cutlass MLA for Blackwell GPUs |
