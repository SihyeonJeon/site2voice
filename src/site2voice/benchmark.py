from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .extract import STOPWORDS, analyze, clean_text, cta_score, sentences, tone_labels, trim_snippet, words


DEFAULT_PASS_SCORE = 75.0
DEFAULT_COPY_SAFETY = 85.0
DEFAULT_CLAIM_SAFETY = 75.0
MAX_COPY_TOKENS = 3000

CLAIM_WORDS = {
    "best",
    "certified",
    "compliance",
    "enterprise",
    "fastest",
    "guaranteed",
    "leading",
    "privacy",
    "secure",
    "security",
    "trusted",
    "보안",
    "안전",
    "인증",
    "최고",
    "유일",
}


def read_candidate(path: str) -> str:
    return Path(path).expanduser().read_text(encoding="utf-8")


def lexicon_for_text(text: str, limit: int = 24) -> list[str]:
    counts: dict[str, int] = {}
    for word in words(text):
        if word in STOPWORDS or len(word) < 2:
            continue
        counts[word] = counts.get(word, 0) + 1
    return [word for word, _ in sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:limit]]


def candidate_profile(text: str) -> dict[str, Any]:
    clean = clean_text(text)
    token_list = words(clean)
    sentence_list = sentences(clean)
    sentence_lengths = [len(words(sentence)) for sentence in sentence_list]
    avg_sentence_words = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0.0
    line_list = [clean_text(line.lstrip("#>- ")) for line in text.splitlines() if clean_text(line.lstrip("#>- "))]
    ctas = [line for line in line_list if cta_score(line)]
    headings = [line.lstrip("# ").strip() for line in text.splitlines() if line.lstrip().startswith("#")]
    lexicon = lexicon_for_text(clean)
    return {
        "metrics": {
            "words": len(token_list),
            "sentences": len(sentence_list),
            "avg_sentence_words": round(avg_sentence_words, 1),
            "headings": len(headings),
            "ctas": len(ctas),
            "type_token_ratio": round(len(set(token_list)) / len(token_list), 3) if token_list else 0.0,
        },
        "tone": tone_labels(avg_sentence_words, len(ctas), lexicon),
        "headings": headings,
        "ctas": ctas,
        "lexicon": lexicon,
        "text": clean,
    }


def clamp(value: float) -> float:
    return max(0.0, min(1.0, value))


def sentence_fit(reference_avg: float, candidate_avg: float) -> float:
    if reference_avg <= 0 or candidate_avg <= 0:
        return 0.0
    return clamp(1.0 - abs(reference_avg - candidate_avg) / max(reference_avg, candidate_avg, 8.0))


def heading_fit(reference: dict[str, Any], candidate: dict[str, Any]) -> float:
    reference_lengths = [len(words(item)) for item in reference.get("headings", []) if words(item)]
    candidate_lengths = [len(words(item)) for item in candidate.get("headings", []) if words(item)]
    if not reference_lengths:
        return 1.0
    if not candidate_lengths:
        return 0.25
    ref_avg = sum(reference_lengths) / len(reference_lengths)
    cand_avg = sum(candidate_lengths) / len(candidate_lengths)
    return sentence_fit(ref_avg, cand_avg)


def cta_fit(reference: dict[str, Any], candidate: dict[str, Any]) -> float:
    ref_verbs = set(reference.get("style", {}).get("cta_verbs", []))
    cand_verbs = {tokens[0] for cta in candidate.get("ctas", []) if (tokens := words(cta))}
    if not ref_verbs:
        return 1.0
    if not cand_verbs:
        return 0.0
    return clamp(len(ref_verbs & cand_verbs) / min(len(ref_verbs), 4))


def lexical_variety_fit(reference: dict[str, Any], candidate: dict[str, Any]) -> float:
    reference_ratio = float(reference.get("metrics", {}).get("type_token_ratio", 0.0))
    candidate_ratio = float(candidate.get("metrics", {}).get("type_token_ratio", 0.0))
    if reference_ratio <= 0 or candidate_ratio <= 0:
        return 0.0
    return clamp(1.0 - abs(reference_ratio - candidate_ratio) / max(reference_ratio, candidate_ratio, 0.25))


