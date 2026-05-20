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
            headers={"User-Agent": "site2voice/0.1 (+https://github.com/SihyeonJeon/site2voice)"},
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
    return re.findall(r"[A-Za-z][A-Za-z0-9'-]*", text.lower())


def sentences(text: str) -> list[str]:
    return [item.strip() for item in re.split(r"[.!?]+", text) if item.strip()]


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

    return {
        "source": resolved_source,
        "title": title_items[-1] if title_items else "",
        "meta_description": parser.meta_description,
        "metrics": {
            "words": len(all_words),
            "sentences": len(all_sentences),
            "avg_sentence_words": round(avg_sentence_words, 1),
            "headings": len(headings),
            "ctas": len(ctas),
            "links": len(links),
        },
        "tone": tone_labels(avg_sentence_words, len(ctas), lexicon),
        "headings": headings,
        "ctas": ctas,
        "links": links,
        "buttons": buttons,
        "lexicon": lexicon,
        "paragraph_samples": paragraphs,
    }


def to_markdown(payload: dict[str, Any], max_snippets: int = 8) -> str:
    metrics = payload["metrics"]
    tone = ", ".join(payload["tone"]) if payload["tone"] else "not enough copy"
    preferred_terms = ", ".join(f"`{term}`" for term in payload["lexicon"][:12]) or "None detected"
    cta_terms = ", ".join(f"`{item}`" for item in payload["ctas"][:8]) or "None detected"
    nav_terms = ", ".join(f"`{item}`" for item in payload["links"][:10]) or "None detected"

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
        "## Agent Rules",
        "",
        "- Start with a concrete user outcome before describing implementation details.",
        "- Prefer short active sentences and visible verbs from the CTA list.",
        "- Reuse the observed vocabulary, but do not copy full marketing paragraphs.",
        "- Keep headings specific; avoid generic labels like `Powerful features` unless the source uses that pattern.",
        "- When adding new sections, match the observed information order: headline, proof, action, details.",
        "- Do not invent compliance, security, customer, or performance claims that are not present in the source.",
        "",
        "## Page Pattern",
        "",
    ]
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
