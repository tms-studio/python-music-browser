PIPENV?=pipenv

install:
	$(PIPENV) install

check-quality:
	$(PIPENV) run flake8 music_browser/

check-security:
	$(PIPENV) run bandit -r music_browser/

check-tests:
	$(PIPENV) run python -m pytest -s tests/

check: check-quality check-security check-tests
	echo "Everything OK"
