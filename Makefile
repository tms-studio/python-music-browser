PIPENV?=pipenv

##@ Project's commands


help: ## Show this help
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

clean:
	rm -rf *.egg-info build/ dist/

install: ## Install development dependencies using pipenv
	$(PIPENV) install --dev

freeze: ## Freeze project dependencies
	$(PIPENV) lock -r --dev > requirements/development
	$(PIPENV) lock -r > requirements/production
	git add requirements/ && git commit -m "[Auto] Update requirements."

pypi: clean ## Manually deploy package to PyPI
	$(PIPENV) run python setup.py build bdist_wheel
	$(PIPENV) run twine upload dist/*
	make clean

##@ Commands to ensure package quality

test: ## Run non-regression tests with pytest
	$(PIPENV) run python -m pytest -s tests/

lint: ## Lint package using flake8
	$(PIPENV) run flake8 music_browser/

security: ## Check for security issue using bandit
	$(PIPENV) run bandit -r music_browser/

pre-release: test lint security ## Run all  pre-release tests
	echo "All pre-release checks passed!"

##@ Commands to manually release package

release: pre-release
	$(PIPENV) run bump2version $(type)
	git push --follow-tags

patch: ## Release a new patch version of this package
	make release type=patch

minor: ## Release a new minor version of this package
	make release type=minor

major: ## Release a new major  version of this package
	make release type=major

hotfix: ## Commit current changes, and overwrite latest release with it.
	@latest_release=$(shell git describe --tags); \
	git tag -d $$latest_release; \
	git push --delete origin $$latest_release; \
	git add . && git commit -m "[Hotfix] fix issue in release $$latest_release"; \
	git tag -am "Release $$latest_release" $$latest_release; \
	git push --follow-tags
