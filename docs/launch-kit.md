# Launch Kit

## One-Line Pitch

`site2voice` turns any website into agent-ready copy context, then benchmarks
whether the agent followed it.

## Short Post

I made `site2voice`, a tiny CLI that generates agent-readable `VOICE.md` files
from website copy and scores whether new AI-written copy follows the source
voice.

It extracts headings, CTA text, navigation labels, sentence length, and repeated
structure, then writes a concise voice brief for Claude Code, Cursor, Codex, or
any other coding agent.

```bash
pipx install site2voice
site2voice init https://example.com
site2voice bench https://example.com draft.md --strict
```

No LLM dependency. No browser dependency. The goal is simple: give agents voice
and positioning context before they write new UI copy.

The benchmark path shows whether the generated copy actually moved closer to
the source voice, without rewarding copied spans.

Repo: https://github.com/SihyeonJeon/site2voice

## Avoid

- Do not claim official brand approval.
- Do not paste long generated excerpts from third-party sites.
- Do not ask for stars.
- Do not spam unrelated design repositories.
