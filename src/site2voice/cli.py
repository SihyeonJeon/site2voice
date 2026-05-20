from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .benchmark import benchmark, benchmark_failures, benchmark_json, benchmark_markdown
from .context_pack import create_context_pack
from .extract import analyze, to_json, to_markdown


def build_generate_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="site2voice",
        description="Generate AI-agent VOICE.md copy profiles from website copy and CTAs.",
        epilog=(
            "Commands:\n"
            "  site2voice SOURCE --out VOICE.md\n"
            "  site2voice init SOURCE --dir .site2voice\n"
            "  site2voice bench REFERENCE candidate.md --strict"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--version", action="version", version=f"site2voice {__version__}")
    parser.add_argument("source", help="URL or local HTML file")
    parser.add_argument("--format", choices=["md", "json"], default="md")
    parser.add_argument("--out", help="write output to this path")
    parser.add_argument("--timeout", type=float, default=20.0, help="seconds to wait for URL fetches")
    parser.add_argument("--max-snippets", type=int, default=8, help="max evidence snippets in Markdown output")
    parser.add_argument("--no-samples", action="store_true", help="omit page-pattern and paragraph samples")
    return parser


def build_bench_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="site2voice bench",
        description="Score candidate copy against a reference copy profile.",
    )
    parser.add_argument("reference", help="URL or local HTML file used as the voice reference")
    parser.add_argument("candidates", nargs="+", help="candidate Markdown/text files to score")
    parser.add_argument("--format", choices=["md", "json"], default="md")
    parser.add_argument("--out", help="write benchmark report to this path")
    parser.add_argument("--timeout", type=float, default=20.0, help="seconds to wait for reference URL fetches")
    parser.add_argument("--strict", action="store_true", help="exit non-zero unless every candidate passes default gates")
    parser.add_argument("--fail-under", type=float, help="exit non-zero if any candidate overall score is below this")
    parser.add_argument("--min-copy-safety", type=float, help="exit non-zero if copy safety is below this")
    parser.add_argument("--min-claim-safety", type=float, help="exit non-zero if claim safety is below this")
    return parser


def build_init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="site2voice init",
        description="Create an agent-ready copy profile context pack.",
    )
    parser.add_argument("source", help="URL or local HTML file")
    parser.add_argument("--dir", default=".site2voice", help="output directory for the context pack")
    parser.add_argument("--timeout", type=float, default=20.0, help="seconds to wait for URL fetches")
    parser.add_argument("--max-snippets", type=int, default=8, help="max evidence snippets in VOICE.md")
    parser.add_argument("--no-samples", action="store_true", help="omit page-pattern and paragraph samples")
    parser.add_argument("--force", action="store_true", help="overwrite existing context pack files")
    return parser


def write_output(output: str, out: str | None) -> None:
    if out:
        path = Path(out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(output, encoding="utf-8")
    else:
        print(output, end="" if output.endswith("\n") else "\n")


def cmd_generate(argv: list[str] | None) -> int:
    args = build_generate_parser().parse_args(argv)
    try:
        payload = analyze(args.source, timeout=args.timeout)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    max_snippets = 0 if args.no_samples else args.max_snippets
    output = to_json(payload) if args.format == "json" else to_markdown(payload, max_snippets=max_snippets)
    write_output(output, args.out)
    return 0


def cmd_bench(argv: list[str]) -> int:
    args = build_bench_parser().parse_args(argv)
    try:
        payload = benchmark(args.reference, args.candidates, timeout=args.timeout)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    output = benchmark_json(payload) if args.format == "json" else benchmark_markdown(payload)
    write_output(output, args.out)
    failures = benchmark_failures(
        payload,
        fail_under=args.fail_under,
        min_copy_safety=args.min_copy_safety,
        min_claim_safety=args.min_claim_safety,
        strict=args.strict,
    )
    if failures:
        print("BENCHMARK FAILED:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 2
    return 0


def cmd_init(argv: list[str]) -> int:
    args = build_init_parser().parse_args(argv)
    try:
        result = create_context_pack(
            args.source,
            output_dir=args.dir,
            timeout=args.timeout,
            max_snippets=0 if args.no_samples else args.max_snippets,
            force=args.force,
        )
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Created voice context pack in {result['output_dir']}:")
    for path in result["files"].values():
        print(f"- {path}")
    return 0


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "bench":
        return cmd_bench(argv[1:])
    if argv and argv[0] == "init":
        return cmd_init(argv[1:])
    return cmd_generate(argv)


if __name__ == "__main__":
    raise SystemExit(main())
