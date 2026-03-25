"""CLI for the Shortcut Python client."""

import functools
import json
import os
import sys

import click
import httpx
from rich.console import Console
from rich.table import Table
from rich.text import Text

from shortcut_python_client.client import ShortcutClient
from shortcut_python_client.models import CreateStoryParams, UpdateStory

console = Console()


def get_client() -> ShortcutClient:
    """Create a ShortcutClient from the SHORTCUT_API_TOKEN env var."""
    token = os.environ.get("SHORTCUT_API_TOKEN")
    if not token:
        click.echo("Error: SHORTCUT_API_TOKEN environment variable is not set.", err=True)
        sys.exit(1)
    return ShortcutClient(api_token=token)


def handle_api_errors(func):
    """Decorator to catch HTTP errors and print a user-friendly message."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except httpx.HTTPStatusError as e:
            click.echo(f"API error {e.response.status_code}: {e.response.text}", err=True)
            sys.exit(1)

    return wrapper


def pretty_option(func):
    """Add --pretty flag to a command."""
    return click.option("--pretty", is_flag=True, default=False, help="Output as a rich table instead of JSON.")(func)


def output_json(data):
    """Print data as formatted JSON. Accepts a pydantic model or list of models."""
    if isinstance(data, list):
        click.echo(json.dumps([item.model_dump(mode="json") for item in data], default=str, indent=2))
    else:
        click.echo(data.model_dump_json(indent=2))


def _str(value) -> str:
    """Convert a value to string for table display."""
    if value is None:
        return ""
    return str(value)


def _color_cell(hex_color: str | None) -> Text:
    """Render a color swatch followed by the hex code using rich Text."""
    if not hex_color:
        return Text("")
    text = Text()
    text.append("\u2588\u2588 ", style=hex_color)
    text.append(hex_color)
    return text


# --- Root group ---


@click.group()
def cli():
    """Shortcut CLI - interact with your Shortcut workspace from the terminal."""


# --- me ---


@cli.command()
@pretty_option
@handle_api_errors
def me(pretty):
    """Show current member info."""
    client = get_client()
    info = client.get_current_member_info()
    if not pretty:
        output_json(info)
        return
    table = Table(title="Current Member")
    table.add_column("Field", style="bold")
    table.add_column("Value")
    table.add_row("ID", info.id)
    table.add_row("Name", info.name)
    table.add_row("Mention Name", f"@{info.mention_name}")
    table.add_row("Role", info.role)
    console.print(table)


# --- search ---


@cli.command()
@click.argument("query")
@pretty_option
@handle_api_errors
def search(query, pretty):
    """Search stories by query string."""
    client = get_client()
    results = client.search_stories(query=query)
    if not pretty:
        output_json(results.data)
        return
    table = Table(title=f"Search Results ({results.total} total)")
    table.add_column("ID", style="bold")
    table.add_column("Type")
    table.add_column("Name")
    table.add_column("Started")
    table.add_column("Completed")
    for story in results.data:
        table.add_row(_str(story.id), story.story_type, story.name, _str(story.started), _str(story.completed))
    console.print(table)


# --- stories ---


@cli.group()
def stories():
    """Manage stories."""


@stories.command("list")
@click.option("--project-id", type=int, default=None, help="List stories for a project.")
@click.option("--label", "label_names", multiple=True, help="Filter by label name (repeatable, must have ALL).")
@click.option("--iteration-id", type=int, default=None, help="List stories for an iteration.")
@pretty_option
@handle_api_errors
def stories_list(project_id, label_names, iteration_id, pretty):
    """List stories, filtered by project, label(s), or iteration."""
    if not project_id and not label_names and not iteration_id:
        click.echo("Error: provide at least one of --project-id, --label, or --iteration-id.", err=True)
        sys.exit(1)

    client = get_client()
    result_sets: list[set[int]] = []
    all_stories: dict[int, object] = {}

    if project_id is not None:
        items = client.list_stories(project_id)
        for s in items:
            all_stories[s.id] = s
        result_sets.append({s.id for s in items})

    if label_names:
        labels = client.list_labels()
        label_map = {label.name.lower(): label for label in labels}
        for name in label_names:
            matched_label = label_map.get(name.lower())
            if not matched_label:
                click.echo(f"Error: label '{name}' not found.", err=True)
                sys.exit(1)
            items = client.list_label_stories(matched_label.id)
            for s in items:
                all_stories[s.id] = s
            result_sets.append({s.id for s in items})

    if iteration_id is not None:
        items = client.list_iteration_stories(iteration_id)
        for s in items:
            all_stories[s.id] = s
        result_sets.append({s.id for s in items})

    story_ids = result_sets[0]
    for s in result_sets[1:]:
        story_ids &= s

    stories_result = [all_stories[sid] for sid in story_ids]

    if not pretty:
        output_json(stories_result)
        return
    table = Table(title="Stories")
    table.add_column("ID", style="bold")
    table.add_column("Type")
    table.add_column("Name")
    table.add_column("Labels")
    table.add_column("Estimate")
    table.add_column("Started")
    table.add_column("Completed")
    for s in stories_result:
        labels_str = ", ".join(label.name for label in s.labels)
        table.add_row(
            _str(s.id), s.story_type, s.name, labels_str, _str(s.estimate), _str(s.started), _str(s.completed)
        )
    console.print(table)


@stories.command("get")
@click.argument("story_id", type=int)
@pretty_option
@handle_api_errors
def stories_get(story_id, pretty):
    """Get a story by ID."""
    client = get_client()
    story = client.get_story(story_id)
    if not pretty:
        output_json(story)
        return
    table = Table(title=f"Story {story.id}")
    table.add_column("Field", style="bold")
    table.add_column("Value")
    table.add_row("ID", _str(story.id))
    table.add_row("Name", story.name)
    table.add_row("Type", story.story_type)
    table.add_row("URL", story.app_url)
    table.add_row("Estimate", _str(story.estimate))
    table.add_row("Epic ID", _str(story.epic_id))
    table.add_row("Project ID", _str(story.project_id))
    table.add_row("Workflow State ID", _str(story.workflow_state_id))
    table.add_row("Started", _str(story.started))
    table.add_row("Completed", _str(story.completed))
    table.add_row("Created", _str(story.created_at))
    table.add_row("Labels", ", ".join(label.name for label in story.labels))
    console.print(table)


@stories.command("create")
@click.option("--name", required=True, help="Story name.")
@click.option("--project-id", type=int, default=None, help="Project ID.")
@click.option("--type", "story_type", type=click.Choice(["feature", "bug", "chore"]), default=None, help="Story type.")
@click.option("--description", default=None, help="Story description.")
@click.option("--epic-id", type=int, default=None, help="Epic ID.")
@click.option("--iteration-id", type=int, default=None, help="Iteration ID.")
@click.option("--workflow-state-id", type=int, default=None, help="Workflow state ID.")
@click.option("--estimate", type=int, default=None, help="Point estimate.")
@pretty_option
@handle_api_errors
def stories_create(
    name, project_id, story_type, description, epic_id, iteration_id, workflow_state_id, estimate, pretty
):
    """Create a new story."""
    client = get_client()
    data = CreateStoryParams(
        name=name,
        project_id=project_id,
        story_type=story_type,
        description=description,
        epic_id=epic_id,
        iteration_id=iteration_id,
        workflow_state_id=workflow_state_id,
        estimate=estimate,
    )
    story = client.create_story(data)
    if not pretty:
        output_json(story)
        return
    click.echo(f"Created story {story.id}: {story.name}")
    click.echo(f"URL: {story.app_url}")


@stories.command("update")
@click.argument("story_id", type=int)
@click.option("--name", default=None, help="Story name.")
@click.option("--type", "story_type", type=click.Choice(["feature", "bug", "chore"]), default=None, help="Story type.")
@click.option("--description", default=None, help="Story description.")
@click.option("--epic-id", type=int, default=None, help="Epic ID.")
@click.option("--project-id", type=int, default=None, help="Project ID.")
@click.option("--workflow-state-id", type=int, default=None, help="Workflow state ID.")
@click.option("--estimate", type=int, default=None, help="Point estimate.")
@pretty_option
@handle_api_errors
def stories_update(story_id, name, story_type, description, epic_id, project_id, workflow_state_id, estimate, pretty):
    """Update an existing story."""
    client = get_client()
    data = UpdateStory(
        name=name,
        story_type=story_type,
        description=description,
        epic_id=epic_id,
        project_id=project_id,
        workflow_state_id=workflow_state_id,
        estimate=estimate,
    )
    story = client.update_story(story_id, data)
    if not pretty:
        output_json(story)
        return
    click.echo(f"Updated story {story.id}: {story.name}")
    click.echo(f"URL: {story.app_url}")


# --- epics ---


@cli.group()
def epics():
    """Manage epics."""


@epics.command("list")
@pretty_option
@handle_api_errors
def epics_list(pretty):
    """List all epics."""
    client = get_client()
    items = client.list_epics()
    if not pretty:
        output_json(items)
        return
    table = Table(title="Epics")
    table.add_column("ID", style="bold")
    table.add_column("Name")
    table.add_column("State")
    table.add_column("Started")
    table.add_column("Completed")
    for e in items:
        table.add_row(_str(e.id), e.name, e.state, _str(e.started), _str(e.completed))
    console.print(table)


@epics.command("get")
@click.argument("epic_id", type=int)
@pretty_option
@handle_api_errors
def epics_get(epic_id, pretty):
    """Get an epic by ID."""
    client = get_client()
    epic = client.get_epic(epic_id)
    if not pretty:
        output_json(epic)
        return
    table = Table(title=f"Epic {epic.id}")
    table.add_column("Field", style="bold")
    table.add_column("Value")
    table.add_row("ID", _str(epic.id))
    table.add_row("Name", epic.name)
    table.add_row("URL", epic.app_url)
    table.add_row("State", epic.state)
    table.add_row("Started", _str(epic.started))
    table.add_row("Completed", _str(epic.completed))
    table.add_row("Deadline", _str(epic.deadline))
    table.add_row("Labels", ", ".join(label.name for label in epic.labels))
    console.print(table)


# --- projects ---


@cli.group()
def projects():
    """Manage projects."""


@projects.command("list")
@pretty_option
@handle_api_errors
def projects_list(pretty):
    """List all projects."""
    client = get_client()
    items = client.list_projects()
    if not pretty:
        output_json(items)
        return
    table = Table(title="Projects")
    table.add_column("ID", style="bold")
    table.add_column("Name")
    table.add_column("Archived")
    for p in items:
        table.add_row(_str(p.id), p.name, _str(p.archived))
    console.print(table)


# --- workflows ---


@cli.group()
def workflows():
    """Manage workflows."""


@workflows.command("list")
@pretty_option
@handle_api_errors
def workflows_list(pretty):
    """List all workflows."""
    client = get_client()
    items = client.list_workflows()
    if not pretty:
        output_json(items)
        return
    table = Table(title="Workflows")
    table.add_column("ID", style="bold")
    table.add_column("Name")
    table.add_column("States")
    for w in items:
        states = ", ".join(f"{s.name} ({s.type})" for s in w.states)
        table.add_row(_str(w.id), w.name, states)
    console.print(table)


# --- members ---


@cli.group()
def members():
    """Manage members."""


@members.command("list")
@pretty_option
@handle_api_errors
def members_list(pretty):
    """List all members."""
    client = get_client()
    items = client.list_members()
    if not pretty:
        output_json(items)
        return
    table = Table(title="Members")
    table.add_column("ID", style="bold")
    table.add_column("Name")
    table.add_column("Mention Name")
    table.add_column("Role")
    table.add_column("Disabled")
    for m in items:
        table.add_row(m.id, m.profile.name or "", f"@{m.profile.mention_name}", m.role, _str(m.disabled))
    console.print(table)


# --- iterations ---


@cli.group()
def iterations():
    """Manage iterations."""


@iterations.command("list")
@pretty_option
@handle_api_errors
def iterations_list(pretty):
    """List all iterations."""
    client = get_client()
    items = client.list_iterations()
    if not pretty:
        output_json(items)
        return
    table = Table(title="Iterations")
    table.add_column("ID", style="bold")
    table.add_column("Name")
    table.add_column("Status")
    table.add_column("Start Date")
    table.add_column("End Date")
    for i in items:
        table.add_row(_str(i.id), i.name, i.status, _str(i.start_date.date()), _str(i.end_date.date()))
    console.print(table)


# --- labels ---


@cli.group()
def labels():
    """Manage labels."""


@labels.command("list")
@click.option("--name", "name_filter", default=None, help="Filter labels by name (case-insensitive substring match).")
@pretty_option
@handle_api_errors
def labels_list(name_filter, pretty):
    """List all labels."""
    client = get_client()
    items = client.list_labels()
    if name_filter:
        name_lower = name_filter.lower()
        items = [label for label in items if name_lower in label.name.lower()]
    if not pretty:
        output_json(items)
        return
    table = Table(title="Labels")
    table.add_column("ID", style="bold")
    table.add_column("Name")
    table.add_column("Color")
    table.add_column("Archived")
    for label in items:
        table.add_row(_str(label.id), label.name, _color_cell(label.color), _str(label.archived))
    console.print(table)
