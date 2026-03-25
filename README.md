# shortcut-python-client

Python client for the [Shortcut](https://shortcut.com) REST API v3.

## Installation

```bash
pip install shortcut-python-client
```

## Usage

```python
from shortcut_python_client import ShortcutClient

client = ShortcutClient("your-api-token")

# List all projects
projects = client.list_projects()
for project in projects:
    print(project.name)

# Create a story
from shortcut_python_client import CreateStoryParams

story = client.create_story(CreateStoryParams(
    name="My new story",
    story_type="feature",
    workflow_state_id=500000001,
))
print(story.id, story.app_url)

# Search stories
results = client.search_stories(query="bug fix")
for story in results.data:
    print(story.name)

# Update a story
from shortcut_python_client import UpdateStory

updated = client.update_story(story.id, UpdateStory(name="Renamed story"))

# Use as context manager
with ShortcutClient("your-api-token") as client:
    members = client.list_members()
```

## Authentication

Get your API token from **Settings > API Tokens** in your Shortcut workspace. The token is sent via the `Shortcut-Token` header.

## Code generation

The client is generated from the [Shortcut OpenAPI spec](https://developer.shortcut.com/api/rest/v3/shortcut.openapi.json):

```bash
# Regenerate models and client from the spec
python bin/generate.py
```

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
shortcut_python_client/
    __init__.py        # Package exports
    client.py          # ShortcutClient with all API methods (generated)
    models.py          # Pydantic models for all schemas (generated)
bin/
    generate.py        # Code generator script
tests/                 # Tests
pyproject.toml         # Project configuration
Makefile               # Development commands
```

---

This project was generated with the help of AI (Claude).
