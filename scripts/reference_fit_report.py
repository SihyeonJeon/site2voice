from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from site2voice.webfit import build_webfit_payload, webfit_markdown


def build_payload(voice_path: Path, site_path: Path, candidates: list[Path]) -> dict[str, Any]:
    payload = build_webfit_payload(voice_path, site_path, candidates)
    return {**payload, "schema_version": "site2voice.reference_fit.v1"}


def markdown_report(payload: dict[str, Any]) -> str:
    return webfit_markdown(payload)


def main() -> int:
    parser = argparse.ArgumentParser(description="Score visible web outputs against SITE.md and VOICE.md profiles.")
    parser.add_argument("--voice", required=True, type=Path, help="voice.json reference profile")
    parser.add_argument("--site", required=True, type=Path, help="site.json reference profile")
    parser.add_argument("--out", type=Path, help="write JSON report")
    parser.add_argument("--markdown", type=Path, help="write Markdown report")
    parser.add_argument("candidates", nargs="+", type=Path, help="HTML files to score")
    args = parser.parse_args()
    payload = build_payload(args.voice, args.site, args.candidates)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.markdown:
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        args.markdown.write_text(markdown_report(payload), encoding="utf-8")
    if not args.out and not args.markdown:
        print(markdown_report(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
