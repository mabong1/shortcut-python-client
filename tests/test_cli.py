import json
from unittest.mock import MagicMock, patch

from click.testing import CliRunner

from shortcut_python_client.cli import cli
from shortcut_python_client.models import (
    BasicWorkspaceInfo,
    Icon,
    IterationSlim,
    IterationStats,
    Label,
    LabelSlim,
    Member,
    MemberInfo,
    MemberInfoOrganization2,
    Profile,
    Project,
    ProjectStats,
    StorySearchResult,
    StorySearchResults,
    StorySlim,
    StoryStats,
    Workflow,
    WorkflowState,
)


def make_runner():
    return CliRunner(env={"SHORTCUT_API_TOKEN": "test-token"})


def make_member_info():
    return MemberInfo(
        id="user-1",
        is_owner=True,
        mention_name="alice",
        name="Alice",
        role="admin",
        workspace2=BasicWorkspaceInfo(
            id="ws-1",
            created_at="2024-01-01T00:00:00Z",
            default_workflow_id=1,
            estimate_scale=[1, 2, 3],
            name="My Workspace",
            url_slug="my-ws",
            utc_offset="+00:00",
        ),
        organization2=MemberInfoOrganization2(id="org-1"),
    )


def make_story_slim(**overrides):
    defaults = dict(
        app_url="https://app.shortcut.com/story/1",
        archived=False,
        started=True,
        story_links=[],
        entity_type="story",
        labels=[],
        task_ids=[],
        mention_ids=[],
        member_mention_ids=[],
        story_type="feature",
        file_ids=[],
        num_tasks_completed=0,
        workflow_id=1,
        completed_at_override=None,
        started_at=None,
        completed_at=None,
        name="Test Story",
        global_id="g1",
        completed=False,
        blocker=False,
        epic_id=None,
        story_template_id=None,
        external_links=[],
        previous_iteration_ids=[],
        requested_by_id="user-1",
        iteration_id=None,
        label_ids=[],
        started_at_override=None,
        group_id=None,
        workflow_state_id=1,
        updated_at=None,
        group_mention_ids=[],
        follower_ids=[],
        owner_ids=[],
        external_id=None,
        id=1,
        estimate=3,
        position=1,
        blocked=False,
        project_id=10,
        linked_file_ids=[],
        deadline=None,
        stats=StoryStats(num_related_documents=0),
        comment_ids=[],
        created_at="2024-01-01T00:00:00Z",
        moved_at=None,
    )
    defaults.update(overrides)
    return StorySlim(**defaults)


def make_project():
    return Project(
        app_url="https://app.shortcut.com/project/10",
        description="A project",
        archived=False,
        entity_type="project",
        days_to_thermometer=60,
        color="#000",
        workflow_id=1,
        name="Backend",
        global_id="gp1",
        start_time="2024-01-01T00:00:00Z",
        updated_at=None,
        follower_ids=[],
        external_id=None,
        id=10,
        show_thermometer=True,
        team_id=1,
        iteration_length=2,
        abbreviation="BE",
        stats=ProjectStats(num_related_documents=0, num_stories=5, num_points=10),
        created_at=None,
    )


def make_label(**overrides):
    defaults = dict(
        app_url="https://app.shortcut.com/label/1",
        description="Bug label",
        archived=False,
        entity_type="label",
        color="#ff0000",
        name="bug",
        global_id="gl1",
        updated_at=None,
        external_id=None,
        id=1,
        stats=None,
        created_at=None,
    )
    defaults.update(overrides)
    return Label(**defaults)


def make_icon():
    return Icon(
        entity_type="icon",
        id="icon-1",
        created_at="2024-01-01T00:00:00Z",
        updated_at="2024-01-01T00:00:00Z",
        url="https://example.com/icon.png",
    )


# --- me ---


