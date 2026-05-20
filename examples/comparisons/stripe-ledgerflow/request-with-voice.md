# Request With VOICE.md

This request used the same task prompt, with `packs/stripe/VOICE.md` provided as additional context above it.

---

# VOICE.md

Source: `https://stripe.com/`

Use this file to keep AI-generated pages, docs, and UI copy aligned with the observed website voice.

## Voice Summary

- Overall tone: **balanced, action-oriented**.
- Sentence shape: about **15.7 words** per sentence.
- Main vocabulary: `stripe`, `read`, `payments`, `story`, `financial`, `business`, `how`, `commerce`, `products`, `crypto`, `billing`, `businesses`.
- Common CTAs: `Sign in`, `Start now`, `Contact sales`, `Get started`, `Sign up with Google`, `Create a card issuing program`, `Watch now`, `Explore no-code`.
- Navigation labels: `Pricing`, `Sign in`, `Start now`, `Contact sales`, `Get started`, `Sign up with Google`, `Watch now`, `historical uptime`, `Stripe for enterprises`, `Read the story`.

## Style Fingerprint

- Heading shape: about **7.2 words** per heading.
- Paragraph rhythm: about **7.8 words** per paragraph sample.
- CTA shape: about **2.6 words** per CTA.
- CTA verbs: `sign`, `start`, `contact`, `get`, `create`, `watch`, `explore`, `see`.
- Lexical variety: **0.301** type-token ratio.

## Agent Rules

- Start with a concrete user outcome before describing implementation details.
- Prefer short active sentences and visible verbs from the CTA list.
- Reuse the observed vocabulary, but do not copy full marketing paragraphs.
- Keep headings specific; avoid generic labels like `Powerful features` unless the source uses that pattern.
- When adding new sections, match the observed information order: headline, proof, action, details.
- Do not invent compliance, security, customer, or performance claims that are not present in the source.

## Evidence

| Signal | Value |
| --- | --- |
| Words | 1748 |
| Sentences | 111 |
| Headings | 12 |
| CTA candidates | 12 |

## Do / Don't

- Do: write concise, outcome-first copy using the observed verbs and nouns.
- Do: keep CTAs short and action-led.
- Don't: paste source paragraphs verbatim.
- Don't: add claims the source did not support.

---

# Task Prompt

Write landing page copy for LedgerFlow, a fictional B2B payments observability platform for finance and engineering teams.

Output Markdown only. Include:

- nav labels;
- hero headline and subheadline;
- two primary CTAs;
- four feature sections, each with a heading and one sentence;
- one proof section;
- one final CTA.

Do not mention any real company or source website. Do not claim certifications, customers, compliance, or uptime.

If a VOICE.md file is provided above this task, follow it for tone, sentence rhythm, CTA style, and vocabulary. If no VOICE.md is provided, write from the product brief alone.

