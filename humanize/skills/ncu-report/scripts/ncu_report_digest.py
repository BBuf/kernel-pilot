#!/usr/bin/env python3
"""Create a first-pass Nsight Compute digest from exported CSV metrics.

This helper is intentionally conservative. It extracts common NCU metric rows,
compares a candidate against an optional baseline, classifies the strongest
signal, and writes a markdown digest that an agent must still inspect and edit.
"""

from __future__ import annotations

import argparse
import csv
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


@dataclass
class MetricValue:
    name: str
    value: float
    unit: str = ""
    kernel: str = ""


IMPORTANT_PATTERNS: Sequence[Tuple[str, str]] = (
    ("duration", r"gpu__time_duration\.sum"),
    ("sm_pct", r"sm__throughput\.avg\.pct_of_peak_sustained_elapsed"),
    ("tensor_pct", r"(sm__inst_executed_pipe_tensor|pipe_tensor).*pct_of_peak"),
    ("alu_pct", r"sm__pipe_alu_cycles_active\.avg\.pct_of_peak"),
    ("dram_pct", r"dram__throughput\.avg\.pct_of_peak_sustained_elapsed"),
    ("l2_pct", r"lts__t_bytes\.avg\.pct_of_peak_sustained_elapsed"),
    ("active_warps", r"sm__warps_active\.avg\.pct_of_peak_sustained_active"),
    ("eligible_warps", r"smsp__warps_eligible\.avg\.per_cycle_active"),
    ("registers_per_thread", r"launch__registers_per_thread"),
    ("smem_static", r"launch__shared_mem_per_block_static"),
    ("smem_dynamic", r"launch__shared_mem_per_block_dynamic"),
    ("bank_conflicts_ld", r"bank_conflicts.*shared.*ld|shared.*bank_conflicts.*ld"),
    ("bank_conflicts_st", r"bank_conflicts.*shared.*st|shared.*bank_conflicts.*st"),
)


STALL_RE = re.compile(r"smsp__warp_issue_stalled_([A-Za-z0-9_]+)\.")


def _row_get(row: Dict[str, str], names: Iterable[str]) -> str:
    lower = {k.strip().lower(): v for k, v in row.items()}
    for name in names:
        if name.lower() in lower:
            return lower[name.lower()]
    return ""


def _to_float(raw: str) -> Optional[float]:
    text = str(raw).strip().replace(",", "")
    if not text or text.upper() in {"N/A", "NAN", "INF", "-INF"}:
        return None
    text = text.rstrip("%")
    try:
        value = float(text)
    except ValueError:
        match = re.search(r"-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?", text)
        if not match:
            return None
        value = float(match.group(0))
    if math.isnan(value) or math.isinf(value):
        return None
    return value


def _kernel_matches(kernel: str, kernel_re: Optional[re.Pattern[str]]) -> bool:
    if kernel_re is None:
        return True
    return bool(kernel_re.search(kernel or ""))


def load_metrics(path: Path, kernel_regex: str = "") -> Dict[str, List[MetricValue]]:
    kernel_re = re.compile(kernel_regex) if kernel_regex else None
    metrics: Dict[str, List[MetricValue]] = {}
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            return metrics
        fields = [f or "" for f in reader.fieldnames]
        has_metric_rows = any(f.strip().lower() in {"metric name", "metric"} for f in fields)

        for row in reader:
            kernel = _row_get(row, ("Kernel Name", "Kernel", "Demangled Name", "Name"))
            if not _kernel_matches(kernel, kernel_re):
                continue

            if has_metric_rows:
                name = _row_get(row, ("Metric Name", "Metric"))
                value = _to_float(_row_get(row, ("Metric Value", "Value")))
                unit = _row_get(row, ("Metric Unit", "Unit"))
                if name and value is not None:
                    metrics.setdefault(name, []).append(MetricValue(name, value, unit, kernel))
                continue

            for key, raw_value in row.items():
                if not key:
                    continue
                if "__" not in key and not key.startswith("launch__"):
                    continue
                value = _to_float(raw_value)
                if value is None:
                    continue
                metrics.setdefault(key, []).append(MetricValue(key, value, "", kernel))
    return metrics


