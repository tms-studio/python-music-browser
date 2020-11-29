PIPENV?=pipenv

install:
	$(PIPENV) install

lint:
	$(PIPENV) run flake8 music_browser/

test:
	$(PIPENV) run python -m pytest -s tests/
