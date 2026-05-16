# Phase 3 SHA-pinned strict verify audit log

Captured: 2026-04-17T23:37:21Z (R25 refresh: same 7 pytorch PRs refetched again after the R25 atomic-swap changes; the gh abbreviation cache flipped between sessions, so local review.diff bytes needed re-alignment with the upstream 12-char abbreviation.)
Command : `python3 scripts/verify_verbatim.py --strict`
Exit    : 0 (documented contract: 0 = full-corpus upstream byte-match; 1 = --strict content mismatch; 2 = env failure)

## Environment

```
gh version 2.90.0 (2026-04-16)
  ✓ Logged in to github.com account DongyunZou (/home/dongyun/.config/gh/hosts.yml)
```

## Scope

- 87 evidence bundles under `evidence/` (89 post-R32 − 2 more blog
  extraction bundles that turned `code_present: false` in R35 after
  the unlabeled-fence heuristic tightened to reject formulas / configs
  without a code-structure signal (`;`, `{`, `}`, or language keyword):
  `nvfp4-format-details` had only a single dequantization formula
  (`x_hat_i = s_m * s_b * deq_FP4(q_i)`) and
  `vllm-deepseek-v3-sparse-attention` had deployment configs
  (`DP=8, EP=8, TP=1`, `vllm serve ... --tensor-parallel-size 8`).)
- 301 files with `mode: verbatim` or `mode: upstream-patch` and no `size_cap_truncated` marker (was 310; minus the files in the 3 dropped vendor-prefixed PR evidence bundles and the pseudo-code file in ping-pong-scheduling/full)

## stdout

```
Verified 87 bundle(s).
All verbatim/upstream-patch assets match upstream.
```

## Exit-code contract (Round 6)

`scripts/verify_verbatim.py` classifies `gh` stderr via a substring allow-list
(`_ENV_ERROR_HINTS`) that covers the DNS / TCP / TLS / proxy / auth / rate-limit
failure modes as well as generic transport strings like `error connecting`,
`failed to connect`, `couldn't connect`, `cannot reach`, and equivalents. A hit
raises `EnvError` and contributes to the `ENV:` stream (exit 2); any other
failure contributes to the `WARN:` stream (exit 1 under `--strict`).

Reproducing an environment failure here (by prepending a fake `gh` shim that
emits `error connecting to api.github.com`) makes the verifier emit
`ENV:` lines and return `exit 2`, confirming the contract end-to-end on the
path Codex's review environment takes.

## Reproducibility

1. Install gh CLI and run `gh auth login`.
2. From the repo root: `python3 scripts/verify_verbatim.py --strict`.
3. Compare the exit code + stdout against this log. In a network-capable
   environment the expected exit is 0 and the stdout is
   "Verified 76 bundle(s). / All verbatim/upstream-patch assets match upstream."
4. In an offline environment the verifier correctly exits 2 (`ENV:` stream),
   NOT 1 — proving the contract separates env failure from content mismatch.
