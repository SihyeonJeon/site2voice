from __future__ import annotations

import html
import json
import re
import statistics
import urllib.request
from collections import Counter
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

from . import __version__


TARGET_TAGS = {"title", "h1", "h2", "h3", "p", "a", "button", "li"}
SKIP_TAGS = {"script", "style", "noscript", "svg", "canvas"}
STOPWORDS = {
    "a",
    "about",
    "all",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "can",
    "for",
    "from",
    "get",
    "in",
    "into",
    "is",
    "it",
    "its",
    "more",
    "of",
    "on",
    "or",
    "our",
    "that",
    "the",
    "their",
    "to",
    "up",
    "use",
    "with",
    "you",
    "your",
    "그리고",
    "대한",
    "에서",
    "으로",
    "이다",
    "있는",
    "하는",
    "한다",
}
CTA_VERBS = {
    "book",
    "build",
    "buy",
    "contact",
    "create",
    "demo",
    "download",
    "explore",
    "get",
    "join",
    "learn",
    "request",
    "see",
    "sign",
    "start",
    "try",
    "watch",
    "구매",
    "만나",
    "보기",
    "살펴",
    "시작",
    "읽기",
    "지원",
    "확인",
}


@dataclass(frozen=True)
class TextItem:
    tag: str
    text: str


class CopyParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.skip_depth = 0
        self.stack: list[tuple[str, list[str]]] = []
        self.items: list[TextItem] = []
        self.meta_description = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag in SKIP_TAGS:
            self.skip_depth += 1
            return
        attr_map = {key.lower(): value or "" for key, value in attrs}
        if tag == "meta":
            name = attr_map.get("name", "").lower()
            prop = attr_map.get("property", "").lower()
            if name == "description" or prop == "og:description":
                self.meta_description = clean_text(attr_map.get("content", ""))
        if self.skip_depth == 0 and tag in TARGET_TAGS:
            self.stack.append((tag, []))

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in SKIP_TAGS and self.skip_depth:
            self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        for index in range(len(self.stack) - 1, -1, -1):
            active_tag, parts = self.stack[index]
            if active_tag == tag:
                text = clean_text(" ".join(parts))
                if text:
                    self.items.append(TextItem(active_tag, text))
                del self.stack[index:]
                return

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        text = clean_text(data)
        if not text:
            return
        for _, parts in self.stack:
            parts.append(text)


def clean_text(value: str) -> str:
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def read_source(source: str, timeout: float = 20.0) -> tuple[str, str]:
    if source.startswith(("http://", "https://")):
        request = urllib.request.Request(
            source,
            headers={"User-Agent": f"site2voice/{__version__} (+https://github.com/SihyeonJeon/site2voice)"},
        )
        with urllib.request.urlopen(request, timeout=timeout) as response:
            content_type = response.headers.get_content_charset() or "utf-8"
            return response.read().decode(content_type, errors="replace"), source
    path = Path(source).expanduser()
    return path.read_text(encoding="utf-8"), str(path)


