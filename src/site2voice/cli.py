from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .benchmark import benchmark, benchmark_json, benchmark_markdown
from .extract import analyze, to_json, to_markdown


def build_generate_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="site2voice",
        description="Generate AI-agent VOICE.md files from website copy and CTAs.",
    )
    parser.add_argument("--version", action="version", version=f"site2voice {__version__}")
    parser.add_argument("source", help="URL or local HTML file")
    parser.add_argument("--format", choices=["md", "json"], default="md")
    parser.add_argument("--out", help="write output to this path")
    parser.add_argument("--timeout", type=float, default=20.0, help="seconds to wait for URL fetches")
    parser.add_argument("--max-snippets", type=int, default=8, help="max evidence snippets in Markdown output")
    return parser


def build_bench_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="site2voice bench",
        description="Score candidate copy against a website voice profile.",
    )
    parser.add_argument("reference", help="URL or local HTML file used as the voice reference")
    parser.add_argument("candidates", nargs="+", help="candidate Markdown/text files to score")
    parser.add_argument("--format", choices=["md", "json"], default="md")
    parser.add_argument("--out", help="write benchmark report to this path")
    parser.add_argument("--timeout", type=float, default=20.0, help="seconds to wait for reference URL fetches")
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
    output = to_json(payload) if args.format == "json" else to_markdown(payload, max_snippets=args.max_snippets)
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
    return 0


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "bench":
        return cmd_bench(argv[1:])
    return cmd_generate(argv)


if __name__ == "__main__":
    raise SystemExit(main())
