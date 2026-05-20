.PHONY: test example

test:
	PYTHONPATH=src python3 -m unittest discover -s tests

example:
	PYTHONPATH=src python3 -m site2voice.cli examples/saas-home.html --out examples/saas-VOICE.md
