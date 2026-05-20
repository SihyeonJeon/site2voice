from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from site2voice.cli import main
from site2voice.extract import analyze


FIXTURE = Path("examples/saas-home.html")


class Site2VoiceTests(unittest.TestCase):
    def test_analyze_extracts_headings_ctas_and_lexicon(self) -> None:
        payload = analyze(str(FIXTURE))
        self.assertEqual(payload["title"], "Northstar Ops")
        self.assertIn("Run your launch room from one calm board", payload["headings"])
        self.assertIn("Start free", payload["ctas"])
        self.assertIn("launch", payload["lexicon"])

    def test_cli_writes_markdown(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "VOICE.md"
            code = main([str(FIXTURE), "--out", str(out)])
            self.assertEqual(code, 0)
            text = out.read_text(encoding="utf-8")
            self.assertIn("# VOICE.md", text)
            self.assertIn("Common CTAs", text)
            self.assertIn("Start free", text)

    def test_cli_writes_json(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "voice.json"
            code = main([str(FIXTURE), "--format", "json", "--out", str(out)])
            self.assertEqual(code, 0)
            payload = json.loads(out.read_text(encoding="utf-8"))
            self.assertGreater(payload["metrics"]["words"], 20)

    def test_benchmark_scores_after_above_before(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "bench.json"
            code = main(
                [
                    "bench",
                    "examples/editorial-home.html",
                    "examples/before-copy.md",
                    "examples/after-copy.md",
                    "--format",
                    "json",
                    "--out",
                    str(out),
                ]
            )
            self.assertEqual(code, 0)
            payload = json.loads(out.read_text(encoding="utf-8"))
            scores = {item["label"]: item["score"] for item in payload["candidates"]}
            self.assertGreater(scores["after-copy"], scores["before-copy"])
            self.assertGreater(scores["after-copy"], 70)


if __name__ == "__main__":
    unittest.main()
