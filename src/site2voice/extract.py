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
    "open",
    "read",
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


def sentence_units(values: list[str]) -> list[str]:
    units: list[str] = []
    for value in values:
        for part in sentences(value):
            count = len(words(part))
            if 2 <= count <= 60:
                units.append(part)
    return units


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
        token = next((item for item in tokens[:2] if item in CTA_VERBS), "")
        if not token:
            continue
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
        "recommended_terms": [],
        "source_terms": lexicon[:12],
        "cta_verbs": cta_verbs,
        "minimum_recommended_terms": 0,
        "content_rule": (
            "Use only the new project's nouns, facts, audience, offer, and domain. "
            "Do not transfer source-specific products, categories, slogans, people, campaigns, or topics."
        ),
        "domain_firewall": {
            "reference_supplies": [
                "sentence rhythm",
                "heading shape",
                "CTA shape",
                "section order",
                "rhetorical moves",
            ],
            "design_md_supplies": [
                "colors",
                "typography",
                "spacing",
                "layout grid",
                "components",
                "motion",
                "visual assets",
            ],
            "project_must_supply": [
                "product category",
                "audience",
                "domain nouns",
                "offer",
                "proof",
                "claims",
                "examples",
                "visual subject matter",
            ],
            "rule": "If a noun, claim, or scenario is not in the new project brief, remove it even if it appears in the reference source.",
        },
        "benchmark_gates": {
            "overall": 75,
            "copy_safety": 85,
            "claim_safety": 75,
        },
    }


def density_label(metrics: dict[str, Any]) -> str:
    structural_score = int(metrics["words"]) + int(metrics["headings"]) * 28 + int(metrics["links"]) * 10
    if structural_score >= 1600:
        return "dense"
    if structural_score >= 650:
        return "balanced"
    return "compact"


def conversion_pressure(metrics: dict[str, Any]) -> str:
    ctas = int(metrics["ctas"])
    links = int(metrics["links"])
    score = ctas * 1.4 + min(links, 16) * 0.2
    if score >= 10:
        return "high"
    if score >= 4:
        return "medium"
    return "low"


def navigation_model(metrics: dict[str, Any]) -> str:
    links = int(metrics["links"])
    if links >= 12:
        return "broad utility navigation"
    if links >= 5:
        return "focused product navigation"
    return "minimal navigation"


def archetype_from_hint(hint: str | None) -> str | None:
    if not hint:
        return None
    value = hint.lower()
    if any(term in value for term in ["streetwear", "fashion", "media", "magazine", "editorial", "culture media"]):
        return "editorial index"
    if any(term in value for term in ["streaming", "audio"]):
        return "subscription landing"
    if any(term in value for term in ["infrastructure", "developer", "technology", "ai research", "browser", "privacy"]):
        return "technical product landing"
    if any(term in value for term in ["visual discovery"]):
        return "community platform landing"
    if any(term in value for term in ["commerce", "merchant", "payments", "financial"]):
        return "commerce journey"
    if any(term in value for term in ["real estate", "marketplace"]):
        return "marketplace landing"
    if any(term in value for term in ["community", "network", "messaging", "video platform", "gaming"]):
        return "community platform landing"
    if any(term in value for term in ["productivity", "collaboration", "communication", "workspace", "design platform"]):
        return "product landing"
    if any(term in value for term in ["hardware", "electronics"]):
        return "product landing"
    return None


def page_archetype(payload: dict[str, Any], category_hint: str | None = None) -> str:
    hinted = archetype_from_hint(category_hint)
    if hinted:
        return hinted
    lexicon = set(payload.get("lexicon", []))
    tone = set(payload.get("tone", []))
    archetypes = [
        (
            {"article", "articles", "culture", "editorial", "fashion", "latest", "magazine", "news", "stories"},
            "editorial index",
        ),
        (
            {"movie", "music", "premium", "show", "shows", "stream", "streaming", "subscribe", "subscription", "video"},
            "subscription landing",
        ),
        (
            {"buy", "cart", "commerce", "merchant", "order", "payment", "payments", "shop", "store"},
            "commerce journey",
        ),
        (
            {"community", "conversation", "creator", "message", "network", "people", "social", "together"},
            "community platform landing",
        ),
        (
            {"api", "app", "code", "data", "deploy", "developer", "model", "platform", "workflow"},
            "technical product landing",
        ),
        (
            {"career", "company", "hiring", "job", "jobs", "professional", "team", "work"},
            "professional product landing",
        ),
        (
            {"home", "loan", "market", "mortgage", "property", "real", "rent", "seller"},
            "marketplace landing",
        ),
    ]
    for terms, label in archetypes:
        if lexicon & terms:
            return label
    if "technical" in tone:
        return "technical product landing"
    if "action-oriented" in tone:
        return "conversion landing"
    return "product landing"


