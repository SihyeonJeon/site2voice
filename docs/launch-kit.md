# Launch Kit

## One-Line Pitch

`site2voice` turns public website copy into agent-ready copy context, then
benchmarks whether the agent followed the measurable writing contract.

## Short Post

I made `site2voice`, a tiny CLI that generates agent-readable `VOICE.md` copy
profiles from public website copy and scores whether new AI-written copy follows
the measurable profile without copying source prose.

It extracts heading shape, CTA verb shape, navigation-label length, sentence
rhythm, paragraph rhythm, and information order, then writes a concise copy
contract for Claude Code, Cursor, Codex, or any other coding agent.

```bash
pipx install site2voice
site2voice init https://example.com
site2voice bench https://example.com draft.md --strict
```

No LLM dependency. No browser dependency. The goal is simple: give agents copy
and positioning context before they write new UI copy.

The benchmark path shows whether the generated copy actually moved closer to
the reference profile, without rewarding copied spans or source vocabulary.

Repo: https://github.com/SihyeonJeon/site2voice

## Avoid

- Do not claim official brand approval.
- Do not describe outputs as brand clones or official voice guidelines.
- Do not publish source nouns, raw CTAs, navigation labels, logos, or screenshots
  as reusable style assets.
- Do not paste long generated excerpts from third-party sites.
- Do not ask for stars.
- Do not spam unrelated design repositories.
