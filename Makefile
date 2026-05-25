.PHONY: test example site-example bench bench-ci webfit web-fit webfit-ci init-example packs

test:
	PYTHONPATH=src python3 -m unittest discover -s tests

example:
	PYTHONPATH=src python3 -m site2voice.cli examples/saas-home.html --out examples/saas-VOICE.md

site-example:
	PYTHONPATH=src python3 -m site2voice.cli site examples/saas-home.html --out examples/saas-SITE.md

bench:
	PYTHONPATH=src python3 -m site2voice.cli bench examples/editorial-home.html examples/before-copy.md examples/after-copy.md --out examples/editorial-benchmark.md

bench-ci:
	PYTHONPATH=src python3 -m site2voice.cli bench examples/editorial-home.html examples/after-copy.md --strict

webfit:
	PYTHONPATH=src python3 -m site2voice.cli webfit --voice packs/stripe/voice.json --site packs/stripe/site.json --format json --out examples/comparisons/stripe-ledgerflow-web/webfit.json examples/comparisons/stripe-ledgerflow-web/without-context.html examples/comparisons/stripe-ledgerflow-web/with-site-voice.html
	PYTHONPATH=src python3 -m site2voice.cli webfit --voice packs/stripe/voice.json --site packs/stripe/site.json --out examples/comparisons/stripe-ledgerflow-web/webfit.md examples/comparisons/stripe-ledgerflow-web/without-context.html examples/comparisons/stripe-ledgerflow-web/with-site-voice.html

web-fit: webfit

webfit-ci:
	PYTHONPATH=src python3 -m site2voice.cli webfit --voice packs/stripe/voice.json --site packs/stripe/site.json --min-delta 20 --min-copy-safety 95 --max-mimic-risk 5 examples/comparisons/stripe-ledgerflow-web/without-context.html examples/comparisons/stripe-ledgerflow-web/with-site-voice.html

init-example:
	rm -rf /tmp/site2voice-context
	PYTHONPATH=src python3 -m site2voice.cli init examples/editorial-home.html --dir /tmp/site2voice-context --no-samples

packs:
	PYTHONPATH=src python3 scripts/build_packs.py