def tone_fit(reference: dict[str, Any], candidate: dict[str, Any]) -> float:
    ref_tone = set(reference.get("tone", []))
    cand_tone = set(candidate.get("tone", []))
    if not ref_tone:
        return 1.0
    return clamp(len(ref_tone & cand_tone) / len(ref_tone))


def claim_safety(reference: dict[str, Any], candidate: dict[str, Any]) -> float:
    reference_text = " ".join(
        [
            *reference.get("lexicon", []),
            *reference.get("headings", []),
            *reference.get("ctas", []),
            *reference.get("links", []),
            *reference.get("paragraph_samples", []),
        ]
    )
    ref_words = set(words(reference_text))
    cand_claims = {word for word in words(candidate.get("text", "")) if word in CLAIM_WORDS}
    unsupported = cand_claims - ref_words
    return clamp(1.0 - len(unsupported) / 4)


def ngrams(tokens: list[str], size: int) -> set[tuple[str, ...]]:
    return {tuple(tokens[index : index + size]) for index in range(0, max(0, len(tokens) - size + 1))}


def longest_shared_run(source_tokens: list[str], candidate_tokens: list[str]) -> int:
    source_tokens = source_tokens[:MAX_COPY_TOKENS]
    candidate_tokens = candidate_tokens[:MAX_COPY_TOKENS]
    if not source_tokens or not candidate_tokens:
        return 0
    best = 0
    previous = [0] * (len(candidate_tokens) + 1)
    for source_token in source_tokens:
        current = [0] * (len(candidate_tokens) + 1)
        for index, candidate_token in enumerate(candidate_tokens, start=1):
            if source_token == candidate_token:
                current[index] = previous[index - 1] + 1
                best = max(best, current[index])
        previous = current
    return best


def copy_safety(reference: dict[str, Any], candidate: dict[str, Any]) -> tuple[float, int]:
    source_text = " ".join(
        [
            *reference.get("headings", []),
            *reference.get("ctas", []),
            *reference.get("links", []),
            *reference.get("paragraph_samples", []),
        ]
    )
    source_tokens = words(source_text)
    candidate_tokens = words(candidate.get("text", ""))
    if len(source_tokens) < 5 or len(candidate_tokens) < 5:
        return 1.0, 0
    source_grams = ngrams(source_tokens, 5)
    candidate_grams = ngrams(candidate_tokens, 5)
    overlap = len(source_grams & candidate_grams) / max(1, len(candidate_grams))
    shared_run = longest_shared_run(source_tokens, candidate_tokens)
    score = clamp(1.0 - overlap * 2.5)
    if shared_run >= 15:
        score = min(score, 0.25)
    elif shared_run >= 8:
        score = min(score, 0.7)
    return score, shared_run


def score_candidate(reference: dict[str, Any], candidate_text: str, label: str) -> dict[str, Any]:
    candidate = candidate_profile(candidate_text)
    ref_avg = float(reference.get("metrics", {}).get("avg_sentence_words", 0.0))
    cand_avg = float(candidate.get("metrics", {}).get("avg_sentence_words", 0.0))
    copy_score, shared_run = copy_safety(reference, candidate)
    scores = {
        "sentence_fit": sentence_fit(ref_avg, cand_avg),
        "lexical_variety_fit": lexical_variety_fit(reference, candidate),
        "cta_fit": cta_fit(reference, candidate),
        "tone_fit": tone_fit(reference, candidate),
        "heading_fit": heading_fit(reference, candidate),
        "claim_safety": claim_safety(reference, candidate),
        "copy_safety": copy_score,
    }
    weighted = (
        scores["sentence_fit"] * 22
        + scores["cta_fit"] * 18
        + scores["tone_fit"] * 16
        + scores["heading_fit"] * 14
        + scores["lexical_variety_fit"] * 10
        + scores["claim_safety"] * 10
        + scores["copy_safety"] * 10
    )
    passed = (
        weighted >= DEFAULT_PASS_SCORE
        and scores["copy_safety"] * 100 >= DEFAULT_COPY_SAFETY
        and scores["claim_safety"] * 100 >= DEFAULT_CLAIM_SAFETY
    )
    return {
        "label": label,
        "score": round(weighted, 1),
        "grade": grade(weighted),
        "pass": passed,
        "scores": {key: round(value * 100, 1) for key, value in scores.items()},
        "metrics": candidate["metrics"],
        "tone": candidate["tone"],
        "longest_shared_run": shared_run,
    }


