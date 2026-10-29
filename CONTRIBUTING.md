# Contributing

Thank you for helping improve Sample Project. Bug reports, feature requests, documentation fixes, and focused pull requests are welcome.

## Local setup

```bash
git clone https://github.com/Viswakarma116/sample-project.git
cd sample-project
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -e .
```

## Before opening a pull request

Run the complete local quality gate:

```bash
make check
```

If `make` is unavailable, run the commands described in the README manually. Keep pull requests focused, add or update tests for behavior changes, update documentation when needed, and add a changelog entry for user-visible changes.

## Commit and pull request guidance

- Use a clear, imperative commit subject, such as `Add greeting option`.
- Explain the motivation and approach in the pull request description.
- Link related issues when applicable.
- Do not commit credentials, generated distributions, or local environment files.

## Release process

1. Update `version` in `pyproject.toml` using semantic versioning.
2. Add release notes under `Unreleased` in `CHANGELOG.md` and move them into a new version section.
3. Run `make check` and merge the pull request.
4. Create and publish a GitHub Release with the same version tag.
5. The publish workflow builds and uploads the package through PyPI Trusted Publishing.

The PyPI trusted publisher must be configured for owner `Viswakarma116`, repository `sample-project`, workflow `publish.yml`, and GitHub environment `pypi` before the first release.
