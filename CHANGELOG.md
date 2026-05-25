# Changelog

## Unreleased

## 0.6.0

- Added `site2voice webfit` for scoring visible HTML outputs against
  `SITE.md` and `VOICE.md` JSON profiles.
- Added CLI gates for visible before/after evidence: minimum reference-fit
  delta, minimum copy safety, and maximum mimic risk.
- Added `webfit.md` and `webfit.json` to the Stripe/LedgerFlow web comparison
  so the screenshot example is reproducible from the package command.
- Refactored the previous reference-fit script to use the packaged webfit
  implementation.

## 0.5.6

- Removed internal planning and positioning notes from the public docs.
- Trimmed README and collection READMEs toward direct use: choose a profile,
  copy `SITE.md` / `VOICE.md`, and keep visual design in `DESIGN.md`.
- Kept user-facing docs focused on role boundaries, benchmarking, CI usage,
  and generated profile semantics.

## 0.5.5

- Added explicit domain-firewall rules to generated `SITE.md`, `VOICE.md`, and
  agent prompts so reference style cannot supply product category, audience,
  examples, offers, claims, or source-domain nouns.
- Added a context-stack contract that separates project brief, `DESIGN.md`,
  `SITE.md`, and `VOICE.md` ownership.
- Changed CLI and context-pack defaults to omit source snippets unless
  `--max-snippets` is explicitly set above zero.
- Added regression coverage for cross-domain leakage from retail-style source
  terms into unrelated generated context files.

- Added a visible Stripe/LedgerFlow web comparison with side-by-side HTML
  outputs, screenshots, and a reproducible `reference-fit` report.
- Added `scripts/reference_fit_report.py` to measure safe motif reproduction:
  structure fit, voice fit, copy safety, claim safety, and mimic risk.

## 0.5.4

- Added `SITE.md` page-structure profiles beside existing `VOICE.md` copy
  profiles.
- Added `site2voice site SOURCE --out SITE.md` and machine-readable
  `site2voice.site.v1` / `site.json` output.
- Updated context packs to include `SITE.md`, `site.json`, `VOICE.md`,
  `voice.json`, and a combined agent prompt.
- Added a flat `sites/` collection for direct file downloads.
- Kept numeric ranges as benchmark drift checks while moving public guidance
  toward section recipes, rhetorical patterns, and content boundaries.

## 0.5.3

- Added 18 reference-only copy profiles from popular web products and platforms.
- Added source-selection notes for expanded public profiles.
- Hardened sentence extraction for card-heavy and JS-rendered pages by deriving
  sentence shape from paragraph-like blocks before broader fallback text.
- Expanded CTA verb detection to include common editorial verbs such as `read`
  and `open`.

## 0.5.2

- Reframed public documentation around reference-only copy profiles instead of
  brand-voice imitation.
- Added `BRAND_USAGE.md` and a `DESIGN.md` vs `VOICE.md` role comparison.
- Added brand-safety scope language to generated `VOICE.md` files and context
  pack prompts.
- Synced the package runtime version with the release version.

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
- Added benchmark and safety docs.

## 0.1.0

- Initial CLI for generating `VOICE.md` from URL or local HTML copy.
