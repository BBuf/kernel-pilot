# Other Kernel Cases PRs

Optimization recipe: Use the PR as grounded prior art; inspect diff, linked tests, and benchmark evidence before applying the idea.

NCU first look: Choose metrics based on the changed kernel family after opening the diff.

## Inspection Questions

- Which source paths actually changed kernel behavior?
- What evidence makes this more than integration churn?

## PRs

| Repo | PR | Merged | What to inspect | Ledger key |
| --- | --- | --- | --- | --- |
| `NVIDIA-developer-blog/code-samples` | [#3](https://github.com/NVIDIA-developer-blog/code-samples/pull/3) double fix coalescing.cu | 2014-09-15 | kernel: `series/cuda-cpp/coalescing-global/coalescing.cu` | `NVIDIA-developer-blog/code-samples#3` |
