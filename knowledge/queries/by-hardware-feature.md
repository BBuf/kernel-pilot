# Hardware Feature Index

<a id="2sm-cooperative"></a>
## 2sm-cooperative

2 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `blog-modular-blackwell` | community-note | [`sources/blogs/modular-blackwell-matmul.md`](../sources/blogs/modular-blackwell-matmul.md) | Modular: Matrix Multiplication on Blackwell |
| `pr-cutlass-2492` | upstream-code | [`sources/prs/cutlass/PR-2492.md`](../sources/prs/cutlass/PR-2492.md) | fix: examples/cute/tutorial/blackwell/04_mma_tma_2sm_sm100.cu GridDim miscalculated |

<a id="blackwell"></a>
## blackwell

259 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-cccl-cub-3543` | upstream-code | [`sources/prs/cccl-cub/PR-3543.md`](../sources/prs/cccl-cub/PR-3543.md) | Tune cub::DeviceTransform for Blackwell |
| `pr-cccl-cub-3544` | upstream-code | [`sources/prs/cccl-cub/PR-3544.md`](../sources/prs/cccl-cub/PR-3544.md) | Bump CI to use CTK 12.8, add sm100 build. |
| `pr-cccl-cub-3559` | upstream-code | [`sources/prs/cccl-cub/PR-3559.md`](../sources/prs/cccl-cub/PR-3559.md) | Add b200 tunings for scan.exclusive.sum |
| `pr-cccl-cub-3565` | upstream-code | [`sources/prs/cccl-cub/PR-3565.md`](../sources/prs/cccl-cub/PR-3565.md) | Backport to 2.8: Tune cub::DeviceTransform for Blackwell (#3543) |
| `pr-cccl-cub-3568` | upstream-code | [`sources/prs/cccl-cub/PR-3568.md`](../sources/prs/cccl-cub/PR-3568.md) | PTX: Update generated files with Blackwell instructions  |
| `pr-cccl-cub-3611` | upstream-code | [`sources/prs/cccl-cub/PR-3611.md`](../sources/prs/cccl-cub/PR-3611.md) | Add b200 tunings for radix_sort.keys |
| `pr-cccl-cub-3624` | upstream-code | [`sources/prs/cccl-cub/PR-3624.md`](../sources/prs/cccl-cub/PR-3624.md) | Backport to 2.8: PTX support for Blackwell |
| `pr-cccl-cub-3671` | upstream-code | [`sources/prs/cccl-cub/PR-3671.md`](../sources/prs/cccl-cub/PR-3671.md) | [libcudacxx] Stable abstraction for Blackwell work-stealing (PTX try_cancel) |
| `pr-cccl-cub-3691` | upstream-code | [`sources/prs/cccl-cub/PR-3691.md`](../sources/prs/cccl-cub/PR-3691.md) | Fix SM100 histogram tunings |
| `pr-cccl-cub-3708` | upstream-code | [`sources/prs/cccl-cub/PR-3708.md`](../sources/prs/cccl-cub/PR-3708.md) | Add b200 policies for partition.three_way |
| `pr-cccl-cub-3818` | upstream-code | [`sources/prs/cccl-cub/PR-3818.md`](../sources/prs/cccl-cub/PR-3818.md) | Add arch_traits for sm100 to cudax. |
| `pr-cccl-cub-4000` | upstream-code | [`sources/prs/cccl-cub/PR-4000.md`](../sources/prs/cccl-cub/PR-4000.md) | Drop CUB_MIN|MAX in warp_scan_shfl |
| `pr-cccl-cub-4778` | upstream-code | [`sources/prs/cccl-cub/PR-4778.md`](../sources/prs/cccl-cub/PR-4778.md) | Align bulk copies to 16 bytes on Blackwell |
| `pr-cccl-cub-5178` | upstream-code | [`sources/prs/cccl-cub/PR-5178.md`](../sources/prs/cccl-cub/PR-5178.md) | Support types with any alignment in UBLKCP transform kernel |
| `pr-cccl-cub-5526` | upstream-code | [`sources/prs/cccl-cub/PR-5526.md`](../sources/prs/cccl-cub/PR-5526.md) | Special case `DeviceTransform` for no inputs and provide a `DeviceTransform::Fill` API |
| `pr-cccl-cub-5822` | upstream-code | [`sources/prs/cccl-cub/PR-5822.md`](../sources/prs/cccl-cub/PR-5822.md) | Do not require `int128` in `for_each_canceled` |
| `pr-cccl-cub-6007` | upstream-code | [`sources/prs/cccl-cub/PR-6007.md`](../sources/prs/cccl-cub/PR-6007.md) | Use just SYNCS unit to wait on cuda::barrier on SM90+ |
| `pr-cccl-cub-6250` | upstream-code | [`sources/prs/cccl-cub/PR-6250.md`](../sources/prs/cccl-cub/PR-6250.md) | Replace inline PTX by cuda::ptx in cuda::barrier<thread_scope_block> |
| `pr-cccl-cub-6362` | upstream-code | [`sources/prs/cccl-cub/PR-6362.md`](../sources/prs/cccl-cub/PR-6362.md) | Use `cp_async_bulk(space_shared,...)` when available |
| `pr-cccl-cub-6811` | upstream-code | [`sources/prs/cccl-cub/PR-6811.md`](../sources/prs/cccl-cub/PR-6811.md) | Integrate decoupled lookahead warpspeed scan |
| `pr-cccl-cub-6915` | upstream-code | [`sources/prs/cccl-cub/PR-6915.md`](../sources/prs/cccl-cub/PR-6915.md) | Remove need for hardcoded `LevelT` for histogram in c.parallel and cuda.compute |
| `pr-cccl-cub-6926` | upstream-code | [`sources/prs/cccl-cub/PR-6926.md`](../sources/prs/cccl-cub/PR-6926.md) | Expose not guaranteed determinism to reduce in cuda.compute |
| `pr-cccl-cub-6932` | upstream-code | [`sources/prs/cccl-cub/PR-6932.md`](../sources/prs/cccl-cub/PR-6932.md) | [CUB]: Use the new tuning API for nondeterministic reduce |
| `pr-cccl-cub-7334` | upstream-code | [`sources/prs/cccl-cub/PR-7334.md`](../sources/prs/cccl-cub/PR-7334.md) | Implement the new tuning API for `DeviceSegmentedReduce` |
| `pr-cccl-cub-7861` | upstream-code | [`sources/prs/cccl-cub/PR-7861.md`](../sources/prs/cccl-cub/PR-7861.md) | Improve warpspeed scan tuning for sm120 |
| `pr-cccl-cub-7924` | upstream-code | [`sources/prs/cccl-cub/PR-7924.md`](../sources/prs/cccl-cub/PR-7924.md) | Implement parallel `cuda::std::reverse` |
| `pr-cccl-cub-8061` | upstream-code | [`sources/prs/cccl-cub/PR-8061.md`](../sources/prs/cccl-cub/PR-8061.md) | Implement parallel `cuda::std::transform_inclusive_scan` |
| `pr-cccl-cub-8107` | upstream-code | [`sources/prs/cccl-cub/PR-8107.md`](../sources/prs/cccl-cub/PR-8107.md) | Implement parallel `cuda::std::shift_left` |
| `pr-cccl-cub-8158` | upstream-code | [`sources/prs/cccl-cub/PR-8158.md`](../sources/prs/cccl-cub/PR-8158.md) | Let scan tuning policy choose warpspeed or not |
| `pr-cccl-cub-8395` | upstream-code | [`sources/prs/cccl-cub/PR-8395.md`](../sources/prs/cccl-cub/PR-8395.md) | [CUB] Replace `Shuffle(Up|Down|Index)` with cuda::device::warp_shuffle - RadixSort only |
| `pr-cccl-cub-8421` | upstream-code | [`sources/prs/cccl-cub/PR-8421.md`](../sources/prs/cccl-cub/PR-8421.md) | New tuning API for DeviceUniqueByKey |
| `pr-cccl-cub-8611` | upstream-code | [`sources/prs/cccl-cub/PR-8611.md`](../sources/prs/cccl-cub/PR-8611.md) | Add B200 tuning for warpspeed_scan  |
| `pr-cccl-cub-8621` | upstream-code | [`sources/prs/cccl-cub/PR-8621.md`](../sources/prs/cccl-cub/PR-8621.md) | Implement parallel `cuda::std::sort` |
| `pr-cccl-cub-8775` | upstream-code | [`sources/prs/cccl-cub/PR-8775.md`](../sources/prs/cccl-cub/PR-8775.md) | `cuda::std::simd` Optimize Arithmetic Floating-point Operations |
| `pr-cccl-cub-8803` | upstream-code | [`sources/prs/cccl-cub/PR-8803.md`](../sources/prs/cccl-cub/PR-8803.md) | Fix DeviceTransform byte-offset overflow when num_items*sizeof(T) > 4Gb |
| `pr-cccl-cub-8922` | upstream-code | [`sources/prs/cccl-cub/PR-8922.md`](../sources/prs/cccl-cub/PR-8922.md) | Disable warpspeed scan on sm120 with nvcc < 13.4 |
| `pr-cccl-cub-8939` | upstream-code | [`sources/prs/cccl-cub/PR-8939.md`](../sources/prs/cccl-cub/PR-8939.md) | Enable clang-diagnositc clang-tidy checks |
| `pr-cutlass-2790` | upstream-code | [`sources/prs/cutlass/PR-2790.md`](../sources/prs/cutlass/PR-2790.md) | Blockscaled Ragged Contiguous Grouped Gemm for MoEs |
| `pr-cutlass-3092` | upstream-code | [`sources/prs/cutlass/PR-3092.md`](../sources/prs/cutlass/PR-3092.md) | Support for Group GEMM in CUTLASS Profiler for GeForce and Spark |
| `pr-deepgemm-112` | upstream-code | [`sources/prs/deepgemm/PR-112.md`](../sources/prs/deepgemm/PR-112.md) | Add more GPU architectures support |
| `pr-deepgemm-158` | upstream-code | [`sources/prs/deepgemm/PR-158.md`](../sources/prs/deepgemm/PR-158.md) | Fix inappropriate configs for some small shapes |
| `pr-deepgemm-193` | upstream-code | [`sources/prs/deepgemm/PR-193.md`](../sources/prs/deepgemm/PR-193.md) | Fix multicast bug and optimize masked GEMM |
| `pr-deepgemm-198` | upstream-code | [`sources/prs/deepgemm/PR-198.md`](../sources/prs/deepgemm/PR-198.md) | Make various updates and fixes |
| `pr-deepgemm-227` | upstream-code | [`sources/prs/deepgemm/PR-227.md`](../sources/prs/deepgemm/PR-227.md) | Use larger MMA shape to optimize sm100_fp8_mqa_logits |
| `pr-deepgemm-233` | upstream-code | [`sources/prs/deepgemm/PR-233.md`](../sources/prs/deepgemm/PR-233.md) | support bf16 bias in deepgemm2 |
| `pr-deepgemm-270` | upstream-code | [`sources/prs/deepgemm/PR-270.md`](../sources/prs/deepgemm/PR-270.md) | fix: use SM90ArchSpec instead of SM100ArchSpec in sm90_bf16_k_grouped_gemm |
| `pr-deepgemm-316` | upstream-code | [`sources/prs/deepgemm/PR-316.md`](../sources/prs/deepgemm/PR-316.md) | Add various optimizations and Mega MoE benchmarks |
| `pr-deepgemm-328` | upstream-code | [`sources/prs/deepgemm/PR-328.md`](../sources/prs/deepgemm/PR-328.md) | Sync nv_dev with upstream #316 (Mega MoE optimizations & benchmarks) |
| `pr-flash-attention-1427` | upstream-code | [`sources/prs/flash-attention/PR-1427.md`](../sources/prs/flash-attention/PR-1427.md) | Generalize cuda version checks for A100 and above |
| `pr-flash-attention-1840` | upstream-code | [`sources/prs/flash-attention/PR-1840.md`](../sources/prs/flash-attention/PR-1840.md) | Refactors to enable FlexAttention |
| `pr-flash-attention-1940` | upstream-code | [`sources/prs/flash-attention/PR-1940.md`](../sources/prs/flash-attention/PR-1940.md) | [Cute,Fwd,Sm100] Implement SplitKV |
| `pr-flash-attention-1945` | upstream-code | [`sources/prs/flash-attention/PR-1945.md`](../sources/prs/flash-attention/PR-1945.md) | Blackwell FlashAttention-BWD (v1.0) |
| `pr-flash-attention-1985` | upstream-code | [`sources/prs/flash-attention/PR-1985.md`](../sources/prs/flash-attention/PR-1985.md) | [Cute] Block sparse support Sm100 |
| `pr-flash-attention-1993` | upstream-code | [`sources/prs/flash-attention/PR-1993.md`](../sources/prs/flash-attention/PR-1993.md) | [Cute,Fwd,Sm100] Support `q_stage=1` for inference |
| `pr-flash-attention-1999` | upstream-code | [`sources/prs/flash-attention/PR-1999.md`](../sources/prs/flash-attention/PR-1999.md) | [Cute,Fwd,Sm100] Support paged attention |
| `pr-flash-attention-2014` | upstream-code | [`sources/prs/flash-attention/PR-2014.md`](../sources/prs/flash-attention/PR-2014.md) | [Cute,Sm100,Fwd] use correction warps for epi when not using TMA |
| `pr-flash-attention-2025` | upstream-code | [`sources/prs/flash-attention/PR-2025.md`](../sources/prs/flash-attention/PR-2025.md) | Bump pin |
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
| `pr-flash-attention-2150` | upstream-code | [`sources/prs/flash-attention/PR-2150.md`](../sources/prs/flash-attention/PR-2150.md) | [Cute, Bwd, Sm100] Add varlen for sm100 bwd |
| `pr-flash-attention-2180` | upstream-code | [`sources/prs/flash-attention/PR-2180.md`](../sources/prs/flash-attention/PR-2180.md) | [Cute][Flex]Add pack-gqa divmod |
| `pr-flash-attention-2186` | upstream-code | [`sources/prs/flash-attention/PR-2186.md`](../sources/prs/flash-attention/PR-2186.md) | [Cute,Fwd,Sm100] support irregular qhead / kvhead ratios |
| `pr-flash-attention-2202` | upstream-code | [`sources/prs/flash-attention/PR-2202.md`](../sources/prs/flash-attention/PR-2202.md) | BWD sm100 2cta |
| `pr-flash-attention-2209` | upstream-code | [`sources/prs/flash-attention/PR-2209.md`](../sources/prs/flash-attention/PR-2209.md) | [Flex][SM100] Replay expand fix on sm100 |
| `pr-flash-attention-2218` | upstream-code | [`sources/prs/flash-attention/PR-2218.md`](../sources/prs/flash-attention/PR-2218.md) | [Ai-assisted] CLC work stealing |
| `pr-flash-attention-2236` | upstream-code | [`sources/prs/flash-attention/PR-2236.md`](../sources/prs/flash-attention/PR-2236.md) | [Cute,Flex,Fwd] Allow vectorized score_mod definitions |
| `pr-flash-attention-2270` | upstream-code | [`sources/prs/flash-attention/PR-2270.md`](../sources/prs/flash-attention/PR-2270.md) | [Cute,Sm100,Bwd] Add hdim 192 hdimv 128 backward for sm100 |
| `pr-flash-attention-2292` | upstream-code | [`sources/prs/flash-attention/PR-2292.md`](../sources/prs/flash-attention/PR-2292.md) | Fix sm100 fwd missing tSrQs init regression |
| `pr-flash-attention-2303` | upstream-code | [`sources/prs/flash-attention/PR-2303.md`](../sources/prs/flash-attention/PR-2303.md) | [Cute,Fwd,Sm100] fix paged kv |
| `pr-flash-attention-2309` | upstream-code | [`sources/prs/flash-attention/PR-2309.md`](../sources/prs/flash-attention/PR-2309.md) | [Fwd,Sm100] Extract named barriers |
| `pr-flash-attention-2313` | upstream-code | [`sources/prs/flash-attention/PR-2313.md`](../sources/prs/flash-attention/PR-2313.md) | [Cute,Sm100] Introduce a flexible lambda-based R2P masking |
| `pr-flash-attention-2329` | upstream-code | [`sources/prs/flash-attention/PR-2329.md`](../sources/prs/flash-attention/PR-2329.md) | SM120 forward pass (Blackwell GeForce / DGX Spark) |
| `pr-flash-attention-2330` | upstream-code | [`sources/prs/flash-attention/PR-2330.md`](../sources/prs/flash-attention/PR-2330.md) | [Bwd,Sm120] Add SM120 backward pass support |
| `pr-flash-attention-2332` | upstream-code | [`sources/prs/flash-attention/PR-2332.md`](../sources/prs/flash-attention/PR-2332.md) | [cutlass] Allow compilation of cutlass FA3 for sm100 via enable_sm90 |
| `pr-flash-attention-2333` | upstream-code | [`sources/prs/flash-attention/PR-2333.md`](../sources/prs/flash-attention/PR-2333.md) | Add SM120 varlen attention support |
| `pr-flash-attention-2338` | upstream-code | [`sources/prs/flash-attention/PR-2338.md`](../sources/prs/flash-attention/PR-2338.md) | [Fwd,SM100,CuTe] Fix split KV OOM with diff headdim + fix SM100 kwarg mismatch |
| `pr-flash-attention-2360` | upstream-code | [`sources/prs/flash-attention/PR-2360.md`](../sources/prs/flash-attention/PR-2360.md) | [Fwd,Sm90] Add paged KV attention support (tma and cp.async) |
| `pr-flash-attention-2368` | upstream-code | [`sources/prs/flash-attention/PR-2368.md`](../sources/prs/flash-attention/PR-2368.md) | [Cute] fix: FA4 paged attention kv load for DeepSeek (192,128) on SM100 |
| `pr-flash-attention-2390` | upstream-code | [`sources/prs/flash-attention/PR-2390.md`](../sources/prs/flash-attention/PR-2390.md) | [Cute,Sm100,Bwd] refine bwd swizzle for deterministic |
| `pr-flash-attention-2412` | upstream-code | [`sources/prs/flash-attention/PR-2412.md`](../sources/prs/flash-attention/PR-2412.md) | Feat([FA4][CUTE DSL]) Add head_dim=256 support (forward + backward) |
| `pr-flash-attention-2433` | upstream-code | [`sources/prs/flash-attention/PR-2433.md`](../sources/prs/flash-attention/PR-2433.md) | Fix: disable 2-CTA backward mode when block_sparse_tensors is used |
| `pr-flash-attention-2441` | upstream-code | [`sources/prs/flash-attention/PR-2441.md`](../sources/prs/flash-attention/PR-2441.md) | [Cute,Sm100,Fwd] add MLA 64/512 with topk sparsity for MQA 128 heads |
| `pr-flash-attention-2455` | upstream-code | [`sources/prs/flash-attention/PR-2455.md`](../sources/prs/flash-attention/PR-2455.md) | Add CLC scheduler heuristic |
| `pr-flash-attention-2459` | upstream-code | [`sources/prs/flash-attention/PR-2459.md`](../sources/prs/flash-attention/PR-2459.md) | Handle linter for flash mla file |
| `pr-flash-attention-2470` | upstream-code | [`sources/prs/flash-attention/PR-2470.md`](../sources/prs/flash-attention/PR-2470.md) | [Cute,Fwd,Sm100] Fix the crash when seqlen_k=0 |
| `pr-flash-attention-2487` | upstream-code | [`sources/prs/flash-attention/PR-2487.md`](../sources/prs/flash-attention/PR-2487.md) | [Cute,hd256] Post-merge cleanup: dead code, duplicate imports |
| `pr-flash-attention-2488` | upstream-code | [`sources/prs/flash-attention/PR-2488.md`](../sources/prs/flash-attention/PR-2488.md) | [hd256] Improve forward kernel with exp2 FMA emulation (3% to 9% performance gain) |
| `pr-flash-attention-2489` | upstream-code | [`sources/prs/flash-attention/PR-2489.md`](../sources/prs/flash-attention/PR-2489.md) | [hd256] Add TMA paged KV support to SM100 2CTA forward kernel |
| `pr-flash-attention-2495` | upstream-code | [`sources/prs/flash-attention/PR-2495.md`](../sources/prs/flash-attention/PR-2495.md) | benchmarks/tune_ex2_emu: hd256 sweep support and clock lock/unlock |
| `pr-flash-attention-2497` | upstream-code | [`sources/prs/flash-attention/PR-2497.md`](../sources/prs/flash-attention/PR-2497.md) | [FA4][hd256] Backward TMA bulk-store epilogue + LSE/dpsum coalesce |
| `pr-flash-attention-2504` | upstream-code | [`sources/prs/flash-attention/PR-2504.md`](../sources/prs/flash-attention/PR-2504.md) | [SM100] Guard gO None in empty-tile correction |
| `pr-flash-attention-2505` | upstream-code | [`sources/prs/flash-attention/PR-2505.md`](../sources/prs/flash-attention/PR-2505.md) | Fix: pass `stream` to SM100 MLA kernel |
| `pr-flash-attention-2510` | upstream-code | [`sources/prs/flash-attention/PR-2510.md`](../sources/prs/flash-attention/PR-2510.md) | [Cute,Bwd,Sm90] Fix determinism for GQA, port Sm100 approach in |
| `pr-flash-attention-2513` | upstream-code | [`sources/prs/flash-attention/PR-2513.md`](../sources/prs/flash-attention/PR-2513.md) | SM90 FA4 QuACK 0.4 Compatibility |
| `pr-flash-attention-2543` | upstream-code | [`sources/prs/flash-attention/PR-2543.md`](../sources/prs/flash-attention/PR-2543.md) | [CuTe,Bwd,Sm100] don't disable 2cta due to cuda 12 in bwd |
| `pr-flash-attention-2549` | upstream-code | [`sources/prs/flash-attention/PR-2549.md`](../sources/prs/flash-attention/PR-2549.md) | [Cute,Bwd,Sm100] fix incorrect calculation of n_block global max for bwd deterministic |
| `pr-flashinfer-2557` | upstream-code | [`sources/prs/flashinfer/PR-2557.md`](../sources/prs/flashinfer/PR-2557.md) | [Bugfix][comm] Fix FP4 one-shot launch config instability in trtllm_allreduce_fusion |
| `pr-flashinfer-2726` | upstream-code | [`sources/prs/flashinfer/PR-2726.md`](../sources/prs/flashinfer/PR-2726.md) | Added missing padding |
| `pr-flashinfer-2779` | upstream-code | [`sources/prs/flashinfer/PR-2779.md`](../sources/prs/flashinfer/PR-2779.md) | feat: FP8 output support for CUTLASS MLA paged attention |
| `pr-flashinfer-2914` | upstream-code | [`sources/prs/flashinfer/PR-2914.md`](../sources/prs/flashinfer/PR-2914.md) | feat: Add cuBLASLt backend for `mm_bf16` and enable multi-tactic autotuning for FP8/MXFP8 runners |
| `pr-flashinfer-2944` | upstream-code | [`sources/prs/flashinfer/PR-2944.md`](../sources/prs/flashinfer/PR-2944.md) | feat: Add CuTe DSL grouped-gemm + combine fusion support |
| `pr-flashinfer-2951` | upstream-code | [`sources/prs/flashinfer/PR-2951.md`](../sources/prs/flashinfer/PR-2951.md) | feat: Add DCP All-to-All kernel for context-parallel attention reduction |
| `pr-flashinfer-2962` | upstream-code | [`sources/prs/flashinfer/PR-2962.md`](../sources/prs/flashinfer/PR-2962.md) | Improved `simple` mamba SSU kernel  |
| `pr-flashinfer-3027` | upstream-code | [`sources/prs/flashinfer/PR-3027.md`](../sources/prs/flashinfer/PR-3027.md) | [feat] Trtllm-gen Per-token Nvfp4 MoE |
| `pr-flashinfer-3039` | upstream-code | [`sources/prs/flashinfer/PR-3039.md`](../sources/prs/flashinfer/PR-3039.md) | feat: Integrate CuTe DSL FMHA prefill kernels by loading cubin |
| `pr-flashinfer-3080` | upstream-code | [`sources/prs/flashinfer/PR-3080.md`](../sources/prs/flashinfer/PR-3080.md) | feat: Add b12x_fused_moe / B12xMoEWrapper SM120 APIs with micro kernel and ReLU2 |
| `pr-flashinfer-3113` | upstream-code | [`sources/prs/flashinfer/PR-3113.md`](../sources/prs/flashinfer/PR-3113.md) | Fix: Extend b12x FP4 GEMM support to SM121 (GB10/DGX Spark) |
| `pr-flashinfer-3132` | upstream-code | [`sources/prs/flashinfer/PR-3132.md`](../sources/prs/flashinfer/PR-3132.md) | [CuTe DSL] Fix FP8 MLA persistent perf regression and ProxyKind cu13 wheel breakage |
| `pr-flashinfer-3155` | upstream-code | [`sources/prs/flashinfer/PR-3155.md`](../sources/prs/flashinfer/PR-3155.md) | fix(gdn): use physical SM count for SM100 persistent prefill kernel |
| `pr-flashinfer-3157` | upstream-code | [`sources/prs/flashinfer/PR-3157.md`](../sources/prs/flashinfer/PR-3157.md) | feat: DiT layer norm fusions for WAN: flashinfer.diffusion_ops |
| `pr-flashinfer-3191` | upstream-code | [`sources/prs/flashinfer/PR-3191.md`](../sources/prs/flashinfer/PR-3191.md) | fix(sm12x): fix micro-kernel workspace sizing when routed_rows > num_local_experts |
| `pr-flashinfer-3193` | upstream-code | [`sources/prs/flashinfer/PR-3193.md`](../sources/prs/flashinfer/PR-3193.md) | perf(moe): optimize SM120 b12x MoE short decode |
| `pr-flashinfer-3203` | upstream-code | [`sources/prs/flashinfer/PR-3203.md`](../sources/prs/flashinfer/PR-3203.md) | Include TinyGEMM into BF16 autotuner |
| `pr-flashinfer-3216` | upstream-code | [`sources/prs/flashinfer/PR-3216.md`](../sources/prs/flashinfer/PR-3216.md) | fix(cute_dsl/moe): make autotuner bucket configuration adapt to runtime input |
| `pr-flashinfer-3235` | upstream-code | [`sources/prs/flashinfer/PR-3235.md`](../sources/prs/flashinfer/PR-3235.md) | Support Kimi K2.5 H64 CuTe DSL MLA decode |
| `pr-flashinfer-3252` | upstream-code | [`sources/prs/flashinfer/PR-3252.md`](../sources/prs/flashinfer/PR-3252.md) | fix(cute_dsl/moe): unbias autotuner profiling for tile_size enumeration |
| `pr-flashinfer-3259` | upstream-code | [`sources/prs/flashinfer/PR-3259.md`](../sources/prs/flashinfer/PR-3259.md) | Add dynamic tokens-per-page TRTLLM-GEN GQA kernels |
| `pr-flashinfer-3271` | upstream-code | [`sources/prs/flashinfer/PR-3271.md`](../sources/prs/flashinfer/PR-3271.md) | feat(moe): add SM120 W4A16 b12x kernels |
| `pr-quack-100` | upstream-code | [`sources/prs/quack/PR-100.md`](../sources/prs/quack/PR-100.md) | Autotune between tma gather and cp.async in SM100 |
| `pr-quack-117` | upstream-code | [`sources/prs/quack/PR-117.md`](../sources/prs/quack/PR-117.md) | [Gemm] Add tile_K parameter and enable 2CTA for tile_m=128 |
| `pr-quack-118` | upstream-code | [`sources/prs/quack/PR-118.md`](../sources/prs/quack/PR-118.md) | Add remaining SM120 / RTX 50 support for GEMM epilogues and RMS paths |
| `pr-quack-120` | upstream-code | [`sources/prs/quack/PR-120.md`](../sources/prs/quack/PR-120.md) | Fix ColVecReduce shared-memory staging |
| `pr-quack-132` | upstream-code | [`sources/prs/quack/PR-132.md`](../sources/prs/quack/PR-132.md) | RMS Norm Bwd: Optimize for GB200 w/ TMA loads, reload_x, separate output dtype, new launch configs |
| `pr-quack-74` | upstream-code | [`sources/prs/quack/PR-74.md`](../sources/prs/quack/PR-74.md) | Fix gather fusion in SM100 |
| `pr-quack-75` | upstream-code | [`sources/prs/quack/PR-75.md`](../sources/prs/quack/PR-75.md) | Better gemm configs that reduce 80% autotuning time |
| `pr-quack-76` | upstream-code | [`sources/prs/quack/PR-76.md`](../sources/prs/quack/PR-76.md) | Support to only store mPostAct |
| `pr-quack-80` | upstream-code | [`sources/prs/quack/PR-80.md`](../sources/prs/quack/PR-80.md) | CLC should be autotunable in SM100 rather than a fixed argument |
| `pr-quack-81` | upstream-code | [`sources/prs/quack/PR-81.md`](../sources/prs/quack/PR-81.md) | [SM100] fix CLC persistence for varlen-M tile scheduler |
| `pr-quack-82` | upstream-code | [`sources/prs/quack/PR-82.md`](../sources/prs/quack/PR-82.md) | Add stochastic rounding support for GEMM epilogue |
| `pr-quack-84` | upstream-code | [`sources/prs/quack/PR-84.md`](../sources/prs/quack/PR-84.md) | Expand SM100 autotuning space |
| `pr-quack-85` | upstream-code | [`sources/prs/quack/PR-85.md`](../sources/prs/quack/PR-85.md) | Avoid CUDA context initialization at import time |
| `pr-quack-87` | upstream-code | [`sources/prs/quack/PR-87.md`](../sources/prs/quack/PR-87.md) | Optimal Tile Size for Blackwell Symmetric is (256, 256) |
| `pr-quack-94` | upstream-code | [`sources/prs/quack/PR-94.md`](../sources/prs/quack/PR-94.md) | [Gemm] fix sm120 gemm kernel invocation error |
| `pr-quack-96` | upstream-code | [`sources/prs/quack/PR-96.md`](../sources/prs/quack/PR-96.md) | Add SM120 (consumer Blackwell) support |
| `pr-quack-98` | upstream-code | [`sources/prs/quack/PR-98.md`](../sources/prs/quack/PR-98.md) | Remove asm_dialect=AD_ATT from inline PTX assembly calls |
| `pr-quack-99` | upstream-code | [`sources/prs/quack/PR-99.md`](../sources/prs/quack/PR-99.md) | add _get_mma_inst_tile_k() virtual method to GemmSm100 |
| `pr-sglang-20047` | upstream-code | [`sources/prs/sglang/PR-20047.md`](../sources/prs/sglang/PR-20047.md) | fix: default FP4 GEMM backend to flashinfer_cudnn on SM120 (Blackwell) |
| `pr-sglang-24925` | upstream-code | [`sources/prs/sglang/PR-24925.md`](../sources/prs/sglang/PR-24925.md) | [attn backend] Integrate tokenspeed_mla prefill/decode kernels (fp8 kv cache, blackwell) |
| `pr-tensorrt-llm-10042` | upstream-code | [`sources/prs/tensorrt-llm/PR-10042.md`](../sources/prs/tensorrt-llm/PR-10042.md) | [None][perf] Add more optimization options for MOE CuteDSL finalized kernel |
| `pr-tensorrt-llm-10043` | upstream-code | [`sources/prs/tensorrt-llm/PR-10043.md`](../sources/prs/tensorrt-llm/PR-10043.md) | [TRTLLM-9992][perf] Enable PDL for CuteDSL kernels and overlap MoeOutputMemset |
| `pr-tensorrt-llm-10088` | upstream-code | [`sources/prs/tensorrt-llm/PR-10088.md`](../sources/prs/tensorrt-llm/PR-10088.md) | [None][feat] CuteDSL MOE FC1 Enhancement |
| `pr-tensorrt-llm-10130` | upstream-code | [`sources/prs/tensorrt-llm/PR-10130.md`](../sources/prs/tensorrt-llm/PR-10130.md) | [TRTLLM-9457][feat] Add cute dsl fp8 gemm for Blackwell |
| `pr-tensorrt-llm-10190` | upstream-code | [`sources/prs/tensorrt-llm/PR-10190.md`](../sources/prs/tensorrt-llm/PR-10190.md) | [None][feat] sm100 weight-only kernel |
| `pr-tensorrt-llm-10201` | upstream-code | [`sources/prs/tensorrt-llm/PR-10201.md`](../sources/prs/tensorrt-llm/PR-10201.md) | [TRTLLM-9831][perf] Enable 2CTA with autotune for CuteDSL MoE and Grouped GEMM optimizations |
| `pr-tensorrt-llm-10226` | upstream-code | [`sources/prs/tensorrt-llm/PR-10226.md`](../sources/prs/tensorrt-llm/PR-10226.md) | [TRTLLM-9798][feat] Change to use new DeepGEMM MQA sm100 kernel for MTP-3 |
| `pr-tensorrt-llm-10327` | upstream-code | [`sources/prs/tensorrt-llm/PR-10327.md`](../sources/prs/tensorrt-llm/PR-10327.md) | [None][fix] impl fused triton kernel for e8m0 resmooth to reduce memory footprint |
| `pr-tensorrt-llm-10429` | upstream-code | [`sources/prs/tensorrt-llm/PR-10429.md`](../sources/prs/tensorrt-llm/PR-10429.md) | [None] [feat] Add test script and raster M for gather fc1 kernel |
| `pr-tensorrt-llm-10479` | upstream-code | [`sources/prs/tensorrt-llm/PR-10479.md`](../sources/prs/tensorrt-llm/PR-10479.md) | [None] [feat] Add densegemm backend for MoE |
| `pr-tensorrt-llm-10987` | upstream-code | [`sources/prs/tensorrt-llm/PR-10987.md`](../sources/prs/tensorrt-llm/PR-10987.md) | [TRTLLM-9831][perf] Use TMA.RED to improve effective memory bandwidth |
| `pr-tensorrt-llm-11273` | upstream-code | [`sources/prs/tensorrt-llm/PR-11273.md`](../sources/prs/tensorrt-llm/PR-11273.md) | [None][feat] Optimize super-v3 nvfp4 for better perf |
| `pr-tensorrt-llm-11473` | upstream-code | [`sources/prs/tensorrt-llm/PR-11473.md`](../sources/prs/tensorrt-llm/PR-11473.md) | [None][feat] Optimize by fuse nvfp4_quant to layernorm_gated for mamba2_mixer |
| `pr-tensorrt-llm-11652` | upstream-code | [`sources/prs/tensorrt-llm/PR-11652.md`](../sources/prs/tensorrt-llm/PR-11652.md) | [None][feat] NVFP4 TRTLLM-Gen MoE for AutoDeploy (Nemotron Super) |
| `pr-tensorrt-llm-11697` | upstream-code | [`sources/prs/tensorrt-llm/PR-11697.md`](../sources/prs/tensorrt-llm/PR-11697.md) | [TRTLLM-11092][feat] add support for visual gen FA4 attention backend |
| `pr-tensorrt-llm-11718` | upstream-code | [`sources/prs/tensorrt-llm/PR-11718.md`](../sources/prs/tensorrt-llm/PR-11718.md) | [TRTLLM-11119][feat] Blackwell SageAttention, Integrate into AttentionOp API |
| `pr-tensorrt-llm-11897` | upstream-code | [`sources/prs/tensorrt-llm/PR-11897.md`](../sources/prs/tensorrt-llm/PR-11897.md) | [TRTLLM-10990][feat] Fuse SwiGLU and quant into shared expert |
| `pr-tensorrt-llm-11900` | upstream-code | [`sources/prs/tensorrt-llm/PR-11900.md`](../sources/prs/tensorrt-llm/PR-11900.md) | [TRTLLM-10407][feat] Integrate CuTE DSL top-k kernel for Blackwell |
| `pr-tensorrt-llm-12074` | upstream-code | [`sources/prs/tensorrt-llm/PR-12074.md`](../sources/prs/tensorrt-llm/PR-12074.md) | [TRTLLM-11289][feat] Integrate CuteDSL's bf16 dense GEMMs |
| `pr-tensorrt-llm-12079` | upstream-code | [`sources/prs/tensorrt-llm/PR-12079.md`](../sources/prs/tensorrt-llm/PR-12079.md) | [None][feat] CuteDSL MOE: Add raster along M/N support for blockscaled contiguous backbone kernel |
| `pr-tensorrt-llm-12136` | upstream-code | [`sources/prs/tensorrt-llm/PR-12136.md`](../sources/prs/tensorrt-llm/PR-12136.md) | [None][feat] Add DWDP (Distributed Weight Data Parallelism) support for MoE inference |
| `pr-tensorrt-llm-12236` | upstream-code | [`sources/prs/tensorrt-llm/PR-12236.md`](../sources/prs/tensorrt-llm/PR-12236.md) | [TRTLLM-10407][perf] Enable CuteDSL indexer_top_k in model |
| `pr-tensorrt-llm-12354` | upstream-code | [`sources/prs/tensorrt-llm/PR-12354.md`](../sources/prs/tensorrt-llm/PR-12354.md) | [TRTLLM-10407][perf] Add cute dsl single pass multi cta cluster topk |
| `pr-tensorrt-llm-12470` | upstream-code | [`sources/prs/tensorrt-llm/PR-12470.md`](../sources/prs/tensorrt-llm/PR-12470.md) | [None][feat] Support sparse mqa/gqa attention |
| `pr-tensorrt-llm-12506` | upstream-code | [`sources/prs/tensorrt-llm/PR-12506.md`](../sources/prs/tensorrt-llm/PR-12506.md) | [None][feat] Add PDL support to CuTE DSL top-k kernels |
| `pr-tensorrt-llm-12519` | upstream-code | [`sources/prs/tensorrt-llm/PR-12519.md`](../sources/prs/tensorrt-llm/PR-12519.md) | [#12634][feat] AutoDeploy: Support rank 256 MLA in flashinfer_mla |
| `pr-tensorrt-llm-12612` | upstream-code | [`sources/prs/tensorrt-llm/PR-12612.md`](../sources/prs/tensorrt-llm/PR-12612.md) | [None][feat] Trtllm-gen FMHA JIT support |
| `pr-tensorrt-llm-12679` | upstream-code | [`sources/prs/tensorrt-llm/PR-12679.md`](../sources/prs/tensorrt-llm/PR-12679.md) | [None][revert] Revert "[TRTLLM-11119][feat] Blackwell SageAttention, Integrate into … |
| `pr-tensorrt-llm-12884` | upstream-code | [`sources/prs/tensorrt-llm/PR-12884.md`](../sources/prs/tensorrt-llm/PR-12884.md) | [TRTLLM-11585][feat] Add CUTEDSL moe backend for nemotron-h |
| `pr-tensorrt-llm-12937` | upstream-code | [`sources/prs/tensorrt-llm/PR-12937.md`](../sources/prs/tensorrt-llm/PR-12937.md) | [TRTLLM-11485][feat] Feature rework: Add SageAttention refreshed kernels (attentionOp only) |
| `pr-tensorrt-llm-12946` | upstream-code | [`sources/prs/tensorrt-llm/PR-12946.md`](../sources/prs/tensorrt-llm/PR-12946.md) | [#12784][feat] AutoDeploy: Optimize DeepSeek-R1 model performance |
| `pr-tensorrt-llm-13064` | upstream-code | [`sources/prs/tensorrt-llm/PR-13064.md`](../sources/prs/tensorrt-llm/PR-13064.md) | [None][chore] Update flashinfer-python from 0.6.6 to 0.6.8 |
| `pr-tensorrt-llm-13081` | upstream-code | [`sources/prs/tensorrt-llm/PR-13081.md`](../sources/prs/tensorrt-llm/PR-13081.md) | [TRTLLM-11540][feat] Revert revert of EAGLE3 dynamic tree speculative decoding support |
| `pr-tensorrt-llm-13169` | upstream-code | [`sources/prs/tensorrt-llm/PR-13169.md`](../sources/prs/tensorrt-llm/PR-13169.md) | [https://nvbugs/5945047][fix] Fix cluster launch enablement for SM120 GPUs in allReduce fusion |
| `pr-tensorrt-llm-13219` | upstream-code | [`sources/prs/tensorrt-llm/PR-13219.md`](../sources/prs/tensorrt-llm/PR-13219.md) | [TRTLLM-34871][feat] Add cute dsl FP8 paged MQA logits decode kernel |
| `pr-tensorrt-llm-13340` | upstream-code | [`sources/prs/tensorrt-llm/PR-13340.md`](../sources/prs/tensorrt-llm/PR-13340.md) | [None][feat] Integrate FP4 indexer for DSA on Blackwell |
| `pr-tensorrt-llm-13470` | upstream-code | [`sources/prs/tensorrt-llm/PR-13470.md`](../sources/prs/tensorrt-llm/PR-13470.md) | [https://nvbugs/6017720][fix] Fix moe backend mismatch on Blackwell in perf test. |
| `pr-tensorrt-llm-13496` | upstream-code | [`sources/prs/tensorrt-llm/PR-13496.md`](../sources/prs/tensorrt-llm/PR-13496.md) | [https://nvbugs/6114727][fix] Unwaive deepseek r1 fp4 v2 grace_blackwell r1 fp4 v2 tep4 mtp3 1k1k |
| `pr-tensorrt-llm-13505` | upstream-code | [`sources/prs/tensorrt-llm/PR-13505.md`](../sources/prs/tensorrt-llm/PR-13505.md) | [None][perf] Drop cubin and Eliminate ~6s FMHA JIT recompile in eager generation by aligning kernel selection with CUDA graph warmup |
| `pr-tensorrt-llm-13542` | upstream-code | [`sources/prs/tensorrt-llm/PR-13542.md`](../sources/prs/tensorrt-llm/PR-13542.md) | [None][chore] Convert cubins in repository to compressed archives |
| `pr-tensorrt-llm-13595` | upstream-code | [`sources/prs/tensorrt-llm/PR-13595.md`](../sources/prs/tensorrt-llm/PR-13595.md) | [None][feat] Enable EPLB for DeepSeek-V4 |
| `pr-tensorrt-llm-13628` | upstream-code | [`sources/prs/tensorrt-llm/PR-13628.md`](../sources/prs/tensorrt-llm/PR-13628.md) | [None][feat] Fuse FP8 1x128 quantize + UE8M0 scale pack on SM100 |
| `pr-tensorrt-llm-13652` | upstream-code | [`sources/prs/tensorrt-llm/PR-13652.md`](../sources/prs/tensorrt-llm/PR-13652.md) | [None][feat] Add DeepSeekV4 attention kernels |
| `pr-tensorrt-llm-13658` | upstream-code | [`sources/prs/tensorrt-llm/PR-13658.md`](../sources/prs/tensorrt-llm/PR-13658.md) | [None][test] add Nemotron Ultra V3 AutoDeploy accuracy test |
| `pr-tensorrt-llm-13660` | upstream-code | [`sources/prs/tensorrt-llm/PR-13660.md`](../sources/prs/tensorrt-llm/PR-13660.md) | [TRTLLM-12383][fix] limit MHC TF32 pmap GEMM to SM100 |
| `pr-tensorrt-llm-13714` | upstream-code | [`sources/prs/tensorrt-llm/PR-13714.md`](../sources/prs/tensorrt-llm/PR-13714.md) | [None][docs] add GVR Top-K technical blog |
| `pr-tensorrt-llm-13740` | upstream-code | [`sources/prs/tensorrt-llm/PR-13740.md`](../sources/prs/tensorrt-llm/PR-13740.md) | [https://nvbugs/6108841][fix] add hidden_dim=6144 router GEMM instantiation for GLM-5 |
| `pr-tensorrt-llm-13767` | upstream-code | [`sources/prs/tensorrt-llm/PR-13767.md`](../sources/prs/tensorrt-llm/PR-13767.md) | [None][fix] Plumb swiglu_limit through DeepGEMM and TRTLLMGen FP8 fused MoE |
| `pr-tensorrt-llm-13808` | upstream-code | [`sources/prs/tensorrt-llm/PR-13808.md`](../sources/prs/tensorrt-llm/PR-13808.md) | [None][feat] Update FMHA cubins for head_dim 80 |
| `pr-tensorrt-llm-13873` | upstream-code | [`sources/prs/tensorrt-llm/PR-13873.md`](../sources/prs/tensorrt-llm/PR-13873.md) | [TRTLLM-12503][feat] Parallel VAE independent scaling and fix arg passing |
| `pr-tensorrt-llm-13929` | upstream-code | [`sources/prs/tensorrt-llm/PR-13929.md`](../sources/prs/tensorrt-llm/PR-13929.md) | [TRTLLM-35237][feat] Add cute dsl FP4 paged MQA logits decode kernel |
| `pr-tensorrt-llm-13938` | upstream-code | [`sources/prs/tensorrt-llm/PR-13938.md`](../sources/prs/tensorrt-llm/PR-13938.md) | [None][feat] Keep DSv4 o_a_proj as FP8, and port vLLM's fused_inv_rope_fp8_quant |
| `pr-tensorrt-llm-4867` | upstream-code | [`sources/prs/tensorrt-llm/PR-4867.md`](../sources/prs/tensorrt-llm/PR-4867.md) | feat: Add w4a8_mxfp4_fp8 quantization recipe. |
| `pr-tensorrt-llm-6809` | upstream-code | [`sources/prs/tensorrt-llm/PR-6809.md`](../sources/prs/tensorrt-llm/PR-6809.md) | [OMNIML-2336][feat] Add NVFP4 x FP8 |
| `pr-tensorrt-llm-9025` | upstream-code | [`sources/prs/tensorrt-llm/PR-9025.md`](../sources/prs/tensorrt-llm/PR-9025.md) | [None][feat] Update TRTLLM MoE cubins; reduce mxfp4 weight padding requirement; tighten TMA bound |
| `pr-tensorrt-llm-9618` | upstream-code | [`sources/prs/tensorrt-llm/PR-9618.md`](../sources/prs/tensorrt-llm/PR-9618.md) | [TRTLLM-9685] [feat] Add gather fc1 kernel by cuteDSL |
| `pr-tensorrt-llm-9729` | upstream-code | [`sources/prs/tensorrt-llm/PR-9729.md`](../sources/prs/tensorrt-llm/PR-9729.md) | [None][feat] add fp4 gemm + allreduce |
| `pr-thunderkittens-172` | upstream-code | [`sources/prs/thunderkittens/PR-172.md`](../sources/prs/thunderkittens/PR-172.md) | add educational blackwell series |
| `pr-thunderkittens-84` | upstream-code | [`sources/prs/thunderkittens/PR-84.md`](../sources/prs/thunderkittens/PR-84.md) | WIP Blackwell fp8 support |
| `pr-tilelang-1229` | upstream-code | [`sources/prs/tilelang/PR-1229.md`](../sources/prs/tilelang/PR-1229.md) | [WIP] support more dtypes for tcgen05 |
| `pr-tilelang-1327` | upstream-code | [`sources/prs/tilelang/PR-1327.md`](../sources/prs/tilelang/PR-1327.md) | [Enhancement] add more dtype and fix mma.ws for fp16 for tcgen05 |
| `pr-tilelang-1717` | upstream-code | [`sources/prs/tilelang/PR-1717.md`](../sources/prs/tilelang/PR-1717.md) | [Enhancement] Add explicit global memory load/store intrinsics (ldg/stg 32/64/128) |
| `pr-tilelang-1764` | upstream-code | [`sources/prs/tilelang/PR-1764.md`](../sources/prs/tilelang/PR-1764.md) | [Feature] Support tcgen5mma lowering for `.kind::i8` |
| `pr-tilelang-1774` | upstream-code | [`sources/prs/tilelang/PR-1774.md`](../sources/prs/tilelang/PR-1774.md) | [Example][BugFix] 1SM GEMM example on Blackwell and fix handling of `mbar` |
| `pr-tilelang-1837` | upstream-code | [`sources/prs/tilelang/PR-1837.md`](../sources/prs/tilelang/PR-1837.md) | Fix tilelang global load/store template |
| `pr-tilelang-1839` | upstream-code | [`sources/prs/tilelang/PR-1839.md`](../sources/prs/tilelang/PR-1839.md) | [CUDA][Feature] Add packed FP32x2 math intrinsics and auto vectorized support |
| `pr-tilelang-1855` | upstream-code | [`sources/prs/tilelang/PR-1855.md`](../sources/prs/tilelang/PR-1855.md) | [Enhancement] GEMM V2 on SM90/SM100 CuTeDSL backend |
| `pr-tilelang-1866` | upstream-code | [`sources/prs/tilelang/PR-1866.md`](../sources/prs/tilelang/PR-1866.md) | [CUDA] Support tcgen5mma gemm ts |
| `pr-tilelang-1874` | upstream-code | [`sources/prs/tilelang/PR-1874.md`](../sources/prs/tilelang/PR-1874.md) | [Feature] Support cluster launch, query, synchronization and barrier operations |
| `pr-tilelang-1882` | upstream-code | [`sources/prs/tilelang/PR-1882.md`](../sources/prs/tilelang/PR-1882.md) | [Feature] 2-SM support for TMA, TMEM and TCGEN5MMA on Blackwell |
| `pr-tilelang-1910` | upstream-code | [`sources/prs/tilelang/PR-1910.md`](../sources/prs/tilelang/PR-1910.md) | [Example] Flash Attention SM100 |
| `pr-tilelang-1945` | upstream-code | [`sources/prs/tilelang/PR-1945.md`](../sources/prs/tilelang/PR-1945.md) | [Feature] Block-scaled GEMM support for MXFP8 on Blackwell |
| `pr-tilelang-1946` | upstream-code | [`sources/prs/tilelang/PR-1946.md`](../sources/prs/tilelang/PR-1946.md) | [BugFix] Update usage of tma load in SM100 manual warp-specialized examples |
| `pr-tilelang-1949` | upstream-code | [`sources/prs/tilelang/PR-1949.md`](../sources/prs/tilelang/PR-1949.md) | [Refactor] Separate gemm into explicit `wgmma_gemm` and `tcgen05_gemm` functions |
| `pr-tilelang-1978` | upstream-code | [`sources/prs/tilelang/PR-1978.md`](../sources/prs/tilelang/PR-1978.md) | Unified packed x2 intrinsics with multi-dtype support and bug fixes |
| `pr-tilelang-1980` | upstream-code | [`sources/prs/tilelang/PR-1980.md`](../sources/prs/tilelang/PR-1980.md) | [BugFix] Add missing fences in GEMM SM100 examples and canonicalize the order of blockIdx |
| `pr-tilelang-1995` | upstream-code | [`sources/prs/tilelang/PR-1995.md`](../sources/prs/tilelang/PR-1995.md) | [BugFix] Fix missing barrier init attrs when TMA is disabled |
| `pr-tilelang-2001` | upstream-code | [`sources/prs/tilelang/PR-2001.md`](../sources/prs/tilelang/PR-2001.md) | [Refactor] Refactor CUDA atomic helpers |
| `pr-tilelang-2003` | upstream-code | [`sources/prs/tilelang/PR-2003.md`](../sources/prs/tilelang/PR-2003.md) | [Transform] Add InjectTcgen05Fence pass |
| `pr-tilelang-2004` | upstream-code | [`sources/prs/tilelang/PR-2004.md`](../sources/prs/tilelang/PR-2004.md) | fix: fix copy+cast vectorize loop to use wider vector load/store instrcution |
| `pr-tilelang-2015` | upstream-code | [`sources/prs/tilelang/PR-2015.md`](../sources/prs/tilelang/PR-2015.md) | [BugFix] Enhance CUDA vectorization for binary operations |
| `pr-tilelang-2017` | upstream-code | [`sources/prs/tilelang/PR-2017.md`](../sources/prs/tilelang/PR-2017.md) | [codex] Fuse packed x2 mul-add into fma2 in CUDA codegen |
| `pr-tilelang-2029` | upstream-code | [`sources/prs/tilelang/PR-2029.md`](../sources/prs/tilelang/PR-2029.md) | [Feature][Example] Introduce CLC tile schedule and add example for sm100 GEMM |
| `pr-tilelang-2033` | upstream-code | [`sources/prs/tilelang/PR-2033.md`](../sources/prs/tilelang/PR-2033.md) | [Refactor] Remove GEMM v1 and promote gemm_py to be the canonical gemm op |
| `pr-tilelang-2037` | upstream-code | [`sources/prs/tilelang/PR-2037.md`](../sources/prs/tilelang/PR-2037.md) | [Bugfix][Subtype] Fix scalar fp4 store/load codegen for non-packed buffers |
| `pr-tilelang-2052` | upstream-code | [`sources/prs/tilelang/PR-2052.md`](../sources/prs/tilelang/PR-2052.md) | [Bugfix] Use shared::cta instead of shared::cluster for non-cluster T… |
| `pr-tilelang-2075` | upstream-code | [`sources/prs/tilelang/PR-2075.md`](../sources/prs/tilelang/PR-2075.md) | [Refactor] Phaseout legacy util `map_torch_type` with `T.dtype.as_torch` |
| `pr-tilelang-2087` | upstream-code | [`sources/prs/tilelang/PR-2087.md`](../sources/prs/tilelang/PR-2087.md) | [Bugfix] Enable `.shared::cta` in TMA copy paths only on CUDA 12.8+ |
| `pr-tilelang-2098` | upstream-code | [`sources/prs/tilelang/PR-2098.md`](../sources/prs/tilelang/PR-2098.md) | [Example] Add MXFP8 blockscaled grouped gemm examples with transB support  |
| `pr-tilelang-2102` | upstream-code | [`sources/prs/tilelang/PR-2102.md`](../sources/prs/tilelang/PR-2102.md) | [CUDA][SM100] Include cuda_fp6.h when emitting FP6 types |
| `pr-tilelang-2107` | upstream-code | [`sources/prs/tilelang/PR-2107.md`](../sources/prs/tilelang/PR-2107.md) | [TMA] Support FP4 TensorMap TMA copies |
| `pr-tilelang-2117` | upstream-code | [`sources/prs/tilelang/PR-2117.md`](../sources/prs/tilelang/PR-2117.md) | [Enhancement][CUDA][SM100] Report unsupported FP6 vector types earlier |
| `pr-tilelang-2134` | upstream-code | [`sources/prs/tilelang/PR-2134.md`](../sources/prs/tilelang/PR-2134.md) | fix: TMA alignment to 1024 bytes on Blackwell |
| `pr-tilelang-2152` | upstream-code | [`sources/prs/tilelang/PR-2152.md`](../sources/prs/tilelang/PR-2152.md) | [docs] fix TMEM description |
| `pr-tilelang-2161` | upstream-code | [`sources/prs/tilelang/PR-2161.md`](../sources/prs/tilelang/PR-2161.md) | [Refactor] Refactor multiple TensorCoreIntrinEmitter to provide atom-level mma control interface |
| `pr-triton-10126` | upstream-code | [`sources/prs/triton/PR-10126.md`](../sources/prs/triton/PR-10126.md) | Do not send f64 dots through tcgen05 |
| `pr-triton-10148` | upstream-code | [`sources/prs/triton/PR-10148.md`](../sources/prs/triton/PR-10148.md) | [Reland][NVIDIA] Support swizzle 0 TMA + MMA for Hopper and Blackwell |
| `pr-triton-10234` | upstream-code | [`sources/prs/triton/PR-10234.md`](../sources/prs/triton/PR-10234.md) | [ BACKEND ]  Enable `tl.dot` with TF32 precision on tiles with N=8 and K=8 |
| `pr-triton-10275` | upstream-code | [`sources/prs/triton/PR-10275.md`](../sources/prs/triton/PR-10275.md) | Support zero-sized Hopper MX scale layouts |
| `pr-triton-10318` | upstream-code | [`sources/prs/triton/PR-10318.md`](../sources/prs/triton/PR-10318.md) | Support MN-packing in decomposed fp4 dot_scaled |
| `pr-vllm-34260` | upstream-code | [`sources/prs/vllm/PR-34260.md`](../sources/prs/vllm/PR-34260.md) | [Model Bash]: Improve FP8 Oracle for Config Specific Kernel Selection |
| `pr-vllm-37463` | upstream-code | [`sources/prs/vllm/PR-37463.md`](../sources/prs/vllm/PR-37463.md) | [Kernel] Add MXFP4 W4A4 CUTLASS MoE kernel for SM100 |
| `pr-vllm-39306` | upstream-code | [`sources/prs/vllm/PR-39306.md`](../sources/prs/vllm/PR-39306.md) | Use CU_MEMCPY_SRC_ACCESS_ORDER_ANY for batch KV cache swaps |
| `pr-vllm-40177` | upstream-code | [`sources/prs/vllm/PR-40177.md`](../sources/prs/vllm/PR-40177.md) | Add nvfp4 kv cache support |
| `pr-vllm-40191` | upstream-code | [`sources/prs/vllm/PR-40191.md`](../sources/prs/vllm/PR-40191.md) | [Bugfix] Guard mxfp4_experts_quant bindings on ENABLE_NVFP4_SM100 |
| `pr-vllm-40408` | upstream-code | [`sources/prs/vllm/PR-40408.md`](../sources/prs/vllm/PR-40408.md) | [Perf] Batch invariance with Cutlass fp8 support, 28.9% E2E latency improvement |
| `pr-vllm-41050` | upstream-code | [`sources/prs/vllm/PR-41050.md`](../sources/prs/vllm/PR-41050.md) | [Kernel][MoE] Support GELU on TRT-LLM NvFP4 fused MoE for Gemma4 |
| `pr-vllm-41326` | upstream-code | [`sources/prs/vllm/PR-41326.md`](../sources/prs/vllm/PR-41326.md) | Faster per-token fp8 group quant packed kernel for blackwell |
| `pr-vllm-41428` | upstream-code | [`sources/prs/vllm/PR-41428.md`](../sources/prs/vllm/PR-41428.md) | [DSv4] Improved fused Indexer Q quant kernel |
| `pr-vllm-41566` | upstream-code | [`sources/prs/vllm/PR-41566.md`](../sources/prs/vllm/PR-41566.md) | [Quantization] Rework quantization_config to use QuantKey and allow for activation override |
| `pr-vllm-41664` | upstream-code | [`sources/prs/vllm/PR-41664.md`](../sources/prs/vllm/PR-41664.md) | [MXFP4] Support for linear layers + compressed-tensors integration |
| `pr-vllm-41778` | upstream-code | [`sources/prs/vllm/PR-41778.md`](../sources/prs/vllm/PR-41778.md) | [MLA Attention Backend] Add TOKENSPEED_MLA backend for DSR1/Kimi K25 prefill + decode on Blackwell |
| `pr-vllm-41882` | upstream-code | [`sources/prs/vllm/PR-41882.md`](../sources/prs/vllm/PR-41882.md) | Add NVFP4 all-gather GEMM fusion for AsyncTP |

<a id="block-scale"></a>
## block-scale

26 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `blog-amandeep-nvfp4` | community-note | [`sources/blogs/amandeep-nvfp4-attempts.md`](../sources/blogs/amandeep-nvfp4-attempts.md) | Twelve Attempts at NVFP4 Batched GEMV |
| `blog-yue-nvfp4` | community-note | [`sources/blogs/yue-nvfp4-hackathon.md`](../sources/blogs/yue-nvfp4-hackathon.md) | Blackwell NVFP4 Kernel Hackathon Journey |
| `contest-flashinfer-track-a` | contest-report | [`sources/contests/flashinfer-mlsys26/track-a-fused-moe.md`](../sources/contests/flashinfer-mlsys26/track-a-fused-moe.md) | FlashInfer MLSys 2026 - Track A: Fused MoE FP8 |
| `contest-flashinfer-track-b` | contest-report | [`sources/contests/flashinfer-mlsys26/track-b-sparse-attention.md`](../sources/contests/flashinfer-mlsys26/track-b-sparse-attention.md) | FlashInfer MLSys 2026 - Track B: DeepSeek V3.2 Sparse Attention |
| `contest-gpumode-p1` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-1-gemv.md`](../sources/contests/gpu-mode-nvfp4/problem-1-gemv.md) | GPU Mode NVFP4 Hackathon - Problem 1: Batched GEMV |
| `contest-gpumode-p2` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-2-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-2-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 2: NVFP4 GEMM |
| `contest-gpumode-p3` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-3-gated-dual-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-3-gated-dual-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 3: Gated Dual GEMM |
| `contest-gpumode-p4` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 4: Grouped GEMM |
| `pr-cutlass-2139` | upstream-code | [`sources/prs/cutlass/PR-2139.md`](../sources/prs/cutlass/PR-2139.md) | Blockwise and Groupwise GEMM for Blackwell and Improvements for Hopper |
| `pr-cutlass-2995` | upstream-code | [`sources/prs/cutlass/PR-2995.md`](../sources/prs/cutlass/PR-2995.md) | [CuTeDSL] Fix: SM100 block-scale gemm overlapping accumulator |
| `pr-deepgemm-304` | upstream-code | [`sources/prs/deepgemm/PR-304.md`](../sources/prs/deepgemm/PR-304.md) | [Public release 26/04] Introducing Mega MoE, FP4 Indexer and other features/fixes |
| `pr-flashinfer-1548` | upstream-code | [`sources/prs/flashinfer/PR-1548.md`](../sources/prs/flashinfer/PR-1548.md) | perf: Enable SplitK and fix autotuner for trtllm fp4 fused moe |
| `pr-flashinfer-1969` | upstream-code | [`sources/prs/flashinfer/PR-1969.md`](../sources/prs/flashinfer/PR-1969.md) | feat: enable deepgemm jit for fp8 block-scale on SM90 |
| `pr-flashinfer-2217` | upstream-code | [`sources/prs/flashinfer/PR-2217.md`](../sources/prs/flashinfer/PR-2217.md) | feat: Support unpadded output hidden size for trtllm_fp4_block_scale_moe |
| `pr-flashinfer-2645` | upstream-code | [`sources/prs/flashinfer/PR-2645.md`](../sources/prs/flashinfer/PR-2645.md) | int16 Block-Scaled State and Stochastic Rounding for SSU (mamba) |
| `pr-flashinfer-2739` | upstream-code | [`sources/prs/flashinfer/PR-2739.md`](../sources/prs/flashinfer/PR-2739.md) | Support in-place update for `trtllm_fp8_block_scale_moe` |
| `pr-flashinfer-2853` | upstream-code | [`sources/prs/flashinfer/PR-2853.md`](../sources/prs/flashinfer/PR-2853.md) | fix: int32 overflow in `trtllm_fp4_block_scale_moe` causing "Unsupported hidden state scale shape" for EP32+ configs |
| `pr-flashinfer-2898` | upstream-code | [`sources/prs/flashinfer/PR-2898.md`](../sources/prs/flashinfer/PR-2898.md) | fix: snap weight_scale_vec_size to handle block_scale_interleave padding for SM120 |
| `pr-flashinfer-2916` | upstream-code | [`sources/prs/flashinfer/PR-2916.md`](../sources/prs/flashinfer/PR-2916.md) | fix: Fix autotuner crash on meta-device tensor in trtllm_fp4_block_scale_routed_moe |
| `pr-flashinfer-2954` | upstream-code | [`sources/prs/flashinfer/PR-2954.md`](../sources/prs/flashinfer/PR-2954.md) | Only swizzle on v block scale; rename kv_block_scales to kv_cache_sf |
| `pr-sglang-15731` | upstream-code | [`sources/prs/sglang/PR-15731.md`](../sources/prs/sglang/PR-15731.md) | [Perf] Eliminate the slice op for Flashinfer `trtllm_fp4_block_scale_moe` |
| `pr-sglang-3529` | upstream-code | [`sources/prs/sglang/PR-3529.md`](../sources/prs/sglang/PR-3529.md) | integrate blockwise fp8 kernel |
| `pr-vllm-13571` | upstream-code | [`sources/prs/vllm/PR-13571.md`](../sources/prs/vllm/PR-13571.md) | [NVIDIA] Support nvfp4 cutlass gemm |
| `pr-vllm-14968` | upstream-code | [`sources/prs/vllm/PR-14968.md`](../sources/prs/vllm/PR-14968.md) | [FEAT] [ROCm]: Add AITER Block-Scaled GEMM Feature |
| `pr-vllm-23696` | upstream-code | [`sources/prs/vllm/PR-23696.md`](../sources/prs/vllm/PR-23696.md) | [Kernel][B200] `mxfp4` fused cutlass moe |
| `pr-vllm-34494` | upstream-code | [`sources/prs/vllm/PR-34494.md`](../sources/prs/vllm/PR-34494.md) | [Bugfix] Handle num_expert_group=None in flashinfer block-scale FP8 MoE |

<a id="clc"></a>
## clc

10 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `blog-modular-blackwell` | community-note | [`sources/blogs/modular-blackwell-matmul.md`](../sources/blogs/modular-blackwell-matmul.md) | Modular: Matrix Multiplication on Blackwell |
| `contest-gpumode-p4` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 4: Grouped GEMM |
| `pr-cutlass-2161` | upstream-code | [`sources/prs/cutlass/PR-2161.md`](../sources/prs/cutlass/PR-2161.md) | Blockwise Improvement and Programmatic Dependent Launch |
| `pr-cutlass-2746` | upstream-code | [`sources/prs/cutlass/PR-2746.md`](../sources/prs/cutlass/PR-2746.md) | Support for GEMM-K=0 for Blackwell Grouped GEMMs |
| `pr-cutlass-3021` | upstream-code | [`sources/prs/cutlass/PR-3021.md`](../sources/prs/cutlass/PR-3021.md) | [Cute-DSL] Add option for issue_clc_query without multicast |
| `pr-flash-attention-2218` | upstream-code | [`sources/prs/flash-attention/PR-2218.md`](../sources/prs/flash-attention/PR-2218.md) | [Ai-assisted] CLC work stealing |
| `pr-flash-attention-2455` | upstream-code | [`sources/prs/flash-attention/PR-2455.md`](../sources/prs/flash-attention/PR-2455.md) | Add CLC scheduler heuristic |
| `pr-quack-80` | upstream-code | [`sources/prs/quack/PR-80.md`](../sources/prs/quack/PR-80.md) | CLC should be autotunable in SM100 rather than a fixed argument |
| `pr-quack-81` | upstream-code | [`sources/prs/quack/PR-81.md`](../sources/prs/quack/PR-81.md) | [SM100] fix CLC persistence for varlen-M tile scheduler |
| `pr-tilelang-2029` | upstream-code | [`sources/prs/tilelang/PR-2029.md`](../sources/prs/tilelang/PR-2029.md) | [Feature][Example] Introduce CLC tile schedule and add example for sm100 GEMM |

<a id="fp4"></a>
## fp4

488 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `blog-amandeep-nvfp4` | community-note | [`sources/blogs/amandeep-nvfp4-attempts.md`](../sources/blogs/amandeep-nvfp4-attempts.md) | Twelve Attempts at NVFP4 Batched GEMV |
| `blog-yue-nvfp4` | community-note | [`sources/blogs/yue-nvfp4-hackathon.md`](../sources/blogs/yue-nvfp4-hackathon.md) | Blackwell NVFP4 Kernel Hackathon Journey |
| `contest-gpumode-p1` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-1-gemv.md`](../sources/contests/gpu-mode-nvfp4/problem-1-gemv.md) | GPU Mode NVFP4 Hackathon - Problem 1: Batched GEMV |
| `contest-gpumode-p2` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-2-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-2-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 2: NVFP4 GEMM |
| `contest-gpumode-p3` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-3-gated-dual-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-3-gated-dual-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 3: Gated Dual GEMM |
| `contest-gpumode-p4` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 4: Grouped GEMM |
| `pr-cccl-cub-3832` | upstream-code | [`sources/prs/cccl-cub/PR-3832.md`](../sources/prs/cccl-cub/PR-3832.md) | Specialize `numeric_limits` for CUDA 12.8 FP types |
| `pr-cccl-cub-4340` | upstream-code | [`sources/prs/cccl-cub/PR-4340.md`](../sources/prs/cccl-cub/PR-4340.md) | Disable extended floating-point types for nvc++ |
| `pr-cccl-cub-5371` | upstream-code | [`sources/prs/cccl-cub/PR-5371.md`](../sources/prs/cccl-cub/PR-5371.md) | Complex sqrt accuracy/speed improvements |
| `pr-cccl-cub-8351` | upstream-code | [`sources/prs/cccl-cub/PR-8351.md`](../sources/prs/cccl-cub/PR-8351.md) | Fix and improve vector type traits |
| `pr-deepgemm-304` | upstream-code | [`sources/prs/deepgemm/PR-304.md`](../sources/prs/deepgemm/PR-304.md) | [Public release 26/04] Introducing Mega MoE, FP4 Indexer and other features/fixes |
| `pr-deepgemm-316` | upstream-code | [`sources/prs/deepgemm/PR-316.md`](../sources/prs/deepgemm/PR-316.md) | Add various optimizations and Mega MoE benchmarks |
| `pr-deepgemm-328` | upstream-code | [`sources/prs/deepgemm/PR-328.md`](../sources/prs/deepgemm/PR-328.md) | Sync nv_dev with upstream #316 (Mega MoE optimizations & benchmarks) |
| `pr-flash-attention-2385` | upstream-code | [`sources/prs/flash-attention/PR-2385.md`](../sources/prs/flash-attention/PR-2385.md) | [ROCM] Fix windows issues |
| `pr-flashinfer-1114` | upstream-code | [`sources/prs/flashinfer/PR-1114.md`](../sources/prs/flashinfer/PR-1114.md) | bugfix: Fix test and output shape of fp4 quantize |
| `pr-flashinfer-1176` | upstream-code | [`sources/prs/flashinfer/PR-1176.md`](../sources/prs/flashinfer/PR-1176.md) | Expose fp4 blockscale swizzling kernel |
| `pr-flashinfer-1214` | upstream-code | [`sources/prs/flashinfer/PR-1214.md`](../sources/prs/flashinfer/PR-1214.md) | Feature/sm100 low latency nvfp4 kernels |
| `pr-flashinfer-1241` | upstream-code | [`sources/prs/flashinfer/PR-1241.md`](../sources/prs/flashinfer/PR-1241.md) | feat: Support MXFP8 x MXFP4 CUTLASS grouped GEMM |
| `pr-flashinfer-1251` | upstream-code | [`sources/prs/flashinfer/PR-1251.md`](../sources/prs/flashinfer/PR-1251.md) | Reduce the JIT compilation time of gen_gemm_sm100_module |
| `pr-flashinfer-1288` | upstream-code | [`sources/prs/flashinfer/PR-1288.md`](../sources/prs/flashinfer/PR-1288.md) | add mm_fp4 use cudnn backend |
| `pr-flashinfer-1294` | upstream-code | [`sources/prs/flashinfer/PR-1294.md`](../sources/prs/flashinfer/PR-1294.md) | Update cutlass fp4 moe kernels |
| `pr-flashinfer-1296` | upstream-code | [`sources/prs/flashinfer/PR-1296.md`](../sources/prs/flashinfer/PR-1296.md) | add cutlass backend for mm_fp4 |
| `pr-flashinfer-1309` | upstream-code | [`sources/prs/flashinfer/PR-1309.md`](../sources/prs/flashinfer/PR-1309.md) | Refactor Fused Moe Module |
| `pr-flashinfer-1310` | upstream-code | [`sources/prs/flashinfer/PR-1310.md`](../sources/prs/flashinfer/PR-1310.md) | Support loading autotuned results from json for cutlass fp4 moe backends |
| `pr-flashinfer-1318` | upstream-code | [`sources/prs/flashinfer/PR-1318.md`](../sources/prs/flashinfer/PR-1318.md) | feat: support output nvfp4 in trtllm-gen function call. |
| `pr-flashinfer-1331` | upstream-code | [`sources/prs/flashinfer/PR-1331.md`](../sources/prs/flashinfer/PR-1331.md) | feat: masked layout fp4 gemm using cute-dsl |
| `pr-flashinfer-1333` | upstream-code | [`sources/prs/flashinfer/PR-1333.md`](../sources/prs/flashinfer/PR-1333.md) | add torch float4_e2m1fn_x2 check for cudnn fp4 backend |
| `pr-flashinfer-1334` | upstream-code | [`sources/prs/flashinfer/PR-1334.md`](../sources/prs/flashinfer/PR-1334.md) | [Fix] remove torch 2.8 requirement for FP4 GEMM |
| `pr-flashinfer-1355` | upstream-code | [`sources/prs/flashinfer/PR-1355.md`](../sources/prs/flashinfer/PR-1355.md) | feature: add fp4 mm using trtllm backend |
| `pr-flashinfer-1360` | upstream-code | [`sources/prs/flashinfer/PR-1360.md`](../sources/prs/flashinfer/PR-1360.md) | support trtllm-gen prefill fp4 output |
| `pr-flashinfer-1361` | upstream-code | [`sources/prs/flashinfer/PR-1361.md`](../sources/prs/flashinfer/PR-1361.md) | Update autotune results for the nvfp4 cutlass moe backends for v0.2.9 |
| `pr-flashinfer-1363` | upstream-code | [`sources/prs/flashinfer/PR-1363.md`](../sources/prs/flashinfer/PR-1363.md) | Support scale factor start index for fp4 mha prefill/decode |
| `pr-flashinfer-1371` | upstream-code | [`sources/prs/flashinfer/PR-1371.md`](../sources/prs/flashinfer/PR-1371.md) | bugfix: fixed cutlass fused moe usage of FP4QuantizationSFLayout::SWIZZLED |
| `pr-flashinfer-1376` | upstream-code | [`sources/prs/flashinfer/PR-1376.md`](../sources/prs/flashinfer/PR-1376.md) | bugfix: Add guard for fp4/fp8 related include headers |
| `pr-flashinfer-1389` | upstream-code | [`sources/prs/flashinfer/PR-1389.md`](../sources/prs/flashinfer/PR-1389.md) | GPT-OSS Support: Add Blackwell MoE mxfp4 implementation from TRTLLM and Attention Sink |
| `pr-flashinfer-1396` | upstream-code | [`sources/prs/flashinfer/PR-1396.md`](../sources/prs/flashinfer/PR-1396.md) | gpt-oss: Add MXFP8 x MXFP4 CUTLASS MOE for SM100 and BF16 x MXFP4 CUTLASS for SM90 + SwigluBias Activation |
| `pr-flashinfer-1405` | upstream-code | [`sources/prs/flashinfer/PR-1405.md`](../sources/prs/flashinfer/PR-1405.md) | feature: enable cublas for fp4 gemm when cudnn == 9.11.1 or >= 9.13 |
| `pr-flashinfer-1412` | upstream-code | [`sources/prs/flashinfer/PR-1412.md`](../sources/prs/flashinfer/PR-1412.md) | Faster weight processing (moe nvfp4) |
| `pr-flashinfer-1446` | upstream-code | [`sources/prs/flashinfer/PR-1446.md`](../sources/prs/flashinfer/PR-1446.md) | Remove getEnvEnablePDL in favor of enable_pdl parameter |
| `pr-flashinfer-1460` | upstream-code | [`sources/prs/flashinfer/PR-1460.md`](../sources/prs/flashinfer/PR-1460.md) | Fix TRTLLM NVFP4-out attention kernel scale factor dim issue |
| `pr-flashinfer-1475` | upstream-code | [`sources/prs/flashinfer/PR-1475.md`](../sources/prs/flashinfer/PR-1475.md) | tuner: Trtllm-gen Fp4 MoE Autotunner |
| `pr-flashinfer-1480` | upstream-code | [`sources/prs/flashinfer/PR-1480.md`](../sources/prs/flashinfer/PR-1480.md) | fix missing enable_pdl argument in trtllm-gen fp4 moe |
| `pr-flashinfer-1481` | upstream-code | [`sources/prs/flashinfer/PR-1481.md`](../sources/prs/flashinfer/PR-1481.md) | Add python API for masked grouped gemm |
| `pr-flashinfer-1498` | upstream-code | [`sources/prs/flashinfer/PR-1498.md`](../sources/prs/flashinfer/PR-1498.md) | feat: scaling at fp4 gemm epilogue |
| `pr-flashinfer-1521` | upstream-code | [`sources/prs/flashinfer/PR-1521.md`](../sources/prs/flashinfer/PR-1521.md) | refactor fp4 masked gemm cute-dsl implementation and add manual cache |
| `pr-flashinfer-1525` | upstream-code | [`sources/prs/flashinfer/PR-1525.md`](../sources/prs/flashinfer/PR-1525.md) | Add GeGLU support to trtllm-gen NVFP4 Fused MoE Kernel |
| `pr-flashinfer-1548` | upstream-code | [`sources/prs/flashinfer/PR-1548.md`](../sources/prs/flashinfer/PR-1548.md) | perf: Enable SplitK and fix autotuner for trtllm fp4 fused moe |
| `pr-flashinfer-1565` | upstream-code | [`sources/prs/flashinfer/PR-1565.md`](../sources/prs/flashinfer/PR-1565.md) | fix: separate out fp4 lib into sm90 and sm100 versions, add oob checking in fused moe |
| `pr-flashinfer-1573` | upstream-code | [`sources/prs/flashinfer/PR-1573.md`](../sources/prs/flashinfer/PR-1573.md) | update trtllm-gen fp4 autotuner and routing |
| `pr-flashinfer-1608` | upstream-code | [`sources/prs/flashinfer/PR-1608.md`](../sources/prs/flashinfer/PR-1608.md) | feat: initial support for SM103, SM110, SM120, SM121 |
| `pr-flashinfer-1609` | upstream-code | [`sources/prs/flashinfer/PR-1609.md`](../sources/prs/flashinfer/PR-1609.md) | feat: cutlass fp4 gemm bringup for SM120 & SM121 |
| `pr-flashinfer-1611` | upstream-code | [`sources/prs/flashinfer/PR-1611.md`](../sources/prs/flashinfer/PR-1611.md) | bugfix: fix fp4 quantization with 8x4 scale factor layout |
| `pr-flashinfer-1633` | upstream-code | [`sources/prs/flashinfer/PR-1633.md`](../sources/prs/flashinfer/PR-1633.md) | feat: add support of fp4_batched_quantize |
| `pr-flashinfer-1644` | upstream-code | [`sources/prs/flashinfer/PR-1644.md`](../sources/prs/flashinfer/PR-1644.md) | Added mx_fp4 support using the cudnn backend |
| `pr-flashinfer-1666` | upstream-code | [`sources/prs/flashinfer/PR-1666.md`](../sources/prs/flashinfer/PR-1666.md) | [Hotfix] `test_fp4_quantize.py` failure on sm103 |
| `pr-flashinfer-1706` | upstream-code | [`sources/prs/flashinfer/PR-1706.md`](../sources/prs/flashinfer/PR-1706.md) | feat: Benchmark mm_fp4 mxfp4 support and gemm autotune support.  Restore mm_fp4 API behavior |
| `pr-flashinfer-1710` | upstream-code | [`sources/prs/flashinfer/PR-1710.md`](../sources/prs/flashinfer/PR-1710.md) | test: skip the unsupported test cases for sm120/121 |
| `pr-flashinfer-1766` | upstream-code | [`sources/prs/flashinfer/PR-1766.md`](../sources/prs/flashinfer/PR-1766.md) | Added xfail for mx_fp4 matmul on SM120 |
| `pr-flashinfer-1774` | upstream-code | [`sources/prs/flashinfer/PR-1774.md`](../sources/prs/flashinfer/PR-1774.md) | Masked batch nvfp4 quantization |
| `pr-flashinfer-1809` | upstream-code | [`sources/prs/flashinfer/PR-1809.md`](../sources/prs/flashinfer/PR-1809.md) | Support checks PoC |
| `pr-flashinfer-1817` | upstream-code | [`sources/prs/flashinfer/PR-1817.md`](../sources/prs/flashinfer/PR-1817.md) | fix: fp4 moe on sm120 |
| `pr-flashinfer-1835` | upstream-code | [`sources/prs/flashinfer/PR-1835.md`](../sources/prs/flashinfer/PR-1835.md) | [Quantization] Add per-expert global scaling factor for fp4 batched quantize |
| `pr-flashinfer-1862` | upstream-code | [`sources/prs/flashinfer/PR-1862.md`](../sources/prs/flashinfer/PR-1862.md) | raise error for group_gemm_fp8_nt_groupwise then num_groups > 1 on sm120/121 |
| `pr-flashinfer-1882` | upstream-code | [`sources/prs/flashinfer/PR-1882.md`](../sources/prs/flashinfer/PR-1882.md) | feat: Add FP4 TRTLLM-Gen throughput MOE batched gemms |
| `pr-flashinfer-1927` | upstream-code | [`sources/prs/flashinfer/PR-1927.md`](../sources/prs/flashinfer/PR-1927.md) | silu_and_mul nvfp4 quanization fusion rework |
| `pr-flashinfer-1959` | upstream-code | [`sources/prs/flashinfer/PR-1959.md`](../sources/prs/flashinfer/PR-1959.md) | fix: Add cutlass as an mm_fp4 backend in compute capability 12.0 in benchmark code |
| `pr-flashinfer-1979` | upstream-code | [`sources/prs/flashinfer/PR-1979.md`](../sources/prs/flashinfer/PR-1979.md) | feat: Add backend='auto' to mm_fp4 and enable autotune for backend='cudnn' |
| `pr-flashinfer-2011` | upstream-code | [`sources/prs/flashinfer/PR-2011.md`](../sources/prs/flashinfer/PR-2011.md) | Feature: Support non-gated activation in cutlass fused MoE nvfp4 |
| `pr-flashinfer-2012` | upstream-code | [`sources/prs/flashinfer/PR-2012.md`](../sources/prs/flashinfer/PR-2012.md) | fix: Enable SM121 for mm_fp4 |
| `pr-flashinfer-2019` | upstream-code | [`sources/prs/flashinfer/PR-2019.md`](../sources/prs/flashinfer/PR-2019.md) | [DSV3] Optimized Router Gemm |
| `pr-flashinfer-2020` | upstream-code | [`sources/prs/flashinfer/PR-2020.md`](../sources/prs/flashinfer/PR-2020.md) | update trtllm cutlass moe  |
| `pr-flashinfer-2025` | upstream-code | [`sources/prs/flashinfer/PR-2025.md`](../sources/prs/flashinfer/PR-2025.md) | perf: Speed up fp4 quantization for small batch with swizzling for cutlass MoE |
| `pr-flashinfer-2049` | upstream-code | [`sources/prs/flashinfer/PR-2049.md`](../sources/prs/flashinfer/PR-2049.md) | [BUG] Fix trtllm-gen fp4 moe renormalize routing |
| `pr-flashinfer-2082` | upstream-code | [`sources/prs/flashinfer/PR-2082.md`](../sources/prs/flashinfer/PR-2082.md) | Patch sm103 for 3xfp4 moe generation |
| `pr-flashinfer-2095` | upstream-code | [`sources/prs/flashinfer/PR-2095.md`](../sources/prs/flashinfer/PR-2095.md) | perf: enable pdl for cutlass fp4 gemm |
| `pr-flashinfer-2159` | upstream-code | [`sources/prs/flashinfer/PR-2159.md`](../sources/prs/flashinfer/PR-2159.md) | feat: MxInt4 x Bf16 TRT-LLM Gen MoE support |
| `pr-flashinfer-2165` | upstream-code | [`sources/prs/flashinfer/PR-2165.md`](../sources/prs/flashinfer/PR-2165.md) | Add data type check for deepseek fp4 moe |
| `pr-flashinfer-2217` | upstream-code | [`sources/prs/flashinfer/PR-2217.md`](../sources/prs/flashinfer/PR-2217.md) | feat: Support unpadded output hidden size for trtllm_fp4_block_scale_moe |
| `pr-flashinfer-2233` | upstream-code | [`sources/prs/flashinfer/PR-2233.md`](../sources/prs/flashinfer/PR-2233.md) | feat: Fused RMSNorm + FP4 Quantization Kernels in CuTe-DSL |
| `pr-flashinfer-2260` | upstream-code | [`sources/prs/flashinfer/PR-2260.md`](../sources/prs/flashinfer/PR-2260.md) | fix: Add global scale support and optional output allocation for RMSNorm+FP4Quant fusion kernels |
| `pr-flashinfer-2268` | upstream-code | [`sources/prs/flashinfer/PR-2268.md`](../sources/prs/flashinfer/PR-2268.md) | [performance]optimize for nvfp4 |
| `pr-flashinfer-2279` | upstream-code | [`sources/prs/flashinfer/PR-2279.md`](../sources/prs/flashinfer/PR-2279.md) | [WIP] Refactor: simplify torch -> cute-dsl boilerplate and enable tvm-ffi for cute-dsl kernels |
| `pr-flashinfer-2303` | upstream-code | [`sources/prs/flashinfer/PR-2303.md`](../sources/prs/flashinfer/PR-2303.md) | [Perf][Feature] Add SM103-specific schedulers for NVFP4 CUTLASS kernels |
| `pr-flashinfer-2304` | upstream-code | [`sources/prs/flashinfer/PR-2304.md`](../sources/prs/flashinfer/PR-2304.md) | feat: Support Fused MoE non gated Relu2 NVFP4 & FP8 and support Nemotron |
| `pr-flashinfer-2343` | upstream-code | [`sources/prs/flashinfer/PR-2343.md`](../sources/prs/flashinfer/PR-2343.md) | Optimize quantization function in large problem size |
| `pr-flashinfer-2385` | upstream-code | [`sources/prs/flashinfer/PR-2385.md`](../sources/prs/flashinfer/PR-2385.md) | fix: In-place Residual Update for add_rmsnorm_fp4quant |
| `pr-flashinfer-2395` | upstream-code | [`sources/prs/flashinfer/PR-2395.md`](../sources/prs/flashinfer/PR-2395.md) | feat: Add output_both_sf_layouts option to add_rmsnorm_fp4quant API |
| `pr-flashinfer-2398` | upstream-code | [`sources/prs/flashinfer/PR-2398.md`](../sources/prs/flashinfer/PR-2398.md) | feat: cuteDSL fp4 moe for better DSR1 performance. |
| `pr-flashinfer-2404` | upstream-code | [`sources/prs/flashinfer/PR-2404.md`](../sources/prs/flashinfer/PR-2404.md) | perf: mm_fp4 heuristic prioritizes CUTLASS over cuDNN on SM103 |
| `pr-flashinfer-2421` | upstream-code | [`sources/prs/flashinfer/PR-2421.md`](../sources/prs/flashinfer/PR-2421.md) | refactor: simplify fp4 rmsnorm |
| `pr-flashinfer-2428` | upstream-code | [`sources/prs/flashinfer/PR-2428.md`](../sources/prs/flashinfer/PR-2428.md) | refactor: refactoring cuda code to cute-dsl (part 1) |
| `pr-flashinfer-2443` | upstream-code | [`sources/prs/flashinfer/PR-2443.md`](../sources/prs/flashinfer/PR-2443.md) | Add cute-dsl backends to mxfp[8,4]_quantization for future refactor |
| `pr-flashinfer-2460` | upstream-code | [`sources/prs/flashinfer/PR-2460.md`](../sources/prs/flashinfer/PR-2460.md) | perf: add fp4 GEMM tile configs and streamK scheduler for SM120 |
| `pr-flashinfer-2462` | upstream-code | [`sources/prs/flashinfer/PR-2462.md`](../sources/prs/flashinfer/PR-2462.md) | feat: Support Fused MoE non gated Relu2 NVFP4 & FP8 and support Nemotron, fixed |
| `pr-flashinfer-2520` | upstream-code | [`sources/prs/flashinfer/PR-2520.md`](../sources/prs/flashinfer/PR-2520.md) | Support NVFP4 KV cache decode on SM120 |
| `pr-flashinfer-2540` | upstream-code | [`sources/prs/flashinfer/PR-2540.md`](../sources/prs/flashinfer/PR-2540.md) | feat: cute dsl mmfp4 for blackwell |
| `pr-flashinfer-2557` | upstream-code | [`sources/prs/flashinfer/PR-2557.md`](../sources/prs/flashinfer/PR-2557.md) | [Bugfix][comm] Fix FP4 one-shot launch config instability in trtllm_allreduce_fusion |
| `pr-flashinfer-2573` | upstream-code | [`sources/prs/flashinfer/PR-2573.md`](../sources/prs/flashinfer/PR-2573.md) | [Bug] Fix spark unit test failures for test_add_rmsnorm_fp4_quant_cute_dsl |
| `pr-flashinfer-2629` | upstream-code | [`sources/prs/flashinfer/PR-2629.md`](../sources/prs/flashinfer/PR-2629.md) | fix: cute dsl nvfp4 moe routing index error |
| `pr-flashinfer-2631` | upstream-code | [`sources/prs/flashinfer/PR-2631.md`](../sources/prs/flashinfer/PR-2631.md) | fix: add SM121 support to SM120 version guards |
| `pr-flashinfer-2635` | upstream-code | [`sources/prs/flashinfer/PR-2635.md`](../sources/prs/flashinfer/PR-2635.md) | benchmark: Add MXFP4/MXFP8 quantization mode support to FP4 MoE benchmark |
| `pr-flashinfer-2650` | upstream-code | [`sources/prs/flashinfer/PR-2650.md`](../sources/prs/flashinfer/PR-2650.md) | Enable sm120f compilation |
| `pr-flashinfer-2653` | upstream-code | [`sources/prs/flashinfer/PR-2653.md`](../sources/prs/flashinfer/PR-2653.md) | [feat] trtllm-gen mxfp8 gemm |
| `pr-flashinfer-2660` | upstream-code | [`sources/prs/flashinfer/PR-2660.md`](../sources/prs/flashinfer/PR-2660.md) | feat: support mxfp4 & mxfp8 entrypoint for blackwell cutedsl dense gemm |
| `pr-flashinfer-2667` | upstream-code | [`sources/prs/flashinfer/PR-2667.md`](../sources/prs/flashinfer/PR-2667.md) | perf: Update trtllm-gen batched GEMM kernels - faster, more NVFP4 tile dims, MXFP8 with relu2 act |
| `pr-flashinfer-2702` | upstream-code | [`sources/prs/flashinfer/PR-2702.md`](../sources/prs/flashinfer/PR-2702.md) | Add NVFP4 KV cache quantization support for SM100 |
| `pr-flashinfer-2725` | upstream-code | [`sources/prs/flashinfer/PR-2725.md`](../sources/prs/flashinfer/PR-2725.md) | fix: Add SM120 (RTX Blackwell desktop) support for NVFP4 MoE kernels |
| `pr-flashinfer-2726` | upstream-code | [`sources/prs/flashinfer/PR-2726.md`](../sources/prs/flashinfer/PR-2726.md) | Added missing padding |
| `pr-flashinfer-2738` | upstream-code | [`sources/prs/flashinfer/PR-2738.md`](../sources/prs/flashinfer/PR-2738.md) | Support for MXFP4 and NVFP4 group GEMMs on GeForce and Spark |
| `pr-flashinfer-2757` | upstream-code | [`sources/prs/flashinfer/PR-2757.md`](../sources/prs/flashinfer/PR-2757.md) | feat: Add FP4 KV cache quant/dequant kernels  |
| `pr-flashinfer-2838` | upstream-code | [`sources/prs/flashinfer/PR-2838.md`](../sources/prs/flashinfer/PR-2838.md) | feat: Add CuTe-DSL backend for NVFP4 quantization |
| `pr-flashinfer-2841` | upstream-code | [`sources/prs/flashinfer/PR-2841.md`](../sources/prs/flashinfer/PR-2841.md) | [Perf] Add FMHAv2 to flashinfer_benchmark.py and eliminate unnecessary H2D |
| `pr-flashinfer-2853` | upstream-code | [`sources/prs/flashinfer/PR-2853.md`](../sources/prs/flashinfer/PR-2853.md) | fix: int32 overflow in `trtllm_fp4_block_scale_moe` causing "Unsupported hidden state scale shape" for EP32+ configs |
| `pr-flashinfer-2898` | upstream-code | [`sources/prs/flashinfer/PR-2898.md`](../sources/prs/flashinfer/PR-2898.md) | fix: snap weight_scale_vec_size to handle block_scale_interleave padding for SM120 |
| `pr-flashinfer-2904` | upstream-code | [`sources/prs/flashinfer/PR-2904.md`](../sources/prs/flashinfer/PR-2904.md) | perf: Optimize CuTe-DSL fp4 and fp8 quantization kernels |
| `pr-flashinfer-2914` | upstream-code | [`sources/prs/flashinfer/PR-2914.md`](../sources/prs/flashinfer/PR-2914.md) | feat: Add cuBLASLt backend for `mm_bf16` and enable multi-tactic autotuning for FP8/MXFP8 runners |
| `pr-flashinfer-2916` | upstream-code | [`sources/prs/flashinfer/PR-2916.md`](../sources/prs/flashinfer/PR-2916.md) | fix: Fix autotuner crash on meta-device tensor in trtllm_fp4_block_scale_routed_moe |
| `pr-flashinfer-2940` | upstream-code | [`sources/prs/flashinfer/PR-2940.md`](../sources/prs/flashinfer/PR-2940.md) | CuTe DSL FP4 GEMM Heuristic |
| `pr-flashinfer-2954` | upstream-code | [`sources/prs/flashinfer/PR-2954.md`](../sources/prs/flashinfer/PR-2954.md) | Only swizzle on v block scale; rename kv_block_scales to kv_cache_sf |
| `pr-flashinfer-2959` | upstream-code | [`sources/prs/flashinfer/PR-2959.md`](../sources/prs/flashinfer/PR-2959.md) | [Fmha] Add head_dim=512 support for trtllm attention kernels |
| `pr-flashinfer-2962` | upstream-code | [`sources/prs/flashinfer/PR-2962.md`](../sources/prs/flashinfer/PR-2962.md) | Improved `simple` mamba SSU kernel  |
| `pr-flashinfer-2988` | upstream-code | [`sources/prs/flashinfer/PR-2988.md`](../sources/prs/flashinfer/PR-2988.md) | [Fmha] support nvfp4 output keepsMmaAb generation kernels |
| `pr-flashinfer-2994` | upstream-code | [`sources/prs/flashinfer/PR-2994.md`](../sources/prs/flashinfer/PR-2994.md) |   Fix MXFP4/MXFP8 failures in SM120 FAST_BUILD and expand all_tiles[]                                                   |
| `pr-flashinfer-3008` | upstream-code | [`sources/prs/flashinfer/PR-3008.md`](../sources/prs/flashinfer/PR-3008.md) | feat: add PDL support to rmsnorm_fp4quant and add_rmsnorm_fp4quant CuTe DSL kernels |
| `pr-flashinfer-3026` | upstream-code | [`sources/prs/flashinfer/PR-3026.md`](../sources/prs/flashinfer/PR-3026.md) | perf: Port TRT-LLM SM120/SM121 FP4 CUTLASS GEMM optimizations. Add PDL |
| `pr-flashinfer-3027` | upstream-code | [`sources/prs/flashinfer/PR-3027.md`](../sources/prs/flashinfer/PR-3027.md) | [feat] Trtllm-gen Per-token Nvfp4 MoE |
| `pr-flashinfer-3039` | upstream-code | [`sources/prs/flashinfer/PR-3039.md`](../sources/prs/flashinfer/PR-3039.md) | feat: Integrate CuTe DSL FMHA prefill kernels by loading cubin |
| `pr-flashinfer-3051` | upstream-code | [`sources/prs/flashinfer/PR-3051.md`](../sources/prs/flashinfer/PR-3051.md) | feat: Add backend="b12x" for mm_fp4 on SM120 |
| `pr-flashinfer-3066` | upstream-code | [`sources/prs/flashinfer/PR-3066.md`](../sources/prs/flashinfer/PR-3066.md) | feat: Add b12x CuTe DSL fused MoE for SM120 |
| `pr-flashinfer-3080` | upstream-code | [`sources/prs/flashinfer/PR-3080.md`](../sources/prs/flashinfer/PR-3080.md) | feat: Add b12x_fused_moe / B12xMoEWrapper SM120 APIs with micro kernel and ReLU2 |
| `pr-flashinfer-3084` | upstream-code | [`sources/prs/flashinfer/PR-3084.md`](../sources/prs/flashinfer/PR-3084.md) | perf: optimize MXFP4xBF16 & INT4xFP8 CUTLASS MoE backend for SM90 |
| `pr-flashinfer-3097` | upstream-code | [`sources/prs/flashinfer/PR-3097.md`](../sources/prs/flashinfer/PR-3097.md) | Support NVFP4 KV for prefill and batch attention kernels |
| `pr-flashinfer-3113` | upstream-code | [`sources/prs/flashinfer/PR-3113.md`](../sources/prs/flashinfer/PR-3113.md) | Fix: Extend b12x FP4 GEMM support to SM121 (GB10/DGX Spark) |
| `pr-flashinfer-3115` | upstream-code | [`sources/prs/flashinfer/PR-3115.md`](../sources/prs/flashinfer/PR-3115.md) | perf(autotuner): replace power-of-2 token buckets with hybrid spacing & fix missing routing_replay_out arg |
| `pr-flashinfer-3152` | upstream-code | [`sources/prs/flashinfer/PR-3152.md`](../sources/prs/flashinfer/PR-3152.md) | Integrate CUTLASS Small Tile N Blockscaled GEMMs/Grouped GEMMs for SM120 and SM121 |
| `pr-flashinfer-3157` | upstream-code | [`sources/prs/flashinfer/PR-3157.md`](../sources/prs/flashinfer/PR-3157.md) | feat: DiT layer norm fusions for WAN: flashinfer.diffusion_ops |
| `pr-flashinfer-3185` | upstream-code | [`sources/prs/flashinfer/PR-3185.md`](../sources/prs/flashinfer/PR-3185.md) | feat: enable glm5 router gemm |
| `pr-flashinfer-3227` | upstream-code | [`sources/prs/flashinfer/PR-3227.md`](../sources/prs/flashinfer/PR-3227.md) | [Bugfix] Fix fused MoE autotuning correctness issues by filtering clusterDimZ |
| `pr-flashinfer-3237` | upstream-code | [`sources/prs/flashinfer/PR-3237.md`](../sources/prs/flashinfer/PR-3237.md) | perf: optimize per-token nvfp4 quantization kernel. |
| `pr-flashinfer-3239` | upstream-code | [`sources/prs/flashinfer/PR-3239.md`](../sources/prs/flashinfer/PR-3239.md) | Update moe gemm |
| `pr-flashinfer-3271` | upstream-code | [`sources/prs/flashinfer/PR-3271.md`](../sources/prs/flashinfer/PR-3271.md) | feat(moe): add SM120 W4A16 b12x kernels |
| `pr-sglang-10078` | upstream-code | [`sources/prs/sglang/PR-10078.md`](../sources/prs/sglang/PR-10078.md) | feat: Add FP4 (E2M1) KV Cache Support with Quantization Utilities for MLA |
| `pr-sglang-10101` | upstream-code | [`sources/prs/sglang/PR-10101.md`](../sources/prs/sglang/PR-10101.md) | Optimize nvfp4 block scaled gemm kernel when M is small. |
| `pr-sglang-10180` | upstream-code | [`sources/prs/sglang/PR-10180.md`](../sources/prs/sglang/PR-10180.md) | Fix chunked prefix cache for nvfp4 |
| `pr-sglang-10426` | upstream-code | [`sources/prs/sglang/PR-10426.md`](../sources/prs/sglang/PR-10426.md) | Fix correction bias undefined behavior for nvfp4 models |
| `pr-sglang-10579` | upstream-code | [`sources/prs/sglang/PR-10579.md`](../sources/prs/sglang/PR-10579.md) | Fix bias handling in TritonMoeQuantInfo within quantization/mxfp4.py |
| `pr-sglang-10758` | upstream-code | [`sources/prs/sglang/PR-10758.md`](../sources/prs/sglang/PR-10758.md) | Fix MTP MoE weight loading with NVFP4 target model. |
| `pr-sglang-11287` | upstream-code | [`sources/prs/sglang/PR-11287.md`](../sources/prs/sglang/PR-11287.md) | [NVIDIA] Add new SMs support for Spark & Thor |
| `pr-sglang-11708` | upstream-code | [`sources/prs/sglang/PR-11708.md`](../sources/prs/sglang/PR-11708.md) | Support running FP4 Deepseek on SM120. |
| `pr-sglang-11737` | upstream-code | [`sources/prs/sglang/PR-11737.md`](../sources/prs/sglang/PR-11737.md) | support cutlass fp4 kernel in sm120 |
| `pr-sglang-11813` | upstream-code | [`sources/prs/sglang/PR-11813.md`](../sources/prs/sglang/PR-11813.md) | Use cutlass fp4 gemm by default |
| `pr-sglang-11866` | upstream-code | [`sources/prs/sglang/PR-11866.md`](../sources/prs/sglang/PR-11866.md) | Support nvidia/NVIDIA-Nemotron-Nano-9B-v2-FP8/NVFP4 |
| `pr-sglang-12018` | upstream-code | [`sources/prs/sglang/PR-12018.md`](../sources/prs/sglang/PR-12018.md) | Feature/nano v2 offline modelopt fp8 and nvfp4 |
| `pr-sglang-12376` | upstream-code | [`sources/prs/sglang/PR-12376.md`](../sources/prs/sglang/PR-12376.md) | Replace [silu_and_mul_]scaled_fp4_group_quant by Flashinfer equivalent |
| `pr-sglang-12482` | upstream-code | [`sources/prs/sglang/PR-12482.md`](../sources/prs/sglang/PR-12482.md) | Use sgl fp4 quant kernel by default |
| `pr-sglang-12581` | upstream-code | [`sources/prs/sglang/PR-12581.md`](../sources/prs/sglang/PR-12581.md) | [NVIDIA] Fix CUDA arch requirement in nvfp4 cast |
| `pr-sglang-12640` | upstream-code | [`sources/prs/sglang/PR-12640.md`](../sources/prs/sglang/PR-12640.md) | [NVIDIA] Fix wrong symmetric sizes for fp4 cases |
| `pr-sglang-12758` | upstream-code | [`sources/prs/sglang/PR-12758.md`](../sources/prs/sglang/PR-12758.md) | [Bugfix] Fix illegal memory access |
| `pr-sglang-12782` | upstream-code | [`sources/prs/sglang/PR-12782.md`](../sources/prs/sglang/PR-12782.md) | ignore the deepgemm check when the model weight with nvfp4 and moe ba… |
| `pr-sglang-13115` | upstream-code | [`sources/prs/sglang/PR-13115.md`](../sources/prs/sglang/PR-13115.md) | support mtp with deepseek r1 nvfp4 model |
| `pr-sglang-13162` | upstream-code | [`sources/prs/sglang/PR-13162.md`](../sources/prs/sglang/PR-13162.md) | Fix nan in global scaling factor for large scale nvfp4 EP |
| `pr-sglang-13715` | upstream-code | [`sources/prs/sglang/PR-13715.md`](../sources/prs/sglang/PR-13715.md) | Fix EPLB + FP4 Quantization Compatibility Issue |
| `pr-sglang-13761` | upstream-code | [`sources/prs/sglang/PR-13761.md`](../sources/prs/sglang/PR-13761.md) | [Feat][NVFP4] Enable NVFP4 MoE for Qwen series models (eg. Qwen3-Next) #13761 |
| `pr-sglang-13794` | upstream-code | [`sources/prs/sglang/PR-13794.md`](../sources/prs/sglang/PR-13794.md) | Support fp4 fp8 non gated moe |
| `pr-sglang-14028` | upstream-code | [`sources/prs/sglang/PR-14028.md`](../sources/prs/sglang/PR-14028.md) | Fix flashinfer cutlass MoE output shape for non-FP4-packed inputs |
| `pr-sglang-14350` | upstream-code | [`sources/prs/sglang/PR-14350.md`](../sources/prs/sglang/PR-14350.md) | [FIX] trtllm-moe-fp4-renorm for Qwen series models |
| `pr-sglang-14385` | upstream-code | [`sources/prs/sglang/PR-14385.md`](../sources/prs/sglang/PR-14385.md) | [CPU] Implement MXFP4 Gemm kernels for intel AMX to support GPT OSS series. |
| `pr-sglang-14485` | upstream-code | [`sources/prs/sglang/PR-14485.md`](../sources/prs/sglang/PR-14485.md) | Mistral Large 3 NVFP4 support |
| `pr-sglang-15049` | upstream-code | [`sources/prs/sglang/PR-15049.md`](../sources/prs/sglang/PR-15049.md) | Mistral Large 3 NVFP4 TRTLLM MoE support |
| `pr-sglang-15280` | upstream-code | [`sources/prs/sglang/PR-15280.md`](../sources/prs/sglang/PR-15280.md) | [NVIDIA] Fixes for NVFP4 all-gather with spec decoding |
| `pr-sglang-15304` | upstream-code | [`sources/prs/sglang/PR-15304.md`](../sources/prs/sglang/PR-15304.md) | Fix the accuracy issue when running mxfp4 dsv3 model and enable ep |
| `pr-sglang-15551` | upstream-code | [`sources/prs/sglang/PR-15551.md`](../sources/prs/sglang/PR-15551.md) | Update flashinfer to 0.6.1 |
| `pr-sglang-15731` | upstream-code | [`sources/prs/sglang/PR-15731.md`](../sources/prs/sglang/PR-15731.md) | [Perf] Eliminate the slice op for Flashinfer `trtllm_fp4_block_scale_moe` |
| `pr-sglang-16014` | upstream-code | [`sources/prs/sglang/PR-16014.md`](../sources/prs/sglang/PR-16014.md) | [Performance] Force split_k=1 for MXFP4 Triton kernels on Hopper |
| `pr-sglang-17158` | upstream-code | [`sources/prs/sglang/PR-17158.md`](../sources/prs/sglang/PR-17158.md) | Inclusion of nvfp4 blockscale in EPLB Rebalance |
| `pr-sglang-17300` | upstream-code | [`sources/prs/sglang/PR-17300.md`](../sources/prs/sglang/PR-17300.md) | [FIX] Always support TP > 4 for FP4 Gemm |
| `pr-sglang-17627` | upstream-code | [`sources/prs/sglang/PR-17627.md`](../sources/prs/sglang/PR-17627.md) | [feat] Support nvfp4 quantized model of Qwen3-Next |
| `pr-sglang-17816` | upstream-code | [`sources/prs/sglang/PR-17816.md`](../sources/prs/sglang/PR-17816.md) | fix(quantization): add sgl_kernel fallback for FP4 quantize on Blackwell GPUs |
| `pr-sglang-18065` | upstream-code | [`sources/prs/sglang/PR-18065.md`](../sources/prs/sglang/PR-18065.md) | [Bugfix] Fix Mistral Large 3 NVFP4 TRTLLM MoE |
| `pr-sglang-18085` | upstream-code | [`sources/prs/sglang/PR-18085.md`](../sources/prs/sglang/PR-18085.md) | Fix nvfp4 weight update |
| `pr-sglang-18370` | upstream-code | [`sources/prs/sglang/PR-18370.md`](../sources/prs/sglang/PR-18370.md) | [Kimi-K2.5] Fix NVFP4 Kimi-K2.5 weight mapping and exclude list |
| `pr-sglang-18389` | upstream-code | [`sources/prs/sglang/PR-18389.md`](../sources/prs/sglang/PR-18389.md) | Nsa trtllm mla sparse fp8 support with Deepseek v3.2 NVFP4 |
| `pr-sglang-18750` | upstream-code | [`sources/prs/sglang/PR-18750.md`](../sources/prs/sglang/PR-18750.md) | fix(sgl-kernel): use >= 120 for SM12x CUDA kernel dispatch |
| `pr-sglang-18801` | upstream-code | [`sources/prs/sglang/PR-18801.md`](../sources/prs/sglang/PR-18801.md) | Support CuteDSL `mm_fp4` backend |
| `pr-sglang-18858` | upstream-code | [`sources/prs/sglang/PR-18858.md`](../sources/prs/sglang/PR-18858.md) | [Perf] ~9.5x faster Blackwell MXFP4 MoE weight loading |
| `pr-sglang-19143` | upstream-code | [`sources/prs/sglang/PR-19143.md`](../sources/prs/sglang/PR-19143.md) | feat: Support MXFP4 quantized dense models on AMD CDNA2/CDNA3 GPUs |
| `pr-sglang-19174` | upstream-code | [`sources/prs/sglang/PR-19174.md`](../sources/prs/sglang/PR-19174.md) | Adjust padding size to improve triton_kernels moe performance |
| `pr-sglang-19425` | upstream-code | [`sources/prs/sglang/PR-19425.md`](../sources/prs/sglang/PR-19425.md) | [AMD] Fix weight load shape mismatch for amd dsr1 0528 mxfp4 |
| `pr-sglang-19437` | upstream-code | [`sources/prs/sglang/PR-19437.md`](../sources/prs/sglang/PR-19437.md) | [Kernel Slimming] Migrate NVFP4 kernels to JIT |
| `pr-sglang-19652` | upstream-code | [`sources/prs/sglang/PR-19652.md`](../sources/prs/sglang/PR-19652.md) | [Feature] NVFP4 Marlin fallback for non-Blackwell GPUs (SM75+) |
| `pr-sglang-19718` | upstream-code | [`sources/prs/sglang/PR-19718.md`](../sources/prs/sglang/PR-19718.md) | Support `triton_kernels` for GPT-OSS on SM120 |
| `pr-sglang-19935` | upstream-code | [`sources/prs/sglang/PR-19935.md`](../sources/prs/sglang/PR-19935.md) | [AMD] Fix FP8 assertion failure in aiter MLA decode by falling back to self.k_scale |
| `pr-sglang-20012` | upstream-code | [`sources/prs/sglang/PR-20012.md`](../sources/prs/sglang/PR-20012.md) | [JIT Kernel] Reland NVFP4 kernels to JIT |
| `pr-sglang-20040` | upstream-code | [`sources/prs/sglang/PR-20040.md`](../sources/prs/sglang/PR-20040.md) | Fix SM120 `triton_kernels` MXFP4 `block_k` for GPT-OSS |
| `pr-sglang-20047` | upstream-code | [`sources/prs/sglang/PR-20047.md`](../sources/prs/sglang/PR-20047.md) | fix: default FP4 GEMM backend to flashinfer_cudnn on SM120 (Blackwell) |
| `pr-sglang-20137` | upstream-code | [`sources/prs/sglang/PR-20137.md`](../sources/prs/sglang/PR-20137.md) | [diffusion] Support nvfp4 for Flux.2 |
| `pr-sglang-20268` | upstream-code | [`sources/prs/sglang/PR-20268.md`](../sources/prs/sglang/PR-20268.md) | [4/n jit_kernel restruct] speed up CI tests and add benchmark workflow |
| `pr-sglang-20305` | upstream-code | [`sources/prs/sglang/PR-20305.md`](../sources/prs/sglang/PR-20305.md) | [Benchmark] use flashinfer bench_gpu_time instead of triton do_bench |
| `pr-sglang-20407` | upstream-code | [`sources/prs/sglang/PR-20407.md`](../sources/prs/sglang/PR-20407.md) | [Model] Support Nemotron 3 Super NVFP4 |
| `pr-sglang-20874` | upstream-code | [`sources/prs/sglang/PR-20874.md`](../sources/prs/sglang/PR-20874.md) | [JIT Kernel] Fix NVFP4 multi-arch compilation failure |
| `pr-sglang-20910` | upstream-code | [`sources/prs/sglang/PR-20910.md`](../sources/prs/sglang/PR-20910.md) | Add SGLang CUDA crash API logging inspired by FlashInfer |
| `pr-sglang-21022` | upstream-code | [`sources/prs/sglang/PR-21022.md`](../sources/prs/sglang/PR-21022.md) | [Chore] Clean up JIT compilation flags |
| `pr-sglang-21213` | upstream-code | [`sources/prs/sglang/PR-21213.md`](../sources/prs/sglang/PR-21213.md) | [AMD]: Support MLA with nhead<16 and FP8 KV cache for TP=8 (Kimi K2.5… |
| `pr-sglang-21239` | upstream-code | [`sources/prs/sglang/PR-21239.md`](../sources/prs/sglang/PR-21239.md) | Refactor JIT kernel CI to use run_suite.py registration system |
| `pr-sglang-21240` | upstream-code | [`sources/prs/sglang/PR-21240.md`](../sources/prs/sglang/PR-21240.md) | [NVIDIA] Enable FP4 flashinfer trtllm routed moe |
| `pr-sglang-21314` | upstream-code | [`sources/prs/sglang/PR-21314.md`](../sources/prs/sglang/PR-21314.md) | CUTLASS NVFP4 GEMM improvement of SM120 |
| `pr-sglang-21321` | upstream-code | [`sources/prs/sglang/PR-21321.md`](../sources/prs/sglang/PR-21321.md) | [Kernel] Support FlashInfer TRTLLM-Gen fused MoE for non-gated FP4 & FP8 (Nemotron) |
| `pr-sglang-21325` | upstream-code | [`sources/prs/sglang/PR-21325.md`](../sources/prs/sglang/PR-21325.md) | [misc] clean up kernel API |
| `pr-sglang-21339` | upstream-code | [`sources/prs/sglang/PR-21339.md`](../sources/prs/sglang/PR-21339.md) | Add dedicated FlashInferCuteDslMoE layer for standard-path FP4 MoE |
| `pr-sglang-21463` | upstream-code | [`sources/prs/sglang/PR-21463.md`](../sources/prs/sglang/PR-21463.md) | Migrate all callers from /get_server_info to /server_info |
| `pr-sglang-21776` | upstream-code | [`sources/prs/sglang/PR-21776.md`](../sources/prs/sglang/PR-21776.md) | Harden FlashInfer FP4 imports in standard dispatcher |
| `pr-sglang-22064` | upstream-code | [`sources/prs/sglang/PR-22064.md`](../sources/prs/sglang/PR-22064.md) | [Diffusion] Fix weight scale swizzle and add large-M kernel config for FLUX.2-dev-NVFP4 |
| `pr-sglang-22079` | upstream-code | [`sources/prs/sglang/PR-22079.md`](../sources/prs/sglang/PR-22079.md) | [nvidia] Gemma4 nvfp4 fix |
| `pr-sglang-22091` | upstream-code | [`sources/prs/sglang/PR-22091.md`](../sources/prs/sglang/PR-22091.md) | [diffusion] Default NVFP4 to CUTLASS and add all-model shape benchmarks |
| `pr-sglang-22127` | upstream-code | [`sources/prs/sglang/PR-22127.md`](../sources/prs/sglang/PR-22127.md) | [Diffusion] Add diffusion NVFP4 scaled-mm correctness test |
| `pr-sglang-22204` | upstream-code | [`sources/prs/sglang/PR-22204.md`](../sources/prs/sglang/PR-22204.md) | [RL] Refactor NVFP4 shuffling/swizzling to in-place replacement |
| `pr-sglang-22574` | upstream-code | [`sources/prs/sglang/PR-22574.md`](../sources/prs/sglang/PR-22574.md) | [Diffusion] Add FLUX.1-dev ModelOpt NVFP4 support |
| `pr-sglang-22672` | upstream-code | [`sources/prs/sglang/PR-22672.md`](../sources/prs/sglang/PR-22672.md) | reland [Diffusion] Add FLUX.1-dev ModelOpt NVFP4 support |
| `pr-sglang-22681` | upstream-code | [`sources/prs/sglang/PR-22681.md`](../sources/prs/sglang/PR-22681.md) | [Diffusion] Add Wan2.2 ModelOpt NVFP4 support |
| `pr-sglang-22717` | upstream-code | [`sources/prs/sglang/PR-22717.md`](../sources/prs/sglang/PR-22717.md) | [codex] Add flashinfer TRTLLM backend for diffusion NVFP4 |
| `pr-sglang-23590` | upstream-code | [`sources/prs/sglang/PR-23590.md`](../sources/prs/sglang/PR-23590.md) | Reland Cute-DSL FP4 dense GEMM |
| `pr-sglang-23686` | upstream-code | [`sources/prs/sglang/PR-23686.md`](../sources/prs/sglang/PR-23686.md) | Deepseek_v4 support w4(mxfp4)a16 on hopper |
| `pr-sglang-23745` | upstream-code | [`sources/prs/sglang/PR-23745.md`](../sources/prs/sglang/PR-23745.md) | Use Cute-DSL NVFP4 quantization kernels |
| `pr-sglang-24490` | upstream-code | [`sources/prs/sglang/PR-24490.md`](../sources/prs/sglang/PR-24490.md) | Port MXFP4 Marlin MoE support to JIT kernel path |
| `pr-sglang-24816` | upstream-code | [`sources/prs/sglang/PR-24816.md`](../sources/prs/sglang/PR-24816.md) | Add FlashInfer SM90 cutlass MXFP4 MoE backend (W4A16) for GPT-OSS + DeepSeek-V4 |
| `pr-sglang-24986` | upstream-code | [`sources/prs/sglang/PR-24986.md`](../sources/prs/sglang/PR-24986.md) | [rebase]Deepseek_v4 support w4(mxfp4)a16 on hopper |
| `pr-sglang-25107` | upstream-code | [`sources/prs/sglang/PR-25107.md`](../sources/prs/sglang/PR-25107.md) | perf(nvfp4): free unused source scales after weight processing |
| `pr-sglang-3899` | upstream-code | [`sources/prs/sglang/PR-3899.md`](../sources/prs/sglang/PR-3899.md) | Support FP4 gemm (1/2) |
| `pr-sglang-4953` | upstream-code | [`sources/prs/sglang/PR-4953.md`](../sources/prs/sglang/PR-4953.md) | [Build] Fix cuda12.8 build error in nvfp4_scaled_mm_kernels.cu |
| `pr-sglang-6093` | upstream-code | [`sources/prs/sglang/PR-6093.md`](../sources/prs/sglang/PR-6093.md) | [1/2] Add Kernel support for Cutlass based Fused FP4 MoE |
| `pr-sglang-6853` | upstream-code | [`sources/prs/sglang/PR-6853.md`](../sources/prs/sglang/PR-6853.md) | [DeepseekR1-FP4] Add Support for nvidia/DeepSeekR1-FP4 model |
| `pr-sglang-7302` | upstream-code | [`sources/prs/sglang/PR-7302.md`](../sources/prs/sglang/PR-7302.md) | Support NVFP4 quantized dense models on AMD CDNA2/CDNA3 GPUs |
| `pr-sglang-7327` | upstream-code | [`sources/prs/sglang/PR-7327.md`](../sources/prs/sglang/PR-7327.md) | FlashInfer NVFP4 MoE with EP & 2-stream shared expert |
| `pr-sglang-7376` | upstream-code | [`sources/prs/sglang/PR-7376.md`](../sources/prs/sglang/PR-7376.md) | Fix MTP with Deepseek R1 Fp4 |
| `pr-sglang-7627` | upstream-code | [`sources/prs/sglang/PR-7627.md`](../sources/prs/sglang/PR-7627.md) | Add dsv3 router gemm kernel |
| `pr-sglang-7667` | upstream-code | [`sources/prs/sglang/PR-7667.md`](../sources/prs/sglang/PR-7667.md) | Add fp4 quantize before all-gather for Flashinfer cutlass MoE DP (max throughput) |
| `pr-sglang-7912` | upstream-code | [`sources/prs/sglang/PR-7912.md`](../sources/prs/sglang/PR-7912.md) | Qwen FP8/NVFP4 ModelOPT Quantization support |
| `pr-sglang-8127` | upstream-code | [`sources/prs/sglang/PR-8127.md`](../sources/prs/sglang/PR-8127.md) | [Fix][Ready]Fix register spilling in cutlass nvfp4 gemm kernel on Blackwell |
| `pr-sglang-8195` | upstream-code | [`sources/prs/sglang/PR-8195.md`](../sources/prs/sglang/PR-8195.md) | [fix] fix modelopt fp4 on b200 |
| `pr-sglang-8552` | upstream-code | [`sources/prs/sglang/PR-8552.md`](../sources/prs/sglang/PR-8552.md) | [NVIDIA] Add Low Latency NVFP4 decode kernels from Flashinfer |
| `pr-sglang-8898` | upstream-code | [`sources/prs/sglang/PR-8898.md`](../sources/prs/sglang/PR-8898.md) | [Perf] Auto enable best flashinfer mxfp4  kernel in b200 |
| `pr-sglang-8908` | upstream-code | [`sources/prs/sglang/PR-8908.md`](../sources/prs/sglang/PR-8908.md) | Fix hopper launch gpt-oss model illegal memory |
| `pr-sglang-9162` | upstream-code | [`sources/prs/sglang/PR-9162.md`](../sources/prs/sglang/PR-9162.md) | Faster weight processing (trtllm-gen moe nvfp4) |
| `pr-sglang-9199` | upstream-code | [`sources/prs/sglang/PR-9199.md`](../sources/prs/sglang/PR-9199.md) | [NVIDIA] [3/N] Nvfp4 Masked Gemm: Add flashinfer grouped_gemm_nt_masked  |
| `pr-sglang-9200` | upstream-code | [`sources/prs/sglang/PR-9200.md`](../sources/prs/sglang/PR-9200.md) | [NVIDA] [1/N] Nvfp4 Masked Gemm: Add quant op for the flashinfer grouped gemm |
| `pr-sglang-9346` | upstream-code | [`sources/prs/sglang/PR-9346.md`](../sources/prs/sglang/PR-9346.md) | Fix FP4 inference corruption issue in glm4.5-air model |
| `pr-sglang-9473` | upstream-code | [`sources/prs/sglang/PR-9473.md`](../sources/prs/sglang/PR-9473.md) | [fix] Fix mxfp4 triton MoE tp bug |
| `pr-sglang-9556` | upstream-code | [`sources/prs/sglang/PR-9556.md`](../sources/prs/sglang/PR-9556.md) | [NVIDIA] [2/N] Optimize `silu_and_mul_scaled_fp4_grouped_quant` perf |
| `pr-sglang-9679` | upstream-code | [`sources/prs/sglang/PR-9679.md`](../sources/prs/sglang/PR-9679.md) | move is_sm90_supported/is_sm100_supported to python/sglang/srt/utils.py |
| `pr-sglang-9712` | upstream-code | [`sources/prs/sglang/PR-9712.md`](../sources/prs/sglang/PR-9712.md) | [ModelOpt] Fix Weight Loading for DSR1-FP4 Quantization |
| `pr-sglang-9807` | upstream-code | [`sources/prs/sglang/PR-9807.md`](../sources/prs/sglang/PR-9807.md) | Make fp4_quantize kernels work on sm103 |
| `pr-tensorrt-llm-10339` | upstream-code | [`sources/prs/tensorrt-llm/PR-10339.md`](../sources/prs/tensorrt-llm/PR-10339.md) | [TRTLLM-9661][chore] Further reduce tuning time for cuteDSL nvFP4 dense gemm. |
| `pr-tensorrt-llm-10479` | upstream-code | [`sources/prs/tensorrt-llm/PR-10479.md`](../sources/prs/tensorrt-llm/PR-10479.md) | [None] [feat] Add densegemm backend for MoE |
| `pr-tensorrt-llm-11143` | upstream-code | [`sources/prs/tensorrt-llm/PR-11143.md`](../sources/prs/tensorrt-llm/PR-11143.md) | [None][feat] fuse shared to sparse experts in TRT-LLM Gen MoE |
| `pr-tensorrt-llm-11165` | upstream-code | [`sources/prs/tensorrt-llm/PR-11165.md`](../sources/prs/tensorrt-llm/PR-11165.md) | [https://nvbugs/5799917][fix] Recover from CUTLASS MoE doActivation perf regression for MXFP4/NVFP4 dtype |
| `pr-tensorrt-llm-11273` | upstream-code | [`sources/prs/tensorrt-llm/PR-11273.md`](../sources/prs/tensorrt-llm/PR-11273.md) | [None][feat] Optimize super-v3 nvfp4 for better perf |
| `pr-tensorrt-llm-11473` | upstream-code | [`sources/prs/tensorrt-llm/PR-11473.md`](../sources/prs/tensorrt-llm/PR-11473.md) | [None][feat] Optimize by fuse nvfp4_quant to layernorm_gated for mamba2_mixer |
| `pr-tensorrt-llm-11589` | upstream-code | [`sources/prs/tensorrt-llm/PR-11589.md`](../sources/prs/tensorrt-llm/PR-11589.md) | [TRTLLM-10004][feat] Enable GEMM -> AR with GEMM output in registered buffers |
| `pr-tensorrt-llm-11652` | upstream-code | [`sources/prs/tensorrt-llm/PR-11652.md`](../sources/prs/tensorrt-llm/PR-11652.md) | [None][feat] NVFP4 TRTLLM-Gen MoE for AutoDeploy (Nemotron Super) |
| `pr-tensorrt-llm-11733` | upstream-code | [`sources/prs/tensorrt-llm/PR-11733.md`](../sources/prs/tensorrt-llm/PR-11733.md) | [https://nvbugs/5799917][fix] Recover from CUTLASS MoE doActivation perf regression for MXFP4/NVFP4 dtype |
| `pr-tensorrt-llm-11774` | upstream-code | [`sources/prs/tensorrt-llm/PR-11774.md`](../sources/prs/tensorrt-llm/PR-11774.md) | [None][fix] Fix SM120 issue for rms_norm with nvfp4_quant_fusion |
| `pr-tensorrt-llm-11897` | upstream-code | [`sources/prs/tensorrt-llm/PR-11897.md`](../sources/prs/tensorrt-llm/PR-11897.md) | [TRTLLM-10990][feat] Fuse SwiGLU and quant into shared expert |
| `pr-tensorrt-llm-12320` | upstream-code | [`sources/prs/tensorrt-llm/PR-12320.md`](../sources/prs/tensorrt-llm/PR-12320.md) | [None][feat] Support update weight for nvfp4 |
| `pr-tensorrt-llm-12322` | upstream-code | [`sources/prs/tensorrt-llm/PR-12322.md`](../sources/prs/tensorrt-llm/PR-12322.md) | [https://nvbugs/5983390][perf] Kernel fusions in _gather_k_cache_for_chunk of Indexer in DSA |
| `pr-tensorrt-llm-12666` | upstream-code | [`sources/prs/tensorrt-llm/PR-12666.md`](../sources/prs/tensorrt-llm/PR-12666.md) | [https://nvbugs/5836828][fix] Fix GPTOSS CUTLASS MOE on Hopper nvlink one-sided workspace overflow |
| `pr-tensorrt-llm-12866` | upstream-code | [`sources/prs/tensorrt-llm/PR-12866.md`](../sources/prs/tensorrt-llm/PR-12866.md) | [None][feat] AutoDeploy: Onboard google/gemma-4-31B-it dense model, including nvfp4 |
| `pr-tensorrt-llm-13033` | upstream-code | [`sources/prs/tensorrt-llm/PR-13033.md`](../sources/prs/tensorrt-llm/PR-13033.md) | [None][feat] Update rms_norm + fp4_qaunt kernel supporting more dim |
| `pr-tensorrt-llm-13117` | upstream-code | [`sources/prs/tensorrt-llm/PR-13117.md`](../sources/prs/tensorrt-llm/PR-13117.md) | [None][feat] Add FP4 residual quantization kernel without channel reo… |
| `pr-tensorrt-llm-13142` | upstream-code | [`sources/prs/tensorrt-llm/PR-13142.md`](../sources/prs/tensorrt-llm/PR-13142.md) | [https://nvbugs/5844149][fix] Fix issues with DSV3.2 perf tests |
| `pr-tensorrt-llm-13149` | upstream-code | [`sources/prs/tensorrt-llm/PR-13149.md`](../sources/prs/tensorrt-llm/PR-13149.md) | [TRTLLM-11958][perf] reduce @torch.library.custom_op host overhead |
| `pr-tensorrt-llm-13176` | upstream-code | [`sources/prs/tensorrt-llm/PR-13176.md`](../sources/prs/tensorrt-llm/PR-13176.md) | [https://nvbugs/6088149][chore] Unwaive perf sanity tests for bug 6088149 |
| `pr-tensorrt-llm-13268` | upstream-code | [`sources/prs/tensorrt-llm/PR-13268.md`](../sources/prs/tensorrt-llm/PR-13268.md) | [https://nvbugs/6095953][fix] Fix cache memory estimation for Qwen3 hybrid models in trtllm-bench |
| `pr-tensorrt-llm-13340` | upstream-code | [`sources/prs/tensorrt-llm/PR-13340.md`](../sources/prs/tensorrt-llm/PR-13340.md) | [None][feat] Integrate FP4 indexer for DSA on Blackwell |
| `pr-tensorrt-llm-13384` | upstream-code | [`sources/prs/tensorrt-llm/PR-13384.md`](../sources/prs/tensorrt-llm/PR-13384.md) | [None][feat] Add MegaMoEDeepGemmFusedMoE backend wrapping DeepGEMM fp8_fp4_mega_moe |
| `pr-tensorrt-llm-13433` | upstream-code | [`sources/prs/tensorrt-llm/PR-13433.md`](../sources/prs/tensorrt-llm/PR-13433.md) | [None][perf] Extend customMoeRouting kernel to support Qwen3.5 |
| `pr-tensorrt-llm-13496` | upstream-code | [`sources/prs/tensorrt-llm/PR-13496.md`](../sources/prs/tensorrt-llm/PR-13496.md) | [https://nvbugs/6114727][fix] Unwaive deepseek r1 fp4 v2 grace_blackwell r1 fp4 v2 tep4 mtp3 1k1k |
| `pr-tensorrt-llm-13505` | upstream-code | [`sources/prs/tensorrt-llm/PR-13505.md`](../sources/prs/tensorrt-llm/PR-13505.md) | [None][perf] Drop cubin and Eliminate ~6s FMHA JIT recompile in eager generation by aligning kernel selection with CUDA graph warmup |
| `pr-tensorrt-llm-13570` | upstream-code | [`sources/prs/tensorrt-llm/PR-13570.md`](../sources/prs/tensorrt-llm/PR-13570.md) | [TRTLLM-12128][feat] enable SageAttention for Wan/FLUX (new commits) |
| `pr-tensorrt-llm-13595` | upstream-code | [`sources/prs/tensorrt-llm/PR-13595.md`](../sources/prs/tensorrt-llm/PR-13595.md) | [None][feat] Enable EPLB for DeepSeek-V4 |
| `pr-tensorrt-llm-13658` | upstream-code | [`sources/prs/tensorrt-llm/PR-13658.md`](../sources/prs/tensorrt-llm/PR-13658.md) | [None][test] add Nemotron Ultra V3 AutoDeploy accuracy test |
| `pr-tensorrt-llm-13667` | upstream-code | [`sources/prs/tensorrt-llm/PR-13667.md`](../sources/prs/tensorrt-llm/PR-13667.md) | [None][perf] Improve TRTLLM MoE autotune in DEP |
| `pr-tensorrt-llm-13708` | upstream-code | [`sources/prs/tensorrt-llm/PR-13708.md`](../sources/prs/tensorrt-llm/PR-13708.md) | [https://nvbugs/6094072][fix] swizzle GPT-OSS dummy MXFP4 weights |
| `pr-tensorrt-llm-13837` | upstream-code | [`sources/prs/tensorrt-llm/PR-13837.md`](../sources/prs/tensorrt-llm/PR-13837.md) | [None][test] Add func and perf case of nemotron-3-Nano-Omni model on DGX-Spark |
| `pr-tensorrt-llm-13873` | upstream-code | [`sources/prs/tensorrt-llm/PR-13873.md`](../sources/prs/tensorrt-llm/PR-13873.md) | [TRTLLM-12503][feat] Parallel VAE independent scaling and fix arg passing |
| `pr-tensorrt-llm-13908` | upstream-code | [`sources/prs/tensorrt-llm/PR-13908.md`](../sources/prs/tensorrt-llm/PR-13908.md) | [None][refactor] MoEScheduler split + MegaMoE EPLB / multi-chunk / CI integration |
| `pr-tensorrt-llm-13929` | upstream-code | [`sources/prs/tensorrt-llm/PR-13929.md`](../sources/prs/tensorrt-llm/PR-13929.md) | [TRTLLM-35237][feat] Add cute dsl FP4 paged MQA logits decode kernel |
| `pr-tensorrt-llm-13971` | upstream-code | [`sources/prs/tensorrt-llm/PR-13971.md`](../sources/prs/tensorrt-llm/PR-13971.md) | [None][perf] Follow-up patch for "Improve TRTLLM MoE autotune in DEP (#13667)" |
| `pr-tensorrt-llm-13997` | upstream-code | [`sources/prs/tensorrt-llm/PR-13997.md`](../sources/prs/tensorrt-llm/PR-13997.md) | [None][feat] enable TRTLLM-Gen internal routing |
| `pr-tensorrt-llm-14004` | upstream-code | [`sources/prs/tensorrt-llm/PR-14004.md`](../sources/prs/tensorrt-llm/PR-14004.md) | [None][feat] AutoDeploy re-onboard GPT_OSS |
| `pr-tensorrt-llm-14054` | upstream-code | [`sources/prs/tensorrt-llm/PR-14054.md`](../sources/prs/tensorrt-llm/PR-14054.md) | [https://nvbugs/6162323][fix] Make mxfp4 H20 swizzle WAR more robust |
| `pr-tensorrt-llm-14106` | upstream-code | [`sources/prs/tensorrt-llm/PR-14106.md`](../sources/prs/tensorrt-llm/PR-14106.md) | [None][fix] Add SPDX Apache-2.0 headers and fix license compliance for llm-c standalone repo |
| `pr-tensorrt-llm-4867` | upstream-code | [`sources/prs/tensorrt-llm/PR-4867.md`](../sources/prs/tensorrt-llm/PR-4867.md) | feat: Add w4a8_mxfp4_fp8 quantization recipe. |
| `pr-tensorrt-llm-6809` | upstream-code | [`sources/prs/tensorrt-llm/PR-6809.md`](../sources/prs/tensorrt-llm/PR-6809.md) | [OMNIML-2336][feat] Add NVFP4 x FP8 |
| `pr-tensorrt-llm-7524` | upstream-code | [`sources/prs/tensorrt-llm/PR-7524.md`](../sources/prs/tensorrt-llm/PR-7524.md) | [None][chore] Fix kernel launch param and add TRTLLM MoE backend test |
| `pr-tensorrt-llm-7761` | upstream-code | [`sources/prs/tensorrt-llm/PR-7761.md`](../sources/prs/tensorrt-llm/PR-7761.md) | [TRTLLM-8637][feat] Optimize the routing kernel for DeepseekV3 (MoE CUTLASS backend); Add support for 384 experts (MoE TRTLLM backend) |
| `pr-tensorrt-llm-7937` | upstream-code | [`sources/prs/tensorrt-llm/PR-7937.md`](../sources/prs/tensorrt-llm/PR-7937.md) | [None][feat] GPT-OSS Sm120/Sm121 Support |
| `pr-tensorrt-llm-8405` | upstream-code | [`sources/prs/tensorrt-llm/PR-8405.md`](../sources/prs/tensorrt-llm/PR-8405.md) | [TRTLLM-8535][feat] Support DeepSeek V3.2 with FP8 + BF16 KV cache/NVFP4 + BF16 KV cache |
| `pr-tensorrt-llm-8620` | upstream-code | [`sources/prs/tensorrt-llm/PR-8620.md`](../sources/prs/tensorrt-llm/PR-8620.md) | [None][feat] Enable nvfp4 cuda core for sm120 |
| `pr-tensorrt-llm-9025` | upstream-code | [`sources/prs/tensorrt-llm/PR-9025.md`](../sources/prs/tensorrt-llm/PR-9025.md) | [None][feat] Update TRTLLM MoE cubins; reduce mxfp4 weight padding requirement; tighten TMA bound |
| `pr-tensorrt-llm-9618` | upstream-code | [`sources/prs/tensorrt-llm/PR-9618.md`](../sources/prs/tensorrt-llm/PR-9618.md) | [TRTLLM-9685] [feat] Add gather fc1 kernel by cuteDSL |
| `pr-tensorrt-llm-9729` | upstream-code | [`sources/prs/tensorrt-llm/PR-9729.md`](../sources/prs/tensorrt-llm/PR-9729.md) | [None][feat] add fp4 gemm + allreduce |
| `pr-tensorrt-llm-9854` | upstream-code | [`sources/prs/tensorrt-llm/PR-9854.md`](../sources/prs/tensorrt-llm/PR-9854.md) | [None][feat] Port fp4 quantization kernel optimization from FlashInfer |
| `pr-tensorrt-llm-9905` | upstream-code | [`sources/prs/tensorrt-llm/PR-9905.md`](../sources/prs/tensorrt-llm/PR-9905.md) | [None][feat] Adding torch ext API for FusedAddRMSNormQuant kernel |
| `pr-tilelang-1722` | upstream-code | [`sources/prs/tilelang/PR-1722.md`](../sources/prs/tilelang/PR-1722.md) | [Refactor] re-implement vector subtype and its access method |
| `pr-tilelang-1724` | upstream-code | [`sources/prs/tilelang/PR-1724.md`](../sources/prs/tilelang/PR-1724.md) | [Enhancement] Legalize subtype access |
| `pr-tilelang-1726` | upstream-code | [`sources/prs/tilelang/PR-1726.md`](../sources/prs/tilelang/PR-1726.md) | [Bugfix] Fix incorrect alignment of vectorized subtype |
| `pr-tilelang-1741` | upstream-code | [`sources/prs/tilelang/PR-1741.md`](../sources/prs/tilelang/PR-1741.md) | [BugFix] Fix FP4 related vectorized cast |
| `pr-tilelang-1845` | upstream-code | [`sources/prs/tilelang/PR-1845.md`](../sources/prs/tilelang/PR-1845.md) | [Enhancement] Optimize templates for half/bfloat16 |
| `pr-tilelang-1880` | upstream-code | [`sources/prs/tilelang/PR-1880.md`](../sources/prs/tilelang/PR-1880.md) | Avoid cvt instruction in FP4 before cuda 13.0 |
| `pr-tilelang-1887` | upstream-code | [`sources/prs/tilelang/PR-1887.md`](../sources/prs/tilelang/PR-1887.md) | [Refactor] Improve cp.async lowering and add async_copy op |
| `pr-tilelang-1909` | upstream-code | [`sources/prs/tilelang/PR-1909.md`](../sources/prs/tilelang/PR-1909.md) | [Feature] Add Producer-Consumer Warp Specialization and T.tma_copy() API |
| `pr-tilelang-1932` | upstream-code | [`sources/prs/tilelang/PR-1932.md`](../sources/prs/tilelang/PR-1932.md) | test: reduce CI runtime for slow Python suites |
| `pr-tilelang-1937` | upstream-code | [`sources/prs/tilelang/PR-1937.md`](../sources/prs/tilelang/PR-1937.md) | Fix predicated cp.async pipeline scheduling |
| `pr-tilelang-1947` | upstream-code | [`sources/prs/tilelang/PR-1947.md`](../sources/prs/tilelang/PR-1947.md) | Support packed subtype views during layout reshape |
| `pr-tilelang-1950` | upstream-code | [`sources/prs/tilelang/PR-1950.md`](../sources/prs/tilelang/PR-1950.md) | [Enhancement] Use stronger prover in `ProveFragmentContains` to avoid false layout conflicts |
| `pr-tilelang-1953` | upstream-code | [`sources/prs/tilelang/PR-1953.md`](../sources/prs/tilelang/PR-1953.md) | [PIpeline] Enable software pipelining when warp specialization is unavailable |
| `pr-tilelang-1975` | upstream-code | [`sources/prs/tilelang/PR-1975.md`](../sources/prs/tilelang/PR-1975.md) | Fix wrapped pre-loop TMA prefixes in producer-consumer WS |
| `pr-tilelang-2001` | upstream-code | [`sources/prs/tilelang/PR-2001.md`](../sources/prs/tilelang/PR-2001.md) | [Refactor] Refactor CUDA atomic helpers |
| `pr-tilelang-2002` | upstream-code | [`sources/prs/tilelang/PR-2002.md`](../sources/prs/tilelang/PR-2002.md) | [Refactor][Pipeline] Run pipeline rewriting before layout inference and stabilize tiled WS |
| `pr-tilelang-2004` | upstream-code | [`sources/prs/tilelang/PR-2004.md`](../sources/prs/tilelang/PR-2004.md) | fix: fix copy+cast vectorize loop to use wider vector load/store instrcution |
| `pr-tilelang-2013` | upstream-code | [`sources/prs/tilelang/PR-2013.md`](../sources/prs/tilelang/PR-2013.md) | [CI] Remove legacy dequantize gemm test |
| `pr-tilelang-2023` | upstream-code | [`sources/prs/tilelang/PR-2023.md`](../sources/prs/tilelang/PR-2023.md) | [Codegen] Add lexical_alloc_scope for scoped local variable lifetime |
| `pr-tilelang-2024` | upstream-code | [`sources/prs/tilelang/PR-2024.md`](../sources/prs/tilelang/PR-2024.md) | Re-enable deprecated `TL_DISABLE_TMA_LOWER` pass config for TMA store |
| `pr-tilelang-2026` | upstream-code | [`sources/prs/tilelang/PR-2026.md`](../sources/prs/tilelang/PR-2026.md) | [Refactor] Refactor `DecoupleTypeCast` Pass |
| `pr-tilelang-2037` | upstream-code | [`sources/prs/tilelang/PR-2037.md`](../sources/prs/tilelang/PR-2037.md) | [Bugfix][Subtype] Fix scalar fp4 store/load codegen for non-packed buffers |
| `pr-tilelang-2046` | upstream-code | [`sources/prs/tilelang/PR-2046.md`](../sources/prs/tilelang/PR-2046.md) | [Refactor] Remove obsolete RewriteWgmmaSync pass |
| `pr-tilelang-2047` | upstream-code | [`sources/prs/tilelang/PR-2047.md`](../sources/prs/tilelang/PR-2047.md) | [Refactor] Move target gating into InjectFenceProxy pass entry |
| `pr-tilelang-2052` | upstream-code | [`sources/prs/tilelang/PR-2052.md`](../sources/prs/tilelang/PR-2052.md) | [Bugfix] Use shared::cta instead of shared::cluster for non-cluster T… |
| `pr-tilelang-2055` | upstream-code | [`sources/prs/tilelang/PR-2055.md`](../sources/prs/tilelang/PR-2055.md) | [BugFix] Keep shared-prelude local vars in producer-consumer WS |
| `pr-tilelang-2063` | upstream-code | [`sources/prs/tilelang/PR-2063.md`](../sources/prs/tilelang/PR-2063.md) | [CUDA] Support int4 `T.gemm` |
| `pr-tilelang-2088` | upstream-code | [`sources/prs/tilelang/PR-2088.md`](../sources/prs/tilelang/PR-2088.md) | [Refactor] Refactor register annotation lowering |
| `pr-tilelang-2092` | upstream-code | [`sources/prs/tilelang/PR-2092.md`](../sources/prs/tilelang/PR-2092.md) | [BugFix] Relax loop wait and adjust trailing drain behavior in async pipeline tests |
| `pr-tilelang-2102` | upstream-code | [`sources/prs/tilelang/PR-2102.md`](../sources/prs/tilelang/PR-2102.md) | [CUDA][SM100] Include cuda_fp6.h when emitting FP6 types |
| `pr-tilelang-2107` | upstream-code | [`sources/prs/tilelang/PR-2107.md`](../sources/prs/tilelang/PR-2107.md) | [TMA] Support FP4 TensorMap TMA copies |
| `pr-tilelang-2126` | upstream-code | [`sources/prs/tilelang/PR-2126.md`](../sources/prs/tilelang/PR-2126.md) | [Feature][Fix] Extend TCGEN5 F8F6F4 dtype plumbing |
| `pr-tilelang-2148` | upstream-code | [`sources/prs/tilelang/PR-2148.md`](../sources/prs/tilelang/PR-2148.md) | [Examples] Add examples for operators in DeepSeek-V4 |
| `pr-tilelang-2166` | upstream-code | [`sources/prs/tilelang/PR-2166.md`](../sources/prs/tilelang/PR-2166.md) | [BugFix] Consider non-local store in external call and SIMT producer for warp specialize |
| `pr-tilelang-2187` | upstream-code | [`sources/prs/tilelang/PR-2187.md`](../sources/prs/tilelang/PR-2187.md) | [WIP] Handle CuTeDSL FP4 torch dtype |
| `pr-triton-10151` | upstream-code | [`sources/prs/triton/PR-10151.md`](../sources/prs/triton/PR-10151.md) | [Tutorials] Fix unbound local variable in Tutorial 10 |
| `pr-triton-10163` | upstream-code | [`sources/prs/triton/PR-10163.md`](../sources/prs/triton/PR-10163.md) | [BACKEND] Enable i16 descriptor gather/scatter indices on NVIDIA |
| `pr-triton-10190` | upstream-code | [`sources/prs/triton/PR-10190.md`](../sources/prs/triton/PR-10190.md) | [mxfp4] Fix Hopper scale padding mask |
| `pr-triton-10196` | upstream-code | [`sources/prs/triton/PR-10196.md`](../sources/prs/triton/PR-10196.md) | [MULTICTA] Fix multicast pattern for tcgen05_mma_scaled |
| `pr-triton-10214` | upstream-code | [`sources/prs/triton/PR-10214.md`](../sources/prs/triton/PR-10214.md) | Allow MXFP8 LHS with Hopper-swizzled MXFP4 RHS |
| `pr-triton-10222` | upstream-code | [`sources/prs/triton/PR-10222.md`](../sources/prs/triton/PR-10222.md) | [AMD][gfx1250] Add transposed support for 32x16 scaled WMMA |
| `pr-triton-10249` | upstream-code | [`sources/prs/triton/PR-10249.md`](../sources/prs/triton/PR-10249.md) | [triton_kernels] nvfp4 x nvfp4 tuning |
| `pr-triton-10275` | upstream-code | [`sources/prs/triton/PR-10275.md`](../sources/prs/triton/PR-10275.md) | Support zero-sized Hopper MX scale layouts |
| `pr-triton-10318` | upstream-code | [`sources/prs/triton/PR-10318.md`](../sources/prs/triton/PR-10318.md) | Support MN-packing in decomposed fp4 dot_scaled |
| `pr-vllm-12784` | upstream-code | [`sources/prs/vllm/PR-12784.md`](../sources/prs/vllm/PR-12784.md) | [NVIDIA] Support nvfp4 quantization |
| `pr-vllm-13571` | upstream-code | [`sources/prs/vllm/PR-13571.md`](../sources/prs/vllm/PR-13571.md) | [NVIDIA] Support nvfp4 cutlass gemm |
| `pr-vllm-16362` | upstream-code | [`sources/prs/vllm/PR-16362.md`](../sources/prs/vllm/PR-16362.md) | [Hardware/NVIDIA/Kernel] [Functional Enablement] [1/N] Enable nvidia/DeepSeek-R1-FP4 Model |
| `pr-vllm-17687` | upstream-code | [`sources/prs/vllm/PR-17687.md`](../sources/prs/vllm/PR-17687.md) | [Kernel] fp4 marlin kernel |
| `pr-vllm-17914` | upstream-code | [`sources/prs/vllm/PR-17914.md`](../sources/prs/vllm/PR-17914.md) | [Misc] Add compressed-tensors NVFP4A16 emulation support |
| `pr-vllm-18000` | upstream-code | [`sources/prs/vllm/PR-18000.md`](../sources/prs/vllm/PR-18000.md) | Use NVFP4 Marlin for CompressedTensorsW4A16Fp4 |
| `pr-vllm-18312` | upstream-code | [`sources/prs/vllm/PR-18312.md`](../sources/prs/vllm/PR-18312.md) | [Quantization] Add compressed-tensors NVFP4 support |
| `pr-vllm-19110` | upstream-code | [`sources/prs/vllm/PR-19110.md`](../sources/prs/vllm/PR-19110.md) | [Hardware][NVIDIA] FP4 MoE kernel optimization |
| `pr-vllm-19500` | upstream-code | [`sources/prs/vllm/PR-19500.md`](../sources/prs/vllm/PR-19500.md) | [Hardware][NVIDIA][kernel] Fp4 MOE quant kernel optimization |
| `pr-vllm-19879` | upstream-code | [`sources/prs/vllm/PR-19879.md`](../sources/prs/vllm/PR-19879.md) | [Quantization] Add compressed-tensors emulations support for NVFP4 |
| `pr-vllm-19990` | upstream-code | [`sources/prs/vllm/PR-19990.md`](../sources/prs/vllm/PR-19990.md) | [Quantization] Add compressed-tensors NVFP4 MoE Support |
| `pr-vllm-20141` | upstream-code | [`sources/prs/vllm/PR-20141.md`](../sources/prs/vllm/PR-20141.md) | [Bugfix] Fix some narrowing conversion warnings |
| `pr-vllm-20324` | upstream-code | [`sources/prs/vllm/PR-20324.md`](../sources/prs/vllm/PR-20324.md) | [Kernel][Bugfix] Fixup some warnings in nvfp4_blockwise_moe when CUDA < 12.8 |
| `pr-vllm-20453` | upstream-code | [`sources/prs/vllm/PR-20453.md`](../sources/prs/vllm/PR-20453.md) | Support Llama 4 for cutlass_moe_fp4 |
| `pr-vllm-20500` | upstream-code | [`sources/prs/vllm/PR-20500.md`](../sources/prs/vllm/PR-20500.md) | [Perf] Reuse workspace for FP8+FP4 Marlin MoE |
| `pr-vllm-21003` | upstream-code | [`sources/prs/vllm/PR-21003.md`](../sources/prs/vllm/PR-21003.md) | Support mnnvl all2allv from Flashinfer |
| `pr-vllm-21166` | upstream-code | [`sources/prs/vllm/PR-21166.md`](../sources/prs/vllm/PR-21166.md) | [Feature][OCP MX] Support mxfp6 and mixed mxfp6-mxfp4 |
| `pr-vllm-21309` | upstream-code | [`sources/prs/vllm/PR-21309.md`](../sources/prs/vllm/PR-21309.md) | Support CUTLASS NVFP4 (w4a4) for Blackwell Geforce GPUs (SM120) |
| `pr-vllm-21331` | upstream-code | [`sources/prs/vllm/PR-21331.md`](../sources/prs/vllm/PR-21331.md) | Support Tensorrt-LLM MoE fp4 for low-latency |
| `pr-vllm-21408` | upstream-code | [`sources/prs/vllm/PR-21408.md`](../sources/prs/vllm/PR-21408.md) | Update flashinfer CUTLASS NVFP4 MoE Kernel to use per expert global scaling factor |
| `pr-vllm-21465` | upstream-code | [`sources/prs/vllm/PR-21465.md`](../sources/prs/vllm/PR-21465.md) | [Bug] Fix Compressed Tensor NVFP4 `cutlass_fp4_group_mm` illegal memory access |
| `pr-vllm-21499` | upstream-code | [`sources/prs/vllm/PR-21499.md`](../sources/prs/vllm/PR-21499.md) | [NVIDIA] Fix Llama4 Scout FP4 functionality issues |
| `pr-vllm-21639` | upstream-code | [`sources/prs/vllm/PR-21639.md`](../sources/prs/vllm/PR-21639.md) | [Feature] Add Flashinfer MoE Support for Compressed Tensor NVFP4 |
| `pr-vllm-22339` | upstream-code | [`sources/prs/vllm/PR-22339.md`](../sources/prs/vllm/PR-22339.md) | [gpt-oss] flashinfer mxfp4 |
| `pr-vllm-22421` | upstream-code | [`sources/prs/vllm/PR-22421.md`](../sources/prs/vllm/PR-22421.md) | [gpt-oss] triton kernel mxfp4 |
| `pr-vllm-22511` | upstream-code | [`sources/prs/vllm/PR-22511.md`](../sources/prs/vllm/PR-22511.md) | Fix Llama4 FlashInfer FP4 MoE issues |
| `pr-vllm-22527` | upstream-code | [`sources/prs/vllm/PR-22527.md`](../sources/prs/vllm/PR-22527.md) | Quantization: support FP4 quantized models on AMD CDNA2/CDNA3 GPUs |
| `pr-vllm-22535` | upstream-code | [`sources/prs/vllm/PR-22535.md`](../sources/prs/vllm/PR-22535.md) | Fix torch version check for SM100 mxfp4  |
| `pr-vllm-22674` | upstream-code | [`sources/prs/vllm/PR-22674.md`](../sources/prs/vllm/PR-22674.md) | [Quantization] Expand compressed-tensors MoE matching logic to support NFP4 + FP8 MoEs |
| `pr-vllm-22703` | upstream-code | [`sources/prs/vllm/PR-22703.md`](../sources/prs/vllm/PR-22703.md) | [NVIDIA] Support Flashinfer TRTLLM FP8-q/kv NVFP4-out Attention Kernel |
| `pr-vllm-23008` | upstream-code | [`sources/prs/vllm/PR-23008.md`](../sources/prs/vllm/PR-23008.md) | Use Blackwell FlashInfer MXFP4 MoE by default if available  |
| `pr-vllm-23123` | upstream-code | [`sources/prs/vllm/PR-23123.md`](../sources/prs/vllm/PR-23123.md) | Add routed_scaling_factor to MoE grouped topk |
| `pr-vllm-23140` | upstream-code | [`sources/prs/vllm/PR-23140.md`](../sources/prs/vllm/PR-23140.md) | Fix nvfp4 swizzling |
| `pr-vllm-23273` | upstream-code | [`sources/prs/vllm/PR-23273.md`](../sources/prs/vllm/PR-23273.md) | [Kernels] Overlap shared experts with send/recv |
| `pr-vllm-23537` | upstream-code | [`sources/prs/vllm/PR-23537.md`](../sources/prs/vllm/PR-23537.md) | Update Flashinfer to  0.2.14.post1 |
| `pr-vllm-23608` | upstream-code | [`sources/prs/vllm/PR-23608.md`](../sources/prs/vllm/PR-23608.md) | DP/EP Support for gpt-oss with deepep-ht comm kernel on SM100 |
| `pr-vllm-23659` | upstream-code | [`sources/prs/vllm/PR-23659.md`](../sources/prs/vllm/PR-23659.md) | [Bugfix] Fix Marlin NVFP4 for modelopt |
| `pr-vllm-23671` | upstream-code | [`sources/prs/vllm/PR-23671.md`](../sources/prs/vllm/PR-23671.md) | [NVIDIA] Support SiluMul + NVFP4 quant fusion |
| `pr-vllm-23696` | upstream-code | [`sources/prs/vllm/PR-23696.md`](../sources/prs/vllm/PR-23696.md) | [Kernel][B200] `mxfp4` fused cutlass moe |
| `pr-vllm-23727` | upstream-code | [`sources/prs/vllm/PR-23727.md`](../sources/prs/vllm/PR-23727.md) | [Bugfix][Misc] Fix silu_and_mul_nvfp4_quant issue and extract common utils for nvfp4 kernel source files |
| `pr-vllm-23819` | upstream-code | [`sources/prs/vllm/PR-23819.md`](../sources/prs/vllm/PR-23819.md) | [Model][gpt-oss] Support DP+EP for GPT-OSS with FlashInfer trtllm-gen MoE |
| `pr-vllm-23929` | upstream-code | [`sources/prs/vllm/PR-23929.md`](../sources/prs/vllm/PR-23929.md) | [BUGFIX ] fix undefined silu_and_mul_nvfp4_quant |
| `pr-vllm-23991` | upstream-code | [`sources/prs/vllm/PR-23991.md`](../sources/prs/vllm/PR-23991.md) | [Model] Add LongCat-Flash  |
| `pr-vllm-24440` | upstream-code | [`sources/prs/vllm/PR-24440.md`](../sources/prs/vllm/PR-24440.md) | [Transform] [Quantization] Add QuTLASS support to vLLM |
| `pr-vllm-24722` | upstream-code | [`sources/prs/vllm/PR-24722.md`](../sources/prs/vllm/PR-24722.md) | [Kernel][Quantization] add w4a8 support for marlin kernel |
| `pr-vllm-24833` | upstream-code | [`sources/prs/vllm/PR-24833.md`](../sources/prs/vllm/PR-24833.md) | [Bugfix] Fix accuracy issue for silu_mul + nvfp4 quant fusion kernel |
| `pr-vllm-25193` | upstream-code | [`sources/prs/vllm/PR-25193.md`](../sources/prs/vllm/PR-25193.md) | [Compile] Fix Compile Warning for Ignoring `MIN_BLOCK_PER_SM` |
| `pr-vllm-25201` | upstream-code | [`sources/prs/vllm/PR-25201.md`](../sources/prs/vllm/PR-25201.md) | [ROCm] Small functional changes for gptoss |
| `pr-vllm-25609` | upstream-code | [`sources/prs/vllm/PR-25609.md`](../sources/prs/vllm/PR-25609.md) | Enable Fbgemm NVFP4 on Dense models |
| `pr-vllm-25947` | upstream-code | [`sources/prs/vllm/PR-25947.md`](../sources/prs/vllm/PR-25947.md) | [Bugfix] Enable padded FP4 quantization |
| `pr-vllm-25968` | upstream-code | [`sources/prs/vllm/PR-25968.md`](../sources/prs/vllm/PR-25968.md) | [Quantization/NVFP4] Speed up TRTLLM NVFP4 MOE weight loading and fix K/V scale loading for MLA Attn |
| `pr-vllm-25987` | upstream-code | [`sources/prs/vllm/PR-25987.md`](../sources/prs/vllm/PR-25987.md) | [Bugfix] Allow skipping MoE in NVFP4 (fix for MTP) |
| `pr-vllm-25990` | upstream-code | [`sources/prs/vllm/PR-25990.md`](../sources/prs/vllm/PR-25990.md) | [MoE] Nvfp4 Masked Gemm: Add flashinfer grouped_gemm_nt_masked |
| `pr-vllm-26107` | upstream-code | [`sources/prs/vllm/PR-26107.md`](../sources/prs/vllm/PR-26107.md) | [NVIDIA] Add support for cudnn fp4 gemm via flashinfer |
| `pr-vllm-26135` | upstream-code | [`sources/prs/vllm/PR-26135.md`](../sources/prs/vllm/PR-26135.md) | [ModelOpt] Load w13/w2_input_scale for all experts, nvfp4 |
| `pr-vllm-26545` | upstream-code | [`sources/prs/vllm/PR-26545.md`](../sources/prs/vllm/PR-26545.md) | [ROCM] MoE fp4 CK kernel |
| `pr-vllm-26669` | upstream-code | [`sources/prs/vllm/PR-26669.md`](../sources/prs/vllm/PR-26669.md) | support flashinfer_fp4 moe for 5090 gpu |
| `pr-vllm-26714` | upstream-code | [`sources/prs/vllm/PR-26714.md`](../sources/prs/vllm/PR-26714.md) | [NVIDIA] [Perf] Update to leverage flashinfer trtllm FP4 MOE throughput kernel |
| `pr-vllm-26729` | upstream-code | [`sources/prs/vllm/PR-26729.md`](../sources/prs/vllm/PR-26729.md) | [Bugfix] Fix gpt-oss w4a8 DP/EP on B200 |
| `pr-vllm-27223` | upstream-code | [`sources/prs/vllm/PR-27223.md`](../sources/prs/vllm/PR-27223.md) | Flashinfer_CUTLASS_MOE fuses quantization for TP |
| `pr-vllm-27532` | upstream-code | [`sources/prs/vllm/PR-27532.md`](../sources/prs/vllm/PR-27532.md) | [Attention] Use sparse prefill kernel for fp8 kv-cache in DeepSeek-v3.2 |
| `pr-vllm-28816` | upstream-code | [`sources/prs/vllm/PR-28816.md`](../sources/prs/vllm/PR-28816.md) | [Bugfix] Fix GPT-OSS on AMD after #28603 |
| `pr-vllm-28892` | upstream-code | [`sources/prs/vllm/PR-28892.md`](../sources/prs/vllm/PR-28892.md) | Add TRTLLM MoE NVFP4 kernel to CompressedTensorsW4A4MoeMethod |
| `pr-vllm-29004` | upstream-code | [`sources/prs/vllm/PR-29004.md`](../sources/prs/vllm/PR-29004.md) | [Feat] Support non-gated activations in NVFP4 modelopt path |
| `pr-vllm-29242` | upstream-code | [`sources/prs/vllm/PR-29242.md`](../sources/prs/vllm/PR-29242.md) | [Kernel] Add NVFP4 MoE CUTLASS support for SM120 |
| `pr-vllm-29339` | upstream-code | [`sources/prs/vllm/PR-29339.md`](../sources/prs/vllm/PR-29339.md) | [Bugfix] Only use triton_kernels for MXFP4 on SM90 and SM100 |
| `pr-vllm-29742` | upstream-code | [`sources/prs/vllm/PR-29742.md`](../sources/prs/vllm/PR-29742.md) | [Bugfix] Fix mismatched nvfp4 gemm output shape |
| `pr-vllm-29775` | upstream-code | [`sources/prs/vllm/PR-29775.md`](../sources/prs/vllm/PR-29775.md) | [ROCm][MXFP4] Infer w4a4 quant method in rocm aiter fused moe |
| `pr-vllm-29804` | upstream-code | [`sources/prs/vllm/PR-29804.md`](../sources/prs/vllm/PR-29804.md) | [EPLB] Support EPLB w/ NVFP4 |
| `pr-vllm-30014` | upstream-code | [`sources/prs/vllm/PR-30014.md`](../sources/prs/vllm/PR-30014.md) | [Perf] Do FP4 quant before All gather on flashinfer trtllmgen MOE  |
| `pr-vllm-30357` | upstream-code | [`sources/prs/vllm/PR-30357.md`](../sources/prs/vllm/PR-30357.md) | [ROCm][Quantization] GPT OSS Upstream MoE wmxfp4_afp8 with static scales |
| `pr-vllm-30484` | upstream-code | [`sources/prs/vllm/PR-30484.md`](../sources/prs/vllm/PR-30484.md) | [Feature] Add SM103 (Blackwell Ultra) Support to vLLM |
| `pr-vllm-30528` | upstream-code | [`sources/prs/vllm/PR-30528.md`](../sources/prs/vllm/PR-30528.md) | [Perf] Set split_k to 1 for triton_kernels |
| `pr-vllm-30647` | upstream-code | [`sources/prs/vllm/PR-30647.md`](../sources/prs/vllm/PR-30647.md) | [Perf] Eliminate padding and slicing op for GPT-OSS with Flashinfer MXFP4 MXFP8 MoE |
| `pr-vllm-30746` | upstream-code | [`sources/prs/vllm/PR-30746.md`](../sources/prs/vllm/PR-30746.md) | [SM100] Enable fp8 compute for prefill MLA |
| `pr-vllm-30881` | upstream-code | [`sources/prs/vllm/PR-30881.md`](../sources/prs/vllm/PR-30881.md) | [Compressed-Tensors] Simplify NVFP4 Conditions, enable marlin support for NVFP4A16 MoEs |
| `pr-vllm-30885` | upstream-code | [`sources/prs/vllm/PR-30885.md`](../sources/prs/vllm/PR-30885.md) | [Kernel][Performance] Enable smaller Scaling Factor tiling for NVFP4 small-batch decoding |
| `pr-vllm-30897` | upstream-code | [`sources/prs/vllm/PR-30897.md`](../sources/prs/vllm/PR-30897.md) | [NVFP4][Perf] Tune NVFP4 input quant kernel for small batch size |
| `pr-vllm-31099` | upstream-code | [`sources/prs/vllm/PR-31099.md`](../sources/prs/vllm/PR-31099.md) |  [FIX] Always support TP > 4 for FP4 Gemm |
| `pr-vllm-31742` | upstream-code | [`sources/prs/vllm/PR-31742.md`](../sources/prs/vllm/PR-31742.md) | [Bugfix] Fix Broken ModelOpt NVFP4 MoE |
| `pr-vllm-31837` | upstream-code | [`sources/prs/vllm/PR-31837.md`](../sources/prs/vllm/PR-31837.md) | [Perf] Fuse stride preparation for NVFP4 cutlass_moe |
| `pr-vllm-32064` | upstream-code | [`sources/prs/vllm/PR-32064.md`](../sources/prs/vllm/PR-32064.md) | [5/N][Attention] Finish eliminating `vllm/attention` folder |
| `pr-vllm-32520` | upstream-code | [`sources/prs/vllm/PR-32520.md`](../sources/prs/vllm/PR-32520.md) | [Perf][Kernel] Optimize FP4 quantization kernels (SM100F) |
| `pr-vllm-33076` | upstream-code | [`sources/prs/vllm/PR-33076.md`](../sources/prs/vllm/PR-33076.md) | Support compress-tensors with nvfp4 or fp8 weights and modelopt with nvfp4 weights on Turing |
| `pr-vllm-33417` | upstream-code | [`sources/prs/vllm/PR-33417.md`](../sources/prs/vllm/PR-33417.md) | fix: Add SM120 (RTX Blackwell) support for FlashInfer CUTLASS NVFP4 MoE kernels |
| `pr-vllm-33506` | upstream-code | [`sources/prs/vllm/PR-33506.md`](../sources/prs/vllm/PR-33506.md) | [Kernel] Support Flashinfer trtllm fused MoE non gated FP8 & NVFP4 |
| `pr-vllm-33932` | upstream-code | [`sources/prs/vllm/PR-33932.md`](../sources/prs/vllm/PR-33932.md) | [Bugfix] Fix DSV3.2 NVFP4 |
| `pr-vllm-33972` | upstream-code | [`sources/prs/vllm/PR-33972.md`](../sources/prs/vllm/PR-33972.md) | [Bugfix]fix output Nan/Inf in marlin if dtype=float16 |
| `pr-vllm-34298` | upstream-code | [`sources/prs/vllm/PR-34298.md`](../sources/prs/vllm/PR-34298.md) | [ModelBash][DSR1 NVFp4] Avoid Bf16 Bias Cast |
| `pr-vllm-34389` | upstream-code | [`sources/prs/vllm/PR-34389.md`](../sources/prs/vllm/PR-34389.md) | [Custom Ops] Add functional + out variant for scaled_fp4_quant |
| `pr-vllm-34478` | upstream-code | [`sources/prs/vllm/PR-34478.md`](../sources/prs/vllm/PR-34478.md) | [Model] Add NVFP4 quantization support for Step3.5-Flash |
| `pr-vllm-34556` | upstream-code | [`sources/prs/vllm/PR-34556.md`](../sources/prs/vllm/PR-34556.md) | [Quantization] add humming quantization kernel |
| `pr-vllm-34577` | upstream-code | [`sources/prs/vllm/PR-34577.md`](../sources/prs/vllm/PR-34577.md) | [Bugfix] Rescale NVFP4 weight scales to fix BF16 dequant underflow |
| `pr-vllm-34725` | upstream-code | [`sources/prs/vllm/PR-34725.md`](../sources/prs/vllm/PR-34725.md) | [Bugfix] Fix NVFP4 TRTLLM MoE non-gated support; add gsm8k for Nemotron-3-Nano FP8+NVFP4 |
| `pr-vllm-35210` | upstream-code | [`sources/prs/vllm/PR-35210.md`](../sources/prs/vllm/PR-35210.md) | [BugFix] Fix fp4 quant kernel on CUDA 12.8 |
| `pr-vllm-35382` | upstream-code | [`sources/prs/vllm/PR-35382.md`](../sources/prs/vllm/PR-35382.md) | fix(mxfp4): return is_monolithic=False when LoRA is enabled for Triton backend |
| `pr-vllm-35733` | upstream-code | [`sources/prs/vllm/PR-35733.md`](../sources/prs/vllm/PR-35733.md) | [NVFP4] Support NVFP4 dense models from `modelopt` and `compressed-tensors` on AMD Instinct MI300, MI355X and Hopper through emulation |
| `pr-vllm-36017` | upstream-code | [`sources/prs/vllm/PR-36017.md`](../sources/prs/vllm/PR-36017.md) | [Bugfix] Fix passing of activation_type to trtllm fused MoE NVFP4 and FP8 |
| `pr-vllm-36162` | upstream-code | [`sources/prs/vllm/PR-36162.md`](../sources/prs/vllm/PR-36162.md) | [Mamba] Flashinfer selective_state_update |
| `pr-vllm-36205` | upstream-code | [`sources/prs/vllm/PR-36205.md`](../sources/prs/vllm/PR-36205.md) | [mla] Support fused FP8/NVFP4 output quantization in MLA attention (#35792) |
| `pr-vllm-36725` | upstream-code | [`sources/prs/vllm/PR-36725.md`](../sources/prs/vllm/PR-36725.md) | [Bug][MoE] Fix TRTLLM NVFP4 Routing Kernel Precision |
| `pr-vllm-36728` | upstream-code | [`sources/prs/vllm/PR-36728.md`](../sources/prs/vllm/PR-36728.md) | [Bug][MoE] Strengthen _supports_current_device() checks in the TRTLLM FP8, NVFP4, and FlashInfer CuteDSL MoE experts |
| `pr-vllm-37128` | upstream-code | [`sources/prs/vllm/PR-37128.md`](../sources/prs/vllm/PR-37128.md) | [MoE Refactor] Mxfp4 oracle rebased |
| `pr-vllm-37217` | upstream-code | [`sources/prs/vllm/PR-37217.md`](../sources/prs/vllm/PR-37217.md) | [MoE/EPLB] Fix FlashInfer nvfp4 experts + EPLB correctness |
| `pr-vllm-37320` | upstream-code | [`sources/prs/vllm/PR-37320.md`](../sources/prs/vllm/PR-37320.md) | [Kernel] Add non-gated support for NVFP4 CUTLASS MoE |
| `pr-vllm-37332` | upstream-code | [`sources/prs/vllm/PR-37332.md`](../sources/prs/vllm/PR-37332.md) | Add nvfp4 support to reshape_and_cache_flash |
| `pr-vllm-37463` | upstream-code | [`sources/prs/vllm/PR-37463.md`](../sources/prs/vllm/PR-37463.md) | [Kernel] Add MXFP4 W4A4 CUTLASS MoE kernel for SM100 |
| `pr-vllm-37465` | upstream-code | [`sources/prs/vllm/PR-37465.md`](../sources/prs/vllm/PR-37465.md) | [Bugfix] Remove assertion for NVFP4 scale dynamic range |
| `pr-vllm-37502` | upstream-code | [`sources/prs/vllm/PR-37502.md`](../sources/prs/vllm/PR-37502.md) | [Bugfix] Fix marlin nvfp4 rescaling |
| `pr-vllm-37503` | upstream-code | [`sources/prs/vllm/PR-37503.md`](../sources/prs/vllm/PR-37503.md) | [4/n] Migrate FP4/W4A8 CUTLASS kernels to torch stable ABI |
| `pr-vllm-37695` | upstream-code | [`sources/prs/vllm/PR-37695.md`](../sources/prs/vllm/PR-37695.md) | [Perf] Use torch compile to fuse pack topk in trtllm moe |
| `pr-vllm-37759` | upstream-code | [`sources/prs/vllm/PR-37759.md`](../sources/prs/vllm/PR-37759.md) | [MoE] Move FlashInfer CuteDSL experts into fused_moe/experts/ |
| `pr-vllm-38050` | upstream-code | [`sources/prs/vllm/PR-38050.md`](../sources/prs/vllm/PR-38050.md) | [MoE Kernel] Flashinfer nvfp4 cutedsl moe kernel integration |
| `pr-vllm-38065` | upstream-code | [`sources/prs/vllm/PR-38065.md`](../sources/prs/vllm/PR-38065.md) | [Perf] FP8 FlashInfer Attn for ViT |
| `pr-vllm-38083` | upstream-code | [`sources/prs/vllm/PR-38083.md`](../sources/prs/vllm/PR-38083.md) | [Bugfix] Fix DeepGemm E8M0 accuracy degradation for Qwen3.5 FP8 on Blackwell |
| `pr-vllm-38148` | upstream-code | [`sources/prs/vllm/PR-38148.md`](../sources/prs/vllm/PR-38148.md) | Fix NaN from stale FP4 scale padding in create_fp4_scale_tensor |
| `pr-vllm-38251` | upstream-code | [`sources/prs/vllm/PR-38251.md`](../sources/prs/vllm/PR-38251.md) | [Quantization] Add FlashInfer CuteDSL batched experts backend for NVFP4 MoE |
| `pr-vllm-38329` | upstream-code | [`sources/prs/vllm/PR-38329.md`](../sources/prs/vllm/PR-38329.md) | [MoE] Add RoutingMethodType.Simulated to TRT-LLM FP8/NVFP4 kernel allowlists |
| `pr-vllm-38423` | upstream-code | [`sources/prs/vllm/PR-38423.md`](../sources/prs/vllm/PR-38423.md) | [NVIDIA] Bugfix NVFP4 DGX Spark and RTX50 |
| `pr-vllm-38504` | upstream-code | [`sources/prs/vllm/PR-38504.md`](../sources/prs/vllm/PR-38504.md) | [Kernels][MoE] Fix legacy_routing to use bitmatrix-based routing path |
| `pr-vllm-38573` | upstream-code | [`sources/prs/vllm/PR-38573.md`](../sources/prs/vllm/PR-38573.md) | [Compile] Fix nvfp4 compile warning |
| `pr-vllm-38960` | upstream-code | [`sources/prs/vllm/PR-38960.md`](../sources/prs/vllm/PR-38960.md) | [MoE Refactor] Split up compressed_tensors_moe.py |
| `pr-vllm-39007` | upstream-code | [`sources/prs/vllm/PR-39007.md`](../sources/prs/vllm/PR-39007.md) | [MoE] Move GPT OSS Triton kernel experts into fused_moe/experts/ |
| `pr-vllm-39129` | upstream-code | [`sources/prs/vllm/PR-39129.md`](../sources/prs/vllm/PR-39129.md) | [Refactor] Move NVFP4 GEMM management into NvFp4LinearKernel |
| `pr-vllm-39322` | upstream-code | [`sources/prs/vllm/PR-39322.md`](../sources/prs/vllm/PR-39322.md) | [Feature] Batch invariant nvfp4 linear support |
| `pr-vllm-39510` | upstream-code | [`sources/prs/vllm/PR-39510.md`](../sources/prs/vllm/PR-39510.md) | [Kernel] Support TRTLLM GEN NVFP4 MoE for non-512-aligned hidden dims via weight padding |
| `pr-vllm-39717` | upstream-code | [`sources/prs/vllm/PR-39717.md`](../sources/prs/vllm/PR-39717.md) | [Bugfix] Reject non-nvfp4 dtypes when using the flashinfer_nvlink_one_sided all2all backend |
| `pr-vllm-39820` | upstream-code | [`sources/prs/vllm/PR-39820.md`](../sources/prs/vllm/PR-39820.md) | [Bug] Fix batch invariance nvfp4 support |
| `pr-vllm-40177` | upstream-code | [`sources/prs/vllm/PR-40177.md`](../sources/prs/vllm/PR-40177.md) | Add nvfp4 kv cache support |
| `pr-vllm-40191` | upstream-code | [`sources/prs/vllm/PR-40191.md`](../sources/prs/vllm/PR-40191.md) | [Bugfix] Guard mxfp4_experts_quant bindings on ENABLE_NVFP4_SM100 |
| `pr-vllm-40392` | upstream-code | [`sources/prs/vllm/PR-40392.md`](../sources/prs/vllm/PR-40392.md) | [Performance][DSR1]: Fused RoPE+KVCache+q_concat for MLA |
| `pr-vllm-40574` | upstream-code | [`sources/prs/vllm/PR-40574.md`](../sources/prs/vllm/PR-40574.md) | [MoE] Move cutlass moe to fused_moe/experts/ |
| `pr-vllm-40960` | upstream-code | [`sources/prs/vllm/PR-40960.md`](../sources/prs/vllm/PR-40960.md) | [DSV4] Add BF16 and MXFP8 A2A support for flashinfer a2a one sided |
| `pr-vllm-41050` | upstream-code | [`sources/prs/vllm/PR-41050.md`](../sources/prs/vllm/PR-41050.md) | [Kernel][MoE] Support GELU on TRT-LLM NvFP4 fused MoE for Gemma4 |
| `pr-vllm-41428` | upstream-code | [`sources/prs/vllm/PR-41428.md`](../sources/prs/vllm/PR-41428.md) | [DSv4] Improved fused Indexer Q quant kernel |
| `pr-vllm-41566` | upstream-code | [`sources/prs/vllm/PR-41566.md`](../sources/prs/vllm/PR-41566.md) | [Quantization] Rework quantization_config to use QuantKey and allow for activation override |
| `pr-vllm-41664` | upstream-code | [`sources/prs/vllm/PR-41664.md`](../sources/prs/vllm/PR-41664.md) | [MXFP4] Support for linear layers + compressed-tensors integration |
| `pr-vllm-41745` | upstream-code | [`sources/prs/vllm/PR-41745.md`](../sources/prs/vllm/PR-41745.md) | [Spec Decode] Add Gemma4 MTP speculative decoding support |
| `pr-vllm-41882` | upstream-code | [`sources/prs/vllm/PR-41882.md`](../sources/prs/vllm/PR-41882.md) | Add NVFP4 all-gather GEMM fusion for AsyncTP |
| `pr-vllm-41979` | upstream-code | [`sources/prs/vllm/PR-41979.md`](../sources/prs/vllm/PR-41979.md) | [MoE] Move various experts classes to fused_moe/experts/ |
| `pr-vllm-41986` | upstream-code | [`sources/prs/vllm/PR-41986.md`](../sources/prs/vllm/PR-41986.md) | [Bugfix] Add swiglu limits to deepgemm fp8 methods |

<a id="fp8"></a>
## fp8

605 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `contest-flashinfer-track-a` | contest-report | [`sources/contests/flashinfer-mlsys26/track-a-fused-moe.md`](../sources/contests/flashinfer-mlsys26/track-a-fused-moe.md) | FlashInfer MLSys 2026 - Track A: Fused MoE FP8 |
| `contest-flashinfer-track-b` | contest-report | [`sources/contests/flashinfer-mlsys26/track-b-sparse-attention.md`](../sources/contests/flashinfer-mlsys26/track-b-sparse-attention.md) | FlashInfer MLSys 2026 - Track B: DeepSeek V3.2 Sparse Attention |
| `pr-cccl-cub-3588` | upstream-code | [`sources/prs/cccl-cub/PR-3588.md`](../sources/prs/cccl-cub/PR-3588.md) | Function-like macros for FP6/BF16 macros |
| `pr-cccl-cub-3832` | upstream-code | [`sources/prs/cccl-cub/PR-3832.md`](../sources/prs/cccl-cub/PR-3832.md) | Specialize `numeric_limits` for CUDA 12.8 FP types |
| `pr-cccl-cub-4256` | upstream-code | [`sources/prs/cccl-cub/PR-4256.md`](../sources/prs/cccl-cub/PR-4256.md) | Implement fp constants |
| `pr-cccl-cub-5413` | upstream-code | [`sources/prs/cccl-cub/PR-5413.md`](../sources/prs/cccl-cub/PR-5413.md) | Add common constants for floating point types |
| `pr-cccl-cub-5978` | upstream-code | [`sources/prs/cccl-cub/PR-5978.md`](../sources/prs/cccl-cub/PR-5978.md) | [BACKPORT 3.1] Use forward declarations of extended floating point types instead of including the headers (#5846) |
| `pr-cccl-cub-8351` | upstream-code | [`sources/prs/cccl-cub/PR-8351.md`](../sources/prs/cccl-cub/PR-8351.md) | Fix and improve vector type traits |
| `pr-cccl-cub-8988` | upstream-code | [`sources/prs/cccl-cub/PR-8988.md`](../sources/prs/cccl-cub/PR-8988.md) | [infra] Add clang-cuda-21 in C++23 job for libcu++ |
| `pr-cutlass-1883` | upstream-code | [`sources/prs/cutlass/PR-1883.md`](../sources/prs/cutlass/PR-1883.md) | Improve sm90 mixed dtype kernel |
| `pr-cutlass-1932` | upstream-code | [`sources/prs/cutlass/PR-1932.md`](../sources/prs/cutlass/PR-1932.md) | Blockwise Scaling for FP8 |
| `pr-cutlass-2037` | upstream-code | [`sources/prs/cutlass/PR-2037.md`](../sources/prs/cutlass/PR-2037.md) | Groupwise scaling along M for FP8 gemm |
| `pr-cutlass-2095` | upstream-code | [`sources/prs/cutlass/PR-2095.md`](../sources/prs/cutlass/PR-2095.md) | Improvements for: Groupwise scaling along M for FP8 gemm |
| `pr-cutlass-2123` | upstream-code | [`sources/prs/cutlass/PR-2123.md`](../sources/prs/cutlass/PR-2123.md) | Hopper Grouped GEMM support for FP8 Accum |
| `pr-cutlass-2139` | upstream-code | [`sources/prs/cutlass/PR-2139.md`](../sources/prs/cutlass/PR-2139.md) | Blockwise and Groupwise GEMM for Blackwell and Improvements for Hopper |
| `pr-cutlass-2270` | upstream-code | [`sources/prs/cutlass/PR-2270.md`](../sources/prs/cutlass/PR-2270.md) | hopper-blockwise-generalization-optimization |
| `pr-cutlass-2378` | upstream-code | [`sources/prs/cutlass/PR-2378.md`](../sources/prs/cutlass/PR-2378.md) | support fp16 accmulator for sm89 fp8 mma |
| `pr-cutlass-2466` | upstream-code | [`sources/prs/cutlass/PR-2466.md`](../sources/prs/cutlass/PR-2466.md) | Example 77 add blackwell fmha bwd for MLA shape |
| `pr-cutlass-2472` | upstream-code | [`sources/prs/cutlass/PR-2472.md`](../sources/prs/cutlass/PR-2472.md) | Add Blackwell MLA forward (shape: d=192, dv=128) implementation |
| `pr-cutlass-2946` | upstream-code | [`sources/prs/cutlass/PR-2946.md`](../sources/prs/cutlass/PR-2946.md) | [Cutlass profiler] Fix SM100 FP8 nosmem epilogue shape_div “Divisibility Condition” for non‑multiple‑of‑64 N tiles |
| `pr-cutlass-2965` | upstream-code | [`sources/prs/cutlass/PR-2965.md`](../sources/prs/cutlass/PR-2965.md) | [Bug Fix]Set NumSplitsM to 1 when TileShapeM < 128 in sm90 fp8 blockwise scaling CollectiveMma |
| `pr-deepgemm-103` | upstream-code | [`sources/prs/deepgemm/PR-103.md`](../sources/prs/deepgemm/PR-103.md) | Grouped GEMM skip useless computation for unaligned Ms |
| `pr-deepgemm-112` | upstream-code | [`sources/prs/deepgemm/PR-112.md`](../sources/prs/deepgemm/PR-112.md) | Add more GPU architectures support |
| `pr-deepgemm-158` | upstream-code | [`sources/prs/deepgemm/PR-158.md`](../sources/prs/deepgemm/PR-158.md) | Fix inappropriate configs for some small shapes |
| `pr-deepgemm-198` | upstream-code | [`sources/prs/deepgemm/PR-198.md`](../sources/prs/deepgemm/PR-198.md) | Make various updates and fixes |
| `pr-deepgemm-227` | upstream-code | [`sources/prs/deepgemm/PR-227.md`](../sources/prs/deepgemm/PR-227.md) | Use larger MMA shape to optimize sm100_fp8_mqa_logits |
| `pr-deepgemm-233` | upstream-code | [`sources/prs/deepgemm/PR-233.md`](../sources/prs/deepgemm/PR-233.md) | support bf16 bias in deepgemm2 |
| `pr-deepgemm-304` | upstream-code | [`sources/prs/deepgemm/PR-304.md`](../sources/prs/deepgemm/PR-304.md) | [Public release 26/04] Introducing Mega MoE, FP4 Indexer and other features/fixes |
| `pr-deepgemm-316` | upstream-code | [`sources/prs/deepgemm/PR-316.md`](../sources/prs/deepgemm/PR-316.md) | Add various optimizations and Mega MoE benchmarks |
| `pr-deepgemm-328` | upstream-code | [`sources/prs/deepgemm/PR-328.md`](../sources/prs/deepgemm/PR-328.md) | Sync nv_dev with upstream #316 (Mega MoE optimizations & benchmarks) |
| `pr-deepgemm-68` | upstream-code | [`sources/prs/deepgemm/PR-68.md`](../sources/prs/deepgemm/PR-68.md) | Correctly flush L2 (+performance impact & upcoming optimization fork) |
| `pr-deepgemm-74` | upstream-code | [`sources/prs/deepgemm/PR-74.md`](../sources/prs/deepgemm/PR-74.md) | Performance: Larger BlockTile optimizations enable 1470+ TF FP8 on the "H800"-SXM |
| `pr-deepgemm-78` | upstream-code | [`sources/prs/deepgemm/PR-78.md`](../sources/prs/deepgemm/PR-78.md) |  Solving bank conflict via padding and TMA 3D store |
| `pr-deepgemm-81` | upstream-code | [`sources/prs/deepgemm/PR-81.md`](../sources/prs/deepgemm/PR-81.md) | Performance: BlockTile 256x128 optimizations enable 1500+ TF FP8 |
| `pr-deepgemm-83` | upstream-code | [`sources/prs/deepgemm/PR-83.md`](../sources/prs/deepgemm/PR-83.md) | Use 1D TMA store instead of 3D |
| `pr-deepgemm-86` | upstream-code | [`sources/prs/deepgemm/PR-86.md`](../sources/prs/deepgemm/PR-86.md) | Use swizzling instead of padding |
| `pr-deepgemm-88` | upstream-code | [`sources/prs/deepgemm/PR-88.md`](../sources/prs/deepgemm/PR-88.md) | Support TMA multicast on B with m_grouped_gemm_contiguous. |
| `pr-deepgemm-95` | upstream-code | [`sources/prs/deepgemm/PR-95.md`](../sources/prs/deepgemm/PR-95.md) | Weight gradient kernels for dense and MoE models |
| `pr-flash-attention-1072` | upstream-code | [`sources/prs/flash-attention/PR-1072.md`](../sources/prs/flash-attention/PR-1072.md) | Add var-seq-len to FA3 fp16 / bf16 fwd |
| `pr-flash-attention-1075` | upstream-code | [`sources/prs/flash-attention/PR-1075.md`](../sources/prs/flash-attention/PR-1075.md) | Changes For FP8  |
| `pr-flash-attention-1100` | upstream-code | [`sources/prs/flash-attention/PR-1100.md`](../sources/prs/flash-attention/PR-1100.md) | Fp8 kernel with "in-kernel" transpose of V in producer |
| `pr-flash-attention-1173` | upstream-code | [`sources/prs/flash-attention/PR-1173.md`](../sources/prs/flash-attention/PR-1173.md) | FA3 FP8 qkv descales + restore max offset for h128 causal + added sync for producer WG |
| `pr-flash-attention-1180` | upstream-code | [`sources/prs/flash-attention/PR-1180.md`](../sources/prs/flash-attention/PR-1180.md) | Add ArchTag to pre/postprocess bwd kernels |
| `pr-flash-attention-1233` | upstream-code | [`sources/prs/flash-attention/PR-1233.md`](../sources/prs/flash-attention/PR-1233.md) | Add local attention in Hopper FAv3 |
| `pr-flash-attention-1236` | upstream-code | [`sources/prs/flash-attention/PR-1236.md`](../sources/prs/flash-attention/PR-1236.md) | FA3 kvcache + split kv + gqa parallelization |
| `pr-flash-attention-1268` | upstream-code | [`sources/prs/flash-attention/PR-1268.md`](../sources/prs/flash-attention/PR-1268.md) | Paged Attention support for FA3 |
| `pr-flash-attention-1610` | upstream-code | [`sources/prs/flash-attention/PR-1610.md`](../sources/prs/flash-attention/PR-1610.md) | [AMD] Triton Backend for ROCm #2 |
| `pr-flash-attention-2109` | upstream-code | [`sources/prs/flash-attention/PR-2109.md`](../sources/prs/flash-attention/PR-2109.md) | [Cute,Fwd,Sm100] fp8 e4m3 and e5m2 support |
| `pr-flash-attention-2178` | upstream-code | [`sources/prs/flash-attention/PR-2178.md`](../sources/prs/flash-attention/PR-2178.md) |  [AMD] Triton Backend for ROCm #3 |
| `pr-flash-attention-2363` | upstream-code | [`sources/prs/flash-attention/PR-2363.md`](../sources/prs/flash-attention/PR-2363.md) | [AMD ROCm] Update ROCm/CK backend to align with latest ComposableKernel API changes |
| `pr-flash-attention-2368` | upstream-code | [`sources/prs/flash-attention/PR-2368.md`](../sources/prs/flash-attention/PR-2368.md) | [Cute] fix: FA4 paged attention kv load for DeepSeek (192,128) on SM100 |
| `pr-flash-attention-2385` | upstream-code | [`sources/prs/flash-attention/PR-2385.md`](../sources/prs/flash-attention/PR-2385.md) | [ROCM] Fix windows issues |
| `pr-flashinfer-1033` | upstream-code | [`sources/prs/flashinfer/PR-1033.md`](../sources/prs/flashinfer/PR-1033.md) | feat: add functional per-head FP8 quantization for FA3 |
| `pr-flashinfer-1086` | upstream-code | [`sources/prs/flashinfer/PR-1086.md`](../sources/prs/flashinfer/PR-1086.md) | perf: accelerate blackwell grouped gemm |
| `pr-flashinfer-1087` | upstream-code | [`sources/prs/flashinfer/PR-1087.md`](../sources/prs/flashinfer/PR-1087.md) | bugfix: fix fp8 attention kernels aot compilation issue |
| `pr-flashinfer-1113` | upstream-code | [`sources/prs/flashinfer/PR-1113.md`](../sources/prs/flashinfer/PR-1113.md) | Add CUTLASS fused moe kernels from TensorRT-LLM. |
| `pr-flashinfer-1117` | upstream-code | [`sources/prs/flashinfer/PR-1117.md`](../sources/prs/flashinfer/PR-1117.md) | [Feature] Support PDL for batch Prefill and Decode |
| `pr-flashinfer-1209` | upstream-code | [`sources/prs/flashinfer/PR-1209.md`](../sources/prs/flashinfer/PR-1209.md) | Add DeepGEMM kernels |
| `pr-flashinfer-1212` | upstream-code | [`sources/prs/flashinfer/PR-1212.md`](../sources/prs/flashinfer/PR-1212.md) | feat: trtllm-gen fp8 moe kernels |
| `pr-flashinfer-1240` | upstream-code | [`sources/prs/flashinfer/PR-1240.md`](../sources/prs/flashinfer/PR-1240.md) | Patch fp8 cubin availability |
| `pr-flashinfer-1241` | upstream-code | [`sources/prs/flashinfer/PR-1241.md`](../sources/prs/flashinfer/PR-1241.md) | feat: Support MXFP8 x MXFP4 CUTLASS grouped GEMM |
| `pr-flashinfer-1242` | upstream-code | [`sources/prs/flashinfer/PR-1242.md`](../sources/prs/flashinfer/PR-1242.md) | Add trtllm-gen attention mha kernel with FP8 Q/K/V and FP8 output |
| `pr-flashinfer-1251` | upstream-code | [`sources/prs/flashinfer/PR-1251.md`](../sources/prs/flashinfer/PR-1251.md) | Reduce the JIT compilation time of gen_gemm_sm100_module |
| `pr-flashinfer-1264` | upstream-code | [`sources/prs/flashinfer/PR-1264.md`](../sources/prs/flashinfer/PR-1264.md) | init add gemm fp8 using cudnn backend |
| `pr-flashinfer-1266` | upstream-code | [`sources/prs/flashinfer/PR-1266.md`](../sources/prs/flashinfer/PR-1266.md) | feat: add masked deepgemm support and benchmarking |
| `pr-flashinfer-1281` | upstream-code | [`sources/prs/flashinfer/PR-1281.md`](../sources/prs/flashinfer/PR-1281.md) | Unify groupwise fp8 GEMM test |
| `pr-flashinfer-1287` | upstream-code | [`sources/prs/flashinfer/PR-1287.md`](../sources/prs/flashinfer/PR-1287.md) | Bug fix: guard fp8 e8m0 and e2m1 compile  |
| `pr-flashinfer-1294` | upstream-code | [`sources/prs/flashinfer/PR-1294.md`](../sources/prs/flashinfer/PR-1294.md) | Update cutlass fp4 moe kernels |
| `pr-flashinfer-1319` | upstream-code | [`sources/prs/flashinfer/PR-1319.md`](../sources/prs/flashinfer/PR-1319.md) | Make Fp8 MoE routing_bias optional |
| `pr-flashinfer-1320` | upstream-code | [`sources/prs/flashinfer/PR-1320.md`](../sources/prs/flashinfer/PR-1320.md) | Add blockwise-scaled FP8 GEMM via TRTLLM-Gen. |
| `pr-flashinfer-1339` | upstream-code | [`sources/prs/flashinfer/PR-1339.md`](../sources/prs/flashinfer/PR-1339.md) | feat: Fused rope fp8 quantize kernel for MLA |
| `pr-flashinfer-1358` | upstream-code | [`sources/prs/flashinfer/PR-1358.md`](../sources/prs/flashinfer/PR-1358.md) | [fix] remove (view) transpose to keep consistent with majorness MN requirement. |
| `pr-flashinfer-1376` | upstream-code | [`sources/prs/flashinfer/PR-1376.md`](../sources/prs/flashinfer/PR-1376.md) | bugfix: Add guard for fp4/fp8 related include headers |
| `pr-flashinfer-1389` | upstream-code | [`sources/prs/flashinfer/PR-1389.md`](../sources/prs/flashinfer/PR-1389.md) | GPT-OSS Support: Add Blackwell MoE mxfp4 implementation from TRTLLM and Attention Sink |
| `pr-flashinfer-1390` | upstream-code | [`sources/prs/flashinfer/PR-1390.md`](../sources/prs/flashinfer/PR-1390.md) | Adding FP8 benchmark on attention and matmul testing |
| `pr-flashinfer-1396` | upstream-code | [`sources/prs/flashinfer/PR-1396.md`](../sources/prs/flashinfer/PR-1396.md) | gpt-oss: Add MXFP8 x MXFP4 CUTLASS MOE for SM100 and BF16 x MXFP4 CUTLASS for SM90 + SwigluBias Activation |
| `pr-flashinfer-1397` | upstream-code | [`sources/prs/flashinfer/PR-1397.md`](../sources/prs/flashinfer/PR-1397.md) | feature: add cutlass as bmm_fp8 backend. |
| `pr-flashinfer-1435` | upstream-code | [`sources/prs/flashinfer/PR-1435.md`](../sources/prs/flashinfer/PR-1435.md) | bugfix: fix perf issue by using fp8 graph that can use cublaslt |
| `pr-flashinfer-1445` | upstream-code | [`sources/prs/flashinfer/PR-1445.md`](../sources/prs/flashinfer/PR-1445.md) | Add alignment in MxFP8Quantization |
| `pr-flashinfer-1446` | upstream-code | [`sources/prs/flashinfer/PR-1446.md`](../sources/prs/flashinfer/PR-1446.md) | Remove getEnvEnablePDL in favor of enable_pdl parameter |
| `pr-flashinfer-1473` | upstream-code | [`sources/prs/flashinfer/PR-1473.md`](../sources/prs/flashinfer/PR-1473.md) | perf: add 1x4x1 cluster shape for fp8 bmm M<16 cases |
| `pr-flashinfer-1479` | upstream-code | [`sources/prs/flashinfer/PR-1479.md`](../sources/prs/flashinfer/PR-1479.md) | refactor: unify autotuner for bmm_fp8 |
| `pr-flashinfer-1490` | upstream-code | [`sources/prs/flashinfer/PR-1490.md`](../sources/prs/flashinfer/PR-1490.md) | feat: Support fp8 qkv, fp16/bf16 out MHA for trtllm-gen. |
| `pr-flashinfer-1491` | upstream-code | [`sources/prs/flashinfer/PR-1491.md`](../sources/prs/flashinfer/PR-1491.md) | Perf: support scale_a/scale_b instead of combined scale in cutlass bmm_fp8 |
| `pr-flashinfer-1512` | upstream-code | [`sources/prs/flashinfer/PR-1512.md`](../sources/prs/flashinfer/PR-1512.md) | flashinfer_benchmark QoL Improvements and Attention FP8 Support |
| `pr-flashinfer-1530` | upstream-code | [`sources/prs/flashinfer/PR-1530.md`](../sources/prs/flashinfer/PR-1530.md) | bugfix: Fix compile error for undefined swizzle enum. |
| `pr-flashinfer-1540` | upstream-code | [`sources/prs/flashinfer/PR-1540.md`](../sources/prs/flashinfer/PR-1540.md) | feat: Add fp8-qkv, fp16/bf16 output MHA |
| `pr-flashinfer-1599` | upstream-code | [`sources/prs/flashinfer/PR-1599.md`](../sources/prs/flashinfer/PR-1599.md) | bugfix: fix unittest test_fp8_quantize |
| `pr-flashinfer-1608` | upstream-code | [`sources/prs/flashinfer/PR-1608.md`](../sources/prs/flashinfer/PR-1608.md) | feat: initial support for SM103, SM110, SM120, SM121 |
| `pr-flashinfer-1610` | upstream-code | [`sources/prs/flashinfer/PR-1610.md`](../sources/prs/flashinfer/PR-1610.md) | feat: cutlass fp8 gemm bringup for SM120 & SM121 |
| `pr-flashinfer-1656` | upstream-code | [`sources/prs/flashinfer/PR-1656.md`](../sources/prs/flashinfer/PR-1656.md) | Add benchmark for MLARopeQuantize |
| `pr-flashinfer-1661` | upstream-code | [`sources/prs/flashinfer/PR-1661.md`](../sources/prs/flashinfer/PR-1661.md) | perf&bugfix: skip kv-tile computation out of sliding window in FA2; fix __syncthreads in mergestate |
| `pr-flashinfer-1668` | upstream-code | [`sources/prs/flashinfer/PR-1668.md`](../sources/prs/flashinfer/PR-1668.md) | TGV GEMM as a BF16 backend alternative to cuBLAS |
| `pr-flashinfer-1694` | upstream-code | [`sources/prs/flashinfer/PR-1694.md`](../sources/prs/flashinfer/PR-1694.md) | Update deepgemm backend for 103a |
| `pr-flashinfer-1710` | upstream-code | [`sources/prs/flashinfer/PR-1710.md`](../sources/prs/flashinfer/PR-1710.md) | test: skip the unsupported test cases for sm120/121 |
| `pr-flashinfer-1725` | upstream-code | [`sources/prs/flashinfer/PR-1725.md`](../sources/prs/flashinfer/PR-1725.md) | TVM: support TVM binding for GroupedGemm |
| `pr-flashinfer-1767` | upstream-code | [`sources/prs/flashinfer/PR-1767.md`](../sources/prs/flashinfer/PR-1767.md) | tests: skip non SM100/103 for grouped deepgemm |
| `pr-flashinfer-1769` | upstream-code | [`sources/prs/flashinfer/PR-1769.md`](../sources/prs/flashinfer/PR-1769.md) | feat: add xqa fp8 mha and fp8 kv cache |
| `pr-flashinfer-1819` | upstream-code | [`sources/prs/flashinfer/PR-1819.md`](../sources/prs/flashinfer/PR-1819.md) | feat:enable fp8 blockscale moe for fused cultass for sm90 |
| `pr-flashinfer-1829` | upstream-code | [`sources/prs/flashinfer/PR-1829.md`](../sources/prs/flashinfer/PR-1829.md) | feat: trtrllm-gen global scaled FP8 GEMMs |
| `pr-flashinfer-1862` | upstream-code | [`sources/prs/flashinfer/PR-1862.md`](../sources/prs/flashinfer/PR-1862.md) | raise error for group_gemm_fp8_nt_groupwise then num_groups > 1 on sm120/121 |
| `pr-flashinfer-1883` | upstream-code | [`sources/prs/flashinfer/PR-1883.md`](../sources/prs/flashinfer/PR-1883.md) | misc: fix some B200 GEMM bench |
| `pr-flashinfer-1924` | upstream-code | [`sources/prs/flashinfer/PR-1924.md`](../sources/prs/flashinfer/PR-1924.md) | MLA RoPE + quantization fused kernel: shape generalization for MHA / GQA |
| `pr-flashinfer-1961` | upstream-code | [`sources/prs/flashinfer/PR-1961.md`](../sources/prs/flashinfer/PR-1961.md) | Fix: Verify scales are not None for Cutlass FP8 FusedMoE |
| `pr-flashinfer-1969` | upstream-code | [`sources/prs/flashinfer/PR-1969.md`](../sources/prs/flashinfer/PR-1969.md) | feat: enable deepgemm jit for fp8 block-scale on SM90 |
| `pr-flashinfer-1982` | upstream-code | [`sources/prs/flashinfer/PR-1982.md`](../sources/prs/flashinfer/PR-1982.md) | fix: correct PDL parameter handling in RopeQuantize kernel |
| `pr-flashinfer-2020` | upstream-code | [`sources/prs/flashinfer/PR-2020.md`](../sources/prs/flashinfer/PR-2020.md) | update trtllm cutlass moe  |
| `pr-flashinfer-2029` | upstream-code | [`sources/prs/flashinfer/PR-2029.md`](../sources/prs/flashinfer/PR-2029.md) | feat: suitable_auto_backends to prune auto backends, bmm_fp8 refactor, heuristic_func intake |
| `pr-flashinfer-2030` | upstream-code | [`sources/prs/flashinfer/PR-2030.md`](../sources/prs/flashinfer/PR-2030.md) | Enable renormalize(naive) routing for fp8 per-tensor |
| `pr-flashinfer-2035` | upstream-code | [`sources/prs/flashinfer/PR-2035.md`](../sources/prs/flashinfer/PR-2035.md) | Added an initial implementation of Q and KV Cache in fp8 and to use t… |
| `pr-flashinfer-2037` | upstream-code | [`sources/prs/flashinfer/PR-2037.md`](../sources/prs/flashinfer/PR-2037.md) | feat: Add flashinfer.rope.rope_quantize_fp8_append_paged_kv_cache (fused RoPE + Q + KV cache, supports MLA/GQA/MHA)  |
| `pr-flashinfer-2047` | upstream-code | [`sources/prs/flashinfer/PR-2047.md`](../sources/prs/flashinfer/PR-2047.md) | Rebase FP8 SM100 Cutlass FMHA Attention to main (original PR#1238) |
| `pr-flashinfer-2061` | upstream-code | [`sources/prs/flashinfer/PR-2061.md`](../sources/prs/flashinfer/PR-2061.md) | Fix moe fp8 failure for sm121 |
| `pr-flashinfer-2063` | upstream-code | [`sources/prs/flashinfer/PR-2063.md`](../sources/prs/flashinfer/PR-2063.md) | perf: TRT-LLM MoE Block-FP8 activation optimization |
| `pr-flashinfer-2081` | upstream-code | [`sources/prs/flashinfer/PR-2081.md`](../sources/prs/flashinfer/PR-2081.md) | enable xqa fp8 output |
| `pr-flashinfer-2111` | upstream-code | [`sources/prs/flashinfer/PR-2111.md`](../sources/prs/flashinfer/PR-2111.md) | refactor: update fa3 codebase and fix hopper unittest [part 1] |
| `pr-flashinfer-2129` | upstream-code | [`sources/prs/flashinfer/PR-2129.md`](../sources/prs/flashinfer/PR-2129.md) | fix: Fix bench_mm_fp8.py |
| `pr-flashinfer-2131` | upstream-code | [`sources/prs/flashinfer/PR-2131.md`](../sources/prs/flashinfer/PR-2131.md) | make DeepGEMM swapAB available for linear gemm SM90 |
| `pr-flashinfer-2142` | upstream-code | [`sources/prs/flashinfer/PR-2142.md`](../sources/prs/flashinfer/PR-2142.md) | feat: TRTLLM FMHAv2 backend for ctx attention |
| `pr-flashinfer-2148` | upstream-code | [`sources/prs/flashinfer/PR-2148.md`](../sources/prs/flashinfer/PR-2148.md) | Enable Hopper FA3 FP8 attention in decode.py |
| `pr-flashinfer-2241` | upstream-code | [`sources/prs/flashinfer/PR-2241.md`](../sources/prs/flashinfer/PR-2241.md) | Fp8 attention are now part of cuDNN 9.17.1 |
| `pr-flashinfer-2243` | upstream-code | [`sources/prs/flashinfer/PR-2243.md`](../sources/prs/flashinfer/PR-2243.md) | feat: RMSNorm/Fused RMSNorm + FP8 Quantization kernels |
| `pr-flashinfer-2255` | upstream-code | [`sources/prs/flashinfer/PR-2255.md`](../sources/prs/flashinfer/PR-2255.md) | fix: support int64 IdType for RoPE part argument in `rope_quantize_fp8_append_paged_kv_cache` |
| `pr-flashinfer-2256` | upstream-code | [`sources/prs/flashinfer/PR-2256.md`](../sources/prs/flashinfer/PR-2256.md) | feat: Add support for bmm mxfp8 |
| `pr-flashinfer-2261` | upstream-code | [`sources/prs/flashinfer/PR-2261.md`](../sources/prs/flashinfer/PR-2261.md) | Fix CUTLASS FP8 gemm correctness issue on SM120/SM121 for shapes where N is not divisible by ScaleGranularityN. |
| `pr-flashinfer-2304` | upstream-code | [`sources/prs/flashinfer/PR-2304.md`](../sources/prs/flashinfer/PR-2304.md) | feat: Support Fused MoE non gated Relu2 NVFP4 & FP8 and support Nemotron |
| `pr-flashinfer-2327` | upstream-code | [`sources/prs/flashinfer/PR-2327.md`](../sources/prs/flashinfer/PR-2327.md) | [perf] Improve gemm_fp8_nt_groupwise (cutlass backend) by 10-40% for batch sizes <= 32 |
| `pr-flashinfer-2328` | upstream-code | [`sources/prs/flashinfer/PR-2328.md`](../sources/prs/flashinfer/PR-2328.md) | fix: guard batchWarpReduceSum with ENABLE_FP8 to fix compilation without FP8 |
| `pr-flashinfer-2441` | upstream-code | [`sources/prs/flashinfer/PR-2441.md`](../sources/prs/flashinfer/PR-2441.md) | fix: Fix NaN output in mxfp8_quantize for very small input values |
| `pr-flashinfer-2443` | upstream-code | [`sources/prs/flashinfer/PR-2443.md`](../sources/prs/flashinfer/PR-2443.md) | Add cute-dsl backends to mxfp[8,4]_quantization for future refactor |
| `pr-flashinfer-2446` | upstream-code | [`sources/prs/flashinfer/PR-2446.md`](../sources/prs/flashinfer/PR-2446.md) | feat: Add TRTLLM fmha_v2 library for SM90 attention with Skip-Softmax  |
| `pr-flashinfer-2462` | upstream-code | [`sources/prs/flashinfer/PR-2462.md`](../sources/prs/flashinfer/PR-2462.md) | feat: Support Fused MoE non gated Relu2 NVFP4 & FP8 and support Nemotron, fixed |
| `pr-flashinfer-2464` | upstream-code | [`sources/prs/flashinfer/PR-2464.md`](../sources/prs/flashinfer/PR-2464.md) | feat: Add MXFP8 GEMM mm_mxfp8 (cutlass) |
| `pr-flashinfer-2505` | upstream-code | [`sources/prs/flashinfer/PR-2505.md`](../sources/prs/flashinfer/PR-2505.md) | Feat: Trtllm-gen MxFP8 MoE integration |
| `pr-flashinfer-2533` | upstream-code | [`sources/prs/flashinfer/PR-2533.md`](../sources/prs/flashinfer/PR-2533.md) | fix: include fp8_blockscale_gemm_90 in AOT jit-cache |
| `pr-flashinfer-2534` | upstream-code | [`sources/prs/flashinfer/PR-2534.md`](../sources/prs/flashinfer/PR-2534.md) | fix: support fp32 logits for fp8_per_tensor and fp8_block |
| `pr-flashinfer-2536` | upstream-code | [`sources/prs/flashinfer/PR-2536.md`](../sources/prs/flashinfer/PR-2536.md) | fallback to fa2 (instead of fa3) for unsupported configuration (bf16 Q, Fp8 KV) |
| `pr-flashinfer-2538` | upstream-code | [`sources/prs/flashinfer/PR-2538.md`](../sources/prs/flashinfer/PR-2538.md) | tests: bmm_fp8 for SM110 |
| `pr-flashinfer-2549` | upstream-code | [`sources/prs/flashinfer/PR-2549.md`](../sources/prs/flashinfer/PR-2549.md) | Add gen_gemm_sm100_module_cutlass_mxfp8 to jit-cache |
| `pr-flashinfer-2581` | upstream-code | [`sources/prs/flashinfer/PR-2581.md`](../sources/prs/flashinfer/PR-2581.md) | Implement `cutlass_fused_moe` mxfp8 |
| `pr-flashinfer-2631` | upstream-code | [`sources/prs/flashinfer/PR-2631.md`](../sources/prs/flashinfer/PR-2631.md) | fix: add SM121 support to SM120 version guards |
| `pr-flashinfer-2635` | upstream-code | [`sources/prs/flashinfer/PR-2635.md`](../sources/prs/flashinfer/PR-2635.md) | benchmark: Add MXFP4/MXFP8 quantization mode support to FP4 MoE benchmark |
| `pr-flashinfer-2642` | upstream-code | [`sources/prs/flashinfer/PR-2642.md`](../sources/prs/flashinfer/PR-2642.md) | [fp8_blockwise]Fix int32 overflow in TRTLLM fused MoE activation kernel |
| `pr-flashinfer-2653` | upstream-code | [`sources/prs/flashinfer/PR-2653.md`](../sources/prs/flashinfer/PR-2653.md) | [feat] trtllm-gen mxfp8 gemm |
| `pr-flashinfer-2660` | upstream-code | [`sources/prs/flashinfer/PR-2660.md`](../sources/prs/flashinfer/PR-2660.md) | feat: support mxfp4 & mxfp8 entrypoint for blackwell cutedsl dense gemm |
| `pr-flashinfer-2666` | upstream-code | [`sources/prs/flashinfer/PR-2666.md`](../sources/prs/flashinfer/PR-2666.md) | benchmarks: Add FP8 input / BF16 output in ragged prefill benchmark |
| `pr-flashinfer-2667` | upstream-code | [`sources/prs/flashinfer/PR-2667.md`](../sources/prs/flashinfer/PR-2667.md) | perf: Update trtllm-gen batched GEMM kernels - faster, more NVFP4 tile dims, MXFP8 with relu2 act |
| `pr-flashinfer-2707` | upstream-code | [`sources/prs/flashinfer/PR-2707.md`](../sources/prs/flashinfer/PR-2707.md) | feat: Add support for TRTLLM MXFP8 non-gated MoE with ReLU2 |
| `pr-flashinfer-2738` | upstream-code | [`sources/prs/flashinfer/PR-2738.md`](../sources/prs/flashinfer/PR-2738.md) | Support for MXFP4 and NVFP4 group GEMMs on GeForce and Spark |
| `pr-flashinfer-2739` | upstream-code | [`sources/prs/flashinfer/PR-2739.md`](../sources/prs/flashinfer/PR-2739.md) | Support in-place update for `trtllm_fp8_block_scale_moe` |
| `pr-flashinfer-2743` | upstream-code | [`sources/prs/flashinfer/PR-2743.md`](../sources/prs/flashinfer/PR-2743.md) | Add cute dsl mla decode op |
| `pr-flashinfer-2751` | upstream-code | [`sources/prs/flashinfer/PR-2751.md`](../sources/prs/flashinfer/PR-2751.md) | [Spark unit test debugging] Fix for tests/gemm/test_groupwise_scaled_gemm_fp8.py |
| `pr-flashinfer-2779` | upstream-code | [`sources/prs/flashinfer/PR-2779.md`](../sources/prs/flashinfer/PR-2779.md) | feat: FP8 output support for CUTLASS MLA paged attention |
| `pr-flashinfer-2805` | upstream-code | [`sources/prs/flashinfer/PR-2805.md`](../sources/prs/flashinfer/PR-2805.md) | [CuTe DSL] Add modular FMHA prefill and MLA decode attention kernels |
| `pr-flashinfer-2841` | upstream-code | [`sources/prs/flashinfer/PR-2841.md`](../sources/prs/flashinfer/PR-2841.md) | [Perf] Add FMHAv2 to flashinfer_benchmark.py and eliminate unnecessary H2D |
| `pr-flashinfer-2882` | upstream-code | [`sources/prs/flashinfer/PR-2882.md`](../sources/prs/flashinfer/PR-2882.md) | Fix silent bug with FP8 per tensor non-gated MoE |
| `pr-flashinfer-2901` | upstream-code | [`sources/prs/flashinfer/PR-2901.md`](../sources/prs/flashinfer/PR-2901.md) | feat: add pdl support for cute dsl mla decode kernel support |
| `pr-flashinfer-2902` | upstream-code | [`sources/prs/flashinfer/PR-2902.md`](../sources/prs/flashinfer/PR-2902.md) | feat: add MXFP8 GEMM support for SM120 |
| `pr-flashinfer-2904` | upstream-code | [`sources/prs/flashinfer/PR-2904.md`](../sources/prs/flashinfer/PR-2904.md) | perf: Optimize CuTe-DSL fp4 and fp8 quantization kernels |
| `pr-flashinfer-2913` | upstream-code | [`sources/prs/flashinfer/PR-2913.md`](../sources/prs/flashinfer/PR-2913.md) | [NVIDIA] fix(jit): enable GDC for CUTLASS fused MoE PDL — prevent random crashes on SM12x |
| `pr-flashinfer-2914` | upstream-code | [`sources/prs/flashinfer/PR-2914.md`](../sources/prs/flashinfer/PR-2914.md) | feat: Add cuBLASLt backend for `mm_bf16` and enable multi-tactic autotuning for FP8/MXFP8 runners |
| `pr-flashinfer-2959` | upstream-code | [`sources/prs/flashinfer/PR-2959.md`](../sources/prs/flashinfer/PR-2959.md) | [Fmha] Add head_dim=512 support for trtllm attention kernels |
| `pr-flashinfer-2994` | upstream-code | [`sources/prs/flashinfer/PR-2994.md`](../sources/prs/flashinfer/PR-2994.md) |   Fix MXFP4/MXFP8 failures in SM120 FAST_BUILD and expand all_tiles[]                                                   |
| `pr-flashinfer-3039` | upstream-code | [`sources/prs/flashinfer/PR-3039.md`](../sources/prs/flashinfer/PR-3039.md) | feat: Integrate CuTe DSL FMHA prefill kernels by loading cubin |
| `pr-flashinfer-3059` | upstream-code | [`sources/prs/flashinfer/PR-3059.md`](../sources/prs/flashinfer/PR-3059.md) | Support Allreduce + Norm + Per-token Group Fp8 Quant Fusion |
| `pr-flashinfer-3084` | upstream-code | [`sources/prs/flashinfer/PR-3084.md`](../sources/prs/flashinfer/PR-3084.md) | perf: optimize MXFP4xBF16 & INT4xFP8 CUTLASS MoE backend for SM90 |
| `pr-flashinfer-3115` | upstream-code | [`sources/prs/flashinfer/PR-3115.md`](../sources/prs/flashinfer/PR-3115.md) | perf(autotuner): replace power-of-2 token buckets with hybrid spacing & fix missing routing_replay_out arg |
| `pr-flashinfer-3129` | upstream-code | [`sources/prs/flashinfer/PR-3129.md`](../sources/prs/flashinfer/PR-3129.md) | feat: Enable FP8 (E4M3/E5M2) in concat_mla_k for optimize long-context prefill performance and refactor type dispatch for BF16/FP16 |
| `pr-flashinfer-3132` | upstream-code | [`sources/prs/flashinfer/PR-3132.md`](../sources/prs/flashinfer/PR-3132.md) | [CuTe DSL] Fix FP8 MLA persistent perf regression and ProxyKind cu13 wheel breakage |
| `pr-flashinfer-3152` | upstream-code | [`sources/prs/flashinfer/PR-3152.md`](../sources/prs/flashinfer/PR-3152.md) | Integrate CUTLASS Small Tile N Blockscaled GEMMs/Grouped GEMMs for SM120 and SM121 |
| `pr-flashinfer-3181` | upstream-code | [`sources/prs/flashinfer/PR-3181.md`](../sources/prs/flashinfer/PR-3181.md) | cute-dsl fmha prefill (cubin integration): remove front-padding, add attention_sink, and pdl support |
| `pr-flashinfer-3216` | upstream-code | [`sources/prs/flashinfer/PR-3216.md`](../sources/prs/flashinfer/PR-3216.md) | fix(cute_dsl/moe): make autotuner bucket configuration adapt to runtime input |
| `pr-flashinfer-3227` | upstream-code | [`sources/prs/flashinfer/PR-3227.md`](../sources/prs/flashinfer/PR-3227.md) | [Bugfix] Fix fused MoE autotuning correctness issues by filtering clusterDimZ |
| `pr-flashinfer-3235` | upstream-code | [`sources/prs/flashinfer/PR-3235.md`](../sources/prs/flashinfer/PR-3235.md) | Support Kimi K2.5 H64 CuTe DSL MLA decode |
| `pr-flashinfer-3239` | upstream-code | [`sources/prs/flashinfer/PR-3239.md`](../sources/prs/flashinfer/PR-3239.md) | Update moe gemm |
| `pr-flashinfer-3271` | upstream-code | [`sources/prs/flashinfer/PR-3271.md`](../sources/prs/flashinfer/PR-3271.md) | feat(moe): add SM120 W4A16 b12x kernels |
| `pr-flashinfer-3276` | upstream-code | [`sources/prs/flashinfer/PR-3276.md`](../sources/prs/flashinfer/PR-3276.md) | fix(fmha_v2): fix FP8 V-scratch pipeline and varlen scheduler on SM90 |
| `pr-flashinfer-869` | upstream-code | [`sources/prs/flashinfer/PR-869.md`](../sources/prs/flashinfer/PR-869.md) | Naive Support for Hopper FP8 Prefill Kernel with Per-Head Quantization |
| `pr-flashinfer-969` | upstream-code | [`sources/prs/flashinfer/PR-969.md`](../sources/prs/flashinfer/PR-969.md) | perf: Fix python API overhead when CUDAGraph is not enabled |
| `pr-sglang-10491` | upstream-code | [`sources/prs/sglang/PR-10491.md`](../sources/prs/sglang/PR-10491.md) | Update CUTLASS. Refine KernelSchedule for fp8 (grouped) gemm. |
| `pr-sglang-11081` | upstream-code | [`sources/prs/sglang/PR-11081.md`](../sources/prs/sglang/PR-11081.md) | Fix DSR1 accuracy for flashinfer_trtllm MoE with FP8 quantization |
| `pr-sglang-11432` | upstream-code | [`sources/prs/sglang/PR-11432.md`](../sources/prs/sglang/PR-11432.md) | [sgl-kernel][1/N]Support Expert Specialization Grouped GEMM |
| `pr-sglang-11655` | upstream-code | [`sources/prs/sglang/PR-11655.md`](../sources/prs/sglang/PR-11655.md) | [DeepseekV32] Enable flashmla_prefill kernel with fp8 kvcache |
| `pr-sglang-11708` | upstream-code | [`sources/prs/sglang/PR-11708.md`](../sources/prs/sglang/PR-11708.md) | Support running FP4 Deepseek on SM120. |
| `pr-sglang-11805` | upstream-code | [`sources/prs/sglang/PR-11805.md`](../sources/prs/sglang/PR-11805.md) | Change bf16 to fp8 for some gemms in attention for DeepSeek ckpt v2 |
| `pr-sglang-11866` | upstream-code | [`sources/prs/sglang/PR-11866.md`](../sources/prs/sglang/PR-11866.md) | Support nvidia/NVIDIA-Nemotron-Nano-9B-v2-FP8/NVFP4 |
| `pr-sglang-12018` | upstream-code | [`sources/prs/sglang/PR-12018.md`](../sources/prs/sglang/PR-12018.md) | Feature/nano v2 offline modelopt fp8 and nvfp4 |
| `pr-sglang-12080` | upstream-code | [`sources/prs/sglang/PR-12080.md`](../sources/prs/sglang/PR-12080.md) | [sgl-kernel][4/N]Support Expert Specialization Grouped GEMM |
| `pr-sglang-12259` | upstream-code | [`sources/prs/sglang/PR-12259.md`](../sources/prs/sglang/PR-12259.md) | [hotfix] missing `w13_weight_fp8` and `w2_weight_fp8` in UE8M0 requantization |
| `pr-sglang-12543` | upstream-code | [`sources/prs/sglang/PR-12543.md`](../sources/prs/sglang/PR-12543.md) | Enable Flashinfer TRTLLM-GEN-MoE FP8 blockwise kernel for Qwen3-Next on Blackwell |
| `pr-sglang-13087` | upstream-code | [`sources/prs/sglang/PR-13087.md`](../sources/prs/sglang/PR-13087.md) | [sgl-kernel] support custom fp8 flashmla kernel |
| `pr-sglang-13147` | upstream-code | [`sources/prs/sglang/PR-13147.md`](../sources/prs/sglang/PR-13147.md) | Aiter fp8 kv cache |
| `pr-sglang-13264` | upstream-code | [`sources/prs/sglang/PR-13264.md`](../sources/prs/sglang/PR-13264.md) | [NVIDIA] Fix broken fp8 MoE of deepseek v3 |
| `pr-sglang-13274` | upstream-code | [`sources/prs/sglang/PR-13274.md`](../sources/prs/sglang/PR-13274.md) | [NVIDIA] Fix use case of SGLANG_ENABLE_FLASHINFER_GEMM |
| `pr-sglang-13617` | upstream-code | [`sources/prs/sglang/PR-13617.md`](../sources/prs/sglang/PR-13617.md) | [ROCM] Optimized deepseek-r1 fp8 model with + triton_gemm_a8w8 + batch_gemm_a8w8 + fused set_mla_kv_buffer kernel |
| `pr-sglang-13731` | upstream-code | [`sources/prs/sglang/PR-13731.md`](../sources/prs/sglang/PR-13731.md) | [sgl-kernel][Feat][B200][1/N]Support MXFP8 Grouped GEMM in Blackwell |
| `pr-sglang-13794` | upstream-code | [`sources/prs/sglang/PR-13794.md`](../sources/prs/sglang/PR-13794.md) | Support fp4 fp8 non gated moe |
| `pr-sglang-13873` | upstream-code | [`sources/prs/sglang/PR-13873.md`](../sources/prs/sglang/PR-13873.md) | Feat: GLM-4.6 supports shared experts fusion |
| `pr-sglang-13910` | upstream-code | [`sources/prs/sglang/PR-13910.md`](../sources/prs/sglang/PR-13910.md) | Fix update weight error for blackwell DeepGEMM |
| `pr-sglang-13959` | upstream-code | [`sources/prs/sglang/PR-13959.md`](../sources/prs/sglang/PR-13959.md) | [DeepSeek v3.2] opt Context Parallelism: support fused moe, multi batch and fp8 kvcache |
| `pr-sglang-14213` | upstream-code | [`sources/prs/sglang/PR-14213.md`](../sources/prs/sglang/PR-14213.md) | Add Mistral Large 3 support. |
| `pr-sglang-14385` | upstream-code | [`sources/prs/sglang/PR-14385.md`](../sources/prs/sglang/PR-14385.md) | [CPU] Implement MXFP4 Gemm kernels for intel AMX to support GPT OSS series. |
| `pr-sglang-14395` | upstream-code | [`sources/prs/sglang/PR-14395.md`](../sources/prs/sglang/PR-14395.md) | Support FP8 MLA prefill and 128k context. |
| `pr-sglang-14466` | upstream-code | [`sources/prs/sglang/PR-14466.md`](../sources/prs/sglang/PR-14466.md) | Add Mistral Large 3 Eagle Support |
| `pr-sglang-14640` | upstream-code | [`sources/prs/sglang/PR-14640.md`](../sources/prs/sglang/PR-14640.md) | [sgl-kernel][Feat][B200][2/N] Support MXFP8 Grouped GEMM in Blackwell |
| `pr-sglang-15422` | upstream-code | [`sources/prs/sglang/PR-15422.md`](../sources/prs/sglang/PR-15422.md) | Flashinfer MOE FP8 support for Mistral Large 3. |
| `pr-sglang-15471` | upstream-code | [`sources/prs/sglang/PR-15471.md`](../sources/prs/sglang/PR-15471.md) | [sgl-kernel][6/7]Support Expert Specialization Grouped GEMM |
| `pr-sglang-15514` | upstream-code | [`sources/prs/sglang/PR-15514.md`](../sources/prs/sglang/PR-15514.md) | [Perf] Add Flashinfer DeepGEMM SM90 for SwapAB Optimization |
| `pr-sglang-15522` | upstream-code | [`sources/prs/sglang/PR-15522.md`](../sources/prs/sglang/PR-15522.md) | Optimize FP8 MLA KV cache writes with Triton kernel |
| `pr-sglang-15836` | upstream-code | [`sources/prs/sglang/PR-15836.md`](../sources/prs/sglang/PR-15836.md) | [JIT kernel] Apply jit per_tensor_quant_fp8 kernel |
| `pr-sglang-16622` | upstream-code | [`sources/prs/sglang/PR-16622.md`](../sources/prs/sglang/PR-16622.md) | Fix FP8 MoE NaN with DeepGEMM on Blackwell |
| `pr-sglang-17235` | upstream-code | [`sources/prs/sglang/PR-17235.md`](../sources/prs/sglang/PR-17235.md) | [GLM 4.7] Add RTX 6000 Pro aka sm120 |
| `pr-sglang-17327` | upstream-code | [`sources/prs/sglang/PR-17327.md`](../sources/prs/sglang/PR-17327.md) | Disable mla persistent kernel when not using fp8 kv_cache |
| `pr-sglang-17449` | upstream-code | [`sources/prs/sglang/PR-17449.md`](../sources/prs/sglang/PR-17449.md) | Add mxfp8 support for online quantization, Triton dense linear, and CUTLASS MoE |
| `pr-sglang-18242` | upstream-code | [`sources/prs/sglang/PR-18242.md`](../sources/prs/sglang/PR-18242.md) | [ROCm] Optimize Deepseek R1 on MI300X |
| `pr-sglang-18389` | upstream-code | [`sources/prs/sglang/PR-18389.md`](../sources/prs/sglang/PR-18389.md) | Nsa trtllm mla sparse fp8 support with Deepseek v3.2 NVFP4 |
| `pr-sglang-18423` | upstream-code | [`sources/prs/sglang/PR-18423.md`](../sources/prs/sglang/PR-18423.md) | [AMD] Update aiter to v0.1.10.post2 |
| `pr-sglang-18528` | upstream-code | [`sources/prs/sglang/PR-18528.md`](../sources/prs/sglang/PR-18528.md) | Fp8 prefill attn kernel integration |
| `pr-sglang-18742` | upstream-code | [`sources/prs/sglang/PR-18742.md`](../sources/prs/sglang/PR-18742.md) | [RL] Support per-layer mixed FP8/BF16 serving for FP8 checkpoints |
| `pr-sglang-18750` | upstream-code | [`sources/prs/sglang/PR-18750.md`](../sources/prs/sglang/PR-18750.md) | fix(sgl-kernel): use >= 120 for SM12x CUDA kernel dispatch |
| `pr-sglang-19148` | upstream-code | [`sources/prs/sglang/PR-19148.md`](../sources/prs/sglang/PR-19148.md) | [DeepSeek-V3.2][JIT-kernel] Support nsa fuse store indexer k cache |
| `pr-sglang-19537` | upstream-code | [`sources/prs/sglang/PR-19537.md`](../sources/prs/sglang/PR-19537.md) | [FlashInfer v0.6.4] [RL] Integrate FlashInfer mxfp8 gemm, MoE, and routed MoE |
| `pr-sglang-19721` | upstream-code | [`sources/prs/sglang/PR-19721.md`](../sources/prs/sglang/PR-19721.md) | Various SM120 improvements |
| `pr-sglang-19935` | upstream-code | [`sources/prs/sglang/PR-19935.md`](../sources/prs/sglang/PR-19935.md) | [AMD] Fix FP8 assertion failure in aiter MLA decode by falling back to self.k_scale |
| `pr-sglang-20082` | upstream-code | [`sources/prs/sglang/PR-20082.md`](../sources/prs/sglang/PR-20082.md) | Enable modelopt quantized FLUX deployment |
| `pr-sglang-20187` | upstream-code | [`sources/prs/sglang/PR-20187.md`](../sources/prs/sglang/PR-20187.md) | [AMD] Fp8 prefill integration with radix cache path for dpsk models |
| `pr-sglang-20305` | upstream-code | [`sources/prs/sglang/PR-20305.md`](../sources/prs/sglang/PR-20305.md) | [Benchmark] use flashinfer bench_gpu_time instead of triton do_bench |
| `pr-sglang-20394` | upstream-code | [`sources/prs/sglang/PR-20394.md`](../sources/prs/sglang/PR-20394.md) | [NVIDIA] Enable fp8 flashinfer_trtllm_routed MoE for MiniMax-M2.5 |
| `pr-sglang-20479` | upstream-code | [`sources/prs/sglang/PR-20479.md`](../sources/prs/sglang/PR-20479.md) | Support Triton MLA FP8 KV cache |
| `pr-sglang-20606` | upstream-code | [`sources/prs/sglang/PR-20606.md`](../sources/prs/sglang/PR-20606.md) | FIX: (NSA) Compute topk_indices_offset when NSA prefill flashmla_sparse is used with FP8 KV cache |
| `pr-sglang-20887` | upstream-code | [`sources/prs/sglang/PR-20887.md`](../sources/prs/sglang/PR-20887.md) | CUTLASS FP8 Blockwise GEMM improvement of SM120 |
| `pr-sglang-20910` | upstream-code | [`sources/prs/sglang/PR-20910.md`](../sources/prs/sglang/PR-20910.md) | Add SGLang CUDA crash API logging inspired by FlashInfer |
| `pr-sglang-20988` | upstream-code | [`sources/prs/sglang/PR-20988.md`](../sources/prs/sglang/PR-20988.md) | ci: run Stage A CUDA tests as stage-a-test-small-1-gpu on 5090 |
| `pr-sglang-21213` | upstream-code | [`sources/prs/sglang/PR-21213.md`](../sources/prs/sglang/PR-21213.md) | [AMD]: Support MLA with nhead<16 and FP8 KV cache for TP=8 (Kimi K2.5… |
| `pr-sglang-21239` | upstream-code | [`sources/prs/sglang/PR-21239.md`](../sources/prs/sglang/PR-21239.md) | Refactor JIT kernel CI to use run_suite.py registration system |
| `pr-sglang-21280` | upstream-code | [`sources/prs/sglang/PR-21280.md`](../sources/prs/sglang/PR-21280.md) | [RL] Support mxfp8 DeepSeek V3 |
| `pr-sglang-21321` | upstream-code | [`sources/prs/sglang/PR-21321.md`](../sources/prs/sglang/PR-21321.md) | [Kernel] Support FlashInfer TRTLLM-Gen fused MoE for non-gated FP4 & FP8 (Nemotron) |
| `pr-sglang-21325` | upstream-code | [`sources/prs/sglang/PR-21325.md`](../sources/prs/sglang/PR-21325.md) | [misc] clean up kernel API |
| `pr-sglang-21463` | upstream-code | [`sources/prs/sglang/PR-21463.md`](../sources/prs/sglang/PR-21463.md) | Migrate all callers from /get_server_info to /server_info |
| `pr-sglang-21511` | upstream-code | [`sources/prs/sglang/PR-21511.md`](../sources/prs/sglang/PR-21511.md) | [AMD] Enable FP8 KV cache and FP8 attention kernel for NSA on MI300/MI355 with TileLang backend |
| `pr-sglang-21576` | upstream-code | [`sources/prs/sglang/PR-21576.md`](../sources/prs/sglang/PR-21576.md) | [FlashInver v0.6.7] Integrate flashinfer_trtllm mxfp8 gemm |
| `pr-sglang-21710` | upstream-code | [`sources/prs/sglang/PR-21710.md`](../sources/prs/sglang/PR-21710.md) | [AMD] Add GLM-5-FP8 nightly performance benchmarks for MI30x and MI35x |
| `pr-sglang-21734` | upstream-code | [`sources/prs/sglang/PR-21734.md`](../sources/prs/sglang/PR-21734.md) | perf: optimize PCG inductor path for FP8 models |
| `pr-sglang-21888` | upstream-code | [`sources/prs/sglang/PR-21888.md`](../sources/prs/sglang/PR-21888.md) | fix pcg torch dynamo recompile in mxfp8 Triton path |
| `pr-sglang-22006` | upstream-code | [`sources/prs/sglang/PR-22006.md`](../sources/prs/sglang/PR-22006.md) | Tiny fix trtllm_fp8_per_tensor_scale_moe_wrapper router_logits dtype |
| `pr-sglang-22258` | upstream-code | [`sources/prs/sglang/PR-22258.md`](../sources/prs/sglang/PR-22258.md) | [AMD][HIP] NSA: bf16 passthrough from RMSNorm to eliminate FP8 dequantization |
| `pr-sglang-22316` | upstream-code | [`sources/prs/sglang/PR-22316.md`](../sources/prs/sglang/PR-22316.md) | [Reland] DeepSeek-R1-0528-w4a8: DeepEP Low Latency Dispatch Adopts FP8 Communication |
| `pr-sglang-22323` | upstream-code | [`sources/prs/sglang/PR-22323.md`](../sources/prs/sglang/PR-22323.md) | [Lora] Lora quat info re-factor and support deepseekv3 mla lora |
| `pr-sglang-22336` | upstream-code | [`sources/prs/sglang/PR-22336.md`](../sources/prs/sglang/PR-22336.md) | [AMD] Add GLM-5.1-FP8 nightly accuracy and performance benchmarks for MI30x and MI35x |
| `pr-sglang-22365` | upstream-code | [`sources/prs/sglang/PR-22365.md`](../sources/prs/sglang/PR-22365.md) | [Diffusion] modelopt diffusion fp8 support for flux1/flux2 and wan2.2 |
| `pr-sglang-22372` | upstream-code | [`sources/prs/sglang/PR-22372.md`](../sources/prs/sglang/PR-22372.md) | [DSA] Hopper FP8 FlashMLA KV padding |
| `pr-sglang-22484` | upstream-code | [`sources/prs/sglang/PR-22484.md`](../sources/prs/sglang/PR-22484.md) | [RL] Fix weight update for mxfp8 flashinfer_cutlass gemm backend |
| `pr-sglang-22574` | upstream-code | [`sources/prs/sglang/PR-22574.md`](../sources/prs/sglang/PR-22574.md) | [Diffusion] Add FLUX.1-dev ModelOpt NVFP4 support |
| `pr-sglang-22672` | upstream-code | [`sources/prs/sglang/PR-22672.md`](../sources/prs/sglang/PR-22672.md) | reland [Diffusion] Add FLUX.1-dev ModelOpt NVFP4 support |
| `pr-sglang-23686` | upstream-code | [`sources/prs/sglang/PR-23686.md`](../sources/prs/sglang/PR-23686.md) | Deepseek_v4 support w4(mxfp4)a16 on hopper |
| `pr-sglang-23965` | upstream-code | [`sources/prs/sglang/PR-23965.md`](../sources/prs/sglang/PR-23965.md) | Enable PDL for various kernels in DSV32/GLM5 |
| `pr-sglang-24197` | upstream-code | [`sources/prs/sglang/PR-24197.md`](../sources/prs/sglang/PR-24197.md) | Refactor device timer, clean up metrics collector, and add fwd occupancy metric |
| `pr-sglang-24490` | upstream-code | [`sources/prs/sglang/PR-24490.md`](../sources/prs/sglang/PR-24490.md) | Port MXFP4 Marlin MoE support to JIT kernel path |
| `pr-sglang-24696` | upstream-code | [`sources/prs/sglang/PR-24696.md`](../sources/prs/sglang/PR-24696.md) | [Gemma4] Optimize Gemm4 with fused Q/K/V RMSNorm + per-expert FP8 ckpt loader |
| `pr-sglang-24816` | upstream-code | [`sources/prs/sglang/PR-24816.md`](../sources/prs/sglang/PR-24816.md) | Add FlashInfer SM90 cutlass MXFP4 MoE backend (W4A16) for GPT-OSS + DeepSeek-V4 |
| `pr-sglang-24925` | upstream-code | [`sources/prs/sglang/PR-24925.md`](../sources/prs/sglang/PR-24925.md) | [attn backend] Integrate tokenspeed_mla prefill/decode kernels (fp8 kv cache, blackwell) |
| `pr-sglang-24986` | upstream-code | [`sources/prs/sglang/PR-24986.md`](../sources/prs/sglang/PR-24986.md) | [rebase]Deepseek_v4 support w4(mxfp4)a16 on hopper |
| `pr-sglang-3047` | upstream-code | [`sources/prs/sglang/PR-3047.md`](../sources/prs/sglang/PR-3047.md) | support w8a8 fp8 kernel with CUTLASS |
| `pr-sglang-3056` | upstream-code | [`sources/prs/sglang/PR-3056.md`](../sources/prs/sglang/PR-3056.md) | feat: integrate bmm_fp8 kernel into sgl-kernel |
| `pr-sglang-3148` | upstream-code | [`sources/prs/sglang/PR-3148.md`](../sources/prs/sglang/PR-3148.md) | Apply sgl w8a8 fp8 kernel |
| `pr-sglang-3216` | upstream-code | [`sources/prs/sglang/PR-3216.md`](../sources/prs/sglang/PR-3216.md) | add tensorrt_llm common and cutlass_extensions as 3rdparty |
| `pr-sglang-3267` | upstream-code | [`sources/prs/sglang/PR-3267.md`](../sources/prs/sglang/PR-3267.md) | support blockwise fp8 matmul kernel |
| `pr-sglang-3529` | upstream-code | [`sources/prs/sglang/PR-3529.md`](../sources/prs/sglang/PR-3529.md) | integrate blockwise fp8 kernel |
| `pr-sglang-3727` | upstream-code | [`sources/prs/sglang/PR-3727.md`](../sources/prs/sglang/PR-3727.md) | add control for cutlass fp8 blockwise gemm |
| `pr-sglang-4165` | upstream-code | [`sources/prs/sglang/PR-4165.md`](../sources/prs/sglang/PR-4165.md) | DeepGemm integrate to sgl-kernel |
| `pr-sglang-4199` | upstream-code | [`sources/prs/sglang/PR-4199.md`](../sources/prs/sglang/PR-4199.md) | linear support deepgemm |
| `pr-sglang-4215` | upstream-code | [`sources/prs/sglang/PR-4215.md`](../sources/prs/sglang/PR-4215.md) | Accelerate FP8 CUDA Kernel by 20-28% |
| `pr-sglang-4230` | upstream-code | [`sources/prs/sglang/PR-4230.md`](../sources/prs/sglang/PR-4230.md) | Clean up fp8 support |
| `pr-sglang-4231` | upstream-code | [`sources/prs/sglang/PR-4231.md`](../sources/prs/sglang/PR-4231.md) | fix per_token_group_quant_fp8 illegal memory when num_groups % 16 != 0 |
| `pr-sglang-4278` | upstream-code | [`sources/prs/sglang/PR-4278.md`](../sources/prs/sglang/PR-4278.md) | Support Blackwell Block Scale FP8 Gemm |
| `pr-sglang-4359` | upstream-code | [`sources/prs/sglang/PR-4359.md`](../sources/prs/sglang/PR-4359.md) | [FIX] fix incorrect output when enable both deepgemm and torch compile |
| `pr-sglang-4510` | upstream-code | [`sources/prs/sglang/PR-4510.md`](../sources/prs/sglang/PR-4510.md) | [ROCm] fix dtype |
| `pr-sglang-4515` | upstream-code | [`sources/prs/sglang/PR-4515.md`](../sources/prs/sglang/PR-4515.md) | Create col-major and tma-aligned x_scale for deep_gemm.gemm_fp8_fp8_bf16_nt |
| `pr-sglang-4558` | upstream-code | [`sources/prs/sglang/PR-4558.md`](../sources/prs/sglang/PR-4558.md) | Support fp8 gemm for blackwell |
| `pr-sglang-4596` | upstream-code | [`sources/prs/sglang/PR-4596.md`](../sources/prs/sglang/PR-4596.md) | [quantization] fix channelwise conversion with scalar weight scale |
| `pr-sglang-4613` | upstream-code | [`sources/prs/sglang/PR-4613.md`](../sources/prs/sglang/PR-4613.md) | Set deepgemm to the default value in the hopper architecture. |
| `pr-sglang-4918` | upstream-code | [`sources/prs/sglang/PR-4918.md`](../sources/prs/sglang/PR-4918.md) | Add DeepSeek V3/R1 shared experts fusion |
| `pr-sglang-5176` | upstream-code | [`sources/prs/sglang/PR-5176.md`](../sources/prs/sglang/PR-5176.md) | feat: add DeepGEMM build warning |
| `pr-sglang-5263` | upstream-code | [`sources/prs/sglang/PR-5263.md`](../sources/prs/sglang/PR-5263.md) | [Fix] Turn off DeepGEMM by default |
| `pr-sglang-5281` | upstream-code | [`sources/prs/sglang/PR-5281.md`](../sources/prs/sglang/PR-5281.md) | [1/2] Add FP8 Blockscale MoE CUTLASS kernel for Blackwell |
| `pr-sglang-5310` | upstream-code | [`sources/prs/sglang/PR-5310.md`](../sources/prs/sglang/PR-5310.md) | fix: use deepgemm only on hopper |
| `pr-sglang-5370` | upstream-code | [`sources/prs/sglang/PR-5370.md`](../sources/prs/sglang/PR-5370.md) | [perf] experimental enhance fp8 per-tensor quant |
| `pr-sglang-5432` | upstream-code | [`sources/prs/sglang/PR-5432.md`](../sources/prs/sglang/PR-5432.md) | [perf] introduce deep gemm group_gemm_masked as bmm |
| `pr-sglang-5580` | upstream-code | [`sources/prs/sglang/PR-5580.md`](../sources/prs/sglang/PR-5580.md) | [feature] enable pre compile jit deep_gemm |
| `pr-sglang-5626` | upstream-code | [`sources/prs/sglang/PR-5626.md`](../sources/prs/sglang/PR-5626.md) |  DeepEP normal support deepgemm-contiguous |
| `pr-sglang-5662` | upstream-code | [`sources/prs/sglang/PR-5662.md`](../sources/prs/sglang/PR-5662.md) | [perf] dsv3 bmm fallback to bf16 |
| `pr-sglang-5694` | upstream-code | [`sources/prs/sglang/PR-5694.md`](../sources/prs/sglang/PR-5694.md) | [2/2] Add python wrapper for CUTLASS FP8 Blockscale MoE Kernel.  |
| `pr-sglang-5820` | upstream-code | [`sources/prs/sglang/PR-5820.md`](../sources/prs/sglang/PR-5820.md) | cutlass 3.9 supported to improve fp8_blockwise_gemm |
| `pr-sglang-6004` | upstream-code | [`sources/prs/sglang/PR-6004.md`](../sources/prs/sglang/PR-6004.md) | chore: upgrade cutlass 3.9.2 |
| `pr-sglang-6336` | upstream-code | [`sources/prs/sglang/PR-6336.md`](../sources/prs/sglang/PR-6336.md) | Upgrade  CUTLASS 4.0 |
| `pr-sglang-6404` | upstream-code | [`sources/prs/sglang/PR-6404.md`](../sources/prs/sglang/PR-6404.md) | Add fp8 fused_experts kernel for CPU in sgl-kernel and add UT |
| `pr-sglang-6449` | upstream-code | [`sources/prs/sglang/PR-6449.md`](../sources/prs/sglang/PR-6449.md) | Fix bug of deepseek-v3 under DP+EP mode with large batchsize/seqlen |
| `pr-sglang-6479` | upstream-code | [`sources/prs/sglang/PR-6479.md`](../sources/prs/sglang/PR-6479.md) | [Feature] Support Flashinfer fp8 blockwise GEMM kernel on Blackwell |
| `pr-sglang-6736` | upstream-code | [`sources/prs/sglang/PR-6736.md`](../sources/prs/sglang/PR-6736.md) | Set `num_fused_shared_experts` as `num_shared_experts` when shared_experts fusion is not disabled |
| `pr-sglang-6769` | upstream-code | [`sources/prs/sglang/PR-6769.md`](../sources/prs/sglang/PR-6769.md) | [CPU] add optimizations for INT8 and FP8 DeepSeek |
| `pr-sglang-6821` | upstream-code | [`sources/prs/sglang/PR-6821.md`](../sources/prs/sglang/PR-6821.md) | feat: integrate deepgemm into EPMoE |
| `pr-sglang-6833` | upstream-code | [`sources/prs/sglang/PR-6833.md`](../sources/prs/sglang/PR-6833.md) | CPU: map changes from developing branch in sgl-kernel |
| `pr-sglang-6890` | upstream-code | [`sources/prs/sglang/PR-6890.md`](../sources/prs/sglang/PR-6890.md) | Use deepgemm instead of triton for fused_qkv_a_proj_with_mqa |
| `pr-sglang-6916` | upstream-code | [`sources/prs/sglang/PR-6916.md`](../sources/prs/sglang/PR-6916.md) | Add a CUDA kernel for fusing mapping and weighted sum for MoE. |
| `pr-sglang-6930` | upstream-code | [`sources/prs/sglang/PR-6930.md`](../sources/prs/sglang/PR-6930.md) | [Feature] Support Flashinfer fmha on Blackwell |
| `pr-sglang-6970` | upstream-code | [`sources/prs/sglang/PR-6970.md`](../sources/prs/sglang/PR-6970.md) | Fuse routed scaling factor in deepseek |
| `pr-sglang-7023` | upstream-code | [`sources/prs/sglang/PR-7023.md`](../sources/prs/sglang/PR-7023.md) | Update default settings for blackwell |
| `pr-sglang-7093` | upstream-code | [`sources/prs/sglang/PR-7093.md`](../sources/prs/sglang/PR-7093.md) | Fix positional argument |
| `pr-sglang-7125` | upstream-code | [`sources/prs/sglang/PR-7125.md`](../sources/prs/sglang/PR-7125.md) | fix amd EP MoE FP8 issue |
| `pr-sglang-7129` | upstream-code | [`sources/prs/sglang/PR-7129.md`](../sources/prs/sglang/PR-7129.md) | Enable ModelOpt Llama4 fp8 checkpoint deployment in SGLang |
| `pr-sglang-7160` | upstream-code | [`sources/prs/sglang/PR-7160.md`](../sources/prs/sglang/PR-7160.md) | [amd] Opt dsv3 moe |
| `pr-sglang-7172` | upstream-code | [`sources/prs/sglang/PR-7172.md`](../sources/prs/sglang/PR-7172.md) | Support new DeepGEMM |
| `pr-sglang-7182` | upstream-code | [`sources/prs/sglang/PR-7182.md`](../sources/prs/sglang/PR-7182.md) | Tiny let DeepGEMM scale checks cover more cases |
| `pr-sglang-7187` | upstream-code | [`sources/prs/sglang/PR-7187.md`](../sources/prs/sglang/PR-7187.md) | [AMD] Fail gracefully when AITER is unavailable gfx90a GPUs |
| `pr-sglang-7247` | upstream-code | [`sources/prs/sglang/PR-7247.md`](../sources/prs/sglang/PR-7247.md) | [fix] fix DeepGEMM blackwell input quant & ut & fix style and log |
| `pr-sglang-7278` | upstream-code | [`sources/prs/sglang/PR-7278.md`](../sources/prs/sglang/PR-7278.md) | Add CUTLASS FP8 Blockscale MoE kernel for Hopper architecture |
| `pr-sglang-7391` | upstream-code | [`sources/prs/sglang/PR-7391.md`](../sources/prs/sglang/PR-7391.md) | Fix torch compile run |
| `pr-sglang-7392` | upstream-code | [`sources/prs/sglang/PR-7392.md`](../sources/prs/sglang/PR-7392.md) | [AMD][Quantization] Add `int4fp8_moe` online quantization on ROCm |
| `pr-sglang-7762` | upstream-code | [`sources/prs/sglang/PR-7762.md`](../sources/prs/sglang/PR-7762.md) | feat: support DeepSeek-R1-W4AFP8 model with ep-moe mode |
| `pr-sglang-7912` | upstream-code | [`sources/prs/sglang/PR-7912.md`](../sources/prs/sglang/PR-7912.md) | Qwen FP8/NVFP4 ModelOPT Quantization support |
| `pr-sglang-8118` | upstream-code | [`sources/prs/sglang/PR-8118.md`](../sources/prs/sglang/PR-8118.md) | [feat] Support tp mode for DeepSeek-R1-W4AFP8 |
| `pr-sglang-8130` | upstream-code | [`sources/prs/sglang/PR-8130.md`](../sources/prs/sglang/PR-8130.md) | [sgl-kernel] Opt per_token_quant_fp8 with warp reduce |
| `pr-sglang-8247` | upstream-code | [`sources/prs/sglang/PR-8247.md`](../sources/prs/sglang/PR-8247.md) | [1/N]Support  DeepSeek-R1 w4a8 normal deepep |
| `pr-sglang-8464` | upstream-code | [`sources/prs/sglang/PR-8464.md`](../sources/prs/sglang/PR-8464.md) | [2/N]Support DeepSeek-R1 w4a8 low latency deepep |
| `pr-sglang-8638` | upstream-code | [`sources/prs/sglang/PR-8638.md`](../sources/prs/sglang/PR-8638.md) | TRTLLM-MLA FP8 path |
| `pr-sglang-8678` | upstream-code | [`sources/prs/sglang/PR-8678.md`](../sources/prs/sglang/PR-8678.md) | feat: support cutlass_moe_fp8 kernel for fusedmoe in sm90 |
| `pr-sglang-8818` | upstream-code | [`sources/prs/sglang/PR-8818.md`](../sources/prs/sglang/PR-8818.md) | [Perf] Tunings for SM100 FP8 CUTLASS kernel |
| `pr-sglang-8962` | upstream-code | [`sources/prs/sglang/PR-8962.md`](../sources/prs/sglang/PR-8962.md) | optimize: reduce shulffle and quantization overhead in cutlass_moe sm90 |
| `pr-sglang-9272` | upstream-code | [`sources/prs/sglang/PR-9272.md`](../sources/prs/sglang/PR-9272.md) | [fix]:  fix cutlass moe ut and and Opt H20 cutlass groupGemm performance |
| `pr-sglang-9403` | upstream-code | [`sources/prs/sglang/PR-9403.md`](../sources/prs/sglang/PR-9403.md) | [sgl-kernel] feat: Support sm120 cutlass fp8 gemm kernel |
| `pr-sglang-9530` | upstream-code | [`sources/prs/sglang/PR-9530.md`](../sources/prs/sglang/PR-9530.md) | fix: blackwell dsv3 fp8 issue temporary solution |
| `pr-sglang-9559` | upstream-code | [`sources/prs/sglang/PR-9559.md`](../sources/prs/sglang/PR-9559.md) | Update CUTLASS 4.2 & Enable K-Major Scale Factor for SM90 FP8 Blockwise Group GEMM |
| `pr-sglang-9679` | upstream-code | [`sources/prs/sglang/PR-9679.md`](../sources/prs/sglang/PR-9679.md) | move is_sm90_supported/is_sm100_supported to python/sglang/srt/utils.py |
| `pr-sglang-9744` | upstream-code | [`sources/prs/sglang/PR-9744.md`](../sources/prs/sglang/PR-9744.md) | [CPU] Add FP8 Bmm support |
| `pr-sglang-9789` | upstream-code | [`sources/prs/sglang/PR-9789.md`](../sources/prs/sglang/PR-9789.md) | Make sm100 fp8 kernels available on sm103 |
| `pr-sglang-9969` | upstream-code | [`sources/prs/sglang/PR-9969.md`](../sources/prs/sglang/PR-9969.md) | CUTLASS fp8 blockwise gemm support of sm120 |
| `pr-tensorrt-llm-10130` | upstream-code | [`sources/prs/tensorrt-llm/PR-10130.md`](../sources/prs/tensorrt-llm/PR-10130.md) | [TRTLLM-9457][feat] Add cute dsl fp8 gemm for Blackwell |
| `pr-tensorrt-llm-10327` | upstream-code | [`sources/prs/tensorrt-llm/PR-10327.md`](../sources/prs/tensorrt-llm/PR-10327.md) | [None][fix] impl fused triton kernel for e8m0 resmooth to reduce memory footprint |
| `pr-tensorrt-llm-10532` | upstream-code | [`sources/prs/tensorrt-llm/PR-10532.md`](../sources/prs/tensorrt-llm/PR-10532.md) | [None][feat] MiniMax M2 support |
| `pr-tensorrt-llm-11143` | upstream-code | [`sources/prs/tensorrt-llm/PR-11143.md`](../sources/prs/tensorrt-llm/PR-11143.md) | [None][feat] fuse shared to sparse experts in TRT-LLM Gen MoE |
| `pr-tensorrt-llm-11165` | upstream-code | [`sources/prs/tensorrt-llm/PR-11165.md`](../sources/prs/tensorrt-llm/PR-11165.md) | [https://nvbugs/5799917][fix] Recover from CUTLASS MoE doActivation perf regression for MXFP4/NVFP4 dtype |
| `pr-tensorrt-llm-11589` | upstream-code | [`sources/prs/tensorrt-llm/PR-11589.md`](../sources/prs/tensorrt-llm/PR-11589.md) | [TRTLLM-10004][feat] Enable GEMM -> AR with GEMM output in registered buffers |
| `pr-tensorrt-llm-11769` | upstream-code | [`sources/prs/tensorrt-llm/PR-11769.md`](../sources/prs/tensorrt-llm/PR-11769.md) | [https://nvbugs/5885070][fix] fix deepeplowlatency with cutedsl moe backend |
| `pr-tensorrt-llm-11899` | upstream-code | [`sources/prs/tensorrt-llm/PR-11899.md`](../sources/prs/tensorrt-llm/PR-11899.md) | [TRTLLM-10421][perf] Add fused cat+fp8_quantize CUDA kernel for DSA indexer |
| `pr-tensorrt-llm-11990` | upstream-code | [`sources/prs/tensorrt-llm/PR-11990.md`](../sources/prs/tensorrt-llm/PR-11990.md) | [None][feat] GLM 5 support and DSA MTP fixes |
| `pr-tensorrt-llm-12503` | upstream-code | [`sources/prs/tensorrt-llm/PR-12503.md`](../sources/prs/tensorrt-llm/PR-12503.md) | [https://nvbugs/5983390][perf] Split MLA DSA custom op for piecewise CUDA graph capture |
| `pr-tensorrt-llm-12937` | upstream-code | [`sources/prs/tensorrt-llm/PR-12937.md`](../sources/prs/tensorrt-llm/PR-12937.md) | [TRTLLM-11485][feat] Feature rework: Add SageAttention refreshed kernels (attentionOp only) |
| `pr-tensorrt-llm-13219` | upstream-code | [`sources/prs/tensorrt-llm/PR-13219.md`](../sources/prs/tensorrt-llm/PR-13219.md) | [TRTLLM-34871][feat] Add cute dsl FP8 paged MQA logits decode kernel |
| `pr-tensorrt-llm-13222` | upstream-code | [`sources/prs/tensorrt-llm/PR-13222.md`](../sources/prs/tensorrt-llm/PR-13222.md) | [#11823][feat] AutoDeploy trtllm_mla attention backend |
| `pr-tensorrt-llm-13340` | upstream-code | [`sources/prs/tensorrt-llm/PR-13340.md`](../sources/prs/tensorrt-llm/PR-13340.md) | [None][feat] Integrate FP4 indexer for DSA on Blackwell |
| `pr-tensorrt-llm-13384` | upstream-code | [`sources/prs/tensorrt-llm/PR-13384.md`](../sources/prs/tensorrt-llm/PR-13384.md) | [None][feat] Add MegaMoEDeepGemmFusedMoE backend wrapping DeepGEMM fp8_fp4_mega_moe |
| `pr-tensorrt-llm-13595` | upstream-code | [`sources/prs/tensorrt-llm/PR-13595.md`](../sources/prs/tensorrt-llm/PR-13595.md) | [None][feat] Enable EPLB for DeepSeek-V4 |
| `pr-tensorrt-llm-13628` | upstream-code | [`sources/prs/tensorrt-llm/PR-13628.md`](../sources/prs/tensorrt-llm/PR-13628.md) | [None][feat] Fuse FP8 1x128 quantize + UE8M0 scale pack on SM100 |
| `pr-tensorrt-llm-13767` | upstream-code | [`sources/prs/tensorrt-llm/PR-13767.md`](../sources/prs/tensorrt-llm/PR-13767.md) | [None][fix] Plumb swiglu_limit through DeepGEMM and TRTLLMGen FP8 fused MoE |
| `pr-tensorrt-llm-13873` | upstream-code | [`sources/prs/tensorrt-llm/PR-13873.md`](../sources/prs/tensorrt-llm/PR-13873.md) | [TRTLLM-12503][feat] Parallel VAE independent scaling and fix arg passing |
| `pr-tensorrt-llm-13929` | upstream-code | [`sources/prs/tensorrt-llm/PR-13929.md`](../sources/prs/tensorrt-llm/PR-13929.md) | [TRTLLM-35237][feat] Add cute dsl FP4 paged MQA logits decode kernel |
| `pr-tensorrt-llm-13938` | upstream-code | [`sources/prs/tensorrt-llm/PR-13938.md`](../sources/prs/tensorrt-llm/PR-13938.md) | [None][feat] Keep DSv4 o_a_proj as FP8, and port vLLM's fused_inv_rope_fp8_quant |
| `pr-tensorrt-llm-14039` | upstream-code | [`sources/prs/tensorrt-llm/PR-14039.md`](../sources/prs/tensorrt-llm/PR-14039.md) | [#8542][feat] AutoDeploy: add Llama-3.1-8B FP8 perf-sanity test on H100 |
| `pr-tensorrt-llm-4867` | upstream-code | [`sources/prs/tensorrt-llm/PR-4867.md`](../sources/prs/tensorrt-llm/PR-4867.md) | feat: Add w4a8_mxfp4_fp8 quantization recipe. |
| `pr-tensorrt-llm-6809` | upstream-code | [`sources/prs/tensorrt-llm/PR-6809.md`](../sources/prs/tensorrt-llm/PR-6809.md) | [OMNIML-2336][feat] Add NVFP4 x FP8 |
| `pr-tensorrt-llm-7524` | upstream-code | [`sources/prs/tensorrt-llm/PR-7524.md`](../sources/prs/tensorrt-llm/PR-7524.md) | [None][chore] Fix kernel launch param and add TRTLLM MoE backend test |
| `pr-tensorrt-llm-7755` | upstream-code | [`sources/prs/tensorrt-llm/PR-7755.md`](../sources/prs/tensorrt-llm/PR-7755.md) | [None][fix] Fix and add test for TRTLLM MoE backend |
| `pr-tensorrt-llm-7761` | upstream-code | [`sources/prs/tensorrt-llm/PR-7761.md`](../sources/prs/tensorrt-llm/PR-7761.md) | [TRTLLM-8637][feat] Optimize the routing kernel for DeepseekV3 (MoE CUTLASS backend); Add support for 384 experts (MoE TRTLLM backend) |
| `pr-tensorrt-llm-7937` | upstream-code | [`sources/prs/tensorrt-llm/PR-7937.md`](../sources/prs/tensorrt-llm/PR-7937.md) | [None][feat] GPT-OSS Sm120/Sm121 Support |
| `pr-tensorrt-llm-8405` | upstream-code | [`sources/prs/tensorrt-llm/PR-8405.md`](../sources/prs/tensorrt-llm/PR-8405.md) | [TRTLLM-8535][feat] Support DeepSeek V3.2 with FP8 + BF16 KV cache/NVFP4 + BF16 KV cache |
| `pr-tensorrt-llm-8501` | upstream-code | [`sources/prs/tensorrt-llm/PR-8501.md`](../sources/prs/tensorrt-llm/PR-8501.md) | [None][fix] Fix the performance issue of FP8 blockwise grouped GEMM when using attention DP |
| `pr-tensorrt-llm-9175` | upstream-code | [`sources/prs/tensorrt-llm/PR-9175.md`](../sources/prs/tensorrt-llm/PR-9175.md) | [None][feat] TRT-LLM Gen MoE optimize DeepSeek Fp8 activation kernel |
| `pr-tensorrt-llm-9838` | upstream-code | [`sources/prs/tensorrt-llm/PR-9838.md`](../sources/prs/tensorrt-llm/PR-9838.md) | [https://nvbugs/5726962][feat] Apply fusion for W4AFP8_AWQ MoE |
| `pr-thunderkittens-84` | upstream-code | [`sources/prs/thunderkittens/PR-84.md`](../sources/prs/thunderkittens/PR-84.md) | WIP Blackwell fp8 support |
| `pr-tilelang-1090` | upstream-code | [`sources/prs/tilelang/PR-1090.md`](../sources/prs/tilelang/PR-1090.md) | [BugFix] Correct direct copy from bf16 to fp8 |
| `pr-tilelang-1229` | upstream-code | [`sources/prs/tilelang/PR-1229.md`](../sources/prs/tilelang/PR-1229.md) | [WIP] support more dtypes for tcgen05 |
| `pr-tilelang-1246` | upstream-code | [`sources/prs/tilelang/PR-1246.md`](../sources/prs/tilelang/PR-1246.md) | [Bugfix] Fix fp8 dtype for some cases |
| `pr-tilelang-1327` | upstream-code | [`sources/prs/tilelang/PR-1327.md`](../sources/prs/tilelang/PR-1327.md) | [Enhancement] add more dtype and fix mma.ws for fp16 for tcgen05 |
| `pr-tilelang-1605` | upstream-code | [`sources/prs/tilelang/PR-1605.md`](../sources/prs/tilelang/PR-1605.md) | [Enhancement][AMD] Add preshuffle fp8 gemm example on amd. |
| `pr-tilelang-1743` | upstream-code | [`sources/prs/tilelang/PR-1743.md`](../sources/prs/tilelang/PR-1743.md) | [AMD] Fix ROCm FP8 dtype selection and MFMA support on gfx942/gfx950 |
| `pr-tilelang-1945` | upstream-code | [`sources/prs/tilelang/PR-1945.md`](../sources/prs/tilelang/PR-1945.md) | [Feature] Block-scaled GEMM support for MXFP8 on Blackwell |
| `pr-tilelang-1953` | upstream-code | [`sources/prs/tilelang/PR-1953.md`](../sources/prs/tilelang/PR-1953.md) | [PIpeline] Enable software pipelining when warp specialization is unavailable |
| `pr-tilelang-1976` | upstream-code | [`sources/prs/tilelang/PR-1976.md`](../sources/prs/tilelang/PR-1976.md) | [Feature] Batched AllReduce for better T.reduce performance |
| `pr-tilelang-2004` | upstream-code | [`sources/prs/tilelang/PR-2004.md`](../sources/prs/tilelang/PR-2004.md) | fix: fix copy+cast vectorize loop to use wider vector load/store instrcution |
| `pr-tilelang-2023` | upstream-code | [`sources/prs/tilelang/PR-2023.md`](../sources/prs/tilelang/PR-2023.md) | [Codegen] Add lexical_alloc_scope for scoped local variable lifetime |
| `pr-tilelang-2024` | upstream-code | [`sources/prs/tilelang/PR-2024.md`](../sources/prs/tilelang/PR-2024.md) | Re-enable deprecated `TL_DISABLE_TMA_LOWER` pass config for TMA store |
| `pr-tilelang-2026` | upstream-code | [`sources/prs/tilelang/PR-2026.md`](../sources/prs/tilelang/PR-2026.md) | [Refactor] Refactor `DecoupleTypeCast` Pass |
| `pr-tilelang-2031` | upstream-code | [`sources/prs/tilelang/PR-2031.md`](../sources/prs/tilelang/PR-2031.md) | [Bugfix] Fix stage-expanded annotated-layout aliases in LayoutInference |
| `pr-tilelang-2046` | upstream-code | [`sources/prs/tilelang/PR-2046.md`](../sources/prs/tilelang/PR-2046.md) | [Refactor] Remove obsolete RewriteWgmmaSync pass |
| `pr-tilelang-2047` | upstream-code | [`sources/prs/tilelang/PR-2047.md`](../sources/prs/tilelang/PR-2047.md) | [Refactor] Move target gating into InjectFenceProxy pass entry |
| `pr-tilelang-2052` | upstream-code | [`sources/prs/tilelang/PR-2052.md`](../sources/prs/tilelang/PR-2052.md) | [Bugfix] Use shared::cta instead of shared::cluster for non-cluster T… |
| `pr-tilelang-2055` | upstream-code | [`sources/prs/tilelang/PR-2055.md`](../sources/prs/tilelang/PR-2055.md) | [BugFix] Keep shared-prelude local vars in producer-consumer WS |
| `pr-tilelang-2063` | upstream-code | [`sources/prs/tilelang/PR-2063.md`](../sources/prs/tilelang/PR-2063.md) | [CUDA] Support int4 `T.gemm` |
| `pr-tilelang-2069` | upstream-code | [`sources/prs/tilelang/PR-2069.md`](../sources/prs/tilelang/PR-2069.md) | [Example]  Add HISA: hierarchical sparse attention indexer |
| `pr-tilelang-2075` | upstream-code | [`sources/prs/tilelang/PR-2075.md`](../sources/prs/tilelang/PR-2075.md) | [Refactor] Phaseout legacy util `map_torch_type` with `T.dtype.as_torch` |
| `pr-tilelang-2088` | upstream-code | [`sources/prs/tilelang/PR-2088.md`](../sources/prs/tilelang/PR-2088.md) | [Refactor] Refactor register annotation lowering |
| `pr-tilelang-2092` | upstream-code | [`sources/prs/tilelang/PR-2092.md`](../sources/prs/tilelang/PR-2092.md) | [BugFix] Relax loop wait and adjust trailing drain behavior in async pipeline tests |
| `pr-tilelang-2098` | upstream-code | [`sources/prs/tilelang/PR-2098.md`](../sources/prs/tilelang/PR-2098.md) | [Example] Add MXFP8 blockscaled grouped gemm examples with transB support  |
| `pr-tilelang-2099` | upstream-code | [`sources/prs/tilelang/PR-2099.md`](../sources/prs/tilelang/PR-2099.md) | [AMD] [gfx950]Fix multiple HIP codegen bugs to support TileKernel   |
| `pr-tilelang-2102` | upstream-code | [`sources/prs/tilelang/PR-2102.md`](../sources/prs/tilelang/PR-2102.md) | [CUDA][SM100] Include cuda_fp6.h when emitting FP6 types |
| `pr-tilelang-2103` | upstream-code | [`sources/prs/tilelang/PR-2103.md`](../sources/prs/tilelang/PR-2103.md) | [Enhancement] Optimize hopper fp8 deepgemm tile size |
| `pr-tilelang-2107` | upstream-code | [`sources/prs/tilelang/PR-2107.md`](../sources/prs/tilelang/PR-2107.md) | [TMA] Support FP4 TensorMap TMA copies |
| `pr-tilelang-2138` | upstream-code | [`sources/prs/tilelang/PR-2138.md`](../sources/prs/tilelang/PR-2138.md) | [Refactor][Backend] Split tl.copy lowering by backend |
| `pr-tilelang-2148` | upstream-code | [`sources/prs/tilelang/PR-2148.md`](../sources/prs/tilelang/PR-2148.md) | [Examples] Add examples for operators in DeepSeek-V4 |
| `pr-tilelang-2165` | upstream-code | [`sources/prs/tilelang/PR-2165.md`](../sources/prs/tilelang/PR-2165.md) | [Refactor] Move backend-specific GEMM implementations and transforms into backend directories |
| `pr-tilelang-2166` | upstream-code | [`sources/prs/tilelang/PR-2166.md`](../sources/prs/tilelang/PR-2166.md) | [BugFix] Consider non-local store in external call and SIMT producer for warp specialize |
| `pr-tilelang-2179` | upstream-code | [`sources/prs/tilelang/PR-2179.md`](../sources/prs/tilelang/PR-2179.md) | [ROCm] Try to fix ROCm CI error  |
| `pr-triton-10214` | upstream-code | [`sources/prs/triton/PR-10214.md`](../sources/prs/triton/PR-10214.md) | Allow MXFP8 LHS with Hopper-swizzled MXFP4 RHS |
| `pr-triton-10234` | upstream-code | [`sources/prs/triton/PR-10234.md`](../sources/prs/triton/PR-10234.md) | [ BACKEND ]  Enable `tl.dot` with TF32 precision on tiles with N=8 and K=8 |
| `pr-triton-9883` | upstream-code | [`sources/prs/triton/PR-9883.md`](../sources/prs/triton/PR-9883.md) | [AMD][gfx9] Use asyncmark/wait_asyncmark for CDNA3/CDNA4 buffer_load_to_lds |
| `pr-vllm-10995` | upstream-code | [`sources/prs/vllm/PR-10995.md`](../sources/prs/vllm/PR-10995.md) | [Kernel]: Cutlass 2:4 Sparsity + FP8/Int8 Quant Support |
| `pr-vllm-11868` | upstream-code | [`sources/prs/vllm/PR-11868.md`](../sources/prs/vllm/PR-11868.md) | [Kernel] Update `cutlass_scaled_mm` to support 2d group (blockwise) scaling |
| `pr-vllm-12097` | upstream-code | [`sources/prs/vllm/PR-12097.md`](../sources/prs/vllm/PR-12097.md) | Add: Support for Sparse24Bitmask Compressed Models |
| `pr-vllm-12583` | upstream-code | [`sources/prs/vllm/PR-12583.md`](../sources/prs/vllm/PR-12583.md) | Expert Parallelism (EP) Support for DeepSeek Models |
| `pr-vllm-12587` | upstream-code | [`sources/prs/vllm/PR-12587.md`](../sources/prs/vllm/PR-12587.md) | [Kernel][Quantization] Integrate block-quantized CUTLASS kernels for DeepSeekV3 |
| `pr-vllm-12601` | upstream-code | [`sources/prs/vllm/PR-12601.md`](../sources/prs/vllm/PR-12601.md) | [Attention] Deepseek v3 MLA support with FP8 compute |
| `pr-vllm-12639` | upstream-code | [`sources/prs/vllm/PR-12639.md`](../sources/prs/vllm/PR-12639.md) | [Attention] MLA with chunked prefill |
| `pr-vllm-12662` | upstream-code | [`sources/prs/vllm/PR-12662.md`](../sources/prs/vllm/PR-12662.md) | [AMD][ROCm] Enable DeepSeek model on ROCm |
| `pr-vllm-12796` | upstream-code | [`sources/prs/vllm/PR-12796.md`](../sources/prs/vllm/PR-12796.md) | [Bugfix] Better FP8 supported defaults |
| `pr-vllm-12978` | upstream-code | [`sources/prs/vllm/PR-12978.md`](../sources/prs/vllm/PR-12978.md) | [Kernel]Add streamK for block-quantized CUTLASS kernels |
| `pr-vllm-13718` | upstream-code | [`sources/prs/vllm/PR-13718.md`](../sources/prs/vllm/PR-13718.md) | [core] Perf improvement for DSv3 on AMD GPUs |
| `pr-vllm-13726` | upstream-code | [`sources/prs/vllm/PR-13726.md`](../sources/prs/vllm/PR-13726.md) | [V1] V1 Enablement Oracle  |
| `pr-vllm-13784` | upstream-code | [`sources/prs/vllm/PR-13784.md`](../sources/prs/vllm/PR-13784.md) | [Bugfix][Quantization] Fix FP8 + EP |
| `pr-vllm-13798` | upstream-code | [`sources/prs/vllm/PR-13798.md`](../sources/prs/vllm/PR-13798.md) | add cutlass support for blackwell fp8 gemm |
| `pr-vllm-13972` | upstream-code | [`sources/prs/vllm/PR-13972.md`](../sources/prs/vllm/PR-13972.md) | [Kernel] CUTLASS grouped gemm fp8 MoE kernel |
| `pr-vllm-14068` | upstream-code | [`sources/prs/vllm/PR-14068.md`](../sources/prs/vllm/PR-14068.md) | [core] moe fp8 block quant tuning support |
| `pr-vllm-14245` | upstream-code | [`sources/prs/vllm/PR-14245.md`](../sources/prs/vllm/PR-14245.md) | dynamic distpatch of fp8 kernels |
| `pr-vllm-14383` | upstream-code | [`sources/prs/vllm/PR-14383.md`](../sources/prs/vllm/PR-14383.md) | Add cutlass support for blackwell fp8 blockwise gemm |
| `pr-vllm-14396` | upstream-code | [`sources/prs/vllm/PR-14396.md`](../sources/prs/vllm/PR-14396.md) | [BugFix] Illegal Memory Access in the blockwise cutlass fp8 GEMMs |
| `pr-vllm-14454` | upstream-code | [`sources/prs/vllm/PR-14454.md`](../sources/prs/vllm/PR-14454.md) | [ROCm][Kernel] MoE weights padding |
| `pr-vllm-14568` | upstream-code | [`sources/prs/vllm/PR-14568.md`](../sources/prs/vllm/PR-14568.md) | permute/unpermute kernel for moe optimization |
| `pr-vllm-14570` | upstream-code | [`sources/prs/vllm/PR-14570.md`](../sources/prs/vllm/PR-14570.md) | [Attention] Flash Attention 3 - fp8 |
| `pr-vllm-14578` | upstream-code | [`sources/prs/vllm/PR-14578.md`](../sources/prs/vllm/PR-14578.md) | [Quantization][FP8] Adding support for fp8 gemm layer input in fp8 |
| `pr-vllm-14770` | upstream-code | [`sources/prs/vllm/PR-14770.md`](../sources/prs/vllm/PR-14770.md) | [Attention] MLA get rid of materialization |
| `pr-vllm-14967` | upstream-code | [`sources/prs/vllm/PR-14967.md`](../sources/prs/vllm/PR-14967.md) | [FEAT][ROCm] Integrate Fused MoE Kernels from AITER |
| `pr-vllm-14968` | upstream-code | [`sources/prs/vllm/PR-14968.md`](../sources/prs/vllm/PR-14968.md) | [FEAT] [ROCm]: Add AITER Block-Scaled GEMM Feature |
| `pr-vllm-15587` | upstream-code | [`sources/prs/vllm/PR-15587.md`](../sources/prs/vllm/PR-15587.md) | [Quantization] Fp8 Channelwise Dynamic Per Token GroupedGEMM |
| `pr-vllm-15956` | upstream-code | [`sources/prs/vllm/PR-15956.md`](../sources/prs/vllm/PR-15956.md) | Modularize fused experts and integrate PPLX kernels |
| `pr-vllm-16113` | upstream-code | [`sources/prs/vllm/PR-16113.md`](../sources/prs/vllm/PR-16113.md) | Upstream Llama4 Support to Main |
| `pr-vllm-16366` | upstream-code | [`sources/prs/vllm/PR-16366.md`](../sources/prs/vllm/PR-16366.md) | [Kernel] Support W8A8 channel-wise weights and per-token activations in triton fused_moe_kernel |
| `pr-vllm-16537` | upstream-code | [`sources/prs/vllm/PR-16537.md`](../sources/prs/vllm/PR-16537.md) | Enable PTPC FP8 for CompressedTensorsW8A8Fp8MoEMethod (triton fused_moe) |
| `pr-vllm-16727` | upstream-code | [`sources/prs/vllm/PR-16727.md`](../sources/prs/vllm/PR-16727.md) | [ROCm] Add aiter tkw1 kernel for Llama4 fp8 |
| `pr-vllm-16850` | upstream-code | [`sources/prs/vllm/PR-16850.md`](../sources/prs/vllm/PR-16850.md) | [Kernel] some optimizations for dense marlin and moe marlin |
| `pr-vllm-16861` | upstream-code | [`sources/prs/vllm/PR-16861.md`](../sources/prs/vllm/PR-16861.md) | [Kernel] Add expert_map support to Cutlass FP8 MOE |
| `pr-vllm-17110` | upstream-code | [`sources/prs/vllm/PR-17110.md`](../sources/prs/vllm/PR-17110.md) | [FEAT] [ROCm]: Add AITER CK 2 Stages MoE support |
| `pr-vllm-17139` | upstream-code | [`sources/prs/vllm/PR-17139.md`](../sources/prs/vllm/PR-17139.md) | [ROCm][FP8][Kernel] FP8 quantization fused into Custom Paged Attention |
| `pr-vllm-17280` | upstream-code | [`sources/prs/vllm/PR-17280.md`](../sources/prs/vllm/PR-17280.md) | [NVIDIA] Support Cutlass w8a8 FP8 for Blackwell Geforce GPUs (sm120) |
| `pr-vllm-17687` | upstream-code | [`sources/prs/vllm/PR-17687.md`](../sources/prs/vllm/PR-17687.md) | [Kernel] fp4 marlin kernel |
| `pr-vllm-17918` | upstream-code | [`sources/prs/vllm/PR-17918.md`](../sources/prs/vllm/PR-17918.md) | use ceil_div in cutlass block scaling shape check |
| `pr-vllm-18343` | upstream-code | [`sources/prs/vllm/PR-18343.md`](../sources/prs/vllm/PR-18343.md) | [Feature] Expert Parallelism Load Balancer (EPLB) |
| `pr-vllm-18564` | upstream-code | [`sources/prs/vllm/PR-18564.md`](../sources/prs/vllm/PR-18564.md) | Sm100 blockwise fp8 swap ab |
| `pr-vllm-18762` | upstream-code | [`sources/prs/vllm/PR-18762.md`](../sources/prs/vllm/PR-18762.md) | [Kernel] Integrate CUTLASS MoE kernel with PPLX |
| `pr-vllm-18778` | upstream-code | [`sources/prs/vllm/PR-18778.md`](../sources/prs/vllm/PR-18778.md) | [Perf] Tunings for SM100 FP8 CUTLASS kernel |
| `pr-vllm-18864` | upstream-code | [`sources/prs/vllm/PR-18864.md`](../sources/prs/vllm/PR-18864.md) | [Kernel] Enable fp8 support for pplx and BatchedTritonExperts. |
| `pr-vllm-19085` | upstream-code | [`sources/prs/vllm/PR-19085.md`](../sources/prs/vllm/PR-19085.md) | [Kernel] Support deep_gemm for linear methods |
| `pr-vllm-19168` | upstream-code | [`sources/prs/vllm/PR-19168.md`](../sources/prs/vllm/PR-19168.md) | [Kernels] Add activation chunking logic to FusedMoEModularKernel |
| `pr-vllm-19566` | upstream-code | [`sources/prs/vllm/PR-19566.md`](../sources/prs/vllm/PR-19566.md) | [Perf] Further tunings for SM100 FP8 CUTLASS kernel |
| `pr-vllm-19757` | upstream-code | [`sources/prs/vllm/PR-19757.md`](../sources/prs/vllm/PR-19757.md) | [feat]: CUTLASS block scaled group gemm for SM100 |
| `pr-vllm-19820` | upstream-code | [`sources/prs/vllm/PR-19820.md`](../sources/prs/vllm/PR-19820.md) | [Feature] Integrate new deepgemm |
| `pr-vllm-20087` | upstream-code | [`sources/prs/vllm/PR-20087.md`](../sources/prs/vllm/PR-20087.md) |  [Feature] Integrate SM100 DeepGEMM support |
| `pr-vllm-20166` | upstream-code | [`sources/prs/vllm/PR-20166.md`](../sources/prs/vllm/PR-20166.md) | [Bugfix] Fix topk_ids indices_type for CUTLASS w8a8 FP8 MoE |
| `pr-vllm-20270` | upstream-code | [`sources/prs/vllm/PR-20270.md`](../sources/prs/vllm/PR-20270.md) | [V1] [ROCm] Enable EP with AITER Fused MoE |
| `pr-vllm-20396` | upstream-code | [`sources/prs/vllm/PR-20396.md`](../sources/prs/vllm/PR-20396.md) | [Kernel] SM90 CUTLASS FP8 GEMM: add support for swap AB + kernel tuning |
| `pr-vllm-20447` | upstream-code | [`sources/prs/vllm/PR-20447.md`](../sources/prs/vllm/PR-20447.md) | [feat]: add SM100 support for cutlass FP8 groupGEMM |
| `pr-vllm-20457` | upstream-code | [`sources/prs/vllm/PR-20457.md`](../sources/prs/vllm/PR-20457.md) | Support Llama 4 for fused_marlin_moe |
| `pr-vllm-20500` | upstream-code | [`sources/prs/vllm/PR-20500.md`](../sources/prs/vllm/PR-20500.md) | [Perf] Reuse workspace for FP8+FP4 Marlin MoE |
| `pr-vllm-20762` | upstream-code | [`sources/prs/vllm/PR-20762.md`](../sources/prs/vllm/PR-20762.md) | [Performance] Performance improvements in non-blockwise fp8 CUTLASS MoE |
| `pr-vllm-20841` | upstream-code | [`sources/prs/vllm/PR-20841.md`](../sources/prs/vllm/PR-20841.md) | [Perf] Use Triton instead of Torch for DeepGEMM Per Token Group Quant |
| `pr-vllm-20911` | upstream-code | [`sources/prs/vllm/PR-20911.md`](../sources/prs/vllm/PR-20911.md) | [Perf] Add swap_ab to SM90 FP8 non-block CUTLASS moe grouped gemm |
| `pr-vllm-21083` | upstream-code | [`sources/prs/vllm/PR-21083.md`](../sources/prs/vllm/PR-21083.md) | [Perf] Cuda Kernel for Per Token Group Quant |
| `pr-vllm-21116` | upstream-code | [`sources/prs/vllm/PR-21116.md`](../sources/prs/vllm/PR-21116.md) | [perf] Add fused MLA QKV + strided layernorm |
| `pr-vllm-21166` | upstream-code | [`sources/prs/vllm/PR-21166.md`](../sources/prs/vllm/PR-21166.md) | [Feature][OCP MX] Support mxfp6 and mixed mxfp6-mxfp4 |
| `pr-vllm-21187` | upstream-code | [`sources/prs/vllm/PR-21187.md`](../sources/prs/vllm/PR-21187.md) | [Bug] DeepGemm: Fix TypeError: per_block_cast_to_fp8() missing 1 required positional argument: 'use_ue8m0' for SM100 |
| `pr-vllm-21411` | upstream-code | [`sources/prs/vllm/PR-21411.md`](../sources/prs/vllm/PR-21411.md) | [NVIDIA] Explicitly disable shuffled weights for flashinfer blockscale moe fp8 kernels |
| `pr-vllm-21420` | upstream-code | [`sources/prs/vllm/PR-21420.md`](../sources/prs/vllm/PR-21420.md) | [Bugfix][CUDA] fixes CUDA FP8 kv cache dtype supported |
| `pr-vllm-21716` | upstream-code | [`sources/prs/vllm/PR-21716.md`](../sources/prs/vllm/PR-21716.md) | [NVIDIA] Support Flashinfer TRTLLM FP8-q/kv/out Attention Kernel |
| `pr-vllm-22131` | upstream-code | [`sources/prs/vllm/PR-22131.md`](../sources/prs/vllm/PR-22131.md) | [Kernel] Add support for block FP8 on SM120 (NVIDIA 5090 and RTX PRO 6000) |
| `pr-vllm-22222` | upstream-code | [`sources/prs/vllm/PR-22222.md`](../sources/prs/vllm/PR-22222.md) | Fp8 paged attention update |
| `pr-vllm-22399` | upstream-code | [`sources/prs/vllm/PR-22399.md`](../sources/prs/vllm/PR-22399.md) | [Bug] Fix B200 DeepGEMM E8M0 Accuracy Issue |
| `pr-vllm-22674` | upstream-code | [`sources/prs/vllm/PR-22674.md`](../sources/prs/vllm/PR-22674.md) | [Quantization] Expand compressed-tensors MoE matching logic to support NFP4 + FP8 MoEs |
| `pr-vllm-22703` | upstream-code | [`sources/prs/vllm/PR-22703.md`](../sources/prs/vllm/PR-22703.md) | [NVIDIA] Support Flashinfer TRTLLM FP8-q/kv NVFP4-out Attention Kernel |
| `pr-vllm-22758` | upstream-code | [`sources/prs/vllm/PR-22758.md`](../sources/prs/vllm/PR-22758.md) | fp8 kv cache support fix for torch.compile |
| `pr-vllm-22895` | upstream-code | [`sources/prs/vllm/PR-22895.md`](../sources/prs/vllm/PR-22895.md) | [Kernel] Added flashinfer fp8 per-tensor gemms |
| `pr-vllm-23031` | upstream-code | [`sources/prs/vllm/PR-23031.md`](../sources/prs/vllm/PR-23031.md) | [Bugfix] fix qwen3 moe fp8 accuracy issue |
| `pr-vllm-23045` | upstream-code | [`sources/prs/vllm/PR-23045.md`](../sources/prs/vllm/PR-23045.md) | [Kernel] CUTLASS MoE FP8: Integrate cuda moe permute/unpermute |
| `pr-vllm-23123` | upstream-code | [`sources/prs/vllm/PR-23123.md`](../sources/prs/vllm/PR-23123.md) | Add routed_scaling_factor to MoE grouped topk |
| `pr-vllm-23148` | upstream-code | [`sources/prs/vllm/PR-23148.md`](../sources/prs/vllm/PR-23148.md) | [XPU][Feature] fp8 online quantization support for XPU |
| `pr-vllm-23198` | upstream-code | [`sources/prs/vllm/PR-23198.md`](../sources/prs/vllm/PR-23198.md) | [kernel] Support W4A8 on Hopper |
| `pr-vllm-23264` | upstream-code | [`sources/prs/vllm/PR-23264.md`](../sources/prs/vllm/PR-23264.md) | [ROCm][Aiter] Add triton fp8 bmm kernel for mla |
| `pr-vllm-23265` | upstream-code | [`sources/prs/vllm/PR-23265.md`](../sources/prs/vllm/PR-23265.md) | [Perf] Small optimizations for silu_mul_fp8_quant_deep_gemm |
| `pr-vllm-23273` | upstream-code | [`sources/prs/vllm/PR-23273.md`](../sources/prs/vllm/PR-23273.md) | [Kernels] Overlap shared experts with send/recv |
| `pr-vllm-23280` | upstream-code | [`sources/prs/vllm/PR-23280.md`](../sources/prs/vllm/PR-23280.md) | [Perf] Use upstream CUTLASS for SM90 Block FP8 kernel |
| `pr-vllm-23294` | upstream-code | [`sources/prs/vllm/PR-23294.md`](../sources/prs/vllm/PR-23294.md) | [Bug] Fix R1 Accuracy 0 Bug |
| `pr-vllm-23608` | upstream-code | [`sources/prs/vllm/PR-23608.md`](../sources/prs/vllm/PR-23608.md) | DP/EP Support for gpt-oss with deepep-ht comm kernel on SM100 |
| `pr-vllm-23647` | upstream-code | [`sources/prs/vllm/PR-23647.md`](../sources/prs/vllm/PR-23647.md) | [Flashinfer] Support Flashinfer TRTLLM FP8-qkv BF16/FP16-out Attention Kernel |
| `pr-vllm-23666` | upstream-code | [`sources/prs/vllm/PR-23666.md`](../sources/prs/vllm/PR-23666.md) | [Feature] Add Hopper DeepGEMM E8M0 for DeepSeekV3.1 scale_fmt |
| `pr-vllm-23696` | upstream-code | [`sources/prs/vllm/PR-23696.md`](../sources/prs/vllm/PR-23696.md) | [Kernel][B200] `mxfp4` fused cutlass moe |
| `pr-vllm-23991` | upstream-code | [`sources/prs/vllm/PR-23991.md`](../sources/prs/vllm/PR-23991.md) | [Model] Add LongCat-Flash  |
| `pr-vllm-24666` | upstream-code | [`sources/prs/vllm/PR-24666.md`](../sources/prs/vllm/PR-24666.md) | [Performance] Move apply_w8a8_block_fp8_linear to an op class |
| `pr-vllm-24673` | upstream-code | [`sources/prs/vllm/PR-24673.md`](../sources/prs/vllm/PR-24673.md) | [NVIDIA] Blackwell Family |
| `pr-vllm-24722` | upstream-code | [`sources/prs/vllm/PR-24722.md`](../sources/prs/vllm/PR-24722.md) | [Kernel][Quantization] add w4a8 support for marlin kernel |
| `pr-vllm-25674` | upstream-code | [`sources/prs/vllm/PR-25674.md`](../sources/prs/vllm/PR-25674.md) | [Flashinfer][gpt-oss] Support FP8-qkv Flashinfer TRTLLM Sinks Attention |
| `pr-vllm-26535` | upstream-code | [`sources/prs/vllm/PR-26535.md`](../sources/prs/vllm/PR-26535.md) | [Bugfix] Convert untraceable GroupShape to list for AMD impl |
| `pr-vllm-26729` | upstream-code | [`sources/prs/vllm/PR-26729.md`](../sources/prs/vllm/PR-26729.md) | [Bugfix] Fix gpt-oss w4a8 DP/EP on B200 |
| `pr-vllm-27127` | upstream-code | [`sources/prs/vllm/PR-27127.md`](../sources/prs/vllm/PR-27127.md) | [Feature] Batch Invariant: Support DeepGEMM and Blackwell |
| `pr-vllm-27134` | upstream-code | [`sources/prs/vllm/PR-27134.md`](../sources/prs/vllm/PR-27134.md) | [Kernels] Enable FlashInfer FP8 Blockscale on SM90 (for TEP DSR1) |
| `pr-vllm-27146` | upstream-code | [`sources/prs/vllm/PR-27146.md`](../sources/prs/vllm/PR-27146.md) | [torch.compile] Enable silu_mul_fp8_quant fusion without custom ops enabled |
| `pr-vllm-27255` | upstream-code | [`sources/prs/vllm/PR-27255.md`](../sources/prs/vllm/PR-27255.md) | Bugfix: Cutlass FP8 FusedMoE bad scaling factors |
| `pr-vllm-27261` | upstream-code | [`sources/prs/vllm/PR-27261.md`](../sources/prs/vllm/PR-27261.md) | Feature: Support Relu2 in FusedMoE fp8 cutlass path |
| `pr-vllm-27284` | upstream-code | [`sources/prs/vllm/PR-27284.md`](../sources/prs/vllm/PR-27284.md) | [Perf] SM100 - add swap AB optimization to CUTLASS FP8 GEMM |
| `pr-vllm-27492` | upstream-code | [`sources/prs/vllm/PR-27492.md`](../sources/prs/vllm/PR-27492.md) | [Performance] Support FP8 flashinfer TRTLLM MOE on Qwen3 and Qwen-3next |
| `pr-vllm-27532` | upstream-code | [`sources/prs/vllm/PR-27532.md`](../sources/prs/vllm/PR-27532.md) | [Attention] Use sparse prefill kernel for fp8 kv-cache in DeepSeek-v3.2 |
| `pr-vllm-27660` | upstream-code | [`sources/prs/vllm/PR-27660.md`](../sources/prs/vllm/PR-27660.md) | [Feature] Batch invariant torch.compile |
| `pr-vllm-27883` | upstream-code | [`sources/prs/vllm/PR-27883.md`](../sources/prs/vllm/PR-27883.md) | [Performance] Fused blockwise quant RMS norm |
| `pr-vllm-27897` | upstream-code | [`sources/prs/vllm/PR-27897.md`](../sources/prs/vllm/PR-27897.md) | [Performance][B200] Fix deepgemm prologue |
| `pr-vllm-28032` | upstream-code | [`sources/prs/vllm/PR-28032.md`](../sources/prs/vllm/PR-28032.md) | [ROCm][MLA] enable fp8 MLA decode on ROCm |
| `pr-vllm-28358` | upstream-code | [`sources/prs/vllm/PR-28358.md`](../sources/prs/vllm/PR-28358.md) | [Performance][B200] silu_mul_quant: pack scales in int32 |
| `pr-vllm-28687` | upstream-code | [`sources/prs/vllm/PR-28687.md`](../sources/prs/vllm/PR-28687.md) | [Performance] Reduce DeepGEMM N dim restriction from 128 to 64 multiplier  |
| `pr-vllm-29213` | upstream-code | [`sources/prs/vllm/PR-29213.md`](../sources/prs/vllm/PR-29213.md) | [Perf][Kernels] Enable FlashInfer DeepGEMM swapAB on SM90 (for W8A8 Linear Op) |
| `pr-vllm-29346` | upstream-code | [`sources/prs/vllm/PR-29346.md`](../sources/prs/vllm/PR-29346.md) | [Perf] Disable DeepGEMM MoE by default when TP=8 is used |
| `pr-vllm-29691` | upstream-code | [`sources/prs/vllm/PR-29691.md`](../sources/prs/vllm/PR-29691.md) | [Kernel]Support W4A8 Grouped GEMM on Hopper |
| `pr-vllm-29748` | upstream-code | [`sources/prs/vllm/PR-29748.md`](../sources/prs/vllm/PR-29748.md) | [MoE-FP8-modelopt] Add FlashInfer alignment padding for intermediate dimensions |
| `pr-vllm-29757` | upstream-code | [`sources/prs/vllm/PR-29757.md`](../sources/prs/vllm/PR-29757.md) | Add Mistral Large 3 and Ministral 3 |
| `pr-vllm-29795` | upstream-code | [`sources/prs/vllm/PR-29795.md`](../sources/prs/vllm/PR-29795.md) | [Perf] Improve fp8 quant in mla; replace ReduceSum with ReduceScatterSum |
| `pr-vllm-29890` | upstream-code | [`sources/prs/vllm/PR-29890.md`](../sources/prs/vllm/PR-29890.md) | [Bugfix] Fix FP8 MoE LoRA |
| `pr-vllm-29901` | upstream-code | [`sources/prs/vllm/PR-29901.md`](../sources/prs/vllm/PR-29901.md) | [Kernel][Quantization][MoE] add marlin kernel support for turing (sm75) |
| `pr-vllm-30071` | upstream-code | [`sources/prs/vllm/PR-30071.md`](../sources/prs/vllm/PR-30071.md) | [Quantization] Support Quark int4-fp8 w4a8 for MoE |
| `pr-vllm-30141` | upstream-code | [`sources/prs/vllm/PR-30141.md`](../sources/prs/vllm/PR-30141.md) | Add llmcompressor fp8 kv-cache quant (per-tensor and per-attn_head) |
| `pr-vllm-30267` | upstream-code | [`sources/prs/vllm/PR-30267.md`](../sources/prs/vllm/PR-30267.md) | [Bugfix] Fix DeepGEMM after #29546  |
| `pr-vllm-30286` | upstream-code | [`sources/prs/vllm/PR-30286.md`](../sources/prs/vllm/PR-30286.md) | [LoRA] Support Quantized Adapters |
| `pr-vllm-30336` | upstream-code | [`sources/prs/vllm/PR-30336.md`](../sources/prs/vllm/PR-30336.md) | [Bugfix] Fix fp8 DeepGemm compilation issues |
| `pr-vllm-30357` | upstream-code | [`sources/prs/vllm/PR-30357.md`](../sources/prs/vllm/PR-30357.md) | [ROCm][Quantization] GPT OSS Upstream MoE wmxfp4_afp8 with static scales |
| `pr-vllm-30484` | upstream-code | [`sources/prs/vllm/PR-30484.md`](../sources/prs/vllm/PR-30484.md) | [Feature] Add SM103 (Blackwell Ultra) Support to vLLM |
| `pr-vllm-30647` | upstream-code | [`sources/prs/vllm/PR-30647.md`](../sources/prs/vllm/PR-30647.md) | [Perf] Eliminate padding and slicing op for GPT-OSS with Flashinfer MXFP4 MXFP8 MoE |
| `pr-vllm-30746` | upstream-code | [`sources/prs/vllm/PR-30746.md`](../sources/prs/vllm/PR-30746.md) | [SM100] Enable fp8 compute for prefill MLA |
| `pr-vllm-30957` | upstream-code | [`sources/prs/vllm/PR-30957.md`](../sources/prs/vllm/PR-30957.md) | [Feature]: Support NVIDIA ModelOpt HF FP8 variants FP8_PER_CHANNEL_PER_TOKEN and FP8_PB_WO  in vLLM |
| `pr-vllm-31106` | upstream-code | [`sources/prs/vllm/PR-31106.md`](../sources/prs/vllm/PR-31106.md) | [Bugfix][Hardware][AMD] Consolidate FP8 min/max values helper function |
| `pr-vllm-31195` | upstream-code | [`sources/prs/vllm/PR-31195.md`](../sources/prs/vllm/PR-31195.md) | [SM100] Resubmit FMHA FP8 prefill for MLA |
| `pr-vllm-31502` | upstream-code | [`sources/prs/vllm/PR-31502.md`](../sources/prs/vllm/PR-31502.md) | [Bugfix][ROCm] Fix Static Quant Issue |
| `pr-vllm-31742` | upstream-code | [`sources/prs/vllm/PR-31742.md`](../sources/prs/vllm/PR-31742.md) | [Bugfix] Fix Broken ModelOpt NVFP4 MoE |
| `pr-vllm-31916` | upstream-code | [`sources/prs/vllm/PR-31916.md`](../sources/prs/vllm/PR-31916.md) | [1/N][Attention] Restructure attention: move files |
| `pr-vllm-32064` | upstream-code | [`sources/prs/vllm/PR-32064.md`](../sources/prs/vllm/PR-32064.md) | [5/N][Attention] Finish eliminating `vllm/attention` folder |
| `pr-vllm-32619` | upstream-code | [`sources/prs/vllm/PR-32619.md`](../sources/prs/vllm/PR-32619.md) | [Perf] Create TMA-aligned input scale tensor for DeepGemm on Hopper |
| `pr-vllm-33076` | upstream-code | [`sources/prs/vllm/PR-33076.md`](../sources/prs/vllm/PR-33076.md) | Support compress-tensors with nvfp4 or fp8 weights and modelopt with nvfp4 weights on Turing |
| `pr-vllm-33174` | upstream-code | [`sources/prs/vllm/PR-33174.md`](../sources/prs/vllm/PR-33174.md) | Add support for Mistral Large 3 inference with Flashinfer MoE |
| `pr-vllm-33255` | upstream-code | [`sources/prs/vllm/PR-33255.md`](../sources/prs/vllm/PR-33255.md) | [Bugfix] Fix quant RMS norm fusion for quantization with TMA-aligned scales |
| `pr-vllm-33285` | upstream-code | [`sources/prs/vllm/PR-33285.md`](../sources/prs/vllm/PR-33285.md) | [Bugfix] Register fp8 cutlass_group_gemm as supported for only SM90+SM100 |
| `pr-vllm-33506` | upstream-code | [`sources/prs/vllm/PR-33506.md`](../sources/prs/vllm/PR-33506.md) | [Kernel] Support Flashinfer trtllm fused MoE non gated FP8 & NVFP4 |
| `pr-vllm-33517` | upstream-code | [`sources/prs/vllm/PR-33517.md`](../sources/prs/vllm/PR-33517.md) | [Kernel] Add enable_sm120_or_later for SM121 (DGX Spark) CUTLASS support |
| `pr-vllm-33568` | upstream-code | [`sources/prs/vllm/PR-33568.md`](../sources/prs/vllm/PR-33568.md) | [Perf] Disable clean_logits in deepgemm fp8_mqa_logits kernel |
| `pr-vllm-33695` | upstream-code | [`sources/prs/vllm/PR-33695.md`](../sources/prs/vllm/PR-33695.md) | enable skipping of SW attention layers when using FP8 KV cache |
| `pr-vllm-34260` | upstream-code | [`sources/prs/vllm/PR-34260.md`](../sources/prs/vllm/PR-34260.md) | [Model Bash]: Improve FP8 Oracle for Config Specific Kernel Selection |
| `pr-vllm-34448` | upstream-code | [`sources/prs/vllm/PR-34448.md`](../sources/prs/vllm/PR-34448.md) | [Kernel] Integrate SM100 MXFP8 blockscaled grouped MM and quant kernels |
| `pr-vllm-34494` | upstream-code | [`sources/prs/vllm/PR-34494.md`](../sources/prs/vllm/PR-34494.md) | [Bugfix] Handle num_expert_group=None in flashinfer block-scale FP8 MoE |
| `pr-vllm-34556` | upstream-code | [`sources/prs/vllm/PR-34556.md`](../sources/prs/vllm/PR-34556.md) | [Quantization] add humming quantization kernel |
| `pr-vllm-34597` | upstream-code | [`sources/prs/vllm/PR-34597.md`](../sources/prs/vllm/PR-34597.md) | [Kernel] Add FP8 KV cache support to Triton MLA decode attention |
| `pr-vllm-34725` | upstream-code | [`sources/prs/vllm/PR-34725.md`](../sources/prs/vllm/PR-34725.md) | [Bugfix] Fix NVFP4 TRTLLM MoE non-gated support; add gsm8k for Nemotron-3-Nano FP8+NVFP4 |
| `pr-vllm-35053` | upstream-code | [`sources/prs/vllm/PR-35053.md`](../sources/prs/vllm/PR-35053.md) | Integrate flashinfer mm_mxfp8 in ModelOpt MXFP8 |
| `pr-vllm-35271` | upstream-code | [`sources/prs/vllm/PR-35271.md`](../sources/prs/vllm/PR-35271.md) | [Feat] Add CUDA torch fallbacks for fp8_mqa_logits/fp8_paged_mqa_logits_torch function |
| `pr-vllm-35290` | upstream-code | [`sources/prs/vllm/PR-35290.md`](../sources/prs/vllm/PR-35290.md) | [Attention][Perf] Optimize cp_gather_and_upconvert_fp8_kv_cache - DeepSeek-v3.2 |
| `pr-vllm-35448` | upstream-code | [`sources/prs/vllm/PR-35448.md`](../sources/prs/vllm/PR-35448.md) | [Quant][Feature] Support online MXFP8 quantization for MoE and dense models |
| `pr-vllm-35850` | upstream-code | [`sources/prs/vllm/PR-35850.md`](../sources/prs/vllm/PR-35850.md) | [ROCm] Support MLA with nhead<16 and FP8 KV cache for TP=8 (Kimi K2.5/Linear) |
| `pr-vllm-35891` | upstream-code | [`sources/prs/vllm/PR-35891.md`](../sources/prs/vllm/PR-35891.md) | [Perf] Support FP8 KV cache for Flashinfer MLA Sparse |
| `pr-vllm-35986` | upstream-code | [`sources/prs/vllm/PR-35986.md`](../sources/prs/vllm/PR-35986.md) | Add support for ModelOpt MXFP8 MoE models |
| `pr-vllm-36017` | upstream-code | [`sources/prs/vllm/PR-36017.md`](../sources/prs/vllm/PR-36017.md) | [Bugfix] Fix passing of activation_type to trtllm fused MoE NVFP4 and FP8 |
| `pr-vllm-36205` | upstream-code | [`sources/prs/vllm/PR-36205.md`](../sources/prs/vllm/PR-36205.md) | [mla] Support fused FP8/NVFP4 output quantization in MLA attention (#35792) |
| `pr-vllm-36307` | upstream-code | [`sources/prs/vllm/PR-36307.md`](../sources/prs/vllm/PR-36307.md) | [Perf] Add TRTLLM FP8 MoE Modular Kernel |
| `pr-vllm-36458` | upstream-code | [`sources/prs/vllm/PR-36458.md`](../sources/prs/vllm/PR-36458.md) | [XPU] Support block fp8 moe by fallback to TritonExpert on XPU |
| `pr-vllm-36518` | upstream-code | [`sources/prs/vllm/PR-36518.md`](../sources/prs/vllm/PR-36518.md) | [Kernel] Fuse FP8 output quantization into merge_attn_states |
| `pr-vllm-36728` | upstream-code | [`sources/prs/vllm/PR-36728.md`](../sources/prs/vllm/PR-36728.md) | [Bug][MoE] Strengthen _supports_current_device() checks in the TRTLLM FP8, NVFP4, and FlashInfer CuteDSL MoE experts |
| `pr-vllm-37054` | upstream-code | [`sources/prs/vllm/PR-37054.md`](../sources/prs/vllm/PR-37054.md) | [Bugfix] Fix KV scales inconsistency in fp8 MLA & FlashInfer kv_cache_dtype "auto" leading to gibberish |
| `pr-vllm-37143` | upstream-code | [`sources/prs/vllm/PR-37143.md`](../sources/prs/vllm/PR-37143.md) | [XPU] support MLA model on Intel GPU |
| `pr-vllm-37252` | upstream-code | [`sources/prs/vllm/PR-37252.md`](../sources/prs/vllm/PR-37252.md) | [Perf] Set Flashinfer sparse MLA as default backend for FP8 kv cache |
| `pr-vllm-37605` | upstream-code | [`sources/prs/vllm/PR-37605.md`](../sources/prs/vllm/PR-37605.md) | [Bugfix] Disable monolithic TRTLLM MoE for Renormalize routing (#37591) |
| `pr-vllm-37695` | upstream-code | [`sources/prs/vllm/PR-37695.md`](../sources/prs/vllm/PR-37695.md) | [Perf] Use torch compile to fuse pack topk in trtllm moe |
| `pr-vllm-37718` | upstream-code | [`sources/prs/vllm/PR-37718.md`](../sources/prs/vllm/PR-37718.md) | [Bug] Fix fp8 deepgemm batch invariant |
| `pr-vllm-37970` | upstream-code | [`sources/prs/vllm/PR-37970.md`](../sources/prs/vllm/PR-37970.md) | [Kernel] Optimize SM120 CUTLASS blockwise FP8 GEMM |
| `pr-vllm-38065` | upstream-code | [`sources/prs/vllm/PR-38065.md`](../sources/prs/vllm/PR-38065.md) | [Perf] FP8 FlashInfer Attn for ViT |
| `pr-vllm-38083` | upstream-code | [`sources/prs/vllm/PR-38083.md`](../sources/prs/vllm/PR-38083.md) | [Bugfix] Fix DeepGemm E8M0 accuracy degradation for Qwen3.5 FP8 on Blackwell |
| `pr-vllm-38325` | upstream-code | [`sources/prs/vllm/PR-38325.md`](../sources/prs/vllm/PR-38325.md) | [Kernel] Add swapAB support for SM120 CUTLASS blockwise FP8 GEMM  |
| `pr-vllm-38329` | upstream-code | [`sources/prs/vllm/PR-38329.md`](../sources/prs/vllm/PR-38329.md) | [MoE] Add RoutingMethodType.Simulated to TRT-LLM FP8/NVFP4 kernel allowlists |
| `pr-vllm-38423` | upstream-code | [`sources/prs/vllm/PR-38423.md`](../sources/prs/vllm/PR-38423.md) | [NVIDIA] Bugfix NVFP4 DGX Spark and RTX50 |
| `pr-vllm-38442` | upstream-code | [`sources/prs/vllm/PR-38442.md`](../sources/prs/vllm/PR-38442.md) | [QeRL] Fix online quantized reloading |
| `pr-vllm-38504` | upstream-code | [`sources/prs/vllm/PR-38504.md`](../sources/prs/vllm/PR-38504.md) | [Kernels][MoE] Fix legacy_routing to use bitmatrix-based routing path |
| `pr-vllm-38682` | upstream-code | [`sources/prs/vllm/PR-38682.md`](../sources/prs/vllm/PR-38682.md) | [XPU] add  xpu backend implementation of mxfp8 quant |
| `pr-vllm-38815` | upstream-code | [`sources/prs/vllm/PR-38815.md`](../sources/prs/vllm/PR-38815.md) | [Quant] add CompressedTensorsW8A8Mxfp8 for linear and MoE layers |
| `pr-vllm-38859` | upstream-code | [`sources/prs/vllm/PR-38859.md`](../sources/prs/vllm/PR-38859.md) | [Bugfix] Re-enable Renormalize routing for TRT-LLM MoE experts |
| `pr-vllm-38922` | upstream-code | [`sources/prs/vllm/PR-38922.md`](../sources/prs/vllm/PR-38922.md) | [Bugfix] Fix broken explicit unquantized kv cache dtype support |
| `pr-vllm-38960` | upstream-code | [`sources/prs/vllm/PR-38960.md`](../sources/prs/vllm/PR-38960.md) | [MoE Refactor] Split up compressed_tensors_moe.py |
| `pr-vllm-38989` | upstream-code | [`sources/prs/vllm/PR-38989.md`](../sources/prs/vllm/PR-38989.md) | [Bug] Fix routing bias dtype for trtllm per-block fp8 moe |
| `pr-vllm-38993` | upstream-code | [`sources/prs/vllm/PR-38993.md`](../sources/prs/vllm/PR-38993.md) | [Perf] Change Trtllm fp8 MoE to use Shuffled Weights and BlockMajorK Layout |
| `pr-vllm-39054` | upstream-code | [`sources/prs/vllm/PR-39054.md`](../sources/prs/vllm/PR-39054.md) | [Bug] Fix Trtllm Fp8 MoE Weight Shuffle Memory Fragamentation |
| `pr-vllm-39205` | upstream-code | [`sources/prs/vllm/PR-39205.md`](../sources/prs/vllm/PR-39205.md) | [Refactor] Move MXFP8 GEMM management into MxFp8LinearKernel |
| `pr-vllm-39391` | upstream-code | [`sources/prs/vllm/PR-39391.md`](../sources/prs/vllm/PR-39391.md) | fix: clamp NaN/Inf in topk_softmax to prevent duplicate expert IDs |
| `pr-vllm-39547` | upstream-code | [`sources/prs/vllm/PR-39547.md`](../sources/prs/vllm/PR-39547.md) | [Perf] Fuse Zero Initializer for FP8 DeepGemm Block Quant Kernel |
| `pr-vllm-39752` | upstream-code | [`sources/prs/vllm/PR-39752.md`](../sources/prs/vllm/PR-39752.md) | add warning when FP8 KV cache misses prefill query quantization |
| `pr-vllm-40177` | upstream-code | [`sources/prs/vllm/PR-40177.md`](../sources/prs/vllm/PR-40177.md) | Add nvfp4 kv cache support |
| `pr-vllm-40408` | upstream-code | [`sources/prs/vllm/PR-40408.md`](../sources/prs/vllm/PR-40408.md) | [Perf] Batch invariance with Cutlass fp8 support, 28.9% E2E latency improvement |
| `pr-vllm-40574` | upstream-code | [`sources/prs/vllm/PR-40574.md`](../sources/prs/vllm/PR-40574.md) | [MoE] Move cutlass moe to fused_moe/experts/ |
| `pr-vllm-40850` | upstream-code | [`sources/prs/vllm/PR-40850.md`](../sources/prs/vllm/PR-40850.md) | [Kernel][Helion] Optimize Helion config parsing latency |
| `pr-vllm-40960` | upstream-code | [`sources/prs/vllm/PR-40960.md`](../sources/prs/vllm/PR-40960.md) | [DSV4] Add BF16 and MXFP8 A2A support for flashinfer a2a one sided |
| `pr-vllm-41326` | upstream-code | [`sources/prs/vllm/PR-41326.md`](../sources/prs/vllm/PR-41326.md) | Faster per-token fp8 group quant packed kernel for blackwell |
| `pr-vllm-41566` | upstream-code | [`sources/prs/vllm/PR-41566.md`](../sources/prs/vllm/PR-41566.md) | [Quantization] Rework quantization_config to use QuantKey and allow for activation override |
| `pr-vllm-41778` | upstream-code | [`sources/prs/vllm/PR-41778.md`](../sources/prs/vllm/PR-41778.md) | [MLA Attention Backend] Add TOKENSPEED_MLA backend for DSR1/Kimi K25 prefill + decode on Blackwell |
| `pr-vllm-41868` | upstream-code | [`sources/prs/vllm/PR-41868.md`](../sources/prs/vllm/PR-41868.md) | [CUDA][CUTLASS] Enable cutlass scaled mm for non-compatible sizes  |
| `pr-vllm-41882` | upstream-code | [`sources/prs/vllm/PR-41882.md`](../sources/prs/vllm/PR-41882.md) | Add NVFP4 all-gather GEMM fusion for AsyncTP |
| `pr-vllm-41979` | upstream-code | [`sources/prs/vllm/PR-41979.md`](../sources/prs/vllm/PR-41979.md) | [MoE] Move various experts classes to fused_moe/experts/ |
| `pr-vllm-41986` | upstream-code | [`sources/prs/vllm/PR-41986.md`](../sources/prs/vllm/PR-41986.md) | [Bugfix] Add swiglu limits to deepgemm fp8 methods |
| `pr-vllm-42153` | upstream-code | [`sources/prs/vllm/PR-42153.md`](../sources/prs/vllm/PR-42153.md) | [Perf] Use 2D-grid to eliminate divmod in W8W8 group quant |
| `pr-vllm-42236` | upstream-code | [`sources/prs/vllm/PR-42236.md`](../sources/prs/vllm/PR-42236.md) | [DSv4] Improved dequant gather K cache kernel |

<a id="gdc"></a>
## gdc

2 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-cutlass-2161` | upstream-code | [`sources/prs/cutlass/PR-2161.md`](../sources/prs/cutlass/PR-2161.md) | Blockwise Improvement and Programmatic Dependent Launch |
| `pr-flashinfer-1695` | upstream-code | [`sources/prs/flashinfer/PR-1695.md`](../sources/prs/flashinfer/PR-1695.md) | [cute_dsl] add gemm + all reduce (two_shot)  |

<a id="hopper"></a>
## hopper

242 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-cccl-cub-2944` | upstream-code | [`sources/prs/cccl-cub/PR-2944.md`](../sources/prs/cccl-cub/PR-2944.md) | fix thread-reduce performance regression |
| `pr-cccl-cub-3236` | upstream-code | [`sources/prs/cccl-cub/PR-3236.md`](../sources/prs/cccl-cub/PR-3236.md) | Fix scan / sm90 perf regression  |
| `pr-cccl-cub-3559` | upstream-code | [`sources/prs/cccl-cub/PR-3559.md`](../sources/prs/cccl-cub/PR-3559.md) | Add b200 tunings for scan.exclusive.sum |
| `pr-cccl-cub-5061` | upstream-code | [`sources/prs/cccl-cub/PR-5061.md`](../sources/prs/cccl-cub/PR-5061.md) | Replace CG by TMA copy in bulk copy fallback path |
| `pr-cccl-cub-5078` | upstream-code | [`sources/prs/cccl-cub/PR-5078.md`](../sources/prs/cccl-cub/PR-5078.md) | Small fixes and improvements to DeviceTransform |
| `pr-cccl-cub-5122` | upstream-code | [`sources/prs/cccl-cub/PR-5122.md`](../sources/prs/cccl-cub/PR-5122.md) | Try, fail and ignore to guarantee dynamic SMEM alignment on Hopper |
| `pr-cccl-cub-5178` | upstream-code | [`sources/prs/cccl-cub/PR-5178.md`](../sources/prs/cccl-cub/PR-5178.md) | Support types with any alignment in UBLKCP transform kernel |
| `pr-cccl-cub-5269` | upstream-code | [`sources/prs/cccl-cub/PR-5269.md`](../sources/prs/cccl-cub/PR-5269.md) | Add sm90 tunings for RFA F32 |
| `pr-cccl-cub-5414` | upstream-code | [`sources/prs/cccl-cub/PR-5414.md`](../sources/prs/cccl-cub/PR-5414.md) | Move TMA barrier in DeviceTransform into dynamic SMEM |
| `pr-cccl-cub-5526` | upstream-code | [`sources/prs/cccl-cub/PR-5526.md`](../sources/prs/cccl-cub/PR-5526.md) | Special case `DeviceTransform` for no inputs and provide a `DeviceTransform::Fill` API |
| `pr-cccl-cub-5780` | upstream-code | [`sources/prs/cccl-cub/PR-5780.md`](../sources/prs/cccl-cub/PR-5780.md) | [CUB] Implement `BlockLoadToShared` |
| `pr-cccl-cub-6007` | upstream-code | [`sources/prs/cccl-cub/PR-6007.md`](../sources/prs/cccl-cub/PR-6007.md) | Use just SYNCS unit to wait on cuda::barrier on SM90+ |
| `pr-cccl-cub-6069` | upstream-code | [`sources/prs/cccl-cub/PR-6069.md`](../sources/prs/cccl-cub/PR-6069.md) | Add dynamic CUB dispatch for segmented_sort |
| `pr-cccl-cub-6077` | upstream-code | [`sources/prs/cccl-cub/PR-6077.md`](../sources/prs/cccl-cub/PR-6077.md) | [CUB] Use `BlockLoadToShared` in `DeviceMerge` |
| `pr-cccl-cub-6189` | upstream-code | [`sources/prs/cccl-cub/PR-6189.md`](../sources/prs/cccl-cub/PR-6189.md) | [CUB] Fix mask types in block_radix_rank.cuh |
| `pr-cccl-cub-6246` | upstream-code | [`sources/prs/cccl-cub/PR-6246.md`](../sources/prs/cccl-cub/PR-6246.md) | Fix invalid refactoring of  #4377 |
| `pr-cccl-cub-6265` | upstream-code | [`sources/prs/cccl-cub/PR-6265.md`](../sources/prs/cccl-cub/PR-6265.md) | [Backport 3.1] Fix invalid refactoring of  #4377 (#6246) |
| `pr-cccl-cub-6329` | upstream-code | [`sources/prs/cccl-cub/PR-6329.md`](../sources/prs/cccl-cub/PR-6329.md) | Improve `cuda::barrier` TMA examples and `elect_one` in `DeviceTransform` |
| `pr-cccl-cub-6362` | upstream-code | [`sources/prs/cccl-cub/PR-6362.md`](../sources/prs/cccl-cub/PR-6362.md) | Use `cp_async_bulk(space_shared,...)` when available |
| `pr-cccl-cub-6496` | upstream-code | [`sources/prs/cccl-cub/PR-6496.md`](../sources/prs/cccl-cub/PR-6496.md) | Expose `ptx::mbarrier_inval` and use it |
| `pr-cccl-cub-6666` | upstream-code | [`sources/prs/cccl-cub/PR-6666.md`](../sources/prs/cccl-cub/PR-6666.md) | Migrate cuco HLL |
| `pr-cccl-cub-6811` | upstream-code | [`sources/prs/cccl-cub/PR-6811.md`](../sources/prs/cccl-cub/PR-6811.md) | Integrate decoupled lookahead warpspeed scan |
| `pr-cccl-cub-6814` | upstream-code | [`sources/prs/cccl-cub/PR-6814.md`](../sources/prs/cccl-cub/PR-6814.md) | Improve our `WarpReduce` implementation |
| `pr-cccl-cub-6819` | upstream-code | [`sources/prs/cccl-cub/PR-6819.md`](../sources/prs/cccl-cub/PR-6819.md) | Use integer promotion for `warp_reduce` |
| `pr-cccl-cub-6921` | upstream-code | [`sources/prs/cccl-cub/PR-6921.md`](../sources/prs/cccl-cub/PR-6921.md) | Use vectorized transform kernel for sizeof(T) < 4 workloads of arity >1 on Hopper |
| `pr-cccl-cub-6980` | upstream-code | [`sources/prs/cccl-cub/PR-6980.md`](../sources/prs/cccl-cub/PR-6980.md) | Initial version of `DeviceSegmentedTopk` for fixed-size segments |
| `pr-cccl-cub-7245` | upstream-code | [`sources/prs/cccl-cub/PR-7245.md`](../sources/prs/cccl-cub/PR-7245.md) | Fix `is_address_from` for `cluster_shared` for pre-sm_90 |
| `pr-cccl-cub-7346` | upstream-code | [`sources/prs/cccl-cub/PR-7346.md`](../sources/prs/cccl-cub/PR-7346.md) | Implement the new tuning API for deterministic (rfa) reduce dispatch |
| `pr-cccl-cub-7561` | upstream-code | [`sources/prs/cccl-cub/PR-7561.md`](../sources/prs/cccl-cub/PR-7561.md) | Remove recursion from __internal_is_address_from |
| `pr-cccl-cub-7575` | upstream-code | [`sources/prs/cccl-cub/PR-7575.md`](../sources/prs/cccl-cub/PR-7575.md) | Support more types in decoupled lookback fastpath |
| `pr-cccl-cub-7681` | upstream-code | [`sources/prs/cccl-cub/PR-7681.md`](../sources/prs/cccl-cub/PR-7681.md) | Fix max atomic size for NVHPC |
| `pr-cccl-cub-8067` | upstream-code | [`sources/prs/cccl-cub/PR-8067.md`](../sources/prs/cccl-cub/PR-8067.md) | Use nv atomics in grid sync |
| `pr-cccl-cub-8395` | upstream-code | [`sources/prs/cccl-cub/PR-8395.md`](../sources/prs/cccl-cub/PR-8395.md) | [CUB] Replace `Shuffle(Up|Down|Index)` with cuda::device::warp_shuffle - RadixSort only |
| `pr-cccl-cub-8421` | upstream-code | [`sources/prs/cccl-cub/PR-8421.md`](../sources/prs/cccl-cub/PR-8421.md) | New tuning API for DeviceUniqueByKey |
| `pr-cutlass-1661` | upstream-code | [`sources/prs/cutlass/PR-1661.md`](../sources/prs/cutlass/PR-1661.md) | Skip void-C kernels in the profiler when beta is non zero |
| `pr-cutlass-1795` | upstream-code | [`sources/prs/cutlass/PR-1795.md`](../sources/prs/cutlass/PR-1795.md) | Support for TMA Epilogue for Group Gemm and add pingpong ptr array & Group Gemm |
| `pr-cutlass-1883` | upstream-code | [`sources/prs/cutlass/PR-1883.md`](../sources/prs/cutlass/PR-1883.md) | Improve sm90 mixed dtype kernel |
| `pr-cutlass-1932` | upstream-code | [`sources/prs/cutlass/PR-1932.md`](../sources/prs/cutlass/PR-1932.md) | Blockwise Scaling for FP8 |
| `pr-cutlass-2095` | upstream-code | [`sources/prs/cutlass/PR-2095.md`](../sources/prs/cutlass/PR-2095.md) | Improvements for: Groupwise scaling along M for FP8 gemm |
| `pr-cutlass-2123` | upstream-code | [`sources/prs/cutlass/PR-2123.md`](../sources/prs/cutlass/PR-2123.md) | Hopper Grouped GEMM support for FP8 Accum |
| `pr-cutlass-2172` | upstream-code | [`sources/prs/cutlass/PR-2172.md`](../sources/prs/cutlass/PR-2172.md) | Fix SM90 beta=1 hang and stream-K launch errors |
| `pr-cutlass-2270` | upstream-code | [`sources/prs/cutlass/PR-2270.md`](../sources/prs/cutlass/PR-2270.md) | hopper-blockwise-generalization-optimization |
| `pr-cutlass-3176` | upstream-code | [`sources/prs/cutlass/PR-3176.md`](../sources/prs/cutlass/PR-3176.md) | Small Tile N BlockScaled GEMM + Grouped GEMM on SM12x |
| `pr-cutlass-3184` | upstream-code | [`sources/prs/cutlass/PR-3184.md`](../sources/prs/cutlass/PR-3184.md) | Add Snake activation functor for EVT |
| `pr-deepgemm-112` | upstream-code | [`sources/prs/deepgemm/PR-112.md`](../sources/prs/deepgemm/PR-112.md) | Add more GPU architectures support |
| `pr-deepgemm-158` | upstream-code | [`sources/prs/deepgemm/PR-158.md`](../sources/prs/deepgemm/PR-158.md) | Fix inappropriate configs for some small shapes |
| `pr-deepgemm-193` | upstream-code | [`sources/prs/deepgemm/PR-193.md`](../sources/prs/deepgemm/PR-193.md) | Fix multicast bug and optimize masked GEMM |
| `pr-deepgemm-198` | upstream-code | [`sources/prs/deepgemm/PR-198.md`](../sources/prs/deepgemm/PR-198.md) | Make various updates and fixes |
| `pr-deepgemm-270` | upstream-code | [`sources/prs/deepgemm/PR-270.md`](../sources/prs/deepgemm/PR-270.md) | fix: use SM90ArchSpec instead of SM100ArchSpec in sm90_bf16_k_grouped_gemm |
| `pr-deepgemm-316` | upstream-code | [`sources/prs/deepgemm/PR-316.md`](../sources/prs/deepgemm/PR-316.md) | Add various optimizations and Mega MoE benchmarks |
| `pr-deepgemm-328` | upstream-code | [`sources/prs/deepgemm/PR-328.md`](../sources/prs/deepgemm/PR-328.md) | Sync nv_dev with upstream #316 (Mega MoE optimizations & benchmarks) |
| `pr-flash-attention-1072` | upstream-code | [`sources/prs/flash-attention/PR-1072.md`](../sources/prs/flash-attention/PR-1072.md) | Add var-seq-len to FA3 fp16 / bf16 fwd |
| `pr-flash-attention-1100` | upstream-code | [`sources/prs/flash-attention/PR-1100.md`](../sources/prs/flash-attention/PR-1100.md) | Fp8 kernel with "in-kernel" transpose of V in producer |
| `pr-flash-attention-1173` | upstream-code | [`sources/prs/flash-attention/PR-1173.md`](../sources/prs/flash-attention/PR-1173.md) | FA3 FP8 qkv descales + restore max offset for h128 causal + added sync for producer WG |
| `pr-flash-attention-1182` | upstream-code | [`sources/prs/flash-attention/PR-1182.md`](../sources/prs/flash-attention/PR-1182.md) | Add seqused_q in fwd / bwd and seqused_k in bwd in hopper FA. |
| `pr-flash-attention-1233` | upstream-code | [`sources/prs/flash-attention/PR-1233.md`](../sources/prs/flash-attention/PR-1233.md) | Add local attention in Hopper FAv3 |
| `pr-flash-attention-1236` | upstream-code | [`sources/prs/flash-attention/PR-1236.md`](../sources/prs/flash-attention/PR-1236.md) | FA3 kvcache + split kv + gqa parallelization |
| `pr-flash-attention-1268` | upstream-code | [`sources/prs/flash-attention/PR-1268.md`](../sources/prs/flash-attention/PR-1268.md) | Paged Attention support for FA3 |
| `pr-flash-attention-1331` | upstream-code | [`sources/prs/flash-attention/PR-1331.md`](../sources/prs/flash-attention/PR-1331.md) | FA3 paged attention: Readiness for Cutlass 3.6 / default value for block_table |
| `pr-flash-attention-1361` | upstream-code | [`sources/prs/flash-attention/PR-1361.md`](../sources/prs/flash-attention/PR-1361.md) | Fix FA3 Varlen Performance regression |
| `pr-flash-attention-1603` | upstream-code | [`sources/prs/flash-attention/PR-1603.md`](../sources/prs/flash-attention/PR-1603.md) | add sm_margin for hopper flash_attn_qkvpacked_func |
| `pr-flash-attention-1604` | upstream-code | [`sources/prs/flash-attention/PR-1604.md`](../sources/prs/flash-attention/PR-1604.md) | Support hdimQK != hdimV backward |
| `pr-flash-attention-1674` | upstream-code | [`sources/prs/flash-attention/PR-1674.md`](../sources/prs/flash-attention/PR-1674.md) | [BE] use more minimal torch headers for hopper/flash_api.cpp |
| `pr-flash-attention-1723` | upstream-code | [`sources/prs/flash-attention/PR-1723.md`](../sources/prs/flash-attention/PR-1723.md) | Fix(hopper): Correct C++ syntax in epilogue_fwd.hpp |
| `pr-flash-attention-1769` | upstream-code | [`sources/prs/flash-attention/PR-1769.md`](../sources/prs/flash-attention/PR-1769.md) | Add torch.compile support to flash attention 3 |
| `pr-flash-attention-1791` | upstream-code | [`sources/prs/flash-attention/PR-1791.md`](../sources/prs/flash-attention/PR-1791.md) | ABI stable fa3 |
| `pr-flash-attention-1823` | upstream-code | [`sources/prs/flash-attention/PR-1823.md`](../sources/prs/flash-attention/PR-1823.md) | Add sorting and head swizzle to varlen scheduler |
| `pr-flash-attention-1868` | upstream-code | [`sources/prs/flash-attention/PR-1868.md`](../sources/prs/flash-attention/PR-1868.md) | flash-attn-cute bwd sm90 |
| `pr-flash-attention-1893` | upstream-code | [`sources/prs/flash-attention/PR-1893.md`](../sources/prs/flash-attention/PR-1893.md) | Improve causal backward determinism perf with SPT schedule |
| `pr-flash-attention-1904` | upstream-code | [`sources/prs/flash-attention/PR-1904.md`](../sources/prs/flash-attention/PR-1904.md) | C++11 fix warnings |
| `pr-flash-attention-1934` | upstream-code | [`sources/prs/flash-attention/PR-1934.md`](../sources/prs/flash-attention/PR-1934.md) | feat: Adding varlen support to cute-dsl sm80 bwd |
| `pr-flash-attention-1940` | upstream-code | [`sources/prs/flash-attention/PR-1940.md`](../sources/prs/flash-attention/PR-1940.md) | [Cute,Fwd,Sm100] Implement SplitKV |
| `pr-flash-attention-1985` | upstream-code | [`sources/prs/flash-attention/PR-1985.md`](../sources/prs/flash-attention/PR-1985.md) | [Cute] Block sparse support Sm100 |
| `pr-flash-attention-2043` | upstream-code | [`sources/prs/flash-attention/PR-2043.md`](../sources/prs/flash-attention/PR-2043.md) | [Cute,Fwd] Extend score_mod to variable sequence length |
| `pr-flash-attention-2070` | upstream-code | [`sources/prs/flash-attention/PR-2070.md`](../sources/prs/flash-attention/PR-2070.md) | Add score-mod bwd support  |
| `pr-flash-attention-2109` | upstream-code | [`sources/prs/flash-attention/PR-2109.md`](../sources/prs/flash-attention/PR-2109.md) | [Cute,Fwd,Sm100] fp8 e4m3 and e5m2 support |
| `pr-flash-attention-2136` | upstream-code | [`sources/prs/flash-attention/PR-2136.md`](../sources/prs/flash-attention/PR-2136.md) | block-sparse backward SM90 |
| `pr-flash-attention-2137` | upstream-code | [`sources/prs/flash-attention/PR-2137.md`](../sources/prs/flash-attention/PR-2137.md) | score-mod backward SM90 |
| `pr-flash-attention-2145` | upstream-code | [`sources/prs/flash-attention/PR-2145.md`](../sources/prs/flash-attention/PR-2145.md) | [CUTE][SM90]Enable pack-gqa with broadcasted maskmods |
| `pr-flash-attention-2158` | upstream-code | [`sources/prs/flash-attention/PR-2158.md`](../sources/prs/flash-attention/PR-2158.md) | [CUTE][SM90] GQA backward non deterministic |
| `pr-flash-attention-2174` | upstream-code | [`sources/prs/flash-attention/PR-2174.md`](../sources/prs/flash-attention/PR-2174.md) | [Cute] update row_max before safe overwrite for online_softmax |
| `pr-flash-attention-2178` | upstream-code | [`sources/prs/flash-attention/PR-2178.md`](../sources/prs/flash-attention/PR-2178.md) |  [AMD] Triton Backend for ROCm #3 |
| `pr-flash-attention-2186` | upstream-code | [`sources/prs/flash-attention/PR-2186.md`](../sources/prs/flash-attention/PR-2186.md) | [Cute,Fwd,Sm100] support irregular qhead / kvhead ratios |
| `pr-flash-attention-2189` | upstream-code | [`sources/prs/flash-attention/PR-2189.md`](../sources/prs/flash-attention/PR-2189.md) | [Cute][Flex] Fix expanded tensor bug |
| `pr-flash-attention-2194` | upstream-code | [`sources/prs/flash-attention/PR-2194.md`](../sources/prs/flash-attention/PR-2194.md) | [Cute, SM90] fix fwd varlen Cute implementation bug for H100 |
| `pr-flash-attention-2218` | upstream-code | [`sources/prs/flash-attention/PR-2218.md`](../sources/prs/flash-attention/PR-2218.md) | [Ai-assisted] CLC work stealing |
| `pr-flash-attention-2227` | upstream-code | [`sources/prs/flash-attention/PR-2227.md`](../sources/prs/flash-attention/PR-2227.md) | Nicer headdim error message |
| `pr-flash-attention-2236` | upstream-code | [`sources/prs/flash-attention/PR-2236.md`](../sources/prs/flash-attention/PR-2236.md) | [Cute,Flex,Fwd] Allow vectorized score_mod definitions |
| `pr-flash-attention-2242` | upstream-code | [`sources/prs/flash-attention/PR-2242.md`](../sources/prs/flash-attention/PR-2242.md) | Fix Hopper tests |
| `pr-flash-attention-2274` | upstream-code | [`sources/prs/flash-attention/PR-2274.md`](../sources/prs/flash-attention/PR-2274.md) | guard use_2cta_instrs on sm90 |
| `pr-flash-attention-2275` | upstream-code | [`sources/prs/flash-attention/PR-2275.md`](../sources/prs/flash-attention/PR-2275.md) | [CuteDSL][SM90] varlen bwd works |
| `pr-flash-attention-2282` | upstream-code | [`sources/prs/flash-attention/PR-2282.md`](../sources/prs/flash-attention/PR-2282.md) | Add FA4 publishing strategy |
| `pr-flash-attention-2297` | upstream-code | [`sources/prs/flash-attention/PR-2297.md`](../sources/prs/flash-attention/PR-2297.md) | [CuTeDSL][Sm80] basic fix for new api |
| `pr-flash-attention-2329` | upstream-code | [`sources/prs/flash-attention/PR-2329.md`](../sources/prs/flash-attention/PR-2329.md) | SM120 forward pass (Blackwell GeForce / DGX Spark) |
| `pr-flash-attention-2330` | upstream-code | [`sources/prs/flash-attention/PR-2330.md`](../sources/prs/flash-attention/PR-2330.md) | [Bwd,Sm120] Add SM120 backward pass support |
| `pr-flash-attention-2332` | upstream-code | [`sources/prs/flash-attention/PR-2332.md`](../sources/prs/flash-attention/PR-2332.md) | [cutlass] Allow compilation of cutlass FA3 for sm100 via enable_sm90 |
| `pr-flash-attention-2333` | upstream-code | [`sources/prs/flash-attention/PR-2333.md`](../sources/prs/flash-attention/PR-2333.md) | Add SM120 varlen attention support |
| `pr-flash-attention-2343` | upstream-code | [`sources/prs/flash-attention/PR-2343.md`](../sources/prs/flash-attention/PR-2343.md) | [ROCm] Auto-detect Triton backend if C++ extension is missing |
| `pr-flash-attention-2360` | upstream-code | [`sources/prs/flash-attention/PR-2360.md`](../sources/prs/flash-attention/PR-2360.md) | [Fwd,Sm90] Add paged KV attention support (tma and cp.async) |
| `pr-flash-attention-2365` | upstream-code | [`sources/prs/flash-attention/PR-2365.md`](../sources/prs/flash-attention/PR-2365.md) | [Sm90] Fix test_mask_mod and bwd block-sparse kwarg mismatch |
| `pr-flash-attention-2385` | upstream-code | [`sources/prs/flash-attention/PR-2385.md`](../sources/prs/flash-attention/PR-2385.md) | [ROCM] Fix windows issues |
| `pr-flash-attention-2388` | upstream-code | [`sources/prs/flash-attention/PR-2388.md`](../sources/prs/flash-attention/PR-2388.md) | fix: use LSE accum strides from params instead of hardcoded ones |
| `pr-flash-attention-2402` | upstream-code | [`sources/prs/flash-attention/PR-2402.md`](../sources/prs/flash-attention/PR-2402.md) | feat(cute): implement softcap backward pass, correct math formula, and resolve JIT cache bug |
| `pr-flash-attention-2481` | upstream-code | [`sources/prs/flash-attention/PR-2481.md`](../sources/prs/flash-attention/PR-2481.md) | [cute,bwd] fix PDL race in bwd_preprocess, which corrupting dpsum on SM90+ |
| `pr-flash-attention-2510` | upstream-code | [`sources/prs/flash-attention/PR-2510.md`](../sources/prs/flash-attention/PR-2510.md) | [Cute,Bwd,Sm90] Fix determinism for GQA, port Sm100 approach in |
| `pr-flash-attention-2513` | upstream-code | [`sources/prs/flash-attention/PR-2513.md`](../sources/prs/flash-attention/PR-2513.md) | SM90 FA4 QuACK 0.4 Compatibility |
| `pr-flash-attention-2515` | upstream-code | [`sources/prs/flash-attention/PR-2515.md`](../sources/prs/flash-attention/PR-2515.md) | Fix ZeroDivisionError in num_splits_heuristic for empty Q workloads |
| `pr-flash-attention-2563` | upstream-code | [`sources/prs/flash-attention/PR-2563.md`](../sources/prs/flash-attention/PR-2563.md) | [Cute, flex, sm90] fix sm90 flex |
| `pr-flashinfer-2439` | upstream-code | [`sources/prs/flashinfer/PR-2439.md`](../sources/prs/flashinfer/PR-2439.md) | Add sm90 guard to fence ptx |
| `pr-flashinfer-2630` | upstream-code | [`sources/prs/flashinfer/PR-2630.md`](../sources/prs/flashinfer/PR-2630.md) | Add parallel attention |
| `pr-flashinfer-2799` | upstream-code | [`sources/prs/flashinfer/PR-2799.md`](../sources/prs/flashinfer/PR-2799.md) | [fmha-v2] Support HND and NHD paged KV cache layouts with conditional stride handling |
| `pr-flashinfer-2841` | upstream-code | [`sources/prs/flashinfer/PR-2841.md`](../sources/prs/flashinfer/PR-2841.md) | [Perf] Add FMHAv2 to flashinfer_benchmark.py and eliminate unnecessary H2D |
| `pr-flashinfer-2928` | upstream-code | [`sources/prs/flashinfer/PR-2928.md`](../sources/prs/flashinfer/PR-2928.md) | fix: clamp enable_pdl=True to False on SM < 90 to prevent PDL PTX on Ampere |
| `pr-flashinfer-2951` | upstream-code | [`sources/prs/flashinfer/PR-2951.md`](../sources/prs/flashinfer/PR-2951.md) | feat: Add DCP All-to-All kernel for context-parallel attention reduction |
| `pr-flashinfer-3009` | upstream-code | [`sources/prs/flashinfer/PR-3009.md`](../sources/prs/flashinfer/PR-3009.md) | [feat] Faster topk algorithm |
| `pr-flashinfer-3084` | upstream-code | [`sources/prs/flashinfer/PR-3084.md`](../sources/prs/flashinfer/PR-3084.md) | perf: optimize MXFP4xBF16 & INT4xFP8 CUTLASS MoE backend for SM90 |
| `pr-flashinfer-3113` | upstream-code | [`sources/prs/flashinfer/PR-3113.md`](../sources/prs/flashinfer/PR-3113.md) | Fix: Extend b12x FP4 GEMM support to SM121 (GB10/DGX Spark) |
| `pr-flashinfer-3157` | upstream-code | [`sources/prs/flashinfer/PR-3157.md`](../sources/prs/flashinfer/PR-3157.md) | feat: DiT layer norm fusions for WAN: flashinfer.diffusion_ops |
| `pr-flashinfer-3276` | upstream-code | [`sources/prs/flashinfer/PR-3276.md`](../sources/prs/flashinfer/PR-3276.md) | fix(fmha_v2): fix FP8 V-scratch pipeline and varlen scheduler on SM90 |
| `pr-quack-118` | upstream-code | [`sources/prs/quack/PR-118.md`](../sources/prs/quack/PR-118.md) | Add remaining SM120 / RTX 50 support for GEMM epilogues and RMS paths |
| `pr-quack-120` | upstream-code | [`sources/prs/quack/PR-120.md`](../sources/prs/quack/PR-120.md) | Fix ColVecReduce shared-memory staging |
| `pr-quack-132` | upstream-code | [`sources/prs/quack/PR-132.md`](../sources/prs/quack/PR-132.md) | RMS Norm Bwd: Optimize for GB200 w/ TMA loads, reload_x, separate output dtype, new launch configs |
| `pr-quack-31` | upstream-code | [`sources/prs/quack/PR-31.md`](../sources/prs/quack/PR-31.md) | Add missing default value for `is_scheduler_warp` |
| `pr-quack-32` | upstream-code | [`sources/prs/quack/PR-32.md`](../sources/prs/quack/PR-32.md) | Fix a potential use-def issue in dynamic control flow |
| `pr-quack-35` | upstream-code | [`sources/prs/quack/PR-35.md`](../sources/prs/quack/PR-35.md) | Add optional epilogue args |
| `pr-quack-36` | upstream-code | [`sources/prs/quack/PR-36.md`](../sources/prs/quack/PR-36.md) | [GemmSm90]Add varlen_utils and make gemm interface api return shape consistent |
| `pr-quack-75` | upstream-code | [`sources/prs/quack/PR-75.md`](../sources/prs/quack/PR-75.md) | Better gemm configs that reduce 80% autotuning time |
| `pr-quack-76` | upstream-code | [`sources/prs/quack/PR-76.md`](../sources/prs/quack/PR-76.md) | Support to only store mPostAct |
| `pr-quack-80` | upstream-code | [`sources/prs/quack/PR-80.md`](../sources/prs/quack/PR-80.md) | CLC should be autotunable in SM100 rather than a fixed argument |
| `pr-quack-81` | upstream-code | [`sources/prs/quack/PR-81.md`](../sources/prs/quack/PR-81.md) | [SM100] fix CLC persistence for varlen-M tile scheduler |
| `pr-quack-82` | upstream-code | [`sources/prs/quack/PR-82.md`](../sources/prs/quack/PR-82.md) | Add stochastic rounding support for GEMM epilogue |
| `pr-quack-85` | upstream-code | [`sources/prs/quack/PR-85.md`](../sources/prs/quack/PR-85.md) | Avoid CUDA context initialization at import time |
| `pr-quack-94` | upstream-code | [`sources/prs/quack/PR-94.md`](../sources/prs/quack/PR-94.md) | [Gemm] fix sm120 gemm kernel invocation error |
| `pr-quack-95` | upstream-code | [`sources/prs/quack/PR-95.md`](../sources/prs/quack/PR-95.md) | [Gemm] Fix `gemm_symmetric` on SM120 + add benchmark |
| `pr-quack-96` | upstream-code | [`sources/prs/quack/PR-96.md`](../sources/prs/quack/PR-96.md) | Add SM120 (consumer Blackwell) support |
| `pr-quack-98` | upstream-code | [`sources/prs/quack/PR-98.md`](../sources/prs/quack/PR-98.md) | Remove asm_dialect=AD_ATT from inline PTX assembly calls |
| `pr-sglang-12787` | upstream-code | [`sources/prs/sglang/PR-12787.md`](../sources/prs/sglang/PR-12787.md) | [Nvidia] Add trtllm mnnvl allreduce with unified flashinfer allreduce fusion api |
| `pr-sglang-16723` | upstream-code | [`sources/prs/sglang/PR-16723.md`](../sources/prs/sglang/PR-16723.md) | [Rework] Add SwapAB Optimization for triton fused_moe_kernel on SM90. |
| `pr-sglang-18750` | upstream-code | [`sources/prs/sglang/PR-18750.md`](../sources/prs/sglang/PR-18750.md) | fix(sgl-kernel): use >= 120 for SM12x CUDA kernel dispatch |
| `pr-sglang-19880` | upstream-code | [`sources/prs/sglang/PR-19880.md`](../sources/prs/sglang/PR-19880.md) | [JIT Kernel][Feature] Support JIT custom all reduce (rewrite as v2) |
| `pr-sglang-20479` | upstream-code | [`sources/prs/sglang/PR-20479.md`](../sources/prs/sglang/PR-20479.md) | Support Triton MLA FP8 KV cache |
| `pr-sglang-20576` | upstream-code | [`sources/prs/sglang/PR-20576.md`](../sources/prs/sglang/PR-20576.md) | [Diffusion] Clean upstream fa3 in hopper |
| `pr-sglang-22869` | upstream-code | [`sources/prs/sglang/PR-22869.md`](../sources/prs/sglang/PR-22869.md) | [diffusion] feat: introduce ltx-2-two-stage device manager |
| `pr-sglang-22931` | upstream-code | [`sources/prs/sglang/PR-22931.md`](../sources/prs/sglang/PR-22931.md) | [Fix/Kernel] Add JIT rmsnorm_hf kernel to fix transformers backend MMLU accuracy regression  |
| `pr-sglang-23686` | upstream-code | [`sources/prs/sglang/PR-23686.md`](../sources/prs/sglang/PR-23686.md) | Deepseek_v4 support w4(mxfp4)a16 on hopper |
| `pr-sglang-24271` | upstream-code | [`sources/prs/sglang/PR-24271.md`](../sources/prs/sglang/PR-24271.md) | [KDA] Optimize prefill kernels with diagonal and recompute fuse |
| `pr-sglang-24490` | upstream-code | [`sources/prs/sglang/PR-24490.md`](../sources/prs/sglang/PR-24490.md) | Port MXFP4 Marlin MoE support to JIT kernel path |
| `pr-sglang-24562` | upstream-code | [`sources/prs/sglang/PR-24562.md`](../sources/prs/sglang/PR-24562.md) | Fix performance regression on Deepseek V3 on `moe-runner-backend=triton` on SM90 |
| `pr-sglang-24816` | upstream-code | [`sources/prs/sglang/PR-24816.md`](../sources/prs/sglang/PR-24816.md) | Add FlashInfer SM90 cutlass MXFP4 MoE backend (W4A16) for GPT-OSS + DeepSeek-V4 |
| `pr-sglang-24986` | upstream-code | [`sources/prs/sglang/PR-24986.md`](../sources/prs/sglang/PR-24986.md) | [rebase]Deepseek_v4 support w4(mxfp4)a16 on hopper |
| `pr-tensorrt-llm-10190` | upstream-code | [`sources/prs/tensorrt-llm/PR-10190.md`](../sources/prs/tensorrt-llm/PR-10190.md) | [None][feat] sm100 weight-only kernel |
| `pr-tensorrt-llm-10226` | upstream-code | [`sources/prs/tensorrt-llm/PR-10226.md`](../sources/prs/tensorrt-llm/PR-10226.md) | [TRTLLM-9798][feat] Change to use new DeepGEMM MQA sm100 kernel for MTP-3 |
| `pr-tensorrt-llm-10264` | upstream-code | [`sources/prs/tensorrt-llm/PR-10264.md`](../sources/prs/tensorrt-llm/PR-10264.md) | [TRTLLM-10022][feat] Add hopper xqa decode support for skip softmax attention |
| `pr-tensorrt-llm-11165` | upstream-code | [`sources/prs/tensorrt-llm/PR-11165.md`](../sources/prs/tensorrt-llm/PR-11165.md) | [https://nvbugs/5799917][fix] Recover from CUTLASS MoE doActivation perf regression for MXFP4/NVFP4 dtype |
| `pr-tensorrt-llm-11381` | upstream-code | [`sources/prs/tensorrt-llm/PR-11381.md`](../sources/prs/tensorrt-llm/PR-11381.md) | [None][feat] Remove non flash attetnion style fmha_v2 kernel for hopper |
| `pr-tensorrt-llm-11510` | upstream-code | [`sources/prs/tensorrt-llm/PR-11510.md`](../sources/prs/tensorrt-llm/PR-11510.md) | [None][feat] Add support for expert_number<=2048 and K<=32 |
| `pr-tensorrt-llm-12666` | upstream-code | [`sources/prs/tensorrt-llm/PR-12666.md`](../sources/prs/tensorrt-llm/PR-12666.md) | [https://nvbugs/5836828][fix] Fix GPTOSS CUTLASS MOE on Hopper nvlink one-sided workspace overflow |
| `pr-tensorrt-llm-12882` | upstream-code | [`sources/prs/tensorrt-llm/PR-12882.md`](../sources/prs/tensorrt-llm/PR-12882.md) | [TRTLLM-11878][feat] Gen-only sync transfer v2 and manager v2 |
| `pr-tensorrt-llm-13081` | upstream-code | [`sources/prs/tensorrt-llm/PR-13081.md`](../sources/prs/tensorrt-llm/PR-13081.md) | [TRTLLM-11540][feat] Revert revert of EAGLE3 dynamic tree speculative decoding support |
| `pr-tensorrt-llm-13120` | upstream-code | [`sources/prs/tensorrt-llm/PR-13120.md`](../sources/prs/tensorrt-llm/PR-13120.md) | [None][bug] fix SM90 full-mask skip-softmax dispatch |
| `pr-tensorrt-llm-13169` | upstream-code | [`sources/prs/tensorrt-llm/PR-13169.md`](../sources/prs/tensorrt-llm/PR-13169.md) | [https://nvbugs/5945047][fix] Fix cluster launch enablement for SM120 GPUs in allReduce fusion |
| `pr-tensorrt-llm-13222` | upstream-code | [`sources/prs/tensorrt-llm/PR-13222.md`](../sources/prs/tensorrt-llm/PR-13222.md) | [#11823][feat] AutoDeploy trtllm_mla attention backend |
| `pr-tensorrt-llm-13328` | upstream-code | [`sources/prs/tensorrt-llm/PR-13328.md`](../sources/prs/tensorrt-llm/PR-13328.md) | [None][feat] Resubmission of the routing refactor in trtllmgen |
| `pr-tensorrt-llm-13938` | upstream-code | [`sources/prs/tensorrt-llm/PR-13938.md`](../sources/prs/tensorrt-llm/PR-13938.md) | [None][feat] Keep DSv4 o_a_proj as FP8, and port vLLM's fused_inv_rope_fp8_quant |
| `pr-tensorrt-llm-14039` | upstream-code | [`sources/prs/tensorrt-llm/PR-14039.md`](../sources/prs/tensorrt-llm/PR-14039.md) | [#8542][feat] AutoDeploy: add Llama-3.1-8B FP8 perf-sanity test on H100 |
| `pr-tensorrt-llm-6538` | upstream-code | [`sources/prs/tensorrt-llm/PR-6538.md`](../sources/prs/tensorrt-llm/PR-6538.md) | [None][feat] Use Separate QKV Input Layout for Context MLA |
| `pr-tensorrt-llm-7937` | upstream-code | [`sources/prs/tensorrt-llm/PR-7937.md`](../sources/prs/tensorrt-llm/PR-7937.md) | [None][feat] GPT-OSS Sm120/Sm121 Support |
| `pr-tensorrt-llm-9811` | upstream-code | [`sources/prs/tensorrt-llm/PR-9811.md`](../sources/prs/tensorrt-llm/PR-9811.md) | [None][feat] spark cublas LUT table for llama-8b-bf16 perf |
| `pr-tensorrt-llm-9838` | upstream-code | [`sources/prs/tensorrt-llm/PR-9838.md`](../sources/prs/tensorrt-llm/PR-9838.md) | [https://nvbugs/5726962][feat] Apply fusion for W4AFP8_AWQ MoE |
| `pr-tensorrt-llm-9854` | upstream-code | [`sources/prs/tensorrt-llm/PR-9854.md`](../sources/prs/tensorrt-llm/PR-9854.md) | [None][feat] Port fp4 quantization kernel optimization from FlashInfer |
| `pr-tensorrt-llm-9905` | upstream-code | [`sources/prs/tensorrt-llm/PR-9905.md`](../sources/prs/tensorrt-llm/PR-9905.md) | [None][feat] Adding torch ext API for FusedAddRMSNormQuant kernel |
| `pr-tensorrt-llm-9924` | upstream-code | [`sources/prs/tensorrt-llm/PR-9924.md`](../sources/prs/tensorrt-llm/PR-9924.md) | [TRTLLM-9493][feat] Add helixPostProcessNative kernel for cp_dim=2 |
| `pr-thunderkittens-101` | upstream-code | [`sources/prs/thunderkittens/PR-101.md`](../sources/prs/thunderkittens/PR-101.md) | feat(mma): add fp16@fp16->fp32 mma and unit tests |
| `pr-thunderkittens-152` | upstream-code | [`sources/prs/thunderkittens/PR-152.md`](../sources/prs/thunderkittens/PR-152.md) | Educational Hopper Matmul level_07 Warp Specialization Fix |
| `pr-tilelang-1090` | upstream-code | [`sources/prs/tilelang/PR-1090.md`](../sources/prs/tilelang/PR-1090.md) | [BugFix] Correct direct copy from bf16 to fp8 |
| `pr-tilelang-1367` | upstream-code | [`sources/prs/tilelang/PR-1367.md`](../sources/prs/tilelang/PR-1367.md) | [Feat] Integrate Z3 in TVM Arith Analyzer |
| `pr-tilelang-1416` | upstream-code | [`sources/prs/tilelang/PR-1416.md`](../sources/prs/tilelang/PR-1416.md) | [CUDA] Add read-only parameter annotation for CUDA codegen |
| `pr-tilelang-1515` | upstream-code | [`sources/prs/tilelang/PR-1515.md`](../sources/prs/tilelang/PR-1515.md) | [BugFix] Phaseout unused tests for gqa decode kernels and add the kernels to CI |
| `pr-tilelang-1667` | upstream-code | [`sources/prs/tilelang/PR-1667.md`](../sources/prs/tilelang/PR-1667.md) | [Feature] Support `cp.reduce.async.bulk.tensor` |
| `pr-tilelang-1677` | upstream-code | [`sources/prs/tilelang/PR-1677.md`](../sources/prs/tilelang/PR-1677.md) | [Refactor] Move AtomicAdd Vectorization to VectorizeLoop Pass |
| `pr-tilelang-1840` | upstream-code | [`sources/prs/tilelang/PR-1840.md`](../sources/prs/tilelang/PR-1840.md) | [BugFix] Fix Hopper TMA lowering without warp specialization |
| `pr-tilelang-1855` | upstream-code | [`sources/prs/tilelang/PR-1855.md`](../sources/prs/tilelang/PR-1855.md) | [Enhancement] GEMM V2 on SM90/SM100 CuTeDSL backend |
| `pr-tilelang-1863` | upstream-code | [`sources/prs/tilelang/PR-1863.md`](../sources/prs/tilelang/PR-1863.md) | [Refactor] Refactor Pass InjectFenceProxy |
| `pr-tilelang-1874` | upstream-code | [`sources/prs/tilelang/PR-1874.md`](../sources/prs/tilelang/PR-1874.md) | [Feature] Support cluster launch, query, synchronization and barrier operations |
| `pr-tilelang-1909` | upstream-code | [`sources/prs/tilelang/PR-1909.md`](../sources/prs/tilelang/PR-1909.md) | [Feature] Add Producer-Consumer Warp Specialization and T.tma_copy() API |
| `pr-tilelang-1926` | upstream-code | [`sources/prs/tilelang/PR-1926.md`](../sources/prs/tilelang/PR-1926.md) | [Bugfix] Fix concurrent TempDirectory creation during CUDA compilation |
| `pr-tilelang-1940` | upstream-code | [`sources/prs/tilelang/PR-1940.md`](../sources/prs/tilelang/PR-1940.md) | [Feature] Support alloc global workspace |
| `pr-tilelang-1953` | upstream-code | [`sources/prs/tilelang/PR-1953.md`](../sources/prs/tilelang/PR-1953.md) | [PIpeline] Enable software pipelining when warp specialization is unavailable |
| `pr-tilelang-1969` | upstream-code | [`sources/prs/tilelang/PR-1969.md`](../sources/prs/tilelang/PR-1969.md) | [BugFix] Fix bugs in `gemm_streamk` example on SM90 |
| `pr-tilelang-1976` | upstream-code | [`sources/prs/tilelang/PR-1976.md`](../sources/prs/tilelang/PR-1976.md) | [Feature] Batched AllReduce for better T.reduce performance |
| `pr-tilelang-1989` | upstream-code | [`sources/prs/tilelang/PR-1989.md`](../sources/prs/tilelang/PR-1989.md) | Add regression test for 1D TMA load compilation and execution |
| `pr-tilelang-2001` | upstream-code | [`sources/prs/tilelang/PR-2001.md`](../sources/prs/tilelang/PR-2001.md) | [Refactor] Refactor CUDA atomic helpers |
| `pr-tilelang-2004` | upstream-code | [`sources/prs/tilelang/PR-2004.md`](../sources/prs/tilelang/PR-2004.md) | fix: fix copy+cast vectorize loop to use wider vector load/store instrcution |
| `pr-tilelang-2008` | upstream-code | [`sources/prs/tilelang/PR-2008.md`](../sources/prs/tilelang/PR-2008.md) | [BugFix] Skip MMA shared buffer layout inference when layout already exists |
| `pr-tilelang-2013` | upstream-code | [`sources/prs/tilelang/PR-2013.md`](../sources/prs/tilelang/PR-2013.md) | [CI] Remove legacy dequantize gemm test |
| `pr-tilelang-2023` | upstream-code | [`sources/prs/tilelang/PR-2023.md`](../sources/prs/tilelang/PR-2023.md) | [Codegen] Add lexical_alloc_scope for scoped local variable lifetime |
| `pr-tilelang-2024` | upstream-code | [`sources/prs/tilelang/PR-2024.md`](../sources/prs/tilelang/PR-2024.md) | Re-enable deprecated `TL_DISABLE_TMA_LOWER` pass config for TMA store |
| `pr-tilelang-2026` | upstream-code | [`sources/prs/tilelang/PR-2026.md`](../sources/prs/tilelang/PR-2026.md) | [Refactor] Refactor `DecoupleTypeCast` Pass |
| `pr-tilelang-2046` | upstream-code | [`sources/prs/tilelang/PR-2046.md`](../sources/prs/tilelang/PR-2046.md) | [Refactor] Remove obsolete RewriteWgmmaSync pass |
| `pr-tilelang-2047` | upstream-code | [`sources/prs/tilelang/PR-2047.md`](../sources/prs/tilelang/PR-2047.md) | [Refactor] Move target gating into InjectFenceProxy pass entry |
| `pr-tilelang-2052` | upstream-code | [`sources/prs/tilelang/PR-2052.md`](../sources/prs/tilelang/PR-2052.md) | [Bugfix] Use shared::cta instead of shared::cluster for non-cluster T… |
| `pr-tilelang-2055` | upstream-code | [`sources/prs/tilelang/PR-2055.md`](../sources/prs/tilelang/PR-2055.md) | [BugFix] Keep shared-prelude local vars in producer-consumer WS |
| `pr-tilelang-2087` | upstream-code | [`sources/prs/tilelang/PR-2087.md`](../sources/prs/tilelang/PR-2087.md) | [Bugfix] Enable `.shared::cta` in TMA copy paths only on CUDA 12.8+ |
| `pr-tilelang-2092` | upstream-code | [`sources/prs/tilelang/PR-2092.md`](../sources/prs/tilelang/PR-2092.md) | [BugFix] Relax loop wait and adjust trailing drain behavior in async pipeline tests |
| `pr-tilelang-2103` | upstream-code | [`sources/prs/tilelang/PR-2103.md`](../sources/prs/tilelang/PR-2103.md) | [Enhancement] Optimize hopper fp8 deepgemm tile size |
| `pr-tilelang-2107` | upstream-code | [`sources/prs/tilelang/PR-2107.md`](../sources/prs/tilelang/PR-2107.md) | [TMA] Support FP4 TensorMap TMA copies |
| `pr-tilelang-2134` | upstream-code | [`sources/prs/tilelang/PR-2134.md`](../sources/prs/tilelang/PR-2134.md) | fix: TMA alignment to 1024 bytes on Blackwell |
| `pr-tilelang-2148` | upstream-code | [`sources/prs/tilelang/PR-2148.md`](../sources/prs/tilelang/PR-2148.md) | [Examples] Add examples for operators in DeepSeek-V4 |
| `pr-tilelang-2151` | upstream-code | [`sources/prs/tilelang/PR-2151.md`](../sources/prs/tilelang/PR-2151.md) | [TMA] Fix TMA descriptor init placement |
| `pr-tilelang-2152` | upstream-code | [`sources/prs/tilelang/PR-2152.md`](../sources/prs/tilelang/PR-2152.md) | [docs] fix TMEM description |
| `pr-tilelang-2161` | upstream-code | [`sources/prs/tilelang/PR-2161.md`](../sources/prs/tilelang/PR-2161.md) | [Refactor] Refactor multiple TensorCoreIntrinEmitter to provide atom-level mma control interface |
| `pr-tilelang-2165` | upstream-code | [`sources/prs/tilelang/PR-2165.md`](../sources/prs/tilelang/PR-2165.md) | [Refactor] Move backend-specific GEMM implementations and transforms into backend directories |
| `pr-tilelang-2166` | upstream-code | [`sources/prs/tilelang/PR-2166.md`](../sources/prs/tilelang/PR-2166.md) | [BugFix] Consider non-local store in external call and SIMT producer for warp specialize |
| `pr-triton-10089` | upstream-code | [`sources/prs/triton/PR-10089.md`](../sources/prs/triton/PR-10089.md) | [Gluon][Translator] Hopper support |
| `pr-triton-10112` | upstream-code | [`sources/prs/triton/PR-10112.md`](../sources/prs/triton/PR-10112.md) | [FPSAN] Add support for wgmma in fpsan |
| `pr-triton-10148` | upstream-code | [`sources/prs/triton/PR-10148.md`](../sources/prs/triton/PR-10148.md) | [Reland][NVIDIA] Support swizzle 0 TMA + MMA for Hopper and Blackwell |
| `pr-triton-10190` | upstream-code | [`sources/prs/triton/PR-10190.md`](../sources/prs/triton/PR-10190.md) | [mxfp4] Fix Hopper scale padding mask |
| `pr-triton-10214` | upstream-code | [`sources/prs/triton/PR-10214.md`](../sources/prs/triton/PR-10214.md) | Allow MXFP8 LHS with Hopper-swizzled MXFP4 RHS |
| `pr-triton-10234` | upstream-code | [`sources/prs/triton/PR-10234.md`](../sources/prs/triton/PR-10234.md) | [ BACKEND ]  Enable `tl.dot` with TF32 precision on tiles with N=8 and K=8 |
| `pr-triton-10242` | upstream-code | [`sources/prs/triton/PR-10242.md`](../sources/prs/triton/PR-10242.md) | Fix convert_layout lowering for CGA + slice layouts. |
| `pr-triton-10275` | upstream-code | [`sources/prs/triton/PR-10275.md`](../sources/prs/triton/PR-10275.md) | Support zero-sized Hopper MX scale layouts |
| `pr-vllm-27134` | upstream-code | [`sources/prs/vllm/PR-27134.md`](../sources/prs/vllm/PR-27134.md) | [Kernels] Enable FlashInfer FP8 Blockscale on SM90 (for TEP DSR1) |
| `pr-vllm-32195` | upstream-code | [`sources/prs/vllm/PR-32195.md`](../sources/prs/vllm/PR-32195.md) | Add TMA support to fused_moe_lora kernel |
| `pr-vllm-32619` | upstream-code | [`sources/prs/vllm/PR-32619.md`](../sources/prs/vllm/PR-32619.md) | [Perf] Create TMA-aligned input scale tensor for DeepGemm on Hopper |
| `pr-vllm-33255` | upstream-code | [`sources/prs/vllm/PR-33255.md`](../sources/prs/vllm/PR-33255.md) | [Bugfix] Fix quant RMS norm fusion for quantization with TMA-aligned scales |
| `pr-vllm-33568` | upstream-code | [`sources/prs/vllm/PR-33568.md`](../sources/prs/vllm/PR-33568.md) | [Perf] Disable clean_logits in deepgemm fp8_mqa_logits kernel |
| `pr-vllm-34043` | upstream-code | [`sources/prs/vllm/PR-34043.md`](../sources/prs/vllm/PR-34043.md) | Reapply [Attention][FA3] Update FA3 to include new swizzle optimization |
| `pr-vllm-34260` | upstream-code | [`sources/prs/vllm/PR-34260.md`](../sources/prs/vllm/PR-34260.md) | [Model Bash]: Improve FP8 Oracle for Config Specific Kernel Selection |
| `pr-vllm-34556` | upstream-code | [`sources/prs/vllm/PR-34556.md`](../sources/prs/vllm/PR-34556.md) | [Quantization] add humming quantization kernel |
| `pr-vllm-34758` | upstream-code | [`sources/prs/vllm/PR-34758.md`](../sources/prs/vllm/PR-34758.md) | [Model Bash] DeepSeek R1 BF16 Min Latency QKV A GEMM (0.5% E2E Speedup) |
| `pr-vllm-35271` | upstream-code | [`sources/prs/vllm/PR-35271.md`](../sources/prs/vllm/PR-35271.md) | [Feat] Add CUDA torch fallbacks for fp8_mqa_logits/fp8_paged_mqa_logits_torch function |
| `pr-vllm-35382` | upstream-code | [`sources/prs/vllm/PR-35382.md`](../sources/prs/vllm/PR-35382.md) | fix(mxfp4): return is_monolithic=False when LoRA is enabled for Triton backend |
| `pr-vllm-38065` | upstream-code | [`sources/prs/vllm/PR-38065.md`](../sources/prs/vllm/PR-38065.md) | [Perf] FP8 FlashInfer Attn for ViT |
| `pr-vllm-38504` | upstream-code | [`sources/prs/vllm/PR-38504.md`](../sources/prs/vllm/PR-38504.md) | [Kernels][MoE] Fix legacy_routing to use bitmatrix-based routing path |
| `pr-vllm-39306` | upstream-code | [`sources/prs/vllm/PR-39306.md`](../sources/prs/vllm/PR-39306.md) | Use CU_MEMCPY_SRC_ACCESS_ORDER_ANY for batch KV cache swaps |
| `pr-vllm-40045` | upstream-code | [`sources/prs/vllm/PR-40045.md`](../sources/prs/vllm/PR-40045.md) | [Attention] use diff kv backend for mimo v2 flash |
| `pr-vllm-40408` | upstream-code | [`sources/prs/vllm/PR-40408.md`](../sources/prs/vllm/PR-40408.md) | [Perf] Batch invariance with Cutlass fp8 support, 28.9% E2E latency improvement |
| `pr-vllm-41263` | upstream-code | [`sources/prs/vllm/PR-41263.md`](../sources/prs/vllm/PR-41263.md) | [DSV4]   Fuse norm and router for low latency scenario |
| `pr-vllm-41566` | upstream-code | [`sources/prs/vllm/PR-41566.md`](../sources/prs/vllm/PR-41566.md) | [Quantization] Rework quantization_config to use QuantKey and allow for activation override |
| `pr-vllm-41868` | upstream-code | [`sources/prs/vllm/PR-41868.md`](../sources/prs/vllm/PR-41868.md) | [CUDA][CUTLASS] Enable cutlass scaled mm for non-compatible sizes  |
| `pr-vllm-42236` | upstream-code | [`sources/prs/vllm/PR-42236.md`](../sources/prs/vllm/PR-42236.md) | [DSv4] Improved dequant gather K cache kernel |
| `pr-vllm-7174` | upstream-code | [`sources/prs/vllm/PR-7174.md`](../sources/prs/vllm/PR-7174.md) | [Kernel] (1/N) Machete - Hopper Optimized Mixed Precision Linear Kernel  |

<a id="mbarrier"></a>
## mbarrier

1 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-flashinfer-2387` | upstream-code | [`sources/prs/flashinfer/PR-2387.md`](../sources/prs/flashinfer/PR-2387.md) | A Blackwell-optimized version of selective_state_update (mamba) |

<a id="mxfp4"></a>
## mxfp4

67 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-flash-attention-2385` | upstream-code | [`sources/prs/flash-attention/PR-2385.md`](../sources/prs/flash-attention/PR-2385.md) | [ROCM] Fix windows issues |
| `pr-flashinfer-2914` | upstream-code | [`sources/prs/flashinfer/PR-2914.md`](../sources/prs/flashinfer/PR-2914.md) | feat: Add cuBLASLt backend for `mm_bf16` and enable multi-tactic autotuning for FP8/MXFP8 runners |
| `pr-flashinfer-2959` | upstream-code | [`sources/prs/flashinfer/PR-2959.md`](../sources/prs/flashinfer/PR-2959.md) | [Fmha] Add head_dim=512 support for trtllm attention kernels |
| `pr-flashinfer-2962` | upstream-code | [`sources/prs/flashinfer/PR-2962.md`](../sources/prs/flashinfer/PR-2962.md) | Improved `simple` mamba SSU kernel  |
| `pr-flashinfer-3039` | upstream-code | [`sources/prs/flashinfer/PR-3039.md`](../sources/prs/flashinfer/PR-3039.md) | feat: Integrate CuTe DSL FMHA prefill kernels by loading cubin |
| `pr-flashinfer-3084` | upstream-code | [`sources/prs/flashinfer/PR-3084.md`](../sources/prs/flashinfer/PR-3084.md) | perf: optimize MXFP4xBF16 & INT4xFP8 CUTLASS MoE backend for SM90 |
| `pr-flashinfer-3152` | upstream-code | [`sources/prs/flashinfer/PR-3152.md`](../sources/prs/flashinfer/PR-3152.md) | Integrate CUTLASS Small Tile N Blockscaled GEMMs/Grouped GEMMs for SM120 and SM121 |
| `pr-flashinfer-3157` | upstream-code | [`sources/prs/flashinfer/PR-3157.md`](../sources/prs/flashinfer/PR-3157.md) | feat: DiT layer norm fusions for WAN: flashinfer.diffusion_ops |
| `pr-flashinfer-3239` | upstream-code | [`sources/prs/flashinfer/PR-3239.md`](../sources/prs/flashinfer/PR-3239.md) | Update moe gemm |
| `pr-sglang-23686` | upstream-code | [`sources/prs/sglang/PR-23686.md`](../sources/prs/sglang/PR-23686.md) | Deepseek_v4 support w4(mxfp4)a16 on hopper |
| `pr-sglang-24490` | upstream-code | [`sources/prs/sglang/PR-24490.md`](../sources/prs/sglang/PR-24490.md) | Port MXFP4 Marlin MoE support to JIT kernel path |
| `pr-sglang-24816` | upstream-code | [`sources/prs/sglang/PR-24816.md`](../sources/prs/sglang/PR-24816.md) | Add FlashInfer SM90 cutlass MXFP4 MoE backend (W4A16) for GPT-OSS + DeepSeek-V4 |
| `pr-sglang-24986` | upstream-code | [`sources/prs/sglang/PR-24986.md`](../sources/prs/sglang/PR-24986.md) | [rebase]Deepseek_v4 support w4(mxfp4)a16 on hopper |
| `pr-tensorrt-llm-11143` | upstream-code | [`sources/prs/tensorrt-llm/PR-11143.md`](../sources/prs/tensorrt-llm/PR-11143.md) | [None][feat] fuse shared to sparse experts in TRT-LLM Gen MoE |
| `pr-tensorrt-llm-11165` | upstream-code | [`sources/prs/tensorrt-llm/PR-11165.md`](../sources/prs/tensorrt-llm/PR-11165.md) | [https://nvbugs/5799917][fix] Recover from CUTLASS MoE doActivation perf regression for MXFP4/NVFP4 dtype |
| `pr-tensorrt-llm-11733` | upstream-code | [`sources/prs/tensorrt-llm/PR-11733.md`](../sources/prs/tensorrt-llm/PR-11733.md) | [https://nvbugs/5799917][fix] Recover from CUTLASS MoE doActivation perf regression for MXFP4/NVFP4 dtype |
| `pr-tensorrt-llm-12666` | upstream-code | [`sources/prs/tensorrt-llm/PR-12666.md`](../sources/prs/tensorrt-llm/PR-12666.md) | [https://nvbugs/5836828][fix] Fix GPTOSS CUTLASS MOE on Hopper nvlink one-sided workspace overflow |
| `pr-tensorrt-llm-13384` | upstream-code | [`sources/prs/tensorrt-llm/PR-13384.md`](../sources/prs/tensorrt-llm/PR-13384.md) | [None][feat] Add MegaMoEDeepGemmFusedMoE backend wrapping DeepGEMM fp8_fp4_mega_moe |
| `pr-tensorrt-llm-13667` | upstream-code | [`sources/prs/tensorrt-llm/PR-13667.md`](../sources/prs/tensorrt-llm/PR-13667.md) | [None][perf] Improve TRTLLM MoE autotune in DEP |
| `pr-tensorrt-llm-13708` | upstream-code | [`sources/prs/tensorrt-llm/PR-13708.md`](../sources/prs/tensorrt-llm/PR-13708.md) | [https://nvbugs/6094072][fix] swizzle GPT-OSS dummy MXFP4 weights |
| `pr-tensorrt-llm-13908` | upstream-code | [`sources/prs/tensorrt-llm/PR-13908.md`](../sources/prs/tensorrt-llm/PR-13908.md) | [None][refactor] MoEScheduler split + MegaMoE EPLB / multi-chunk / CI integration |
| `pr-tensorrt-llm-14004` | upstream-code | [`sources/prs/tensorrt-llm/PR-14004.md`](../sources/prs/tensorrt-llm/PR-14004.md) | [None][feat] AutoDeploy re-onboard GPT_OSS |
| `pr-tensorrt-llm-14054` | upstream-code | [`sources/prs/tensorrt-llm/PR-14054.md`](../sources/prs/tensorrt-llm/PR-14054.md) | [https://nvbugs/6162323][fix] Make mxfp4 H20 swizzle WAR more robust |
| `pr-tensorrt-llm-14106` | upstream-code | [`sources/prs/tensorrt-llm/PR-14106.md`](../sources/prs/tensorrt-llm/PR-14106.md) | [None][fix] Add SPDX Apache-2.0 headers and fix license compliance for llm-c standalone repo |
| `pr-tensorrt-llm-4867` | upstream-code | [`sources/prs/tensorrt-llm/PR-4867.md`](../sources/prs/tensorrt-llm/PR-4867.md) | feat: Add w4a8_mxfp4_fp8 quantization recipe. |
| `pr-tensorrt-llm-7761` | upstream-code | [`sources/prs/tensorrt-llm/PR-7761.md`](../sources/prs/tensorrt-llm/PR-7761.md) | [TRTLLM-8637][feat] Optimize the routing kernel for DeepseekV3 (MoE CUTLASS backend); Add support for 384 experts (MoE TRTLLM backend) |
| `pr-tensorrt-llm-9025` | upstream-code | [`sources/prs/tensorrt-llm/PR-9025.md`](../sources/prs/tensorrt-llm/PR-9025.md) | [None][feat] Update TRTLLM MoE cubins; reduce mxfp4 weight padding requirement; tighten TMA bound |
| `pr-tilelang-1845` | upstream-code | [`sources/prs/tilelang/PR-1845.md`](../sources/prs/tilelang/PR-1845.md) | [Enhancement] Optimize templates for half/bfloat16 |
| `pr-tilelang-1887` | upstream-code | [`sources/prs/tilelang/PR-1887.md`](../sources/prs/tilelang/PR-1887.md) | [Refactor] Improve cp.async lowering and add async_copy op |
| `pr-tilelang-1909` | upstream-code | [`sources/prs/tilelang/PR-1909.md`](../sources/prs/tilelang/PR-1909.md) | [Feature] Add Producer-Consumer Warp Specialization and T.tma_copy() API |
| `pr-tilelang-1932` | upstream-code | [`sources/prs/tilelang/PR-1932.md`](../sources/prs/tilelang/PR-1932.md) | test: reduce CI runtime for slow Python suites |
| `pr-tilelang-1937` | upstream-code | [`sources/prs/tilelang/PR-1937.md`](../sources/prs/tilelang/PR-1937.md) | Fix predicated cp.async pipeline scheduling |
| `pr-tilelang-1947` | upstream-code | [`sources/prs/tilelang/PR-1947.md`](../sources/prs/tilelang/PR-1947.md) | Support packed subtype views during layout reshape |
| `pr-tilelang-1950` | upstream-code | [`sources/prs/tilelang/PR-1950.md`](../sources/prs/tilelang/PR-1950.md) | [Enhancement] Use stronger prover in `ProveFragmentContains` to avoid false layout conflicts |
| `pr-tilelang-1953` | upstream-code | [`sources/prs/tilelang/PR-1953.md`](../sources/prs/tilelang/PR-1953.md) | [PIpeline] Enable software pipelining when warp specialization is unavailable |
| `pr-tilelang-1975` | upstream-code | [`sources/prs/tilelang/PR-1975.md`](../sources/prs/tilelang/PR-1975.md) | Fix wrapped pre-loop TMA prefixes in producer-consumer WS |
| `pr-tilelang-2001` | upstream-code | [`sources/prs/tilelang/PR-2001.md`](../sources/prs/tilelang/PR-2001.md) | [Refactor] Refactor CUDA atomic helpers |
| `pr-tilelang-2002` | upstream-code | [`sources/prs/tilelang/PR-2002.md`](../sources/prs/tilelang/PR-2002.md) | [Refactor][Pipeline] Run pipeline rewriting before layout inference and stabilize tiled WS |
| `pr-tilelang-2004` | upstream-code | [`sources/prs/tilelang/PR-2004.md`](../sources/prs/tilelang/PR-2004.md) | fix: fix copy+cast vectorize loop to use wider vector load/store instrcution |
| `pr-tilelang-2013` | upstream-code | [`sources/prs/tilelang/PR-2013.md`](../sources/prs/tilelang/PR-2013.md) | [CI] Remove legacy dequantize gemm test |
| `pr-tilelang-2023` | upstream-code | [`sources/prs/tilelang/PR-2023.md`](../sources/prs/tilelang/PR-2023.md) | [Codegen] Add lexical_alloc_scope for scoped local variable lifetime |
| `pr-tilelang-2024` | upstream-code | [`sources/prs/tilelang/PR-2024.md`](../sources/prs/tilelang/PR-2024.md) | Re-enable deprecated `TL_DISABLE_TMA_LOWER` pass config for TMA store |
| `pr-tilelang-2026` | upstream-code | [`sources/prs/tilelang/PR-2026.md`](../sources/prs/tilelang/PR-2026.md) | [Refactor] Refactor `DecoupleTypeCast` Pass |
| `pr-tilelang-2046` | upstream-code | [`sources/prs/tilelang/PR-2046.md`](../sources/prs/tilelang/PR-2046.md) | [Refactor] Remove obsolete RewriteWgmmaSync pass |
| `pr-tilelang-2047` | upstream-code | [`sources/prs/tilelang/PR-2047.md`](../sources/prs/tilelang/PR-2047.md) | [Refactor] Move target gating into InjectFenceProxy pass entry |
| `pr-tilelang-2052` | upstream-code | [`sources/prs/tilelang/PR-2052.md`](../sources/prs/tilelang/PR-2052.md) | [Bugfix] Use shared::cta instead of shared::cluster for non-cluster T… |
| `pr-tilelang-2055` | upstream-code | [`sources/prs/tilelang/PR-2055.md`](../sources/prs/tilelang/PR-2055.md) | [BugFix] Keep shared-prelude local vars in producer-consumer WS |
| `pr-tilelang-2092` | upstream-code | [`sources/prs/tilelang/PR-2092.md`](../sources/prs/tilelang/PR-2092.md) | [BugFix] Relax loop wait and adjust trailing drain behavior in async pipeline tests |
| `pr-tilelang-2107` | upstream-code | [`sources/prs/tilelang/PR-2107.md`](../sources/prs/tilelang/PR-2107.md) | [TMA] Support FP4 TensorMap TMA copies |
| `pr-tilelang-2166` | upstream-code | [`sources/prs/tilelang/PR-2166.md`](../sources/prs/tilelang/PR-2166.md) | [BugFix] Consider non-local store in external call and SIMT producer for warp specialize |
| `pr-triton-10151` | upstream-code | [`sources/prs/triton/PR-10151.md`](../sources/prs/triton/PR-10151.md) | [Tutorials] Fix unbound local variable in Tutorial 10 |
| `pr-triton-10190` | upstream-code | [`sources/prs/triton/PR-10190.md`](../sources/prs/triton/PR-10190.md) | [mxfp4] Fix Hopper scale padding mask |
| `pr-triton-10196` | upstream-code | [`sources/prs/triton/PR-10196.md`](../sources/prs/triton/PR-10196.md) | [MULTICTA] Fix multicast pattern for tcgen05_mma_scaled |
| `pr-triton-10214` | upstream-code | [`sources/prs/triton/PR-10214.md`](../sources/prs/triton/PR-10214.md) | Allow MXFP8 LHS with Hopper-swizzled MXFP4 RHS |
| `pr-triton-10275` | upstream-code | [`sources/prs/triton/PR-10275.md`](../sources/prs/triton/PR-10275.md) | Support zero-sized Hopper MX scale layouts |
| `pr-vllm-34556` | upstream-code | [`sources/prs/vllm/PR-34556.md`](../sources/prs/vllm/PR-34556.md) | [Quantization] add humming quantization kernel |
| `pr-vllm-35382` | upstream-code | [`sources/prs/vllm/PR-35382.md`](../sources/prs/vllm/PR-35382.md) | fix(mxfp4): return is_monolithic=False when LoRA is enabled for Triton backend |
| `pr-vllm-37463` | upstream-code | [`sources/prs/vllm/PR-37463.md`](../sources/prs/vllm/PR-37463.md) | [Kernel] Add MXFP4 W4A4 CUTLASS MoE kernel for SM100 |
| `pr-vllm-38504` | upstream-code | [`sources/prs/vllm/PR-38504.md`](../sources/prs/vllm/PR-38504.md) | [Kernels][MoE] Fix legacy_routing to use bitmatrix-based routing path |
| `pr-vllm-40191` | upstream-code | [`sources/prs/vllm/PR-40191.md`](../sources/prs/vllm/PR-40191.md) | [Bugfix] Guard mxfp4_experts_quant bindings on ENABLE_NVFP4_SM100 |
| `pr-vllm-40392` | upstream-code | [`sources/prs/vllm/PR-40392.md`](../sources/prs/vllm/PR-40392.md) | [Performance][DSR1]: Fused RoPE+KVCache+q_concat for MLA |
| `pr-vllm-40574` | upstream-code | [`sources/prs/vllm/PR-40574.md`](../sources/prs/vllm/PR-40574.md) | [MoE] Move cutlass moe to fused_moe/experts/ |
| `pr-vllm-40960` | upstream-code | [`sources/prs/vllm/PR-40960.md`](../sources/prs/vllm/PR-40960.md) | [DSV4] Add BF16 and MXFP8 A2A support for flashinfer a2a one sided |
| `pr-vllm-41428` | upstream-code | [`sources/prs/vllm/PR-41428.md`](../sources/prs/vllm/PR-41428.md) | [DSv4] Improved fused Indexer Q quant kernel |
| `pr-vllm-41566` | upstream-code | [`sources/prs/vllm/PR-41566.md`](../sources/prs/vllm/PR-41566.md) | [Quantization] Rework quantization_config to use QuantKey and allow for activation override |
| `pr-vllm-41664` | upstream-code | [`sources/prs/vllm/PR-41664.md`](../sources/prs/vllm/PR-41664.md) | [MXFP4] Support for linear layers + compressed-tensors integration |
| `pr-vllm-41986` | upstream-code | [`sources/prs/vllm/PR-41986.md`](../sources/prs/vllm/PR-41986.md) | [Bugfix] Add swiglu limits to deepgemm fp8 methods |

<a id="nvfp4"></a>
## nvfp4

233 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `blog-amandeep-nvfp4` | community-note | [`sources/blogs/amandeep-nvfp4-attempts.md`](../sources/blogs/amandeep-nvfp4-attempts.md) | Twelve Attempts at NVFP4 Batched GEMV |
| `blog-yue-nvfp4` | community-note | [`sources/blogs/yue-nvfp4-hackathon.md`](../sources/blogs/yue-nvfp4-hackathon.md) | Blackwell NVFP4 Kernel Hackathon Journey |
| `contest-gpumode-p1` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-1-gemv.md`](../sources/contests/gpu-mode-nvfp4/problem-1-gemv.md) | GPU Mode NVFP4 Hackathon - Problem 1: Batched GEMV |
| `contest-gpumode-p2` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-2-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-2-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 2: NVFP4 GEMM |
| `contest-gpumode-p3` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-3-gated-dual-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-3-gated-dual-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 3: Gated Dual GEMM |
| `contest-gpumode-p4` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 4: Grouped GEMM |
| `pr-cccl-cub-4340` | upstream-code | [`sources/prs/cccl-cub/PR-4340.md`](../sources/prs/cccl-cub/PR-4340.md) | Disable extended floating-point types for nvc++ |
| `pr-cutlass-2139` | upstream-code | [`sources/prs/cutlass/PR-2139.md`](../sources/prs/cutlass/PR-2139.md) | Blockwise and Groupwise GEMM for Blackwell and Improvements for Hopper |
| `pr-deepgemm-304` | upstream-code | [`sources/prs/deepgemm/PR-304.md`](../sources/prs/deepgemm/PR-304.md) | [Public release 26/04] Introducing Mega MoE, FP4 Indexer and other features/fixes |
| `pr-flashinfer-1214` | upstream-code | [`sources/prs/flashinfer/PR-1214.md`](../sources/prs/flashinfer/PR-1214.md) | Feature/sm100 low latency nvfp4 kernels |
| `pr-flashinfer-1318` | upstream-code | [`sources/prs/flashinfer/PR-1318.md`](../sources/prs/flashinfer/PR-1318.md) | feat: support output nvfp4 in trtllm-gen function call. |
| `pr-flashinfer-1361` | upstream-code | [`sources/prs/flashinfer/PR-1361.md`](../sources/prs/flashinfer/PR-1361.md) | Update autotune results for the nvfp4 cutlass moe backends for v0.2.9 |
| `pr-flashinfer-1412` | upstream-code | [`sources/prs/flashinfer/PR-1412.md`](../sources/prs/flashinfer/PR-1412.md) | Faster weight processing (moe nvfp4) |
| `pr-flashinfer-1460` | upstream-code | [`sources/prs/flashinfer/PR-1460.md`](../sources/prs/flashinfer/PR-1460.md) | Fix TRTLLM NVFP4-out attention kernel scale factor dim issue |
| `pr-flashinfer-1525` | upstream-code | [`sources/prs/flashinfer/PR-1525.md`](../sources/prs/flashinfer/PR-1525.md) | Add GeGLU support to trtllm-gen NVFP4 Fused MoE Kernel |
| `pr-flashinfer-1548` | upstream-code | [`sources/prs/flashinfer/PR-1548.md`](../sources/prs/flashinfer/PR-1548.md) | perf: Enable SplitK and fix autotuner for trtllm fp4 fused moe |
| `pr-flashinfer-1774` | upstream-code | [`sources/prs/flashinfer/PR-1774.md`](../sources/prs/flashinfer/PR-1774.md) | Masked batch nvfp4 quantization |
| `pr-flashinfer-1927` | upstream-code | [`sources/prs/flashinfer/PR-1927.md`](../sources/prs/flashinfer/PR-1927.md) | silu_and_mul nvfp4 quanization fusion rework |
| `pr-flashinfer-2011` | upstream-code | [`sources/prs/flashinfer/PR-2011.md`](../sources/prs/flashinfer/PR-2011.md) | Feature: Support non-gated activation in cutlass fused MoE nvfp4 |
| `pr-flashinfer-2268` | upstream-code | [`sources/prs/flashinfer/PR-2268.md`](../sources/prs/flashinfer/PR-2268.md) | [performance]optimize for nvfp4 |
| `pr-flashinfer-2303` | upstream-code | [`sources/prs/flashinfer/PR-2303.md`](../sources/prs/flashinfer/PR-2303.md) | [Perf][Feature] Add SM103-specific schedulers for NVFP4 CUTLASS kernels |
| `pr-flashinfer-2304` | upstream-code | [`sources/prs/flashinfer/PR-2304.md`](../sources/prs/flashinfer/PR-2304.md) | feat: Support Fused MoE non gated Relu2 NVFP4 & FP8 and support Nemotron |
| `pr-flashinfer-2462` | upstream-code | [`sources/prs/flashinfer/PR-2462.md`](../sources/prs/flashinfer/PR-2462.md) | feat: Support Fused MoE non gated Relu2 NVFP4 & FP8 and support Nemotron, fixed |
| `pr-flashinfer-2520` | upstream-code | [`sources/prs/flashinfer/PR-2520.md`](../sources/prs/flashinfer/PR-2520.md) | Support NVFP4 KV cache decode on SM120 |
| `pr-flashinfer-2629` | upstream-code | [`sources/prs/flashinfer/PR-2629.md`](../sources/prs/flashinfer/PR-2629.md) | fix: cute dsl nvfp4 moe routing index error |
| `pr-flashinfer-2667` | upstream-code | [`sources/prs/flashinfer/PR-2667.md`](../sources/prs/flashinfer/PR-2667.md) | perf: Update trtllm-gen batched GEMM kernels - faster, more NVFP4 tile dims, MXFP8 with relu2 act |
| `pr-flashinfer-2702` | upstream-code | [`sources/prs/flashinfer/PR-2702.md`](../sources/prs/flashinfer/PR-2702.md) | Add NVFP4 KV cache quantization support for SM100 |
| `pr-flashinfer-2725` | upstream-code | [`sources/prs/flashinfer/PR-2725.md`](../sources/prs/flashinfer/PR-2725.md) | fix: Add SM120 (RTX Blackwell desktop) support for NVFP4 MoE kernels |
| `pr-flashinfer-2738` | upstream-code | [`sources/prs/flashinfer/PR-2738.md`](../sources/prs/flashinfer/PR-2738.md) | Support for MXFP4 and NVFP4 group GEMMs on GeForce and Spark |
| `pr-flashinfer-2838` | upstream-code | [`sources/prs/flashinfer/PR-2838.md`](../sources/prs/flashinfer/PR-2838.md) | feat: Add CuTe-DSL backend for NVFP4 quantization |
| `pr-flashinfer-2841` | upstream-code | [`sources/prs/flashinfer/PR-2841.md`](../sources/prs/flashinfer/PR-2841.md) | [Perf] Add FMHAv2 to flashinfer_benchmark.py and eliminate unnecessary H2D |
| `pr-flashinfer-2904` | upstream-code | [`sources/prs/flashinfer/PR-2904.md`](../sources/prs/flashinfer/PR-2904.md) | perf: Optimize CuTe-DSL fp4 and fp8 quantization kernels |
| `pr-flashinfer-2959` | upstream-code | [`sources/prs/flashinfer/PR-2959.md`](../sources/prs/flashinfer/PR-2959.md) | [Fmha] Add head_dim=512 support for trtllm attention kernels |
| `pr-flashinfer-2988` | upstream-code | [`sources/prs/flashinfer/PR-2988.md`](../sources/prs/flashinfer/PR-2988.md) | [Fmha] support nvfp4 output keepsMmaAb generation kernels |
| `pr-flashinfer-3027` | upstream-code | [`sources/prs/flashinfer/PR-3027.md`](../sources/prs/flashinfer/PR-3027.md) | [feat] Trtllm-gen Per-token Nvfp4 MoE |
| `pr-flashinfer-3080` | upstream-code | [`sources/prs/flashinfer/PR-3080.md`](../sources/prs/flashinfer/PR-3080.md) | feat: Add b12x_fused_moe / B12xMoEWrapper SM120 APIs with micro kernel and ReLU2 |
| `pr-flashinfer-3097` | upstream-code | [`sources/prs/flashinfer/PR-3097.md`](../sources/prs/flashinfer/PR-3097.md) | Support NVFP4 KV for prefill and batch attention kernels |
| `pr-flashinfer-3113` | upstream-code | [`sources/prs/flashinfer/PR-3113.md`](../sources/prs/flashinfer/PR-3113.md) | Fix: Extend b12x FP4 GEMM support to SM121 (GB10/DGX Spark) |
| `pr-flashinfer-3152` | upstream-code | [`sources/prs/flashinfer/PR-3152.md`](../sources/prs/flashinfer/PR-3152.md) | Integrate CUTLASS Small Tile N Blockscaled GEMMs/Grouped GEMMs for SM120 and SM121 |
| `pr-flashinfer-3157` | upstream-code | [`sources/prs/flashinfer/PR-3157.md`](../sources/prs/flashinfer/PR-3157.md) | feat: DiT layer norm fusions for WAN: flashinfer.diffusion_ops |
| `pr-flashinfer-3185` | upstream-code | [`sources/prs/flashinfer/PR-3185.md`](../sources/prs/flashinfer/PR-3185.md) | feat: enable glm5 router gemm |
| `pr-flashinfer-3237` | upstream-code | [`sources/prs/flashinfer/PR-3237.md`](../sources/prs/flashinfer/PR-3237.md) | perf: optimize per-token nvfp4 quantization kernel. |
| `pr-sglang-10101` | upstream-code | [`sources/prs/sglang/PR-10101.md`](../sources/prs/sglang/PR-10101.md) | Optimize nvfp4 block scaled gemm kernel when M is small. |
| `pr-sglang-10180` | upstream-code | [`sources/prs/sglang/PR-10180.md`](../sources/prs/sglang/PR-10180.md) | Fix chunked prefix cache for nvfp4 |
| `pr-sglang-10426` | upstream-code | [`sources/prs/sglang/PR-10426.md`](../sources/prs/sglang/PR-10426.md) | Fix correction bias undefined behavior for nvfp4 models |
| `pr-sglang-10758` | upstream-code | [`sources/prs/sglang/PR-10758.md`](../sources/prs/sglang/PR-10758.md) | Fix MTP MoE weight loading with NVFP4 target model. |
| `pr-sglang-11287` | upstream-code | [`sources/prs/sglang/PR-11287.md`](../sources/prs/sglang/PR-11287.md) | [NVIDIA] Add new SMs support for Spark & Thor |
| `pr-sglang-11737` | upstream-code | [`sources/prs/sglang/PR-11737.md`](../sources/prs/sglang/PR-11737.md) | support cutlass fp4 kernel in sm120 |
| `pr-sglang-11866` | upstream-code | [`sources/prs/sglang/PR-11866.md`](../sources/prs/sglang/PR-11866.md) | Support nvidia/NVIDIA-Nemotron-Nano-9B-v2-FP8/NVFP4 |
| `pr-sglang-12018` | upstream-code | [`sources/prs/sglang/PR-12018.md`](../sources/prs/sglang/PR-12018.md) | Feature/nano v2 offline modelopt fp8 and nvfp4 |
| `pr-sglang-12581` | upstream-code | [`sources/prs/sglang/PR-12581.md`](../sources/prs/sglang/PR-12581.md) | [NVIDIA] Fix CUDA arch requirement in nvfp4 cast |
| `pr-sglang-12782` | upstream-code | [`sources/prs/sglang/PR-12782.md`](../sources/prs/sglang/PR-12782.md) | ignore the deepgemm check when the model weight with nvfp4 and moe ba… |
| `pr-sglang-13115` | upstream-code | [`sources/prs/sglang/PR-13115.md`](../sources/prs/sglang/PR-13115.md) | support mtp with deepseek r1 nvfp4 model |
| `pr-sglang-13162` | upstream-code | [`sources/prs/sglang/PR-13162.md`](../sources/prs/sglang/PR-13162.md) | Fix nan in global scaling factor for large scale nvfp4 EP |
| `pr-sglang-13761` | upstream-code | [`sources/prs/sglang/PR-13761.md`](../sources/prs/sglang/PR-13761.md) | [Feat][NVFP4] Enable NVFP4 MoE for Qwen series models (eg. Qwen3-Next) #13761 |
| `pr-sglang-14485` | upstream-code | [`sources/prs/sglang/PR-14485.md`](../sources/prs/sglang/PR-14485.md) | Mistral Large 3 NVFP4 support |
| `pr-sglang-15049` | upstream-code | [`sources/prs/sglang/PR-15049.md`](../sources/prs/sglang/PR-15049.md) | Mistral Large 3 NVFP4 TRTLLM MoE support |
| `pr-sglang-15280` | upstream-code | [`sources/prs/sglang/PR-15280.md`](../sources/prs/sglang/PR-15280.md) | [NVIDIA] Fixes for NVFP4 all-gather with spec decoding |
| `pr-sglang-17158` | upstream-code | [`sources/prs/sglang/PR-17158.md`](../sources/prs/sglang/PR-17158.md) | Inclusion of nvfp4 blockscale in EPLB Rebalance |
| `pr-sglang-17627` | upstream-code | [`sources/prs/sglang/PR-17627.md`](../sources/prs/sglang/PR-17627.md) | [feat] Support nvfp4 quantized model of Qwen3-Next |
| `pr-sglang-18065` | upstream-code | [`sources/prs/sglang/PR-18065.md`](../sources/prs/sglang/PR-18065.md) | [Bugfix] Fix Mistral Large 3 NVFP4 TRTLLM MoE |
| `pr-sglang-18085` | upstream-code | [`sources/prs/sglang/PR-18085.md`](../sources/prs/sglang/PR-18085.md) | Fix nvfp4 weight update |
| `pr-sglang-18370` | upstream-code | [`sources/prs/sglang/PR-18370.md`](../sources/prs/sglang/PR-18370.md) | [Kimi-K2.5] Fix NVFP4 Kimi-K2.5 weight mapping and exclude list |
| `pr-sglang-18389` | upstream-code | [`sources/prs/sglang/PR-18389.md`](../sources/prs/sglang/PR-18389.md) | Nsa trtllm mla sparse fp8 support with Deepseek v3.2 NVFP4 |
| `pr-sglang-18750` | upstream-code | [`sources/prs/sglang/PR-18750.md`](../sources/prs/sglang/PR-18750.md) | fix(sgl-kernel): use >= 120 for SM12x CUDA kernel dispatch |
| `pr-sglang-18801` | upstream-code | [`sources/prs/sglang/PR-18801.md`](../sources/prs/sglang/PR-18801.md) | Support CuteDSL `mm_fp4` backend |
| `pr-sglang-19143` | upstream-code | [`sources/prs/sglang/PR-19143.md`](../sources/prs/sglang/PR-19143.md) | feat: Support MXFP4 quantized dense models on AMD CDNA2/CDNA3 GPUs |
| `pr-sglang-19437` | upstream-code | [`sources/prs/sglang/PR-19437.md`](../sources/prs/sglang/PR-19437.md) | [Kernel Slimming] Migrate NVFP4 kernels to JIT |
| `pr-sglang-19652` | upstream-code | [`sources/prs/sglang/PR-19652.md`](../sources/prs/sglang/PR-19652.md) | [Feature] NVFP4 Marlin fallback for non-Blackwell GPUs (SM75+) |
| `pr-sglang-20012` | upstream-code | [`sources/prs/sglang/PR-20012.md`](../sources/prs/sglang/PR-20012.md) | [JIT Kernel] Reland NVFP4 kernels to JIT |
| `pr-sglang-20137` | upstream-code | [`sources/prs/sglang/PR-20137.md`](../sources/prs/sglang/PR-20137.md) | [diffusion] Support nvfp4 for Flux.2 |
| `pr-sglang-20268` | upstream-code | [`sources/prs/sglang/PR-20268.md`](../sources/prs/sglang/PR-20268.md) | [4/n jit_kernel restruct] speed up CI tests and add benchmark workflow |
| `pr-sglang-20407` | upstream-code | [`sources/prs/sglang/PR-20407.md`](../sources/prs/sglang/PR-20407.md) | [Model] Support Nemotron 3 Super NVFP4 |
| `pr-sglang-20874` | upstream-code | [`sources/prs/sglang/PR-20874.md`](../sources/prs/sglang/PR-20874.md) | [JIT Kernel] Fix NVFP4 multi-arch compilation failure |
| `pr-sglang-20910` | upstream-code | [`sources/prs/sglang/PR-20910.md`](../sources/prs/sglang/PR-20910.md) | Add SGLang CUDA crash API logging inspired by FlashInfer |
| `pr-sglang-21022` | upstream-code | [`sources/prs/sglang/PR-21022.md`](../sources/prs/sglang/PR-21022.md) | [Chore] Clean up JIT compilation flags |
| `pr-sglang-21239` | upstream-code | [`sources/prs/sglang/PR-21239.md`](../sources/prs/sglang/PR-21239.md) | Refactor JIT kernel CI to use run_suite.py registration system |
| `pr-sglang-21314` | upstream-code | [`sources/prs/sglang/PR-21314.md`](../sources/prs/sglang/PR-21314.md) | CUTLASS NVFP4 GEMM improvement of SM120 |
| `pr-sglang-21321` | upstream-code | [`sources/prs/sglang/PR-21321.md`](../sources/prs/sglang/PR-21321.md) | [Kernel] Support FlashInfer TRTLLM-Gen fused MoE for non-gated FP4 & FP8 (Nemotron) |
| `pr-sglang-21325` | upstream-code | [`sources/prs/sglang/PR-21325.md`](../sources/prs/sglang/PR-21325.md) | [misc] clean up kernel API |
| `pr-sglang-22064` | upstream-code | [`sources/prs/sglang/PR-22064.md`](../sources/prs/sglang/PR-22064.md) | [Diffusion] Fix weight scale swizzle and add large-M kernel config for FLUX.2-dev-NVFP4 |
| `pr-sglang-22079` | upstream-code | [`sources/prs/sglang/PR-22079.md`](../sources/prs/sglang/PR-22079.md) | [nvidia] Gemma4 nvfp4 fix |
| `pr-sglang-22091` | upstream-code | [`sources/prs/sglang/PR-22091.md`](../sources/prs/sglang/PR-22091.md) | [diffusion] Default NVFP4 to CUTLASS and add all-model shape benchmarks |
| `pr-sglang-22127` | upstream-code | [`sources/prs/sglang/PR-22127.md`](../sources/prs/sglang/PR-22127.md) | [Diffusion] Add diffusion NVFP4 scaled-mm correctness test |
| `pr-sglang-22204` | upstream-code | [`sources/prs/sglang/PR-22204.md`](../sources/prs/sglang/PR-22204.md) | [RL] Refactor NVFP4 shuffling/swizzling to in-place replacement |
| `pr-sglang-22574` | upstream-code | [`sources/prs/sglang/PR-22574.md`](../sources/prs/sglang/PR-22574.md) | [Diffusion] Add FLUX.1-dev ModelOpt NVFP4 support |
| `pr-sglang-22672` | upstream-code | [`sources/prs/sglang/PR-22672.md`](../sources/prs/sglang/PR-22672.md) | reland [Diffusion] Add FLUX.1-dev ModelOpt NVFP4 support |
| `pr-sglang-22681` | upstream-code | [`sources/prs/sglang/PR-22681.md`](../sources/prs/sglang/PR-22681.md) | [Diffusion] Add Wan2.2 ModelOpt NVFP4 support |
| `pr-sglang-22717` | upstream-code | [`sources/prs/sglang/PR-22717.md`](../sources/prs/sglang/PR-22717.md) | [codex] Add flashinfer TRTLLM backend for diffusion NVFP4 |
| `pr-sglang-23590` | upstream-code | [`sources/prs/sglang/PR-23590.md`](../sources/prs/sglang/PR-23590.md) | Reland Cute-DSL FP4 dense GEMM |
| `pr-sglang-23745` | upstream-code | [`sources/prs/sglang/PR-23745.md`](../sources/prs/sglang/PR-23745.md) | Use Cute-DSL NVFP4 quantization kernels |
| `pr-sglang-25107` | upstream-code | [`sources/prs/sglang/PR-25107.md`](../sources/prs/sglang/PR-25107.md) | perf(nvfp4): free unused source scales after weight processing |
| `pr-sglang-3899` | upstream-code | [`sources/prs/sglang/PR-3899.md`](../sources/prs/sglang/PR-3899.md) | Support FP4 gemm (1/2) |
| `pr-sglang-4953` | upstream-code | [`sources/prs/sglang/PR-4953.md`](../sources/prs/sglang/PR-4953.md) | [Build] Fix cuda12.8 build error in nvfp4_scaled_mm_kernels.cu |
| `pr-sglang-6093` | upstream-code | [`sources/prs/sglang/PR-6093.md`](../sources/prs/sglang/PR-6093.md) | [1/2] Add Kernel support for Cutlass based Fused FP4 MoE |
| `pr-sglang-7302` | upstream-code | [`sources/prs/sglang/PR-7302.md`](../sources/prs/sglang/PR-7302.md) | Support NVFP4 quantized dense models on AMD CDNA2/CDNA3 GPUs |
| `pr-sglang-7327` | upstream-code | [`sources/prs/sglang/PR-7327.md`](../sources/prs/sglang/PR-7327.md) | FlashInfer NVFP4 MoE with EP & 2-stream shared expert |
| `pr-sglang-7912` | upstream-code | [`sources/prs/sglang/PR-7912.md`](../sources/prs/sglang/PR-7912.md) | Qwen FP8/NVFP4 ModelOPT Quantization support |
| `pr-sglang-8127` | upstream-code | [`sources/prs/sglang/PR-8127.md`](../sources/prs/sglang/PR-8127.md) | [Fix][Ready]Fix register spilling in cutlass nvfp4 gemm kernel on Blackwell |
| `pr-sglang-8552` | upstream-code | [`sources/prs/sglang/PR-8552.md`](../sources/prs/sglang/PR-8552.md) | [NVIDIA] Add Low Latency NVFP4 decode kernels from Flashinfer |
| `pr-sglang-9162` | upstream-code | [`sources/prs/sglang/PR-9162.md`](../sources/prs/sglang/PR-9162.md) | Faster weight processing (trtllm-gen moe nvfp4) |
| `pr-sglang-9199` | upstream-code | [`sources/prs/sglang/PR-9199.md`](../sources/prs/sglang/PR-9199.md) | [NVIDIA] [3/N] Nvfp4 Masked Gemm: Add flashinfer grouped_gemm_nt_masked  |
| `pr-sglang-9200` | upstream-code | [`sources/prs/sglang/PR-9200.md`](../sources/prs/sglang/PR-9200.md) | [NVIDA] [1/N] Nvfp4 Masked Gemm: Add quant op for the flashinfer grouped gemm |
| `pr-sglang-9556` | upstream-code | [`sources/prs/sglang/PR-9556.md`](../sources/prs/sglang/PR-9556.md) | [NVIDIA] [2/N] Optimize `silu_and_mul_scaled_fp4_grouped_quant` perf |
| `pr-sglang-9807` | upstream-code | [`sources/prs/sglang/PR-9807.md`](../sources/prs/sglang/PR-9807.md) | Make fp4_quantize kernels work on sm103 |
| `pr-tensorrt-llm-10339` | upstream-code | [`sources/prs/tensorrt-llm/PR-10339.md`](../sources/prs/tensorrt-llm/PR-10339.md) | [TRTLLM-9661][chore] Further reduce tuning time for cuteDSL nvFP4 dense gemm. |
| `pr-tensorrt-llm-10479` | upstream-code | [`sources/prs/tensorrt-llm/PR-10479.md`](../sources/prs/tensorrt-llm/PR-10479.md) | [None] [feat] Add densegemm backend for MoE |
| `pr-tensorrt-llm-11165` | upstream-code | [`sources/prs/tensorrt-llm/PR-11165.md`](../sources/prs/tensorrt-llm/PR-11165.md) | [https://nvbugs/5799917][fix] Recover from CUTLASS MoE doActivation perf regression for MXFP4/NVFP4 dtype |
| `pr-tensorrt-llm-11273` | upstream-code | [`sources/prs/tensorrt-llm/PR-11273.md`](../sources/prs/tensorrt-llm/PR-11273.md) | [None][feat] Optimize super-v3 nvfp4 for better perf |
| `pr-tensorrt-llm-11473` | upstream-code | [`sources/prs/tensorrt-llm/PR-11473.md`](../sources/prs/tensorrt-llm/PR-11473.md) | [None][feat] Optimize by fuse nvfp4_quant to layernorm_gated for mamba2_mixer |
| `pr-tensorrt-llm-11589` | upstream-code | [`sources/prs/tensorrt-llm/PR-11589.md`](../sources/prs/tensorrt-llm/PR-11589.md) | [TRTLLM-10004][feat] Enable GEMM -> AR with GEMM output in registered buffers |
| `pr-tensorrt-llm-11652` | upstream-code | [`sources/prs/tensorrt-llm/PR-11652.md`](../sources/prs/tensorrt-llm/PR-11652.md) | [None][feat] NVFP4 TRTLLM-Gen MoE for AutoDeploy (Nemotron Super) |
| `pr-tensorrt-llm-11733` | upstream-code | [`sources/prs/tensorrt-llm/PR-11733.md`](../sources/prs/tensorrt-llm/PR-11733.md) | [https://nvbugs/5799917][fix] Recover from CUTLASS MoE doActivation perf regression for MXFP4/NVFP4 dtype |
| `pr-tensorrt-llm-11774` | upstream-code | [`sources/prs/tensorrt-llm/PR-11774.md`](../sources/prs/tensorrt-llm/PR-11774.md) | [None][fix] Fix SM120 issue for rms_norm with nvfp4_quant_fusion |
| `pr-tensorrt-llm-11897` | upstream-code | [`sources/prs/tensorrt-llm/PR-11897.md`](../sources/prs/tensorrt-llm/PR-11897.md) | [TRTLLM-10990][feat] Fuse SwiGLU and quant into shared expert |
| `pr-tensorrt-llm-12320` | upstream-code | [`sources/prs/tensorrt-llm/PR-12320.md`](../sources/prs/tensorrt-llm/PR-12320.md) | [None][feat] Support update weight for nvfp4 |
| `pr-tensorrt-llm-12322` | upstream-code | [`sources/prs/tensorrt-llm/PR-12322.md`](../sources/prs/tensorrt-llm/PR-12322.md) | [https://nvbugs/5983390][perf] Kernel fusions in _gather_k_cache_for_chunk of Indexer in DSA |
| `pr-tensorrt-llm-12866` | upstream-code | [`sources/prs/tensorrt-llm/PR-12866.md`](../sources/prs/tensorrt-llm/PR-12866.md) | [None][feat] AutoDeploy: Onboard google/gemma-4-31B-it dense model, including nvfp4 |
| `pr-tensorrt-llm-13117` | upstream-code | [`sources/prs/tensorrt-llm/PR-13117.md`](../sources/prs/tensorrt-llm/PR-13117.md) | [None][feat] Add FP4 residual quantization kernel without channel reo… |
| `pr-tensorrt-llm-13149` | upstream-code | [`sources/prs/tensorrt-llm/PR-13149.md`](../sources/prs/tensorrt-llm/PR-13149.md) | [TRTLLM-11958][perf] reduce @torch.library.custom_op host overhead |
| `pr-tensorrt-llm-13268` | upstream-code | [`sources/prs/tensorrt-llm/PR-13268.md`](../sources/prs/tensorrt-llm/PR-13268.md) | [https://nvbugs/6095953][fix] Fix cache memory estimation for Qwen3 hybrid models in trtllm-bench |
| `pr-tensorrt-llm-13433` | upstream-code | [`sources/prs/tensorrt-llm/PR-13433.md`](../sources/prs/tensorrt-llm/PR-13433.md) | [None][perf] Extend customMoeRouting kernel to support Qwen3.5 |
| `pr-tensorrt-llm-13570` | upstream-code | [`sources/prs/tensorrt-llm/PR-13570.md`](../sources/prs/tensorrt-llm/PR-13570.md) | [TRTLLM-12128][feat] enable SageAttention for Wan/FLUX (new commits) |
| `pr-tensorrt-llm-13595` | upstream-code | [`sources/prs/tensorrt-llm/PR-13595.md`](../sources/prs/tensorrt-llm/PR-13595.md) | [None][feat] Enable EPLB for DeepSeek-V4 |
| `pr-tensorrt-llm-13658` | upstream-code | [`sources/prs/tensorrt-llm/PR-13658.md`](../sources/prs/tensorrt-llm/PR-13658.md) | [None][test] add Nemotron Ultra V3 AutoDeploy accuracy test |
| `pr-tensorrt-llm-13837` | upstream-code | [`sources/prs/tensorrt-llm/PR-13837.md`](../sources/prs/tensorrt-llm/PR-13837.md) | [None][test] Add func and perf case of nemotron-3-Nano-Omni model on DGX-Spark |
| `pr-tensorrt-llm-13997` | upstream-code | [`sources/prs/tensorrt-llm/PR-13997.md`](../sources/prs/tensorrt-llm/PR-13997.md) | [None][feat] enable TRTLLM-Gen internal routing |
| `pr-tensorrt-llm-4867` | upstream-code | [`sources/prs/tensorrt-llm/PR-4867.md`](../sources/prs/tensorrt-llm/PR-4867.md) | feat: Add w4a8_mxfp4_fp8 quantization recipe. |
| `pr-tensorrt-llm-6809` | upstream-code | [`sources/prs/tensorrt-llm/PR-6809.md`](../sources/prs/tensorrt-llm/PR-6809.md) | [OMNIML-2336][feat] Add NVFP4 x FP8 |
| `pr-tensorrt-llm-7524` | upstream-code | [`sources/prs/tensorrt-llm/PR-7524.md`](../sources/prs/tensorrt-llm/PR-7524.md) | [None][chore] Fix kernel launch param and add TRTLLM MoE backend test |
| `pr-tensorrt-llm-8405` | upstream-code | [`sources/prs/tensorrt-llm/PR-8405.md`](../sources/prs/tensorrt-llm/PR-8405.md) | [TRTLLM-8535][feat] Support DeepSeek V3.2 with FP8 + BF16 KV cache/NVFP4 + BF16 KV cache |
| `pr-tensorrt-llm-8620` | upstream-code | [`sources/prs/tensorrt-llm/PR-8620.md`](../sources/prs/tensorrt-llm/PR-8620.md) | [None][feat] Enable nvfp4 cuda core for sm120 |
| `pr-tensorrt-llm-9025` | upstream-code | [`sources/prs/tensorrt-llm/PR-9025.md`](../sources/prs/tensorrt-llm/PR-9025.md) | [None][feat] Update TRTLLM MoE cubins; reduce mxfp4 weight padding requirement; tighten TMA bound |
| `pr-tensorrt-llm-9729` | upstream-code | [`sources/prs/tensorrt-llm/PR-9729.md`](../sources/prs/tensorrt-llm/PR-9729.md) | [None][feat] add fp4 gemm + allreduce |
| `pr-triton-10151` | upstream-code | [`sources/prs/triton/PR-10151.md`](../sources/prs/triton/PR-10151.md) | [Tutorials] Fix unbound local variable in Tutorial 10 |
| `pr-triton-10196` | upstream-code | [`sources/prs/triton/PR-10196.md`](../sources/prs/triton/PR-10196.md) | [MULTICTA] Fix multicast pattern for tcgen05_mma_scaled |
| `pr-triton-10249` | upstream-code | [`sources/prs/triton/PR-10249.md`](../sources/prs/triton/PR-10249.md) | [triton_kernels] nvfp4 x nvfp4 tuning |
| `pr-vllm-12784` | upstream-code | [`sources/prs/vllm/PR-12784.md`](../sources/prs/vllm/PR-12784.md) | [NVIDIA] Support nvfp4 quantization |
| `pr-vllm-13571` | upstream-code | [`sources/prs/vllm/PR-13571.md`](../sources/prs/vllm/PR-13571.md) | [NVIDIA] Support nvfp4 cutlass gemm |
| `pr-vllm-16362` | upstream-code | [`sources/prs/vllm/PR-16362.md`](../sources/prs/vllm/PR-16362.md) | [Hardware/NVIDIA/Kernel] [Functional Enablement] [1/N] Enable nvidia/DeepSeek-R1-FP4 Model |
| `pr-vllm-17914` | upstream-code | [`sources/prs/vllm/PR-17914.md`](../sources/prs/vllm/PR-17914.md) | [Misc] Add compressed-tensors NVFP4A16 emulation support |
| `pr-vllm-18000` | upstream-code | [`sources/prs/vllm/PR-18000.md`](../sources/prs/vllm/PR-18000.md) | Use NVFP4 Marlin for CompressedTensorsW4A16Fp4 |
| `pr-vllm-18312` | upstream-code | [`sources/prs/vllm/PR-18312.md`](../sources/prs/vllm/PR-18312.md) | [Quantization] Add compressed-tensors NVFP4 support |
| `pr-vllm-19110` | upstream-code | [`sources/prs/vllm/PR-19110.md`](../sources/prs/vllm/PR-19110.md) | [Hardware][NVIDIA] FP4 MoE kernel optimization |
| `pr-vllm-19500` | upstream-code | [`sources/prs/vllm/PR-19500.md`](../sources/prs/vllm/PR-19500.md) | [Hardware][NVIDIA][kernel] Fp4 MOE quant kernel optimization |
| `pr-vllm-19879` | upstream-code | [`sources/prs/vllm/PR-19879.md`](../sources/prs/vllm/PR-19879.md) | [Quantization] Add compressed-tensors emulations support for NVFP4 |
| `pr-vllm-19990` | upstream-code | [`sources/prs/vllm/PR-19990.md`](../sources/prs/vllm/PR-19990.md) | [Quantization] Add compressed-tensors NVFP4 MoE Support |
| `pr-vllm-20141` | upstream-code | [`sources/prs/vllm/PR-20141.md`](../sources/prs/vllm/PR-20141.md) | [Bugfix] Fix some narrowing conversion warnings |
| `pr-vllm-20324` | upstream-code | [`sources/prs/vllm/PR-20324.md`](../sources/prs/vllm/PR-20324.md) | [Kernel][Bugfix] Fixup some warnings in nvfp4_blockwise_moe when CUDA < 12.8 |
| `pr-vllm-21309` | upstream-code | [`sources/prs/vllm/PR-21309.md`](../sources/prs/vllm/PR-21309.md) | Support CUTLASS NVFP4 (w4a4) for Blackwell Geforce GPUs (SM120) |
| `pr-vllm-21331` | upstream-code | [`sources/prs/vllm/PR-21331.md`](../sources/prs/vllm/PR-21331.md) | Support Tensorrt-LLM MoE fp4 for low-latency |
| `pr-vllm-21408` | upstream-code | [`sources/prs/vllm/PR-21408.md`](../sources/prs/vllm/PR-21408.md) | Update flashinfer CUTLASS NVFP4 MoE Kernel to use per expert global scaling factor |
| `pr-vllm-21465` | upstream-code | [`sources/prs/vllm/PR-21465.md`](../sources/prs/vllm/PR-21465.md) | [Bug] Fix Compressed Tensor NVFP4 `cutlass_fp4_group_mm` illegal memory access |
| `pr-vllm-21639` | upstream-code | [`sources/prs/vllm/PR-21639.md`](../sources/prs/vllm/PR-21639.md) | [Feature] Add Flashinfer MoE Support for Compressed Tensor NVFP4 |
| `pr-vllm-22703` | upstream-code | [`sources/prs/vllm/PR-22703.md`](../sources/prs/vllm/PR-22703.md) | [NVIDIA] Support Flashinfer TRTLLM FP8-q/kv NVFP4-out Attention Kernel |
| `pr-vllm-23140` | upstream-code | [`sources/prs/vllm/PR-23140.md`](../sources/prs/vllm/PR-23140.md) | Fix nvfp4 swizzling |
| `pr-vllm-23659` | upstream-code | [`sources/prs/vllm/PR-23659.md`](../sources/prs/vllm/PR-23659.md) | [Bugfix] Fix Marlin NVFP4 for modelopt |
| `pr-vllm-23671` | upstream-code | [`sources/prs/vllm/PR-23671.md`](../sources/prs/vllm/PR-23671.md) | [NVIDIA] Support SiluMul + NVFP4 quant fusion |
| `pr-vllm-23696` | upstream-code | [`sources/prs/vllm/PR-23696.md`](../sources/prs/vllm/PR-23696.md) | [Kernel][B200] `mxfp4` fused cutlass moe |
| `pr-vllm-23727` | upstream-code | [`sources/prs/vllm/PR-23727.md`](../sources/prs/vllm/PR-23727.md) | [Bugfix][Misc] Fix silu_and_mul_nvfp4_quant issue and extract common utils for nvfp4 kernel source files |
| `pr-vllm-23929` | upstream-code | [`sources/prs/vllm/PR-23929.md`](../sources/prs/vllm/PR-23929.md) | [BUGFIX ] fix undefined silu_and_mul_nvfp4_quant |
| `pr-vllm-24440` | upstream-code | [`sources/prs/vllm/PR-24440.md`](../sources/prs/vllm/PR-24440.md) | [Transform] [Quantization] Add QuTLASS support to vLLM |
| `pr-vllm-24833` | upstream-code | [`sources/prs/vllm/PR-24833.md`](../sources/prs/vllm/PR-24833.md) | [Bugfix] Fix accuracy issue for silu_mul + nvfp4 quant fusion kernel |
| `pr-vllm-25193` | upstream-code | [`sources/prs/vllm/PR-25193.md`](../sources/prs/vllm/PR-25193.md) | [Compile] Fix Compile Warning for Ignoring `MIN_BLOCK_PER_SM` |
| `pr-vllm-25609` | upstream-code | [`sources/prs/vllm/PR-25609.md`](../sources/prs/vllm/PR-25609.md) | Enable Fbgemm NVFP4 on Dense models |
| `pr-vllm-25968` | upstream-code | [`sources/prs/vllm/PR-25968.md`](../sources/prs/vllm/PR-25968.md) | [Quantization/NVFP4] Speed up TRTLLM NVFP4 MOE weight loading and fix K/V scale loading for MLA Attn |
| `pr-vllm-25987` | upstream-code | [`sources/prs/vllm/PR-25987.md`](../sources/prs/vllm/PR-25987.md) | [Bugfix] Allow skipping MoE in NVFP4 (fix for MTP) |
| `pr-vllm-25990` | upstream-code | [`sources/prs/vllm/PR-25990.md`](../sources/prs/vllm/PR-25990.md) | [MoE] Nvfp4 Masked Gemm: Add flashinfer grouped_gemm_nt_masked |
| `pr-vllm-26107` | upstream-code | [`sources/prs/vllm/PR-26107.md`](../sources/prs/vllm/PR-26107.md) | [NVIDIA] Add support for cudnn fp4 gemm via flashinfer |
| `pr-vllm-26135` | upstream-code | [`sources/prs/vllm/PR-26135.md`](../sources/prs/vllm/PR-26135.md) | [ModelOpt] Load w13/w2_input_scale for all experts, nvfp4 |
| `pr-vllm-27532` | upstream-code | [`sources/prs/vllm/PR-27532.md`](../sources/prs/vllm/PR-27532.md) | [Attention] Use sparse prefill kernel for fp8 kv-cache in DeepSeek-v3.2 |
| `pr-vllm-28892` | upstream-code | [`sources/prs/vllm/PR-28892.md`](../sources/prs/vllm/PR-28892.md) | Add TRTLLM MoE NVFP4 kernel to CompressedTensorsW4A4MoeMethod |
| `pr-vllm-29004` | upstream-code | [`sources/prs/vllm/PR-29004.md`](../sources/prs/vllm/PR-29004.md) | [Feat] Support non-gated activations in NVFP4 modelopt path |
| `pr-vllm-29242` | upstream-code | [`sources/prs/vllm/PR-29242.md`](../sources/prs/vllm/PR-29242.md) | [Kernel] Add NVFP4 MoE CUTLASS support for SM120 |
| `pr-vllm-29742` | upstream-code | [`sources/prs/vllm/PR-29742.md`](../sources/prs/vllm/PR-29742.md) | [Bugfix] Fix mismatched nvfp4 gemm output shape |
| `pr-vllm-29804` | upstream-code | [`sources/prs/vllm/PR-29804.md`](../sources/prs/vllm/PR-29804.md) | [EPLB] Support EPLB w/ NVFP4 |
| `pr-vllm-30881` | upstream-code | [`sources/prs/vllm/PR-30881.md`](../sources/prs/vllm/PR-30881.md) | [Compressed-Tensors] Simplify NVFP4 Conditions, enable marlin support for NVFP4A16 MoEs |
| `pr-vllm-30885` | upstream-code | [`sources/prs/vllm/PR-30885.md`](../sources/prs/vllm/PR-30885.md) | [Kernel][Performance] Enable smaller Scaling Factor tiling for NVFP4 small-batch decoding |
| `pr-vllm-30897` | upstream-code | [`sources/prs/vllm/PR-30897.md`](../sources/prs/vllm/PR-30897.md) | [NVFP4][Perf] Tune NVFP4 input quant kernel for small batch size |
| `pr-vllm-31099` | upstream-code | [`sources/prs/vllm/PR-31099.md`](../sources/prs/vllm/PR-31099.md) |  [FIX] Always support TP > 4 for FP4 Gemm |
| `pr-vllm-31742` | upstream-code | [`sources/prs/vllm/PR-31742.md`](../sources/prs/vllm/PR-31742.md) | [Bugfix] Fix Broken ModelOpt NVFP4 MoE |
| `pr-vllm-31837` | upstream-code | [`sources/prs/vllm/PR-31837.md`](../sources/prs/vllm/PR-31837.md) | [Perf] Fuse stride preparation for NVFP4 cutlass_moe |
| `pr-vllm-32520` | upstream-code | [`sources/prs/vllm/PR-32520.md`](../sources/prs/vllm/PR-32520.md) | [Perf][Kernel] Optimize FP4 quantization kernels (SM100F) |
| `pr-vllm-33076` | upstream-code | [`sources/prs/vllm/PR-33076.md`](../sources/prs/vllm/PR-33076.md) | Support compress-tensors with nvfp4 or fp8 weights and modelopt with nvfp4 weights on Turing |
| `pr-vllm-33417` | upstream-code | [`sources/prs/vllm/PR-33417.md`](../sources/prs/vllm/PR-33417.md) | fix: Add SM120 (RTX Blackwell) support for FlashInfer CUTLASS NVFP4 MoE kernels |
| `pr-vllm-33506` | upstream-code | [`sources/prs/vllm/PR-33506.md`](../sources/prs/vllm/PR-33506.md) | [Kernel] Support Flashinfer trtllm fused MoE non gated FP8 & NVFP4 |
| `pr-vllm-33932` | upstream-code | [`sources/prs/vllm/PR-33932.md`](../sources/prs/vllm/PR-33932.md) | [Bugfix] Fix DSV3.2 NVFP4 |
| `pr-vllm-34298` | upstream-code | [`sources/prs/vllm/PR-34298.md`](../sources/prs/vllm/PR-34298.md) | [ModelBash][DSR1 NVFp4] Avoid Bf16 Bias Cast |
| `pr-vllm-34389` | upstream-code | [`sources/prs/vllm/PR-34389.md`](../sources/prs/vllm/PR-34389.md) | [Custom Ops] Add functional + out variant for scaled_fp4_quant |
| `pr-vllm-34478` | upstream-code | [`sources/prs/vllm/PR-34478.md`](../sources/prs/vllm/PR-34478.md) | [Model] Add NVFP4 quantization support for Step3.5-Flash |
| `pr-vllm-34556` | upstream-code | [`sources/prs/vllm/PR-34556.md`](../sources/prs/vllm/PR-34556.md) | [Quantization] add humming quantization kernel |
| `pr-vllm-34577` | upstream-code | [`sources/prs/vllm/PR-34577.md`](../sources/prs/vllm/PR-34577.md) | [Bugfix] Rescale NVFP4 weight scales to fix BF16 dequant underflow |
| `pr-vllm-34725` | upstream-code | [`sources/prs/vllm/PR-34725.md`](../sources/prs/vllm/PR-34725.md) | [Bugfix] Fix NVFP4 TRTLLM MoE non-gated support; add gsm8k for Nemotron-3-Nano FP8+NVFP4 |
| `pr-vllm-35210` | upstream-code | [`sources/prs/vllm/PR-35210.md`](../sources/prs/vllm/PR-35210.md) | [BugFix] Fix fp4 quant kernel on CUDA 12.8 |
| `pr-vllm-35733` | upstream-code | [`sources/prs/vllm/PR-35733.md`](../sources/prs/vllm/PR-35733.md) | [NVFP4] Support NVFP4 dense models from `modelopt` and `compressed-tensors` on AMD Instinct MI300, MI355X and Hopper through emulation |
| `pr-vllm-36017` | upstream-code | [`sources/prs/vllm/PR-36017.md`](../sources/prs/vllm/PR-36017.md) | [Bugfix] Fix passing of activation_type to trtllm fused MoE NVFP4 and FP8 |
| `pr-vllm-36162` | upstream-code | [`sources/prs/vllm/PR-36162.md`](../sources/prs/vllm/PR-36162.md) | [Mamba] Flashinfer selective_state_update |
| `pr-vllm-36205` | upstream-code | [`sources/prs/vllm/PR-36205.md`](../sources/prs/vllm/PR-36205.md) | [mla] Support fused FP8/NVFP4 output quantization in MLA attention (#35792) |
| `pr-vllm-36725` | upstream-code | [`sources/prs/vllm/PR-36725.md`](../sources/prs/vllm/PR-36725.md) | [Bug][MoE] Fix TRTLLM NVFP4 Routing Kernel Precision |
| `pr-vllm-36728` | upstream-code | [`sources/prs/vllm/PR-36728.md`](../sources/prs/vllm/PR-36728.md) | [Bug][MoE] Strengthen _supports_current_device() checks in the TRTLLM FP8, NVFP4, and FlashInfer CuteDSL MoE experts |
| `pr-vllm-37128` | upstream-code | [`sources/prs/vllm/PR-37128.md`](../sources/prs/vllm/PR-37128.md) | [MoE Refactor] Mxfp4 oracle rebased |
| `pr-vllm-37217` | upstream-code | [`sources/prs/vllm/PR-37217.md`](../sources/prs/vllm/PR-37217.md) | [MoE/EPLB] Fix FlashInfer nvfp4 experts + EPLB correctness |
| `pr-vllm-37320` | upstream-code | [`sources/prs/vllm/PR-37320.md`](../sources/prs/vllm/PR-37320.md) | [Kernel] Add non-gated support for NVFP4 CUTLASS MoE |
| `pr-vllm-37332` | upstream-code | [`sources/prs/vllm/PR-37332.md`](../sources/prs/vllm/PR-37332.md) | Add nvfp4 support to reshape_and_cache_flash |
| `pr-vllm-37463` | upstream-code | [`sources/prs/vllm/PR-37463.md`](../sources/prs/vllm/PR-37463.md) | [Kernel] Add MXFP4 W4A4 CUTLASS MoE kernel for SM100 |
| `pr-vllm-37465` | upstream-code | [`sources/prs/vllm/PR-37465.md`](../sources/prs/vllm/PR-37465.md) | [Bugfix] Remove assertion for NVFP4 scale dynamic range |
| `pr-vllm-37502` | upstream-code | [`sources/prs/vllm/PR-37502.md`](../sources/prs/vllm/PR-37502.md) | [Bugfix] Fix marlin nvfp4 rescaling |
| `pr-vllm-37503` | upstream-code | [`sources/prs/vllm/PR-37503.md`](../sources/prs/vllm/PR-37503.md) | [4/n] Migrate FP4/W4A8 CUTLASS kernels to torch stable ABI |
| `pr-vllm-37695` | upstream-code | [`sources/prs/vllm/PR-37695.md`](../sources/prs/vllm/PR-37695.md) | [Perf] Use torch compile to fuse pack topk in trtllm moe |
| `pr-vllm-37759` | upstream-code | [`sources/prs/vllm/PR-37759.md`](../sources/prs/vllm/PR-37759.md) | [MoE] Move FlashInfer CuteDSL experts into fused_moe/experts/ |
| `pr-vllm-38050` | upstream-code | [`sources/prs/vllm/PR-38050.md`](../sources/prs/vllm/PR-38050.md) | [MoE Kernel] Flashinfer nvfp4 cutedsl moe kernel integration |
| `pr-vllm-38065` | upstream-code | [`sources/prs/vllm/PR-38065.md`](../sources/prs/vllm/PR-38065.md) | [Perf] FP8 FlashInfer Attn for ViT |
| `pr-vllm-38083` | upstream-code | [`sources/prs/vllm/PR-38083.md`](../sources/prs/vllm/PR-38083.md) | [Bugfix] Fix DeepGemm E8M0 accuracy degradation for Qwen3.5 FP8 on Blackwell |
| `pr-vllm-38251` | upstream-code | [`sources/prs/vllm/PR-38251.md`](../sources/prs/vllm/PR-38251.md) | [Quantization] Add FlashInfer CuteDSL batched experts backend for NVFP4 MoE |
| `pr-vllm-38329` | upstream-code | [`sources/prs/vllm/PR-38329.md`](../sources/prs/vllm/PR-38329.md) | [MoE] Add RoutingMethodType.Simulated to TRT-LLM FP8/NVFP4 kernel allowlists |
| `pr-vllm-38423` | upstream-code | [`sources/prs/vllm/PR-38423.md`](../sources/prs/vllm/PR-38423.md) | [NVIDIA] Bugfix NVFP4 DGX Spark and RTX50 |
| `pr-vllm-38573` | upstream-code | [`sources/prs/vllm/PR-38573.md`](../sources/prs/vllm/PR-38573.md) | [Compile] Fix nvfp4 compile warning |
| `pr-vllm-38960` | upstream-code | [`sources/prs/vllm/PR-38960.md`](../sources/prs/vllm/PR-38960.md) | [MoE Refactor] Split up compressed_tensors_moe.py |
| `pr-vllm-39129` | upstream-code | [`sources/prs/vllm/PR-39129.md`](../sources/prs/vllm/PR-39129.md) | [Refactor] Move NVFP4 GEMM management into NvFp4LinearKernel |
| `pr-vllm-39322` | upstream-code | [`sources/prs/vllm/PR-39322.md`](../sources/prs/vllm/PR-39322.md) | [Feature] Batch invariant nvfp4 linear support |
| `pr-vllm-39510` | upstream-code | [`sources/prs/vllm/PR-39510.md`](../sources/prs/vllm/PR-39510.md) | [Kernel] Support TRTLLM GEN NVFP4 MoE for non-512-aligned hidden dims via weight padding |
| `pr-vllm-39717` | upstream-code | [`sources/prs/vllm/PR-39717.md`](../sources/prs/vllm/PR-39717.md) | [Bugfix] Reject non-nvfp4 dtypes when using the flashinfer_nvlink_one_sided all2all backend |
| `pr-vllm-39820` | upstream-code | [`sources/prs/vllm/PR-39820.md`](../sources/prs/vllm/PR-39820.md) | [Bug] Fix batch invariance nvfp4 support |
| `pr-vllm-40177` | upstream-code | [`sources/prs/vllm/PR-40177.md`](../sources/prs/vllm/PR-40177.md) | Add nvfp4 kv cache support |
| `pr-vllm-40191` | upstream-code | [`sources/prs/vllm/PR-40191.md`](../sources/prs/vllm/PR-40191.md) | [Bugfix] Guard mxfp4_experts_quant bindings on ENABLE_NVFP4_SM100 |
| `pr-vllm-40574` | upstream-code | [`sources/prs/vllm/PR-40574.md`](../sources/prs/vllm/PR-40574.md) | [MoE] Move cutlass moe to fused_moe/experts/ |
| `pr-vllm-40960` | upstream-code | [`sources/prs/vllm/PR-40960.md`](../sources/prs/vllm/PR-40960.md) | [DSV4] Add BF16 and MXFP8 A2A support for flashinfer a2a one sided |
| `pr-vllm-41050` | upstream-code | [`sources/prs/vllm/PR-41050.md`](../sources/prs/vllm/PR-41050.md) | [Kernel][MoE] Support GELU on TRT-LLM NvFP4 fused MoE for Gemma4 |
| `pr-vllm-41566` | upstream-code | [`sources/prs/vllm/PR-41566.md`](../sources/prs/vllm/PR-41566.md) | [Quantization] Rework quantization_config to use QuantKey and allow for activation override |
| `pr-vllm-41664` | upstream-code | [`sources/prs/vllm/PR-41664.md`](../sources/prs/vllm/PR-41664.md) | [MXFP4] Support for linear layers + compressed-tensors integration |
| `pr-vllm-41745` | upstream-code | [`sources/prs/vllm/PR-41745.md`](../sources/prs/vllm/PR-41745.md) | [Spec Decode] Add Gemma4 MTP speculative decoding support |
| `pr-vllm-41882` | upstream-code | [`sources/prs/vllm/PR-41882.md`](../sources/prs/vllm/PR-41882.md) | Add NVFP4 all-gather GEMM fusion for AsyncTP |
| `pr-vllm-41979` | upstream-code | [`sources/prs/vllm/PR-41979.md`](../sources/prs/vllm/PR-41979.md) | [MoE] Move various experts classes to fused_moe/experts/ |

<a id="pdl"></a>
## pdl

22 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-cutlass-2161` | upstream-code | [`sources/prs/cutlass/PR-2161.md`](../sources/prs/cutlass/PR-2161.md) | Blockwise Improvement and Programmatic Dependent Launch |
| `pr-flash-attention-2481` | upstream-code | [`sources/prs/flash-attention/PR-2481.md`](../sources/prs/flash-attention/PR-2481.md) | [cute,bwd] fix PDL race in bwd_preprocess, which corrupting dpsum on SM90+ |
| `pr-flashinfer-1668` | upstream-code | [`sources/prs/flashinfer/PR-1668.md`](../sources/prs/flashinfer/PR-1668.md) | TGV GEMM as a BF16 backend alternative to cuBLAS |
| `pr-flashinfer-2928` | upstream-code | [`sources/prs/flashinfer/PR-2928.md`](../sources/prs/flashinfer/PR-2928.md) | fix: clamp enable_pdl=True to False on SM < 90 to prevent PDL PTX on Ampere |
| `pr-flashinfer-3181` | upstream-code | [`sources/prs/flashinfer/PR-3181.md`](../sources/prs/flashinfer/PR-3181.md) | cute-dsl fmha prefill (cubin integration): remove front-padding, add attention_sink, and pdl support |
| `pr-flashinfer-3203` | upstream-code | [`sources/prs/flashinfer/PR-3203.md`](../sources/prs/flashinfer/PR-3203.md) | Include TinyGEMM into BF16 autotuner |
| `pr-sglang-15471` | upstream-code | [`sources/prs/sglang/PR-15471.md`](../sources/prs/sglang/PR-15471.md) | [sgl-kernel][6/7]Support Expert Specialization Grouped GEMM |
| `pr-sglang-15835` | upstream-code | [`sources/prs/sglang/PR-15835.md`](../sources/prs/sglang/PR-15835.md) | [Feature] JIT Fused QK norm + qk norm clean up |
| `pr-sglang-19148` | upstream-code | [`sources/prs/sglang/PR-19148.md`](../sources/prs/sglang/PR-19148.md) | [DeepSeek-V3.2][JIT-kernel] Support nsa fuse store indexer k cache |
| `pr-sglang-19880` | upstream-code | [`sources/prs/sglang/PR-19880.md`](../sources/prs/sglang/PR-19880.md) | [JIT Kernel][Feature] Support JIT custom all reduce (rewrite as v2) |
| `pr-sglang-20047` | upstream-code | [`sources/prs/sglang/PR-20047.md`](../sources/prs/sglang/PR-20047.md) | fix: default FP4 GEMM backend to flashinfer_cudnn on SM120 (Blackwell) |
| `pr-sglang-20479` | upstream-code | [`sources/prs/sglang/PR-20479.md`](../sources/prs/sglang/PR-20479.md) | Support Triton MLA FP8 KV cache |
| `pr-sglang-22931` | upstream-code | [`sources/prs/sglang/PR-22931.md`](../sources/prs/sglang/PR-22931.md) | [Fix/Kernel] Add JIT rmsnorm_hf kernel to fix transformers backend MMLU accuracy regression  |
| `pr-sglang-23745` | upstream-code | [`sources/prs/sglang/PR-23745.md`](../sources/prs/sglang/PR-23745.md) | Use Cute-DSL NVFP4 quantization kernels |
| `pr-sglang-23965` | upstream-code | [`sources/prs/sglang/PR-23965.md`](../sources/prs/sglang/PR-23965.md) | Enable PDL for various kernels in DSV32/GLM5 |
| `pr-sglang-7627` | upstream-code | [`sources/prs/sglang/PR-7627.md`](../sources/prs/sglang/PR-7627.md) | Add dsv3 router gemm kernel |
| `pr-sglang-7630` | upstream-code | [`sources/prs/sglang/PR-7630.md`](../sources/prs/sglang/PR-7630.md) | Add dsv3 fused a gemm to sgl-kernel |
| `pr-tensorrt-llm-10043` | upstream-code | [`sources/prs/tensorrt-llm/PR-10043.md`](../sources/prs/tensorrt-llm/PR-10043.md) | [TRTLLM-9992][perf] Enable PDL for CuteDSL kernels and overlap MoeOutputMemset |
| `pr-tensorrt-llm-12046` | upstream-code | [`sources/prs/tensorrt-llm/PR-12046.md`](../sources/prs/tensorrt-llm/PR-12046.md) | [https://nvbugs/5955188][fix] Fix harmony parsers and WAR routing PDL for agentic coding use cases |
| `pr-tensorrt-llm-12506` | upstream-code | [`sources/prs/tensorrt-llm/PR-12506.md`](../sources/prs/tensorrt-llm/PR-12506.md) | [None][feat] Add PDL support to CuTE DSL top-k kernels |
| `pr-tensorrt-llm-13477` | upstream-code | [`sources/prs/tensorrt-llm/PR-13477.md`](../sources/prs/tensorrt-llm/PR-13477.md) | [None][perf] Scheme X L2-aware dispatcher and PDL launchers for sparse-attention GVR Top-K |
| `pr-vllm-34758` | upstream-code | [`sources/prs/vllm/PR-34758.md`](../sources/prs/vllm/PR-34758.md) | [Model Bash] DeepSeek R1 BF16 Min Latency QKV A GEMM (0.5% E2E Speedup) |

<a id="tcgen05"></a>
## tcgen05

41 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `blog-modular-blackwell` | community-note | [`sources/blogs/modular-blackwell-matmul.md`](../sources/blogs/modular-blackwell-matmul.md) | Modular: Matrix Multiplication on Blackwell |
| `contest-flashinfer-track-a` | contest-report | [`sources/contests/flashinfer-mlsys26/track-a-fused-moe.md`](../sources/contests/flashinfer-mlsys26/track-a-fused-moe.md) | FlashInfer MLSys 2026 - Track A: Fused MoE FP8 |
| `contest-flashinfer-track-b` | contest-report | [`sources/contests/flashinfer-mlsys26/track-b-sparse-attention.md`](../sources/contests/flashinfer-mlsys26/track-b-sparse-attention.md) | FlashInfer MLSys 2026 - Track B: DeepSeek V3.2 Sparse Attention |
| `contest-flashinfer-track-c` | contest-report | [`sources/contests/flashinfer-mlsys26/track-c-gated-delta-net.md`](../sources/contests/flashinfer-mlsys26/track-c-gated-delta-net.md) | FlashInfer MLSys 2026 - Track C: Gated Delta Net |
| `contest-gpumode-p2` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-2-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-2-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 2: NVFP4 GEMM |
| `contest-gpumode-p3` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-3-gated-dual-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-3-gated-dual-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 3: Gated Dual GEMM |
| `contest-gpumode-p4` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 4: Grouped GEMM |
| `pr-cutlass-2139` | upstream-code | [`sources/prs/cutlass/PR-2139.md`](../sources/prs/cutlass/PR-2139.md) | Blockwise and Groupwise GEMM for Blackwell and Improvements for Hopper |
| `pr-cutlass-2161` | upstream-code | [`sources/prs/cutlass/PR-2161.md`](../sources/prs/cutlass/PR-2161.md) | Blockwise Improvement and Programmatic Dependent Launch |
| `pr-cutlass-2466` | upstream-code | [`sources/prs/cutlass/PR-2466.md`](../sources/prs/cutlass/PR-2466.md) | Example 77 add blackwell fmha bwd for MLA shape |
| `pr-cutlass-2472` | upstream-code | [`sources/prs/cutlass/PR-2472.md`](../sources/prs/cutlass/PR-2472.md) | Add Blackwell MLA forward (shape: d=192, dv=128) implementation |
| `pr-cutlass-2746` | upstream-code | [`sources/prs/cutlass/PR-2746.md`](../sources/prs/cutlass/PR-2746.md) | Support for GEMM-K=0 for Blackwell Grouped GEMMs |
| `pr-cutlass-2946` | upstream-code | [`sources/prs/cutlass/PR-2946.md`](../sources/prs/cutlass/PR-2946.md) | [Cutlass profiler] Fix SM100 FP8 nosmem epilogue shape_div “Divisibility Condition” for non‑multiple‑of‑64 N tiles |
| `pr-cutlass-2995` | upstream-code | [`sources/prs/cutlass/PR-2995.md`](../sources/prs/cutlass/PR-2995.md) | [CuTeDSL] Fix: SM100 block-scale gemm overlapping accumulator |
| `pr-deepgemm-304` | upstream-code | [`sources/prs/deepgemm/PR-304.md`](../sources/prs/deepgemm/PR-304.md) | [Public release 26/04] Introducing Mega MoE, FP4 Indexer and other features/fixes |
| `pr-flash-attention-2108` | upstream-code | [`sources/prs/flash-attention/PR-2108.md`](../sources/prs/flash-attention/PR-2108.md) | [NVIDIA] Enable Jetson Thor FA4 |
| `pr-flashinfer-1548` | upstream-code | [`sources/prs/flashinfer/PR-1548.md`](../sources/prs/flashinfer/PR-1548.md) | perf: Enable SplitK and fix autotuner for trtllm fp4 fused moe |
| `pr-flashinfer-1668` | upstream-code | [`sources/prs/flashinfer/PR-1668.md`](../sources/prs/flashinfer/PR-1668.md) | TGV GEMM as a BF16 backend alternative to cuBLAS |
| `pr-flashinfer-1681` | upstream-code | [`sources/prs/flashinfer/PR-1681.md`](../sources/prs/flashinfer/PR-1681.md) | perf: improve performance of cutlass fmha |
| `pr-flashinfer-1695` | upstream-code | [`sources/prs/flashinfer/PR-1695.md`](../sources/prs/flashinfer/PR-1695.md) | [cute_dsl] add gemm + all reduce (two_shot)  |
| `pr-flashinfer-1850` | upstream-code | [`sources/prs/flashinfer/PR-1850.md`](../sources/prs/flashinfer/PR-1850.md) | Add head_dim=64 for blackwell cutlass fmha implementation |
| `pr-flashinfer-2387` | upstream-code | [`sources/prs/flashinfer/PR-2387.md`](../sources/prs/flashinfer/PR-2387.md) | A Blackwell-optimized version of selective_state_update (mamba) |
| `pr-sglang-3529` | upstream-code | [`sources/prs/sglang/PR-3529.md`](../sources/prs/sglang/PR-3529.md) | integrate blockwise fp8 kernel |
| `pr-sglang-5390` | upstream-code | [`sources/prs/sglang/PR-5390.md`](../sources/prs/sglang/PR-5390.md) | Add Cutlass MLA attention backend |
| `pr-tilelang-1229` | upstream-code | [`sources/prs/tilelang/PR-1229.md`](../sources/prs/tilelang/PR-1229.md) | [WIP] support more dtypes for tcgen05 |
| `pr-tilelang-1323` | upstream-code | [`sources/prs/tilelang/PR-1323.md`](../sources/prs/tilelang/PR-1323.md) | Revert "[WIP] support more dtypes for tcgen05 (#1229)" |
| `pr-tilelang-1327` | upstream-code | [`sources/prs/tilelang/PR-1327.md`](../sources/prs/tilelang/PR-1327.md) | [Enhancement] add more dtype and fix mma.ws for fp16 for tcgen05 |
| `pr-tilelang-1764` | upstream-code | [`sources/prs/tilelang/PR-1764.md`](../sources/prs/tilelang/PR-1764.md) | [Feature] Support tcgen5mma lowering for `.kind::i8` |
| `pr-tilelang-1866` | upstream-code | [`sources/prs/tilelang/PR-1866.md`](../sources/prs/tilelang/PR-1866.md) | [CUDA] Support tcgen5mma gemm ts |
| `pr-tilelang-1882` | upstream-code | [`sources/prs/tilelang/PR-1882.md`](../sources/prs/tilelang/PR-1882.md) | [Feature] 2-SM support for TMA, TMEM and TCGEN5MMA on Blackwell |
| `pr-tilelang-1945` | upstream-code | [`sources/prs/tilelang/PR-1945.md`](../sources/prs/tilelang/PR-1945.md) | [Feature] Block-scaled GEMM support for MXFP8 on Blackwell |
| `pr-tilelang-1949` | upstream-code | [`sources/prs/tilelang/PR-1949.md`](../sources/prs/tilelang/PR-1949.md) | [Refactor] Separate gemm into explicit `wgmma_gemm` and `tcgen05_gemm` functions |
| `pr-tilelang-2003` | upstream-code | [`sources/prs/tilelang/PR-2003.md`](../sources/prs/tilelang/PR-2003.md) | [Transform] Add InjectTcgen05Fence pass |
| `pr-triton-10126` | upstream-code | [`sources/prs/triton/PR-10126.md`](../sources/prs/triton/PR-10126.md) | Do not send f64 dots through tcgen05 |
| `pr-triton-10196` | upstream-code | [`sources/prs/triton/PR-10196.md`](../sources/prs/triton/PR-10196.md) | [MULTICTA] Fix multicast pattern for tcgen05_mma_scaled |
| `pr-vllm-13571` | upstream-code | [`sources/prs/vllm/PR-13571.md`](../sources/prs/vllm/PR-13571.md) | [NVIDIA] Support nvfp4 cutlass gemm |
| `pr-vllm-13798` | upstream-code | [`sources/prs/vllm/PR-13798.md`](../sources/prs/vllm/PR-13798.md) | add cutlass support for blackwell fp8 gemm |
| `pr-vllm-16032` | upstream-code | [`sources/prs/vllm/PR-16032.md`](../sources/prs/vllm/PR-16032.md) | [NVIDIA] Support Cutlass MLA for Blackwell GPUs |
| `pr-vllm-19566` | upstream-code | [`sources/prs/vllm/PR-19566.md`](../sources/prs/vllm/PR-19566.md) | [Perf] Further tunings for SM100 FP8 CUTLASS kernel |
| `pr-vllm-22738` | upstream-code | [`sources/prs/vllm/PR-22738.md`](../sources/prs/vllm/PR-22738.md) | [Bugfix] Fix default enable for CUTLASS MLA on SM100 |
| `pr-vllm-23696` | upstream-code | [`sources/prs/vllm/PR-23696.md`](../sources/prs/vllm/PR-23696.md) | [Kernel][B200] `mxfp4` fused cutlass moe |

<a id="tma"></a>
## tma

231 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `blog-modular-blackwell` | community-note | [`sources/blogs/modular-blackwell-matmul.md`](../sources/blogs/modular-blackwell-matmul.md) | Modular: Matrix Multiplication on Blackwell |
| `contest-flashinfer-track-a` | contest-report | [`sources/contests/flashinfer-mlsys26/track-a-fused-moe.md`](../sources/contests/flashinfer-mlsys26/track-a-fused-moe.md) | FlashInfer MLSys 2026 - Track A: Fused MoE FP8 |
| `contest-flashinfer-track-b` | contest-report | [`sources/contests/flashinfer-mlsys26/track-b-sparse-attention.md`](../sources/contests/flashinfer-mlsys26/track-b-sparse-attention.md) | FlashInfer MLSys 2026 - Track B: DeepSeek V3.2 Sparse Attention |
| `contest-flashinfer-track-c` | contest-report | [`sources/contests/flashinfer-mlsys26/track-c-gated-delta-net.md`](../sources/contests/flashinfer-mlsys26/track-c-gated-delta-net.md) | FlashInfer MLSys 2026 - Track C: Gated Delta Net |
| `contest-gpumode-p2` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-2-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-2-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 2: NVFP4 GEMM |
| `contest-gpumode-p3` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-3-gated-dual-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-3-gated-dual-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 3: Gated Dual GEMM |
| `contest-gpumode-p4` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 4: Grouped GEMM |
| `pr-cccl-cub-5061` | upstream-code | [`sources/prs/cccl-cub/PR-5061.md`](../sources/prs/cccl-cub/PR-5061.md) | Replace CG by TMA copy in bulk copy fallback path |
| `pr-cccl-cub-5414` | upstream-code | [`sources/prs/cccl-cub/PR-5414.md`](../sources/prs/cccl-cub/PR-5414.md) | Move TMA barrier in DeviceTransform into dynamic SMEM |
| `pr-cccl-cub-6329` | upstream-code | [`sources/prs/cccl-cub/PR-6329.md`](../sources/prs/cccl-cub/PR-6329.md) | Improve `cuda::barrier` TMA examples and `elect_one` in `DeviceTransform` |
| `pr-cutlass-1661` | upstream-code | [`sources/prs/cutlass/PR-1661.md`](../sources/prs/cutlass/PR-1661.md) | Skip void-C kernels in the profiler when beta is non zero |
| `pr-cutlass-1795` | upstream-code | [`sources/prs/cutlass/PR-1795.md`](../sources/prs/cutlass/PR-1795.md) | Support for TMA Epilogue for Group Gemm and add pingpong ptr array & Group Gemm |
| `pr-cutlass-1883` | upstream-code | [`sources/prs/cutlass/PR-1883.md`](../sources/prs/cutlass/PR-1883.md) | Improve sm90 mixed dtype kernel |
| `pr-cutlass-1932` | upstream-code | [`sources/prs/cutlass/PR-1932.md`](../sources/prs/cutlass/PR-1932.md) | Blockwise Scaling for FP8 |
| `pr-cutlass-2033` | upstream-code | [`sources/prs/cutlass/PR-2033.md`](../sources/prs/cutlass/PR-2033.md) | [EVT] Add support for Row/Col broadcast PtrArray |
| `pr-cutlass-2037` | upstream-code | [`sources/prs/cutlass/PR-2037.md`](../sources/prs/cutlass/PR-2037.md) | Groupwise scaling along M for FP8 gemm |
| `pr-cutlass-2095` | upstream-code | [`sources/prs/cutlass/PR-2095.md`](../sources/prs/cutlass/PR-2095.md) | Improvements for: Groupwise scaling along M for FP8 gemm |
| `pr-cutlass-2123` | upstream-code | [`sources/prs/cutlass/PR-2123.md`](../sources/prs/cutlass/PR-2123.md) | Hopper Grouped GEMM support for FP8 Accum |
| `pr-cutlass-2130` | upstream-code | [`sources/prs/cutlass/PR-2130.md`](../sources/prs/cutlass/PR-2130.md) | Flash MLA support |
| `pr-cutlass-2134` | upstream-code | [`sources/prs/cutlass/PR-2134.md`](../sources/prs/cutlass/PR-2134.md) | Flash MLA Support - Step 2 |
| `pr-cutlass-2167` | upstream-code | [`sources/prs/cutlass/PR-2167.md`](../sources/prs/cutlass/PR-2167.md) | Fix sm100 gemm wrong static constexpr that breaks compilation on Windows |
| `pr-cutlass-2172` | upstream-code | [`sources/prs/cutlass/PR-2172.md`](../sources/prs/cutlass/PR-2172.md) | Fix SM90 beta=1 hang and stream-K launch errors |
| `pr-cutlass-2270` | upstream-code | [`sources/prs/cutlass/PR-2270.md`](../sources/prs/cutlass/PR-2270.md) | hopper-blockwise-generalization-optimization |
| `pr-cutlass-2366` | upstream-code | [`sources/prs/cutlass/PR-2366.md`](../sources/prs/cutlass/PR-2366.md) | [ex77] fix mla split; add fwd lse; add bwd varlen |
| `pr-cutlass-2466` | upstream-code | [`sources/prs/cutlass/PR-2466.md`](../sources/prs/cutlass/PR-2466.md) | Example 77 add blackwell fmha bwd for MLA shape |
| `pr-cutlass-2472` | upstream-code | [`sources/prs/cutlass/PR-2472.md`](../sources/prs/cutlass/PR-2472.md) | Add Blackwell MLA forward (shape: d=192, dv=128) implementation |
| `pr-cutlass-2492` | upstream-code | [`sources/prs/cutlass/PR-2492.md`](../sources/prs/cutlass/PR-2492.md) | fix: examples/cute/tutorial/blackwell/04_mma_tma_2sm_sm100.cu GridDim miscalculated |
| `pr-cutlass-2719` | upstream-code | [`sources/prs/cutlass/PR-2719.md`](../sources/prs/cutlass/PR-2719.md) | Support PDL for SM90 Array TMA GEMM |
| `pr-cutlass-2790` | upstream-code | [`sources/prs/cutlass/PR-2790.md`](../sources/prs/cutlass/PR-2790.md) | Blockscaled Ragged Contiguous Grouped Gemm for MoEs |
| `pr-cutlass-2865` | upstream-code | [`sources/prs/cutlass/PR-2865.md`](../sources/prs/cutlass/PR-2865.md) | [Bug Fix]Bypass launch grids for SM120 Kernel with SM90 Mainloop & SM100 TileScheduler |
| `pr-cutlass-2881` | upstream-code | [`sources/prs/cutlass/PR-2881.md`](../sources/prs/cutlass/PR-2881.md) | new example with TMA prefetch feature targeting for DRAM latency boun… |
| `pr-cutlass-2965` | upstream-code | [`sources/prs/cutlass/PR-2965.md`](../sources/prs/cutlass/PR-2965.md) | [Bug Fix]Set NumSplitsM to 1 when TileShapeM < 128 in sm90 fp8 blockwise scaling CollectiveMma |
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
| `pr-flashinfer-1035` | upstream-code | [`sources/prs/flashinfer/PR-1035.md`](../sources/prs/flashinfer/PR-1035.md) | feat: Softmax free sampling |
| `pr-flashinfer-1039` | upstream-code | [`sources/prs/flashinfer/PR-1039.md`](../sources/prs/flashinfer/PR-1039.md) | [nvidia] initial support for blackwell kernels |
| `pr-flashinfer-1071` | upstream-code | [`sources/prs/flashinfer/PR-1071.md`](../sources/prs/flashinfer/PR-1071.md) | bugfix: adding lse output to blackwell fmha kernels |
| `pr-flashinfer-1072` | upstream-code | [`sources/prs/flashinfer/PR-1072.md`](../sources/prs/flashinfer/PR-1072.md) | bugfix: follow user-specified sm_scale for blackwell cutlass fmha |
| `pr-flashinfer-1106` | upstream-code | [`sources/prs/flashinfer/PR-1106.md`](../sources/prs/flashinfer/PR-1106.md) | bugfix: host-precomuted plan function for blackwell fmha |
| `pr-flashinfer-1113` | upstream-code | [`sources/prs/flashinfer/PR-1113.md`](../sources/prs/flashinfer/PR-1113.md) | Add CUTLASS fused moe kernels from TensorRT-LLM. |
| `pr-flashinfer-1153` | upstream-code | [`sources/prs/flashinfer/PR-1153.md`](../sources/prs/flashinfer/PR-1153.md) | feat: Fused temperature online softmax kernel |
| `pr-flashinfer-1170` | upstream-code | [`sources/prs/flashinfer/PR-1170.md`](../sources/prs/flashinfer/PR-1170.md) | feat: logits processor fustion rule for temperature softmax |
| `pr-flashinfer-1178` | upstream-code | [`sources/prs/flashinfer/PR-1178.md`](../sources/prs/flashinfer/PR-1178.md) | bugfix: softmax NaN results caused by large -inf masks |
| `pr-flashinfer-1198` | upstream-code | [`sources/prs/flashinfer/PR-1198.md`](../sources/prs/flashinfer/PR-1198.md) | bugfix: fix blackwell fmha hanging issue for empty kv_len |
| `pr-flashinfer-1212` | upstream-code | [`sources/prs/flashinfer/PR-1212.md`](../sources/prs/flashinfer/PR-1212.md) | feat: trtllm-gen fp8 moe kernels |
| `pr-flashinfer-1294` | upstream-code | [`sources/prs/flashinfer/PR-1294.md`](../sources/prs/flashinfer/PR-1294.md) | Update cutlass fp4 moe kernels |
| `pr-flashinfer-1320` | upstream-code | [`sources/prs/flashinfer/PR-1320.md`](../sources/prs/flashinfer/PR-1320.md) | Add blockwise-scaled FP8 GEMM via TRTLLM-Gen. |
| `pr-flashinfer-1389` | upstream-code | [`sources/prs/flashinfer/PR-1389.md`](../sources/prs/flashinfer/PR-1389.md) | GPT-OSS Support: Add Blackwell MoE mxfp4 implementation from TRTLLM and Attention Sink |
| `pr-flashinfer-1396` | upstream-code | [`sources/prs/flashinfer/PR-1396.md`](../sources/prs/flashinfer/PR-1396.md) | gpt-oss: Add MXFP8 x MXFP4 CUTLASS MOE for SM100 and BF16 x MXFP4 CUTLASS for SM90 + SwigluBias Activation |
| `pr-flashinfer-1446` | upstream-code | [`sources/prs/flashinfer/PR-1446.md`](../sources/prs/flashinfer/PR-1446.md) | Remove getEnvEnablePDL in favor of enable_pdl parameter |
| `pr-flashinfer-1548` | upstream-code | [`sources/prs/flashinfer/PR-1548.md`](../sources/prs/flashinfer/PR-1548.md) | perf: Enable SplitK and fix autotuner for trtllm fp4 fused moe |
| `pr-flashinfer-1596` | upstream-code | [`sources/prs/flashinfer/PR-1596.md`](../sources/prs/flashinfer/PR-1596.md) | bugfix: fix fused-temperature softmax IMA issue |
| `pr-flashinfer-1608` | upstream-code | [`sources/prs/flashinfer/PR-1608.md`](../sources/prs/flashinfer/PR-1608.md) | feat: initial support for SM103, SM110, SM120, SM121 |
| `pr-flashinfer-1668` | upstream-code | [`sources/prs/flashinfer/PR-1668.md`](../sources/prs/flashinfer/PR-1668.md) | TGV GEMM as a BF16 backend alternative to cuBLAS |
| `pr-flashinfer-1681` | upstream-code | [`sources/prs/flashinfer/PR-1681.md`](../sources/prs/flashinfer/PR-1681.md) | perf: improve performance of cutlass fmha |
| `pr-flashinfer-1695` | upstream-code | [`sources/prs/flashinfer/PR-1695.md`](../sources/prs/flashinfer/PR-1695.md) | [cute_dsl] add gemm + all reduce (two_shot)  |
| `pr-flashinfer-1769` | upstream-code | [`sources/prs/flashinfer/PR-1769.md`](../sources/prs/flashinfer/PR-1769.md) | feat: add xqa fp8 mha and fp8 kv cache |
| `pr-flashinfer-1819` | upstream-code | [`sources/prs/flashinfer/PR-1819.md`](../sources/prs/flashinfer/PR-1819.md) | feat:enable fp8 blockscale moe for fused cultass for sm90 |
| `pr-flashinfer-1829` | upstream-code | [`sources/prs/flashinfer/PR-1829.md`](../sources/prs/flashinfer/PR-1829.md) | feat: trtrllm-gen global scaled FP8 GEMMs |
| `pr-flashinfer-1850` | upstream-code | [`sources/prs/flashinfer/PR-1850.md`](../sources/prs/flashinfer/PR-1850.md) | Add head_dim=64 for blackwell cutlass fmha implementation |
| `pr-flashinfer-1878` | upstream-code | [`sources/prs/flashinfer/PR-1878.md`](../sources/prs/flashinfer/PR-1878.md) | Tune kernel compilation parameters for https://github.com/flashinfer-ai/flashinfer/pull/1850  |
| `pr-flashinfer-1955` | upstream-code | [`sources/prs/flashinfer/PR-1955.md`](../sources/prs/flashinfer/PR-1955.md) | Update trtllm-gen fused moe routing kernel and add more kernels |
| `pr-flashinfer-1973` | upstream-code | [`sources/prs/flashinfer/PR-1973.md`](../sources/prs/flashinfer/PR-1973.md) | Feature: Add support for L40 FusedMoE in cutlass path |
| `pr-flashinfer-2020` | upstream-code | [`sources/prs/flashinfer/PR-2020.md`](../sources/prs/flashinfer/PR-2020.md) | update trtllm cutlass moe  |
| `pr-flashinfer-2044` | upstream-code | [`sources/prs/flashinfer/PR-2044.md`](../sources/prs/flashinfer/PR-2044.md) | perf: improve sampling/mask/softmax performance (part 1/2) |
| `pr-flashinfer-2047` | upstream-code | [`sources/prs/flashinfer/PR-2047.md`](../sources/prs/flashinfer/PR-2047.md) | Rebase FP8 SM100 Cutlass FMHA Attention to main (original PR#1238) |
| `pr-flashinfer-2117` | upstream-code | [`sources/prs/flashinfer/PR-2117.md`](../sources/prs/flashinfer/PR-2117.md) | update xqa license |
| `pr-flashinfer-2142` | upstream-code | [`sources/prs/flashinfer/PR-2142.md`](../sources/prs/flashinfer/PR-2142.md) | feat: TRTLLM FMHAv2 backend for ctx attention |
| `pr-flashinfer-2159` | upstream-code | [`sources/prs/flashinfer/PR-2159.md`](../sources/prs/flashinfer/PR-2159.md) | feat: MxInt4 x Bf16 TRT-LLM Gen MoE support |
| `pr-flashinfer-2235` | upstream-code | [`sources/prs/flashinfer/PR-2235.md`](../sources/prs/flashinfer/PR-2235.md) | refactor: pull trtllm-gen batch-gemm/gemm headers from artifactory; update tma descriptor shape init |
| `pr-flashinfer-2276` | upstream-code | [`sources/prs/flashinfer/PR-2276.md`](../sources/prs/flashinfer/PR-2276.md) | feat: add GDN Attention |
| `pr-flashinfer-2387` | upstream-code | [`sources/prs/flashinfer/PR-2387.md`](../sources/prs/flashinfer/PR-2387.md) | A Blackwell-optimized version of selective_state_update (mamba) |
| `pr-flashinfer-2416` | upstream-code | [`sources/prs/flashinfer/PR-2416.md`](../sources/prs/flashinfer/PR-2416.md) | feat: update trtllm-gen MoE cubins |
| `pr-flashinfer-2422` | upstream-code | [`sources/prs/flashinfer/PR-2422.md`](../sources/prs/flashinfer/PR-2422.md) | refactor: reduce hopper's gdn prefill compilation time and fix docstring. |
| `pr-flashinfer-2446` | upstream-code | [`sources/prs/flashinfer/PR-2446.md`](../sources/prs/flashinfer/PR-2446.md) | feat: Add TRTLLM fmha_v2 library for SM90 attention with Skip-Softmax  |
| `pr-flashinfer-2477` | upstream-code | [`sources/prs/flashinfer/PR-2477.md`](../sources/prs/flashinfer/PR-2477.md) | feat: Add TRTLLM-Gen Skip-Softmax kernels for prefill and decode |
| `pr-flashinfer-2547` | upstream-code | [`sources/prs/flashinfer/PR-2547.md`](../sources/prs/flashinfer/PR-2547.md) | feat: Enable TRTLLM-Gen Skip-Softmax attention for MLA |
| `pr-flashinfer-2581` | upstream-code | [`sources/prs/flashinfer/PR-2581.md`](../sources/prs/flashinfer/PR-2581.md) | Implement `cutlass_fused_moe` mxfp8 |
| `pr-flashinfer-2630` | upstream-code | [`sources/prs/flashinfer/PR-2630.md`](../sources/prs/flashinfer/PR-2630.md) | Add parallel attention |
| `pr-flashinfer-2653` | upstream-code | [`sources/prs/flashinfer/PR-2653.md`](../sources/prs/flashinfer/PR-2653.md) | [feat] trtllm-gen mxfp8 gemm |
| `pr-flashinfer-2711` | upstream-code | [`sources/prs/flashinfer/PR-2711.md`](../sources/prs/flashinfer/PR-2711.md) | feat: Add DiT-oriented kernels where Qk (Bmm1) type can be reinterpreted into Int8 or BFloat16 |
| `pr-flashinfer-2726` | upstream-code | [`sources/prs/flashinfer/PR-2726.md`](../sources/prs/flashinfer/PR-2726.md) | Added missing padding |
| `pr-flashinfer-2740` | upstream-code | [`sources/prs/flashinfer/PR-2740.md`](../sources/prs/flashinfer/PR-2740.md) | misc: Update gemm/batched gemm cubins from trtllm-gen, gemm header refactor |
| `pr-flashinfer-2798` | upstream-code | [`sources/prs/flashinfer/PR-2798.md`](../sources/prs/flashinfer/PR-2798.md) | Upgrade cutlass 4.2.1 -> 4.4.2 |
| `pr-flashinfer-2799` | upstream-code | [`sources/prs/flashinfer/PR-2799.md`](../sources/prs/flashinfer/PR-2799.md) | [fmha-v2] Support HND and NHD paged KV cache layouts with conditional stride handling |
| `pr-flashinfer-2805` | upstream-code | [`sources/prs/flashinfer/PR-2805.md`](../sources/prs/flashinfer/PR-2805.md) | [CuTe DSL] Add modular FMHA prefill and MLA decode attention kernels |
| `pr-flashinfer-2841` | upstream-code | [`sources/prs/flashinfer/PR-2841.md`](../sources/prs/flashinfer/PR-2841.md) | [Perf] Add FMHAv2 to flashinfer_benchmark.py and eliminate unnecessary H2D |
| `pr-flashinfer-2908` | upstream-code | [`sources/prs/flashinfer/PR-2908.md`](../sources/prs/flashinfer/PR-2908.md) | feat(gdn): state checkpointing in chunk_gated_delta_rule |
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
| `pr-pytorch-157241` | upstream-code | [`sources/prs/pytorch/PR-157241.md`](../sources/prs/pytorch/PR-157241.md) | [user triton] AOT inductor support for device-side TMA |
| `pr-quack-100` | upstream-code | [`sources/prs/quack/PR-100.md`](../sources/prs/quack/PR-100.md) | Autotune between tma gather and cp.async in SM100 |
| `pr-quack-126` | upstream-code | [`sources/prs/quack/PR-126.md`](../sources/prs/quack/PR-126.md) | feat: add `weight` to cross entropy |
| `pr-quack-132` | upstream-code | [`sources/prs/quack/PR-132.md`](../sources/prs/quack/PR-132.md) | RMS Norm Bwd: Optimize for GB200 w/ TMA loads, reload_x, separate output dtype, new launch configs |
| `pr-quack-96` | upstream-code | [`sources/prs/quack/PR-96.md`](../sources/prs/quack/PR-96.md) | Add SM120 (consumer Blackwell) support |
| `pr-sglang-13969` | upstream-code | [`sources/prs/sglang/PR-13969.md`](../sources/prs/sglang/PR-13969.md) | [kernel][moe] add moe topk fast |
| `pr-sglang-17353` | upstream-code | [`sources/prs/sglang/PR-17353.md`](../sources/prs/sglang/PR-17353.md) | Move fa4 from sgl-kernel to jit kernel |
| `pr-sglang-19089` | upstream-code | [`sources/prs/sglang/PR-19089.md`](../sources/prs/sglang/PR-19089.md) | Support skip-softmax attention |
| `pr-sglang-20501` | upstream-code | [`sources/prs/sglang/PR-20501.md`](../sources/prs/sglang/PR-20501.md) | [Kernel] Fuse temperature + softmax in sampling for decode speedup |
| `pr-sglang-23965` | upstream-code | [`sources/prs/sglang/PR-23965.md`](../sources/prs/sglang/PR-23965.md) | Enable PDL for various kernels in DSV32/GLM5 |
| `pr-sglang-3216` | upstream-code | [`sources/prs/sglang/PR-3216.md`](../sources/prs/sglang/PR-3216.md) | add tensorrt_llm common and cutlass_extensions as 3rdparty |
| `pr-sglang-3267` | upstream-code | [`sources/prs/sglang/PR-3267.md`](../sources/prs/sglang/PR-3267.md) | support blockwise fp8 matmul kernel |
| `pr-sglang-3529` | upstream-code | [`sources/prs/sglang/PR-3529.md`](../sources/prs/sglang/PR-3529.md) | integrate blockwise fp8 kernel |
| `pr-sglang-4165` | upstream-code | [`sources/prs/sglang/PR-4165.md`](../sources/prs/sglang/PR-4165.md) | DeepGemm integrate to sgl-kernel |
| `pr-sglang-4515` | upstream-code | [`sources/prs/sglang/PR-4515.md`](../sources/prs/sglang/PR-4515.md) | Create col-major and tma-aligned x_scale for deep_gemm.gemm_fp8_fp8_bf16_nt |
| `pr-sglang-5390` | upstream-code | [`sources/prs/sglang/PR-5390.md`](../sources/prs/sglang/PR-5390.md) | Add Cutlass MLA attention backend |
| `pr-sglang-5432` | upstream-code | [`sources/prs/sglang/PR-5432.md`](../sources/prs/sglang/PR-5432.md) | [perf] introduce deep gemm group_gemm_masked as bmm |
| `pr-sglang-6929` | upstream-code | [`sources/prs/sglang/PR-6929.md`](../sources/prs/sglang/PR-6929.md) | [perf][sgl-kernel] extend cutlass_mla_decode to support num_head < 128 |
| `pr-sglang-7772` | upstream-code | [`sources/prs/sglang/PR-7772.md`](../sources/prs/sglang/PR-7772.md) | [1/n]: add cutlass W4A8 moe kernel for hopper architecture |
| `pr-sglang-8955` | upstream-code | [`sources/prs/sglang/PR-8955.md`](../sources/prs/sglang/PR-8955.md) | [NVIDIA] Fix missing `get_col_major_tma_aligned_tensor` for Blackwell deepgemm in EpMoE |
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
| `pr-tensorrt-llm-13892` | upstream-code | [`sources/prs/tensorrt-llm/PR-13892.md`](../sources/prs/tensorrt-llm/PR-13892.md) | [None][perf] mHC fused_hc kernel optimizations + DS-V4 entry-boundary RMSNorm fold-in |
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
| `pr-vllm-11868` | upstream-code | [`sources/prs/vllm/PR-11868.md`](../sources/prs/vllm/PR-11868.md) | [Kernel] Update `cutlass_scaled_mm` to support 2d group (blockwise) scaling |
| `pr-vllm-12097` | upstream-code | [`sources/prs/vllm/PR-12097.md`](../sources/prs/vllm/PR-12097.md) | Add: Support for Sparse24Bitmask Compressed Models |
| `pr-vllm-13571` | upstream-code | [`sources/prs/vllm/PR-13571.md`](../sources/prs/vllm/PR-13571.md) | [NVIDIA] Support nvfp4 cutlass gemm |
| `pr-vllm-13798` | upstream-code | [`sources/prs/vllm/PR-13798.md`](../sources/prs/vllm/PR-13798.md) | add cutlass support for blackwell fp8 gemm |
| `pr-vllm-14396` | upstream-code | [`sources/prs/vllm/PR-14396.md`](../sources/prs/vllm/PR-14396.md) | [BugFix] Illegal Memory Access in the blockwise cutlass fp8 GEMMs |
| `pr-vllm-15956` | upstream-code | [`sources/prs/vllm/PR-15956.md`](../sources/prs/vllm/PR-15956.md) | Modularize fused experts and integrate PPLX kernels |
| `pr-vllm-16032` | upstream-code | [`sources/prs/vllm/PR-16032.md`](../sources/prs/vllm/PR-16032.md) | [NVIDIA] Support Cutlass MLA for Blackwell GPUs |
| `pr-vllm-17082` | upstream-code | [`sources/prs/vllm/PR-17082.md`](../sources/prs/vllm/PR-17082.md) | Fix `numel()` downcast in vllm/csrc/moe/moe_align_sum_kernels.cu +2 |
| `pr-vllm-19566` | upstream-code | [`sources/prs/vllm/PR-19566.md`](../sources/prs/vllm/PR-19566.md) | [Perf] Further tunings for SM100 FP8 CUTLASS kernel |
| `pr-vllm-19757` | upstream-code | [`sources/prs/vllm/PR-19757.md`](../sources/prs/vllm/PR-19757.md) | [feat]: CUTLASS block scaled group gemm for SM100 |
| `pr-vllm-20769` | upstream-code | [`sources/prs/vllm/PR-20769.md`](../sources/prs/vllm/PR-20769.md) | SM100 Cutlass MLA decode with unrestricted num_heads (< 128) for DeepSeek TP |
| `pr-vllm-23280` | upstream-code | [`sources/prs/vllm/PR-23280.md`](../sources/prs/vllm/PR-23280.md) | [Perf] Use upstream CUTLASS for SM90 Block FP8 kernel |
| `pr-vllm-23696` | upstream-code | [`sources/prs/vllm/PR-23696.md`](../sources/prs/vllm/PR-23696.md) | [Kernel][B200] `mxfp4` fused cutlass moe |
| `pr-vllm-31246` | upstream-code | [`sources/prs/vllm/PR-31246.md`](../sources/prs/vllm/PR-31246.md) | [Kernel] Add topk_sigmoid kernel |
| `pr-vllm-32195` | upstream-code | [`sources/prs/vllm/PR-32195.md`](../sources/prs/vllm/PR-32195.md) | Add TMA support to fused_moe_lora kernel |
| `pr-vllm-32619` | upstream-code | [`sources/prs/vllm/PR-32619.md`](../sources/prs/vllm/PR-32619.md) | [Perf] Create TMA-aligned input scale tensor for DeepGemm on Hopper |
| `pr-vllm-33255` | upstream-code | [`sources/prs/vllm/PR-33255.md`](../sources/prs/vllm/PR-33255.md) | [Bugfix] Fix quant RMS norm fusion for quantization with TMA-aligned scales |
| `pr-vllm-38504` | upstream-code | [`sources/prs/vllm/PR-38504.md`](../sources/prs/vllm/PR-38504.md) | [Kernels][MoE] Fix legacy_routing to use bitmatrix-based routing path |
| `pr-vllm-39391` | upstream-code | [`sources/prs/vllm/PR-39391.md`](../sources/prs/vllm/PR-39391.md) | fix: clamp NaN/Inf in topk_softmax to prevent duplicate expert IDs |

<a id="tmem"></a>
## tmem

37 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `blog-modular-blackwell` | community-note | [`sources/blogs/modular-blackwell-matmul.md`](../sources/blogs/modular-blackwell-matmul.md) | Modular: Matrix Multiplication on Blackwell |
| `contest-flashinfer-track-a` | contest-report | [`sources/contests/flashinfer-mlsys26/track-a-fused-moe.md`](../sources/contests/flashinfer-mlsys26/track-a-fused-moe.md) | FlashInfer MLSys 2026 - Track A: Fused MoE FP8 |
| `contest-flashinfer-track-b` | contest-report | [`sources/contests/flashinfer-mlsys26/track-b-sparse-attention.md`](../sources/contests/flashinfer-mlsys26/track-b-sparse-attention.md) | FlashInfer MLSys 2026 - Track B: DeepSeek V3.2 Sparse Attention |
| `contest-flashinfer-track-c` | contest-report | [`sources/contests/flashinfer-mlsys26/track-c-gated-delta-net.md`](../sources/contests/flashinfer-mlsys26/track-c-gated-delta-net.md) | FlashInfer MLSys 2026 - Track C: Gated Delta Net |
| `contest-gpumode-p2` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-2-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-2-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 2: NVFP4 GEMM |
| `contest-gpumode-p3` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-3-gated-dual-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-3-gated-dual-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 3: Gated Dual GEMM |
| `contest-gpumode-p4` | contest-report | [`sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md`](../sources/contests/gpu-mode-nvfp4/problem-4-grouped-gemm.md) | GPU Mode NVFP4 Hackathon - Problem 4: Grouped GEMM |
| `pr-cutlass-2139` | upstream-code | [`sources/prs/cutlass/PR-2139.md`](../sources/prs/cutlass/PR-2139.md) | Blockwise and Groupwise GEMM for Blackwell and Improvements for Hopper |
| `pr-cutlass-2161` | upstream-code | [`sources/prs/cutlass/PR-2161.md`](../sources/prs/cutlass/PR-2161.md) | Blockwise Improvement and Programmatic Dependent Launch |
| `pr-cutlass-2466` | upstream-code | [`sources/prs/cutlass/PR-2466.md`](../sources/prs/cutlass/PR-2466.md) | Example 77 add blackwell fmha bwd for MLA shape |
| `pr-cutlass-2472` | upstream-code | [`sources/prs/cutlass/PR-2472.md`](../sources/prs/cutlass/PR-2472.md) | Add Blackwell MLA forward (shape: d=192, dv=128) implementation |
| `pr-cutlass-2746` | upstream-code | [`sources/prs/cutlass/PR-2746.md`](../sources/prs/cutlass/PR-2746.md) | Support for GEMM-K=0 for Blackwell Grouped GEMMs |
| `pr-cutlass-2995` | upstream-code | [`sources/prs/cutlass/PR-2995.md`](../sources/prs/cutlass/PR-2995.md) | [CuTeDSL] Fix: SM100 block-scale gemm overlapping accumulator |
| `pr-deepgemm-304` | upstream-code | [`sources/prs/deepgemm/PR-304.md`](../sources/prs/deepgemm/PR-304.md) | [Public release 26/04] Introducing Mega MoE, FP4 Indexer and other features/fixes |
| `pr-flash-attention-2033` | upstream-code | [`sources/prs/flash-attention/PR-2033.md`](../sources/prs/flash-attention/PR-2033.md) | [Cute,Bwd,Sm100] enable deterministic mode for sm100 bwd and fix race conditions |
| `pr-flash-attention-2070` | upstream-code | [`sources/prs/flash-attention/PR-2070.md`](../sources/prs/flash-attention/PR-2070.md) | Add score-mod bwd support  |
| `pr-flash-attention-2108` | upstream-code | [`sources/prs/flash-attention/PR-2108.md`](../sources/prs/flash-attention/PR-2108.md) | [NVIDIA] Enable Jetson Thor FA4 |
| `pr-flashinfer-1668` | upstream-code | [`sources/prs/flashinfer/PR-1668.md`](../sources/prs/flashinfer/PR-1668.md) | TGV GEMM as a BF16 backend alternative to cuBLAS |
| `pr-flashinfer-1681` | upstream-code | [`sources/prs/flashinfer/PR-1681.md`](../sources/prs/flashinfer/PR-1681.md) | perf: improve performance of cutlass fmha |
| `pr-flashinfer-1695` | upstream-code | [`sources/prs/flashinfer/PR-1695.md`](../sources/prs/flashinfer/PR-1695.md) | [cute_dsl] add gemm + all reduce (two_shot)  |
| `pr-flashinfer-1850` | upstream-code | [`sources/prs/flashinfer/PR-1850.md`](../sources/prs/flashinfer/PR-1850.md) | Add head_dim=64 for blackwell cutlass fmha implementation |
| `pr-flashinfer-2387` | upstream-code | [`sources/prs/flashinfer/PR-2387.md`](../sources/prs/flashinfer/PR-2387.md) | A Blackwell-optimized version of selective_state_update (mamba) |
| `pr-flashinfer-2805` | upstream-code | [`sources/prs/flashinfer/PR-2805.md`](../sources/prs/flashinfer/PR-2805.md) | [CuTe DSL] Add modular FMHA prefill and MLA decode attention kernels |
| `pr-sglang-5390` | upstream-code | [`sources/prs/sglang/PR-5390.md`](../sources/prs/sglang/PR-5390.md) | Add Cutlass MLA attention backend |
| `pr-tensorrt-llm-10042` | upstream-code | [`sources/prs/tensorrt-llm/PR-10042.md`](../sources/prs/tensorrt-llm/PR-10042.md) | [None][perf] Add more optimization options for MOE CuteDSL finalized kernel |
| `pr-tensorrt-llm-10043` | upstream-code | [`sources/prs/tensorrt-llm/PR-10043.md`](../sources/prs/tensorrt-llm/PR-10043.md) | [TRTLLM-9992][perf] Enable PDL for CuteDSL kernels and overlap MoeOutputMemset |
| `pr-tensorrt-llm-10088` | upstream-code | [`sources/prs/tensorrt-llm/PR-10088.md`](../sources/prs/tensorrt-llm/PR-10088.md) | [None][feat] CuteDSL MOE FC1 Enhancement |
| `pr-tensorrt-llm-10201` | upstream-code | [`sources/prs/tensorrt-llm/PR-10201.md`](../sources/prs/tensorrt-llm/PR-10201.md) | [TRTLLM-9831][perf] Enable 2CTA with autotune for CuteDSL MoE and Grouped GEMM optimizations |
| `pr-tilelang-1866` | upstream-code | [`sources/prs/tilelang/PR-1866.md`](../sources/prs/tilelang/PR-1866.md) | [CUDA] Support tcgen5mma gemm ts |
| `pr-tilelang-1882` | upstream-code | [`sources/prs/tilelang/PR-1882.md`](../sources/prs/tilelang/PR-1882.md) | [Feature] 2-SM support for TMA, TMEM and TCGEN5MMA on Blackwell |
| `pr-tilelang-1971` | upstream-code | [`sources/prs/tilelang/PR-1971.md`](../sources/prs/tilelang/PR-1971.md) | Introduce T.deallocate_tmem and T.transpose |
| `pr-tilelang-2003` | upstream-code | [`sources/prs/tilelang/PR-2003.md`](../sources/prs/tilelang/PR-2003.md) | [Transform] Add InjectTcgen05Fence pass |
| `pr-tilelang-2152` | upstream-code | [`sources/prs/tilelang/PR-2152.md`](../sources/prs/tilelang/PR-2152.md) | [docs] fix TMEM description |
| `pr-triton-10231` | upstream-code | [`sources/prs/triton/PR-10231.md`](../sources/prs/triton/PR-10231.md) | [rel/3.7] Cherry pick "Sink tmem allocs after pipelining to reduce liveranges (#9093)" |
| `pr-triton-10308` | upstream-code | [`sources/prs/triton/PR-10308.md`](../sources/prs/triton/PR-10308.md) | [CONSAN] Add smem and tmem initialization to NaN |
| `pr-vllm-16032` | upstream-code | [`sources/prs/vllm/PR-16032.md`](../sources/prs/vllm/PR-16032.md) | [NVIDIA] Support Cutlass MLA for Blackwell GPUs |
| `pr-vllm-22738` | upstream-code | [`sources/prs/vllm/PR-22738.md`](../sources/prs/vllm/PR-22738.md) | [Bugfix] Fix default enable for CUTLASS MLA on SM100 |

<a id="wgmma"></a>
## wgmma

19 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-cutlass-1932` | upstream-code | [`sources/prs/cutlass/PR-1932.md`](../sources/prs/cutlass/PR-1932.md) | Blockwise Scaling for FP8 |
| `pr-flash-attention-1361` | upstream-code | [`sources/prs/flash-attention/PR-1361.md`](../sources/prs/flash-attention/PR-1361.md) | Fix FA3 Varlen Performance regression |
| `pr-flash-attention-2329` | upstream-code | [`sources/prs/flash-attention/PR-2329.md`](../sources/prs/flash-attention/PR-2329.md) | SM120 forward pass (Blackwell GeForce / DGX Spark) |
| `pr-flash-attention-2332` | upstream-code | [`sources/prs/flash-attention/PR-2332.md`](../sources/prs/flash-attention/PR-2332.md) | [cutlass] Allow compilation of cutlass FA3 for sm100 via enable_sm90 |
| `pr-flash-attention-2365` | upstream-code | [`sources/prs/flash-attention/PR-2365.md`](../sources/prs/flash-attention/PR-2365.md) | [Sm90] Fix test_mask_mod and bwd block-sparse kwarg mismatch |
| `pr-sglang-3056` | upstream-code | [`sources/prs/sglang/PR-3056.md`](../sources/prs/sglang/PR-3056.md) | feat: integrate bmm_fp8 kernel into sgl-kernel |
| `pr-sglang-3529` | upstream-code | [`sources/prs/sglang/PR-3529.md`](../sources/prs/sglang/PR-3529.md) | integrate blockwise fp8 kernel |
| `pr-sglang-4165` | upstream-code | [`sources/prs/sglang/PR-4165.md`](../sources/prs/sglang/PR-4165.md) | DeepGemm integrate to sgl-kernel |
| `pr-sglang-5432` | upstream-code | [`sources/prs/sglang/PR-5432.md`](../sources/prs/sglang/PR-5432.md) | [perf] introduce deep gemm group_gemm_masked as bmm |
| `pr-tilelang-1736` | upstream-code | [`sources/prs/tilelang/PR-1736.md`](../sources/prs/tilelang/PR-1736.md) | Add swizzle layout detection and automatic merging for layout conflicts |
| `pr-tilelang-1762` | upstream-code | [`sources/prs/tilelang/PR-1762.md`](../sources/prs/tilelang/PR-1762.md) | [Feature] Hierarchical reduction and warp reduction intrinsics support |
| `pr-tilelang-1840` | upstream-code | [`sources/prs/tilelang/PR-1840.md`](../sources/prs/tilelang/PR-1840.md) | [BugFix] Fix Hopper TMA lowering without warp specialization |
| `pr-tilelang-1845` | upstream-code | [`sources/prs/tilelang/PR-1845.md`](../sources/prs/tilelang/PR-1845.md) | [Enhancement] Optimize templates for half/bfloat16 |
| `pr-tilelang-1874` | upstream-code | [`sources/prs/tilelang/PR-1874.md`](../sources/prs/tilelang/PR-1874.md) | [Feature] Support cluster launch, query, synchronization and barrier operations |
| `pr-tilelang-1909` | upstream-code | [`sources/prs/tilelang/PR-1909.md`](../sources/prs/tilelang/PR-1909.md) | [Feature] Add Producer-Consumer Warp Specialization and T.tma_copy() API |
| `pr-tilelang-1949` | upstream-code | [`sources/prs/tilelang/PR-1949.md`](../sources/prs/tilelang/PR-1949.md) | [Refactor] Separate gemm into explicit `wgmma_gemm` and `tcgen05_gemm` functions |
| `pr-tilelang-2046` | upstream-code | [`sources/prs/tilelang/PR-2046.md`](../sources/prs/tilelang/PR-2046.md) | [Refactor] Remove obsolete RewriteWgmmaSync pass |
| `pr-tilelang-2153` | upstream-code | [`sources/prs/tilelang/PR-2153.md`](../sources/prs/tilelang/PR-2153.md) | [codex] Split GEMM implementations by backend |
| `pr-triton-10112` | upstream-code | [`sources/prs/triton/PR-10112.md`](../sources/prs/triton/PR-10112.md) | [FPSAN] Add support for wgmma in fpsan |
