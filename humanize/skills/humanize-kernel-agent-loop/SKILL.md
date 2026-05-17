---
name: humanize-kernel-agent-loop
description: "Run an end-to-end Humanize Kernel Agent Loop for GPU kernel optimization: plan, refine, create a clean standalone repo, use kernel-knowledge, benchmark, profile with ncu-report/Nsight Compute, maintain lineage/ledgers, and start RLCR."
type: flow
---

# Humanize Kernel Agent Loop

Use this flow when the user wants a CUDA kernel optimization loop, not a
general software feature loop. This is a kernel-specialized wrapper around
Humanize RLCR.

## Algorithm Mapping

This skill follows the Humanize kernel loop architecture without pinning the
writer agent or review model:

- Planning: the current writer agent turns the one-sentence kernel goal into a
  kernel-specific plan, refines it, and records acceptance criteria.
- Execution: the current writer agent edits the standalone repo, compiles,
  tests, benchmarks, profiles with `ncu-report`, and queries `kernel-knowledge`
  when useful.
- Review: Humanize's native Stop hook uses the configured review backend and
  model to review evidence; after implementation is accepted, the review phase
  runs the configured branch-diff review.
- Feedback loop: if review blocks exit, the current writer agent applies the
  feedback and reruns the inspect/edit/compile/test/benchmark/profile loop.

In diagrams or papers that say "Claude executes, Codex reviews", read "Claude"
as "the current writer agent". In a Claude Code session that may be Claude; in
a Codex session that may be Codex. The review model is controlled by Humanize
configuration or CLI flags, not by this skill.

The installer hydrates these paths:

```text
Humanize runtime: {{HUMANIZE_RUNTIME_ROOT}}
KernelPilot root: {{KERNELPILOT_ROOT}}
```

If `{{KERNELPILOT_ROOT}}` was not hydrated, locate a repository containing
`knowledge/SKILL.md` and `knowledge/evidence/pull-bundles/`.

## Contract

Run the Humanize steps inside this skill. Do not ask the user to run separate
`gen-plan`, `refine-plan`, or `humanize-rlcr` commands.

Given a one-sentence kernel request, you must:

1. Build the kernel-specific plan yourself.
2. Refine it yourself.
3. Create or enter a clean standalone optimization repo.
4. Start Humanize RLCR on the refined plan.
5. Execute the current round until the Stop hook takes over.

Ask the user only if the target kernel, target GPU, comparison target, or hard
scope constraint is missing and cannot be inferred safely.

## Hard Rules

- Candidate implementation language is user-directed. If the user specifies
  CUDA C++/PTX, Triton, CuTe DSL, TileLang, CUTLASS/CuTe, ThunderKittens,
  torch.compile/Inductor, or another kernel stack, use that stack.
- If the user does not specify a language, choose the implementation system most
  likely to reach the stated correctness and performance target, using the
  baseline framework as one available signal rather than a required route.
- Treat "standalone" as a repository, build, benchmark, and runtime boundary.
  It does not prescribe whether the implementation starts from public source,
  prior art, generated code, or a new kernel design. The candidate must live in
  the isolated optimization repo and must not call the baseline package as its
  runtime implementation.
- The writer agent owns the implementation route. It may copy, port, adapt,
  study, or ignore public baseline/prior-art source when that choice is
  compatible with the user request, license, and attribution requirements.
  Humanize should not ask the user to choose baseline-derived versus
  from-scratch unless there is a concrete ambiguity that blocks safe execution.
- If public source directly affects code, record the exact source path/URL,
  commit or version, license/notice, copied/adapted files, and delta in the
  attempt ledger or lineage. If no source is copied, still record influential
  profile or knowledge evidence that drove the route.
- Keep the source framework checkout itself read-only for standalone work unless
  the user explicitly asks for an in-place framework patch. The standalone repo
  may contain copied/adapted public source and subsequent mutations when the
  agent chooses that route.
- Run optimization work in a fresh standalone git repo with its own PyTorch
  binding, correctness tests, benchmark harness, ledgers, lineage, and profile
  artifacts.
- Every correct candidate attempt gets an attempt-ledger row. Only correct
  candidates that improve performance get an optimization-ledger row.
- Collect one baseline `ncu-report` digest for a representative case after
  baseline correctness/benchmark succeeds. Skip it only when Nsight Compute
  cannot run, and record the reason.
- Use `ncu-report` again for regressions, plateaus, surprising wins, or
  profile-driven edits. Do not run full NCU for every tiny iteration unless the
  benchmark result is hard to explain.
- Do not declare the loop complete while relevant NCU/profile acceptance
  criteria are unmet.

## Required Files In The Standalone Repo