def core_section_slot(archetype: str) -> dict[str, str]:
    if archetype == "editorial index":
        return {
            "slot": "feed_index",
            "goal": "Turn many topics into a scannable editorial path.",
            "copy_shape": "Short section labels, compact summaries, clear onward links.",
            "agent_rule": "Use the structure for topic grouping only; bring new subjects and article angles.",
        }
    if archetype == "technical product landing":
        return {
            "slot": "capability_stack",
            "goal": "Move from outcome to workflow, proof, and implementation detail.",
            "copy_shape": "Outcome heading, concrete capability sentence, concise action link.",
            "agent_rule": "Explain the new product's actual mechanics; do not borrow platform claims.",
        }
    if archetype in {"commerce journey", "marketplace landing"}:
        return {
            "slot": "decision_path",
            "goal": "Help the reader compare, trust, and choose the next action.",
            "copy_shape": "Benefit-led heading, practical constraint, short action.",
            "agent_rule": "Use only the new offer, price, availability, and trust claims.",
        }
    if archetype == "subscription landing":
        return {
            "slot": "offer_stack",
            "goal": "Convert attention into subscription understanding.",
            "copy_shape": "Offer heading, short value sentence, plan or catalog proof.",
            "agent_rule": "Replace all catalog, plan, and availability details with owned facts.",
        }
    if archetype == "community platform landing":
        return {
            "slot": "participation_path",
            "goal": "Show who joins, what they do, and why they return.",
            "copy_shape": "People-first heading, one behavior sentence, one join action.",
            "agent_rule": "Use the new community's real audience and participation model.",
        }
    return {
        "slot": "core_value_sections",
        "goal": "Explain the product through repeated value, proof, and action blocks.",
        "copy_shape": "Specific heading, short proof sentence, compact CTA.",
        "agent_rule": "Keep each section tied to a real product capability.",
    }


def site_sections(payload: dict[str, Any], category_hint: str | None = None) -> list[dict[str, str]]:
    metrics = payload["metrics"]
    density = density_label(metrics)
    pressure = conversion_pressure(metrics)
    archetype = page_archetype(payload, category_hint=category_hint)

    sections = [
        {
            "slot": "navigation",
            "goal": "Orient the reader before the first claim.",
            "copy_shape": "Use short noun-led labels; keep utility paths separate from product paths.",
            "agent_rule": "Use navigation categories from the new product, not the reference source.",
        },
        {
            "slot": "first_screen",
            "goal": "State the main outcome and give a visible next action.",
            "copy_shape": "Specific headline, one compact value sentence, and one or two action CTAs.",
            "agent_rule": "Name the new outcome plainly before explaining features.",
        },
        core_section_slot(archetype),
        {
            "slot": "proof_band",
            "goal": "Make the promise believable without overclaiming.",
            "copy_shape": "Use concrete evidence blocks: metric, customer type, workflow step, or product constraint.",
            "agent_rule": "Only include proof that the new project can independently support.",
        },
    ]
    if density != "compact":
        sections.append(
            {
                "slot": "detail_sections",
                "goal": "Give deeper readers enough structure to evaluate fit.",
                "copy_shape": "Alternate short headings with one-paragraph explanations and compact lists.",
                "agent_rule": "Split detail by user job, workflow step, or decision criterion.",
            }
        )
    if pressure != "low":
        sections.append(
            {
                "slot": "conversion_band",
                "goal": "Repeat the next action after value and proof are established.",
                "copy_shape": "Short reminder sentence plus one primary action CTA.",
                "agent_rule": "Repeat the real conversion action; do not add urgency unless it is true.",
            }
        )
    sections.append(
        {
            "slot": "footer",
            "goal": "Close with utility, trust, and legal/support paths.",
            "copy_shape": "Grouped utility links with short labels and no marketing prose.",
            "agent_rule": "Use owned support, policy, company, and resource links.",
        }
    )
    return sections


