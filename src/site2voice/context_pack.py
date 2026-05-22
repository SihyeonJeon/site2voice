from __future__ import annotations

from pathlib import Path
from typing import Any

from .extract import analyze, to_json, to_markdown, to_site_json, to_site_markdown


PROMPT_TEMPLATE = """# SITE.md + VOICE.md Agent Prompt

Use `SITE.md` and `VOICE.md` together:

- `SITE.md`: page structure, section order, section jobs, and content boundaries.
- `VOICE.md`: sentence rhythm, CTA shape, paragraph rhythm, and benchmark gates.

Together they form a reference-only copy contract and page-structure contract.
They do not replace `DESIGN.md`. If `DESIGN.md` is present, it owns colors,
typography, spacing, layout grid, components, motion, and imagery style.

Before shipping new copy, run a benchmark against the source:

```bash
site2voice bench {source} path/to/candidate.md --strict
```

Rules:

- Treat the `Output Contract` section in `VOICE.md` as the measurable
  pass/fail target.
- Treat the `Page Blueprint` and `Section Recipes` sections in `SITE.md` as the
  page-structure target.
- Reuse rhythm, CTA shape, and information order; bring your own product nouns.
- Do not transfer source-specific nouns from the reference site.
- Do not infer the new product category, audience, examples, or offer from the
  reference site.
- Do not use `SITE.md` or `VOICE.md` for colors, fonts, spacing, components,
  animation, imagery, or responsive layout.
- Keep unsupported security, performance, customer, pricing, or AI claims out.
- Do not imply brand affiliation, endorsement, or official guideline status.
- Treat `voice.json` and `site.json` as machine-readable evidence, not brand approval.
"""


def create_context_pack(
    source: str,
    output_dir: str,
    timeout: float = 20.0,
    max_snippets: int = 0,
    force: bool = False,
    category_hint: str | None = None,
) -> dict[str, Any]:
    payload = analyze(source, timeout=timeout)
    json_payload = dict(payload)
    if max_snippets == 0:
        json_payload["title"] = ""
        json_payload["meta_description"] = ""
        json_payload["headings"] = []
        json_payload["paragraph_samples"] = []
        json_payload["lexicon"] = []
        json_payload["ctas"] = []
        json_payload["links"] = []
        json_payload["buttons"] = []
        json_payload["output_contract"] = dict(payload["output_contract"])
        json_payload["output_contract"]["source_terms"] = []
    target = Path(output_dir).expanduser()
    paths = {
        "voice_md": target / "VOICE.md",
        "site_md": target / "SITE.md",
        "voice_json": target / "voice.json",
        "site_json": target / "site.json",
        "agent_prompt": target / "agent-prompt.md",
    }
    existing = [path for path in paths.values() if path.exists()]
    if existing and not force:
        names = ", ".join(str(path) for path in existing)
        raise FileExistsError(f"refusing to overwrite existing files: {names}")

    target.mkdir(parents=True, exist_ok=True)
    paths["voice_md"].write_text(to_markdown(payload, max_snippets=max_snippets), encoding="utf-8")
    paths["site_md"].write_text(to_site_markdown(payload, category_hint=category_hint), encoding="utf-8")
    paths["voice_json"].write_text(to_json(json_payload), encoding="utf-8")
    paths["site_json"].write_text(to_site_json(payload, category_hint=category_hint), encoding="utf-8")
    paths["agent_prompt"].write_text(PROMPT_TEMPLATE.format(source=payload["source"]), encoding="utf-8")

    return {
        "source": payload["source"],
        "output_dir": str(target),
        "files": {key: str(path) for key, path in paths.items()},
    }
