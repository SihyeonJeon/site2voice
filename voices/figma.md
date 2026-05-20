# VOICE.md

Reference source: `https://www.figma.com/`

Use this file as a reference-only copy profile for AI-generated pages, docs, and UI microcopy.

## Voice Summary

- Overall tone: **short and direct, action-oriented, technical**.
- Sentence shape: about **7 words** per sentence.
- Content policy: this file captures rhythm and structure, not source nouns.
- Brand policy: this is not an official guideline, endorsement, or permission to impersonate the reference source.

## Scope

- Reuse measurable writing patterns: sentence rhythm, heading shape, CTA verb shape, paragraph rhythm, and information order.
- Bring your own product names, topics, claims, examples, and domain nouns.
- Do not use trademarks, logos, proprietary product names, or brand claims unless you already have independent rights to use them.

## Style Fingerprint

- Heading shape: about **4.8 words** per heading.
- Paragraph rhythm: about **3.2 words** per paragraph sample.
- CTA shape: about **3.2 words** per CTA.
- CTA verbs: `explore`, `see`, `learn`, `contact`, `get`, `build`.
- Navigation label shape: about **2.7 words** per label.
- Lexical variety: **0.227** type-token ratio.

## Agent Rules

- Start with a concrete user outcome before describing implementation details.
- Prefer short active sentences and visible verbs from the CTA list.
- Reuse rhythm, CTA shape, and information order; bring your own product nouns.
- Do not import source-specific topics, product names, market claims, or domain nouns.
- Do not imply affiliation with, approval from, or official representation of the reference source.
- Keep headings specific; avoid generic labels like `<generic feature label>` unless the source uses that pattern.
- When adding new sections, match the observed information order: headline, proof, action, details.
- Do not invent compliance, security, customer, or performance claims that are not present in the source.

## Output Contract

- Keep average sentence length between **5.2 and 8.8 words**.
- Keep headings near **4.8 words**; avoid generic one-word section labels unless the source uses them.
- Keep paragraph blocks near **3.2 words**.
- Keep CTAs near **3.2 words** and start them with: `explore`, `see`, `learn`, `contact`, `get`, `build`.
- Content boundary: Use only the new project's nouns. Do not transfer source-specific terms from the reference site.
- Keep the first screen structure close to: specific headline, short proof/value sentence, one or two action CTAs.
- If writing a candidate file, run:
  `site2voice bench https://www.figma.com/ path/to/candidate.md --strict`
- Revise until overall >= **75**, copy safety >= **85**, and claim safety >= **75**.

## Evidence

| Signal | Value |
| --- | --- |
| Words | 1544 |
| Sentences | 51 |
| Headings | 12 |
| CTA candidates | 12 |

## Do / Don't

- Do: write concise, outcome-first copy using the observed rhythm and CTA verbs.
- Do: keep CTAs short and action-led.
- Don't: transfer source-specific nouns into an unrelated project.
- Don't: present the result as official brand copy or a brand guideline.
- Don't: paste source paragraphs verbatim.
- Don't: add claims the source did not support.
