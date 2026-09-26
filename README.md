# Sample Project

A small, dependency-free Python project demonstrating a clean repository structure, a command-line entry point, and automated tests.

## Project structure

```text
sample-project/
├── .github/workflows/ci.yml  # Continuous integration
├── src/sample_project/       # Application package
├── tests/                    # Unit tests
├── pyproject.toml            # Build and package metadata
└── README.md
```

## Run locally

```bash
PYTHONPATH=src python -m sample_project.cli Ada
# Hello, Ada!
```

## Run tests

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

## License

Released under the MIT License.