def choose(metrics: Dict[str, List[MetricValue]], pattern: str) -> Optional[MetricValue]:
    regex = re.compile(pattern)
    for name in sorted(metrics):
        if regex.search(name):
            return metrics[name][0]
    return None


def choose_exact(metrics: Dict[str, List[MetricValue]], name: str) -> Optional[MetricValue]:
    values = metrics.get(name)
    return values[0] if values else None


def summarize(metrics: Dict[str, List[MetricValue]]) -> Dict[str, MetricValue]:
    found: Dict[str, MetricValue] = {}
    for label, pattern in IMPORTANT_PATTERNS:
        value = choose(metrics, pattern)
        if value is not None:
            found[label] = value
    return found


def stall_breakdown(metrics: Dict[str, List[MetricValue]]) -> List[Tuple[str, str, float, float]]:
    totals: List[Tuple[str, str, float]] = []
    for name, values in metrics.items():
        match = STALL_RE.search(name)
        if match and values:
            totals.append((match.group(1), name, values[0].value))
    total = sum(max(v, 0.0) for _, _, v in totals)
    if total <= 0:
        return []
    rows = [(stall, name, value, value * 100.0 / total) for stall, name, value in totals]
    return sorted(rows, key=lambda item: item[3], reverse=True)


def classify(summary: Dict[str, MetricValue], stalls: List[Tuple[str, str, float, float]]) -> Tuple[str, str, str, str]:
    top_stall = stalls[0][0] if stalls else "unknown"
    top_pct = stalls[0][3] if stalls else 0.0
    sm = summary.get("sm_pct").value if "sm_pct" in summary else None
    tensor = summary.get("tensor_pct").value if "tensor_pct" in summary else None
    dram = summary.get("dram_pct").value if "dram_pct" in summary else None
    l2 = summary.get("l2_pct").value if "l2_pct" in summary else None

    if tensor is not None and tensor >= 85.0:
        return ("Tensor-pipe-saturated", top_stall, "High", "No low-effort tensor-core edit; inspect epilogue, routing, or launch/fusion overhead.")
    if dram is not None and dram >= 70.0 and (sm is None or sm < dram):
        return ("HBM-bound", top_stall, "High", "Reduce bytes or improve global access coalescing/vectorization for the hot path.")
    if l2 is not None and l2 >= 70.0 and (dram is None or dram < 60.0):
        return ("L2-bound", top_stall, "Medium", "Increase tile reuse or adjust persistent scheduling/cache policy.")
    if top_stall == "long_scoreboard" and top_pct >= 25.0:
        return ("Memory-latency-bound", top_stall, "High", "Add prefetch/MLIO or rewrite the hot load for coalesced vectorized access.")
    if top_stall == "short_scoreboard" and top_pct >= 20.0:
        return ("Shared-memory-latency-bound", top_stall, "Medium", "Inspect shared-memory layout and apply padding/swizzle or reduce smem round trips.")
    if top_stall in {"barrier", "membar"} and top_pct >= 15.0:
        return ("Synchronization-bound", top_stall, "Medium", "Inspect barrier/mbarrier phase tracking and pipeline stage lifetime.")
    if top_stall in {"no_instruction", "imc_miss"} and top_pct >= 15.0:
        return ("Front-end-bound", top_stall, "Medium", "Reduce code size/unroll pressure or split/specialize the hot path.")
    if sm is not None and dram is not None and sm < 35.0 and dram < 35.0:
        return ("Latency-or-tail-bound", top_stall, "Low", "Use source/PM-sampling evidence to identify tail waves, divergence, or launch gaps.")
    return ("Mixed", top_stall, "Low", "Inspect source counters and PM-sampling before selecting a code edit.")


def fmt_metric(value: Optional[MetricValue]) -> str:
    if value is None:
        return "missing"
    if value.unit:
        return f"{value.value:g} {value.unit}"
    return f"{value.value:g}"


def pct_delta(candidate: Optional[MetricValue], baseline: Optional[MetricValue]) -> str:
    if candidate is None or baseline is None or baseline.value == 0:
        return ""
    delta = (candidate.value - baseline.value) * 100.0 / baseline.value
    return f"{delta:+.2f}%"


