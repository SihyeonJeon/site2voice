# Harness

`site2voice` is built as a small agent-orchestration harness:

1. **Scout** finds relevant public sources and decides whether they are safe as
   live examples or should be represented by synthetic fixtures.
2. **Profiler** runs `site2voice SOURCE --format json` and extracts measurable
   voice signals: sentence shape, heading shape, CTA verbs, lexical variety,
   and repeated vocabulary.
3. **Initializer** runs `site2voice init SOURCE` to create `VOICE.md`,
   `voice.json`, and `agent-prompt.md`.
4. **Writer** uses the generated `VOICE.md` as context to write new candidate
   copy.
5. **Evaluator** runs `site2voice bench SOURCE candidate.md --strict` and checks
   alignment, claim boundaries, and copy safety.
6. **Publisher** updates examples, docs, releases, and launch notes.

## Claude Operator Review

Claude operator review agreed with the direction and recommended:

- deterministic style fingerprints instead of vague tone claims;
- a scorer before additional promotion;
- explicit copy-safety and unsupported-claim gates;
- source candidates as live examples, not committed third-party prose.

## Current Team Findings

- Editorial/magazine sources are useful for tone, but checked-in examples should
  be synthetic.
- `site2voice` should be submitted to awesome lists only after release/demo
  evidence is stronger.
- Best awesome-list fit found so far: vibe-coding/context-engineering lists, not
  visual design lists.

See [awesome-eligibility.md](awesome-eligibility.md) for submission gates.
