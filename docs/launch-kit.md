# Launch Kit

## One-Line Pitch

`site2voice` turns any website into a small `VOICE.md` file for AI coding
agents.

## Short Post

I made `site2voice`, a tiny CLI that generates agent-readable `VOICE.md` files
from website copy.

It extracts headings, CTA text, navigation labels, sentence length, and repeated
vocabulary, then writes a concise voice brief for Claude Code, Cursor, Codex, or
any other coding agent.

```bash
pipx install git+https://github.com/SihyeonJeon/site2voice
site2voice https://example.com --out VOICE.md
```

No LLM dependency. No browser dependency. The goal is simple: give agents voice
and positioning context before they write new UI copy.

Repo: https://github.com/SihyeonJeon/site2voice

## Avoid

- Do not claim official brand approval.
- Do not paste long generated excerpts from third-party sites.
- Do not ask for stars.
- Do not spam unrelated design repositories.