Create these before starting RLCR, then keep them updated during the loop:

```text
.gitignore
.humanize/kernel-agent/refined-plan.md
README.md
src/<task_name>/
bindings/
tests/
benchmarks/
ledgers/attempt-ledger.md
ledgers/optimization-ledger.md
ledgers/lineage.jsonl
profile-artifacts/README.md
```

The plan file may stay gitignored under `.humanize/` so RLCR can start without
tracking local loop state.

## Knowledge Evidence

KernelPilot provides a PR-driven evidence corpus, and Humanize owns when, how,
and how much to use it. Knowledge lookup is part of the autonomous optimization
loop: the writer agent queries PR artifacts whenever they help the current
plan, implementation choice, benchmark result, profile digest,
plateau/regression explanation, reviewer question, or next kernel edit.
PR diffs and materialized source snapshots are the primary evidence, while
wiki syntheses, docs, blogs, contest notes, and query indices are supporting
knowledge that Humanize may use whenever they clarify hardware behavior,
techniques, profile interpretation, or implementation choices.

Useful entry points from `{{KERNELPILOT_ROOT}}/knowledge`:

```bash
cd {{KERNELPILOT_ROOT}}/knowledge
python3 scripts/query.py "tcgen05" --architecture B200 --limit 10
python3 scripts/query.py --repo pytorch/pytorch --compact
python3 scripts/get_page.py pr-pytorch-157241 --follow-sources
```

Useful wiki/doc/blog entry points:

```bash
cd {{KERNELPILOT_ROOT}}/knowledge

# Synthesized wiki pages: hardware, techniques, patterns, languages, kernels.
python3 scripts/query.py "Blackwell memory hierarchy" --type hardware --limit 10
python3 scripts/query.py --type technique --tag pipeline-stages --compact
python3 scripts/query.py "tail effect persistent scheduling" --type pattern --compact
python3 scripts/query.py "PTX cache policy" --type language --compact

# Source docs and blogs. Source pages use source_category values as --type.
python3 scripts/query.py "tcgen05 tmem tuning guide" --type official-doc --limit 10
python3 scripts/query.py "Blackwell microbenchmark tensor memory" --type benchmark-blog --limit 10
python3 scripts/query.py "CuTe DSL TMA swizzle" --type community-note --limit 10
python3 scripts/get_page.py doc-nvidia-tuning-guide --body-only
python3 scripts/get_page.py blog-blackwell-microbenchmarking --body-only

# Regex search: wiki-only for synthesized pages, sources-only for docs/blogs.
python3 scripts/grep_wiki.py "tcgen05\\.fence" --only wiki
python3 scripts/grep_wiki.py "long scoreboard" "prefetch" --only sources --any
```

Prefer materialized bundles under:

```text
knowledge/evidence/pull-bundles/<repo-id>/gh-<number>/
```

Each bundle should contain `review.diff`, `ORIGIN.yaml`, `upstream.json`,
and key changed source/test/benchmark files under `source-snapshot/`.

Autonomous query order:

1. Use `scripts/query.py` for broad routing by architecture, repo, tag,
   operator, bottleneck, or exact instruction/feature term.
2. Use `scripts/get_page.py --follow-sources` to expand a promising wiki or PR
   page into its cited evidence.
3. Open the materialized `review.diff`, `ORIGIN.yaml`, `upstream.json`, and
   `source-snapshot/` files for the PR before borrowing any idea.
4. Use `scripts/grep_wiki.py` for exact terms such as instruction mnemonics,
   CuTe atoms, profiler counters, dtype names, and memory/cache policy names.
5. Use wiki syntheses to choose techniques and interpret profiler symptoms; use
   docs/blogs to understand hardware contracts, DSL semantics, and public
   performance claims; then ground implementation choices back in PR/source
   evidence when code is borrowed or adapted.

Knowledge lookup should remain autonomous. Do not create a separate reading
ledger just to prove that pages were opened. When a source directly affects
code, record the actionable provenance in the relevant attempt row, lineage
entry, or profile digest.

## Plan Requirements

Write `.humanize/kernel-agent/refined-plan.md` in the standalone repo. It must
use the Humanize gen-plan schema and include these acceptance criteria:

- Clean standalone repo exists and is committed before RLCR starts.
- Baseline framework checkout is protected from accidental edits unless the
  user asks for an in-place patch.
- Candidate implementation language is documented and follows the user request
  or the agent's selected strategy.
- Implementation strategy is selected by the writer agent and tied directly to
  the performance/correctness target. The plan must not create a pending user
  decision merely to choose baseline-derived versus from-scratch.
- If public baseline or prior-art code seeds any candidate, provenance,
  license/notice, copied/adapted files, and the first optimization delta are
  recorded before further mutation.
