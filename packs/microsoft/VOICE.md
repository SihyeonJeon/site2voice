# VOICE.md

Reference source: `https://www.microsoft.com/en-us/ai`

Use this file as a reference-only copy profile for AI-generated pages, docs, and UI microcopy.

## Voice Summary

- Overall tone: **balanced, action-oriented, technical, trust-forward**.
- Copy method: follow the rhetorical moves, section behavior, CTA pattern, and claim boundaries below.
- Measurement policy: word ranges are benchmark drift checks, not the main writing method.
- Content policy: this file captures rhythm and structure, not source nouns.
- Brand policy: this is not an official guideline, endorsement, or permission to impersonate the reference source.

## Scope

- Reuse measurable writing patterns: sentence rhythm, heading shape, CTA verb shape, paragraph rhythm, and information order.
- Bring your own product names, topics, audience, claims, examples, and domain nouns.
- Do not use trademarks, logos, proprietary product names, or brand claims unless you already have independent rights to use them.
- Do not infer the new project's product category from the reference site.
- Do not use this file for colors, fonts, spacing, components, animation, imagery, or responsive layout.

## Context Stack

- Project brief owns: product category, audience, facts, domain nouns, examples, offers, and claims.
- `DESIGN.md` owns: colors, typography, spacing, layout grid, visual components, motion, and imagery style.
- `SITE.md` owns: page structure, section order, section jobs, and conversion path.
- `VOICE.md` owns: sentence rhythm, heading behavior, CTA shape, and claim boundaries.
- If files conflict, do not merge responsibilities; use the owner above.

## Domain Firewall

- Reference supplies: rhythm, heading shape, CTA shape, section behavior, and rhetorical moves.
- New project supplies: category, audience, domain nouns, examples, offer, claims, proof, and visual subject matter.
- If a noun or scenario is not in the new project brief, remove it even if it appears in the reference source.
- Example: when using a retail reference for an education product, keep all nouns, examples, proof, and CTAs educational.

## Writing Moves

- First screen: start with a concrete user outcome, then add one short proof/value sentence.
- Heading move: make headings specific enough to stand alone in a scan.
- Body move: explain one idea per paragraph; do not stack unrelated claims.
- CTA move: use visible action verbs and keep the next step unambiguous.
- Claim move: prefer supported product behavior over broad market promises.

## Style Fingerprint

Use these numbers as calibration checks after drafting.

- Heading shape: about **8.8 words** per heading.
- Paragraph rhythm: about **13 words** per paragraph sample.
- CTA shape: about **3.2 words** per CTA.
- CTA verbs: `download`, `get`, `explore`, `learn`, `read`.
- Navigation label shape: about **2.1 words** per label.
- Lexical variety: **0.207** type-token ratio.

## Agent Rules

- Start with a concrete user outcome before describing implementation details.
- Prefer short active sentences and visible verbs from the CTA list.
- Reuse rhythm, CTA shape, and information order; bring your own product nouns.
- Do not import source-specific topics, product names, market claims, audience assumptions, or domain nouns.
- Defer all visual decisions to `DESIGN.md` when it is present.
- Do not imply affiliation with, approval from, or official representation of the reference source.
- Keep headings specific; avoid generic labels like `<generic feature label>` unless the source uses that pattern.
- When adding new sections, match the observed information order: headline, proof, action, details.
- Do not invent compliance, security, customer, or performance claims that are not present in the source.

## Output Contract

- Benchmark drift check: keep average sentence length between **8.2 and 13.6 words**.
- Keep headings near **8.8 words**; avoid generic one-word section labels unless the source uses them.
- Keep paragraph blocks near **13.0 words**.
- Keep CTAs near **3.2 words** and start them with: `download`, `get`, `explore`, `learn`, `read`.
- Content boundary: Use only the new project's nouns, facts, audience, offer, and domain. Do not transfer source-specific products, categories, slogans, people, campaigns, or topics.
- Keep the first screen structure close to: specific headline, short proof/value sentence, one or two action CTAs.
- If writing a candidate file, run:
  `site2voice bench https://www.microsoft.com/en-us/ai path/to/candidate.md --strict`
- Revise until overall >= **75**, copy safety >= **85**, and claim safety >= **75**.

## Evidence

| Signal | Value |
| --- | --- |
| Words | 3369 |
| Sentences | 222 |
| Headings | 12 |
| CTA candidates | 12 |

## Do / Don't

- Do: write concise, outcome-first copy using the observed rhythm and CTA verbs.
- Do: keep CTAs short and action-led.
- Don't: transfer source-specific nouns into an unrelated project.
- Don't: present the result as official brand copy or a brand guideline.
- Don't: paste source paragraphs verbatim.
- Don't: add claims the source did not support.
