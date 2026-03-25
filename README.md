# shortcut-python-client

Python client for https://shortcut.com to interact with their API

## Setup

```bash
make install
uv run pre-commit install
```

## Development

```bash
make test            # Run tests
make cov             # Run tests with coverage
make check           # Lint with ruff
make format          # Format code with ruff
make format-check    # Check formatting without modifying
```

## Project structure

```
shortcut_python_client/    # Source code
tests/                              # Tests
pyproject.toml                      # Project configuration
Makefile                            # Development commands
```
