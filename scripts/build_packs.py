from __future__ import annotations

import json
from pathlib import Path

from site2voice.context_pack import create_context_pack


PACKS = [
    {
        "slug": "apple",
        "name": "Apple",
        "url": "https://www.apple.com/",
        "category": "consumer hardware",
        "use": "minimal premium product copy",
    },
    {
        "slug": "stripe",
        "name": "Stripe",
        "url": "https://stripe.com/",
        "category": "financial infrastructure",
        "use": "technical trust-forward SaaS copy",
    },
    {
        "slug": "linear",
        "name": "Linear",
        "url": "https://linear.app/",
        "category": "developer productivity",
        "use": "precise product-team positioning",
    },
    {
        "slug": "vercel",
        "name": "Vercel",
        "url": "https://vercel.com/",
        "category": "developer platform",
        "use": "performance and deployment copy",
    },
    {
        "slug": "notion",
        "name": "Notion",
        "url": "https://www.notion.com/",
        "category": "workspace productivity",
        "use": "simple workspace and AI-product copy",
    },
    {
        "slug": "figma",
        "name": "Figma",
        "url": "https://www.figma.com/",
        "category": "design collaboration",
        "use": "creative collaboration copy",
    },
    {
        "slug": "shopify",
        "name": "Shopify",
        "url": "https://www.shopify.com/",
        "category": "commerce platform",
        "use": "merchant-growth product copy",
    },
    {
        "slug": "github",
        "name": "GitHub",
        "url": "https://github.com/",
        "category": "developer platform",
        "use": "developer ecosystem copy",
    },
    {
        "slug": "openai",
        "name": "OpenAI",
        "url": "https://openai.com/",
        "category": "AI research and product",
        "use": "research-to-product institutional copy",
    },
    {
        "slug": "anthropic",
        "name": "Anthropic",
        "url": "https://www.anthropic.com/",
        "category": "AI research and product",
        "use": "measured AI safety and product copy",
    },
    {
        "slug": "hypebeast",
        "name": "Hypebeast",
        "url": "https://hypebeast.com/",
        "category": "streetwear and culture media",
        "use": "trend-led culture editorial copy",
    },
    {
        "slug": "highsnobiety",
        "name": "Highsnobiety",
        "url": "https://www.highsnobiety.com/",
        "category": "fashion and culture media",
        "use": "commerce-aware culture editorial copy",
    },
    {
        "slug": "monocle",
        "name": "Monocle",
        "url": "https://monocle.com/",
        "category": "global affairs and culture media",
        "use": "polished city, design, and affairs copy",
    },
    {
        "slug": "wallpaper",
        "name": "Wallpaper",
        "url": "https://www.wallpaper.com/",
        "category": "design and architecture media",
        "use": "design, interiors, and architecture editorial copy",
    },
    {
        "slug": "eyesmag",
        "name": "EYESMAG",
        "url": "https://www.eyesmag.com/about",
        "category": "Korean fashion and lifestyle media",
        "use": "Korean fashion and lifestyle editorial intro copy",
    },
]


def build_readme(rows: list[dict[str, object]]) -> str:
    lines = [
        "# Voice Packs",
        "",
        "Full context packs generated from well-known public websites.",
        "",
        "These packs are safe public artifacts: they keep derived style metrics and",
        "short labels, but remove source paragraph samples. They are not official",
        "brand guidelines and should not be used to copy protected prose.",
        "",
        "For the fastest path, use the single-file [VOICE.md collection](../voices).",
        "",
        "## Use",
        "",
        "```bash",
        "curl -L https://raw.githubusercontent.com/SihyeonJeon/site2voice/main/voices/stripe.md -o VOICE.md",
        "```",
        "",
        "Then tell your agent:",
        "",
        "```text",
        "Use @VOICE.md for headings, CTAs, navigation labels, and UI microcopy.",
        "```",
        "",
        "## Packs",
        "",
        "| Pack | Category | Words | Sentence | CTA | Use |",
        "| --- | --- | ---: | ---: | ---: | --- |",
    ]
    for row in rows:
        metrics = row["metrics"]
        assert isinstance(metrics, dict)
        lines.append(
            f"| [{row['name']}]({row['slug']}/VOICE.md) | {row['category']} | "
            f"{metrics['words']} | {metrics['avg_sentence_words']} | {metrics['ctas']} | {row['use']} |"
        )
    lines.extend(
        [
            "",
            "Regenerate:",
            "",
            "```bash",
            "PYTHONPATH=src python3 scripts/build_packs.py",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def build_voice_readme(rows: list[dict[str, object]]) -> str:
    lines = [
        "# VOICE.md Collection",
        "",
        "Drop-in writing style files for AI agents.",
        "",
        "`DESIGN.md` tells agents how UI should look. `VOICE.md` tells them how copy should sound.",
        "",
        "Copy one file into your project as `VOICE.md`, then tell your agent:",
        "",
        "```text",
        "Use @VOICE.md for headings, CTAs, navigation labels, and UI microcopy.",
        "```",
        "",
        "**No install. No JSON. No generation step.**",
        "",
        "## Download",
        "",
        "```bash",
        "curl -L https://raw.githubusercontent.com/SihyeonJeon/site2voice/main/voices/stripe.md -o VOICE.md",
        "```",
        "",
        "## Voices",
        "",
        "| Voice | Tone | Use |",
        "| --- | --- | --- |",
    ]
    for row in rows:
        tone = ", ".join(row.get("tone", [])) or str(row["category"])
        lines.append(f"| [{row['name']}]({row['slug']}.md) | {tone} | {row['use']} |")
    lines.extend(
        [
            "",
            "Need machine-readable metrics or an agent prompt too? Use the full",
            "[context packs](../packs).",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    packs_dir = root / "packs"
    voices_dir = root / "voices"
    packs_dir.mkdir(exist_ok=True)
    voices_dir.mkdir(exist_ok=True)

    rows: list[dict[str, object]] = []
    for pack in PACKS:
        target = packs_dir / pack["slug"]
        try:
            create_context_pack(
                pack["url"],
                output_dir=str(target),
                max_snippets=0,
                force=True,
                timeout=20.0,
            )
        except Exception as exc:  # noqa: BLE001
            if not (target / "VOICE.md").exists() or not (target / "voice.json").exists():
                raise
            print(f"warning: keeping existing {pack['slug']} pack after fetch failed: {exc}")
        (voices_dir / f"{pack['slug']}.md").write_text(
            (target / "VOICE.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        profile = json.loads((target / "voice.json").read_text(encoding="utf-8"))
        row: dict[str, object] = {
            **pack,
            "metrics": profile["metrics"],
            "tone": profile["tone"],
        }
        rows.append(row)

    rows = sorted(rows, key=lambda item: str(item["slug"]))
    (packs_dir / "index.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (packs_dir / "README.md").write_text(build_readme(rows), encoding="utf-8")
    (voices_dir / "README.md").write_text(build_voice_readme(rows), encoding="utf-8")


if __name__ == "__main__":
    main()
