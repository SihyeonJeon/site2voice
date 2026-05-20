# Market Position

Agentic coding tools increasingly depend on repo-local context files and
specialized instructions:

- Claude Code loads project memory from `CLAUDE.md` files and supports reusable
  skills.
- Codex documents repo-scoped `AGENTS.md` instructions.
- GitHub Copilot exposes coding-agent workflows and repository instructions.

The gap: these files usually describe architecture and coding conventions, not
the product's public writing behavior.

`site2voice` sits in that gap:

```text
public copy -> VOICE.md + voice.json -> agent writes copy -> bench gate
```

## Why This Can Travel

- It is easy to explain in one sentence.
- It produces visible output in one command.
- It works with any coding agent because the output is Markdown and JSON.
- It has an eval path, so the result is not just a prompt artifact.
- It avoids a weak claim: it does not "clone a brand"; it extracts reference-only
  copy signals, strips source nouns, and checks drift.
- It has a defensible boundary: reference names identify measurement sources,
  not affiliation or permission to impersonate.

## Sources

- [Claude Code memory](https://docs.claude.com/en/docs/claude-code/memory)
- [Claude Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills)
- [Codex AGENTS.md](https://github.com/openai/codex/blob/main/docs/agents_md.md)
- [GitHub Copilot agents](https://docs.github.com/en/copilot/how-tos/agents)
