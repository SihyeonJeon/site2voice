.PHONY: test example bench

test:
	PYTHONPATH=src python3 -m unittest discover -s tests

example:
	PYTHONPATH=src python3 -m site2voice.cli examples/saas-home.html --out examples/saas-VOICE.md

bench:
	PYTHONPATH=src python3 -m site2voice.cli bench examples/editorial-home.html examples/before-copy.md examples/after-copy.md --out examples/editorial-benchmark.md
