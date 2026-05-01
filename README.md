# Python Project Template (Absolute Imports Enforced)

This is a reusable template for Python projects that enforces **absolute imports** by default.

## Features
- **Linter:** Ruff (primary), Flake8, and Pylint configurations included.
- **Import Policy:** Relative imports (e.g., `from .module import ...`) are strictly banned and will cause linting failures.
- **Structure:** Modern `src` layout.

## Getting Started

1.  Clone/Copy this directory to your new project name.
2.  Install development dependencies:
    ```bash
    pip install -r requirements-dev.txt
    ```
3.  Run the linter to verify:
    ```bash
    ruff check .
    ```

## Enforcing Absolute Imports
The template uses Ruff's `flake8-tidy-imports` rule `TID252` set to `all`.

If you try to use:
```python
from .utils import get_greeting  # FAILS
```
Ruff will report:
`TID252 Relative imports from parent modules are banned`

Instead, use:
```python
from template_package.utils import get_greeting  # PASSES
```

## Structure
- `src/template_package/`: Your package source code.
- `tests/`: Your test suite.
- `.github/workflows/ci.yml`: Cross-platform GitHub Actions pipeline.
- `pyproject.toml`: Configuration for Ruff and build system.
- `.flake8`: Fallback configuration for Flake8.
- `.pylintrc`: Fallback configuration for Pylint.

## CI/CD Pipeline
The template includes a pre-configured GitHub Actions workflow (`.github/workflows/ci.yml`) that:
1.  Runs on every push and pull request to `main` or `master`.
2.  Executes on a matrix of **Ubuntu** and **Windows**.
3.  Performs strict linting with Ruff, Flake8, and Pylint to enforce absolute imports.
4.  Runs the test suite using `pytest`.

To activate the pipeline for a new repository:
1.  Push the project code to GitHub.
2.  GitHub Actions will automatically detect the `.github/workflows/ci.yml` file and start the workflow.
