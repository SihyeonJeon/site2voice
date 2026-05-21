from __future__ import annotations

import json
from pathlib import Path

from site2voice import __version__
from site2voice.context_pack import create_context_pack
from site2voice.extract import output_contract, to_json, to_markdown, to_site_json, to_site_markdown


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
        "slug": "canva",
        "name": "Canva",
        "url": "https://www.canva.com/about/",
        "category": "design platform",
        "use": "accessible creator-tool positioning",
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
        "slug": "microsoft",
        "name": "Microsoft",
        "url": "https://www.microsoft.com/en-us/ai",
        "category": "technology platform",
        "use": "broad AI product-ecosystem copy",
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
        "slug": "whatsapp",
        "name": "WhatsApp",
        "url": "https://www.whatsapp.com/",
        "category": "messaging platform",
        "use": "privacy-forward consumer utility copy",
    },
    {
        "slug": "linkedin",
        "name": "LinkedIn",
        "url": "https://www.linkedin.com/",
        "category": "professional network",
        "use": "career and professional-network copy",
    },
    {
        "slug": "reddit",
        "name": "Reddit",
        "url": "https://www.redditinc.com/",
        "category": "community platform",
        "use": "community and conversation-platform copy",
    },
    {
        "slug": "pinterest",
        "name": "Pinterest",
        "url": "https://www.pinterest.com/about/",
        "category": "visual discovery platform",
        "use": "visual discovery and inspiration copy",
    },
    {
        "slug": "tiktok",
        "name": "TikTok",
        "url": "https://www.tiktok.com/about",
        "category": "short-form video platform",
        "use": "creator and entertainment-platform copy",
    },
    {
        "slug": "discord",
        "name": "Discord",
        "url": "https://discord.com/",
        "category": "community communication",
        "use": "casual community-product copy",
    },
    {
        "slug": "netflix",
        "name": "Netflix",
        "url": "https://www.netflix.com/",
        "category": "streaming entertainment",
        "use": "direct entertainment subscription copy",
    },
    {
        "slug": "spotify",
        "name": "Spotify",
        "url": "https://www.spotify.com/us/premium/",
        "category": "audio streaming",
        "use": "music and audio subscription copy",
    },
    {
        "slug": "disneyplus",
        "name": "Disney+",
        "url": "https://www.disneyplus.com/",
        "category": "streaming entertainment",
        "use": "franchise entertainment subscription copy",
    },
    {
        "slug": "primevideo",
        "name": "Prime Video",
        "url": "https://www.primevideo.com/",
        "category": "streaming entertainment",
        "use": "catalog-led entertainment copy",
    },
    {
        "slug": "zoom",
        "name": "Zoom",
        "url": "https://www.zoom.com/",
        "category": "work communication",
        "use": "meeting and collaboration SaaS copy",
    },
    {
        "slug": "paypal",
        "name": "PayPal",
        "url": "https://www.paypal.com/us/business",
        "category": "payments platform",
        "use": "consumer and business payments copy",
    },
    {
        "slug": "samsung",
        "name": "Samsung",
        "url": "https://www.samsung.com/",
        "category": "consumer electronics",
        "use": "consumer hardware ecosystem copy",
    },
    {
        "slug": "roblox",
        "name": "Roblox",
        "url": "https://corp.roblox.com/",
        "category": "gaming and creation platform",
        "use": "youth gaming and creator-platform copy",
    },
    {
        "slug": "zillow",
        "name": "Zillow",
        "url": "https://www.zillow.com/mortgages/",
        "category": "real estate marketplace",
        "use": "real-estate finance and marketplace copy",
    },
    {
        "slug": "brave",
        "name": "Brave",
        "url": "https://brave.com/",
        "category": "browser and privacy technology",
        "use": "privacy-first browser and search copy",
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
        "# Context Packs",
        "",
        "Full reference-only `SITE.md` + `VOICE.md` context packs generated from public websites.",
        "",
        "These packs are public artifacts: they keep derived copy metrics and",
        "benchmark contracts, but remove source paragraph samples, source nouns,",
        "raw CTAs, navigation labels, screenshots, logos, and brand assets.",
        "",
        "They are not official brand guidelines, endorsements, or permission to",
        "impersonate a reference source. Reference names identify measurement",
        "sources only.",
        "",
        "For the fastest path, use the single-file [VOICE.md](../voices) and",
        "[SITE.md](../sites) collections.",
        "",
        "## Use",
        "",
        "```bash",
        "curl -L https://raw.githubusercontent.com/SihyeonJeon/site2voice/main/voices/stripe.md -o VOICE.md",
        "curl -L https://raw.githubusercontent.com/SihyeonJeon/site2voice/main/sites/stripe.md -o SITE.md",
        "```",
        "",
        "Then tell your agent:",
        "",
        "```text",
        "Use @SITE.md for page structure and @VOICE.md for copy rhythm.",
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
            f"| [{row['name']}]({row['slug']}/VOICE.md) / [SITE]({row['slug']}/SITE.md) | {row['category']} | "
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
        "Drop-in reference-only copy profiles for AI agents.",
        "",
        "`VOICE.md` captures writing behavior: rhythm, CTA shape, information order, and benchmark gates.",
        "It is not a visual design-system file and not a brand-cloning file.",
        "",
        "Reference names identify public pages used for measurement. They do not imply",
        "sponsorship, endorsement, affiliation, or permission to use protected brand",
        "identity.",
        "",
        "Copy one file into your project as `VOICE.md`, then tell your agent:",
        "",
        "```text",
        "Use @VOICE.md as a copy contract for headings, CTA shape, paragraph rhythm, and UI microcopy.",
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


def build_site_readme(rows: list[dict[str, object]]) -> str:
    lines = [
        "# SITE.md Collection",
        "",
        "Drop-in reference-only page-structure profiles for AI agents.",
        "",
        "`SITE.md` captures page architecture: section order, section jobs,",
        "content boundaries, and agent instructions. It does not include visual",
        "design tokens, source headings, raw CTAs, screenshots, logos, or brand assets.",
        "",
        "Use it with the matching `VOICE.md`:",
        "",
        "```bash",
        "curl -L https://raw.githubusercontent.com/SihyeonJeon/site2voice/main/sites/stripe.md -o SITE.md",
        "curl -L https://raw.githubusercontent.com/SihyeonJeon/site2voice/main/voices/stripe.md -o VOICE.md",
        "```",
        "",
        "Then tell your agent:",
        "",
        "```text",
        "Use @SITE.md for page structure and @VOICE.md for copy rhythm. Bring our own product nouns, facts, and claims.",
        "```",
        "",
        "**No install. No JSON. No generation step.**",
        "",
        "## Sites",
        "",
        "| Site | Archetype | Density | Conversion | Use |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        site = row["site_summary"]
        assert isinstance(site, dict)
        lines.append(
            f"| [{row['name']}]({row['slug']}.md) | {site['page_archetype']} | "
            f"{site['information_density']} | {site['conversion_pressure']} | {row['use']} |"
        )
    lines.extend(
        [
            "",
            "Need machine-readable evidence or an agent prompt too? Use the full",
            "[context packs](../packs).",
            "",
        ]
    )
    return "\n".join(lines)


def normalize_existing_profile(profile: dict[str, object]) -> dict[str, object]:
    metrics = profile["metrics"]
    style = profile.get("style", {})
    assert isinstance(metrics, dict)
    assert isinstance(style, dict)
    cta_verbs = style.get("cta_verbs", [])
    assert isinstance(cta_verbs, list)
    normalized = dict(profile)
    normalized["generator"] = f"site2voice/{__version__}"
    normalized["title"] = ""
    normalized["meta_description"] = ""
    normalized["headings"] = []
    normalized["paragraph_samples"] = []
    normalized["lexicon"] = []
    normalized["ctas"] = []
    normalized["links"] = []
    normalized["buttons"] = []
    normalized["output_contract"] = output_contract(metrics, [], [str(item) for item in cta_verbs])
    normalized["output_contract"]["source_terms"] = []
    return normalized


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    packs_dir = root / "packs"
    voices_dir = root / "voices"
    sites_dir = root / "sites"
    packs_dir.mkdir(exist_ok=True)
    voices_dir.mkdir(exist_ok=True)
    sites_dir.mkdir(exist_ok=True)

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
                category_hint=pack["category"],
            )
        except Exception as exc:  # noqa: BLE001
            if (target / "VOICE.md").exists() and (target / "voice.json").exists():
                existing_profile = normalize_existing_profile(
                    json.loads((target / "voice.json").read_text(encoding="utf-8"))
                )
                (target / "VOICE.md").write_text(to_markdown(existing_profile, max_snippets=0), encoding="utf-8")
                (target / "voice.json").write_text(to_json(existing_profile), encoding="utf-8")
                (target / "SITE.md").write_text(
                    to_site_markdown(existing_profile, category_hint=pack["category"]),
                    encoding="utf-8",
                )
                (target / "site.json").write_text(
                    to_site_json(existing_profile, category_hint=pack["category"]),
                    encoding="utf-8",
                )
            required = ["VOICE.md", "SITE.md", "voice.json", "site.json"]
            if any(not (target / name).exists() for name in required):
                raise
            print(f"warning: keeping existing {pack['slug']} pack after fetch failed: {exc}")
        (voices_dir / f"{pack['slug']}.md").write_text(
            (target / "VOICE.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        (sites_dir / f"{pack['slug']}.md").write_text(
            (target / "SITE.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        profile = json.loads((target / "voice.json").read_text(encoding="utf-8"))
        site_profile = json.loads((target / "site.json").read_text(encoding="utf-8"))
        row: dict[str, object] = {
            **pack,
            "metrics": profile["metrics"],
            "tone": profile["tone"],
            "site_summary": site_profile["site_summary"],
        }
        rows.append(row)

    rows = sorted(rows, key=lambda item: str(item["slug"]))
    (packs_dir / "index.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (packs_dir / "README.md").write_text(build_readme(rows), encoding="utf-8")
    (voices_dir / "README.md").write_text(build_voice_readme(rows), encoding="utf-8")
    (sites_dir / "README.md").write_text(build_site_readme(rows), encoding="utf-8")


if __name__ == "__main__":
    main()
