# Web Output Reference Fit

Reference source: `https://stripe.com/`
Reference archetype: **technical product landing**

This report compares visible web outputs against the same reference context.
`Reference fit` rewards safe structural and copy alignment. `Mimic risk` should stay low.

## Scores

| Candidate | Reference fit | Structure | Voice | Copy safety | Claim safety | Mimic risk | Observed slots |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| [without-context](without-context.html) | 63.2 | 74.5 | 49.2 | 100.0 | 50.0 | 0.0 | `navigation`, `first_screen`, `capability_stack`, `proof_band`, `conversion_band`, `footer` |
| [with-site-voice](with-site-voice.html) | 92.1 | 95.8 | 89.4 | 100.0 | 75.0 | 0.0 | `navigation`, `first_screen`, `capability_stack`, `proof_band`, `detail_sections`, `conversion_band`, `footer` |

## Interpretation

- `with-site-voice` should score higher on structure and voice when the same prompt receives `SITE.md` and `VOICE.md` as context.
- `without-context` can still look polished, but it is more likely to use generic layout, generic proof, and unsupported claims.
- A high reference-fit score is only useful when copy safety and claim safety remain high.
