# Blackwell Kernel Wiki — Phase 2 Massive Expansion Plan

## Goal Description

Expand the Blackwell kernel optimization knowledge base from 91 files to 540+ by collecting at least 50% of all Blackwell/SM100-related merged PRs from 5 major repositories (Jan 2025 - Apr 2026), contest submission data, and additional community resources. Use a 2-stage pipeline: first build reviewed candidate ledgers, then generate markdown source pages. Extend wiki synthesis to cover newly discovered concepts.

## Acceptance Criteria

- AC-1: Candidate ledger files exist for all 5 repositories
  - Positive Tests:
    - `candidates/cutlass.yaml`, `candidates/sglang.yaml`, `candidates/vllm.yaml`, `candidates/flashinfer.yaml`, `candidates/pytorch.yaml` exist
    - Each ledger contains PR number, title, files_changed, decision (include/exclude/defer), and reason
    - Total candidates across all ledgers ≥ 400 unique PRs
  - Negative Tests:
    - A ledger with only PR numbers and no decision field is incomplete
    - A ledger with zero `defer` entries is suspicious (should have ambiguous cases)

- AC-2: Source PR pages reach target counts per repository
  - AC-2.1: `sources/prs/cutlass/` contains ≥ 20 PR pages
  - AC-2.2: `sources/prs/sglang/` contains ≥ 80 PR pages
  - AC-2.3: `sources/prs/vllm/` contains ≥ 100 PR pages
  - AC-2.4: `sources/prs/flashinfer/` contains ≥ 100 PR pages
  - AC-2.5: `sources/prs/pytorch/` contains ≥ 50 PR pages
  - Positive Tests:
    - Each directory meets minimum count
    - All pages pass `python3 scripts/validate.py`
    - Every page has `inclusion_reason` in frontmatter
  - Negative Tests:
    - A page missing `inclusion_reason` is rejected
    - A page for a non-merged PR is rejected (status must be "merged")

- AC-3: All new source pages have valid frontmatter and consistent metadata
  - Positive Tests:
    - `python3 scripts/validate.py` reports 0 errors on the full corpus
    - Every PR page's `kernel_types` includes all kernel-type tags from its `tags` field
    - Every PR page's `hardware_features` includes all hw tags from its `tags` field
  - Negative Tests:
    - A page with `tags: [tcgen05]` but `hardware_features: []` fails validation
    - A page with duplicate values in any list field fails validation

- AC-4: Contest data expanded with submission details
  - Positive Tests:
    - GPU Mode pages include top-3 solutions per problem with rank, score, technique analysis
    - FlashInfer contest pages include analysis of notable fork submissions
    - Each contest page has a `submissions` list in frontmatter
  - Negative Tests:
    - A contest page claiming "top solutions" without specific technique descriptions is incomplete

- AC-5: Additional blogs and docs collected
  - Positive Tests:
    - `sources/blogs/` contains ≥ 20 pages (up from 10)
    - `sources/docs/` contains ≥ 10 pages (up from 6)
    - Each new page has valid frontmatter and language tags where applicable
  - Negative Tests:
    - A blog page without `retrieved_at` date is rejected

- AC-6: Wiki layer expanded to cover new concepts
  - Positive Tests:
    - At least 10 new wiki pages created where 3+ new sources support an uncovered concept
    - New wiki technique/kernel pages include code snippets (reproducibility ≥ snippet)
    - All new wiki pages pass validation including `blackwell_relevance` for Hopper-inclusive pages
  - Negative Tests:
    - A new wiki page with fewer than 3 supporting sources is premature

- AC-7: Query indices regenerated and complete
  - Positive Tests:
    - `python3 scripts/generate-indices.py` runs successfully on the expanded corpus
    - `queries/by-repo.md` shows all 5 repos with updated PR counts
    - Link integrity check reports 0 broken links
  - Negative Tests:
    - A query page linking to a non-existent source file is broken

- AC-8: Schema extended for new metadata fields
  - Positive Tests:
    - `data/schemas.yaml` includes `inclusion_reason` and `changed_paths` as optional fields for `source-pr`
    - `data/schemas.yaml` includes `submissions` as optional field for `source-contest`
    - `candidates/` directory is committed with ledger files
  - Negative Tests:
    - Using `inclusion_reason` in frontmatter without the schema update causes validation to ignore it

