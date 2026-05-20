# VOICE.md

Reference source: `examples/saas-home.html`

Use this file as a reference-only copy profile for AI-generated pages, docs, and UI microcopy.

## Voice Summary

- Overall tone: **balanced, action-oriented, trust-forward**.
- Copy method: follow the rhetorical moves, section behavior, CTA pattern, and claim boundaries below.
- Measurement policy: word ranges are benchmark drift checks, not the main writing method.
- Content policy: this file captures rhythm and structure, not source nouns.
- Brand policy: this is not an official guideline, endorsement, or permission to impersonate the reference source.

## Scope

- Reuse measurable writing patterns: sentence rhythm, heading shape, CTA verb shape, paragraph rhythm, and information order.
- Bring your own product names, topics, claims, examples, and domain nouns.
- Do not use trademarks, logos, proprietary product names, or brand claims unless you already have independent rights to use them.

## Writing Moves

- First screen: start with a concrete user outcome, then add one short proof/value sentence.
- Heading move: make headings specific enough to stand alone in a scan.
- Body move: explain one idea per paragraph; do not stack unrelated claims.
- CTA move: use visible action verbs and keep the next step unambiguous.
- Claim move: prefer supported product behavior over broad market promises.

## Style Fingerprint

Use these numbers as calibration checks after drafting.

- Heading shape: about **5.8 words** per heading.
- Paragraph rhythm: about **16.5 words** per paragraph sample.
- CTA shape: about **2.2 words** per CTA.
- CTA verbs: `sign`, `start`, `book`, `see`.
- Navigation label shape: about **1.6 words** per label.
- Lexical variety: **0.853** type-token ratio.

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

- Benchmark drift check: keep average sentence length between **12.4 and 20.6 words**.
- Keep headings near **5.8 words**; avoid generic one-word section labels unless the source uses them.
- Keep paragraph blocks near **16.5 words**.
- Keep CTAs near **2.2 words** and start them with: `sign`, `start`, `book`, `see`.
- Content boundary: Use only the new project's nouns. Do not transfer source-specific terms from the reference site.
- Keep the first screen structure close to: specific headline, short proof/value sentence, one or two action CTAs.
- If writing a candidate file, run:
  `site2voice bench examples/saas-home.html path/to/candidate.md --strict`
- Revise until overall >= **75**, copy safety >= **85**, and claim safety >= **75**.

## Page Pattern

- Heading: Run your launch room from one calm board
- Heading: One place for launch decisions
- Heading: Built for focused teams
- Heading: Trusted by teams that ship weekly

## Evidence

| Signal | Value |
| --- | --- |
| Words | 102 |
| Sentences | 4 |
| Headings | 4 |
| CTA candidates | 4 |

## Short Copy Samples

- Northstar Ops helps small software teams plan releases, review blockers, and ship without…
- Bring specs, owners, risks, and approvals into a shared timeline that stays readable when the…
- Use clear handoffs, quiet notifications, and concise audit trails so every teammate knows what…
- Security controls, role-based access, and exportable logs keep release work accountable…

## Do / Don't

- Do: write concise, outcome-first copy using the observed rhythm and CTA verbs.
- Do: keep CTAs short and action-led.
- Don't: transfer source-specific nouns into an unrelated project.
- Don't: present the result as official brand copy or a brand guideline.
- Don't: paste source paragraphs verbatim.
- Don't: add claims the source did not support.
