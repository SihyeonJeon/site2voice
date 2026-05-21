from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

from site2voice.benchmark import score_candidate
from site2voice.extract import clean_text, cta_score, words


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.skip_depth = 0
        self.current_tag = ""
        self.current_attrs: dict[str, str] = {}
        self.text_parts: list[str] = []
        self.headings: list[str] = []
        self.ctas: list[str] = []
        self.tags: list[str] = []
        self.sections = 0
        self.explicit_slots: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "svg", "canvas"}:
            self.skip_depth += 1
            return
        attr_map = {key.lower(): value or "" for key, value in attrs}
        self.current_tag = tag
        self.current_attrs = attr_map
        self.tags.append(tag)
        if tag == "section":
            self.sections += 1
        slot = attr_map.get("data-slot", "")
        if slot and slot not in self.explicit_slots:
            self.explicit_slots.append(slot)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "svg", "canvas"} and self.skip_depth:
            self.skip_depth -= 1
        self.current_tag = ""
        self.current_attrs = {}

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        text = clean_text(data)
        if not text:
            return
        self.text_parts.append(text)
        if self.current_tag in {"h1", "h2", "h3"}:
            self.headings.append(text)
        if self.current_tag in {"a", "button"} and cta_score(text):
            self.ctas.append(text)


def parse_page(path: Path) -> dict[str, Any]:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    text = clean_text(" ".join(parser.text_parts))
    link_like = sum(1 for tag in parser.tags if tag == "a")
    return {
        "path": str(path),
        "text": text,
        "words": len(words(text)),
        "headings": parser.headings,
        "ctas": parser.ctas,
        "links": link_like,
        "tags": parser.tags,
        "sections": parser.sections,
        "explicit_slots": parser.explicit_slots,
    }


def label_density(word_count: int, headings: int, links: int) -> str:
    score = word_count + headings * 28 + links * 10
    if score >= 1600:
        return "dense"
    if score >= 650:
        return "balanced"
    return "compact"


def label_conversion(ctas: int, links: int) -> str:
    score = ctas * 1.4 + min(links, 16) * 0.2
    if score >= 10:
        return "high"
    if score >= 4:
        return "medium"
    return "low"


def nav_model(links: int) -> str:
    if links >= 12:
        return "broad utility navigation"
    if links >= 5:
        return "focused product navigation"
    return "minimal navigation"


def infer_slots(page: dict[str, Any]) -> list[str]:
    if page["explicit_slots"]:
        return page["explicit_slots"]
    text = page["text"].lower()
    tags = set(page["tags"])
    slots: list[str] = []
    if "nav" in tags:
        slots.append("navigation")
    if page["headings"]:
        slots.append("first_screen")
    if re.search(r"\b(api|event|ledger|payment|workflow|trace|reconcile|alert|query|observability)\b", text):
        slots.append("capability_stack")
    if re.search(r"\b(proof|review|audit|metric|evidence|close|operator|constraint)\b", text):
        slots.append("proof_band")
    if page["sections"] >= 5 or re.search(r"\b(workflow|detail|integration|investigate|export)\b", text):
        slots.append("detail_sections")
    if len(page["ctas"]) >= 4 or re.search(r"\b(start|contact|get|create|demo)\b", text):
        slots.append("conversion_band")
    if "footer" in tags:
        slots.append("footer")
    return unique(slots)


def unique(values: list[str]) -> list[str]:
    output: list[str] = []
    for value in values:
        if value not in output:
            output.append(value)
    return output


def lcs_length(left: list[str], right: list[str]) -> int:
    previous = [0] * (len(right) + 1)
    for left_item in left:
        current = [0] * (len(right) + 1)
        for index, right_item in enumerate(right, start=1):
            if left_item == right_item:
                current[index] = previous[index - 1] + 1
            else:
                current[index] = max(previous[index], current[index - 1])
        previous = current
    return previous[-1]


def categorical_fit(expected: str, observed: str, ordered: list[str]) -> float:
    if expected == observed:
        return 1.0
    if expected in ordered and observed in ordered:
        distance = abs(ordered.index(expected) - ordered.index(observed))
        return max(0.25, 1.0 - distance * 0.35)
    return 0.4