def site_contract(payload: dict[str, Any], category_hint: str | None = None) -> dict[str, Any]:
    metrics = payload["metrics"]
    contract = payload["output_contract"]
    archetype = page_archetype(payload, category_hint=category_hint)
    density = density_label(metrics)
    pressure = conversion_pressure(metrics)
    sections = site_sections(payload, category_hint=category_hint)
    return {
        "schema_version": "site2voice.site.v1",
        "generator": f"site2voice/{__version__}",
        "source": payload["source"],
        "site_summary": {
            "page_archetype": archetype,
            "information_density": density,
            "conversion_pressure": pressure,
            "navigation_model": navigation_model(metrics),
            "content_boundary": (
                "Structure and copy shape only. Bring new project nouns, facts, claims, audience, domain, and offers."
            ),
        },
        "structure_metrics": {
            "words": metrics["words"],
            "headings": metrics["headings"],
            "ctas": metrics["ctas"],
            "links": metrics["links"],
            "avg_heading_words": metrics["avg_heading_words"],
            "avg_paragraph_words": metrics["avg_paragraph_words"],
            "avg_cta_words": metrics["avg_cta_words"],
            "avg_link_words": metrics.get("avg_link_words", 0.0),
        },
        "measurement_note": "Numeric ranges are drift checks for benchmarking, not the primary writing method.",
        "target_ranges": {
            "heading_words": contract["heading_words"],
            "paragraph_words": contract["paragraph_words"],
            "cta_words": contract["cta_words"],
        },
        "page_blueprint": [
            {
                "order": index,
                "slot": section["slot"],
                "goal": section["goal"],
                "copy_shape": section["copy_shape"],
            }
            for index, section in enumerate(sections, start=1)
        ],
        "section_recipes": sections,
        "agent_instructions": [
            "Use SITE.md for page structure and section order.",
            "Use VOICE.md for sentence rhythm, CTA shape, and benchmark gates.",
            "Treat the new project brief as the only source of product category, audience, domain nouns, examples, offers, and claims.",
            "Replace every topic, product noun, market claim, price, and proof point with facts from the new project.",
            "Do not imply affiliation with, endorsement from, or official representation of the reference source.",
            "If a needed fact is missing, write a neutral placeholder or remove the claim.",
        ],
        "anti_patterns": [
            "Do not copy source headings, CTA labels, navigation labels, slogans, or campaign names.",
            "Do not import the reference site's product catalog, category, audience, pricing, legal claims, feature names, people, events, or cultural context.",
            "Do not turn structure guidance into a visual design system.",
            "Do not add urgency, security, performance, customer, or compliance claims without evidence.",
        ],
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
    paragraph_blocks = [item.text for item in parser.items if item.tag == "p"]
    all_sentences = sentence_units(paragraph_blocks)
    if len(all_sentences) < 3:
        natural_blocks = [item.text for item in parser.items if item.tag in {"h1", "h2", "h3", "p", "li"}]
        all_sentences = sentence_units(natural_blocks)
    if len(all_sentences) < 3:
        all_sentences = sentence_units([item.text for item in parser.items if item.tag != "title"])
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
        "avg_link_words": average_word_count(links),
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


def to_markdown(payload: dict[str, Any], max_snippets: int = 0) -> str:
    metrics = payload["metrics"]
    contract = payload["output_contract"]
    sentence_words = contract["sentence_words"]
    heading_words = contract["heading_words"]
    paragraph_words = contract["paragraph_words"]
    cta_words = contract["cta_words"]
    gates = contract["benchmark_gates"]
    tone = ", ".join(payload["tone"]) if payload["tone"] else "not enough copy"
    contract_verbs = ", ".join(f"`{item}`" for item in contract["cta_verbs"]) or "the observed CTA verbs"
    content_rule = contract.get(
        "content_rule",
        "Use only the new project's nouns. Do not transfer source-specific terms from the reference site.",
    )

    lines = [
        "# VOICE.md",
        "",
        f"Reference source: `{payload['source']}`",
        "",
        "Use this file as a reference-only copy profile for AI-generated pages, docs, and UI microcopy.",
        "",
        "## Voice Summary",
        "",
        f"- Overall tone: **{tone}**.",
        "- Copy method: follow the rhetorical moves, section behavior, CTA pattern, and claim boundaries below.",
        "- Measurement policy: word ranges are benchmark drift checks, not the main writing method.",
        "- Content policy: this file captures rhythm and structure, not source nouns.",
        "- Brand policy: this is not an official guideline, endorsement, or permission to impersonate the reference source.",
        "",
        "## Scope",
        "",
        "- Reuse measurable writing patterns: sentence rhythm, heading shape, CTA verb shape, paragraph rhythm, and information order.",
        "- Bring your own product names, topics, audience, claims, examples, and domain nouns.",
        "- Do not use trademarks, logos, proprietary product names, or brand claims unless you already have independent rights to use them.",
        "- Do not infer the new project's product category from the reference site.",
        "- Do not use this file for colors, fonts, spacing, components, animation, imagery, or responsive layout.",
        "",
        "## Context Stack",
        "",
        "- Project brief owns: product category, audience, facts, domain nouns, examples, offers, and claims.",
        "- `DESIGN.md` owns: colors, typography, spacing, layout grid, visual components, motion, and imagery style.",
        "- `SITE.md` owns: page structure, section order, section jobs, and conversion path.",
        "- `VOICE.md` owns: sentence rhythm, heading behavior, CTA shape, and claim boundaries.",
        "- If files conflict, do not merge responsibilities; use the owner above.",
        "",
        "## Domain Firewall",
        "",
        "- Reference supplies: rhythm, heading shape, CTA shape, section behavior, and rhetorical moves.",
        "- New project supplies: category, audience, domain nouns, examples, offer, claims, proof, and visual subject matter.",
        "- If a noun or scenario is not in the new project brief, remove it even if it appears in the reference source.",
        "- Example: when using a retail reference for an education product, keep all nouns, examples, proof, and CTAs educational.",
        "",
        "## Writing Moves",
        "",
        "- First screen: start with a concrete user outcome, then add one short proof/value sentence.",
        "- Heading move: make headings specific enough to stand alone in a scan.",
        "- Body move: explain one idea per paragraph; do not stack unrelated claims.",
        "- CTA move: use visible action verbs and keep the next step unambiguous.",
        "- Claim move: prefer supported product behavior over broad market promises.",
        "",
        "## Style Fingerprint",
        "",
        "Use these numbers as calibration checks after drafting.",
        "",
        f"- Heading shape: about **{metrics['avg_heading_words']} words** per heading.",
        f"- Paragraph rhythm: about **{metrics['avg_paragraph_words']} words** per paragraph sample.",
        f"- CTA shape: about **{metrics['avg_cta_words']} words** per CTA.",
        f"- CTA verbs: {', '.join(f'`{item}`' for item in payload['style']['cta_verbs']) or 'None detected'}.",
        f"- Navigation label shape: about **{metrics.get('avg_link_words', 0.0)} words** per label.",
        f"- Lexical variety: **{metrics['type_token_ratio']}** type-token ratio.",
        "",
        "## Agent Rules",
        "",
        "- Start with a concrete user outcome before describing implementation details.",
        "- Prefer short active sentences and visible verbs from the CTA list.",
        "- Reuse rhythm, CTA shape, and information order; bring your own product nouns.",
        "- Do not import source-specific topics, product names, market claims, audience assumptions, or domain nouns.",
        "- Defer all visual decisions to `DESIGN.md` when it is present.",
        "- Do not imply affiliation with, approval from, or official representation of the reference source.",
        "- Keep headings specific; avoid generic labels like `<generic feature label>` unless the source uses that pattern.",
        "- When adding new sections, match the observed information order: headline, proof, action, details.",
        "- Do not invent compliance, security, customer, or performance claims that are not present in the source.",
        "",
        "## Output Contract",
        "",
        f"- Benchmark drift check: keep average sentence length between **{sentence_words['min']} and {sentence_words['max']} words**.",
        f"- Keep headings near **{heading_words['target']} words**; avoid generic one-word section labels unless the source uses them.",
        f"- Keep paragraph blocks near **{paragraph_words['target']} words**.",
        f"- Keep CTAs near **{cta_words['target']} words** and start them with: {contract_verbs}.",
        f"- Content boundary: {content_rule}",
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
            "- Do: write concise, outcome-first copy using the observed rhythm and CTA verbs.",
            "- Do: keep CTAs short and action-led.",
            "- Don't: transfer source-specific nouns into an unrelated project.",
            "- Don't: present the result as official brand copy or a brand guideline.",
            "- Don't: paste source paragraphs verbatim.",
            "- Don't: add claims the source did not support.",
            "",
        ]
    )
    return "\n".join(lines)


