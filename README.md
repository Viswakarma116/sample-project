# Sample Project

A small, dependency-free Python project demonstrating a clean repository structure, a command-line entry point, automated tests, and secure publishing to PyPI with GitHub Actions.

## Project structure

```text
sample-project/
├── .github/workflows/ci.yml       # Test and compile checks
├── .github/workflows/publish.yml  # PyPI CD workflow
├── src/sample_project/             # Application package
├── tests/                          # Unit tests
├── pyproject.toml                  # Build and package metadata
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

## Configure PyPI publishing

The publish workflow uses **PyPI Trusted Publishing** through GitHub's OIDC identity token. No long-lived PyPI API token is stored in the repository.

One-time setup for the repository owner:

1. Create the `sample-project` project on PyPI, or register it as a pending publisher.
2. In PyPI, add a trusted publisher for this GitHub repository:
   - Owner: `Viswakarma116`
   - Repository: `sample-project`
   - Workflow: `publish.yml`
   - Environment: `pypi`
3. Create a GitHub environment named `pypi` under **Settings → Environments**. Add an optional required reviewer for release approval.
4. Update the version in `pyproject.toml` before each release.
5. Create and publish a GitHub Release. The `publish.yml` workflow will build the package and publish it to PyPI automatically.

The workflow is intentionally triggered by **published GitHub Releases**, rather than every push, so normal development cannot publish an unintended package.

## License

Released under the MIT License.