## Path Boundaries

### Upper Bound (Maximum Acceptable Scope)
Complete ingestion of every Blackwell-related merged PR from all 5 repos (potentially 500+ PRs), full contest leaderboard data with detailed solution analysis, 25+ additional blogs/docs, 25+ new wiki pages with comprehensive code examples, and updated validation/generation tooling.

### Lower Bound (Minimum Acceptable Scope)
At least 350 new PR source pages (20 CUTLASS + 80 SGLang + 100 vLLM + 100 FlashInfer + 50 PyTorch), contest pages with top-3 solutions, 10 new blogs/docs, 10 new wiki pages, and regenerated query indices.

### Allowed Choices
- Can use: GitHub REST API (authenticated), `curl`, Python scripts, parallel sub-agents
- Can use: Candidate YAML ledgers as intermediate artifacts
- Fixed: Only merged PRs collected (per user decision)
- Fixed: Include dispatch/selector PRs that enable Blackwell kernels (per user decision)
- Fixed: Candidate ledgers committed to repo (per user decision)
- Fixed: Contest top-3 + highlights (per user decision)
- Cannot use: Unauthenticated API (rate limits too restrictive)

## Feasibility Hints and Suggestions

### Conceptual Approach

```
Milestone 1: Schema Extension + Candidate Collection
  1a. Extend data/schemas.yaml with inclusion_reason, changed_paths, submissions
  1b. For each repo, search GitHub API with multiple keywords by time period
  1c. Deduplicate by PR number, classify include/exclude/defer
  1d. Write candidates/{repo}.yaml

Milestone 2: Source Page Generation (parallel per repo)
  For each repo:
    For each included candidate:
      Fetch PR details → create sources/prs/{repo}/PR-{N}.md
      Ensure all frontmatter fields populated and consistent

Milestone 3: Contest + Blog/Doc Expansion
  3a. Fetch GPU Mode leaderboards, analyze top-3 solutions
  3b. Fetch FlashInfer contest forks, analyze notable submissions
  3c. Collect additional blogs and docs

Milestone 4: Wiki Synthesis
  Scan new sources for uncovered concepts
  Create new wiki pages where 3+ sources support a concept
  Update existing wiki pages with better examples from new sources

Milestone 5: Index Regeneration + Validation
  Run validate.py, fix errors
  Run generate-indices.py
  Run link integrity check
```

### Relevant References
- `scripts/validate.py` — Existing validator (441 lines)
- `scripts/generate-indices.py` — Existing index generator (346 lines)
- `data/schemas.yaml` — Page-type schemas to extend
- `data/tags.yaml` — Controlled vocabulary
- `.humanize/bitlesson.md` — Lessons from Phase 1 (tag validation, merge-vs-fallback)

## Dependencies and Sequence

### Milestones

1. **Schema Extension**: Update schemas and create candidates/ directory
   - Must complete before any candidate collection

2. **Candidate Collection**: Parallel across 5 repos
   - Each repo independently searchable
   - Produces candidates/{repo}.yaml
   - Depends on: Milestone 1

