# Agent Workflows

`site2voice init` creates the files an agent needs before writing copy:

```bash
site2voice init https://example.com
```

Then give the agent this instruction:

```text
Use @.site2voice/VOICE.md for headings, CTAs, navigation labels, and UI
microcopy. Follow the Output Contract. Do not invent claims. Before finishing,
run site2voice bench.
```

## Codex

Add this to `AGENTS.md`:

```md
Use `.site2voice/VOICE.md` for public-facing copy.
Run `site2voice bench SOURCE path/to/candidate.md --strict` before changing
landing-page or docs copy.
```

## Claude Code

Add this to `CLAUDE.md` or a project skill:

```md
When writing website copy, read `.site2voice/VOICE.md` first. Use the vocabulary,
CTA shape, Output Contract, and claim boundaries. Do not paste source
paragraphs. Validate with `site2voice bench`.
```

## Cursor / Copilot

Reference `.site2voice/VOICE.md` in the task prompt or project instructions.
Use `voice.json` when you want deterministic metrics in a script.