def unique(values: list[str], limit: int) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for value in values:
        key = value.lower()
        if key in seen:
            continue
        seen.add(key)
        output.append(value)
        if len(output) >= limit:
            break
    return output


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z가-힣][A-Za-z0-9가-힣'-]*", text.lower())


def sentences(text: str) -> list[str]:
    return [item.strip() for item in re.split(r"[.!?。！？]+", text) if item.strip()]


def cta_score(text: str) -> bool:
    tokens = words(text)
    if not tokens or len(tokens) > 8:
        return False
    return tokens[0] in CTA_VERBS or any(token in CTA_VERBS for token in tokens[:2])


def tone_labels(avg_sentence_words: float, cta_count: int, lexicon: list[str]) -> list[str]:
    labels: list[str] = []
    if avg_sentence_words <= 10:
        labels.append("short and direct")
    elif avg_sentence_words >= 18:
        labels.append("explanatory")
    else:
        labels.append("balanced")
    if cta_count >= 4:
        labels.append("action-oriented")
    tech_terms = {"api", "agent", "code", "data", "deploy", "developer", "workflow", "tool"}
    trust_terms = {"secure", "security", "trusted", "compliance", "enterprise", "privacy"}
    lexicon_set = set(lexicon)
    if lexicon_set & tech_terms:
        labels.append("technical")
    if lexicon_set & trust_terms:
        labels.append("trust-forward")
    return labels


def average_word_count(values: list[str]) -> float:
    lengths = [len(words(value)) for value in values if words(value)]
    return round(statistics.mean(lengths), 1) if lengths else 0.0


def first_words(values: list[str], limit: int = 8) -> list[str]:
    output: list[str] = []
    for value in values:
        tokens = words(value)
        if not tokens:
            continue
        token = tokens[0]
        if token not in output:
            output.append(token)
        if len(output) >= limit:
            break
    return output


def punctuation_profile(text: str) -> dict[str, int]:
    return {
        "periods": text.count("."),
        "questions": text.count("?") + text.count("？"),
        "exclamations": text.count("!") + text.count("！"),
        "colons": text.count(":"),
    }


def metric_window(target: float, minimum_floor: float = 1.0) -> dict[str, float]:
    if target <= 0:
        return {"target": 0.0, "min": 0.0, "max": 0.0}
    return {
        "target": round(target, 1),
        "min": round(max(minimum_floor, target * 0.75), 1),
        "max": round(max(minimum_floor, target * 1.25), 1),
    }


def output_contract(metrics: dict[str, Any], lexicon: list[str], cta_verbs: list[str]) -> dict[str, Any]:
    return {
        "sentence_words": metric_window(float(metrics["avg_sentence_words"]), minimum_floor=4.0),
        "heading_words": metric_window(float(metrics["avg_heading_words"]), minimum_floor=1.0),
        "paragraph_words": metric_window(float(metrics["avg_paragraph_words"]), minimum_floor=4.0),
        "cta_words": metric_window(float(metrics["avg_cta_words"]), minimum_floor=1.0),
        "recommended_terms": lexicon[:12],
        "cta_verbs": cta_verbs,
        "minimum_recommended_terms": min(4, len(lexicon[:12])),
        "benchmark_gates": {
            "overall": 75,
            "copy_safety": 85,
            "claim_safety": 75,
        },
    }


def analyze(source: str, timeout: float = 20.0) -> dict[str, Any]:
    markup, resolved_source = read_source(source, timeout=timeout)
    parser = CopyParser()
    parser.feed(markup)

    title_items = [item.text for item in parser.items if item.tag == "title"]
    headings = unique([item.text for item in parser.items if item.tag in {"h1", "h2", "h3"}], 12)
    links = unique([item.text for item in parser.items if item.tag == "a" and 1 <= len(words(item.text)) <= 6], 16)
    buttons = unique([item.text for item in parser.items if item.tag == "button"], 12)
    ctas = unique([item.text for item in parser.items if item.tag in {"a", "button"} and cta_score(item.text)], 12)
    paragraphs = unique([item.text for item in parser.items if item.tag == "p"], 8)
    all_copy = " ".join(item.text for item in parser.items if item.tag != "title")
    all_words = words(all_copy)
    all_sentences = sentences(all_copy)
    sentence_lengths = [len(words(sentence)) for sentence in all_sentences]
    avg_sentence_words = statistics.mean(sentence_lengths) if sentence_lengths else 0.0
    lexicon = [
        word
        for word, _ in Counter(word for word in all_words if word not in STOPWORDS and len(word) >= 3).most_common(24)
    ]

    metrics = {
        "words": len(all_words),
        "sentences": len(all_sentences),
        "avg_sentence_words": round(avg_sentence_words, 1),
        "avg_heading_words": average_word_count(headings),
        "avg_paragraph_words": average_word_count(paragraphs),
        "avg_cta_words": average_word_count(ctas),
        "headings": len(headings),
        "ctas": len(ctas),
        "links": len(links),
        "type_token_ratio": round(len(set(all_words)) / len(all_words), 3) if all_words else 0.0,
    }
    cta_verbs = first_words(ctas)

    return {
        "schema_version": "site2voice.voice.v1",
        "generator": f"site2voice/{__version__}",
        "source": resolved_source,
        "title": title_items[-1] if title_items else "",
        "meta_description": parser.meta_description,
        "metrics": metrics,
        "tone": tone_labels(avg_sentence_words, len(ctas), lexicon),
        "style": {
            "cta_verbs": cta_verbs,
            "punctuation": punctuation_profile(all_copy),
        },
        "output_contract": output_contract(metrics, lexicon, cta_verbs),
        "headings": headings,
        "ctas": ctas,
        "links": links,
        "buttons": buttons,
        "lexicon": lexicon,
        "paragraph_samples": paragraphs,
    }


def to_markdown(payload: dict[str, Any], max_snippets: int = 8) -> str:
    metrics = payload["metrics"]
    contract = payload["output_contract"]
    sentence_words = contract["sentence_words"]
    heading_words = contract["heading_words"]
    paragraph_words = contract["paragraph_words"]
    cta_words = contract["cta_words"]
    gates = contract["benchmark_gates"]
    tone = ", ".join(payload["tone"]) if payload["tone"] else "not enough copy"
    preferred_terms = ", ".join(f"`{term}`" for term in payload["lexicon"][:12]) or "None detected"
    cta_terms = ", ".join(f"`{item}`" for item in payload["ctas"][:8]) or "None detected"
    nav_terms = ", ".join(f"`{item}`" for item in payload["links"][:10]) or "None detected"
    contract_terms = ", ".join(f"`{term}`" for term in contract["recommended_terms"]) or "None detected"
    contract_verbs = ", ".join(f"`{item}`" for item in contract["cta_verbs"]) or "the observed CTA verbs"

    lines = [
        "# VOICE.md",
        "",
        f"Source: `{payload['source']}`",
        "",
        "Use this file to keep AI-generated pages, docs, and UI copy aligned with the observed website voice.",
        "",
        "## Voice Summary",
        "",
        f"- Overall tone: **{tone}**.",
        f"- Sentence shape: about **{metrics['avg_sentence_words']} words** per sentence.",
        f"- Main vocabulary: {preferred_terms}.",
        f"- Common CTAs: {cta_terms}.",
        f"- Navigation labels: {nav_terms}.",
        "",
        "## Style Fingerprint",
        "",
        f"- Heading shape: about **{metrics['avg_heading_words']} words** per heading.",
        f"- Paragraph rhythm: about **{metrics['avg_paragraph_words']} words** per paragraph sample.",
        f"- CTA shape: about **{metrics['avg_cta_words']} words** per CTA.",
        f"- CTA verbs: {', '.join(f'`{item}`' for item in payload['style']['cta_verbs']) or 'None detected'}.",
        f"- Lexical variety: **{metrics['type_token_ratio']}** type-token ratio.",
        "",
        "## Agent Rules",
        "",
        "- Start with a concrete user outcome before describing implementation details.",
        "- Prefer short active sentences and visible verbs from the CTA list.",
        "- Reuse the observed vocabulary, but do not copy full marketing paragraphs.",
        "- Keep headings specific; avoid generic labels like `Powerful features` unless the source uses that pattern.",
        "- When adding new sections, match the observed information order: headline, proof, action, details.",
        "- Do not invent compliance, security, customer, or performance claims that are not present in the source.",
        "",
        "## Output Contract",
        "",
        f"- Keep average sentence length between **{sentence_words['min']} and {sentence_words['max']} words**.",
        f"- Keep headings near **{heading_words['target']} words**; avoid generic one-word section labels unless the source uses them.",
        f"- Keep paragraph blocks near **{paragraph_words['target']} words**.",
        f"- Keep CTAs near **{cta_words['target']} words** and start them with: {contract_verbs}.",
        f"- Use at least **{contract['minimum_recommended_terms']}** of these terms where natural: {contract_terms}.",
        "- Keep the first screen structure close to: specific headline, short proof/value sentence, one or two action CTAs.",
        "- If writing a candidate file, run:",
        f"  `site2voice bench {payload['source']} path/to/candidate.md --strict`",
        f"- Revise until overall >= **{gates['overall']}**, copy safety >= **{gates['copy_safety']}**, and claim safety >= **{gates['claim_safety']}**.",
    ]
    if max_snippets > 0:
        lines.extend(["", "## Page Pattern", ""])
        if payload["headings"]:
            lines.extend(f"- Heading: {trim_snippet(item)}" for item in payload["headings"][:max_snippets])
        else:
            lines.append("- No headings detected.")
    lines.extend(
        [
            "",
            "## Evidence",
            "",
            "| Signal | Value |",
            "| --- | --- |",
            f"| Words | {metrics['words']} |",
            f"| Sentences | {metrics['sentences']} |",
            f"| Headings | {metrics['headings']} |",
            f"| CTA candidates | {metrics['ctas']} |",
            "",
        ]
    )
    samples = payload["paragraph_samples"][:max_snippets]
    if samples:
        lines.extend(["## Short Copy Samples", ""])
        lines.extend(f"- {trim_snippet(item)}" for item in samples)
        lines.append("")
    lines.extend(
        [
            "## Do / Don't",
            "",
            "- Do: write concise, outcome-first copy using the observed verbs and nouns.",
            "- Do: keep CTAs short and action-led.",
            "- Don't: paste source paragraphs verbatim.",
            "- Don't: add claims the source did not support.",
            "",
        ]
    )
    return "\n".join(lines)


def trim_snippet(value: str, limit: int = 96) -> str:
    value = clean_text(value)
    if len(value) <= limit:
        return value
    clipped = value[: limit - 1].rsplit(" ", 1)[0].rstrip()
    return (clipped or value[: limit - 1].rstrip()) + "…"


def to_json(payload: dict[str, Any]) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
