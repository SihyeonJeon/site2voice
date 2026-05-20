from __future__ import annotations

import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path

from site2voice import __version__
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
            self.assertIn("CTA verbs", text)
            self.assertIn("Navigation label shape", text)
            self.assertIn("Output Contract", text)
            self.assertIn("Content boundary", text)
            self.assertIn("Brand policy", text)
            self.assertIn("not an official guideline", text)
            self.assertNotIn("Main vocabulary", text)
            self.assertNotIn("Start free", text)

    def test_cli_writes_json(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "voice.json"
            code = main([str(FIXTURE), "--format", "json", "--out", str(out)])
            self.assertEqual(code, 0)
            payload = json.loads(out.read_text(encoding="utf-8"))
            self.assertEqual(payload["schema_version"], "site2voice.voice.v1")
            self.assertEqual(payload["generator"], f"site2voice/{__version__}")
            self.assertGreater(payload["metrics"]["words"], 20)
            self.assertIn("output_contract", payload)
            self.assertIn("sentence_words", payload["output_contract"])
            self.assertEqual(payload["output_contract"]["recommended_terms"], [])
            self.assertIn("source_terms", payload["output_contract"])

    def test_cli_writes_site_markdown(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "SITE.md"
            code = main(["site", str(FIXTURE), "--out", str(out)])
            self.assertEqual(code, 0)
            text = out.read_text(encoding="utf-8")
            self.assertIn("# SITE.md", text)
            self.assertIn("Page Blueprint", text)
            self.assertIn("Section Recipes", text)
            self.assertIn("Rhetorical Pattern", text)
            self.assertIn("Content Boundary", text)
            self.assertIn("Pair it with `VOICE.md`", text)
            self.assertNotIn("Start free", text)
            self.assertNotIn("Northstar Ops", text)

    def test_cli_writes_site_json(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "site.json"
            code = main(["site", str(FIXTURE), "--format", "json", "--out", str(out)])
            self.assertEqual(code, 0)
            payload = json.loads(out.read_text(encoding="utf-8"))
            self.assertEqual(payload["schema_version"], "site2voice.site.v1")
            self.assertEqual(payload["generator"], f"site2voice/{__version__}")
            self.assertIn("site_summary", payload)
            self.assertIn("page_blueprint", payload)
            self.assertIn("section_recipes", payload)
            self.assertNotIn("headings", payload)
            self.assertNotIn("ctas", payload)
            self.assertNotIn("links", payload)
            self.assertNotIn("lexicon", payload)
            self.assertNotIn("paragraph_samples", payload)

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

    def test_benchmark_strict_gate_fails_bad_copy(self) -> None:
        stdout = StringIO()
        stderr = StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            code = main(
                [
                    "bench",
                    "examples/editorial-home.html",
                    "examples/before-copy.md",
                    "--strict",
                ]
            )
        self.assertEqual(code, 2)
        self.assertIn("overall", stderr.getvalue())

    def test_benchmark_strict_gate_passes_good_copy(self) -> None:
        stdout = StringIO()
        with redirect_stdout(stdout):
            code = main(
                [
                    "bench",
                    "examples/editorial-home.html",
                    "examples/after-copy.md",
                    "--strict",
                ]
            )
        self.assertEqual(code, 0)

    def test_init_writes_context_pack(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / ".site2voice"
            stdout = StringIO()
            with redirect_stdout(stdout):
                code = main(["init", str(FIXTURE), "--dir", str(target), "--no-samples"])
            self.assertEqual(code, 0)
            self.assertTrue((target / "VOICE.md").exists())
            self.assertTrue((target / "SITE.md").exists())
            self.assertTrue((target / "voice.json").exists())
            self.assertTrue((target / "site.json").exists())
            self.assertTrue((target / "agent-prompt.md").exists())
            voice_json = json.loads((target / "voice.json").read_text(encoding="utf-8"))
            self.assertEqual(voice_json["schema_version"], "site2voice.voice.v1")
            self.assertIn("output_contract", voice_json)
            self.assertEqual(voice_json["title"], "")
            self.assertEqual(voice_json["meta_description"], "")
            self.assertEqual(voice_json["headings"], [])
            self.assertEqual(voice_json["paragraph_samples"], [])
            self.assertEqual(voice_json["lexicon"], [])
            self.assertEqual(voice_json["ctas"], [])
            self.assertEqual(voice_json["links"], [])
            self.assertEqual(voice_json["buttons"], [])
            self.assertEqual(voice_json["output_contract"]["source_terms"], [])
            site_json = json.loads((target / "site.json").read_text(encoding="utf-8"))
            self.assertEqual(site_json["schema_version"], "site2voice.site.v1")
            self.assertIn("site_summary", site_json)
            self.assertNotIn("headings", site_json)
            self.assertNotIn("ctas", site_json)
            site_md = (target / "SITE.md").read_text(encoding="utf-8")
            self.assertIn("Page Blueprint", site_md)
            self.assertIn("Section Recipes", site_md)
            agent_prompt = (target / "agent-prompt.md").read_text(encoding="utf-8")
            self.assertIn("Output Contract", agent_prompt)
            self.assertIn("Page Blueprint", agent_prompt)
            self.assertIn("site2voice bench", agent_prompt)
            self.assertIn("reference-only copy contract", agent_prompt)
            self.assertIn("Do not imply brand affiliation", agent_prompt)


if __name__ == "__main__":
    unittest.main()
