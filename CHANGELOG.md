# Changelog

## Unreleased

## 0.5.1

- Repositioned the README around ready-to-use `VOICE.md` downloads.
- Added a flat `voices/` collection for direct single-file use.
- Updated pack generation to build `voices/` and avoid duplicate URL fetches.
- Removed source vocabulary, raw CTA text, and navigation labels from public
  `VOICE.md` files so content nouns do not leak as style.
- Redacted raw text arrays from public `voice.json` files generated with
  `--no-samples`.
- Updated benchmarks to reward lexical variety and CTA verbs instead of source
  vocabulary overlap.

## 0.5.0

- Added an `Output Contract` section to generated `VOICE.md` files.
- Added machine-readable `output_contract` fields to generated `voice.json`.
- Updated context-pack agent prompts to treat the output contract as the
  measurable target before running `site2voice bench`.
- Regenerated public voice packs and the Stripe comparison with the stronger
  contract included.

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
