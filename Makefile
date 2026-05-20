.PHONY: test example bench bench-ci init-example

test:
	PYTHONPATH=src python3 -m unittest discover -s tests

example:
	PYTHONPATH=src python3 -m site2voice.cli examples/saas-home.html --out examples/saas-VOICE.md

bench:
	PYTHONPATH=src python3 -m site2voice.cli bench examples/editorial-home.html examples/before-copy.md examples/after-copy.md --out examples/editorial-benchmark.md

bench-ci:
	PYTHONPATH=src python3 -m site2voice.cli bench examples/editorial-home.html examples/after-copy.md --strict

init-example:
	rm -rf /tmp/site2voice-context
	PYTHONPATH=src python3 -m site2voice.cli init examples/editorial-home.html --dir /tmp/site2voice-context --no-samples
