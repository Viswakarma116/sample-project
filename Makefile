PYTHON ?= python3
PIP ?= $(PYTHON) -m pip

.PHONY: check test lint format build clean

check: test lint build
	@git diff --check
	@echo "All checks passed."

test:
	PYTHONPATH=src $(PYTHON) -m unittest discover -s tests -v

lint:
	$(PIP) install --quiet ruff
	ruff check .
	ruff format --check .

format:
	$(PIP) install --quiet ruff
	ruff check --fix .
	ruff format .

build:
	$(PIP) install --quiet build
	$(PYTHON) -m build

clean:
	rm -rf build dist *.egg-info src/*.egg-info src/sample_project.egg-info
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