- If no public source is copied or adapted, the plan and lineage still record
  the profile, knowledge, or engineering reason for that route.
- Correctness tests cover representative shapes, dtypes, edge cases, and
  baseline parity.
- Benchmark harness records per-shape timing, geomean, best/worst cases, and
  environment metadata.
- A baseline `ncu-report` profile is captured for one representative
  bottleneck case after baseline benchmark succeeds and before the first
  profile-driven edit.
- Later `ncu-report` profiles are captured for regressions, plateaus, surprising
  wins, or reviewer-requested evidence, then converted into NCU Report Digests.
- Attempt ledger records every version, including failed correctness,
  regressions, plateaus, and abandoned ideas.
- Optimization ledger records only correct versions with measured improvement.
- Lineage records parent version, mutation/motivation, influential source or PR
  evidence when it directly affects code, result, and selected/rejected status.
- When progress stalls, Humanize expands PR research autonomously. Prefer unread
  PR bundles, changed kernel files, linked tests, benchmarks, and profiler
  notes, guided by the current task context and existing attempt/lineage notes.
- When profiling shows a candidate is far below the target or in a different
  bottleneck class than the baseline, do not keep spending rounds on the same
  lineage's local micro-tuning unless `ncu-report` names a concrete edit with
  plausible target-scale impact. The next round must change strategy, produce a
  design reset, or justify the current route with new evidence.
- Experimental GPU kernels that can hang must have timeout-bounded bring-up
  milestones. A timeout marks that lineage rejected until a minimal executable
  tile validates the suspected protocol, descriptor, layout, memory, and
  synchronization semantics.
- Stop only when all ACs are met, or when `ncu-report` evidence shows the kernel is
  already beyond 85% of the relevant peak and no low-effort implementation edit
  remains.

## Implementation Strategy Autonomy

Use this policy when refining kernel plans and writing round contracts:

- The user should define the operator, scope, hardware, allowed implementation
  stack, correctness checks, benchmark method, and performance target.
- The agent chooses the implementation route needed to satisfy those goals. It
  may start from existing code, port helpers, write a fresh kernel, combine
  approaches, or abandon a route when evidence says it will not converge.
- Do not split prompts, plans, or pending decisions into "baseline-derived" and
  "from-scratch" tracks unless the user explicitly makes that distinction part
  of the task.
- Reviewers judge whether the current route is advancing the main objective,
  not whether it matches a preferred source-use style.
- Source use is a provenance and license concern, not a separate product
  requirement. Record it rigorously when it happens; do not block progress just
  to ask whether it is allowed when the user has not prohibited it.

## Progress And Timeout Gates

- If an attempt times out or hangs, reproduce the failure with the smallest
  shape/tile under a hard timeout before any target-size benchmark. Record the
  rejected lineage and the suspected root-cause surface.
- If two consecutive reviews identify the same mainline blocker, the next
  round must be a strategy-reset round with a narrower executable milestone,
  not another broad implementation pass.
- If a candidate remains orders of magnitude below the target after a correct
  tensor-core-class attempt, treat further same-lineage tuning as evidence
  maintenance unless `ncu-report` names a specific low-risk edit with plausible
  order-of-magnitude impact.

## NCU Report Evidence

Invoke the `ncu-report` skill whenever any of these hold:

- Baseline benchmark has passed and no baseline NCU Report Digest exists.
- A correct candidate is within +/-2% of baseline across configured cases.
- A correct candidate regresses on one or more configured cases.
- The benchmark has plateaued or weakly improved and the next edit is unclear.
- A candidate is much faster than expected and needs explanation.
- A reviewer asks for an NCU Report Digest.

Persist `.ncu-rep`, raw CSV, source export, PM-sampling export when available,
and comparison paths in the digest. Each digest must end with one concrete next
kernel edit.

## RLCR Startup

After writing and committing the standalone repo scaffolding, start the loop
from inside the standalone repo:

```bash
"{{HUMANIZE_RUNTIME_ROOT}}/scripts/setup-rlcr-loop.sh" .humanize/kernel-agent/refined-plan.md --yolo
```

If setup exits non-zero, stop and report the error. Do not bypass the gate.
The loop uses Humanize's configured review model and default max iteration
limit unless the caller explicitly passes overrides such as `--max` or a model
flag. The current default max iteration limit is 84 rounds.

After setup succeeds:

1. Read `.humanize/rlcr/<timestamp>/round-0-prompt.md`.
2. Execute the current round.
3. Commit changes.
4. Write the required round summary.
5. Stop normally so the native Humanize Stop hook can review.

If the hook blocks exit, follow the generated next-round prompt exactly.
