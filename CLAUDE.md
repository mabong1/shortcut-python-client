# CLAUDE.md

## Project overview

**shortcut-python-client** is a Python SDK for the Shortcut (project management) REST API v3. It provides:

- Auto-generated typed Pydantic models and HTTP client from `shortcut.openapi.json`
- A Click-based CLI (`shortcut` command)
- Python 3.13+, MIT license, version 0.1.0

## Project structure

```
bin/generate.py              # Code generator: OpenAPI spec -> client.py + models.py
shortcut_python_client/
  __init__.py                # Package exports
  client.py                  # Auto-generated ShortcutClient (httpx-based, ~1200 lines)
  models.py                  # Auto-generated Pydantic v2 models (~2900 lines)
  cli.py                     # Hand-written CLI (Click + Rich)
tests/
  test_main.py               # Client tests
  test_cli.py                # CLI tests (mocked, CliRunner-based)
shortcut.openapi.json        # Source OpenAPI 3.0 spec
Makefile                     # Dev workflow commands
```

## Key commands

```bash
make install       # uv sync
make test          # pytest
make cov           # pytest with coverage
make check         # ruff lint
make format        # ruff fix + format
make generate      # regenerate client.py & models.py from OpenAPI spec, then ruff
```

## Dependencies

- **Runtime:** httpx, pydantic (v2), click, rich
- **Dev:** pytest, pytest-cov, ruff, pre-commit
- **Build:** hatchling
- **Package manager:** uv

## Code conventions

- **Line length:** 120 characters
- **Target:** Python 3.13 (ruff target-version)
- **Do NOT use** `from __future__ import annotations` — project targets 3.13+ where `X | Y` works natively
- `client.py` and `models.py` are **generated** — edit `bin/generate.py` instead, then `make generate`
- `cli.py` and tests are **hand-written**
- Models use `ConfigDict(populate_by_name=True)`, `Field(alias=...)` for snake_case/original-name compat
- Nullable fields: `X | None = Field(default=None)`
- CLI uses `@pretty_option` / `@handle_api_errors` decorators, outputs JSON by default or Rich tables with `--pretty`
- Tests mock the client via `@patch("shortcut_python_client.cli.get_client")`

## Authentication

`SHORTCUT_API_TOKEN` env var, passed as `Shortcut-Token` header.

## Pre-commit hooks

Ruff check (with `--fix`) and ruff format run automatically on commit.