def benchmark(reference_source: str, candidate_paths: list[str], timeout: float = 20.0) -> dict[str, Any]:
    reference = analyze(reference_source, timeout=timeout)
    candidates = [
        score_candidate(reference, read_candidate(path), Path(path).stem)
        for path in candidate_paths
    ]
    return {
        "reference": {
            "source": reference["source"],
            "metrics": reference["metrics"],
            "tone": reference["tone"],
            "style": reference.get("style", {}),
        },
        "candidates": sorted(candidates, key=lambda item: item["score"], reverse=True),
    }


def benchmark_json(payload: dict[str, Any]) -> str:
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def benchmark_failures(
    payload: dict[str, Any],
    fail_under: float | None = None,
    min_copy_safety: float | None = None,
    min_claim_safety: float | None = None,
    strict: bool = False,
) -> list[str]:
    failures: list[str] = []
    score_floor = DEFAULT_PASS_SCORE if strict and fail_under is None else fail_under
    copy_floor = DEFAULT_COPY_SAFETY if strict and min_copy_safety is None else min_copy_safety
    claim_floor = DEFAULT_CLAIM_SAFETY if strict and min_claim_safety is None else min_claim_safety

    for candidate in payload["candidates"]:
        label = candidate["label"]
        if score_floor is not None and candidate["score"] < score_floor:
            failures.append(f"{label}: overall {candidate['score']:.1f} < {score_floor:.1f}")
        copy_score = candidate["scores"]["copy_safety"]
        if copy_floor is not None and copy_score < copy_floor:
            failures.append(f"{label}: copy safety {copy_score:.1f} < {copy_floor:.1f}")
        claim_score = candidate["scores"]["claim_safety"]
        if claim_floor is not None and claim_score < claim_floor:
            failures.append(f"{label}: claim safety {claim_score:.1f} < {claim_floor:.1f}")
        if strict and not candidate["pass"] and not any(item.startswith(f"{label}:") for item in failures):
            failures.append(f"{label}: did not pass default gates")
    return failures


def benchmark_markdown(payload: dict[str, Any]) -> str:
    reference = payload["reference"]
    lines = [
        "# Voice Benchmark",
        "",
        f"Reference: `{reference['source']}`",
        "",
        "## Reference Profile",
        "",
        f"- Tone: {', '.join(reference['tone']) or 'not enough copy'}",
        f"- Average sentence length: {reference['metrics']['avg_sentence_words']} words",
        f"- Lexical variety: {reference['metrics'].get('type_token_ratio', 0.0)} type-token ratio",
        f"- CTA verbs: {', '.join(f'`{item}`' for item in reference.get('style', {}).get('cta_verbs', [])[:8]) or 'None detected'}",
        "",
        "## Scores",
        "",
        "| Candidate | Result | Overall | Sentence | Variety | CTA | Tone | Heading | Claim safety | Copy safety |",
        "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for candidate in payload["candidates"]:
        scores = candidate["scores"]
        result = "PASS" if candidate["pass"] else "FAIL"
        lines.append(
            f"| `{candidate['label']}` | **{result}** | {candidate['score']:.1f} | "
            f"{scores['sentence_fit']:.1f} | {scores['lexical_variety_fit']:.1f} | "
            f"{scores['cta_fit']:.1f} | {scores['tone_fit']:.1f} | "
            f"{scores['heading_fit']:.1f} | {scores['claim_safety']:.1f} | "
            f"{scores['copy_safety']:.1f} |"
        )
    lines.extend(["", "## Why This Is Useful", ""])
    lines.append(
        "The score is deterministic. It checks measurable copy signals and gates against unsupported claims and copied spans."
    )
    lines.extend(["", "## Candidate Evidence", ""])
    for candidate in payload["candidates"]:
        lines.append(
            f"- `{candidate['label']}` longest shared run: {candidate['longest_shared_run']} words."
        )
    lines.append("")
    return "\n".join(lines)


def grade(score: float) -> str:
    if score >= 90:
        return "excellent"
    if score >= 75:
        return "aligned"
    if score >= 60:
        return "mixed"
    if score >= 40:
        return "weak"
    return "off-voice"
