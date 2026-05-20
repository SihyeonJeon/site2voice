# VOICE.md

Source: `examples/saas-home.html`

Use this file to keep AI-generated pages, docs, and UI copy aligned with the observed website voice.

## Voice Summary

- Overall tone: **explanatory, action-oriented, trust-forward**.
- Sentence shape: about **20.4 words** per sentence.
- Content policy: this file captures rhythm and structure, not source nouns.

## Style Fingerprint

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
- Keep headings specific; avoid generic labels like `<generic feature label>` unless the source uses that pattern.
- When adding new sections, match the observed information order: headline, proof, action, details.
- Do not invent compliance, security, customer, or performance claims that are not present in the source.

## Output Contract

- Keep average sentence length between **15.3 and 25.5 words**.
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
| Sentences | 5 |
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
- Don't: paste source paragraphs verbatim.
- Don't: add claims the source did not support.