@patch("shortcut_python_client.cli.get_client")
def test_me_json_default(mock_get_client):
    client = MagicMock()
    client.get_current_member_info.return_value = make_member_info()
    mock_get_client.return_value = client

    runner = make_runner()
    result = runner.invoke(cli, ["me"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert data["name"] == "Alice"
    assert data["mention_name"] == "alice"


@patch("shortcut_python_client.cli.get_client")
def test_me_pretty(mock_get_client):
    client = MagicMock()
    client.get_current_member_info.return_value = make_member_info()
    mock_get_client.return_value = client

    runner = make_runner()
    result = runner.invoke(cli, ["me", "--pretty"])
    assert result.exit_code == 0
    assert "Alice" in result.output
    assert "@alice" in result.output


# --- stories list ---


@patch("shortcut_python_client.cli.get_client")
def test_stories_list_by_project(mock_get_client):
    client = MagicMock()
    client.list_stories.return_value = [make_story_slim()]
    mock_get_client.return_value = client

    runner = make_runner()
    result = runner.invoke(cli, ["stories", "list", "--project-id", "10"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert len(data) == 1
    assert data[0]["name"] == "Test Story"


@patch("shortcut_python_client.cli.get_client")
def test_stories_list_by_project_pretty(mock_get_client):
    client = MagicMock()
    client.list_stories.return_value = [make_story_slim()]
    mock_get_client.return_value = client

    runner = make_runner()
    result = runner.invoke(cli, ["stories", "list", "--project-id", "10", "--pretty"])
    assert result.exit_code == 0
    assert "Test Story" in result.output


@patch("shortcut_python_client.cli.get_client")
def test_stories_list_by_label(mock_get_client):
    client = MagicMock()
    label = make_label()
    client.list_labels.return_value = [label]
    label_slim = LabelSlim(
        app_url="https://app.shortcut.com/label/1",
        description="Bug label",
        archived=False,
        entity_type="label",
        color="#ff0000",
        name="bug",
        global_id="gl1",
        updated_at=None,
        external_id=None,
        id=1,
        created_at=None,
    )
    client.list_label_stories.return_value = [make_story_slim(labels=[label_slim])]
    mock_get_client.return_value = client

    runner = make_runner()
    result = runner.invoke(cli, ["stories", "list", "--label", "bug"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert len(data) == 1
    assert data[0]["name"] == "Test Story"
    client.list_label_stories.assert_called_once_with(1)


@patch("shortcut_python_client.cli.get_client")
def test_stories_list_by_iteration(mock_get_client):
    client = MagicMock()
    client.list_iteration_stories.return_value = [make_story_slim()]
    mock_get_client.return_value = client

    runner = make_runner()
    result = runner.invoke(cli, ["stories", "list", "--iteration-id", "5"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert len(data) == 1
    client.list_iteration_stories.assert_called_once_with(5)


@patch("shortcut_python_client.cli.get_client")
def test_stories_list_by_multiple_labels_intersects(mock_get_client):
    """Stories must have ALL specified labels."""
    client = MagicMock()
    label_bug = make_label(id=1, name="bug")
    label_urgent = make_label(id=2, name="urgent", global_id="gl2", app_url="https://app.shortcut.com/label/2")
    client.list_labels.return_value = [label_bug, label_urgent]

    story_both = make_story_slim(id=1, name="Both Labels")
    story_bug_only = make_story_slim(id=2, name="Bug Only")

    client.list_label_stories.side_effect = [
        [story_both, story_bug_only],  # bug label
        [story_both],  # urgent label
    ]
    mock_get_client.return_value = client

    runner = make_runner()
    result = runner.invoke(cli, ["stories", "list", "--label", "bug", "--label", "urgent"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert len(data) == 1
    assert data[0]["name"] == "Both Labels"


def test_stories_list_no_filter():
    runner = make_runner()
    result = runner.invoke(cli, ["stories", "list"])
    assert result.exit_code != 0


@patch("shortcut_python_client.cli.get_client")
def test_stories_list_label_not_found(mock_get_client):
    client = MagicMock()
    client.list_labels.return_value = [make_label()]
    mock_get_client.return_value = client

    runner = make_runner()
    result = runner.invoke(cli, ["stories", "list", "--label", "nonexistent"])
    assert result.exit_code != 0


# --- search ---


@patch("shortcut_python_client.cli.get_client")
def test_search(mock_get_client):
    search_result = StorySearchResult(
        app_url="https://app.shortcut.com/story/1",
        archived=False,
        started=True,
        story_links=[],
        entity_type="story",
        labels=[],
        mention_ids=[],
        member_mention_ids=[],
        story_type="feature",
        workflow_id=1,
        completed_at_override=None,
        started_at=None,
        completed_at=None,
        name="Found Story",
        global_id="g1",
        completed=False,
        blocker=False,
        epic_id=None,
        story_template_id=None,
        external_links=[],
        previous_iteration_ids=[],
        requested_by_id="user-1",
        iteration_id=None,
        label_ids=[],
        started_at_override=None,
        group_id=None,
        workflow_state_id=1,
        updated_at=None,
        group_mention_ids=[],
        follower_ids=[],
        owner_ids=[],
        external_id=None,
        id=1,
        estimate=None,
        position=1,
        blocked=False,
        project_id=10,
        deadline=None,
        stats=StoryStats(num_related_documents=0),
        created_at="2024-01-01T00:00:00Z",
        moved_at=None,
    )
    client = MagicMock()
    client.search_stories.return_value = StorySearchResults(total=1, data=[search_result], next=None)
    mock_get_client.return_value = client

    runner = make_runner()
    result = runner.invoke(cli, ["search", "bug fix"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert len(data) == 1
    assert data[0]["name"] == "Found Story"


# --- projects ---


@patch("shortcut_python_client.cli.get_client")
def test_projects_list(mock_get_client):
    client = MagicMock()
    client.list_projects.return_value = [make_project()]
    mock_get_client.return_value = client

    runner = make_runner()
    result = runner.invoke(cli, ["projects", "list"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert data[0]["name"] == "Backend"


# --- labels ---


@patch("shortcut_python_client.cli.get_client")
def test_labels_list(mock_get_client):
    client = MagicMock()
    client.list_labels.return_value = [make_label()]
    mock_get_client.return_value = client

    runner = make_runner()
    result = runner.invoke(cli, ["labels", "list"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert data[0]["name"] == "bug"


@patch("shortcut_python_client.cli.get_client")
def test_labels_list_filter_by_name(mock_get_client):
    client = MagicMock()
    client.list_labels.return_value = [
        make_label(id=1, name="bug"),
        make_label(id=2, name="feature", global_id="gl2", app_url="https://app.shortcut.com/label/2"),
        make_label(id=3, name="bugfix", global_id="gl3", app_url="https://app.shortcut.com/label/3"),
    ]
    mock_get_client.return_value = client

    runner = make_runner()
    result = runner.invoke(cli, ["labels", "list", "--name", "bug"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert len(data) == 2
    names = {item["name"] for item in data}
    assert names == {"bug", "bugfix"}


@patch("shortcut_python_client.cli.get_client")
def test_labels_list_pretty_shows_color_swatch(mock_get_client):
    client = MagicMock()
    client.list_labels.return_value = [make_label(color="#ff0000")]
    mock_get_client.return_value = client

    runner = make_runner()
    result = runner.invoke(cli, ["labels", "list", "--pretty"])
    assert result.exit_code == 0
    assert "#ff0000" in result.output
    assert "\u2588\u2588" in result.output


# --- workflows ---


@patch("shortcut_python_client.cli.get_client")
def test_workflows_list(mock_get_client):
    state = WorkflowState(
        description="",
        entity_type="workflow-state",
        name="In Progress",
        global_id="gs1",
        num_stories=5,
        type="Started",
        updated_at="2024-01-01T00:00:00Z",
        id=100,
        num_story_templates=0,
        position=1,
        created_at="2024-01-01T00:00:00Z",
        verb="start",
    )
    workflow = Workflow(
        description="Default",
        entity_type="workflow",
        project_ids=[10],
        states=[state],
        name="Dev Workflow",
        updated_at="2024-01-01T00:00:00Z",
        auto_assign_owner=False,
        id=1,
        team_id=1,
        created_at="2024-01-01T00:00:00Z",
        default_state_id=100,
    )
    client = MagicMock()
    client.list_workflows.return_value = [workflow]
    mock_get_client.return_value = client

    runner = make_runner()
    result = runner.invoke(cli, ["workflows", "list", "--pretty"])
    assert result.exit_code == 0
    assert "Dev Workflow" in result.output
    assert "In Progress" in result.output


# --- members ---


@patch("shortcut_python_client.cli.get_client")
def test_members_list(mock_get_client):
    member = Member(
        role="admin",
        entity_type="member",
        disabled=False,
        global_id="gm1",
        state="full",
        updated_at=None,
        created_without_invite=False,
        group_ids=[],
        id="user-1",
        profile=Profile(
            entity_type="profile",
            deactivated=False,
            mention_name="alice",
            name="Alice",
            gravatar_hash=None,
            id="user-1",
            display_icon=make_icon(),
            is_owner=True,
            email_address="alice@example.com",
        ),
        created_at=None,
    )
    client = MagicMock()
    client.list_members.return_value = [member]
    mock_get_client.return_value = client

    runner = make_runner()
    result = runner.invoke(cli, ["members", "list", "--pretty"])
    assert result.exit_code == 0
    assert "Alice" in result.output
    assert "@alice" in result.output


# --- iterations ---


@patch("shortcut_python_client.cli.get_client")
def test_iterations_list(mock_get_client):
    iteration = IterationSlim(
        app_url="https://app.shortcut.com/iteration/1",
        entity_type="iteration",
        labels=[],
        mention_ids=[],
        member_mention_ids=[],
        associated_groups=[],
        name="Sprint 1",
        global_id="gi1",
        label_ids=[],
        updated_at="2024-01-01T00:00:00Z",
        group_mention_ids=[],
        end_date="2024-01-14T00:00:00Z",
        follower_ids=[],
        group_ids=[],
        start_date="2024-01-01T00:00:00Z",
        status="started",
        id=1,
        stats=IterationStats(
            num_points_done=0,
            num_related_documents=0,
            num_stories_unstarted=0,
            num_points_started=0,
            num_points_unstarted=0,
            num_stories_started=0,
            num_stories_unestimated=0,
            num_stories_backlog=0,
            num_points_backlog=0,
            num_points=0,
            num_stories_done=0,
        ),
        created_at="2024-01-01T00:00:00Z",
    )
    client = MagicMock()
    client.list_iterations.return_value = [iteration]
    mock_get_client.return_value = client

    runner = make_runner()
    result = runner.invoke(cli, ["iterations", "list", "--pretty"])
    assert result.exit_code == 0
    assert "Sprint 1" in result.output
    assert "started" in result.output


# --- missing token ---


def test_missing_token():
    runner = CliRunner(env={"SHORTCUT_API_TOKEN": ""})
    result = runner.invoke(cli, ["me"])
    assert result.exit_code != 0
    assert "SHORTCUT_API_TOKEN" in result.output
