.PHONY: test example site-example bench bench-ci web-fit init-example packs

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

web-fit:
	PYTHONPATH=src python3 scripts/reference_fit_report.py --voice packs/stripe/voice.json --site packs/stripe/site.json --out examples/comparisons/stripe-ledgerflow-web/reference-fit.json --markdown examples/comparisons/stripe-ledgerflow-web/reference-fit.md examples/comparisons/stripe-ledgerflow-web/without-context.html examples/comparisons/stripe-ledgerflow-web/with-site-voice.html

init-example:
	rm -rf /tmp/site2voice-context
	PYTHONPATH=src python3 -m site2voice.cli init examples/editorial-home.html --dir /tmp/site2voice-context --no-samples

packs:
	PYTHONPATH=src python3 scripts/build_packs.py
