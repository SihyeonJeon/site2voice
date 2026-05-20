from __future__ import annotations

from pathlib import Path
from typing import Any

from .extract import analyze, to_json, to_markdown


PROMPT_TEMPLATE = """# site2voice Agent Prompt

Use `VOICE.md` as the source of truth for landing-page copy, headings, CTAs,
navigation labels, and UI microcopy.

Before shipping new copy, run a benchmark against the source:

```bash
site2voice bench {source} path/to/candidate.md --strict
```

Rules:

- Treat the `Output Contract` section in `VOICE.md` as the measurable
  pass/fail target.
- Reuse rhythm, CTA shape, and information order; bring your own product nouns.
- Do not transfer source-specific nouns from the reference site.
- Keep unsupported security, performance, customer, pricing, or AI claims out.
- Treat `voice.json` as machine-readable evidence, not as brand approval.
"""


def create_context_pack(
    source: str,
    output_dir: str,
    timeout: float = 20.0,
    max_snippets: int = 8,
    force: bool = False,
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
        "voice_json": target / "voice.json",
        "agent_prompt": target / "agent-prompt.md",
    }
    existing = [path for path in paths.values() if path.exists()]
    if existing and not force:
        names = ", ".join(str(path) for path in existing)
        raise FileExistsError(f"refusing to overwrite existing files: {names}")

    target.mkdir(parents=True, exist_ok=True)
    paths["voice_md"].write_text(to_markdown(payload, max_snippets=max_snippets), encoding="utf-8")
    paths["voice_json"].write_text(to_json(json_payload), encoding="utf-8")
    paths["agent_prompt"].write_text(PROMPT_TEMPLATE.format(source=payload["source"]), encoding="utf-8")

    return {
        "source": payload["source"],
        "output_dir": str(target),
        "files": {key: str(path) for key, path in paths.items()},
    }
