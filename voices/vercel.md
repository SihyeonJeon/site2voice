# VOICE.md

Source: `https://vercel.com/`

Use this file to keep AI-generated pages, docs, and UI copy aligned with the observed website voice.

## Voice Summary

- Overall tone: **explanatory, action-oriented, technical, trust-forward**.
- Sentence shape: about **34.5 words** per sentence.
- Main vocabulary: `web`, `apps`, `scale`, `platform`, `deploy`, `vercel`, `protection`, `next`, `one`, `ship`, `fast`, `help`.
- Common CTAs: `v0 Build applications with AI`, `Changelog See what shipped`, `Events Join us at an event`, `Community Join the conversation`, `Sign Up`, `Get your ticket`, `Deploy Start Deploying`, `Get a Demo`.
- Navigation labels: `Skip to content`, `AI Cloud`, `Sandbox Isolated, safe code execution`, `v0 Build applications with AI`, `CI/CD Helping teams ship 6× faster`, `Content Delivery Fast, scalable, and reliable`, `Fluid Compute Servers, in serverless form`, `Workflow Long-running workflows at scale`, `Observability Trace every step`, `Security`.

## Style Fingerprint

- Heading shape: about **2.6 words** per heading.
- Paragraph rhythm: about **4.5 words** per paragraph sample.
- CTA shape: about **3.9 words** per CTA.
- CTA verbs: `v0`, `changelog`, `events`, `community`, `sign`, `get`, `deploy`, `learn`.
- Lexical variety: **0.171** type-token ratio.

## Agent Rules

- Start with a concrete user outcome before describing implementation details.
- Prefer short active sentences and visible verbs from the CTA list.
- Reuse the observed vocabulary, but do not copy full marketing paragraphs.
- Keep headings specific; avoid generic labels like `Powerful features` unless the source uses that pattern.
- When adding new sections, match the observed information order: headline, proof, action, details.
- Do not invent compliance, security, customer, or performance claims that are not present in the source.

## Output Contract

- Keep average sentence length between **25.9 and 43.1 words**.
- Keep headings near **2.6 words**; avoid generic one-word section labels unless the source uses them.
- Keep paragraph blocks near **4.5 words**.
- Keep CTAs near **3.9 words** and start them with: `v0`, `changelog`, `events`, `community`, `sign`, `get`, `deploy`, `learn`.
- Use at least **4** of these terms where natural: `web`, `apps`, `scale`, `platform`, `deploy`, `vercel`, `protection`, `next`, `one`, `ship`, `fast`, `help`.
- Keep the first screen structure close to: specific headline, short proof/value sentence, one or two action CTAs.
- If writing a candidate file, run:
  `site2voice bench https://vercel.com/ path/to/candidate.md --strict`
- Revise until overall >= **75**, copy safety >= **85**, and claim safety >= **75**.

## Evidence

| Signal | Value |
| --- | --- |
| Words | 2033 |
| Sentences | 59 |
| Headings | 12 |
| CTA candidates | 11 |

## Do / Don't

- Do: write concise, outcome-first copy using the observed verbs and nouns.
- Do: keep CTAs short and action-led.
- Don't: paste source paragraphs verbatim.
- Don't: add claims the source did not support.