def render_digest(
    candidate: Dict[str, List[MetricValue]],
    baseline: Optional[Dict[str, List[MetricValue]]],
    args: argparse.Namespace,
) -> str:
    cand_summary = summarize(candidate)
    base_summary = summarize(baseline or {})
    stalls = stall_breakdown(candidate)
    bottleneck, top_stall, confidence, next_edit = classify(cand_summary, stalls)

    lines: List[str] = []
    lines.append(f"### NCU Report Digest: {args.kernel_regex or '<kernel>'} @ {args.version}")
    lines.append("")
    lines.append("Environment")
    lines.append(f"- GPU / arch: {args.gpu or '<fill in>'}")
    lines.append(f"- Benchmark command: {args.command or '<fill in>'}")
    lines.append(f"- Shape / dtype: {args.shape or '<fill in>'}")
    lines.append(f"- Baseline or parent report: {args.baseline_report or '<none>'}")
    lines.append(f"- Candidate report: {args.report or '<fill in>'}")
    lines.append(f"- Raw CSV: {args.csv}")
    lines.append("")
    lines.append("Headline")
    lines.append(f"- Bottleneck class: {bottleneck}")
    lines.append(f"- Dominant stall or hotspot: {top_stall}")
    lines.append(f"- Confidence: {confidence}")
    lines.append("- Why this report is valid: kernel regex matched exported NCU metrics; inspect details/source exports before finalizing.")
    lines.append("")
    lines.append("Evidence")
    lines.append("| Metric | Baseline | Candidate | Delta | Interpretation |")
    lines.append("|---|---:|---:|---:|---|")
    for label, _pattern in IMPORTANT_PATTERNS:
        cand = cand_summary.get(label)
        base = base_summary.get(label)
        if cand is None and base is None:
            continue
        lines.append(f"| `{cand.name if cand else (base.name if base else label)}` | {fmt_metric(base)} | {fmt_metric(cand)} | {pct_delta(cand, base)} | {label} |")

    if stalls:
        lines.append("")
        lines.append("Stall Breakdown")
        lines.append("| Stall | Metric | Value | Share |")
        lines.append("|---|---|---:|---:|")
        for stall, name, value, share in stalls[:8]:
            lines.append(f"| {stall} | `{name}` | {value:g} | {share:.1f}% |")

    lines.append("")
    lines.append("Source / PM-Sampling Hotspots")
    lines.append("- <inspect SourceCounters or PM-sampling exports and fill in the source/PTX/SASS line or timeline phase>")
    lines.append("")
    lines.append("Inference Chain")
    lines.append(f"1. Measured counter: dominant stall `{top_stall}` with bottleneck `{bottleneck}`.")
    lines.append(f"2. Likely mechanism: {next_edit}")
    lines.append("3. Why other hypotheses are weaker: <fill in after source/sampling inspection>")
    lines.append("4. Risk: <fill in>")
    lines.append("")
    lines.append("Next Concrete Edit")
    lines.append("- File: <fill in>")
    lines.append(f"- Change: {next_edit}")
    lines.append("- Validation: rerun the same benchmark shape and re-check the metric(s) above.")
    lines.append("- Expected metric movement: <fill in>")
    lines.append("")
    return "\n".join(lines)


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", required=True, help="Candidate NCU raw CSV export")
    parser.add_argument("--baseline-csv", default="", help="Baseline or parent NCU raw CSV export")
    parser.add_argument("--kernel-regex", default="", help="Regex used to filter kernel rows")
    parser.add_argument("--output", default="", help="Digest output path; stdout if omitted")
    parser.add_argument("--version", default="candidate", help="Candidate version label")
    parser.add_argument("--report", default="", help="Candidate .ncu-rep path")
    parser.add_argument("--baseline-report", default="", help="Baseline .ncu-rep path")
    parser.add_argument("--gpu", default="", help="GPU/architecture label")
    parser.add_argument("--shape", default="", help="Shape/dtype label")
    parser.add_argument("--command", default="", help="Benchmark command")
    return parser.parse_args(argv)


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    candidate = load_metrics(Path(args.csv), args.kernel_regex)
    if not candidate:
        print(f"error: no metrics loaded from {args.csv}", file=sys.stderr)
        return 2
    baseline = load_metrics(Path(args.baseline_csv), args.kernel_regex) if args.baseline_csv else None
    digest = render_digest(candidate, baseline, args)
    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        Path(args.output).write_text(digest, encoding="utf-8")
    else:
        print(digest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
