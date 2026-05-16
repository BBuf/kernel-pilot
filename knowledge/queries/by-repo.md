# Repository Index

<a id="dao-ailabflash-attention"></a>
## Dao-AILab/flash-attention

146 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-flash-attention-1010` | upstream-code | [`sources/prs/flash-attention/PR-1010.md`](../sources/prs/flash-attention/PR-1010.md) | Support AMD ROCm on FlashAttention 2 |
| `pr-flash-attention-1025` | upstream-code | [`sources/prs/flash-attention/PR-1025.md`](../sources/prs/flash-attention/PR-1025.md) | [WIP] First draft for softcapping. |
| `pr-flash-attention-1072` | upstream-code | [`sources/prs/flash-attention/PR-1072.md`](../sources/prs/flash-attention/PR-1072.md) | Add var-seq-len to FA3 fp16 / bf16 fwd |
| `pr-flash-attention-1075` | upstream-code | [`sources/prs/flash-attention/PR-1075.md`](../sources/prs/flash-attention/PR-1075.md) | Changes For FP8  |
| `pr-flash-attention-1100` | upstream-code | [`sources/prs/flash-attention/PR-1100.md`](../sources/prs/flash-attention/PR-1100.md) | Fp8 kernel with "in-kernel" transpose of V in producer |
| `pr-flash-attention-1173` | upstream-code | [`sources/prs/flash-attention/PR-1173.md`](../sources/prs/flash-attention/PR-1173.md) | FA3 FP8 qkv descales + restore max offset for h128 causal + added sync for producer WG |
| `pr-flash-attention-1180` | upstream-code | [`sources/prs/flash-attention/PR-1180.md`](../sources/prs/flash-attention/PR-1180.md) | Add ArchTag to pre/postprocess bwd kernels |
| `pr-flash-attention-1182` | upstream-code | [`sources/prs/flash-attention/PR-1182.md`](../sources/prs/flash-attention/PR-1182.md) | Add seqused_q in fwd / bwd and seqused_k in bwd in hopper FA. |
| `pr-flash-attention-1203` | upstream-code | [`sources/prs/flash-attention/PR-1203.md`](../sources/prs/flash-attention/PR-1203.md) | [AMD] Triton Backend for ROCm |
| `pr-flash-attention-1233` | upstream-code | [`sources/prs/flash-attention/PR-1233.md`](../sources/prs/flash-attention/PR-1233.md) | Add local attention in Hopper FAv3 |
| `pr-flash-attention-1236` | upstream-code | [`sources/prs/flash-attention/PR-1236.md`](../sources/prs/flash-attention/PR-1236.md) | FA3 kvcache + split kv + gqa parallelization |
| `pr-flash-attention-1268` | upstream-code | [`sources/prs/flash-attention/PR-1268.md`](../sources/prs/flash-attention/PR-1268.md) | Paged Attention support for FA3 |
| `pr-flash-attention-1331` | upstream-code | [`sources/prs/flash-attention/PR-1331.md`](../sources/prs/flash-attention/PR-1331.md) | FA3 paged attention: Readiness for Cutlass 3.6 / default value for block_table |
| `pr-flash-attention-1361` | upstream-code | [`sources/prs/flash-attention/PR-1361.md`](../sources/prs/flash-attention/PR-1361.md) | Fix FA3 Varlen Performance regression |
| `pr-flash-attention-1393` | upstream-code | [`sources/prs/flash-attention/PR-1393.md`](../sources/prs/flash-attention/PR-1393.md) | Add hipBLAS/cuBLAS distinction in benchmark_gemm.py |
| `pr-flash-attention-1427` | upstream-code | [`sources/prs/flash-attention/PR-1427.md`](../sources/prs/flash-attention/PR-1427.md) | Generalize cuda version checks for A100 and above |
| `pr-flash-attention-1511` | upstream-code | [`sources/prs/flash-attention/PR-1511.md`](../sources/prs/flash-attention/PR-1511.md) | Fix CUDA 12.1 build |
| `pr-flash-attention-1603` | upstream-code | [`sources/prs/flash-attention/PR-1603.md`](../sources/prs/flash-attention/PR-1603.md) | add sm_margin for hopper flash_attn_qkvpacked_func |
| `pr-flash-attention-1604` | upstream-code | [`sources/prs/flash-attention/PR-1604.md`](../sources/prs/flash-attention/PR-1604.md) | Support hdimQK != hdimV backward |
| `pr-flash-attention-1610` | upstream-code | [`sources/prs/flash-attention/PR-1610.md`](../sources/prs/flash-attention/PR-1610.md) | [AMD] Triton Backend for ROCm #2 |
| `pr-flash-attention-1674` | upstream-code | [`sources/prs/flash-attention/PR-1674.md`](../sources/prs/flash-attention/PR-1674.md) | [BE] use more minimal torch headers for hopper/flash_api.cpp |
| `pr-flash-attention-1698` | upstream-code | [`sources/prs/flash-attention/PR-1698.md`](../sources/prs/flash-attention/PR-1698.md) | [fa3] Some fixes for windows build |
| `pr-flash-attention-1723` | upstream-code | [`sources/prs/flash-attention/PR-1723.md`](../sources/prs/flash-attention/PR-1723.md) | Fix(hopper): Correct C++ syntax in epilogue_fwd.hpp |
| `pr-flash-attention-1769` | upstream-code | [`sources/prs/flash-attention/PR-1769.md`](../sources/prs/flash-attention/PR-1769.md) | Add torch.compile support to flash attention 3 |
| `pr-flash-attention-1791` | upstream-code | [`sources/prs/flash-attention/PR-1791.md`](../sources/prs/flash-attention/PR-1791.md) | ABI stable fa3 |
| `pr-flash-attention-1823` | upstream-code | [`sources/prs/flash-attention/PR-1823.md`](../sources/prs/flash-attention/PR-1823.md) | Add sorting and head swizzle to varlen scheduler |
| `pr-flash-attention-1840` | upstream-code | [`sources/prs/flash-attention/PR-1840.md`](../sources/prs/flash-attention/PR-1840.md) | Refactors to enable FlexAttention |
| `pr-flash-attention-1856` | upstream-code | [`sources/prs/flash-attention/PR-1856.md`](../sources/prs/flash-attention/PR-1856.md) | [BugFix] fix flash_fwd.FlashAttentionForwardSm80  bugs |
| `pr-flash-attention-1868` | upstream-code | [`sources/prs/flash-attention/PR-1868.md`](../sources/prs/flash-attention/PR-1868.md) | flash-attn-cute bwd sm90 |
| `pr-flash-attention-1893` | upstream-code | [`sources/prs/flash-attention/PR-1893.md`](../sources/prs/flash-attention/PR-1893.md) | Improve causal backward determinism perf with SPT schedule |
| `pr-flash-attention-1904` | upstream-code | [`sources/prs/flash-attention/PR-1904.md`](../sources/prs/flash-attention/PR-1904.md) | C++11 fix warnings |
| `pr-flash-attention-1924` | upstream-code | [`sources/prs/flash-attention/PR-1924.md`](../sources/prs/flash-attention/PR-1924.md) | Remove self refs in softmax for-loop |
| `pr-flash-attention-1934` | upstream-code | [`sources/prs/flash-attention/PR-1934.md`](../sources/prs/flash-attention/PR-1934.md) | feat: Adding varlen support to cute-dsl sm80 bwd |
| `pr-flash-attention-1940` | upstream-code | [`sources/prs/flash-attention/PR-1940.md`](../sources/prs/flash-attention/PR-1940.md) | [Cute,Fwd,Sm100] Implement SplitKV |
| `pr-flash-attention-1942` | upstream-code | [`sources/prs/flash-attention/PR-1942.md`](../sources/prs/flash-attention/PR-1942.md) | Block Sparsity and Flex Attention mask mod support |
| `pr-flash-attention-1945` | upstream-code | [`sources/prs/flash-attention/PR-1945.md`](../sources/prs/flash-attention/PR-1945.md) | Blackwell FlashAttention-BWD (v1.0) |
| `pr-flash-attention-1970` | upstream-code | [`sources/prs/flash-attention/PR-1970.md`](../sources/prs/flash-attention/PR-1970.md) | BlockSparse Tweaks |
| `pr-flash-attention-1983` | upstream-code | [`sources/prs/flash-attention/PR-1983.md`](../sources/prs/flash-attention/PR-1983.md) | [CuTe DSL] Block sparsity computation kernel |
| `pr-flash-attention-1984` | upstream-code | [`sources/prs/flash-attention/PR-1984.md`](../sources/prs/flash-attention/PR-1984.md) | [Cute] Extract block-sparse utilities from SM80/90 |
| `pr-flash-attention-1985` | upstream-code | [`sources/prs/flash-attention/PR-1985.md`](../sources/prs/flash-attention/PR-1985.md) | [Cute] Block sparse support Sm100 |
| `pr-flash-attention-1993` | upstream-code | [`sources/prs/flash-attention/PR-1993.md`](../sources/prs/flash-attention/PR-1993.md) | [Cute,Fwd,Sm100] Support `q_stage=1` for inference |
| `pr-flash-attention-1999` | upstream-code | [`sources/prs/flash-attention/PR-1999.md`](../sources/prs/flash-attention/PR-1999.md) | [Cute,Fwd,Sm100] Support paged attention |
| `pr-flash-attention-2014` | upstream-code | [`sources/prs/flash-attention/PR-2014.md`](../sources/prs/flash-attention/PR-2014.md) | [Cute,Sm100,Fwd] use correction warps for epi when not using TMA |
| `pr-flash-attention-2025` | upstream-code | [`sources/prs/flash-attention/PR-2025.md`](../sources/prs/flash-attention/PR-2025.md) | Bump pin |
| `pr-flash-attention-2026` | upstream-code | [`sources/prs/flash-attention/PR-2026.md`](../sources/prs/flash-attention/PR-2026.md) | [Cute,Fwd,Sm100] don't pass mask_fn to softmax_step generically |
| `pr-flash-attention-2033` | upstream-code | [`sources/prs/flash-attention/PR-2033.md`](../sources/prs/flash-attention/PR-2033.md) | [Cute,Bwd,Sm100] enable deterministic mode for sm100 bwd and fix race conditions |
| `pr-flash-attention-2042` | upstream-code | [`sources/prs/flash-attention/PR-2042.md`](../sources/prs/flash-attention/PR-2042.md) | [CUTE] Enabling TVM-FFI to reduce cpu overhead |
| `pr-flash-attention-2043` | upstream-code | [`sources/prs/flash-attention/PR-2043.md`](../sources/prs/flash-attention/PR-2043.md) | [Cute,Fwd] Extend score_mod to variable sequence length |
| `pr-flash-attention-2070` | upstream-code | [`sources/prs/flash-attention/PR-2070.md`](../sources/prs/flash-attention/PR-2070.md) | Add score-mod bwd support  |
| `pr-flash-attention-2085` | upstream-code | [`sources/prs/flash-attention/PR-2085.md`](../sources/prs/flash-attention/PR-2085.md) | Add blocksparse support for bwd on blackwell |
| `pr-flash-attention-2091` | upstream-code | [`sources/prs/flash-attention/PR-2091.md`](../sources/prs/flash-attention/PR-2091.md) | Fix IMA in fwd on m boundary |
| `pr-flash-attention-2098` | upstream-code | [`sources/prs/flash-attention/PR-2098.md`](../sources/prs/flash-attention/PR-2098.md) | Add pack-gqa fwd support for sparse impl w/ broadcasted H dim |
| `pr-flash-attention-2100` | upstream-code | [`sources/prs/flash-attention/PR-2100.md`](../sources/prs/flash-attention/PR-2100.md) | [Cute,Fwd] improved block sparsity |
| `pr-flash-attention-2104` | upstream-code | [`sources/prs/flash-attention/PR-2104.md`](../sources/prs/flash-attention/PR-2104.md) | [Cute,Fwd,Sm100] distributed offset calculation for paged KV |
| `pr-flash-attention-2108` | upstream-code | [`sources/prs/flash-attention/PR-2108.md`](../sources/prs/flash-attention/PR-2108.md) | [NVIDIA] Enable Jetson Thor FA4 |
| `pr-flash-attention-2109` | upstream-code | [`sources/prs/flash-attention/PR-2109.md`](../sources/prs/flash-attention/PR-2109.md) | [Cute,Fwd,Sm100] fp8 e4m3 and e5m2 support |
| `pr-flash-attention-2136` | upstream-code | [`sources/prs/flash-attention/PR-2136.md`](../sources/prs/flash-attention/PR-2136.md) | block-sparse backward SM90 |
| `pr-flash-attention-2137` | upstream-code | [`sources/prs/flash-attention/PR-2137.md`](../sources/prs/flash-attention/PR-2137.md) | score-mod backward SM90 |
| `pr-flash-attention-2145` | upstream-code | [`sources/prs/flash-attention/PR-2145.md`](../sources/prs/flash-attention/PR-2145.md) | [CUTE][SM90]Enable pack-gqa with broadcasted maskmods |
| `pr-flash-attention-2150` | upstream-code | [`sources/prs/flash-attention/PR-2150.md`](../sources/prs/flash-attention/PR-2150.md) | [Cute, Bwd, Sm100] Add varlen for sm100 bwd |
| `pr-flash-attention-2158` | upstream-code | [`sources/prs/flash-attention/PR-2158.md`](../sources/prs/flash-attention/PR-2158.md) | [CUTE][SM90] GQA backward non deterministic |
| `pr-flash-attention-2174` | upstream-code | [`sources/prs/flash-attention/PR-2174.md`](../sources/prs/flash-attention/PR-2174.md) | [Cute] update row_max before safe overwrite for online_softmax |
| `pr-flash-attention-2177` | upstream-code | [`sources/prs/flash-attention/PR-2177.md`](../sources/prs/flash-attention/PR-2177.md) | [Cute][Flex] add back in contig |
| `pr-flash-attention-2178` | upstream-code | [`sources/prs/flash-attention/PR-2178.md`](../sources/prs/flash-attention/PR-2178.md) |  [AMD] Triton Backend for ROCm #3 |
| `pr-flash-attention-2180` | upstream-code | [`sources/prs/flash-attention/PR-2180.md`](../sources/prs/flash-attention/PR-2180.md) | [Cute][Flex]Add pack-gqa divmod |
| `pr-flash-attention-2186` | upstream-code | [`sources/prs/flash-attention/PR-2186.md`](../sources/prs/flash-attention/PR-2186.md) | [Cute,Fwd,Sm100] support irregular qhead / kvhead ratios |
| `pr-flash-attention-2189` | upstream-code | [`sources/prs/flash-attention/PR-2189.md`](../sources/prs/flash-attention/PR-2189.md) | [Cute][Flex] Fix expanded tensor bug |
| `pr-flash-attention-2194` | upstream-code | [`sources/prs/flash-attention/PR-2194.md`](../sources/prs/flash-attention/PR-2194.md) | [Cute, SM90] fix fwd varlen Cute implementation bug for H100 |
| `pr-flash-attention-2202` | upstream-code | [`sources/prs/flash-attention/PR-2202.md`](../sources/prs/flash-attention/PR-2202.md) | BWD sm100 2cta |
| `pr-flash-attention-2209` | upstream-code | [`sources/prs/flash-attention/PR-2209.md`](../sources/prs/flash-attention/PR-2209.md) | [Flex][SM100] Replay expand fix on sm100 |
| `pr-flash-attention-2216` | upstream-code | [`sources/prs/flash-attention/PR-2216.md`](../sources/prs/flash-attention/PR-2216.md) | [CUTE]Bump to Cutedsl |
| `pr-flash-attention-2218` | upstream-code | [`sources/prs/flash-attention/PR-2218.md`](../sources/prs/flash-attention/PR-2218.md) | [Ai-assisted] CLC work stealing |
| `pr-flash-attention-2224` | upstream-code | [`sources/prs/flash-attention/PR-2224.md`](../sources/prs/flash-attention/PR-2224.md) | [CuTe,Flex] varlen blocksparsity |
| `pr-flash-attention-2227` | upstream-code | [`sources/prs/flash-attention/PR-2227.md`](../sources/prs/flash-attention/PR-2227.md) | Nicer headdim error message |
| `pr-flash-attention-2230` | upstream-code | [`sources/prs/flash-attention/PR-2230.md`](../sources/prs/flash-attention/PR-2230.md) | [AMD] Migrate to Triton Backend to Aiter |
| `pr-flash-attention-2236` | upstream-code | [`sources/prs/flash-attention/PR-2236.md`](../sources/prs/flash-attention/PR-2236.md) | [Cute,Flex,Fwd] Allow vectorized score_mod definitions |
| `pr-flash-attention-2239` | upstream-code | [`sources/prs/flash-attention/PR-2239.md`](../sources/prs/flash-attention/PR-2239.md) | Add `FLASH_ATTENTION_TRITON_AMD_CONFIG_JSON` env var support |
| `pr-flash-attention-2242` | upstream-code | [`sources/prs/flash-attention/PR-2242.md`](../sources/prs/flash-attention/PR-2242.md) | Fix Hopper tests |
| `pr-flash-attention-2251` | upstream-code | [`sources/prs/flash-attention/PR-2251.md`](../sources/prs/flash-attention/PR-2251.md) | [Cute] Handle window_size=(-1, -1) for non-local attention |
| `pr-flash-attention-2270` | upstream-code | [`sources/prs/flash-attention/PR-2270.md`](../sources/prs/flash-attention/PR-2270.md) | [Cute,Sm100,Bwd] Add hdim 192 hdimv 128 backward for sm100 |
| `pr-flash-attention-2271` | upstream-code | [`sources/prs/flash-attention/PR-2271.md`](../sources/prs/flash-attention/PR-2271.md) | [cute] Add return_lse |
| `pr-flash-attention-2273` | upstream-code | [`sources/prs/flash-attention/PR-2273.md`](../sources/prs/flash-attention/PR-2273.md) | Correct Cutlass Error Handling |
| `pr-flash-attention-2274` | upstream-code | [`sources/prs/flash-attention/PR-2274.md`](../sources/prs/flash-attention/PR-2274.md) | guard use_2cta_instrs on sm90 |
| `pr-flash-attention-2275` | upstream-code | [`sources/prs/flash-attention/PR-2275.md`](../sources/prs/flash-attention/PR-2275.md) | [CuteDSL][SM90] varlen bwd works |
| `pr-flash-attention-2282` | upstream-code | [`sources/prs/flash-attention/PR-2282.md`](../sources/prs/flash-attention/PR-2282.md) | Add FA4 publishing strategy |
| `pr-flash-attention-2283` | upstream-code | [`sources/prs/flash-attention/PR-2283.md`](../sources/prs/flash-attention/PR-2283.md) | [Cute][Testing] Add fake tensor mode support for compile-only test passes |
| `pr-flash-attention-2292` | upstream-code | [`sources/prs/flash-attention/PR-2292.md`](../sources/prs/flash-attention/PR-2292.md) | Fix sm100 fwd missing tSrQs init regression |
| `pr-flash-attention-2297` | upstream-code | [`sources/prs/flash-attention/PR-2297.md`](../sources/prs/flash-attention/PR-2297.md) | [CuTeDSL][Sm80] basic fix for new api |
| `pr-flash-attention-2298` | upstream-code | [`sources/prs/flash-attention/PR-2298.md`](../sources/prs/flash-attention/PR-2298.md) | [CuTe] Include broadcast dims in backward compile cache keys |
| `pr-flash-attention-2301` | upstream-code | [`sources/prs/flash-attention/PR-2301.md`](../sources/prs/flash-attention/PR-2301.md) | Fix GQA crash in cute FLASH backend: init load_Q before conditional |
| `pr-flash-attention-2303` | upstream-code | [`sources/prs/flash-attention/PR-2303.md`](../sources/prs/flash-attention/PR-2303.md) | [Cute,Fwd,Sm100] fix paged kv |
| `pr-flash-attention-2304` | upstream-code | [`sources/prs/flash-attention/PR-2304.md`](../sources/prs/flash-attention/PR-2304.md) | [Cute][Testing] Add persistent compile cache for cutedsl AOT compilation |
| `pr-flash-attention-2309` | upstream-code | [`sources/prs/flash-attention/PR-2309.md`](../sources/prs/flash-attention/PR-2309.md) | [Fwd,Sm100] Extract named barriers |
| `pr-flash-attention-2313` | upstream-code | [`sources/prs/flash-attention/PR-2313.md`](../sources/prs/flash-attention/PR-2313.md) | [Cute,Sm100] Introduce a flexible lambda-based R2P masking |
| `pr-flash-attention-2329` | upstream-code | [`sources/prs/flash-attention/PR-2329.md`](../sources/prs/flash-attention/PR-2329.md) | SM120 forward pass (Blackwell GeForce / DGX Spark) |
| `pr-flash-attention-2330` | upstream-code | [`sources/prs/flash-attention/PR-2330.md`](../sources/prs/flash-attention/PR-2330.md) | [Bwd,Sm120] Add SM120 backward pass support |
| `pr-flash-attention-2332` | upstream-code | [`sources/prs/flash-attention/PR-2332.md`](../sources/prs/flash-attention/PR-2332.md) | [cutlass] Allow compilation of cutlass FA3 for sm100 via enable_sm90 |
| `pr-flash-attention-2333` | upstream-code | [`sources/prs/flash-attention/PR-2333.md`](../sources/prs/flash-attention/PR-2333.md) | Add SM120 varlen attention support |
| `pr-flash-attention-2335` | upstream-code | [`sources/prs/flash-attention/PR-2335.md`](../sources/prs/flash-attention/PR-2335.md) | [Cute] fix: rename logging module to avoid circular import at building |
| `pr-flash-attention-2337` | upstream-code | [`sources/prs/flash-attention/PR-2337.md`](../sources/prs/flash-attention/PR-2337.md) | BUG: SeqlenInfo.create has a tile parameter that defaults to 128 |
| `pr-flash-attention-2338` | upstream-code | [`sources/prs/flash-attention/PR-2338.md`](../sources/prs/flash-attention/PR-2338.md) | [Fwd,SM100,CuTe] Fix split KV OOM with diff headdim + fix SM100 kwarg mismatch |
| `pr-flash-attention-2341` | upstream-code | [`sources/prs/flash-attention/PR-2341.md`](../sources/prs/flash-attention/PR-2341.md) | [Bwd, SM80] Fix tdKrdS typo |
| `pr-flash-attention-2343` | upstream-code | [`sources/prs/flash-attention/PR-2343.md`](../sources/prs/flash-attention/PR-2343.md) | [ROCm] Auto-detect Triton backend if C++ extension is missing |
| `pr-flash-attention-2360` | upstream-code | [`sources/prs/flash-attention/PR-2360.md`](../sources/prs/flash-attention/PR-2360.md) | [Fwd,Sm90] Add paged KV attention support (tma and cp.async) |
| `pr-flash-attention-2363` | upstream-code | [`sources/prs/flash-attention/PR-2363.md`](../sources/prs/flash-attention/PR-2363.md) | [AMD ROCm] Update ROCm/CK backend to align with latest ComposableKernel API changes |
| `pr-flash-attention-2365` | upstream-code | [`sources/prs/flash-attention/PR-2365.md`](../sources/prs/flash-attention/PR-2365.md) | [Sm90] Fix test_mask_mod and bwd block-sparse kwarg mismatch |
| `pr-flash-attention-2368` | upstream-code | [`sources/prs/flash-attention/PR-2368.md`](../sources/prs/flash-attention/PR-2368.md) | [Cute] fix: FA4 paged attention kv load for DeepSeek (192,128) on SM100 |
| `pr-flash-attention-2369` | upstream-code | [`sources/prs/flash-attention/PR-2369.md`](../sources/prs/flash-attention/PR-2369.md) | [Cute, Testing] Fix aot + tvm-ffi EnvStream related parameter mismatch |
| `pr-flash-attention-2370` | upstream-code | [`sources/prs/flash-attention/PR-2370.md`](../sources/prs/flash-attention/PR-2370.md) | [Cute, Testing] Bump cutedsl to 4.4.2 and remove prior aot cache management workarounds |
| `pr-flash-attention-2385` | upstream-code | [`sources/prs/flash-attention/PR-2385.md`](../sources/prs/flash-attention/PR-2385.md) | [ROCM] Fix windows issues |
| `pr-flash-attention-2388` | upstream-code | [`sources/prs/flash-attention/PR-2388.md`](../sources/prs/flash-attention/PR-2388.md) | fix: use LSE accum strides from params instead of hardcoded ones |
| `pr-flash-attention-2390` | upstream-code | [`sources/prs/flash-attention/PR-2390.md`](../sources/prs/flash-attention/PR-2390.md) | [Cute,Sm100,Bwd] refine bwd swizzle for deterministic |
| `pr-flash-attention-2393` | upstream-code | [`sources/prs/flash-attention/PR-2393.md`](../sources/prs/flash-attention/PR-2393.md) | Add FA4 CI: GitHub Actions workflow with Apptainer on B200 runner |
| `pr-flash-attention-2400` | upstream-code | [`sources/prs/flash-attention/PR-2400.md`](../sources/prs/flash-attention/PR-2400.md) | [AMD ROCm] Update CK and add RDNA 3/4 support |
| `pr-flash-attention-2402` | upstream-code | [`sources/prs/flash-attention/PR-2402.md`](../sources/prs/flash-attention/PR-2402.md) | feat(cute): implement softcap backward pass, correct math formula, and resolve JIT cache bug |
| `pr-flash-attention-2412` | upstream-code | [`sources/prs/flash-attention/PR-2412.md`](../sources/prs/flash-attention/PR-2412.md) | Feat([FA4][CUTE DSL]) Add head_dim=256 support (forward + backward) |
| `pr-flash-attention-2417` | upstream-code | [`sources/prs/flash-attention/PR-2417.md`](../sources/prs/flash-attention/PR-2417.md) | Allow compact block sparse index tensors |
| `pr-flash-attention-2421` | upstream-code | [`sources/prs/flash-attention/PR-2421.md`](../sources/prs/flash-attention/PR-2421.md) | [AMD ROCm] Fix NaN in FMHA BWD when seq_q=0 |
| `pr-flash-attention-2433` | upstream-code | [`sources/prs/flash-attention/PR-2433.md`](../sources/prs/flash-attention/PR-2433.md) | Fix: disable 2-CTA backward mode when block_sparse_tensors is used |
| `pr-flash-attention-2441` | upstream-code | [`sources/prs/flash-attention/PR-2441.md`](../sources/prs/flash-attention/PR-2441.md) | [Cute,Sm100,Fwd] add MLA 64/512 with topk sparsity for MQA 128 heads |
| `pr-flash-attention-2455` | upstream-code | [`sources/prs/flash-attention/PR-2455.md`](../sources/prs/flash-attention/PR-2455.md) | Add CLC scheduler heuristic |
| `pr-flash-attention-2459` | upstream-code | [`sources/prs/flash-attention/PR-2459.md`](../sources/prs/flash-attention/PR-2459.md) | Handle linter for flash mla file |
| `pr-flash-attention-2463` | upstream-code | [`sources/prs/flash-attention/PR-2463.md`](../sources/prs/flash-attention/PR-2463.md) | fix causal calcs |
| `pr-flash-attention-2470` | upstream-code | [`sources/prs/flash-attention/PR-2470.md`](../sources/prs/flash-attention/PR-2470.md) | [Cute,Fwd,Sm100] Fix the crash when seqlen_k=0 |
| `pr-flash-attention-2473` | upstream-code | [`sources/prs/flash-attention/PR-2473.md`](../sources/prs/flash-attention/PR-2473.md) | Expose --pack-gqa and --num-splits in benchmark_attn.py |
| `pr-flash-attention-2481` | upstream-code | [`sources/prs/flash-attention/PR-2481.md`](../sources/prs/flash-attention/PR-2481.md) | [cute,bwd] fix PDL race in bwd_preprocess, which corrupting dpsum on SM90+ |
| `pr-flash-attention-2485` | upstream-code | [`sources/prs/flash-attention/PR-2485.md`](../sources/prs/flash-attention/PR-2485.md) | [CuTe,Flex] Wire up interface for flex autograd support |
| `pr-flash-attention-2487` | upstream-code | [`sources/prs/flash-attention/PR-2487.md`](../sources/prs/flash-attention/PR-2487.md) | [Cute,hd256] Post-merge cleanup: dead code, duplicate imports |
| `pr-flash-attention-2488` | upstream-code | [`sources/prs/flash-attention/PR-2488.md`](../sources/prs/flash-attention/PR-2488.md) | [hd256] Improve forward kernel with exp2 FMA emulation (3% to 9% performance gain) |
| `pr-flash-attention-2489` | upstream-code | [`sources/prs/flash-attention/PR-2489.md`](../sources/prs/flash-attention/PR-2489.md) | [hd256] Add TMA paged KV support to SM100 2CTA forward kernel |
| `pr-flash-attention-2495` | upstream-code | [`sources/prs/flash-attention/PR-2495.md`](../sources/prs/flash-attention/PR-2495.md) | benchmarks/tune_ex2_emu: hd256 sweep support and clock lock/unlock |
| `pr-flash-attention-2496` | upstream-code | [`sources/prs/flash-attention/PR-2496.md`](../sources/prs/flash-attention/PR-2496.md) | [CuTe,Flex] Add score_mod_bwd param to flash_attn_varlen_func |
| `pr-flash-attention-2497` | upstream-code | [`sources/prs/flash-attention/PR-2497.md`](../sources/prs/flash-attention/PR-2497.md) | [FA4][hd256] Backward TMA bulk-store epilogue + LSE/dpsum coalesce |
| `pr-flash-attention-2502` | upstream-code | [`sources/prs/flash-attention/PR-2502.md`](../sources/prs/flash-attention/PR-2502.md) | fix: typos and missing comments in FA4 cute kernel files |
| `pr-flash-attention-2504` | upstream-code | [`sources/prs/flash-attention/PR-2504.md`](../sources/prs/flash-attention/PR-2504.md) | [SM100] Guard gO None in empty-tile correction |
| `pr-flash-attention-2505` | upstream-code | [`sources/prs/flash-attention/PR-2505.md`](../sources/prs/flash-attention/PR-2505.md) | Fix: pass `stream` to SM100 MLA kernel |
| `pr-flash-attention-2506` | upstream-code | [`sources/prs/flash-attention/PR-2506.md`](../sources/prs/flash-attention/PR-2506.md) | [CuTe, Flex] simplify blocksparse interface in flash_attn_func |
| `pr-flash-attention-2510` | upstream-code | [`sources/prs/flash-attention/PR-2510.md`](../sources/prs/flash-attention/PR-2510.md) | [Cute,Bwd,Sm90] Fix determinism for GQA, port Sm100 approach in |
| `pr-flash-attention-2513` | upstream-code | [`sources/prs/flash-attention/PR-2513.md`](../sources/prs/flash-attention/PR-2513.md) | SM90 FA4 QuACK 0.4 Compatibility |
| `pr-flash-attention-2515` | upstream-code | [`sources/prs/flash-attention/PR-2515.md`](../sources/prs/flash-attention/PR-2515.md) | Fix ZeroDivisionError in num_splits_heuristic for empty Q workloads |
| `pr-flash-attention-2543` | upstream-code | [`sources/prs/flash-attention/PR-2543.md`](../sources/prs/flash-attention/PR-2543.md) | [CuTe,Bwd,Sm100] don't disable 2cta due to cuda 12 in bwd |
| `pr-flash-attention-2544` | upstream-code | [`sources/prs/flash-attention/PR-2544.md`](../sources/prs/flash-attention/PR-2544.md) | [CuTe,Bwd] guard softcap for varlen backward |
| `pr-flash-attention-2549` | upstream-code | [`sources/prs/flash-attention/PR-2549.md`](../sources/prs/flash-attention/PR-2549.md) | [Cute,Bwd,Sm100] fix incorrect calculation of n_block global max for bwd deterministic |
| `pr-flash-attention-2550` | upstream-code | [`sources/prs/flash-attention/PR-2550.md`](../sources/prs/flash-attention/PR-2550.md) | fix varlen w/ paging split kv bug |
| `pr-flash-attention-2563` | upstream-code | [`sources/prs/flash-attention/PR-2563.md`](../sources/prs/flash-attention/PR-2563.md) | [Cute, flex, sm90] fix sm90 flex |
| `pr-flash-attention-911` | upstream-code | [`sources/prs/flash-attention/PR-911.md`](../sources/prs/flash-attention/PR-911.md) | Fix spurious re-compilations of `rotary_kernel` |

<a id="dao-ailabquack"></a>
## Dao-AILab/quack

49 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-quack-100` | upstream-code | [`sources/prs/quack/PR-100.md`](../sources/prs/quack/PR-100.md) | Autotune between tma gather and cp.async in SM100 |
| `pr-quack-103` | upstream-code | [`sources/prs/quack/PR-103.md`](../sources/prs/quack/PR-103.md) | Fix gemm_out inplace versus separate out tensor pytorch custom op schema mismatch |
| `pr-quack-104` | upstream-code | [`sources/prs/quack/PR-104.md`](../sources/prs/quack/PR-104.md) | Fix autotuner worker device affinity |
| `pr-quack-107` | upstream-code | [`sources/prs/quack/PR-107.md`](../sources/prs/quack/PR-107.md) | [Gemm] Implement concat_layout |
| `pr-quack-117` | upstream-code | [`sources/prs/quack/PR-117.md`](../sources/prs/quack/PR-117.md) | [Gemm] Add tile_K parameter and enable 2CTA for tile_m=128 |
| `pr-quack-118` | upstream-code | [`sources/prs/quack/PR-118.md`](../sources/prs/quack/PR-118.md) | Add remaining SM120 / RTX 50 support for GEMM epilogues and RMS paths |
| `pr-quack-119` | upstream-code | [`sources/prs/quack/PR-119.md`](../sources/prs/quack/PR-119.md) | ruff benchmarks/ |
| `pr-quack-120` | upstream-code | [`sources/prs/quack/PR-120.md`](../sources/prs/quack/PR-120.md) | Fix ColVecReduce shared-memory staging |
| `pr-quack-123` | upstream-code | [`sources/prs/quack/PR-123.md`](../sources/prs/quack/PR-123.md) | Fix cute dsl arch import |
| `pr-quack-126` | upstream-code | [`sources/prs/quack/PR-126.md`](../sources/prs/quack/PR-126.md) | feat: add `weight` to cross entropy |
| `pr-quack-132` | upstream-code | [`sources/prs/quack/PR-132.md`](../sources/prs/quack/PR-132.md) | RMS Norm Bwd: Optimize for GB200 w/ TMA loads, reload_x, separate output dtype, new launch configs |
| `pr-quack-134` | upstream-code | [`sources/prs/quack/PR-134.md`](../sources/prs/quack/PR-134.md) | [Bug] Tracer |
| `pr-quack-137` | upstream-code | [`sources/prs/quack/PR-137.md`](../sources/prs/quack/PR-137.md) | Fix exception chaining in CuTeDSL ELF patch |
| `pr-quack-16` | upstream-code | [`sources/prs/quack/PR-16.md`](../sources/prs/quack/PR-16.md) | Add RMSNorm support for BF16 and FP16 weights, add unit tests to verify BF16, FP16 weight results for fwd, bwd |
| `pr-quack-19` | upstream-code | [`sources/prs/quack/PR-19.md`](../sources/prs/quack/PR-19.md) | add PyTorch focused benchmarking for quack rmsnorm |
| `pr-quack-20` | upstream-code | [`sources/prs/quack/PR-20.md`](../sources/prs/quack/PR-20.md) | add reduction options to Quack Cross Entropy for PyTorch drop-in usage |
| `pr-quack-27` | upstream-code | [`sources/prs/quack/PR-27.md`](../sources/prs/quack/PR-27.md) | Symmetric alpha * A @ B + beta * C |
| `pr-quack-28` | upstream-code | [`sources/prs/quack/PR-28.md`](../sources/prs/quack/PR-28.md) | Speedup Torch Wrapper for Symm Matmul |
| `pr-quack-29` | upstream-code | [`sources/prs/quack/PR-29.md`](../sources/prs/quack/PR-29.md) | Fix Symmetric Compile Cache |
| `pr-quack-31` | upstream-code | [`sources/prs/quack/PR-31.md`](../sources/prs/quack/PR-31.md) | Add missing default value for `is_scheduler_warp` |
| `pr-quack-32` | upstream-code | [`sources/prs/quack/PR-32.md`](../sources/prs/quack/PR-32.md) | Fix a potential use-def issue in dynamic control flow |
| `pr-quack-33` | upstream-code | [`sources/prs/quack/PR-33.md`](../sources/prs/quack/PR-33.md) | [TORCH_COMPILE] add torch compile support |
| `pr-quack-35` | upstream-code | [`sources/prs/quack/PR-35.md`](../sources/prs/quack/PR-35.md) | Add optional epilogue args |
| `pr-quack-36` | upstream-code | [`sources/prs/quack/PR-36.md`](../sources/prs/quack/PR-36.md) | [GemmSm90]Add varlen_utils and make gemm interface api return shape consistent |
| `pr-quack-46` | upstream-code | [`sources/prs/quack/PR-46.md`](../sources/prs/quack/PR-46.md) | Refactor Symmetric GEMM to be an activation |
| `pr-quack-53` | upstream-code | [`sources/prs/quack/PR-53.md`](../sources/prs/quack/PR-53.md) | Fix gradient computation in RMS PreNorm backward pass |
| `pr-quack-57` | upstream-code | [`sources/prs/quack/PR-57.md`](../sources/prs/quack/PR-57.md) | Swap order of decorators |
| `pr-quack-59` | upstream-code | [`sources/prs/quack/PR-59.md`](../sources/prs/quack/PR-59.md) | Don't write to same tile twice in symmetric gemm |
| `pr-quack-66` | upstream-code | [`sources/prs/quack/PR-66.md`](../sources/prs/quack/PR-66.md) | Fix unroll_full kwarg typo in bitonic_sort |
| `pr-quack-7` | upstream-code | [`sources/prs/quack/PR-7.md`](../sources/prs/quack/PR-7.md) | Add Layernorm example |
| `pr-quack-71` | upstream-code | [`sources/prs/quack/PR-71.md`](../sources/prs/quack/PR-71.md) | Add utils for gated activation  |
| `pr-quack-74` | upstream-code | [`sources/prs/quack/PR-74.md`](../sources/prs/quack/PR-74.md) | Fix gather fusion in SM100 |
| `pr-quack-75` | upstream-code | [`sources/prs/quack/PR-75.md`](../sources/prs/quack/PR-75.md) | Better gemm configs that reduce 80% autotuning time |
| `pr-quack-76` | upstream-code | [`sources/prs/quack/PR-76.md`](../sources/prs/quack/PR-76.md) | Support to only store mPostAct |
| `pr-quack-78` | upstream-code | [`sources/prs/quack/PR-78.md`](../sources/prs/quack/PR-78.md) | new nvvm.fmin signature |
| `pr-quack-79` | upstream-code | [`sources/prs/quack/PR-79.md`](../sources/prs/quack/PR-79.md) | Fix Triangular Scheduler |
| `pr-quack-80` | upstream-code | [`sources/prs/quack/PR-80.md`](../sources/prs/quack/PR-80.md) | CLC should be autotunable in SM100 rather than a fixed argument |
| `pr-quack-81` | upstream-code | [`sources/prs/quack/PR-81.md`](../sources/prs/quack/PR-81.md) | [SM100] fix CLC persistence for varlen-M tile scheduler |
| `pr-quack-82` | upstream-code | [`sources/prs/quack/PR-82.md`](../sources/prs/quack/PR-82.md) | Add stochastic rounding support for GEMM epilogue |
| `pr-quack-83` | upstream-code | [`sources/prs/quack/PR-83.md`](../sources/prs/quack/PR-83.md) | Allow for patching tvm-ffi |
| `pr-quack-84` | upstream-code | [`sources/prs/quack/PR-84.md`](../sources/prs/quack/PR-84.md) | Expand SM100 autotuning space |
| `pr-quack-85` | upstream-code | [`sources/prs/quack/PR-85.md`](../sources/prs/quack/PR-85.md) | Avoid CUDA context initialization at import time |
| `pr-quack-87` | upstream-code | [`sources/prs/quack/PR-87.md`](../sources/prs/quack/PR-87.md) | Optimal Tile Size for Blackwell Symmetric is (256, 256) |
| `pr-quack-94` | upstream-code | [`sources/prs/quack/PR-94.md`](../sources/prs/quack/PR-94.md) | [Gemm] fix sm120 gemm kernel invocation error |
| `pr-quack-95` | upstream-code | [`sources/prs/quack/PR-95.md`](../sources/prs/quack/PR-95.md) | [Gemm] Fix `gemm_symmetric` on SM120 + add benchmark |
| `pr-quack-96` | upstream-code | [`sources/prs/quack/PR-96.md`](../sources/prs/quack/PR-96.md) | Add SM120 (consumer Blackwell) support |
| `pr-quack-97` | upstream-code | [`sources/prs/quack/PR-97.md`](../sources/prs/quack/PR-97.md) | [BugFix] Fix `_is_warp_leader` in `TraceContext`  |
| `pr-quack-98` | upstream-code | [`sources/prs/quack/PR-98.md`](../sources/prs/quack/PR-98.md) | Remove asm_dialect=AD_ATT from inline PTX assembly calls |
| `pr-quack-99` | upstream-code | [`sources/prs/quack/PR-99.md`](../sources/prs/quack/PR-99.md) | add _get_mma_inst_tile_k() virtual method to GemmSm100 |

<a id="hazyresearchthunderkittens"></a>
## HazyResearch/ThunderKittens

13 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-thunderkittens-101` | upstream-code | [`sources/prs/thunderkittens/PR-101.md`](../sources/prs/thunderkittens/PR-101.md) | feat(mma): add fp16@fp16->fp32 mma and unit tests |
| `pr-thunderkittens-104` | upstream-code | [`sources/prs/thunderkittens/PR-104.md`](../sources/prs/thunderkittens/PR-104.md) | Fix scaled matmul |
| `pr-thunderkittens-11` | upstream-code | [`sources/prs/thunderkittens/PR-11.md`](../sources/prs/thunderkittens/PR-11.md) | Attention h100 |
| `pr-thunderkittens-112` | upstream-code | [`sources/prs/thunderkittens/PR-112.md`](../sources/prs/thunderkittens/PR-112.md) | Add Ring Attention Kernel |
| `pr-thunderkittens-122` | upstream-code | [`sources/prs/thunderkittens/PR-122.md`](../sources/prs/thunderkittens/PR-122.md) | fix h100 bench interface |
| `pr-thunderkittens-13` | upstream-code | [`sources/prs/thunderkittens/PR-13.md`](../sources/prs/thunderkittens/PR-13.md) | add based upate step |
| `pr-thunderkittens-141` | upstream-code | [`sources/prs/thunderkittens/PR-141.md`](../sources/prs/thunderkittens/PR-141.md) | Zero the initial accumulator before applying `HMMA.16816` |
| `pr-thunderkittens-152` | upstream-code | [`sources/prs/thunderkittens/PR-152.md`](../sources/prs/thunderkittens/PR-152.md) | Educational Hopper Matmul level_07 Warp Specialization Fix |
| `pr-thunderkittens-172` | upstream-code | [`sources/prs/thunderkittens/PR-172.md`](../sources/prs/thunderkittens/PR-172.md) | add educational blackwell series |
| `pr-thunderkittens-18` | upstream-code | [`sources/prs/thunderkittens/PR-18.md`](../sources/prs/thunderkittens/PR-18.md) | Cutlass parity |
| `pr-thunderkittens-28` | upstream-code | [`sources/prs/thunderkittens/PR-28.md`](../sources/prs/thunderkittens/PR-28.md) | [feat] add simple half gemm example |
| `pr-thunderkittens-84` | upstream-code | [`sources/prs/thunderkittens/PR-84.md`](../sources/prs/thunderkittens/PR-84.md) | WIP Blackwell fp8 support |
| `pr-thunderkittens-98` | upstream-code | [`sources/prs/thunderkittens/PR-98.md`](../sources/prs/thunderkittens/PR-98.md) | Performance Parity for H100_mma_ABt and H100_mma Kernels |

<a id="nvidiatensorrt-llm"></a>
## NVIDIA/TensorRT-LLM

180 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-tensorrt-llm-10042` | upstream-code | [`sources/prs/tensorrt-llm/PR-10042.md`](../sources/prs/tensorrt-llm/PR-10042.md) | [None][perf] Add more optimization options for MOE CuteDSL finalized kernel |
| `pr-tensorrt-llm-10043` | upstream-code | [`sources/prs/tensorrt-llm/PR-10043.md`](../sources/prs/tensorrt-llm/PR-10043.md) | [TRTLLM-9992][perf] Enable PDL for CuteDSL kernels and overlap MoeOutputMemset |
| `pr-tensorrt-llm-10088` | upstream-code | [`sources/prs/tensorrt-llm/PR-10088.md`](../sources/prs/tensorrt-llm/PR-10088.md) | [None][feat] CuteDSL MOE FC1 Enhancement |
| `pr-tensorrt-llm-10130` | upstream-code | [`sources/prs/tensorrt-llm/PR-10130.md`](../sources/prs/tensorrt-llm/PR-10130.md) | [TRTLLM-9457][feat] Add cute dsl fp8 gemm for Blackwell |
| `pr-tensorrt-llm-10190` | upstream-code | [`sources/prs/tensorrt-llm/PR-10190.md`](../sources/prs/tensorrt-llm/PR-10190.md) | [None][feat] sm100 weight-only kernel |
| `pr-tensorrt-llm-10201` | upstream-code | [`sources/prs/tensorrt-llm/PR-10201.md`](../sources/prs/tensorrt-llm/PR-10201.md) | [TRTLLM-9831][perf] Enable 2CTA with autotune for CuteDSL MoE and Grouped GEMM optimizations |
| `pr-tensorrt-llm-10226` | upstream-code | [`sources/prs/tensorrt-llm/PR-10226.md`](../sources/prs/tensorrt-llm/PR-10226.md) | [TRTLLM-9798][feat] Change to use new DeepGEMM MQA sm100 kernel for MTP-3 |
| `pr-tensorrt-llm-10264` | upstream-code | [`sources/prs/tensorrt-llm/PR-10264.md`](../sources/prs/tensorrt-llm/PR-10264.md) | [TRTLLM-10022][feat] Add hopper xqa decode support for skip softmax attention |
| `pr-tensorrt-llm-10279` | upstream-code | [`sources/prs/tensorrt-llm/PR-10279.md`](../sources/prs/tensorrt-llm/PR-10279.md) | [TRTLLM-10147][perf] Balanced random MoE workload generator for CuteDSL kernel UT, autotuner and layerwise benchmark |
| `pr-tensorrt-llm-10327` | upstream-code | [`sources/prs/tensorrt-llm/PR-10327.md`](../sources/prs/tensorrt-llm/PR-10327.md) | [None][fix] impl fused triton kernel for e8m0 resmooth to reduce memory footprint |
| `pr-tensorrt-llm-10339` | upstream-code | [`sources/prs/tensorrt-llm/PR-10339.md`](../sources/prs/tensorrt-llm/PR-10339.md) | [TRTLLM-9661][chore] Further reduce tuning time for cuteDSL nvFP4 dense gemm. |
| `pr-tensorrt-llm-10429` | upstream-code | [`sources/prs/tensorrt-llm/PR-10429.md`](../sources/prs/tensorrt-llm/PR-10429.md) | [None] [feat] Add test script and raster M for gather fc1 kernel |
| `pr-tensorrt-llm-10476` | upstream-code | [`sources/prs/tensorrt-llm/PR-10476.md`](../sources/prs/tensorrt-llm/PR-10476.md) | [TRTLLM-10276][feat] Integrate cutedsl argmax kernel |
| `pr-tensorrt-llm-10479` | upstream-code | [`sources/prs/tensorrt-llm/PR-10479.md`](../sources/prs/tensorrt-llm/PR-10479.md) | [None] [feat] Add densegemm backend for MoE |
| `pr-tensorrt-llm-10532` | upstream-code | [`sources/prs/tensorrt-llm/PR-10532.md`](../sources/prs/tensorrt-llm/PR-10532.md) | [None][feat] MiniMax M2 support |
| `pr-tensorrt-llm-10742` | upstream-code | [`sources/prs/tensorrt-llm/PR-10742.md`](../sources/prs/tensorrt-llm/PR-10742.md) | [https://nvbugs/5669671][fix] Support GuidedDecoder with sharded logits (pick #10698) |
| `pr-tensorrt-llm-10987` | upstream-code | [`sources/prs/tensorrt-llm/PR-10987.md`](../sources/prs/tensorrt-llm/PR-10987.md) | [TRTLLM-9831][perf] Use TMA.RED to improve effective memory bandwidth |
| `pr-tensorrt-llm-11143` | upstream-code | [`sources/prs/tensorrt-llm/PR-11143.md`](../sources/prs/tensorrt-llm/PR-11143.md) | [None][feat] fuse shared to sparse experts in TRT-LLM Gen MoE |
| `pr-tensorrt-llm-11165` | upstream-code | [`sources/prs/tensorrt-llm/PR-11165.md`](../sources/prs/tensorrt-llm/PR-11165.md) | [https://nvbugs/5799917][fix] Recover from CUTLASS MoE doActivation perf regression for MXFP4/NVFP4 dtype |
| `pr-tensorrt-llm-11181` | upstream-code | [`sources/prs/tensorrt-llm/PR-11181.md`](../sources/prs/tensorrt-llm/PR-11181.md) | [https://nvbugs/5854860][fix] Fix cutedsl argmax on sm120 |
| `pr-tensorrt-llm-11273` | upstream-code | [`sources/prs/tensorrt-llm/PR-11273.md`](../sources/prs/tensorrt-llm/PR-11273.md) | [None][feat] Optimize super-v3 nvfp4 for better perf |
| `pr-tensorrt-llm-11381` | upstream-code | [`sources/prs/tensorrt-llm/PR-11381.md`](../sources/prs/tensorrt-llm/PR-11381.md) | [None][feat] Remove non flash attetnion style fmha_v2 kernel for hopper |
| `pr-tensorrt-llm-11473` | upstream-code | [`sources/prs/tensorrt-llm/PR-11473.md`](../sources/prs/tensorrt-llm/PR-11473.md) | [None][feat] Optimize by fuse nvfp4_quant to layernorm_gated for mamba2_mixer |
| `pr-tensorrt-llm-11501` | upstream-code | [`sources/prs/tensorrt-llm/PR-11501.md`](../sources/prs/tensorrt-llm/PR-11501.md) | [None][feat] TRT-LLM Gen MoE finalize kernel optimization |
| `pr-tensorrt-llm-11510` | upstream-code | [`sources/prs/tensorrt-llm/PR-11510.md`](../sources/prs/tensorrt-llm/PR-11510.md) | [None][feat] Add support for expert_number<=2048 and K<=32 |
| `pr-tensorrt-llm-11589` | upstream-code | [`sources/prs/tensorrt-llm/PR-11589.md`](../sources/prs/tensorrt-llm/PR-11589.md) | [TRTLLM-10004][feat] Enable GEMM -> AR with GEMM output in registered buffers |
| `pr-tensorrt-llm-11652` | upstream-code | [`sources/prs/tensorrt-llm/PR-11652.md`](../sources/prs/tensorrt-llm/PR-11652.md) | [None][feat] NVFP4 TRTLLM-Gen MoE for AutoDeploy (Nemotron Super) |
| `pr-tensorrt-llm-11697` | upstream-code | [`sources/prs/tensorrt-llm/PR-11697.md`](../sources/prs/tensorrt-llm/PR-11697.md) | [TRTLLM-11092][feat] add support for visual gen FA4 attention backend |
| `pr-tensorrt-llm-11718` | upstream-code | [`sources/prs/tensorrt-llm/PR-11718.md`](../sources/prs/tensorrt-llm/PR-11718.md) | [TRTLLM-11119][feat] Blackwell SageAttention, Integrate into AttentionOp API |
| `pr-tensorrt-llm-11733` | upstream-code | [`sources/prs/tensorrt-llm/PR-11733.md`](../sources/prs/tensorrt-llm/PR-11733.md) | [https://nvbugs/5799917][fix] Recover from CUTLASS MoE doActivation perf regression for MXFP4/NVFP4 dtype |
| `pr-tensorrt-llm-11769` | upstream-code | [`sources/prs/tensorrt-llm/PR-11769.md`](../sources/prs/tensorrt-llm/PR-11769.md) | [https://nvbugs/5885070][fix] fix deepeplowlatency with cutedsl moe backend |
| `pr-tensorrt-llm-11774` | upstream-code | [`sources/prs/tensorrt-llm/PR-11774.md`](../sources/prs/tensorrt-llm/PR-11774.md) | [None][fix] Fix SM120 issue for rms_norm with nvfp4_quant_fusion |
| `pr-tensorrt-llm-11869` | upstream-code | [`sources/prs/tensorrt-llm/PR-11869.md`](../sources/prs/tensorrt-llm/PR-11869.md) | [None][feat] Add fused DiT QK Norm + RoPE CUDA kernel for FLUX |
| `pr-tensorrt-llm-11897` | upstream-code | [`sources/prs/tensorrt-llm/PR-11897.md`](../sources/prs/tensorrt-llm/PR-11897.md) | [TRTLLM-10990][feat] Fuse SwiGLU and quant into shared expert |
| `pr-tensorrt-llm-11899` | upstream-code | [`sources/prs/tensorrt-llm/PR-11899.md`](../sources/prs/tensorrt-llm/PR-11899.md) | [TRTLLM-10421][perf] Add fused cat+fp8_quantize CUDA kernel for DSA indexer |
| `pr-tensorrt-llm-11900` | upstream-code | [`sources/prs/tensorrt-llm/PR-11900.md`](../sources/prs/tensorrt-llm/PR-11900.md) | [TRTLLM-10407][feat] Integrate CuTE DSL top-k kernel for Blackwell |
| `pr-tensorrt-llm-11990` | upstream-code | [`sources/prs/tensorrt-llm/PR-11990.md`](../sources/prs/tensorrt-llm/PR-11990.md) | [None][feat] GLM 5 support and DSA MTP fixes |
| `pr-tensorrt-llm-11993` | upstream-code | [`sources/prs/tensorrt-llm/PR-11993.md`](../sources/prs/tensorrt-llm/PR-11993.md) | [#11694][feat] AutoDeploy: Improve the piecewise CG memory usage |
| `pr-tensorrt-llm-12046` | upstream-code | [`sources/prs/tensorrt-llm/PR-12046.md`](../sources/prs/tensorrt-llm/PR-12046.md) | [https://nvbugs/5955188][fix] Fix harmony parsers and WAR routing PDL for agentic coding use cases |
| `pr-tensorrt-llm-12055` | upstream-code | [`sources/prs/tensorrt-llm/PR-12055.md`](../sources/prs/tensorrt-llm/PR-12055.md) | [TRTLLM-11285][feat] Fuse indexer wk + weights_proj into single GEMM in TF32 for DS-V3.2 |
| `pr-tensorrt-llm-12062` | upstream-code | [`sources/prs/tensorrt-llm/PR-12062.md`](../sources/prs/tensorrt-llm/PR-12062.md) | [TRTLLM-11540][feat] Add EAGLE3 dynamic tree speculative decoding support |
| `pr-tensorrt-llm-12074` | upstream-code | [`sources/prs/tensorrt-llm/PR-12074.md`](../sources/prs/tensorrt-llm/PR-12074.md) | [TRTLLM-11289][feat] Integrate CuteDSL's bf16 dense GEMMs |
| `pr-tensorrt-llm-12079` | upstream-code | [`sources/prs/tensorrt-llm/PR-12079.md`](../sources/prs/tensorrt-llm/PR-12079.md) | [None][feat] CuteDSL MOE: Add raster along M/N support for blockscaled contiguous backbone kernel |
| `pr-tensorrt-llm-12136` | upstream-code | [`sources/prs/tensorrt-llm/PR-12136.md`](../sources/prs/tensorrt-llm/PR-12136.md) | [None][feat] Add DWDP (Distributed Weight Data Parallelism) support for MoE inference |
| `pr-tensorrt-llm-12163` | upstream-code | [`sources/prs/tensorrt-llm/PR-12163.md`](../sources/prs/tensorrt-llm/PR-12163.md) | [None][feat] Minimax RMS norm optimization |
| `pr-tensorrt-llm-12201` | upstream-code | [`sources/prs/tensorrt-llm/PR-12201.md`](../sources/prs/tensorrt-llm/PR-12201.md) | [None][feat] Add fused allreduce+RMSNorm op and optional residual in … |
| `pr-tensorrt-llm-12236` | upstream-code | [`sources/prs/tensorrt-llm/PR-12236.md`](../sources/prs/tensorrt-llm/PR-12236.md) | [TRTLLM-10407][perf] Enable CuteDSL indexer_top_k in model |
| `pr-tensorrt-llm-12320` | upstream-code | [`sources/prs/tensorrt-llm/PR-12320.md`](../sources/prs/tensorrt-llm/PR-12320.md) | [None][feat] Support update weight for nvfp4 |
| `pr-tensorrt-llm-12322` | upstream-code | [`sources/prs/tensorrt-llm/PR-12322.md`](../sources/prs/tensorrt-llm/PR-12322.md) | [https://nvbugs/5983390][perf] Kernel fusions in _gather_k_cache_for_chunk of Indexer in DSA |
| `pr-tensorrt-llm-12354` | upstream-code | [`sources/prs/tensorrt-llm/PR-12354.md`](../sources/prs/tensorrt-llm/PR-12354.md) | [TRTLLM-10407][perf] Add cute dsl single pass multi cta cluster topk |
| `pr-tensorrt-llm-12385` | upstream-code | [`sources/prs/tensorrt-llm/PR-12385.md`](../sources/prs/tensorrt-llm/PR-12385.md) | [None][feat] Temporally-Correlated Heuristic-guided Indexer TopK for Sparse Attention |
| `pr-tensorrt-llm-12427` | upstream-code | [`sources/prs/tensorrt-llm/PR-12427.md`](../sources/prs/tensorrt-llm/PR-12427.md) | [None][feat] MLIR-based auto-generated elementwise fusion for AutoDeploy |
| `pr-tensorrt-llm-12440` | upstream-code | [`sources/prs/tensorrt-llm/PR-12440.md`](../sources/prs/tensorrt-llm/PR-12440.md) | [None][feat] Update TRTLLM MoE cubins |
| `pr-tensorrt-llm-12445` | upstream-code | [`sources/prs/tensorrt-llm/PR-12445.md`](../sources/prs/tensorrt-llm/PR-12445.md) | [https://nvbugs/5983390][fix] Remove redundant D2H sync to optimize perf |
| `pr-tensorrt-llm-12456` | upstream-code | [`sources/prs/tensorrt-llm/PR-12456.md`](../sources/prs/tensorrt-llm/PR-12456.md) | [None][perf] add Dynamic SMEM block routing in MOE |
| `pr-tensorrt-llm-12470` | upstream-code | [`sources/prs/tensorrt-llm/PR-12470.md`](../sources/prs/tensorrt-llm/PR-12470.md) | [None][feat] Support sparse mqa/gqa attention |
| `pr-tensorrt-llm-12503` | upstream-code | [`sources/prs/tensorrt-llm/PR-12503.md`](../sources/prs/tensorrt-llm/PR-12503.md) | [https://nvbugs/5983390][perf] Split MLA DSA custom op for piecewise CUDA graph capture |
| `pr-tensorrt-llm-12506` | upstream-code | [`sources/prs/tensorrt-llm/PR-12506.md`](../sources/prs/tensorrt-llm/PR-12506.md) | [None][feat] Add PDL support to CuTE DSL top-k kernels |
| `pr-tensorrt-llm-12507` | upstream-code | [`sources/prs/tensorrt-llm/PR-12507.md`](../sources/prs/tensorrt-llm/PR-12507.md) | [#4674][feat] optimize llama8B decode: trtllm silu_mul backend, quant+silu_mul, QKV passthrough to attention |
| `pr-tensorrt-llm-12519` | upstream-code | [`sources/prs/tensorrt-llm/PR-12519.md`](../sources/prs/tensorrt-llm/PR-12519.md) | [#12634][feat] AutoDeploy: Support rank 256 MLA in flashinfer_mla |
| `pr-tensorrt-llm-12537` | upstream-code | [`sources/prs/tensorrt-llm/PR-12537.md`](../sources/prs/tensorrt-llm/PR-12537.md) | [None][feat] Add Mamba2 MTP SSM cache CUDA kernel for tree-based speculative decoding |
| `pr-tensorrt-llm-12581` | upstream-code | [`sources/prs/tensorrt-llm/PR-12581.md`](../sources/prs/tensorrt-llm/PR-12581.md) | [https://nvbugs/5983390][perf] Multiple host perf optimizations for DSA part |
| `pr-tensorrt-llm-12612` | upstream-code | [`sources/prs/tensorrt-llm/PR-12612.md`](../sources/prs/tensorrt-llm/PR-12612.md) | [None][feat] Trtllm-gen FMHA JIT support |
| `pr-tensorrt-llm-12642` | upstream-code | [`sources/prs/tensorrt-llm/PR-12642.md`](../sources/prs/tensorrt-llm/PR-12642.md) | [None][feat] Add triton paged attention for AutoDeploy |
| `pr-tensorrt-llm-12664` | upstream-code | [`sources/prs/tensorrt-llm/PR-12664.md`](../sources/prs/tensorrt-llm/PR-12664.md) | [None][feat] AutoDeploy: Add the Triton kernel for MLA |
| `pr-tensorrt-llm-12666` | upstream-code | [`sources/prs/tensorrt-llm/PR-12666.md`](../sources/prs/tensorrt-llm/PR-12666.md) | [https://nvbugs/5836828][fix] Fix GPTOSS CUTLASS MOE on Hopper nvlink one-sided workspace overflow |
| `pr-tensorrt-llm-12679` | upstream-code | [`sources/prs/tensorrt-llm/PR-12679.md`](../sources/prs/tensorrt-llm/PR-12679.md) | [None][revert] Revert "[TRTLLM-11119][feat] Blackwell SageAttention, Integrate into … |
| `pr-tensorrt-llm-12731` | upstream-code | [`sources/prs/tensorrt-llm/PR-12731.md`](../sources/prs/tensorrt-llm/PR-12731.md) | [None][feat] Optimize mamba SSD prefill and extend flashinfer dispatch |
| `pr-tensorrt-llm-12738` | upstream-code | [`sources/prs/tensorrt-llm/PR-12738.md`](../sources/prs/tensorrt-llm/PR-12738.md) | [None][feat] Add bf16 trtllm-gen moe support through flashinfer. |
| `pr-tensorrt-llm-12761` | upstream-code | [`sources/prs/tensorrt-llm/PR-12761.md`](../sources/prs/tensorrt-llm/PR-12761.md) | [None][fix] Add missing allow_partial_loading param to CuteDSL and ConfigurableMoE load_weights |
| `pr-tensorrt-llm-12799` | upstream-code | [`sources/prs/tensorrt-llm/PR-12799.md`](../sources/prs/tensorrt-llm/PR-12799.md) | [TRTLLM-11797][feat] Add cutedsl moe backend supporting for qwen3.5. |
| `pr-tensorrt-llm-12831` | upstream-code | [`sources/prs/tensorrt-llm/PR-12831.md`](../sources/prs/tensorrt-llm/PR-12831.md) | [None][feat] Add Claude Code agents and skills for kernel dev, perf analysis, and compilation |
| `pr-tensorrt-llm-12847` | upstream-code | [`sources/prs/tensorrt-llm/PR-12847.md`](../sources/prs/tensorrt-llm/PR-12847.md) | [None][fix] Fix multi_stream_moe accuracy with MLIR and piecewise cudagraphs |
| `pr-tensorrt-llm-12861` | upstream-code | [`sources/prs/tensorrt-llm/PR-12861.md`](../sources/prs/tensorrt-llm/PR-12861.md) | [None][feat] AutoDeploy: Add Gemma4 vision support |
| `pr-tensorrt-llm-12866` | upstream-code | [`sources/prs/tensorrt-llm/PR-12866.md`](../sources/prs/tensorrt-llm/PR-12866.md) | [None][feat] AutoDeploy: Onboard google/gemma-4-31B-it dense model, including nvfp4 |
| `pr-tensorrt-llm-12882` | upstream-code | [`sources/prs/tensorrt-llm/PR-12882.md`](../sources/prs/tensorrt-llm/PR-12882.md) | [TRTLLM-11878][feat] Gen-only sync transfer v2 and manager v2 |
| `pr-tensorrt-llm-12884` | upstream-code | [`sources/prs/tensorrt-llm/PR-12884.md`](../sources/prs/tensorrt-llm/PR-12884.md) | [TRTLLM-11585][feat] Add CUTEDSL moe backend for nemotron-h |
| `pr-tensorrt-llm-12911` | upstream-code | [`sources/prs/tensorrt-llm/PR-12911.md`](../sources/prs/tensorrt-llm/PR-12911.md) | [TRTLLM-11794][feat] Optimize ViT Attention kernel on Nemotron |
| `pr-tensorrt-llm-12929` | upstream-code | [`sources/prs/tensorrt-llm/PR-12929.md`](../sources/prs/tensorrt-llm/PR-12929.md) | [None][fix] Fix moe_chunking_tokens during MoE A2A |
| `pr-tensorrt-llm-12932` | upstream-code | [`sources/prs/tensorrt-llm/PR-12932.md`](../sources/prs/tensorrt-llm/PR-12932.md) | [None][feat] Add Gemma4 multimodal model support (text + vision + audio) |
| `pr-tensorrt-llm-12937` | upstream-code | [`sources/prs/tensorrt-llm/PR-12937.md`](../sources/prs/tensorrt-llm/PR-12937.md) | [TRTLLM-11485][feat] Feature rework: Add SageAttention refreshed kernels (attentionOp only) |
| `pr-tensorrt-llm-12946` | upstream-code | [`sources/prs/tensorrt-llm/PR-12946.md`](../sources/prs/tensorrt-llm/PR-12946.md) | [#12784][feat] AutoDeploy: Optimize DeepSeek-R1 model performance |
| `pr-tensorrt-llm-13033` | upstream-code | [`sources/prs/tensorrt-llm/PR-13033.md`](../sources/prs/tensorrt-llm/PR-13033.md) | [None][feat] Update rms_norm + fp4_qaunt kernel supporting more dim |
| `pr-tensorrt-llm-13052` | upstream-code | [`sources/prs/tensorrt-llm/PR-13052.md`](../sources/prs/tensorrt-llm/PR-13052.md) | [#12716][feat] Fused cross-head QK Norm + RoPE kernel for WAN |
| `pr-tensorrt-llm-13064` | upstream-code | [`sources/prs/tensorrt-llm/PR-13064.md`](../sources/prs/tensorrt-llm/PR-13064.md) | [None][chore] Update flashinfer-python from 0.6.6 to 0.6.8 |
| `pr-tensorrt-llm-13081` | upstream-code | [`sources/prs/tensorrt-llm/PR-13081.md`](../sources/prs/tensorrt-llm/PR-13081.md) | [TRTLLM-11540][feat] Revert revert of EAGLE3 dynamic tree speculative decoding support |
| `pr-tensorrt-llm-13103` | upstream-code | [`sources/prs/tensorrt-llm/PR-13103.md`](../sources/prs/tensorrt-llm/PR-13103.md) | [None][feat] Optimize causal_conv1d prefill and decode kernels |
| `pr-tensorrt-llm-13117` | upstream-code | [`sources/prs/tensorrt-llm/PR-13117.md`](../sources/prs/tensorrt-llm/PR-13117.md) | [None][feat] Add FP4 residual quantization kernel without channel reo… |
| `pr-tensorrt-llm-13120` | upstream-code | [`sources/prs/tensorrt-llm/PR-13120.md`](../sources/prs/tensorrt-llm/PR-13120.md) | [None][bug] fix SM90 full-mask skip-softmax dispatch |
| `pr-tensorrt-llm-13142` | upstream-code | [`sources/prs/tensorrt-llm/PR-13142.md`](../sources/prs/tensorrt-llm/PR-13142.md) | [https://nvbugs/5844149][fix] Fix issues with DSV3.2 perf tests |
| `pr-tensorrt-llm-13149` | upstream-code | [`sources/prs/tensorrt-llm/PR-13149.md`](../sources/prs/tensorrt-llm/PR-13149.md) | [TRTLLM-11958][perf] reduce @torch.library.custom_op host overhead |
| `pr-tensorrt-llm-13157` | upstream-code | [`sources/prs/tensorrt-llm/PR-13157.md`](../sources/prs/tensorrt-llm/PR-13157.md) | [https://nvbugs/6086538][fix] suppress misleading skip-softmax FMHA warning in generation |
| `pr-tensorrt-llm-13160` | upstream-code | [`sources/prs/tensorrt-llm/PR-13160.md`](../sources/prs/tensorrt-llm/PR-13160.md) | [None][chore] improve gemm perf for nemotron in spark |
| `pr-tensorrt-llm-13169` | upstream-code | [`sources/prs/tensorrt-llm/PR-13169.md`](../sources/prs/tensorrt-llm/PR-13169.md) | [https://nvbugs/5945047][fix] Fix cluster launch enablement for SM120 GPUs in allReduce fusion |
| `pr-tensorrt-llm-13176` | upstream-code | [`sources/prs/tensorrt-llm/PR-13176.md`](../sources/prs/tensorrt-llm/PR-13176.md) | [https://nvbugs/6088149][chore] Unwaive perf sanity tests for bug 6088149 |
| `pr-tensorrt-llm-13186` | upstream-code | [`sources/prs/tensorrt-llm/PR-13186.md`](../sources/prs/tensorrt-llm/PR-13186.md) | [None][feat] Update the deepseek routing |
| `pr-tensorrt-llm-13207` | upstream-code | [`sources/prs/tensorrt-llm/PR-13207.md`](../sources/prs/tensorrt-llm/PR-13207.md) | [None][fix] Propagate init_load_balancer to DeepGemmFusedMoE in create_moe_backend |
| `pr-tensorrt-llm-13219` | upstream-code | [`sources/prs/tensorrt-llm/PR-13219.md`](../sources/prs/tensorrt-llm/PR-13219.md) | [TRTLLM-34871][feat] Add cute dsl FP8 paged MQA logits decode kernel |
| `pr-tensorrt-llm-13222` | upstream-code | [`sources/prs/tensorrt-llm/PR-13222.md`](../sources/prs/tensorrt-llm/PR-13222.md) | [#11823][feat] AutoDeploy trtllm_mla attention backend |
| `pr-tensorrt-llm-13268` | upstream-code | [`sources/prs/tensorrt-llm/PR-13268.md`](../sources/prs/tensorrt-llm/PR-13268.md) | [https://nvbugs/6095953][fix] Fix cache memory estimation for Qwen3 hybrid models in trtllm-bench |
| `pr-tensorrt-llm-13294` | upstream-code | [`sources/prs/tensorrt-llm/PR-13294.md`](../sources/prs/tensorrt-llm/PR-13294.md) | [None][fix] Revert "Refactor the routing part in trtllmgen" (#12246) |
| `pr-tensorrt-llm-13328` | upstream-code | [`sources/prs/tensorrt-llm/PR-13328.md`](../sources/prs/tensorrt-llm/PR-13328.md) | [None][feat] Resubmission of the routing refactor in trtllmgen |
| `pr-tensorrt-llm-13340` | upstream-code | [`sources/prs/tensorrt-llm/PR-13340.md`](../sources/prs/tensorrt-llm/PR-13340.md) | [None][feat] Integrate FP4 indexer for DSA on Blackwell |
| `pr-tensorrt-llm-13379` | upstream-code | [`sources/prs/tensorrt-llm/PR-13379.md`](../sources/prs/tensorrt-llm/PR-13379.md) | [https://nvbugs/6098442][fix] WAR IMA on DS V3.2 and update trtllm-gen cubin, lib and src |
| `pr-tensorrt-llm-13384` | upstream-code | [`sources/prs/tensorrt-llm/PR-13384.md`](../sources/prs/tensorrt-llm/PR-13384.md) | [None][feat] Add MegaMoEDeepGemmFusedMoE backend wrapping DeepGEMM fp8_fp4_mega_moe |
| `pr-tensorrt-llm-13410` | upstream-code | [`sources/prs/tensorrt-llm/PR-13410.md`](../sources/prs/tensorrt-llm/PR-13410.md) | [None][fix] Add support for context multiCtaKv sparse fmha |
| `pr-tensorrt-llm-13433` | upstream-code | [`sources/prs/tensorrt-llm/PR-13433.md`](../sources/prs/tensorrt-llm/PR-13433.md) | [None][perf] Extend customMoeRouting kernel to support Qwen3.5 |
| `pr-tensorrt-llm-13452` | upstream-code | [`sources/prs/tensorrt-llm/PR-13452.md`](../sources/prs/tensorrt-llm/PR-13452.md) | [TRTLLM-11285][perf] Force enable TF32 tensor cores for DSA indexer fused GEMM |
| `pr-tensorrt-llm-13453` | upstream-code | [`sources/prs/tensorrt-llm/PR-13453.md`](../sources/prs/tensorrt-llm/PR-13453.md) | [None][feat] Use a replay method for state rollback in Mamba-2 speculative decoding |
| `pr-tensorrt-llm-13454` | upstream-code | [`sources/prs/tensorrt-llm/PR-13454.md`](../sources/prs/tensorrt-llm/PR-13454.md) | [None][fix] Split TRT-LLM-only rope fusion out of standalone auto_deploy |
| `pr-tensorrt-llm-13470` | upstream-code | [`sources/prs/tensorrt-llm/PR-13470.md`](../sources/prs/tensorrt-llm/PR-13470.md) | [https://nvbugs/6017720][fix] Fix moe backend mismatch on Blackwell in perf test. |
| `pr-tensorrt-llm-13477` | upstream-code | [`sources/prs/tensorrt-llm/PR-13477.md`](../sources/prs/tensorrt-llm/PR-13477.md) | [None][perf] Scheme X L2-aware dispatcher and PDL launchers for sparse-attention GVR Top-K |
| `pr-tensorrt-llm-13486` | upstream-code | [`sources/prs/tensorrt-llm/PR-13486.md`](../sources/prs/tensorrt-llm/PR-13486.md) | [None][fix] visual_gen UlyssesAttention: pass post-A2A seq_len to inner backend |
| `pr-tensorrt-llm-13496` | upstream-code | [`sources/prs/tensorrt-llm/PR-13496.md`](../sources/prs/tensorrt-llm/PR-13496.md) | [https://nvbugs/6114727][fix] Unwaive deepseek r1 fp4 v2 grace_blackwell r1 fp4 v2 tep4 mtp3 1k1k |
| `pr-tensorrt-llm-13505` | upstream-code | [`sources/prs/tensorrt-llm/PR-13505.md`](../sources/prs/tensorrt-llm/PR-13505.md) | [None][perf] Drop cubin and Eliminate ~6s FMHA JIT recompile in eager generation by aligning kernel selection with CUDA graph warmup |
| `pr-tensorrt-llm-13541` | upstream-code | [`sources/prs/tensorrt-llm/PR-13541.md`](../sources/prs/tensorrt-llm/PR-13541.md) | [https://nvbugs/6098442][fix] Add fix for IMA with TRTLLM-Gen GmemReductionWithSeparateKernel |
| `pr-tensorrt-llm-13542` | upstream-code | [`sources/prs/tensorrt-llm/PR-13542.md`](../sources/prs/tensorrt-llm/PR-13542.md) | [None][chore] Convert cubins in repository to compressed archives |
| `pr-tensorrt-llm-13570` | upstream-code | [`sources/prs/tensorrt-llm/PR-13570.md`](../sources/prs/tensorrt-llm/PR-13570.md) | [TRTLLM-12128][feat] enable SageAttention for Wan/FLUX (new commits) |
| `pr-tensorrt-llm-13594` | upstream-code | [`sources/prs/tensorrt-llm/PR-13594.md`](../sources/prs/tensorrt-llm/PR-13594.md) | [None][test] Add GB300 DISAGG NIXL CI Perf Test Back |
| `pr-tensorrt-llm-13595` | upstream-code | [`sources/prs/tensorrt-llm/PR-13595.md`](../sources/prs/tensorrt-llm/PR-13595.md) | [None][feat] Enable EPLB for DeepSeek-V4 |
| `pr-tensorrt-llm-13628` | upstream-code | [`sources/prs/tensorrt-llm/PR-13628.md`](../sources/prs/tensorrt-llm/PR-13628.md) | [None][feat] Fuse FP8 1x128 quantize + UE8M0 scale pack on SM100 |
| `pr-tensorrt-llm-13633` | upstream-code | [`sources/prs/tensorrt-llm/PR-13633.md`](../sources/prs/tensorrt-llm/PR-13633.md) | [None][fix] Plumb promptIgnoreLength through Triton backend to fix silently-dropped lengthPenalty and earlyStopping |
| `pr-tensorrt-llm-13646` | upstream-code | [`sources/prs/tensorrt-llm/PR-13646.md`](../sources/prs/tensorrt-llm/PR-13646.md) | [None][perf] Use bf16 custom router GEMM kernel for DeepSeek-V4 |
| `pr-tensorrt-llm-13652` | upstream-code | [`sources/prs/tensorrt-llm/PR-13652.md`](../sources/prs/tensorrt-llm/PR-13652.md) | [None][feat] Add DeepSeekV4 attention kernels |
| `pr-tensorrt-llm-13658` | upstream-code | [`sources/prs/tensorrt-llm/PR-13658.md`](../sources/prs/tensorrt-llm/PR-13658.md) | [None][test] add Nemotron Ultra V3 AutoDeploy accuracy test |
| `pr-tensorrt-llm-13660` | upstream-code | [`sources/prs/tensorrt-llm/PR-13660.md`](../sources/prs/tensorrt-llm/PR-13660.md) | [TRTLLM-12383][fix] limit MHC TF32 pmap GEMM to SM100 |
| `pr-tensorrt-llm-13667` | upstream-code | [`sources/prs/tensorrt-llm/PR-13667.md`](../sources/prs/tensorrt-llm/PR-13667.md) | [None][perf] Improve TRTLLM MoE autotune in DEP |
| `pr-tensorrt-llm-13677` | upstream-code | [`sources/prs/tensorrt-llm/PR-13677.md`](../sources/prs/tensorrt-llm/PR-13677.md) | [#11823][feat] AutoDeploy's mla chunked prefill loop support |
| `pr-tensorrt-llm-13688` | upstream-code | [`sources/prs/tensorrt-llm/PR-13688.md`](../sources/prs/tensorrt-llm/PR-13688.md) | [None][fix] Revert 'Add bf16 trtllm-gen moe support through flashinfer.' |
| `pr-tensorrt-llm-13692` | upstream-code | [`sources/prs/tensorrt-llm/PR-13692.md`](../sources/prs/tensorrt-llm/PR-13692.md) | [None][fix] Fix early_stopping type and plumb through Triton ensemble… |
| `pr-tensorrt-llm-13708` | upstream-code | [`sources/prs/tensorrt-llm/PR-13708.md`](../sources/prs/tensorrt-llm/PR-13708.md) | [https://nvbugs/6094072][fix] swizzle GPT-OSS dummy MXFP4 weights |
| `pr-tensorrt-llm-13714` | upstream-code | [`sources/prs/tensorrt-llm/PR-13714.md`](../sources/prs/tensorrt-llm/PR-13714.md) | [None][docs] add GVR Top-K technical blog |
| `pr-tensorrt-llm-13740` | upstream-code | [`sources/prs/tensorrt-llm/PR-13740.md`](../sources/prs/tensorrt-llm/PR-13740.md) | [https://nvbugs/6108841][fix] add hidden_dim=6144 router GEMM instantiation for GLM-5 |
| `pr-tensorrt-llm-13761` | upstream-code | [`sources/prs/tensorrt-llm/PR-13761.md`](../sources/prs/tensorrt-llm/PR-13761.md) | [None][perf] Optimize DeepSeek-V4 compressor BF16 input |
| `pr-tensorrt-llm-13767` | upstream-code | [`sources/prs/tensorrt-llm/PR-13767.md`](../sources/prs/tensorrt-llm/PR-13767.md) | [None][fix] Plumb swiglu_limit through DeepGEMM and TRTLLMGen FP8 fused MoE |
| `pr-tensorrt-llm-13771` | upstream-code | [`sources/prs/tensorrt-llm/PR-13771.md`](../sources/prs/tensorrt-llm/PR-13771.md) | [None][fix] Fix fused MHC for DeepSeek-V4-Pro hidden size |
| `pr-tensorrt-llm-13802` | upstream-code | [`sources/prs/tensorrt-llm/PR-13802.md`](../sources/prs/tensorrt-llm/PR-13802.md) | [None][fix] Use compressed lengths for DeepSeek-V4 indexer |
| `pr-tensorrt-llm-13808` | upstream-code | [`sources/prs/tensorrt-llm/PR-13808.md`](../sources/prs/tensorrt-llm/PR-13808.md) | [None][feat] Update FMHA cubins for head_dim 80 |
| `pr-tensorrt-llm-13811` | upstream-code | [`sources/prs/tensorrt-llm/PR-13811.md`](../sources/prs/tensorrt-llm/PR-13811.md) | [None][feat] Indexer topk opt |
| `pr-tensorrt-llm-13837` | upstream-code | [`sources/prs/tensorrt-llm/PR-13837.md`](../sources/prs/tensorrt-llm/PR-13837.md) | [None][test] Add func and perf case of nemotron-3-Nano-Omni model on DGX-Spark |
| `pr-tensorrt-llm-13873` | upstream-code | [`sources/prs/tensorrt-llm/PR-13873.md`](../sources/prs/tensorrt-llm/PR-13873.md) | [TRTLLM-12503][feat] Parallel VAE independent scaling and fix arg passing |
| `pr-tensorrt-llm-13892` | upstream-code | [`sources/prs/tensorrt-llm/PR-13892.md`](../sources/prs/tensorrt-llm/PR-13892.md) | [None][perf] mHC fused_hc kernel optimizations + DS-V4 entry-boundary RMSNorm fold-in |
| `pr-tensorrt-llm-13901` | upstream-code | [`sources/prs/tensorrt-llm/PR-13901.md`](../sources/prs/tensorrt-llm/PR-13901.md) | [None][chore] Remove glm_moe_dsa tokenizer WAR after Transformers 5.x upgrade |
| `pr-tensorrt-llm-13908` | upstream-code | [`sources/prs/tensorrt-llm/PR-13908.md`](../sources/prs/tensorrt-llm/PR-13908.md) | [None][refactor] MoEScheduler split + MegaMoE EPLB / multi-chunk / CI integration |
| `pr-tensorrt-llm-13929` | upstream-code | [`sources/prs/tensorrt-llm/PR-13929.md`](../sources/prs/tensorrt-llm/PR-13929.md) | [TRTLLM-35237][feat] Add cute dsl FP4 paged MQA logits decode kernel |
| `pr-tensorrt-llm-13938` | upstream-code | [`sources/prs/tensorrt-llm/PR-13938.md`](../sources/prs/tensorrt-llm/PR-13938.md) | [None][feat] Keep DSv4 o_a_proj as FP8, and port vLLM's fused_inv_rope_fp8_quant |
| `pr-tensorrt-llm-13945` | upstream-code | [`sources/prs/tensorrt-llm/PR-13945.md`](../sources/prs/tensorrt-llm/PR-13945.md) | [https://nvbugs/6100102][fix] Fix cutlass grouped gemm launcher EpilogueScalars construction |
| `pr-tensorrt-llm-13971` | upstream-code | [`sources/prs/tensorrt-llm/PR-13971.md`](../sources/prs/tensorrt-llm/PR-13971.md) | [None][perf] Follow-up patch for "Improve TRTLLM MoE autotune in DEP (#13667)" |
| `pr-tensorrt-llm-13997` | upstream-code | [`sources/prs/tensorrt-llm/PR-13997.md`](../sources/prs/tensorrt-llm/PR-13997.md) | [None][feat] enable TRTLLM-Gen internal routing |
| `pr-tensorrt-llm-14000` | upstream-code | [`sources/prs/tensorrt-llm/PR-14000.md`](../sources/prs/tensorrt-llm/PR-14000.md) | [TRTLLM-12589][fix] Reset MoE A2A dispatch state on warmup OOM |
| `pr-tensorrt-llm-14004` | upstream-code | [`sources/prs/tensorrt-llm/PR-14004.md`](../sources/prs/tensorrt-llm/PR-14004.md) | [None][feat] AutoDeploy re-onboard GPT_OSS |
| `pr-tensorrt-llm-14039` | upstream-code | [`sources/prs/tensorrt-llm/PR-14039.md`](../sources/prs/tensorrt-llm/PR-14039.md) | [#8542][feat] AutoDeploy: add Llama-3.1-8B FP8 perf-sanity test on H100 |
| `pr-tensorrt-llm-14054` | upstream-code | [`sources/prs/tensorrt-llm/PR-14054.md`](../sources/prs/tensorrt-llm/PR-14054.md) | [https://nvbugs/6162323][fix] Make mxfp4 H20 swizzle WAR more robust |
| `pr-tensorrt-llm-14070` | upstream-code | [`sources/prs/tensorrt-llm/PR-14070.md`](../sources/prs/tensorrt-llm/PR-14070.md) | [None][perf] Speed up model init: cache support_nvlink() |
| `pr-tensorrt-llm-14074` | upstream-code | [`sources/prs/tensorrt-llm/PR-14074.md`](../sources/prs/tensorrt-llm/PR-14074.md) | [None][fix] Support DeepSeekV4 routing in perfect-router planner |
| `pr-tensorrt-llm-14106` | upstream-code | [`sources/prs/tensorrt-llm/PR-14106.md`](../sources/prs/tensorrt-llm/PR-14106.md) | [None][fix] Add SPDX Apache-2.0 headers and fix license compliance for llm-c standalone repo |
| `pr-tensorrt-llm-4867` | upstream-code | [`sources/prs/tensorrt-llm/PR-4867.md`](../sources/prs/tensorrt-llm/PR-4867.md) | feat: Add w4a8_mxfp4_fp8 quantization recipe. |
| `pr-tensorrt-llm-6538` | upstream-code | [`sources/prs/tensorrt-llm/PR-6538.md`](../sources/prs/tensorrt-llm/PR-6538.md) | [None][feat] Use Separate QKV Input Layout for Context MLA |
| `pr-tensorrt-llm-6809` | upstream-code | [`sources/prs/tensorrt-llm/PR-6809.md`](../sources/prs/tensorrt-llm/PR-6809.md) | [OMNIML-2336][feat] Add NVFP4 x FP8 |
| `pr-tensorrt-llm-7524` | upstream-code | [`sources/prs/tensorrt-llm/PR-7524.md`](../sources/prs/tensorrt-llm/PR-7524.md) | [None][chore] Fix kernel launch param and add TRTLLM MoE backend test |
| `pr-tensorrt-llm-7755` | upstream-code | [`sources/prs/tensorrt-llm/PR-7755.md`](../sources/prs/tensorrt-llm/PR-7755.md) | [None][fix] Fix and add test for TRTLLM MoE backend |
| `pr-tensorrt-llm-7761` | upstream-code | [`sources/prs/tensorrt-llm/PR-7761.md`](../sources/prs/tensorrt-llm/PR-7761.md) | [TRTLLM-8637][feat] Optimize the routing kernel for DeepseekV3 (MoE CUTLASS backend); Add support for 384 experts (MoE TRTLLM backend) |
| `pr-tensorrt-llm-7937` | upstream-code | [`sources/prs/tensorrt-llm/PR-7937.md`](../sources/prs/tensorrt-llm/PR-7937.md) | [None][feat] GPT-OSS Sm120/Sm121 Support |
| `pr-tensorrt-llm-8405` | upstream-code | [`sources/prs/tensorrt-llm/PR-8405.md`](../sources/prs/tensorrt-llm/PR-8405.md) | [TRTLLM-8535][feat] Support DeepSeek V3.2 with FP8 + BF16 KV cache/NVFP4 + BF16 KV cache |
| `pr-tensorrt-llm-8501` | upstream-code | [`sources/prs/tensorrt-llm/PR-8501.md`](../sources/prs/tensorrt-llm/PR-8501.md) | [None][fix] Fix the performance issue of FP8 blockwise grouped GEMM when using attention DP |
| `pr-tensorrt-llm-8620` | upstream-code | [`sources/prs/tensorrt-llm/PR-8620.md`](../sources/prs/tensorrt-llm/PR-8620.md) | [None][feat] Enable nvfp4 cuda core for sm120 |
| `pr-tensorrt-llm-8675` | upstream-code | [`sources/prs/tensorrt-llm/PR-8675.md`](../sources/prs/tensorrt-llm/PR-8675.md) | [TRTLLM-8827] [feat] Enable low precision alltoall for Cutlass and TRTLLMGen backends |
| `pr-tensorrt-llm-8886` | upstream-code | [`sources/prs/tensorrt-llm/PR-8886.md`](../sources/prs/tensorrt-llm/PR-8886.md) | [None][feat] Enable EPLB for trtllm-gen and cutlass backend |
| `pr-tensorrt-llm-9025` | upstream-code | [`sources/prs/tensorrt-llm/PR-9025.md`](../sources/prs/tensorrt-llm/PR-9025.md) | [None][feat] Update TRTLLM MoE cubins; reduce mxfp4 weight padding requirement; tighten TMA bound |
| `pr-tensorrt-llm-9087` | upstream-code | [`sources/prs/tensorrt-llm/PR-9087.md`](../sources/prs/tensorrt-llm/PR-9087.md) | [None][fix] support topk autotuner input for expert slot per group larger than 32 |
| `pr-tensorrt-llm-9175` | upstream-code | [`sources/prs/tensorrt-llm/PR-9175.md`](../sources/prs/tensorrt-llm/PR-9175.md) | [None][feat] TRT-LLM Gen MoE optimize DeepSeek Fp8 activation kernel |
| `pr-tensorrt-llm-9486` | upstream-code | [`sources/prs/tensorrt-llm/PR-9486.md`](../sources/prs/tensorrt-llm/PR-9486.md) | [TRTLLM-8958][feat] and [TRTLLM-8960]: create ConfigurableMoE and support TRTLLMGenFusedMoE as backend |
| `pr-tensorrt-llm-9618` | upstream-code | [`sources/prs/tensorrt-llm/PR-9618.md`](../sources/prs/tensorrt-llm/PR-9618.md) | [TRTLLM-9685] [feat] Add gather fc1 kernel by cuteDSL |
| `pr-tensorrt-llm-9729` | upstream-code | [`sources/prs/tensorrt-llm/PR-9729.md`](../sources/prs/tensorrt-llm/PR-9729.md) | [None][feat] add fp4 gemm + allreduce |
| `pr-tensorrt-llm-9811` | upstream-code | [`sources/prs/tensorrt-llm/PR-9811.md`](../sources/prs/tensorrt-llm/PR-9811.md) | [None][feat] spark cublas LUT table for llama-8b-bf16 perf |
| `pr-tensorrt-llm-9838` | upstream-code | [`sources/prs/tensorrt-llm/PR-9838.md`](../sources/prs/tensorrt-llm/PR-9838.md) | [https://nvbugs/5726962][feat] Apply fusion for W4AFP8_AWQ MoE |
| `pr-tensorrt-llm-9852` | upstream-code | [`sources/prs/tensorrt-llm/PR-9852.md`](../sources/prs/tensorrt-llm/PR-9852.md) | [None][feat] Fused kernels (qknormrope + moe routing) and two-model MTP support for glm4moe |
| `pr-tensorrt-llm-9854` | upstream-code | [`sources/prs/tensorrt-llm/PR-9854.md`](../sources/prs/tensorrt-llm/PR-9854.md) | [None][feat] Port fp4 quantization kernel optimization from FlashInfer |
| `pr-tensorrt-llm-9905` | upstream-code | [`sources/prs/tensorrt-llm/PR-9905.md`](../sources/prs/tensorrt-llm/PR-9905.md) | [None][feat] Adding torch ext API for FusedAddRMSNormQuant kernel |
| `pr-tensorrt-llm-9924` | upstream-code | [`sources/prs/tensorrt-llm/PR-9924.md`](../sources/prs/tensorrt-llm/PR-9924.md) | [TRTLLM-9493][feat] Add helixPostProcessNative kernel for cp_dim=2 |

<a id="nvidiacccl"></a>
## NVIDIA/cccl

228 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-cccl-cub-1973` | upstream-code | [`sources/prs/cccl-cub/PR-1973.md`](../sources/prs/cccl-cub/PR-1973.md) | Experimental Python cooperative algorithms |
| `pr-cccl-cub-2944` | upstream-code | [`sources/prs/cccl-cub/PR-2944.md`](../sources/prs/cccl-cub/PR-2944.md) | fix thread-reduce performance regression |
| `pr-cccl-cub-3218` | upstream-code | [`sources/prs/cccl-cub/PR-3218.md`](../sources/prs/cccl-cub/PR-3218.md) | cuda.parallel: Support structured types as algorithm inputs |
| `pr-cccl-cub-3236` | upstream-code | [`sources/prs/cccl-cub/PR-3236.md`](../sources/prs/cccl-cub/PR-3236.md) | Fix scan / sm90 perf regression  |
| `pr-cccl-cub-3517` | upstream-code | [`sources/prs/cccl-cub/PR-3517.md`](../sources/prs/cccl-cub/PR-3517.md) | Fix the vectorized loading of BlockLoad |
| `pr-cccl-cub-3543` | upstream-code | [`sources/prs/cccl-cub/PR-3543.md`](../sources/prs/cccl-cub/PR-3543.md) | Tune cub::DeviceTransform for Blackwell |
| `pr-cccl-cub-3544` | upstream-code | [`sources/prs/cccl-cub/PR-3544.md`](../sources/prs/cccl-cub/PR-3544.md) | Bump CI to use CTK 12.8, add sm100 build. |
| `pr-cccl-cub-3559` | upstream-code | [`sources/prs/cccl-cub/PR-3559.md`](../sources/prs/cccl-cub/PR-3559.md) | Add b200 tunings for scan.exclusive.sum |
| `pr-cccl-cub-3565` | upstream-code | [`sources/prs/cccl-cub/PR-3565.md`](../sources/prs/cccl-cub/PR-3565.md) | Backport to 2.8: Tune cub::DeviceTransform for Blackwell (#3543) |
| `pr-cccl-cub-3568` | upstream-code | [`sources/prs/cccl-cub/PR-3568.md`](../sources/prs/cccl-cub/PR-3568.md) | PTX: Update generated files with Blackwell instructions  |
| `pr-cccl-cub-3588` | upstream-code | [`sources/prs/cccl-cub/PR-3588.md`](../sources/prs/cccl-cub/PR-3588.md) | Function-like macros for FP6/BF16 macros |
| `pr-cccl-cub-3611` | upstream-code | [`sources/prs/cccl-cub/PR-3611.md`](../sources/prs/cccl-cub/PR-3611.md) | Add b200 tunings for radix_sort.keys |
| `pr-cccl-cub-3624` | upstream-code | [`sources/prs/cccl-cub/PR-3624.md`](../sources/prs/cccl-cub/PR-3624.md) | Backport to 2.8: PTX support for Blackwell |
| `pr-cccl-cub-3671` | upstream-code | [`sources/prs/cccl-cub/PR-3671.md`](../sources/prs/cccl-cub/PR-3671.md) | [libcudacxx] Stable abstraction for Blackwell work-stealing (PTX try_cancel) |
| `pr-cccl-cub-3691` | upstream-code | [`sources/prs/cccl-cub/PR-3691.md`](../sources/prs/cccl-cub/PR-3691.md) | Fix SM100 histogram tunings |
| `pr-cccl-cub-3708` | upstream-code | [`sources/prs/cccl-cub/PR-3708.md`](../sources/prs/cccl-cub/PR-3708.md) | Add b200 policies for partition.three_way |
| `pr-cccl-cub-3818` | upstream-code | [`sources/prs/cccl-cub/PR-3818.md`](../sources/prs/cccl-cub/PR-3818.md) | Add arch_traits for sm100 to cudax. |
| `pr-cccl-cub-3832` | upstream-code | [`sources/prs/cccl-cub/PR-3832.md`](../sources/prs/cccl-cub/PR-3832.md) | Specialize `numeric_limits` for CUDA 12.8 FP types |
| `pr-cccl-cub-4000` | upstream-code | [`sources/prs/cccl-cub/PR-4000.md`](../sources/prs/cccl-cub/PR-4000.md) | Drop CUB_MIN|MAX in warp_scan_shfl |
| `pr-cccl-cub-4256` | upstream-code | [`sources/prs/cccl-cub/PR-4256.md`](../sources/prs/cccl-cub/PR-4256.md) | Implement fp constants |
| `pr-cccl-cub-4340` | upstream-code | [`sources/prs/cccl-cub/PR-4340.md`](../sources/prs/cccl-cub/PR-4340.md) | Disable extended floating-point types for nvc++ |
| `pr-cccl-cub-4618` | upstream-code | [`sources/prs/cccl-cub/PR-4618.md`](../sources/prs/cccl-cub/PR-4618.md) | Pass `cached_segment` by `span` |
| `pr-cccl-cub-4716` | upstream-code | [`sources/prs/cccl-cub/PR-4716.md`](../sources/prs/cccl-cub/PR-4716.md) | Split Optimize Warp Reduce PR - CUB part |
| `pr-cccl-cub-4778` | upstream-code | [`sources/prs/cccl-cub/PR-4778.md`](../sources/prs/cccl-cub/PR-4778.md) | Align bulk copies to 16 bytes on Blackwell |
| `pr-cccl-cub-4961` | upstream-code | [`sources/prs/cccl-cub/PR-4961.md`](../sources/prs/cccl-cub/PR-4961.md) | Add nondeterministic reduce that uses atomics |
| `pr-cccl-cub-4976` | upstream-code | [`sources/prs/cccl-cub/PR-4976.md`](../sources/prs/cccl-cub/PR-4976.md) | Replace `cg::memcpy_async` in `memcpy_async` transform kernel by custom implementation |
| `pr-cccl-cub-5061` | upstream-code | [`sources/prs/cccl-cub/PR-5061.md`](../sources/prs/cccl-cub/PR-5061.md) | Replace CG by TMA copy in bulk copy fallback path |
| `pr-cccl-cub-5078` | upstream-code | [`sources/prs/cccl-cub/PR-5078.md`](../sources/prs/cccl-cub/PR-5078.md) | Small fixes and improvements to DeviceTransform |
| `pr-cccl-cub-5122` | upstream-code | [`sources/prs/cccl-cub/PR-5122.md`](../sources/prs/cccl-cub/PR-5122.md) | Try, fail and ignore to guarantee dynamic SMEM alignment on Hopper |
| `pr-cccl-cub-5178` | upstream-code | [`sources/prs/cccl-cub/PR-5178.md`](../sources/prs/cccl-cub/PR-5178.md) | Support types with any alignment in UBLKCP transform kernel |
| `pr-cccl-cub-5210` | upstream-code | [`sources/prs/cccl-cub/PR-5210.md`](../sources/prs/cccl-cub/PR-5210.md) | Expose Fast Modulo Division in libcu++ |
| `pr-cccl-cub-5223` | upstream-code | [`sources/prs/cccl-cub/PR-5223.md`](../sources/prs/cccl-cub/PR-5223.md) | Re-enable UBLKCP transform kernel on sm120 |
| `pr-cccl-cub-5269` | upstream-code | [`sources/prs/cccl-cub/PR-5269.md`](../sources/prs/cccl-cub/PR-5269.md) | Add sm90 tunings for RFA F32 |
| `pr-cccl-cub-5314` | upstream-code | [`sources/prs/cccl-cub/PR-5314.md`](../sources/prs/cccl-cub/PR-5314.md) | CUB - Add internal integer utils and tests (Split `WarpReduce` PR) |
| `pr-cccl-cub-5371` | upstream-code | [`sources/prs/cccl-cub/PR-5371.md`](../sources/prs/cccl-cub/PR-5371.md) | Complex sqrt accuracy/speed improvements |
| `pr-cccl-cub-5408` | upstream-code | [`sources/prs/cccl-cub/PR-5408.md`](../sources/prs/cccl-cub/PR-5408.md) | Combine `block_reduce_warp_reduction_nondeterministic.cuh` specialization with original deterministic one  |
| `pr-cccl-cub-5413` | upstream-code | [`sources/prs/cccl-cub/PR-5413.md`](../sources/prs/cccl-cub/PR-5413.md) | Add common constants for floating point types |
| `pr-cccl-cub-5414` | upstream-code | [`sources/prs/cccl-cub/PR-5414.md`](../sources/prs/cccl-cub/PR-5414.md) | Move TMA barrier in DeviceTransform into dynamic SMEM |
| `pr-cccl-cub-5526` | upstream-code | [`sources/prs/cccl-cub/PR-5526.md`](../sources/prs/cccl-cub/PR-5526.md) | Special case `DeviceTransform` for no inputs and provide a `DeviceTransform::Fill` API |
| `pr-cccl-cub-5578` | upstream-code | [`sources/prs/cccl-cub/PR-5578.md`](../sources/prs/cccl-cub/PR-5578.md) | `cuda.cccl.parallel`: Expose "well-known" operations to Python |
| `pr-cccl-cub-5677` | upstream-code | [`sources/prs/cccl-cub/PR-5677.md`](../sources/prs/cccl-cub/PR-5677.md) | Adds device-level Top-K Parallel Algorithm to CUB |
| `pr-cccl-cub-5780` | upstream-code | [`sources/prs/cccl-cub/PR-5780.md`](../sources/prs/cccl-cub/PR-5780.md) | [CUB] Implement `BlockLoadToShared` |
| `pr-cccl-cub-5822` | upstream-code | [`sources/prs/cccl-cub/PR-5822.md`](../sources/prs/cccl-cub/PR-5822.md) | Do not require `int128` in `for_each_canceled` |
| `pr-cccl-cub-5978` | upstream-code | [`sources/prs/cccl-cub/PR-5978.md`](../sources/prs/cccl-cub/PR-5978.md) | [BACKPORT 3.1] Use forward declarations of extended floating point types instead of including the headers (#5846) |
| `pr-cccl-cub-6007` | upstream-code | [`sources/prs/cccl-cub/PR-6007.md`](../sources/prs/cccl-cub/PR-6007.md) | Use just SYNCS unit to wait on cuda::barrier on SM90+ |
| `pr-cccl-cub-6069` | upstream-code | [`sources/prs/cccl-cub/PR-6069.md`](../sources/prs/cccl-cub/PR-6069.md) | Add dynamic CUB dispatch for segmented_sort |
| `pr-cccl-cub-6077` | upstream-code | [`sources/prs/cccl-cub/PR-6077.md`](../sources/prs/cccl-cub/PR-6077.md) | [CUB] Use `BlockLoadToShared` in `DeviceMerge` |
| `pr-cccl-cub-6152` | upstream-code | [`sources/prs/cccl-cub/PR-6152.md`](../sources/prs/cccl-cub/PR-6152.md) | Fix debug section around line 390 of dispatch_topk |
| `pr-cccl-cub-6189` | upstream-code | [`sources/prs/cccl-cub/PR-6189.md`](../sources/prs/cccl-cub/PR-6189.md) | [CUB] Fix mask types in block_radix_rank.cuh |
| `pr-cccl-cub-6202` | upstream-code | [`sources/prs/cccl-cub/PR-6202.md`](../sources/prs/cccl-cub/PR-6202.md) | [Backport 3.1]: [CUB] Replace several direct uses of `__clz` (#6099) |
| `pr-cccl-cub-6246` | upstream-code | [`sources/prs/cccl-cub/PR-6246.md`](../sources/prs/cccl-cub/PR-6246.md) | Fix invalid refactoring of  #4377 |
| `pr-cccl-cub-6250` | upstream-code | [`sources/prs/cccl-cub/PR-6250.md`](../sources/prs/cccl-cub/PR-6250.md) | Replace inline PTX by cuda::ptx in cuda::barrier<thread_scope_block> |
| `pr-cccl-cub-6265` | upstream-code | [`sources/prs/cccl-cub/PR-6265.md`](../sources/prs/cccl-cub/PR-6265.md) | [Backport 3.1] Fix invalid refactoring of  #4377 (#6246) |
| `pr-cccl-cub-6329` | upstream-code | [`sources/prs/cccl-cub/PR-6329.md`](../sources/prs/cccl-cub/PR-6329.md) | Improve `cuda::barrier` TMA examples and `elect_one` in `DeviceTransform` |
| `pr-cccl-cub-6362` | upstream-code | [`sources/prs/cccl-cub/PR-6362.md`](../sources/prs/cccl-cub/PR-6362.md) | Use `cp_async_bulk(space_shared,...)` when available |
| `pr-cccl-cub-6484` | upstream-code | [`sources/prs/cccl-cub/PR-6484.md`](../sources/prs/cccl-cub/PR-6484.md) | Avoid potentially ambiguous overload in `warp_excahnge_shfl` |
| `pr-cccl-cub-6496` | upstream-code | [`sources/prs/cccl-cub/PR-6496.md`](../sources/prs/cccl-cub/PR-6496.md) | Expose `ptx::mbarrier_inval` and use it |
| `pr-cccl-cub-6597` | upstream-code | [`sources/prs/cccl-cub/PR-6597.md`](../sources/prs/cccl-cub/PR-6597.md) | Split fixed-size segmented reduce dispatch header |
| `pr-cccl-cub-6608` | upstream-code | [`sources/prs/cccl-cub/PR-6608.md`](../sources/prs/cccl-cub/PR-6608.md) | Fix `cuda::memcpy async` edge cases and add more tests |
| `pr-cccl-cub-6642` | upstream-code | [`sources/prs/cccl-cub/PR-6642.md`](../sources/prs/cccl-cub/PR-6642.md) | Fea/6482 enable grid constant for all non-mutable CUB kernel parameters |
| `pr-cccl-cub-6666` | upstream-code | [`sources/prs/cccl-cub/PR-6666.md`](../sources/prs/cccl-cub/PR-6666.md) | Migrate cuco HLL |
| `pr-cccl-cub-6811` | upstream-code | [`sources/prs/cccl-cub/PR-6811.md`](../sources/prs/cccl-cub/PR-6811.md) | Integrate decoupled lookahead warpspeed scan |
| `pr-cccl-cub-6814` | upstream-code | [`sources/prs/cccl-cub/PR-6814.md`](../sources/prs/cccl-cub/PR-6814.md) | Improve our `WarpReduce` implementation |
| `pr-cccl-cub-6819` | upstream-code | [`sources/prs/cccl-cub/PR-6819.md`](../sources/prs/cccl-cub/PR-6819.md) | Use integer promotion for `warp_reduce` |
| `pr-cccl-cub-6846` | upstream-code | [`sources/prs/cccl-cub/PR-6846.md`](../sources/prs/cccl-cub/PR-6846.md) | [cuda.coop]: add device-side `coop.warp.sum` benchmark with pynvbench |
| `pr-cccl-cub-6915` | upstream-code | [`sources/prs/cccl-cub/PR-6915.md`](../sources/prs/cccl-cub/PR-6915.md) | Remove need for hardcoded `LevelT` for histogram in c.parallel and cuda.compute |
| `pr-cccl-cub-6921` | upstream-code | [`sources/prs/cccl-cub/PR-6921.md`](../sources/prs/cccl-cub/PR-6921.md) | Use vectorized transform kernel for sizeof(T) < 4 workloads of arity >1 on Hopper |
| `pr-cccl-cub-6926` | upstream-code | [`sources/prs/cccl-cub/PR-6926.md`](../sources/prs/cccl-cub/PR-6926.md) | Expose not guaranteed determinism to reduce in cuda.compute |
| `pr-cccl-cub-6932` | upstream-code | [`sources/prs/cccl-cub/PR-6932.md`](../sources/prs/cccl-cub/PR-6932.md) | [CUB]: Use the new tuning API for nondeterministic reduce |
| `pr-cccl-cub-6938` | upstream-code | [`sources/prs/cccl-cub/PR-6938.md`](../sources/prs/cccl-cub/PR-6938.md) | Unify operator handling in cuda.compute |
| `pr-cccl-cub-6980` | upstream-code | [`sources/prs/cccl-cub/PR-6980.md`](../sources/prs/cccl-cub/PR-6980.md) | Initial version of `DeviceSegmentedTopk` for fixed-size segments |
| `pr-cccl-cub-6992` | upstream-code | [`sources/prs/cccl-cub/PR-6992.md`](../sources/prs/cccl-cub/PR-6992.md) | use cooperative_groups in `execution::bulk` to synchronize across thread blocks |
| `pr-cccl-cub-7093` | upstream-code | [`sources/prs/cccl-cub/PR-7093.md`](../sources/prs/cccl-cub/PR-7093.md) | Implement new tuning API arch dispatching |
| `pr-cccl-cub-7114` | upstream-code | [`sources/prs/cccl-cub/PR-7114.md`](../sources/prs/cccl-cub/PR-7114.md) | Two-phase reduction for fixed size segmented reduction for very large segment sizes |
| `pr-cccl-cub-7245` | upstream-code | [`sources/prs/cccl-cub/PR-7245.md`](../sources/prs/cccl-cub/PR-7245.md) | Fix `is_address_from` for `cluster_shared` for pre-sm_90 |
| `pr-cccl-cub-7334` | upstream-code | [`sources/prs/cccl-cub/PR-7334.md`](../sources/prs/cccl-cub/PR-7334.md) | Implement the new tuning API for `DeviceSegmentedReduce` |
| `pr-cccl-cub-7341` | upstream-code | [`sources/prs/cccl-cub/PR-7341.md`](../sources/prs/cccl-cub/PR-7341.md) | bench: Migrate Python cuda.compute benchmarks to nvbench |
| `pr-cccl-cub-7346` | upstream-code | [`sources/prs/cccl-cub/PR-7346.md`](../sources/prs/cccl-cub/PR-7346.md) | Implement the new tuning API for deterministic (rfa) reduce dispatch |
| `pr-cccl-cub-7384` | upstream-code | [`sources/prs/cccl-cub/PR-7384.md`](../sources/prs/cccl-cub/PR-7384.md) | Radix-selection based `BlockTopK` specialization |
| `pr-cccl-cub-7500` | upstream-code | [`sources/prs/cccl-cub/PR-7500.md`](../sources/prs/cccl-cub/PR-7500.md) | cuda.compute: Use native CCCL.c support for stateful ops |
| `pr-cccl-cub-7501` | upstream-code | [`sources/prs/cccl-cub/PR-7501.md`](../sources/prs/cccl-cub/PR-7501.md) | cuda.compute: improve caching performance by not relying on `isinstance()` checks for protocols |
| `pr-cccl-cub-7510` | upstream-code | [`sources/prs/cccl-cub/PR-7510.md`](../sources/prs/cccl-cub/PR-7510.md) | Extend `DeviceTransform` tuning |
| `pr-cccl-cub-7561` | upstream-code | [`sources/prs/cccl-cub/PR-7561.md`](../sources/prs/cccl-cub/PR-7561.md) | Remove recursion from __internal_is_address_from |
| `pr-cccl-cub-7565` | upstream-code | [`sources/prs/cccl-cub/PR-7565.md`](../sources/prs/cccl-cub/PR-7565.md) | Implement the new tuning API for `DeviceScan` |
| `pr-cccl-cub-7571` | upstream-code | [`sources/prs/cccl-cub/PR-7571.md`](../sources/prs/cccl-cub/PR-7571.md) | Vectorize reduction also for trivially relocatable types |
| `pr-cccl-cub-7575` | upstream-code | [`sources/prs/cccl-cub/PR-7575.md`](../sources/prs/cccl-cub/PR-7575.md) | Support more types in decoupled lookback fastpath |
| `pr-cccl-cub-7603` | upstream-code | [`sources/prs/cccl-cub/PR-7603.md`](../sources/prs/cccl-cub/PR-7603.md) | [cudax] Implement _this_ hierarchy groups |
| `pr-cccl-cub-7667` | upstream-code | [`sources/prs/cccl-cub/PR-7667.md`](../sources/prs/cccl-cub/PR-7667.md) | Implement the new tuning API for `Dispatch[Streaming]ReduceByKey` |
| `pr-cccl-cub-7669` | upstream-code | [`sources/prs/cccl-cub/PR-7669.md`](../sources/prs/cccl-cub/PR-7669.md) | Implement the new tuning API for `DeviceRleDispatch` |
| `pr-cccl-cub-7676` | upstream-code | [`sources/prs/cccl-cub/PR-7676.md`](../sources/prs/cccl-cub/PR-7676.md) | Generalized `cudax::copy_bytes` for `mdspan` |
| `pr-cccl-cub-7681` | upstream-code | [`sources/prs/cccl-cub/PR-7681.md`](../sources/prs/cccl-cub/PR-7681.md) | Fix max atomic size for NVHPC |
| `pr-cccl-cub-7692` | upstream-code | [`sources/prs/cccl-cub/PR-7692.md`](../sources/prs/cccl-cub/PR-7692.md) | Implement `WarpReduceBatched` |
| `pr-cccl-cub-7718` | upstream-code | [`sources/prs/cccl-cub/PR-7718.md`](../sources/prs/cccl-cub/PR-7718.md) | Optimize non fixed size segmented reduce for small segments using max_segment_size |
| `pr-cccl-cub-7795` | upstream-code | [`sources/prs/cccl-cub/PR-7795.md`](../sources/prs/cccl-cub/PR-7795.md) | Add env SegmentedReduce (non fixed-size overloads) |
| `pr-cccl-cub-7805` | upstream-code | [`sources/prs/cccl-cub/PR-7805.md`](../sources/prs/cccl-cub/PR-7805.md) | Forward policy hub from `dispatch_streaming_arg_reduce_t` to `reduce::dispatch` |
| `pr-cccl-cub-7807` | upstream-code | [`sources/prs/cccl-cub/PR-7807.md`](../sources/prs/cccl-cub/PR-7807.md) | Implement the new tuning API for `detail::reduce::dispatch_streaming_arg_reduce_t` |
| `pr-cccl-cub-7810` | upstream-code | [`sources/prs/cccl-cub/PR-7810.md`](../sources/prs/cccl-cub/PR-7810.md) | Use the new tuning API internally for `detail::transform::dispatch` |
| `pr-cccl-cub-7814` | upstream-code | [`sources/prs/cccl-cub/PR-7814.md`](../sources/prs/cccl-cub/PR-7814.md) | [Backport branch/3.3.x] Forward policy hub from `dispatch_streaming_arg_reduce_t` to `reduce::dispatch` |
| `pr-cccl-cub-7822` | upstream-code | [`sources/prs/cccl-cub/PR-7822.md`](../sources/prs/cccl-cub/PR-7822.md) | Use `__block_size__` attribute in `cuda::launch` |
| `pr-cccl-cub-7823` | upstream-code | [`sources/prs/cccl-cub/PR-7823.md`](../sources/prs/cccl-cub/PR-7823.md) | Optimized Device-to-Device Tensor Copy (`cudax`) |
| `pr-cccl-cub-7844` | upstream-code | [`sources/prs/cccl-cub/PR-7844.md`](../sources/prs/cccl-cub/PR-7844.md) | Implement the new tuning API for `DispatchSegmentedRadixSort` |
| `pr-cccl-cub-7861` | upstream-code | [`sources/prs/cccl-cub/PR-7861.md`](../sources/prs/cccl-cub/PR-7861.md) | Improve warpspeed scan tuning for sm120 |
| `pr-cccl-cub-7869` | upstream-code | [`sources/prs/cccl-cub/PR-7869.md`](../sources/prs/cccl-cub/PR-7869.md) | Enables sort_by_key with long double keys on the host |
| `pr-cccl-cub-7874` | upstream-code | [`sources/prs/cccl-cub/PR-7874.md`](../sources/prs/cccl-cub/PR-7874.md) | Implement the new tuning API for `DispatchSegmentedSort` |
| `pr-cccl-cub-7892` | upstream-code | [`sources/prs/cccl-cub/PR-7892.md`](../sources/prs/cccl-cub/PR-7892.md) | Reduce warpspeed scan to 256 threads/block on NVHPC |
| `pr-cccl-cub-7908` | upstream-code | [`sources/prs/cccl-cub/PR-7908.md`](../sources/prs/cccl-cub/PR-7908.md) | Add env RLE |
| `pr-cccl-cub-7916` | upstream-code | [`sources/prs/cccl-cub/PR-7916.md`](../sources/prs/cccl-cub/PR-7916.md) | [cuda.compute]: Merge sort negative temp storage bytes fix |
| `pr-cccl-cub-7924` | upstream-code | [`sources/prs/cccl-cub/PR-7924.md`](../sources/prs/cccl-cub/PR-7924.md) | Implement parallel `cuda::std::reverse` |
| `pr-cccl-cub-7928` | upstream-code | [`sources/prs/cccl-cub/PR-7928.md`](../sources/prs/cccl-cub/PR-7928.md) | Implement the new tuning API for `DispatchTopK` |
| `pr-cccl-cub-7933` | upstream-code | [`sources/prs/cccl-cub/PR-7933.md`](../sources/prs/cccl-cub/PR-7933.md) | Improve this hierarchy groups |
| `pr-cccl-cub-7940` | upstream-code | [`sources/prs/cccl-cub/PR-7940.md`](../sources/prs/cccl-cub/PR-7940.md) | [cuda.compute]: Fix faulty pointer arithmetic calculation in CUB dispatch |
| `pr-cccl-cub-7944` | upstream-code | [`sources/prs/cccl-cub/PR-7944.md`](../sources/prs/cccl-cub/PR-7944.md) | Reduce usage of `cub::DispatchReduce` |
| `pr-cccl-cub-7949` | upstream-code | [`sources/prs/cccl-cub/PR-7949.md`](../sources/prs/cccl-cub/PR-7949.md) | Use the new tuning API for `detail::radix_sort::dispatch` |
| `pr-cccl-cub-7967` | upstream-code | [`sources/prs/cccl-cub/PR-7967.md`](../sources/prs/cccl-cub/PR-7967.md) | Add environment overloads for `DeviceHistogram::*` |
| `pr-cccl-cub-7968` | upstream-code | [`sources/prs/cccl-cub/PR-7968.md`](../sources/prs/cccl-cub/PR-7968.md) | Add environment `DeviceMergeSort` |
| `pr-cccl-cub-7987` | upstream-code | [`sources/prs/cccl-cub/PR-7987.md`](../sources/prs/cccl-cub/PR-7987.md) | Implement parallel `cuda::std::unique_copy` |
| `pr-cccl-cub-7999` | upstream-code | [`sources/prs/cccl-cub/PR-7999.md`](../sources/prs/cccl-cub/PR-7999.md) | Add env overloads for DeviceSegmentedRadixSort |
| `pr-cccl-cub-8008` | upstream-code | [`sources/prs/cccl-cub/PR-8008.md`](../sources/prs/cccl-cub/PR-8008.md) | Make warpspeed scan tunable |
| `pr-cccl-cub-8010` | upstream-code | [`sources/prs/cccl-cub/PR-8010.md`](../sources/prs/cccl-cub/PR-8010.md) | Properly support complex64 in nvbench_helper |
| `pr-cccl-cub-8020` | upstream-code | [`sources/prs/cccl-cub/PR-8020.md`](../sources/prs/cccl-cub/PR-8020.md) | Add env ReduceByKey and TransformReduce |
| `pr-cccl-cub-8035` | upstream-code | [`sources/prs/cccl-cub/PR-8035.md`](../sources/prs/cccl-cub/PR-8035.md) | [STF] Refactor exec_place to unified grid model |
| `pr-cccl-cub-8040` | upstream-code | [`sources/prs/cccl-cub/PR-8040.md`](../sources/prs/cccl-cub/PR-8040.md) | Adds support for non-fundamental types via decomposer to `DeviceTopK`  |
| `pr-cccl-cub-8061` | upstream-code | [`sources/prs/cccl-cub/PR-8061.md`](../sources/prs/cccl-cub/PR-8061.md) | Implement parallel `cuda::std::transform_inclusive_scan` |
| `pr-cccl-cub-8067` | upstream-code | [`sources/prs/cccl-cub/PR-8067.md`](../sources/prs/cccl-cub/PR-8067.md) | Use nv atomics in grid sync |
| `pr-cccl-cub-8080` | upstream-code | [`sources/prs/cccl-cub/PR-8080.md`](../sources/prs/cccl-cub/PR-8080.md) | Implement `is_root_rank` and `is_part_of` queries for groups |
| `pr-cccl-cub-8107` | upstream-code | [`sources/prs/cccl-cub/PR-8107.md`](../sources/prs/cccl-cub/PR-8107.md) | Implement parallel `cuda::std::shift_left` |
| `pr-cccl-cub-8125` | upstream-code | [`sources/prs/cccl-cub/PR-8125.md`](../sources/prs/cccl-cub/PR-8125.md) | Optimized Device-to-Device Tensor Copy (cudax) - Transpose Case |
| `pr-cccl-cub-8128` | upstream-code | [`sources/prs/cccl-cub/PR-8128.md`](../sources/prs/cccl-cub/PR-8128.md) | Implement the new tuning API for `DispatchMergeSort` |
| `pr-cccl-cub-8145` | upstream-code | [`sources/prs/cccl-cub/PR-8145.md`](../sources/prs/cccl-cub/PR-8145.md) | Refactor warpspeed scan tuning |
| `pr-cccl-cub-8158` | upstream-code | [`sources/prs/cccl-cub/PR-8158.md`](../sources/prs/cccl-cub/PR-8158.md) | Let scan tuning policy choose warpspeed or not |
| `pr-cccl-cub-8164` | upstream-code | [`sources/prs/cccl-cub/PR-8164.md`](../sources/prs/cccl-cub/PR-8164.md) | New tuning API for DeviceScanByKey |
| `pr-cccl-cub-8169` | upstream-code | [`sources/prs/cccl-cub/PR-8169.md`](../sources/prs/cccl-cub/PR-8169.md) | Fix UB in `cuda::device::warp_match_all` |
| `pr-cccl-cub-8172` | upstream-code | [`sources/prs/cccl-cub/PR-8172.md`](../sources/prs/cccl-cub/PR-8172.md) | [CUB] Add detail::uninitialized_array |
| `pr-cccl-cub-8184` | upstream-code | [`sources/prs/cccl-cub/PR-8184.md`](../sources/prs/cccl-cub/PR-8184.md) | Avoid passing uninitialized values to scan_op |
| `pr-cccl-cub-8210` | upstream-code | [`sources/prs/cccl-cub/PR-8210.md`](../sources/prs/cccl-cub/PR-8210.md) | Add warp shuffle constraints |
| `pr-cccl-cub-8212` | upstream-code | [`sources/prs/cccl-cub/PR-8212.md`](../sources/prs/cccl-cub/PR-8212.md) | Implement the new tuning API for `DispatchHistogram` |
| `pr-cccl-cub-8214` | upstream-code | [`sources/prs/cccl-cub/PR-8214.md`](../sources/prs/cccl-cub/PR-8214.md) | Fix typos in `_CCCL_BLOCK_SIZE` definition |
| `pr-cccl-cub-8222` | upstream-code | [`sources/prs/cccl-cub/PR-8222.md`](../sources/prs/cccl-cub/PR-8222.md) | Small warpspeed scan improvements |
| `pr-cccl-cub-8223` | upstream-code | [`sources/prs/cccl-cub/PR-8223.md`](../sources/prs/cccl-cub/PR-8223.md) | Don't specify `__launch_bounds__` together with  `__block_size__` |
| `pr-cccl-cub-8236` | upstream-code | [`sources/prs/cccl-cub/PR-8236.md`](../sources/prs/cccl-cub/PR-8236.md) | Prevent ADL from finding user-namespace functions in `kernel_scan_warp` |
| `pr-cccl-cub-8251` | upstream-code | [`sources/prs/cccl-cub/PR-8251.md`](../sources/prs/cccl-cub/PR-8251.md) | `cuda::std::simd` core functionalities |
| `pr-cccl-cub-8253` | upstream-code | [`sources/prs/cccl-cub/PR-8253.md`](../sources/prs/cccl-cub/PR-8253.md) | `cuda::std::simd` Reduction functionalities |
| `pr-cccl-cub-8254` | upstream-code | [`sources/prs/cccl-cub/PR-8254.md`](../sources/prs/cccl-cub/PR-8254.md) | Recover `warp_shuffle` original behavior (revert #8210) |
| `pr-cccl-cub-8265` | upstream-code | [`sources/prs/cccl-cub/PR-8265.md`](../sources/prs/cccl-cub/PR-8265.md) | `cuda::is_trivially_copyable` |
| `pr-cccl-cub-8270` | upstream-code | [`sources/prs/cccl-cub/PR-8270.md`](../sources/prs/cccl-cub/PR-8270.md) | `cuda::is_bitwise_comparable` |
| `pr-cccl-cub-8284` | upstream-code | [`sources/prs/cccl-cub/PR-8284.md`](../sources/prs/cccl-cub/PR-8284.md) | Expose `max_segment_size` guarantee in cuda.compute |
| `pr-cccl-cub-8285` | upstream-code | [`sources/prs/cccl-cub/PR-8285.md`](../sources/prs/cccl-cub/PR-8285.md) | Support a custom comparison operator in `DeviceReduce::ArgMin|Max` |
| `pr-cccl-cub-8286` | upstream-code | [`sources/prs/cccl-cub/PR-8286.md`](../sources/prs/cccl-cub/PR-8286.md) | Add nonstable env `DeviceSegmentedSort::Pairs`  2/2 |
| `pr-cccl-cub-8291` | upstream-code | [`sources/prs/cccl-cub/PR-8291.md`](../sources/prs/cccl-cub/PR-8291.md) | Port `thrust::min|max_element` to CUB |
| `pr-cccl-cub-8299` | upstream-code | [`sources/prs/cccl-cub/PR-8299.md`](../sources/prs/cccl-cub/PR-8299.md) | Extract first histogram-only pass in `DeviceTopK` into its own kernel |
| `pr-cccl-cub-8311` | upstream-code | [`sources/prs/cccl-cub/PR-8311.md`](../sources/prs/cccl-cub/PR-8311.md) | Implement the new tuning API for `DispatchSelectIf` |
| `pr-cccl-cub-8323` | upstream-code | [`sources/prs/cccl-cub/PR-8323.md`](../sources/prs/cccl-cub/PR-8323.md) | Add `DoubleBuffer` env overloads for `DeviceSegmentedRadixSort::SortKeys` |
| `pr-cccl-cub-8328` | upstream-code | [`sources/prs/cccl-cub/PR-8328.md`](../sources/prs/cccl-cub/PR-8328.md) | Disable `__block_dims__` kernel launcher |
| `pr-cccl-cub-8331` | upstream-code | [`sources/prs/cccl-cub/PR-8331.md`](../sources/prs/cccl-cub/PR-8331.md) | Refactor radix rank sort operations |
| `pr-cccl-cub-8332` | upstream-code | [`sources/prs/cccl-cub/PR-8332.md`](../sources/prs/cccl-cub/PR-8332.md) | simplify dispatch segmented reduce to use latest dispatch and new tunings API |
| `pr-cccl-cub-8342` | upstream-code | [`sources/prs/cccl-cub/PR-8342.md`](../sources/prs/cccl-cub/PR-8342.md) | Make warpspeed scan tunable |
| `pr-cccl-cub-8351` | upstream-code | [`sources/prs/cccl-cub/PR-8351.md`](../sources/prs/cccl-cub/PR-8351.md) | Fix and improve vector type traits |
| `pr-cccl-cub-8352` | upstream-code | [`sources/prs/cccl-cub/PR-8352.md`](../sources/prs/cccl-cub/PR-8352.md) | Apply some random warpspeed tunings |
| `pr-cccl-cub-8355` | upstream-code | [`sources/prs/cccl-cub/PR-8355.md`](../sources/prs/cccl-cub/PR-8355.md) | [cub]: implement utilities for policy selection |
| `pr-cccl-cub-8381` | upstream-code | [`sources/prs/cccl-cub/PR-8381.md`](../sources/prs/cccl-cub/PR-8381.md) | Replace `detail::merge::dispatch` by CUB's public API |
| `pr-cccl-cub-8383` | upstream-code | [`sources/prs/cccl-cub/PR-8383.md`](../sources/prs/cccl-cub/PR-8383.md) | [docs] Fix SortKeysCopy code snippet to include d_output_keys parameter |
| `pr-cccl-cub-8394` | upstream-code | [`sources/prs/cccl-cub/PR-8394.md`](../sources/prs/cccl-cub/PR-8394.md) | Refactor and improve `extents_as` queries |
| `pr-cccl-cub-8395` | upstream-code | [`sources/prs/cccl-cub/PR-8395.md`](../sources/prs/cccl-cub/PR-8395.md) | [CUB] Replace `Shuffle(Up|Down|Index)` with cuda::device::warp_shuffle - RadixSort only |
| `pr-cccl-cub-8407` | upstream-code | [`sources/prs/cccl-cub/PR-8407.md`](../sources/prs/cccl-cub/PR-8407.md) | Workaround nvc++ crash in warpspeed scan |
| `pr-cccl-cub-8421` | upstream-code | [`sources/prs/cccl-cub/PR-8421.md`](../sources/prs/cccl-cub/PR-8421.md) | New tuning API for DeviceUniqueByKey |
| `pr-cccl-cub-8423` | upstream-code | [`sources/prs/cccl-cub/PR-8423.md`](../sources/prs/cccl-cub/PR-8423.md) | Vectorize mbarrier initialization in warpspeed scan |
| `pr-cccl-cub-8427` | upstream-code | [`sources/prs/cccl-cub/PR-8427.md`](../sources/prs/cccl-cub/PR-8427.md) | [thrust] Single-pass `is_partitioned` via adjacent zip_iterator |
| `pr-cccl-cub-8439` | upstream-code | [`sources/prs/cccl-cub/PR-8439.md`](../sources/prs/cccl-cub/PR-8439.md) | Swap the `store_algorithm` and `scan_algorithm` in `scan_by_key_policy` |
| `pr-cccl-cub-8440` | upstream-code | [`sources/prs/cccl-cub/PR-8440.md`](../sources/prs/cccl-cub/PR-8440.md) | Swap the `load_modifier` and `store_algorithm` in `sub_warp_merge_sort_policy` |
| `pr-cccl-cub-8441` | upstream-code | [`sources/prs/cccl-cub/PR-8441.md`](../sources/prs/cccl-cub/PR-8441.md) | Rename `agent_warp_reduce_policy` to `warp_reduce_policy` |
| `pr-cccl-cub-8456` | upstream-code | [`sources/prs/cccl-cub/PR-8456.md`](../sources/prs/cccl-cub/PR-8456.md) | modernize-type-traits |
| `pr-cccl-cub-8473` | upstream-code | [`sources/prs/cccl-cub/PR-8473.md`](../sources/prs/cccl-cub/PR-8473.md) | Replace `detail::merge_sort::dispatch` by CUB's public API |
| `pr-cccl-cub-8487` | upstream-code | [`sources/prs/cccl-cub/PR-8487.md`](../sources/prs/cccl-cub/PR-8487.md) | Enable hierarchy query tests for nvrtc |
| `pr-cccl-cub-8495` | upstream-code | [`sources/prs/cccl-cub/PR-8495.md`](../sources/prs/cccl-cub/PR-8495.md) | Replace `detail::scan::dispatch` by CUB's public API |
| `pr-cccl-cub-8504` | upstream-code | [`sources/prs/cccl-cub/PR-8504.md`](../sources/prs/cccl-cub/PR-8504.md) | thrust: add 4-iterator mismatch overloads (bounded last2) |
| `pr-cccl-cub-8522` | upstream-code | [`sources/prs/cccl-cub/PR-8522.md`](../sources/prs/cccl-cub/PR-8522.md) | [CUB] Delegate large segments to Multi-CTA Implementation in `DeviceSegmentedTopK` |
| `pr-cccl-cub-8523` | upstream-code | [`sources/prs/cccl-cub/PR-8523.md`](../sources/prs/cccl-cub/PR-8523.md) | [cudax] Implement public groups synchronizers |
| `pr-cccl-cub-8527` | upstream-code | [`sources/prs/cccl-cub/PR-8527.md`](../sources/prs/cccl-cub/PR-8527.md) | [cudax] Make groups constructible from other groups |
| `pr-cccl-cub-8529` | upstream-code | [`sources/prs/cccl-cub/PR-8529.md`](../sources/prs/cccl-cub/PR-8529.md) | Prefer the term warpspeed over lookahead |
| `pr-cccl-cub-8538` | upstream-code | [`sources/prs/cccl-cub/PR-8538.md`](../sources/prs/cccl-cub/PR-8538.md) | Implement the new tuning API for `detail::batched_topk::dispatch_batched_topk` |
| `pr-cccl-cub-8540` | upstream-code | [`sources/prs/cccl-cub/PR-8540.md`](../sources/prs/cccl-cub/PR-8540.md) | Properly migrate scan_by_key benchmark to policy_selector. |
| `pr-cccl-cub-8565` | upstream-code | [`sources/prs/cccl-cub/PR-8565.md`](../sources/prs/cccl-cub/PR-8565.md) | Replace `detail::for_each::dispatch` by CUB's public API |
| `pr-cccl-cub-8611` | upstream-code | [`sources/prs/cccl-cub/PR-8611.md`](../sources/prs/cccl-cub/PR-8611.md) | Add B200 tuning for warpspeed_scan  |
| `pr-cccl-cub-8616` | upstream-code | [`sources/prs/cccl-cub/PR-8616.md`](../sources/prs/cccl-cub/PR-8616.md) | Also update the second overload of `inclusive_scan` |
| `pr-cccl-cub-8621` | upstream-code | [`sources/prs/cccl-cub/PR-8621.md`](../sources/prs/cccl-cub/PR-8621.md) | Implement parallel `cuda::std::sort` |
| `pr-cccl-cub-8639` | upstream-code | [`sources/prs/cccl-cub/PR-8639.md`](../sources/prs/cccl-cub/PR-8639.md) | Segmented scan multisegment part 1 |
| `pr-cccl-cub-8648` | upstream-code | [`sources/prs/cccl-cub/PR-8648.md`](../sources/prs/cccl-cub/PR-8648.md) | Refactor offset type assertion in segmented scan |
| `pr-cccl-cub-8657` | upstream-code | [`sources/prs/cccl-cub/PR-8657.md`](../sources/prs/cccl-cub/PR-8657.md) | Add a killswitch for warpspeed scan |
| `pr-cccl-cub-8674` | upstream-code | [`sources/prs/cccl-cub/PR-8674.md`](../sources/prs/cccl-cub/PR-8674.md) | [STF] Fix stream_ctx under CUDA graph capture |
| `pr-cccl-cub-8689` | upstream-code | [`sources/prs/cccl-cub/PR-8689.md`](../sources/prs/cccl-cub/PR-8689.md) | Revert I8 tunings for warpspeed scan |
| `pr-cccl-cub-8695` | upstream-code | [`sources/prs/cccl-cub/PR-8695.md`](../sources/prs/cccl-cub/PR-8695.md) | Replace `detail::segmented_reduce::dispatch` by the public API |
| `pr-cccl-cub-8708` | upstream-code | [`sources/prs/cccl-cub/PR-8708.md`](../sources/prs/cccl-cub/PR-8708.md) | Unify always_true and always_false into libcu++ |
| `pr-cccl-cub-8733` | upstream-code | [`sources/prs/cccl-cub/PR-8733.md`](../sources/prs/cccl-cub/PR-8733.md) | Allows moving the token returned from `BlockLoadToShared`.  |
| `pr-cccl-cub-8742` | upstream-code | [`sources/prs/cccl-cub/PR-8742.md`](../sources/prs/cccl-cub/PR-8742.md) | Use the new tuning API internally for `detail::topk::dispatch` |
| `pr-cccl-cub-8755` | upstream-code | [`sources/prs/cccl-cub/PR-8755.md`](../sources/prs/cccl-cub/PR-8755.md) | [cudax] Change the group mapping application logic |
| `pr-cccl-cub-8763` | upstream-code | [`sources/prs/cccl-cub/PR-8763.md`](../sources/prs/cccl-cub/PR-8763.md) | [HostJit] Pretend HostJit suppports cuda atomics |
| `pr-cccl-cub-8766` | upstream-code | [`sources/prs/cccl-cub/PR-8766.md`](../sources/prs/cccl-cub/PR-8766.md) | [cudax] Implement `composite_mapping` for groups |
| `pr-cccl-cub-8769` | upstream-code | [`sources/prs/cccl-cub/PR-8769.md`](../sources/prs/cccl-cub/PR-8769.md) | [thrust] Fix is_partitioned with non-const predicates |
| `pr-cccl-cub-8772` | upstream-code | [`sources/prs/cccl-cub/PR-8772.md`](../sources/prs/cccl-cub/PR-8772.md) | [cuda.compute]: API cleanup before 1.0 |
| `pr-cccl-cub-8775` | upstream-code | [`sources/prs/cccl-cub/PR-8775.md`](../sources/prs/cccl-cub/PR-8775.md) | `cuda::std::simd` Optimize Arithmetic Floating-point Operations |
| `pr-cccl-cub-8788` | upstream-code | [`sources/prs/cccl-cub/PR-8788.md`](../sources/prs/cccl-cub/PR-8788.md) | Rename cuda.coop backend to cuda.coop._experimental |
| `pr-cccl-cub-8802` | upstream-code | [`sources/prs/cccl-cub/PR-8802.md`](../sources/prs/cccl-cub/PR-8802.md) | [libcu++] Add shared versions of memory pool owning objects |
| `pr-cccl-cub-8803` | upstream-code | [`sources/prs/cccl-cub/PR-8803.md`](../sources/prs/cccl-cub/PR-8803.md) | Fix DeviceTransform byte-offset overflow when num_items*sizeof(T) > 4Gb |
| `pr-cccl-cub-8809` | upstream-code | [`sources/prs/cccl-cub/PR-8809.md`](../sources/prs/cccl-cub/PR-8809.md) | Split off non-determin. reduce tuning |
| `pr-cccl-cub-8810` | upstream-code | [`sources/prs/cccl-cub/PR-8810.md`](../sources/prs/cccl-cub/PR-8810.md) | [Tile] Improve overlapping range check for `cuda::std::copy` |
| `pr-cccl-cub-8826` | upstream-code | [`sources/prs/cccl-cub/PR-8826.md`](../sources/prs/cccl-cub/PR-8826.md) | Use the new tuning API internally for `detail::reduce[_nd]::dispatch[_nd]` |
| `pr-cccl-cub-8835` | upstream-code | [`sources/prs/cccl-cub/PR-8835.md`](../sources/prs/cccl-cub/PR-8835.md) | Rename `BlockThreads` to `ThreadsPerBlock` |
| `pr-cccl-cub-8836` | upstream-code | [`sources/prs/cccl-cub/PR-8836.md`](../sources/prs/cccl-cub/PR-8836.md) | Rename `block_threads` -> `threads_per_block` |
| `pr-cccl-cub-8839` | upstream-code | [`sources/prs/cccl-cub/PR-8839.md`](../sources/prs/cccl-cub/PR-8839.md) | Fix Warpspeed scan shifted output store |
| `pr-cccl-cub-8857` | upstream-code | [`sources/prs/cccl-cub/PR-8857.md`](../sources/prs/cccl-cub/PR-8857.md) | cudax: introduce HLL Policy template parameter |
| `pr-cccl-cub-8861` | upstream-code | [`sources/prs/cccl-cub/PR-8861.md`](../sources/prs/cccl-cub/PR-8861.md) | [cub] Simplify arch dispatch |
| `pr-cccl-cub-8898` | upstream-code | [`sources/prs/cccl-cub/PR-8898.md`](../sources/prs/cccl-cub/PR-8898.md) | Move segmented radix sort policies to own header |
| `pr-cccl-cub-8922` | upstream-code | [`sources/prs/cccl-cub/PR-8922.md`](../sources/prs/cccl-cub/PR-8922.md) | Disable warpspeed scan on sm120 with nvcc < 13.4 |
| `pr-cccl-cub-8924` | upstream-code | [`sources/prs/cccl-cub/PR-8924.md`](../sources/prs/cccl-cub/PR-8924.md) | Fix nightly GCC8 build regressions in bit_cast and DeviceReduce |
| `pr-cccl-cub-8928` | upstream-code | [`sources/prs/cccl-cub/PR-8928.md`](../sources/prs/cccl-cub/PR-8928.md) | [c2h] Make catch macros work on device |
| `pr-cccl-cub-8939` | upstream-code | [`sources/prs/cccl-cub/PR-8939.md`](../sources/prs/cccl-cub/PR-8939.md) | Enable clang-diagnositc clang-tidy checks |
| `pr-cccl-cub-8958` | upstream-code | [`sources/prs/cccl-cub/PR-8958.md`](../sources/prs/cccl-cub/PR-8958.md) | [Tile] Move annotated_ptr to _CCCL_HOST_DEVICE_API |
| `pr-cccl-cub-8967` | upstream-code | [`sources/prs/cccl-cub/PR-8967.md`](../sources/prs/cccl-cub/PR-8967.md) | Also disable warpspeed scan below NVRTC 13.4 |
| `pr-cccl-cub-8980` | upstream-code | [`sources/prs/cccl-cub/PR-8980.md`](../sources/prs/cccl-cub/PR-8980.md) | docs: fix duplicated words in host_stub_visibility and permutation_iterator comments |
| `pr-cccl-cub-8988` | upstream-code | [`sources/prs/cccl-cub/PR-8988.md`](../sources/prs/cccl-cub/PR-8988.md) | [infra] Add clang-cuda-21 in C++23 job for libcu++ |
| `pr-cccl-cub-8992` | upstream-code | [`sources/prs/cccl-cub/PR-8992.md`](../sources/prs/cccl-cub/PR-8992.md) | Use the new tuning API internally for `detail::segmented_sort::dispatch` |
| `pr-cccl-cub-9013` | upstream-code | [`sources/prs/cccl-cub/PR-9013.md`](../sources/prs/cccl-cub/PR-9013.md) | [Tile] Mark `simd` as `_CCCL_HOST_DEVICE` |
| `pr-cccl-cub-9018` | upstream-code | [`sources/prs/cccl-cub/PR-9018.md`](../sources/prs/cccl-cub/PR-9018.md) | [Tile] Mark some algorithms as `_CCCL_HOST_DEVICE_API` |
| `pr-cccl-cub-9020` | upstream-code | [`sources/prs/cccl-cub/PR-9020.md`](../sources/prs/cccl-cub/PR-9020.md) | Fix mdspan support in modernized CUB interfaces |
| `pr-cccl-cub-9023` | upstream-code | [`sources/prs/cccl-cub/PR-9023.md`](../sources/prs/cccl-cub/PR-9023.md) | [Tile] Avoid internal usage of CPOs |
| `pr-cccl-cub-9031` | upstream-code | [`sources/prs/cccl-cub/PR-9031.md`](../sources/prs/cccl-cub/PR-9031.md) | [Tile] Avoid calling a device only function in tile mode |
| `pr-cccl-cub-9032` | upstream-code | [`sources/prs/cccl-cub/PR-9032.md`](../sources/prs/cccl-cub/PR-9032.md) | [Tile] Avoid return in switch statements in `variant` |
| `pr-cccl-cub-9035` | upstream-code | [`sources/prs/cccl-cub/PR-9035.md`](../sources/prs/cccl-cub/PR-9035.md) | [Tile] Try to appease tile compiler |

<a id="nvidiacutlass"></a>
## NVIDIA/cutlass

64 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-cutlass-1189` | upstream-code | [`sources/prs/cutlass/PR-1189.md`](../sources/prs/cutlass/PR-1189.md) | Add support for sparse GEMM with visitor epilogue |
| `pr-cutlass-1275` | upstream-code | [`sources/prs/cutlass/PR-1275.md`](../sources/prs/cutlass/PR-1275.md) | Allow per-column bias in EpilogueTensorBroadcast |
| `pr-cutlass-1302` | upstream-code | [`sources/prs/cutlass/PR-1302.md`](../sources/prs/cutlass/PR-1302.md) | Remove sparse GEMM with row broadcasted bias vector |
| `pr-cutlass-1350` | upstream-code | [`sources/prs/cutlass/PR-1350.md`](../sources/prs/cutlass/PR-1350.md) | Add couple configs into generator.py for mixed input MM |
| `pr-cutlass-1413` | upstream-code | [`sources/prs/cutlass/PR-1413.md`](../sources/prs/cutlass/PR-1413.md) | Add support for mixed 4-bit/8-bit data types GEMM |
| `pr-cutlass-1543` | upstream-code | [`sources/prs/cutlass/PR-1543.md`](../sources/prs/cutlass/PR-1543.md) | Fix potential out-of-bounds access in 3.x grouped gemm kernel |
| `pr-cutlass-1661` | upstream-code | [`sources/prs/cutlass/PR-1661.md`](../sources/prs/cutlass/PR-1661.md) | Skip void-C kernels in the profiler when beta is non zero |
| `pr-cutlass-1713` | upstream-code | [`sources/prs/cutlass/PR-1713.md`](../sources/prs/cutlass/PR-1713.md) | update 3.5.1 readme/changelog |
| `pr-cutlass-1753` | upstream-code | [`sources/prs/cutlass/PR-1753.md`](../sources/prs/cutlass/PR-1753.md) | Fix EVT for cutlass::gemm::kernel::DefaultGemmWithVisitor's behavior when constructing GemmUniversalAdapter |
| `pr-cutlass-1795` | upstream-code | [`sources/prs/cutlass/PR-1795.md`](../sources/prs/cutlass/PR-1795.md) | Support for TMA Epilogue for Group Gemm and add pingpong ptr array & Group Gemm |
| `pr-cutlass-1796` | upstream-code | [`sources/prs/cutlass/PR-1796.md`](../sources/prs/cutlass/PR-1796.md) | Prefix a member template name with the template keyword. |
| `pr-cutlass-1833` | upstream-code | [`sources/prs/cutlass/PR-1833.md`](../sources/prs/cutlass/PR-1833.md) | EVT: add maximum/minimum evt support |
| `pr-cutlass-1883` | upstream-code | [`sources/prs/cutlass/PR-1883.md`](../sources/prs/cutlass/PR-1883.md) | Improve sm90 mixed dtype kernel |
| `pr-cutlass-1932` | upstream-code | [`sources/prs/cutlass/PR-1932.md`](../sources/prs/cutlass/PR-1932.md) | Blockwise Scaling for FP8 |
| `pr-cutlass-1993` | upstream-code | [`sources/prs/cutlass/PR-1993.md`](../sources/prs/cutlass/PR-1993.md) | bugfix generic-k code in top-k with softmax |
| `pr-cutlass-2033` | upstream-code | [`sources/prs/cutlass/PR-2033.md`](../sources/prs/cutlass/PR-2033.md) | [EVT] Add support for Row/Col broadcast PtrArray |
| `pr-cutlass-2037` | upstream-code | [`sources/prs/cutlass/PR-2037.md`](../sources/prs/cutlass/PR-2037.md) | Groupwise scaling along M for FP8 gemm |
| `pr-cutlass-2095` | upstream-code | [`sources/prs/cutlass/PR-2095.md`](../sources/prs/cutlass/PR-2095.md) | Improvements for: Groupwise scaling along M for FP8 gemm |
| `pr-cutlass-2123` | upstream-code | [`sources/prs/cutlass/PR-2123.md`](../sources/prs/cutlass/PR-2123.md) | Hopper Grouped GEMM support for FP8 Accum |
| `pr-cutlass-2130` | upstream-code | [`sources/prs/cutlass/PR-2130.md`](../sources/prs/cutlass/PR-2130.md) | Flash MLA support |
| `pr-cutlass-2134` | upstream-code | [`sources/prs/cutlass/PR-2134.md`](../sources/prs/cutlass/PR-2134.md) | Flash MLA Support - Step 2 |
| `pr-cutlass-2139` | upstream-code | [`sources/prs/cutlass/PR-2139.md`](../sources/prs/cutlass/PR-2139.md) | Blockwise and Groupwise GEMM for Blackwell and Improvements for Hopper |
| `pr-cutlass-2161` | upstream-code | [`sources/prs/cutlass/PR-2161.md`](../sources/prs/cutlass/PR-2161.md) | Blockwise Improvement and Programmatic Dependent Launch |
| `pr-cutlass-2167` | upstream-code | [`sources/prs/cutlass/PR-2167.md`](../sources/prs/cutlass/PR-2167.md) | Fix sm100 gemm wrong static constexpr that breaks compilation on Windows |
| `pr-cutlass-2172` | upstream-code | [`sources/prs/cutlass/PR-2172.md`](../sources/prs/cutlass/PR-2172.md) | Fix SM90 beta=1 hang and stream-K launch errors |
| `pr-cutlass-2185` | upstream-code | [`sources/prs/cutlass/PR-2185.md`](../sources/prs/cutlass/PR-2185.md) | v3.9 |
| `pr-cutlass-2203` | upstream-code | [`sources/prs/cutlass/PR-2203.md`](../sources/prs/cutlass/PR-2203.md) | v3.9 update |
| `pr-cutlass-2220` | upstream-code | [`sources/prs/cutlass/PR-2220.md`](../sources/prs/cutlass/PR-2220.md) | Set EpiTile correctly when TileN is not divisible by 32 |
| `pr-cutlass-2256` | upstream-code | [`sources/prs/cutlass/PR-2256.md`](../sources/prs/cutlass/PR-2256.md) | Use cudaMemcpyAsync in gemm grouped with kRequiresPrecomputation sche… |
| `pr-cutlass-2267` | upstream-code | [`sources/prs/cutlass/PR-2267.md`](../sources/prs/cutlass/PR-2267.md) | war to fix blackwell grouped groupwise hang |
| `pr-cutlass-2270` | upstream-code | [`sources/prs/cutlass/PR-2270.md`](../sources/prs/cutlass/PR-2270.md) | hopper-blockwise-generalization-optimization |
| `pr-cutlass-2291` | upstream-code | [`sources/prs/cutlass/PR-2291.md`](../sources/prs/cutlass/PR-2291.md) | Correct divmod order in example 77 (blackwell fmha) |
| `pr-cutlass-2292` | upstream-code | [`sources/prs/cutlass/PR-2292.md`](../sources/prs/cutlass/PR-2292.md) | Handle get_masked_trip_count for small length in fmha example |
| `pr-cutlass-2333` | upstream-code | [`sources/prs/cutlass/PR-2333.md`](../sources/prs/cutlass/PR-2333.md) | Fix epilogue::thread::Convert cannot be used with DefaultEpilogue |
| `pr-cutlass-2366` | upstream-code | [`sources/prs/cutlass/PR-2366.md`](../sources/prs/cutlass/PR-2366.md) | [ex77] fix mla split; add fwd lse; add bwd varlen |
| `pr-cutlass-2378` | upstream-code | [`sources/prs/cutlass/PR-2378.md`](../sources/prs/cutlass/PR-2378.md) | support fp16 accmulator for sm89 fp8 mma |
| `pr-cutlass-2466` | upstream-code | [`sources/prs/cutlass/PR-2466.md`](../sources/prs/cutlass/PR-2466.md) | Example 77 add blackwell fmha bwd for MLA shape |
| `pr-cutlass-2472` | upstream-code | [`sources/prs/cutlass/PR-2472.md`](../sources/prs/cutlass/PR-2472.md) | Add Blackwell MLA forward (shape: d=192, dv=128) implementation |
| `pr-cutlass-2480` | upstream-code | [`sources/prs/cutlass/PR-2480.md`](../sources/prs/cutlass/PR-2480.md) | Feature/add bottom causal mask |
| `pr-cutlass-2492` | upstream-code | [`sources/prs/cutlass/PR-2492.md`](../sources/prs/cutlass/PR-2492.md) | fix: examples/cute/tutorial/blackwell/04_mma_tma_2sm_sm100.cu GridDim miscalculated |
| `pr-cutlass-2596` | upstream-code | [`sources/prs/cutlass/PR-2596.md`](../sources/prs/cutlass/PR-2596.md) | Fix broken imports in heuristics_provider.py |
| `pr-cutlass-2599` | upstream-code | [`sources/prs/cutlass/PR-2599.md`](../sources/prs/cutlass/PR-2599.md) | fix gqa issue for blackwell fmha.py |
| `pr-cutlass-2713` | upstream-code | [`sources/prs/cutlass/PR-2713.md`](../sources/prs/cutlass/PR-2713.md) | DistGEMM bug fixes |
| `pr-cutlass-2719` | upstream-code | [`sources/prs/cutlass/PR-2719.md`](../sources/prs/cutlass/PR-2719.md) | Support PDL for SM90 Array TMA GEMM |
| `pr-cutlass-2746` | upstream-code | [`sources/prs/cutlass/PR-2746.md`](../sources/prs/cutlass/PR-2746.md) | Support for GEMM-K=0 for Blackwell Grouped GEMMs |
| `pr-cutlass-2750` | upstream-code | [`sources/prs/cutlass/PR-2750.md`](../sources/prs/cutlass/PR-2750.md) | Add tutorial fp16_gemm_1 |
| `pr-cutlass-2790` | upstream-code | [`sources/prs/cutlass/PR-2790.md`](../sources/prs/cutlass/PR-2790.md) | Blockscaled Ragged Contiguous Grouped Gemm for MoEs |
| `pr-cutlass-2865` | upstream-code | [`sources/prs/cutlass/PR-2865.md`](../sources/prs/cutlass/PR-2865.md) | [Bug Fix]Bypass launch grids for SM120 Kernel with SM90 Mainloop & SM100 TileScheduler |
| `pr-cutlass-2875` | upstream-code | [`sources/prs/cutlass/PR-2875.md`](../sources/prs/cutlass/PR-2875.md) | [cute] Add constexpr specifier to make_tiled_copy |
| `pr-cutlass-2881` | upstream-code | [`sources/prs/cutlass/PR-2881.md`](../sources/prs/cutlass/PR-2881.md) | new example with TMA prefetch feature targeting for DRAM latency boun… |
| `pr-cutlass-2917` | upstream-code | [`sources/prs/cutlass/PR-2917.md`](../sources/prs/cutlass/PR-2917.md) | New RMS Norm example with unit tests |
| `pr-cutlass-2921` | upstream-code | [`sources/prs/cutlass/PR-2921.md`](../sources/prs/cutlass/PR-2921.md) | Fix incorrect tensor layout strides in Blackwell MMA tutorial comments |
| `pr-cutlass-2946` | upstream-code | [`sources/prs/cutlass/PR-2946.md`](../sources/prs/cutlass/PR-2946.md) | [Cutlass profiler] Fix SM100 FP8 nosmem epilogue shape_div “Divisibility Condition” for non‑multiple‑of‑64 N tiles |
| `pr-cutlass-2965` | upstream-code | [`sources/prs/cutlass/PR-2965.md`](../sources/prs/cutlass/PR-2965.md) | [Bug Fix]Set NumSplitsM to 1 when TileShapeM < 128 in sm90 fp8 blockwise scaling CollectiveMma |
| `pr-cutlass-2995` | upstream-code | [`sources/prs/cutlass/PR-2995.md`](../sources/prs/cutlass/PR-2995.md) | [CuTeDSL] Fix: SM100 block-scale gemm overlapping accumulator |
| `pr-cutlass-3021` | upstream-code | [`sources/prs/cutlass/PR-3021.md`](../sources/prs/cutlass/PR-3021.md) | [Cute-DSL] Add option for issue_clc_query without multicast |
| `pr-cutlass-3055` | upstream-code | [`sources/prs/cutlass/PR-3055.md`](../sources/prs/cutlass/PR-3055.md) | Replace std::min with cute::min in sm120 blockwise scaling device functions |
| `pr-cutlass-3091` | upstream-code | [`sources/prs/cutlass/PR-3091.md`](../sources/prs/cutlass/PR-3091.md) | [Hopper CuTeDSL] Add grouped GEMM kernel example |
| `pr-cutlass-3092` | upstream-code | [`sources/prs/cutlass/PR-3092.md`](../sources/prs/cutlass/PR-3092.md) | Support for Group GEMM in CUTLASS Profiler for GeForce and Spark |
| `pr-cutlass-3106` | upstream-code | [`sources/prs/cutlass/PR-3106.md`](../sources/prs/cutlass/PR-3106.md) | [CLI] add cutedsl fp16 gemm tutorial from 2 to 6 |
| `pr-cutlass-3130` | upstream-code | [`sources/prs/cutlass/PR-3130.md`](../sources/prs/cutlass/PR-3130.md) | Update blackwell tutorial to be compatible with 4.5-dev version |
| `pr-cutlass-3149` | upstream-code | [`sources/prs/cutlass/PR-3149.md`](../sources/prs/cutlass/PR-3149.md) | [Hopper CuTeDSL] Add FP8 GEMM with 2xAcc |
| `pr-cutlass-3176` | upstream-code | [`sources/prs/cutlass/PR-3176.md`](../sources/prs/cutlass/PR-3176.md) | Small Tile N BlockScaled GEMM + Grouped GEMM on SM12x |
| `pr-cutlass-3184` | upstream-code | [`sources/prs/cutlass/PR-3184.md`](../sources/prs/cutlass/PR-3184.md) | Add Snake activation functor for EVT |

<a id="deepseek-aideepgemm"></a>
## deepseek-ai/DeepGEMM

27 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-deepgemm-103` | upstream-code | [`sources/prs/deepgemm/PR-103.md`](../sources/prs/deepgemm/PR-103.md) | Grouped GEMM skip useless computation for unaligned Ms |
| `pr-deepgemm-112` | upstream-code | [`sources/prs/deepgemm/PR-112.md`](../sources/prs/deepgemm/PR-112.md) | Add more GPU architectures support |
| `pr-deepgemm-113` | upstream-code | [`sources/prs/deepgemm/PR-113.md`](../sources/prs/deepgemm/PR-113.md) | Fix illegal memory address when skipping -1 m indices |
| `pr-deepgemm-115` | upstream-code | [`sources/prs/deepgemm/PR-115.md`](../sources/prs/deepgemm/PR-115.md) | Fixed the bug in get_swizzle_mode function related to elem_size setting. |
| `pr-deepgemm-157` | upstream-code | [`sources/prs/deepgemm/PR-157.md`](../sources/prs/deepgemm/PR-157.md) | Add sm_100f support and make nvcc 13 happy |
| `pr-deepgemm-158` | upstream-code | [`sources/prs/deepgemm/PR-158.md`](../sources/prs/deepgemm/PR-158.md) | Fix inappropriate configs for some small shapes |
| `pr-deepgemm-163` | upstream-code | [`sources/prs/deepgemm/PR-163.md`](../sources/prs/deepgemm/PR-163.md) | Make various updates and fixes |
| `pr-deepgemm-164` | upstream-code | [`sources/prs/deepgemm/PR-164.md`](../sources/prs/deepgemm/PR-164.md) | BF16 support |
| `pr-deepgemm-168` | upstream-code | [`sources/prs/deepgemm/PR-168.md`](../sources/prs/deepgemm/PR-168.md) | Fix performance issue of m-grouped contiguous GEMMs. |
| `pr-deepgemm-193` | upstream-code | [`sources/prs/deepgemm/PR-193.md`](../sources/prs/deepgemm/PR-193.md) | Fix multicast bug and optimize masked GEMM |
| `pr-deepgemm-198` | upstream-code | [`sources/prs/deepgemm/PR-198.md`](../sources/prs/deepgemm/PR-198.md) | Make various updates and fixes |
| `pr-deepgemm-226` | upstream-code | [`sources/prs/deepgemm/PR-226.md`](../sources/prs/deepgemm/PR-226.md) | fix: prevent int32 overflow in k-grouped GEMM size calculations |
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

<a id="deepseek-aitilekernels"></a>
## deepseek-ai/TileKernels

1 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-tilekernels-1` | upstream-code | [`sources/prs/tilekernels/PR-1.md`](../sources/prs/tilekernels/PR-1.md) | Revise Engram Kernel Comments |

<a id="flashinfer-aiflashinfer"></a>
## flashinfer-ai/flashinfer

779 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-flashinfer-1007` | upstream-code | [`sources/prs/flashinfer/PR-1007.md`](../sources/prs/flashinfer/PR-1007.md) | feat: update decode attention APIs |
| `pr-flashinfer-1008` | upstream-code | [`sources/prs/flashinfer/PR-1008.md`](../sources/prs/flashinfer/PR-1008.md) | bugfix: Fix illegal memory access due to custom mask ptr |
| `pr-flashinfer-1013` | upstream-code | [`sources/prs/flashinfer/PR-1013.md`](../sources/prs/flashinfer/PR-1013.md) | bugfix: import wrapper of mla decode |
| `pr-flashinfer-1014` | upstream-code | [`sources/prs/flashinfer/PR-1014.md`](../sources/prs/flashinfer/PR-1014.md) | misc: fix instrument code for mla profiler |
| `pr-flashinfer-1015` | upstream-code | [`sources/prs/flashinfer/PR-1015.md`](../sources/prs/flashinfer/PR-1015.md) | add multi-item scoring |
| `pr-flashinfer-1025` | upstream-code | [`sources/prs/flashinfer/PR-1025.md`](../sources/prs/flashinfer/PR-1025.md) | feat: ragged tensor padding kernel for blackwell kernel alignment |
| `pr-flashinfer-1028` | upstream-code | [`sources/prs/flashinfer/PR-1028.md`](../sources/prs/flashinfer/PR-1028.md) | bugfix: fix custom mask not be reseted after convert custom mask into causal or non-causal |
| `pr-flashinfer-1029` | upstream-code | [`sources/prs/flashinfer/PR-1029.md`](../sources/prs/flashinfer/PR-1029.md) | fix: add zero init for KV tiled copy |
| `pr-flashinfer-1033` | upstream-code | [`sources/prs/flashinfer/PR-1033.md`](../sources/prs/flashinfer/PR-1033.md) | feat: add functional per-head FP8 quantization for FA3 |
| `pr-flashinfer-1035` | upstream-code | [`sources/prs/flashinfer/PR-1035.md`](../sources/prs/flashinfer/PR-1035.md) | feat: Softmax free sampling |
| `pr-flashinfer-1039` | upstream-code | [`sources/prs/flashinfer/PR-1039.md`](../sources/prs/flashinfer/PR-1039.md) | [nvidia] initial support for blackwell kernels |
| `pr-flashinfer-1050` | upstream-code | [`sources/prs/flashinfer/PR-1050.md`](../sources/prs/flashinfer/PR-1050.md) | fix: top_k_mask_logits hangs on -inf inputs |
| `pr-flashinfer-1051` | upstream-code | [`sources/prs/flashinfer/PR-1051.md`](../sources/prs/flashinfer/PR-1051.md) | [nvidia] Add Blackwell FMHA decode kernel from TRT-LLM |
| `pr-flashinfer-1052` | upstream-code | [`sources/prs/flashinfer/PR-1052.md`](../sources/prs/flashinfer/PR-1052.md) | Benchmark: POD vs batched prefill |
| `pr-flashinfer-1054` | upstream-code | [`sources/prs/flashinfer/PR-1054.md`](../sources/prs/flashinfer/PR-1054.md) | Fix KV chunking for POD.  |
| `pr-flashinfer-1055` | upstream-code | [`sources/prs/flashinfer/PR-1055.md`](../sources/prs/flashinfer/PR-1055.md) | bugfix: temporally disable split-kv in blackwell mla |
| `pr-flashinfer-1056` | upstream-code | [`sources/prs/flashinfer/PR-1056.md`](../sources/prs/flashinfer/PR-1056.md) | bugfix: remove device allocation |
| `pr-flashinfer-1059` | upstream-code | [`sources/prs/flashinfer/PR-1059.md`](../sources/prs/flashinfer/PR-1059.md) | Parameterize prefix mask call (needed by POD-Attention) |
| `pr-flashinfer-1060` | upstream-code | [`sources/prs/flashinfer/PR-1060.md`](../sources/prs/flashinfer/PR-1060.md) | bugfix: move `cum_m` calculation inside kernels |
| `pr-flashinfer-1071` | upstream-code | [`sources/prs/flashinfer/PR-1071.md`](../sources/prs/flashinfer/PR-1071.md) | bugfix: adding lse output to blackwell fmha kernels |
| `pr-flashinfer-1072` | upstream-code | [`sources/prs/flashinfer/PR-1072.md`](../sources/prs/flashinfer/PR-1072.md) | bugfix: follow user-specified sm_scale for blackwell cutlass fmha |
| `pr-flashinfer-1086` | upstream-code | [`sources/prs/flashinfer/PR-1086.md`](../sources/prs/flashinfer/PR-1086.md) | perf: accelerate blackwell grouped gemm |
| `pr-flashinfer-1087` | upstream-code | [`sources/prs/flashinfer/PR-1087.md`](../sources/prs/flashinfer/PR-1087.md) | bugfix: fix fp8 attention kernels aot compilation issue |
| `pr-flashinfer-1089` | upstream-code | [`sources/prs/flashinfer/PR-1089.md`](../sources/prs/flashinfer/PR-1089.md) | comm: refactor and initialize `flashinfer.comm` module |
| `pr-flashinfer-1096` | upstream-code | [`sources/prs/flashinfer/PR-1096.md`](../sources/prs/flashinfer/PR-1096.md) | feat: add trtllm all-reduce (non-MoE) |
| `pr-flashinfer-1106` | upstream-code | [`sources/prs/flashinfer/PR-1106.md`](../sources/prs/flashinfer/PR-1106.md) | bugfix: host-precomuted plan function for blackwell fmha |
| `pr-flashinfer-1108` | upstream-code | [`sources/prs/flashinfer/PR-1108.md`](../sources/prs/flashinfer/PR-1108.md) | feat: add trtllm moe_allreduce_fusion |
| `pr-flashinfer-1113` | upstream-code | [`sources/prs/flashinfer/PR-1113.md`](../sources/prs/flashinfer/PR-1113.md) | Add CUTLASS fused moe kernels from TensorRT-LLM. |
| `pr-flashinfer-1114` | upstream-code | [`sources/prs/flashinfer/PR-1114.md`](../sources/prs/flashinfer/PR-1114.md) | bugfix: Fix test and output shape of fp4 quantize |
| `pr-flashinfer-1116` | upstream-code | [`sources/prs/flashinfer/PR-1116.md`](../sources/prs/flashinfer/PR-1116.md) | hotfix: fix the blackwell fmha stream |
| `pr-flashinfer-1117` | upstream-code | [`sources/prs/flashinfer/PR-1117.md`](../sources/prs/flashinfer/PR-1117.md) | [Feature] Support PDL for batch Prefill and Decode |
| `pr-flashinfer-1129` | upstream-code | [`sources/prs/flashinfer/PR-1129.md`](../sources/prs/flashinfer/PR-1129.md) | Fix pointer dtype bug in rope |
| `pr-flashinfer-1131` | upstream-code | [`sources/prs/flashinfer/PR-1131.md`](../sources/prs/flashinfer/PR-1131.md) | feat: add trtllm all-reduce fusion |
| `pr-flashinfer-1134` | upstream-code | [`sources/prs/flashinfer/PR-1134.md`](../sources/prs/flashinfer/PR-1134.md) | MNNVL MoE All-to-All Support |
| `pr-flashinfer-1136` | upstream-code | [`sources/prs/flashinfer/PR-1136.md`](../sources/prs/flashinfer/PR-1136.md) | fix: negative zero by type trait --> binary value |
| `pr-flashinfer-1137` | upstream-code | [`sources/prs/flashinfer/PR-1137.md`](../sources/prs/flashinfer/PR-1137.md) | [feat] add unified batch attention w/ correctness tests. |
| `pr-flashinfer-1140` | upstream-code | [`sources/prs/flashinfer/PR-1140.md`](../sources/prs/flashinfer/PR-1140.md) | Fix FA2 and FA3 multi-item scoring and cuda illegal memory access error |
| `pr-flashinfer-1148` | upstream-code | [`sources/prs/flashinfer/PR-1148.md`](../sources/prs/flashinfer/PR-1148.md) | [fix] fix precision errors when applying causal mask on Qwen-2.5 series models |
| `pr-flashinfer-1153` | upstream-code | [`sources/prs/flashinfer/PR-1153.md`](../sources/prs/flashinfer/PR-1153.md) | feat: Fused temperature online softmax kernel |
| `pr-flashinfer-1158` | upstream-code | [`sources/prs/flashinfer/PR-1158.md`](../sources/prs/flashinfer/PR-1158.md) | Add more logging to TRTLLM-GEN debug trace (NFC) |
| `pr-flashinfer-1159` | upstream-code | [`sources/prs/flashinfer/PR-1159.md`](../sources/prs/flashinfer/PR-1159.md) | feat: add finalize_moe_allreduce from trtllm |
| `pr-flashinfer-1160` | upstream-code | [`sources/prs/flashinfer/PR-1160.md`](../sources/prs/flashinfer/PR-1160.md) | feat: nvshmem python bindings |
| `pr-flashinfer-1161` | upstream-code | [`sources/prs/flashinfer/PR-1161.md`](../sources/prs/flashinfer/PR-1161.md) | feat: update non-fused moe |
| `pr-flashinfer-1162` | upstream-code | [`sources/prs/flashinfer/PR-1162.md`](../sources/prs/flashinfer/PR-1162.md) | refactor: communication module |
| `pr-flashinfer-1164` | upstream-code | [`sources/prs/flashinfer/PR-1164.md`](../sources/prs/flashinfer/PR-1164.md) | feat: enable and update all-reduce fused quantization |
| `pr-flashinfer-1168` | upstream-code | [`sources/prs/flashinfer/PR-1168.md`](../sources/prs/flashinfer/PR-1168.md) | Fix missing symbols in trtllm_utils.so |
| `pr-flashinfer-1170` | upstream-code | [`sources/prs/flashinfer/PR-1170.md`](../sources/prs/flashinfer/PR-1170.md) | feat: logits processor fustion rule for temperature softmax |
| `pr-flashinfer-1176` | upstream-code | [`sources/prs/flashinfer/PR-1176.md`](../sources/prs/flashinfer/PR-1176.md) | Expose fp4 blockscale swizzling kernel |
| `pr-flashinfer-1177` | upstream-code | [`sources/prs/flashinfer/PR-1177.md`](../sources/prs/flashinfer/PR-1177.md) | [feat] support block sparse attention w/ variable block sizes and head-wise sparse patterns |
| `pr-flashinfer-1178` | upstream-code | [`sources/prs/flashinfer/PR-1178.md`](../sources/prs/flashinfer/PR-1178.md) | bugfix: softmax NaN results caused by large -inf masks |
| `pr-flashinfer-1179` | upstream-code | [`sources/prs/flashinfer/PR-1179.md`](../sources/prs/flashinfer/PR-1179.md) | Add mypy to pre-commit |
| `pr-flashinfer-1187` | upstream-code | [`sources/prs/flashinfer/PR-1187.md`](../sources/prs/flashinfer/PR-1187.md) | Feature/cudnn dynamic cubin |
| `pr-flashinfer-1189` | upstream-code | [`sources/prs/flashinfer/PR-1189.md`](../sources/prs/flashinfer/PR-1189.md) | update trtllm-gen decode attention kernel launcher |
| `pr-flashinfer-1190` | upstream-code | [`sources/prs/flashinfer/PR-1190.md`](../sources/prs/flashinfer/PR-1190.md) | feat: support green ctx creation by a list of SM counts |
| `pr-flashinfer-1198` | upstream-code | [`sources/prs/flashinfer/PR-1198.md`](../sources/prs/flashinfer/PR-1198.md) | bugfix: fix blackwell fmha hanging issue for empty kv_len |
| `pr-flashinfer-1200` | upstream-code | [`sources/prs/flashinfer/PR-1200.md`](../sources/prs/flashinfer/PR-1200.md) | [feat] optimize persistent batch attention perf. |
| `pr-flashinfer-1206` | upstream-code | [`sources/prs/flashinfer/PR-1206.md`](../sources/prs/flashinfer/PR-1206.md) | [fix] fix BatchAttention CTA_TILE_KV mask issue |
| `pr-flashinfer-1208` | upstream-code | [`sources/prs/flashinfer/PR-1208.md`](../sources/prs/flashinfer/PR-1208.md) | Fix the issue with auxillary kernel launch and grid dim calculation |
| `pr-flashinfer-1209` | upstream-code | [`sources/prs/flashinfer/PR-1209.md`](../sources/prs/flashinfer/PR-1209.md) | Add DeepGEMM kernels |
| `pr-flashinfer-1212` | upstream-code | [`sources/prs/flashinfer/PR-1212.md`](../sources/prs/flashinfer/PR-1212.md) | feat: trtllm-gen fp8 moe kernels |
| `pr-flashinfer-1213` | upstream-code | [`sources/prs/flashinfer/PR-1213.md`](../sources/prs/flashinfer/PR-1213.md) | [comm] TRT-LLM's Multi-Node NVLink All-Reduce Kernel |
| `pr-flashinfer-1214` | upstream-code | [`sources/prs/flashinfer/PR-1214.md`](../sources/prs/flashinfer/PR-1214.md) | Feature/sm100 low latency nvfp4 kernels |
| `pr-flashinfer-1217` | upstream-code | [`sources/prs/flashinfer/PR-1217.md`](../sources/prs/flashinfer/PR-1217.md) | [TVM] Remove `enable_pdl` from TVM binding interface |
| `pr-flashinfer-1221` | upstream-code | [`sources/prs/flashinfer/PR-1221.md`](../sources/prs/flashinfer/PR-1221.md) | Enable cudnn decode and add tests for the cudnn decode kernel |
| `pr-flashinfer-1222` | upstream-code | [`sources/prs/flashinfer/PR-1222.md`](../sources/prs/flashinfer/PR-1222.md) | feat: add trtllm-gen mla cubin |
| `pr-flashinfer-1227` | upstream-code | [`sources/prs/flashinfer/PR-1227.md`](../sources/prs/flashinfer/PR-1227.md) | Fix missing hash in the cudnn cubin path |
| `pr-flashinfer-1230` | upstream-code | [`sources/prs/flashinfer/PR-1230.md`](../sources/prs/flashinfer/PR-1230.md) | feat: Add non-causal cudnn prefill kernels |
| `pr-flashinfer-1234` | upstream-code | [`sources/prs/flashinfer/PR-1234.md`](../sources/prs/flashinfer/PR-1234.md) | bugfix: support uint8_t for vec_t class template |
| `pr-flashinfer-1239` | upstream-code | [`sources/prs/flashinfer/PR-1239.md`](../sources/prs/flashinfer/PR-1239.md) | add trtllm-gen context attention |
| `pr-flashinfer-1240` | upstream-code | [`sources/prs/flashinfer/PR-1240.md`](../sources/prs/flashinfer/PR-1240.md) | Patch fp8 cubin availability |
| `pr-flashinfer-1241` | upstream-code | [`sources/prs/flashinfer/PR-1241.md`](../sources/prs/flashinfer/PR-1241.md) | feat: Support MXFP8 x MXFP4 CUTLASS grouped GEMM |
| `pr-flashinfer-1242` | upstream-code | [`sources/prs/flashinfer/PR-1242.md`](../sources/prs/flashinfer/PR-1242.md) | Add trtllm-gen attention mha kernel with FP8 Q/K/V and FP8 output |
| `pr-flashinfer-1245` | upstream-code | [`sources/prs/flashinfer/PR-1245.md`](../sources/prs/flashinfer/PR-1245.md) | Mnnvl memory with custom communicator |
| `pr-flashinfer-1249` | upstream-code | [`sources/prs/flashinfer/PR-1249.md`](../sources/prs/flashinfer/PR-1249.md) | Remove sm100+ requirment for trtllm allreduce kernels |
| `pr-flashinfer-1251` | upstream-code | [`sources/prs/flashinfer/PR-1251.md`](../sources/prs/flashinfer/PR-1251.md) | Reduce the JIT compilation time of gen_gemm_sm100_module |
| `pr-flashinfer-1254` | upstream-code | [`sources/prs/flashinfer/PR-1254.md`](../sources/prs/flashinfer/PR-1254.md) | fix: correctly pass k_scale and v_scale to run() in forward_return_lse (#1023) |
| `pr-flashinfer-1255` | upstream-code | [`sources/prs/flashinfer/PR-1255.md`](../sources/prs/flashinfer/PR-1255.md) | TRT-LLM's Multi-Node NVLink AR + fused RMSNorm kernel |
| `pr-flashinfer-1258` | upstream-code | [`sources/prs/flashinfer/PR-1258.md`](../sources/prs/flashinfer/PR-1258.md) | feat: enable trtllm-gen mla MTP |
| `pr-flashinfer-1264` | upstream-code | [`sources/prs/flashinfer/PR-1264.md`](../sources/prs/flashinfer/PR-1264.md) | init add gemm fp8 using cudnn backend |
| `pr-flashinfer-1265` | upstream-code | [`sources/prs/flashinfer/PR-1265.md`](../sources/prs/flashinfer/PR-1265.md) | Made AR output optional + esthetic changes |
| `pr-flashinfer-1266` | upstream-code | [`sources/prs/flashinfer/PR-1266.md`](../sources/prs/flashinfer/PR-1266.md) | feat: add masked deepgemm support and benchmarking |
| `pr-flashinfer-1267` | upstream-code | [`sources/prs/flashinfer/PR-1267.md`](../sources/prs/flashinfer/PR-1267.md) | Bug fix: fix duplicate launch in POD |
| `pr-flashinfer-1272` | upstream-code | [`sources/prs/flashinfer/PR-1272.md`](../sources/prs/flashinfer/PR-1272.md) | Add shuffle matrix flag |
| `pr-flashinfer-1275` | upstream-code | [`sources/prs/flashinfer/PR-1275.md`](../sources/prs/flashinfer/PR-1275.md) | Add missing import in comm/__init__,py |
| `pr-flashinfer-1278` | upstream-code | [`sources/prs/flashinfer/PR-1278.md`](../sources/prs/flashinfer/PR-1278.md) | hotfix: fix deepgemm artifactory hash |
| `pr-flashinfer-1280` | upstream-code | [`sources/prs/flashinfer/PR-1280.md`](../sources/prs/flashinfer/PR-1280.md) | fix: update trtllm-gen fmha benchmark |
| `pr-flashinfer-1281` | upstream-code | [`sources/prs/flashinfer/PR-1281.md`](../sources/prs/flashinfer/PR-1281.md) | Unify groupwise fp8 GEMM test |
| `pr-flashinfer-1283` | upstream-code | [`sources/prs/flashinfer/PR-1283.md`](../sources/prs/flashinfer/PR-1283.md) | Add native cudnn_decode for improved cudnn decode performance |
| `pr-flashinfer-1284` | upstream-code | [`sources/prs/flashinfer/PR-1284.md`](../sources/prs/flashinfer/PR-1284.md) | Convert scale_factor from scalar to Tensor in trt_allreduce_fusion |
| `pr-flashinfer-1286` | upstream-code | [`sources/prs/flashinfer/PR-1286.md`](../sources/prs/flashinfer/PR-1286.md) | fix multiCtasKvScratchPtr misalignment issue (new one) |
| `pr-flashinfer-1287` | upstream-code | [`sources/prs/flashinfer/PR-1287.md`](../sources/prs/flashinfer/PR-1287.md) | Bug fix: guard fp8 e8m0 and e2m1 compile  |
| `pr-flashinfer-1288` | upstream-code | [`sources/prs/flashinfer/PR-1288.md`](../sources/prs/flashinfer/PR-1288.md) | add mm_fp4 use cudnn backend |
| `pr-flashinfer-1289` | upstream-code | [`sources/prs/flashinfer/PR-1289.md`](../sources/prs/flashinfer/PR-1289.md) | refactor: refactor trtllm-gen attention kernel integration code |
| `pr-flashinfer-1290` | upstream-code | [`sources/prs/flashinfer/PR-1290.md`](../sources/prs/flashinfer/PR-1290.md) | [fix] fix integer overflow in FA2 customized_mask & add buffer overflow warning. |
| `pr-flashinfer-1291` | upstream-code | [`sources/prs/flashinfer/PR-1291.md`](../sources/prs/flashinfer/PR-1291.md) | Remove FAST_BUILD FLAG for MOE |
| `pr-flashinfer-1292` | upstream-code | [`sources/prs/flashinfer/PR-1292.md`](../sources/prs/flashinfer/PR-1292.md) | refactor: Improved metainfo for trtllm-gen fmha |
| `pr-flashinfer-1294` | upstream-code | [`sources/prs/flashinfer/PR-1294.md`](../sources/prs/flashinfer/PR-1294.md) | Update cutlass fp4 moe kernels |
| `pr-flashinfer-1296` | upstream-code | [`sources/prs/flashinfer/PR-1296.md`](../sources/prs/flashinfer/PR-1296.md) | add cutlass backend for mm_fp4 |
| `pr-flashinfer-1297` | upstream-code | [`sources/prs/flashinfer/PR-1297.md`](../sources/prs/flashinfer/PR-1297.md) | feat: Add weight layout option for trtllm-gen fused moe |
| `pr-flashinfer-1298` | upstream-code | [`sources/prs/flashinfer/PR-1298.md`](../sources/prs/flashinfer/PR-1298.md) | perfix: use lightweight API to query device property |
| `pr-flashinfer-1302` | upstream-code | [`sources/prs/flashinfer/PR-1302.md`](../sources/prs/flashinfer/PR-1302.md) | minor: some fix and cleanup for trtllm-gen mha |
| `pr-flashinfer-1303` | upstream-code | [`sources/prs/flashinfer/PR-1303.md`](../sources/prs/flashinfer/PR-1303.md) | bugfix: ensure graph is captured and executed on the same stream to avoid rep… |
| `pr-flashinfer-1305` | upstream-code | [`sources/prs/flashinfer/PR-1305.md`](../sources/prs/flashinfer/PR-1305.md) | [Feature] SM level profiler  |
| `pr-flashinfer-1306` | upstream-code | [`sources/prs/flashinfer/PR-1306.md`](../sources/prs/flashinfer/PR-1306.md) | Heuristics + testing unification + CUDA Graphs |
| `pr-flashinfer-1307` | upstream-code | [`sources/prs/flashinfer/PR-1307.md`](../sources/prs/flashinfer/PR-1307.md) | Fix the bug of the kernel-selection heuristic in trtllm-gen |
| `pr-flashinfer-1309` | upstream-code | [`sources/prs/flashinfer/PR-1309.md`](../sources/prs/flashinfer/PR-1309.md) | Refactor Fused Moe Module |
| `pr-flashinfer-1310` | upstream-code | [`sources/prs/flashinfer/PR-1310.md`](../sources/prs/flashinfer/PR-1310.md) | Support loading autotuned results from json for cutlass fp4 moe backends |
| `pr-flashinfer-1316` | upstream-code | [`sources/prs/flashinfer/PR-1316.md`](../sources/prs/flashinfer/PR-1316.md) | minor: add trtllm_gen_mla benchmark |
| `pr-flashinfer-1317` | upstream-code | [`sources/prs/flashinfer/PR-1317.md`](../sources/prs/flashinfer/PR-1317.md) | Allow cudnn prefill kernels to be called natively |
| `pr-flashinfer-1318` | upstream-code | [`sources/prs/flashinfer/PR-1318.md`](../sources/prs/flashinfer/PR-1318.md) | feat: support output nvfp4 in trtllm-gen function call. |
| `pr-flashinfer-1319` | upstream-code | [`sources/prs/flashinfer/PR-1319.md`](../sources/prs/flashinfer/PR-1319.md) | Make Fp8 MoE routing_bias optional |
| `pr-flashinfer-1320` | upstream-code | [`sources/prs/flashinfer/PR-1320.md`](../sources/prs/flashinfer/PR-1320.md) | Add blockwise-scaled FP8 GEMM via TRTLLM-Gen. |
| `pr-flashinfer-1321` | upstream-code | [`sources/prs/flashinfer/PR-1321.md`](../sources/prs/flashinfer/PR-1321.md) | Optimizations for TRTLLM MNNVL Allreduce |
| `pr-flashinfer-1322` | upstream-code | [`sources/prs/flashinfer/PR-1322.md`](../sources/prs/flashinfer/PR-1322.md) | feat: Add k_scale and v_scale to persistent attention  |
| `pr-flashinfer-1323` | upstream-code | [`sources/prs/flashinfer/PR-1323.md`](../sources/prs/flashinfer/PR-1323.md) | Addition of flashinfer_benchmark.py for benchmarking routines |
| `pr-flashinfer-1324` | upstream-code | [`sources/prs/flashinfer/PR-1324.md`](../sources/prs/flashinfer/PR-1324.md) | feat: Support logits_soft_cap for Persistent attn; fix kv split limit |
| `pr-flashinfer-1328` | upstream-code | [`sources/prs/flashinfer/PR-1328.md`](../sources/prs/flashinfer/PR-1328.md) | refactor: Improved metainfo for trtllm-gen kernels |
| `pr-flashinfer-1331` | upstream-code | [`sources/prs/flashinfer/PR-1331.md`](../sources/prs/flashinfer/PR-1331.md) | feat: masked layout fp4 gemm using cute-dsl |
| `pr-flashinfer-1333` | upstream-code | [`sources/prs/flashinfer/PR-1333.md`](../sources/prs/flashinfer/PR-1333.md) | add torch float4_e2m1fn_x2 check for cudnn fp4 backend |
| `pr-flashinfer-1334` | upstream-code | [`sources/prs/flashinfer/PR-1334.md`](../sources/prs/flashinfer/PR-1334.md) | [Fix] remove torch 2.8 requirement for FP4 GEMM |
| `pr-flashinfer-1337` | upstream-code | [`sources/prs/flashinfer/PR-1337.md`](../sources/prs/flashinfer/PR-1337.md) | Refactor scripts in benchmarks to use flasinfer.testing.bench_gpu_time |
| `pr-flashinfer-1339` | upstream-code | [`sources/prs/flashinfer/PR-1339.md`](../sources/prs/flashinfer/PR-1339.md) | feat: Fused rope fp8 quantize kernel for MLA |
| `pr-flashinfer-1344` | upstream-code | [`sources/prs/flashinfer/PR-1344.md`](../sources/prs/flashinfer/PR-1344.md) | Fix bench deepgemm setting |
| `pr-flashinfer-1346` | upstream-code | [`sources/prs/flashinfer/PR-1346.md`](../sources/prs/flashinfer/PR-1346.md) | Add trtllm-gen prefill test. Fix related wrapper issue. |
| `pr-flashinfer-1348` | upstream-code | [`sources/prs/flashinfer/PR-1348.md`](../sources/prs/flashinfer/PR-1348.md) | fix: fix trtllm-gen mla error on new interface |
| `pr-flashinfer-1349` | upstream-code | [`sources/prs/flashinfer/PR-1349.md`](../sources/prs/flashinfer/PR-1349.md) | [Bugfix] Change max_size for LRU |
| `pr-flashinfer-1350` | upstream-code | [`sources/prs/flashinfer/PR-1350.md`](../sources/prs/flashinfer/PR-1350.md) | Support passing kv_data_type to MultiLevelCascadeAttentionWrapper.plan() |
| `pr-flashinfer-1354` | upstream-code | [`sources/prs/flashinfer/PR-1354.md`](../sources/prs/flashinfer/PR-1354.md) | cleanup: retire aot-build-utils |
| `pr-flashinfer-1355` | upstream-code | [`sources/prs/flashinfer/PR-1355.md`](../sources/prs/flashinfer/PR-1355.md) | feature: add fp4 mm using trtllm backend |
| `pr-flashinfer-1356` | upstream-code | [`sources/prs/flashinfer/PR-1356.md`](../sources/prs/flashinfer/PR-1356.md) | gen_trtllm_comm_module: fix device capability detection |
| `pr-flashinfer-1358` | upstream-code | [`sources/prs/flashinfer/PR-1358.md`](../sources/prs/flashinfer/PR-1358.md) | [fix] remove (view) transpose to keep consistent with majorness MN requirement. |
| `pr-flashinfer-1360` | upstream-code | [`sources/prs/flashinfer/PR-1360.md`](../sources/prs/flashinfer/PR-1360.md) | support trtllm-gen prefill fp4 output |
| `pr-flashinfer-1361` | upstream-code | [`sources/prs/flashinfer/PR-1361.md`](../sources/prs/flashinfer/PR-1361.md) | Update autotune results for the nvfp4 cutlass moe backends for v0.2.9 |
| `pr-flashinfer-1363` | upstream-code | [`sources/prs/flashinfer/PR-1363.md`](../sources/prs/flashinfer/PR-1363.md) | Support scale factor start index for fp4 mha prefill/decode |
| `pr-flashinfer-1365` | upstream-code | [`sources/prs/flashinfer/PR-1365.md`](../sources/prs/flashinfer/PR-1365.md) | feat: auto deduce use_oneshot from token_num in all-reduce |
| `pr-flashinfer-1369` | upstream-code | [`sources/prs/flashinfer/PR-1369.md`](../sources/prs/flashinfer/PR-1369.md) | Artifact downloading and single sourced artifact path |
| `pr-flashinfer-1371` | upstream-code | [`sources/prs/flashinfer/PR-1371.md`](../sources/prs/flashinfer/PR-1371.md) | bugfix: fixed cutlass fused moe usage of FP4QuantizationSFLayout::SWIZZLED |
| `pr-flashinfer-1374` | upstream-code | [`sources/prs/flashinfer/PR-1374.md`](../sources/prs/flashinfer/PR-1374.md) | Update documentation index |
| `pr-flashinfer-1375` | upstream-code | [`sources/prs/flashinfer/PR-1375.md`](../sources/prs/flashinfer/PR-1375.md) | Unify and modularize decode and prefill test. |
| `pr-flashinfer-1376` | upstream-code | [`sources/prs/flashinfer/PR-1376.md`](../sources/prs/flashinfer/PR-1376.md) | bugfix: Add guard for fp4/fp8 related include headers |
| `pr-flashinfer-1377` | upstream-code | [`sources/prs/flashinfer/PR-1377.md`](../sources/prs/flashinfer/PR-1377.md) | bugfix: do cudnn related error check only when cudnn backend is enabled. |
| `pr-flashinfer-1378` | upstream-code | [`sources/prs/flashinfer/PR-1378.md`](../sources/prs/flashinfer/PR-1378.md) | refactor: download trtllm gemm metadata from server |
| `pr-flashinfer-1384` | upstream-code | [`sources/prs/flashinfer/PR-1384.md`](../sources/prs/flashinfer/PR-1384.md) | Allow BatchPrefillPagedWrapper to call cudnn API |
| `pr-flashinfer-1389` | upstream-code | [`sources/prs/flashinfer/PR-1389.md`](../sources/prs/flashinfer/PR-1389.md) | GPT-OSS Support: Add Blackwell MoE mxfp4 implementation from TRTLLM and Attention Sink |
| `pr-flashinfer-1390` | upstream-code | [`sources/prs/flashinfer/PR-1390.md`](../sources/prs/flashinfer/PR-1390.md) | Adding FP8 benchmark on attention and matmul testing |
| `pr-flashinfer-1392` | upstream-code | [`sources/prs/flashinfer/PR-1392.md`](../sources/prs/flashinfer/PR-1392.md) | Fix flag order |
| `pr-flashinfer-1393` | upstream-code | [`sources/prs/flashinfer/PR-1393.md`](../sources/prs/flashinfer/PR-1393.md) | Add flags to trim down AoT builds |
| `pr-flashinfer-1396` | upstream-code | [`sources/prs/flashinfer/PR-1396.md`](../sources/prs/flashinfer/PR-1396.md) | gpt-oss: Add MXFP8 x MXFP4 CUTLASS MOE for SM100 and BF16 x MXFP4 CUTLASS for SM90 + SwigluBias Activation |
| `pr-flashinfer-1397` | upstream-code | [`sources/prs/flashinfer/PR-1397.md`](../sources/prs/flashinfer/PR-1397.md) | feature: add cutlass as bmm_fp8 backend. |
| `pr-flashinfer-1398` | upstream-code | [`sources/prs/flashinfer/PR-1398.md`](../sources/prs/flashinfer/PR-1398.md) | Fix trtllm moe launcher local_num_experts |
| `pr-flashinfer-1402` | upstream-code | [`sources/prs/flashinfer/PR-1402.md`](../sources/prs/flashinfer/PR-1402.md) | fix shared memory alignment conflict in sampling.cuh |
| `pr-flashinfer-1405` | upstream-code | [`sources/prs/flashinfer/PR-1405.md`](../sources/prs/flashinfer/PR-1405.md) | feature: enable cublas for fp4 gemm when cudnn == 9.11.1 or >= 9.13 |
| `pr-flashinfer-1410` | upstream-code | [`sources/prs/flashinfer/PR-1410.md`](../sources/prs/flashinfer/PR-1410.md) | [bugfix] Fix compilation failure when compiling csrc/trtllm_moe_allreduce_fusion.cu |
| `pr-flashinfer-1412` | upstream-code | [`sources/prs/flashinfer/PR-1412.md`](../sources/prs/flashinfer/PR-1412.md) | Faster weight processing (moe nvfp4) |
| `pr-flashinfer-1413` | upstream-code | [`sources/prs/flashinfer/PR-1413.md`](../sources/prs/flashinfer/PR-1413.md) | Fix crash when pos_encoding_mode is passed as int |
| `pr-flashinfer-1415` | upstream-code | [`sources/prs/flashinfer/PR-1415.md`](../sources/prs/flashinfer/PR-1415.md) | benchmark: trtllm-gen mha with sink, add benchmark args |
| `pr-flashinfer-1416` | upstream-code | [`sources/prs/flashinfer/PR-1416.md`](../sources/prs/flashinfer/PR-1416.md) | Fix missing v_scale for prefill wrapper. |
| `pr-flashinfer-1421` | upstream-code | [`sources/prs/flashinfer/PR-1421.md`](../sources/prs/flashinfer/PR-1421.md) | Remote const qualifier to avoid compilation error |
| `pr-flashinfer-1424` | upstream-code | [`sources/prs/flashinfer/PR-1424.md`](../sources/prs/flashinfer/PR-1424.md) | Fix FusedMoeRunner does not exist error |
| `pr-flashinfer-1427` | upstream-code | [`sources/prs/flashinfer/PR-1427.md`](../sources/prs/flashinfer/PR-1427.md) | refactor: Sink attention AoT |
| `pr-flashinfer-1428` | upstream-code | [`sources/prs/flashinfer/PR-1428.md`](../sources/prs/flashinfer/PR-1428.md) | Fix redundant kernels in moe |
| `pr-flashinfer-1435` | upstream-code | [`sources/prs/flashinfer/PR-1435.md`](../sources/prs/flashinfer/PR-1435.md) | bugfix: fix perf issue by using fp8 graph that can use cublaslt |
| `pr-flashinfer-1438` | upstream-code | [`sources/prs/flashinfer/PR-1438.md`](../sources/prs/flashinfer/PR-1438.md) | Putting back cudnn_batch_prefill_with_kv_cache that was deleted by ruff |
| `pr-flashinfer-1441` | upstream-code | [`sources/prs/flashinfer/PR-1441.md`](../sources/prs/flashinfer/PR-1441.md) | Decouple cutlass config version from flashinfer version |
| `pr-flashinfer-1444` | upstream-code | [`sources/prs/flashinfer/PR-1444.md`](../sources/prs/flashinfer/PR-1444.md) | fix: remote redundant zero_init from trtllm-gen attn |
| `pr-flashinfer-1445` | upstream-code | [`sources/prs/flashinfer/PR-1445.md`](../sources/prs/flashinfer/PR-1445.md) | Add alignment in MxFP8Quantization |
| `pr-flashinfer-1446` | upstream-code | [`sources/prs/flashinfer/PR-1446.md`](../sources/prs/flashinfer/PR-1446.md) | Remove getEnvEnablePDL in favor of enable_pdl parameter |
| `pr-flashinfer-1453` | upstream-code | [`sources/prs/flashinfer/PR-1453.md`](../sources/prs/flashinfer/PR-1453.md) | feat: enable trtllm-gen attn speculative decoding verify by decode |
| `pr-flashinfer-1460` | upstream-code | [`sources/prs/flashinfer/PR-1460.md`](../sources/prs/flashinfer/PR-1460.md) | Fix TRTLLM NVFP4-out attention kernel scale factor dim issue |
| `pr-flashinfer-1463` | upstream-code | [`sources/prs/flashinfer/PR-1463.md`](../sources/prs/flashinfer/PR-1463.md) | fix: remove redundant zero_init reverted by #1459 |
| `pr-flashinfer-1469` | upstream-code | [`sources/prs/flashinfer/PR-1469.md`](../sources/prs/flashinfer/PR-1469.md) | bugfix: Verify num_experts greater or equal to local_experts + offset |
| `pr-flashinfer-1471` | upstream-code | [`sources/prs/flashinfer/PR-1471.md`](../sources/prs/flashinfer/PR-1471.md) | Fix "more than one operator "/" matches these operands" |
| `pr-flashinfer-1472` | upstream-code | [`sources/prs/flashinfer/PR-1472.md`](../sources/prs/flashinfer/PR-1472.md) | feat: Enable multiple fused-moe backends |
| `pr-flashinfer-1473` | upstream-code | [`sources/prs/flashinfer/PR-1473.md`](../sources/prs/flashinfer/PR-1473.md) | perf: add 1x4x1 cluster shape for fp8 bmm M<16 cases |
| `pr-flashinfer-1475` | upstream-code | [`sources/prs/flashinfer/PR-1475.md`](../sources/prs/flashinfer/PR-1475.md) | tuner: Trtllm-gen Fp4 MoE Autotunner |
| `pr-flashinfer-1476` | upstream-code | [`sources/prs/flashinfer/PR-1476.md`](../sources/prs/flashinfer/PR-1476.md) | fix: minor fix after #1384 |
| `pr-flashinfer-1479` | upstream-code | [`sources/prs/flashinfer/PR-1479.md`](../sources/prs/flashinfer/PR-1479.md) | refactor: unify autotuner for bmm_fp8 |
| `pr-flashinfer-1480` | upstream-code | [`sources/prs/flashinfer/PR-1480.md`](../sources/prs/flashinfer/PR-1480.md) | fix missing enable_pdl argument in trtllm-gen fp4 moe |
| `pr-flashinfer-1481` | upstream-code | [`sources/prs/flashinfer/PR-1481.md`](../sources/prs/flashinfer/PR-1481.md) | Add python API for masked grouped gemm |
| `pr-flashinfer-1483` | upstream-code | [`sources/prs/flashinfer/PR-1483.md`](../sources/prs/flashinfer/PR-1483.md) | perf: add fast path to TopPRenormProbKernel for top_p >= 1.0, significantly boosting SGLang workloads |
| `pr-flashinfer-1484` | upstream-code | [`sources/prs/flashinfer/PR-1484.md`](../sources/prs/flashinfer/PR-1484.md) | feat: add pdl for trtllm-gen attn |
| `pr-flashinfer-1488` | upstream-code | [`sources/prs/flashinfer/PR-1488.md`](../sources/prs/flashinfer/PR-1488.md) | fix: update cutedsl masked moe gemm |
| `pr-flashinfer-1490` | upstream-code | [`sources/prs/flashinfer/PR-1490.md`](../sources/prs/flashinfer/PR-1490.md) | feat: Support fp8 qkv, fp16/bf16 out MHA for trtllm-gen. |
| `pr-flashinfer-1491` | upstream-code | [`sources/prs/flashinfer/PR-1491.md`](../sources/prs/flashinfer/PR-1491.md) | Perf: support scale_a/scale_b instead of combined scale in cutlass bmm_fp8 |
| `pr-flashinfer-1497` | upstream-code | [`sources/prs/flashinfer/PR-1497.md`](../sources/prs/flashinfer/PR-1497.md) | benchmark: add moe to benchmark |
| `pr-flashinfer-1498` | upstream-code | [`sources/prs/flashinfer/PR-1498.md`](../sources/prs/flashinfer/PR-1498.md) | feat: scaling at fp4 gemm epilogue |
| `pr-flashinfer-1500` | upstream-code | [`sources/prs/flashinfer/PR-1500.md`](../sources/prs/flashinfer/PR-1500.md) | fix: Replace cub Max/Min with cuda::maximum/minimum for cuda 13 compatibility |
| `pr-flashinfer-1502` | upstream-code | [`sources/prs/flashinfer/PR-1502.md`](../sources/prs/flashinfer/PR-1502.md) | Add benchmark for cutedsl gemm |
| `pr-flashinfer-1503` | upstream-code | [`sources/prs/flashinfer/PR-1503.md`](../sources/prs/flashinfer/PR-1503.md) | feat: integrate xqa attention backend |
| `pr-flashinfer-1507` | upstream-code | [`sources/prs/flashinfer/PR-1507.md`](../sources/prs/flashinfer/PR-1507.md) | update allreduce to match trtllm |
| `pr-flashinfer-1508` | upstream-code | [`sources/prs/flashinfer/PR-1508.md`](../sources/prs/flashinfer/PR-1508.md) | Support cuda<12.8 built for trtllm_allreduce_fusion. |
| `pr-flashinfer-1509` | upstream-code | [`sources/prs/flashinfer/PR-1509.md`](../sources/prs/flashinfer/PR-1509.md) | bugfix: Fix stream handling in cutedsl gemm |
| `pr-flashinfer-1512` | upstream-code | [`sources/prs/flashinfer/PR-1512.md`](../sources/prs/flashinfer/PR-1512.md) | flashinfer_benchmark QoL Improvements and Attention FP8 Support |
| `pr-flashinfer-1518` | upstream-code | [`sources/prs/flashinfer/PR-1518.md`](../sources/prs/flashinfer/PR-1518.md) | backend: Refactor trtllm-gen fmha metainfo loading |
| `pr-flashinfer-1521` | upstream-code | [`sources/prs/flashinfer/PR-1521.md`](../sources/prs/flashinfer/PR-1521.md) | refactor fp4 masked gemm cute-dsl implementation and add manual cache |
| `pr-flashinfer-1523` | upstream-code | [`sources/prs/flashinfer/PR-1523.md`](../sources/prs/flashinfer/PR-1523.md) | Fix linking errors with CUDA 13 |
| `pr-flashinfer-1525` | upstream-code | [`sources/prs/flashinfer/PR-1525.md`](../sources/prs/flashinfer/PR-1525.md) | Add GeGLU support to trtllm-gen NVFP4 Fused MoE Kernel |
| `pr-flashinfer-1526` | upstream-code | [`sources/prs/flashinfer/PR-1526.md`](../sources/prs/flashinfer/PR-1526.md) | add cuda version check for jit |
| `pr-flashinfer-1529` | upstream-code | [`sources/prs/flashinfer/PR-1529.md`](../sources/prs/flashinfer/PR-1529.md) | feat: pass sm_count as param for fp4_masked_gemm |
| `pr-flashinfer-1530` | upstream-code | [`sources/prs/flashinfer/PR-1530.md`](../sources/prs/flashinfer/PR-1530.md) | bugfix: Fix compile error for undefined swizzle enum. |
| `pr-flashinfer-1533` | upstream-code | [`sources/prs/flashinfer/PR-1533.md`](../sources/prs/flashinfer/PR-1533.md) | bugfix: Fix Persistent kernel precision for masked output  |
| `pr-flashinfer-1534` | upstream-code | [`sources/prs/flashinfer/PR-1534.md`](../sources/prs/flashinfer/PR-1534.md) | Remove cuda-python from dependency and check at runtime |
| `pr-flashinfer-1535` | upstream-code | [`sources/prs/flashinfer/PR-1535.md`](../sources/prs/flashinfer/PR-1535.md) | Add sm check for sm100 only cutlass/trtllm kernel |
| `pr-flashinfer-1536` | upstream-code | [`sources/prs/flashinfer/PR-1536.md`](../sources/prs/flashinfer/PR-1536.md) | benchmark: Add autotunner to moe benchmark |
| `pr-flashinfer-1537` | upstream-code | [`sources/prs/flashinfer/PR-1537.md`](../sources/prs/flashinfer/PR-1537.md) | feat: Integrate TRTLLM varlen kernel for deepseek R1 prefill  |
| `pr-flashinfer-1539` | upstream-code | [`sources/prs/flashinfer/PR-1539.md`](../sources/prs/flashinfer/PR-1539.md) | bugfix: fix autotuner failure with low precision data types |
| `pr-flashinfer-1540` | upstream-code | [`sources/prs/flashinfer/PR-1540.md`](../sources/prs/flashinfer/PR-1540.md) | feat: Add fp8-qkv, fp16/bf16 output MHA |
| `pr-flashinfer-1545` | upstream-code | [`sources/prs/flashinfer/PR-1545.md`](../sources/prs/flashinfer/PR-1545.md) | fix trtllm_allreduce_fusion twoshot register problem. |
| `pr-flashinfer-1547` | upstream-code | [`sources/prs/flashinfer/PR-1547.md`](../sources/prs/flashinfer/PR-1547.md) | perf: replace cudaGetDeviceProperties with cudaDeviceGetAttribute |
| `pr-flashinfer-1548` | upstream-code | [`sources/prs/flashinfer/PR-1548.md`](../sources/prs/flashinfer/PR-1548.md) | perf: Enable SplitK and fix autotuner for trtllm fp4 fused moe |
| `pr-flashinfer-1550` | upstream-code | [`sources/prs/flashinfer/PR-1550.md`](../sources/prs/flashinfer/PR-1550.md) | Add mnnvl_moe_alltoallv_prepare_without_allgather |
| `pr-flashinfer-1559` | upstream-code | [`sources/prs/flashinfer/PR-1559.md`](../sources/prs/flashinfer/PR-1559.md) | bugfix: fix persistent attention kernel correctness on blackwell |
| `pr-flashinfer-1562` | upstream-code | [`sources/prs/flashinfer/PR-1562.md`](../sources/prs/flashinfer/PR-1562.md) | Bugfix: some typos in Persistent kernel  |
| `pr-flashinfer-1565` | upstream-code | [`sources/prs/flashinfer/PR-1565.md`](../sources/prs/flashinfer/PR-1565.md) | fix: separate out fp4 lib into sm90 and sm100 versions, add oob checking in fused moe |
| `pr-flashinfer-1567` | upstream-code | [`sources/prs/flashinfer/PR-1567.md`](../sources/prs/flashinfer/PR-1567.md) | Backend: downgrade trtllm-gen kernel to cuda-12 |
| `pr-flashinfer-1571` | upstream-code | [`sources/prs/flashinfer/PR-1571.md`](../sources/prs/flashinfer/PR-1571.md) | bugfix: fix cuda version guard macros |
| `pr-flashinfer-1573` | upstream-code | [`sources/prs/flashinfer/PR-1573.md`](../sources/prs/flashinfer/PR-1573.md) | update trtllm-gen fp4 autotuner and routing |
| `pr-flashinfer-1577` | upstream-code | [`sources/prs/flashinfer/PR-1577.md`](../sources/prs/flashinfer/PR-1577.md) | bugfix: update trtllm-gen gemm kernel names |
| `pr-flashinfer-1578` | upstream-code | [`sources/prs/flashinfer/PR-1578.md`](../sources/prs/flashinfer/PR-1578.md) | feat: Support for inferring out_dtype from out.dtype for TRTLLM attention kernel |
| `pr-flashinfer-1581` | upstream-code | [`sources/prs/flashinfer/PR-1581.md`](../sources/prs/flashinfer/PR-1581.md) | refactor: Expose calculate_tile_tokens_dim function |
| `pr-flashinfer-1582` | upstream-code | [`sources/prs/flashinfer/PR-1582.md`](../sources/prs/flashinfer/PR-1582.md) | bugfix: Fix arg passing to TORCH_CHECK and TORCH_WARN macros |
| `pr-flashinfer-1584` | upstream-code | [`sources/prs/flashinfer/PR-1584.md`](../sources/prs/flashinfer/PR-1584.md) | fix: semaphoress must be at the fixed range in workspace buffer on trtllm_gen attention |
| `pr-flashinfer-1588` | upstream-code | [`sources/prs/flashinfer/PR-1588.md`](../sources/prs/flashinfer/PR-1588.md) | refactor: use allocator class for workspace buffer allocation |
| `pr-flashinfer-1590` | upstream-code | [`sources/prs/flashinfer/PR-1590.md`](../sources/prs/flashinfer/PR-1590.md) | fix: Improve TRTLLM attention kernel out_dtype unit test |
| `pr-flashinfer-1596` | upstream-code | [`sources/prs/flashinfer/PR-1596.md`](../sources/prs/flashinfer/PR-1596.md) | bugfix: fix fused-temperature softmax IMA issue |
| `pr-flashinfer-1597` | upstream-code | [`sources/prs/flashinfer/PR-1597.md`](../sources/prs/flashinfer/PR-1597.md) | bugfix: fix the register overflow issue for topk renorm kernels on blackwell |
| `pr-flashinfer-1598` | upstream-code | [`sources/prs/flashinfer/PR-1598.md`](../sources/prs/flashinfer/PR-1598.md) | bugfix: Fix RuntimeError("FlashInfer requires sm75+") |
| `pr-flashinfer-1599` | upstream-code | [`sources/prs/flashinfer/PR-1599.md`](../sources/prs/flashinfer/PR-1599.md) | bugfix: fix unittest test_fp8_quantize |
| `pr-flashinfer-1601` | upstream-code | [`sources/prs/flashinfer/PR-1601.md`](../sources/prs/flashinfer/PR-1601.md) | feat: Enable MnnvlMemory (for alltoallv) on B200 |
| `pr-flashinfer-1608` | upstream-code | [`sources/prs/flashinfer/PR-1608.md`](../sources/prs/flashinfer/PR-1608.md) | feat: initial support for SM103, SM110, SM120, SM121 |
| `pr-flashinfer-1609` | upstream-code | [`sources/prs/flashinfer/PR-1609.md`](../sources/prs/flashinfer/PR-1609.md) | feat: cutlass fp4 gemm bringup for SM120 & SM121 |
| `pr-flashinfer-1610` | upstream-code | [`sources/prs/flashinfer/PR-1610.md`](../sources/prs/flashinfer/PR-1610.md) | feat: cutlass fp8 gemm bringup for SM120 & SM121 |
| `pr-flashinfer-1611` | upstream-code | [`sources/prs/flashinfer/PR-1611.md`](../sources/prs/flashinfer/PR-1611.md) | bugfix: fix fp4 quantization with 8x4 scale factor layout |
| `pr-flashinfer-1614` | upstream-code | [`sources/prs/flashinfer/PR-1614.md`](../sources/prs/flashinfer/PR-1614.md) | bugfix: fix merge_attention_state in BatchAttention w/ gqa-group-size in Qwen family |
| `pr-flashinfer-1615` | upstream-code | [`sources/prs/flashinfer/PR-1615.md`](../sources/prs/flashinfer/PR-1615.md) | perf: Fix the tactic sorting in TrtllmGenBatchedGemmRunner::getValidConfigIndices |
| `pr-flashinfer-1622` | upstream-code | [`sources/prs/flashinfer/PR-1622.md`](../sources/prs/flashinfer/PR-1622.md) | bugfix: collect all modules to aot |
| `pr-flashinfer-1625` | upstream-code | [`sources/prs/flashinfer/PR-1625.md`](../sources/prs/flashinfer/PR-1625.md) | bugfix: fix flashinfer_benchmark.py IMA when running a test list |
| `pr-flashinfer-1628` | upstream-code | [`sources/prs/flashinfer/PR-1628.md`](../sources/prs/flashinfer/PR-1628.md) | patch mm segfault & patch cubin avail. |
| `pr-flashinfer-1631` | upstream-code | [`sources/prs/flashinfer/PR-1631.md`](../sources/prs/flashinfer/PR-1631.md) | bugfix: trtllm-gen fmha sm101 and sm100 compatibility |
| `pr-flashinfer-1633` | upstream-code | [`sources/prs/flashinfer/PR-1633.md`](../sources/prs/flashinfer/PR-1633.md) | feat: add support of fp4_batched_quantize |
| `pr-flashinfer-1635` | upstream-code | [`sources/prs/flashinfer/PR-1635.md`](../sources/prs/flashinfer/PR-1635.md) | fix: pass workspace for trtllm-gen attention |
| `pr-flashinfer-1640` | upstream-code | [`sources/prs/flashinfer/PR-1640.md`](../sources/prs/flashinfer/PR-1640.md) | bugfix: Fix FLOPS calculation for bench_trtllm_gen_mla.py |
| `pr-flashinfer-1641` | upstream-code | [`sources/prs/flashinfer/PR-1641.md`](../sources/prs/flashinfer/PR-1641.md) | refactor: using tvm-ffi for multi-platform bindings |
| `pr-flashinfer-1644` | upstream-code | [`sources/prs/flashinfer/PR-1644.md`](../sources/prs/flashinfer/PR-1644.md) | Added mx_fp4 support using the cudnn backend |
| `pr-flashinfer-1652` | upstream-code | [`sources/prs/flashinfer/PR-1652.md`](../sources/prs/flashinfer/PR-1652.md) | fix: add _check_tensor_params to check correct sampling parameters and dtype validation in decode.py |
| `pr-flashinfer-1656` | upstream-code | [`sources/prs/flashinfer/PR-1656.md`](../sources/prs/flashinfer/PR-1656.md) | Add benchmark for MLARopeQuantize |
| `pr-flashinfer-1659` | upstream-code | [`sources/prs/flashinfer/PR-1659.md`](../sources/prs/flashinfer/PR-1659.md) | Tiny allow compiling with line info and release moe |
| `pr-flashinfer-1661` | upstream-code | [`sources/prs/flashinfer/PR-1661.md`](../sources/prs/flashinfer/PR-1661.md) | perf&bugfix: skip kv-tile computation out of sliding window in FA2; fix __syncthreads in mergestate |
| `pr-flashinfer-1662` | upstream-code | [`sources/prs/flashinfer/PR-1662.md`](../sources/prs/flashinfer/PR-1662.md) | benchmark: add cupti support to benchmark |
| `pr-flashinfer-1664` | upstream-code | [`sources/prs/flashinfer/PR-1664.md`](../sources/prs/flashinfer/PR-1664.md) | feat: Support s_qo < s_kv for prefill in flashinfer_benchmark.py and benchmark minor updates |
| `pr-flashinfer-1666` | upstream-code | [`sources/prs/flashinfer/PR-1666.md`](../sources/prs/flashinfer/PR-1666.md) | [Hotfix] `test_fp4_quantize.py` failure on sm103 |
| `pr-flashinfer-1667` | upstream-code | [`sources/prs/flashinfer/PR-1667.md`](../sources/prs/flashinfer/PR-1667.md) | Refactor Blackwell unit test scripts |
| `pr-flashinfer-1668` | upstream-code | [`sources/prs/flashinfer/PR-1668.md`](../sources/prs/flashinfer/PR-1668.md) | TGV GEMM as a BF16 backend alternative to cuBLAS |
| `pr-flashinfer-1670` | upstream-code | [`sources/prs/flashinfer/PR-1670.md`](../sources/prs/flashinfer/PR-1670.md) | feat: Add `variant.OutputTransform()` to decode kernels |
| `pr-flashinfer-1675` | upstream-code | [`sources/prs/flashinfer/PR-1675.md`](../sources/prs/flashinfer/PR-1675.md) | feat: Batch-size invariant FA2 Prefill & Decode |
| `pr-flashinfer-1677` | upstream-code | [`sources/prs/flashinfer/PR-1677.md`](../sources/prs/flashinfer/PR-1677.md) | Support output signals for overlapping for cutedsl gemm |
| `pr-flashinfer-1679` | upstream-code | [`sources/prs/flashinfer/PR-1679.md`](../sources/prs/flashinfer/PR-1679.md) | [misc] add a wrapper class for attention sink jit args |
| `pr-flashinfer-1680` | upstream-code | [`sources/prs/flashinfer/PR-1680.md`](../sources/prs/flashinfer/PR-1680.md) | [TVM] Default `fixed_split_size` value in TVM binding |
| `pr-flashinfer-1681` | upstream-code | [`sources/prs/flashinfer/PR-1681.md`](../sources/prs/flashinfer/PR-1681.md) | perf: improve performance of cutlass fmha |
| `pr-flashinfer-1682` | upstream-code | [`sources/prs/flashinfer/PR-1682.md`](../sources/prs/flashinfer/PR-1682.md) | Update TGV GEMM default kernel and TGV code cleanup. |
| `pr-flashinfer-1685` | upstream-code | [`sources/prs/flashinfer/PR-1685.md`](../sources/prs/flashinfer/PR-1685.md) | perf: Port the separate reduce kernel mode from trtllm. |
| `pr-flashinfer-1688` | upstream-code | [`sources/prs/flashinfer/PR-1688.md`](../sources/prs/flashinfer/PR-1688.md) | gemm: Enabled alpha with the mx_fp4 format |
| `pr-flashinfer-1694` | upstream-code | [`sources/prs/flashinfer/PR-1694.md`](../sources/prs/flashinfer/PR-1694.md) | Update deepgemm backend for 103a |
| `pr-flashinfer-1695` | upstream-code | [`sources/prs/flashinfer/PR-1695.md`](../sources/prs/flashinfer/PR-1695.md) | [cute_dsl] add gemm + all reduce (two_shot)  |
| `pr-flashinfer-1696` | upstream-code | [`sources/prs/flashinfer/PR-1696.md`](../sources/prs/flashinfer/PR-1696.md) | Support Kimi-K2 for TRT: templatize number of experts |
| `pr-flashinfer-1699` | upstream-code | [`sources/prs/flashinfer/PR-1699.md`](../sources/prs/flashinfer/PR-1699.md) | Remove incorrect method call "isdigit" on number type |
| `pr-flashinfer-1706` | upstream-code | [`sources/prs/flashinfer/PR-1706.md`](../sources/prs/flashinfer/PR-1706.md) | feat: Benchmark mm_fp4 mxfp4 support and gemm autotune support.  Restore mm_fp4 API behavior |
| `pr-flashinfer-1710` | upstream-code | [`sources/prs/flashinfer/PR-1710.md`](../sources/prs/flashinfer/PR-1710.md) | test: skip the unsupported test cases for sm120/121 |
| `pr-flashinfer-1715` | upstream-code | [`sources/prs/flashinfer/PR-1715.md`](../sources/prs/flashinfer/PR-1715.md) | test: skip unsupported (non-SM90) test cases for xqa |
| `pr-flashinfer-1716` | upstream-code | [`sources/prs/flashinfer/PR-1716.md`](../sources/prs/flashinfer/PR-1716.md) | perf: Add tuning config for cutlass moe for a hardware |
| `pr-flashinfer-1719` | upstream-code | [`sources/prs/flashinfer/PR-1719.md`](../sources/prs/flashinfer/PR-1719.md) | disable optimization and add more debug information during verbose mode |
| `pr-flashinfer-1723` | upstream-code | [`sources/prs/flashinfer/PR-1723.md`](../sources/prs/flashinfer/PR-1723.md) | Fix DeepSeek quality for TRTLLM fused MoE routing |
| `pr-flashinfer-1724` | upstream-code | [`sources/prs/flashinfer/PR-1724.md`](../sources/prs/flashinfer/PR-1724.md) | bugfix: partially fix tests/test_trtllm_gen_fused_moe.py unit test failure |
| `pr-flashinfer-1725` | upstream-code | [`sources/prs/flashinfer/PR-1725.md`](../sources/prs/flashinfer/PR-1725.md) | TVM: support TVM binding for GroupedGemm |
| `pr-flashinfer-1727` | upstream-code | [`sources/prs/flashinfer/PR-1727.md`](../sources/prs/flashinfer/PR-1727.md) | fix: put sampling kernel launch into macro |
| `pr-flashinfer-1729` | upstream-code | [`sources/prs/flashinfer/PR-1729.md`](../sources/prs/flashinfer/PR-1729.md) | bugfix: Fix flashinfer download-cubin |
| `pr-flashinfer-1731` | upstream-code | [`sources/prs/flashinfer/PR-1731.md`](../sources/prs/flashinfer/PR-1731.md) | Fix missing namespace qualifier |
| `pr-flashinfer-1745` | upstream-code | [`sources/prs/flashinfer/PR-1745.md`](../sources/prs/flashinfer/PR-1745.md) | feat: port fast_decode_plan from sgl |
| `pr-flashinfer-1757` | upstream-code | [`sources/prs/flashinfer/PR-1757.md`](../sources/prs/flashinfer/PR-1757.md) | fix: should pass global_override_indptr_cpu in fast_decode_plan param list |
| `pr-flashinfer-1758` | upstream-code | [`sources/prs/flashinfer/PR-1758.md`](../sources/prs/flashinfer/PR-1758.md) | Fix sink attention accuracy regression, add sink test and cleanup. |
| `pr-flashinfer-1764` | upstream-code | [`sources/prs/flashinfer/PR-1764.md`](../sources/prs/flashinfer/PR-1764.md) | fix: fix cannot import name 'cuda' from 'cuda' in CUDA13 |
| `pr-flashinfer-1766` | upstream-code | [`sources/prs/flashinfer/PR-1766.md`](../sources/prs/flashinfer/PR-1766.md) | Added xfail for mx_fp4 matmul on SM120 |
| `pr-flashinfer-1767` | upstream-code | [`sources/prs/flashinfer/PR-1767.md`](../sources/prs/flashinfer/PR-1767.md) | tests: skip non SM100/103 for grouped deepgemm |
| `pr-flashinfer-1769` | upstream-code | [`sources/prs/flashinfer/PR-1769.md`](../sources/prs/flashinfer/PR-1769.md) | feat: add xqa fp8 mha and fp8 kv cache |
| `pr-flashinfer-1771` | upstream-code | [`sources/prs/flashinfer/PR-1771.md`](../sources/prs/flashinfer/PR-1771.md) | Waive / disable test_mla_decode_kernel.py::test_mla_decode_kernel for not sm80  |
| `pr-flashinfer-1774` | upstream-code | [`sources/prs/flashinfer/PR-1774.md`](../sources/prs/flashinfer/PR-1774.md) | Masked batch nvfp4 quantization |
| `pr-flashinfer-1778` | upstream-code | [`sources/prs/flashinfer/PR-1778.md`](../sources/prs/flashinfer/PR-1778.md) | refactor: Test reorganization phase 2 |
| `pr-flashinfer-1782` | upstream-code | [`sources/prs/flashinfer/PR-1782.md`](../sources/prs/flashinfer/PR-1782.md) | hotfix: make aot wheel work without nvcc |
| `pr-flashinfer-1795` | upstream-code | [`sources/prs/flashinfer/PR-1795.md`](../sources/prs/flashinfer/PR-1795.md) | refactor: cleanup codebase after tvm-ffi refactor |
| `pr-flashinfer-1798` | upstream-code | [`sources/prs/flashinfer/PR-1798.md`](../sources/prs/flashinfer/PR-1798.md) | bugfix: remove the append "a" logic if user specifies cuda arch explicitly |
| `pr-flashinfer-1800` | upstream-code | [`sources/prs/flashinfer/PR-1800.md`](../sources/prs/flashinfer/PR-1800.md) | fix: compilation failure in fp4Op.cpp |
| `pr-flashinfer-1801` | upstream-code | [`sources/prs/flashinfer/PR-1801.md`](../sources/prs/flashinfer/PR-1801.md) | Enable support for CFLAGS as well as LDFLAGS when building |
| `pr-flashinfer-1802` | upstream-code | [`sources/prs/flashinfer/PR-1802.md`](../sources/prs/flashinfer/PR-1802.md) | fix: missing header include in decode kernel jit binding |
| `pr-flashinfer-1809` | upstream-code | [`sources/prs/flashinfer/PR-1809.md`](../sources/prs/flashinfer/PR-1809.md) | Support checks PoC |
| `pr-flashinfer-1810` | upstream-code | [`sources/prs/flashinfer/PR-1810.md`](../sources/prs/flashinfer/PR-1810.md) | tests: Update support for tgv_gemm to SM100 only and add to ut |
| `pr-flashinfer-1812` | upstream-code | [`sources/prs/flashinfer/PR-1812.md`](../sources/prs/flashinfer/PR-1812.md) | tests: upgrade cutlass, fix import and skip non-SM100 cutedsl two shot allreduce |
| `pr-flashinfer-1817` | upstream-code | [`sources/prs/flashinfer/PR-1817.md`](../sources/prs/flashinfer/PR-1817.md) | fix: fp4 moe on sm120 |
| `pr-flashinfer-1819` | upstream-code | [`sources/prs/flashinfer/PR-1819.md`](../sources/prs/flashinfer/PR-1819.md) | feat:enable fp8 blockscale moe for fused cultass for sm90 |
| `pr-flashinfer-1821` | upstream-code | [`sources/prs/flashinfer/PR-1821.md`](../sources/prs/flashinfer/PR-1821.md) | Remove `-isystem /usr/include` |
| `pr-flashinfer-1824` | upstream-code | [`sources/prs/flashinfer/PR-1824.md`](../sources/prs/flashinfer/PR-1824.md) | [Perf] Cache device property functions to avoid recomputation |
| `pr-flashinfer-1825` | upstream-code | [`sources/prs/flashinfer/PR-1825.md`](../sources/prs/flashinfer/PR-1825.md) | jit: add `-lcuda` to default ldflags |
| `pr-flashinfer-1826` | upstream-code | [`sources/prs/flashinfer/PR-1826.md`](../sources/prs/flashinfer/PR-1826.md) | Bugfix: Fix data hazard in persistent reduce |
| `pr-flashinfer-1829` | upstream-code | [`sources/prs/flashinfer/PR-1829.md`](../sources/prs/flashinfer/PR-1829.md) | feat: trtrllm-gen global scaled FP8 GEMMs |
| `pr-flashinfer-1831` | upstream-code | [`sources/prs/flashinfer/PR-1831.md`](../sources/prs/flashinfer/PR-1831.md) | Update the routing for TRTLLMGEN to support kimi k2 and qwen |
| `pr-flashinfer-1835` | upstream-code | [`sources/prs/flashinfer/PR-1835.md`](../sources/prs/flashinfer/PR-1835.md) | [Quantization] Add per-expert global scaling factor for fp4 batched quantize |
| `pr-flashinfer-1836` | upstream-code | [`sources/prs/flashinfer/PR-1836.md`](../sources/prs/flashinfer/PR-1836.md) | jit: add `get_object_paths` to JitSpec |
| `pr-flashinfer-1838` | upstream-code | [`sources/prs/flashinfer/PR-1838.md`](../sources/prs/flashinfer/PR-1838.md) | bugfix: deep_gemm artifact load path |
| `pr-flashinfer-1843` | upstream-code | [`sources/prs/flashinfer/PR-1843.md`](../sources/prs/flashinfer/PR-1843.md) | feat: add warp-level persistent qk norm |
| `pr-flashinfer-1850` | upstream-code | [`sources/prs/flashinfer/PR-1850.md`](../sources/prs/flashinfer/PR-1850.md) | Add head_dim=64 for blackwell cutlass fmha implementation |
| `pr-flashinfer-1862` | upstream-code | [`sources/prs/flashinfer/PR-1862.md`](../sources/prs/flashinfer/PR-1862.md) | raise error for group_gemm_fp8_nt_groupwise then num_groups > 1 on sm120/121 |
| `pr-flashinfer-1865` | upstream-code | [`sources/prs/flashinfer/PR-1865.md`](../sources/prs/flashinfer/PR-1865.md) | Bugfix: fix o_strides in persistent kernel  |
| `pr-flashinfer-1876` | upstream-code | [`sources/prs/flashinfer/PR-1876.md`](../sources/prs/flashinfer/PR-1876.md) | Fix bias dtype |
| `pr-flashinfer-1878` | upstream-code | [`sources/prs/flashinfer/PR-1878.md`](../sources/prs/flashinfer/PR-1878.md) | Tune kernel compilation parameters for https://github.com/flashinfer-ai/flashinfer/pull/1850  |
| `pr-flashinfer-1882` | upstream-code | [`sources/prs/flashinfer/PR-1882.md`](../sources/prs/flashinfer/PR-1882.md) | feat: Add FP4 TRTLLM-Gen throughput MOE batched gemms |
| `pr-flashinfer-1883` | upstream-code | [`sources/prs/flashinfer/PR-1883.md`](../sources/prs/flashinfer/PR-1883.md) | misc: fix some B200 GEMM bench |
| `pr-flashinfer-1894` | upstream-code | [`sources/prs/flashinfer/PR-1894.md`](../sources/prs/flashinfer/PR-1894.md) | fix vllm graph register and add test |
| `pr-flashinfer-1905` | upstream-code | [`sources/prs/flashinfer/PR-1905.md`](../sources/prs/flashinfer/PR-1905.md) | bugfix: fix cli error when cuda toolkit is not installed |
| `pr-flashinfer-1912` | upstream-code | [`sources/prs/flashinfer/PR-1912.md`](../sources/prs/flashinfer/PR-1912.md) | fix: Fix trtllm-gen prefill IMA when batch_size==1 |
| `pr-flashinfer-1924` | upstream-code | [`sources/prs/flashinfer/PR-1924.md`](../sources/prs/flashinfer/PR-1924.md) | MLA RoPE + quantization fused kernel: shape generalization for MHA / GQA |
| `pr-flashinfer-1926` | upstream-code | [`sources/prs/flashinfer/PR-1926.md`](../sources/prs/flashinfer/PR-1926.md) | Add layernorm op for inputs of mixed dtype |
| `pr-flashinfer-1927` | upstream-code | [`sources/prs/flashinfer/PR-1927.md`](../sources/prs/flashinfer/PR-1927.md) | silu_and_mul nvfp4 quanization fusion rework |
| `pr-flashinfer-1930` | upstream-code | [`sources/prs/flashinfer/PR-1930.md`](../sources/prs/flashinfer/PR-1930.md) | fix get max_q_len in page prefill plan |
| `pr-flashinfer-1942` | upstream-code | [`sources/prs/flashinfer/PR-1942.md`](../sources/prs/flashinfer/PR-1942.md) | Add realistic bench for persistent kernel  |
| `pr-flashinfer-1948` | upstream-code | [`sources/prs/flashinfer/PR-1948.md`](../sources/prs/flashinfer/PR-1948.md) | Fix #1641: Use `/usr/local/cuda` as default `CUDA_HOME` if possible, like `torch.utils.cpp_extension.CUDA_HOME` |
| `pr-flashinfer-1951` | upstream-code | [`sources/prs/flashinfer/PR-1951.md`](../sources/prs/flashinfer/PR-1951.md) | bugfix: fix failed unittest `test_green_ctx` and `test_jit_example` on spark (sm_121) |
| `pr-flashinfer-1953` | upstream-code | [`sources/prs/flashinfer/PR-1953.md`](../sources/prs/flashinfer/PR-1953.md) | unittest: fix deepgemm sha256 |
| `pr-flashinfer-1954` | upstream-code | [`sources/prs/flashinfer/PR-1954.md`](../sources/prs/flashinfer/PR-1954.md) | Feature: Support Relu2 activation in fused MoE |
| `pr-flashinfer-1955` | upstream-code | [`sources/prs/flashinfer/PR-1955.md`](../sources/prs/flashinfer/PR-1955.md) | Update trtllm-gen fused moe routing kernel and add more kernels |
| `pr-flashinfer-1959` | upstream-code | [`sources/prs/flashinfer/PR-1959.md`](../sources/prs/flashinfer/PR-1959.md) | fix: Add cutlass as an mm_fp4 backend in compute capability 12.0 in benchmark code |
| `pr-flashinfer-1961` | upstream-code | [`sources/prs/flashinfer/PR-1961.md`](../sources/prs/flashinfer/PR-1961.md) | Fix: Verify scales are not None for Cutlass FP8 FusedMoE |
| `pr-flashinfer-1963` | upstream-code | [`sources/prs/flashinfer/PR-1963.md`](../sources/prs/flashinfer/PR-1963.md) | fix: ensure SM120/121 SFA/SFB contiguity |
| `pr-flashinfer-1969` | upstream-code | [`sources/prs/flashinfer/PR-1969.md`](../sources/prs/flashinfer/PR-1969.md) | feat: enable deepgemm jit for fp8 block-scale on SM90 |
| `pr-flashinfer-1972` | upstream-code | [`sources/prs/flashinfer/PR-1972.md`](../sources/prs/flashinfer/PR-1972.md) | Added heuristic for trtllm_allreduce_fusion |
| `pr-flashinfer-1973` | upstream-code | [`sources/prs/flashinfer/PR-1973.md`](../sources/prs/flashinfer/PR-1973.md) | Feature: Add support for L40 FusedMoE in cutlass path |
| `pr-flashinfer-1976` | upstream-code | [`sources/prs/flashinfer/PR-1976.md`](../sources/prs/flashinfer/PR-1976.md) | fix: Make attention microbenchmark correctly use page table |
| `pr-flashinfer-1979` | upstream-code | [`sources/prs/flashinfer/PR-1979.md`](../sources/prs/flashinfer/PR-1979.md) | feat: Add backend='auto' to mm_fp4 and enable autotune for backend='cudnn' |
| `pr-flashinfer-1980` | upstream-code | [`sources/prs/flashinfer/PR-1980.md`](../sources/prs/flashinfer/PR-1980.md) | feat: autotune tile_tokens_dim in trtllm-gen MOE |
| `pr-flashinfer-1982` | upstream-code | [`sources/prs/flashinfer/PR-1982.md`](../sources/prs/flashinfer/PR-1982.md) | fix: correct PDL parameter handling in RopeQuantize kernel |
| `pr-flashinfer-1991` | upstream-code | [`sources/prs/flashinfer/PR-1991.md`](../sources/prs/flashinfer/PR-1991.md) | Added workspace check and reflected this in test |
| `pr-flashinfer-1994` | upstream-code | [`sources/prs/flashinfer/PR-1994.md`](../sources/prs/flashinfer/PR-1994.md) | minor fix for xqa |
| `pr-flashinfer-1995` | upstream-code | [`sources/prs/flashinfer/PR-1995.md`](../sources/prs/flashinfer/PR-1995.md) | Bugfix: Change get() -> GetDLTensorPtr() in cutlass FusedMoE validations |
| `pr-flashinfer-2001` | upstream-code | [`sources/prs/flashinfer/PR-2001.md`](../sources/prs/flashinfer/PR-2001.md) | feat: add xqa backend and completes NHD/HND coverage for trtllm-gen/xqa backend |
| `pr-flashinfer-2002` | upstream-code | [`sources/prs/flashinfer/PR-2002.md`](../sources/prs/flashinfer/PR-2002.md) | Fix trtllm-gen attention illegal memory access |
| `pr-flashinfer-2011` | upstream-code | [`sources/prs/flashinfer/PR-2011.md`](../sources/prs/flashinfer/PR-2011.md) | Feature: Support non-gated activation in cutlass fused MoE nvfp4 |
| `pr-flashinfer-2012` | upstream-code | [`sources/prs/flashinfer/PR-2012.md`](../sources/prs/flashinfer/PR-2012.md) | fix: Enable SM121 for mm_fp4 |
| `pr-flashinfer-2013` | upstream-code | [`sources/prs/flashinfer/PR-2013.md`](../sources/prs/flashinfer/PR-2013.md) | More realistic bench for POD Attn |
| `pr-flashinfer-2014` | upstream-code | [`sources/prs/flashinfer/PR-2014.md`](../sources/prs/flashinfer/PR-2014.md) | [feat] Refactor trtllmgen MOE and add Bf16 trtllmgen moe |
| `pr-flashinfer-2015` | upstream-code | [`sources/prs/flashinfer/PR-2015.md`](../sources/prs/flashinfer/PR-2015.md) | Support cc common check decorator for empty backends |
| `pr-flashinfer-2018` | upstream-code | [`sources/prs/flashinfer/PR-2018.md`](../sources/prs/flashinfer/PR-2018.md) | test: Enable xfailed trtllm decode long seqlen tests and update microbenchmark |
| `pr-flashinfer-2019` | upstream-code | [`sources/prs/flashinfer/PR-2019.md`](../sources/prs/flashinfer/PR-2019.md) | [DSV3] Optimized Router Gemm |
| `pr-flashinfer-2020` | upstream-code | [`sources/prs/flashinfer/PR-2020.md`](../sources/prs/flashinfer/PR-2020.md) | update trtllm cutlass moe  |
| `pr-flashinfer-2025` | upstream-code | [`sources/prs/flashinfer/PR-2025.md`](../sources/prs/flashinfer/PR-2025.md) | perf: Speed up fp4 quantization for small batch with swizzling for cutlass MoE |
| `pr-flashinfer-2026` | upstream-code | [`sources/prs/flashinfer/PR-2026.md`](../sources/prs/flashinfer/PR-2026.md) | Updated decorator to support unspecified default |
| `pr-flashinfer-2028` | upstream-code | [`sources/prs/flashinfer/PR-2028.md`](../sources/prs/flashinfer/PR-2028.md) | [NVIDIA] Thor & Spark Support |
| `pr-flashinfer-2029` | upstream-code | [`sources/prs/flashinfer/PR-2029.md`](../sources/prs/flashinfer/PR-2029.md) | feat: suitable_auto_backends to prune auto backends, bmm_fp8 refactor, heuristic_func intake |
| `pr-flashinfer-2030` | upstream-code | [`sources/prs/flashinfer/PR-2030.md`](../sources/prs/flashinfer/PR-2030.md) | Enable renormalize(naive) routing for fp8 per-tensor |
| `pr-flashinfer-2033` | upstream-code | [`sources/prs/flashinfer/PR-2033.md`](../sources/prs/flashinfer/PR-2033.md) | use scalar for kv_scale in xqa |
| `pr-flashinfer-2035` | upstream-code | [`sources/prs/flashinfer/PR-2035.md`](../sources/prs/flashinfer/PR-2035.md) | Added an initial implementation of Q and KV Cache in fp8 and to use t… |
| `pr-flashinfer-2037` | upstream-code | [`sources/prs/flashinfer/PR-2037.md`](../sources/prs/flashinfer/PR-2037.md) | feat: Add flashinfer.rope.rope_quantize_fp8_append_paged_kv_cache (fused RoPE + Q + KV cache, supports MLA/GQA/MHA)  |
| `pr-flashinfer-2044` | upstream-code | [`sources/prs/flashinfer/PR-2044.md`](../sources/prs/flashinfer/PR-2044.md) | perf: improve sampling/mask/softmax performance (part 1/2) |
| `pr-flashinfer-2047` | upstream-code | [`sources/prs/flashinfer/PR-2047.md`](../sources/prs/flashinfer/PR-2047.md) | Rebase FP8 SM100 Cutlass FMHA Attention to main (original PR#1238) |
| `pr-flashinfer-2048` | upstream-code | [`sources/prs/flashinfer/PR-2048.md`](../sources/prs/flashinfer/PR-2048.md) | Fix dtype of output scales from mnnvl_moe_alltoallv_prepare_without_allgather |
| `pr-flashinfer-2049` | upstream-code | [`sources/prs/flashinfer/PR-2049.md`](../sources/prs/flashinfer/PR-2049.md) | [BUG] Fix trtllm-gen fp4 moe renormalize routing |
| `pr-flashinfer-2051` | upstream-code | [`sources/prs/flashinfer/PR-2051.md`](../sources/prs/flashinfer/PR-2051.md) | Add support for topkPacked input in block-level renormalize |
| `pr-flashinfer-2053` | upstream-code | [`sources/prs/flashinfer/PR-2053.md`](../sources/prs/flashinfer/PR-2053.md) | feat: add xqa mla backend |
| `pr-flashinfer-2055` | upstream-code | [`sources/prs/flashinfer/PR-2055.md`](../sources/prs/flashinfer/PR-2055.md) | misc: Add XQA decode to microbenchmark for sm90 and sm120 |
| `pr-flashinfer-2056` | upstream-code | [`sources/prs/flashinfer/PR-2056.md`](../sources/prs/flashinfer/PR-2056.md) | Add custom communicator for trtllm_mnnvl_ar |
| `pr-flashinfer-2058` | upstream-code | [`sources/prs/flashinfer/PR-2058.md`](../sources/prs/flashinfer/PR-2058.md) | perf: Optimize helper max/minmax function in sampling.cuh |
| `pr-flashinfer-2061` | upstream-code | [`sources/prs/flashinfer/PR-2061.md`](../sources/prs/flashinfer/PR-2061.md) | Fix moe fp8 failure for sm121 |
| `pr-flashinfer-2062` | upstream-code | [`sources/prs/flashinfer/PR-2062.md`](../sources/prs/flashinfer/PR-2062.md) | Fix: several bugs/issues with trtllm-gen attention kernels.  |
| `pr-flashinfer-2063` | upstream-code | [`sources/prs/flashinfer/PR-2063.md`](../sources/prs/flashinfer/PR-2063.md) | perf: TRT-LLM MoE Block-FP8 activation optimization |
| `pr-flashinfer-2064` | upstream-code | [`sources/prs/flashinfer/PR-2064.md`](../sources/prs/flashinfer/PR-2064.md) | refactor: remove MetaInfoHash class |
| `pr-flashinfer-2070` | upstream-code | [`sources/prs/flashinfer/PR-2070.md`](../sources/prs/flashinfer/PR-2070.md) | feat: BF16 GEMM using CUTLASS backend for SM100 |
| `pr-flashinfer-2074` | upstream-code | [`sources/prs/flashinfer/PR-2074.md`](../sources/prs/flashinfer/PR-2074.md) | MNNVL All Reduce for large number of tokens |
| `pr-flashinfer-2079` | upstream-code | [`sources/prs/flashinfer/PR-2079.md`](../sources/prs/flashinfer/PR-2079.md) | [Feature] Support batch prefill for POD Attention |
| `pr-flashinfer-2081` | upstream-code | [`sources/prs/flashinfer/PR-2081.md`](../sources/prs/flashinfer/PR-2081.md) | enable xqa fp8 output |
| `pr-flashinfer-2082` | upstream-code | [`sources/prs/flashinfer/PR-2082.md`](../sources/prs/flashinfer/PR-2082.md) | Patch sm103 for 3xfp4 moe generation |
| `pr-flashinfer-2084` | upstream-code | [`sources/prs/flashinfer/PR-2084.md`](../sources/prs/flashinfer/PR-2084.md) | [API change] Allow using torch.Tensor for scales for trtllm-gen attention |
| `pr-flashinfer-2086` | upstream-code | [`sources/prs/flashinfer/PR-2086.md`](../sources/prs/flashinfer/PR-2086.md) | [API change] deprecate tile_token_dim in trtllm_moe |
| `pr-flashinfer-2090` | upstream-code | [`sources/prs/flashinfer/PR-2090.md`](../sources/prs/flashinfer/PR-2090.md) | refactor: pass hopper deepgemm include directory through python |
| `pr-flashinfer-2092` | upstream-code | [`sources/prs/flashinfer/PR-2092.md`](../sources/prs/flashinfer/PR-2092.md) | perf: TRT-LLM Gen finalize kernel optimization |
| `pr-flashinfer-2095` | upstream-code | [`sources/prs/flashinfer/PR-2095.md`](../sources/prs/flashinfer/PR-2095.md) | perf: enable pdl for cutlass fp4 gemm |
| `pr-flashinfer-2099` | upstream-code | [`sources/prs/flashinfer/PR-2099.md`](../sources/prs/flashinfer/PR-2099.md) | [DSV3] Optimized routing kernels dsv3 |
| `pr-flashinfer-2102` | upstream-code | [`sources/prs/flashinfer/PR-2102.md`](../sources/prs/flashinfer/PR-2102.md) | Port TRT-LLM communication kernels to flashinfer |
| `pr-flashinfer-2105` | upstream-code | [`sources/prs/flashinfer/PR-2105.md`](../sources/prs/flashinfer/PR-2105.md) | enable xqa speculative decoding |
| `pr-flashinfer-2109` | upstream-code | [`sources/prs/flashinfer/PR-2109.md`](../sources/prs/flashinfer/PR-2109.md) | feat: support more head dim in RoPE kernel |
| `pr-flashinfer-2110` | upstream-code | [`sources/prs/flashinfer/PR-2110.md`](../sources/prs/flashinfer/PR-2110.md) | add tensor scale input for xqa |
| `pr-flashinfer-2111` | upstream-code | [`sources/prs/flashinfer/PR-2111.md`](../sources/prs/flashinfer/PR-2111.md) | refactor: update fa3 codebase and fix hopper unittest [part 1] |
| `pr-flashinfer-2114` | upstream-code | [`sources/prs/flashinfer/PR-2114.md`](../sources/prs/flashinfer/PR-2114.md) | feature: make the LSE returned by MLA support base 2 or e  #2113 |
| `pr-flashinfer-2116` | upstream-code | [`sources/prs/flashinfer/PR-2116.md`](../sources/prs/flashinfer/PR-2116.md) | update autotuner input tensor random range |
| `pr-flashinfer-2117` | upstream-code | [`sources/prs/flashinfer/PR-2117.md`](../sources/prs/flashinfer/PR-2117.md) | update xqa license |
| `pr-flashinfer-2118` | upstream-code | [`sources/prs/flashinfer/PR-2118.md`](../sources/prs/flashinfer/PR-2118.md) | Refactor trtllm_mnnvl_allreduce |
| `pr-flashinfer-2119` | upstream-code | [`sources/prs/flashinfer/PR-2119.md`](../sources/prs/flashinfer/PR-2119.md) | perf: bunch of features and optimizations for top-k (sampling + sparse attention) |
| `pr-flashinfer-2125` | upstream-code | [`sources/prs/flashinfer/PR-2125.md`](../sources/prs/flashinfer/PR-2125.md) | feat: support variable sequence length in decode kernel of trtllm-gen attention |
| `pr-flashinfer-2126` | upstream-code | [`sources/prs/flashinfer/PR-2126.md`](../sources/prs/flashinfer/PR-2126.md) | fix flaky xqa test |
| `pr-flashinfer-2127` | upstream-code | [`sources/prs/flashinfer/PR-2127.md`](../sources/prs/flashinfer/PR-2127.md) | fix: add a check for int32 indices in sampling.py |
| `pr-flashinfer-2128` | upstream-code | [`sources/prs/flashinfer/PR-2128.md`](../sources/prs/flashinfer/PR-2128.md) | fix: DeepSeek activation uninitialized data |
| `pr-flashinfer-2129` | upstream-code | [`sources/prs/flashinfer/PR-2129.md`](../sources/prs/flashinfer/PR-2129.md) | fix: Fix bench_mm_fp8.py |
| `pr-flashinfer-2130` | upstream-code | [`sources/prs/flashinfer/PR-2130.md`](../sources/prs/flashinfer/PR-2130.md) | A unified API for the MNNVL and single-node/multi-GPU AllReduce kernels. |
| `pr-flashinfer-2131` | upstream-code | [`sources/prs/flashinfer/PR-2131.md`](../sources/prs/flashinfer/PR-2131.md) | make DeepGEMM swapAB available for linear gemm SM90 |
| `pr-flashinfer-2132` | upstream-code | [`sources/prs/flashinfer/PR-2132.md`](../sources/prs/flashinfer/PR-2132.md) | feat: add seed offset args to sampler to allow cuda graph support |
| `pr-flashinfer-2134` | upstream-code | [`sources/prs/flashinfer/PR-2134.md`](../sources/prs/flashinfer/PR-2134.md) | fix(trtllm): reset negative strideBatch to 0 for ragged KV layout to … |
| `pr-flashinfer-2137` | upstream-code | [`sources/prs/flashinfer/PR-2137.md`](../sources/prs/flashinfer/PR-2137.md) | fix: some bugs of headDim 256 trtllm-gen fmha kernels.  |
| `pr-flashinfer-2138` | upstream-code | [`sources/prs/flashinfer/PR-2138.md`](../sources/prs/flashinfer/PR-2138.md) | feat: add trtllm-gen per-tensor sparseMla kernels. |
| `pr-flashinfer-2140` | upstream-code | [`sources/prs/flashinfer/PR-2140.md`](../sources/prs/flashinfer/PR-2140.md) | Use global TuningConfig, to fix memory leak caused by AutoTuner LRU cache and dynamic lambda TuningConfig |
| `pr-flashinfer-2142` | upstream-code | [`sources/prs/flashinfer/PR-2142.md`](../sources/prs/flashinfer/PR-2142.md) | feat: TRTLLM FMHAv2 backend for ctx attention |
| `pr-flashinfer-2148` | upstream-code | [`sources/prs/flashinfer/PR-2148.md`](../sources/prs/flashinfer/PR-2148.md) | Enable Hopper FA3 FP8 attention in decode.py |
| `pr-flashinfer-2149` | upstream-code | [`sources/prs/flashinfer/PR-2149.md`](../sources/prs/flashinfer/PR-2149.md) | enable sm103 moe dsl backend |
| `pr-flashinfer-2154` | upstream-code | [`sources/prs/flashinfer/PR-2154.md`](../sources/prs/flashinfer/PR-2154.md) | bugfix: add driver support to CUPTI benchmark function, issue #2145 |
| `pr-flashinfer-2157` | upstream-code | [`sources/prs/flashinfer/PR-2157.md`](../sources/prs/flashinfer/PR-2157.md) | fix xqa mha_sm90.cu |
| `pr-flashinfer-2159` | upstream-code | [`sources/prs/flashinfer/PR-2159.md`](../sources/prs/flashinfer/PR-2159.md) | feat: MxInt4 x Bf16 TRT-LLM Gen MoE support |
| `pr-flashinfer-2160` | upstream-code | [`sources/prs/flashinfer/PR-2160.md`](../sources/prs/flashinfer/PR-2160.md) | feat: C++ side tensor validation |
| `pr-flashinfer-2163` | upstream-code | [`sources/prs/flashinfer/PR-2163.md`](../sources/prs/flashinfer/PR-2163.md) | refactor: Move mla code from decode.py to mla.py and add to documentation |
| `pr-flashinfer-2165` | upstream-code | [`sources/prs/flashinfer/PR-2165.md`](../sources/prs/flashinfer/PR-2165.md) | Add data type check for deepseek fp4 moe |
| `pr-flashinfer-2171` | upstream-code | [`sources/prs/flashinfer/PR-2171.md`](../sources/prs/flashinfer/PR-2171.md) | Fix gemm allreduce two shot |
| `pr-flashinfer-2175` | upstream-code | [`sources/prs/flashinfer/PR-2175.md`](../sources/prs/flashinfer/PR-2175.md) | fix: compile flags for trtllm fmha_v2  |
| `pr-flashinfer-2178` | upstream-code | [`sources/prs/flashinfer/PR-2178.md`](../sources/prs/flashinfer/PR-2178.md) | Fix/dsl smem query |
| `pr-flashinfer-2180` | upstream-code | [`sources/prs/flashinfer/PR-2180.md`](../sources/prs/flashinfer/PR-2180.md) | benchmark: Make use_cupti the default in microbenchmarks. |
| `pr-flashinfer-2181` | upstream-code | [`sources/prs/flashinfer/PR-2181.md`](../sources/prs/flashinfer/PR-2181.md) | Rename noauxtc to fused_topk_deepseek |
| `pr-flashinfer-2190` | upstream-code | [`sources/prs/flashinfer/PR-2190.md`](../sources/prs/flashinfer/PR-2190.md) | Fix for moe on sm110 |
| `pr-flashinfer-2193` | upstream-code | [`sources/prs/flashinfer/PR-2193.md`](../sources/prs/flashinfer/PR-2193.md) | feat: unit-test and api change, w4a8 grouped-gemm fused MoE for SM90 |
| `pr-flashinfer-2194` | upstream-code | [`sources/prs/flashinfer/PR-2194.md`](../sources/prs/flashinfer/PR-2194.md) | Permute page table in benchmarking |
| `pr-flashinfer-2211` | upstream-code | [`sources/prs/flashinfer/PR-2211.md`](../sources/prs/flashinfer/PR-2211.md) | Move the run function definition out of BatchedGemmInterface |
| `pr-flashinfer-2213` | upstream-code | [`sources/prs/flashinfer/PR-2213.md`](../sources/prs/flashinfer/PR-2213.md) | feat: Cold L2 Cache Benchmarking with Rotating Buffers |
| `pr-flashinfer-2214` | upstream-code | [`sources/prs/flashinfer/PR-2214.md`](../sources/prs/flashinfer/PR-2214.md) | misc: support checks for gemm |
| `pr-flashinfer-2215` | upstream-code | [`sources/prs/flashinfer/PR-2215.md`](../sources/prs/flashinfer/PR-2215.md) | feat: further optimize top-k and add fused top-k page construction kernels for DSA |
| `pr-flashinfer-2217` | upstream-code | [`sources/prs/flashinfer/PR-2217.md`](../sources/prs/flashinfer/PR-2217.md) | feat: Support unpadded output hidden size for trtllm_fp4_block_scale_moe |
| `pr-flashinfer-2223` | upstream-code | [`sources/prs/flashinfer/PR-2223.md`](../sources/prs/flashinfer/PR-2223.md) | feat: add memcpy and memset to CUPTI timing method |
| `pr-flashinfer-2228` | upstream-code | [`sources/prs/flashinfer/PR-2228.md`](../sources/prs/flashinfer/PR-2228.md) | fix: Eliminate the usage of CUDA ARCH macro in host function. |
| `pr-flashinfer-2233` | upstream-code | [`sources/prs/flashinfer/PR-2233.md`](../sources/prs/flashinfer/PR-2233.md) | feat: Fused RMSNorm + FP4 Quantization Kernels in CuTe-DSL |
| `pr-flashinfer-2234` | upstream-code | [`sources/prs/flashinfer/PR-2234.md`](../sources/prs/flashinfer/PR-2234.md) | fix: add DeepSeek routing for Bf16xBf16 and MxIntxBf16 TRT-LLM Gen MoE |
| `pr-flashinfer-2235` | upstream-code | [`sources/prs/flashinfer/PR-2235.md`](../sources/prs/flashinfer/PR-2235.md) | refactor: pull trtllm-gen batch-gemm/gemm headers from artifactory; update tma descriptor shape init |
| `pr-flashinfer-2237` | upstream-code | [`sources/prs/flashinfer/PR-2237.md`](../sources/prs/flashinfer/PR-2237.md) | [feat] Integrate SGLang concat_mla_k kernel into flashinfer |
| `pr-flashinfer-2238` | upstream-code | [`sources/prs/flashinfer/PR-2238.md`](../sources/prs/flashinfer/PR-2238.md) | fix: Handle zeros in Mistral Large 3 MoE inference |
| `pr-flashinfer-2239` | upstream-code | [`sources/prs/flashinfer/PR-2239.md`](../sources/prs/flashinfer/PR-2239.md) | Allreduce auto backend improvements |
| `pr-flashinfer-2241` | upstream-code | [`sources/prs/flashinfer/PR-2241.md`](../sources/prs/flashinfer/PR-2241.md) | Fp8 attention are now part of cuDNN 9.17.1 |
| `pr-flashinfer-2242` | upstream-code | [`sources/prs/flashinfer/PR-2242.md`](../sources/prs/flashinfer/PR-2242.md) | fix: Fix compilation with GCC 11 |
| `pr-flashinfer-2243` | upstream-code | [`sources/prs/flashinfer/PR-2243.md`](../sources/prs/flashinfer/PR-2243.md) | feat: RMSNorm/Fused RMSNorm + FP8 Quantization kernels |
| `pr-flashinfer-2244` | upstream-code | [`sources/prs/flashinfer/PR-2244.md`](../sources/prs/flashinfer/PR-2244.md) | Remove cudaStreamSynchronize from gemm_groupwise_sm120.cuh for CUDA graph compatibility |
| `pr-flashinfer-2247` | upstream-code | [`sources/prs/flashinfer/PR-2247.md`](../sources/prs/flashinfer/PR-2247.md) | feat: Support numLocalTokens=0 for moe All-to-all |
| `pr-flashinfer-2254` | upstream-code | [`sources/prs/flashinfer/PR-2254.md`](../sources/prs/flashinfer/PR-2254.md) | feat: support non-contiguous query for trtllm-gen attention backend |
| `pr-flashinfer-2255` | upstream-code | [`sources/prs/flashinfer/PR-2255.md`](../sources/prs/flashinfer/PR-2255.md) | fix: support int64 IdType for RoPE part argument in `rope_quantize_fp8_append_paged_kv_cache` |
| `pr-flashinfer-2256` | upstream-code | [`sources/prs/flashinfer/PR-2256.md`](../sources/prs/flashinfer/PR-2256.md) | feat: Add support for bmm mxfp8 |
| `pr-flashinfer-2260` | upstream-code | [`sources/prs/flashinfer/PR-2260.md`](../sources/prs/flashinfer/PR-2260.md) | fix: Add global scale support and optional output allocation for RMSNorm+FP4Quant fusion kernels |
| `pr-flashinfer-2261` | upstream-code | [`sources/prs/flashinfer/PR-2261.md`](../sources/prs/flashinfer/PR-2261.md) | Fix CUTLASS FP8 gemm correctness issue on SM120/SM121 for shapes where N is not divisible by ScaleGranularityN. |
| `pr-flashinfer-2264` | upstream-code | [`sources/prs/flashinfer/PR-2264.md`](../sources/prs/flashinfer/PR-2264.md) | [Minor] Reduce num blocks of qknorm in small batch size |
| `pr-flashinfer-2265` | upstream-code | [`sources/prs/flashinfer/PR-2265.md`](../sources/prs/flashinfer/PR-2265.md) | [TRTLLM-Gen Fmha] add optimized trtllm-gen decode kernels for high throughput + speculative decoding |
| `pr-flashinfer-2268` | upstream-code | [`sources/prs/flashinfer/PR-2268.md`](../sources/prs/flashinfer/PR-2268.md) | [performance]optimize for nvfp4 |
| `pr-flashinfer-2276` | upstream-code | [`sources/prs/flashinfer/PR-2276.md`](../sources/prs/flashinfer/PR-2276.md) | feat: add GDN Attention |
| `pr-flashinfer-2277` | upstream-code | [`sources/prs/flashinfer/PR-2277.md`](../sources/prs/flashinfer/PR-2277.md) | Tiny fix bench tgv gemm |
| `pr-flashinfer-2279` | upstream-code | [`sources/prs/flashinfer/PR-2279.md`](../sources/prs/flashinfer/PR-2279.md) | [WIP] Refactor: simplify torch -> cute-dsl boilerplate and enable tvm-ffi for cute-dsl kernels |
| `pr-flashinfer-2281` | upstream-code | [`sources/prs/flashinfer/PR-2281.md`](../sources/prs/flashinfer/PR-2281.md) | feat: IdType indices in sampling kernels |
| `pr-flashinfer-2295` | upstream-code | [`sources/prs/flashinfer/PR-2295.md`](../sources/prs/flashinfer/PR-2295.md) | bugfix: use torch cached default generators |
| `pr-flashinfer-2301` | upstream-code | [`sources/prs/flashinfer/PR-2301.md`](../sources/prs/flashinfer/PR-2301.md) | Selective State Update kernel (mamba) |
| `pr-flashinfer-2302` | upstream-code | [`sources/prs/flashinfer/PR-2302.md`](../sources/prs/flashinfer/PR-2302.md) | fix: Decode benchmark's fa2_tc uses backend=fa2 in wrapper |
| `pr-flashinfer-2303` | upstream-code | [`sources/prs/flashinfer/PR-2303.md`](../sources/prs/flashinfer/PR-2303.md) | [Perf][Feature] Add SM103-specific schedulers for NVFP4 CUTLASS kernels |
| `pr-flashinfer-2304` | upstream-code | [`sources/prs/flashinfer/PR-2304.md`](../sources/prs/flashinfer/PR-2304.md) | feat: Support Fused MoE non gated Relu2 NVFP4 & FP8 and support Nemotron |
| `pr-flashinfer-2308` | upstream-code | [`sources/prs/flashinfer/PR-2308.md`](../sources/prs/flashinfer/PR-2308.md) | Fix: FilteredTopKUnifiedKernel read value out of length |
| `pr-flashinfer-2311` | upstream-code | [`sources/prs/flashinfer/PR-2311.md`](../sources/prs/flashinfer/PR-2311.md) | refactor: decorate all operators with @flashinfer_api |
| `pr-flashinfer-2313` | upstream-code | [`sources/prs/flashinfer/PR-2313.md`](../sources/prs/flashinfer/PR-2313.md) | tiny support glm routing |
| `pr-flashinfer-2323` | upstream-code | [`sources/prs/flashinfer/PR-2323.md`](../sources/prs/flashinfer/PR-2323.md) | [ML3] Optimized Router Gemm |
| `pr-flashinfer-2325` | upstream-code | [`sources/prs/flashinfer/PR-2325.md`](../sources/prs/flashinfer/PR-2325.md) | bugfix: fix multi-cta top-k implementation when k value is different for different row |
| `pr-flashinfer-2327` | upstream-code | [`sources/prs/flashinfer/PR-2327.md`](../sources/prs/flashinfer/PR-2327.md) | [perf] Improve gemm_fp8_nt_groupwise (cutlass backend) by 10-40% for batch sizes <= 32 |
| `pr-flashinfer-2328` | upstream-code | [`sources/prs/flashinfer/PR-2328.md`](../sources/prs/flashinfer/PR-2328.md) | fix: guard batchWarpReduceSum with ENABLE_FP8 to fix compilation without FP8 |
| `pr-flashinfer-2330` | upstream-code | [`sources/prs/flashinfer/PR-2330.md`](../sources/prs/flashinfer/PR-2330.md) | feat: expose swizzled_input_sf parameter for CUTLASS fused MOE |
| `pr-flashinfer-2343` | upstream-code | [`sources/prs/flashinfer/PR-2343.md`](../sources/prs/flashinfer/PR-2343.md) | Optimize quantization function in large problem size |
| `pr-flashinfer-2344` | upstream-code | [`sources/prs/flashinfer/PR-2344.md`](../sources/prs/flashinfer/PR-2344.md) | fix: explicitly set device to CPU for RNG state tensor |
| `pr-flashinfer-2352` | upstream-code | [`sources/prs/flashinfer/PR-2352.md`](../sources/prs/flashinfer/PR-2352.md) | Added the cudnn backend Ragged KV Cache wrapper |
| `pr-flashinfer-2362` | upstream-code | [`sources/prs/flashinfer/PR-2362.md`](../sources/prs/flashinfer/PR-2362.md) | benchmarks: Add norm and quantization routines to microbenchmark harness. |
| `pr-flashinfer-2366` | upstream-code | [`sources/prs/flashinfer/PR-2366.md`](../sources/prs/flashinfer/PR-2366.md) | Enable fp16/bf16/f32 support for selective_state_update (mamba) |
| `pr-flashinfer-2370` | upstream-code | [`sources/prs/flashinfer/PR-2370.md`](../sources/prs/flashinfer/PR-2370.md) | feat: [Qwen3-Next] Add Cute DSL GDN decode kernel and  tests |
| `pr-flashinfer-2376` | upstream-code | [`sources/prs/flashinfer/PR-2376.md`](../sources/prs/flashinfer/PR-2376.md) | feat: BF16 GEMM using cuDNN backend |
| `pr-flashinfer-2378` | upstream-code | [`sources/prs/flashinfer/PR-2378.md`](../sources/prs/flashinfer/PR-2378.md) | bugfix: hotfix of PR 2366 (mamba kernel) |
| `pr-flashinfer-2380` | upstream-code | [`sources/prs/flashinfer/PR-2380.md`](../sources/prs/flashinfer/PR-2380.md) | fix: ensure each CTA processes full numHeadsQPerKv for trtllm decode kernel |
| `pr-flashinfer-2385` | upstream-code | [`sources/prs/flashinfer/PR-2385.md`](../sources/prs/flashinfer/PR-2385.md) | fix: In-place Residual Update for add_rmsnorm_fp4quant |
| `pr-flashinfer-2387` | upstream-code | [`sources/prs/flashinfer/PR-2387.md`](../sources/prs/flashinfer/PR-2387.md) | A Blackwell-optimized version of selective_state_update (mamba) |
| `pr-flashinfer-2395` | upstream-code | [`sources/prs/flashinfer/PR-2395.md`](../sources/prs/flashinfer/PR-2395.md) | feat: Add output_both_sf_layouts option to add_rmsnorm_fp4quant API |
| `pr-flashinfer-2398` | upstream-code | [`sources/prs/flashinfer/PR-2398.md`](../sources/prs/flashinfer/PR-2398.md) | feat: cuteDSL fp4 moe for better DSR1 performance. |
| `pr-flashinfer-2404` | upstream-code | [`sources/prs/flashinfer/PR-2404.md`](../sources/prs/flashinfer/PR-2404.md) | perf: mm_fp4 heuristic prioritizes CUTLASS over cuDNN on SM103 |
| `pr-flashinfer-2405` | upstream-code | [`sources/prs/flashinfer/PR-2405.md`](../sources/prs/flashinfer/PR-2405.md) | perf: improve gdn decode cute-dsl kernels |
| `pr-flashinfer-2414` | upstream-code | [`sources/prs/flashinfer/PR-2414.md`](../sources/prs/flashinfer/PR-2414.md) | Update cudnn prefill to use correct sequence strides |
| `pr-flashinfer-2415` | upstream-code | [`sources/prs/flashinfer/PR-2415.md`](../sources/prs/flashinfer/PR-2415.md) | Remove cudaMalloc/Free in GDN prefill kernel |
| `pr-flashinfer-2416` | upstream-code | [`sources/prs/flashinfer/PR-2416.md`](../sources/prs/flashinfer/PR-2416.md) | feat: update trtllm-gen MoE cubins |
| `pr-flashinfer-2421` | upstream-code | [`sources/prs/flashinfer/PR-2421.md`](../sources/prs/flashinfer/PR-2421.md) | refactor: simplify fp4 rmsnorm |
| `pr-flashinfer-2422` | upstream-code | [`sources/prs/flashinfer/PR-2422.md`](../sources/prs/flashinfer/PR-2422.md) | refactor: reduce hopper's gdn prefill compilation time and fix docstring. |
| `pr-flashinfer-2428` | upstream-code | [`sources/prs/flashinfer/PR-2428.md`](../sources/prs/flashinfer/PR-2428.md) | refactor: refactoring cuda code to cute-dsl (part 1) |
| `pr-flashinfer-2432` | upstream-code | [`sources/prs/flashinfer/PR-2432.md`](../sources/prs/flashinfer/PR-2432.md) | fix: Sampling: CUDA Graph fix |
| `pr-flashinfer-2439` | upstream-code | [`sources/prs/flashinfer/PR-2439.md`](../sources/prs/flashinfer/PR-2439.md) | Add sm90 guard to fence ptx |
| `pr-flashinfer-2441` | upstream-code | [`sources/prs/flashinfer/PR-2441.md`](../sources/prs/flashinfer/PR-2441.md) | fix: Fix NaN output in mxfp8_quantize for very small input values |
| `pr-flashinfer-2442` | upstream-code | [`sources/prs/flashinfer/PR-2442.md`](../sources/prs/flashinfer/PR-2442.md) | Fix autotuner oom |
| `pr-flashinfer-2443` | upstream-code | [`sources/prs/flashinfer/PR-2443.md`](../sources/prs/flashinfer/PR-2443.md) | Add cute-dsl backends to mxfp[8,4]_quantization for future refactor |
| `pr-flashinfer-2444` | upstream-code | [`sources/prs/flashinfer/PR-2444.md`](../sources/prs/flashinfer/PR-2444.md) | MTP for mamba  |
| `pr-flashinfer-2445` | upstream-code | [`sources/prs/flashinfer/PR-2445.md`](../sources/prs/flashinfer/PR-2445.md) | bugfix: fix stub generation directory in fused_moe module |
| `pr-flashinfer-2446` | upstream-code | [`sources/prs/flashinfer/PR-2446.md`](../sources/prs/flashinfer/PR-2446.md) | feat: Add TRTLLM fmha_v2 library for SM90 attention with Skip-Softmax  |
| `pr-flashinfer-2456` | upstream-code | [`sources/prs/flashinfer/PR-2456.md`](../sources/prs/flashinfer/PR-2456.md) | fix: fix illegal memory access for NaN input in sampling kernels |
| `pr-flashinfer-2460` | upstream-code | [`sources/prs/flashinfer/PR-2460.md`](../sources/prs/flashinfer/PR-2460.md) | perf: add fp4 GEMM tile configs and streamK scheduler for SM120 |
| `pr-flashinfer-2462` | upstream-code | [`sources/prs/flashinfer/PR-2462.md`](../sources/prs/flashinfer/PR-2462.md) | feat: Support Fused MoE non gated Relu2 NVFP4 & FP8 and support Nemotron, fixed |
| `pr-flashinfer-2464` | upstream-code | [`sources/prs/flashinfer/PR-2464.md`](../sources/prs/flashinfer/PR-2464.md) | feat: Add MXFP8 GEMM mm_mxfp8 (cutlass) |
| `pr-flashinfer-2476` | upstream-code | [`sources/prs/flashinfer/PR-2476.md`](../sources/prs/flashinfer/PR-2476.md) | fix: blockscale moe routine supports non-DS routing |
| `pr-flashinfer-2477` | upstream-code | [`sources/prs/flashinfer/PR-2477.md`](../sources/prs/flashinfer/PR-2477.md) | feat: Add TRTLLM-Gen Skip-Softmax kernels for prefill and decode |
| `pr-flashinfer-2479` | upstream-code | [`sources/prs/flashinfer/PR-2479.md`](../sources/prs/flashinfer/PR-2479.md) | fix: Fix memory bandwidth calculation in MLA benchmarks |
| `pr-flashinfer-2484` | upstream-code | [`sources/prs/flashinfer/PR-2484.md`](../sources/prs/flashinfer/PR-2484.md) | benchmarks: Expand microbenchmark harness to include sampling and RoPe APIs |
| `pr-flashinfer-2489` | upstream-code | [`sources/prs/flashinfer/PR-2489.md`](../sources/prs/flashinfer/PR-2489.md) | [bugfix]Correct chunk_end calculation in multi-CTA collaboration when max_len > length |
| `pr-flashinfer-2495` | upstream-code | [`sources/prs/flashinfer/PR-2495.md`](../sources/prs/flashinfer/PR-2495.md) | fix: add support check for gemm config for cutlass moe |
| `pr-flashinfer-2498` | upstream-code | [`sources/prs/flashinfer/PR-2498.md`](../sources/prs/flashinfer/PR-2498.md) | Ameyn/gdn decode cutedsl kernel |
| `pr-flashinfer-2503` | upstream-code | [`sources/prs/flashinfer/PR-2503.md`](../sources/prs/flashinfer/PR-2503.md) | refactor: Port upstream CUTLASS fixes and refactor grouped_gemm_nt_masked GEMM module location |
| `pr-flashinfer-2505` | upstream-code | [`sources/prs/flashinfer/PR-2505.md`](../sources/prs/flashinfer/PR-2505.md) | Feat: Trtllm-gen MxFP8 MoE integration |
| `pr-flashinfer-2508` | upstream-code | [`sources/prs/flashinfer/PR-2508.md`](../sources/prs/flashinfer/PR-2508.md) | bugfix: fix the enum/int type mismatch mentioned in #2507 |
| `pr-flashinfer-2509` | upstream-code | [`sources/prs/flashinfer/PR-2509.md`](../sources/prs/flashinfer/PR-2509.md) | perf: cache cudaGetDeviceProperties in gdn_prefill to avoid per-call overhead |
| `pr-flashinfer-2512` | upstream-code | [`sources/prs/flashinfer/PR-2512.md`](../sources/prs/flashinfer/PR-2512.md) | benchmarks: Add microbenchmark support for Mamba selective_state_update |
| `pr-flashinfer-2520` | upstream-code | [`sources/prs/flashinfer/PR-2520.md`](../sources/prs/flashinfer/PR-2520.md) | Support NVFP4 KV cache decode on SM120 |
| `pr-flashinfer-2521` | upstream-code | [`sources/prs/flashinfer/PR-2521.md`](../sources/prs/flashinfer/PR-2521.md) | Feat/gdn decode pooled |
| `pr-flashinfer-2525` | upstream-code | [`sources/prs/flashinfer/PR-2525.md`](../sources/prs/flashinfer/PR-2525.md) | feat: BF16 GEMM benchmarking support |
| `pr-flashinfer-2530` | upstream-code | [`sources/prs/flashinfer/PR-2530.md`](../sources/prs/flashinfer/PR-2530.md) | pick fa2 for BatchDecodeWithPagedKVCacheWrapper auto backend |
| `pr-flashinfer-2533` | upstream-code | [`sources/prs/flashinfer/PR-2533.md`](../sources/prs/flashinfer/PR-2533.md) | fix: include fp8_blockscale_gemm_90 in AOT jit-cache |
| `pr-flashinfer-2534` | upstream-code | [`sources/prs/flashinfer/PR-2534.md`](../sources/prs/flashinfer/PR-2534.md) | fix: support fp32 logits for fp8_per_tensor and fp8_block |
| `pr-flashinfer-2535` | upstream-code | [`sources/prs/flashinfer/PR-2535.md`](../sources/prs/flashinfer/PR-2535.md) | Add sm90 guard to fence.acquire |
| `pr-flashinfer-2536` | upstream-code | [`sources/prs/flashinfer/PR-2536.md`](../sources/prs/flashinfer/PR-2536.md) | fallback to fa2 (instead of fa3) for unsupported configuration (bf16 Q, Fp8 KV) |
| `pr-flashinfer-2538` | upstream-code | [`sources/prs/flashinfer/PR-2538.md`](../sources/prs/flashinfer/PR-2538.md) | tests: bmm_fp8 for SM110 |
| `pr-flashinfer-2540` | upstream-code | [`sources/prs/flashinfer/PR-2540.md`](../sources/prs/flashinfer/PR-2540.md) | feat: cute dsl mmfp4 for blackwell |
| `pr-flashinfer-2543` | upstream-code | [`sources/prs/flashinfer/PR-2543.md`](../sources/prs/flashinfer/PR-2543.md) | misc: point triton blackwell-ptxas to local cuda ptxas |
| `pr-flashinfer-2547` | upstream-code | [`sources/prs/flashinfer/PR-2547.md`](../sources/prs/flashinfer/PR-2547.md) | feat: Enable TRTLLM-Gen Skip-Softmax attention for MLA |
| `pr-flashinfer-2549` | upstream-code | [`sources/prs/flashinfer/PR-2549.md`](../sources/prs/flashinfer/PR-2549.md) | Add gen_gemm_sm100_module_cutlass_mxfp8 to jit-cache |
| `pr-flashinfer-2554` | upstream-code | [`sources/prs/flashinfer/PR-2554.md`](../sources/prs/flashinfer/PR-2554.md) | feat: Add autotuner config caching, thread safety, and documentation |
| `pr-flashinfer-2557` | upstream-code | [`sources/prs/flashinfer/PR-2557.md`](../sources/prs/flashinfer/PR-2557.md) | [Bugfix][comm] Fix FP4 one-shot launch config instability in trtllm_allreduce_fusion |
| `pr-flashinfer-2559` | upstream-code | [`sources/prs/flashinfer/PR-2559.md`](../sources/prs/flashinfer/PR-2559.md) | fix: allow fmha_v2_prefill_deepseek on SM121 (DGX Spark) |
| `pr-flashinfer-2560` | upstream-code | [`sources/prs/flashinfer/PR-2560.md`](../sources/prs/flashinfer/PR-2560.md) | fix: guard CUTLASS FMHA against SM12x and fix fmha_v2 SM121a check |
| `pr-flashinfer-2563` | upstream-code | [`sources/prs/flashinfer/PR-2563.md`](../sources/prs/flashinfer/PR-2563.md) | Add support for the combinations of allreduce, allgather, and reducescatter |
| `pr-flashinfer-2564` | upstream-code | [`sources/prs/flashinfer/PR-2564.md`](../sources/prs/flashinfer/PR-2564.md) | fix: W4A8 autotune crash in cutlass_fused_moe profiler workspace |
| `pr-flashinfer-2573` | upstream-code | [`sources/prs/flashinfer/PR-2573.md`](../sources/prs/flashinfer/PR-2573.md) | [Bug] Fix spark unit test failures for test_add_rmsnorm_fp4_quant_cute_dsl |
| `pr-flashinfer-2574` | upstream-code | [`sources/prs/flashinfer/PR-2574.md`](../sources/prs/flashinfer/PR-2574.md) | feat: add is_sm12x_supported() helper for SM12x family detection |
| `pr-flashinfer-2581` | upstream-code | [`sources/prs/flashinfer/PR-2581.md`](../sources/prs/flashinfer/PR-2581.md) | Implement `cutlass_fused_moe` mxfp8 |
| `pr-flashinfer-2587` | upstream-code | [`sources/prs/flashinfer/PR-2587.md`](../sources/prs/flashinfer/PR-2587.md) | feat: trtllm tinygemm2 in flashinfer as bf16 routergemm |
| `pr-flashinfer-2588` | upstream-code | [`sources/prs/flashinfer/PR-2588.md`](../sources/prs/flashinfer/PR-2588.md) | Perf: Optimize GDN decode pretranspose kernel for all batch sizes |
| `pr-flashinfer-2591` | upstream-code | [`sources/prs/flashinfer/PR-2591.md`](../sources/prs/flashinfer/PR-2591.md) | Mamba SSU: better automatic kernel selection + algorithm selection optionally exposed to the user. |
| `pr-flashinfer-2594` | upstream-code | [`sources/prs/flashinfer/PR-2594.md`](../sources/prs/flashinfer/PR-2594.md) | Bf16 routed moe |
| `pr-flashinfer-2602` | upstream-code | [`sources/prs/flashinfer/PR-2602.md`](../sources/prs/flashinfer/PR-2602.md) | fix: get tensors by const ref to not rely on deleted move constructor for `TensorView` |
| `pr-flashinfer-2605` | upstream-code | [`sources/prs/flashinfer/PR-2605.md`](../sources/prs/flashinfer/PR-2605.md) | [bugfix] Fix FilteredTopK overflow correctness |
| `pr-flashinfer-2607` | upstream-code | [`sources/prs/flashinfer/PR-2607.md`](../sources/prs/flashinfer/PR-2607.md) | support qk_nope_head_dim for 192 check for GLM-5 |
| `pr-flashinfer-2610` | upstream-code | [`sources/prs/flashinfer/PR-2610.md`](../sources/prs/flashinfer/PR-2610.md) | Ameyn/gdn bf16 tolerance parallel reduction |
| `pr-flashinfer-2617` | upstream-code | [`sources/prs/flashinfer/PR-2617.md`](../sources/prs/flashinfer/PR-2617.md) | fix: Add tests for the AutoTuner and fix bug in _find_nearest_profile |
| `pr-flashinfer-2618` | upstream-code | [`sources/prs/flashinfer/PR-2618.md`](../sources/prs/flashinfer/PR-2618.md) | perf(gdn): optimize MTP kernel with ILP rows and SMEM v caching |
| `pr-flashinfer-2619` | upstream-code | [`sources/prs/flashinfer/PR-2619.md`](../sources/prs/flashinfer/PR-2619.md) | feat: add pool+indices support to gated_delta_rule_decode_pretranspose (bf16 path)  |
| `pr-flashinfer-2628` | upstream-code | [`sources/prs/flashinfer/PR-2628.md`](../sources/prs/flashinfer/PR-2628.md) | benchmark: Enable speculative decode microbenchmarking for paged decode |
| `pr-flashinfer-2629` | upstream-code | [`sources/prs/flashinfer/PR-2629.md`](../sources/prs/flashinfer/PR-2629.md) | fix: cute dsl nvfp4 moe routing index error |
| `pr-flashinfer-2630` | upstream-code | [`sources/prs/flashinfer/PR-2630.md`](../sources/prs/flashinfer/PR-2630.md) | Add parallel attention |
| `pr-flashinfer-2631` | upstream-code | [`sources/prs/flashinfer/PR-2631.md`](../sources/prs/flashinfer/PR-2631.md) | fix: add SM121 support to SM120 version guards |
| `pr-flashinfer-2635` | upstream-code | [`sources/prs/flashinfer/PR-2635.md`](../sources/prs/flashinfer/PR-2635.md) | benchmark: Add MXFP4/MXFP8 quantization mode support to FP4 MoE benchmark |
| `pr-flashinfer-2642` | upstream-code | [`sources/prs/flashinfer/PR-2642.md`](../sources/prs/flashinfer/PR-2642.md) | [fp8_blockwise]Fix int32 overflow in TRTLLM fused MoE activation kernel |
| `pr-flashinfer-2644` | upstream-code | [`sources/prs/flashinfer/PR-2644.md`](../sources/prs/flashinfer/PR-2644.md) | feat: FP32 dtype output for BF16 matmuls (CUTLASS & cuDNN) |
| `pr-flashinfer-2645` | upstream-code | [`sources/prs/flashinfer/PR-2645.md`](../sources/prs/flashinfer/PR-2645.md) | int16 Block-Scaled State and Stochastic Rounding for SSU (mamba) |
| `pr-flashinfer-2650` | upstream-code | [`sources/prs/flashinfer/PR-2650.md`](../sources/prs/flashinfer/PR-2650.md) | Enable sm120f compilation |
| `pr-flashinfer-2653` | upstream-code | [`sources/prs/flashinfer/PR-2653.md`](../sources/prs/flashinfer/PR-2653.md) | [feat] trtllm-gen mxfp8 gemm |
| `pr-flashinfer-2654` | upstream-code | [`sources/prs/flashinfer/PR-2654.md`](../sources/prs/flashinfer/PR-2654.md) | fix: Add fused MOE and GEMM AOT modules for SM121 |
| `pr-flashinfer-2660` | upstream-code | [`sources/prs/flashinfer/PR-2660.md`](../sources/prs/flashinfer/PR-2660.md) | feat: support mxfp4 & mxfp8 entrypoint for blackwell cutedsl dense gemm |
| `pr-flashinfer-2661` | upstream-code | [`sources/prs/flashinfer/PR-2661.md`](../sources/prs/flashinfer/PR-2661.md) | feat: implement deterministic topk |
| `pr-flashinfer-2662` | upstream-code | [`sources/prs/flashinfer/PR-2662.md`](../sources/prs/flashinfer/PR-2662.md) | fix: use current CUDA device instead of tp_rank for SymmDeviceMemory allocation |
| `pr-flashinfer-2663` | upstream-code | [`sources/prs/flashinfer/PR-2663.md`](../sources/prs/flashinfer/PR-2663.md) | feat: Autotuner support CUDA graph and cold L2 cache |
| `pr-flashinfer-2666` | upstream-code | [`sources/prs/flashinfer/PR-2666.md`](../sources/prs/flashinfer/PR-2666.md) | benchmarks: Add FP8 input / BF16 output in ragged prefill benchmark |
| `pr-flashinfer-2667` | upstream-code | [`sources/prs/flashinfer/PR-2667.md`](../sources/prs/flashinfer/PR-2667.md) | perf: Update trtllm-gen batched GEMM kernels - faster, more NVFP4 tile dims, MXFP8 with relu2 act |
| `pr-flashinfer-2670` | upstream-code | [`sources/prs/flashinfer/PR-2670.md`](../sources/prs/flashinfer/PR-2670.md) | fix: reduce smem allocation for tinygemm2 kernel in SM120 |
| `pr-flashinfer-2674` | upstream-code | [`sources/prs/flashinfer/PR-2674.md`](../sources/prs/flashinfer/PR-2674.md) | Ensure -gencode flags are in deterministic order (for ccache) |
| `pr-flashinfer-2677` | upstream-code | [`sources/prs/flashinfer/PR-2677.md`](../sources/prs/flashinfer/PR-2677.md) | feat: add support for more MLA head dimensions |
| `pr-flashinfer-2678` | upstream-code | [`sources/prs/flashinfer/PR-2678.md`](../sources/prs/flashinfer/PR-2678.md) | [chore] bench_moe_deepseek.py allows adjusting expert distribution |
| `pr-flashinfer-2679` | upstream-code | [`sources/prs/flashinfer/PR-2679.md`](../sources/prs/flashinfer/PR-2679.md) | feat(gdn): add BF16 state kernel with MTP support beyond T>4 with intermediate caching. |
| `pr-flashinfer-2688` | upstream-code | [`sources/prs/flashinfer/PR-2688.md`](../sources/prs/flashinfer/PR-2688.md) | Create separate cuDNN handle per GPU |
| `pr-flashinfer-2696` | upstream-code | [`sources/prs/flashinfer/PR-2696.md`](../sources/prs/flashinfer/PR-2696.md) | [benchmark] Add All Reduce benchmark |
| `pr-flashinfer-2697` | upstream-code | [`sources/prs/flashinfer/PR-2697.md`](../sources/prs/flashinfer/PR-2697.md) | Undo fix to AutoTuner find_nearest_profile |
| `pr-flashinfer-2699` | upstream-code | [`sources/prs/flashinfer/PR-2699.md`](../sources/prs/flashinfer/PR-2699.md) | HOTFIX: Skip mamba Stochastic Rounding tests on sm_120 |
| `pr-flashinfer-2700` | upstream-code | [`sources/prs/flashinfer/PR-2700.md`](../sources/prs/flashinfer/PR-2700.md) | Add varlen and speculative decoding support to selective state update |
| `pr-flashinfer-2702` | upstream-code | [`sources/prs/flashinfer/PR-2702.md`](../sources/prs/flashinfer/PR-2702.md) | Add NVFP4 KV cache quantization support for SM100 |
| `pr-flashinfer-2707` | upstream-code | [`sources/prs/flashinfer/PR-2707.md`](../sources/prs/flashinfer/PR-2707.md) | feat: Add support for TRTLLM MXFP8 non-gated MoE with ReLU2 |
| `pr-flashinfer-2709` | upstream-code | [`sources/prs/flashinfer/PR-2709.md`](../sources/prs/flashinfer/PR-2709.md) | Mamba2 SSD Combined Forward Pass (Blackwell CuTe DSL Kernel) |
| `pr-flashinfer-2711` | upstream-code | [`sources/prs/flashinfer/PR-2711.md`](../sources/prs/flashinfer/PR-2711.md) | feat: Add DiT-oriented kernels where Qk (Bmm1) type can be reinterpreted into Int8 or BFloat16 |
| `pr-flashinfer-2716` | upstream-code | [`sources/prs/flashinfer/PR-2716.md`](../sources/prs/flashinfer/PR-2716.md) | fix(jit): GEMM kernels produce NaN under concurrency — missing GDC flags cause PDL synchronization barriers to compile as no-ops |
| `pr-flashinfer-2725` | upstream-code | [`sources/prs/flashinfer/PR-2725.md`](../sources/prs/flashinfer/PR-2725.md) | fix: Add SM120 (RTX Blackwell desktop) support for NVFP4 MoE kernels |
| `pr-flashinfer-2726` | upstream-code | [`sources/prs/flashinfer/PR-2726.md`](../sources/prs/flashinfer/PR-2726.md) | Added missing padding |
| `pr-flashinfer-2727` | upstream-code | [`sources/prs/flashinfer/PR-2727.md`](../sources/prs/flashinfer/PR-2727.md) | [gdn] support non-contiguous state for decoding |
| `pr-flashinfer-2730` | upstream-code | [`sources/prs/flashinfer/PR-2730.md`](../sources/prs/flashinfer/PR-2730.md) | Deprecation for gated_delta_rule_mtp's intermediate_states_buffer=True |
| `pr-flashinfer-2735` | upstream-code | [`sources/prs/flashinfer/PR-2735.md`](../sources/prs/flashinfer/PR-2735.md) | fix: Fix cute dsl moe failure with nvidia-cutlass-dsl >= 4.4.0 |
| `pr-flashinfer-2738` | upstream-code | [`sources/prs/flashinfer/PR-2738.md`](../sources/prs/flashinfer/PR-2738.md) | Support for MXFP4 and NVFP4 group GEMMs on GeForce and Spark |
| `pr-flashinfer-2739` | upstream-code | [`sources/prs/flashinfer/PR-2739.md`](../sources/prs/flashinfer/PR-2739.md) | Support in-place update for `trtllm_fp8_block_scale_moe` |
| `pr-flashinfer-2740` | upstream-code | [`sources/prs/flashinfer/PR-2740.md`](../sources/prs/flashinfer/PR-2740.md) | misc: Update gemm/batched gemm cubins from trtllm-gen, gemm header refactor |
| `pr-flashinfer-2743` | upstream-code | [`sources/prs/flashinfer/PR-2743.md`](../sources/prs/flashinfer/PR-2743.md) | Add cute dsl mla decode op |
| `pr-flashinfer-2744` | upstream-code | [`sources/prs/flashinfer/PR-2744.md`](../sources/prs/flashinfer/PR-2744.md) | [feat] Add 2048 experts and 32 Top K  |
| `pr-flashinfer-2750` | upstream-code | [`sources/prs/flashinfer/PR-2750.md`](../sources/prs/flashinfer/PR-2750.md) | [Spark unit test debugging] Fix for tests/attention/test_trtllm_gen_mla.py |
| `pr-flashinfer-2751` | upstream-code | [`sources/prs/flashinfer/PR-2751.md`](../sources/prs/flashinfer/PR-2751.md) | [Spark unit test debugging] Fix for tests/gemm/test_groupwise_scaled_gemm_fp8.py |
| `pr-flashinfer-2752` | upstream-code | [`sources/prs/flashinfer/PR-2752.md`](../sources/prs/flashinfer/PR-2752.md) | [feat] Add air top-p algorithm |
| `pr-flashinfer-2756` | upstream-code | [`sources/prs/flashinfer/PR-2756.md`](../sources/prs/flashinfer/PR-2756.md) | Fix autotuner crash when input tensor is None |
| `pr-flashinfer-2757` | upstream-code | [`sources/prs/flashinfer/PR-2757.md`](../sources/prs/flashinfer/PR-2757.md) | feat: Add FP4 KV cache quant/dequant kernels  |
| `pr-flashinfer-2762` | upstream-code | [`sources/prs/flashinfer/PR-2762.md`](../sources/prs/flashinfer/PR-2762.md) | fix: fix OOB issue for vLLM |
| `pr-flashinfer-2770` | upstream-code | [`sources/prs/flashinfer/PR-2770.md`](../sources/prs/flashinfer/PR-2770.md) | feat: Expose TRT-LLM FMHA style paged KV Cache and page table layout |
| `pr-flashinfer-2772` | upstream-code | [`sources/prs/flashinfer/PR-2772.md`](../sources/prs/flashinfer/PR-2772.md) | Fix compilation error: add missing <optional> header |
| `pr-flashinfer-2777` | upstream-code | [`sources/prs/flashinfer/PR-2777.md`](../sources/prs/flashinfer/PR-2777.md) | perf: Performance tune cute dsl RMSNorm variants |
| `pr-flashinfer-2779` | upstream-code | [`sources/prs/flashinfer/PR-2779.md`](../sources/prs/flashinfer/PR-2779.md) | feat: FP8 output support for CUTLASS MLA paged attention |
| `pr-flashinfer-2780` | upstream-code | [`sources/prs/flashinfer/PR-2780.md`](../sources/prs/flashinfer/PR-2780.md) | fix(jit): enable GDC for CUTLASS GEMM PDL — SM100 flag only |
| `pr-flashinfer-2783` | upstream-code | [`sources/prs/flashinfer/PR-2783.md`](../sources/prs/flashinfer/PR-2783.md) | fix: add missing re-exports for rmsnorm quant and fused_add_rmsnorm q… |
| `pr-flashinfer-2790` | upstream-code | [`sources/prs/flashinfer/PR-2790.md`](../sources/prs/flashinfer/PR-2790.md) | Implement override shape support for cuDNN GEMM operations |
| `pr-flashinfer-2792` | upstream-code | [`sources/prs/flashinfer/PR-2792.md`](../sources/prs/flashinfer/PR-2792.md) | feat: Support padding tokens with seqlen=0 for rope+quant+kv cache update fusion kernel |
| `pr-flashinfer-2798` | upstream-code | [`sources/prs/flashinfer/PR-2798.md`](../sources/prs/flashinfer/PR-2798.md) | Upgrade cutlass 4.2.1 -> 4.4.2 |
| `pr-flashinfer-2799` | upstream-code | [`sources/prs/flashinfer/PR-2799.md`](../sources/prs/flashinfer/PR-2799.md) | [fmha-v2] Support HND and NHD paged KV cache layouts with conditional stride handling |
| `pr-flashinfer-2801` | upstream-code | [`sources/prs/flashinfer/PR-2801.md`](../sources/prs/flashinfer/PR-2801.md) | [fix] bugfix 1419: Add batch size shape validation in decode and prefill run() APIs |
| `pr-flashinfer-2802` | upstream-code | [`sources/prs/flashinfer/PR-2802.md`](../sources/prs/flashinfer/PR-2802.md) | [fix] Bugfix 1367: fix VariableBlockSparseAttention buffer overflow by dynamically resizing kv_lens_buffer |
| `pr-flashinfer-2803` | upstream-code | [`sources/prs/flashinfer/PR-2803.md`](../sources/prs/flashinfer/PR-2803.md) | Refactor the routing part |
| `pr-flashinfer-2805` | upstream-code | [`sources/prs/flashinfer/PR-2805.md`](../sources/prs/flashinfer/PR-2805.md) | [CuTe DSL] Add modular FMHA prefill and MLA decode attention kernels |
| `pr-flashinfer-2807` | upstream-code | [`sources/prs/flashinfer/PR-2807.md`](../sources/prs/flashinfer/PR-2807.md) | Build mnnvl_moe_alltoall with logger and stringUtils |
| `pr-flashinfer-2810` | upstream-code | [`sources/prs/flashinfer/PR-2810.md`](../sources/prs/flashinfer/PR-2810.md) | feat(gdn): add padding index guard for bf16 decode kernel |
| `pr-flashinfer-2811` | upstream-code | [`sources/prs/flashinfer/PR-2811.md`](../sources/prs/flashinfer/PR-2811.md) | CuteDSL MoE fix redundant output buffer zeroing |
| `pr-flashinfer-2821` | upstream-code | [`sources/prs/flashinfer/PR-2821.md`](../sources/prs/flashinfer/PR-2821.md) | fix: Autotuner _find_nearest_profile non-power-of-2 num_tokens, create launchers for all supported tileN in trtllm fused MoE |
| `pr-flashinfer-2833` | upstream-code | [`sources/prs/flashinfer/PR-2833.md`](../sources/prs/flashinfer/PR-2833.md) | feat: bump nvidia-cutlass-dsl to >=4.4.2 |
| `pr-flashinfer-2836` | upstream-code | [`sources/prs/flashinfer/PR-2836.md`](../sources/prs/flashinfer/PR-2836.md) | [Fmha] Sparse MLA decode kernel selection heuristics |
| `pr-flashinfer-2838` | upstream-code | [`sources/prs/flashinfer/PR-2838.md`](../sources/prs/flashinfer/PR-2838.md) | feat: Add CuTe-DSL backend for NVFP4 quantization |
| `pr-flashinfer-2839` | upstream-code | [`sources/prs/flashinfer/PR-2839.md`](../sources/prs/flashinfer/PR-2839.md) | [Spark bug] Fix arch 12.1 -> "sm120a" flag for Spark, CUDA 12.9 |
| `pr-flashinfer-2841` | upstream-code | [`sources/prs/flashinfer/PR-2841.md`](../sources/prs/flashinfer/PR-2841.md) | [Perf] Add FMHAv2 to flashinfer_benchmark.py and eliminate unnecessary H2D |
| `pr-flashinfer-2842` | upstream-code | [`sources/prs/flashinfer/PR-2842.md`](../sources/prs/flashinfer/PR-2842.md) | perf: Optimize GDN MTP decode kernel (v15) — eliminate ilp=1 fallback… |
| `pr-flashinfer-2844` | upstream-code | [`sources/prs/flashinfer/PR-2844.md`](../sources/prs/flashinfer/PR-2844.md) | read real strides for kv and block scale |
| `pr-flashinfer-2853` | upstream-code | [`sources/prs/flashinfer/PR-2853.md`](../sources/prs/flashinfer/PR-2853.md) | fix: int32 overflow in `trtllm_fp4_block_scale_moe` causing "Unsupported hidden state scale shape" for EP32+ configs |
| `pr-flashinfer-2855` | upstream-code | [`sources/prs/flashinfer/PR-2855.md`](../sources/prs/flashinfer/PR-2855.md) | [fix] bugfix 1044: Auto-inject well-known JIT additional tensor buffers in prefill and decode run() APIs |
| `pr-flashinfer-2857` | upstream-code | [`sources/prs/flashinfer/PR-2857.md`](../sources/prs/flashinfer/PR-2857.md) | [fix] bugfix 541: Make single_prefill/decode compatible with torch.compile CUDA graphs |
| `pr-flashinfer-2863` | upstream-code | [`sources/prs/flashinfer/PR-2863.md`](../sources/prs/flashinfer/PR-2863.md) | Yanqinz/gemm cudnn autotune fix |
| `pr-flashinfer-2864` | upstream-code | [`sources/prs/flashinfer/PR-2864.md`](../sources/prs/flashinfer/PR-2864.md) | Add support for Relu2 in BF16 fused MoE |
| `pr-flashinfer-2865` | upstream-code | [`sources/prs/flashinfer/PR-2865.md`](../sources/prs/flashinfer/PR-2865.md) | Mamba SSU: horizontal MTP kernel (+ DSTATE=96 support) |
| `pr-flashinfer-2870` | upstream-code | [`sources/prs/flashinfer/PR-2870.md`](../sources/prs/flashinfer/PR-2870.md) | fix: fix cute dsl swap_ab tactic failure |
| `pr-flashinfer-2872` | upstream-code | [`sources/prs/flashinfer/PR-2872.md`](../sources/prs/flashinfer/PR-2872.md) | fix: add cute dsl moe utils to AOT |
| `pr-flashinfer-2876` | upstream-code | [`sources/prs/flashinfer/PR-2876.md`](../sources/prs/flashinfer/PR-2876.md) | [fix] bugfix 2856: Fix pre-allocated out shape check in trtllm_batch_decode_with_kv_cache_mla for q_len_per_req > 1 |
| `pr-flashinfer-2882` | upstream-code | [`sources/prs/flashinfer/PR-2882.md`](../sources/prs/flashinfer/PR-2882.md) | Fix silent bug with FP8 per tensor non-gated MoE |
| `pr-flashinfer-2894` | upstream-code | [`sources/prs/flashinfer/PR-2894.md`](../sources/prs/flashinfer/PR-2894.md) | fix: expose trigger_completion_at_end through unified API |
| `pr-flashinfer-2898` | upstream-code | [`sources/prs/flashinfer/PR-2898.md`](../sources/prs/flashinfer/PR-2898.md) | fix: snap weight_scale_vec_size to handle block_scale_interleave padding for SM120 |
| `pr-flashinfer-2901` | upstream-code | [`sources/prs/flashinfer/PR-2901.md`](../sources/prs/flashinfer/PR-2901.md) | feat: add pdl support for cute dsl mla decode kernel support |
| `pr-flashinfer-2902` | upstream-code | [`sources/prs/flashinfer/PR-2902.md`](../sources/prs/flashinfer/PR-2902.md) | feat: add MXFP8 GEMM support for SM120 |
| `pr-flashinfer-2903` | upstream-code | [`sources/prs/flashinfer/PR-2903.md`](../sources/prs/flashinfer/PR-2903.md) | fix: avoid re-downloading BMM export headers when flashinfer-cubin is installed |
| `pr-flashinfer-2904` | upstream-code | [`sources/prs/flashinfer/PR-2904.md`](../sources/prs/flashinfer/PR-2904.md) | perf: Optimize CuTe-DSL fp4 and fp8 quantization kernels |
| `pr-flashinfer-2908` | upstream-code | [`sources/prs/flashinfer/PR-2908.md`](../sources/prs/flashinfer/PR-2908.md) | feat(gdn): state checkpointing in chunk_gated_delta_rule |
| `pr-flashinfer-2910` | upstream-code | [`sources/prs/flashinfer/PR-2910.md`](../sources/prs/flashinfer/PR-2910.md) | Yanqinz/dynamic shape unified api |
| `pr-flashinfer-2913` | upstream-code | [`sources/prs/flashinfer/PR-2913.md`](../sources/prs/flashinfer/PR-2913.md) | [NVIDIA] fix(jit): enable GDC for CUTLASS fused MoE PDL — prevent random crashes on SM12x |
| `pr-flashinfer-2914` | upstream-code | [`sources/prs/flashinfer/PR-2914.md`](../sources/prs/flashinfer/PR-2914.md) | feat: Add cuBLASLt backend for `mm_bf16` and enable multi-tactic autotuning for FP8/MXFP8 runners |
| `pr-flashinfer-2916` | upstream-code | [`sources/prs/flashinfer/PR-2916.md`](../sources/prs/flashinfer/PR-2916.md) | fix: Fix autotuner crash on meta-device tensor in trtllm_fp4_block_scale_routed_moe |
| `pr-flashinfer-2926` | upstream-code | [`sources/prs/flashinfer/PR-2926.md`](../sources/prs/flashinfer/PR-2926.md) | feat: add Relu2 (squared ReLU) activation support in CUTLASS MoE backend |
| `pr-flashinfer-2927` | upstream-code | [`sources/prs/flashinfer/PR-2927.md`](../sources/prs/flashinfer/PR-2927.md) | feat: SM121 (GB10) tile filtering and autotuner robustness |
| `pr-flashinfer-2928` | upstream-code | [`sources/prs/flashinfer/PR-2928.md`](../sources/prs/flashinfer/PR-2928.md) | fix: clamp enable_pdl=True to False on SM < 90 to prevent PDL PTX on Ampere |
| `pr-flashinfer-2931` | upstream-code | [`sources/prs/flashinfer/PR-2931.md`](../sources/prs/flashinfer/PR-2931.md) | feat: add get flashinfer-trace interface .fi_trace |
| `pr-flashinfer-2935` | upstream-code | [`sources/prs/flashinfer/PR-2935.md`](../sources/prs/flashinfer/PR-2935.md) | fix: vectorize get_shuffle_matrix_a_row_indices to eliminate CPU contention |
| `pr-flashinfer-2940` | upstream-code | [`sources/prs/flashinfer/PR-2940.md`](../sources/prs/flashinfer/PR-2940.md) | CuTe DSL FP4 GEMM Heuristic |
| `pr-flashinfer-2942` | upstream-code | [`sources/prs/flashinfer/PR-2942.md`](../sources/prs/flashinfer/PR-2942.md) | [Perf] Refactor MoE autotuning to set valid topk ids in routed MoE tuning |
| `pr-flashinfer-2944` | upstream-code | [`sources/prs/flashinfer/PR-2944.md`](../sources/prs/flashinfer/PR-2944.md) | feat: Add CuTe DSL grouped-gemm + combine fusion support |
| `pr-flashinfer-2945` | upstream-code | [`sources/prs/flashinfer/PR-2945.md`](../sources/prs/flashinfer/PR-2945.md) | fix: use float instead of double in sampling binary search to avoid FP64 bottleneck on SM103 |
| `pr-flashinfer-2948` | upstream-code | [`sources/prs/flashinfer/PR-2948.md`](../sources/prs/flashinfer/PR-2948.md) | enable_pdl_and_bias_for_cudnn_backend |
| `pr-flashinfer-2951` | upstream-code | [`sources/prs/flashinfer/PR-2951.md`](../sources/prs/flashinfer/PR-2951.md) | feat: Add DCP All-to-All kernel for context-parallel attention reduction |
| `pr-flashinfer-2954` | upstream-code | [`sources/prs/flashinfer/PR-2954.md`](../sources/prs/flashinfer/PR-2954.md) | Only swizzle on v block scale; rename kv_block_scales to kv_cache_sf |
| `pr-flashinfer-2956` | upstream-code | [`sources/prs/flashinfer/PR-2956.md`](../sources/prs/flashinfer/PR-2956.md) | [Fmha] revert blackwell ultra optimization that causes deadlocks. |
| `pr-flashinfer-2959` | upstream-code | [`sources/prs/flashinfer/PR-2959.md`](../sources/prs/flashinfer/PR-2959.md) | [Fmha] Add head_dim=512 support for trtllm attention kernels |
| `pr-flashinfer-2960` | upstream-code | [`sources/prs/flashinfer/PR-2960.md`](../sources/prs/flashinfer/PR-2960.md) | Update NVSHMEM interface to use NVSHMEM4Py instead of custom bindings |
| `pr-flashinfer-2962` | upstream-code | [`sources/prs/flashinfer/PR-2962.md`](../sources/prs/flashinfer/PR-2962.md) | Improved `simple` mamba SSU kernel  |
| `pr-flashinfer-2965` | upstream-code | [`sources/prs/flashinfer/PR-2965.md`](../sources/prs/flashinfer/PR-2965.md) | Add flashinfer.fused_rmsnorm_silu() with native kernel backend |
| `pr-flashinfer-2966` | upstream-code | [`sources/prs/flashinfer/PR-2966.md`](../sources/prs/flashinfer/PR-2966.md) | Fused moe all-reduce routed scaling factor + quant support |
| `pr-flashinfer-2979` | upstream-code | [`sources/prs/flashinfer/PR-2979.md`](../sources/prs/flashinfer/PR-2979.md) | Add filelock to ensure_symlink |
| `pr-flashinfer-2982` | upstream-code | [`sources/prs/flashinfer/PR-2982.md`](../sources/prs/flashinfer/PR-2982.md) | feat(comm): add MOE Finalize/Reduction patterns to unified allreduce_fusion API |
| `pr-flashinfer-2984` | upstream-code | [`sources/prs/flashinfer/PR-2984.md`](../sources/prs/flashinfer/PR-2984.md) | fix: restore SM120 CUTLASS MoE tile candidate removed by #2927 (test_trtllm_cutlass_fused_moe.py) |
| `pr-flashinfer-2988` | upstream-code | [`sources/prs/flashinfer/PR-2988.md`](../sources/prs/flashinfer/PR-2988.md) | [Fmha] support nvfp4 output keepsMmaAb generation kernels |
| `pr-flashinfer-2991` | upstream-code | [`sources/prs/flashinfer/PR-2991.md`](../sources/prs/flashinfer/PR-2991.md) | Add SM 103 as one of supported capabilities for mm_M1_16_K7168_N256 |
| `pr-flashinfer-2993` | upstream-code | [`sources/prs/flashinfer/PR-2993.md`](../sources/prs/flashinfer/PR-2993.md) | Second part of refactoring the routing part |
| `pr-flashinfer-2994` | upstream-code | [`sources/prs/flashinfer/PR-2994.md`](../sources/prs/flashinfer/PR-2994.md) |   Fix MXFP4/MXFP8 failures in SM120 FAST_BUILD and expand all_tiles[]                                                   |
| `pr-flashinfer-2996` | upstream-code | [`sources/prs/flashinfer/PR-2996.md`](../sources/prs/flashinfer/PR-2996.md) | fix: tinygemm2 hang issue due to barrier sync |
| `pr-flashinfer-3001` | upstream-code | [`sources/prs/flashinfer/PR-3001.md`](../sources/prs/flashinfer/PR-3001.md) | [feat] Add blackwell GDN prefill kernel |
| `pr-flashinfer-3002` | upstream-code | [`sources/prs/flashinfer/PR-3002.md`](../sources/prs/flashinfer/PR-3002.md) | bench: Enable microbenchmarking on SM121 |
| `pr-flashinfer-3007` | upstream-code | [`sources/prs/flashinfer/PR-3007.md`](../sources/prs/flashinfer/PR-3007.md) | fix: use sym_int64 for strides in rmsnorm CuTe DSL kernels to prevent int32 overflow |
| `pr-flashinfer-3008` | upstream-code | [`sources/prs/flashinfer/PR-3008.md`](../sources/prs/flashinfer/PR-3008.md) | feat: add PDL support to rmsnorm_fp4quant and add_rmsnorm_fp4quant CuTe DSL kernels |
| `pr-flashinfer-3009` | upstream-code | [`sources/prs/flashinfer/PR-3009.md`](../sources/prs/flashinfer/PR-3009.md) | [feat] Faster topk algorithm |
| `pr-flashinfer-3014` | upstream-code | [`sources/prs/flashinfer/PR-3014.md`](../sources/prs/flashinfer/PR-3014.md) | perf: Optimize CUTLASS MoE helper kernels for small-batch decode workloads |
| `pr-flashinfer-3019` | upstream-code | [`sources/prs/flashinfer/PR-3019.md`](../sources/prs/flashinfer/PR-3019.md) | docs(gdn): document -1 padding index semantics for pool+indices path |
| `pr-flashinfer-3021` | upstream-code | [`sources/prs/flashinfer/PR-3021.md`](../sources/prs/flashinfer/PR-3021.md) | fix: extend moe alltoall top-k specializations |
| `pr-flashinfer-3024` | upstream-code | [`sources/prs/flashinfer/PR-3024.md`](../sources/prs/flashinfer/PR-3024.md) | [feat] Add routing_replay_out support to MoE kernels and Python API |
| `pr-flashinfer-3025` | upstream-code | [`sources/prs/flashinfer/PR-3025.md`](../sources/prs/flashinfer/PR-3025.md) | Prevent MoE autotuner buffer overflow on large token buckets |
| `pr-flashinfer-3026` | upstream-code | [`sources/prs/flashinfer/PR-3026.md`](../sources/prs/flashinfer/PR-3026.md) | perf: Port TRT-LLM SM120/SM121 FP4 CUTLASS GEMM optimizations. Add PDL |
| `pr-flashinfer-3027` | upstream-code | [`sources/prs/flashinfer/PR-3027.md`](../sources/prs/flashinfer/PR-3027.md) | [feat] Trtllm-gen Per-token Nvfp4 MoE |
| `pr-flashinfer-3032` | upstream-code | [`sources/prs/flashinfer/PR-3032.md`](../sources/prs/flashinfer/PR-3032.md) | fused_moe: pre-filter SM89 tactics with zero occupancy on SM120 Blackwell (fix review feedback on #2764) |
| `pr-flashinfer-3039` | upstream-code | [`sources/prs/flashinfer/PR-3039.md`](../sources/prs/flashinfer/PR-3039.md) | feat: Integrate CuTe DSL FMHA prefill kernels by loading cubin |
| `pr-flashinfer-3040` | upstream-code | [`sources/prs/flashinfer/PR-3040.md`](../sources/prs/flashinfer/PR-3040.md) | [chore] Fix CI pre-commit mypy error |
| `pr-flashinfer-3050` | upstream-code | [`sources/prs/flashinfer/PR-3050.md`](../sources/prs/flashinfer/PR-3050.md) | [fmhav2] skip fp8 tests and add warning |
| `pr-flashinfer-3051` | upstream-code | [`sources/prs/flashinfer/PR-3051.md`](../sources/prs/flashinfer/PR-3051.md) | feat: Add backend="b12x" for mm_fp4 on SM120 |
| `pr-flashinfer-3056` | upstream-code | [`sources/prs/flashinfer/PR-3056.md`](../sources/prs/flashinfer/PR-3056.md) | PR #2772 might have introduced a device side compilation regression |
| `pr-flashinfer-3058` | upstream-code | [`sources/prs/flashinfer/PR-3058.md`](../sources/prs/flashinfer/PR-3058.md) | Support lse in trtllm paged attn kernels |
| `pr-flashinfer-3059` | upstream-code | [`sources/prs/flashinfer/PR-3059.md`](../sources/prs/flashinfer/PR-3059.md) | Support Allreduce + Norm + Per-token Group Fp8 Quant Fusion |
| `pr-flashinfer-3066` | upstream-code | [`sources/prs/flashinfer/PR-3066.md`](../sources/prs/flashinfer/PR-3066.md) | feat: Add b12x CuTe DSL fused MoE for SM120 |
| `pr-flashinfer-3080` | upstream-code | [`sources/prs/flashinfer/PR-3080.md`](../sources/prs/flashinfer/PR-3080.md) | feat: Add b12x_fused_moe / B12xMoEWrapper SM120 APIs with micro kernel and ReLU2 |
| `pr-flashinfer-3082` | upstream-code | [`sources/prs/flashinfer/PR-3082.md`](../sources/prs/flashinfer/PR-3082.md) | fix: guard MXFP8 fc1 weight shape check for non-gated activations |
| `pr-flashinfer-3084` | upstream-code | [`sources/prs/flashinfer/PR-3084.md`](../sources/prs/flashinfer/PR-3084.md) | perf: optimize MXFP4xBF16 & INT4xFP8 CUTLASS MoE backend for SM90 |
| `pr-flashinfer-3089` | upstream-code | [`sources/prs/flashinfer/PR-3089.md`](../sources/prs/flashinfer/PR-3089.md) | [Fmha] update trtllm-gen FMHA cubins and sync headers for context SWA fix |
| `pr-flashinfer-3091` | upstream-code | [`sources/prs/flashinfer/PR-3091.md`](../sources/prs/flashinfer/PR-3091.md) | Vendor CCCL v3.3.2 from GitHub instead of relying on CTK-bundled copy |
| `pr-flashinfer-3092` | upstream-code | [`sources/prs/flashinfer/PR-3092.md`](../sources/prs/flashinfer/PR-3092.md) | Add examples of calling FlashInfer from JAX via jax-tvm-ffi |
| `pr-flashinfer-3094` | upstream-code | [`sources/prs/flashinfer/PR-3094.md`](../sources/prs/flashinfer/PR-3094.md) | Route the missing parameter for `trtllm_fp8_per_tensor_scale_moe_op`   |
| `pr-flashinfer-3097` | upstream-code | [`sources/prs/flashinfer/PR-3097.md`](../sources/prs/flashinfer/PR-3097.md) | Support NVFP4 KV for prefill and batch attention kernels |
| `pr-flashinfer-3113` | upstream-code | [`sources/prs/flashinfer/PR-3113.md`](../sources/prs/flashinfer/PR-3113.md) | Fix: Extend b12x FP4 GEMM support to SM121 (GB10/DGX Spark) |
| `pr-flashinfer-3115` | upstream-code | [`sources/prs/flashinfer/PR-3115.md`](../sources/prs/flashinfer/PR-3115.md) | perf(autotuner): replace power-of-2 token buckets with hybrid spacing & fix missing routing_replay_out arg |
| `pr-flashinfer-3128` | upstream-code | [`sources/prs/flashinfer/PR-3128.md`](../sources/prs/flashinfer/PR-3128.md) | chore: Address non-blocking review feedback for #3051 / #3080 |
| `pr-flashinfer-3129` | upstream-code | [`sources/prs/flashinfer/PR-3129.md`](../sources/prs/flashinfer/PR-3129.md) | feat: Enable FP8 (E4M3/E5M2) in concat_mla_k for optimize long-context prefill performance and refactor type dispatch for BF16/FP16 |
| `pr-flashinfer-3132` | upstream-code | [`sources/prs/flashinfer/PR-3132.md`](../sources/prs/flashinfer/PR-3132.md) | [CuTe DSL] Fix FP8 MLA persistent perf regression and ProxyKind cu13 wheel breakage |
| `pr-flashinfer-3151` | upstream-code | [`sources/prs/flashinfer/PR-3151.md`](../sources/prs/flashinfer/PR-3151.md) | perf: Add no-bias path for tinygemm_bf16 |
| `pr-flashinfer-3152` | upstream-code | [`sources/prs/flashinfer/PR-3152.md`](../sources/prs/flashinfer/PR-3152.md) | Integrate CUTLASS Small Tile N Blockscaled GEMMs/Grouped GEMMs for SM120 and SM121 |
| `pr-flashinfer-3155` | upstream-code | [`sources/prs/flashinfer/PR-3155.md`](../sources/prs/flashinfer/PR-3155.md) | fix(gdn): use physical SM count for SM100 persistent prefill kernel |
| `pr-flashinfer-3156` | upstream-code | [`sources/prs/flashinfer/PR-3156.md`](../sources/prs/flashinfer/PR-3156.md) | [fix] fix blackwell gdn accuracy issue |
| `pr-flashinfer-3157` | upstream-code | [`sources/prs/flashinfer/PR-3157.md`](../sources/prs/flashinfer/PR-3157.md) | feat: DiT layer norm fusions for WAN: flashinfer.diffusion_ops |
| `pr-flashinfer-3158` | upstream-code | [`sources/prs/flashinfer/PR-3158.md`](../sources/prs/flashinfer/PR-3158.md) | CICD bug fix: ensure data/ symlinks exist before jit-cache AOT compilation |
| `pr-flashinfer-3181` | upstream-code | [`sources/prs/flashinfer/PR-3181.md`](../sources/prs/flashinfer/PR-3181.md) | cute-dsl fmha prefill (cubin integration): remove front-padding, add attention_sink, and pdl support |
| `pr-flashinfer-3185` | upstream-code | [`sources/prs/flashinfer/PR-3185.md`](../sources/prs/flashinfer/PR-3185.md) | feat: enable glm5 router gemm |
| `pr-flashinfer-3191` | upstream-code | [`sources/prs/flashinfer/PR-3191.md`](../sources/prs/flashinfer/PR-3191.md) | fix(sm12x): fix micro-kernel workspace sizing when routed_rows > num_local_experts |
| `pr-flashinfer-3193` | upstream-code | [`sources/prs/flashinfer/PR-3193.md`](../sources/prs/flashinfer/PR-3193.md) | perf(moe): optimize SM120 b12x MoE short decode |
| `pr-flashinfer-3203` | upstream-code | [`sources/prs/flashinfer/PR-3203.md`](../sources/prs/flashinfer/PR-3203.md) | Include TinyGEMM into BF16 autotuner |
| `pr-flashinfer-3216` | upstream-code | [`sources/prs/flashinfer/PR-3216.md`](../sources/prs/flashinfer/PR-3216.md) | fix(cute_dsl/moe): make autotuner bucket configuration adapt to runtime input |
| `pr-flashinfer-3227` | upstream-code | [`sources/prs/flashinfer/PR-3227.md`](../sources/prs/flashinfer/PR-3227.md) | [Bugfix] Fix fused MoE autotuning correctness issues by filtering clusterDimZ |
| `pr-flashinfer-3235` | upstream-code | [`sources/prs/flashinfer/PR-3235.md`](../sources/prs/flashinfer/PR-3235.md) | Support Kimi K2.5 H64 CuTe DSL MLA decode |
| `pr-flashinfer-3237` | upstream-code | [`sources/prs/flashinfer/PR-3237.md`](../sources/prs/flashinfer/PR-3237.md) | perf: optimize per-token nvfp4 quantization kernel. |
| `pr-flashinfer-3239` | upstream-code | [`sources/prs/flashinfer/PR-3239.md`](../sources/prs/flashinfer/PR-3239.md) | Update moe gemm |
| `pr-flashinfer-3252` | upstream-code | [`sources/prs/flashinfer/PR-3252.md`](../sources/prs/flashinfer/PR-3252.md) | fix(cute_dsl/moe): unbias autotuner profiling for tile_size enumeration |
| `pr-flashinfer-3259` | upstream-code | [`sources/prs/flashinfer/PR-3259.md`](../sources/prs/flashinfer/PR-3259.md) | Add dynamic tokens-per-page TRTLLM-GEN GQA kernels |
| `pr-flashinfer-3271` | upstream-code | [`sources/prs/flashinfer/PR-3271.md`](../sources/prs/flashinfer/PR-3271.md) | feat(moe): add SM120 W4A16 b12x kernels |
| `pr-flashinfer-3276` | upstream-code | [`sources/prs/flashinfer/PR-3276.md`](../sources/prs/flashinfer/PR-3276.md) | fix(fmha_v2): fix FP8 V-scratch pipeline and varlen scheduler on SM90 |
| `pr-flashinfer-714` | upstream-code | [`sources/prs/flashinfer/PR-714.md`](../sources/prs/flashinfer/PR-714.md) | perf: fix the iteration bound of SWA in FA2 prefill template |
| `pr-flashinfer-718` | upstream-code | [`sources/prs/flashinfer/PR-718.md`](../sources/prs/flashinfer/PR-718.md) | bugfix: FusedAddRMSNorm kernels might require more than 48KB shared memory when d is large. |
| `pr-flashinfer-719` | upstream-code | [`sources/prs/flashinfer/PR-719.md`](../sources/prs/flashinfer/PR-719.md) | bugfix: Choose sm90 kernels only for Hopper GPUs. |
| `pr-flashinfer-728` | upstream-code | [`sources/prs/flashinfer/PR-728.md`](../sources/prs/flashinfer/PR-728.md) | Align KV chunk size binary search with actual KV chunk splitting. |
| `pr-flashinfer-748` | upstream-code | [`sources/prs/flashinfer/PR-748.md`](../sources/prs/flashinfer/PR-748.md) | [Refactor] Unify JIT/Customization/AOT mode |
| `pr-flashinfer-752` | upstream-code | [`sources/prs/flashinfer/PR-752.md`](../sources/prs/flashinfer/PR-752.md) | bugfix: various AOT issues |
| `pr-flashinfer-753` | upstream-code | [`sources/prs/flashinfer/PR-753.md`](../sources/prs/flashinfer/PR-753.md) | [bugfix] Fix cpp tests/benchmarks |
| `pr-flashinfer-754` | upstream-code | [`sources/prs/flashinfer/PR-754.md`](../sources/prs/flashinfer/PR-754.md) | Change `apply_rope_with_cos_sin_cache` to accept `cos_sin_cache` |
| `pr-flashinfer-755` | upstream-code | [`sources/prs/flashinfer/PR-755.md`](../sources/prs/flashinfer/PR-755.md) | fix pin memory device |
| `pr-flashinfer-757` | upstream-code | [`sources/prs/flashinfer/PR-757.md`](../sources/prs/flashinfer/PR-757.md) | hotfix: bugfix to #756 |
| `pr-flashinfer-759` | upstream-code | [`sources/prs/flashinfer/PR-759.md`](../sources/prs/flashinfer/PR-759.md) | fix: match statement not supported in Python 3.8 |
| `pr-flashinfer-762` | upstream-code | [`sources/prs/flashinfer/PR-762.md`](../sources/prs/flashinfer/PR-762.md) | bugfix: use actual sm count for num_sm90_ctas |
| `pr-flashinfer-764` | upstream-code | [`sources/prs/flashinfer/PR-764.md`](../sources/prs/flashinfer/PR-764.md) | refactor: change to TORCH_LIBRARY |
| `pr-flashinfer-765` | upstream-code | [`sources/prs/flashinfer/PR-765.md`](../sources/prs/flashinfer/PR-765.md) | feat: support deepseek prefill attention shape |
| `pr-flashinfer-774` | upstream-code | [`sources/prs/flashinfer/PR-774.md`](../sources/prs/flashinfer/PR-774.md) | bugfix: Ensure Loop Termination by Enforcing IEEE-754 Compliance in Sampling Kernels |
| `pr-flashinfer-776` | upstream-code | [`sources/prs/flashinfer/PR-776.md`](../sources/prs/flashinfer/PR-776.md) | perf: refactor fa2 prefill template |
| `pr-flashinfer-778` | upstream-code | [`sources/prs/flashinfer/PR-778.md`](../sources/prs/flashinfer/PR-778.md) | feat: Separate QK/VO head dim dispatch for sm90 AOT |
| `pr-flashinfer-785` | upstream-code | [`sources/prs/flashinfer/PR-785.md`](../sources/prs/flashinfer/PR-785.md) | bugfix: drop CTA_TILE_Q=32 |
| `pr-flashinfer-787` | upstream-code | [`sources/prs/flashinfer/PR-787.md`](../sources/prs/flashinfer/PR-787.md) | bugfix: MLA decode should multiply sm_scale by math::log2e |
| `pr-flashinfer-793` | upstream-code | [`sources/prs/flashinfer/PR-793.md`](../sources/prs/flashinfer/PR-793.md) | fix rope logic in mla decoding |
| `pr-flashinfer-795` | upstream-code | [`sources/prs/flashinfer/PR-795.md`](../sources/prs/flashinfer/PR-795.md) | Fix arguments of `plan` for split QK/VO head dims |
| `pr-flashinfer-798` | upstream-code | [`sources/prs/flashinfer/PR-798.md`](../sources/prs/flashinfer/PR-798.md) | Fix the type annotation of q_dtype and kv_dtype on ragged prefill |
| `pr-flashinfer-799` | upstream-code | [`sources/prs/flashinfer/PR-799.md`](../sources/prs/flashinfer/PR-799.md) | feat: support f32 attention output in FA2 template |
| `pr-flashinfer-801` | upstream-code | [`sources/prs/flashinfer/PR-801.md`](../sources/prs/flashinfer/PR-801.md) | feat: apply sm_scale at logits instead of q in FA2 template |
| `pr-flashinfer-804` | upstream-code | [`sources/prs/flashinfer/PR-804.md`](../sources/prs/flashinfer/PR-804.md) | perf: memory efficient deepseek mla fused page-attention kernel |
| `pr-flashinfer-808` | upstream-code | [`sources/prs/flashinfer/PR-808.md`](../sources/prs/flashinfer/PR-808.md) | fix: Pass backend in BatchPrefillWith*KVCacheWrapper.plan() |
| `pr-flashinfer-810` | upstream-code | [`sources/prs/flashinfer/PR-810.md`](../sources/prs/flashinfer/PR-810.md) | bugfix: mla page-attention kernel for different page sizes |
| `pr-flashinfer-812` | upstream-code | [`sources/prs/flashinfer/PR-812.md`](../sources/prs/flashinfer/PR-812.md) | feat: unlocking MLA for A100 |
| `pr-flashinfer-814` | upstream-code | [`sources/prs/flashinfer/PR-814.md`](../sources/prs/flashinfer/PR-814.md) | feat: unlock MLA attention for sm89 (L40/L40s/4090) |
| `pr-flashinfer-821` | upstream-code | [`sources/prs/flashinfer/PR-821.md`](../sources/prs/flashinfer/PR-821.md) | bugfix: bugfix on sm89 MLA |
| `pr-flashinfer-827` | upstream-code | [`sources/prs/flashinfer/PR-827.md`](../sources/prs/flashinfer/PR-827.md) | bugfix: fix the signature of `CutlassSegmentGEMMSM90` |
| `pr-flashinfer-828` | upstream-code | [`sources/prs/flashinfer/PR-828.md`](../sources/prs/flashinfer/PR-828.md) | bugfix: Another bugfix for torch.library |
| `pr-flashinfer-844` | upstream-code | [`sources/prs/flashinfer/PR-844.md`](../sources/prs/flashinfer/PR-844.md) | perf: MLA decode kernel implemented by CuTe targeted to SM80 |
| `pr-flashinfer-847` | upstream-code | [`sources/prs/flashinfer/PR-847.md`](../sources/prs/flashinfer/PR-847.md) | bugfix: Fix inline RoPE in decode kernels |
| `pr-flashinfer-858` | upstream-code | [`sources/prs/flashinfer/PR-858.md`](../sources/prs/flashinfer/PR-858.md) | Add POD-Attention to FlashInfer |
| `pr-flashinfer-863` | upstream-code | [`sources/prs/flashinfer/PR-863.md`](../sources/prs/flashinfer/PR-863.md) | perf: dynamic split-k for MLA |
| `pr-flashinfer-868` | upstream-code | [`sources/prs/flashinfer/PR-868.md`](../sources/prs/flashinfer/PR-868.md) | bugfix: fix the behavior of MLA kernel when kv-length is 0 |
| `pr-flashinfer-869` | upstream-code | [`sources/prs/flashinfer/PR-869.md`](../sources/prs/flashinfer/PR-869.md) | Naive Support for Hopper FP8 Prefill Kernel with Per-Head Quantization |
| `pr-flashinfer-880` | upstream-code | [`sources/prs/flashinfer/PR-880.md`](../sources/prs/flashinfer/PR-880.md) | JIT compilation support for TVM |
| `pr-flashinfer-887` | upstream-code | [`sources/prs/flashinfer/PR-887.md`](../sources/prs/flashinfer/PR-887.md) | perf: FlashAttention-3 style MLA PageAttention |
| `pr-flashinfer-888` | upstream-code | [`sources/prs/flashinfer/PR-888.md`](../sources/prs/flashinfer/PR-888.md) | feat - support mla kvcache store |
| `pr-flashinfer-898` | upstream-code | [`sources/prs/flashinfer/PR-898.md`](../sources/prs/flashinfer/PR-898.md) | perf: fix MLA split-k performance bug |
| `pr-flashinfer-901` | upstream-code | [`sources/prs/flashinfer/PR-901.md`](../sources/prs/flashinfer/PR-901.md) | perf: tweak the pipeline design of mla kernel |
| `pr-flashinfer-904` | upstream-code | [`sources/prs/flashinfer/PR-904.md`](../sources/prs/flashinfer/PR-904.md) | bugfix: Fix no return type error |
| `pr-flashinfer-913` | upstream-code | [`sources/prs/flashinfer/PR-913.md`](../sources/prs/flashinfer/PR-913.md) | feat: flashinfer intra-kernel profiler |
| `pr-flashinfer-930` | upstream-code | [`sources/prs/flashinfer/PR-930.md`](../sources/prs/flashinfer/PR-930.md) | feat: experimenta support of PDL |
| `pr-flashinfer-942` | upstream-code | [`sources/prs/flashinfer/PR-942.md`](../sources/prs/flashinfer/PR-942.md) | fix - fix bug when not relevant seq has nan data |
| `pr-flashinfer-945` | upstream-code | [`sources/prs/flashinfer/PR-945.md`](../sources/prs/flashinfer/PR-945.md) | bugfix: fix potential issues of FA3 template loading nans for PageAttention |
| `pr-flashinfer-951` | upstream-code | [`sources/prs/flashinfer/PR-951.md`](../sources/prs/flashinfer/PR-951.md) | bugfix: bugfix to #949 |
| `pr-flashinfer-952` | upstream-code | [`sources/prs/flashinfer/PR-952.md`](../sources/prs/flashinfer/PR-952.md) | perf: Use 2WG pipeline design for MLA implementation on Hopper |
| `pr-flashinfer-958` | upstream-code | [`sources/prs/flashinfer/PR-958.md`](../sources/prs/flashinfer/PR-958.md) | [TVM] Added tvm binding for sampling kernel |
| `pr-flashinfer-961` | upstream-code | [`sources/prs/flashinfer/PR-961.md`](../sources/prs/flashinfer/PR-961.md) | Fix compilation on cuda 12.2 |
| `pr-flashinfer-968` | upstream-code | [`sources/prs/flashinfer/PR-968.md`](../sources/prs/flashinfer/PR-968.md) | perf: reduce torch.library dispatch overhead |
| `pr-flashinfer-969` | upstream-code | [`sources/prs/flashinfer/PR-969.md`](../sources/prs/flashinfer/PR-969.md) | perf: Fix python API overhead when CUDAGraph is not enabled |
| `pr-flashinfer-970` | upstream-code | [`sources/prs/flashinfer/PR-970.md`](../sources/prs/flashinfer/PR-970.md) | benchmark: add sampling.renorm benchmarks |
| `pr-flashinfer-974` | upstream-code | [`sources/prs/flashinfer/PR-974.md`](../sources/prs/flashinfer/PR-974.md) | perf: dual pivot top-p/top-k renorm |
| `pr-flashinfer-982` | upstream-code | [`sources/prs/flashinfer/PR-982.md`](../sources/prs/flashinfer/PR-982.md) | SM-constraint-GEMM by triton persistent kernel |
| `pr-flashinfer-983` | upstream-code | [`sources/prs/flashinfer/PR-983.md`](../sources/prs/flashinfer/PR-983.md) | Triton `rms_norm` kernels |
| `pr-flashinfer-991` | upstream-code | [`sources/prs/flashinfer/PR-991.md`](../sources/prs/flashinfer/PR-991.md) | perf: prefetch page indices for mla kernel |
| `pr-flashinfer-994` | upstream-code | [`sources/prs/flashinfer/PR-994.md`](../sources/prs/flashinfer/PR-994.md) | feat: SM-constraint Communication Kernels |
| `pr-flashinfer-997` | upstream-code | [`sources/prs/flashinfer/PR-997.md`](../sources/prs/flashinfer/PR-997.md) | 3rdparty: upgrade cutlass to 3.9 |
| `pr-flashinfer-998` | upstream-code | [`sources/prs/flashinfer/PR-998.md`](../sources/prs/flashinfer/PR-998.md) | perf: add `-DNDEBUG` compilation flag |

<a id="pytorchpytorch"></a>
## pytorch/pytorch

75 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-pytorch-116518` | upstream-code | [`sources/prs/pytorch/PR-116518.md`](../sources/prs/pytorch/PR-116518.md) | [CUDA] baddmm should fall back to addmm for batch=1 (#114992) |
| `pr-pytorch-119003` | upstream-code | [`sources/prs/pytorch/PR-119003.md`](../sources/prs/pytorch/PR-119003.md) | [Inductor max autotune] Multithreaded Precompilation |
| `pr-pytorch-122139` | upstream-code | [`sources/prs/pytorch/PR-122139.md`](../sources/prs/pytorch/PR-122139.md) | necessary change to make torch2.3 work with triton2.2 |
| `pr-pytorch-122967` | upstream-code | [`sources/prs/pytorch/PR-122967.md`](../sources/prs/pytorch/PR-122967.md) | Fix performance regression and memory storage handling of Flash Attention on ROCM (#122857) |
| `pr-pytorch-128539` | upstream-code | [`sources/prs/pytorch/PR-128539.md`](../sources/prs/pytorch/PR-128539.md) | Revert "[cuDNN][SDPA] Remove `TORCH_CUDNN_SDPA_ENABLED=1`, enable cuDNN SDPA by default on H100 and 2nd on other archs >= sm80 (#125343)" |
| `pr-pytorch-129499` | upstream-code | [`sources/prs/pytorch/PR-129499.md`](../sources/prs/pytorch/PR-129499.md) |   TunableOp hotfix |
| `pr-pytorch-130788` | upstream-code | [`sources/prs/pytorch/PR-130788.md`](../sources/prs/pytorch/PR-130788.md) | Add flex decoding to score_mod benchmark |
| `pr-pytorch-130854` | upstream-code | [`sources/prs/pytorch/PR-130854.md`](../sources/prs/pytorch/PR-130854.md) | Add flex decoding + block mask support to score_mod benchmark |
| `pr-pytorch-135561` | upstream-code | [`sources/prs/pytorch/PR-135561.md`](../sources/prs/pytorch/PR-135561.md) | [inductor] [cpp] fix the input contiguous check in max-autotune |
| `pr-pytorch-135869` | upstream-code | [`sources/prs/pytorch/PR-135869.md`](../sources/prs/pytorch/PR-135869.md) | [ROCm] Update to AOTriton 0.7b (Cherry-picked) |
| `pr-pytorch-136536` | upstream-code | [`sources/prs/pytorch/PR-136536.md`](../sources/prs/pytorch/PR-136536.md) | SDPA regression fix to work around high-precision by default |
| `pr-pytorch-136885` | upstream-code | [`sources/prs/pytorch/PR-136885.md`](../sources/prs/pytorch/PR-136885.md) | [cuDNN][SDPA] cherrypick Support `attn_bias` in cuDNN (#130482) |
| `pr-pytorch-138587` | upstream-code | [`sources/prs/pytorch/PR-138587.md`](../sources/prs/pytorch/PR-138587.md) | [SDPA-CUDNN] Make CuDNN Attention Opt in |
| `pr-pytorch-144248` | upstream-code | [`sources/prs/pytorch/PR-144248.md`](../sources/prs/pytorch/PR-144248.md) | [inductor][cpu] Fix bmm b_index for dynamic expressions in inductor autotuner |
| `pr-pytorch-144398` | upstream-code | [`sources/prs/pytorch/PR-144398.md`](../sources/prs/pytorch/PR-144398.md) | ROCm SDPA: Ensure attn_mask has the same dtype with q |
| `pr-pytorch-144484` | upstream-code | [`sources/prs/pytorch/PR-144484.md`](../sources/prs/pytorch/PR-144484.md) | Cleanup gpt_fast benchmark |
| `pr-pytorch-149125` | upstream-code | [`sources/prs/pytorch/PR-149125.md`](../sources/prs/pytorch/PR-149125.md) | Remove runtime dependency on packaging |
| `pr-pytorch-149386` | upstream-code | [`sources/prs/pytorch/PR-149386.md`](../sources/prs/pytorch/PR-149386.md) | Add AOTI shim for _weight_int4pack_mm_cpu_tensor (#149031) |
| `pr-pytorch-149644` | upstream-code | [`sources/prs/pytorch/PR-149644.md`](../sources/prs/pytorch/PR-149644.md) | op should NOT be static in aoti_torch_call_dispatcher |
| `pr-pytorch-150145` | upstream-code | [`sources/prs/pytorch/PR-150145.md`](../sources/prs/pytorch/PR-150145.md) | Dont exclude constant_pad_nd in prologue fusion |
| `pr-pytorch-150640` | upstream-code | [`sources/prs/pytorch/PR-150640.md`](../sources/prs/pytorch/PR-150640.md) | [CUDA][avgpool2d] Fix backward launch bounds again for `sm100`, `sm120` |
| `pr-pytorch-150676` | upstream-code | [`sources/prs/pytorch/PR-150676.md`](../sources/prs/pytorch/PR-150676.md) | [CUDA][avgpool2d] Fix backward launch bounds again for `sm100`, `sm120` |
| `pr-pytorch-150705` | upstream-code | [`sources/prs/pytorch/PR-150705.md`](../sources/prs/pytorch/PR-150705.md) | [CUDA] Only use vec128 if CUDA version is newer than 12.8 |
| `pr-pytorch-152774` | upstream-code | [`sources/prs/pytorch/PR-152774.md`](../sources/prs/pytorch/PR-152774.md) | [dynamo][super variable] Fix bug to use correct source |
| `pr-pytorch-152967` | upstream-code | [`sources/prs/pytorch/PR-152967.md`](../sources/prs/pytorch/PR-152967.md) | [ATen][CUDA] Optimize 128 bit vectorization |
| `pr-pytorch-153104` | upstream-code | [`sources/prs/pytorch/PR-153104.md`](../sources/prs/pytorch/PR-153104.md) | [FlexAttention] Remove Old Constraint on lastdim strides |
| `pr-pytorch-153641` | upstream-code | [`sources/prs/pytorch/PR-153641.md`](../sources/prs/pytorch/PR-153641.md) | [FlexAttention] explicilty create grad_q w/ strides |
| `pr-pytorch-156932` | upstream-code | [`sources/prs/pytorch/PR-156932.md`](../sources/prs/pytorch/PR-156932.md) | Fix macOS build with `USE_MPS=OFF` |
| `pr-pytorch-157241` | upstream-code | [`sources/prs/pytorch/PR-157241.md`](../sources/prs/pytorch/PR-157241.md) | [user triton] AOT inductor support for device-side TMA |
| `pr-pytorch-157422` | upstream-code | [`sources/prs/pytorch/PR-157422.md`](../sources/prs/pytorch/PR-157422.md) | [PowerPC] Fixed build issue for vsx vec256 complexfloat and scaled_mm_out_cpu  |
| `pr-pytorch-158237` | upstream-code | [`sources/prs/pytorch/PR-158237.md`](../sources/prs/pytorch/PR-158237.md) | [MPS] Switch Cholesky  decomp to column wise |
| `pr-pytorch-158301` | upstream-code | [`sources/prs/pytorch/PR-158301.md`](../sources/prs/pytorch/PR-158301.md) | Add warning about removed sm50 and sm60 arches |
| `pr-pytorch-158478` | upstream-code | [`sources/prs/pytorch/PR-158478.md`](../sources/prs/pytorch/PR-158478.md) | Add warning about removed sm50 and sm60 arches |
| `pr-pytorch-158646` | upstream-code | [`sources/prs/pytorch/PR-158646.md`](../sources/prs/pytorch/PR-158646.md) | [cherry-pick][inductor][triton] Update HAS_WARP_SPEC to check triton.Config params. Update Triton Hash to top of release/3.4.x stack |
| `pr-pytorch-161816` | upstream-code | [`sources/prs/pytorch/PR-161816.md`](../sources/prs/pytorch/PR-161816.md) | [Reland][Inductor] Prune configs that require more shared memory than the hardware limit |
| `pr-pytorch-163097` | upstream-code | [`sources/prs/pytorch/PR-163097.md`](../sources/prs/pytorch/PR-163097.md) | [Cherry Pick][Graph Partition] allow sharing default device context |
| `pr-pytorch-163380` | upstream-code | [`sources/prs/pytorch/PR-163380.md`](../sources/prs/pytorch/PR-163380.md) | [Graph Partition] improve custom op output alias |
| `pr-pytorch-163388` | upstream-code | [`sources/prs/pytorch/PR-163388.md`](../sources/prs/pytorch/PR-163388.md) | [Inductor][Intel GPU] Save `threads_per_warp` from tirton compiled kernel for launching kernel correctly in cpp wrapper. |
| `pr-pytorch-163395` | upstream-code | [`sources/prs/pytorch/PR-163395.md`](../sources/prs/pytorch/PR-163395.md) | [graph partition] Add way to register custom rule (#163310) |
| `pr-pytorch-163585` | upstream-code | [`sources/prs/pytorch/PR-163585.md`](../sources/prs/pytorch/PR-163585.md) | CUDA 13.0 Warning update for supported architectures |
| `pr-pytorch-163633` | upstream-code | [`sources/prs/pytorch/PR-163633.md`](../sources/prs/pytorch/PR-163633.md) | CUDA 13.0 Warning update for supported architectures |
| `pr-pytorch-163954` | upstream-code | [`sources/prs/pytorch/PR-163954.md`](../sources/prs/pytorch/PR-163954.md) | Move inductor jobs 3.9->3.10 |
| `pr-pytorch-164026` | upstream-code | [`sources/prs/pytorch/PR-164026.md`](../sources/prs/pytorch/PR-164026.md) | [cuDNN][SDPA] Disable dropout for cuDNN SDPA on 9.11 - 9.13 |
| `pr-pytorch-164364` | upstream-code | [`sources/prs/pytorch/PR-164364.md`](../sources/prs/pytorch/PR-164364.md) | [SDPA] [MPS] Fixes regression in 2.8.0 for scaled_dot_product_attention using mps |
| `pr-pytorch-164368` | upstream-code | [`sources/prs/pytorch/PR-164368.md`](../sources/prs/pytorch/PR-164368.md) | [Flex attention] Fix flex attention head broadcast |
| `pr-pytorch-166910` | upstream-code | [`sources/prs/pytorch/PR-166910.md`](../sources/prs/pytorch/PR-166910.md) | [inductor] don't try to reorder loops for template |
| `pr-pytorch-166913` | upstream-code | [`sources/prs/pytorch/PR-166913.md`](../sources/prs/pytorch/PR-166913.md) | [Dynamo] Don't guard data ptrs by default with mark_static_address |
| `pr-pytorch-166922` | upstream-code | [`sources/prs/pytorch/PR-166922.md`](../sources/prs/pytorch/PR-166922.md) | [Inductor] No longer throw error in bmm out_dtype lowering due to tem… |
| `pr-pytorch-166967` | upstream-code | [`sources/prs/pytorch/PR-166967.md`](../sources/prs/pytorch/PR-166967.md) | [Graph Partition] move custom rules to inductor config (#166458) |
| `pr-pytorch-166985` | upstream-code | [`sources/prs/pytorch/PR-166985.md`](../sources/prs/pytorch/PR-166985.md) | [Graph Partition] fix graph partition input signature for fallback kernels |
| `pr-pytorch-167327` | upstream-code | [`sources/prs/pytorch/PR-167327.md`](../sources/prs/pytorch/PR-167327.md) | [cuDNN][SDPA][Convolution] Expose cuDNN runtime version in CUDA hooks |
| `pr-pytorch-170112` | upstream-code | [`sources/prs/pytorch/PR-170112.md`](../sources/prs/pytorch/PR-170112.md) | [RELEASE 2.10] Release only changes |
| `pr-pytorch-170190` | upstream-code | [`sources/prs/pytorch/PR-170190.md`](../sources/prs/pytorch/PR-170190.md) | [ROCm] Enable shared memory based pruning for Triton configs |
| `pr-pytorch-170486` | upstream-code | [`sources/prs/pytorch/PR-170486.md`](../sources/prs/pytorch/PR-170486.md) | [flex_attention] adds support for low precision K/V inputs in compiled mode with GPU |
| `pr-pytorch-170555` | upstream-code | [`sources/prs/pytorch/PR-170555.md`](../sources/prs/pytorch/PR-170555.md) | [cherry-pick] Fix vllm issue for flex (#170499) |
| `pr-pytorch-170884` | upstream-code | [`sources/prs/pytorch/PR-170884.md`](../sources/prs/pytorch/PR-170884.md) | [inductor] Fix cudagraph skip for index_put_ with boolean indices, gr… |
| `pr-pytorch-171129` | upstream-code | [`sources/prs/pytorch/PR-171129.md`](../sources/prs/pytorch/PR-171129.md) | [Inductor] Fix constants handling for Triton constexpr (triton#8248) |
| `pr-pytorch-171140` | upstream-code | [`sources/prs/pytorch/PR-171140.md`](../sources/prs/pytorch/PR-171140.md) | [ROCm] Make grouped GEMM CK opt‑in via env and default to fallback path |
| `pr-pytorch-171247` | upstream-code | [`sources/prs/pytorch/PR-171247.md`](../sources/prs/pytorch/PR-171247.md) | [xpu][fix][inductor] fallback bfloat16 atomics to eager |
| `pr-pytorch-171895` | upstream-code | [`sources/prs/pytorch/PR-171895.md`](../sources/prs/pytorch/PR-171895.md) | [cherry-pick][cuDNN][SDPA] cuDNN SDPA off-by-default for cuDNN versions < 12.9 (#171627) |
| `pr-pytorch-172141` | upstream-code | [`sources/prs/pytorch/PR-172141.md`](../sources/prs/pytorch/PR-172141.md) | Skip modded_nanogpt model in TorchInductor benchmark |
| `pr-pytorch-172577` | upstream-code | [`sources/prs/pytorch/PR-172577.md`](../sources/prs/pytorch/PR-172577.md) | [Graph Partition] Improve support for mutation ops |
| `pr-pytorch-175091` | upstream-code | [`sources/prs/pytorch/PR-175091.md`](../sources/prs/pytorch/PR-175091.md) | [RELEASE 2.11] Release only changes |
| `pr-pytorch-175096` | upstream-code | [`sources/prs/pytorch/PR-175096.md`](../sources/prs/pytorch/PR-175096.md) | Update inductor expected accuracy files |
| `pr-pytorch-175299` | upstream-code | [`sources/prs/pytorch/PR-175299.md`](../sources/prs/pytorch/PR-175299.md) | [benchmark] Skip pytorch_CycleGAN_and_pix2pix from inductor benchmarks |
| `pr-pytorch-176410` | upstream-code | [`sources/prs/pytorch/PR-176410.md`](../sources/prs/pytorch/PR-176410.md) | [Inductor] Reject non-contiguous subnode fusion in mix-order reduction. |
| `pr-pytorch-176495` | upstream-code | [`sources/prs/pytorch/PR-176495.md`](../sources/prs/pytorch/PR-176495.md) | [inductor] avoid multi-stage for mix-order-red by default (#176228) |
| `pr-pytorch-177142` | upstream-code | [`sources/prs/pytorch/PR-177142.md`](../sources/prs/pytorch/PR-177142.md) | fix acc failure for vit_base_patch14_dinov2.lvd142m |
| `pr-pytorch-177144` | upstream-code | [`sources/prs/pytorch/PR-177144.md`](../sources/prs/pytorch/PR-177144.md) | [Inductor] Don't unfuse addmm for bf16/fp16 to avoid precision loss |
| `pr-pytorch-178009` | upstream-code | [`sources/prs/pytorch/PR-178009.md`](../sources/prs/pytorch/PR-178009.md) | [MPS] fix compiling of SDPA producing nan results |
| `pr-pytorch-180470` | upstream-code | [`sources/prs/pytorch/PR-180470.md`](../sources/prs/pytorch/PR-180470.md) | [release 2.12] Apply Release only changes to 2.12 branch |
| `pr-pytorch-180691` | upstream-code | [`sources/prs/pytorch/PR-180691.md`](../sources/prs/pytorch/PR-180691.md) | [ROCm] Enable ROCm swizzle check and update scaled_mm swizzle tests |
| `pr-pytorch-180692` | upstream-code | [`sources/prs/pytorch/PR-180692.md`](../sources/prs/pytorch/PR-180692.md) | [ROCm] Resolve timeouts caused due to hipblasLT module creation during graph capture |
| `pr-pytorch-180815` | upstream-code | [`sources/prs/pytorch/PR-180815.md`](../sources/prs/pytorch/PR-180815.md) | [xpu][fix] Include lazy_triton_compile.h in XPU cpp_wrapper header |
| `pr-pytorch-181287` | upstream-code | [`sources/prs/pytorch/PR-181287.md`](../sources/prs/pytorch/PR-181287.md) | [inductor] makes cuda 13.0 cross compliation works (#179229) |

<a id="sgl-projectsglang"></a>
## sgl-project/sglang

777 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-sglang-10058` | upstream-code | [`sources/prs/sglang/PR-10058.md`](../sources/prs/sglang/PR-10058.md) | Disable kernel cutlass_mla_decode on SM103 |
| `pr-sglang-10062` | upstream-code | [`sources/prs/sglang/PR-10062.md`](../sources/prs/sglang/PR-10062.md) | Piecewise CUDA Graph Support & Torch Compile Backend |
| `pr-sglang-10078` | upstream-code | [`sources/prs/sglang/PR-10078.md`](../sources/prs/sglang/PR-10078.md) | feat: Add FP4 (E2M1) KV Cache Support with Quantization Utilities for MLA |
| `pr-sglang-10101` | upstream-code | [`sources/prs/sglang/PR-10101.md`](../sources/prs/sglang/PR-10101.md) | Optimize nvfp4 block scaled gemm kernel when M is small. |
| `pr-sglang-10130` | upstream-code | [`sources/prs/sglang/PR-10130.md`](../sources/prs/sglang/PR-10130.md) | [Feature] Add MLAProcess for DeepSeek MLA on NPU |
| `pr-sglang-10154` | upstream-code | [`sources/prs/sglang/PR-10154.md`](../sources/prs/sglang/PR-10154.md) | Enable native ModelOpt quantization support (3/3) |
| `pr-sglang-10180` | upstream-code | [`sources/prs/sglang/PR-10180.md`](../sources/prs/sglang/PR-10180.md) | Fix chunked prefix cache for nvfp4 |
| `pr-sglang-10183` | upstream-code | [`sources/prs/sglang/PR-10183.md`](../sources/prs/sglang/PR-10183.md) | Add --speculative-moe-runner-backend server arg |
| `pr-sglang-10263` | upstream-code | [`sources/prs/sglang/PR-10263.md`](../sources/prs/sglang/PR-10263.md) | Support dispatch low latency |
| `pr-sglang-10275` | upstream-code | [`sources/prs/sglang/PR-10275.md`](../sources/prs/sglang/PR-10275.md) | Add support for bf16 x bf16 cutlass fused MoE |
| `pr-sglang-10281` | upstream-code | [`sources/prs/sglang/PR-10281.md`](../sources/prs/sglang/PR-10281.md) | Enables TRT-LLM backend to be used for target_verify |
| `pr-sglang-10312` | upstream-code | [`sources/prs/sglang/PR-10312.md`](../sources/prs/sglang/PR-10312.md) | Reland [1/2] Optimizations and refactors about quant kernel |
| `pr-sglang-10403` | upstream-code | [`sources/prs/sglang/PR-10403.md`](../sources/prs/sglang/PR-10403.md) | support qwen3_next blackwell |
| `pr-sglang-10422` | upstream-code | [`sources/prs/sglang/PR-10422.md`](../sources/prs/sglang/PR-10422.md) | Support single batch overlap |
| `pr-sglang-10426` | upstream-code | [`sources/prs/sglang/PR-10426.md`](../sources/prs/sglang/PR-10426.md) | Fix correction bias undefined behavior for nvfp4 models |
| `pr-sglang-10491` | upstream-code | [`sources/prs/sglang/PR-10491.md`](../sources/prs/sglang/PR-10491.md) | Update CUTLASS. Refine KernelSchedule for fp8 (grouped) gemm. |
| `pr-sglang-10498` | upstream-code | [`sources/prs/sglang/PR-10498.md`](../sources/prs/sglang/PR-10498.md) | Cache the result of `is_blackwell` platform check |
| `pr-sglang-10526` | upstream-code | [`sources/prs/sglang/PR-10526.md`](../sources/prs/sglang/PR-10526.md) | Enable trtllm mla prefix extend |
| `pr-sglang-10543` | upstream-code | [`sources/prs/sglang/PR-10543.md`](../sources/prs/sglang/PR-10543.md) | [sgl-kernel] Optimize concat_mla_k kernel |
| `pr-sglang-10579` | upstream-code | [`sources/prs/sglang/PR-10579.md`](../sources/prs/sglang/PR-10579.md) | Fix bias handling in TritonMoeQuantInfo within quantization/mxfp4.py |
| `pr-sglang-10678` | upstream-code | [`sources/prs/sglang/PR-10678.md`](../sources/prs/sglang/PR-10678.md) | [2/2] Support deterministic inference for temperature > 0 |
| `pr-sglang-10688` | upstream-code | [`sources/prs/sglang/PR-10688.md`](../sources/prs/sglang/PR-10688.md) | [Auto Sync] Update modelopt_quant.py (20250920) |
| `pr-sglang-10714` | upstream-code | [`sources/prs/sglang/PR-10714.md`](../sources/prs/sglang/PR-10714.md) | Optimize cutlass int8 gemm kernel for large M on SM89 Ada GPU |
| `pr-sglang-10758` | upstream-code | [`sources/prs/sglang/PR-10758.md`](../sources/prs/sglang/PR-10758.md) | Fix MTP MoE weight loading with NVFP4 target model. |
| `pr-sglang-10779` | upstream-code | [`sources/prs/sglang/PR-10779.md`](../sources/prs/sglang/PR-10779.md) | Fuse quantize and rope in trtllm_mla MTP |
| `pr-sglang-10816` | upstream-code | [`sources/prs/sglang/PR-10816.md`](../sources/prs/sglang/PR-10816.md) | Remove hybrid_linear_attn attention backend and refactor attention registry |
| `pr-sglang-10858` | upstream-code | [`sources/prs/sglang/PR-10858.md`](../sources/prs/sglang/PR-10858.md) | [Intel GPU] fix import error to run DeepSeek-V2-Lite model with BF16 on XPU |
| `pr-sglang-10937` | upstream-code | [`sources/prs/sglang/PR-10937.md`](../sources/prs/sglang/PR-10937.md) | [2/2] Support MHA prefill with FlashAttention 4. |
| `pr-sglang-11081` | upstream-code | [`sources/prs/sglang/PR-11081.md`](../sources/prs/sglang/PR-11081.md) | Fix DSR1 accuracy for flashinfer_trtllm MoE with FP8 quantization |
| `pr-sglang-11138` | upstream-code | [`sources/prs/sglang/PR-11138.md`](../sources/prs/sglang/PR-11138.md) | Allow use of TRTLLM_MHA backend for hybrid attention on Blackwell |
| `pr-sglang-11211` | upstream-code | [`sources/prs/sglang/PR-11211.md`](../sources/prs/sglang/PR-11211.md) | [8/N] MoE Refactor: deprecate `EPMoE` |
| `pr-sglang-11228` | upstream-code | [`sources/prs/sglang/PR-11228.md`](../sources/prs/sglang/PR-11228.md) | Rename runner labels |
| `pr-sglang-11287` | upstream-code | [`sources/prs/sglang/PR-11287.md`](../sources/prs/sglang/PR-11287.md) | [NVIDIA] Add new SMs support for Spark & Thor |
| `pr-sglang-11349` | upstream-code | [`sources/prs/sglang/PR-11349.md`](../sources/prs/sglang/PR-11349.md) | [AMD] Clean up vllm dependencies in moe_runner/triton.py |
| `pr-sglang-11432` | upstream-code | [`sources/prs/sglang/PR-11432.md`](../sources/prs/sglang/PR-11432.md) | [sgl-kernel][1/N]Support Expert Specialization Grouped GEMM |
| `pr-sglang-11537` | upstream-code | [`sources/prs/sglang/PR-11537.md`](../sources/prs/sglang/PR-11537.md) | Tiny cleanup fp4 gemm calls |
| `pr-sglang-11606` | upstream-code | [`sources/prs/sglang/PR-11606.md`](../sources/prs/sglang/PR-11606.md) | [NVIDIA] FA3/FA4 Fix  |
| `pr-sglang-11611` | upstream-code | [`sources/prs/sglang/PR-11611.md`](../sources/prs/sglang/PR-11611.md) | Support shared experts overlap in cutlass moe |
| `pr-sglang-11655` | upstream-code | [`sources/prs/sglang/PR-11655.md`](../sources/prs/sglang/PR-11655.md) | [DeepseekV32] Enable flashmla_prefill kernel with fp8 kvcache |
| `pr-sglang-11664` | upstream-code | [`sources/prs/sglang/PR-11664.md`](../sources/prs/sglang/PR-11664.md) | Use trtllm_mla decode kernel for draft extend in speculative decoding |
| `pr-sglang-11708` | upstream-code | [`sources/prs/sglang/PR-11708.md`](../sources/prs/sglang/PR-11708.md) | Support running FP4 Deepseek on SM120. |
| `pr-sglang-11712` | upstream-code | [`sources/prs/sglang/PR-11712.md`](../sources/prs/sglang/PR-11712.md) | enable ut test for xpu devices |
| `pr-sglang-11717` | upstream-code | [`sources/prs/sglang/PR-11717.md`](../sources/prs/sglang/PR-11717.md) | [sgl-kernel] support flashmla libtorch |
| `pr-sglang-11737` | upstream-code | [`sources/prs/sglang/PR-11737.md`](../sources/prs/sglang/PR-11737.md) | support cutlass fp4 kernel in sm120 |
| `pr-sglang-11781` | upstream-code | [`sources/prs/sglang/PR-11781.md`](../sources/prs/sglang/PR-11781.md) | Fix install instructions and pyproject.tomls |
| `pr-sglang-11805` | upstream-code | [`sources/prs/sglang/PR-11805.md`](../sources/prs/sglang/PR-11805.md) | Change bf16 to fp8 for some gemms in attention for DeepSeek ckpt v2 |
| `pr-sglang-11812` | upstream-code | [`sources/prs/sglang/PR-11812.md`](../sources/prs/sglang/PR-11812.md) | Support piecewise cuda graph for MLA |
| `pr-sglang-11813` | upstream-code | [`sources/prs/sglang/PR-11813.md`](../sources/prs/sglang/PR-11813.md) | Use cutlass fp4 gemm by default |
| `pr-sglang-11816` | upstream-code | [`sources/prs/sglang/PR-11816.md`](../sources/prs/sglang/PR-11816.md) | use flashinfer_trtllm moe runner backend to gain around 10% perf on b200 fp8 dpsk |
| `pr-sglang-11821` | upstream-code | [`sources/prs/sglang/PR-11821.md`](../sources/prs/sglang/PR-11821.md) | Support overlap-spec-v2 with trtllm_mla attention backend |
| `pr-sglang-11852` | upstream-code | [`sources/prs/sglang/PR-11852.md`](../sources/prs/sglang/PR-11852.md) | [PP] Refactor PP to async mode |
| `pr-sglang-11866` | upstream-code | [`sources/prs/sglang/PR-11866.md`](../sources/prs/sglang/PR-11866.md) | Support nvidia/NVIDIA-Nemotron-Nano-9B-v2-FP8/NVFP4 |
| `pr-sglang-11892` | upstream-code | [`sources/prs/sglang/PR-11892.md`](../sources/prs/sglang/PR-11892.md) | DeepSeek-V3.2: Add Adaptive MHA Attention Pathway for Short-Sequence Prefill |
| `pr-sglang-11928` | upstream-code | [`sources/prs/sglang/PR-11928.md`](../sources/prs/sglang/PR-11928.md) | Use Flashinfer TRT-LLM as Llama 4 compatible MoE backend |
| `pr-sglang-11985` | upstream-code | [`sources/prs/sglang/PR-11985.md`](../sources/prs/sglang/PR-11985.md) | Fix incorrect KV indices creation when page_size=32 in TRTLLM MLA backend |
| `pr-sglang-12018` | upstream-code | [`sources/prs/sglang/PR-12018.md`](../sources/prs/sglang/PR-12018.md) | Feature/nano v2 offline modelopt fp8 and nvfp4 |
| `pr-sglang-12065` | upstream-code | [`sources/prs/sglang/PR-12065.md`](../sources/prs/sglang/PR-12065.md) | (1/n)support context parallel with deepseekv3.2-DSA |
| `pr-sglang-12067` | upstream-code | [`sources/prs/sglang/PR-12067.md`](../sources/prs/sglang/PR-12067.md) | [b200] fix piecewise cuda graph launch bug |
| `pr-sglang-12078` | upstream-code | [`sources/prs/sglang/PR-12078.md`](../sources/prs/sglang/PR-12078.md) | [Ascend] qwen optimization |
| `pr-sglang-12080` | upstream-code | [`sources/prs/sglang/PR-12080.md`](../sources/prs/sglang/PR-12080.md) | [sgl-kernel][4/N]Support Expert Specialization Grouped GEMM |
| `pr-sglang-12093` | upstream-code | [`sources/prs/sglang/PR-12093.md`](../sources/prs/sglang/PR-12093.md) | perf: trtllm_mla attention backend spec decoding speedup w/ cuda graph |
| `pr-sglang-12135` | upstream-code | [`sources/prs/sglang/PR-12135.md`](../sources/prs/sglang/PR-12135.md) | Import flash_mla from sgl-kernel |
| `pr-sglang-12214` | upstream-code | [`sources/prs/sglang/PR-12214.md`](../sources/prs/sglang/PR-12214.md) | [Ascend][feature] support L1+ L2 radixcache on ascend |
| `pr-sglang-12215` | upstream-code | [`sources/prs/sglang/PR-12215.md`](../sources/prs/sglang/PR-12215.md) | [DeepseekV32]: use `_concat_mla_absorb_q_general` to replace `torch.cat` |
| `pr-sglang-12259` | upstream-code | [`sources/prs/sglang/PR-12259.md`](../sources/prs/sglang/PR-12259.md) | [hotfix] missing `w13_weight_fp8` and `w2_weight_fp8` in UE8M0 requantization |
| `pr-sglang-12294` | upstream-code | [`sources/prs/sglang/PR-12294.md`](../sources/prs/sglang/PR-12294.md) | [Deepseek V3.2] Enable flashmla_auto with MTP |
| `pr-sglang-12295` | upstream-code | [`sources/prs/sglang/PR-12295.md`](../sources/prs/sglang/PR-12295.md) | fix seqlen bug for trtllm_mla's draft_extend |
| `pr-sglang-12306` | upstream-code | [`sources/prs/sglang/PR-12306.md`](../sources/prs/sglang/PR-12306.md) | feat: support flashinfer kernel autotune |
| `pr-sglang-12325` | upstream-code | [`sources/prs/sglang/PR-12325.md`](../sources/prs/sglang/PR-12325.md) | Fix Flashinfer Backend for SM120 Usage |
| `pr-sglang-12353` | upstream-code | [`sources/prs/sglang/PR-12353.md`](../sources/prs/sglang/PR-12353.md) | [NVIDIA] Fix cutedsl backend of MoE |
| `pr-sglang-12361` | upstream-code | [`sources/prs/sglang/PR-12361.md`](../sources/prs/sglang/PR-12361.md) | [Fix] Fix trtllm-mla backend when chunked prefix cache is disabled |
| `pr-sglang-12376` | upstream-code | [`sources/prs/sglang/PR-12376.md`](../sources/prs/sglang/PR-12376.md) | Replace [silu_and_mul_]scaled_fp4_group_quant by Flashinfer equivalent |
| `pr-sglang-12406` | upstream-code | [`sources/prs/sglang/PR-12406.md`](../sources/prs/sglang/PR-12406.md) | Add mm_fp4 trtllm backend |
| `pr-sglang-12435` | upstream-code | [`sources/prs/sglang/PR-12435.md`](../sources/prs/sglang/PR-12435.md) | perf: trtllm mla performance minor improvements |
| `pr-sglang-12482` | upstream-code | [`sources/prs/sglang/PR-12482.md`](../sources/prs/sglang/PR-12482.md) | Use sgl fp4 quant kernel by default |
| `pr-sglang-12491` | upstream-code | [`sources/prs/sglang/PR-12491.md`](../sources/prs/sglang/PR-12491.md) | [Ascend] Support enable-mixed-chunk in non-MLA scenarios |
| `pr-sglang-12497` | upstream-code | [`sources/prs/sglang/PR-12497.md`](../sources/prs/sglang/PR-12497.md) | [Fix] Remove assertion for padding for NVFP4 weight scales to fix GLM 4.5 NVFP4 |
| `pr-sglang-12543` | upstream-code | [`sources/prs/sglang/PR-12543.md`](../sources/prs/sglang/PR-12543.md) | Enable Flashinfer TRTLLM-GEN-MoE FP8 blockwise kernel for Qwen3-Next on Blackwell |
| `pr-sglang-12581` | upstream-code | [`sources/prs/sglang/PR-12581.md`](../sources/prs/sglang/PR-12581.md) | [NVIDIA] Fix CUDA arch requirement in nvfp4 cast |
| `pr-sglang-12640` | upstream-code | [`sources/prs/sglang/PR-12640.md`](../sources/prs/sglang/PR-12640.md) | [NVIDIA] Fix wrong symmetric sizes for fp4 cases |
| `pr-sglang-12666` | upstream-code | [`sources/prs/sglang/PR-12666.md`](../sources/prs/sglang/PR-12666.md) | [sgl-kernel][5/N]Support Expert Specialization Grouped GEMM |
| `pr-sglang-12687` | upstream-code | [`sources/prs/sglang/PR-12687.md`](../sources/prs/sglang/PR-12687.md) | fix trtllm_mla attention backend when disabling cuda graph. |
| `pr-sglang-12758` | upstream-code | [`sources/prs/sglang/PR-12758.md`](../sources/prs/sglang/PR-12758.md) | [Bugfix] Fix illegal memory access |
| `pr-sglang-12759` | upstream-code | [`sources/prs/sglang/PR-12759.md`](../sources/prs/sglang/PR-12759.md) | [Ascend] support Kimi-K2-Thinking |
| `pr-sglang-12782` | upstream-code | [`sources/prs/sglang/PR-12782.md`](../sources/prs/sglang/PR-12782.md) | ignore the deepgemm check when the model weight with nvfp4 and moe ba… |
| `pr-sglang-12787` | upstream-code | [`sources/prs/sglang/PR-12787.md`](../sources/prs/sglang/PR-12787.md) | [Nvidia] Add trtllm mnnvl allreduce with unified flashinfer allreduce fusion api |
| `pr-sglang-12788` | upstream-code | [`sources/prs/sglang/PR-12788.md`](../sources/prs/sglang/PR-12788.md) | [DeepSeek-V3.2][NSA] Enable MHA Pathway for Short Sequence Prefill on B200 (SM100) |
| `pr-sglang-12816` | upstream-code | [`sources/prs/sglang/PR-12816.md`](../sources/prs/sglang/PR-12816.md) | [Deepseek V3.2] Only skip Indexer logits computation when is_extend_without_speculative |
| `pr-sglang-12888` | upstream-code | [`sources/prs/sglang/PR-12888.md`](../sources/prs/sglang/PR-12888.md) | Apply moe_reduce_sum kernel for fused_marlin_moe |
| `pr-sglang-13022` | upstream-code | [`sources/prs/sglang/PR-13022.md`](../sources/prs/sglang/PR-13022.md) | [Deepseek V3.2] Use torch.compile to speed up torch.cat in nsa |
| `pr-sglang-13049` | upstream-code | [`sources/prs/sglang/PR-13049.md`](../sources/prs/sglang/PR-13049.md) | Support moe topk sigmoid kernel |
| `pr-sglang-13087` | upstream-code | [`sources/prs/sglang/PR-13087.md`](../sources/prs/sglang/PR-13087.md) | [sgl-kernel] support custom fp8 flashmla kernel |
| `pr-sglang-13094` | upstream-code | [`sources/prs/sglang/PR-13094.md`](../sources/prs/sglang/PR-13094.md) | [Piecewise CUDA Graph] Support ModelOpt FP8 |
| `pr-sglang-13115` | upstream-code | [`sources/prs/sglang/PR-13115.md`](../sources/prs/sglang/PR-13115.md) | support mtp with deepseek r1 nvfp4 model |
| `pr-sglang-13147` | upstream-code | [`sources/prs/sglang/PR-13147.md`](../sources/prs/sglang/PR-13147.md) | Aiter fp8 kv cache |
| `pr-sglang-13151` | upstream-code | [`sources/prs/sglang/PR-13151.md`](../sources/prs/sglang/PR-13151.md) | Support internvl on Blackwell (which doesn't support fa3): add `SingletonCache` support to Vision{Sdpa|Triton|Ascend}Attention |
| `pr-sglang-13158` | upstream-code | [`sources/prs/sglang/PR-13158.md`](../sources/prs/sglang/PR-13158.md) | [NPU]Optimization of `forward_npu` for `UnquantizedFusedMoEMethod` |
| `pr-sglang-13162` | upstream-code | [`sources/prs/sglang/PR-13162.md`](../sources/prs/sglang/PR-13162.md) | Fix nan in global scaling factor for large scale nvfp4 EP |
| `pr-sglang-13263` | upstream-code | [`sources/prs/sglang/PR-13263.md`](../sources/prs/sglang/PR-13263.md) | diffusion: enable fa4 for blackwell |
| `pr-sglang-13264` | upstream-code | [`sources/prs/sglang/PR-13264.md`](../sources/prs/sglang/PR-13264.md) | [NVIDIA] Fix broken fp8 MoE of deepseek v3 |
| `pr-sglang-13274` | upstream-code | [`sources/prs/sglang/PR-13274.md`](../sources/prs/sglang/PR-13274.md) | [NVIDIA] Fix use case of SGLANG_ENABLE_FLASHINFER_GEMM |
| `pr-sglang-13327` | upstream-code | [`sources/prs/sglang/PR-13327.md`](../sources/prs/sglang/PR-13327.md) | [11/N] MoE Refactor: Simplifying SBO Implementation with Dispatcher Hooks |
| `pr-sglang-13341` | upstream-code | [`sources/prs/sglang/PR-13341.md`](../sources/prs/sglang/PR-13341.md) | Clean up deprecated tile_tokens_dim for next flashinfer |
| `pr-sglang-13528` | upstream-code | [`sources/prs/sglang/PR-13528.md`](../sources/prs/sglang/PR-13528.md) | [NVIDIA] Add fp8 gemm benchmark on blackwell |
| `pr-sglang-13539` | upstream-code | [`sources/prs/sglang/PR-13539.md`](../sources/prs/sglang/PR-13539.md) | add the fa4 mm backend and varlen func |
| `pr-sglang-13544` | upstream-code | [`sources/prs/sglang/PR-13544.md`](../sources/prs/sglang/PR-13544.md) | [DeepSeekV3.2] Centralize NSA dispatch logic in NativeSparseAttnBackend |
| `pr-sglang-13561` | upstream-code | [`sources/prs/sglang/PR-13561.md`](../sources/prs/sglang/PR-13561.md) | [XPU] Integrate MoE and minor improvements in XPU attention backend |
| `pr-sglang-13573` | upstream-code | [`sources/prs/sglang/PR-13573.md`](../sources/prs/sglang/PR-13573.md) | [BugFix] fix prefixcache performance and accuracy on ascend |
| `pr-sglang-13601` | upstream-code | [`sources/prs/sglang/PR-13601.md`](../sources/prs/sglang/PR-13601.md) | [1/2] Refactor DeepGeem requant for FP8 Linear on Blackwell  |
| `pr-sglang-13607` | upstream-code | [`sources/prs/sglang/PR-13607.md`](../sources/prs/sglang/PR-13607.md) | tiny remove deprecated endpoint call |
| `pr-sglang-13617` | upstream-code | [`sources/prs/sglang/PR-13617.md`](../sources/prs/sglang/PR-13617.md) | [ROCM] Optimized deepseek-r1 fp8 model with + triton_gemm_a8w8 + batch_gemm_a8w8 + fused set_mla_kv_buffer kernel |
| `pr-sglang-13646` | upstream-code | [`sources/prs/sglang/PR-13646.md`](../sources/prs/sglang/PR-13646.md) | [DeepSeekV3.2] Enable pure TP & Partial DP Attention |
| `pr-sglang-13715` | upstream-code | [`sources/prs/sglang/PR-13715.md`](../sources/prs/sglang/PR-13715.md) | Fix EPLB + FP4 Quantization Compatibility Issue |
| `pr-sglang-13731` | upstream-code | [`sources/prs/sglang/PR-13731.md`](../sources/prs/sglang/PR-13731.md) | [sgl-kernel][Feat][B200][1/N]Support MXFP8 Grouped GEMM in Blackwell |
| `pr-sglang-13738` | upstream-code | [`sources/prs/sglang/PR-13738.md`](../sources/prs/sglang/PR-13738.md) | fix trtllm mla spec |
| `pr-sglang-13747` | upstream-code | [`sources/prs/sglang/PR-13747.md`](../sources/prs/sglang/PR-13747.md) | [AMD] Support --enable-aiter-allreduce-fusion on AMD GPUs |
| `pr-sglang-13756` | upstream-code | [`sources/prs/sglang/PR-13756.md`](../sources/prs/sglang/PR-13756.md) | [Tiny] Renaming environ for NVFP4 dispatch |
| `pr-sglang-13761` | upstream-code | [`sources/prs/sglang/PR-13761.md`](../sources/prs/sglang/PR-13761.md) | [Feat][NVFP4] Enable NVFP4 MoE for Qwen series models (eg. Qwen3-Next) #13761 |
| `pr-sglang-13794` | upstream-code | [`sources/prs/sglang/PR-13794.md`](../sources/prs/sglang/PR-13794.md) | Support fp4 fp8 non gated moe |
| `pr-sglang-13797` | upstream-code | [`sources/prs/sglang/PR-13797.md`](../sources/prs/sglang/PR-13797.md) | [1/N] Optimize All Reduce - Benchmark different AR operations |
| `pr-sglang-13798` | upstream-code | [`sources/prs/sglang/PR-13798.md`](../sources/prs/sglang/PR-13798.md) | [NVIDIA] Enable TRTLLM BF16 MoE on Blackwell GPUs |
| `pr-sglang-13864` | upstream-code | [`sources/prs/sglang/PR-13864.md`](../sources/prs/sglang/PR-13864.md) | [BugFix] fix outplace_fused_experts missing is_gated |
| `pr-sglang-13873` | upstream-code | [`sources/prs/sglang/PR-13873.md`](../sources/prs/sglang/PR-13873.md) | Feat: GLM-4.6 supports shared experts fusion |
| `pr-sglang-13907` | upstream-code | [`sources/prs/sglang/PR-13907.md`](../sources/prs/sglang/PR-13907.md) | [sgl-kernel] fix b200 kernel ci |
| `pr-sglang-13910` | upstream-code | [`sources/prs/sglang/PR-13910.md`](../sources/prs/sglang/PR-13910.md) | Fix update weight error for blackwell DeepGEMM |
| `pr-sglang-13959` | upstream-code | [`sources/prs/sglang/PR-13959.md`](../sources/prs/sglang/PR-13959.md) | [DeepSeek v3.2] opt Context Parallelism: support fused moe, multi batch and fp8 kvcache |
| `pr-sglang-13960` | upstream-code | [`sources/prs/sglang/PR-13960.md`](../sources/prs/sglang/PR-13960.md) | [2/2] Refactor DeepGeem requant for FP8 FusedMoE on Blackwell |
| `pr-sglang-13969` | upstream-code | [`sources/prs/sglang/PR-13969.md`](../sources/prs/sglang/PR-13969.md) | [kernel][moe] add moe topk fast |
| `pr-sglang-13976` | upstream-code | [`sources/prs/sglang/PR-13976.md`](../sources/prs/sglang/PR-13976.md) | Use trtllm mha decode kernel for target_verify in speculative decoding |
| `pr-sglang-14028` | upstream-code | [`sources/prs/sglang/PR-14028.md`](../sources/prs/sglang/PR-14028.md) | Fix flashinfer cutlass MoE output shape for non-FP4-packed inputs |
| `pr-sglang-14093` | upstream-code | [`sources/prs/sglang/PR-14093.md`](../sources/prs/sglang/PR-14093.md) | Add fused FP8 KV cache write kernel for TRTLLM MHA backend |
| `pr-sglang-14105` | upstream-code | [`sources/prs/sglang/PR-14105.md`](../sources/prs/sglang/PR-14105.md) | [LoRA][III] Add LoRA support for MoE layers and enable TP |
| `pr-sglang-14122` | upstream-code | [`sources/prs/sglang/PR-14122.md`](../sources/prs/sglang/PR-14122.md) | Add new moe wna16 marlin gemm |
| `pr-sglang-14125` | upstream-code | [`sources/prs/sglang/PR-14125.md`](../sources/prs/sglang/PR-14125.md) | Apply new moe wna16 marlin gemm |
| `pr-sglang-14133` | upstream-code | [`sources/prs/sglang/PR-14133.md`](../sources/prs/sglang/PR-14133.md) | Opt moe align block size kernel |
| `pr-sglang-14134` | upstream-code | [`sources/prs/sglang/PR-14134.md`](../sources/prs/sglang/PR-14134.md) | Apply new moe align block size kernel |
| `pr-sglang-14162` | upstream-code | [`sources/prs/sglang/PR-14162.md`](../sources/prs/sglang/PR-14162.md) | DeepSeek-R1-0528-w4a8: DeepEP Low Latency Dispatch Adopts FP8 Communication |
| `pr-sglang-14164` | upstream-code | [`sources/prs/sglang/PR-14164.md`](../sources/prs/sglang/PR-14164.md) | EP Support for Piecewise Cuda Graph |
| `pr-sglang-14173` | upstream-code | [`sources/prs/sglang/PR-14173.md`](../sources/prs/sglang/PR-14173.md) | fix: Increase FlashInfer workspace size for Qwen3VL models |
| `pr-sglang-14213` | upstream-code | [`sources/prs/sglang/PR-14213.md`](../sources/prs/sglang/PR-14213.md) | Add Mistral Large 3 support. |
| `pr-sglang-14252` | upstream-code | [`sources/prs/sglang/PR-14252.md`](../sources/prs/sglang/PR-14252.md) | [Auto Sync] Rename is_hybrid to is_hybrid_swa |
| `pr-sglang-14311` | upstream-code | [`sources/prs/sglang/PR-14311.md`](../sources/prs/sglang/PR-14311.md) | [Fix] add block size logic for sm120 smem size |
| `pr-sglang-14350` | upstream-code | [`sources/prs/sglang/PR-14350.md`](../sources/prs/sglang/PR-14350.md) | [FIX] trtllm-moe-fp4-renorm for Qwen series models |
| `pr-sglang-14357` | upstream-code | [`sources/prs/sglang/PR-14357.md`](../sources/prs/sglang/PR-14357.md) | [Perf] Enable Flashinfer autotune by default |
| `pr-sglang-14379` | upstream-code | [`sources/prs/sglang/PR-14379.md`](../sources/prs/sglang/PR-14379.md) | Add FP8 Blockwise GEMM Backend Flag `--fp8-gemm-backend` |
| `pr-sglang-14385` | upstream-code | [`sources/prs/sglang/PR-14385.md`](../sources/prs/sglang/PR-14385.md) | [CPU] Implement MXFP4 Gemm kernels for intel AMX to support GPT OSS series. |
| `pr-sglang-14395` | upstream-code | [`sources/prs/sglang/PR-14395.md`](../sources/prs/sglang/PR-14395.md) | Support FP8 MLA prefill and 128k context. |
| `pr-sglang-14423` | upstream-code | [`sources/prs/sglang/PR-14423.md`](../sources/prs/sglang/PR-14423.md) | [NPU] perf update with kvcache nz & w4a8 quant |
| `pr-sglang-14449` | upstream-code | [`sources/prs/sglang/PR-14449.md`](../sources/prs/sglang/PR-14449.md) | Update FP4 GEMM Benchmark |
| `pr-sglang-14466` | upstream-code | [`sources/prs/sglang/PR-14466.md`](../sources/prs/sglang/PR-14466.md) | Add Mistral Large 3 Eagle Support |
| `pr-sglang-14485` | upstream-code | [`sources/prs/sglang/PR-14485.md`](../sources/prs/sglang/PR-14485.md) | Mistral Large 3 NVFP4 support |
| `pr-sglang-14538` | upstream-code | [`sources/prs/sglang/PR-14538.md`](../sources/prs/sglang/PR-14538.md) | [Misc]Register and refactor some environs for dpsk-fp4 and DeepEp |
| `pr-sglang-14640` | upstream-code | [`sources/prs/sglang/PR-14640.md`](../sources/prs/sglang/PR-14640.md) | [sgl-kernel][Feat][B200][2/N] Support MXFP8 Grouped GEMM in Blackwell |
| `pr-sglang-14668` | upstream-code | [`sources/prs/sglang/PR-14668.md`](../sources/prs/sglang/PR-14668.md) | [NVIDIA] Add flashinfer all-to-all MOE dispatcher |
| `pr-sglang-14717` | upstream-code | [`sources/prs/sglang/PR-14717.md`](../sources/prs/sglang/PR-14717.md) | [diffusion] kernel fusion: gated residual layernorm scale shift and layernorm scale shift kernel fusion for Qwen-Image, WAN and HunyuanVideo |
| `pr-sglang-14781` | upstream-code | [`sources/prs/sglang/PR-14781.md`](../sources/prs/sglang/PR-14781.md) | [Performance] optimize NSA backend metadata computation for multi-step speculative decoding |
| `pr-sglang-14820` | upstream-code | [`sources/prs/sglang/PR-14820.md`](../sources/prs/sglang/PR-14820.md) | [NPU][eagle3] support qwen eagle3 on NPU |
| `pr-sglang-14829` | upstream-code | [`sources/prs/sglang/PR-14829.md`](../sources/prs/sglang/PR-14829.md) | Apply back moe_sum_reduce for fused_marlin_moe |
| `pr-sglang-14844` | upstream-code | [`sources/prs/sglang/PR-14844.md`](../sources/prs/sglang/PR-14844.md) | fix fp8 gemm nightly CI |
| `pr-sglang-14878` | upstream-code | [`sources/prs/sglang/PR-14878.md`](../sources/prs/sglang/PR-14878.md) | [diffusion] feat: support sageattn & sageattn3 backend |
| `pr-sglang-14897` | upstream-code | [`sources/prs/sglang/PR-14897.md`](../sources/prs/sglang/PR-14897.md) | Fix dsv3 dp accuracy issue when using bf16-kv |
| `pr-sglang-14936` | upstream-code | [`sources/prs/sglang/PR-14936.md`](../sources/prs/sglang/PR-14936.md) | Fix accuracy issue when using a16w16 mla_decode_fwd |
| `pr-sglang-15002` | upstream-code | [`sources/prs/sglang/PR-15002.md`](../sources/prs/sglang/PR-15002.md) | [Fix] Disable trtllm moe backend for draft model for a qucik fix |
| `pr-sglang-15022` | upstream-code | [`sources/prs/sglang/PR-15022.md`](../sources/prs/sglang/PR-15022.md) | fixed trtllm nvfp4 backend for moe |
| `pr-sglang-15049` | upstream-code | [`sources/prs/sglang/PR-15049.md`](../sources/prs/sglang/PR-15049.md) | Mistral Large 3 NVFP4 TRTLLM MoE support |
| `pr-sglang-15100` | upstream-code | [`sources/prs/sglang/PR-15100.md`](../sources/prs/sglang/PR-15100.md) | Support piecewise cuda graph for fused marlin moe |
| `pr-sglang-15131` | upstream-code | [`sources/prs/sglang/PR-15131.md`](../sources/prs/sglang/PR-15131.md) | Feature/trtllm mha workspace size configurable #15089 |
| `pr-sglang-15141` | upstream-code | [`sources/prs/sglang/PR-15141.md`](../sources/prs/sglang/PR-15141.md) | [sgl-kernel][1/2] Fused qk_norm_rope for GLM4.6 |
| `pr-sglang-15151` | upstream-code | [`sources/prs/sglang/PR-15151.md`](../sources/prs/sglang/PR-15151.md) | MoE Refactor: Refactor `fp8.py` -> `flashinfer_trllm.py` |
| `pr-sglang-15182` | upstream-code | [`sources/prs/sglang/PR-15182.md`](../sources/prs/sglang/PR-15182.md) | [NVIDIA] upstream FA4 |
| `pr-sglang-15280` | upstream-code | [`sources/prs/sglang/PR-15280.md`](../sources/prs/sglang/PR-15280.md) | [NVIDIA] Fixes for NVFP4 all-gather with spec decoding |
| `pr-sglang-15304` | upstream-code | [`sources/prs/sglang/PR-15304.md`](../sources/prs/sglang/PR-15304.md) | Fix the accuracy issue when running mxfp4 dsv3 model and enable ep |
| `pr-sglang-15306` | upstream-code | [`sources/prs/sglang/PR-15306.md`](../sources/prs/sglang/PR-15306.md) | Fix warp illegal instruction in kimi k2 thinking PCG |
| `pr-sglang-15325` | upstream-code | [`sources/prs/sglang/PR-15325.md`](../sources/prs/sglang/PR-15325.md) | feat: support bitsandbytes quantization algorithm |
| `pr-sglang-15347` | upstream-code | [`sources/prs/sglang/PR-15347.md`](../sources/prs/sglang/PR-15347.md) | Use dsv3 optimized routing `fused_topk_deepseek` instead of `moe_fused_gate` |
| `pr-sglang-15353` | upstream-code | [`sources/prs/sglang/PR-15353.md`](../sources/prs/sglang/PR-15353.md) | Refactor fp8 nextn layer for DeepSeek nvfp4 checkpoint |
| `pr-sglang-15381` | upstream-code | [`sources/prs/sglang/PR-15381.md`](../sources/prs/sglang/PR-15381.md) | [NPU]DeepSeek-V3.2 support npu mlaprolog |
| `pr-sglang-15382` | upstream-code | [`sources/prs/sglang/PR-15382.md`](../sources/prs/sglang/PR-15382.md) | [diffusion] Add Sage Attention 3 Support for sm 120 (RTX5090) |
| `pr-sglang-15422` | upstream-code | [`sources/prs/sglang/PR-15422.md`](../sources/prs/sglang/PR-15422.md) | Flashinfer MOE FP8 support for Mistral Large 3. |
| `pr-sglang-15471` | upstream-code | [`sources/prs/sglang/PR-15471.md`](../sources/prs/sglang/PR-15471.md) | [sgl-kernel][6/7]Support Expert Specialization Grouped GEMM |
| `pr-sglang-15514` | upstream-code | [`sources/prs/sglang/PR-15514.md`](../sources/prs/sglang/PR-15514.md) | [Perf] Add Flashinfer DeepGEMM SM90 for SwapAB Optimization |
| `pr-sglang-15522` | upstream-code | [`sources/prs/sglang/PR-15522.md`](../sources/prs/sglang/PR-15522.md) | Optimize FP8 MLA KV cache writes with Triton kernel |
| `pr-sglang-15531` | upstream-code | [`sources/prs/sglang/PR-15531.md`](../sources/prs/sglang/PR-15531.md) | Support piecewise cuda graph for dsv3 fp4 |
| `pr-sglang-15539` | upstream-code | [`sources/prs/sglang/PR-15539.md`](../sources/prs/sglang/PR-15539.md) | MoE: Skip SiLU/GELU activation for masked experts |
| `pr-sglang-15551` | upstream-code | [`sources/prs/sglang/PR-15551.md`](../sources/prs/sglang/PR-15551.md) | Update flashinfer to 0.6.1 |
| `pr-sglang-15569` | upstream-code | [`sources/prs/sglang/PR-15569.md`](../sources/prs/sglang/PR-15569.md) | Add triton_fused_moe config for GLM-4.6-FP8 tp8 blackwell |
| `pr-sglang-15601` | upstream-code | [`sources/prs/sglang/PR-15601.md`](../sources/prs/sglang/PR-15601.md) | Fix BatchMLAPagedAttentionWrapper query/qo_inptr mismatch for EAGLE |
| `pr-sglang-15631` | upstream-code | [`sources/prs/sglang/PR-15631.md`](../sources/prs/sglang/PR-15631.md) | [jit-kernel] Add CuTe DSL GDN Decode Kernel |
| `pr-sglang-15712` | upstream-code | [`sources/prs/sglang/PR-15712.md`](../sources/prs/sglang/PR-15712.md) | Add SwapAB Optimization for triton fused_moe_kernel on SM90. |
| `pr-sglang-15731` | upstream-code | [`sources/prs/sglang/PR-15731.md`](../sources/prs/sglang/PR-15731.md) | [Perf] Eliminate the slice op for Flashinfer `trtllm_fp4_block_scale_moe` |
| `pr-sglang-15790` | upstream-code | [`sources/prs/sglang/PR-15790.md`](../sources/prs/sglang/PR-15790.md) | [MTP][spec_v2] Fix TRTLLM MLA backend crash in EAGLE draft_extend mode  |
| `pr-sglang-15815` | upstream-code | [`sources/prs/sglang/PR-15815.md`](../sources/prs/sglang/PR-15815.md) | [Nemotron 3 Nano] Add triton MoE configs |
| `pr-sglang-15835` | upstream-code | [`sources/prs/sglang/PR-15835.md`](../sources/prs/sglang/PR-15835.md) | [Feature] JIT Fused QK norm + qk norm clean up |
| `pr-sglang-15836` | upstream-code | [`sources/prs/sglang/PR-15836.md`](../sources/prs/sglang/PR-15836.md) | [JIT kernel] Apply jit per_tensor_quant_fp8 kernel |
| `pr-sglang-15842` | upstream-code | [`sources/prs/sglang/PR-15842.md`](../sources/prs/sglang/PR-15842.md) | [diffusion] refactor: centralize hardware platform detection and streamline environment variable management |
| `pr-sglang-15888` | upstream-code | [`sources/prs/sglang/PR-15888.md`](../sources/prs/sglang/PR-15888.md) | [diffusion] model: support TurboWan2.1-T2V-1.3B/14B SLA |
| `pr-sglang-15891` | upstream-code | [`sources/prs/sglang/PR-15891.md`](../sources/prs/sglang/PR-15891.md) | [fix]deepgemm precompile when warmup |
| `pr-sglang-15894` | upstream-code | [`sources/prs/sglang/PR-15894.md`](../sources/prs/sglang/PR-15894.md) | Bugfix for ds-vl2 |
| `pr-sglang-15904` | upstream-code | [`sources/prs/sglang/PR-15904.md`](../sources/prs/sglang/PR-15904.md) | [NPU] NZ for non-quantized MOE, Qwen3 MOE double memory consumption fix |
| `pr-sglang-15927` | upstream-code | [`sources/prs/sglang/PR-15927.md`](../sources/prs/sglang/PR-15927.md) | Piecewise Cuda Graph Memory Usage |
| `pr-sglang-15948` | upstream-code | [`sources/prs/sglang/PR-15948.md`](../sources/prs/sglang/PR-15948.md) |  Add tuned triton==3.5.1 h200 tp2, tp4 for qwen 3 next |
| `pr-sglang-16014` | upstream-code | [`sources/prs/sglang/PR-16014.md`](../sources/prs/sglang/PR-16014.md) | [Performance] Force split_k=1 for MXFP4 Triton kernels on Hopper |
| `pr-sglang-16034` | upstream-code | [`sources/prs/sglang/PR-16034.md`](../sources/prs/sglang/PR-16034.md) | Support fa4 decoding |
| `pr-sglang-16043` | upstream-code | [`sources/prs/sglang/PR-16043.md`](../sources/prs/sglang/PR-16043.md) | optimize get_topk_ragged by fusing get k and k_scale triton kernel |
| `pr-sglang-16076` | upstream-code | [`sources/prs/sglang/PR-16076.md`](../sources/prs/sglang/PR-16076.md) | enhance accuracy for model kimi-vl-instruct-a3b |
| `pr-sglang-16084` | upstream-code | [`sources/prs/sglang/PR-16084.md`](../sources/prs/sglang/PR-16084.md) | fix layer intermediate size |
| `pr-sglang-16162` | upstream-code | [`sources/prs/sglang/PR-16162.md`](../sources/prs/sglang/PR-16162.md) | [Feature] add aligned_vector type for JIT kernel |
| `pr-sglang-16171` | upstream-code | [`sources/prs/sglang/PR-16171.md`](../sources/prs/sglang/PR-16171.md) | [VLM] Adopt jit qk_norm kernel in VLM |
| `pr-sglang-16227` | upstream-code | [`sources/prs/sglang/PR-16227.md`](../sources/prs/sglang/PR-16227.md) | [NemotronH] Add latent MoE support |
| `pr-sglang-16335` | upstream-code | [`sources/prs/sglang/PR-16335.md`](../sources/prs/sglang/PR-16335.md) | [diffusion] Fix RuntimeError in SageAttention3 on Nvidia Blackwell with Qwen-Image |
| `pr-sglang-16382` | upstream-code | [`sources/prs/sglang/PR-16382.md`](../sources/prs/sglang/PR-16382.md) | [Fix]Fix FA3 Performance in Diffusion Model  |
| `pr-sglang-16531` | upstream-code | [`sources/prs/sglang/PR-16531.md`](../sources/prs/sglang/PR-16531.md) | [AMD] Fix aiter page-size handling, DeepSeek MLA tuple inputs, and HiCache/FA3 decode-backend override |
| `pr-sglang-16622` | upstream-code | [`sources/prs/sglang/PR-16622.md`](../sources/prs/sglang/PR-16622.md) | Fix FP8 MoE NaN with DeepGEMM on Blackwell |
| `pr-sglang-16685` | upstream-code | [`sources/prs/sglang/PR-16685.md`](../sources/prs/sglang/PR-16685.md) | MoE Refactor: Refactor `modelopt_quant.py` -> `flashinfer_trllm.py` |
| `pr-sglang-16723` | upstream-code | [`sources/prs/sglang/PR-16723.md`](../sources/prs/sglang/PR-16723.md) | [Rework] Add SwapAB Optimization for triton fused_moe_kernel on SM90. |
| `pr-sglang-16824` | upstream-code | [`sources/prs/sglang/PR-16824.md`](../sources/prs/sglang/PR-16824.md) | [Fix] `flashinfer_trtllm` `intermediate_size` assertion with Qwen3 + TP=8 |
| `pr-sglang-16882` | upstream-code | [`sources/prs/sglang/PR-16882.md`](../sources/prs/sglang/PR-16882.md) | Add dpsk-r1-fp4 in nightly perf ci |
| `pr-sglang-16892` | upstream-code | [`sources/prs/sglang/PR-16892.md`](../sources/prs/sglang/PR-16892.md) | Support mxint4 flashinfer_trtllm moe gemm |
| `pr-sglang-16961` | upstream-code | [`sources/prs/sglang/PR-16961.md`](../sources/prs/sglang/PR-16961.md) | [DeepSeek v3.2] Opt MTP decode cuda batch sizes and nsa implementation |
| `pr-sglang-16971` | upstream-code | [`sources/prs/sglang/PR-16971.md`](../sources/prs/sglang/PR-16971.md) | fix: renaming test file and job names + skip blocking llama4 nightly |
| `pr-sglang-16974` | upstream-code | [`sources/prs/sglang/PR-16974.md`](../sources/prs/sglang/PR-16974.md) | [SPEC_V2] Enable cudagraph draft_extend for trtllm_mla_backend and Acclen Fix for DP under cudagraph mode |
| `pr-sglang-17007` | upstream-code | [`sources/prs/sglang/PR-17007.md`](../sources/prs/sglang/PR-17007.md) | [NPU]bugfix: fix for dsv3.2 and dsvl2 |
| `pr-sglang-17012` | upstream-code | [`sources/prs/sglang/PR-17012.md`](../sources/prs/sglang/PR-17012.md) | Integration mori backend for EP a2a data communication |
| `pr-sglang-17022` | upstream-code | [`sources/prs/sglang/PR-17022.md`](../sources/prs/sglang/PR-17022.md) | Add 5090 dry run stage to PR test workflow |
| `pr-sglang-17053` | upstream-code | [`sources/prs/sglang/PR-17053.md`](../sources/prs/sglang/PR-17053.md) | [MUSA][2/N] sgl-kernel build |
| `pr-sglang-17077` | upstream-code | [`sources/prs/sglang/PR-17077.md`](../sources/prs/sglang/PR-17077.md) | [Diffusion] Revise Diffusion FA backend to support blackwell |
| `pr-sglang-17094` | upstream-code | [`sources/prs/sglang/PR-17094.md`](../sources/prs/sglang/PR-17094.md) | Optimize GDN decode for Qwen3 Next |
| `pr-sglang-17111` | upstream-code | [`sources/prs/sglang/PR-17111.md`](../sources/prs/sglang/PR-17111.md) | [diffusion] fix: fix using upstream flash_attn on blackwell |
| `pr-sglang-17115` | upstream-code | [`sources/prs/sglang/PR-17115.md`](../sources/prs/sglang/PR-17115.md) | Enable XQA for SM90 and SM120 |
| `pr-sglang-17158` | upstream-code | [`sources/prs/sglang/PR-17158.md`](../sources/prs/sglang/PR-17158.md) | Inclusion of nvfp4 blockscale in EPLB Rebalance |
| `pr-sglang-17235` | upstream-code | [`sources/prs/sglang/PR-17235.md`](../sources/prs/sglang/PR-17235.md) | [GLM 4.7] Add RTX 6000 Pro aka sm120 |
| `pr-sglang-17300` | upstream-code | [`sources/prs/sglang/PR-17300.md`](../sources/prs/sglang/PR-17300.md) | [FIX] Always support TP > 4 for FP4 Gemm |
| `pr-sglang-17309` | upstream-code | [`sources/prs/sglang/PR-17309.md`](../sources/prs/sglang/PR-17309.md) | [Refactor] Set `fp4-gemm-backend=auto` on SM100 and rename `fp4-gemm-backend` with `flashinfer_` prefix |
| `pr-sglang-17327` | upstream-code | [`sources/prs/sglang/PR-17327.md`](../sources/prs/sglang/PR-17327.md) | Disable mla persistent kernel when not using fp8 kv_cache |
| `pr-sglang-17353` | upstream-code | [`sources/prs/sglang/PR-17353.md`](../sources/prs/sglang/PR-17353.md) | Move fa4 from sgl-kernel to jit kernel |
| `pr-sglang-17449` | upstream-code | [`sources/prs/sglang/PR-17449.md`](../sources/prs/sglang/PR-17449.md) | Add mxfp8 support for online quantization, Triton dense linear, and CUTLASS MoE |
| `pr-sglang-17450` | upstream-code | [`sources/prs/sglang/PR-17450.md`](../sources/prs/sglang/PR-17450.md) | [AMD] Support speculative decoding v2 for aiter backend on ROCm/HIP |
| `pr-sglang-17480` | upstream-code | [`sources/prs/sglang/PR-17480.md`](../sources/prs/sglang/PR-17480.md) | [NPU] enhance accuracy for model kimi-vl-a3b-instruct |
| `pr-sglang-17499` | upstream-code | [`sources/prs/sglang/PR-17499.md`](../sources/prs/sglang/PR-17499.md) | [MUSA][7/N] Enhance CUDA / PyNccl wrapper to support MTLink connectivity detection |
| `pr-sglang-17503` | upstream-code | [`sources/prs/sglang/PR-17503.md`](../sources/prs/sglang/PR-17503.md) | [2/N] Quantization Refactor: Compressed tensors MoE schemes |
| `pr-sglang-17514` | upstream-code | [`sources/prs/sglang/PR-17514.md`](../sources/prs/sglang/PR-17514.md) | [Diffusion] Support select fa2 backend in hopper |
| `pr-sglang-17554` | upstream-code | [`sources/prs/sglang/PR-17554.md`](../sources/prs/sglang/PR-17554.md) | Kernel: optimize decoding metadata in NSA multi-spec backend with fused kernels |
| `pr-sglang-17627` | upstream-code | [`sources/prs/sglang/PR-17627.md`](../sources/prs/sglang/PR-17627.md) | [feat] Support nvfp4 quantized model of Qwen3-Next |
| `pr-sglang-17707` | upstream-code | [`sources/prs/sglang/PR-17707.md`](../sources/prs/sglang/PR-17707.md) | Add dsv3 router gemm benchmark on blackwell |
| `pr-sglang-17784` | upstream-code | [`sources/prs/sglang/PR-17784.md`](../sources/prs/sglang/PR-17784.md) | Upgrade transformers==5.3.0 |
| `pr-sglang-17816` | upstream-code | [`sources/prs/sglang/PR-17816.md`](../sources/prs/sglang/PR-17816.md) | fix(quantization): add sgl_kernel fallback for FP4 quantize on Blackwell GPUs |
| `pr-sglang-17838` | upstream-code | [`sources/prs/sglang/PR-17838.md`](../sources/prs/sglang/PR-17838.md) | Feature/support longcat flash lite |
| `pr-sglang-17889` | upstream-code | [`sources/prs/sglang/PR-17889.md`](../sources/prs/sglang/PR-17889.md) | [Move sgl-kernel Kernel to JIT] Add JIT concat MLA kernels |
| `pr-sglang-17985` | upstream-code | [`sources/prs/sglang/PR-17985.md`](../sources/prs/sglang/PR-17985.md) | [MUSA][9/N] Add FA3 attention backend support through MATE (MUSA AI Tensor Engine) |
| `pr-sglang-18065` | upstream-code | [`sources/prs/sglang/PR-18065.md`](../sources/prs/sglang/PR-18065.md) | [Bugfix] Fix Mistral Large 3 NVFP4 TRTLLM MoE |
| `pr-sglang-18070` | upstream-code | [`sources/prs/sglang/PR-18070.md`](../sources/prs/sglang/PR-18070.md) | Feat/add fi selective state update kernel call |
| `pr-sglang-18073` | upstream-code | [`sources/prs/sglang/PR-18073.md`](../sources/prs/sglang/PR-18073.md) | [Diffsuion & JIT_kernel] QKNorm cross heads kernel |
| `pr-sglang-18085` | upstream-code | [`sources/prs/sglang/PR-18085.md`](../sources/prs/sglang/PR-18085.md) | Fix nvfp4 weight update |
| `pr-sglang-18111` | upstream-code | [`sources/prs/sglang/PR-18111.md`](../sources/prs/sglang/PR-18111.md) | [DeepGemm] Add a flag for fast warmup |
| `pr-sglang-18113` | upstream-code | [`sources/prs/sglang/PR-18113.md`](../sources/prs/sglang/PR-18113.md) | [HiCache] refactor page_first_direct io kernel |
| `pr-sglang-18184` | upstream-code | [`sources/prs/sglang/PR-18184.md`](../sources/prs/sglang/PR-18184.md) | Add piecewise cuda graph for Qwen3-Next FP8 flashinfer_trtllm moe backend |
| `pr-sglang-18233` | upstream-code | [`sources/prs/sglang/PR-18233.md`](../sources/prs/sglang/PR-18233.md) | Support Qwen3 MoE context parallel |
| `pr-sglang-18242` | upstream-code | [`sources/prs/sglang/PR-18242.md`](../sources/prs/sglang/PR-18242.md) | [ROCm] Optimize Deepseek R1 on MI300X |
| `pr-sglang-18311` | upstream-code | [`sources/prs/sglang/PR-18311.md`](../sources/prs/sglang/PR-18311.md) | [Hicache & JIT_kernel] Support page first layout  & mla jit kernel |
| `pr-sglang-18341` | upstream-code | [`sources/prs/sglang/PR-18341.md`](../sources/prs/sglang/PR-18341.md) | [FlashInfer] Switch FlashInfer allreduce fusion to unified API |
| `pr-sglang-18355` | upstream-code | [`sources/prs/sglang/PR-18355.md`](../sources/prs/sglang/PR-18355.md) | [AMD] Support Qwen3-Coder-Next on AMD platform |
| `pr-sglang-18357` | upstream-code | [`sources/prs/sglang/PR-18357.md`](../sources/prs/sglang/PR-18357.md) | [MUSA][10/N] Add GGUF support |
| `pr-sglang-18361` | upstream-code | [`sources/prs/sglang/PR-18361.md`](../sources/prs/sglang/PR-18361.md) | feat(gdn): add FlashInfer K-last SSM layout support for GDN prefill and decode for Hopper |
| `pr-sglang-18362` | upstream-code | [`sources/prs/sglang/PR-18362.md`](../sources/prs/sglang/PR-18362.md) | [sgl-kernel] upgrade deepgemm |
| `pr-sglang-18364` | upstream-code | [`sources/prs/sglang/PR-18364.md`](../sources/prs/sglang/PR-18364.md) | [Fix] Fix backend selection after flashinfer version update |
| `pr-sglang-18370` | upstream-code | [`sources/prs/sglang/PR-18370.md`](../sources/prs/sglang/PR-18370.md) | [Kimi-K2.5] Fix NVFP4 Kimi-K2.5 weight mapping and exclude list |
| `pr-sglang-18389` | upstream-code | [`sources/prs/sglang/PR-18389.md`](../sources/prs/sglang/PR-18389.md) | Nsa trtllm mla sparse fp8 support with Deepseek v3.2 NVFP4 |
| `pr-sglang-18396` | upstream-code | [`sources/prs/sglang/PR-18396.md`](../sources/prs/sglang/PR-18396.md) | Fix TRT-LLM MLA backend applying k_scale to BF16 KV cache in BMM1 |
| `pr-sglang-18423` | upstream-code | [`sources/prs/sglang/PR-18423.md`](../sources/prs/sglang/PR-18423.md) | [AMD] Update aiter to v0.1.10.post2 |
| `pr-sglang-18442` | upstream-code | [`sources/prs/sglang/PR-18442.md`](../sources/prs/sglang/PR-18442.md) | feat: add FA4 SM90 paged KV decode support & update attention docs |
| `pr-sglang-18488` | upstream-code | [`sources/prs/sglang/PR-18488.md`](../sources/prs/sglang/PR-18488.md) | Tilelang sparse decode fwd for dsv32 mi355 |
| `pr-sglang-18500` | upstream-code | [`sources/prs/sglang/PR-18500.md`](../sources/prs/sglang/PR-18500.md) | [Flashinfer Autotune] Fix FlashInfer FP4 MoE autotuning crash by removing incorrect flatten on hidden_states_scale |
| `pr-sglang-18526` | upstream-code | [`sources/prs/sglang/PR-18526.md`](../sources/prs/sglang/PR-18526.md) | [AMD] Enable cudagraph for aiter nsa backend and add aiter impl for nsa pr… |
| `pr-sglang-18528` | upstream-code | [`sources/prs/sglang/PR-18528.md`](../sources/prs/sglang/PR-18528.md) | Fp8 prefill attn kernel integration |
| `pr-sglang-18562` | upstream-code | [`sources/prs/sglang/PR-18562.md`](../sources/prs/sglang/PR-18562.md) | Revert "[sgl-kernel] upgrade deepgemm" |
| `pr-sglang-18607` | upstream-code | [`sources/prs/sglang/PR-18607.md`](../sources/prs/sglang/PR-18607.md) | [AMD] Fix accuracy issue when running TP4 dsv3 model with mtp |
| `pr-sglang-18639` | upstream-code | [`sources/prs/sglang/PR-18639.md`](../sources/prs/sglang/PR-18639.md) | [sglang-miles] True on-policy training support for FSDP2 |
| `pr-sglang-18696` | upstream-code | [`sources/prs/sglang/PR-18696.md`](../sources/prs/sglang/PR-18696.md) | use flashinfer.sampling |
| `pr-sglang-18742` | upstream-code | [`sources/prs/sglang/PR-18742.md`](../sources/prs/sglang/PR-18742.md) | [RL] Support per-layer mixed FP8/BF16 serving for FP8 checkpoints |
| `pr-sglang-18750` | upstream-code | [`sources/prs/sglang/PR-18750.md`](../sources/prs/sglang/PR-18750.md) | fix(sgl-kernel): use >= 120 for SM12x CUDA kernel dispatch |
| `pr-sglang-18762` | upstream-code | [`sources/prs/sglang/PR-18762.md`](../sources/prs/sglang/PR-18762.md) | [diffusion] Diffusion norm fusion for z-image |
| `pr-sglang-18801` | upstream-code | [`sources/prs/sglang/PR-18801.md`](../sources/prs/sglang/PR-18801.md) | Support CuteDSL `mm_fp4` backend |
| `pr-sglang-18844` | upstream-code | [`sources/prs/sglang/PR-18844.md`](../sources/prs/sglang/PR-18844.md) | [Feature] rewrite rope kernel; remove flashinfer dependencies |
| `pr-sglang-18854` | upstream-code | [`sources/prs/sglang/PR-18854.md`](../sources/prs/sglang/PR-18854.md) | Migrate renorm kernels from sgl-kernel to FlashInfer JIT |
| `pr-sglang-18858` | upstream-code | [`sources/prs/sglang/PR-18858.md`](../sources/prs/sglang/PR-18858.md) | [Perf] ~9.5x faster Blackwell MXFP4 MoE weight loading |
| `pr-sglang-18871` | upstream-code | [`sources/prs/sglang/PR-18871.md`](../sources/prs/sglang/PR-18871.md) | Migrate norm kernels to FlashInfer JIT implementation |
| `pr-sglang-18882` | upstream-code | [`sources/prs/sglang/PR-18882.md`](../sources/prs/sglang/PR-18882.md) | feat: Add FP8 KV cache support for Triton attention backend |
| `pr-sglang-18902` | upstream-code | [`sources/prs/sglang/PR-18902.md`](../sources/prs/sglang/PR-18902.md) | [sgl-kernel] rebase FlashMLA 0217 |
| `pr-sglang-19003` | upstream-code | [`sources/prs/sglang/PR-19003.md`](../sources/prs/sglang/PR-19003.md) | [VLM] Introduce FlashInfer CUDNN Prefill as ViT Backend |
| `pr-sglang-19041` | upstream-code | [`sources/prs/sglang/PR-19041.md`](../sources/prs/sglang/PR-19041.md) | [DSv32] [GLM5] Improve Model Quality by Avoiding FP32 Precision Loss in `weights_proj` |
| `pr-sglang-19059` | upstream-code | [`sources/prs/sglang/PR-19059.md`](../sources/prs/sglang/PR-19059.md) | [jit_kernel] Add fused_qknorm_rope JIT kernel |
| `pr-sglang-19086` | upstream-code | [`sources/prs/sglang/PR-19086.md`](../sources/prs/sglang/PR-19086.md) | [Fix][Qwen3.5] Fix KV cache slice transfer for GQA models with replicated KV heads |
| `pr-sglang-19089` | upstream-code | [`sources/prs/sglang/PR-19089.md`](../sources/prs/sglang/PR-19089.md) | Support skip-softmax attention |
| `pr-sglang-19122` | upstream-code | [`sources/prs/sglang/PR-19122.md`](../sources/prs/sglang/PR-19122.md) | [3/n] deepseek_v2.py Refactor: Migrate MLA forward method in deepseek_v2.py |
| `pr-sglang-19143` | upstream-code | [`sources/prs/sglang/PR-19143.md`](../sources/prs/sglang/PR-19143.md) | feat: Support MXFP4 quantized dense models on AMD CDNA2/CDNA3 GPUs |
| `pr-sglang-19148` | upstream-code | [`sources/prs/sglang/PR-19148.md`](../sources/prs/sglang/PR-19148.md) | [DeepSeek-V3.2][JIT-kernel] Support nsa fuse store indexer k cache |
| `pr-sglang-19150` | upstream-code | [`sources/prs/sglang/PR-19150.md`](../sources/prs/sglang/PR-19150.md) | [NVIDIA] Integrate FlashInfer decode kernel (Blackwell) for Qwen3.5 |
| `pr-sglang-19174` | upstream-code | [`sources/prs/sglang/PR-19174.md`](../sources/prs/sglang/PR-19174.md) | Adjust padding size to improve triton_kernels moe performance |
| `pr-sglang-19189` | upstream-code | [`sources/prs/sglang/PR-19189.md`](../sources/prs/sglang/PR-19189.md) | Fix fallback to default tactic (flashinfer autotuner) with trtllm_fp4_block_scale_moe |
| `pr-sglang-19201` | upstream-code | [`sources/prs/sglang/PR-19201.md`](../sources/prs/sglang/PR-19201.md) | Add server CUDA graph warmup CI step for cold H200 nodes |
| `pr-sglang-19216` | upstream-code | [`sources/prs/sglang/PR-19216.md`](../sources/prs/sglang/PR-19216.md) | [AMD][with CI Fix] support two batch overlapping for mori ep |
| `pr-sglang-19220` | upstream-code | [`sources/prs/sglang/PR-19220.md`](../sources/prs/sglang/PR-19220.md) | [PCG] fix piecewise cuda graph for Qwen3.5 |
| `pr-sglang-19247` | upstream-code | [`sources/prs/sglang/PR-19247.md`](../sources/prs/sglang/PR-19247.md) | [AMD] Fix accuracy while using --enable-dp-attention |
| `pr-sglang-19362` | upstream-code | [`sources/prs/sglang/PR-19362.md`](../sources/prs/sglang/PR-19362.md) | [AMD] Fix EAGLE3 speculative decoding with aiter attention backend |
| `pr-sglang-19391` | upstream-code | [`sources/prs/sglang/PR-19391.md`](../sources/prs/sglang/PR-19391.md) | [Qwen3.5] Enable MTP spec_v2 and add test for nvidia/Qwen3.5-397B-A17B-NVFP4 |
| `pr-sglang-19400` | upstream-code | [`sources/prs/sglang/PR-19400.md`](../sources/prs/sglang/PR-19400.md) | Fix missing StandardCombineInput import in BF16 flashinfer_trtllm MoE |
| `pr-sglang-19425` | upstream-code | [`sources/prs/sglang/PR-19425.md`](../sources/prs/sglang/PR-19425.md) | [AMD] Fix weight load shape mismatch for amd dsr1 0528 mxfp4 |
| `pr-sglang-19428` | upstream-code | [`sources/prs/sglang/PR-19428.md`](../sources/prs/sglang/PR-19428.md) | [Feature] add feature mla_ag_after_qlora for dsv3.2 |
| `pr-sglang-19433` | upstream-code | [`sources/prs/sglang/PR-19433.md`](../sources/prs/sglang/PR-19433.md) | Fix/nemotron mtp quantaized |
| `pr-sglang-19437` | upstream-code | [`sources/prs/sglang/PR-19437.md`](../sources/prs/sglang/PR-19437.md) | [Kernel Slimming] Migrate NVFP4 kernels to JIT |
| `pr-sglang-19504` | upstream-code | [`sources/prs/sglang/PR-19504.md`](../sources/prs/sglang/PR-19504.md) | [PD] Support PD with context parallel after refactor |
| `pr-sglang-19536` | upstream-code | [`sources/prs/sglang/PR-19536.md`](../sources/prs/sglang/PR-19536.md) | [Perf] Optimize NSA backend metadata under MTP |
| `pr-sglang-19537` | upstream-code | [`sources/prs/sglang/PR-19537.md`](../sources/prs/sglang/PR-19537.md) | [FlashInfer v0.6.4] [RL] Integrate FlashInfer mxfp8 gemm, MoE, and routed MoE |
| `pr-sglang-19544` | upstream-code | [`sources/prs/sglang/PR-19544.md`](../sources/prs/sglang/PR-19544.md) | [NPU] bugs fix for Deepseek models |
| `pr-sglang-19549` | upstream-code | [`sources/prs/sglang/PR-19549.md`](../sources/prs/sglang/PR-19549.md) | [diffusion][llm] macOS support |
| `pr-sglang-19550` | upstream-code | [`sources/prs/sglang/PR-19550.md`](../sources/prs/sglang/PR-19550.md) | [AMD] Add AWQ AMD CI coverage and quantization platform compatibility docs |
| `pr-sglang-19634` | upstream-code | [`sources/prs/sglang/PR-19634.md`](../sources/prs/sglang/PR-19634.md) | [miles] fix for glm5 |
| `pr-sglang-19652` | upstream-code | [`sources/prs/sglang/PR-19652.md`](../sources/prs/sglang/PR-19652.md) | [Feature] NVFP4 Marlin fallback for non-Blackwell GPUs (SM75+) |
| `pr-sglang-19718` | upstream-code | [`sources/prs/sglang/PR-19718.md`](../sources/prs/sglang/PR-19718.md) | Support `triton_kernels` for GPT-OSS on SM120 |
| `pr-sglang-19721` | upstream-code | [`sources/prs/sglang/PR-19721.md`](../sources/prs/sglang/PR-19721.md) | Various SM120 improvements |
| `pr-sglang-19725` | upstream-code | [`sources/prs/sglang/PR-19725.md`](../sources/prs/sglang/PR-19725.md) | [SGLang-Diffusion] Fix custom op fake impl missing eps default for torch.compile |
| `pr-sglang-19736` | upstream-code | [`sources/prs/sglang/PR-19736.md`](../sources/prs/sglang/PR-19736.md) | [AMD] Fix Qwen3-Coder-Next: Add missing k_scale/v_scale args to extend_attention_fwd in aiter_backend |
| `pr-sglang-19770` | upstream-code | [`sources/prs/sglang/PR-19770.md`](../sources/prs/sglang/PR-19770.md) | [Docs] Add docstrings to JIT kernel include headers |
| `pr-sglang-19794` | upstream-code | [`sources/prs/sglang/PR-19794.md`](../sources/prs/sglang/PR-19794.md) | Add compile-time 256-bit vector guard for pre-Blackwell |
| `pr-sglang-19835` | upstream-code | [`sources/prs/sglang/PR-19835.md`](../sources/prs/sglang/PR-19835.md) | fix cuda graph capturing error in sm120 mxfp8 triton path |
| `pr-sglang-19880` | upstream-code | [`sources/prs/sglang/PR-19880.md`](../sources/prs/sglang/PR-19880.md) | [JIT Kernel][Feature] Support JIT custom all reduce (rewrite as v2) |
| `pr-sglang-19902` | upstream-code | [`sources/prs/sglang/PR-19902.md`](../sources/prs/sglang/PR-19902.md) | Fix MLA decode path returning unwritten (padded) rows |
| `pr-sglang-19928` | upstream-code | [`sources/prs/sglang/PR-19928.md`](../sources/prs/sglang/PR-19928.md) | [AMD] Fix Tensor Memory Aliasing  |
| `pr-sglang-19935` | upstream-code | [`sources/prs/sglang/PR-19935.md`](../sources/prs/sglang/PR-19935.md) | [AMD] Fix FP8 assertion failure in aiter MLA decode by falling back to self.k_scale |
| `pr-sglang-19945` | upstream-code | [`sources/prs/sglang/PR-19945.md`](../sources/prs/sglang/PR-19945.md) | [AMD] Tilelang sparse fwd for dsv32 mi355/mi300 |
| `pr-sglang-20012` | upstream-code | [`sources/prs/sglang/PR-20012.md`](../sources/prs/sglang/PR-20012.md) | [JIT Kernel] Reland NVFP4 kernels to JIT |
| `pr-sglang-20039` | upstream-code | [`sources/prs/sglang/PR-20039.md`](../sources/prs/sglang/PR-20039.md) | [Bugfix] Work around FlashInfer unified transport issue on GB |
| `pr-sglang-20040` | upstream-code | [`sources/prs/sglang/PR-20040.md`](../sources/prs/sglang/PR-20040.md) | Fix SM120 `triton_kernels` MXFP4 `block_k` for GPT-OSS |
| `pr-sglang-20047` | upstream-code | [`sources/prs/sglang/PR-20047.md`](../sources/prs/sglang/PR-20047.md) | fix: default FP4 GEMM backend to flashinfer_cudnn on SM120 (Blackwell) |
| `pr-sglang-20061` | upstream-code | [`sources/prs/sglang/PR-20061.md`](../sources/prs/sglang/PR-20061.md) | Fix flashinfer backend with pcg |
| `pr-sglang-20062` | upstream-code | [`sources/prs/sglang/PR-20062.md`](../sources/prs/sglang/PR-20062.md) | [V32/GLM5] Control the threshold of applying dense attention with an environ |
| `pr-sglang-20082` | upstream-code | [`sources/prs/sglang/PR-20082.md`](../sources/prs/sglang/PR-20082.md) | Enable modelopt quantized FLUX deployment |
| `pr-sglang-20094` | upstream-code | [`sources/prs/sglang/PR-20094.md`](../sources/prs/sglang/PR-20094.md) | [diffusion] fix bug of copy_if |
| `pr-sglang-20137` | upstream-code | [`sources/prs/sglang/PR-20137.md`](../sources/prs/sglang/PR-20137.md) | [diffusion] Support nvfp4 for Flux.2 |
| `pr-sglang-20187` | upstream-code | [`sources/prs/sglang/PR-20187.md`](../sources/prs/sglang/PR-20187.md) | [AMD] Fp8 prefill integration with radix cache path for dpsk models |
| `pr-sglang-20214` | upstream-code | [`sources/prs/sglang/PR-20214.md`](../sources/prs/sglang/PR-20214.md) | [FlashInfer v0.6.6][RL] Support fp8-last-n-bf16 RL for `flashinfer_trtllm_routed` moe backend |
| `pr-sglang-20268` | upstream-code | [`sources/prs/sglang/PR-20268.md`](../sources/prs/sglang/PR-20268.md) | [4/n jit_kernel restruct] speed up CI tests and add benchmark workflow |
| `pr-sglang-20277` | upstream-code | [`sources/prs/sglang/PR-20277.md`](../sources/prs/sglang/PR-20277.md) | [kernel slimming] Clean many useless sgl-kernel deprecated kernels |
| `pr-sglang-20305` | upstream-code | [`sources/prs/sglang/PR-20305.md`](../sources/prs/sglang/PR-20305.md) | [Benchmark] use flashinfer bench_gpu_time instead of triton do_bench |
| `pr-sglang-20384` | upstream-code | [`sources/prs/sglang/PR-20384.md`](../sources/prs/sglang/PR-20384.md) | [Fix] Add fallback for flashinfer allreduce fusion |
| `pr-sglang-20394` | upstream-code | [`sources/prs/sglang/PR-20394.md`](../sources/prs/sglang/PR-20394.md) | [NVIDIA] Enable fp8 flashinfer_trtllm_routed MoE for MiniMax-M2.5 |
| `pr-sglang-20399` | upstream-code | [`sources/prs/sglang/PR-20399.md`](../sources/prs/sglang/PR-20399.md) | [AMD][Bug-fix] Fix gpu fault when run the test with dp-attention-enabled and max-concurrency is over 256 |
| `pr-sglang-20407` | upstream-code | [`sources/prs/sglang/PR-20407.md`](../sources/prs/sglang/PR-20407.md) | [Model] Support Nemotron 3 Super NVFP4 |
| `pr-sglang-20409` | upstream-code | [`sources/prs/sglang/PR-20409.md`](../sources/prs/sglang/PR-20409.md) | [AMD][AITER] Guard _use_mla_ps_kernel with self.use_mla in draft_extend_v2 paths |
| `pr-sglang-20428` | upstream-code | [`sources/prs/sglang/PR-20428.md`](../sources/prs/sglang/PR-20428.md) | [GDN] Add benchmark for sglang gdn prefill |
| `pr-sglang-20457` | upstream-code | [`sources/prs/sglang/PR-20457.md`](../sources/prs/sglang/PR-20457.md) | [HiCache][HybridModel]: Support mamba state offloading & HybridCacheController |
| `pr-sglang-20479` | upstream-code | [`sources/prs/sglang/PR-20479.md`](../sources/prs/sglang/PR-20479.md) | Support Triton MLA FP8 KV cache |
| `pr-sglang-20501` | upstream-code | [`sources/prs/sglang/PR-20501.md`](../sources/prs/sglang/PR-20501.md) | [Kernel] Fuse temperature + softmax in sampling for decode speedup |
| `pr-sglang-20576` | upstream-code | [`sources/prs/sglang/PR-20576.md`](../sources/prs/sglang/PR-20576.md) | [Diffusion] Clean upstream fa3 in hopper |
| `pr-sglang-20604` | upstream-code | [`sources/prs/sglang/PR-20604.md`](../sources/prs/sglang/PR-20604.md) | Use Flashinfer for target_verify in GDN model for SM120 |
| `pr-sglang-20606` | upstream-code | [`sources/prs/sglang/PR-20606.md`](../sources/prs/sglang/PR-20606.md) | FIX: (NSA) Compute topk_indices_offset when NSA prefill flashmla_sparse is used with FP8 KV cache |
| `pr-sglang-20632` | upstream-code | [`sources/prs/sglang/PR-20632.md`](../sources/prs/sglang/PR-20632.md) | [Diffusion] Add a benchmark for rmsnorm/fuse_add_rmsnorm |
| `pr-sglang-20661` | upstream-code | [`sources/prs/sglang/PR-20661.md`](../sources/prs/sglang/PR-20661.md) | Fix(jit): support rmsnorm for hidden_size in {64, 128, 256} |
| `pr-sglang-20673` | upstream-code | [`sources/prs/sglang/PR-20673.md`](../sources/prs/sglang/PR-20673.md) | [Feature][JIT Kernel] Fused TP QK norm For Minimax |
| `pr-sglang-20708` | upstream-code | [`sources/prs/sglang/PR-20708.md`](../sources/prs/sglang/PR-20708.md) | Add Mistral Small 4 (Pixtral) support |
| `pr-sglang-20868` | upstream-code | [`sources/prs/sglang/PR-20868.md`](../sources/prs/sglang/PR-20868.md) | fix: guard configure_deep_gemm_num_sms when JIT disabled |
| `pr-sglang-20874` | upstream-code | [`sources/prs/sglang/PR-20874.md`](../sources/prs/sglang/PR-20874.md) | [JIT Kernel] Fix NVFP4 multi-arch compilation failure |
| `pr-sglang-20887` | upstream-code | [`sources/prs/sglang/PR-20887.md`](../sources/prs/sglang/PR-20887.md) | CUTLASS FP8 Blockwise GEMM improvement of SM120 |
| `pr-sglang-20910` | upstream-code | [`sources/prs/sglang/PR-20910.md`](../sources/prs/sglang/PR-20910.md) | Add SGLang CUDA crash API logging inspired by FlashInfer |
| `pr-sglang-20988` | upstream-code | [`sources/prs/sglang/PR-20988.md`](../sources/prs/sglang/PR-20988.md) | ci: run Stage A CUDA tests as stage-a-test-small-1-gpu on 5090 |
| `pr-sglang-21017` | upstream-code | [`sources/prs/sglang/PR-21017.md`](../sources/prs/sglang/PR-21017.md) | ci: refactor CUDA dependency install script |
| `pr-sglang-21019` | upstream-code | [`sources/prs/sglang/PR-21019.md`](../sources/prs/sglang/PR-21019.md) | [Qwen3.5] Fuse split/reshape/cat ops in GDN projection with Triton kernel |
| `pr-sglang-21022` | upstream-code | [`sources/prs/sglang/PR-21022.md`](../sources/prs/sglang/PR-21022.md) | [Chore] Clean up JIT compilation flags |
| `pr-sglang-21104` | upstream-code | [`sources/prs/sglang/PR-21104.md`](../sources/prs/sglang/PR-21104.md) | perf: precompute FA3 scheduler_metadata to eliminate per-layer prepare_varlen_num_blocks |
| `pr-sglang-21166` | upstream-code | [`sources/prs/sglang/PR-21166.md`](../sources/prs/sglang/PR-21166.md) | [Not-Merge][AMD] GLM-5 performance optimization |
| `pr-sglang-21190` | upstream-code | [`sources/prs/sglang/PR-21190.md`](../sources/prs/sglang/PR-21190.md) | [Whisper] Enable CUDA graph support and timestamp for whisper model |
| `pr-sglang-21203` | upstream-code | [`sources/prs/sglang/PR-21203.md`](../sources/prs/sglang/PR-21203.md) | [KDA] Support CuTeDSL KDA decode kernel |
| `pr-sglang-21213` | upstream-code | [`sources/prs/sglang/PR-21213.md`](../sources/prs/sglang/PR-21213.md) | [AMD]: Support MLA with nhead<16 and FP8 KV cache for TP=8 (Kimi K2.5… |
| `pr-sglang-21233` | upstream-code | [`sources/prs/sglang/PR-21233.md`](../sources/prs/sglang/PR-21233.md) | [refactor] Clean up duplicate flashinfer trtllm moe code |
| `pr-sglang-21239` | upstream-code | [`sources/prs/sglang/PR-21239.md`](../sources/prs/sglang/PR-21239.md) | Refactor JIT kernel CI to use run_suite.py registration system |
| `pr-sglang-21240` | upstream-code | [`sources/prs/sglang/PR-21240.md`](../sources/prs/sglang/PR-21240.md) | [NVIDIA] Enable FP4 flashinfer trtllm routed moe |
| `pr-sglang-21280` | upstream-code | [`sources/prs/sglang/PR-21280.md`](../sources/prs/sglang/PR-21280.md) | [RL] Support mxfp8 DeepSeek V3 |
| `pr-sglang-21314` | upstream-code | [`sources/prs/sglang/PR-21314.md`](../sources/prs/sglang/PR-21314.md) | CUTLASS NVFP4 GEMM improvement of SM120 |
| `pr-sglang-21321` | upstream-code | [`sources/prs/sglang/PR-21321.md`](../sources/prs/sglang/PR-21321.md) | [Kernel] Support FlashInfer TRTLLM-Gen fused MoE for non-gated FP4 & FP8 (Nemotron) |
| `pr-sglang-21325` | upstream-code | [`sources/prs/sglang/PR-21325.md`](../sources/prs/sglang/PR-21325.md) | [misc] clean up kernel API |
| `pr-sglang-21339` | upstream-code | [`sources/prs/sglang/PR-21339.md`](../sources/prs/sglang/PR-21339.md) | Add dedicated FlashInferCuteDslMoE layer for standard-path FP4 MoE |
| `pr-sglang-21403` | upstream-code | [`sources/prs/sglang/PR-21403.md`](../sources/prs/sglang/PR-21403.md) | [AMD] Fuse RMSNorm + FP8 per-token quant for GLM-4.7-FP8 |
| `pr-sglang-21411` | upstream-code | [`sources/prs/sglang/PR-21411.md`](../sources/prs/sglang/PR-21411.md) | [GDN] Fuse GDN kkt + solve_tril into one kernel |
| `pr-sglang-21428` | upstream-code | [`sources/prs/sglang/PR-21428.md`](../sources/prs/sglang/PR-21428.md) | [Bugfix] Lazy-import CuteDSL KDA kernel to fix AMD/ROCm startup crash |
| `pr-sglang-21440` | upstream-code | [`sources/prs/sglang/PR-21440.md`](../sources/prs/sglang/PR-21440.md) | [Diffusion] Add qknorm rope fuse kernel |
| `pr-sglang-21452` | upstream-code | [`sources/prs/sglang/PR-21452.md`](../sources/prs/sglang/PR-21452.md) | fix: piecewise_cuda_graph get correct qo_indptr |
| `pr-sglang-21463` | upstream-code | [`sources/prs/sglang/PR-21463.md`](../sources/prs/sglang/PR-21463.md) | Migrate all callers from /get_server_info to /server_info |
| `pr-sglang-21511` | upstream-code | [`sources/prs/sglang/PR-21511.md`](../sources/prs/sglang/PR-21511.md) | [AMD] Enable FP8 KV cache and FP8 attention kernel for NSA on MI300/MI355 with TileLang backend |
| `pr-sglang-21536` | upstream-code | [`sources/prs/sglang/PR-21536.md`](../sources/prs/sglang/PR-21536.md) | [Clean] Remove deprecated environs |
| `pr-sglang-21576` | upstream-code | [`sources/prs/sglang/PR-21576.md`](../sources/prs/sglang/PR-21576.md) | [FlashInver v0.6.7] Integrate flashinfer_trtllm mxfp8 gemm |
| `pr-sglang-21595` | upstream-code | [`sources/prs/sglang/PR-21595.md`](../sources/prs/sglang/PR-21595.md) | Change default mm-attention backend from triton_attn to fa4 |
| `pr-sglang-21649` | upstream-code | [`sources/prs/sglang/PR-21649.md`](../sources/prs/sglang/PR-21649.md) | fix: TRT-LLM MHA CUDA illegal address with EAGLE v2 + DP attention |
| `pr-sglang-21654` | upstream-code | [`sources/prs/sglang/PR-21654.md`](../sources/prs/sglang/PR-21654.md) | [jit_kernel] Optimize fused_qknorm_rope: deduplicate sincosf for interleave RoPE  |
| `pr-sglang-21710` | upstream-code | [`sources/prs/sglang/PR-21710.md`](../sources/prs/sglang/PR-21710.md) | [AMD] Add GLM-5-FP8 nightly performance benchmarks for MI30x and MI35x |
| `pr-sglang-21734` | upstream-code | [`sources/prs/sglang/PR-21734.md`](../sources/prs/sglang/PR-21734.md) | perf: optimize PCG inductor path for FP8 models |
| `pr-sglang-21776` | upstream-code | [`sources/prs/sglang/PR-21776.md`](../sources/prs/sglang/PR-21776.md) | Harden FlashInfer FP4 imports in standard dispatcher |
| `pr-sglang-21783` | upstream-code | [`sources/prs/sglang/PR-21783.md`](../sources/prs/sglang/PR-21783.md) | [DSA] Support trtllm sparse mla kernel for prefill batches  |
| `pr-sglang-21834` | upstream-code | [`sources/prs/sglang/PR-21834.md`](../sources/prs/sglang/PR-21834.md) | [Feature] JIT rmsnorm update (with claude) |
| `pr-sglang-21888` | upstream-code | [`sources/prs/sglang/PR-21888.md`](../sources/prs/sglang/PR-21888.md) | fix pcg torch dynamo recompile in mxfp8 Triton path |
| `pr-sglang-21906` | upstream-code | [`sources/prs/sglang/PR-21906.md`](../sources/prs/sglang/PR-21906.md) | [Bugfix] Temporarily skip TRTLLM attention on (G)B300 (SM103) to avoid high-concurrency hang |
| `pr-sglang-21921` | upstream-code | [`sources/prs/sglang/PR-21921.md`](../sources/prs/sglang/PR-21921.md) | Add staging buffer CI test and documentation for heterogeneous TP |
| `pr-sglang-21987` | upstream-code | [`sources/prs/sglang/PR-21987.md`](../sources/prs/sglang/PR-21987.md) | [Bugfix] Fix CUDA graph replay issues in trtllm_mla draft_extend |
| `pr-sglang-22006` | upstream-code | [`sources/prs/sglang/PR-22006.md`](../sources/prs/sglang/PR-22006.md) | Tiny fix trtllm_fp8_per_tensor_scale_moe_wrapper router_logits dtype |
| `pr-sglang-22024` | upstream-code | [`sources/prs/sglang/PR-22024.md`](../sources/prs/sglang/PR-22024.md) | [NPU] enable mla prepare fused kernel only when being mla attn |
| `pr-sglang-22051` | upstream-code | [`sources/prs/sglang/PR-22051.md`](../sources/prs/sglang/PR-22051.md) | [MUSA][9/N] Add FA3 attention backend support through MATE (MUSA AI Tensor Engine) |
| `pr-sglang-22064` | upstream-code | [`sources/prs/sglang/PR-22064.md`](../sources/prs/sglang/PR-22064.md) | [Diffusion] Fix weight scale swizzle and add large-M kernel config for FLUX.2-dev-NVFP4 |
| `pr-sglang-22079` | upstream-code | [`sources/prs/sglang/PR-22079.md`](../sources/prs/sglang/PR-22079.md) | [nvidia] Gemma4 nvfp4 fix |
| `pr-sglang-22091` | upstream-code | [`sources/prs/sglang/PR-22091.md`](../sources/prs/sglang/PR-22091.md) | [diffusion] Default NVFP4 to CUTLASS and add all-model shape benchmarks |
| `pr-sglang-22094` | upstream-code | [`sources/prs/sglang/PR-22094.md`](../sources/prs/sglang/PR-22094.md) | [JIT Kernel] Reland JIT activation |
| `pr-sglang-22127` | upstream-code | [`sources/prs/sglang/PR-22127.md`](../sources/prs/sglang/PR-22127.md) | [Diffusion] Add diffusion NVFP4 scaled-mm correctness test |
| `pr-sglang-22136` | upstream-code | [`sources/prs/sglang/PR-22136.md`](../sources/prs/sglang/PR-22136.md) | [CI] Lower GSM8K baselines for B200 nightly after eval unification |
| `pr-sglang-22187` | upstream-code | [`sources/prs/sglang/PR-22187.md`](../sources/prs/sglang/PR-22187.md) | [HiSparse]: Add benchmark for hisparse kernel |
| `pr-sglang-22204` | upstream-code | [`sources/prs/sglang/PR-22204.md`](../sources/prs/sglang/PR-22204.md) | [RL] Refactor NVFP4 shuffling/swizzling to in-place replacement |
| `pr-sglang-22218` | upstream-code | [`sources/prs/sglang/PR-22218.md`](../sources/prs/sglang/PR-22218.md) | [Experimental] Breakable Piecewise Cuda Graph |
| `pr-sglang-22232` | upstream-code | [`sources/prs/sglang/PR-22232.md`](../sources/prs/sglang/PR-22232.md) | Reduce unnecessary kernels and copies in the NSA indexer |
| `pr-sglang-22258` | upstream-code | [`sources/prs/sglang/PR-22258.md`](../sources/prs/sglang/PR-22258.md) | [AMD][HIP] NSA: bf16 passthrough from RMSNorm to eliminate FP8 dequantization |
| `pr-sglang-22316` | upstream-code | [`sources/prs/sglang/PR-22316.md`](../sources/prs/sglang/PR-22316.md) | [Reland] DeepSeek-R1-0528-w4a8: DeepEP Low Latency Dispatch Adopts FP8 Communication |
| `pr-sglang-22323` | upstream-code | [`sources/prs/sglang/PR-22323.md`](../sources/prs/sglang/PR-22323.md) | [Lora] Lora quat info re-factor and support deepseekv3 mla lora |
| `pr-sglang-22336` | upstream-code | [`sources/prs/sglang/PR-22336.md`](../sources/prs/sglang/PR-22336.md) | [AMD] Add GLM-5.1-FP8 nightly accuracy and performance benchmarks for MI30x and MI35x |
| `pr-sglang-22365` | upstream-code | [`sources/prs/sglang/PR-22365.md`](../sources/prs/sglang/PR-22365.md) | [Diffusion] modelopt diffusion fp8 support for flux1/flux2 and wan2.2 |
| `pr-sglang-22372` | upstream-code | [`sources/prs/sglang/PR-22372.md`](../sources/prs/sglang/PR-22372.md) | [DSA] Hopper FP8 FlashMLA KV padding |
| `pr-sglang-22381` | upstream-code | [`sources/prs/sglang/PR-22381.md`](../sources/prs/sglang/PR-22381.md) | [Lora] Lora kimi support |
| `pr-sglang-22424` | upstream-code | [`sources/prs/sglang/PR-22424.md`](../sources/prs/sglang/PR-22424.md) | [AMD] Use aiter CK layernorm2d for LayerNorm to reduce NSA indexer kernel launches |
| `pr-sglang-22430` | upstream-code | [`sources/prs/sglang/PR-22430.md`](../sources/prs/sglang/PR-22430.md) | [Fix] Fix several bugs on DSA models |
| `pr-sglang-22484` | upstream-code | [`sources/prs/sglang/PR-22484.md`](../sources/prs/sglang/PR-22484.md) | [RL] Fix weight update for mxfp8 flashinfer_cutlass gemm backend |
| `pr-sglang-22492` | upstream-code | [`sources/prs/sglang/PR-22492.md`](../sources/prs/sglang/PR-22492.md) | [diffusion] split ModelOpt FP8 skill and tools from runtime PR |
| `pr-sglang-22544` | upstream-code | [`sources/prs/sglang/PR-22544.md`](../sources/prs/sglang/PR-22544.md) | [Score API] Add Multi-Item Scoring with pre-computed delimiter indices |
| `pr-sglang-22574` | upstream-code | [`sources/prs/sglang/PR-22574.md`](../sources/prs/sglang/PR-22574.md) | [Diffusion] Add FLUX.1-dev ModelOpt NVFP4 support |
| `pr-sglang-22594` | upstream-code | [`sources/prs/sglang/PR-22594.md`](../sources/prs/sglang/PR-22594.md) | diffusion: fix layerwise offload for ModelOpt quantized DiTs |
| `pr-sglang-22626` | upstream-code | [`sources/prs/sglang/PR-22626.md`](../sources/prs/sglang/PR-22626.md) | [ROCm]fix(aiter): cast fp8 prefill output back to model dtype |
| `pr-sglang-22643` | upstream-code | [`sources/prs/sglang/PR-22643.md`](../sources/prs/sglang/PR-22643.md) | [sgl] update specdec sampling kernel to return valid token ID |
| `pr-sglang-22672` | upstream-code | [`sources/prs/sglang/PR-22672.md`](../sources/prs/sglang/PR-22672.md) | reland [Diffusion] Add FLUX.1-dev ModelOpt NVFP4 support |
| `pr-sglang-22681` | upstream-code | [`sources/prs/sglang/PR-22681.md`](../sources/prs/sglang/PR-22681.md) | [Diffusion] Add Wan2.2 ModelOpt NVFP4 support |
| `pr-sglang-22688` | upstream-code | [`sources/prs/sglang/PR-22688.md`](../sources/prs/sglang/PR-22688.md) | Fix trtllm mla chunked-prefill zero-length bug (#22291) |
| `pr-sglang-22717` | upstream-code | [`sources/prs/sglang/PR-22717.md`](../sources/prs/sglang/PR-22717.md) | [codex] Add flashinfer TRTLLM backend for diffusion NVFP4 |
| `pr-sglang-22722` | upstream-code | [`sources/prs/sglang/PR-22722.md`](../sources/prs/sglang/PR-22722.md) | [AMD] Add MiniMax-M2.7 accuracy and performance nightly tests |
| `pr-sglang-22772` | upstream-code | [`sources/prs/sglang/PR-22772.md`](../sources/prs/sglang/PR-22772.md) | [codex] Update modelopt quantization docs and CI coverage |
| `pr-sglang-22774` | upstream-code | [`sources/prs/sglang/PR-22774.md`](../sources/prs/sglang/PR-22774.md) | [MUSA][16/N] Add MUSA backend support for layers and DeepSeek models (V2/V3/R1) |
| `pr-sglang-22809` | upstream-code | [`sources/prs/sglang/PR-22809.md`](../sources/prs/sglang/PR-22809.md) | Dual MoE CUDA graph capture for lora/nolora batches |
| `pr-sglang-22814` | upstream-code | [`sources/prs/sglang/PR-22814.md`](../sources/prs/sglang/PR-22814.md) | diffusion: add HunyuanVideo GroupNorm+SiLU fast path |
| `pr-sglang-22869` | upstream-code | [`sources/prs/sglang/PR-22869.md`](../sources/prs/sglang/PR-22869.md) | [diffusion] feat: introduce ltx-2-two-stage device manager |
| `pr-sglang-22914` | upstream-code | [`sources/prs/sglang/PR-22914.md`](../sources/prs/sglang/PR-22914.md) | [Refactor] Deduplicate NSA utils.py into cp_utils.py for context parallel |
| `pr-sglang-22925` | upstream-code | [`sources/prs/sglang/PR-22925.md`](../sources/prs/sglang/PR-22925.md) | fix legacy deepep path for flashinfer_cutedsl |
| `pr-sglang-22931` | upstream-code | [`sources/prs/sglang/PR-22931.md`](../sources/prs/sglang/PR-22931.md) | [Fix/Kernel] Add JIT rmsnorm_hf kernel to fix transformers backend MMLU accuracy regression  |
| `pr-sglang-22955` | upstream-code | [`sources/prs/sglang/PR-22955.md`](../sources/prs/sglang/PR-22955.md) | [Diffusion] Fix ModelOpt B200 CI artifact coverage |
| `pr-sglang-23001` | upstream-code | [`sources/prs/sglang/PR-23001.md`](../sources/prs/sglang/PR-23001.md) | Add new Mintlify documentation site (docs_new/) |
| `pr-sglang-23065` | upstream-code | [`sources/prs/sglang/PR-23065.md`](../sources/prs/sglang/PR-23065.md) | sglang miles lora |
| `pr-sglang-23110` | upstream-code | [`sources/prs/sglang/PR-23110.md`](../sources/prs/sglang/PR-23110.md) | Clean up bench_one_batch warning and simplify norm dispatch |
| `pr-sglang-23148` | upstream-code | [`sources/prs/sglang/PR-23148.md`](../sources/prs/sglang/PR-23148.md) | [codex] diffusion: enable group norm silu fuse by default |
| `pr-sglang-23159` | upstream-code | [`sources/prs/sglang/PR-23159.md`](../sources/prs/sglang/PR-23159.md) | Revert "perf: optimize PCG inductor path for FP8 models (#21734)" |
| `pr-sglang-23178` | upstream-code | [`sources/prs/sglang/PR-23178.md`](../sources/prs/sglang/PR-23178.md) | [LoRA] Fix EP + per-expert MoE LoRA illegal memory access |
| `pr-sglang-23185` | upstream-code | [`sources/prs/sglang/PR-23185.md`](../sources/prs/sglang/PR-23185.md) | [Bugfix] Fix DeepEP timeout when compiling DeepGeMM in EP+DP+TP |
| `pr-sglang-23186` | upstream-code | [`sources/prs/sglang/PR-23186.md`](../sources/prs/sglang/PR-23186.md) | [AMD] Fused qk rmsnorm bf16 for amd/Kimi-K2.5-MXFP4 |
| `pr-sglang-23227` | upstream-code | [`sources/prs/sglang/PR-23227.md`](../sources/prs/sglang/PR-23227.md) | perf: optimize PCG inductor path for FP8 models (redo of #21734) |
| `pr-sglang-23319` | upstream-code | [`sources/prs/sglang/PR-23319.md`](../sources/prs/sglang/PR-23319.md) | [AMD] Use bpreshuffle FP8 blockscale GEMM to replace ABScale GEMM |
| `pr-sglang-23417` | upstream-code | [`sources/prs/sglang/PR-23417.md`](../sources/prs/sglang/PR-23417.md) | [ci] split stage-c-test-4-gpu-b200 to enable a low-disk runner pool |
| `pr-sglang-23454` | upstream-code | [`sources/prs/sglang/PR-23454.md`](../sources/prs/sglang/PR-23454.md) | [srt] Add Moss-VL Python runtime support |
| `pr-sglang-23467` | upstream-code | [`sources/prs/sglang/PR-23467.md`](../sources/prs/sglang/PR-23467.md) | fix: dot-boundary match in is_layer_skipped for FP8 modules_to_not_convert |
| `pr-sglang-23493` | upstream-code | [`sources/prs/sglang/PR-23493.md`](../sources/prs/sglang/PR-23493.md) | Skip unselected experts in flashinfer_trtllm |
| `pr-sglang-23590` | upstream-code | [`sources/prs/sglang/PR-23590.md`](../sources/prs/sglang/PR-23590.md) | Reland Cute-DSL FP4 dense GEMM |
| `pr-sglang-23620` | upstream-code | [`sources/prs/sglang/PR-23620.md`](../sources/prs/sglang/PR-23620.md) | [AMD] Optimize MiniMax-M2.5 - enable fused Triton kernel for FP8 KV cache write in aiter decode path |
| `pr-sglang-23671` | upstream-code | [`sources/prs/sglang/PR-23671.md`](../sources/prs/sglang/PR-23671.md) | [AMD][bugfix] add gate rocm >= 7.2 for bpreshuffle |
| `pr-sglang-23682` | upstream-code | [`sources/prs/sglang/PR-23682.md`](../sources/prs/sglang/PR-23682.md) | Add fused moe triton config for Qwen3.5-397B-A17B-FP8 |
| `pr-sglang-23686` | upstream-code | [`sources/prs/sglang/PR-23686.md`](../sources/prs/sglang/PR-23686.md) | Deepseek_v4 support w4(mxfp4)a16 on hopper |
| `pr-sglang-23699` | upstream-code | [`sources/prs/sglang/PR-23699.md`](../sources/prs/sglang/PR-23699.md) | [NSA] Fall back to fast_hadamard_transform when sgl_kernel lacks the symbol |
| `pr-sglang-23707` | upstream-code | [`sources/prs/sglang/PR-23707.md`](../sources/prs/sglang/PR-23707.md) | [MoE] Deprecate act_and_mul_triton; fold filter_expert into JIT silu/gelu_and_mul |
| `pr-sglang-23745` | upstream-code | [`sources/prs/sglang/PR-23745.md`](../sources/prs/sglang/PR-23745.md) | Use Cute-DSL NVFP4 quantization kernels |
| `pr-sglang-23748` | upstream-code | [`sources/prs/sglang/PR-23748.md`](../sources/prs/sglang/PR-23748.md) | refactor(moe): centralize post-experts all-reduce skip predicate |
| `pr-sglang-23756` | upstream-code | [`sources/prs/sglang/PR-23756.md`](../sources/prs/sglang/PR-23756.md) | feat: port SGLANG_JIT_DEEPGEMM_FAST_WARMUP to deepseek_v4 branch |
| `pr-sglang-23787` | upstream-code | [`sources/prs/sglang/PR-23787.md`](../sources/prs/sglang/PR-23787.md) | amd/deepseek_v4 integration 1/N - 0426 |
| `pr-sglang-23938` | upstream-code | [`sources/prs/sglang/PR-23938.md`](../sources/prs/sglang/PR-23938.md) | Optimize large GroupNorm SiLU apply |
| `pr-sglang-23965` | upstream-code | [`sources/prs/sglang/PR-23965.md`](../sources/prs/sglang/PR-23965.md) | Enable PDL for various kernels in DSV32/GLM5 |
| `pr-sglang-24048` | upstream-code | [`sources/prs/sglang/PR-24048.md`](../sources/prs/sglang/PR-24048.md) | [VLM] Optimize Gemma4 VLM with PCG and fuse RMSNorm + residual add + scalar |
| `pr-sglang-24197` | upstream-code | [`sources/prs/sglang/PR-24197.md`](../sources/prs/sglang/PR-24197.md) | Refactor device timer, clean up metrics collector, and add fwd occupancy metric |
| `pr-sglang-24271` | upstream-code | [`sources/prs/sglang/PR-24271.md`](../sources/prs/sglang/PR-24271.md) | [KDA] Optimize prefill kernels with diagonal and recompute fuse |
| `pr-sglang-24411` | upstream-code | [`sources/prs/sglang/PR-24411.md`](../sources/prs/sglang/PR-24411.md) | [diffusion] Fuse LTX2 split rotary embedding |
| `pr-sglang-24490` | upstream-code | [`sources/prs/sglang/PR-24490.md`](../sources/prs/sglang/PR-24490.md) | Port MXFP4 Marlin MoE support to JIT kernel path |
| `pr-sglang-24562` | upstream-code | [`sources/prs/sglang/PR-24562.md`](../sources/prs/sglang/PR-24562.md) | Fix performance regression on Deepseek V3 on `moe-runner-backend=triton` on SM90 |
| `pr-sglang-24696` | upstream-code | [`sources/prs/sglang/PR-24696.md`](../sources/prs/sglang/PR-24696.md) | [Gemma4] Optimize Gemm4 with fused Q/K/V RMSNorm + per-expert FP8 ckpt loader |
| `pr-sglang-24816` | upstream-code | [`sources/prs/sglang/PR-24816.md`](../sources/prs/sglang/PR-24816.md) | Add FlashInfer SM90 cutlass MXFP4 MoE backend (W4A16) for GPT-OSS + DeepSeek-V4 |
| `pr-sglang-24925` | upstream-code | [`sources/prs/sglang/PR-24925.md`](../sources/prs/sglang/PR-24925.md) | [attn backend] Integrate tokenspeed_mla prefill/decode kernels (fp8 kv cache, blackwell) |
| `pr-sglang-24986` | upstream-code | [`sources/prs/sglang/PR-24986.md`](../sources/prs/sglang/PR-24986.md) | [rebase]Deepseek_v4 support w4(mxfp4)a16 on hopper |
| `pr-sglang-25107` | upstream-code | [`sources/prs/sglang/PR-25107.md`](../sources/prs/sglang/PR-25107.md) | perf(nvfp4): free unused source scales after weight processing |
| `pr-sglang-2693` | upstream-code | [`sources/prs/sglang/PR-2693.md`](../sources/prs/sglang/PR-2693.md) | Hierarchical Caching for SGLang |
| `pr-sglang-2752` | upstream-code | [`sources/prs/sglang/PR-2752.md`](../sources/prs/sglang/PR-2752.md) | Support cutlass Int8 gemm |
| `pr-sglang-3033` | upstream-code | [`sources/prs/sglang/PR-3033.md`](../sources/prs/sglang/PR-3033.md) | feat: add flashinfer as 3rdparty and use rmsnorm as example |
| `pr-sglang-3035` | upstream-code | [`sources/prs/sglang/PR-3035.md`](../sources/prs/sglang/PR-3035.md) | Support sm90 Int8 gemm |
| `pr-sglang-3047` | upstream-code | [`sources/prs/sglang/PR-3047.md`](../sources/prs/sglang/PR-3047.md) | support w8a8 fp8 kernel with CUTLASS |
| `pr-sglang-3056` | upstream-code | [`sources/prs/sglang/PR-3056.md`](../sources/prs/sglang/PR-3056.md) | feat: integrate bmm_fp8 kernel into sgl-kernel |
| `pr-sglang-3148` | upstream-code | [`sources/prs/sglang/PR-3148.md`](../sources/prs/sglang/PR-3148.md) | Apply sgl w8a8 fp8 kernel |
| `pr-sglang-3161` | upstream-code | [`sources/prs/sglang/PR-3161.md`](../sources/prs/sglang/PR-3161.md) | [Feature] Define backends and add Triton backend for Lora |
| `pr-sglang-3216` | upstream-code | [`sources/prs/sglang/PR-3216.md`](../sources/prs/sglang/PR-3216.md) | add tensorrt_llm common and cutlass_extensions as 3rdparty |
| `pr-sglang-3267` | upstream-code | [`sources/prs/sglang/PR-3267.md`](../sources/prs/sglang/PR-3267.md) | support blockwise fp8 matmul kernel |
| `pr-sglang-3272` | upstream-code | [`sources/prs/sglang/PR-3272.md`](../sources/prs/sglang/PR-3272.md) | adding Triton configs for DeepSeekV3 on Blackwell |
| `pr-sglang-3529` | upstream-code | [`sources/prs/sglang/PR-3529.md`](../sources/prs/sglang/PR-3529.md) | integrate blockwise fp8 kernel |
| `pr-sglang-3550` | upstream-code | [`sources/prs/sglang/PR-3550.md`](../sources/prs/sglang/PR-3550.md) | feat: support flashinfer mla attention for deepseek v3 |
| `pr-sglang-3629` | upstream-code | [`sources/prs/sglang/PR-3629.md`](../sources/prs/sglang/PR-3629.md) | [Feature] Apply Cublas Grouped Gemm kernel |
| `pr-sglang-3643` | upstream-code | [`sources/prs/sglang/PR-3643.md`](../sources/prs/sglang/PR-3643.md) | feat: support flashinfer mla with prefix cache |
| `pr-sglang-3727` | upstream-code | [`sources/prs/sglang/PR-3727.md`](../sources/prs/sglang/PR-3727.md) | add control for cutlass fp8 blockwise gemm |
| `pr-sglang-3730` | upstream-code | [`sources/prs/sglang/PR-3730.md`](../sources/prs/sglang/PR-3730.md) | Feature DeepSeek V3/R1 INT8 Quantization (block-wise) |
| `pr-sglang-3785` | upstream-code | [`sources/prs/sglang/PR-3785.md`](../sources/prs/sglang/PR-3785.md) | Refactor flashinfer logic for deepseek v3 and fix accuracy bug |
| `pr-sglang-3888` | upstream-code | [`sources/prs/sglang/PR-3888.md`](../sources/prs/sglang/PR-3888.md) | [Feature] DeepSeek V3/R1 INT8 Quantization (channel-wise)  |
| `pr-sglang-3893` | upstream-code | [`sources/prs/sglang/PR-3893.md`](../sources/prs/sglang/PR-3893.md) | add deepgemm and sglang fp8 block-wise gemm benchmark |
| `pr-sglang-3899` | upstream-code | [`sources/prs/sglang/PR-3899.md`](../sources/prs/sglang/PR-3899.md) | Support FP4 gemm (1/2) |
| `pr-sglang-3963` | upstream-code | [`sources/prs/sglang/PR-3963.md`](../sources/prs/sglang/PR-3963.md) | Remove unused imports from rocm mla kernel.  |
| `pr-sglang-3967` | upstream-code | [`sources/prs/sglang/PR-3967.md`](../sources/prs/sglang/PR-3967.md) | [Feature]Support ragged prefill in flashinfer mla backend |
| `pr-sglang-3987` | upstream-code | [`sources/prs/sglang/PR-3987.md`](../sources/prs/sglang/PR-3987.md) | Add fast decode plan for flashinfer mla |
| `pr-sglang-3993` | upstream-code | [`sources/prs/sglang/PR-3993.md`](../sources/prs/sglang/PR-3993.md) | Add Benchmark for DeepGEMM Group GEMM |
| `pr-sglang-4012` | upstream-code | [`sources/prs/sglang/PR-4012.md`](../sources/prs/sglang/PR-4012.md) | [Revision] Add fast decode plan for flashinfer mla  |
| `pr-sglang-4014` | upstream-code | [`sources/prs/sglang/PR-4014.md`](../sources/prs/sglang/PR-4014.md) | Optimize Triton Kernel of Group GEMM in DeepGEMM Benchmark |
| `pr-sglang-4068` | upstream-code | [`sources/prs/sglang/PR-4068.md`](../sources/prs/sglang/PR-4068.md) | Support overlapping two batches |
| `pr-sglang-4147` | upstream-code | [`sources/prs/sglang/PR-4147.md`](../sources/prs/sglang/PR-4147.md) | Fix nightly ci Gsm8k & Fix flashinfer backend kvcache quant |
| `pr-sglang-4165` | upstream-code | [`sources/prs/sglang/PR-4165.md`](../sources/prs/sglang/PR-4165.md) | DeepGemm integrate to sgl-kernel |
| `pr-sglang-4178` | upstream-code | [`sources/prs/sglang/PR-4178.md`](../sources/prs/sglang/PR-4178.md) | ROCm: Flex Attention Enablement with custom backends |
| `pr-sglang-4199` | upstream-code | [`sources/prs/sglang/PR-4199.md`](../sources/prs/sglang/PR-4199.md) | linear support deepgemm |
| `pr-sglang-4215` | upstream-code | [`sources/prs/sglang/PR-4215.md`](../sources/prs/sglang/PR-4215.md) | Accelerate FP8 CUDA Kernel by 20-28% |
| `pr-sglang-4218` | upstream-code | [`sources/prs/sglang/PR-4218.md`](../sources/prs/sglang/PR-4218.md) | Support nextn for flashinfer mla attention backend |
| `pr-sglang-4230` | upstream-code | [`sources/prs/sglang/PR-4230.md`](../sources/prs/sglang/PR-4230.md) | Clean up fp8 support |
| `pr-sglang-4231` | upstream-code | [`sources/prs/sglang/PR-4231.md`](../sources/prs/sglang/PR-4231.md) | fix per_token_group_quant_fp8 illegal memory when num_groups % 16 != 0 |
| `pr-sglang-4232` | upstream-code | [`sources/prs/sglang/PR-4232.md`](../sources/prs/sglang/PR-4232.md) | [Feature] Integrate DeepEP into SGLang |
| `pr-sglang-4278` | upstream-code | [`sources/prs/sglang/PR-4278.md`](../sources/prs/sglang/PR-4278.md) | Support Blackwell Block Scale FP8 Gemm |
| `pr-sglang-4359` | upstream-code | [`sources/prs/sglang/PR-4359.md`](../sources/prs/sglang/PR-4359.md) | [FIX] fix incorrect output when enable both deepgemm and torch compile |
| `pr-sglang-4510` | upstream-code | [`sources/prs/sglang/PR-4510.md`](../sources/prs/sglang/PR-4510.md) | [ROCm] fix dtype |
| `pr-sglang-4514` | upstream-code | [`sources/prs/sglang/PR-4514.md`](../sources/prs/sglang/PR-4514.md) | Support FlashMLA backend cuda graph |
| `pr-sglang-4515` | upstream-code | [`sources/prs/sglang/PR-4515.md`](../sources/prs/sglang/PR-4515.md) | Create col-major and tma-aligned x_scale for deep_gemm.gemm_fp8_fp8_bf16_nt |
| `pr-sglang-4530` | upstream-code | [`sources/prs/sglang/PR-4530.md`](../sources/prs/sglang/PR-4530.md) | Add deepseek style fused moe group gate selection kernel |
| `pr-sglang-4557` | upstream-code | [`sources/prs/sglang/PR-4557.md`](../sources/prs/sglang/PR-4557.md) | [Fix] Fix raw_bs bug when using flashinfer mla and eagle |
| `pr-sglang-4558` | upstream-code | [`sources/prs/sglang/PR-4558.md`](../sources/prs/sglang/PR-4558.md) | Support fp8 gemm for blackwell |
| `pr-sglang-4596` | upstream-code | [`sources/prs/sglang/PR-4596.md`](../sources/prs/sglang/PR-4596.md) | [quantization] fix channelwise conversion with scalar weight scale |
| `pr-sglang-4605` | upstream-code | [`sources/prs/sglang/PR-4605.md`](../sources/prs/sglang/PR-4605.md) | rename benchmark_deepgemm_fp8_group_gemm.py |
| `pr-sglang-4613` | upstream-code | [`sources/prs/sglang/PR-4613.md`](../sources/prs/sglang/PR-4613.md) | Set deepgemm to the default value in the hopper architecture. |
| `pr-sglang-4640` | upstream-code | [`sources/prs/sglang/PR-4640.md`](../sources/prs/sglang/PR-4640.md) | fix SUPPORT_CUTLASS_BLOCK_FP8 flag |
| `pr-sglang-4643` | upstream-code | [`sources/prs/sglang/PR-4643.md`](../sources/prs/sglang/PR-4643.md) | Optimize Permute Kernel in DeepEP |
| `pr-sglang-4686` | upstream-code | [`sources/prs/sglang/PR-4686.md`](../sources/prs/sglang/PR-4686.md) | Fix loading KV quantization scale; Enable modelopt kv cache |
| `pr-sglang-4693` | upstream-code | [`sources/prs/sglang/PR-4693.md`](../sources/prs/sglang/PR-4693.md) | [Model] Adding Qwen3 and Qwen3MoE |
| `pr-sglang-4706` | upstream-code | [`sources/prs/sglang/PR-4706.md`](../sources/prs/sglang/PR-4706.md) | support cmake for sgl-kernel |
| `pr-sglang-4735` | upstream-code | [`sources/prs/sglang/PR-4735.md`](../sources/prs/sglang/PR-4735.md) | [Benchmark] tilelang vs deepgemm vs w8a8_block_fp8_matmul |
| `pr-sglang-4767` | upstream-code | [`sources/prs/sglang/PR-4767.md`](../sources/prs/sglang/PR-4767.md) | [Feature] Support DeepEP Low Latency |
| `pr-sglang-4770` | upstream-code | [`sources/prs/sglang/PR-4770.md`](../sources/prs/sglang/PR-4770.md) | Support (1 <= dp < tp) in the dp attention in DeepEP |
| `pr-sglang-4831` | upstream-code | [`sources/prs/sglang/PR-4831.md`](../sources/prs/sglang/PR-4831.md) | [Feature] Support FA3 backend for MLA |
| `pr-sglang-4880` | upstream-code | [`sources/prs/sglang/PR-4880.md`](../sources/prs/sglang/PR-4880.md) | [PD] Support KV transfer with mooncake |
| `pr-sglang-4887` | upstream-code | [`sources/prs/sglang/PR-4887.md`](../sources/prs/sglang/PR-4887.md) | Feat/support encoder model (like bert) |
| `pr-sglang-4918` | upstream-code | [`sources/prs/sglang/PR-4918.md`](../sources/prs/sglang/PR-4918.md) | Add DeepSeek V3/R1 shared experts fusion |
| `pr-sglang-4932` | upstream-code | [`sources/prs/sglang/PR-4932.md`](../sources/prs/sglang/PR-4932.md) | [Fix] avoid stream sync and torch compile in prefill for fa3 backend |
| `pr-sglang-4953` | upstream-code | [`sources/prs/sglang/PR-4953.md`](../sources/prs/sglang/PR-4953.md) | [Build] Fix cuda12.8 build error in nvfp4_scaled_mm_kernels.cu |
| `pr-sglang-5005` | upstream-code | [`sources/prs/sglang/PR-5005.md`](../sources/prs/sglang/PR-5005.md) | Replace enable_flashinfer_mla argument with attention_backend |
| `pr-sglang-5050` | upstream-code | [`sources/prs/sglang/PR-5050.md`](../sources/prs/sglang/PR-5050.md) | FA3 Spec Decoding to support top k = 1 and add cuda graph support |
| `pr-sglang-5052` | upstream-code | [`sources/prs/sglang/PR-5052.md`](../sources/prs/sglang/PR-5052.md) | [Revision] Replace enable_flashinfer_mla argument with attention_backend |
| `pr-sglang-5068` | upstream-code | [`sources/prs/sglang/PR-5068.md`](../sources/prs/sglang/PR-5068.md) | [Fix] DeepEP Compatibility with Low Latency |
| `pr-sglang-5086` | upstream-code | [`sources/prs/sglang/PR-5086.md`](../sources/prs/sglang/PR-5086.md) | reduce moe_align_block_size_kernel small batch mode overhead |
| `pr-sglang-5090` | upstream-code | [`sources/prs/sglang/PR-5090.md`](../sources/prs/sglang/PR-5090.md) | Refactor and Optimize FA3 Code |
| `pr-sglang-5113` | upstream-code | [`sources/prs/sglang/PR-5113.md`](../sources/prs/sglang/PR-5113.md) | Support MHA with chunked prefix cache for DeepSeek chunked prefill |
| `pr-sglang-5142` | upstream-code | [`sources/prs/sglang/PR-5142.md`](../sources/prs/sglang/PR-5142.md) | Blackwell Cutlass MLA kernel |
| `pr-sglang-5150` | upstream-code | [`sources/prs/sglang/PR-5150.md`](../sources/prs/sglang/PR-5150.md) | Add optimized native kernels in sgl-kernel |
| `pr-sglang-5176` | upstream-code | [`sources/prs/sglang/PR-5176.md`](../sources/prs/sglang/PR-5176.md) | feat: add DeepGEMM build warning |
| `pr-sglang-5207` | upstream-code | [`sources/prs/sglang/PR-5207.md`](../sources/prs/sglang/PR-5207.md) | sgl-kernel use cutlass latest version for fp8 blockwise gemm |
| `pr-sglang-5210` | upstream-code | [`sources/prs/sglang/PR-5210.md`](../sources/prs/sglang/PR-5210.md) | feat: use fa3 mla by default on hopper |
| `pr-sglang-5263` | upstream-code | [`sources/prs/sglang/PR-5263.md`](../sources/prs/sglang/PR-5263.md) | [Fix] Turn off DeepGEMM by default |
| `pr-sglang-5281` | upstream-code | [`sources/prs/sglang/PR-5281.md`](../sources/prs/sglang/PR-5281.md) | [1/2] Add FP8 Blockscale MoE CUTLASS kernel for Blackwell |
| `pr-sglang-5310` | upstream-code | [`sources/prs/sglang/PR-5310.md`](../sources/prs/sglang/PR-5310.md) | fix: use deepgemm only on hopper |
| `pr-sglang-5318` | upstream-code | [`sources/prs/sglang/PR-5318.md`](../sources/prs/sglang/PR-5318.md) | Add Speculative Decoding Eagle3 topk > 1 |
| `pr-sglang-5331` | upstream-code | [`sources/prs/sglang/PR-5331.md`](../sources/prs/sglang/PR-5331.md) | fix: solve cu118 issue for cutlass mla |
| `pr-sglang-5340` | upstream-code | [`sources/prs/sglang/PR-5340.md`](../sources/prs/sglang/PR-5340.md) | Fix DeepGEMM masked cannot be run on groups not being multiple or 4 |
| `pr-sglang-5370` | upstream-code | [`sources/prs/sglang/PR-5370.md`](../sources/prs/sglang/PR-5370.md) | [perf] experimental enhance fp8 per-tensor quant |
| `pr-sglang-5371` | upstream-code | [`sources/prs/sglang/PR-5371.md`](../sources/prs/sglang/PR-5371.md) | apply fused moe gate in ds v3/r1 |
| `pr-sglang-5390` | upstream-code | [`sources/prs/sglang/PR-5390.md`](../sources/prs/sglang/PR-5390.md) | Add Cutlass MLA attention backend |
| `pr-sglang-5415` | upstream-code | [`sources/prs/sglang/PR-5415.md`](../sources/prs/sglang/PR-5415.md) | [PD] Fix dynamic port support and MLA buffer for Mooncake |
| `pr-sglang-5417` | upstream-code | [`sources/prs/sglang/PR-5417.md`](../sources/prs/sglang/PR-5417.md) | [Feat] upgrade pytorch2.6 |
| `pr-sglang-5419` | upstream-code | [`sources/prs/sglang/PR-5419.md`](../sources/prs/sglang/PR-5419.md) | bugfix: fix merge_state_v2 cuda graph |
| `pr-sglang-5428` | upstream-code | [`sources/prs/sglang/PR-5428.md`](../sources/prs/sglang/PR-5428.md) | feat: Add a unified merge_state API |
| `pr-sglang-5431` | upstream-code | [`sources/prs/sglang/PR-5431.md`](../sources/prs/sglang/PR-5431.md) | BLackwell cutlass mla: Add check for bad page size/block num combinations |
| `pr-sglang-5432` | upstream-code | [`sources/prs/sglang/PR-5432.md`](../sources/prs/sglang/PR-5432.md) | [perf] introduce deep gemm group_gemm_masked as bmm |
| `pr-sglang-5476` | upstream-code | [`sources/prs/sglang/PR-5476.md`](../sources/prs/sglang/PR-5476.md) | Avoid computing lse in Ragged Prefill when there's no prefix. |
| `pr-sglang-5480` | upstream-code | [`sources/prs/sglang/PR-5480.md`](../sources/prs/sglang/PR-5480.md) | Deprecate enable-flashinfer-mla and enable-flashmla |
| `pr-sglang-5481` | upstream-code | [`sources/prs/sglang/PR-5481.md`](../sources/prs/sglang/PR-5481.md) | Deprecate disable-mla |
| `pr-sglang-5500` | upstream-code | [`sources/prs/sglang/PR-5500.md`](../sources/prs/sglang/PR-5500.md) | [Feat] Update sgl-kernel flashinfer to latest main version |
| `pr-sglang-5546` | upstream-code | [`sources/prs/sglang/PR-5546.md`](../sources/prs/sglang/PR-5546.md) | Fix sampler nan check when calling top_k_top_p_sampling_from_probs |
| `pr-sglang-5549` | upstream-code | [`sources/prs/sglang/PR-5549.md`](../sources/prs/sglang/PR-5549.md) | Remove one kernel in per_tensor_quant_mla_fp8 |
| `pr-sglang-5580` | upstream-code | [`sources/prs/sglang/PR-5580.md`](../sources/prs/sglang/PR-5580.md) | [feature] enable pre compile jit deep_gemm |
| `pr-sglang-5587` | upstream-code | [`sources/prs/sglang/PR-5587.md`](../sources/prs/sglang/PR-5587.md) | [Test] Add flashmla attention backend test |
| `pr-sglang-5618` | upstream-code | [`sources/prs/sglang/PR-5618.md`](../sources/prs/sglang/PR-5618.md) | [fix] force use deepgemm in compile_deep_gemm |
| `pr-sglang-5626` | upstream-code | [`sources/prs/sglang/PR-5626.md`](../sources/prs/sglang/PR-5626.md) |  DeepEP normal support deepgemm-contiguous |
| `pr-sglang-5628` | upstream-code | [`sources/prs/sglang/PR-5628.md`](../sources/prs/sglang/PR-5628.md) | Turn on DeepGemm By Default and Update Doc |
| `pr-sglang-5634` | upstream-code | [`sources/prs/sglang/PR-5634.md`](../sources/prs/sglang/PR-5634.md) | [fix] reduce dp capture bs |
| `pr-sglang-5662` | upstream-code | [`sources/prs/sglang/PR-5662.md`](../sources/prs/sglang/PR-5662.md) | [perf] dsv3 bmm fallback to bf16 |
| `pr-sglang-5694` | upstream-code | [`sources/prs/sglang/PR-5694.md`](../sources/prs/sglang/PR-5694.md) | [2/2] Add python wrapper for CUTLASS FP8 Blockscale MoE Kernel.  |
| `pr-sglang-5716` | upstream-code | [`sources/prs/sglang/PR-5716.md`](../sources/prs/sglang/PR-5716.md) | perf: update H20 fused_moe_triton kernel config to get higher throughput during prefilling |
| `pr-sglang-5724` | upstream-code | [`sources/prs/sglang/PR-5724.md`](../sources/prs/sglang/PR-5724.md) | [PP] Add pipeline parallelism |
| `pr-sglang-5726` | upstream-code | [`sources/prs/sglang/PR-5726.md`](../sources/prs/sglang/PR-5726.md) | [PD] support pd fake transfer for warmup |
| `pr-sglang-5740` | upstream-code | [`sources/prs/sglang/PR-5740.md`](../sources/prs/sglang/PR-5740.md) | update triton 3.2.0 h200 fused moe triton config and add warning about triton fused_moe_kernel performance degradation due to different Triton versions. |
| `pr-sglang-5748` | upstream-code | [`sources/prs/sglang/PR-5748.md`](../sources/prs/sglang/PR-5748.md) | Fuse MLA set kv cache kernel |
| `pr-sglang-5801` | upstream-code | [`sources/prs/sglang/PR-5801.md`](../sources/prs/sglang/PR-5801.md) | simplify fused_moe config logging |
| `pr-sglang-5820` | upstream-code | [`sources/prs/sglang/PR-5820.md`](../sources/prs/sglang/PR-5820.md) | cutlass 3.9 supported to improve fp8_blockwise_gemm |
| `pr-sglang-5822` | upstream-code | [`sources/prs/sglang/PR-5822.md`](../sources/prs/sglang/PR-5822.md) | opt flashinfer mla cat |
| `pr-sglang-5833` | upstream-code | [`sources/prs/sglang/PR-5833.md`](../sources/prs/sglang/PR-5833.md) | feat: Add fused moe triton config for qwen3 moe on h100 |
| `pr-sglang-5839` | upstream-code | [`sources/prs/sglang/PR-5839.md`](../sources/prs/sglang/PR-5839.md) | feat: Add fused moe triton config for qwen3bf16 moe on h20 |
| `pr-sglang-5850` | upstream-code | [`sources/prs/sglang/PR-5850.md`](../sources/prs/sglang/PR-5850.md) | feat: Add fused moe triton config for qwen3-30b-fp8 moe on h20 |
| `pr-sglang-5859` | upstream-code | [`sources/prs/sglang/PR-5859.md`](../sources/prs/sglang/PR-5859.md) | Add qwen3 30b fused moe config |
| `pr-sglang-5868` | upstream-code | [`sources/prs/sglang/PR-5868.md`](../sources/prs/sglang/PR-5868.md) | Cutlass MLA decode - fix dtype error |
| `pr-sglang-5875` | upstream-code | [`sources/prs/sglang/PR-5875.md`](../sources/prs/sglang/PR-5875.md) | [Fix] Fix a bug for flashmla to run R1 model |
| `pr-sglang-5893` | upstream-code | [`sources/prs/sglang/PR-5893.md`](../sources/prs/sglang/PR-5893.md) | [fix] relax mem_fraction_static for h200 |
| `pr-sglang-5900` | upstream-code | [`sources/prs/sglang/PR-5900.md`](../sources/prs/sglang/PR-5900.md) | Add A800 fused moe config for qwen3 235b |
| `pr-sglang-5909` | upstream-code | [`sources/prs/sglang/PR-5909.md`](../sources/prs/sglang/PR-5909.md) | Add TP2 MOE benchmarks for AMD. |
| `pr-sglang-5922` | upstream-code | [`sources/prs/sglang/PR-5922.md`](../sources/prs/sglang/PR-5922.md) | [PD] Add support for different TP sizes per DP rank |
| `pr-sglang-5992` | upstream-code | [`sources/prs/sglang/PR-5992.md`](../sources/prs/sglang/PR-5992.md) | [Fix] Suppress dynamo logging when using flashinfer backend with torch compile |
| `pr-sglang-6004` | upstream-code | [`sources/prs/sglang/PR-6004.md`](../sources/prs/sglang/PR-6004.md) | chore: upgrade cutlass 3.9.2 |
| `pr-sglang-6042` | upstream-code | [`sources/prs/sglang/PR-6042.md`](../sources/prs/sglang/PR-6042.md) | Support tuning moe for llama 4 model |
| `pr-sglang-6081` | upstream-code | [`sources/prs/sglang/PR-6081.md`](../sources/prs/sglang/PR-6081.md) | feat: mtp support dp-attention |
| `pr-sglang-6093` | upstream-code | [`sources/prs/sglang/PR-6093.md`](../sources/prs/sglang/PR-6093.md) | [1/2] Add Kernel support for Cutlass based Fused FP4 MoE |
| `pr-sglang-6101` | upstream-code | [`sources/prs/sglang/PR-6101.md`](../sources/prs/sglang/PR-6101.md) | Cutlass MLA: Disable split kv due to https://github.com/NVIDIA/cutlass/issues/2274 |
| `pr-sglang-6106` | upstream-code | [`sources/prs/sglang/PR-6106.md`](../sources/prs/sglang/PR-6106.md) | Support VILA models |
| `pr-sglang-6109` | upstream-code | [`sources/prs/sglang/PR-6109.md`](../sources/prs/sglang/PR-6109.md) | [Feat] Support FlashMLA backend with MTP and FP8 KV cache |
| `pr-sglang-6111` | upstream-code | [`sources/prs/sglang/PR-6111.md`](../sources/prs/sglang/PR-6111.md) | adding Triton configs for DeepSeekV3 FusedMoE kernel on Blackwell |
| `pr-sglang-6147` | upstream-code | [`sources/prs/sglang/PR-6147.md`](../sources/prs/sglang/PR-6147.md) | Reduce MoE memory usage |
| `pr-sglang-6226` | upstream-code | [`sources/prs/sglang/PR-6226.md`](../sources/prs/sglang/PR-6226.md) | enable auto-round quantization model |
| `pr-sglang-6230` | upstream-code | [`sources/prs/sglang/PR-6230.md`](../sources/prs/sglang/PR-6230.md) | Enable FlashInfer support encoder models and add head_dim padding workaround |
| `pr-sglang-6260` | upstream-code | [`sources/prs/sglang/PR-6260.md`](../sources/prs/sglang/PR-6260.md) | fix log_info_on_rank0 error when run benchmark |
| `pr-sglang-6295` | upstream-code | [`sources/prs/sglang/PR-6295.md`](../sources/prs/sglang/PR-6295.md) | fix: enable multi-GPU Triton fused MoE tuning |
| `pr-sglang-6336` | upstream-code | [`sources/prs/sglang/PR-6336.md`](../sources/prs/sglang/PR-6336.md) | Upgrade  CUTLASS 4.0 |
| `pr-sglang-6338` | upstream-code | [`sources/prs/sglang/PR-6338.md`](../sources/prs/sglang/PR-6338.md) | [feat] Support different attention backends for prefill and decode  |
| `pr-sglang-6369` | upstream-code | [`sources/prs/sglang/PR-6369.md`](../sources/prs/sglang/PR-6369.md) | reduce torch.zeros overhead in moe align block size kernel |
| `pr-sglang-6389` | upstream-code | [`sources/prs/sglang/PR-6389.md`](../sources/prs/sglang/PR-6389.md) | [Feature] Comprehensive Hybrid Parallelism Support |
| `pr-sglang-6404` | upstream-code | [`sources/prs/sglang/PR-6404.md`](../sources/prs/sglang/PR-6404.md) | Add fp8 fused_experts kernel for CPU in sgl-kernel and add UT |
| `pr-sglang-6449` | upstream-code | [`sources/prs/sglang/PR-6449.md`](../sources/prs/sglang/PR-6449.md) | Fix bug of deepseek-v3 under DP+EP mode with large batchsize/seqlen |
| `pr-sglang-6474` | upstream-code | [`sources/prs/sglang/PR-6474.md`](../sources/prs/sglang/PR-6474.md) | Fix topk inference performance reduce |
| `pr-sglang-6479` | upstream-code | [`sources/prs/sglang/PR-6479.md`](../sources/prs/sglang/PR-6479.md) | [Feature] Support Flashinfer fp8 blockwise GEMM kernel on Blackwell |
| `pr-sglang-6509` | upstream-code | [`sources/prs/sglang/PR-6509.md`](../sources/prs/sglang/PR-6509.md) | Support sliding window in triton backend |
| `pr-sglang-6545` | upstream-code | [`sources/prs/sglang/PR-6545.md`](../sources/prs/sglang/PR-6545.md) | refactor apply_w8a8_block_fp8_linear in fp |
| `pr-sglang-6627` | upstream-code | [`sources/prs/sglang/PR-6627.md`](../sources/prs/sglang/PR-6627.md) | Refine pre_reorder_triton_kernel slightly to improve performance |
| `pr-sglang-6641` | upstream-code | [`sources/prs/sglang/PR-6641.md`](../sources/prs/sglang/PR-6641.md) | [CPU] [BF16] Call fused_experts_cpu, weight_packed_linear and bmm_cpu kernel in DeepSeek model |
| `pr-sglang-6673` | upstream-code | [`sources/prs/sglang/PR-6673.md`](../sources/prs/sglang/PR-6673.md) | Fix DeepEP error in Qwen 3 MoE models |
| `pr-sglang-6699` | upstream-code | [`sources/prs/sglang/PR-6699.md`](../sources/prs/sglang/PR-6699.md) | [EP] Add cuda kernel for moe_ep_pre_reorder |
| `pr-sglang-6735` | upstream-code | [`sources/prs/sglang/PR-6735.md`](../sources/prs/sglang/PR-6735.md) | [Refactor] Rename `n_share_experts_fusion` as `num_fused_shared_experts` |
| `pr-sglang-6736` | upstream-code | [`sources/prs/sglang/PR-6736.md`](../sources/prs/sglang/PR-6736.md) | Set `num_fused_shared_experts` as `num_shared_experts` when shared_experts fusion is not disabled |
| `pr-sglang-6769` | upstream-code | [`sources/prs/sglang/PR-6769.md`](../sources/prs/sglang/PR-6769.md) | [CPU] add optimizations for INT8 and FP8 DeepSeek |
| `pr-sglang-6771` | upstream-code | [`sources/prs/sglang/PR-6771.md`](../sources/prs/sglang/PR-6771.md) | [CPU] support the case where num_attention_heads or intermediate_size is not divisible by the TP size |
| `pr-sglang-6782` | upstream-code | [`sources/prs/sglang/PR-6782.md`](../sources/prs/sglang/PR-6782.md) | Support token-level quantization for EP MoE |
| `pr-sglang-6793` | upstream-code | [`sources/prs/sglang/PR-6793.md`](../sources/prs/sglang/PR-6793.md) | [PD] Add different TP sizes support for no-MLA models |
| `pr-sglang-6803` | upstream-code | [`sources/prs/sglang/PR-6803.md`](../sources/prs/sglang/PR-6803.md) | Correctly abort the failed grammar requests & Improve the handling of abort |
| `pr-sglang-6804` | upstream-code | [`sources/prs/sglang/PR-6804.md`](../sources/prs/sglang/PR-6804.md) | Remove contiguous before Flashinfer groupwise fp8 gemm |
| `pr-sglang-6805` | upstream-code | [`sources/prs/sglang/PR-6805.md`](../sources/prs/sglang/PR-6805.md) | Add draft extend CUDA graph for flashinfer backend  |
| `pr-sglang-6821` | upstream-code | [`sources/prs/sglang/PR-6821.md`](../sources/prs/sglang/PR-6821.md) | feat: integrate deepgemm into EPMoE |
| `pr-sglang-6833` | upstream-code | [`sources/prs/sglang/PR-6833.md`](../sources/prs/sglang/PR-6833.md) | CPU: map changes from developing branch in sgl-kernel |
| `pr-sglang-6837` | upstream-code | [`sources/prs/sglang/PR-6837.md`](../sources/prs/sglang/PR-6837.md) | [EP] Add cuda kernel for moe_ep_post_reorder |
| `pr-sglang-6838` | upstream-code | [`sources/prs/sglang/PR-6838.md`](../sources/prs/sglang/PR-6838.md) | AITER backend extension and workload optimizations |
| `pr-sglang-6842` | upstream-code | [`sources/prs/sglang/PR-6842.md`](../sources/prs/sglang/PR-6842.md) | Fix AWQ Dequant and Weight Loading of deepseek v2 |
| `pr-sglang-6853` | upstream-code | [`sources/prs/sglang/PR-6853.md`](../sources/prs/sglang/PR-6853.md) | [DeepseekR1-FP4] Add Support for nvidia/DeepSeekR1-FP4 model |
| `pr-sglang-6858` | upstream-code | [`sources/prs/sglang/PR-6858.md`](../sources/prs/sglang/PR-6858.md) | fix ep_moe_reorder kernel bugs |
| `pr-sglang-6885` | upstream-code | [`sources/prs/sglang/PR-6885.md`](../sources/prs/sglang/PR-6885.md) | Add H20 fused MoE kernel tuning configs for DeepSeek-R1/V3 |
| `pr-sglang-6890` | upstream-code | [`sources/prs/sglang/PR-6890.md`](../sources/prs/sglang/PR-6890.md) | Use deepgemm instead of triton for fused_qkv_a_proj_with_mqa |
| `pr-sglang-6916` | upstream-code | [`sources/prs/sglang/PR-6916.md`](../sources/prs/sglang/PR-6916.md) | Add a CUDA kernel for fusing mapping and weighted sum for MoE. |
| `pr-sglang-6919` | upstream-code | [`sources/prs/sglang/PR-6919.md`](../sources/prs/sglang/PR-6919.md) | [sgl-kernel] Add cuda kernel for moe_ep_silu_and_mul |
| `pr-sglang-6924` | upstream-code | [`sources/prs/sglang/PR-6924.md`](../sources/prs/sglang/PR-6924.md) | add fbgemm moe grouped gemm kernel benchmark |
| `pr-sglang-6929` | upstream-code | [`sources/prs/sglang/PR-6929.md`](../sources/prs/sglang/PR-6929.md) | [perf][sgl-kernel] extend cutlass_mla_decode to support num_head < 128 |
| `pr-sglang-6930` | upstream-code | [`sources/prs/sglang/PR-6930.md`](../sources/prs/sglang/PR-6930.md) | [Feature] Support Flashinfer fmha on Blackwell |
| `pr-sglang-6939` | upstream-code | [`sources/prs/sglang/PR-6939.md`](../sources/prs/sglang/PR-6939.md) | Add triton fused moe kernel config for E=257 on B200 |
| `pr-sglang-6956` | upstream-code | [`sources/prs/sglang/PR-6956.md`](../sources/prs/sglang/PR-6956.md) | Slightly improve the sampler to skip unnecessary steps |
| `pr-sglang-6958` | upstream-code | [`sources/prs/sglang/PR-6958.md`](../sources/prs/sglang/PR-6958.md) | chore: upgrade flashinfer v0.2.6.post1 jit |
| `pr-sglang-6965` | upstream-code | [`sources/prs/sglang/PR-6965.md`](../sources/prs/sglang/PR-6965.md) | Remove unnecessary kernels of num_token_non_padded |
| `pr-sglang-6966` | upstream-code | [`sources/prs/sglang/PR-6966.md`](../sources/prs/sglang/PR-6966.md) | rebase h20 fused_moe config |
| `pr-sglang-6970` | upstream-code | [`sources/prs/sglang/PR-6970.md`](../sources/prs/sglang/PR-6970.md) | Fuse routed scaling factor in deepseek |
| `pr-sglang-6974` | upstream-code | [`sources/prs/sglang/PR-6974.md`](../sources/prs/sglang/PR-6974.md) | Fix CI and triton moe Configs |
| `pr-sglang-6998` | upstream-code | [`sources/prs/sglang/PR-6998.md`](../sources/prs/sglang/PR-6998.md) | Fix cutlass MLA gets almost zero accuracy |
| `pr-sglang-7004` | upstream-code | [`sources/prs/sglang/PR-7004.md`](../sources/prs/sglang/PR-7004.md) | Add Triton Fused MoE kernel config for E=16 on B200 |
| `pr-sglang-7013` | upstream-code | [`sources/prs/sglang/PR-7013.md`](../sources/prs/sglang/PR-7013.md) | Fallback to lower triton version for unfound fused moe configs |
| `pr-sglang-7020` | upstream-code | [`sources/prs/sglang/PR-7020.md`](../sources/prs/sglang/PR-7020.md) | Remove 200us slow concat kernel (part 2: srt) |
| `pr-sglang-7021` | upstream-code | [`sources/prs/sglang/PR-7021.md`](../sources/prs/sglang/PR-7021.md) | [WA] fix output data is nan in CI test "test_moe_eval_accuracy_large.py" |
| `pr-sglang-7023` | upstream-code | [`sources/prs/sglang/PR-7023.md`](../sources/prs/sglang/PR-7023.md) | Update default settings for blackwell |
| `pr-sglang-7037` | upstream-code | [`sources/prs/sglang/PR-7037.md`](../sources/prs/sglang/PR-7037.md) | Clean up server_args.py |
| `pr-sglang-7057` | upstream-code | [`sources/prs/sglang/PR-7057.md`](../sources/prs/sglang/PR-7057.md) | Tiny fix cutlass_mla_get_workspace_size stub incorrect signature |
| `pr-sglang-7093` | upstream-code | [`sources/prs/sglang/PR-7093.md`](../sources/prs/sglang/PR-7093.md) | Fix positional argument |
| `pr-sglang-7119` | upstream-code | [`sources/prs/sglang/PR-7119.md`](../sources/prs/sglang/PR-7119.md) | feat: update blackwell setup |
| `pr-sglang-7125` | upstream-code | [`sources/prs/sglang/PR-7125.md`](../sources/prs/sglang/PR-7125.md) | fix amd EP MoE FP8 issue |
| `pr-sglang-7129` | upstream-code | [`sources/prs/sglang/PR-7129.md`](../sources/prs/sglang/PR-7129.md) | Enable ModelOpt Llama4 fp8 checkpoint deployment in SGLang |
| `pr-sglang-7145` | upstream-code | [`sources/prs/sglang/PR-7145.md`](../sources/prs/sglang/PR-7145.md) | Remove 200us slow concat kernel (part 1: kernel) |
| `pr-sglang-7148` | upstream-code | [`sources/prs/sglang/PR-7148.md`](../sources/prs/sglang/PR-7148.md) | Fix FP8 KV Cache Support in FA3 Backend |
| `pr-sglang-7149` | upstream-code | [`sources/prs/sglang/PR-7149.md`](../sources/prs/sglang/PR-7149.md) | Enable native ModelOpt quantization support (1/3)  |
| `pr-sglang-7150` | upstream-code | [`sources/prs/sglang/PR-7150.md`](../sources/prs/sglang/PR-7150.md) | Refactor DeepGEMM integration |
| `pr-sglang-7160` | upstream-code | [`sources/prs/sglang/PR-7160.md`](../sources/prs/sglang/PR-7160.md) | [amd] Opt dsv3 moe |
| `pr-sglang-7163` | upstream-code | [`sources/prs/sglang/PR-7163.md`](../sources/prs/sglang/PR-7163.md) | [EAGLE] Refactor code for page size > 1 & more simplifications |
| `pr-sglang-7172` | upstream-code | [`sources/prs/sglang/PR-7172.md`](../sources/prs/sglang/PR-7172.md) | Support new DeepGEMM |
| `pr-sglang-7182` | upstream-code | [`sources/prs/sglang/PR-7182.md`](../sources/prs/sglang/PR-7182.md) | Tiny let DeepGEMM scale checks cover more cases |
| `pr-sglang-7184` | upstream-code | [`sources/prs/sglang/PR-7184.md`](../sources/prs/sglang/PR-7184.md) | [fix] fix cutlass_mla_backend with cuda_graph and add sm_scale for sgl-kernel cutlass_mla |
| `pr-sglang-7186` | upstream-code | [`sources/prs/sglang/PR-7186.md`](../sources/prs/sglang/PR-7186.md) | chore: upgrade sgl-kernel v0.1.8.post2 |
| `pr-sglang-7187` | upstream-code | [`sources/prs/sglang/PR-7187.md`](../sources/prs/sglang/PR-7187.md) | [AMD] Fail gracefully when AITER is unavailable gfx90a GPUs |
| `pr-sglang-7191` | upstream-code | [`sources/prs/sglang/PR-7191.md`](../sources/prs/sglang/PR-7191.md) | Fix a minor bug related to DeepGEMM upgrade |
| `pr-sglang-7198` | upstream-code | [`sources/prs/sglang/PR-7198.md`](../sources/prs/sglang/PR-7198.md) | Fix error when disabling new DeepGEMM |
| `pr-sglang-7204` | upstream-code | [`sources/prs/sglang/PR-7204.md`](../sources/prs/sglang/PR-7204.md) | Fix grammar abort & Minor style fixes |
| `pr-sglang-7213` | upstream-code | [`sources/prs/sglang/PR-7213.md`](../sources/prs/sglang/PR-7213.md) | [EAGLE] Refactor code for page size > 1 & more simplifications |
| `pr-sglang-7221` | upstream-code | [`sources/prs/sglang/PR-7221.md`](../sources/prs/sglang/PR-7221.md) | refine fused_moe benchmark |
| `pr-sglang-7225` | upstream-code | [`sources/prs/sglang/PR-7225.md`](../sources/prs/sglang/PR-7225.md) | feat: support compatibility between MTP and two-batch-overlap |
| `pr-sglang-7228` | upstream-code | [`sources/prs/sglang/PR-7228.md`](../sources/prs/sglang/PR-7228.md) | Minor style and doc fix |
| `pr-sglang-7233` | upstream-code | [`sources/prs/sglang/PR-7233.md`](../sources/prs/sglang/PR-7233.md) | Use seq_len_fill_value in the cuda graph runners |
| `pr-sglang-7247` | upstream-code | [`sources/prs/sglang/PR-7247.md`](../sources/prs/sglang/PR-7247.md) | [fix] fix DeepGEMM blackwell input quant & ut & fix style and log |
| `pr-sglang-7268` | upstream-code | [`sources/prs/sglang/PR-7268.md`](../sources/prs/sglang/PR-7268.md) | [AMD] add aiter fused moe in DeepEP path |
| `pr-sglang-7278` | upstream-code | [`sources/prs/sglang/PR-7278.md`](../sources/prs/sglang/PR-7278.md) | Add CUTLASS FP8 Blockscale MoE kernel for Hopper architecture |
| `pr-sglang-7279` | upstream-code | [`sources/prs/sglang/PR-7279.md`](../sources/prs/sglang/PR-7279.md) | refine aiter_backend for mtp |
| `pr-sglang-7302` | upstream-code | [`sources/prs/sglang/PR-7302.md`](../sources/prs/sglang/PR-7302.md) | Support NVFP4 quantized dense models on AMD CDNA2/CDNA3 GPUs |
| `pr-sglang-7310` | upstream-code | [`sources/prs/sglang/PR-7310.md`](../sources/prs/sglang/PR-7310.md) | Let EP prefill support new DeepGEMM |
| `pr-sglang-7327` | upstream-code | [`sources/prs/sglang/PR-7327.md`](../sources/prs/sglang/PR-7327.md) | FlashInfer NVFP4 MoE with EP & 2-stream shared expert |
| `pr-sglang-7376` | upstream-code | [`sources/prs/sglang/PR-7376.md`](../sources/prs/sglang/PR-7376.md) | Fix MTP with Deepseek R1 Fp4 |
| `pr-sglang-7382` | upstream-code | [`sources/prs/sglang/PR-7382.md`](../sources/prs/sglang/PR-7382.md) | kvcache io kernels and test case |
| `pr-sglang-7391` | upstream-code | [`sources/prs/sglang/PR-7391.md`](../sources/prs/sglang/PR-7391.md) | Fix torch compile run |
| `pr-sglang-7392` | upstream-code | [`sources/prs/sglang/PR-7392.md`](../sources/prs/sglang/PR-7392.md) | [AMD][Quantization] Add `int4fp8_moe` online quantization on ROCm |
| `pr-sglang-7422` | upstream-code | [`sources/prs/sglang/PR-7422.md`](../sources/prs/sglang/PR-7422.md) | [benchmark] fbgemm benchmark support bandwidth report and support fbgemm_cutlass_gmm |
| `pr-sglang-7437` | upstream-code | [`sources/prs/sglang/PR-7437.md`](../sources/prs/sglang/PR-7437.md) | Fuse sorted_token_ids padding to moe_align_block_size kernel |
| `pr-sglang-7444` | upstream-code | [`sources/prs/sglang/PR-7444.md`](../sources/prs/sglang/PR-7444.md) | fix: fix apply_shuffle_mul_sum |
| `pr-sglang-7445` | upstream-code | [`sources/prs/sglang/PR-7445.md`](../sources/prs/sglang/PR-7445.md) | add fused moe config for qwen3 in triton3.3.1 |
| `pr-sglang-7457` | upstream-code | [`sources/prs/sglang/PR-7457.md`](../sources/prs/sglang/PR-7457.md) | Fix a bug in BatchTokenIDOut & Misc style and dependency updates |
| `pr-sglang-7462` | upstream-code | [`sources/prs/sglang/PR-7462.md`](../sources/prs/sglang/PR-7462.md) | Support non-contiguous query input for extend/decode attention |
| `pr-sglang-7484` | upstream-code | [`sources/prs/sglang/PR-7484.md`](../sources/prs/sglang/PR-7484.md) | [AMD] Remove vllm's scaled_fp8_quant and moe_sum when SGLANG_USE_AITER=1 |
| `pr-sglang-7569` | upstream-code | [`sources/prs/sglang/PR-7569.md`](../sources/prs/sglang/PR-7569.md) | Fix MTP error when enabling two-batch overlap  |
| `pr-sglang-7621` | upstream-code | [`sources/prs/sglang/PR-7621.md`](../sources/prs/sglang/PR-7621.md) | [b200] support trt-llm allreduce fuse rms_norm_add kernel |
| `pr-sglang-7627` | upstream-code | [`sources/prs/sglang/PR-7627.md`](../sources/prs/sglang/PR-7627.md) | Add dsv3 router gemm kernel |
| `pr-sglang-7630` | upstream-code | [`sources/prs/sglang/PR-7630.md`](../sources/prs/sglang/PR-7630.md) | Add dsv3 fused a gemm to sgl-kernel |
| `pr-sglang-7631` | upstream-code | [`sources/prs/sglang/PR-7631.md`](../sources/prs/sglang/PR-7631.md) | Add H20 fused MoE kernel configs for Dpsk & Qwen3 |
| `pr-sglang-7634` | upstream-code | [`sources/prs/sglang/PR-7634.md`](../sources/prs/sglang/PR-7634.md) | [Feature] Layer-wise Prefill |
| `pr-sglang-7648` | upstream-code | [`sources/prs/sglang/PR-7648.md`](../sources/prs/sglang/PR-7648.md) | Fix: sync prepare_fp8_layer_for_marlin with latest vllm changes |
| `pr-sglang-7649` | upstream-code | [`sources/prs/sglang/PR-7649.md`](../sources/prs/sglang/PR-7649.md) | [Feature] CUDA Green Context Support |
| `pr-sglang-7667` | upstream-code | [`sources/prs/sglang/PR-7667.md`](../sources/prs/sglang/PR-7667.md) | Add fp4 quantize before all-gather for Flashinfer cutlass MoE DP (max throughput) |
| `pr-sglang-7689` | upstream-code | [`sources/prs/sglang/PR-7689.md`](../sources/prs/sglang/PR-7689.md) | Integrate triton moe kernel |
| `pr-sglang-7762` | upstream-code | [`sources/prs/sglang/PR-7762.md`](../sources/prs/sglang/PR-7762.md) | feat: support DeepSeek-R1-W4AFP8 model with ep-moe mode |
| `pr-sglang-7772` | upstream-code | [`sources/prs/sglang/PR-7772.md`](../sources/prs/sglang/PR-7772.md) | [1/n]: add cutlass W4A8 moe kernel for hopper architecture |
| `pr-sglang-7884` | upstream-code | [`sources/prs/sglang/PR-7884.md`](../sources/prs/sglang/PR-7884.md) | [kernel] opt moe align block kernel by block/warp scan algorithm |
| `pr-sglang-7912` | upstream-code | [`sources/prs/sglang/PR-7912.md`](../sources/prs/sglang/PR-7912.md) | Qwen FP8/NVFP4 ModelOPT Quantization support |
| `pr-sglang-8118` | upstream-code | [`sources/prs/sglang/PR-8118.md`](../sources/prs/sglang/PR-8118.md) | [feat] Support tp mode for DeepSeek-R1-W4AFP8 |
| `pr-sglang-8127` | upstream-code | [`sources/prs/sglang/PR-8127.md`](../sources/prs/sglang/PR-8127.md) | [Fix][Ready]Fix register spilling in cutlass nvfp4 gemm kernel on Blackwell |
| `pr-sglang-8130` | upstream-code | [`sources/prs/sglang/PR-8130.md`](../sources/prs/sglang/PR-8130.md) | [sgl-kernel] Opt per_token_quant_fp8 with warp reduce |
| `pr-sglang-8195` | upstream-code | [`sources/prs/sglang/PR-8195.md`](../sources/prs/sglang/PR-8195.md) | [fix] fix modelopt fp4 on b200 |
| `pr-sglang-8247` | upstream-code | [`sources/prs/sglang/PR-8247.md`](../sources/prs/sglang/PR-8247.md) | [1/N]Support  DeepSeek-R1 w4a8 normal deepep |
| `pr-sglang-8258` | upstream-code | [`sources/prs/sglang/PR-8258.md`](../sources/prs/sglang/PR-8258.md) | Support triton kernels v3.4.0 for fused_moe |
| `pr-sglang-8401` | upstream-code | [`sources/prs/sglang/PR-8401.md`](../sources/prs/sglang/PR-8401.md) | Add nvfp4 scaled mm benchmark. |
| `pr-sglang-8464` | upstream-code | [`sources/prs/sglang/PR-8464.md`](../sources/prs/sglang/PR-8464.md) | [2/N]Support DeepSeek-R1 w4a8 low latency deepep |
| `pr-sglang-8535` | upstream-code | [`sources/prs/sglang/PR-8535.md`](../sources/prs/sglang/PR-8535.md) | Update cutlass_moe.py |
| `pr-sglang-8545` | upstream-code | [`sources/prs/sglang/PR-8545.md`](../sources/prs/sglang/PR-8545.md) | Update cutlass_moe.py |
| `pr-sglang-8552` | upstream-code | [`sources/prs/sglang/PR-8552.md`](../sources/prs/sglang/PR-8552.md) | [NVIDIA] Add Low Latency NVFP4 decode kernels from Flashinfer |
| `pr-sglang-8638` | upstream-code | [`sources/prs/sglang/PR-8638.md`](../sources/prs/sglang/PR-8638.md) | TRTLLM-MLA FP8 path |
| `pr-sglang-8678` | upstream-code | [`sources/prs/sglang/PR-8678.md`](../sources/prs/sglang/PR-8678.md) | feat: support cutlass_moe_fp8 kernel for fusedmoe in sm90 |
| `pr-sglang-8731` | upstream-code | [`sources/prs/sglang/PR-8731.md`](../sources/prs/sglang/PR-8731.md) | fuse allreduce and residual_rmsnorm |
| `pr-sglang-8766` | upstream-code | [`sources/prs/sglang/PR-8766.md`](../sources/prs/sglang/PR-8766.md) | Fix mismatch between padded_scales shape and reshape dimensions in modelopt quantization |
| `pr-sglang-8782` | upstream-code | [`sources/prs/sglang/PR-8782.md`](../sources/prs/sglang/PR-8782.md) | feat: add trtllm-gen mha from direct call |
| `pr-sglang-8815` | upstream-code | [`sources/prs/sglang/PR-8815.md`](../sources/prs/sglang/PR-8815.md) | fix benchmark fp8 blockwise group gemm |
| `pr-sglang-8818` | upstream-code | [`sources/prs/sglang/PR-8818.md`](../sources/prs/sglang/PR-8818.md) | [Perf] Tunings for SM100 FP8 CUTLASS kernel |
| `pr-sglang-8829` | upstream-code | [`sources/prs/sglang/PR-8829.md`](../sources/prs/sglang/PR-8829.md) | Modelopt quant config adaptation |
| `pr-sglang-8898` | upstream-code | [`sources/prs/sglang/PR-8898.md`](../sources/prs/sglang/PR-8898.md) | [Perf] Auto enable best flashinfer mxfp4  kernel in b200 |
| `pr-sglang-8908` | upstream-code | [`sources/prs/sglang/PR-8908.md`](../sources/prs/sglang/PR-8908.md) | Fix hopper launch gpt-oss model illegal memory |
| `pr-sglang-8913` | upstream-code | [`sources/prs/sglang/PR-8913.md`](../sources/prs/sglang/PR-8913.md) | [sgl-kernel] 1/N Refactor sglang cutlass 3x - gemm fp8 blockwise sm90 |
| `pr-sglang-8953` | upstream-code | [`sources/prs/sglang/PR-8953.md`](../sources/prs/sglang/PR-8953.md) | Better optimization log for gpt-oss model |
| `pr-sglang-8955` | upstream-code | [`sources/prs/sglang/PR-8955.md`](../sources/prs/sglang/PR-8955.md) | [NVIDIA] Fix missing `get_col_major_tma_aligned_tensor` for Blackwell deepgemm in EpMoE |
| `pr-sglang-8962` | upstream-code | [`sources/prs/sglang/PR-8962.md`](../sources/prs/sglang/PR-8962.md) | optimize: reduce shulffle and quantization overhead in cutlass_moe sm90 |
| `pr-sglang-9004` | upstream-code | [`sources/prs/sglang/PR-9004.md`](../sources/prs/sglang/PR-9004.md) | Add enable_flashinfer_mxfp4_bf16_moe for higher precision and slower moe backend |
| `pr-sglang-9060` | upstream-code | [`sources/prs/sglang/PR-9060.md`](../sources/prs/sglang/PR-9060.md) | [sgl-kernel] Support FlashInfer top_k_top_p_sampling_from_logits |
| `pr-sglang-9162` | upstream-code | [`sources/prs/sglang/PR-9162.md`](../sources/prs/sglang/PR-9162.md) | Faster weight processing (trtllm-gen moe nvfp4) |
| `pr-sglang-9199` | upstream-code | [`sources/prs/sglang/PR-9199.md`](../sources/prs/sglang/PR-9199.md) | [NVIDIA] [3/N] Nvfp4 Masked Gemm: Add flashinfer grouped_gemm_nt_masked  |
| `pr-sglang-9200` | upstream-code | [`sources/prs/sglang/PR-9200.md`](../sources/prs/sglang/PR-9200.md) | [NVIDA] [1/N] Nvfp4 Masked Gemm: Add quant op for the flashinfer grouped gemm |
| `pr-sglang-9251` | upstream-code | [`sources/prs/sglang/PR-9251.md`](../sources/prs/sglang/PR-9251.md) | feat: Add Triton fallback option and SM120 MoE configs for FP8 models |
| `pr-sglang-9272` | upstream-code | [`sources/prs/sglang/PR-9272.md`](../sources/prs/sglang/PR-9272.md) | [fix]:  fix cutlass moe ut and and Opt H20 cutlass groupGemm performance |
| `pr-sglang-9333` | upstream-code | [`sources/prs/sglang/PR-9333.md`](../sources/prs/sglang/PR-9333.md) | [code  clean] add H20 cutlass groupGemm default  config |
| `pr-sglang-9339` | upstream-code | [`sources/prs/sglang/PR-9339.md`](../sources/prs/sglang/PR-9339.md) | Support trtllm_allreduce_fusion in flashinfer for cuda<12.8 |
| `pr-sglang-9346` | upstream-code | [`sources/prs/sglang/PR-9346.md`](../sources/prs/sglang/PR-9346.md) | Fix FP4 inference corruption issue in glm4.5-air model |
| `pr-sglang-9403` | upstream-code | [`sources/prs/sglang/PR-9403.md`](../sources/prs/sglang/PR-9403.md) | [sgl-kernel] feat: Support sm120 cutlass fp8 gemm kernel |
| `pr-sglang-9473` | upstream-code | [`sources/prs/sglang/PR-9473.md`](../sources/prs/sglang/PR-9473.md) | [fix] Fix mxfp4 triton MoE tp bug |
| `pr-sglang-9477` | upstream-code | [`sources/prs/sglang/PR-9477.md`](../sources/prs/sglang/PR-9477.md) | Optimize moe_sum_reduce_kernel |
| `pr-sglang-9530` | upstream-code | [`sources/prs/sglang/PR-9530.md`](../sources/prs/sglang/PR-9530.md) | fix: blackwell dsv3 fp8 issue temporary solution |
| `pr-sglang-9556` | upstream-code | [`sources/prs/sglang/PR-9556.md`](../sources/prs/sglang/PR-9556.md) | [NVIDIA] [2/N] Optimize `silu_and_mul_scaled_fp4_grouped_quant` perf |
| `pr-sglang-9559` | upstream-code | [`sources/prs/sglang/PR-9559.md`](../sources/prs/sglang/PR-9559.md) | Update CUTLASS 4.2 & Enable K-Major Scale Factor for SM90 FP8 Blockwise Group GEMM |
| `pr-sglang-9589` | upstream-code | [`sources/prs/sglang/PR-9589.md`](../sources/prs/sglang/PR-9589.md) | Tiny fix wrong comments |
| `pr-sglang-9660` | upstream-code | [`sources/prs/sglang/PR-9660.md`](../sources/prs/sglang/PR-9660.md) | Single Batch Overlap for MoE Models |
| `pr-sglang-9679` | upstream-code | [`sources/prs/sglang/PR-9679.md`](../sources/prs/sglang/PR-9679.md) | move is_sm90_supported/is_sm100_supported to python/sglang/srt/utils.py |
| `pr-sglang-9712` | upstream-code | [`sources/prs/sglang/PR-9712.md`](../sources/prs/sglang/PR-9712.md) | [ModelOpt] Fix Weight Loading for DSR1-FP4 Quantization |
| `pr-sglang-9744` | upstream-code | [`sources/prs/sglang/PR-9744.md`](../sources/prs/sglang/PR-9744.md) | [CPU] Add FP8 Bmm support |
| `pr-sglang-9789` | upstream-code | [`sources/prs/sglang/PR-9789.md`](../sources/prs/sglang/PR-9789.md) | Make sm100 fp8 kernels available on sm103 |
| `pr-sglang-9807` | upstream-code | [`sources/prs/sglang/PR-9807.md`](../sources/prs/sglang/PR-9807.md) | Make fp4_quantize kernels work on sm103 |
| `pr-sglang-9824` | upstream-code | [`sources/prs/sglang/PR-9824.md`](../sources/prs/sglang/PR-9824.md) | [Model] Support Meituan LongCat-Flash && LongCat-Flash-MTP |
| `pr-sglang-9928` | upstream-code | [`sources/prs/sglang/PR-9928.md`](../sources/prs/sglang/PR-9928.md) | support using fa4 on deepseek on blackwell |
| `pr-sglang-9946` | upstream-code | [`sources/prs/sglang/PR-9946.md`](../sources/prs/sglang/PR-9946.md) | [Fix] DeepSeek EP accuracy issue on B200 GPUs |
| `pr-sglang-9969` | upstream-code | [`sources/prs/sglang/PR-9969.md`](../sources/prs/sglang/PR-9969.md) | CUTLASS fp8 blockwise gemm support of sm120 |

<a id="tile-aitilelang"></a>
## tile-ai/tilelang

195 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-tilelang-1056` | upstream-code | [`sources/prs/tilelang/PR-1056.md`](../sources/prs/tilelang/PR-1056.md) | [Language] support `T.gemm_sp_v2` on sm80 and sm89 |
| `pr-tilelang-1090` | upstream-code | [`sources/prs/tilelang/PR-1090.md`](../sources/prs/tilelang/PR-1090.md) | [BugFix] Correct direct copy from bf16 to fp8 |
| `pr-tilelang-1114` | upstream-code | [`sources/prs/tilelang/PR-1114.md`](../sources/prs/tilelang/PR-1114.md) | [Feature] Support None type as input for `T.ptr` and `T.Tensor` |
| `pr-tilelang-1120` | upstream-code | [`sources/prs/tilelang/PR-1120.md`](../sources/prs/tilelang/PR-1120.md) | [Language] Initial version of tilelang frontend v2 |
| `pr-tilelang-1188` | upstream-code | [`sources/prs/tilelang/PR-1188.md`](../sources/prs/tilelang/PR-1188.md) | [Feat] Add support for `T.serial` with step and negative step |
| `pr-tilelang-1200` | upstream-code | [`sources/prs/tilelang/PR-1200.md`](../sources/prs/tilelang/PR-1200.md) | [Refactor] Add kernel selection option for GEMM v1 in environment settings |
| `pr-tilelang-1221` | upstream-code | [`sources/prs/tilelang/PR-1221.md`](../sources/prs/tilelang/PR-1221.md) |  [Enhancement] Improve iterator handling in layout utilities and parallel operations |
| `pr-tilelang-1229` | upstream-code | [`sources/prs/tilelang/PR-1229.md`](../sources/prs/tilelang/PR-1229.md) | [WIP] support more dtypes for tcgen05 |
| `pr-tilelang-1246` | upstream-code | [`sources/prs/tilelang/PR-1246.md`](../sources/prs/tilelang/PR-1246.md) | [Bugfix] Fix fp8 dtype for some cases |
| `pr-tilelang-1269` | upstream-code | [`sources/prs/tilelang/PR-1269.md`](../sources/prs/tilelang/PR-1269.md) | [Enhancement] Keep max score attention across blocks in FlashAttention for better numerical stablity |
| `pr-tilelang-1281` | upstream-code | [`sources/prs/tilelang/PR-1281.md`](../sources/prs/tilelang/PR-1281.md) | [Fix] Fix memory leak bug |
| `pr-tilelang-1296` | upstream-code | [`sources/prs/tilelang/PR-1296.md`](../sources/prs/tilelang/PR-1296.md) | Add sparse fine-tuning kernel for deepseek sparse attention to example |
| `pr-tilelang-1323` | upstream-code | [`sources/prs/tilelang/PR-1323.md`](../sources/prs/tilelang/PR-1323.md) | Revert "[WIP] support more dtypes for tcgen05 (#1229)" |
| `pr-tilelang-1327` | upstream-code | [`sources/prs/tilelang/PR-1327.md`](../sources/prs/tilelang/PR-1327.md) | [Enhancement] add more dtype and fix mma.ws for fp16 for tcgen05 |
| `pr-tilelang-1337` | upstream-code | [`sources/prs/tilelang/PR-1337.md`](../sources/prs/tilelang/PR-1337.md) | [Language] Tilelang LazyJIT Experimental Version |
| `pr-tilelang-1338` | upstream-code | [`sources/prs/tilelang/PR-1338.md`](../sources/prs/tilelang/PR-1338.md) | [Language][UX] Semantic check for parallel fragment access |
| `pr-tilelang-1348` | upstream-code | [`sources/prs/tilelang/PR-1348.md`](../sources/prs/tilelang/PR-1348.md) | [Fix] Fix missing `not` operator in frontend (#1347) |
| `pr-tilelang-1367` | upstream-code | [`sources/prs/tilelang/PR-1367.md`](../sources/prs/tilelang/PR-1367.md) | [Feat] Integrate Z3 in TVM Arith Analyzer |
| `pr-tilelang-1399` | upstream-code | [`sources/prs/tilelang/PR-1399.md`](../sources/prs/tilelang/PR-1399.md) | [Enhancement] Refactor inflight computing to support dynamic pipeline extents |
| `pr-tilelang-1414` | upstream-code | [`sources/prs/tilelang/PR-1414.md`](../sources/prs/tilelang/PR-1414.md) | [Enhancement] Introduce `T.__ldg` |
| `pr-tilelang-1416` | upstream-code | [`sources/prs/tilelang/PR-1416.md`](../sources/prs/tilelang/PR-1416.md) | [CUDA] Add read-only parameter annotation for CUDA codegen |
| `pr-tilelang-1417` | upstream-code | [`sources/prs/tilelang/PR-1417.md`](../sources/prs/tilelang/PR-1417.md) | [Lint] Phaseout Yapf format and embrace ruff format |
| `pr-tilelang-1421` | upstream-code | [`sources/prs/tilelang/PR-1421.md`](../sources/prs/tilelang/PR-1421.md) | feat(cutedsl): add CuTeDSL backend |
| `pr-tilelang-1439` | upstream-code | [`sources/prs/tilelang/PR-1439.md`](../sources/prs/tilelang/PR-1439.md) | [Lint] Enable whitespace and permission bit hooks |
| `pr-tilelang-1489` | upstream-code | [`sources/prs/tilelang/PR-1489.md`](../sources/prs/tilelang/PR-1489.md) | [CI] Add preformance regression test script |
| `pr-tilelang-1503` | upstream-code | [`sources/prs/tilelang/PR-1503.md`](../sources/prs/tilelang/PR-1503.md) | Update cutedsl docs and version check |
| `pr-tilelang-1505` | upstream-code | [`sources/prs/tilelang/PR-1505.md`](../sources/prs/tilelang/PR-1505.md) | [Misc] configure pymarkdown |
| `pr-tilelang-1513` | upstream-code | [`sources/prs/tilelang/PR-1513.md`](../sources/prs/tilelang/PR-1513.md) | [CuTeDSL][Fix] thread safety + context safety |
| `pr-tilelang-1514` | upstream-code | [`sources/prs/tilelang/PR-1514.md`](../sources/prs/tilelang/PR-1514.md) | [Cleanup] Remove unnecessary macros in tilelang examples |
| `pr-tilelang-1515` | upstream-code | [`sources/prs/tilelang/PR-1515.md`](../sources/prs/tilelang/PR-1515.md) | [BugFix] Phaseout unused tests for gqa decode kernels and add the kernels to CI |
| `pr-tilelang-1519` | upstream-code | [`sources/prs/tilelang/PR-1519.md`](../sources/prs/tilelang/PR-1519.md) | [Enhancement] Improve GitHub Actions permissions check and refine performance regression testing |
| `pr-tilelang-1521` | upstream-code | [`sources/prs/tilelang/PR-1521.md`](../sources/prs/tilelang/PR-1521.md) | [Bugfix] Fallback to a Linear Layout instead of raising errors |
| `pr-tilelang-1533` | upstream-code | [`sources/prs/tilelang/PR-1533.md`](../sources/prs/tilelang/PR-1533.md) | [Fix] Add support for non-var complement arithmetic computation (#1374) |
| `pr-tilelang-1548` | upstream-code | [`sources/prs/tilelang/PR-1548.md`](../sources/prs/tilelang/PR-1548.md) | [Enhancement] Support larger `H` in deepseek sparse mla backward via split-H |
| `pr-tilelang-1559` | upstream-code | [`sources/prs/tilelang/PR-1559.md`](../sources/prs/tilelang/PR-1559.md) | [Parallel][Infer] Free-mode chooses minimal replication between buffer-based and PlanLoopPartition |
| `pr-tilelang-1568` | upstream-code | [`sources/prs/tilelang/PR-1568.md`](../sources/prs/tilelang/PR-1568.md) | [Refactor] Simplify do_bench calls by using default warmup and rep parameters |
| `pr-tilelang-1577` | upstream-code | [`sources/prs/tilelang/PR-1577.md`](../sources/prs/tilelang/PR-1577.md) | [BugFix] fix tcgen5mma example |
| `pr-tilelang-1579` | upstream-code | [`sources/prs/tilelang/PR-1579.md`](../sources/prs/tilelang/PR-1579.md) | [Layout] Support annotating loop layout in frontend |
| `pr-tilelang-1582` | upstream-code | [`sources/prs/tilelang/PR-1582.md`](../sources/prs/tilelang/PR-1582.md) | [Feature] Add more curand operations & support vectorization |
| `pr-tilelang-1584` | upstream-code | [`sources/prs/tilelang/PR-1584.md`](../sources/prs/tilelang/PR-1584.md) | [CI] Add CUDA-aware pytest scheduler + auto workers |
| `pr-tilelang-1585` | upstream-code | [`sources/prs/tilelang/PR-1585.md`](../sources/prs/tilelang/PR-1585.md) | [Enhancement] Improve performance regression output with timing and streaming |
| `pr-tilelang-1590` | upstream-code | [`sources/prs/tilelang/PR-1590.md`](../sources/prs/tilelang/PR-1590.md) | [Refactor] Use access_ptr instead of buffer and offsets for cp async params |
| `pr-tilelang-1597` | upstream-code | [`sources/prs/tilelang/PR-1597.md`](../sources/prs/tilelang/PR-1597.md) | [Fix][CuteDSL] add support for tanh/tanhf (fixes #1595) |
| `pr-tilelang-1599` | upstream-code | [`sources/prs/tilelang/PR-1599.md`](../sources/prs/tilelang/PR-1599.md) | [Enhancement][Subtype] Enhance symbolic shape/stride handling for subtype |
| `pr-tilelang-1600` | upstream-code | [`sources/prs/tilelang/PR-1600.md`](../sources/prs/tilelang/PR-1600.md) | Add conversion from cutlass::float_e4m3/e5m2 to tl::float_e4m3/e5m2 |
| `pr-tilelang-1605` | upstream-code | [`sources/prs/tilelang/PR-1605.md`](../sources/prs/tilelang/PR-1605.md) | [Enhancement][AMD] Add preshuffle fp8 gemm example on amd. |
| `pr-tilelang-1616` | upstream-code | [`sources/prs/tilelang/PR-1616.md`](../sources/prs/tilelang/PR-1616.md) | [Feat] Allow print macro call stack in device assert |
| `pr-tilelang-1627` | upstream-code | [`sources/prs/tilelang/PR-1627.md`](../sources/prs/tilelang/PR-1627.md) | [BugFix] Correct index_map selection for transposed A matrix in MFMA Layout with `k_dim==4` and open rocm-ci for gemmsr |
| `pr-tilelang-1632` | upstream-code | [`sources/prs/tilelang/PR-1632.md`](../sources/prs/tilelang/PR-1632.md) | [Refactor] Unify @jit and @lazy_jit into a single @jit decorator |
| `pr-tilelang-1636` | upstream-code | [`sources/prs/tilelang/PR-1636.md`](../sources/prs/tilelang/PR-1636.md) | [Example] Add Seesaw Sparse MLA Forward Kernel for DeepSeek-V3.2 |
| `pr-tilelang-1644` | upstream-code | [`sources/prs/tilelang/PR-1644.md`](../sources/prs/tilelang/PR-1644.md) | [Feature] Introduce DecoupleTypeCast pass for mixed-precision vectorization |
| `pr-tilelang-1647` | upstream-code | [`sources/prs/tilelang/PR-1647.md`](../sources/prs/tilelang/PR-1647.md) | [Feat] Allow dangling producer in wasp pipeline planning (#1263) |
| `pr-tilelang-1658` | upstream-code | [`sources/prs/tilelang/PR-1658.md`](../sources/prs/tilelang/PR-1658.md) | [Feat] profiler support cudagraph backend |
| `pr-tilelang-1660` | upstream-code | [`sources/prs/tilelang/PR-1660.md`](../sources/prs/tilelang/PR-1660.md) | [Example] Add KDA algorithm implementation in tilelang |
| `pr-tilelang-1664` | upstream-code | [`sources/prs/tilelang/PR-1664.md`](../sources/prs/tilelang/PR-1664.md) | [EagerJIT] Add Support for Parameter Only Kernel Compilation |
| `pr-tilelang-1667` | upstream-code | [`sources/prs/tilelang/PR-1667.md`](../sources/prs/tilelang/PR-1667.md) | [Feature] Support `cp.reduce.async.bulk.tensor` |
| `pr-tilelang-1669` | upstream-code | [`sources/prs/tilelang/PR-1669.md`](../sources/prs/tilelang/PR-1669.md) | [CUDA] Enhance Broadcast Codegen for Symbolic Value |
| `pr-tilelang-1670` | upstream-code | [`sources/prs/tilelang/PR-1670.md`](../sources/prs/tilelang/PR-1670.md) | Refactor: Use centralized do_bench from tilelang.profiler |
| `pr-tilelang-1672` | upstream-code | [`sources/prs/tilelang/PR-1672.md`](../sources/prs/tilelang/PR-1672.md) | [Clean][Refactor] Phaseout Legacy Pass `ParallelLoopTransformer` |
| `pr-tilelang-1676` | upstream-code | [`sources/prs/tilelang/PR-1676.md`](../sources/prs/tilelang/PR-1676.md) | [Feature] Atomic Reduction Operations and Vectorization Enhancement |
| `pr-tilelang-1677` | upstream-code | [`sources/prs/tilelang/PR-1677.md`](../sources/prs/tilelang/PR-1677.md) | [Refactor] Move AtomicAdd Vectorization to VectorizeLoop Pass |
| `pr-tilelang-1692` | upstream-code | [`sources/prs/tilelang/PR-1692.md`](../sources/prs/tilelang/PR-1692.md) | [Chore] Use python-side control flow keywords in examples for consistency |
| `pr-tilelang-1701` | upstream-code | [`sources/prs/tilelang/PR-1701.md`](../sources/prs/tilelang/PR-1701.md) | [AMD] Fix bugs about AMD FA kernel |
| `pr-tilelang-1703` | upstream-code | [`sources/prs/tilelang/PR-1703.md`](../sources/prs/tilelang/PR-1703.md) | [Enhancement] Use `cute::elect_one_sync()` for slightly better performance |
| `pr-tilelang-1717` | upstream-code | [`sources/prs/tilelang/PR-1717.md`](../sources/prs/tilelang/PR-1717.md) | [Enhancement] Add explicit global memory load/store intrinsics (ldg/stg 32/64/128) |
| `pr-tilelang-1722` | upstream-code | [`sources/prs/tilelang/PR-1722.md`](../sources/prs/tilelang/PR-1722.md) | [Refactor] re-implement vector subtype and its access method |
| `pr-tilelang-1724` | upstream-code | [`sources/prs/tilelang/PR-1724.md`](../sources/prs/tilelang/PR-1724.md) | [Enhancement] Legalize subtype access |
| `pr-tilelang-1726` | upstream-code | [`sources/prs/tilelang/PR-1726.md`](../sources/prs/tilelang/PR-1726.md) | [Bugfix] Fix incorrect alignment of vectorized subtype |
| `pr-tilelang-1736` | upstream-code | [`sources/prs/tilelang/PR-1736.md`](../sources/prs/tilelang/PR-1736.md) | Add swizzle layout detection and automatic merging for layout conflicts |
| `pr-tilelang-1740` | upstream-code | [`sources/prs/tilelang/PR-1740.md`](../sources/prs/tilelang/PR-1740.md) | [fix]: fix deepseek_mla amd example and add aiter mla compare test |
| `pr-tilelang-1741` | upstream-code | [`sources/prs/tilelang/PR-1741.md`](../sources/prs/tilelang/PR-1741.md) | [BugFix] Fix FP4 related vectorized cast |
| `pr-tilelang-1743` | upstream-code | [`sources/prs/tilelang/PR-1743.md`](../sources/prs/tilelang/PR-1743.md) | [AMD] Fix ROCm FP8 dtype selection and MFMA support on gfx942/gfx950 |
| `pr-tilelang-1753` | upstream-code | [`sources/prs/tilelang/PR-1753.md`](../sources/prs/tilelang/PR-1753.md) | [Enhancement] Add dynamic symbolic constraints support for Profiler benchmarking |
| `pr-tilelang-1757` | upstream-code | [`sources/prs/tilelang/PR-1757.md`](../sources/prs/tilelang/PR-1757.md) | [Refactor] Unify the usage of cast-related operators |
| `pr-tilelang-1762` | upstream-code | [`sources/prs/tilelang/PR-1762.md`](../sources/prs/tilelang/PR-1762.md) | [Feature] Hierarchical reduction and warp reduction intrinsics support |
| `pr-tilelang-1764` | upstream-code | [`sources/prs/tilelang/PR-1764.md`](../sources/prs/tilelang/PR-1764.md) | [Feature] Support tcgen5mma lowering for `.kind::i8` |
| `pr-tilelang-1774` | upstream-code | [`sources/prs/tilelang/PR-1774.md`](../sources/prs/tilelang/PR-1774.md) | [Example][BugFix] 1SM GEMM example on Blackwell and fix handling of `mbar` |
| `pr-tilelang-1776` | upstream-code | [`sources/prs/tilelang/PR-1776.md`](../sources/prs/tilelang/PR-1776.md) | [Bugfix] Copy pass_configs dict to prevent mutation across multiple JIT compilations |
| `pr-tilelang-1781` | upstream-code | [`sources/prs/tilelang/PR-1781.md`](../sources/prs/tilelang/PR-1781.md) | [Bugfix] Fix thread storage sync conflict detection for loop carry write-after-read |
| `pr-tilelang-1786` | upstream-code | [`sources/prs/tilelang/PR-1786.md`](../sources/prs/tilelang/PR-1786.md) | fix(intrinsics): add missing _legalize_to_buffer_region in SM70 emitter |
| `pr-tilelang-1801` | upstream-code | [`sources/prs/tilelang/PR-1801.md`](../sources/prs/tilelang/PR-1801.md) | [BugFix] Missing Recursive Loop Var Checking in Loop Unswitching |
| `pr-tilelang-1820` | upstream-code | [`sources/prs/tilelang/PR-1820.md`](../sources/prs/tilelang/PR-1820.md) | [Bugfix] Remove mistaken coalesced_width parameter in regression test of fusedmoe kernel |
| `pr-tilelang-1827` | upstream-code | [`sources/prs/tilelang/PR-1827.md`](../sources/prs/tilelang/PR-1827.md) | [Refactor] Introduce `T.access_of` to combine `T.address_of` and `access_ptr` |
| `pr-tilelang-1837` | upstream-code | [`sources/prs/tilelang/PR-1837.md`](../sources/prs/tilelang/PR-1837.md) | Fix tilelang global load/store template |
| `pr-tilelang-1839` | upstream-code | [`sources/prs/tilelang/PR-1839.md`](../sources/prs/tilelang/PR-1839.md) | [CUDA][Feature] Add packed FP32x2 math intrinsics and auto vectorized support |
| `pr-tilelang-1840` | upstream-code | [`sources/prs/tilelang/PR-1840.md`](../sources/prs/tilelang/PR-1840.md) | [BugFix] Fix Hopper TMA lowering without warp specialization |
| `pr-tilelang-1845` | upstream-code | [`sources/prs/tilelang/PR-1845.md`](../sources/prs/tilelang/PR-1845.md) | [Enhancement] Optimize templates for half/bfloat16 |
| `pr-tilelang-1855` | upstream-code | [`sources/prs/tilelang/PR-1855.md`](../sources/prs/tilelang/PR-1855.md) | [Enhancement] GEMM V2 on SM90/SM100 CuTeDSL backend |
| `pr-tilelang-1857` | upstream-code | [`sources/prs/tilelang/PR-1857.md`](../sources/prs/tilelang/PR-1857.md) | [Codegen] Metal codegen on Linux |
| `pr-tilelang-1858` | upstream-code | [`sources/prs/tilelang/PR-1858.md`](../sources/prs/tilelang/PR-1858.md) | [Feature] Add TIR builtins for warp-level vote and block-level predicate sync |
| `pr-tilelang-1863` | upstream-code | [`sources/prs/tilelang/PR-1863.md`](../sources/prs/tilelang/PR-1863.md) | [Refactor] Refactor Pass InjectFenceProxy |
| `pr-tilelang-1865` | upstream-code | [`sources/prs/tilelang/PR-1865.md`](../sources/prs/tilelang/PR-1865.md) | [FIX] Fix kernel file suffix for cutedsl |
| `pr-tilelang-1866` | upstream-code | [`sources/prs/tilelang/PR-1866.md`](../sources/prs/tilelang/PR-1866.md) | [CUDA] Support tcgen5mma gemm ts |
| `pr-tilelang-1874` | upstream-code | [`sources/prs/tilelang/PR-1874.md`](../sources/prs/tilelang/PR-1874.md) | [Feature] Support cluster launch, query, synchronization and barrier operations |
| `pr-tilelang-1878` | upstream-code | [`sources/prs/tilelang/PR-1878.md`](../sources/prs/tilelang/PR-1878.md) | [AMD] Fix gfx950 ci and add 16x16x32_bf16/fp16 instructions support |
| `pr-tilelang-1880` | upstream-code | [`sources/prs/tilelang/PR-1880.md`](../sources/prs/tilelang/PR-1880.md) | Avoid cvt instruction in FP4 before cuda 13.0 |
| `pr-tilelang-1882` | upstream-code | [`sources/prs/tilelang/PR-1882.md`](../sources/prs/tilelang/PR-1882.md) | [Feature] 2-SM support for TMA, TMEM and TCGEN5MMA on Blackwell |
| `pr-tilelang-1884` | upstream-code | [`sources/prs/tilelang/PR-1884.md`](../sources/prs/tilelang/PR-1884.md) | [Analysis] Refactor FragmentLoopChecker visiting style |
| `pr-tilelang-1887` | upstream-code | [`sources/prs/tilelang/PR-1887.md`](../sources/prs/tilelang/PR-1887.md) | [Refactor] Improve cp.async lowering and add async_copy op |
| `pr-tilelang-1899` | upstream-code | [`sources/prs/tilelang/PR-1899.md`](../sources/prs/tilelang/PR-1899.md) | [BugFix] add target context and avoid redundant re-lowering in TLCPUSourceWrapper |
| `pr-tilelang-1901` | upstream-code | [`sources/prs/tilelang/PR-1901.md`](../sources/prs/tilelang/PR-1901.md) | [BugFix] Add vector type definitions to common.h for CPU codegen |
| `pr-tilelang-1906` | upstream-code | [`sources/prs/tilelang/PR-1906.md`](../sources/prs/tilelang/PR-1906.md) | [Enhancement] Add eager-mode support for tilelang.autotune |
| `pr-tilelang-1909` | upstream-code | [`sources/prs/tilelang/PR-1909.md`](../sources/prs/tilelang/PR-1909.md) | [Feature] Add Producer-Consumer Warp Specialization and T.tma_copy() API |
| `pr-tilelang-1910` | upstream-code | [`sources/prs/tilelang/PR-1910.md`](../sources/prs/tilelang/PR-1910.md) | [Example] Flash Attention SM100 |
| `pr-tilelang-1923` | upstream-code | [`sources/prs/tilelang/PR-1923.md`](../sources/prs/tilelang/PR-1923.md) | Support ptr-table grouped GEMM kernels |
| `pr-tilelang-1926` | upstream-code | [`sources/prs/tilelang/PR-1926.md`](../sources/prs/tilelang/PR-1926.md) | [Bugfix] Fix concurrent TempDirectory creation during CUDA compilation |
| `pr-tilelang-1931` | upstream-code | [`sources/prs/tilelang/PR-1931.md`](../sources/prs/tilelang/PR-1931.md) | [Runtime] Improve TMA descriptor diagnostics |
| `pr-tilelang-1932` | upstream-code | [`sources/prs/tilelang/PR-1932.md`](../sources/prs/tilelang/PR-1932.md) | test: reduce CI runtime for slow Python suites |
| `pr-tilelang-1937` | upstream-code | [`sources/prs/tilelang/PR-1937.md`](../sources/prs/tilelang/PR-1937.md) | Fix predicated cp.async pipeline scheduling |
| `pr-tilelang-1940` | upstream-code | [`sources/prs/tilelang/PR-1940.md`](../sources/prs/tilelang/PR-1940.md) | [Feature] Support alloc global workspace |
| `pr-tilelang-1945` | upstream-code | [`sources/prs/tilelang/PR-1945.md`](../sources/prs/tilelang/PR-1945.md) | [Feature] Block-scaled GEMM support for MXFP8 on Blackwell |
| `pr-tilelang-1946` | upstream-code | [`sources/prs/tilelang/PR-1946.md`](../sources/prs/tilelang/PR-1946.md) | [BugFix] Update usage of tma load in SM100 manual warp-specialized examples |
| `pr-tilelang-1947` | upstream-code | [`sources/prs/tilelang/PR-1947.md`](../sources/prs/tilelang/PR-1947.md) | Support packed subtype views during layout reshape |
| `pr-tilelang-1949` | upstream-code | [`sources/prs/tilelang/PR-1949.md`](../sources/prs/tilelang/PR-1949.md) | [Refactor] Separate gemm into explicit `wgmma_gemm` and `tcgen05_gemm` functions |
| `pr-tilelang-1950` | upstream-code | [`sources/prs/tilelang/PR-1950.md`](../sources/prs/tilelang/PR-1950.md) | [Enhancement] Use stronger prover in `ProveFragmentContains` to avoid false layout conflicts |
| `pr-tilelang-1951` | upstream-code | [`sources/prs/tilelang/PR-1951.md`](../sources/prs/tilelang/PR-1951.md) | [AMD][Radeon] Upgrade Rocm version to be 7.2 and add the support of RDNA4 GPU  |
| `pr-tilelang-1953` | upstream-code | [`sources/prs/tilelang/PR-1953.md`](../sources/prs/tilelang/PR-1953.md) | [PIpeline] Enable software pipelining when warp specialization is unavailable |
| `pr-tilelang-1956` | upstream-code | [`sources/prs/tilelang/PR-1956.md`](../sources/prs/tilelang/PR-1956.md) | Fix T.gemm() on SM75 Turing GPUs by including SM75 MMA headers |
| `pr-tilelang-1962` | upstream-code | [`sources/prs/tilelang/PR-1962.md`](../sources/prs/tilelang/PR-1962.md) | [Bugfix] Fix double buffer versioning when TMA is used without warp specialization |
| `pr-tilelang-1969` | upstream-code | [`sources/prs/tilelang/PR-1969.md`](../sources/prs/tilelang/PR-1969.md) | [BugFix] Fix bugs in `gemm_streamk` example on SM90 |
| `pr-tilelang-1970` | upstream-code | [`sources/prs/tilelang/PR-1970.md`](../sources/prs/tilelang/PR-1970.md) | [Feature] Introduce T.CUDASourceCodeKernel |
| `pr-tilelang-1971` | upstream-code | [`sources/prs/tilelang/PR-1971.md`](../sources/prs/tilelang/PR-1971.md) | Introduce T.deallocate_tmem and T.transpose |
| `pr-tilelang-1972` | upstream-code | [`sources/prs/tilelang/PR-1972.md`](../sources/prs/tilelang/PR-1972.md) | [Bugfix] Fix CuTeDSL autotune cache invalid ELF header (#1967) |
| `pr-tilelang-1975` | upstream-code | [`sources/prs/tilelang/PR-1975.md`](../sources/prs/tilelang/PR-1975.md) | Fix wrapped pre-loop TMA prefixes in producer-consumer WS |
| `pr-tilelang-1976` | upstream-code | [`sources/prs/tilelang/PR-1976.md`](../sources/prs/tilelang/PR-1976.md) | [Feature] Batched AllReduce for better T.reduce performance |
| `pr-tilelang-1978` | upstream-code | [`sources/prs/tilelang/PR-1978.md`](../sources/prs/tilelang/PR-1978.md) | Unified packed x2 intrinsics with multi-dtype support and bug fixes |
| `pr-tilelang-1979` | upstream-code | [`sources/prs/tilelang/PR-1979.md`](../sources/prs/tilelang/PR-1979.md) | [Feature] Introduce annotation for `minBlocksPerMultiprocessor` in `__launch_bounds__` |
| `pr-tilelang-1980` | upstream-code | [`sources/prs/tilelang/PR-1980.md`](../sources/prs/tilelang/PR-1980.md) | [BugFix] Add missing fences in GEMM SM100 examples and canonicalize the order of blockIdx |
| `pr-tilelang-1981` | upstream-code | [`sources/prs/tilelang/PR-1981.md`](../sources/prs/tilelang/PR-1981.md) | [Feature] Support TMA store in T.tma_copy() |
| `pr-tilelang-1982` | upstream-code | [`sources/prs/tilelang/PR-1982.md`](../sources/prs/tilelang/PR-1982.md) | [Enhancement] Use atomic directory rename for cache writes |
| `pr-tilelang-1987` | upstream-code | [`sources/prs/tilelang/PR-1987.md`](../sources/prs/tilelang/PR-1987.md) | fix(merge_shmem): allow shared memory reuse for buffers with disjoint lifetimes |
| `pr-tilelang-1989` | upstream-code | [`sources/prs/tilelang/PR-1989.md`](../sources/prs/tilelang/PR-1989.md) | Add regression test for 1D TMA load compilation and execution |
| `pr-tilelang-1991` | upstream-code | [`sources/prs/tilelang/PR-1991.md`](../sources/prs/tilelang/PR-1991.md) | [example] use alloc_global in split-kv decode kernel |
| `pr-tilelang-1995` | upstream-code | [`sources/prs/tilelang/PR-1995.md`](../sources/prs/tilelang/PR-1995.md) | [BugFix] Fix missing barrier init attrs when TMA is disabled |
| `pr-tilelang-2001` | upstream-code | [`sources/prs/tilelang/PR-2001.md`](../sources/prs/tilelang/PR-2001.md) | [Refactor] Refactor CUDA atomic helpers |
| `pr-tilelang-2002` | upstream-code | [`sources/prs/tilelang/PR-2002.md`](../sources/prs/tilelang/PR-2002.md) | [Refactor][Pipeline] Run pipeline rewriting before layout inference and stabilize tiled WS |
| `pr-tilelang-2003` | upstream-code | [`sources/prs/tilelang/PR-2003.md`](../sources/prs/tilelang/PR-2003.md) | [Transform] Add InjectTcgen05Fence pass |
| `pr-tilelang-2004` | upstream-code | [`sources/prs/tilelang/PR-2004.md`](../sources/prs/tilelang/PR-2004.md) | fix: fix copy+cast vectorize loop to use wider vector load/store instrcution |
| `pr-tilelang-2006` | upstream-code | [`sources/prs/tilelang/PR-2006.md`](../sources/prs/tilelang/PR-2006.md) | [Feature] Support T.annotate_compile_flags, T.annotate_pass_configs, and out_idx as PrimFunc attrs |
| `pr-tilelang-2008` | upstream-code | [`sources/prs/tilelang/PR-2008.md`](../sources/prs/tilelang/PR-2008.md) | [BugFix] Skip MMA shared buffer layout inference when layout already exists |
| `pr-tilelang-2009` | upstream-code | [`sources/prs/tilelang/PR-2009.md`](../sources/prs/tilelang/PR-2009.md) | [BugFix] Fix CI failures: clean /tmp on self-hosted runners and skip CuTeDSL alloc_global tests |
| `pr-tilelang-2013` | upstream-code | [`sources/prs/tilelang/PR-2013.md`](../sources/prs/tilelang/PR-2013.md) | [CI] Remove legacy dequantize gemm test |
| `pr-tilelang-2015` | upstream-code | [`sources/prs/tilelang/PR-2015.md`](../sources/prs/tilelang/PR-2015.md) | [BugFix] Enhance CUDA vectorization for binary operations |
| `pr-tilelang-2017` | upstream-code | [`sources/prs/tilelang/PR-2017.md`](../sources/prs/tilelang/PR-2017.md) | [codex] Fuse packed x2 mul-add into fma2 in CUDA codegen |
| `pr-tilelang-2023` | upstream-code | [`sources/prs/tilelang/PR-2023.md`](../sources/prs/tilelang/PR-2023.md) | [Codegen] Add lexical_alloc_scope for scoped local variable lifetime |
| `pr-tilelang-2024` | upstream-code | [`sources/prs/tilelang/PR-2024.md`](../sources/prs/tilelang/PR-2024.md) | Re-enable deprecated `TL_DISABLE_TMA_LOWER` pass config for TMA store |
| `pr-tilelang-2026` | upstream-code | [`sources/prs/tilelang/PR-2026.md`](../sources/prs/tilelang/PR-2026.md) | [Refactor] Refactor `DecoupleTypeCast` Pass |
| `pr-tilelang-2029` | upstream-code | [`sources/prs/tilelang/PR-2029.md`](../sources/prs/tilelang/PR-2029.md) | [Feature][Example] Introduce CLC tile schedule and add example for sm100 GEMM |
| `pr-tilelang-2031` | upstream-code | [`sources/prs/tilelang/PR-2031.md`](../sources/prs/tilelang/PR-2031.md) | [Bugfix] Fix stage-expanded annotated-layout aliases in LayoutInference |
| `pr-tilelang-2033` | upstream-code | [`sources/prs/tilelang/PR-2033.md`](../sources/prs/tilelang/PR-2033.md) | [Refactor] Remove GEMM v1 and promote gemm_py to be the canonical gemm op |
| `pr-tilelang-2037` | upstream-code | [`sources/prs/tilelang/PR-2037.md`](../sources/prs/tilelang/PR-2037.md) | [Bugfix][Subtype] Fix scalar fp4 store/load codegen for non-packed buffers |
| `pr-tilelang-2039` | upstream-code | [`sources/prs/tilelang/PR-2039.md`](../sources/prs/tilelang/PR-2039.md) | [API] Default warp-lane mask to 0xFFFFFFFF for warp-sync builtins |
| `pr-tilelang-2044` | upstream-code | [`sources/prs/tilelang/PR-2044.md`](../sources/prs/tilelang/PR-2044.md) | [AMD][Radeon] Add the Support of RDNA3/RDNA3.5(gfx11) WMMA |
| `pr-tilelang-2046` | upstream-code | [`sources/prs/tilelang/PR-2046.md`](../sources/prs/tilelang/PR-2046.md) | [Refactor] Remove obsolete RewriteWgmmaSync pass |
| `pr-tilelang-2047` | upstream-code | [`sources/prs/tilelang/PR-2047.md`](../sources/prs/tilelang/PR-2047.md) | [Refactor] Move target gating into InjectFenceProxy pass entry |
| `pr-tilelang-2052` | upstream-code | [`sources/prs/tilelang/PR-2052.md`](../sources/prs/tilelang/PR-2052.md) | [Bugfix] Use shared::cta instead of shared::cluster for non-cluster T… |
| `pr-tilelang-2055` | upstream-code | [`sources/prs/tilelang/PR-2055.md`](../sources/prs/tilelang/PR-2055.md) | [BugFix] Keep shared-prelude local vars in producer-consumer WS |
| `pr-tilelang-2058` | upstream-code | [`sources/prs/tilelang/PR-2058.md`](../sources/prs/tilelang/PR-2058.md) | [AMD][Gfx950] Add the support of 160K LDS and copy.async   |
| `pr-tilelang-2060` | upstream-code | [`sources/prs/tilelang/PR-2060.md`](../sources/prs/tilelang/PR-2060.md) | [Release] Bump version into 0.1.9 |
| `pr-tilelang-2063` | upstream-code | [`sources/prs/tilelang/PR-2063.md`](../sources/prs/tilelang/PR-2063.md) | [CUDA] Support int4 `T.gemm` |
| `pr-tilelang-2069` | upstream-code | [`sources/prs/tilelang/PR-2069.md`](../sources/prs/tilelang/PR-2069.md) | [Example]  Add HISA: hierarchical sparse attention indexer |
| `pr-tilelang-2071` | upstream-code | [`sources/prs/tilelang/PR-2071.md`](../sources/prs/tilelang/PR-2071.md) | [FFI] Remove upper version bound on apache-tvm-ffi |
| `pr-tilelang-2073` | upstream-code | [`sources/prs/tilelang/PR-2073.md`](../sources/prs/tilelang/PR-2073.md) | [CUDA] Improve int4 GEMM lowering and packed codegen support |
| `pr-tilelang-2075` | upstream-code | [`sources/prs/tilelang/PR-2075.md`](../sources/prs/tilelang/PR-2075.md) | [Refactor] Phaseout legacy util `map_torch_type` with `T.dtype.as_torch` |
| `pr-tilelang-2085` | upstream-code | [`sources/prs/tilelang/PR-2085.md`](../sources/prs/tilelang/PR-2085.md) | [AMD][gfx950] Add ds_read_tr16_b64 / ds_read_tr8_b64 support for gfx950  LDS transpose reads |
| `pr-tilelang-2087` | upstream-code | [`sources/prs/tilelang/PR-2087.md`](../sources/prs/tilelang/PR-2087.md) | [Bugfix] Enable `.shared::cta` in TMA copy paths only on CUDA 12.8+ |
| `pr-tilelang-2088` | upstream-code | [`sources/prs/tilelang/PR-2088.md`](../sources/prs/tilelang/PR-2088.md) | [Refactor] Refactor register annotation lowering |
| `pr-tilelang-2092` | upstream-code | [`sources/prs/tilelang/PR-2092.md`](../sources/prs/tilelang/PR-2092.md) | [BugFix] Relax loop wait and adjust trailing drain behavior in async pipeline tests |
| `pr-tilelang-2093` | upstream-code | [`sources/prs/tilelang/PR-2093.md`](../sources/prs/tilelang/PR-2093.md) | [Feature] Add full Windows support and fix related cross-platform issues |
| `pr-tilelang-2097` | upstream-code | [`sources/prs/tilelang/PR-2097.md`](../sources/prs/tilelang/PR-2097.md) | feat: support cdna4 v_mfma_i32_16x16x64_i8 & v_mfma_i32_32x32x32_i8 |
| `pr-tilelang-2098` | upstream-code | [`sources/prs/tilelang/PR-2098.md`](../sources/prs/tilelang/PR-2098.md) | [Example] Add MXFP8 blockscaled grouped gemm examples with transB support  |
| `pr-tilelang-2099` | upstream-code | [`sources/prs/tilelang/PR-2099.md`](../sources/prs/tilelang/PR-2099.md) | [AMD] [gfx950]Fix multiple HIP codegen bugs to support TileKernel   |
| `pr-tilelang-2102` | upstream-code | [`sources/prs/tilelang/PR-2102.md`](../sources/prs/tilelang/PR-2102.md) | [CUDA][SM100] Include cuda_fp6.h when emitting FP6 types |
| `pr-tilelang-2103` | upstream-code | [`sources/prs/tilelang/PR-2103.md`](../sources/prs/tilelang/PR-2103.md) | [Enhancement] Optimize hopper fp8 deepgemm tile size |
| `pr-tilelang-2105` | upstream-code | [`sources/prs/tilelang/PR-2105.md`](../sources/prs/tilelang/PR-2105.md) | [AMD][CI issue] add gfx950 guard to fix the CI issues  |
| `pr-tilelang-2107` | upstream-code | [`sources/prs/tilelang/PR-2107.md`](../sources/prs/tilelang/PR-2107.md) | [TMA] Support FP4 TensorMap TMA copies |
| `pr-tilelang-2117` | upstream-code | [`sources/prs/tilelang/PR-2117.md`](../sources/prs/tilelang/PR-2117.md) | [Enhancement][CUDA][SM100] Report unsupported FP6 vector types earlier |
| `pr-tilelang-2126` | upstream-code | [`sources/prs/tilelang/PR-2126.md`](../sources/prs/tilelang/PR-2126.md) | [Feature][Fix] Extend TCGEN5 F8F6F4 dtype plumbing |
| `pr-tilelang-2127` | upstream-code | [`sources/prs/tilelang/PR-2127.md`](../sources/prs/tilelang/PR-2127.md) | Add RDNA gfx1151 ROCm target support |
| `pr-tilelang-2134` | upstream-code | [`sources/prs/tilelang/PR-2134.md`](../sources/prs/tilelang/PR-2134.md) | fix: TMA alignment to 1024 bytes on Blackwell |
| `pr-tilelang-2138` | upstream-code | [`sources/prs/tilelang/PR-2138.md`](../sources/prs/tilelang/PR-2138.md) | [Refactor][Backend] Split tl.copy lowering by backend |
| `pr-tilelang-2148` | upstream-code | [`sources/prs/tilelang/PR-2148.md`](../sources/prs/tilelang/PR-2148.md) | [Examples] Add examples for operators in DeepSeek-V4 |
| `pr-tilelang-2151` | upstream-code | [`sources/prs/tilelang/PR-2151.md`](../sources/prs/tilelang/PR-2151.md) | [TMA] Fix TMA descriptor init placement |
| `pr-tilelang-2152` | upstream-code | [`sources/prs/tilelang/PR-2152.md`](../sources/prs/tilelang/PR-2152.md) | [docs] fix TMEM description |
| `pr-tilelang-2153` | upstream-code | [`sources/prs/tilelang/PR-2153.md`](../sources/prs/tilelang/PR-2153.md) | [codex] Split GEMM implementations by backend |
| `pr-tilelang-2156` | upstream-code | [`sources/prs/tilelang/PR-2156.md`](../sources/prs/tilelang/PR-2156.md) | [Refactor][Backend] Split remaining TileOps by backend |
| `pr-tilelang-2159` | upstream-code | [`sources/prs/tilelang/PR-2159.md`](../sources/prs/tilelang/PR-2159.md) | [Autotune] Add pipeline, grouped compilation, and multi-GPU benchmark support |
| `pr-tilelang-2161` | upstream-code | [`sources/prs/tilelang/PR-2161.md`](../sources/prs/tilelang/PR-2161.md) | [Refactor] Refactor multiple TensorCoreIntrinEmitter to provide atom-level mma control interface |
| `pr-tilelang-2163` | upstream-code | [`sources/prs/tilelang/PR-2163.md`](../sources/prs/tilelang/PR-2163.md) | [Backend] Share common GPU tile op lowerers |
| `pr-tilelang-2164` | upstream-code | [`sources/prs/tilelang/PR-2164.md`](../sources/prs/tilelang/PR-2164.md) | [Refactor] Move backend stubs out of codegen |
| `pr-tilelang-2165` | upstream-code | [`sources/prs/tilelang/PR-2165.md`](../sources/prs/tilelang/PR-2165.md) | [Refactor] Move backend-specific GEMM implementations and transforms into backend directories |
| `pr-tilelang-2166` | upstream-code | [`sources/prs/tilelang/PR-2166.md`](../sources/prs/tilelang/PR-2166.md) | [BugFix] Consider non-local store in external call and SIMT producer for warp specialize |
| `pr-tilelang-2173` | upstream-code | [`sources/prs/tilelang/PR-2173.md`](../sources/prs/tilelang/PR-2173.md) | [BugFix] Fix T.gemm() on SM75 (Turing) GPUs (#1992) |
| `pr-tilelang-2179` | upstream-code | [`sources/prs/tilelang/PR-2179.md`](../sources/prs/tilelang/PR-2179.md) | [ROCm] Try to fix ROCm CI error  |
| `pr-tilelang-2187` | upstream-code | [`sources/prs/tilelang/PR-2187.md`](../sources/prs/tilelang/PR-2187.md) | [WIP] Handle CuTeDSL FP4 torch dtype |

<a id="triton-langtriton"></a>
## triton-lang/triton

57 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-triton-10004` | upstream-code | [`sources/prs/triton/PR-10004.md`](../sources/prs/triton/PR-10004.md) | Fix nested `def` in `@triton.jit` to raise intended `UnsupportedLanguageConstruct` |
| `pr-triton-10042` | upstream-code | [`sources/prs/triton/PR-10042.md`](../sources/prs/triton/PR-10042.md) | [Triton] Fix LLVMDILocalVariable pass crash with LLVM_EXTRACT_DI_LOCAL_VARIABLES |
| `pr-triton-10056` | upstream-code | [`sources/prs/triton/PR-10056.md`](../sources/prs/triton/PR-10056.md) | [AMD][gfx1250] Support warp usage hints in TDM copy |
| `pr-triton-10081` | upstream-code | [`sources/prs/triton/PR-10081.md`](../sources/prs/triton/PR-10081.md) | [AMD][gfx9] Restore token-aware wait count derivation on asyncmark ta… |
| `pr-triton-10089` | upstream-code | [`sources/prs/triton/PR-10089.md`](../sources/prs/triton/PR-10089.md) | [Gluon][Translator] Hopper support |
| `pr-triton-10099` | upstream-code | [`sources/prs/triton/PR-10099.md`](../sources/prs/triton/PR-10099.md) | Enable PartitionedSharedEncodingAttr in the memdesc_subslice lowering  |
| `pr-triton-10100` | upstream-code | [`sources/prs/triton/PR-10100.md`](../sources/prs/triton/PR-10100.md) | [GLUON] `shared_atomic_add` implementation |
| `pr-triton-10112` | upstream-code | [`sources/prs/triton/PR-10112.md`](../sources/prs/triton/PR-10112.md) | [FPSAN] Add support for wgmma in fpsan |
| `pr-triton-10118` | upstream-code | [`sources/prs/triton/PR-10118.md`](../sources/prs/triton/PR-10118.md) | [FPSAN] Add support for batched matmul, make fpsan errors fatal |
| `pr-triton-10125` | upstream-code | [`sources/prs/triton/PR-10125.md`](../sources/prs/triton/PR-10125.md) | Add AutotuneListener hook to triton knobs |
| `pr-triton-10126` | upstream-code | [`sources/prs/triton/PR-10126.md`](../sources/prs/triton/PR-10126.md) | Do not send f64 dots through tcgen05 |
| `pr-triton-10127` | upstream-code | [`sources/prs/triton/PR-10127.md`](../sources/prs/triton/PR-10127.md) | Fixing splitClusterBefore implicit-insert bug |
| `pr-triton-10132` | upstream-code | [`sources/prs/triton/PR-10132.md`](../sources/prs/triton/PR-10132.md) | [TritonGPU] Split RemoveLayoutConversions cleanup; tolerate SCF non-convergence |
| `pr-triton-10145` | upstream-code | [`sources/prs/triton/PR-10145.md`](../sources/prs/triton/PR-10145.md) | [AMD] End-to-end support for resolving LDS partition conflicts in GFX1250 GEMMs |
| `pr-triton-10148` | upstream-code | [`sources/prs/triton/PR-10148.md`](../sources/prs/triton/PR-10148.md) | [Reland][NVIDIA] Support swizzle 0 TMA + MMA for Hopper and Blackwell |
| `pr-triton-10149` | upstream-code | [`sources/prs/triton/PR-10149.md`](../sources/prs/triton/PR-10149.md) | [BENCH][PROTON] Implement `do_bench_proton` and `do_bench_cudagraph_proton` as alternatives for benchmarking |
| `pr-triton-10150` | upstream-code | [`sources/prs/triton/PR-10150.md`](../sources/prs/triton/PR-10150.md) | [triton_kernels] Optimize matmul metadata metrics |
| `pr-triton-10151` | upstream-code | [`sources/prs/triton/PR-10151.md`](../sources/prs/triton/PR-10151.md) | [Tutorials] Fix unbound local variable in Tutorial 10 |
| `pr-triton-10157` | upstream-code | [`sources/prs/triton/PR-10157.md`](../sources/prs/triton/PR-10157.md) | [AMD] Add Triton-level tt.descriptor_gather and tt.descriptor_scatter support for gfx1250 |
| `pr-triton-10163` | upstream-code | [`sources/prs/triton/PR-10163.md`](../sources/prs/triton/PR-10163.md) | [BACKEND] Enable i16 descriptor gather/scatter indices on NVIDIA |
| `pr-triton-10167` | upstream-code | [`sources/prs/triton/PR-10167.md`](../sources/prs/triton/PR-10167.md) | [CONSAN] Add read before any write check |
| `pr-triton-10172` | upstream-code | [`sources/prs/triton/PR-10172.md`](../sources/prs/triton/PR-10172.md) | [AMD][TDM] Pipeline tt.descriptor_gather through the TDM async chain |
| `pr-triton-10174` | upstream-code | [`sources/prs/triton/PR-10174.md`](../sources/prs/triton/PR-10174.md) | [release/3.7.x] Cherry pick "Split RemoveLayoutConversions cleanup so scf.if non-convergence is non fatal" |
| `pr-triton-10183` | upstream-code | [`sources/prs/triton/PR-10183.md`](../sources/prs/triton/PR-10183.md) | [GLUON] Generalize `local_atomic_scatter_add` to `local_atomic_scatter_rmw` |
| `pr-triton-10186` | upstream-code | [`sources/prs/triton/PR-10186.md`](../sources/prs/triton/PR-10186.md) | [RUNTIME] Initialize profile scratch on stream 0 |
| `pr-triton-10189` | upstream-code | [`sources/prs/triton/PR-10189.md`](../sources/prs/triton/PR-10189.md) | Support returning tensors in TritonToTritonGPU |
| `pr-triton-10190` | upstream-code | [`sources/prs/triton/PR-10190.md`](../sources/prs/triton/PR-10190.md) | [mxfp4] Fix Hopper scale padding mask |
| `pr-triton-10194` | upstream-code | [`sources/prs/triton/PR-10194.md`](../sources/prs/triton/PR-10194.md) | [AMD] Fixing mi350 BlockPingpong update waits |
| `pr-triton-10196` | upstream-code | [`sources/prs/triton/PR-10196.md`](../sources/prs/triton/PR-10196.md) | [MULTICTA] Fix multicast pattern for tcgen05_mma_scaled |
| `pr-triton-10212` | upstream-code | [`sources/prs/triton/PR-10212.md`](../sources/prs/triton/PR-10212.md) | [CONSAN] Multi CTA model v2 |
| `pr-triton-10214` | upstream-code | [`sources/prs/triton/PR-10214.md`](../sources/prs/triton/PR-10214.md) | Allow MXFP8 LHS with Hopper-swizzled MXFP4 RHS |
| `pr-triton-10217` | upstream-code | [`sources/prs/triton/PR-10217.md`](../sources/prs/triton/PR-10217.md) | [ConSan] Fix missing captureBytes argument in passToWarpSpecialize call |
| `pr-triton-10222` | upstream-code | [`sources/prs/triton/PR-10222.md`](../sources/prs/triton/PR-10222.md) | [AMD][gfx1250] Add transposed support for 32x16 scaled WMMA |
| `pr-triton-10225` | upstream-code | [`sources/prs/triton/PR-10225.md`](../sources/prs/triton/PR-10225.md) | [AMD][gfx1250] Add `update_tensor_descriptor` op |
| `pr-triton-10230` | upstream-code | [`sources/prs/triton/PR-10230.md`](../sources/prs/triton/PR-10230.md) | [AMD][gfx1250] Combine redundant amdgpu.async_tdm_wait ops |
| `pr-triton-10231` | upstream-code | [`sources/prs/triton/PR-10231.md`](../sources/prs/triton/PR-10231.md) | [rel/3.7] Cherry pick "Sink tmem allocs after pipelining to reduce liveranges (#9093)" |
| `pr-triton-10234` | upstream-code | [`sources/prs/triton/PR-10234.md`](../sources/prs/triton/PR-10234.md) | [ BACKEND ]  Enable `tl.dot` with TF32 precision on tiles with N=8 and K=8 |
| `pr-triton-10236` | upstream-code | [`sources/prs/triton/PR-10236.md`](../sources/prs/triton/PR-10236.md) | Custom Intermediate split-k dtype  |
| `pr-triton-10242` | upstream-code | [`sources/prs/triton/PR-10242.md`](../sources/prs/triton/PR-10242.md) | Fix convert_layout lowering for CGA + slice layouts. |
| `pr-triton-10243` | upstream-code | [`sources/prs/triton/PR-10243.md`](../sources/prs/triton/PR-10243.md) | [BACKEND] Reinterpreted memory should represent the same amount of memory |
| `pr-triton-10249` | upstream-code | [`sources/prs/triton/PR-10249.md`](../sources/prs/triton/PR-10249.md) | [triton_kernels] nvfp4 x nvfp4 tuning |
| `pr-triton-10270` | upstream-code | [`sources/prs/triton/PR-10270.md`](../sources/prs/triton/PR-10270.md) | Fix negation of +0.0 |
| `pr-triton-10271` | upstream-code | [`sources/prs/triton/PR-10271.md`](../sources/prs/triton/PR-10271.md) | [PROTON] Group metadata kernels under the corresponding triton operator if available |
| `pr-triton-10275` | upstream-code | [`sources/prs/triton/PR-10275.md`](../sources/prs/triton/PR-10275.md) | Support zero-sized Hopper MX scale layouts |
| `pr-triton-10280` | upstream-code | [`sources/prs/triton/PR-10280.md`](../sources/prs/triton/PR-10280.md) | [BACKEND] Recognise fneg in clamp and use it in the MoE |
| `pr-triton-10286` | upstream-code | [`sources/prs/triton/PR-10286.md`](../sources/prs/triton/PR-10286.md) | [BACKEND] Allow reinterpret to modify the rank |
| `pr-triton-10295` | upstream-code | [`sources/prs/triton/PR-10295.md`](../sources/prs/triton/PR-10295.md) | [runtime] Skip None args in autotune restore_value/reset_to_zero hooks |
| `pr-triton-10303` | upstream-code | [`sources/prs/triton/PR-10303.md`](../sources/prs/triton/PR-10303.md) | Revert "Use ptxas 13.1.80 for all NVIDIA targets" |
| `pr-triton-10308` | upstream-code | [`sources/prs/triton/PR-10308.md`](../sources/prs/triton/PR-10308.md) | [CONSAN] Add smem and tmem initialization to NaN |
| `pr-triton-10318` | upstream-code | [`sources/prs/triton/PR-10318.md`](../sources/prs/triton/PR-10318.md) | Support MN-packing in decomposed fp4 dot_scaled |
| `pr-triton-10324` | upstream-code | [`sources/prs/triton/PR-10324.md`](../sources/prs/triton/PR-10324.md) | [BACKEND] Allow two_ctas=False barriers in TMA ops in a 2CTA kernel |
| `pr-triton-6896` | upstream-code | [`sources/prs/triton/PR-6896.md`](../sources/prs/triton/PR-6896.md) | [AxisInfo] Fix signed division AxisInfo bug and revert PyTorch workaround |
| `pr-triton-9572` | upstream-code | [`sources/prs/triton/PR-9572.md`](../sources/prs/triton/PR-9572.md) | [Language] Add field inheritance, defaults, and aggregate_replace to @aggregate |
| `pr-triton-9666` | upstream-code | [`sources/prs/triton/PR-9666.md`](../sources/prs/triton/PR-9666.md) | [AMD] Enable loop unrolling for Gluon warp-pipelined kernels |
| `pr-triton-9704` | upstream-code | [`sources/prs/triton/PR-9704.md`](../sources/prs/triton/PR-9704.md) | [PROTON] Migrate Proton ROCm backend from roctracer to rocprofiler-sdk |
| `pr-triton-9850` | upstream-code | [`sources/prs/triton/PR-9850.md`](../sources/prs/triton/PR-9850.md) | Add dense matmul benchmark for triton_kernels |
| `pr-triton-9883` | upstream-code | [`sources/prs/triton/PR-9883.md`](../sources/prs/triton/PR-9883.md) | [AMD][gfx9] Use asyncmark/wait_asyncmark for CDNA3/CDNA4 buffer_load_to_lds |

<a id="vllm-projectvllm"></a>
## vllm-project/vllm

1069 pages

| ID | Type | Path | Title |
| --- | --- | --- | --- |
| `pr-vllm-10995` | upstream-code | [`sources/prs/vllm/PR-10995.md`](../sources/prs/vllm/PR-10995.md) | [Kernel]: Cutlass 2:4 Sparsity + FP8/Int8 Quant Support |
| `pr-vllm-11698` | upstream-code | [`sources/prs/vllm/PR-11698.md`](../sources/prs/vllm/PR-11698.md) | [Kernel][Triton][AMD] Use block size heuristic for avg 2.8x speedup for int8 models |
| `pr-vllm-11743` | upstream-code | [`sources/prs/vllm/PR-11743.md`](../sources/prs/vllm/PR-11743.md) | [Core] Support fully transparent sleep mode |
| `pr-vllm-11844` | upstream-code | [`sources/prs/vllm/PR-11844.md`](../sources/prs/vllm/PR-11844.md) | Implements dual-chunk-flash-attn backend for dual chunk attention with sparse attention support |
| `pr-vllm-11868` | upstream-code | [`sources/prs/vllm/PR-11868.md`](../sources/prs/vllm/PR-11868.md) | [Kernel] Update `cutlass_scaled_mm` to support 2d group (blockwise) scaling |
| `pr-vllm-11981` | upstream-code | [`sources/prs/vllm/PR-11981.md`](../sources/prs/vllm/PR-11981.md) | [Platform] Add output for Attention Backend |
| `pr-vllm-12049` | upstream-code | [`sources/prs/vllm/PR-12049.md`](../sources/prs/vllm/PR-12049.md) | [ROCm][MoE] moe tuning support for rocm |
| `pr-vllm-12093` | upstream-code | [`sources/prs/vllm/PR-12093.md`](../sources/prs/vllm/PR-12093.md) | [Kernel] Flash Attention 3 Support |
| `pr-vllm-12097` | upstream-code | [`sources/prs/vllm/PR-12097.md`](../sources/prs/vllm/PR-12097.md) | Add: Support for Sparse24Bitmask Compressed Models |
| `pr-vllm-12185` | upstream-code | [`sources/prs/vllm/PR-12185.md`](../sources/prs/vllm/PR-12185.md) | [Kernel] add triton fused moe kernel for gptq/awq |
| `pr-vllm-12218` | upstream-code | [`sources/prs/vllm/PR-12218.md`](../sources/prs/vllm/PR-12218.md) | [Misc] Pass `attention` to impl backend |
| `pr-vllm-12222` | upstream-code | [`sources/prs/vllm/PR-12222.md`](../sources/prs/vllm/PR-12222.md) | [Kernel] optimize moe_align_block_size for cuda graph and large num_experts (e.g. DeepSeek-V3) |
| `pr-vllm-12282` | upstream-code | [`sources/prs/vllm/PR-12282.md`](../sources/prs/vllm/PR-12282.md) | [AMD][Quantization] Add TritonScaledMMLinearKernel since int8 is broken for AMD |
| `pr-vllm-12303` | upstream-code | [`sources/prs/vllm/PR-12303.md`](../sources/prs/vllm/PR-12303.md) | [Hardware][Gaudi][Feature] Enable Dynamic MoE for Mixtral |
| `pr-vllm-12348` | upstream-code | [`sources/prs/vllm/PR-12348.md`](../sources/prs/vllm/PR-12348.md) | [ROCm] Faster Custom Paged Attention kernels |
| `pr-vllm-12417` | upstream-code | [`sources/prs/vllm/PR-12417.md`](../sources/prs/vllm/PR-12417.md) | [Bugfix] Disable w16a16 2of4 sparse CompressedTensors24 |
| `pr-vllm-12517` | upstream-code | [`sources/prs/vllm/PR-12517.md`](../sources/prs/vllm/PR-12517.md) | Fix: Respect `sparsity_config.ignore` in Cutlass Integration |
| `pr-vllm-12528` | upstream-code | [`sources/prs/vllm/PR-12528.md`](../sources/prs/vllm/PR-12528.md) | [Attention] MLA decode optimizations |
| `pr-vllm-12558` | upstream-code | [`sources/prs/vllm/PR-12558.md`](../sources/prs/vllm/PR-12558.md) | [Misc][MoE] add Deepseek-V3 moe tuning support |
| `pr-vllm-12562` | upstream-code | [`sources/prs/vllm/PR-12562.md`](../sources/prs/vllm/PR-12562.md) | [Bugfix/CI] Fixup benchmark_moe.py |
| `pr-vllm-12574` | upstream-code | [`sources/prs/vllm/PR-12574.md`](../sources/prs/vllm/PR-12574.md) | [Kernel] port sgl moe_align_block_size kernels |
| `pr-vllm-12583` | upstream-code | [`sources/prs/vllm/PR-12583.md`](../sources/prs/vllm/PR-12583.md) | Expert Parallelism (EP) Support for DeepSeek Models |
| `pr-vllm-12587` | upstream-code | [`sources/prs/vllm/PR-12587.md`](../sources/prs/vllm/PR-12587.md) | [Kernel][Quantization] Integrate block-quantized CUTLASS kernels for DeepSeekV3 |
| `pr-vllm-12601` | upstream-code | [`sources/prs/vllm/PR-12601.md`](../sources/prs/vllm/PR-12601.md) | [Attention] Deepseek v3 MLA support with FP8 compute |
| `pr-vllm-12604` | upstream-code | [`sources/prs/vllm/PR-12604.md`](../sources/prs/vllm/PR-12604.md) | [VLM] Qwen2.5-VL |
| `pr-vllm-12637` | upstream-code | [`sources/prs/vllm/PR-12637.md`](../sources/prs/vllm/PR-12637.md) | Apply torch.compile to fused_moe/grouped_topk |
| `pr-vllm-12639` | upstream-code | [`sources/prs/vllm/PR-12639.md`](../sources/prs/vllm/PR-12639.md) | [Attention] MLA with chunked prefill |
| `pr-vllm-12662` | upstream-code | [`sources/prs/vllm/PR-12662.md`](../sources/prs/vllm/PR-12662.md) | [AMD][ROCm] Enable DeepSeek model on ROCm |
| `pr-vllm-12676` | upstream-code | [`sources/prs/vllm/PR-12676.md`](../sources/prs/vllm/PR-12676.md) | [Perf] Mem align KV caches for CUDA devices (MLA perf improvement) |
| `pr-vllm-12695` | upstream-code | [`sources/prs/vllm/PR-12695.md`](../sources/prs/vllm/PR-12695.md) | [Core][AMD] Migrate fully transparent sleep mode to ROCm platform |
| `pr-vllm-12696` | upstream-code | [`sources/prs/vllm/PR-12696.md`](../sources/prs/vllm/PR-12696.md) | [Bugfix][Kernel] Fix per-token/per-channel quantization for Hopper scaled mm |
| `pr-vllm-12721` | upstream-code | [`sources/prs/vllm/PR-12721.md`](../sources/prs/vllm/PR-12721.md) | Update to torch==2.6.0 |
| `pr-vllm-12729` | upstream-code | [`sources/prs/vllm/PR-12729.md`](../sources/prs/vllm/PR-12729.md) | [VLM] Add MLA with pure RoPE support for deepseek-vl2 models |
| `pr-vllm-12755` | upstream-code | [`sources/prs/vllm/PR-12755.md`](../sources/prs/vllm/PR-12755.md) | [Model][Speculative Decoding] DeepSeek MTP spec decode |
| `pr-vllm-12757` | upstream-code | [`sources/prs/vllm/PR-12757.md`](../sources/prs/vllm/PR-12757.md) | [Misc] Update w2 scale loading for GPTQMarlinMoE |
| `pr-vllm-12777` | upstream-code | [`sources/prs/vllm/PR-12777.md`](../sources/prs/vllm/PR-12777.md) | [Kernel] Make rotary_embedding ops more flexible with input shape |
| `pr-vllm-12784` | upstream-code | [`sources/prs/vllm/PR-12784.md`](../sources/prs/vllm/PR-12784.md) | [NVIDIA] Support nvfp4 quantization |
| `pr-vllm-12796` | upstream-code | [`sources/prs/vllm/PR-12796.md`](../sources/prs/vllm/PR-12796.md) | [Bugfix] Better FP8 supported defaults |
| `pr-vllm-12807` | upstream-code | [`sources/prs/vllm/PR-12807.md`](../sources/prs/vllm/PR-12807.md) | [Attention] Use FA3 for MLA on Hopper |
| `pr-vllm-12850` | upstream-code | [`sources/prs/vllm/PR-12850.md`](../sources/prs/vllm/PR-12850.md) | Optimize moe_align_block_size for deepseek_v3 |
| `pr-vllm-12931` | upstream-code | [`sources/prs/vllm/PR-12931.md`](../sources/prs/vllm/PR-12931.md) | [Misc][Kernel]: Add GPTQAllSpark Quantization |
| `pr-vllm-12959` | upstream-code | [`sources/prs/vllm/PR-12959.md`](../sources/prs/vllm/PR-12959.md) | [bugfix] fix early import of flash attention |
| `pr-vllm-12978` | upstream-code | [`sources/prs/vllm/PR-12978.md`](../sources/prs/vllm/PR-12978.md) | [Kernel]Add streamK for block-quantized CUTLASS kernels |
| `pr-vllm-13111` | upstream-code | [`sources/prs/vllm/PR-13111.md`](../sources/prs/vllm/PR-13111.md) | [Attention] Update to lastest FA3 code |
| `pr-vllm-13167` | upstream-code | [`sources/prs/vllm/PR-13167.md`](../sources/prs/vllm/PR-13167.md) | [Model] Deepseek GGUF support  |
| `pr-vllm-13181` | upstream-code | [`sources/prs/vllm/PR-13181.md`](../sources/prs/vllm/PR-13181.md) | Expand MLA to support most types of quantization |
| `pr-vllm-13198` | upstream-code | [`sources/prs/vllm/PR-13198.md`](../sources/prs/vllm/PR-13198.md) | [Kernel][Bugfix] Refactor and Fix CUTLASS 2:4 Sparse Kernels |
| `pr-vllm-13236` | upstream-code | [`sources/prs/vllm/PR-13236.md`](../sources/prs/vllm/PR-13236.md) | [Quant][Perf] Use moe_wna16 kernel by default for MoEs with many experts |
| `pr-vllm-13310` | upstream-code | [`sources/prs/vllm/PR-13310.md`](../sources/prs/vllm/PR-13310.md) | [Bugfix] Massage MLA's usage of flash attn for RoCM |
| `pr-vllm-13321` | upstream-code | [`sources/prs/vllm/PR-13321.md`](../sources/prs/vllm/PR-13321.md) | [Kernel] moe wna16 cuda kernel |
| `pr-vllm-13571` | upstream-code | [`sources/prs/vllm/PR-13571.md`](../sources/prs/vllm/PR-13571.md) | [NVIDIA] Support nvfp4 cutlass gemm |
| `pr-vllm-13591` | upstream-code | [`sources/prs/vllm/PR-13591.md`](../sources/prs/vllm/PR-13591.md) | [core] set up data parallel communication |
| `pr-vllm-13625` | upstream-code | [`sources/prs/vllm/PR-13625.md`](../sources/prs/vllm/PR-13625.md) | [Kernel] Optimize moe intermediate_cache usage |
| `pr-vllm-13626` | upstream-code | [`sources/prs/vllm/PR-13626.md`](../sources/prs/vllm/PR-13626.md) | [Model][Speculative Decoding] Expand DeepSeek MTP code to support k > n_predict |
| `pr-vllm-13650` | upstream-code | [`sources/prs/vllm/PR-13650.md`](../sources/prs/vllm/PR-13650.md) | [ROCM] fix native attention function call |
| `pr-vllm-13693` | upstream-code | [`sources/prs/vllm/PR-13693.md`](../sources/prs/vllm/PR-13693.md) | [BugFix]  Illegal memory access for MoE On H20 |
| `pr-vllm-13706` | upstream-code | [`sources/prs/vllm/PR-13706.md`](../sources/prs/vllm/PR-13706.md) | [BugFix] Minor: logger import in attention backend |
| `pr-vllm-13718` | upstream-code | [`sources/prs/vllm/PR-13718.md`](../sources/prs/vllm/PR-13718.md) | [core] Perf improvement for DSv3 on AMD GPUs |
| `pr-vllm-13725` | upstream-code | [`sources/prs/vllm/PR-13725.md`](../sources/prs/vllm/PR-13725.md) | [Bugfix] Support MLA for CompressedTensorsWNA16 |
| `pr-vllm-13726` | upstream-code | [`sources/prs/vllm/PR-13726.md`](../sources/prs/vllm/PR-13726.md) | [V1] V1 Enablement Oracle  |
| `pr-vllm-13747` | upstream-code | [`sources/prs/vllm/PR-13747.md`](../sources/prs/vllm/PR-13747.md) | [Kernel] FlashMLA integration |
| `pr-vllm-13769` | upstream-code | [`sources/prs/vllm/PR-13769.md`](../sources/prs/vllm/PR-13769.md) | Fix CompressedTensorsWNA16MoE with grouped scales |
| `pr-vllm-13772` | upstream-code | [`sources/prs/vllm/PR-13772.md`](../sources/prs/vllm/PR-13772.md) | Fix precommit fail in fused_moe intermediate_cache2 chunking |
| `pr-vllm-13784` | upstream-code | [`sources/prs/vllm/PR-13784.md`](../sources/prs/vllm/PR-13784.md) | [Bugfix][Quantization] Fix FP8 + EP |
| `pr-vllm-13789` | upstream-code | [`sources/prs/vllm/PR-13789.md`](../sources/prs/vllm/PR-13789.md) | [Attention] MLA support for V1 |
| `pr-vllm-13798` | upstream-code | [`sources/prs/vllm/PR-13798.md`](../sources/prs/vllm/PR-13798.md) | add cutlass support for blackwell fp8 gemm |
| `pr-vllm-13844` | upstream-code | [`sources/prs/vllm/PR-13844.md`](../sources/prs/vllm/PR-13844.md) | [ROCm] Disable chunked prefill/prefix caching when running MLA on non-cuda platforms |
| `pr-vllm-13867` | upstream-code | [`sources/prs/vllm/PR-13867.md`](../sources/prs/vllm/PR-13867.md) | [Attention] Flash MLA for V1 |
| `pr-vllm-13897` | upstream-code | [`sources/prs/vllm/PR-13897.md`](../sources/prs/vllm/PR-13897.md) | Fix mla prefill context performance |
| `pr-vllm-13917` | upstream-code | [`sources/prs/vllm/PR-13917.md`](../sources/prs/vllm/PR-13917.md) | Add benchmark for DeepGEMM and vLLM Block FP8 Dense GEMM |
| `pr-vllm-13922` | upstream-code | [`sources/prs/vllm/PR-13922.md`](../sources/prs/vllm/PR-13922.md) | [ROCm][V1] Update reshape_and_cache to properly work with CUDA graph padding |
| `pr-vllm-13931` | upstream-code | [`sources/prs/vllm/PR-13931.md`](../sources/prs/vllm/PR-13931.md) | [V1] EP/TP MoE + DP Attention |
| `pr-vllm-13932` | upstream-code | [`sources/prs/vllm/PR-13932.md`](../sources/prs/vllm/PR-13932.md) | Add option to use DeepGemm contiguous grouped gemm kernel for fused MoE operations. |
| `pr-vllm-13972` | upstream-code | [`sources/prs/vllm/PR-13972.md`](../sources/prs/vllm/PR-13972.md) | [Kernel] CUTLASS grouped gemm fp8 MoE kernel |
| `pr-vllm-13974` | upstream-code | [`sources/prs/vllm/PR-13974.md`](../sources/prs/vllm/PR-13974.md) | [Misc] Print FusedMoE detail info |
| `pr-vllm-14068` | upstream-code | [`sources/prs/vllm/PR-14068.md`](../sources/prs/vllm/PR-14068.md) | [core] moe fp8 block quant tuning support |
| `pr-vllm-14071` | upstream-code | [`sources/prs/vllm/PR-14071.md`](../sources/prs/vllm/PR-14071.md) | [V1] Enable Triton(ROCm) Attention backend for Nvidia GPUs |
| `pr-vllm-14138` | upstream-code | [`sources/prs/vllm/PR-14138.md`](../sources/prs/vllm/PR-14138.md) | [Kernel] optimize performance of gptq marlin kernel when n is small |
| `pr-vllm-14155` | upstream-code | [`sources/prs/vllm/PR-14155.md`](../sources/prs/vllm/PR-14155.md) | [v1] Add comments to the new ragged paged attention Pallas kernel |
| `pr-vllm-14164` | upstream-code | [`sources/prs/vllm/PR-14164.md`](../sources/prs/vllm/PR-14164.md) | Fix benchmark_moe.py tuning for CUDA devices |
| `pr-vllm-14221` | upstream-code | [`sources/prs/vllm/PR-14221.md`](../sources/prs/vllm/PR-14221.md) | [V1][Bugfix] Standardize quantized kv cache rejection for attention backends |
| `pr-vllm-14227` | upstream-code | [`sources/prs/vllm/PR-14227.md`](../sources/prs/vllm/PR-14227.md) | [V1][TPU] Support V1 Sampler for ragged attention |
| `pr-vllm-14244` | upstream-code | [`sources/prs/vllm/PR-14244.md`](../sources/prs/vllm/PR-14244.md) | [Hardware] Update the flash attn tag to support Blackwell |
| `pr-vllm-14245` | upstream-code | [`sources/prs/vllm/PR-14245.md`](../sources/prs/vllm/PR-14245.md) | dynamic distpatch of fp8 kernels |
| `pr-vllm-14253` | upstream-code | [`sources/prs/vllm/PR-14253.md`](../sources/prs/vllm/PR-14253.md) | [BugFix] MLA + V1, illegal memory access and accuracy issues |
| `pr-vllm-14255` | upstream-code | [`sources/prs/vllm/PR-14255.md`](../sources/prs/vllm/PR-14255.md) | [BugFix] Fix prefix caching V0 MLA |
| `pr-vllm-14258` | upstream-code | [`sources/prs/vllm/PR-14258.md`](../sources/prs/vllm/PR-14258.md) | [Attention] FlashAttn MLA |
| `pr-vllm-14276` | upstream-code | [`sources/prs/vllm/PR-14276.md`](../sources/prs/vllm/PR-14276.md) | [Misc] Add Qwen2MoeForCausalLM moe tuning support  |
| `pr-vllm-14310` | upstream-code | [`sources/prs/vllm/PR-14310.md`](../sources/prs/vllm/PR-14310.md) | [Hardware][TPU]Enable ragged paged attention kernel and resolve recompilation issue |
| `pr-vllm-14313` | upstream-code | [`sources/prs/vllm/PR-14313.md`](../sources/prs/vllm/PR-14313.md) | [Bug] Fix Attention when ignored in by quant_method |
| `pr-vllm-14316` | upstream-code | [`sources/prs/vllm/PR-14316.md`](../sources/prs/vllm/PR-14316.md) | [ROCm] Enable chunked prefill/paged attention in MLA on ROCm |
| `pr-vllm-14323` | upstream-code | [`sources/prs/vllm/PR-14323.md`](../sources/prs/vllm/PR-14323.md) | [Model] Add PLaMo2 |
| `pr-vllm-14327` | upstream-code | [`sources/prs/vllm/PR-14327.md`](../sources/prs/vllm/PR-14327.md) | fix minor miscalled method |
| `pr-vllm-14354` | upstream-code | [`sources/prs/vllm/PR-14354.md`](../sources/prs/vllm/PR-14354.md) | [Build/BugFix] Fix hopper 12.8 build |
| `pr-vllm-14383` | upstream-code | [`sources/prs/vllm/PR-14383.md`](../sources/prs/vllm/PR-14383.md) | Add cutlass support for blackwell fp8 blockwise gemm |
| `pr-vllm-14384` | upstream-code | [`sources/prs/vllm/PR-14384.md`](../sources/prs/vllm/PR-14384.md) | [Perf] Reduce MLA CPU overheads in V1 |
| `pr-vllm-14390` | upstream-code | [`sources/prs/vllm/PR-14390.md`](../sources/prs/vllm/PR-14390.md) | [FP8] Refactor apply_fp8_linear and apply_fp8_linear_generic into an object |
| `pr-vllm-14396` | upstream-code | [`sources/prs/vllm/PR-14396.md`](../sources/prs/vllm/PR-14396.md) | [BugFix] Illegal Memory Access in the blockwise cutlass fp8 GEMMs |
| `pr-vllm-14447` | upstream-code | [`sources/prs/vllm/PR-14447.md`](../sources/prs/vllm/PR-14447.md) | [Kernel] moe wna16 marlin kernel |
| `pr-vllm-14451` | upstream-code | [`sources/prs/vllm/PR-14451.md`](../sources/prs/vllm/PR-14451.md) | [Attention] Default to FlashMLA backend for MLA |
| `pr-vllm-14454` | upstream-code | [`sources/prs/vllm/PR-14454.md`](../sources/prs/vllm/PR-14454.md) | [ROCm][Kernel] MoE weights padding |
| `pr-vllm-14476` | upstream-code | [`sources/prs/vllm/PR-14476.md`](../sources/prs/vllm/PR-14476.md) | [Bugfix] DeepSeek Accuracy |
| `pr-vllm-14540` | upstream-code | [`sources/prs/vllm/PR-14540.md`](../sources/prs/vllm/PR-14540.md) | [Perf] Improve MLA on V1 |
| `pr-vllm-14568` | upstream-code | [`sources/prs/vllm/PR-14568.md`](../sources/prs/vllm/PR-14568.md) | permute/unpermute kernel for moe optimization |
| `pr-vllm-14570` | upstream-code | [`sources/prs/vllm/PR-14570.md`](../sources/prs/vllm/PR-14570.md) | [Attention] Flash Attention 3 - fp8 |
| `pr-vllm-14572` | upstream-code | [`sources/prs/vllm/PR-14572.md`](../sources/prs/vllm/PR-14572.md) | [BugFix/Build] Fix sparse kernels not getting built on hopper |
| `pr-vllm-14578` | upstream-code | [`sources/prs/vllm/PR-14578.md`](../sources/prs/vllm/PR-14578.md) | [Quantization][FP8] Adding support for fp8 gemm layer input in fp8 |
| `pr-vllm-14613` | upstream-code | [`sources/prs/vllm/PR-14613.md`](../sources/prs/vllm/PR-14613.md) | [Kernel] GGUF MoE kernel |
| `pr-vllm-14653` | upstream-code | [`sources/prs/vllm/PR-14653.md`](../sources/prs/vllm/PR-14653.md) | [Bugfix] fix benchmark moe |
| `pr-vllm-14658` | upstream-code | [`sources/prs/vllm/PR-14658.md`](../sources/prs/vllm/PR-14658.md) | [Kernel] allow non-contiguous input for marlin kernel |
| `pr-vllm-14660` | upstream-code | [`sources/prs/vllm/PR-14660.md`](../sources/prs/vllm/PR-14660.md) | [Model] Add support for Gemma 3 |
| `pr-vllm-14681` | upstream-code | [`sources/prs/vllm/PR-14681.md`](../sources/prs/vllm/PR-14681.md) | [Bugfix][IPEX] Add `VLLM_CPU_MOE_PREPACK` to allow disabling MoE prepack when CPU does not support it |
| `pr-vllm-14712` | upstream-code | [`sources/prs/vllm/PR-14712.md`](../sources/prs/vllm/PR-14712.md) | [Neuron] flatten test parameterization for neuron attention kernels |
| `pr-vllm-14744` | upstream-code | [`sources/prs/vllm/PR-14744.md`](../sources/prs/vllm/PR-14744.md) | [Kernel][CPU] CPU MLA |
| `pr-vllm-14770` | upstream-code | [`sources/prs/vllm/PR-14770.md`](../sources/prs/vllm/PR-14770.md) | [Attention] MLA get rid of materialization |
| `pr-vllm-14796` | upstream-code | [`sources/prs/vllm/PR-14796.md`](../sources/prs/vllm/PR-14796.md) | [Bugfix][W8A8] fixed cutlass block fp8 binding |
| `pr-vllm-14842` | upstream-code | [`sources/prs/vllm/PR-14842.md`](../sources/prs/vllm/PR-14842.md) | [Attention] Get rid of mla cache alignment |
| `pr-vllm-14877` | upstream-code | [`sources/prs/vllm/PR-14877.md`](../sources/prs/vllm/PR-14877.md) | [Kernel] Add more tuned configs |
| `pr-vllm-14967` | upstream-code | [`sources/prs/vllm/PR-14967.md`](../sources/prs/vllm/PR-14967.md) | [FEAT][ROCm] Integrate Fused MoE Kernels from AITER |
| `pr-vllm-14968` | upstream-code | [`sources/prs/vllm/PR-14968.md`](../sources/prs/vllm/PR-14968.md) | [FEAT] [ROCm]: Add AITER Block-Scaled GEMM Feature |
| `pr-vllm-14987` | upstream-code | [`sources/prs/vllm/PR-14987.md`](../sources/prs/vllm/PR-14987.md) | MI325 configs, fused_moe_kernel bugfix |
| `pr-vllm-15001` | upstream-code | [`sources/prs/vllm/PR-15001.md`](../sources/prs/vllm/PR-15001.md) | [FEAT][ROCm] Integrate Paged Attention Kernel from AITER |
| `pr-vllm-15099` | upstream-code | [`sources/prs/vllm/PR-15099.md`](../sources/prs/vllm/PR-15099.md) | [Bugfix][Misc] Use TritonPlaceholderModule to defensively import triton |
| `pr-vllm-15200` | upstream-code | [`sources/prs/vllm/PR-15200.md`](../sources/prs/vllm/PR-15200.md) | [Bugfix] Fix incorrect qwen2.5-vl attention mask pre-computation |
| `pr-vllm-15322` | upstream-code | [`sources/prs/vllm/PR-15322.md`](../sources/prs/vllm/PR-15322.md) | [Misc] Add tuned R1 w8a8 and MoE configs for NVIDIA L20 |
| `pr-vllm-15354` | upstream-code | [`sources/prs/vllm/PR-15354.md`](../sources/prs/vllm/PR-15354.md) | [V1] Fully Transparent Implementation of CPU Offloading |
| `pr-vllm-15433` | upstream-code | [`sources/prs/vllm/PR-15433.md`](../sources/prs/vllm/PR-15433.md) | [FEAT] [ROCm] Add AITER int8 scaled gemm kernel |
| `pr-vllm-15456` | upstream-code | [`sources/prs/vllm/PR-15456.md`](../sources/prs/vllm/PR-15456.md) | [Kernel] Fix conflicting macro names for gguf kernels |
| `pr-vllm-15492` | upstream-code | [`sources/prs/vllm/PR-15492.md`](../sources/prs/vllm/PR-15492.md) | [BugFix] Fix nightly MLA failure (FA2 + MLA chunked prefill, i.e. V1, producing bad results) |
| `pr-vllm-15511` | upstream-code | [`sources/prs/vllm/PR-15511.md`](../sources/prs/vllm/PR-15511.md) | Use Cache Hinting for fused_moe kernel |
| `pr-vllm-15515` | upstream-code | [`sources/prs/vllm/PR-15515.md`](../sources/prs/vllm/PR-15515.md) | [moe][quant] add weight name case for offset |
| `pr-vllm-15587` | upstream-code | [`sources/prs/vllm/PR-15587.md`](../sources/prs/vllm/PR-15587.md) | [Quantization] Fp8 Channelwise Dynamic Per Token GroupedGEMM |
| `pr-vllm-15589` | upstream-code | [`sources/prs/vllm/PR-15589.md`](../sources/prs/vllm/PR-15589.md) | [TPU] Avoid Triton Import |
| `pr-vllm-15720` | upstream-code | [`sources/prs/vllm/PR-15720.md`](../sources/prs/vllm/PR-15720.md) | [ROCM][KERNEL] Paged attention for V1 |
| `pr-vllm-15732` | upstream-code | [`sources/prs/vllm/PR-15732.md`](../sources/prs/vllm/PR-15732.md) | [TPU] Support sliding window and logit soft capping in the paged attention kernel for TPU. |
| `pr-vllm-15834` | upstream-code | [`sources/prs/vllm/PR-15834.md`](../sources/prs/vllm/PR-15834.md) | [V1] TPU - Fix fused MOE |
| `pr-vllm-15841` | upstream-code | [`sources/prs/vllm/PR-15841.md`](../sources/prs/vllm/PR-15841.md) | [Bugfix] Fix imports for MoE on CPU |
| `pr-vllm-15893` | upstream-code | [`sources/prs/vllm/PR-15893.md`](../sources/prs/vllm/PR-15893.md) | [FEAT][ROCm]: Support AITER MLA |
| `pr-vllm-15914` | upstream-code | [`sources/prs/vllm/PR-15914.md`](../sources/prs/vllm/PR-15914.md) | [Minor] Fused experts refactor |
| `pr-vllm-15945` | upstream-code | [`sources/prs/vllm/PR-15945.md`](../sources/prs/vllm/PR-15945.md) | [Hardware][Gaudi][BugFix] fix arguments of hpu fused moe |
| `pr-vllm-15946` | upstream-code | [`sources/prs/vllm/PR-15946.md`](../sources/prs/vllm/PR-15946.md) | [Bugfix] fix use_atomic_add support of marlin kernel when using v1 engine |
| `pr-vllm-15956` | upstream-code | [`sources/prs/vllm/PR-15956.md`](../sources/prs/vllm/PR-15956.md) | Modularize fused experts and integrate PPLX kernels |
| `pr-vllm-15960` | upstream-code | [`sources/prs/vllm/PR-15960.md`](../sources/prs/vllm/PR-15960.md) | [P/D][V1] KV Connector API V1 |
| `pr-vllm-15961` | upstream-code | [`sources/prs/vllm/PR-15961.md`](../sources/prs/vllm/PR-15961.md) | Add support to modelopt quantization of Mixtral model |
| `pr-vllm-16032` | upstream-code | [`sources/prs/vllm/PR-16032.md`](../sources/prs/vllm/PR-16032.md) | [NVIDIA] Support Cutlass MLA for Blackwell GPUs |
| `pr-vllm-16034` | upstream-code | [`sources/prs/vllm/PR-16034.md`](../sources/prs/vllm/PR-16034.md) | [ROCM] Add gfx950 to the custom attention archs |
| `pr-vllm-16038` | upstream-code | [`sources/prs/vllm/PR-16038.md`](../sources/prs/vllm/PR-16038.md) | [Kernel] Use moe_wna16 kernel for compressed tensors wna16 moe models |
| `pr-vllm-16041` | upstream-code | [`sources/prs/vllm/PR-16041.md`](../sources/prs/vllm/PR-16041.md) | [TPU][V1] Remove ragged attention kernel parameter hard coding |
| `pr-vllm-16071` | upstream-code | [`sources/prs/vllm/PR-16071.md`](../sources/prs/vllm/PR-16071.md) | [Kernel][Bugfix] Re-fuse triton moe weight application |
| `pr-vllm-16072` | upstream-code | [`sources/prs/vllm/PR-16072.md`](../sources/prs/vllm/PR-16072.md) | [Core] Support full cuda graph in v1 |
| `pr-vllm-16078` | upstream-code | [`sources/prs/vllm/PR-16078.md`](../sources/prs/vllm/PR-16078.md) | Add FlexAttention to V1 |
| `pr-vllm-16113` | upstream-code | [`sources/prs/vllm/PR-16113.md`](../sources/prs/vllm/PR-16113.md) | Upstream Llama4 Support to Main |
| `pr-vllm-16173` | upstream-code | [`sources/prs/vllm/PR-16173.md`](../sources/prs/vllm/PR-16173.md) | [Kernel] support merge_attn_states CUDA kernel, 3x speedup |
| `pr-vllm-16198` | upstream-code | [`sources/prs/vllm/PR-16198.md`](../sources/prs/vllm/PR-16198.md) | [Bug] [ROCm] Fix Llama 4 Enablement Bug on ROCm: V0 ROCmFlashAttentionImpl and Triton Fused MoE bugs |
| `pr-vllm-16212` | upstream-code | [`sources/prs/vllm/PR-16212.md`](../sources/prs/vllm/PR-16212.md) | Add warning for Attention backends that do not support irope yet |
| `pr-vllm-16247` | upstream-code | [`sources/prs/vllm/PR-16247.md`](../sources/prs/vllm/PR-16247.md) | [BugFix][ROCm] Fix GGUF MoE Dispatch Block_Dim for ROCm |
| `pr-vllm-16263` | upstream-code | [`sources/prs/vllm/PR-16263.md`](../sources/prs/vllm/PR-16263.md) | [Hardware][AMD] Improve OAM device ID + llama4 Maverick MOE tuning |
| `pr-vllm-16362` | upstream-code | [`sources/prs/vllm/PR-16362.md`](../sources/prs/vllm/PR-16362.md) | [Hardware/NVIDIA/Kernel] [Functional Enablement] [1/N] Enable nvidia/DeepSeek-R1-FP4 Model |
| `pr-vllm-16366` | upstream-code | [`sources/prs/vllm/PR-16366.md`](../sources/prs/vllm/PR-16366.md) | [Kernel] Support W8A8 channel-wise weights and per-token activations in triton fused_moe_kernel |
| `pr-vllm-16387` | upstream-code | [`sources/prs/vllm/PR-16387.md`](../sources/prs/vllm/PR-16387.md) | [Model][VLM] Add Kimi-VL model support |
| `pr-vllm-16431` | upstream-code | [`sources/prs/vllm/PR-16431.md`](../sources/prs/vllm/PR-16431.md) | [ROCm] [Attention] Cleanup ROCm output passing |
| `pr-vllm-16457` | upstream-code | [`sources/prs/vllm/PR-16457.md`](../sources/prs/vllm/PR-16457.md) | [Perf]Optimize rotary_emb implementation to use Triton operator for improved inference performance |
| `pr-vllm-16537` | upstream-code | [`sources/prs/vllm/PR-16537.md`](../sources/prs/vllm/PR-16537.md) | Enable PTPC FP8 for CompressedTensorsW8A8Fp8MoEMethod (triton fused_moe) |
| `pr-vllm-16601` | upstream-code | [`sources/prs/vllm/PR-16601.md`](../sources/prs/vllm/PR-16601.md) | [Bugfix] Move current_platform import to avoid python import cache. |
| `pr-vllm-16605` | upstream-code | [`sources/prs/vllm/PR-16605.md`](../sources/prs/vllm/PR-16605.md) | Allocate kv_cache with stride order |
| `pr-vllm-16673` | upstream-code | [`sources/prs/vllm/PR-16673.md`](../sources/prs/vllm/PR-16673.md) | [MLA] Simplification to batch P/D reordering |
| `pr-vllm-16674` | upstream-code | [`sources/prs/vllm/PR-16674.md`](../sources/prs/vllm/PR-16674.md) | [ROCM] enable aiter fused moe kernel for llama4 bf16 checkpoints |
| `pr-vllm-16684` | upstream-code | [`sources/prs/vllm/PR-16684.md`](../sources/prs/vllm/PR-16684.md) | [V1] V1 FlashInfer Attention |
| `pr-vllm-16693` | upstream-code | [`sources/prs/vllm/PR-16693.md`](../sources/prs/vllm/PR-16693.md) | [Bugfix][Kernel] fix potential cuda graph broken for merge_attn_states kernel |
| `pr-vllm-16727` | upstream-code | [`sources/prs/vllm/PR-16727.md`](../sources/prs/vllm/PR-16727.md) | [ROCm] Add aiter tkw1 kernel for Llama4 fp8 |
| `pr-vllm-16745` | upstream-code | [`sources/prs/vllm/PR-16745.md`](../sources/prs/vllm/PR-16745.md) | Support W8A8 INT8 MoE for compressed-tensors |
| `pr-vllm-16751` | upstream-code | [`sources/prs/vllm/PR-16751.md`](../sources/prs/vllm/PR-16751.md) | [Bugfix] Fix cutlass dispatch for fp8/int8 to properly invoke M<=16 c… |
| `pr-vllm-16752` | upstream-code | [`sources/prs/vllm/PR-16752.md`](../sources/prs/vllm/PR-16752.md) | [FEAT] [ROCm]: AITER Fused MOE V1 Support |
| `pr-vllm-16756` | upstream-code | [`sources/prs/vllm/PR-16756.md`](../sources/prs/vllm/PR-16756.md) | [torch.compile][ROCm] Fuse quantization onto attention using a torch.compile pass |
| `pr-vllm-16780` | upstream-code | [`sources/prs/vllm/PR-16780.md`](../sources/prs/vllm/PR-16780.md) | [Kernel] GGUF MoeVec kernel |
| `pr-vllm-16801` | upstream-code | [`sources/prs/vllm/PR-16801.md`](../sources/prs/vllm/PR-16801.md) | [BugFix] Accuracy fix for llama4 int4 - improperly casted scales |
| `pr-vllm-16828` | upstream-code | [`sources/prs/vllm/PR-16828.md`](../sources/prs/vllm/PR-16828.md) | [Kernel] Unified Triton kernel that doesn't distinguish between prefill + decode |
| `pr-vllm-16850` | upstream-code | [`sources/prs/vllm/PR-16850.md`](../sources/prs/vllm/PR-16850.md) | [Kernel] some optimizations for dense marlin and moe marlin |
| `pr-vllm-16854` | upstream-code | [`sources/prs/vllm/PR-16854.md`](../sources/prs/vllm/PR-16854.md) | [Bugfix] Fix moe weight losing all extra attrs after `process_weights_after_loading`. |
| `pr-vllm-16859` | upstream-code | [`sources/prs/vllm/PR-16859.md`](../sources/prs/vllm/PR-16859.md) | Update PyTorch to 2.7.0 |
| `pr-vllm-16861` | upstream-code | [`sources/prs/vllm/PR-16861.md`](../sources/prs/vllm/PR-16861.md) | [Kernel] Add expert_map support to Cutlass FP8 MOE |
| `pr-vllm-16902` | upstream-code | [`sources/prs/vllm/PR-16902.md`](../sources/prs/vllm/PR-16902.md) | [Bugfix] Triton FA function takes no keyword arguments |
| `pr-vllm-16937` | upstream-code | [`sources/prs/vllm/PR-16937.md`](../sources/prs/vllm/PR-16937.md) | [V1][Spec Decode] EAGLE-3 Support |
| `pr-vllm-17004` | upstream-code | [`sources/prs/vllm/PR-17004.md`](../sources/prs/vllm/PR-17004.md) | [ROCm][Kernel][V1] Enable AMD Radeon GPU Custom Paged Attention on v1 |
| `pr-vllm-17082` | upstream-code | [`sources/prs/vllm/PR-17082.md`](../sources/prs/vllm/PR-17082.md) | Fix `numel()` downcast in vllm/csrc/moe/moe_align_sum_kernels.cu +2 |
| `pr-vllm-17091` | upstream-code | [`sources/prs/vllm/PR-17091.md`](../sources/prs/vllm/PR-17091.md) | [Bugfix] Add contiguous call inside rope kernel wrapper |
| `pr-vllm-17110` | upstream-code | [`sources/prs/vllm/PR-17110.md`](../sources/prs/vllm/PR-17110.md) | [FEAT] [ROCm]: Add AITER CK 2 Stages MoE support |
| `pr-vllm-17139` | upstream-code | [`sources/prs/vllm/PR-17139.md`](../sources/prs/vllm/PR-17139.md) | [ROCm][FP8][Kernel] FP8 quantization fused into Custom Paged Attention |
| `pr-vllm-17180` | upstream-code | [`sources/prs/vllm/PR-17180.md`](../sources/prs/vllm/PR-17180.md) | [Bugfix] gemma[2,3] interleaved attention when sliding window is disabled |
| `pr-vllm-17193` | upstream-code | [`sources/prs/vllm/PR-17193.md`](../sources/prs/vllm/PR-17193.md) | [V1] Remove num_input_tokens from attn_metadata |
| `pr-vllm-17215` | upstream-code | [`sources/prs/vllm/PR-17215.md`](../sources/prs/vllm/PR-17215.md) | [AMD][FP8][BugFix] Remove V1 check in arg_utils.py for FP8 since it is not necessary |
| `pr-vllm-17222` | upstream-code | [`sources/prs/vllm/PR-17222.md`](../sources/prs/vllm/PR-17222.md) | [Bugfix] Get a specific type of layer from forward context |
| `pr-vllm-17267` | upstream-code | [`sources/prs/vllm/PR-17267.md`](../sources/prs/vllm/PR-17267.md) | [BugFix] Fix vllm_flash_attn install issues |
| `pr-vllm-17280` | upstream-code | [`sources/prs/vllm/PR-17280.md`](../sources/prs/vllm/PR-17280.md) | [NVIDIA] Support Cutlass w8a8 FP8 for Blackwell Geforce GPUs (sm120) |
| `pr-vllm-17283` | upstream-code | [`sources/prs/vllm/PR-17283.md`](../sources/prs/vllm/PR-17283.md) | [BugFix] Fix cascade attention - RuntimeError: scheduler_metadata must have shape (metadata_size) |
| `pr-vllm-17289` | upstream-code | [`sources/prs/vllm/PR-17289.md`](../sources/prs/vllm/PR-17289.md) | [Misc][ROCm] Exclude `cutlass_mla_decode` for ROCm build |
| `pr-vllm-17328` | upstream-code | [`sources/prs/vllm/PR-17328.md`](../sources/prs/vllm/PR-17328.md) | Add tuned triton fused_moe configs for Qwen3Moe |
| `pr-vllm-17331` | upstream-code | [`sources/prs/vllm/PR-17331.md`](../sources/prs/vllm/PR-17331.md) | [AMD] [Quantization] Add override flag for attention dtype instead of using kv_cache_dtype trigger |
| `pr-vllm-17394` | upstream-code | [`sources/prs/vllm/PR-17394.md`](../sources/prs/vllm/PR-17394.md) | [v1] AttentionMetadata for each layer |
| `pr-vllm-17414` | upstream-code | [`sources/prs/vllm/PR-17414.md`](../sources/prs/vllm/PR-17414.md) | Fix noisy warning for uncalibrated q_scale/p_scale |
| `pr-vllm-17483` | upstream-code | [`sources/prs/vllm/PR-17483.md`](../sources/prs/vllm/PR-17483.md) | [v1] Pass BlockTable and KVCacheSpec to AttentionMetadataBuilders |
| `pr-vllm-17484` | upstream-code | [`sources/prs/vllm/PR-17484.md`](../sources/prs/vllm/PR-17484.md) | [Attention] MLA move o_proj q_proj into cuda-graph region |
| `pr-vllm-17494` | upstream-code | [`sources/prs/vllm/PR-17494.md`](../sources/prs/vllm/PR-17494.md) | [BugFix] Fix mla cpu - missing 3 required positional arguments |
| `pr-vllm-17496` | upstream-code | [`sources/prs/vllm/PR-17496.md`](../sources/prs/vllm/PR-17496.md) | [TPU] Add kernel test for moe_pallas |
| `pr-vllm-17523` | upstream-code | [`sources/prs/vllm/PR-17523.md`](../sources/prs/vllm/PR-17523.md) | [FEAT][ROCm]: Support AITER MLA on V1 Engine |
| `pr-vllm-17625` | upstream-code | [`sources/prs/vllm/PR-17625.md`](../sources/prs/vllm/PR-17625.md) | [NVIDIA] Add Cutlass MLA backend |
| `pr-vllm-17668` | upstream-code | [`sources/prs/vllm/PR-17668.md`](../sources/prs/vllm/PR-17668.md) | [Attention] MLA move rotary embedding to cuda-graph region |
| `pr-vllm-17687` | upstream-code | [`sources/prs/vllm/PR-17687.md`](../sources/prs/vllm/PR-17687.md) | [Kernel] fp4 marlin kernel |
| `pr-vllm-17751` | upstream-code | [`sources/prs/vllm/PR-17751.md`](../sources/prs/vllm/PR-17751.md) | [P/D] NIXL Integration |
| `pr-vllm-17864` | upstream-code | [`sources/prs/vllm/PR-17864.md`](../sources/prs/vllm/PR-17864.md) | [BugFix][AMD] Compatible patch for latest AITER(05/07/2025) |
| `pr-vllm-17871` | upstream-code | [`sources/prs/vllm/PR-17871.md`](../sources/prs/vllm/PR-17871.md) | fix amd triton mla path |
| `pr-vllm-17880` | upstream-code | [`sources/prs/vllm/PR-17880.md`](../sources/prs/vllm/PR-17880.md) | [Bugfix][ROCm] Fix AITER MLA V1 |
| `pr-vllm-17912` | upstream-code | [`sources/prs/vllm/PR-17912.md`](../sources/prs/vllm/PR-17912.md) | [BugFix][AMD] Compatible patch for AITER lib after 04/20 |
| `pr-vllm-17914` | upstream-code | [`sources/prs/vllm/PR-17914.md`](../sources/prs/vllm/PR-17914.md) | [Misc] Add compressed-tensors NVFP4A16 emulation support |
| `pr-vllm-17918` | upstream-code | [`sources/prs/vllm/PR-17918.md`](../sources/prs/vllm/PR-17918.md) | use ceil_div in cutlass block scaling shape check |
| `pr-vllm-17945` | upstream-code | [`sources/prs/vllm/PR-17945.md`](../sources/prs/vllm/PR-17945.md) | [v1] Support multiple KV cache groups in GPU model runner |
| `pr-vllm-17961` | upstream-code | [`sources/prs/vllm/PR-17961.md`](../sources/prs/vllm/PR-17961.md) | [BUG] [ROCm] [MLA] Fix variable name bug due to change in variable name in PR #17483 |
| `pr-vllm-18000` | upstream-code | [`sources/prs/vllm/PR-18000.md`](../sources/prs/vllm/PR-18000.md) | Use NVFP4 Marlin for CompressedTensorsW4A16Fp4 |
| `pr-vllm-18046` | upstream-code | [`sources/prs/vllm/PR-18046.md`](../sources/prs/vllm/PR-18046.md) | [Kernel] Have rotary embeddings support tensors |
| `pr-vllm-18049` | upstream-code | [`sources/prs/vllm/PR-18049.md`](../sources/prs/vllm/PR-18049.md) | Fix Broken macro for cutlass moe |
| `pr-vllm-18093` | upstream-code | [`sources/prs/vllm/PR-18093.md`](../sources/prs/vllm/PR-18093.md) | [Bugfix][ROCm] Use `chunked_prefill_paged_decode` as fallback for V1 attention on ROCm |
| `pr-vllm-18275` | upstream-code | [`sources/prs/vllm/PR-18275.md`](../sources/prs/vllm/PR-18275.md) | [Attention][V1] Toggle for v1 attention backend |
| `pr-vllm-18312` | upstream-code | [`sources/prs/vllm/PR-18312.md`](../sources/prs/vllm/PR-18312.md) | [Quantization] Add compressed-tensors NVFP4 support |
| `pr-vllm-18321` | upstream-code | [`sources/prs/vllm/PR-18321.md`](../sources/prs/vllm/PR-18321.md) | [Model]: Fused MoE for nomic-embed-text-v2-moe |
| `pr-vllm-18338` | upstream-code | [`sources/prs/vllm/PR-18338.md`](../sources/prs/vllm/PR-18338.md) | [FEAT][ROCm] Upgrade AITER MLA v1 backend |
| `pr-vllm-18343` | upstream-code | [`sources/prs/vllm/PR-18343.md`](../sources/prs/vllm/PR-18343.md) | [Feature] Expert Parallelism Load Balancer (EPLB) |
| `pr-vllm-18356` | upstream-code | [`sources/prs/vllm/PR-18356.md`](../sources/prs/vllm/PR-18356.md) | [Minor] Rename quantization nvfp4 to modelopt_fp4 |
| `pr-vllm-18435` | upstream-code | [`sources/prs/vllm/PR-18435.md`](../sources/prs/vllm/PR-18435.md) | [V1] Support Deepseek MTP |
| `pr-vllm-18440` | upstream-code | [`sources/prs/vllm/PR-18440.md`](../sources/prs/vllm/PR-18440.md) | [Bug] Fix moe_sum signature |
| `pr-vllm-18564` | upstream-code | [`sources/prs/vllm/PR-18564.md`](../sources/prs/vllm/PR-18564.md) | Sm100 blockwise fp8 swap ab |
| `pr-vllm-18581` | upstream-code | [`sources/prs/vllm/PR-18581.md`](../sources/prs/vllm/PR-18581.md) | [CUDA] Enable full cudagraph for FlashMLA |
| `pr-vllm-18596` | upstream-code | [`sources/prs/vllm/PR-18596.md`](../sources/prs/vllm/PR-18596.md) | [Hardware][AMD] integrate aiter chunked prefill into vllm |
| `pr-vllm-18762` | upstream-code | [`sources/prs/vllm/PR-18762.md`](../sources/prs/vllm/PR-18762.md) | [Kernel] Integrate CUTLASS MoE kernel with PPLX |
| `pr-vllm-18778` | upstream-code | [`sources/prs/vllm/PR-18778.md`](../sources/prs/vllm/PR-18778.md) | [Perf] Tunings for SM100 FP8 CUTLASS kernel |
| `pr-vllm-18807` | upstream-code | [`sources/prs/vllm/PR-18807.md`](../sources/prs/vllm/PR-18807.md) | [BugFix] FA2 MLA Accuracy Issue |
| `pr-vllm-18833` | upstream-code | [`sources/prs/vllm/PR-18833.md`](../sources/prs/vllm/PR-18833.md) | [P/D] Heterogeneous TP |
| `pr-vllm-18864` | upstream-code | [`sources/prs/vllm/PR-18864.md`](../sources/prs/vllm/PR-18864.md) | [Kernel] Enable fp8 support for pplx and BatchedTritonExperts. |
| `pr-vllm-18938` | upstream-code | [`sources/prs/vllm/PR-18938.md`](../sources/prs/vllm/PR-18938.md) | [ROCm] Remove unnecessary assertion of max_model_len in ROCM_AITER_MLA attention backend. |
| `pr-vllm-18990` | upstream-code | [`sources/prs/vllm/PR-18990.md`](../sources/prs/vllm/PR-18990.md) | [ROCm] [AITER] [Bugfix] Patch for AITER commit `648764942e552a8bb5fe16026703716a81f05374` |
| `pr-vllm-19067` | upstream-code | [`sources/prs/vllm/PR-19067.md`](../sources/prs/vllm/PR-19067.md) | [BugFix][V1][ROCm] Triton MLA uses V0 backend on V1 engine |
| `pr-vllm-19085` | upstream-code | [`sources/prs/vllm/PR-19085.md`](../sources/prs/vllm/PR-19085.md) | [Kernel] Support deep_gemm for linear methods |
| `pr-vllm-19110` | upstream-code | [`sources/prs/vllm/PR-19110.md`](../sources/prs/vllm/PR-19110.md) | [Hardware][NVIDIA] FP4 MoE kernel optimization |
| `pr-vllm-19118` | upstream-code | [`sources/prs/vllm/PR-19118.md`](../sources/prs/vllm/PR-19118.md) | [V1] Use FlashInfer by default on Blackwell GPUs |
| `pr-vllm-19168` | upstream-code | [`sources/prs/vllm/PR-19168.md`](../sources/prs/vllm/PR-19168.md) | [Kernels] Add activation chunking logic to FusedMoEModularKernel |
| `pr-vllm-19346` | upstream-code | [`sources/prs/vllm/PR-19346.md`](../sources/prs/vllm/PR-19346.md) | [Kernel] Apply torch.Tag.needs_fixed_stride_order only for torch==2.6.0 |
| `pr-vllm-19351` | upstream-code | [`sources/prs/vllm/PR-19351.md`](../sources/prs/vllm/PR-19351.md) | [Core] Support Local Chunked Attention for Hybrid KV Cache |
| `pr-vllm-19374` | upstream-code | [`sources/prs/vllm/PR-19374.md`](../sources/prs/vllm/PR-19374.md) | [HOT-FIX] Add `kv_sharing_target_layer_name` argument to cutlass_mla backend |
| `pr-vllm-19436` | upstream-code | [`sources/prs/vllm/PR-19436.md`](../sources/prs/vllm/PR-19436.md) | Add cache to cuda get_device_capability |
| `pr-vllm-19492` | upstream-code | [`sources/prs/vllm/PR-19492.md`](../sources/prs/vllm/PR-19492.md) | [Bugfix][V1] Allow manual FlashAttention for Blackwell |
| `pr-vllm-19500` | upstream-code | [`sources/prs/vllm/PR-19500.md`](../sources/prs/vllm/PR-19500.md) | [Hardware][NVIDIA][kernel] Fp4 MOE quant kernel optimization |
| `pr-vllm-19563` | upstream-code | [`sources/prs/vllm/PR-19563.md`](../sources/prs/vllm/PR-19563.md) | [Quantization] Remove FP4 emulation; Fall-back to marlin for device < 100 |
| `pr-vllm-19566` | upstream-code | [`sources/prs/vllm/PR-19566.md`](../sources/prs/vllm/PR-19566.md) | [Perf] Further tunings for SM100 FP8 CUTLASS kernel |
| `pr-vllm-19636` | upstream-code | [`sources/prs/vllm/PR-19636.md`](../sources/prs/vllm/PR-19636.md) | [Kernels] MoE refactor |
| `pr-vllm-19642` | upstream-code | [`sources/prs/vllm/PR-19642.md`](../sources/prs/vllm/PR-19642.md) | [BugFix] Add an env to disable moe chunking to work around compile incompatibility |
| `pr-vllm-19667` | upstream-code | [`sources/prs/vllm/PR-19667.md`](../sources/prs/vllm/PR-19667.md) | [Kernels] Use empty for modular MoE workspaces |
| `pr-vllm-19717` | upstream-code | [`sources/prs/vllm/PR-19717.md`](../sources/prs/vllm/PR-19717.md) | [Kernels][Bugfix] Use torch op for all kernels in FusedMoE forward.  Add additional testing for cudagraphs. |
| `pr-vllm-19757` | upstream-code | [`sources/prs/vllm/PR-19757.md`](../sources/prs/vllm/PR-19757.md) | [feat]: CUTLASS block scaled group gemm for SM100 |
| `pr-vllm-19767` | upstream-code | [`sources/prs/vllm/PR-19767.md`](../sources/prs/vllm/PR-19767.md) | [torch.compile][ROCm][V1] Enable attention output FP8 fusion for V1 attention backends |
| `pr-vllm-19781` | upstream-code | [`sources/prs/vllm/PR-19781.md`](../sources/prs/vllm/PR-19781.md) | Fix FA2 fallback for Blackwell V1 |
| `pr-vllm-19815` | upstream-code | [`sources/prs/vllm/PR-19815.md`](../sources/prs/vllm/PR-19815.md) | Add Nvidia ModelOpt config adaptation |
| `pr-vllm-19820` | upstream-code | [`sources/prs/vllm/PR-19820.md`](../sources/prs/vllm/PR-19820.md) | [Feature] Integrate new deepgemm |
| `pr-vllm-19822` | upstream-code | [`sources/prs/vllm/PR-19822.md`](../sources/prs/vllm/PR-19822.md) | [Bugfix] Enable PP with AITER+V1 |
| `pr-vllm-19825` | upstream-code | [`sources/prs/vllm/PR-19825.md`](../sources/prs/vllm/PR-19825.md) | [Core] Add Flashinfer TRTLLM Backend for Flashinfer decode path (SM100).  |
| `pr-vllm-19879` | upstream-code | [`sources/prs/vllm/PR-19879.md`](../sources/prs/vllm/PR-19879.md) | [Quantization] Add compressed-tensors emulations support for NVFP4 |
| `pr-vllm-19904` | upstream-code | [`sources/prs/vllm/PR-19904.md`](../sources/prs/vllm/PR-19904.md) | [Bugfix][V1][ROCm] Fix AITER Flash Attention Backend (Fix API Break and Local Attention Logic: affecting Llama4) |
| `pr-vllm-19990` | upstream-code | [`sources/prs/vllm/PR-19990.md`](../sources/prs/vllm/PR-19990.md) | [Quantization] Add compressed-tensors NVFP4 MoE Support |
| `pr-vllm-20034` | upstream-code | [`sources/prs/vllm/PR-20034.md`](../sources/prs/vllm/PR-20034.md) | [Attention] MLA - Flashinfer Ragged Prefill |
| `pr-vllm-20037` | upstream-code | [`sources/prs/vllm/PR-20037.md`](../sources/prs/vllm/PR-20037.md) | [Core] FlashInfer CUTLASS fused MoE backend (NVFP4) |
| `pr-vllm-20059` | upstream-code | [`sources/prs/vllm/PR-20059.md`](../sources/prs/vllm/PR-20059.md) | [Core] Allow full cudagraph with separate attention routines and orthogonal to compilation, add support for FA2 and FlashInfer |
| `pr-vllm-20071` | upstream-code | [`sources/prs/vllm/PR-20071.md`](../sources/prs/vllm/PR-20071.md) | [Perf] SM100 FP8 GEMM Optimizations after cutlass_profiler |
| `pr-vllm-20086` | upstream-code | [`sources/prs/vllm/PR-20086.md`](../sources/prs/vllm/PR-20086.md) | [Bugfix] Build moe_data for both sm100 and sm90 |
| `pr-vllm-20087` | upstream-code | [`sources/prs/vllm/PR-20087.md`](../sources/prs/vllm/PR-20087.md) |  [Feature] Integrate SM100 DeepGEMM support |
| `pr-vllm-20141` | upstream-code | [`sources/prs/vllm/PR-20141.md`](../sources/prs/vllm/PR-20141.md) | [Bugfix] Fix some narrowing conversion warnings |
| `pr-vllm-20142` | upstream-code | [`sources/prs/vllm/PR-20142.md`](../sources/prs/vllm/PR-20142.md) | Replace `multiply_add` with `homogeneous_multiply_add` to Address Clang Template Parameter Issue |
| `pr-vllm-20152` | upstream-code | [`sources/prs/vllm/PR-20152.md`](../sources/prs/vllm/PR-20152.md) | [Bugfix] Mark 'hidden_states' as mutable in moe_forward registration. |
| `pr-vllm-20166` | upstream-code | [`sources/prs/vllm/PR-20166.md`](../sources/prs/vllm/PR-20166.md) | [Bugfix] Fix topk_ids indices_type for CUTLASS w8a8 FP8 MoE |
| `pr-vllm-20167` | upstream-code | [`sources/prs/vllm/PR-20167.md`](../sources/prs/vllm/PR-20167.md) | [Bugfix] Fix Maverick correctness by filling zero to cache space in cutlass_moe |
| `pr-vllm-20254` | upstream-code | [`sources/prs/vllm/PR-20254.md`](../sources/prs/vllm/PR-20254.md) | [ROCm][FEAT] Enable Full Graph Mode in AITER MLA V1 Attn Backend (Decode Phase only) |
| `pr-vllm-20270` | upstream-code | [`sources/prs/vllm/PR-20270.md`](../sources/prs/vllm/PR-20270.md) | [V1] [ROCm] Enable EP with AITER Fused MoE |
| `pr-vllm-20308` | upstream-code | [`sources/prs/vllm/PR-20308.md`](../sources/prs/vllm/PR-20308.md) | [Kernel] Optimize Prefill Attention in Unified Triton Attention Kernel |
| `pr-vllm-20324` | upstream-code | [`sources/prs/vllm/PR-20324.md`](../sources/prs/vllm/PR-20324.md) | [Kernel][Bugfix] Fixup some warnings in nvfp4_blockwise_moe when CUDA < 12.8 |
| `pr-vllm-20332` | upstream-code | [`sources/prs/vllm/PR-20332.md`](../sources/prs/vllm/PR-20332.md) | [Misc] DP : Add ExpertTokensMetadata |
| `pr-vllm-20358` | upstream-code | [`sources/prs/vllm/PR-20358.md`](../sources/prs/vllm/PR-20358.md) | Update PyTorch to 2.8.0 |
| `pr-vllm-20381` | upstream-code | [`sources/prs/vllm/PR-20381.md`](../sources/prs/vllm/PR-20381.md) | [Bugfix] Fix import of CutlassExpertsFp8 in compressed_tensors_moe.py |
| `pr-vllm-20396` | upstream-code | [`sources/prs/vllm/PR-20396.md`](../sources/prs/vllm/PR-20396.md) | [Kernel] SM90 CUTLASS FP8 GEMM: add support for swap AB + kernel tuning |
| `pr-vllm-20401` | upstream-code | [`sources/prs/vllm/PR-20401.md`](../sources/prs/vllm/PR-20401.md) | Add tree attention backend for v1 (part 1) |
| `pr-vllm-20411` | upstream-code | [`sources/prs/vllm/PR-20411.md`](../sources/prs/vllm/PR-20411.md) | [Nvidia] Integrate SM100 cudnn prefill API to MLA prefill |
| `pr-vllm-20447` | upstream-code | [`sources/prs/vllm/PR-20447.md`](../sources/prs/vllm/PR-20447.md) | [feat]: add SM100 support for cutlass FP8 groupGEMM |
| `pr-vllm-20453` | upstream-code | [`sources/prs/vllm/PR-20453.md`](../sources/prs/vllm/PR-20453.md) | Support Llama 4 for cutlass_moe_fp4 |
| `pr-vllm-20457` | upstream-code | [`sources/prs/vllm/PR-20457.md`](../sources/prs/vllm/PR-20457.md) | Support Llama 4 for fused_marlin_moe |
| `pr-vllm-20466` | upstream-code | [`sources/prs/vllm/PR-20466.md`](../sources/prs/vllm/PR-20466.md) | [Attention] Refactor attention metadata builder interface |
| `pr-vllm-20500` | upstream-code | [`sources/prs/vllm/PR-20500.md`](../sources/prs/vllm/PR-20500.md) | [Perf] Reuse workspace for FP8+FP4 Marlin MoE |
| `pr-vllm-20509` | upstream-code | [`sources/prs/vllm/PR-20509.md`](../sources/prs/vllm/PR-20509.md) | [Bugfix] Fix missing per_act_token parameter in compressed_tensors_moe |
| `pr-vllm-20513` | upstream-code | [`sources/prs/vllm/PR-20513.md`](../sources/prs/vllm/PR-20513.md) | [BugFix] Fix: ImportError when building on hopper systems |
| `pr-vllm-20560` | upstream-code | [`sources/prs/vllm/PR-20560.md`](../sources/prs/vllm/PR-20560.md) | [CI/Build][CPU] Fix CPU CI and remove all CPU V0 files |
| `pr-vllm-20578` | upstream-code | [`sources/prs/vllm/PR-20578.md`](../sources/prs/vllm/PR-20578.md) | [Bench] Add NVFP4 GEMM benchmark script |
| `pr-vllm-20640` | upstream-code | [`sources/prs/vllm/PR-20640.md`](../sources/prs/vllm/PR-20640.md) | [feat] enable SM100 CUTLASS block scaled group gemm for smaller batch sizes |
| `pr-vllm-20645` | upstream-code | [`sources/prs/vllm/PR-20645.md`](../sources/prs/vllm/PR-20645.md) | [NVIDIA] Add SM100 Flashinfer MoE blockscale fp8 backend for low latency |
| `pr-vllm-20646` | upstream-code | [`sources/prs/vllm/PR-20646.md`](../sources/prs/vllm/PR-20646.md) | [Kernel] Basic tuned configs for NVFP4 CUTLASS dense GEMM |
| `pr-vllm-20699` | upstream-code | [`sources/prs/vllm/PR-20699.md`](../sources/prs/vllm/PR-20699.md) | [Misc] Log the reason for falling back to FlexAttention |
| `pr-vllm-20736` | upstream-code | [`sources/prs/vllm/PR-20736.md`](../sources/prs/vllm/PR-20736.md) | GLM-4.5 Model Support |
| `pr-vllm-20759` | upstream-code | [`sources/prs/vllm/PR-20759.md`](../sources/prs/vllm/PR-20759.md) | [PERF] PyTorch Symmetric Memory All-Reduce |
| `pr-vllm-20762` | upstream-code | [`sources/prs/vllm/PR-20762.md`](../sources/prs/vllm/PR-20762.md) | [Performance] Performance improvements in non-blockwise fp8 CUTLASS MoE |
| `pr-vllm-20769` | upstream-code | [`sources/prs/vllm/PR-20769.md`](../sources/prs/vllm/PR-20769.md) | SM100 Cutlass MLA decode with unrestricted num_heads (< 128) for DeepSeek TP |
| `pr-vllm-20781` | upstream-code | [`sources/prs/vllm/PR-20781.md`](../sources/prs/vllm/PR-20781.md) | [fix]: disable cutlass block scaled group gemm for EP |
| `pr-vllm-20825` | upstream-code | [`sources/prs/vllm/PR-20825.md`](../sources/prs/vllm/PR-20825.md) | [Bugfix] Fix a couple PPLX+CUTLASS MoE bugs |
| `pr-vllm-20827` | upstream-code | [`sources/prs/vllm/PR-20827.md`](../sources/prs/vllm/PR-20827.md) | [Misc] Restrict deep_gemm's log output |
| `pr-vllm-20833` | upstream-code | [`sources/prs/vllm/PR-20833.md`](../sources/prs/vllm/PR-20833.md) | [Bug] Fix DeepGemm for EP low latency case |
| `pr-vllm-20841` | upstream-code | [`sources/prs/vllm/PR-20841.md`](../sources/prs/vllm/PR-20841.md) | [Perf] Use Triton instead of Torch for DeepGEMM Per Token Group Quant |
| `pr-vllm-20880` | upstream-code | [`sources/prs/vllm/PR-20880.md`](../sources/prs/vllm/PR-20880.md) | [V1] [ROCm] [AITER] Upgrade AITER to commit `916bf3c` and bugfix APIs |
| `pr-vllm-20903` | upstream-code | [`sources/prs/vllm/PR-20903.md`](../sources/prs/vllm/PR-20903.md) | [Kernel] DeepGemm MoE : Integrate triton permute / unpermute kernels  |
| `pr-vllm-20911` | upstream-code | [`sources/prs/vllm/PR-20911.md`](../sources/prs/vllm/PR-20911.md) | [Perf] Add swap_ab to SM90 FP8 non-block CUTLASS moe grouped gemm |
| `pr-vllm-20930` | upstream-code | [`sources/prs/vllm/PR-20930.md`](../sources/prs/vllm/PR-20930.md) | [Model] Pooling models default to using chunked prefill & prefix caching if supported. |
| `pr-vllm-20933` | upstream-code | [`sources/prs/vllm/PR-20933.md`](../sources/prs/vllm/PR-20933.md) | [Bugfix] Fix incorrect dispatch for CutlassBlockScaledGroupedGemm and DeepGEMM |
| `pr-vllm-21003` | upstream-code | [`sources/prs/vllm/PR-21003.md`](../sources/prs/vllm/PR-21003.md) | Support mnnvl all2allv from Flashinfer |
| `pr-vllm-21020` | upstream-code | [`sources/prs/vllm/PR-21020.md`](../sources/prs/vllm/PR-21020.md) | [BugFix] Fix import error on non-blackwell machines |
| `pr-vllm-21077` | upstream-code | [`sources/prs/vllm/PR-21077.md`](../sources/prs/vllm/PR-21077.md) | [Bugfix] Voxtral on Blackwell GPUs (RTX 50 series) |
| `pr-vllm-21078` | upstream-code | [`sources/prs/vllm/PR-21078.md`](../sources/prs/vllm/PR-21078.md) | [Kernel] Flashinfer MLA (trtllm-gen) decode kernel integration |
| `pr-vllm-21083` | upstream-code | [`sources/prs/vllm/PR-21083.md`](../sources/prs/vllm/PR-21083.md) | [Perf] Cuda Kernel for Per Token Group Quant |
| `pr-vllm-21086` | upstream-code | [`sources/prs/vllm/PR-21086.md`](../sources/prs/vllm/PR-21086.md) | [Model] Support deepseek with eagle |
| `pr-vllm-21088` | upstream-code | [`sources/prs/vllm/PR-21088.md`](../sources/prs/vllm/PR-21088.md) | [v1] Add Whisper model support (encoder-decoder) |
| `pr-vllm-21093` | upstream-code | [`sources/prs/vllm/PR-21093.md`](../sources/prs/vllm/PR-21093.md) | [Attention] Make local attention backend agnostic |
| `pr-vllm-21116` | upstream-code | [`sources/prs/vllm/PR-21116.md`](../sources/prs/vllm/PR-21116.md) | [perf] Add fused MLA QKV + strided layernorm |
| `pr-vllm-21121` | upstream-code | [`sources/prs/vllm/PR-21121.md`](../sources/prs/vllm/PR-21121.md) | [Bugfix] Allocate less memory in non-batched CUTLASS MoE |
| `pr-vllm-21137` | upstream-code | [`sources/prs/vllm/PR-21137.md`](../sources/prs/vllm/PR-21137.md) | [Attention] Optimize FlashInfer MetadataBuilder Build call |
| `pr-vllm-21153` | upstream-code | [`sources/prs/vllm/PR-21153.md`](../sources/prs/vllm/PR-21153.md) | [Attention][DBO] Add support for "splitting" the CommonAttentionMetadata |
| `pr-vllm-21166` | upstream-code | [`sources/prs/vllm/PR-21166.md`](../sources/prs/vllm/PR-21166.md) | [Feature][OCP MX] Support mxfp6 and mixed mxfp6-mxfp4 |
| `pr-vllm-21187` | upstream-code | [`sources/prs/vllm/PR-21187.md`](../sources/prs/vllm/PR-21187.md) | [Bug] DeepGemm: Fix TypeError: per_block_cast_to_fp8() missing 1 required positional argument: 'use_ue8m0' for SM100 |
| `pr-vllm-21188` | upstream-code | [`sources/prs/vllm/PR-21188.md`](../sources/prs/vllm/PR-21188.md) | [Attention] Clean up iRoPE in V1 |
| `pr-vllm-21197` | upstream-code | [`sources/prs/vllm/PR-21197.md`](../sources/prs/vllm/PR-21197.md) | [Kernel] Enable Hybrid Model Support in Triton Unified Attention Kernel |
| `pr-vllm-21229` | upstream-code | [`sources/prs/vllm/PR-21229.md`](../sources/prs/vllm/PR-21229.md) | [Feature][Kernel]FusedMoE LoRA |
| `pr-vllm-21249` | upstream-code | [`sources/prs/vllm/PR-21249.md`](../sources/prs/vllm/PR-21249.md) | [v1] - Mamba1 Attention Metadata |
| `pr-vllm-21270` | upstream-code | [`sources/prs/vllm/PR-21270.md`](../sources/prs/vllm/PR-21270.md) | Support encoder-only models without KV-Cache |
| `pr-vllm-21309` | upstream-code | [`sources/prs/vllm/PR-21309.md`](../sources/prs/vllm/PR-21309.md) | Support CUTLASS NVFP4 (w4a4) for Blackwell Geforce GPUs (SM120) |
| `pr-vllm-21327` | upstream-code | [`sources/prs/vllm/PR-21327.md`](../sources/prs/vllm/PR-21327.md) | Update fp4 quantize API |
| `pr-vllm-21331` | upstream-code | [`sources/prs/vllm/PR-21331.md`](../sources/prs/vllm/PR-21331.md) | Support Tensorrt-LLM MoE fp4 for low-latency |
| `pr-vllm-21340` | upstream-code | [`sources/prs/vllm/PR-21340.md`](../sources/prs/vllm/PR-21340.md) | [TPU][Bugfix] fix moe layer |
| `pr-vllm-21342` | upstream-code | [`sources/prs/vllm/PR-21342.md`](../sources/prs/vllm/PR-21342.md) | [V1] port xformers backend to v1 |
| `pr-vllm-21367` | upstream-code | [`sources/prs/vllm/PR-21367.md`](../sources/prs/vllm/PR-21367.md) | [V1][CUDA] Full cudagraph support for FlashInfer |
| `pr-vllm-21401` | upstream-code | [`sources/prs/vllm/PR-21401.md`](../sources/prs/vllm/PR-21401.md) | [V1] [Hybrid] Enable Full CUDA Graph (decode-only) for Mamba layers |
| `pr-vllm-21408` | upstream-code | [`sources/prs/vllm/PR-21408.md`](../sources/prs/vllm/PR-21408.md) | Update flashinfer CUTLASS NVFP4 MoE Kernel to use per expert global scaling factor |
| `pr-vllm-21411` | upstream-code | [`sources/prs/vllm/PR-21411.md`](../sources/prs/vllm/PR-21411.md) | [NVIDIA] Explicitly disable shuffled weights for flashinfer blockscale moe fp8 kernels |
| `pr-vllm-21412` | upstream-code | [`sources/prs/vllm/PR-21412.md`](../sources/prs/vllm/PR-21412.md) | [v1][attention] Support Hybrid Allocator + FlashInfer |
| `pr-vllm-21416` | upstream-code | [`sources/prs/vllm/PR-21416.md`](../sources/prs/vllm/PR-21416.md) | Updates to Flex + VLLm integration |
| `pr-vllm-21419` | upstream-code | [`sources/prs/vllm/PR-21419.md`](../sources/prs/vllm/PR-21419.md) | [V1] Fix local chunked attention always disabled |
| `pr-vllm-21420` | upstream-code | [`sources/prs/vllm/PR-21420.md`](../sources/prs/vllm/PR-21420.md) | [Bugfix][CUDA] fixes CUDA FP8 kv cache dtype supported |
| `pr-vllm-21458` | upstream-code | [`sources/prs/vllm/PR-21458.md`](../sources/prs/vllm/PR-21458.md) | [NVIDIA] Add SM100 Flashinfer MoE per tensor scale fp8 backend |
| `pr-vllm-21465` | upstream-code | [`sources/prs/vllm/PR-21465.md`](../sources/prs/vllm/PR-21465.md) | [Bug] Fix Compressed Tensor NVFP4 `cutlass_fp4_group_mm` illegal memory access |
| `pr-vllm-21485` | upstream-code | [`sources/prs/vllm/PR-21485.md`](../sources/prs/vllm/PR-21485.md) | update flashinfer to v0.2.9rc1 |
| `pr-vllm-21497` | upstream-code | [`sources/prs/vllm/PR-21497.md`](../sources/prs/vllm/PR-21497.md) | [MoE] More balanced expert sharding |
| `pr-vllm-21499` | upstream-code | [`sources/prs/vllm/PR-21499.md`](../sources/prs/vllm/PR-21499.md) | [NVIDIA] Fix Llama4 Scout FP4 functionality issues |
| `pr-vllm-21525` | upstream-code | [`sources/prs/vllm/PR-21525.md`](../sources/prs/vllm/PR-21525.md) | [Bugfix] Fix workspace buffer None issue for Flashinfer TRTLLM Backend |
| `pr-vllm-21533` | upstream-code | [`sources/prs/vllm/PR-21533.md`](../sources/prs/vllm/PR-21533.md) | Add DeepGEMM to Dockerfile in vllm-base image |
| `pr-vllm-21556` | upstream-code | [`sources/prs/vllm/PR-21556.md`](../sources/prs/vllm/PR-21556.md) | [Kernel] Improve machete memory bound perf |
| `pr-vllm-21588` | upstream-code | [`sources/prs/vllm/PR-21588.md`](../sources/prs/vllm/PR-21588.md) | [Attention] Support multiple attention metadata builders per kv_cache_spec  + proper local attention no hybrid kv cache fix |
| `pr-vllm-21590` | upstream-code | [`sources/prs/vllm/PR-21590.md`](../sources/prs/vllm/PR-21590.md) | Override attention metadata for fast prefill in some KV sharing setups |
| `pr-vllm-21626` | upstream-code | [`sources/prs/vllm/PR-21626.md`](../sources/prs/vllm/PR-21626.md) | [Attention] Make CutlassMLA the default backend for SM100 (blackwell) |
| `pr-vllm-21631` | upstream-code | [`sources/prs/vllm/PR-21631.md`](../sources/prs/vllm/PR-21631.md) | [Refactor] Refactor MOE NVFP4 Code Base: ModelOpt + Compressed Tensor |
| `pr-vllm-21634` | upstream-code | [`sources/prs/vllm/PR-21634.md`](../sources/prs/vllm/PR-21634.md) | [Bug] Fix `has_flashinfer_moe` Import Error when it is not installed |
| `pr-vllm-21639` | upstream-code | [`sources/prs/vllm/PR-21639.md`](../sources/prs/vllm/PR-21639.md) | [Feature] Add Flashinfer MoE Support for Compressed Tensor NVFP4 |
| `pr-vllm-21643` | upstream-code | [`sources/prs/vllm/PR-21643.md`](../sources/prs/vllm/PR-21643.md) | [xpu]support moe models on XPU platform |
| `pr-vllm-21691` | upstream-code | [`sources/prs/vllm/PR-21691.md`](../sources/prs/vllm/PR-21691.md) | [BugFix] Fix IMA FlashMLA full cuda-graph and DP + Update FlashMLA |
| `pr-vllm-21716` | upstream-code | [`sources/prs/vllm/PR-21716.md`](../sources/prs/vllm/PR-21716.md) | [NVIDIA] Support Flashinfer TRTLLM FP8-q/kv/out Attention Kernel |
| `pr-vllm-21733` | upstream-code | [`sources/prs/vllm/PR-21733.md`](../sources/prs/vllm/PR-21733.md) | feat: Add Support GPTQ Quantization MOE on ROCM vllm serve |
| `pr-vllm-21759` | upstream-code | [`sources/prs/vllm/PR-21759.md`](../sources/prs/vllm/PR-21759.md) | [Logs] Change flashinfer sampler logs to once |
| `pr-vllm-21775` | upstream-code | [`sources/prs/vllm/PR-21775.md`](../sources/prs/vllm/PR-21775.md) | [Refactor] Merge Compressed Tensor FP8 `CompressedTensorsW8A8Fp8MoEMethod` and `CompressedTensorsW8A8Fp8MoECutlassMethod` |
| `pr-vllm-21787` | upstream-code | [`sources/prs/vllm/PR-21787.md`](../sources/prs/vllm/PR-21787.md) | [Refactor] Remove Duplicate `per_block_cast_to_fp8`, Remove Dependencies of DeepGEMM |
| `pr-vllm-21837` | upstream-code | [`sources/prs/vllm/PR-21837.md`](../sources/prs/vllm/PR-21837.md) | [Bugfix] [Performance] DeepEPHighThroughput + DeepSeek : Quant before Dispatch |
| `pr-vllm-21893` | upstream-code | [`sources/prs/vllm/PR-21893.md`](../sources/prs/vllm/PR-21893.md) | [Bugfix] Check NVIDIA artifactory is accessible before using flashinfer cubin kernels |
| `pr-vllm-21963` | upstream-code | [`sources/prs/vllm/PR-21963.md`](../sources/prs/vllm/PR-21963.md) | Fix Flashinfer CUTLASS MOE Allgather |
| `pr-vllm-21966` | upstream-code | [`sources/prs/vllm/PR-21966.md`](../sources/prs/vllm/PR-21966.md) | [UX] Rename CUTLASS_MLA_VLLM_V1 to CUTLASS_MLA |
| `pr-vllm-21968` | upstream-code | [`sources/prs/vllm/PR-21968.md`](../sources/prs/vllm/PR-21968.md) | [Feature] Add `VLLM_USE_DEEP_GEMM_E8M0` Env to Control E8M0 Scale |
| `pr-vllm-22035` | upstream-code | [`sources/prs/vllm/PR-22035.md`](../sources/prs/vllm/PR-22035.md) | [Kernels] Clean up FusedMoeMethodBase and modular kernel setup.  Remove extra arguments from modular kernel methods. |
| `pr-vllm-22068` | upstream-code | [`sources/prs/vllm/PR-22068.md`](../sources/prs/vllm/PR-22068.md) | [Misc] Minor enhancement of benchmark_moe |
| `pr-vllm-22095` | upstream-code | [`sources/prs/vllm/PR-22095.md`](../sources/prs/vllm/PR-22095.md) | [NVIDIA] Support Flashinfer TRT-LLM Prefill Attention Kernel |
| `pr-vllm-22097` | upstream-code | [`sources/prs/vllm/PR-22097.md`](../sources/prs/vllm/PR-22097.md) | [ROCm][Misc] Rename the context_len to seq_len in ROCm custom paged attention kernel |
| `pr-vllm-22131` | upstream-code | [`sources/prs/vllm/PR-22131.md`](../sources/prs/vllm/PR-22131.md) | [Kernel] Add support for block FP8 on SM120 (NVIDIA 5090 and RTX PRO 6000) |
| `pr-vllm-22154` | upstream-code | [`sources/prs/vllm/PR-22154.md`](../sources/prs/vllm/PR-22154.md) | [fix] fix correct assertion syntax error in attention utils. |
| `pr-vllm-22208` | upstream-code | [`sources/prs/vllm/PR-22208.md`](../sources/prs/vllm/PR-22208.md) | [Log] DeepGEMM Update Log for Unaligned Problem Size |
| `pr-vllm-22217` | upstream-code | [`sources/prs/vllm/PR-22217.md`](../sources/prs/vllm/PR-22217.md) | [UX] Fail if an invalid attention backend is specified |
| `pr-vllm-22222` | upstream-code | [`sources/prs/vllm/PR-22222.md`](../sources/prs/vllm/PR-22222.md) | Fp8 paged attention update |
| `pr-vllm-22251` | upstream-code | [`sources/prs/vllm/PR-22251.md`](../sources/prs/vllm/PR-22251.md) | [Misc] benchmark_moe supports expert parallel |
| `pr-vllm-22260` | upstream-code | [`sources/prs/vllm/PR-22260.md`](../sources/prs/vllm/PR-22260.md) | [Bugfix] Fix MoE BNB version |
| `pr-vllm-22273` | upstream-code | [`sources/prs/vllm/PR-22273.md`](../sources/prs/vllm/PR-22273.md) | Support encoder_only attention for FlexAttention |
| `pr-vllm-22278` | upstream-code | [`sources/prs/vllm/PR-22278.md`](../sources/prs/vllm/PR-22278.md) | [Bugfix] Fix 3D input passed into cutlass_scaled_mm |
| `pr-vllm-22314` | upstream-code | [`sources/prs/vllm/PR-22314.md`](../sources/prs/vllm/PR-22314.md) | [Bugfix] Add proper comparison for package versions |
| `pr-vllm-22320` | upstream-code | [`sources/prs/vllm/PR-22320.md`](../sources/prs/vllm/PR-22320.md) | Add attention sink in attention backends |
| `pr-vllm-22339` | upstream-code | [`sources/prs/vllm/PR-22339.md`](../sources/prs/vllm/PR-22339.md) | [gpt-oss] flashinfer mxfp4 |
| `pr-vllm-22346` | upstream-code | [`sources/prs/vllm/PR-22346.md`](../sources/prs/vllm/PR-22346.md) | [Kernel] Add nvfp4 gemm flashinfer backends |
| `pr-vllm-22357` | upstream-code | [`sources/prs/vllm/PR-22357.md`](../sources/prs/vllm/PR-22357.md) | [NVIDIA] Add SM100 Flashinfer Cutlass MoE fp8 backend |
| `pr-vllm-22368` | upstream-code | [`sources/prs/vllm/PR-22368.md`](../sources/prs/vllm/PR-22368.md) | [BugFix] Fix triton compile error in `kernel_unified_attention_2/3d` caused by attention sinks |
| `pr-vllm-22378` | upstream-code | [`sources/prs/vllm/PR-22378.md`](../sources/prs/vllm/PR-22378.md) | Fix trtllm-gen attention env and add attention sink |
| `pr-vllm-22387` | upstream-code | [`sources/prs/vllm/PR-22387.md`](../sources/prs/vllm/PR-22387.md) | [Sampler] Support returning final logprobs |
| `pr-vllm-22399` | upstream-code | [`sources/prs/vllm/PR-22399.md`](../sources/prs/vllm/PR-22399.md) | [Bug] Fix B200 DeepGEMM E8M0 Accuracy Issue |
| `pr-vllm-22421` | upstream-code | [`sources/prs/vllm/PR-22421.md`](../sources/prs/vllm/PR-22421.md) | [gpt-oss] triton kernel mxfp4 |
| `pr-vllm-22426` | upstream-code | [`sources/prs/vllm/PR-22426.md`](../sources/prs/vllm/PR-22426.md) | [bugfix] Fix Llama3/4 issues caused by FlashInfer 0.2.10 |
| `pr-vllm-22511` | upstream-code | [`sources/prs/vllm/PR-22511.md`](../sources/prs/vllm/PR-22511.md) | Fix Llama4 FlashInfer FP4 MoE issues |
| `pr-vllm-22527` | upstream-code | [`sources/prs/vllm/PR-22527.md`](../sources/prs/vllm/PR-22527.md) | Quantization: support FP4 quantized models on AMD CDNA2/CDNA3 GPUs |
| `pr-vllm-22535` | upstream-code | [`sources/prs/vllm/PR-22535.md`](../sources/prs/vllm/PR-22535.md) | Fix torch version check for SM100 mxfp4  |
| `pr-vllm-22537` | upstream-code | [`sources/prs/vllm/PR-22537.md`](../sources/prs/vllm/PR-22537.md) | [Kernel] Delegate construction of FusedMoEQuantConfig to FusedMoEMethodBase subclasses |
| `pr-vllm-22637` | upstream-code | [`sources/prs/vllm/PR-22637.md`](../sources/prs/vllm/PR-22637.md) | [Bugfix] Fix ModernBert load & Enable sliding window attention for bidirectional attention. |
| `pr-vllm-22650` | upstream-code | [`sources/prs/vllm/PR-22650.md`](../sources/prs/vllm/PR-22650.md) | `FusedMoE` support for the Transformers backend |
| `pr-vllm-22668` | upstream-code | [`sources/prs/vllm/PR-22668.md`](../sources/prs/vllm/PR-22668.md) | [Kernel] Add FP8 support with FlashMLA backend |
| `pr-vllm-22674` | upstream-code | [`sources/prs/vllm/PR-22674.md`](../sources/prs/vllm/PR-22674.md) | [Quantization] Expand compressed-tensors MoE matching logic to support NFP4 + FP8 MoEs |
| `pr-vllm-22678` | upstream-code | [`sources/prs/vllm/PR-22678.md`](../sources/prs/vllm/PR-22678.md) | Force TRTLLM attention for gpt-oss on SM100 |
| `pr-vllm-22703` | upstream-code | [`sources/prs/vllm/PR-22703.md`](../sources/prs/vllm/PR-22703.md) | [NVIDIA] Support Flashinfer TRTLLM FP8-q/kv NVFP4-out Attention Kernel |
| `pr-vllm-22735` | upstream-code | [`sources/prs/vllm/PR-22735.md`](../sources/prs/vllm/PR-22735.md) | [Kernel] Simplify `get_kv_cache_layout` and cache `use_trtllm_attention` env-dependent bit |
| `pr-vllm-22738` | upstream-code | [`sources/prs/vllm/PR-22738.md`](../sources/prs/vllm/PR-22738.md) | [Bugfix] Fix default enable for CUTLASS MLA on SM100 |
| `pr-vllm-22758` | upstream-code | [`sources/prs/vllm/PR-22758.md`](../sources/prs/vllm/PR-22758.md) | fp8 kv cache support fix for torch.compile |
| `pr-vllm-22763` | upstream-code | [`sources/prs/vllm/PR-22763.md`](../sources/prs/vllm/PR-22763.md) | [Feature] Full Cuda Graph Support for Cutlass MLA and 6% E2E Throughput Improvement |
| `pr-vllm-22771` | upstream-code | [`sources/prs/vllm/PR-22771.md`](../sources/prs/vllm/PR-22771.md) | Enable modelopt gemma3 nvfp4/fp8, make workflow more robust |
| `pr-vllm-22791` | upstream-code | [`sources/prs/vllm/PR-22791.md`](../sources/prs/vllm/PR-22791.md) | [FEATURE] support custom vllm tuned config path |
| `pr-vllm-22795` | upstream-code | [`sources/prs/vllm/PR-22795.md`](../sources/prs/vllm/PR-22795.md) | [FIXBUG ] Allow disabling rocm_aiter_fa backend for ROCm GPUs not compatible with AITER |
| `pr-vllm-22797` | upstream-code | [`sources/prs/vllm/PR-22797.md`](../sources/prs/vllm/PR-22797.md) | [FIXBUG] Add return_success parameter to moe_wna16_weight_loader function |
| `pr-vllm-22812` | upstream-code | [`sources/prs/vllm/PR-22812.md`](../sources/prs/vllm/PR-22812.md) | refactor: Change scaling factors calculation for flashinfer FusedMoE |
| `pr-vllm-22887` | upstream-code | [`sources/prs/vllm/PR-22887.md`](../sources/prs/vllm/PR-22887.md) | [XPU] support data parallel for MoE models on XPU |
| `pr-vllm-22895` | upstream-code | [`sources/prs/vllm/PR-22895.md`](../sources/prs/vllm/PR-22895.md) | [Kernel] Added flashinfer fp8 per-tensor gemms |
| `pr-vllm-22933` | upstream-code | [`sources/prs/vllm/PR-22933.md`](../sources/prs/vllm/PR-22933.md) | [Bugfix] use flash attn on sm90 |
| `pr-vllm-22991` | upstream-code | [`sources/prs/vllm/PR-22991.md`](../sources/prs/vllm/PR-22991.md) | [Fix] enable swap_ab for pplx problem size computation |
| `pr-vllm-23006` | upstream-code | [`sources/prs/vllm/PR-23006.md`](../sources/prs/vllm/PR-23006.md) | [UX] Separate marlin moe config logic from triton moe |
| `pr-vllm-23008` | upstream-code | [`sources/prs/vllm/PR-23008.md`](../sources/prs/vllm/PR-23008.md) | Use Blackwell FlashInfer MXFP4 MoE by default if available  |
| `pr-vllm-23016` | upstream-code | [`sources/prs/vllm/PR-23016.md`](../sources/prs/vllm/PR-23016.md) | [Bugfix gpt-oss] Fix float32 convert for flashinfer sink support |
| `pr-vllm-23020` | upstream-code | [`sources/prs/vllm/PR-23020.md`](../sources/prs/vllm/PR-23020.md) | [Misc] Add --save-dir option to benchmark_moe |
| `pr-vllm-23031` | upstream-code | [`sources/prs/vllm/PR-23031.md`](../sources/prs/vllm/PR-23031.md) | [Bugfix] fix qwen3 moe fp8 accuracy issue |
| `pr-vllm-23035` | upstream-code | [`sources/prs/vllm/PR-23035.md`](../sources/prs/vllm/PR-23035.md) | [V1][Mamba1] - Full CUDA and Piecewise CUDA Graphs Support |
| `pr-vllm-23045` | upstream-code | [`sources/prs/vllm/PR-23045.md`](../sources/prs/vllm/PR-23045.md) | [Kernel] CUTLASS MoE FP8: Integrate cuda moe permute/unpermute |
| `pr-vllm-23046` | upstream-code | [`sources/prs/vllm/PR-23046.md`](../sources/prs/vllm/PR-23046.md) | [V1] address post issues related to #20059 (part 1); cascade attention reenable by default |
| `pr-vllm-23123` | upstream-code | [`sources/prs/vllm/PR-23123.md`](../sources/prs/vllm/PR-23123.md) | Add routed_scaling_factor to MoE grouped topk |
| `pr-vllm-23125` | upstream-code | [`sources/prs/vllm/PR-23125.md`](../sources/prs/vllm/PR-23125.md) | [Bugfix] Fix accuracy issue when using flashinfer cutlass moe, TP=1 and modelopt. |
| `pr-vllm-23137` | upstream-code | [`sources/prs/vllm/PR-23137.md`](../sources/prs/vllm/PR-23137.md) | [Log] Warning Once for Cutlass MLA  |
| `pr-vllm-23140` | upstream-code | [`sources/prs/vllm/PR-23140.md`](../sources/prs/vllm/PR-23140.md) | Fix nvfp4 swizzling |
| `pr-vllm-23146` | upstream-code | [`sources/prs/vllm/PR-23146.md`](../sources/prs/vllm/PR-23146.md) | [CPU] add cpu fused moe pytorch native implementation |
| `pr-vllm-23147` | upstream-code | [`sources/prs/vllm/PR-23147.md`](../sources/prs/vllm/PR-23147.md) | [Misc] Minor refactoring for FlashInfer backend |
| `pr-vllm-23148` | upstream-code | [`sources/prs/vllm/PR-23148.md`](../sources/prs/vllm/PR-23148.md) | [XPU][Feature] fp8 online quantization support for XPU |
| `pr-vllm-23154` | upstream-code | [`sources/prs/vllm/PR-23154.md`](../sources/prs/vllm/PR-23154.md) | [Attention] Refactor AttentionMetadata Preparation for Encoder-only Models |
| `pr-vllm-23171` | upstream-code | [`sources/prs/vllm/PR-23171.md`](../sources/prs/vllm/PR-23171.md) | [Attention] Unify mamba and attention backend selection |
| `pr-vllm-23174` | upstream-code | [`sources/prs/vllm/PR-23174.md`](../sources/prs/vllm/PR-23174.md) | Optimize input preparation for FlashInfer [2/N] |
| `pr-vllm-23177` | upstream-code | [`sources/prs/vllm/PR-23177.md`](../sources/prs/vllm/PR-23177.md) | [Bugfix] Fix benchmark_moe.py  |
| `pr-vllm-23183` | upstream-code | [`sources/prs/vllm/PR-23183.md`](../sources/prs/vllm/PR-23183.md) | Remove chunked_prefill_enabled flag in V1 MLA |
| `pr-vllm-23185` | upstream-code | [`sources/prs/vllm/PR-23185.md`](../sources/prs/vllm/PR-23185.md) | [Attention] Optimize make_local_attention_virtual_batches for Flash Attention |
| `pr-vllm-23193` | upstream-code | [`sources/prs/vllm/PR-23193.md`](../sources/prs/vllm/PR-23193.md) | [Misc] Enable yapf for FlashInfer backend |
| `pr-vllm-23195` | upstream-code | [`sources/prs/vllm/PR-23195.md`](../sources/prs/vllm/PR-23195.md) | Feature/mla tests |
| `pr-vllm-23198` | upstream-code | [`sources/prs/vllm/PR-23198.md`](../sources/prs/vllm/PR-23198.md) | [kernel] Support W4A8 on Hopper |
| `pr-vllm-23200` | upstream-code | [`sources/prs/vllm/PR-23200.md`](../sources/prs/vllm/PR-23200.md) | [BugFix] fix CUTLASS MLA full cudagraph  |
| `pr-vllm-23207` | upstream-code | [`sources/prs/vllm/PR-23207.md`](../sources/prs/vllm/PR-23207.md) | [Misc][qwen2_5_vl][torch.compile] Enable `supports_torch_compile` on generic nn.Module and demonstrate speedup on Qwen Vision model |
| `pr-vllm-23214` | upstream-code | [`sources/prs/vllm/PR-23214.md`](../sources/prs/vllm/PR-23214.md) | [Core] Always use tensor cores for Flashinfer Decode Wrapper |
| `pr-vllm-23264` | upstream-code | [`sources/prs/vllm/PR-23264.md`](../sources/prs/vllm/PR-23264.md) | [ROCm][Aiter] Add triton fp8 bmm kernel for mla |
| `pr-vllm-23265` | upstream-code | [`sources/prs/vllm/PR-23265.md`](../sources/prs/vllm/PR-23265.md) | [Perf] Small optimizations for silu_mul_fp8_quant_deep_gemm |
| `pr-vllm-23273` | upstream-code | [`sources/prs/vllm/PR-23273.md`](../sources/prs/vllm/PR-23273.md) | [Kernels] Overlap shared experts with send/recv |
| `pr-vllm-23274` | upstream-code | [`sources/prs/vllm/PR-23274.md`](../sources/prs/vllm/PR-23274.md) | [Kernel] Add fused grouped_topk kernel for MoE |
| `pr-vllm-23280` | upstream-code | [`sources/prs/vllm/PR-23280.md`](../sources/prs/vllm/PR-23280.md) | [Perf] Use upstream CUTLASS for SM90 Block FP8 kernel |
| `pr-vllm-23286` | upstream-code | [`sources/prs/vllm/PR-23286.md`](../sources/prs/vllm/PR-23286.md) | [Fix] remove is_marlin param in benchmark_moe |
| `pr-vllm-23287` | upstream-code | [`sources/prs/vllm/PR-23287.md`](../sources/prs/vllm/PR-23287.md) | [Compile] Fix Compile Warning SM100 Cutlass MLA |
| `pr-vllm-23289` | upstream-code | [`sources/prs/vllm/PR-23289.md`](../sources/prs/vllm/PR-23289.md) | [Attention] Blackwell FP8 MLA support with CUTLASS_MLA backend |
| `pr-vllm-23294` | upstream-code | [`sources/prs/vllm/PR-23294.md`](../sources/prs/vllm/PR-23294.md) | [Bug] Fix R1 Accuracy 0 Bug |
| `pr-vllm-23296` | upstream-code | [`sources/prs/vllm/PR-23296.md`](../sources/prs/vllm/PR-23296.md) | Remove duplicate entry in vllm.attention.__all__ |
| `pr-vllm-23297` | upstream-code | [`sources/prs/vllm/PR-23297.md`](../sources/prs/vllm/PR-23297.md) | [Attention] Allow V1 flash_attn to support cross-attention |
| `pr-vllm-23332` | upstream-code | [`sources/prs/vllm/PR-23332.md`](../sources/prs/vllm/PR-23332.md) | [Attention][Platform] Refactor MLA to support Custom Op |
| `pr-vllm-23351` | upstream-code | [`sources/prs/vllm/PR-23351.md`](../sources/prs/vllm/PR-23351.md) | [Feature] Enable DeepGEMM Linear on B200; 1.5% E2E throughput improvement |
| `pr-vllm-23379` | upstream-code | [`sources/prs/vllm/PR-23379.md`](../sources/prs/vllm/PR-23379.md) | [Perf] Remove duplicated NVFP4 blockscales to save memory |
| `pr-vllm-23424` | upstream-code | [`sources/prs/vllm/PR-23424.md`](../sources/prs/vllm/PR-23424.md) | [Bugfix] Fixing division by zero in triton_attn if query_heads/kv_heads > 16  |
| `pr-vllm-23439` | upstream-code | [`sources/prs/vllm/PR-23439.md`](../sources/prs/vllm/PR-23439.md) | [Perf] Warmup FlashInfer attention during startup |
| `pr-vllm-23459` | upstream-code | [`sources/prs/vllm/PR-23459.md`](../sources/prs/vllm/PR-23459.md) | [Misc] Modify CacheConfig import |
| `pr-vllm-23465` | upstream-code | [`sources/prs/vllm/PR-23465.md`](../sources/prs/vllm/PR-23465.md) | [Attention][FA3] Update FA3 to include new swizzle optimization |
| `pr-vllm-23537` | upstream-code | [`sources/prs/vllm/PR-23537.md`](../sources/prs/vllm/PR-23537.md) | Update Flashinfer to  0.2.14.post1 |
| `pr-vllm-23568` | upstream-code | [`sources/prs/vllm/PR-23568.md`](../sources/prs/vllm/PR-23568.md) | [CI Fix] Pin deepep and pplx tags in tools/ep_kernels/, gate multigpu tests |
| `pr-vllm-23585` | upstream-code | [`sources/prs/vllm/PR-23585.md`](../sources/prs/vllm/PR-23585.md) | [Misc] Simplify FlashInfer attention metadata |
| `pr-vllm-23608` | upstream-code | [`sources/prs/vllm/PR-23608.md`](../sources/prs/vllm/PR-23608.md) | DP/EP Support for gpt-oss with deepep-ht comm kernel on SM100 |
| `pr-vllm-23642` | upstream-code | [`sources/prs/vllm/PR-23642.md`](../sources/prs/vllm/PR-23642.md) | [Model] Use the same fused_moe configs for all H200 devices |
| `pr-vllm-23647` | upstream-code | [`sources/prs/vllm/PR-23647.md`](../sources/prs/vllm/PR-23647.md) | [Flashinfer] Support Flashinfer TRTLLM FP8-qkv BF16/FP16-out Attention Kernel |
| `pr-vllm-23649` | upstream-code | [`sources/prs/vllm/PR-23649.md`](../sources/prs/vllm/PR-23649.md) | [Docs] Fix warnings in `mkdocs build` |
| `pr-vllm-23659` | upstream-code | [`sources/prs/vllm/PR-23659.md`](../sources/prs/vllm/PR-23659.md) | [Bugfix] Fix Marlin NVFP4 for modelopt |
| `pr-vllm-23660` | upstream-code | [`sources/prs/vllm/PR-23660.md`](../sources/prs/vllm/PR-23660.md) | [Compile] Fix Compile Warning for `w4a8_mm_entry.cu` |
| `pr-vllm-23666` | upstream-code | [`sources/prs/vllm/PR-23666.md`](../sources/prs/vllm/PR-23666.md) | [Feature] Add Hopper DeepGEMM E8M0 for DeepSeekV3.1 scale_fmt |
| `pr-vllm-23671` | upstream-code | [`sources/prs/vllm/PR-23671.md`](../sources/prs/vllm/PR-23671.md) | [NVIDIA] Support SiluMul + NVFP4 quant fusion |
| `pr-vllm-23678` | upstream-code | [`sources/prs/vllm/PR-23678.md`](../sources/prs/vllm/PR-23678.md) | [Bugfix] Lazy import gpt_oss_triton_kernels_moe for mxfp4 |
| `pr-vllm-23693` | upstream-code | [`sources/prs/vllm/PR-23693.md`](../sources/prs/vllm/PR-23693.md) | [Core/DBO][1/N] Add Dual-Batch Overlap mechanism to VLLM |
| `pr-vllm-23696` | upstream-code | [`sources/prs/vllm/PR-23696.md`](../sources/prs/vllm/PR-23696.md) | [Kernel][B200] `mxfp4` fused cutlass moe |
| `pr-vllm-23725` | upstream-code | [`sources/prs/vllm/PR-23725.md`](../sources/prs/vllm/PR-23725.md) | [Misc] Removed force_fp8_e4m3fnuz from FP8LinearOp |
| `pr-vllm-23727` | upstream-code | [`sources/prs/vllm/PR-23727.md`](../sources/prs/vllm/PR-23727.md) | [Bugfix][Misc] Fix silu_and_mul_nvfp4_quant issue and extract common utils for nvfp4 kernel source files |
| `pr-vllm-23732` | upstream-code | [`sources/prs/vllm/PR-23732.md`](../sources/prs/vllm/PR-23732.md) | [FlashInfer] Cache hyper params in metadata builder |
| `pr-vllm-23734` | upstream-code | [`sources/prs/vllm/PR-23734.md`](../sources/prs/vllm/PR-23734.md) | [Feature] Support Decode Context Parallel (DCP) for MLA |
| `pr-vllm-23737` | upstream-code | [`sources/prs/vllm/PR-23737.md`](../sources/prs/vllm/PR-23737.md) | [BugFix][FlashInfer] Fix potential race condition for paged_kv_indptr_cpu |
| `pr-vllm-23743` | upstream-code | [`sources/prs/vllm/PR-23743.md`](../sources/prs/vllm/PR-23743.md) | [Docs] Fix warnings in `mkdocs build` (continued) |
| `pr-vllm-23745` | upstream-code | [`sources/prs/vllm/PR-23745.md`](../sources/prs/vllm/PR-23745.md) | [Feat][EPLB] A novel static EPLB placement strategy for MoE models. |
| `pr-vllm-23750` | upstream-code | [`sources/prs/vllm/PR-23750.md`](../sources/prs/vllm/PR-23750.md) | [ux] Switch a warning to debug about a pytorch fallback |
| `pr-vllm-23791` | upstream-code | [`sources/prs/vllm/PR-23791.md`](../sources/prs/vllm/PR-23791.md) | [Kernel] cuda kernels for upcoming decode context parallel feature |
| `pr-vllm-23798` | upstream-code | [`sources/prs/vllm/PR-23798.md`](../sources/prs/vllm/PR-23798.md) | [Misc] add reorder_batch AttentionMetadataBuilder |
| `pr-vllm-23809` | upstream-code | [`sources/prs/vllm/PR-23809.md`](../sources/prs/vllm/PR-23809.md) | [fix]: add Arm 4bit fused moe support |
| `pr-vllm-23819` | upstream-code | [`sources/prs/vllm/PR-23819.md`](../sources/prs/vllm/PR-23819.md) | [Model][gpt-oss] Support DP+EP for GPT-OSS with FlashInfer trtllm-gen MoE |
| `pr-vllm-23823` | upstream-code | [`sources/prs/vllm/PR-23823.md`](../sources/prs/vllm/PR-23823.md) | [Bugfix] Fix benchmark_moe.py for blockwise fp8. |
| `pr-vllm-23929` | upstream-code | [`sources/prs/vllm/PR-23929.md`](../sources/prs/vllm/PR-23929.md) | [BUGFIX ] fix undefined silu_and_mul_nvfp4_quant |
| `pr-vllm-23958` | upstream-code | [`sources/prs/vllm/PR-23958.md`](../sources/prs/vllm/PR-23958.md) | [Attention] FlashAttention MLA cudagraph support |
| `pr-vllm-23961` | upstream-code | [`sources/prs/vllm/PR-23961.md`](../sources/prs/vllm/PR-23961.md) | Remove old cutlass mla |
| `pr-vllm-23964` | upstream-code | [`sources/prs/vllm/PR-23964.md`](../sources/prs/vllm/PR-23964.md) | Enable Allgather/ReduceScatter backend for NaiveAllToAll |
| `pr-vllm-23972` | upstream-code | [`sources/prs/vllm/PR-23972.md`](../sources/prs/vllm/PR-23972.md) | [Kernel] Faster pre-processing time for W4A8 |
| `pr-vllm-23978` | upstream-code | [`sources/prs/vllm/PR-23978.md`](../sources/prs/vllm/PR-23978.md) | Feature/vit attention unification# 23880 |
| `pr-vllm-23991` | upstream-code | [`sources/prs/vllm/PR-23991.md`](../sources/prs/vllm/PR-23991.md) | [Model] Add LongCat-Flash  |
| `pr-vllm-23994` | upstream-code | [`sources/prs/vllm/PR-23994.md`](../sources/prs/vllm/PR-23994.md) | [BUGFIX] GPTQ quantization compatibility for Qwen3 MOE models (AutoGPTQ and AutoRound-GPTQ) |
| `pr-vllm-24248` | upstream-code | [`sources/prs/vllm/PR-24248.md`](../sources/prs/vllm/PR-24248.md) | [PERF] Allreduce fusion. Support torch native matching. Tuning of the thresholds |
| `pr-vllm-24385` | upstream-code | [`sources/prs/vllm/PR-24385.md`](../sources/prs/vllm/PR-24385.md) | [Kernel] Support decode context parallelism on Blackwell with CUTLASS MLA |
| `pr-vllm-24440` | upstream-code | [`sources/prs/vllm/PR-24440.md`](../sources/prs/vllm/PR-24440.md) | [Transform] [Quantization] Add QuTLASS support to vLLM |
| `pr-vllm-24521` | upstream-code | [`sources/prs/vllm/PR-24521.md`](../sources/prs/vllm/PR-24521.md) | [Feature] Disallow FlashMLA on Blackwell |
| `pr-vllm-24577` | upstream-code | [`sources/prs/vllm/PR-24577.md`](../sources/prs/vllm/PR-24577.md) | [Bugfix] Enable FP8 KV cache for FlashInfer and Triton backend on non-sm100 GPUs |
| `pr-vllm-24600` | upstream-code | [`sources/prs/vllm/PR-24600.md`](../sources/prs/vllm/PR-24600.md) | [Bugfix] Refactor Flashinfer TRTLLM attention kernel selection logic |
| `pr-vllm-24649` | upstream-code | [`sources/prs/vllm/PR-24649.md`](../sources/prs/vllm/PR-24649.md) | [Rocm] [quantization] Fix quark ptpc moe and add test case |
| `pr-vllm-24666` | upstream-code | [`sources/prs/vllm/PR-24666.md`](../sources/prs/vllm/PR-24666.md) | [Performance] Move apply_w8a8_block_fp8_linear to an op class |
| `pr-vllm-24673` | upstream-code | [`sources/prs/vllm/PR-24673.md`](../sources/prs/vllm/PR-24673.md) | [NVIDIA] Blackwell Family |
| `pr-vllm-24675` | upstream-code | [`sources/prs/vllm/PR-24675.md`](../sources/prs/vllm/PR-24675.md) | [MoE Refactor][Test] FusedMoE layer test |
| `pr-vllm-24722` | upstream-code | [`sources/prs/vllm/PR-24722.md`](../sources/prs/vllm/PR-24722.md) | [Kernel][Quantization] add w4a8 support for marlin kernel |
| `pr-vllm-24750` | upstream-code | [`sources/prs/vllm/PR-24750.md`](../sources/prs/vllm/PR-24750.md) | [CI Failure] Fix test_flashinfer_cutlass_mxfp4_mxfp8_fused_moe |
| `pr-vllm-24774` | upstream-code | [`sources/prs/vllm/PR-24774.md`](../sources/prs/vllm/PR-24774.md) | [Bug] Fix `is_flashmla_supported` Check Error |
| `pr-vllm-24794` | upstream-code | [`sources/prs/vllm/PR-24794.md`](../sources/prs/vllm/PR-24794.md) | [Attention] Refactor CUDA attention backend selection logic |
| `pr-vllm-24833` | upstream-code | [`sources/prs/vllm/PR-24833.md`](../sources/prs/vllm/PR-24833.md) | [Bugfix] Fix accuracy issue for silu_mul + nvfp4 quant fusion kernel |
| `pr-vllm-24864` | upstream-code | [`sources/prs/vllm/PR-24864.md`](../sources/prs/vllm/PR-24864.md) | [DCP] Support Decode Context Parallel (DCP) for GQA with FlashAttention |
| `pr-vllm-24891` | upstream-code | [`sources/prs/vllm/PR-24891.md`](../sources/prs/vllm/PR-24891.md) | [Performance] Remove redundant clone() calls in cutlass_mla |
| `pr-vllm-24966` | upstream-code | [`sources/prs/vllm/PR-24966.md`](../sources/prs/vllm/PR-24966.md) | [Bugfix][B200] Fix `cutlass_mla` hang |
| `pr-vllm-25049` | upstream-code | [`sources/prs/vllm/PR-25049.md`](../sources/prs/vllm/PR-25049.md) | [Attention][DCP] Support DCP with query length > 1 (MTP) with FA3 |
| `pr-vllm-25106` | upstream-code | [`sources/prs/vllm/PR-25106.md`](../sources/prs/vllm/PR-25106.md) | [Bug] Fix `returned_lse` not Defined issue |
| `pr-vllm-25193` | upstream-code | [`sources/prs/vllm/PR-25193.md`](../sources/prs/vllm/PR-25193.md) | [Compile] Fix Compile Warning for Ignoring `MIN_BLOCK_PER_SM` |
| `pr-vllm-25201` | upstream-code | [`sources/prs/vllm/PR-25201.md`](../sources/prs/vllm/PR-25201.md) | [ROCm] Small functional changes for gptoss |
| `pr-vllm-25246` | upstream-code | [`sources/prs/vllm/PR-25246.md`](../sources/prs/vllm/PR-25246.md) | Enable Eagle3 speculative decoding for GPT-OSS model |
| `pr-vllm-25396` | upstream-code | [`sources/prs/vllm/PR-25396.md`](../sources/prs/vllm/PR-25396.md) | [CI Failure] Fix fp8 kv cache on <SM90 |
| `pr-vllm-25478` | upstream-code | [`sources/prs/vllm/PR-25478.md`](../sources/prs/vllm/PR-25478.md) | [BugFix] Fix MLA assert with CUTLASS MLA |
| `pr-vllm-25503` | upstream-code | [`sources/prs/vllm/PR-25503.md`](../sources/prs/vllm/PR-25503.md) | feat: BF16 FlashInfer Fused Cutlass MOE for Hopper and Blackwell Expert Parallel |
| `pr-vllm-25507` | upstream-code | [`sources/prs/vllm/PR-25507.md`](../sources/prs/vllm/PR-25507.md) | [ROCm] Split AITER unified attention into its own backend |
| `pr-vllm-25509` | upstream-code | [`sources/prs/vllm/PR-25509.md`](../sources/prs/vllm/PR-25509.md) | [Bugfix] [B200] cutlass_mla - ensure kv_split == 1 for batch size > 1 |
| `pr-vllm-25609` | upstream-code | [`sources/prs/vllm/PR-25609.md`](../sources/prs/vllm/PR-25609.md) | Enable Fbgemm NVFP4 on Dense models |
| `pr-vllm-25674` | upstream-code | [`sources/prs/vllm/PR-25674.md`](../sources/prs/vllm/PR-25674.md) | [Flashinfer][gpt-oss] Support FP8-qkv Flashinfer TRTLLM Sinks Attention |
| `pr-vllm-25774` | upstream-code | [`sources/prs/vllm/PR-25774.md`](../sources/prs/vllm/PR-25774.md) | Fuse RoPE and MLA KV-cache write |
| `pr-vllm-25843` | upstream-code | [`sources/prs/vllm/PR-25843.md`](../sources/prs/vllm/PR-25843.md) | Update launch_bounds_utils.h for correct compile on Multiple Cuda Arch - PTXAS out of range Warning |
| `pr-vllm-25851` | upstream-code | [`sources/prs/vllm/PR-25851.md`](../sources/prs/vllm/PR-25851.md) | [Bugfix] Fallback ViT attn backend to SDPA for blackwell |
| `pr-vllm-25895` | upstream-code | [`sources/prs/vllm/PR-25895.md`](../sources/prs/vllm/PR-25895.md) | [Bugfix] Fix accuracy issue of TRTLLM FP8 MOE and improve logging |
| `pr-vllm-25935` | upstream-code | [`sources/prs/vllm/PR-25935.md`](../sources/prs/vllm/PR-25935.md) | Fix INT8 quantization error on Blackwell GPUs (SM100+) |
| `pr-vllm-25947` | upstream-code | [`sources/prs/vllm/PR-25947.md`](../sources/prs/vllm/PR-25947.md) | [Bugfix] Enable padded FP4 quantization |
| `pr-vllm-25954` | upstream-code | [`sources/prs/vllm/PR-25954.md`](../sources/prs/vllm/PR-25954.md) | [Performance] Split FlashAttn attention and cache update |
| `pr-vllm-25968` | upstream-code | [`sources/prs/vllm/PR-25968.md`](../sources/prs/vllm/PR-25968.md) | [Quantization/NVFP4] Speed up TRTLLM NVFP4 MOE weight loading and fix K/V scale loading for MLA Attn |
| `pr-vllm-25984` | upstream-code | [`sources/prs/vllm/PR-25984.md`](../sources/prs/vllm/PR-25984.md) | [Spec Decode] Enable efficient speculative decoding with FlashInfer-MLA |
| `pr-vllm-25987` | upstream-code | [`sources/prs/vllm/PR-25987.md`](../sources/prs/vllm/PR-25987.md) | [Bugfix] Allow skipping MoE in NVFP4 (fix for MTP) |
| `pr-vllm-25990` | upstream-code | [`sources/prs/vllm/PR-25990.md`](../sources/prs/vllm/PR-25990.md) | [MoE] Nvfp4 Masked Gemm: Add flashinfer grouped_gemm_nt_masked |
| `pr-vllm-26044` | upstream-code | [`sources/prs/vllm/PR-26044.md`](../sources/prs/vllm/PR-26044.md) | [Refactor] Optimize FP8 MOE Backend Choice and Log |
| `pr-vllm-26098` | upstream-code | [`sources/prs/vllm/PR-26098.md`](../sources/prs/vllm/PR-26098.md) | Fix undefined symbol: cutlass_moe_mm_sm100 |
| `pr-vllm-26107` | upstream-code | [`sources/prs/vllm/PR-26107.md`](../sources/prs/vllm/PR-26107.md) | [NVIDIA] Add support for cudnn fp4 gemm via flashinfer |
| `pr-vllm-26116` | upstream-code | [`sources/prs/vllm/PR-26116.md`](../sources/prs/vllm/PR-26116.md) | [torch.compile] Fix tests for torch==2.9 inductor partition |
| `pr-vllm-26135` | upstream-code | [`sources/prs/vllm/PR-26135.md`](../sources/prs/vllm/PR-26135.md) | [ModelOpt] Load w13/w2_input_scale for all experts, nvfp4 |
| `pr-vllm-26138` | upstream-code | [`sources/prs/vllm/PR-26138.md`](../sources/prs/vllm/PR-26138.md) | [CI/Build] Conditionally register cutlass_fp4_group_mm to fix building on Hopper |
| `pr-vllm-26197` | upstream-code | [`sources/prs/vllm/PR-26197.md`](../sources/prs/vllm/PR-26197.md) | [Feature] Enable E8M0 by Default on Hopper for DeepGEMM, 5% E2E throughput improvement |
| `pr-vllm-26315` | upstream-code | [`sources/prs/vllm/PR-26315.md`](../sources/prs/vllm/PR-26315.md) | [Attention][UX][1/N] Add AttentionConfig and change attention env vars to CLI arguments |
| `pr-vllm-26322` | upstream-code | [`sources/prs/vllm/PR-26322.md`](../sources/prs/vllm/PR-26322.md) | [Bug] Fix Shape Validation for Fallback while Enabling E8M0 for DeepGEMM |
| `pr-vllm-26397` | upstream-code | [`sources/prs/vllm/PR-26397.md`](../sources/prs/vllm/PR-26397.md) | [Attention] Add MLA prefill backend: trtllm_ragged_attention_deepseek |
| `pr-vllm-26440` | upstream-code | [`sources/prs/vllm/PR-26440.md`](../sources/prs/vllm/PR-26440.md) | [Performance] Dual stream execution of "shared_experts" and "selected_experts" inside FusedMoE |
| `pr-vllm-26501` | upstream-code | [`sources/prs/vllm/PR-26501.md`](../sources/prs/vllm/PR-26501.md) | [CI/Build] upgrade compressed-tensors to 0.12.2 to address LGPLv3 |
| `pr-vllm-26534` | upstream-code | [`sources/prs/vllm/PR-26534.md`](../sources/prs/vllm/PR-26534.md) | Move query quantization to attention layer for Flashinfer & Triton. |
| `pr-vllm-26535` | upstream-code | [`sources/prs/vllm/PR-26535.md`](../sources/prs/vllm/PR-26535.md) | [Bugfix] Convert untraceable GroupShape to list for AMD impl |
| `pr-vllm-26545` | upstream-code | [`sources/prs/vllm/PR-26545.md`](../sources/prs/vllm/PR-26545.md) | [ROCM] MoE fp4 CK kernel |
| `pr-vllm-26669` | upstream-code | [`sources/prs/vllm/PR-26669.md`](../sources/prs/vllm/PR-26669.md) | support flashinfer_fp4 moe for 5090 gpu |
| `pr-vllm-26714` | upstream-code | [`sources/prs/vllm/PR-26714.md`](../sources/prs/vllm/PR-26714.md) | [NVIDIA] [Perf] Update to leverage flashinfer trtllm FP4 MOE throughput kernel |
| `pr-vllm-26729` | upstream-code | [`sources/prs/vllm/PR-26729.md`](../sources/prs/vllm/PR-26729.md) | [Bugfix] Fix gpt-oss w4a8 DP/EP on B200 |
| `pr-vllm-26779` | upstream-code | [`sources/prs/vllm/PR-26779.md`](../sources/prs/vllm/PR-26779.md) | [Bugfix] DeepSeek V3.2 MTP metadata & CUDA graph issues |
| `pr-vllm-26789` | upstream-code | [`sources/prs/vllm/PR-26789.md`](../sources/prs/vllm/PR-26789.md) | [bugfix] remove unused parameters to reduce unnecessary vram usage |
| `pr-vllm-26835` | upstream-code | [`sources/prs/vllm/PR-26835.md`](../sources/prs/vllm/PR-26835.md) | Add attention benchmarking tools |
| `pr-vllm-26846` | upstream-code | [`sources/prs/vllm/PR-26846.md`](../sources/prs/vllm/PR-26846.md) | [Attention] Tune CUTLASS MLA num_splits |
| `pr-vllm-26859` | upstream-code | [`sources/prs/vllm/PR-26859.md`](../sources/prs/vllm/PR-26859.md) | Disable FlashInfer sampler by default |
| `pr-vllm-26891` | upstream-code | [`sources/prs/vllm/PR-26891.md`](../sources/prs/vllm/PR-26891.md) | [ModelOpt] Remove NVFP4 MoE K%16==0 constraint |
| `pr-vllm-26977` | upstream-code | [`sources/prs/vllm/PR-26977.md`](../sources/prs/vllm/PR-26977.md) | [Kernel] Lazy import FlashInfer |
| `pr-vllm-27035` | upstream-code | [`sources/prs/vllm/PR-27035.md`](../sources/prs/vllm/PR-27035.md) | [fix][cpu] fix prefill attention in CPU attention backend |
| `pr-vllm-27127` | upstream-code | [`sources/prs/vllm/PR-27127.md`](../sources/prs/vllm/PR-27127.md) | [Feature] Batch Invariant: Support DeepGEMM and Blackwell |
| `pr-vllm-27128` | upstream-code | [`sources/prs/vllm/PR-27128.md`](../sources/prs/vllm/PR-27128.md) | [BugFix] bugfix for Flash Attention MLA with full cuda graph IMA following pr-25490 |
| `pr-vllm-27134` | upstream-code | [`sources/prs/vllm/PR-27134.md`](../sources/prs/vllm/PR-27134.md) | [Kernels] Enable FlashInfer FP8 Blockscale on SM90 (for TEP DSR1) |
| `pr-vllm-27141` | upstream-code | [`sources/prs/vllm/PR-27141.md`](../sources/prs/vllm/PR-27141.md) | [MoE] CuteDSL MoE with Nvfp4 DeepEP dispatch  |
| `pr-vllm-27146` | upstream-code | [`sources/prs/vllm/PR-27146.md`](../sources/prs/vllm/PR-27146.md) | [torch.compile] Enable silu_mul_fp8_quant fusion without custom ops enabled |
| `pr-vllm-27187` | upstream-code | [`sources/prs/vllm/PR-27187.md`](../sources/prs/vllm/PR-27187.md) | [ROCM] Enable CompressedTensorsWNA16 |
| `pr-vllm-27190` | upstream-code | [`sources/prs/vllm/PR-27190.md`](../sources/prs/vllm/PR-27190.md) | [BUGFIX][ROCM] ViT FlashAttention on ROCm (no GFX9) and contiguous on qwen3vl ROCm TORCH_SDPA |
| `pr-vllm-27223` | upstream-code | [`sources/prs/vllm/PR-27223.md`](../sources/prs/vllm/PR-27223.md) | Flashinfer_CUTLASS_MOE fuses quantization for TP |
| `pr-vllm-27224` | upstream-code | [`sources/prs/vllm/PR-27224.md`](../sources/prs/vllm/PR-27224.md) | [ROCm][MLA] Support block-size > 1 for AITER MLA backend  |
| `pr-vllm-27232` | upstream-code | [`sources/prs/vllm/PR-27232.md`](../sources/prs/vllm/PR-27232.md) | [Bugfix] Ensure calculated KV scales are applied in attention. |
| `pr-vllm-27255` | upstream-code | [`sources/prs/vllm/PR-27255.md`](../sources/prs/vllm/PR-27255.md) | Bugfix: Cutlass FP8 FusedMoE bad scaling factors |
| `pr-vllm-27261` | upstream-code | [`sources/prs/vllm/PR-27261.md`](../sources/prs/vllm/PR-27261.md) | Feature: Support Relu2 in FusedMoE fp8 cutlass path |
| `pr-vllm-27284` | upstream-code | [`sources/prs/vllm/PR-27284.md`](../sources/prs/vllm/PR-27284.md) | [Perf] SM100 - add swap AB optimization to CUTLASS FP8 GEMM |
| `pr-vllm-27363` | upstream-code | [`sources/prs/vllm/PR-27363.md`](../sources/prs/vllm/PR-27363.md) | Prefer FlashAttention MLA as default over FlashMLA |
| `pr-vllm-27367` | upstream-code | [`sources/prs/vllm/PR-27367.md`](../sources/prs/vllm/PR-27367.md) | [Misc] Make reorder batch also separate extends |
| `pr-vllm-27424` | upstream-code | [`sources/prs/vllm/PR-27424.md`](../sources/prs/vllm/PR-27424.md) | [Bug] Raise error explicitly if using incompatible backend |
| `pr-vllm-27439` | upstream-code | [`sources/prs/vllm/PR-27439.md`](../sources/prs/vllm/PR-27439.md) | [Bugfix] Use latency MOE backend as default for Flashinfer and other misc fixes |
| `pr-vllm-27457` | upstream-code | [`sources/prs/vllm/PR-27457.md`](../sources/prs/vllm/PR-27457.md) | [Performance][MLA][ROCm] Remove redundant D2D copy in deepseek |
| `pr-vllm-27492` | upstream-code | [`sources/prs/vllm/PR-27492.md`](../sources/prs/vllm/PR-27492.md) | [Performance] Support FP8 flashinfer TRTLLM MOE on Qwen3 and Qwen-3next |
| `pr-vllm-27532` | upstream-code | [`sources/prs/vllm/PR-27532.md`](../sources/prs/vllm/PR-27532.md) | [Attention] Use sparse prefill kernel for fp8 kv-cache in DeepSeek-v3.2 |
| `pr-vllm-27660` | upstream-code | [`sources/prs/vllm/PR-27660.md`](../sources/prs/vllm/PR-27660.md) | [Feature] Batch invariant torch.compile |
| `pr-vllm-27663` | upstream-code | [`sources/prs/vllm/PR-27663.md`](../sources/prs/vllm/PR-27663.md) | Add FLASHINFER_MLA to test_mla_backends and add B200 CI run |
| `pr-vllm-27715` | upstream-code | [`sources/prs/vllm/PR-27715.md`](../sources/prs/vllm/PR-27715.md) | [AMD] Use Decoupled Kernel Block Size to Support AITER MLA block_size=1 |
| `pr-vllm-27814` | upstream-code | [`sources/prs/vllm/PR-27814.md`](../sources/prs/vllm/PR-27814.md) | [Refactor] Make FP8 Linear Ops use kernel abstraction |
| `pr-vllm-27816` | upstream-code | [`sources/prs/vllm/PR-27816.md`](../sources/prs/vllm/PR-27816.md) | [Misc] Refactor Attention kv transfer methods into decorator |
| `pr-vllm-27856` | upstream-code | [`sources/prs/vllm/PR-27856.md`](../sources/prs/vllm/PR-27856.md) | [Feature] Extend batch invariant torch.compile to B200 |
| `pr-vllm-27883` | upstream-code | [`sources/prs/vllm/PR-27883.md`](../sources/prs/vllm/PR-27883.md) | [Performance] Fused blockwise quant RMS norm |
| `pr-vllm-27884` | upstream-code | [`sources/prs/vllm/PR-27884.md`](../sources/prs/vllm/PR-27884.md) | [Bug] Batch invariant: Fix flash attn MLA `RuntimeError: scheduler_metadata must have shape (metadata_size)` |
| `pr-vllm-27897` | upstream-code | [`sources/prs/vllm/PR-27897.md`](../sources/prs/vllm/PR-27897.md) | [Performance][B200] Fix deepgemm prologue |
| `pr-vllm-27904` | upstream-code | [`sources/prs/vllm/PR-27904.md`](../sources/prs/vllm/PR-27904.md) | [BugFix][Performance] Restore flashinfer autotuning for all scenarios |
| `pr-vllm-27931` | upstream-code | [`sources/prs/vllm/PR-27931.md`](../sources/prs/vllm/PR-27931.md) | [Kernel] Optimize rms_norm kernel |
| `pr-vllm-27952` | upstream-code | [`sources/prs/vllm/PR-27952.md`](../sources/prs/vllm/PR-27952.md) | Update Flashinfer from `v0.4.1` to `v0.5.2` |
| `pr-vllm-27954` | upstream-code | [`sources/prs/vllm/PR-27954.md`](../sources/prs/vllm/PR-27954.md) | [CPU] Refactor CPU attention backend |
| `pr-vllm-27994` | upstream-code | [`sources/prs/vllm/PR-27994.md`](../sources/prs/vllm/PR-27994.md) | [FlashInfer] Avoid FlashInfer block_size 16 + head_size 256 on blackwell |
| `pr-vllm-28032` | upstream-code | [`sources/prs/vllm/PR-28032.md`](../sources/prs/vllm/PR-28032.md) | [ROCm][MLA] enable fp8 MLA decode on ROCm |
| `pr-vllm-28076` | upstream-code | [`sources/prs/vllm/PR-28076.md`](../sources/prs/vllm/PR-28076.md) | Consolidate Nvidia ModelOpt quant config handling for all quantization methods |
| `pr-vllm-28124` | upstream-code | [`sources/prs/vllm/PR-28124.md`](../sources/prs/vllm/PR-28124.md) | [Perf][DeepSeek] Add sigmoid+bias fusion to fused_grouped_topk from TRTLLM |
| `pr-vllm-28133` | upstream-code | [`sources/prs/vllm/PR-28133.md`](../sources/prs/vllm/PR-28133.md) | [Mamba] - Consolidate Mambas Attention Logic |
| `pr-vllm-28161` | upstream-code | [`sources/prs/vllm/PR-28161.md`](../sources/prs/vllm/PR-28161.md) | Adding a benchmark for batch invariance |
| `pr-vllm-28166` | upstream-code | [`sources/prs/vllm/PR-28166.md`](../sources/prs/vllm/PR-28166.md) | [flashinfer] fix FI all2all with FI cutlass moe |
| `pr-vllm-28269` | upstream-code | [`sources/prs/vllm/PR-28269.md`](../sources/prs/vllm/PR-28269.md) | [Feature] Allow configuring FlashInfer workspace size |
| `pr-vllm-28284` | upstream-code | [`sources/prs/vllm/PR-28284.md`](../sources/prs/vllm/PR-28284.md) | [Feature] Support recording expert indices for rollout router replay |
| `pr-vllm-28306` | upstream-code | [`sources/prs/vllm/PR-28306.md`](../sources/prs/vllm/PR-28306.md) | [Kernel] Support CUDA Graphs in 3D Triton Attention Kernel |
| `pr-vllm-28346` | upstream-code | [`sources/prs/vllm/PR-28346.md`](../sources/prs/vllm/PR-28346.md) | fix cross attention |
| `pr-vllm-28358` | upstream-code | [`sources/prs/vllm/PR-28358.md`](../sources/prs/vllm/PR-28358.md) | [Performance][B200] silu_mul_quant: pack scales in int32 |
| `pr-vllm-28376` | upstream-code | [`sources/prs/vllm/PR-28376.md`](../sources/prs/vllm/PR-28376.md) | [ROCm] Support for Whisper v1 with Aiter Unified Attention and Aiter Flash Attention |
| `pr-vllm-28377` | upstream-code | [`sources/prs/vllm/PR-28377.md`](../sources/prs/vllm/PR-28377.md) | [Bugfix][EPLB] Disabled shared expert overlap when EPLB is enabled |
| `pr-vllm-28404` | upstream-code | [`sources/prs/vllm/PR-28404.md`](../sources/prs/vllm/PR-28404.md) | [CI/Test Fix] Fix CP tests on Blackwell |
| `pr-vllm-28431` | upstream-code | [`sources/prs/vllm/PR-28431.md`](../sources/prs/vllm/PR-28431.md) | Remove weight_scale.T special case for SM90 Block FP8 CUTLASS kernel |
| `pr-vllm-28479` | upstream-code | [`sources/prs/vllm/PR-28479.md`](../sources/prs/vllm/PR-28479.md) | [Perf] Refactor cudagraph_support to enable full CUDA graphs for spec decoding with FlashInfer |
| `pr-vllm-28561` | upstream-code | [`sources/prs/vllm/PR-28561.md`](../sources/prs/vllm/PR-28561.md) | [Bugfix] Fix SM100 gpt-oss regression due to faulty attn sink support |
| `pr-vllm-28569` | upstream-code | [`sources/prs/vllm/PR-28569.md`](../sources/prs/vllm/PR-28569.md) | [Performance][Fix] update nvfp4 code to support renorm routing |
| `pr-vllm-28624` | upstream-code | [`sources/prs/vllm/PR-28624.md`](../sources/prs/vllm/PR-28624.md) | [ROCm][MTP] Support MTP for AITER MLA backend |
| `pr-vllm-28660` | upstream-code | [`sources/prs/vllm/PR-28660.md`](../sources/prs/vllm/PR-28660.md) | [Attention][Bugfix] Fix FA sink support |
| `pr-vllm-28664` | upstream-code | [`sources/prs/vllm/PR-28664.md`](../sources/prs/vllm/PR-28664.md) | [AMD][ROCm] MoRI EP: a high-performance all2all backend |
| `pr-vllm-28687` | upstream-code | [`sources/prs/vllm/PR-28687.md`](../sources/prs/vllm/PR-28687.md) | [Performance] Reduce DeepGEMM N dim restriction from 128 to 64 multiplier  |
| `pr-vllm-28701` | upstream-code | [`sources/prs/vllm/PR-28701.md`](../sources/prs/vllm/PR-28701.md) | Upstreaming aiter triton attention backend as a new backend |
| `pr-vllm-28718` | upstream-code | [`sources/prs/vllm/PR-28718.md`](../sources/prs/vllm/PR-28718.md) | [Feature] Prefill Context Parallel (PCP) basic support |
| `pr-vllm-28739` | upstream-code | [`sources/prs/vllm/PR-28739.md`](../sources/prs/vllm/PR-28739.md) | [Bugfix] Fix ChunkedLocalAttention CUDA Graph setting |
| `pr-vllm-28740` | upstream-code | [`sources/prs/vllm/PR-28740.md`](../sources/prs/vllm/PR-28740.md) | [Bugfix] Fix incorrect use of hidden_states for shared_experts due to do_naive_dispatch_combine |
| `pr-vllm-28755` | upstream-code | [`sources/prs/vllm/PR-28755.md`](../sources/prs/vllm/PR-28755.md) | [PERF] Remove TRTLLM Gen attn kernel limitation `max_seq_len <=131072` |
| `pr-vllm-28763` | upstream-code | [`sources/prs/vllm/PR-28763.md`](../sources/prs/vllm/PR-28763.md) | [Attention] FA2 support more head sizes, ViT support, make default backend |
| `pr-vllm-28775` | upstream-code | [`sources/prs/vllm/PR-28775.md`](../sources/prs/vllm/PR-28775.md) | [Model] Add support for openPangu moe model |
| `pr-vllm-28816` | upstream-code | [`sources/prs/vllm/PR-28816.md`](../sources/prs/vllm/PR-28816.md) | [Bugfix] Fix GPT-OSS on AMD after #28603 |
| `pr-vllm-28840` | upstream-code | [`sources/prs/vllm/PR-28840.md`](../sources/prs/vllm/PR-28840.md) | bugfix: correct attn output with base 2 or e |
| `pr-vllm-28841` | upstream-code | [`sources/prs/vllm/PR-28841.md`](../sources/prs/vllm/PR-28841.md) | [Bugfix] Fix GPT-OSS AR+NORM fusion |
| `pr-vllm-28846` | upstream-code | [`sources/prs/vllm/PR-28846.md`](../sources/prs/vllm/PR-28846.md) | [Bugfix] Safeguard against missing backend in AttentionBackendEnum |
| `pr-vllm-28878` | upstream-code | [`sources/prs/vllm/PR-28878.md`](../sources/prs/vllm/PR-28878.md) | [Bugfix] Make compressed-tensors MoEs respect ignored layers |
| `pr-vllm-28892` | upstream-code | [`sources/prs/vllm/PR-28892.md`](../sources/prs/vllm/PR-28892.md) | Add TRTLLM MoE NVFP4 kernel to CompressedTensorsW4A4MoeMethod |
| `pr-vllm-28934` | upstream-code | [`sources/prs/vllm/PR-28934.md`](../sources/prs/vllm/PR-28934.md) | [Attention] add `_cudagraph_support` for linear attention |
| `pr-vllm-28968` | upstream-code | [`sources/prs/vllm/PR-28968.md`](../sources/prs/vllm/PR-28968.md) | [DeepSeek] Fix DeepSeek V3.2 Rope Embedding |
| `pr-vllm-28990` | upstream-code | [`sources/prs/vllm/PR-28990.md`](../sources/prs/vllm/PR-28990.md) | [BugFix] Fix async-scheduling + FlashAttn MLA |
| `pr-vllm-29004` | upstream-code | [`sources/prs/vllm/PR-29004.md`](../sources/prs/vllm/PR-29004.md) | [Feat] Support non-gated activations in NVFP4 modelopt path |
| `pr-vllm-29066` | upstream-code | [`sources/prs/vllm/PR-29066.md`](../sources/prs/vllm/PR-29066.md) | [MoE][Refactor] Remove most arguments to FusedMoEMethodBase.apply |
| `pr-vllm-29067` | upstream-code | [`sources/prs/vllm/PR-29067.md`](../sources/prs/vllm/PR-29067.md) | [MoE][Refactor] Make select_experts a non-static method |
| `pr-vllm-29084` | upstream-code | [`sources/prs/vllm/PR-29084.md`](../sources/prs/vllm/PR-29084.md) | [Attention] Refactor FA `block_size` limitations to hybrid models only  |
| `pr-vllm-29103` | upstream-code | [`sources/prs/vllm/PR-29103.md`](../sources/prs/vllm/PR-29103.md) | [Attention] Add ROCM_AITER_MLA_SPARSE to attention backend registry |
| `pr-vllm-29111` | upstream-code | [`sources/prs/vllm/PR-29111.md`](../sources/prs/vllm/PR-29111.md) | [CI Failure] Fix Gemma3 RoPE configuration for sliding attention layers |
| `pr-vllm-29125` | upstream-code | [`sources/prs/vllm/PR-29125.md`](../sources/prs/vllm/PR-29125.md) | [Feature] Batch invariant: Enable `TRITON_MLA` without prefix-caching |
| `pr-vllm-29144` | upstream-code | [`sources/prs/vllm/PR-29144.md`](../sources/prs/vllm/PR-29144.md) | [Fix] Add SM check to flashinfer MOE backend |
| `pr-vllm-29194` | upstream-code | [`sources/prs/vllm/PR-29194.md`](../sources/prs/vllm/PR-29194.md) | [Model Runner V2] Change bookkeeping logic in preparation for spec decoding |
| `pr-vllm-29213` | upstream-code | [`sources/prs/vllm/PR-29213.md`](../sources/prs/vllm/PR-29213.md) | [Perf][Kernels] Enable FlashInfer DeepGEMM swapAB on SM90 (for W8A8 Linear Op) |
| `pr-vllm-29222` | upstream-code | [`sources/prs/vllm/PR-29222.md`](../sources/prs/vllm/PR-29222.md) | [LoRA] Optimize 3D MoE logic |
| `pr-vllm-29234` | upstream-code | [`sources/prs/vllm/PR-29234.md`](../sources/prs/vllm/PR-29234.md) | [ROCm][Attention] Sliding window support for `AiterFlashAttentionBackend` |
| `pr-vllm-29242` | upstream-code | [`sources/prs/vllm/PR-29242.md`](../sources/prs/vllm/PR-29242.md) | [Kernel] Add NVFP4 MoE CUTLASS support for SM120 |
| `pr-vllm-29257` | upstream-code | [`sources/prs/vllm/PR-29257.md`](../sources/prs/vllm/PR-29257.md) | Lora MoE Align Improvements |
| `pr-vllm-29287` | upstream-code | [`sources/prs/vllm/PR-29287.md`](../sources/prs/vllm/PR-29287.md) | [ROCm][Deepseekv3.2] Refactor Sparse Indexer as CustomOp |
| `pr-vllm-29337` | upstream-code | [`sources/prs/vllm/PR-29337.md`](../sources/prs/vllm/PR-29337.md) | [UX] Put CUDA attention backend selection log into one line |
| `pr-vllm-29338` | upstream-code | [`sources/prs/vllm/PR-29338.md`](../sources/prs/vllm/PR-29338.md) | [CI/Test Fix] Fix CP tests on Blackwell |
| `pr-vllm-29339` | upstream-code | [`sources/prs/vllm/PR-29339.md`](../sources/prs/vllm/PR-29339.md) | [Bugfix] Only use triton_kernels for MXFP4 on SM90 and SM100 |
| `pr-vllm-29346` | upstream-code | [`sources/prs/vllm/PR-29346.md`](../sources/prs/vllm/PR-29346.md) | [Perf] Disable DeepGEMM MoE by default when TP=8 is used |
| `pr-vllm-29352` | upstream-code | [`sources/prs/vllm/PR-29352.md`](../sources/prs/vllm/PR-29352.md) | [Attention][CUDAGraph] Remove CG padding from attention backends |
| `pr-vllm-29354` | upstream-code | [`sources/prs/vllm/PR-29354.md`](../sources/prs/vllm/PR-29354.md) | Add unpermute-aware fused MoE path and small-batch fallback |
| `pr-vllm-29415` | upstream-code | [`sources/prs/vllm/PR-29415.md`](../sources/prs/vllm/PR-29415.md) | Guard FlashInfer sampler using the same check as FlashInfer attention backend |
| `pr-vllm-29426` | upstream-code | [`sources/prs/vllm/PR-29426.md`](../sources/prs/vllm/PR-29426.md) | [BugFix] Fix `plan` API Mismatch when using latest FlashInfer |
| `pr-vllm-29439` | upstream-code | [`sources/prs/vllm/PR-29439.md`](../sources/prs/vllm/PR-29439.md) | [Bugfix] Fix grouped_topk pytorch impl when num_experts can't be grouped properly |
| `pr-vllm-29441` | upstream-code | [`sources/prs/vllm/PR-29441.md`](../sources/prs/vllm/PR-29441.md) | Change warning logs to debug for unimplemented MXFP4 Linear/Attention |
| `pr-vllm-29471` | upstream-code | [`sources/prs/vllm/PR-29471.md`](../sources/prs/vllm/PR-29471.md) | Remove upstream fa checks |
| `pr-vllm-29487` | upstream-code | [`sources/prs/vllm/PR-29487.md`](../sources/prs/vllm/PR-29487.md) | [Bugfix] Correct num_q_heads on DCP for Flashinfer backends  |
| `pr-vllm-29540` | upstream-code | [`sources/prs/vllm/PR-29540.md`](../sources/prs/vllm/PR-29540.md) | [Attention] Update attention imports |
| `pr-vllm-29614` | upstream-code | [`sources/prs/vllm/PR-29614.md`](../sources/prs/vllm/PR-29614.md) | [Bugfix][MM encoder] Fix ViT attention backend resolving for Turing GPU |
| `pr-vllm-29624` | upstream-code | [`sources/prs/vllm/PR-29624.md`](../sources/prs/vllm/PR-29624.md) | [Attention] Make seq_lens_cpu optional in CommonAttentionMetadata to enable true async spec-decode |
| `pr-vllm-29627` | upstream-code | [`sources/prs/vllm/PR-29627.md`](../sources/prs/vllm/PR-29627.md) | [Attention] Cache attention metadata builds across hybrid KV-cache groups |
| `pr-vllm-29642` | upstream-code | [`sources/prs/vllm/PR-29642.md`](../sources/prs/vllm/PR-29642.md) | [Kernel][MoE] optimize `moe_align_block_size` |
| `pr-vllm-29644` | upstream-code | [`sources/prs/vllm/PR-29644.md`](../sources/prs/vllm/PR-29644.md) | [Attention] Make `split_decodes_and_prefills(..., require_uniform=True)` support padding |
| `pr-vllm-29650` | upstream-code | [`sources/prs/vllm/PR-29650.md`](../sources/prs/vllm/PR-29650.md) | [Misc] Remove redundant attention var constants |
| `pr-vllm-29691` | upstream-code | [`sources/prs/vllm/PR-29691.md`](../sources/prs/vllm/PR-29691.md) | [Kernel]Support W4A8 Grouped GEMM on Hopper |
| `pr-vllm-29710` | upstream-code | [`sources/prs/vllm/PR-29710.md`](../sources/prs/vllm/PR-29710.md) | [perf] Use direct copy (broadcast) instead of cat for k_nope/k_pe in MLA prefill |
| `pr-vllm-29711` | upstream-code | [`sources/prs/vllm/PR-29711.md`](../sources/prs/vllm/PR-29711.md) |  SM120 / NVFP4: add device guard and runtime SM dispatch to cutlass_scaled_fp4_mm |
| `pr-vllm-29742` | upstream-code | [`sources/prs/vllm/PR-29742.md`](../sources/prs/vllm/PR-29742.md) | [Bugfix] Fix mismatched nvfp4 gemm output shape |
| `pr-vllm-29748` | upstream-code | [`sources/prs/vllm/PR-29748.md`](../sources/prs/vllm/PR-29748.md) | [MoE-FP8-modelopt] Add FlashInfer alignment padding for intermediate dimensions |
| `pr-vllm-29757` | upstream-code | [`sources/prs/vllm/PR-29757.md`](../sources/prs/vllm/PR-29757.md) | Add Mistral Large 3 and Ministral 3 |
| `pr-vllm-29773` | upstream-code | [`sources/prs/vllm/PR-29773.md`](../sources/prs/vllm/PR-29773.md) | [ROCm] [Fused Moe EP] Use binary expert mask for aiter fused moe kernel |
| `pr-vllm-29775` | upstream-code | [`sources/prs/vllm/PR-29775.md`](../sources/prs/vllm/PR-29775.md) | [ROCm][MXFP4] Infer w4a4 quant method in rocm aiter fused moe |
| `pr-vllm-29795` | upstream-code | [`sources/prs/vllm/PR-29795.md`](../sources/prs/vllm/PR-29795.md) | [Perf] Improve fp8 quant in mla; replace ReduceSum with ReduceScatterSum |
| `pr-vllm-29804` | upstream-code | [`sources/prs/vllm/PR-29804.md`](../sources/prs/vllm/PR-29804.md) | [EPLB] Support EPLB w/ NVFP4 |
| `pr-vllm-29845` | upstream-code | [`sources/prs/vllm/PR-29845.md`](../sources/prs/vllm/PR-29845.md) | [SpecDecode] Simplified alternative padded-speculation acceptance rate fix |
| `pr-vllm-29867` | upstream-code | [`sources/prs/vllm/PR-29867.md`](../sources/prs/vllm/PR-29867.md) | [Quantization] fix: overflow with static per-tensor scaling |
| `pr-vllm-29887` | upstream-code | [`sources/prs/vllm/PR-29887.md`](../sources/prs/vllm/PR-29887.md) | [ROCm][Perf] Enable shuffle kv cache layout and assembly paged attention kernel for `AiterFlashAttentionBackend` |
| `pr-vllm-29890` | upstream-code | [`sources/prs/vllm/PR-29890.md`](../sources/prs/vllm/PR-29890.md) | [Bugfix] Fix FP8 MoE LoRA |
| `pr-vllm-29901` | upstream-code | [`sources/prs/vllm/PR-29901.md`](../sources/prs/vllm/PR-29901.md) | [Kernel][Quantization][MoE] add marlin kernel support for turing (sm75) |
| `pr-vllm-29933` | upstream-code | [`sources/prs/vllm/PR-29933.md`](../sources/prs/vllm/PR-29933.md) | [BugFix] Fix DBO assert `assert B_block_table == B_q` |
| `pr-vllm-29935` | upstream-code | [`sources/prs/vllm/PR-29935.md`](../sources/prs/vllm/PR-29935.md) | [moe] Use enable_chunking func (to support disabling chunking) |
| `pr-vllm-29936` | upstream-code | [`sources/prs/vllm/PR-29936.md`](../sources/prs/vllm/PR-29936.md) | [moe] Allow disabling DP chunking |
| `pr-vllm-29941` | upstream-code | [`sources/prs/vllm/PR-29941.md`](../sources/prs/vllm/PR-29941.md) | [offloader] v2: Hide weight onloading latency via prefetching |
| `pr-vllm-29999` | upstream-code | [`sources/prs/vllm/PR-29999.md`](../sources/prs/vllm/PR-29999.md) | [Bug] Fix vLLM config is not set error |
| `pr-vllm-30014` | upstream-code | [`sources/prs/vllm/PR-30014.md`](../sources/prs/vllm/PR-30014.md) | [Perf] Do FP4 quant before All gather on flashinfer trtllmgen MOE  |
| `pr-vllm-30071` | upstream-code | [`sources/prs/vllm/PR-30071.md`](../sources/prs/vllm/PR-30071.md) | [Quantization] Support Quark int4-fp8 w4a8 for MoE |
| `pr-vllm-30102` | upstream-code | [`sources/prs/vllm/PR-30102.md`](../sources/prs/vllm/PR-30102.md) | Fix AWQ MoE marlin check issue in marlin_utils.py for AMD backend |
| `pr-vllm-30116` | upstream-code | [`sources/prs/vllm/PR-30116.md`](../sources/prs/vllm/PR-30116.md) | [Model][Quantization] Restore MoE + GGUF models support (incl. Qwen3 MoE) by allowing Sideload Parameters |
| `pr-vllm-30141` | upstream-code | [`sources/prs/vllm/PR-30141.md`](../sources/prs/vllm/PR-30141.md) | Add llmcompressor fp8 kv-cache quant (per-tensor and per-attn_head) |
| `pr-vllm-30156` | upstream-code | [`sources/prs/vllm/PR-30156.md`](../sources/prs/vllm/PR-30156.md) | feat: add TxtSlicesDataset to allow sampling slices from txt file for benchmarking |
| `pr-vllm-30164` | upstream-code | [`sources/prs/vllm/PR-30164.md`](../sources/prs/vllm/PR-30164.md) | Nvidia ModelOpt workaround for issue 28072 |
| `pr-vllm-30195` | upstream-code | [`sources/prs/vllm/PR-30195.md`](../sources/prs/vllm/PR-30195.md) | [BugFix][DeepSeek-V3.2] Fix backend selection logic for Blackwell |
| `pr-vllm-30210` | upstream-code | [`sources/prs/vllm/PR-30210.md`](../sources/prs/vllm/PR-30210.md) | [Bugfix]: Fix glm46 awq marlin moe wna16 compatibility |
| `pr-vllm-30212` | upstream-code | [`sources/prs/vllm/PR-30212.md`](../sources/prs/vllm/PR-30212.md) | [Platform] Refactor Platform attention backend selection to avoid breakpoint for OOT platform |
| `pr-vllm-30241` | upstream-code | [`sources/prs/vllm/PR-30241.md`](../sources/prs/vllm/PR-30241.md) | [bug] Fix "Current vLLM config is not set." warnings when FlashInfer attention is used |
| `pr-vllm-30254` | upstream-code | [`sources/prs/vllm/PR-30254.md`](../sources/prs/vllm/PR-30254.md) | gptq marlin quantization support for fused moe with lora |
| `pr-vllm-30267` | upstream-code | [`sources/prs/vllm/PR-30267.md`](../sources/prs/vllm/PR-30267.md) | [Bugfix] Fix DeepGEMM after #29546  |
| `pr-vllm-30282` | upstream-code | [`sources/prs/vllm/PR-30282.md`](../sources/prs/vllm/PR-30282.md) | [Feat] Refactor for `parallel_config` in `FusedMoEModularKernel` |
| `pr-vllm-30286` | upstream-code | [`sources/prs/vllm/PR-30286.md`](../sources/prs/vllm/PR-30286.md) | [LoRA] Support Quantized Adapters |
| `pr-vllm-30314` | upstream-code | [`sources/prs/vllm/PR-30314.md`](../sources/prs/vllm/PR-30314.md) | [fix] fix SM check for Flashinfer TRTLLM MOE |
| `pr-vllm-30336` | upstream-code | [`sources/prs/vllm/PR-30336.md`](../sources/prs/vllm/PR-30336.md) | [Bugfix] Fix fp8 DeepGemm compilation issues |
| `pr-vllm-30357` | upstream-code | [`sources/prs/vllm/PR-30357.md`](../sources/prs/vllm/PR-30357.md) | [ROCm][Quantization] GPT OSS Upstream MoE wmxfp4_afp8 with static scales |
| `pr-vllm-30361` | upstream-code | [`sources/prs/vllm/PR-30361.md`](../sources/prs/vllm/PR-30361.md) | [Attention][AMD] Make flash-attn optional |
| `pr-vllm-30399` | upstream-code | [`sources/prs/vllm/PR-30399.md`](../sources/prs/vllm/PR-30399.md) | [BugFix] Fix `AttributeError: 'MergedColumnParallelLinear' object has no attribute 'weight_scale'` |
| `pr-vllm-30408` | upstream-code | [`sources/prs/vllm/PR-30408.md`](../sources/prs/vllm/PR-30408.md) | fix(gguf): Disable bfloat16 for GGUF on blackwell device |
| `pr-vllm-30430` | upstream-code | [`sources/prs/vllm/PR-30430.md`](../sources/prs/vllm/PR-30430.md) | [ROCm][Bugfix] Add MLACommonMetadata to allowed attention types for speculative decoding |
| `pr-vllm-30484` | upstream-code | [`sources/prs/vllm/PR-30484.md`](../sources/prs/vllm/PR-30484.md) | [Feature] Add SM103 (Blackwell Ultra) Support to vLLM |
| `pr-vllm-30515` | upstream-code | [`sources/prs/vllm/PR-30515.md`](../sources/prs/vllm/PR-30515.md) | [UX][Startup] Account for CUDA graphs during memory profiling |
| `pr-vllm-30519` | upstream-code | [`sources/prs/vllm/PR-30519.md`](../sources/prs/vllm/PR-30519.md) | [Misc][Refactor] Add FusedMoERouter object |
| `pr-vllm-30528` | upstream-code | [`sources/prs/vllm/PR-30528.md`](../sources/prs/vllm/PR-30528.md) | [Perf] Set split_k to 1 for triton_kernels |
| `pr-vllm-30531` | upstream-code | [`sources/prs/vllm/PR-30531.md`](../sources/prs/vllm/PR-30531.md) | [CPU] Refactor CPU fused MOE |
| `pr-vllm-30562` | upstream-code | [`sources/prs/vllm/PR-30562.md`](../sources/prs/vllm/PR-30562.md) | [Refactor] Small refactor for group topk |
| `pr-vllm-30575` | upstream-code | [`sources/prs/vllm/PR-30575.md`](../sources/prs/vllm/PR-30575.md) | [Bugfix] Pass FA version in `MultiHeadAttention` |
| `pr-vllm-30585` | upstream-code | [`sources/prs/vllm/PR-30585.md`](../sources/prs/vllm/PR-30585.md) | [Bugfix] Fix Triton FusedMoE LoRA |
| `pr-vllm-30623` | upstream-code | [`sources/prs/vllm/PR-30623.md`](../sources/prs/vllm/PR-30623.md) | [MoE Refactor] Separate Router into OO Classes |
| `pr-vllm-30627` | upstream-code | [`sources/prs/vllm/PR-30627.md`](../sources/prs/vllm/PR-30627.md) | [MoE][Refactor 1/N] Separate Online Quantization |
| `pr-vllm-30647` | upstream-code | [`sources/prs/vllm/PR-30647.md`](../sources/prs/vllm/PR-30647.md) | [Perf] Eliminate padding and slicing op for GPT-OSS with Flashinfer MXFP4 MXFP8 MoE |
| `pr-vllm-30684` | upstream-code | [`sources/prs/vllm/PR-30684.md`](../sources/prs/vllm/PR-30684.md) | [MM Encoder]: Migrate legacy ViT `MultiHeadAttention` to new `MMEncoderAttention` interface |
| `pr-vllm-30687` | upstream-code | [`sources/prs/vllm/PR-30687.md`](../sources/prs/vllm/PR-30687.md) | Triton Attention: Support cross-layers blocks |
| `pr-vllm-30692` | upstream-code | [`sources/prs/vllm/PR-30692.md`](../sources/prs/vllm/PR-30692.md) | OffloadingConnector: Support kernel_block_size != block_size |
| `pr-vllm-30709` | upstream-code | [`sources/prs/vllm/PR-30709.md`](../sources/prs/vllm/PR-30709.md) | [Misc][LLaMa4] Compile LLaMa Vision Encoder |
| `pr-vllm-30713` | upstream-code | [`sources/prs/vllm/PR-30713.md`](../sources/prs/vllm/PR-30713.md) | [TRTLLM] Remove the MoE GEMM weight name change |
| `pr-vllm-30716` | upstream-code | [`sources/prs/vllm/PR-30716.md`](../sources/prs/vllm/PR-30716.md) | fused_moe_lora PDL improvements |
| `pr-vllm-30746` | upstream-code | [`sources/prs/vllm/PR-30746.md`](../sources/prs/vllm/PR-30746.md) | [SM100] Enable fp8 compute for prefill MLA |
| `pr-vllm-30802` | upstream-code | [`sources/prs/vllm/PR-30802.md`](../sources/prs/vllm/PR-30802.md) | Add support for LoRA adapters in Nemotron-H models |
| `pr-vllm-30825` | upstream-code | [`sources/prs/vllm/PR-30825.md`](../sources/prs/vllm/PR-30825.md) | [MoE Refactor][2/N] Use Modular Kernels for Fp8 |
| `pr-vllm-30842` | upstream-code | [`sources/prs/vllm/PR-30842.md`](../sources/prs/vllm/PR-30842.md) | [Kernels][FI] Skip trtllm attention when num_kv_heads=1 |
| `pr-vllm-30869` | upstream-code | [`sources/prs/vllm/PR-30869.md`](../sources/prs/vllm/PR-30869.md) | [Bugfix] fix the alias bug of AttentionBackendEnum when register CUSTOM attention backend to vllm |
| `pr-vllm-30881` | upstream-code | [`sources/prs/vllm/PR-30881.md`](../sources/prs/vllm/PR-30881.md) | [Compressed-Tensors] Simplify NVFP4 Conditions, enable marlin support for NVFP4A16 MoEs |
| `pr-vllm-30885` | upstream-code | [`sources/prs/vllm/PR-30885.md`](../sources/prs/vllm/PR-30885.md) | [Kernel][Performance] Enable smaller Scaling Factor tiling for NVFP4 small-batch decoding |
| `pr-vllm-30887` | upstream-code | [`sources/prs/vllm/PR-30887.md`](../sources/prs/vllm/PR-30887.md) | [Bugfix] [Kernel] Triton attention kernels: mask out V blocks that fall outside sliding window |
| `pr-vllm-30897` | upstream-code | [`sources/prs/vllm/PR-30897.md`](../sources/prs/vllm/PR-30897.md) | [NVFP4][Perf] Tune NVFP4 input quant kernel for small batch size |
| `pr-vllm-30898` | upstream-code | [`sources/prs/vllm/PR-30898.md`](../sources/prs/vllm/PR-30898.md) | [Refactor] Refactor for `DeepGemmQuantScaleFMT` using cache |
| `pr-vllm-30903` | upstream-code | [`sources/prs/vllm/PR-30903.md`](../sources/prs/vllm/PR-30903.md) | [UX] Reduce DeepGEMM warmup log output to single progress bar |
| `pr-vllm-30957` | upstream-code | [`sources/prs/vllm/PR-30957.md`](../sources/prs/vllm/PR-30957.md) | [Feature]: Support NVIDIA ModelOpt HF FP8 variants FP8_PER_CHANNEL_PER_TOKEN and FP8_PB_WO  in vLLM |
| `pr-vllm-30967` | upstream-code | [`sources/prs/vllm/PR-30967.md`](../sources/prs/vllm/PR-30967.md) | [Misc] Remove unused custom ops `copy_blocks` and `copy_blocks_mla` |
| `pr-vllm-30973` | upstream-code | [`sources/prs/vllm/PR-30973.md`](../sources/prs/vllm/PR-30973.md) | [Bugfix] Remove `tile_size=64` for mm_prefix triton attention |
| `pr-vllm-30974` | upstream-code | [`sources/prs/vllm/PR-30974.md`](../sources/prs/vllm/PR-30974.md) | [Bugfix] Fix incorrect tiles creation for mm prefix triton attention |
| `pr-vllm-31003` | upstream-code | [`sources/prs/vllm/PR-31003.md`](../sources/prs/vllm/PR-31003.md) | [Mics] add pcp basic support to MoE model |
| `pr-vllm-31034` | upstream-code | [`sources/prs/vllm/PR-31034.md`](../sources/prs/vllm/PR-31034.md) | [P/D] rework mooncake connector and introduce its bootstrap server |
| `pr-vllm-31036` | upstream-code | [`sources/prs/vllm/PR-31036.md`](../sources/prs/vllm/PR-31036.md) | [MoE Refactor][4/N] Marlin Fp8 Mk |
| `pr-vllm-31050` | upstream-code | [`sources/prs/vllm/PR-31050.md`](../sources/prs/vllm/PR-31050.md) | [MoE Refactor] Split `invoke_fused_moe_kernel` |
| `pr-vllm-31052` | upstream-code | [`sources/prs/vllm/PR-31052.md`](../sources/prs/vllm/PR-31052.md) | [MoE Refactor][9/N] Use modular kernel for unquantized Triton MoE |
| `pr-vllm-31055` | upstream-code | [`sources/prs/vllm/PR-31055.md`](../sources/prs/vllm/PR-31055.md) | [Bugfix] Fix GLM-4 MoE router logits dtype for data parallel chunking |
| `pr-vllm-31099` | upstream-code | [`sources/prs/vllm/PR-31099.md`](../sources/prs/vllm/PR-31099.md) |  [FIX] Always support TP > 4 for FP4 Gemm |
| `pr-vllm-31102` | upstream-code | [`sources/prs/vllm/PR-31102.md`](../sources/prs/vllm/PR-31102.md) | [MoE Refactor][7/N] AITER MK |
| `pr-vllm-31104` | upstream-code | [`sources/prs/vllm/PR-31104.md`](../sources/prs/vllm/PR-31104.md) | [BugFix] LoRA: Support loading base_layer of experts |
| `pr-vllm-31106` | upstream-code | [`sources/prs/vllm/PR-31106.md`](../sources/prs/vllm/PR-31106.md) | [Bugfix][Hardware][AMD] Consolidate FP8 min/max values helper function |
| `pr-vllm-31115` | upstream-code | [`sources/prs/vllm/PR-31115.md`](../sources/prs/vllm/PR-31115.md) | [Misc] Fix grammar errors in comments and messages |
| `pr-vllm-31153` | upstream-code | [`sources/prs/vllm/PR-31153.md`](../sources/prs/vllm/PR-31153.md) | [Chore] Update more locations to use `attention_config.backend` |
| `pr-vllm-31156` | upstream-code | [`sources/prs/vllm/PR-31156.md`](../sources/prs/vllm/PR-31156.md) | [ROCm] [Critical]: Remove unused variable |
| `pr-vllm-31167` | upstream-code | [`sources/prs/vllm/PR-31167.md`](../sources/prs/vllm/PR-31167.md) | [Perf] Remove blocking copy in GDN Attention |
| `pr-vllm-31169` | upstream-code | [`sources/prs/vllm/PR-31169.md`](../sources/prs/vllm/PR-31169.md) | [MoE Refactor][10/N] Cleanup Fp8 Process Weights After Loading |
| `pr-vllm-31171` | upstream-code | [`sources/prs/vllm/PR-31171.md`](../sources/prs/vllm/PR-31171.md) | [perf] Integrate flashinfer concat_mla_k |
| `pr-vllm-31195` | upstream-code | [`sources/prs/vllm/PR-31195.md`](../sources/prs/vllm/PR-31195.md) | [SM100] Resubmit FMHA FP8 prefill for MLA |
| `pr-vllm-31246` | upstream-code | [`sources/prs/vllm/PR-31246.md`](../sources/prs/vllm/PR-31246.md) | [Kernel] Add topk_sigmoid kernel |
| `pr-vllm-31282` | upstream-code | [`sources/prs/vllm/PR-31282.md`](../sources/prs/vllm/PR-31282.md) | [Bugfix][Hardware][AMD] Fix last_page_len calculation in AITER MLA decode |
| `pr-vllm-31286` | upstream-code | [`sources/prs/vllm/PR-31286.md`](../sources/prs/vllm/PR-31286.md) | fix(rocm): add early return in get_flash_attn_version for ROCm |
| `pr-vllm-31317` | upstream-code | [`sources/prs/vllm/PR-31317.md`](../sources/prs/vllm/PR-31317.md) | pin lora_b moe weights on cpu |
| `pr-vllm-31380` | upstream-code | [`sources/prs/vllm/PR-31380.md`](../sources/prs/vllm/PR-31380.md) | [Bugfix][ROCm]Fix Qwen3-Next-80B-A3B-Thinking inference and optimize non-standard block size (544) support under rocm_atten |
| `pr-vllm-31406` | upstream-code | [`sources/prs/vllm/PR-31406.md`](../sources/prs/vllm/PR-31406.md) | [v1] Add encoder-only/cross attention support to Triton Attention backend |
| `pr-vllm-31415` | upstream-code | [`sources/prs/vllm/PR-31415.md`](../sources/prs/vllm/PR-31415.md) | [MoE Refactor][15/N] Apply Refactor to Fp8 |
| `pr-vllm-31453` | upstream-code | [`sources/prs/vllm/PR-31453.md`](../sources/prs/vllm/PR-31453.md) | [BugFix]  add select_gemm_impl on CompressedTensorsWNA16MoEMethod to support LoRA |
| `pr-vllm-31465` | upstream-code | [`sources/prs/vllm/PR-31465.md`](../sources/prs/vllm/PR-31465.md) | fixed mypy warnings for files vllm/v1/attention with TEMPORARY workaround |
| `pr-vllm-31499` | upstream-code | [`sources/prs/vllm/PR-31499.md`](../sources/prs/vllm/PR-31499.md) | [MoE Refactor][12/N] Marlin Fp8 MoE Pure Function |
| `pr-vllm-31502` | upstream-code | [`sources/prs/vllm/PR-31502.md`](../sources/prs/vllm/PR-31502.md) | [Bugfix][ROCm] Fix Static Quant Issue |
| `pr-vllm-31504` | upstream-code | [`sources/prs/vllm/PR-31504.md`](../sources/prs/vllm/PR-31504.md) | [MoE Refactor] Explicit construct mk for flashinfer bf16 kernel |
| `pr-vllm-31528` | upstream-code | [`sources/prs/vllm/PR-31528.md`](../sources/prs/vllm/PR-31528.md) | [FIX] Add NO_MUL activation support for modular kernel path |
| `pr-vllm-31531` | upstream-code | [`sources/prs/vllm/PR-31531.md`](../sources/prs/vllm/PR-31531.md) | Use the same memory for workspace13 and fused_output. |
| `pr-vllm-31533` | upstream-code | [`sources/prs/vllm/PR-31533.md`](../sources/prs/vllm/PR-31533.md) | [MoE Refactor][13/N] Convert FI to Use PFNoEP |
| `pr-vllm-31534` | upstream-code | [`sources/prs/vllm/PR-31534.md`](../sources/prs/vllm/PR-31534.md) | [Fix] Align fused moe lora_b shape with peft |
| `pr-vllm-31540` | upstream-code | [`sources/prs/vllm/PR-31540.md`](../sources/prs/vllm/PR-31540.md) | [Bugfix] Fix block size used in EAGLE slot mapping |
| `pr-vllm-31542` | upstream-code | [`sources/prs/vllm/PR-31542.md`](../sources/prs/vllm/PR-31542.md) | [MoE Refactor] Aiter Experts for BF16 MoE |
| `pr-vllm-31571` | upstream-code | [`sources/prs/vllm/PR-31571.md`](../sources/prs/vllm/PR-31571.md) | [Quantization][MoE] remove unused ep logic from moe marlin |
| `pr-vllm-31593` | upstream-code | [`sources/prs/vllm/PR-31593.md`](../sources/prs/vllm/PR-31593.md) | [MoE Refactor][14/N] Clean Up FI Quant Config Smuggling |
| `pr-vllm-31742` | upstream-code | [`sources/prs/vllm/PR-31742.md`](../sources/prs/vllm/PR-31742.md) | [Bugfix] Fix Broken ModelOpt NVFP4 MoE |
| `pr-vllm-31777` | upstream-code | [`sources/prs/vllm/PR-31777.md`](../sources/prs/vllm/PR-31777.md) | [LoRA]Disable linear LoRA  kernel PDL |
| `pr-vllm-31827` | upstream-code | [`sources/prs/vllm/PR-31827.md`](../sources/prs/vllm/PR-31827.md) | [MoE Refactor][17/N] Apply Refactor to Bf16 |
| `pr-vllm-31837` | upstream-code | [`sources/prs/vllm/PR-31837.md`](../sources/prs/vllm/PR-31837.md) | [Perf] Fuse stride preparation for NVFP4 cutlass_moe |
| `pr-vllm-31916` | upstream-code | [`sources/prs/vllm/PR-31916.md`](../sources/prs/vllm/PR-31916.md) | [1/N][Attention] Restructure attention: move files |
| `pr-vllm-32008` | upstream-code | [`sources/prs/vllm/PR-32008.md`](../sources/prs/vllm/PR-32008.md) | [MISC] Add strict contiguity check for FlashInfer attention tensors |
| `pr-vllm-32060` | upstream-code | [`sources/prs/vllm/PR-32060.md`](../sources/prs/vllm/PR-32060.md) | [4/N][Attention] Move MLA common to model_executor |
| `pr-vllm-32064` | upstream-code | [`sources/prs/vllm/PR-32064.md`](../sources/prs/vllm/PR-32064.md) | [5/N][Attention] Finish eliminating `vllm/attention` folder |
| `pr-vllm-32195` | upstream-code | [`sources/prs/vllm/PR-32195.md`](../sources/prs/vllm/PR-32195.md) | Add TMA support to fused_moe_lora kernel |
| `pr-vllm-32339` | upstream-code | [`sources/prs/vllm/PR-32339.md`](../sources/prs/vllm/PR-32339.md) | [Attention][MLA] Make `FLASHINFER_MLA` the default MLA backend on Blackwell, and TRTLLM the default prefill |
| `pr-vllm-32361` | upstream-code | [`sources/prs/vllm/PR-32361.md`](../sources/prs/vllm/PR-32361.md) | [BugFix] Fix DeepSeek-V3.1 + DeepGEMM incompatible scale shapes |
| `pr-vllm-32362` | upstream-code | [`sources/prs/vllm/PR-32362.md`](../sources/prs/vllm/PR-32362.md) | [BugFix] Fix `assert x_s.shape[-1] == x_q.shape[-1] // group_shape[1]` in Blackwell Quantized MoE Test |
| `pr-vllm-32437` | upstream-code | [`sources/prs/vllm/PR-32437.md`](../sources/prs/vllm/PR-32437.md) | [Hardware][SM100] Add TRTLLM Kernel for INT4 W4A16 Kernel. |
| `pr-vllm-32477` | upstream-code | [`sources/prs/vllm/PR-32477.md`](../sources/prs/vllm/PR-32477.md) | [7/N][Attention][Docs] Add documentation for attention backends |
| `pr-vllm-32520` | upstream-code | [`sources/prs/vllm/PR-32520.md`](../sources/prs/vllm/PR-32520.md) | [Perf][Kernel] Optimize FP4 quantization kernels (SM100F) |
| `pr-vllm-32564` | upstream-code | [`sources/prs/vllm/PR-32564.md`](../sources/prs/vllm/PR-32564.md) | [MoE Refactor] Create MK for TRTLLM Kernels |
| `pr-vllm-32614` | upstream-code | [`sources/prs/vllm/PR-32614.md`](../sources/prs/vllm/PR-32614.md) | fix: Add glm4_moe_lite to MLA detection |
| `pr-vllm-32615` | upstream-code | [`sources/prs/vllm/PR-32615.md`](../sources/prs/vllm/PR-32615.md) | [Attention][MLA] Make FLASHINFER_MLA the default MLA backend on Blackwell, and TRTLLM the default prefill |
| `pr-vllm-32619` | upstream-code | [`sources/prs/vllm/PR-32619.md`](../sources/prs/vllm/PR-32619.md) | [Perf] Create TMA-aligned input scale tensor for DeepGemm on Hopper |
| `pr-vllm-32771` | upstream-code | [`sources/prs/vllm/PR-32771.md`](../sources/prs/vllm/PR-32771.md) | [Model Runner V2] support piecewise & mixed cudagraph |
| `pr-vllm-32795` | upstream-code | [`sources/prs/vllm/PR-32795.md`](../sources/prs/vllm/PR-32795.md) | [Bugfix][Attention] Explicitly report support for kv_cache_dtype bfloat16 |
| `pr-vllm-32887` | upstream-code | [`sources/prs/vllm/PR-32887.md`](../sources/prs/vllm/PR-32887.md) | [Spec Decode] Unified Parallel Drafting |
| `pr-vllm-32914` | upstream-code | [`sources/prs/vllm/PR-32914.md`](../sources/prs/vllm/PR-32914.md) | [ROCm][perf] Shuffle KV cache to use paged_attention_common |
| `pr-vllm-32936` | upstream-code | [`sources/prs/vllm/PR-32936.md`](../sources/prs/vllm/PR-32936.md) | [Model Runner V2] support auto resolve cudagraph mode/sizes based on attn backend |
| `pr-vllm-32954` | upstream-code | [`sources/prs/vllm/PR-32954.md`](../sources/prs/vllm/PR-32954.md) | [NVIDIA] [feat] Integrate flashinfer Trtllmgen bf16 moe |
| `pr-vllm-32974` | upstream-code | [`sources/prs/vllm/PR-32974.md`](../sources/prs/vllm/PR-32974.md) | [Attention] FA4 integration |
| `pr-vllm-32993` | upstream-code | [`sources/prs/vllm/PR-32993.md`](../sources/prs/vllm/PR-32993.md) | [Feature] Support CPU Offloading without Pytorch Pinned Memory that leads to doubled allocation |
| `pr-vllm-33022` | upstream-code | [`sources/prs/vllm/PR-33022.md`](../sources/prs/vllm/PR-33022.md) | [Kernel] Apply 256bit LDG/STG To Activation Kernels |
| `pr-vllm-33049` | upstream-code | [`sources/prs/vllm/PR-33049.md`](../sources/prs/vllm/PR-33049.md) | [MoE Refactor] DefaultMoERunner simplifcation |
| `pr-vllm-33076` | upstream-code | [`sources/prs/vllm/PR-33076.md`](../sources/prs/vllm/PR-33076.md) | Support compress-tensors with nvfp4 or fp8 weights and modelopt with nvfp4 weights on Turing |
| `pr-vllm-33174` | upstream-code | [`sources/prs/vllm/PR-33174.md`](../sources/prs/vllm/PR-33174.md) | Add support for Mistral Large 3 inference with Flashinfer MoE |
| `pr-vllm-33177` | upstream-code | [`sources/prs/vllm/PR-33177.md`](../sources/prs/vllm/PR-33177.md) | [Attention] Use `has_flashinfer` helper |
| `pr-vllm-33192` | upstream-code | [`sources/prs/vllm/PR-33192.md`](../sources/prs/vllm/PR-33192.md) | [Bugfix] Disable TRTLLM attention when KV transfer is enabled |
| `pr-vllm-33201` | upstream-code | [`sources/prs/vllm/PR-33201.md`](../sources/prs/vllm/PR-33201.md) | Refactor NVFP4 Linear utils for ModelOpt and CT |
| `pr-vllm-33230` | upstream-code | [`sources/prs/vllm/PR-33230.md`](../sources/prs/vllm/PR-33230.md) | Add XPU MLA Sparse backend for DeepSeek v3.2 |
| `pr-vllm-33255` | upstream-code | [`sources/prs/vllm/PR-33255.md`](../sources/prs/vllm/PR-33255.md) | [Bugfix] Fix quant RMS norm fusion for quantization with TMA-aligned scales |
| `pr-vllm-33284` | upstream-code | [`sources/prs/vllm/PR-33284.md`](../sources/prs/vllm/PR-33284.md) | [Attention] Move MLA `forward` from backend to layer |
| `pr-vllm-33285` | upstream-code | [`sources/prs/vllm/PR-33285.md`](../sources/prs/vllm/PR-33285.md) | [Bugfix] Register fp8 cutlass_group_gemm as supported for only SM90+SM100 |
| `pr-vllm-33417` | upstream-code | [`sources/prs/vllm/PR-33417.md`](../sources/prs/vllm/PR-33417.md) | fix: Add SM120 (RTX Blackwell) support for FlashInfer CUTLASS NVFP4 MoE kernels |
| `pr-vllm-33451` | upstream-code | [`sources/prs/vllm/PR-33451.md`](../sources/prs/vllm/PR-33451.md) | [Attention] Add FlashInfer Sparse MLA backend |
| `pr-vllm-33462` | upstream-code | [`sources/prs/vllm/PR-33462.md`](../sources/prs/vllm/PR-33462.md) | [Misc] Fix flashinfer related tests |
| `pr-vllm-33506` | upstream-code | [`sources/prs/vllm/PR-33506.md`](../sources/prs/vllm/PR-33506.md) | [Kernel] Support Flashinfer trtllm fused MoE non gated FP8 & NVFP4 |
| `pr-vllm-33511` | upstream-code | [`sources/prs/vllm/PR-33511.md`](../sources/prs/vllm/PR-33511.md) | fix(ROCm): Make flash_attn import optional in MLA attention |
| `pr-vllm-33517` | upstream-code | [`sources/prs/vllm/PR-33517.md`](../sources/prs/vllm/PR-33517.md) | [Kernel] Add enable_sm120_or_later for SM121 (DGX Spark) CUTLASS support |
| `pr-vllm-33529` | upstream-code | [`sources/prs/vllm/PR-33529.md`](../sources/prs/vllm/PR-33529.md) | Triton MLA perf fixes |
| `pr-vllm-33540` | upstream-code | [`sources/prs/vllm/PR-33540.md`](../sources/prs/vllm/PR-33540.md) | [Feature][Core] Support Fabric detection to adapt the MNNVL protocol for the GB series |
| `pr-vllm-33568` | upstream-code | [`sources/prs/vllm/PR-33568.md`](../sources/prs/vllm/PR-33568.md) | [Perf] Disable clean_logits in deepgemm fp8_mqa_logits kernel |
| `pr-vllm-33579` | upstream-code | [`sources/prs/vllm/PR-33579.md`](../sources/prs/vllm/PR-33579.md) | [Bugfix] Fix sparse MLA metadata building |
| `pr-vllm-33595` | upstream-code | [`sources/prs/vllm/PR-33595.md`](../sources/prs/vllm/PR-33595.md) | [MoE] Add routing simulation override for MXFP4 quantized MoE |
| `pr-vllm-33600` | upstream-code | [`sources/prs/vllm/PR-33600.md`](../sources/prs/vllm/PR-33600.md) | [Attention] Refactor `check_and_update_config` |
| `pr-vllm-33637` | upstream-code | [`sources/prs/vllm/PR-33637.md`](../sources/prs/vllm/PR-33637.md) | [Bugfix] fix DeepSeek R1 with CUTLASS MLA Broken on B200 |
| `pr-vllm-33695` | upstream-code | [`sources/prs/vllm/PR-33695.md`](../sources/prs/vllm/PR-33695.md) | enable skipping of SW attention layers when using FP8 KV cache |
| `pr-vllm-33738` | upstream-code | [`sources/prs/vllm/PR-33738.md`](../sources/prs/vllm/PR-33738.md) | [WideEP] Fix nvfp4 DeepEP High Throughput All2All backend |
| `pr-vllm-33810` | upstream-code | [`sources/prs/vllm/PR-33810.md`](../sources/prs/vllm/PR-33810.md) | [Misc] Fix up attention benchmarks |
| `pr-vllm-33892` | upstream-code | [`sources/prs/vllm/PR-33892.md`](../sources/prs/vllm/PR-33892.md) | [W8A8 Block Linear Refactor][2/N] Remove W8A8Fp8BlockLinearOp and adopt Fp8 block linear kernel selections. |
| `pr-vllm-33919` | upstream-code | [`sources/prs/vllm/PR-33919.md`](../sources/prs/vllm/PR-33919.md) | Fix RoutingMethodType logic |
| `pr-vllm-33932` | upstream-code | [`sources/prs/vllm/PR-33932.md`](../sources/prs/vllm/PR-33932.md) | [Bugfix] Fix DSV3.2 NVFP4 |
| `pr-vllm-33972` | upstream-code | [`sources/prs/vllm/PR-33972.md`](../sources/prs/vllm/PR-33972.md) | [Bugfix]fix output Nan/Inf in marlin if dtype=float16 |
| `pr-vllm-33992` | upstream-code | [`sources/prs/vllm/PR-33992.md`](../sources/prs/vllm/PR-33992.md) | [Bugfix] Fix CUDA compatibility path setting for both datacenter and consumer NVIDIA GPUs |
| `pr-vllm-34043` | upstream-code | [`sources/prs/vllm/PR-34043.md`](../sources/prs/vllm/PR-34043.md) | Reapply [Attention][FA3] Update FA3 to include new swizzle optimization |
| `pr-vllm-34052` | upstream-code | [`sources/prs/vllm/PR-34052.md`](../sources/prs/vllm/PR-34052.md) | fix(cpu): fix mla_decode compilation on x86 without AVX512 |
| `pr-vllm-34109` | upstream-code | [`sources/prs/vllm/PR-34109.md`](../sources/prs/vllm/PR-34109.md) | [Kernel] Refactor FlashInfer allreduce for mnnvl backend |
| `pr-vllm-34158` | upstream-code | [`sources/prs/vllm/PR-34158.md`](../sources/prs/vllm/PR-34158.md) | [Bugfix] Relax TRTLLM KV cache contiguity assertion for cross-layer layout |
| `pr-vllm-34206` | upstream-code | [`sources/prs/vllm/PR-34206.md`](../sources/prs/vllm/PR-34206.md) | [Kernel] Optimize grouped topk kernel |
| `pr-vllm-34260` | upstream-code | [`sources/prs/vllm/PR-34260.md`](../sources/prs/vllm/PR-34260.md) | [Model Bash]: Improve FP8 Oracle for Config Specific Kernel Selection |
| `pr-vllm-34270` | upstream-code | [`sources/prs/vllm/PR-34270.md`](../sources/prs/vllm/PR-34270.md) | fix(mxfp4): Disable monolithic path for TRITON backend with EP |
| `pr-vllm-34285` | upstream-code | [`sources/prs/vllm/PR-34285.md`](../sources/prs/vllm/PR-34285.md) | [Refactor] Move FusedMoE hidden_size roundup to quant_method |
| `pr-vllm-34298` | upstream-code | [`sources/prs/vllm/PR-34298.md`](../sources/prs/vllm/PR-34298.md) | [ModelBash][DSR1 NVFp4] Avoid Bf16 Bias Cast |
| `pr-vllm-34302` | upstream-code | [`sources/prs/vllm/PR-34302.md`](../sources/prs/vllm/PR-34302.md) | [ModelBash][DSV3] Add TRTLLM DSV3 Router GEMM kernel (6% B1 Speedup) |
| `pr-vllm-34389` | upstream-code | [`sources/prs/vllm/PR-34389.md`](../sources/prs/vllm/PR-34389.md) | [Custom Ops] Add functional + out variant for scaled_fp4_quant |
| `pr-vllm-34434` | upstream-code | [`sources/prs/vllm/PR-34434.md`](../sources/prs/vllm/PR-34434.md) | [CPU][Perf] Accelerate Attention head for s390x using vector intrinsics |
| `pr-vllm-34448` | upstream-code | [`sources/prs/vllm/PR-34448.md`](../sources/prs/vllm/PR-34448.md) | [Kernel] Integrate SM100 MXFP8 blockscaled grouped MM and quant kernels |
| `pr-vllm-34457` | upstream-code | [`sources/prs/vllm/PR-34457.md`](../sources/prs/vllm/PR-34457.md) | [Bugfix][MTP][Sparse MLA] Allow sparse MLA with MTP to run with FULL cudagraphs |
| `pr-vllm-34478` | upstream-code | [`sources/prs/vllm/PR-34478.md`](../sources/prs/vllm/PR-34478.md) | [Model] Add NVFP4 quantization support for Step3.5-Flash |
| `pr-vllm-34494` | upstream-code | [`sources/prs/vllm/PR-34494.md`](../sources/prs/vllm/PR-34494.md) | [Bugfix] Handle num_expert_group=None in flashinfer block-scale FP8 MoE |
| `pr-vllm-34542` | upstream-code | [`sources/prs/vllm/PR-34542.md`](../sources/prs/vllm/PR-34542.md) | [MoE Refactor] MXFP4 Cutlass Experts to MK |
| `pr-vllm-34552` | upstream-code | [`sources/prs/vllm/PR-34552.md`](../sources/prs/vllm/PR-34552.md) | [BugFix] Add support for MTP num_speculative_tokens > 1 with sparse MLA |
| `pr-vllm-34556` | upstream-code | [`sources/prs/vllm/PR-34556.md`](../sources/prs/vllm/PR-34556.md) | [Quantization] add humming quantization kernel |
| `pr-vllm-34577` | upstream-code | [`sources/prs/vllm/PR-34577.md`](../sources/prs/vllm/PR-34577.md) | [Bugfix] Rescale NVFP4 weight scales to fix BF16 dequant underflow |
| `pr-vllm-34580` | upstream-code | [`sources/prs/vllm/PR-34580.md`](../sources/prs/vllm/PR-34580.md) | Flashinfer cuDNN backend for Qwen3 VL ViT attention |
| `pr-vllm-34597` | upstream-code | [`sources/prs/vllm/PR-34597.md`](../sources/prs/vllm/PR-34597.md) | [Kernel] Add FP8 KV cache support to Triton MLA decode attention |
| `pr-vllm-34627` | upstream-code | [`sources/prs/vllm/PR-34627.md`](../sources/prs/vllm/PR-34627.md) | [Performance] Extract kv update ops from MLA attention backends |
| `pr-vllm-34664` | upstream-code | [`sources/prs/vllm/PR-34664.md`](../sources/prs/vllm/PR-34664.md) | [Kernel] Add MXFP8 to Marlin GEMM/MoE and refactor Mxfp8LinearOp |
| `pr-vllm-34673` | upstream-code | [`sources/prs/vllm/PR-34673.md`](../sources/prs/vllm/PR-34673.md) | [Bugfix][MoE Kernel] Fix incorrect routing selection for models without expert groups (e.g., MiniMax-M2.1) |
| `pr-vllm-34687` | upstream-code | [`sources/prs/vllm/PR-34687.md`](../sources/prs/vllm/PR-34687.md) | [Update] Use FlashInfer fast_decode_plan directly instead of replication |
| `pr-vllm-34695` | upstream-code | [`sources/prs/vllm/PR-34695.md`](../sources/prs/vllm/PR-34695.md) | [Bugfix] Fix MLA attention crash with AWQ/GPTQ quantized models |
| `pr-vllm-34725` | upstream-code | [`sources/prs/vllm/PR-34725.md`](../sources/prs/vllm/PR-34725.md) | [Bugfix] Fix NVFP4 TRTLLM MoE non-gated support; add gsm8k for Nemotron-3-Nano FP8+NVFP4 |
| `pr-vllm-34732` | upstream-code | [`sources/prs/vllm/PR-34732.md`](../sources/prs/vllm/PR-34732.md) | [Attention] Use FA4 for MLA prefill |
| `pr-vllm-34758` | upstream-code | [`sources/prs/vllm/PR-34758.md`](../sources/prs/vllm/PR-34758.md) | [Model Bash] DeepSeek R1 BF16 Min Latency QKV A GEMM (0.5% E2E Speedup) |
| `pr-vllm-34791` | upstream-code | [`sources/prs/vllm/PR-34791.md`](../sources/prs/vllm/PR-34791.md) | [Bugfix] Gate 256-bit instructions to CUDA 12.9+ |
| `pr-vllm-34871` | upstream-code | [`sources/prs/vllm/PR-34871.md`](../sources/prs/vllm/PR-34871.md) | [Bugfix] Fix GDN attention crash with mixed decode/spec-decode batches |
| `pr-vllm-34883` | upstream-code | [`sources/prs/vllm/PR-34883.md`](../sources/prs/vllm/PR-34883.md) | [Core] Add All-to-All communication backend for DCP  |
| `pr-vllm-34900` | upstream-code | [`sources/prs/vllm/PR-34900.md`](../sources/prs/vllm/PR-34900.md) | [Model Bash][DSR1] Add selective dynamic shape marking for CustomOp |
| `pr-vllm-34916` | upstream-code | [`sources/prs/vllm/PR-34916.md`](../sources/prs/vllm/PR-34916.md) | [Minor] Add logging when using MXFP4 MXFP8 TRTLLM backend |
| `pr-vllm-34917` | upstream-code | [`sources/prs/vllm/PR-34917.md`](../sources/prs/vllm/PR-34917.md) | [Attention][Perf][Kernel] Replace torch.cat with vectorized CUDA kernel MLA query concat - DeepSeek-V3.2 |
| `pr-vllm-34924` | upstream-code | [`sources/prs/vllm/PR-34924.md`](../sources/prs/vllm/PR-34924.md) | [Perf] Enable FlashInfer DeepGEMM swapAB on SM90 by default |
| `pr-vllm-35036` | upstream-code | [`sources/prs/vllm/PR-35036.md`](../sources/prs/vllm/PR-35036.md) | [Model Runner V2] Support attention group |
| `pr-vllm-35047` | upstream-code | [`sources/prs/vllm/PR-35047.md`](../sources/prs/vllm/PR-35047.md) | add mixed precision support for modelopt |
| `pr-vllm-35053` | upstream-code | [`sources/prs/vllm/PR-35053.md`](../sources/prs/vllm/PR-35053.md) | Integrate flashinfer mm_mxfp8 in ModelOpt MXFP8 |
| `pr-vllm-35075` | upstream-code | [`sources/prs/vllm/PR-35075.md`](../sources/prs/vllm/PR-35075.md) | [Bug][DSV3.2] Always prepare metadata for DeepGEMM Sparse Attention |
| `pr-vllm-35088` | upstream-code | [`sources/prs/vllm/PR-35088.md`](../sources/prs/vllm/PR-35088.md) | Fix fallback to default tactic (flashinfer autotuner) with trtllm_fp4_block_scale_moe |
| `pr-vllm-35105` | upstream-code | [`sources/prs/vllm/PR-35105.md`](../sources/prs/vllm/PR-35105.md) | [Refactor][Kernel] Add global helper to deduplicate vectorized memory ops |
| `pr-vllm-35121` | upstream-code | [`sources/prs/vllm/PR-35121.md`](../sources/prs/vllm/PR-35121.md) | [Performance] Cublas Bf16 Gate with Fp32 Output |
| `pr-vllm-35122` | upstream-code | [`sources/prs/vllm/PR-35122.md`](../sources/prs/vllm/PR-35122.md) | Reapply [Attention] Refactor `check_and_update_config` |
| `pr-vllm-35123` | upstream-code | [`sources/prs/vllm/PR-35123.md`](../sources/prs/vllm/PR-35123.md) | [Bugfix] Fix DSV3 kernels breaking _C and _moe_C on unsupported arches |
| `pr-vllm-35161` | upstream-code | [`sources/prs/vllm/PR-35161.md`](../sources/prs/vllm/PR-35161.md) | [Bugfix] Fix expert_ids padding values in moe_align_block_size kernel |
| `pr-vllm-35175` | upstream-code | [`sources/prs/vllm/PR-35175.md`](../sources/prs/vllm/PR-35175.md) | [Bugfix] Restore CUDA graph persistent buffers for FP8 FlashMLA decode |
| `pr-vllm-35210` | upstream-code | [`sources/prs/vllm/PR-35210.md`](../sources/prs/vllm/PR-35210.md) | [BugFix] Fix fp4 quant kernel on CUDA 12.8 |
| `pr-vllm-35219` | upstream-code | [`sources/prs/vllm/PR-35219.md`](../sources/prs/vllm/PR-35219.md) | [BUGFIX][Mamba][Qwen3.5] Zero freed SSM cache blocks on GPU |
| `pr-vllm-35246` | upstream-code | [`sources/prs/vllm/PR-35246.md`](../sources/prs/vllm/PR-35246.md) | [ROCm] Refactor ROCm attention backend selection logic |
| `pr-vllm-35271` | upstream-code | [`sources/prs/vllm/PR-35271.md`](../sources/prs/vllm/PR-35271.md) | [Feat] Add CUDA torch fallbacks for fp8_mqa_logits/fp8_paged_mqa_logits_torch function |
| `pr-vllm-35290` | upstream-code | [`sources/prs/vllm/PR-35290.md`](../sources/prs/vllm/PR-35290.md) | [Attention][Perf] Optimize cp_gather_and_upconvert_fp8_kv_cache - DeepSeek-v3.2 |
| `pr-vllm-35382` | upstream-code | [`sources/prs/vllm/PR-35382.md`](../sources/prs/vllm/PR-35382.md) | fix(mxfp4): return is_monolithic=False when LoRA is enabled for Triton backend |
| `pr-vllm-35418` | upstream-code | [`sources/prs/vllm/PR-35418.md`](../sources/prs/vllm/PR-35418.md) | [Refactor] Remove dead code for attention benchmark script |
| `pr-vllm-35422` | upstream-code | [`sources/prs/vllm/PR-35422.md`](../sources/prs/vllm/PR-35422.md) | [Performance] Extract KV cache update op from flashinfer forward |
| `pr-vllm-35430` | upstream-code | [`sources/prs/vllm/PR-35430.md`](../sources/prs/vllm/PR-35430.md) | [Bugfix] Fix KV Scale loading for MLA Models |
| `pr-vllm-35448` | upstream-code | [`sources/prs/vllm/PR-35448.md`](../sources/prs/vllm/PR-35448.md) | [Quant][Feature] Support online MXFP8 quantization for MoE and dense models |
| `pr-vllm-35719` | upstream-code | [`sources/prs/vllm/PR-35719.md`](../sources/prs/vllm/PR-35719.md) | [ROCm][Perf] Enable `sparse_mla`'s cudagraph on ROCm platform |
| `pr-vllm-35733` | upstream-code | [`sources/prs/vllm/PR-35733.md`](../sources/prs/vllm/PR-35733.md) | [NVFP4] Support NVFP4 dense models from `modelopt` and `compressed-tensors` on AMD Instinct MI300, MI355X and Hopper through emulation |
| `pr-vllm-35765` | upstream-code | [`sources/prs/vllm/PR-35765.md`](../sources/prs/vllm/PR-35765.md) | AITER MLA backend: Avoid CPU sync in _build_decode |
| `pr-vllm-35777` | upstream-code | [`sources/prs/vllm/PR-35777.md`](../sources/prs/vllm/PR-35777.md) | [Kernel] Add fused_sigmoid_gating_delta_rule_update kernel for Qwen3 Next |
| `pr-vllm-35850` | upstream-code | [`sources/prs/vllm/PR-35850.md`](../sources/prs/vllm/PR-35850.md) | [ROCm] Support MLA with nhead<16 and FP8 KV cache for TP=8 (Kimi K2.5/Linear) |
| `pr-vllm-35891` | upstream-code | [`sources/prs/vllm/PR-35891.md`](../sources/prs/vllm/PR-35891.md) | [Perf] Support FP8 KV cache for Flashinfer MLA Sparse |
| `pr-vllm-35927` | upstream-code | [`sources/prs/vllm/PR-35927.md`](../sources/prs/vllm/PR-35927.md) | [MoE] Move PF Methods to Folder |
| `pr-vllm-35963` | upstream-code | [`sources/prs/vllm/PR-35963.md`](../sources/prs/vllm/PR-35963.md) | [Feature] ViT Full CUDA Graph |
| `pr-vllm-35986` | upstream-code | [`sources/prs/vllm/PR-35986.md`](../sources/prs/vllm/PR-35986.md) | Add support for ModelOpt MXFP8 MoE models |
| `pr-vllm-36017` | upstream-code | [`sources/prs/vllm/PR-36017.md`](../sources/prs/vllm/PR-36017.md) | [Bugfix] Fix passing of activation_type to trtllm fused MoE NVFP4 and FP8 |
| `pr-vllm-36022` | upstream-code | [`sources/prs/vllm/PR-36022.md`](../sources/prs/vllm/PR-36022.md) | [Kernel] Add FlashInfer MoE A2A Kernel |
| `pr-vllm-36059` | upstream-code | [`sources/prs/vllm/PR-36059.md`](../sources/prs/vllm/PR-36059.md) | [BugFix] Fallback from FA4->FA2 for Batch Invariance |
| `pr-vllm-36146` | upstream-code | [`sources/prs/vllm/PR-36146.md`](../sources/prs/vllm/PR-36146.md) | [Bugfix] Disable FlashInfer TRTLLM BF16 path for non-gated MoE |
| `pr-vllm-36161` | upstream-code | [`sources/prs/vllm/PR-36161.md`](../sources/prs/vllm/PR-36161.md) | Add 320 dimension size support to MLA |
| `pr-vllm-36162` | upstream-code | [`sources/prs/vllm/PR-36162.md`](../sources/prs/vllm/PR-36162.md) | [Mamba] Flashinfer selective_state_update |
| `pr-vllm-36178` | upstream-code | [`sources/prs/vllm/PR-36178.md`](../sources/prs/vllm/PR-36178.md) | [Bugfix][MLA] Add logits size budget to sparse indexer prefill chunking |
| `pr-vllm-36185` | upstream-code | [`sources/prs/vllm/PR-36185.md`](../sources/prs/vllm/PR-36185.md) | Reenable features for ROCm attention backends |
| `pr-vllm-36205` | upstream-code | [`sources/prs/vllm/PR-36205.md`](../sources/prs/vllm/PR-36205.md) | [mla] Support fused FP8/NVFP4 output quantization in MLA attention (#35792) |
| `pr-vllm-36263` | upstream-code | [`sources/prs/vllm/PR-36263.md`](../sources/prs/vllm/PR-36263.md) | feat(attention): extract KV-cache update from FlexAttention backend |
| `pr-vllm-36282` | upstream-code | [`sources/prs/vllm/PR-36282.md`](../sources/prs/vllm/PR-36282.md) | mla: don't update kv cache on dummy forwards |
| `pr-vllm-36286` | upstream-code | [`sources/prs/vllm/PR-36286.md`](../sources/prs/vllm/PR-36286.md) | [MoE Refactor] Migrate Unquantized to Full Oracle Flow |
| `pr-vllm-36307` | upstream-code | [`sources/prs/vllm/PR-36307.md`](../sources/prs/vllm/PR-36307.md) | [Perf] Add TRTLLM FP8 MoE Modular Kernel |
| `pr-vllm-36361` | upstream-code | [`sources/prs/vllm/PR-36361.md`](../sources/prs/vllm/PR-36361.md) | Kimi k2.5 MLA based eagle3 |
| `pr-vllm-36458` | upstream-code | [`sources/prs/vllm/PR-36458.md`](../sources/prs/vllm/PR-36458.md) | [XPU] Support block fp8 moe by fallback to TritonExpert on XPU |
| `pr-vllm-36466` | upstream-code | [`sources/prs/vllm/PR-36466.md`](../sources/prs/vllm/PR-36466.md) | feat(attention): extract KV-cache update from FlashAttentionDiffKV ba… |
| `pr-vllm-36494` | upstream-code | [`sources/prs/vllm/PR-36494.md`](../sources/prs/vllm/PR-36494.md) | Fix: Re-Enable EP for trtllm MoE FP8 backend |
| `pr-vllm-36518` | upstream-code | [`sources/prs/vllm/PR-36518.md`](../sources/prs/vllm/PR-36518.md) | [Kernel] Fuse FP8 output quantization into merge_attn_states |
| `pr-vllm-36519` | upstream-code | [`sources/prs/vllm/PR-36519.md`](../sources/prs/vllm/PR-36519.md) | [Bugfix][Sparse MLA] report indexer CG support properly |
| `pr-vllm-36540` | upstream-code | [`sources/prs/vllm/PR-36540.md`](../sources/prs/vllm/PR-36540.md) | [fix] Remove trtllm ragged mla prefills |
| `pr-vllm-36574` | upstream-code | [`sources/prs/vllm/PR-36574.md`](../sources/prs/vllm/PR-36574.md) | [ROCm] Utilize persistent MLA kernel from AITER |
| `pr-vllm-36673` | upstream-code | [`sources/prs/vllm/PR-36673.md`](../sources/prs/vllm/PR-36673.md) | [Misc][Attention] Clean up unused method in `CPU_ATTN` |
| `pr-vllm-36674` | upstream-code | [`sources/prs/vllm/PR-36674.md`](../sources/prs/vllm/PR-36674.md) | [Bug] Fix FlashInfer MNNVL socket collisions under concurrent vLLM jobs |
| `pr-vllm-36681` | upstream-code | [`sources/prs/vllm/PR-36681.md`](../sources/prs/vllm/PR-36681.md) | [ROCm][Perf] Allow MTP lens > 1 in Sparse MLA |
| `pr-vllm-36702` | upstream-code | [`sources/prs/vllm/PR-36702.md`](../sources/prs/vllm/PR-36702.md) | [ROCm] Attention selector reordering |
| `pr-vllm-36723` | upstream-code | [`sources/prs/vllm/PR-36723.md`](../sources/prs/vllm/PR-36723.md) | [DSV3.2][MTP] Optimize Indexer MTP handling |
| `pr-vllm-36725` | upstream-code | [`sources/prs/vllm/PR-36725.md`](../sources/prs/vllm/PR-36725.md) | [Bug][MoE] Fix TRTLLM NVFP4 Routing Kernel Precision |
| `pr-vllm-36728` | upstream-code | [`sources/prs/vllm/PR-36728.md`](../sources/prs/vllm/PR-36728.md) | [Bug][MoE] Strengthen _supports_current_device() checks in the TRTLLM FP8, NVFP4, and FlashInfer CuteDSL MoE experts |
| `pr-vllm-36847` | upstream-code | [`sources/prs/vllm/PR-36847.md`](../sources/prs/vllm/PR-36847.md) | [Feat][Spec Decode] DFlash |
| `pr-vllm-36931` | upstream-code | [`sources/prs/vllm/PR-36931.md`](../sources/prs/vllm/PR-36931.md) | [Feat][Bugfix] Enable additional dimension for Flashinfer MLA and fix routing dtype |
| `pr-vllm-36955` | upstream-code | [`sources/prs/vllm/PR-36955.md`](../sources/prs/vllm/PR-36955.md) | [Bugfix] Fix unclean shutdown crash with AllReduce Fusion workspace |
| `pr-vllm-36982` | upstream-code | [`sources/prs/vllm/PR-36982.md`](../sources/prs/vllm/PR-36982.md) | [MTP][Sparse MLA] Take advantage of native MTP support in indexer when possible |
| `pr-vllm-37054` | upstream-code | [`sources/prs/vllm/PR-37054.md`](../sources/prs/vllm/PR-37054.md) | [Bugfix] Fix KV scales inconsistency in fp8 MLA & FlashInfer kv_cache_dtype "auto" leading to gibberish |
| `pr-vllm-37090` | upstream-code | [`sources/prs/vllm/PR-37090.md`](../sources/prs/vllm/PR-37090.md) | [Bugfix] Disable cross-layer KV cache for MLA attention backends |
| `pr-vllm-37115` | upstream-code | [`sources/prs/vllm/PR-37115.md`](../sources/prs/vllm/PR-37115.md) | [Benchmark] Improvements to attention benchmark script |
| `pr-vllm-37128` | upstream-code | [`sources/prs/vllm/PR-37128.md`](../sources/prs/vllm/PR-37128.md) | [MoE Refactor] Mxfp4 oracle rebased |
| `pr-vllm-37143` | upstream-code | [`sources/prs/vllm/PR-37143.md`](../sources/prs/vllm/PR-37143.md) | [XPU] support MLA model on Intel GPU |
| `pr-vllm-37199` | upstream-code | [`sources/prs/vllm/PR-37199.md`](../sources/prs/vllm/PR-37199.md) | [Misc] Add `float16` to `CacheDType` |
| `pr-vllm-37205` | upstream-code | [`sources/prs/vllm/PR-37205.md`](../sources/prs/vllm/PR-37205.md) | [Kernel] Add gpt-oss Router GEMM kernel |
| `pr-vllm-37217` | upstream-code | [`sources/prs/vllm/PR-37217.md`](../sources/prs/vllm/PR-37217.md) | [MoE/EPLB] Fix FlashInfer nvfp4 experts + EPLB correctness |
| `pr-vllm-37228` | upstream-code | [`sources/prs/vllm/PR-37228.md`](../sources/prs/vllm/PR-37228.md) | [ROCM][Bugfix] Use correct stride in cp_mha_gather_cache_kernel for hybrid model (#37228) |
| `pr-vllm-37252` | upstream-code | [`sources/prs/vllm/PR-37252.md`](../sources/prs/vllm/PR-37252.md) | [Perf] Set Flashinfer sparse MLA as default backend for FP8 kv cache |
| `pr-vllm-37303` | upstream-code | [`sources/prs/vllm/PR-37303.md`](../sources/prs/vllm/PR-37303.md) | [Attention] Support distinguishing between short extends and decodes |
| `pr-vllm-37320` | upstream-code | [`sources/prs/vllm/PR-37320.md`](../sources/prs/vllm/PR-37320.md) | [Kernel] Add non-gated support for NVFP4 CUTLASS MoE |
| `pr-vllm-37332` | upstream-code | [`sources/prs/vllm/PR-37332.md`](../sources/prs/vllm/PR-37332.md) | Add nvfp4 support to reshape_and_cache_flash |
| `pr-vllm-37364` | upstream-code | [`sources/prs/vllm/PR-37364.md`](../sources/prs/vllm/PR-37364.md) | [Model Runner V2] fix draft attention metadata generation |
| `pr-vllm-37373` | upstream-code | [`sources/prs/vllm/PR-37373.md`](../sources/prs/vllm/PR-37373.md) | [torch.compile] Refactor Attention Quant Fusion Pass and Remove Boilerplate |
| `pr-vllm-37421` | upstream-code | [`sources/prs/vllm/PR-37421.md`](../sources/prs/vllm/PR-37421.md) | [Perf][Kernel] Persistent TopK scheduler: unified CUDAGraph-safe kernel with dynamic per-row dispatch - DeepSeek-V3.2 DSA decode |
| `pr-vllm-37463` | upstream-code | [`sources/prs/vllm/PR-37463.md`](../sources/prs/vllm/PR-37463.md) | [Kernel] Add MXFP4 W4A4 CUTLASS MoE kernel for SM100 |
| `pr-vllm-37465` | upstream-code | [`sources/prs/vllm/PR-37465.md`](../sources/prs/vllm/PR-37465.md) | [Bugfix] Remove assertion for NVFP4 scale dynamic range |
| `pr-vllm-37475` | upstream-code | [`sources/prs/vllm/PR-37475.md`](../sources/prs/vllm/PR-37475.md) | [BugFix] Allow qk_nope_head_dim=192 in FlashInfer MLA backend checks |
| `pr-vllm-37502` | upstream-code | [`sources/prs/vllm/PR-37502.md`](../sources/prs/vllm/PR-37502.md) | [Bugfix] Fix marlin nvfp4 rescaling |
| `pr-vllm-37503` | upstream-code | [`sources/prs/vllm/PR-37503.md`](../sources/prs/vllm/PR-37503.md) | [4/n] Migrate FP4/W4A8 CUTLASS kernels to torch stable ABI |
| `pr-vllm-37519` | upstream-code | [`sources/prs/vllm/PR-37519.md`](../sources/prs/vllm/PR-37519.md) | refactor: abstract deepgemm support into platform |
| `pr-vllm-37539` | upstream-code | [`sources/prs/vllm/PR-37539.md`](../sources/prs/vllm/PR-37539.md) | [Performance] Remove unnecessary zero-fill of MLA decode output tensor in Aiter backend |
| `pr-vllm-37547` | upstream-code | [`sources/prs/vllm/PR-37547.md`](../sources/prs/vllm/PR-37547.md) | [Bugfix][ROCm] Fix lru_cache on paged_mqa_logits_module |
| `pr-vllm-37605` | upstream-code | [`sources/prs/vllm/PR-37605.md`](../sources/prs/vllm/PR-37605.md) | [Bugfix] Disable monolithic TRTLLM MoE for Renormalize routing (#37591) |
| `pr-vllm-37606` | upstream-code | [`sources/prs/vllm/PR-37606.md`](../sources/prs/vllm/PR-37606.md) | [ROCm][Bugfix] fix cache block size mismatch for aiter unified attention |
| `pr-vllm-37695` | upstream-code | [`sources/prs/vllm/PR-37695.md`](../sources/prs/vllm/PR-37695.md) | [Perf] Use torch compile to fuse pack topk in trtllm moe |
| `pr-vllm-37718` | upstream-code | [`sources/prs/vllm/PR-37718.md`](../sources/prs/vllm/PR-37718.md) | [Bug] Fix fp8 deepgemm batch invariant |
| `pr-vllm-37759` | upstream-code | [`sources/prs/vllm/PR-37759.md`](../sources/prs/vllm/PR-37759.md) | [MoE] Move FlashInfer CuteDSL experts into fused_moe/experts/ |
| `pr-vllm-37880` | upstream-code | [`sources/prs/vllm/PR-37880.md`](../sources/prs/vllm/PR-37880.md) | [Feature] Support per-draft-model MoE backend via `--speculative-config` |
| `pr-vllm-37887` | upstream-code | [`sources/prs/vllm/PR-37887.md`](../sources/prs/vllm/PR-37887.md) | [ROCm][perf] fix Aiter sparse MLA with MTP>1 |
| `pr-vllm-37940` | upstream-code | [`sources/prs/vllm/PR-37940.md`](../sources/prs/vllm/PR-37940.md) | [NIXL][BUG] Fix Triton heterogeneous TP |
| `pr-vllm-37948` | upstream-code | [`sources/prs/vllm/PR-37948.md`](../sources/prs/vllm/PR-37948.md) | [Perf] triton bilinear_pos_embed kernel for ViT |
| `pr-vllm-37970` | upstream-code | [`sources/prs/vllm/PR-37970.md`](../sources/prs/vllm/PR-37970.md) | [Kernel] Optimize SM120 CUTLASS blockwise FP8 GEMM |
| `pr-vllm-38050` | upstream-code | [`sources/prs/vllm/PR-38050.md`](../sources/prs/vllm/PR-38050.md) | [MoE Kernel] Flashinfer nvfp4 cutedsl moe kernel integration |
| `pr-vllm-38061` | upstream-code | [`sources/prs/vllm/PR-38061.md`](../sources/prs/vllm/PR-38061.md) | [MM][Perf][CG] Support ViT full CUDA graph for Qwen3-VL video inference |
| `pr-vllm-38065` | upstream-code | [`sources/prs/vllm/PR-38065.md`](../sources/prs/vllm/PR-38065.md) | [Perf] FP8 FlashInfer Attn for ViT |
| `pr-vllm-38083` | upstream-code | [`sources/prs/vllm/PR-38083.md`](../sources/prs/vllm/PR-38083.md) | [Bugfix] Fix DeepGemm E8M0 accuracy degradation for Qwen3.5 FP8 on Blackwell |
| `pr-vllm-38136` | upstream-code | [`sources/prs/vllm/PR-38136.md`](../sources/prs/vllm/PR-38136.md) | Fix multi-node allreduce fusion |
| `pr-vllm-38148` | upstream-code | [`sources/prs/vllm/PR-38148.md`](../sources/prs/vllm/PR-38148.md) | Fix NaN from stale FP4 scale padding in create_fp4_scale_tensor |
| `pr-vllm-38251` | upstream-code | [`sources/prs/vllm/PR-38251.md`](../sources/prs/vllm/PR-38251.md) | [Quantization] Add FlashInfer CuteDSL batched experts backend for NVFP4 MoE |
| `pr-vllm-38311` | upstream-code | [`sources/prs/vllm/PR-38311.md`](../sources/prs/vllm/PR-38311.md) | [Model Runner V2] Rebuild attention metadata before eagle decode full… |
| `pr-vllm-38325` | upstream-code | [`sources/prs/vllm/PR-38325.md`](../sources/prs/vllm/PR-38325.md) | [Kernel] Add swapAB support for SM120 CUTLASS blockwise FP8 GEMM  |
| `pr-vllm-38329` | upstream-code | [`sources/prs/vllm/PR-38329.md`](../sources/prs/vllm/PR-38329.md) | [MoE] Add RoutingMethodType.Simulated to TRT-LLM FP8/NVFP4 kernel allowlists |
| `pr-vllm-38361` | upstream-code | [`sources/prs/vllm/PR-38361.md`](../sources/prs/vllm/PR-38361.md) | [GDN] Eliminate GPU->CPU sync in prepare_chunk_indices during prefill |
| `pr-vllm-38423` | upstream-code | [`sources/prs/vllm/PR-38423.md`](../sources/prs/vllm/PR-38423.md) | [NVIDIA] Bugfix NVFP4 DGX Spark and RTX50 |
| `pr-vllm-38442` | upstream-code | [`sources/prs/vllm/PR-38442.md`](../sources/prs/vllm/PR-38442.md) | [QeRL] Fix online quantized reloading |
| `pr-vllm-38460` | upstream-code | [`sources/prs/vllm/PR-38460.md`](../sources/prs/vllm/PR-38460.md) | [Perf] Batch KV cache swap copies via cuMemcpyBatchAsync |
| `pr-vllm-38479` | upstream-code | [`sources/prs/vllm/PR-38479.md`](../sources/prs/vllm/PR-38479.md) | [Attention Backend] TurboQuant: 2-bit KV cache compression with 4x capacity |
| `pr-vllm-38504` | upstream-code | [`sources/prs/vllm/PR-38504.md`](../sources/prs/vllm/PR-38504.md) | [Kernels][MoE] Fix legacy_routing to use bitmatrix-based routing path |
| `pr-vllm-38573` | upstream-code | [`sources/prs/vllm/PR-38573.md`](../sources/prs/vllm/PR-38573.md) | [Compile] Fix nvfp4 compile warning |
| `pr-vllm-38615` | upstream-code | [`sources/prs/vllm/PR-38615.md`](../sources/prs/vllm/PR-38615.md) | [ROCm] Fix aiter persistent mode mla with q/o nhead<16 for kimi-k2.5 tp8 |
| `pr-vllm-38631` | upstream-code | [`sources/prs/vllm/PR-38631.md`](../sources/prs/vllm/PR-38631.md) | Fix MLA runs when use_inductor_graph_partition=True |
| `pr-vllm-38635` | upstream-code | [`sources/prs/vllm/PR-38635.md`](../sources/prs/vllm/PR-38635.md) | [Feature] NUMA binding support for GPU workers |
| `pr-vllm-38670` | upstream-code | [`sources/prs/vllm/PR-38670.md`](../sources/prs/vllm/PR-38670.md) | [Bugfix] Fix AWQ models batch invariance issues |
| `pr-vllm-38682` | upstream-code | [`sources/prs/vllm/PR-38682.md`](../sources/prs/vllm/PR-38682.md) | [XPU] add  xpu backend implementation of mxfp8 quant |
| `pr-vllm-38730` | upstream-code | [`sources/prs/vllm/PR-38730.md`](../sources/prs/vllm/PR-38730.md) | [Bugfix] Restrict TRTLLM attention to SM100, fixing GB300 (SM103) hang |
| `pr-vllm-38794` | upstream-code | [`sources/prs/vllm/PR-38794.md`](../sources/prs/vllm/PR-38794.md) | [Perf] Reduce H2D pageable memory copies |
| `pr-vllm-38814` | upstream-code | [`sources/prs/vllm/PR-38814.md`](../sources/prs/vllm/PR-38814.md) | [FlashAttention] Symlink FA4 instead of copying when using `VLLM_FLASH_ATTN_SRC_DIR` |
| `pr-vllm-38815` | upstream-code | [`sources/prs/vllm/PR-38815.md`](../sources/prs/vllm/PR-38815.md) | [Quant] add CompressedTensorsW8A8Mxfp8 for linear and MoE layers |
| `pr-vllm-38835` | upstream-code | [`sources/prs/vllm/PR-38835.md`](../sources/prs/vllm/PR-38835.md) | [Attention] relax the head dim 512 and paged kv for sm90+FA4 |
| `pr-vllm-38859` | upstream-code | [`sources/prs/vllm/PR-38859.md`](../sources/prs/vllm/PR-38859.md) | [Bugfix] Re-enable Renormalize routing for TRT-LLM MoE experts |
| `pr-vllm-38865` | upstream-code | [`sources/prs/vllm/PR-38865.md`](../sources/prs/vllm/PR-38865.md) | [Refactor] Improve indexer decode path metadata preparation |
| `pr-vllm-38879` | upstream-code | [`sources/prs/vllm/PR-38879.md`](../sources/prs/vllm/PR-38879.md) | [Gemma4] Enable Fast Prefill Optimization |
| `pr-vllm-38922` | upstream-code | [`sources/prs/vllm/PR-38922.md`](../sources/prs/vllm/PR-38922.md) | [Bugfix] Fix broken explicit unquantized kv cache dtype support |
| `pr-vllm-38960` | upstream-code | [`sources/prs/vllm/PR-38960.md`](../sources/prs/vllm/PR-38960.md) | [MoE Refactor] Split up compressed_tensors_moe.py |
| `pr-vllm-38989` | upstream-code | [`sources/prs/vllm/PR-38989.md`](../sources/prs/vllm/PR-38989.md) | [Bug] Fix routing bias dtype for trtllm per-block fp8 moe |
| `pr-vllm-38990` | upstream-code | [`sources/prs/vllm/PR-38990.md`](../sources/prs/vllm/PR-38990.md) | [Bugfix][MoE] Fix 6-8% decode regression: prefer multi-stream shared expert overlap |
| `pr-vllm-38993` | upstream-code | [`sources/prs/vllm/PR-38993.md`](../sources/prs/vllm/PR-38993.md) | [Perf] Change Trtllm fp8 MoE to use Shuffled Weights and BlockMajorK Layout |
| `pr-vllm-39002` | upstream-code | [`sources/prs/vllm/PR-39002.md`](../sources/prs/vllm/PR-39002.md) | [Bugfix] Fix FlashInfer crash with kv_cache_dtype_skip_layers |
| `pr-vllm-39007` | upstream-code | [`sources/prs/vllm/PR-39007.md`](../sources/prs/vllm/PR-39007.md) | [MoE] Move GPT OSS Triton kernel experts into fused_moe/experts/ |
| `pr-vllm-39045` | upstream-code | [`sources/prs/vllm/PR-39045.md`](../sources/prs/vllm/PR-39045.md) | [Gemma4] Support quantized MoE  |
| `pr-vllm-39054` | upstream-code | [`sources/prs/vllm/PR-39054.md`](../sources/prs/vllm/PR-39054.md) | [Bug] Fix Trtllm Fp8 MoE Weight Shuffle Memory Fragamentation |
| `pr-vllm-39088` | upstream-code | [`sources/prs/vllm/PR-39088.md`](../sources/prs/vllm/PR-39088.md) | [XPU] Quick fix for TritonMLA to remove cuda hardcode |
| `pr-vllm-39119` | upstream-code | [`sources/prs/vllm/PR-39119.md`](../sources/prs/vllm/PR-39119.md) | [ROCm] Align AiterFlashAttentionImpl attn_type check with backend |
| `pr-vllm-39129` | upstream-code | [`sources/prs/vllm/PR-39129.md`](../sources/prs/vllm/PR-39129.md) | [Refactor] Move NVFP4 GEMM management into NvFp4LinearKernel |
| `pr-vllm-39205` | upstream-code | [`sources/prs/vllm/PR-39205.md`](../sources/prs/vllm/PR-39205.md) | [Refactor] Move MXFP8 GEMM management into MxFp8LinearKernel |
| `pr-vllm-39217` | upstream-code | [`sources/prs/vllm/PR-39217.md`](../sources/prs/vllm/PR-39217.md) | [Mistral Grammar] Fix tool and reasoning parsing |
| `pr-vllm-39225` | upstream-code | [`sources/prs/vllm/PR-39225.md`](../sources/prs/vllm/PR-39225.md) | [Bug] Fix rocm sparse attn indexer issue |
| `pr-vllm-39306` | upstream-code | [`sources/prs/vllm/PR-39306.md`](../sources/prs/vllm/PR-39306.md) | Use CU_MEMCPY_SRC_ACCESS_ORDER_ANY for batch KV cache swaps |
| `pr-vllm-39315` | upstream-code | [`sources/prs/vllm/PR-39315.md`](../sources/prs/vllm/PR-39315.md) | [Bugfix] FlashInfer MXINT4 MoE crashes, missing do_finalize |
| `pr-vllm-39322` | upstream-code | [`sources/prs/vllm/PR-39322.md`](../sources/prs/vllm/PR-39322.md) | [Feature] Batch invariant nvfp4 linear support |
| `pr-vllm-39353` | upstream-code | [`sources/prs/vllm/PR-39353.md`](../sources/prs/vllm/PR-39353.md) | [Model Runner V2] Fix flex attention kv blocks calculation issue |
| `pr-vllm-39361` | upstream-code | [`sources/prs/vllm/PR-39361.md`](../sources/prs/vllm/PR-39361.md) | Fix NUMA binding on non-CDMM Grace-Blackwell systems |
| `pr-vllm-39391` | upstream-code | [`sources/prs/vllm/PR-39391.md`](../sources/prs/vllm/PR-39391.md) | fix: clamp NaN/Inf in topk_softmax to prevent duplicate expert IDs |
| `pr-vllm-39418` | upstream-code | [`sources/prs/vllm/PR-39418.md`](../sources/prs/vllm/PR-39418.md) | [Bugfix][CT] Fix KV cache scale handling |
| `pr-vllm-39458` | upstream-code | [`sources/prs/vllm/PR-39458.md`](../sources/prs/vllm/PR-39458.md) | [MLA] Optimize mla indexer prepare uniform decode for MTP > 1 |
| `pr-vllm-39510` | upstream-code | [`sources/prs/vllm/PR-39510.md`](../sources/prs/vllm/PR-39510.md) | [Kernel] Support TRTLLM GEN NVFP4 MoE for non-512-aligned hidden dims via weight padding |
| `pr-vllm-39547` | upstream-code | [`sources/prs/vllm/PR-39547.md`](../sources/prs/vllm/PR-39547.md) | [Perf] Fuse Zero Initializer for FP8 DeepGemm Block Quant Kernel |
| `pr-vllm-39676` | upstream-code | [`sources/prs/vllm/PR-39676.md`](../sources/prs/vllm/PR-39676.md) | [XPU] properly handle q_descale on XPU as quant query input not supported |
| `pr-vllm-39717` | upstream-code | [`sources/prs/vllm/PR-39717.md`](../sources/prs/vllm/PR-39717.md) | [Bugfix] Reject non-nvfp4 dtypes when using the flashinfer_nvlink_one_sided all2all backend |
| `pr-vllm-39752` | upstream-code | [`sources/prs/vllm/PR-39752.md`](../sources/prs/vllm/PR-39752.md) | add warning when FP8 KV cache misses prefill query quantization |
| `pr-vllm-39773` | upstream-code | [`sources/prs/vllm/PR-39773.md`](../sources/prs/vllm/PR-39773.md) | [Model Runner V2] Disable piecewise cudagraph mode fallback for eagle draft decodes |
| `pr-vllm-39820` | upstream-code | [`sources/prs/vllm/PR-39820.md`](../sources/prs/vllm/PR-39820.md) | [Bug] Fix batch invariance nvfp4 support |
| `pr-vllm-39825` | upstream-code | [`sources/prs/vllm/PR-39825.md`](../sources/prs/vllm/PR-39825.md) | [Bugfix] Disable FlashInfer CUTLASS MoE on SM121 (DGX Spark) |
| `pr-vllm-39917` | upstream-code | [`sources/prs/vllm/PR-39917.md`](../sources/prs/vllm/PR-39917.md) | [Core] Replace routing replay with device cache and async D2H pipeline |
| `pr-vllm-40045` | upstream-code | [`sources/prs/vllm/PR-40045.md`](../sources/prs/vllm/PR-40045.md) | [Attention] use diff kv backend for mimo v2 flash |
| `pr-vllm-40105` | upstream-code | [`sources/prs/vllm/PR-40105.md`](../sources/prs/vllm/PR-40105.md) | [Bugfix] Add Marlin kernel in block scaled mm kernel selection. |
| `pr-vllm-40177` | upstream-code | [`sources/prs/vllm/PR-40177.md`](../sources/prs/vllm/PR-40177.md) | Add nvfp4 kv cache support |
| `pr-vllm-40191` | upstream-code | [`sources/prs/vllm/PR-40191.md`](../sources/prs/vllm/PR-40191.md) | [Bugfix] Guard mxfp4_experts_quant bindings on ENABLE_NVFP4_SM100 |
| `pr-vllm-40273` | upstream-code | [`sources/prs/vllm/PR-40273.md`](../sources/prs/vllm/PR-40273.md) | Fix MoE backend selection for LoRA (unquantized MoE) |
| `pr-vllm-40392` | upstream-code | [`sources/prs/vllm/PR-40392.md`](../sources/prs/vllm/PR-40392.md) | [Performance][DSR1]: Fused RoPE+KVCache+q_concat for MLA |
| `pr-vllm-40408` | upstream-code | [`sources/prs/vllm/PR-40408.md`](../sources/prs/vllm/PR-40408.md) | [Perf] Batch invariance with Cutlass fp8 support, 28.9% E2E latency improvement |
| `pr-vllm-40574` | upstream-code | [`sources/prs/vllm/PR-40574.md`](../sources/prs/vllm/PR-40574.md) | [MoE] Move cutlass moe to fused_moe/experts/ |
| `pr-vllm-40850` | upstream-code | [`sources/prs/vllm/PR-40850.md`](../sources/prs/vllm/PR-40850.md) | [Kernel][Helion] Optimize Helion config parsing latency |
| `pr-vllm-40941` | upstream-code | [`sources/prs/vllm/PR-40941.md`](../sources/prs/vllm/PR-40941.md) | [Attention][TurboQuant] Share dequant buffers, eliminate float16_copy |
| `pr-vllm-40950` | upstream-code | [`sources/prs/vllm/PR-40950.md`](../sources/prs/vllm/PR-40950.md) | [DSV4] Add silu clamp limit to shared expert |
| `pr-vllm-40960` | upstream-code | [`sources/prs/vllm/PR-40960.md`](../sources/prs/vllm/PR-40960.md) | [DSV4] Add BF16 and MXFP8 A2A support for flashinfer a2a one sided |
| `pr-vllm-41050` | upstream-code | [`sources/prs/vllm/PR-41050.md`](../sources/prs/vllm/PR-41050.md) | [Kernel][MoE] Support GELU on TRT-LLM NvFP4 fused MoE for Gemma4 |
| `pr-vllm-41189` | upstream-code | [`sources/prs/vllm/PR-41189.md`](../sources/prs/vllm/PR-41189.md) | [Bugfix] Fix persistent_topk cooperative deadlock at TopK=1024 |
| `pr-vllm-41263` | upstream-code | [`sources/prs/vllm/PR-41263.md`](../sources/prs/vllm/PR-41263.md) | [DSV4]   Fuse norm and router for low latency scenario |
| `pr-vllm-41326` | upstream-code | [`sources/prs/vllm/PR-41326.md`](../sources/prs/vllm/PR-41326.md) | Faster per-token fp8 group quant packed kernel for blackwell |
| `pr-vllm-41428` | upstream-code | [`sources/prs/vllm/PR-41428.md`](../sources/prs/vllm/PR-41428.md) | [DSv4] Improved fused Indexer Q quant kernel |
| `pr-vllm-41566` | upstream-code | [`sources/prs/vllm/PR-41566.md`](../sources/prs/vllm/PR-41566.md) | [Quantization] Rework quantization_config to use QuantKey and allow for activation override |
| `pr-vllm-41664` | upstream-code | [`sources/prs/vllm/PR-41664.md`](../sources/prs/vllm/PR-41664.md) | [MXFP4] Support for linear layers + compressed-tensors integration |
| `pr-vllm-41665` | upstream-code | [`sources/prs/vllm/PR-41665.md`](../sources/prs/vllm/PR-41665.md) | [Bugfix] Fix condition to clear persistent topk so that it can be captured regardless |
| `pr-vllm-41745` | upstream-code | [`sources/prs/vllm/PR-41745.md`](../sources/prs/vllm/PR-41745.md) | [Spec Decode] Add Gemma4 MTP speculative decoding support |
| `pr-vllm-41778` | upstream-code | [`sources/prs/vllm/PR-41778.md`](../sources/prs/vllm/PR-41778.md) | [MLA Attention Backend] Add TOKENSPEED_MLA backend for DSR1/Kimi K25 prefill + decode on Blackwell |
| `pr-vllm-41868` | upstream-code | [`sources/prs/vllm/PR-41868.md`](../sources/prs/vllm/PR-41868.md) | [CUDA][CUTLASS] Enable cutlass scaled mm for non-compatible sizes  |
| `pr-vllm-41882` | upstream-code | [`sources/prs/vllm/PR-41882.md`](../sources/prs/vllm/PR-41882.md) | Add NVFP4 all-gather GEMM fusion for AsyncTP |
| `pr-vllm-41979` | upstream-code | [`sources/prs/vllm/PR-41979.md`](../sources/prs/vllm/PR-41979.md) | [MoE] Move various experts classes to fused_moe/experts/ |
| `pr-vllm-41986` | upstream-code | [`sources/prs/vllm/PR-41986.md`](../sources/prs/vllm/PR-41986.md) | [Bugfix] Add swiglu limits to deepgemm fp8 methods |
| `pr-vllm-42112` | upstream-code | [`sources/prs/vllm/PR-42112.md`](../sources/prs/vllm/PR-42112.md) | [Bugfix] Fix TRTLLM ragged MLA prefill workspace warmup |
| `pr-vllm-42153` | upstream-code | [`sources/prs/vllm/PR-42153.md`](../sources/prs/vllm/PR-42153.md) | [Perf] Use 2D-grid to eliminate divmod in W8W8 group quant |
| `pr-vllm-42236` | upstream-code | [`sources/prs/vllm/PR-42236.md`](../sources/prs/vllm/PR-42236.md) | [DSv4] Improved dequant gather K cache kernel |
| `pr-vllm-7174` | upstream-code | [`sources/prs/vllm/PR-7174.md`](../sources/prs/vllm/PR-7174.md) | [Kernel] (1/N) Machete - Hopper Optimized Mixed Precision Linear Kernel  |
| `pr-vllm-7701` | upstream-code | [`sources/prs/vllm/PR-7701.md`](../sources/prs/vllm/PR-7701.md) | [Kernel] (2/N) Machete - Integrate into CompressedTensorsWNA16 and GPTQMarlin |
| `pr-vllm-9218` | upstream-code | [`sources/prs/vllm/PR-9218.md`](../sources/prs/vllm/PR-9218.md) | [Bugfix] Fix Machete unittests failing with `NotImplementedError` |
