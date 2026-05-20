# Changelog

## 0.3.0

- Added `site2voice init` for agent-ready context packs.
- Added benchmark CI gates: `--strict`, `--fail-under`,
  `--min-copy-safety`, and `--min-claim-safety`.
- Added stable `site2voice.voice.v1` metadata to JSON output.
- Improved copy-safety runtime on longer inputs.
- Added repo hygiene docs, demo assets, and agent workflow documentation.

## 0.2.1

- Added the `pypi` GitHub environment claim to the Trusted Publishing workflow.

## 0.2.0

- Added `site2voice bench` for before/after voice-alignment scoring.
- Added style fingerprints for heading shape, paragraph rhythm, CTA shape, CTA
  verbs, and lexical variety.
- Added copy-safety and claim-boundary gates.
- Added synthetic editorial fixtures and benchmark report.
- Added source-candidate, benchmark, awesome-eligibility, and harness docs.

## 0.1.0

- Initial CLI for generating `VOICE.md` from URL or local HTML copy.
