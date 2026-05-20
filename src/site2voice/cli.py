from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .extract import analyze, to_json, to_markdown


def build_parser() -> argparse.ArgumentParser:
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


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        payload = analyze(args.source, timeout=args.timeout)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    output = to_json(payload) if args.format == "json" else to_markdown(payload, max_snippets=args.max_snippets)
    if args.out:
        path = Path(args.out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(output, encoding="utf-8")
    else:
        print(output, end="" if output.endswith("\n") else "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