3. **Source Page Generation**: Parallel across 5 repos
   - Each repo's pages generated from its candidate ledger
   - Depends on: Milestone 2 (that repo's ledger)

4. **Contest + Blog/Doc Expansion**: Independent of PR collection
   - Can run in parallel with Milestones 2-3
   - Contest analysis may reference some PR pages

5. **Wiki Synthesis**: Requires source data
   - Depends on: Milestones 3-4 complete
   - Scans all new sources to find uncovered concepts

6. **Index Regeneration + Validation**: Final step
   - Depends on: All previous milestones
   - Regenerates all query pages, validates entire corpus

## Task Breakdown

| Task ID | Description | Target AC | Tag | Depends On |
|---------|-------------|-----------|-----|------------|
| task1 | Extend data/schemas.yaml with inclusion_reason, changed_paths, submissions | AC-8 | coding | - |
| task2 | Create candidates/ directory structure | AC-1 | coding | task1 |
| task3 | Collect CUTLASS candidate ledger (all keywords, 2025-01 to 2026-04) | AC-1, AC-2.1 | coding | task2 |
| task4 | Collect SGLang candidate ledger (split by time periods) | AC-1, AC-2.2 | coding | task2 |
| task5 | Collect vLLM candidate ledger (split by time periods) | AC-1, AC-2.3 | coding | task2 |
| task6 | Collect FlashInfer candidate ledger (split by time periods) | AC-1, AC-2.4 | coding | task2 |
| task7 | Collect PyTorch candidate ledger (split by time periods) | AC-1, AC-2.5 | coding | task2 |
| task8 | Generate CUTLASS PR source pages from ledger | AC-2.1, AC-3 | coding | task3 |
| task9 | Generate SGLang PR source pages from ledger | AC-2.2, AC-3 | coding | task4 |
| task10 | Generate vLLM PR source pages from ledger | AC-2.3, AC-3 | coding | task5 |
| task11 | Generate FlashInfer PR source pages from ledger | AC-2.4, AC-3 | coding | task6 |
| task12 | Generate PyTorch PR source pages from ledger | AC-2.5, AC-3 | coding | task7 |
| task13 | Expand GPU Mode contest pages (top-3 solutions + highlights) | AC-4 | coding | task2 |
| task14 | Expand FlashInfer contest pages (fork analysis + submissions) | AC-4 | coding | task2 |
| task15 | Collect additional blogs (10+ new) | AC-5 | coding | - |
| task16 | Collect additional docs (4+ new) | AC-5 | coding | - |
| task17 | Wiki synthesis: create new pages for uncovered concepts | AC-6 | coding | task8-task16 |
| task18 | Regenerate all query indices | AC-7 | coding | task17 |
| task19 | Run validate.py + link integrity check, fix all errors | AC-3, AC-7 | coding | task18 |
| task20 | Audit: verify coverage targets met per repo | AC-2 | analyze | task19 |
| task21 | Audit: verify contest data completeness | AC-4 | analyze | task19 |
| task22 | Audit: verify wiki expansion quality | AC-6 | analyze | task19 |

Tasks 3-7 can run in parallel. Tasks 8-12 can run in parallel (each depends on its own ledger). Tasks 13-16 can run in parallel with 3-12.

## Claude-Codex Deliberation

### Agreements
- 2-stage pipeline (candidate ledger → page generation) is the right architecture
- Candidate ledgers should be committed for auditability
- Only merged PRs in scope
- Dispatch/selector PRs included when they enable Blackwell kernels
- Wiki expansion should be a separate stage with explicit entry criteria (3+ sources)
- validate.py and generate-indices.py remain the quality gates
- Deferred PRs should be tracked, not silently excluded

### Resolved Disagreements
- **Include/exclude strictness**: Claude proposed `≥1 hard + ≥1 semantic`. Codex argued this is too strict — misses generic-title bugfixes. Resolution: strong file evidence alone can `include`; semantic-only → `defer`. Dispatch/selector PRs explicitly included per user decision.
- **Agent count**: Draft proposed 22 parallel agents. Codex suggested 7 (5 repo + 1 contest + 1 blog). Resolution: use 7 primary workers, each handling full time range internally with sequential API calls.
- **Coverage metric**: Claude proposed "≥50% of API matches." Codex argued raw matches are noisy. Resolution: measure against deduped reviewed candidates (included + deferred), not raw API count. Target remains high per user requirement.

### Convergence Status
- Final Status: `converged`
- Rounds: 1

## Pending User Decisions

- DEC-1: PR scope (dispatch PRs)
  - Decision Status: `Include if enables Blackwell` (user confirmed)

- DEC-2: Candidate ledger persistence
  - Decision Status: `Commit as audit trail` (user confirmed)

- DEC-3: Contest depth
  - Decision Status: `Top-3 only + highlights` (user confirmed)

- DEC-4: PR status filter
  - Decision Status: `Merged only` (user confirmed)

## Implementation Notes

### Code Style Requirements
- Implementation code and comments must NOT contain plan-specific terminology such as "AC-", "Milestone", "Step", "Phase", or similar workflow markers
- These terms are for plan documentation only, not for the resulting codebase
- Use descriptive, domain-appropriate naming in code instead

### Inclusion Rules (Deterministic)

**Include** a merged PR if ANY of these apply:
1. Touches kernel files (`.cu`, `.cuh`, `.ptx`, Triton `.py`, CuTe DSL `.py`) AND title/body references SM100/Blackwell/tcgen05/TMEM/NVFP4
2. Modifies scheduler/pipeline/epilogue/dispatch code for SM100 path
3. Adds or changes kernel backend selection that routes to Blackwell kernels
4. Contains Blackwell-specific performance benchmarks with kernel changes
5. Fixes correctness/precision bug in a Blackwell kernel path

**Exclude** a merged PR if ALL of these apply:
- Title matches: `[CI]`, `[Doc]`, `[Docs]`, `bump`, `typo`, `format`, `lint`, `nit`, `revert`, `readme`, `changelog`
- No kernel-bearing or dispatch file changes
- No SM100/Blackwell-specific behavior change

**Defer** when the agent cannot confidently classify. Record `defer_reason`.

### Search Keywords Per Repo

```
Common: blackwell, sm100, sm_100, sm_100a, tcgen05, tmem, nvfp4, fp8, B200
CUTLASS: 2sm, cta_group, clc, cluster_launch, umma, persistent, warp_special, fmha, mla, epilogue, tile_scheduler, grouped_gemm, sub_byte, block_scale
SGLang: cutlass, deepgemm, flashmla, mla, flashinfer, triton, attention, moe, sparse, gated_delta, sgl-kernel, trtllm, decode, prefill, quantiz
vLLM: cutlass, mla, deepseek, flashmla, attention, moe, fused_moe, sparse_attention, gated_delta, quantiz, block_scale, triton, flashinfer, grouped_gemm, decode, prefill
FlashInfer: tcgen05, tmem, cutlass, cute_dsl, fmha, mla, attention, moe, fp4, block_scale, trtllm, decode, prefill, sparse, gated_delta, splitk, allreduce, head_dim, gemm, gemv
PyTorch: sm_100a, cuda_13, nvfp4, inductor, triton, cutlass, flash_attention, vec128, launch_bounds, sm120, compute_10
```

### Rate Limiting
- Single coordinator queues API requests
- Max 30 requests/minute globally (well under 5000/hour authenticated limit)
- Exponential backoff on 403/429 responses
- Each sub-agent processes its repo sequentially, not in parallel bursts

--- Original Design Draft Start ---

# Blackwell Kernel Wiki — 大规模扩展计划 (Phase 2)

## 现状

Phase 1 建立了知识库骨架（91 files），但PR覆盖严重不足：
- CUTLASS: 7/~41+ Blackwell PRs
- SGLang: 5/~194+ sm100 PRs (466 提到blackwell)
- vLLM: 6/~254+ sm100 PRs (574 提到blackwell, 555 nvfp4)
- FlashInfer: 6/~300+ sm100 PRs (247 提到blackwell)
- PyTorch: 7/~141+ sm100 PRs (159 提到blackwell)
- 比赛: 仅7个概述页，无具体提交方案

注意：上述数字包含大量仅mention关键词的PR（如CI/doc/依赖更新），实际kernel相关PR需要过滤。

## 目标

从2025-01-01至今，完整覆盖每个仓库中**与Blackwell/Hopper kernel编程直接相关**的PR。同时收录比赛的具体提交方案和排名。

## 过滤标准

PR必须满足以下至少一条才收录：
1. **新增/修改kernel代码**（CUDA C++, CuTe DSL, Triton, PTX, TileLang）
2. **kernel性能优化**（tile size tuning, schedule改进, 新的pipeline策略）
3. **新增硬件特性支持**（tcgen05, TMEM, CLC, 2-SM, NVFP4, FP8 block scale）
4. **kernel算法创新**（新的attention variant, MoE routing, sparse pattern）
5. **重要bug fix影响kernel正确性**（sync issues, precision bugs, launch bounds）

不收录的PR类型：
- 纯CI/CD改动
- 文档/README更新（除非包含kernel技术细节）
- 依赖版本bump
- 代码格式化/lint
- 纯Python binding（无kernel逻辑改动）

## 搜索策略

### NVIDIA/cutlass（预计收录 30-50 PRs）

GitHub API显示 ~41 PRs提到"blackwell"。CUTLASS是Blackwell kernel的核心实现。

**搜索关键词**（每个单独搜索，去重合并）：
```
blackwell, sm100, sm_100, sm_100a, tcgen05, tmem, tensor_memory,
nvfp4, fp4, mxfp4, block_scale, 2sm, cta_group, clc,
cluster_launch, umma, persistent, warp_special, fmha, mla,
epilogue, tile_scheduler, grouped_gemm, sub_byte
```

**按时间段分批搜索**（避免API限制）：
- 2025-01 ~ 2025-03（早期Blackwell支持）
- 2025-04 ~ 2025-06（CUTLASS 4.0发布期）
- 2025-07 ~ 2025-09（SM100 attention kernel）
- 2025-10 ~ 2025-12（sub-byte GEMM, NVFP4）
- 2026-01 ~ 2026-04（CuTe-DSL, bugfix）

**重点关注**：
- examples/cute/tutorial/blackwell/ 相关PR
- SM100 FMHA forward/backward
- Grouped GEMM / MoE support
- CuTe-DSL SM100 atoms
- Block-scale GEMM (NVFP4, MXFP4)
- PersistentTileSchedulerSm100
- 2-CTA cooperative MMA

### sgl-project/sglang（预计收录 20-30 PRs）

SGLang有大量Blackwell集成工作。~194 PRs提到sm100。

**搜索关键词**：
```
blackwell, sm100, cutlass, deepgemm, flashmla, fp8, nvfp4,
mla, flashinfer, triton, attention, moe, sparse, gated_delta,
sgl-kernel, trtllm, decode, prefill, quantiz
```

**重点关注**：
- DeepGEMM集成（FP8 GEMM, grouped GEMM）
- FlashMLA集成（dense/sparse MLA decode）
- CUTLASS MLA backend
- FP8 blockwise quantization
- NSA (Native Sparse Attention) 支持
- GatedDeltaNet 支持
- Blackwell-specific kernel选择逻辑

### vllm-project/vllm（预计收录 25-40 PRs）

vLLM有最多的Blackwell适配PR。~254 PRs提到sm100。

**搜索关键词**：
```
blackwell, sm100, cutlass, fp8, nvfp4, mxfp4, B200,
mla, deepseek, flashmla, attention, moe, fused_moe,
sparse_attention, gated_delta, quantiz, block_scale,
triton, flashinfer, grouped_gemm, decode, prefill
```

**重点关注**：
- CUTLASS FP8 GEMM on SM100
- NVFP4/MXFP4 GEMM和fused MoE
- CUTLASS MLA for Blackwell
- DeepSeek V3.2 sparse attention支持
- GatedDeltaNet/Qwen3-Next支持
- FP8 block-scale quantization kernels
- Attention backend selection for SM100

### flashinfer-ai/flashinfer（预计收录 25-35 PRs）

FlashInfer是Blackwell attention kernel的核心库。~300 PRs提到sm100。

**搜索关键词**：
```
blackwell, sm100, sm_100, tcgen05, tmem, cutlass, cute_dsl,
fmha, mla, attention, moe, fp8, fp4, nvfp4, block_scale,
trtllm, decode, prefill, sparse, gated_delta, splitk,
allreduce, head_dim, gemm, gemv
```

**重点关注**：
- CuTe-DSL FMHA kernels for SM100
- SM100 MLA kernels (forward/backward)
- FP4/FP8 fused MoE on Blackwell
- FlashInfer-Bench kernel definitions
- TGV GEMM和alternative backends
- head_dim variants for SM100
- GEMM+allreduce fusion

### pytorch/pytorch（预计收录 15-25 PRs）

PyTorch的Blackwell支持更侧重build/runtime层面，但也有kernel相关改动。

**搜索关键词**：
```
blackwell, sm100, sm_100, sm_100a, cuda_13, nvfp4,
B200, inductor, triton, cutlass, flash_attention,
vec128, launch_bounds, sm120, compute_10
```

**重点关注**：
- TorchInductor SM100 code generation
- Triton kernel templates for Blackwell
- CUTLASS integration for SM100
- NVFP4 support in torch
- Flash attention Blackwell path
- Launch bounds fixes for SM100/SM120
- 新的vectorized ops (vec128)

## 比赛数据扩展

### GPU Mode NVFP4 Blackwell Hackathon

**当前**：4个problem概述页
**需要新增**：
1. **排名数据**：每个problem的完整leaderboard（top 10+排名、用户名、成绩）
2. **获奖方案分析**：
   - Problem 1 (GEMV): Top 3方案的具体实现策略和代码模式
   - Problem 2 (GEMM): Simon/yue/currybab的kernel设计
   - Problem 3 (Gated Dual GEMM): 前几名的fusion策略
   - Problem 4 (Grouped GEMM): 前几名的CLC/tile策略
3. **参赛者博客和代码**：
   - 搜索GitHub repos: `nvfp4 hackathon`, `gpu-mode blackwell`
   - 搜索博客: GPU Mode Discord讨论摘要
4. **Reward hack分析**：已有概述，扩展技术细节

**搜索方法**：
```
# GitHub repos
curl "https://api.github.com/search/repositories?q=nvfp4+hackathon"
curl "https://api.github.com/search/repositories?q=gpu-mode+blackwell+kernel"

# GPU Mode leaderboard API (if available)
# https://www.gpumode.com/leaderboard/595 (GEMV)
# https://www.gpumode.com/leaderboard/597 (GEMM)

# Participant blogs
WebSearch: "blackwell nvfp4 hackathon solution"
WebSearch: "gpu mode hackathon blackwell winner"
WebSearch: "nvfp4 kernel optimization blog"
```

### FlashInfer AI Kernel Generation Contest (MLSys 2026)

**当前**：3个track概述页
**需要新增**：
1. **提交方案仓库**：搜索所有flashinfer-bench-starter-kit的forks（17个fork）
2. **每个fork的solution分析**：
   - Track A (Fused MoE): 参赛者的kernel实现
   - Track B (Sparse Attention): 参赛者的indexer+attention kernel
   - Track C (GatedDeltaNet): 参赛者的prefill/decode kernel
3. **Agent baseline分析**：
   - flashinfer-ai/mlsys26-agent-baseline 的evolve/iterative agent策略
   - K-Search论文的co-evolving world model方法
4. **FlashInfer-Bench leaderboard数据**：
   - bench.flashinfer.ai 的AI-generated kernel排名
   - 每个model (Gemini, GPT-5, Claude) 的per-kernel性能

**搜索方法**：
```
# Contest forks
curl "https://api.github.com/repos/flashinfer-ai/flashinfer-bench-starter-kit/forks?per_page=100"

# Contest submissions tagged on GitHub
curl "https://api.github.com/search/repositories?q=flashinfer+mlsys+2026"
curl "https://api.github.com/search/repositories?q=flashinfer-bench"

# Leaderboard
WebFetch: https://bench.flashinfer.ai/
WebSearch: "flashinfer mlsys 2026 contest results"
WebSearch: "flashinfer bench leaderboard kernel"
```

## 执行策略

### 并行度

大仓库需要更多sub-agent，每个agent负责一个时间段内50-80个PR的搜索+过滤+创建：

**CUTLASS**（41 PRs, 小规模）：2 agents
- Agent: 2025-01 ~ 2025-09
- Agent: 2025-10 ~ 2026-04

**SGLang**（194 PRs）：4 agents
- Agent: 2025-01 ~ 2025-03
- Agent: 2025-04 ~ 2025-06
- Agent: 2025-07 ~ 2025-09
- Agent: 2025-10 ~ 2026-04

**vLLM**（254 PRs）：5 agents
- Agent: 2025-01 ~ 2025-03
- Agent: 2025-04 ~ 2025-06
- Agent: 2025-07 ~ 2025-09
- Agent: 2025-10 ~ 2025-12
- Agent: 2026-01 ~ 2026-04

**FlashInfer**（300 PRs）：5 agents
- Agent: 2025-01 ~ 2025-03
- Agent: 2025-04 ~ 2025-06
- Agent: 2025-07 ~ 2025-09
- Agent: 2025-10 ~ 2025-12
- Agent: 2026-01 ~ 2026-04

**PyTorch**（141 PRs）：3 agents
- Agent: 2025-01 ~ 2025-06
- Agent: 2025-07 ~ 2025-12
- Agent: 2026-01 ~ 2026-04

**比赛**：3 agents
- Agent: GPU Mode hackathon leaderboards + solutions
- Agent: FlashInfer contest forks + submissions
- Agent: Additional blogs + docs

总共：**2 + 4 + 5 + 5 + 3 + 3 = 22 个并行 sub-agents**

每批可发6个并行agent，需要 4 批执行。

### 每个sub-agent的工作流

```
1. 用多个关键词搜索GitHub API，收集所有匹配PR的number和title
2. 去重合并
3. 对每个PR：
   a. 获取PR描述（gh api repos/{repo}/pulls/{number}）
   b. 根据过滤标准判断是否收录
   c. 如果收录：提取metadata，创建sources/prs/{repo}/PR-{N}.md
4. 使用严格的controlled vocabulary（从data/tags.yaml）
5. 确保frontmatter完整且validate.py通过
```

### 质量保证

1. 每个sub-agent完成后立即运行 `python3 scripts/validate.py`
2. 不合格的文件立即修复
3. 最终运行 `python3 scripts/generate-indices.py` 重建所有索引
4. 运行link integrity check

### 预期结果（收录至少一半匹配PR）

| 来源 | API匹配数 | 目标（≥50%） | 当前 | 新增 |
|------|----------|-------------|------|------|
| CUTLASS PRs | 41 (blackwell) | **20+** | 7 | 13+ |
| SGLang PRs | 194 (sm100) | **100+** | 5 | 95+ |
| vLLM PRs | 254 (sm100) | **130+** | 6 | 124+ |
| FlashInfer PRs | 300 (sm100) | **150+** | 6 | 144+ |
| PyTorch PRs | 141 (sm100) | **70+** | 7 | 63+ |
| GPU Mode 比赛 | leaderboards + solutions | **20+** | 4 | 16+ |
| FlashInfer 比赛 | 17 forks + leaderboard | **15+** | 3 | 12+ |
| Blogs | identified | **25+** | 10 | 15+ |
| Docs | identified | **12+** | 6 | 6+ |
| **Total sources** | **~930+** | **540+** | **54** | **~490+ new** |

加上现有37 wiki pages + 大量新增wiki pages → **总计 600-700+ files**

### 过滤策略说明

GitHub API匹配数中有大量重复（多个关键词匹配同一PR）和低相关PR。实际唯一PR数约为匹配数的60-70%。过滤掉纯CI/doc/bump后，目标是保留**至少50%的唯一匹配PR**。

对于大仓库（SGLang 194, vLLM 254, FlashInfer 300），需要：
1. 先用API获取全部匹配PR列表（number + title）
2. 按title快速过滤掉明显无关的（`[CI]`, `[Doc]`, `bump`, `typo`, `format`）
3. 对剩余PR获取详情并创建source page
4. 每个sub-agent处理50-100个PR，需要拆更多时间段

## 额外博客和文档待收录

### 博客（新增 10-15 篇）
- Simon's NVFP4 GEMV Blog (Part 1 + Part 2)
- TFLOPS Gap: FP4 MoE Kernel Engineering on Blackwell (HuggingFace)
- NVFP4 Format Details (Harold Benoit)
- JAX Pallas Blackwell Matmul tutorial
- Tilus ASPLOS paper summary
- Blackwell Microbenchmarking papers (arxiv 2512.02189, 2507.10789)
- vLLM DeepSeek V3.2 Sparse Attention blog
- Qwen3-Next architecture blog (NVIDIA, Alibaba)
- K-Search automated kernel generation (arxiv 2602.19128)
- GPU Mode "Anatomy of a Reward Hack" full analysis

### 文档（新增 4-6 篇）
- CUTLASS Changelog (SM100 entries)
- CUTLASS CLC documentation
- Blackwell Compatibility Guide
- NVIDIA cuTile Python DSL reference
- Tilus documentation

--- Original Design Draft End ---