def to_site_markdown(payload: dict[str, Any], category_hint: str | None = None) -> str:
    contract = site_contract(payload, category_hint=category_hint)
    summary = contract["site_summary"]
    metrics = contract["structure_metrics"]
    ranges = contract["target_ranges"]
    blueprint = contract["page_blueprint"]
    recipes = contract["section_recipes"]

    lines = [
        "# SITE.md",
        "",
        f"Reference source: `{payload['source']}`",
        "",
        "Use this file as a reference-only page-structure contract for AI-generated websites.",
        "",
        "Pair it with `VOICE.md`: `SITE.md` controls section order and page intent; `VOICE.md` controls copy rhythm, CTA shape, and benchmark gates.",
        "If a `DESIGN.md` file is present, it controls colors, typography, spacing, components, motion, and responsive layout.",
        "",
        "## Site Summary",
        "",
        f"- Page archetype: **{summary['page_archetype']}**.",
        f"- Information density: **{summary['information_density']}**.",
        f"- Conversion pressure: **{summary['conversion_pressure']}**.",
        f"- Navigation model: **{summary['navigation_model']}**.",
        f"- Content boundary: {summary['content_boundary']}",
        "- Brand policy: this is not an official guideline, endorsement, or permission to impersonate the reference source.",
        "",
        "## Page Blueprint",
        "",
        "| Order | Slot | Purpose |",
        "| ---: | --- | --- |",
    ]
    for item in blueprint:
        lines.append(f"| {item['order']} | `{item['slot']}` | {item['goal']} |")

    lines.extend(
        [
            "",
            "## Section Recipes",
            "",
            "| Slot | Copy Shape | Agent Rule |",
            "| --- | --- | --- |",
        ]
    )
    for recipe in recipes:
        lines.append(f"| `{recipe['slot']}` | {recipe['copy_shape']} | {recipe['agent_rule']} |")

    lines.extend(
        [
        "",
        "## Rhetorical Pattern",
            "",
            "- Opening move: name the reader outcome before listing mechanics.",
            "- Section rhythm: move from value, to proof, to action, then to detail only when needed.",
        "- Proof move: use real product behavior, customer evidence, constraints, or measurable facts.",
        "- CTA move: repeat one primary next action after the reader has enough context.",
        "- Density move: keep compact pages decisive; make dense pages scannable with clear section jobs.",
        "",
        "## Context Stack",
        "",
        "- Project brief owns: product category, audience, facts, domain nouns, examples, offers, and claims.",
        "- `DESIGN.md` owns: colors, typography, spacing, layout grid, visual components, motion, and imagery style.",
        "- `SITE.md` owns: page structure, section order, section jobs, and conversion path.",
        "- `VOICE.md` owns: sentence rhythm, heading behavior, CTA shape, and claim boundaries.",
        "- If files conflict, do not merge responsibilities; use the owner above.",
        "",
        "## Domain Firewall",
        "",
        "- Reference supplies: page architecture, section order, density, conversion pressure, and section jobs.",
        "- New project supplies: product category, user domain, audience, examples, proof, imagery, and offer.",
        "- `DESIGN.md` supplies all visual identity and component decisions; this file does not supply colors, fonts, spacing, animation, or components.",
        "- Do not let the reference site's business, catalog, cultural context, or customer scenario become the new site's subject.",
        "- If using a retail reference for an education product, the output must stay educational in nouns, examples, proof, and CTAs.",
        "",
        "## Agent Instructions",
        "",
        ]
    )
    lines.extend(f"- {item}" for item in contract["agent_instructions"])
    lines.extend(
        [
            "",
            "## Content Boundary",
            "",
        ]
    )
    lines.extend(f"- {item}" for item in contract["anti_patterns"])
    lines.extend(
        [
            "",
            "## Measurement",
            "",
            "These numbers are drift checks for benchmarking, not the main writing method.",
            "",
            "| Signal | Value |",
            "| --- | ---: |",
            f"| Words measured | {metrics['words']} |",
            f"| Headings measured | {metrics['headings']} |",
            f"| CTA candidates measured | {metrics['ctas']} |",
            f"| Link labels measured | {metrics['links']} |",
            f"| Heading word target | {ranges['heading_words']['target']} |",
            f"| Paragraph word target | {ranges['paragraph_words']['target']} |",
            f"| CTA word target | {ranges['cta_words']['target']} |",
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


def to_site_json(payload: dict[str, Any], category_hint: str | None = None) -> str:
    return json.dumps(site_contract(payload, category_hint=category_hint), ensure_ascii=False, indent=2) + "\n"
