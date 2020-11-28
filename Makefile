PYTHON?=.venv/bin/python

lint:
	$(PYTHON) -m flake8 music_browser/

test:
	$(PYTHON) -m pytest -s tests/
