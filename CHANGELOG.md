# Changelog

## 0.4.0

- Added public voice packs for 15 well-known product and editorial sites.
- Added `packs/index.json` and `packs/README.md`.
- Added `scripts/build_packs.py` for reproducible pack generation.
- Redacted paragraph samples from `site2voice init --no-samples` JSON output.
- Updated README around downloadable voice packs.

## 0.3.0

- Added `site2voice init` for agent-ready context packs.
- Added benchmark CI gates: `--strict`, `--fail-under`,
  `--min-copy-safety`, and `--min-claim-safety`.
- Added stable `site2voice.voice.v1` metadata to JSON output.
- Improved copy-safety runtime on longer inputs.
- Added repo hygiene docs, demo assets, agent workflow documentation, and
  public voice packs for well-known websites.

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