def structure_score(site_profile: dict[str, Any], page: dict[str, Any]) -> dict[str, Any]:
    expected_slots = [item["slot"] for item in site_profile["page_blueprint"]]
    observed_slots = infer_slots(page)
    expected_set = set(expected_slots)
    observed_set = set(observed_slots)
    coverage = len(expected_set & observed_set) / max(1, len(expected_set))
    order = lcs_length(expected_slots, observed_slots) / max(1, len(expected_slots))
    observed_density = label_density(page["words"], len(page["headings"]), page["links"])
    observed_conversion = label_conversion(len(page["ctas"]), page["links"])
    observed_nav = nav_model(page["links"])
    summary = site_profile["site_summary"]
    density_fit = categorical_fit(summary["information_density"], observed_density, ["compact", "balanced", "dense"])
    conversion_fit = categorical_fit(summary["conversion_pressure"], observed_conversion, ["low", "medium", "high"])
    nav_fit = 1.0 if summary["navigation_model"] == observed_nav else 0.55
    score = coverage * 42 + order * 28 + density_fit * 12 + conversion_fit * 10 + nav_fit * 8
    return {
        "score": round(score, 1),
        "slot_coverage": round(coverage * 100, 1),
        "slot_order": round(order * 100, 1),
        "density_fit": round(density_fit * 100, 1),
        "conversion_fit": round(conversion_fit * 100, 1),
        "navigation_fit": round(nav_fit * 100, 1),
        "observed_slots": observed_slots,
        "observed_density": observed_density,
        "observed_conversion": observed_conversion,
        "observed_navigation": observed_nav,
    }


def score_page(voice_profile: dict[str, Any], site_profile: dict[str, Any], path: Path) -> dict[str, Any]:
    page = parse_page(path)
    candidate_text = "\n".join(
        [
            *(f"## {heading}" for heading in page["headings"]),
            *page["ctas"],
            page["text"],
        ]
    )
    voice = score_candidate(voice_profile, candidate_text, path.stem)
    structure = structure_score(site_profile, page)
    voice_score = float(voice["score"])
    copy_safety = float(voice["scores"]["copy_safety"])
    claim_safety = float(voice["scores"]["claim_safety"])
    reference_fit = structure["score"] * 0.45 + voice_score * 0.45 + copy_safety * 0.05 + claim_safety * 0.05
    mimic_risk = max(0.0, 100.0 - copy_safety)
    return {
        "label": path.stem,
        "path": str(path),
        "reference_fit": round(reference_fit, 1),
        "structure_fit": structure,
        "voice_fit": voice,
        "mimic_risk": round(mimic_risk, 1),
        "page_metrics": {
            "words": page["words"],
            "headings": len(page["headings"]),
            "ctas": len(page["ctas"]),
            "links": page["links"],
            "sections": page["sections"],
        },
    }


def build_payload(voice_path: Path, site_path: Path, candidates: list[Path]) -> dict[str, Any]:
    voice_profile = json.loads(voice_path.read_text(encoding="utf-8"))
    site_profile = json.loads(site_path.read_text(encoding="utf-8"))
    return {
        "schema_version": "site2voice.reference_fit.v1",
        "reference": {
            "voice": str(voice_path),
            "site": str(site_path),
            "source": voice_profile.get("source", site_profile.get("source", "")),
            "page_archetype": site_profile["site_summary"]["page_archetype"],
        },
        "scoring": {
            "reference_fit": "45% structure fit + 45% voice fit + 5% copy safety + 5% claim safety",
            "mimic_risk": "100 - copy safety. Keep this low; reference fit should not reward copying.",
        },
        "candidates": [score_page(voice_profile, site_profile, path) for path in candidates],
    }


def markdown_report(payload: dict[str, Any]) -> str:
    lines = [
        "# Web Output Reference Fit",
        "",
        f"Reference source: `{payload['reference']['source']}`",
        f"Reference archetype: **{payload['reference']['page_archetype']}**",
        "",
        "This report compares visible web outputs against the same reference context.",
        "`Reference fit` rewards safe structural and copy alignment. `Mimic risk` should stay low.",
        "",
        "## Scores",
        "",
        "| Candidate | Reference fit | Structure | Voice | Copy safety | Claim safety | Mimic risk | Observed slots |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for item in payload["candidates"]:
        voice_scores = item["voice_fit"]["scores"]
        slots = ", ".join(f"`{slot}`" for slot in item["structure_fit"]["observed_slots"])
        lines.append(
            f"| [{item['label']}]({Path(item['path']).name}) | {item['reference_fit']:.1f} | "
            f"{item['structure_fit']['score']:.1f} | {item['voice_fit']['score']:.1f} | "
            f"{voice_scores['copy_safety']:.1f} | {voice_scores['claim_safety']:.1f} | "
            f"{item['mimic_risk']:.1f} | {slots} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- `with-site-voice` should score higher on structure and voice because the same prompt receives `SITE.md` and `VOICE.md` as context.",
            "- `without-context` can still look polished, but it is more likely to use generic SaaS layout, generic proof, and unsupported claims.",
            "- A high reference-fit score is only useful when copy safety and claim safety remain high.",
            "",
        ]
    )
    return "\n".join(lines)


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
