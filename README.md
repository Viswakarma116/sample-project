# Sample Project

[![CI](https://github.com/Viswakarma116/sample-project/actions/workflows/ci.yml/badge.svg)](https://github.com/Viswakarma116/sample-project/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/sample-project.svg)](https://pypi.org/project/sample-project/)
[![Python](https://img.shields.io/pypi/pyversions/sample-project.svg)](https://pypi.org/project/sample-project/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A small, dependency-free Python project demonstrating a maintainable package layout, a command-line interface, automated quality checks, and secure PyPI publishing with GitHub Actions.

## Features

- Modern `src/` package layout
- Zero runtime dependencies
- Installable command-line tool: `sample-project`
- Unit tests using the Python standard library
- Ruff linting and multi-version CI
- Release-based PyPI publishing with Trusted Publishing

## Quick start

Requires Python 3.9 or newer.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -e .
sample-project Ada
# Hello, Ada!
```

Without installing the package:

```bash
PYTHONPATH=src python -m sample_project.cli Ada
```

## Development

```bash
make check       # tests, lint, build, and repository hygiene checks
make test        # unit tests
make lint        # Ruff lint and formatting checks
make build       # source distribution and wheel
```

The project intentionally keeps runtime dependencies at zero. Development tools are installed on demand by the Makefile or CI workflow.

## Release process

1. Update the version in `pyproject.toml` and add release notes to `CHANGELOG.md`.
2. Run `make check` locally.
3. Open a pull request and merge it to `main`.
4. Create and publish a GitHub Release matching the package version.
5. GitHub Actions builds and publishes the distributions to PyPI using OIDC Trusted Publishing.

Before the first release, configure the PyPI trusted publisher and GitHub `pypi` environment as described in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Repository layout

```text
.github/                 # CI, release automation, and contribution templates
src/sample_project/      # Package source
tests/                   # Unit tests
CHANGELOG.md             # Release history
CONTRIBUTING.md          # Development and release guide
pyproject.toml           # Package metadata and tool configuration
```

## Contributing

Bug reports, feature requests, documentation improvements, and pull requests are welcome. Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) first and use the provided issue and pull request templates.

## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.
