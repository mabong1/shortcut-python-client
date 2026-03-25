"""Auto-generated Pydantic models from Shortcut OpenAPI spec."""

from datetime import date, datetime  # noqa: F401
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field


class BaseTaskParams(BaseModel):
    """Request parameters for specifying how to pre-populate a task through a template."""

    model_config = ConfigDict(populate_by_name=True)

    description: str = Field(description="The Task description.")
    complete: bool | None = Field(default=None, description="True/false boolean indicating whether the Task is comp...")
    owner_ids: list[str] | None = Field(default=None, description="An array of UUIDs for any members you want to ad...")
    external_id: str | None = Field(default=None, description="This field can be set to another unique ID. In the c...")


class BasicWorkspaceInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    created_at: datetime
    default_workflow_id: int
    estimate_scale: list[int]
    name: str
    url_slug: str
    utc_offset: str
    korey_enabled: bool | None = Field(default=None)


class PullRequestLabel(BaseModel):
    """Corresponds to a VCS Label associated with a Pull Request."""

    model_config = ConfigDict(populate_by_name=True)

    entity_type: str = Field(description="A string description of this resource.")
    id: int = Field(description="The unique ID of the VCS Label.")
    color: str = Field(description="The color of the VCS label.")
    description: str | None = Field(default=None, description="The description of the VCS label.")
    name: str = Field(description="The name of the VCS label.")


class PullRequest(BaseModel):
    """Corresponds to a VCS Pull Request attached to a Shortcut story."""

    model_config = ConfigDict(populate_by_name=True)

    entity_type: str = Field(description="A string description of this resource.")
    closed: bool = Field(description="True/False boolean indicating whether the VCS pull request has been closed.")
    merged: bool = Field(description="True/False boolean indicating whether the VCS pull request has been merged.")
    num_added: int = Field(description="Number of lines added in the pull request, according to VCS.")
    branch_id: int = Field(description="The ID of the branch for the particular pull request.")
    overlapping_stories: list[int] | None = Field(default=None, description="An array of Story ids that have Pull R...")
    number: int = Field(description="The pull request's unique number ID in VCS.")
    branch_name: str = Field(description="The name of the branch for the particular pull request.")
    target_branch_name: str = Field(description="The name of the target branch for the particular pull request.")
    num_commits: int | None = Field(description="The number of commits on the pull request.")
    title: str = Field(description="The title of the pull request.")
    updated_at: datetime = Field(description="The time/date the pull request was created.")
    has_overlapping_stories: bool = Field(description="Boolean indicating that the Pull Request has Stories that ha...")
    draft: bool = Field(description="True/False boolean indicating whether the VCS pull request is in the draft state.")
    id: int = Field(description="The unique ID associated with the pull request in Shortcut.")
    vcs_labels: list[PullRequestLabel] | None = Field(default=None, description="An array of PullRequestLabels atta...")
    url: str = Field(description="The URL for the pull request.")
    num_removed: int = Field(description="Number of lines removed in the pull request, according to VCS.")
    review_status: str | None = Field(default=None, description="The status of the review for the pull request.")
    num_modified: int | None = Field(description="Number of lines modified in the pull request, according to VCS.")
    build_status: str | None = Field(default=None, description="The status of the Continuous Integration workflow f...")
    target_branch_id: int = Field(description="The ID of the target branch for the particular pull request.")
    repository_id: int = Field(description="The ID of the repository for the particular pull request.")
    created_at: datetime = Field(description="The time/date the pull request was created.")


class Branch(BaseModel):
    """Branch refers to a VCS branch. Branches are feature branches associated with Shortcut Stories."""

    model_config = ConfigDict(populate_by_name=True)

    entity_type: str = Field(description="A string description of this resource.")
    deleted: bool = Field(description="A true/false boolean indicating if the Branch has been deleted.")
    name: str = Field(description="The name of the Branch.")
    persistent: bool = Field(description="This field is deprecated, and will always be false.")
    updated_at: datetime | None = Field(description="The time/date the Branch was updated.")
    pull_requests: list[PullRequest] = Field(description="An array of PullRequests attached to the Branch (there is...")
    merged_branch_ids: list[int] = Field(description="The IDs of the Branches the Branch has been merged into.")
    id: int | None = Field(description="The unique ID of the Branch.")
    url: str = Field(description="The URL of the Branch.")
    repository_id: int = Field(description="The ID of the Repository that contains the Branch.")
    created_at: datetime | None = Field(description="The time/date the Branch was created.")


class Category(BaseModel):
    """A Category can be used to associate Objectives."""

    model_config = ConfigDict(populate_by_name=True)

    archived: bool = Field(description="A true/false boolean indicating if the Category has been archived.")
    entity_type: str = Field(description="A string description of this resource.")
    color: str | None = Field(description='The hex color to be displayed with the Category (for example, "#ff0000").')
    name: str = Field(description="The name of the Category.")
    global_id: str = Field(description="The Global ID of the Category.")
    type: str = Field(description="The type of entity this Category is associated with; currently Milestone or Obje...")
    updated_at: datetime = Field(description="The time/date that the Category was updated.")
    external_id: str | None = Field(description="This field can be set to another unique ID. In the case that the C...")
    id: int = Field(description="The unique ID of the Category.")
    created_at: datetime = Field(description="The time/date that the Category was created.")


class Identity(BaseModel):
    """The Identity of the VCS user that authored the Commit."""

    model_config = ConfigDict(populate_by_name=True)

    entity_type: str = Field(description="A string description of this resource.")
    name: str | None = Field(description="This is your login in VCS.")
    type: Literal["slack", "github", "gitlab", "bitbucket"] | None = Field(description="The service this Identity i...")


class Commit(BaseModel):
    """Commit refers to a VCS commit and all associated details."""

    model_config = ConfigDict(populate_by_name=True)

    entity_type: str = Field(description="A string description of this resource.")
    author_id: str | None = Field(description="The ID of the Member that authored the Commit, if known.")
    hash: str = Field(description="The Commit hash.")
    updated_at: datetime | None = Field(description="The time/date the Commit was updated.")
    id: int | None = Field(description="The unique ID of the Commit.")
    url: str = Field(description="The URL of the Commit.")
    author_email: str = Field(description="The email address of the VCS user that authored the Commit.")
    timestamp: datetime = Field(description="The time/date the Commit was pushed.")
    author_identity: Identity
    repository_id: int | None = Field(description="The ID of the Repository that contains the Commit.")
    created_at: datetime = Field(description="The time/date the Commit was created.")
    message: str = Field(description="The Commit message.")


class CreateCategory(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str = Field(description="The name of the new Category.")
    color: str | None = Field(default=None, description="The hex color to be displayed with the Category (for examp...")
    external_id: str | None = Field(default=None, description="This field can be set to another unique ID. In the c...")
    type: dict[str, Any] | None = Field(default=None, description="The type of entity this Category is associated w...")


class CreateCategoryParams(BaseModel):
    """Request parameters for creating a Category with a Objective."""

    model_config = ConfigDict(populate_by_name=True)

    name: str = Field(description="The name of the new Category.")
    color: str | None = Field(default=None, description="The hex color to be displayed with the Category (for examp...")
    external_id: str | None = Field(default=None, description="This field can be set to another unique ID. In the c...")


class CreateCommentComment(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    text: str = Field(description="The comment text.")
    author_id: str | None = Field(default=None, description="The Member ID of the Comment's author. Defaults to the...")
    created_at: datetime | None = Field(default=None, description="Defaults to the time/date the comment is created...")
    updated_at: datetime | None = Field(default=None, description="Defaults to the time/date the comment is last up...")
    external_id: str | None = Field(default=None, description="This field can be set to another unique ID. In the c...")


class CreateDoc(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(description="The title for the new document.")
    content: str = Field(description="The content for the new document.")
    content_format: Literal["markdown", "html"] | None = Field(default=None, description="Format of the content bei...")


class CreateLabelParams(BaseModel):
    """Request parameters for creating a Label on a Shortcut Story."""

    model_config = ConfigDict(populate_by_name=True)

    name: str = Field(description="The name of the new Label.")
    description: str | None = Field(default=None, description="The description of the new Label.")
    color: str | None = Field(default=None, description="The hex color to be displayed with the Label (for example,...")
    external_id: str | None = Field(default=None, description="This field can be set to another unique ID. In the c...")


class CustomFieldValueParams(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    field_id: str = Field(description="The unique public ID for the CustomField.")
    value_id: str = Field(description="The unique public ID for the CustomFieldEnumValue.")
    value: str | None = Field(default=None, description="A literal value for the CustomField. Currently ignored.")


class CreateSubTaskParams(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str = Field(description="The name of the SubTask.")
    owner_ids: list[str] | None = Field(default=None, description="An array of UUIDs of the owners of this story.")
    workflow_state_id: int | None = Field(default=None, description="The ID of the workflow state the story will be...")


class CreateStoryContents(BaseModel):
    """A map of story attributes this template populates."""

    model_config = ConfigDict(populate_by_name=True)

    description: str | None = Field(default=None, description="The description of the story.")
    labels: list[CreateLabelParams] | None = Field(default=None, description="An array of labels to be populated by...")
    story_type: str | None = Field(default=None, description="The type of story (feature, bug, chore).")
    custom_fields: list[CustomFieldValueParams] | None = Field(default=None, description="An array of maps specifyi...")
    file_ids: list[int] | None = Field(default=None, description="An array of the attached file IDs to be populated.")
    name: str | None = Field(default=None, description="The name of the story.")
    epic_id: int | None = Field(default=None, description="The ID of the epic the to be populated.")
    external_links: list[str] | None = Field(default=None, description="An array of external links to be populated.")
    sub_tasks: list[CreateSubTaskParams] | None = Field(default=None, description="An array of maps specifying the ...")
    iteration_id: int | None = Field(default=None, description="The ID of the iteration the to be populated.")
    tasks: list[BaseTaskParams] | None = Field(default=None, description="An array of tasks to be populated by the ...")
    group_id: str | None = Field(default=None, description="The ID of the group to be populated.")
    workflow_state_id: int | None = Field(default=None, description="The ID of the workflow state to be populated.")
    follower_ids: list[str] | None = Field(default=None, description="An array of UUIDs for any Members listed as F...")
    owner_ids: list[str] | None = Field(default=None, description="An array of UUIDs of the owners of this story.")
    estimate: int | None = Field(default=None, description="The numeric point estimate to be populated.")
    project_id: int | None = Field(default=None, description="The ID of the project the story belongs to.")
    linked_file_ids: list[int] | None = Field(default=None, description="An array of the linked file IDs to be popu...")
    deadline: datetime | None = Field(default=None, description="The due date of the story.")


class CreateEntityTemplate(BaseModel):
    """Request parameters for creating an entirely new entity template."""

    model_config = ConfigDict(populate_by_name=True)

    name: str = Field(description="The name of the new entity template")
    author_id: str | None = Field(default=None, description="The id of the user creating this template.")
    story_contents: CreateStoryContents


class CreateEpic(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    description: str | None = Field(default=None, description="The Epic's description.")
    labels: list[CreateLabelParams] | None = Field(default=None, description="An array of Labels attached to the Epic.")
    completed_at_override: datetime | None = Field(default=None, description="A manual override for the time/date t...")
    objective_ids: list[int] | None = Field(default=None, description="An array of IDs for Objectives to which this...")
    name: str = Field(description="The Epic's name.")
    planned_start_date: datetime | None = Field(default=None, description="The Epic's planned start date.")
    state: Literal["in progress", "to do", "done"] | None = Field(default=None, description="`Deprecated` The Epic'...")
    milestone_id: int | None = Field(default=None, description="`Deprecated` The ID of the Milestone this Epic is r...")
    requested_by_id: str | None = Field(default=None, description="The ID of the member that requested the epic.")
    epic_state_id: int | None = Field(default=None, description="The ID of the Epic State.")
    started_at_override: datetime | None = Field(default=None, description="A manual override for the time/date the...")
    group_id: str | None = Field(default=None, description="`Deprecated` The ID of the group to associate with the ...")
    updated_at: datetime | None = Field(default=None, description="Defaults to the time/date it is created but can ...")
    follower_ids: list[str] | None = Field(default=None, description="An array of UUIDs for any Members you want to...")
    group_ids: list[str] | None = Field(default=None, description="An array of UUIDS for Groups to which this Epic ...")
    converted_from_story_id: int | None = Field(default=None, description="The ID of the Story that was converted t...")
    owner_ids: list[str] | None = Field(default=None, description="An array of UUIDs for any members you want to ad...")
    external_id: str | None = Field(default=None, description="This field can be set to another unique ID. In the c...")
    deadline: datetime | None = Field(default=None, description="The Epic's deadline.")
    created_at: datetime | None = Field(default=None, description="Defaults to the time/date it is created but can ...")


class CreateEpicComment(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    text: str = Field(description="The comment text.")
    author_id: str | None = Field(default=None, description="The Member ID of the Comment's author. Defaults to the...")
    created_at: datetime | None = Field(default=None, description="Defaults to the time/date the comment is created...")
    updated_at: datetime | None = Field(default=None, description="Defaults to the time/date the comment is last up...")
    external_id: str | None = Field(default=None, description="This field can be set to another unique ID. In the c...")


class CreateEpicHealth(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    status: Literal["At Risk", "On Track", "Off Track", "No Health"] = Field(description="The health status of the ...")
    text: str | None = Field(default=None, description="The description of the Health status.")


class CreateGenericIntegration(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    webhook_url: str
    secret: str | None = Field(default=None)


class CreateGroup(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    description: str | None = Field(default=None, description="The description of the Group.")
    member_ids: list[str] | None = Field(default=None, description="The Member ids to add to this Group.")
    workflow_ids: list[int] | None = Field(default=None, description="The Workflow ids to add to the Group.")
    name: str = Field(description="The name of this Group.")
    mention_name: str = Field(description="The mention name of this Group.")
    color: str | None = Field(default=None, description="The color you wish to use for the Group in the system.")
    color_key: str | None = Field(default=None, description="The color key you wish to use for the Group in the sys...")
    display_icon_id: str | None = Field(default=None, description="The Icon id for the avatar of this Group.")


class CreateIteration(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    follower_ids: list[str] | None = Field(default=None, description="An array of UUIDs for any Members you want to...")
    group_ids: list[str] | None = Field(default=None, description="An array of UUIDs for any Groups you want to add...")
    labels: list[CreateLabelParams] | None = Field(default=None, description="An array of Labels attached to the It...")
    description: str | None = Field(default=None, description="The description of the Iteration.")
    name: str = Field(description="The name of this Iteration.")
    start_date: str = Field(description="The date this Iteration begins, e.g. 2019-07-01.")
    end_date: str = Field(description="The date this Iteration ends, e.g. 2019-07-01.")


class CreateLinkedFile(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    description: str | None = Field(default=None, description="The description of the file.")
    story_id: int | None = Field(default=None, description="The ID of the linked story.")
    name: str = Field(description="The name of the file.")
    thumbnail_url: str | None = Field(default=None, description="The URL of the thumbnail, if the integration provi...")
    type: Literal["google", "url", "dropbox", "box", "onedrive"] = Field(description="The integration type of the f...")
    size: int | None = Field(default=None, description="The filesize, if the integration provided it.")
    uploader_id: str | None = Field(default=None, description="The UUID of the member that uploaded the file.")
    content_type: str | None = Field(default=None, description="The content type of the image (e.g. txt/plain).")
    url: str = Field(description="The URL of linked file.")


class CreateMilestone(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str = Field(description="The name of the Milestone.")
    description: str | None = Field(default=None, description="The Milestone's description.")
    state: Literal["in progress", "to do", "done"] | None = Field(default=None, description="The workflow state tha...")
    started_at_override: datetime | None = Field(default=None, description="A manual override for the time/date the...")
    completed_at_override: datetime | None = Field(default=None, description="A manual override for the time/date t...")
    categories: list[CreateCategoryParams] | None = Field(default=None, description="An array of IDs of Categories ...")


class CreateObjective(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str = Field(description="The name of the Objective.")
    description: str | None = Field(default=None, description="The Objective's description.")
    state: Literal["in progress", "to do", "done"] | None = Field(default=None, description="The workflow state tha...")
    started_at_override: datetime | None = Field(default=None, description="A manual override for the time/date the...")
    completed_at_override: datetime | None = Field(default=None, description="A manual override for the time/date t...")
    categories: list[CreateCategoryParams] | None = Field(default=None, description="An array of IDs of Categories ...")


class CreateObjectiveHealth(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    status: Literal["At Risk", "On Track", "Off Track", "No Health"] = Field(description="The health status of the ...")
    text: str | None = Field(default=None, description="The description of the Health status.")


class CreateOrDeleteStoryReaction(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    emoji: str = Field(description="The emoji short-code to add / remove. E.g. `:thumbsup::skin-tone-4:`.")


class CreateProject(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    description: str | None = Field(default=None, description="The Project description.")
    color: str | None = Field(default=None, description="The color you wish to use for the Project in the system.")
    name: str = Field(description="The name of the Project.")
    start_time: datetime | None = Field(default=None, description="The date at which the Project was started.")
    updated_at: datetime | None = Field(default=None, description="Defaults to the time/date it is created but can ...")
    follower_ids: list[str] | None = Field(default=None, description="An array of UUIDs for any members you want to...")
    external_id: str | None = Field(default=None, description="This field can be set to another unique ID. In the c...")
    team_id: int = Field(description="The ID of the team the project belongs to.")
    iteration_length: int | None = Field(default=None, description="The number of weeks per iteration in this Project.")
    abbreviation: str | None = Field(default=None, description="The Project abbreviation used in Story summaries. S...")
    created_at: datetime | None = Field(default=None, description="Defaults to the time/date it is created but can ...")


class CreateStoryLinkParams(BaseModel):
    """Request parameters for creating a Story Link within a Story."""

    model_config = ConfigDict(populate_by_name=True)

    subject_id: int | None = Field(default=None, description="The unique ID of the Story defined as subject.")
    verb: Literal["blocks", "duplicates", "relates to"] = Field(description="How the subject Story acts on the obje...")
    object_id: int | None = Field(default=None, description="The unique ID of the Story defined as object.")


class CreateStoryCommentParams(BaseModel):
    """Request parameters for creating a Comment on a Shortcut Story."""

    model_config = ConfigDict(populate_by_name=True)

    text: str = Field(description="The comment text.")
    author_id: str | None = Field(default=None, description="The Member ID of the Comment's author. Defaults to the...")
    created_at: datetime | None = Field(default=None, description="Defaults to the time/date the comment is created...")
    updated_at: datetime | None = Field(default=None, description="Defaults to the time/date the comment is last up...")
    external_id: str | None = Field(default=None, description="This field can be set to another unique ID. In the c...")
    parent_id: int | None = Field(default=None, description="The ID of the Comment that this comment is threaded un...")


class CreateTaskParams(BaseModel):
    """Request parameters for creating a Task on a Story."""

    model_config = ConfigDict(populate_by_name=True)

    description: str = Field(description="The Task description.")
    complete: bool | None = Field(default=None, description="True/false boolean indicating whether the Task is comp...")
    owner_ids: list[str] | None = Field(default=None, description="An array of UUIDs for any members you want to ad...")
    external_id: str | None = Field(default=None, description="This field can be set to another unique ID. In the c...")
    created_at: datetime | None = Field(default=None, description="Defaults to the time/date the Task is created bu...")
    updated_at: datetime | None = Field(default=None, description="Defaults to the time/date the Task is created in...")


class CreateStoryParams(BaseModel):
    """Request parameters for creating a story."""

    model_config = ConfigDict(populate_by_name=True)

    description: str | None = Field(default=None, description="The description of the story.")
    archived: bool | None = Field(default=None, description="Controls the story's archived state.")
    story_links: list[CreateStoryLinkParams] | None = Field(default=None, description="An array of story links atta...")
    labels: list[CreateLabelParams] | None = Field(default=None, description="An array of labels attached to the st...")
    story_type: Literal["feature", "chore", "bug"] | None = Field(default=None, description="The type of story (fea...")
    custom_fields: list[CustomFieldValueParams] | None = Field(default=None, description="A map specifying a Custom...")
    move_to: Literal["last", "first"] | None = Field(default=None, description='One of "first" or "last". This ...')
    file_ids: list[int] | None = Field(default=None, description="An array of IDs of files attached to the story.")
    source_task_id: int | None = Field(default=None, description="Given this story was converted from a task in ano...")
    completed_at_override: datetime | None = Field(default=None, description="A manual override for the time/date t...")
    name: str = Field(description="The name of the story.")
    comments: list[CreateStoryCommentParams] | None = Field(default=None, description="An array of comments to add ...")
    epic_id: int | None = Field(default=None, description="The ID of the epic the story belongs to.")
    story_template_id: str | None = Field(default=None, description="The id of the story template used to create th...")
    external_links: list[str] | None = Field(default=None, description="An array of External Links associated with ...")
    sub_tasks: list[dict[str, Any]] | None = Field(default=None, description="An array of maps specifying sub-tasks...")
    requested_by_id: str | None = Field(default=None, description="The ID of the member that requested the story.")
    iteration_id: int | None = Field(default=None, description="The ID of the iteration the story belongs to.")
    tasks: list[CreateTaskParams] | None = Field(default=None, description="An array of tasks connected to the story.")
    started_at_override: datetime | None = Field(default=None, description="A manual override for the time/date the...")
    group_id: str | None = Field(default=None, description="The id of the group to associate with this story.")
    workflow_state_id: int | None = Field(default=None, description="The ID of the workflow state the story will be...")
    updated_at: datetime | None = Field(default=None, description="The time/date the Story was updated.")
    follower_ids: list[str] | None = Field(default=None, description="An array of UUIDs of the followers of this st...")
    owner_ids: list[str] | None = Field(default=None, description="An array of UUIDs of the owners of this story.")
    external_id: str | None = Field(default=None, description="This field can be set to another unique ID. In the c...")
    parent_story_id: int | None = Field(default=None, description="The ID of the parent story to associate with thi...")
    estimate: int | None = Field(default=None, description="The numeric point estimate of the story. Can also be nu...")
    project_id: int | None = Field(default=None, description="The ID of the project the story belongs to.")
    linked_file_ids: list[int] | None = Field(default=None, description="An array of IDs of linked files attached t...")
    deadline: datetime | None = Field(default=None, description="The due date of the story.")
    created_at: datetime | None = Field(default=None, description="The time/date the Story was created.")


class CreateStories(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    stories: list[CreateStoryParams] = Field(description="An array of stories to be created.")


class CreateStoryComment(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    text: str = Field(description="The comment text.")
    author_id: str | None = Field(default=None, description="The Member ID of the Comment's author. Defaults to the...")
    created_at: datetime | None = Field(default=None, description="Defaults to the time/date the comment is created...")
    updated_at: datetime | None = Field(default=None, description="Defaults to the time/date the comment is last up...")
    external_id: str | None = Field(default=None, description="This field can be set to another unique ID. In the c...")
    parent_id: int | None = Field(default=None, description="The ID of the Comment that this comment is threaded un...")


class RemoveCustomFieldParams(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    field_id: str = Field(description="The unique public ID for the CustomField.")


class RemoveLabelParams(BaseModel):
    """Request parameters for removing a Label from a Shortcut Story."""

    model_config = ConfigDict(populate_by_name=True)

    name: str = Field(description="The name of the new Label to remove.")


class CreateStoryFromTemplateParams(BaseModel):
    """
    Request parameters for creating a story from a story template. These parameters are merged with the values
    derived from the template.
    """

    model_config = ConfigDict(populate_by_name=True)

    description: str | None = Field(default=None, description="The description of the story.")
    archived: bool | None = Field(default=None, description="Controls the story's archived state.")
    story_links: list[CreateStoryLinkParams] | None = Field(default=None, description="An array of story links atta...")
    labels: list[CreateLabelParams] | None = Field(default=None, description="An array of labels attached to the st...")
    external_links_add: list[str] | None = Field(default=None, description="An array of External Links associated w...")
    story_type: Literal["feature", "chore", "bug"] | None = Field(default=None, description="The type of story (fea...")
    custom_fields: list[CustomFieldValueParams] | None = Field(default=None, description="A map specifying a Custom...")
    move_to: Literal["last", "first"] | None = Field(default=None, description='One of "first" or "last". This ...')
    file_ids: list[int] | None = Field(default=None, description="An array of IDs of files attached to the story.")
    source_task_id: int | None = Field(default=None, description="Given this story was converted from a task in ano...")
    completed_at_override: datetime | None = Field(default=None, description="A manual override for the time/date t...")
    name: str | None = Field(default=None, description="The name of the story. Must be provided if the template doe...")
    file_ids_add: list[int] | None = Field(default=None, description="An array of IDs of files attached to the stor...")
    file_ids_remove: list[int] | None = Field(default=None, description="An array of IDs of files removed from file...")
    comments: list[CreateStoryCommentParams] | None = Field(default=None, description="An array of comments to add ...")
    follower_ids_add: list[str] | None = Field(default=None, description="The UUIDs of the new followers to be adde...")
    epic_id: int | None = Field(default=None, description="The ID of the epic the story belongs to.")
    story_template_id: str = Field(description="The id of the story template used to create this story.")
    external_links: list[str] | None = Field(default=None, description="An array of External Links associated with ...")
    follower_ids_remove: list[str] | None = Field(default=None, description="The UUIDs of the new followers to be r...")
    sub_tasks: list[dict[str, Any]] | None = Field(default=None, description="An array of maps specifying sub-tasks...")
    linked_file_ids_remove: list[int] | None = Field(default=None, description="An array of IDs of linked files rem...")
    requested_by_id: str | None = Field(default=None, description="The ID of the member that requested the story.")
    iteration_id: int | None = Field(default=None, description="The ID of the iteration the story belongs to.")
    custom_fields_remove: list[RemoveCustomFieldParams] | None = Field(default=None)
    tasks: list[CreateTaskParams] | None = Field(default=None, description="An array of tasks connected to the story.")
    started_at_override: datetime | None = Field(default=None, description="A manual override for the time/date the...")
    labels_add: list[CreateLabelParams] | None = Field(default=None, description="An array of labels attached to th...")
    group_id: str | None = Field(default=None, description="The id of the group to associate with this story.")
    workflow_state_id: int | None = Field(default=None, description="The ID of the workflow state the story will be...")
    updated_at: datetime | None = Field(default=None, description="The time/date the Story was updated.")
    follower_ids: list[str] | None = Field(default=None, description="An array of UUIDs of the followers of this st...")
    owner_ids: list[str] | None = Field(default=None, description="An array of UUIDs of the owners of this story.")
    external_id: str | None = Field(default=None, description="This field can be set to another unique ID. In the c...")
    parent_story_id: int | None = Field(default=None, description="The ID of the parent story to associate with thi...")
    estimate: int | None = Field(default=None, description="The numeric point estimate of the story. Can also be nu...")
    owner_ids_remove: list[str] | None = Field(default=None, description="The UUIDs of the new owners to be removed...")
    custom_fields_add: list[CustomFieldValueParams] | None = Field(default=None, description="A map specifying a Cu...")
    project_id: int | None = Field(default=None, description="The ID of the project the story belongs to.")
    linked_file_ids_add: list[int] | None = Field(default=None, description="An array of IDs of linked files attach...")
    linked_file_ids: list[int] | None = Field(default=None, description="An array of IDs of linked files attached t...")
    labels_remove: list[RemoveLabelParams] | None = Field(default=None, description="An array of labels to remove f...")
    deadline: datetime | None = Field(default=None, description="The due date of the story.")
    owner_ids_add: list[str] | None = Field(default=None, description="The UUIDs of the new owners to be added in a...")
    created_at: datetime | None = Field(default=None, description="The time/date the Story was created.")
    external_links_remove: list[str] | None = Field(default=None, description="An array of External Links associate...")


class CreateStoryLink(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    verb: Literal["blocks", "duplicates", "relates to"] = Field(description="The type of link.")
    subject_id: int = Field(description="The ID of the subject Story.")
    object_id: int = Field(description="The ID of the object Story.")


class CreateTask(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    description: str = Field(description="The Task description.")
    complete: bool | None = Field(default=None, description="True/false boolean indicating whether the Task is comp...")
    owner_ids: list[str] | None = Field(default=None, description="An array of UUIDs for any members you want to ad...")
    external_id: str | None = Field(default=None, description="This field can be set to another unique ID. In the c...")
    created_at: datetime | None = Field(default=None, description="Defaults to the time/date the Task is created bu...")
    updated_at: datetime | None = Field(default=None, description="Defaults to the time/date the Task is created in...")


class CustomFieldEnumValue(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str = Field(description="The unique public ID for the Custom Field.")
    value: str = Field(description="A string value within the domain of this Custom Field.")
    position: int = Field(description="An integer indicating the position of this Value with respect to the other C...")
    color_key: str | None = Field(description="A color key associated with this CustomFieldEnumValue.")
    entity_type: Literal["custom-field-enum-value"] = Field(description="A string description of this resource.")
    enabled: bool = Field(description="When true, the CustomFieldEnumValue can be selected for the CustomField.")


class CustomField(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    description: str | None = Field(default=None, description="A string description of the CustomField")
    icon_set_identifier: str | None = Field(default=None, description="A string that represents the icon that corre...")
    entity_type: Literal["custom-field"] = Field(description="A string description of this resource.")
    story_types: list[str] | None = Field(default=None, description="The types of stories this CustomField is scope...")
    name: str = Field(description="The name of the Custom Field.")
    fixed_position: bool | None = Field(default=None, description="When true, the CustomFieldEnumValues may not be ...")
    updated_at: datetime = Field(description="The instant when this CustomField was last updated.")
    id: str = Field(description="The unique public ID for the CustomField.")
    values: list[CustomFieldEnumValue] | None = Field(default=None, description="A collection of legal values for a...")
    field_type: Literal["enum"] = Field(description="The type of Custom Field, eg. 'enum'.")
    position: int = Field(description="An integer indicating the position of this Custom Field with respect to the ...")
    canonical_name: str | None = Field(default=None, description="The canonical name for a Shortcut-defined field.")
    enabled: bool = Field(description="When true, the CustomField can be applied to entities in the Workspace.")
    created_at: datetime = Field(description="The instant when this CustomField was created.")


class DataConflictError(BaseModel):
    """Error returned when Datomic tx fails due to Datomc :db.error/cas-failed error"""

    model_config = ConfigDict(populate_by_name=True)

    error: Literal["data-conflict-error"]
    message: str = Field(description='An explanatory message: "The update failed due to a data conflict. Please re...')


class DeleteStories(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    story_ids: list[int] = Field(description="An array of IDs of Stories to delete.")


class DisabledFeatureError(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    feature_tag: str = Field(description="The feature that is disabled")
    message: str = Field(description="The message explaining the error")


class Doc(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str = Field(description="The public id of the Doc")
    title: str | None = Field(description="The Doc's title")
    content_markdown: str | None = Field(description="The Doc's content in Markdown format (converted from HTML sto...")
    content_html: str | None = Field(default=None, description="The Doc's content in HTML format (as stored in S3)....")
    app_url: str = Field(description="The Shortcut application url for the Doc")
    created_at: datetime = Field(description="The time/date the Doc was created")
    updated_at: datetime = Field(description="The time/date the Doc was last updated")
    archived: bool = Field(description="Whether the Doc is archived")


class DocSlim(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str = Field(description="The public id of the Doc")
    title: str | None = Field(description="The Docs Title")
    app_url: str = Field(description="The Shortcut application url for the Doc.")


class DocSearchResults(BaseModel):
    """The results of the Document search query."""

    model_config = ConfigDict(populate_by_name=True)

    total: int = Field(description="The total number of matches for the search query. The first 1000 matches can be...")
    data: list[DocSlim] = Field(description="A list of document search results.")
    next: str | None = Field(description="The URL path and query string for the next page of search results.")


class LabelSlim(BaseModel):
    """
    A Label can be used to associate and filter Stories and Epics, and also create new Workspaces. A slim Label does
    not include aggregate stats. Fetch the Label using the labels endpoint to retrieve them.
    """

    model_config = ConfigDict(populate_by_name=True)

    app_url: str = Field(description="The Shortcut application url for the Label.")
    description: str | None = Field(description="The description of the Label.")
    archived: bool = Field(description="A true/false boolean indicating if the Label has been archived.")
    entity_type: str = Field(description="A string description of this resource.")
    color: str | None = Field(description='The hex color to be displayed with the Label (for example, "#ff0000").')
    name: str = Field(description="The name of the Label.")
    global_id: str
    updated_at: datetime | None = Field(description="The time/date that the Label was updated.")
    external_id: str | None = Field(description="This field can be set to another unique ID. In the case that the L...")
    id: int = Field(description="The unique ID of the Label.")
    created_at: datetime | None = Field(description="The time/date that the Label was created.")


class LinkedFile(BaseModel):
    """
    Linked files are stored on a third-party website and linked to one or more Stories. Shortcut currently supports
    linking files from Google Drive, Dropbox, Box, and by URL.
    """

    model_config = ConfigDict(populate_by_name=True)

    description: str | None = Field(description="The description of the file.")
    entity_type: str = Field(description="A string description of this resource.")
    story_ids: list[int] = Field(description="The IDs of the stories this file is attached to.")
    mention_ids: list[str] = Field(description="`Deprecated:` use `member_mention_ids`.")
    member_mention_ids: list[str] = Field(description="The members that are mentioned in the description of the file.")
    name: str = Field(description="The name of the linked file.")
    thumbnail_url: str | None = Field(description="The URL of the file thumbnail, if the integration provided it.")
    type: str = Field(description="The integration type (e.g. google, dropbox, box).")
    size: int | None = Field(description="The filesize, if the integration provided it.")
    uploader_id: str = Field(description="The UUID of the member that uploaded the file.")
    content_type: str | None = Field(description="The content type of the image (e.g. txt/plain).")
    updated_at: datetime = Field(description="The time/date the LinkedFile was updated.")
    group_mention_ids: list[str] = Field(description="The groups that are mentioned in the description of the file.")
    id: int = Field(description="The unique identifier for the file.")
    url: str = Field(description="The URL of the file.")
    created_at: datetime = Field(description="The time/date the LinkedFile was created.")


class StoryContentsTask(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    description: str = Field(description="Full text of the Task.")
    position: int | None = Field(default=None, description="The number corresponding to the Task's position within ...")
    complete: bool | None = Field(default=None, description="True/false boolean indicating whether the Task has bee...")
    owner_ids: list[str] | None = Field(default=None, description="An array of UUIDs of the Owners of this Task.")
    external_id: str | None = Field(default=None, description="This field can be set to another unique ID. In the c...")


class UploadedFile(BaseModel):
    """
    An UploadedFile is any document uploaded to your Shortcut Workspace. Files attached from a third-party service
    are different: see the Linked Files endpoint.
    """

    model_config = ConfigDict(populate_by_name=True)

    description: str | None = Field(description="The description of the file.")
    entity_type: str = Field(description="A string description of this resource.")
    story_ids: list[int] = Field(description="The unique IDs of the Stories associated with this file.")
    mention_ids: list[str] = Field(description="`Deprecated:` use `member_mention_ids`.")
    member_mention_ids: list[str] = Field(description="The unique IDs of the Members who are mentioned in the file ...")
    name: str = Field(description="The optional User-specified name of the file.")
    thumbnail_url: str | None = Field(description="The url where the thumbnail of the file can be found in Shortcut.")
    size: int = Field(description="The size of the file.")
    uploader_id: str = Field(description="The unique ID of the Member who uploaded the file.")
    content_type: str = Field(description="Free form string corresponding to a text or image file.")
    updated_at: datetime | None = Field(description="The time/date that the file was updated.")
    filename: str = Field(description="The name assigned to the file in Shortcut upon upload.")
    group_mention_ids: list[str] = Field(description="The unique IDs of the Groups who are mentioned in the file de...")
    external_id: str | None = Field(description="This field can be set to another unique ID. In the case that the F...")
    id: int = Field(description="The unique ID for the file.")
    url: str | None = Field(description="The URL for the file.")
    created_at: datetime = Field(description="The time/date that the file was created.")


class StoryContents(BaseModel):
    """A container entity for the attributes this template should populate."""

    model_config = ConfigDict(populate_by_name=True)

    description: str | None = Field(default=None, description="The description of the story.")
    entity_type: str | None = Field(default=None, description="A string description of this resource.")
    labels: list[LabelSlim] | None = Field(default=None, description="An array of labels attached to the story.")
    story_type: str | None = Field(default=None, description="The type of story (feature, bug, chore).")
    custom_fields: list[CustomFieldValueParams] | None = Field(default=None, description="An array of maps specifyi...")
    linked_files: list[LinkedFile] | None = Field(default=None, description="An array of linked files attached to t...")
    name: str | None = Field(default=None, description="The name of the story.")
    epic_id: int | None = Field(default=None, description="The ID of the epic the story belongs to.")
    external_links: list[str] | None = Field(default=None, description="An array of external links connected to the...")
    sub_tasks: list[CreateSubTaskParams] | None = Field(default=None, description="An array of maps specifying the ...")
    iteration_id: int | None = Field(default=None, description="The ID of the iteration the story belongs to.")
    tasks: list[StoryContentsTask] | None = Field(default=None, description="An array of tasks connected to the story.")
    label_ids: list[int] | None = Field(default=None, description="An array of label ids attached to the story.")
    group_id: str | None = Field(default=None, description="The ID of the group to which the story is assigned.")
    workflow_state_id: int | None = Field(default=None, description="The ID of the workflow state the story is curr...")
    follower_ids: list[str] | None = Field(default=None, description="An array of UUIDs for any Members listed as F...")
    owner_ids: list[str] | None = Field(default=None, description="An array of UUIDs of the owners of this story.")
    estimate: int | None = Field(default=None, description="The numeric point estimate of the story. Can also be nu...")
    files: list[UploadedFile] | None = Field(default=None, description="An array of files attached to the story.")
    project_id: int | None = Field(default=None, description="The ID of the project the story belongs to.")
    deadline: datetime | None = Field(default=None, description="The due date of the story.")


class EntityTemplate(BaseModel):
    """An entity template can be used to prefill various fields when creating new stories."""

    model_config = ConfigDict(populate_by_name=True)

    entity_type: str = Field(description="A string description of this resource.")
    id: str = Field(description="The unique identifier for the entity template.")
    created_at: datetime = Field(description="The time/date when the entity template was created.")
    updated_at: datetime = Field(description="The time/date when the entity template was last updated.")
    name: str = Field(description="The template's name.")
    author_id: str = Field(description="The unique ID of the member who created the template.")
    last_used_at: datetime = Field(description="The last time that someone created an entity using this template.")
    story_contents: StoryContents


class EpicAssociatedGroup(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    group_id: str = Field(description="The Group ID of the associated group.")
    associated_stories_count: int | None = Field(default=None, description="The number of stories this Group owns i...")


class ThreadedComment(BaseModel):
    """Comments associated with Epic Discussions."""

    model_config = ConfigDict(populate_by_name=True)

    app_url: str = Field(description="The Shortcut application url for the Comment.")
    entity_type: str = Field(description="A string description of this resource.")
    deleted: bool = Field(description="True/false boolean indicating whether the Comment is deleted.")
    mention_ids: list[str] = Field(description="`Deprecated:` use `member_mention_ids`.")
    author_id: str = Field(description="The unique ID of the Member that authored the Comment.")
    member_mention_ids: list[str] = Field(description="An array of Member IDs that have been mentioned in this Comm...")
    comments: list["ThreadedComment"] = Field(description="A nested array of threaded comments.")
    updated_at: datetime = Field(description="The time/date the Comment was updated.")
    group_mention_ids: list[str] = Field(description="An array of Group IDs that have been mentioned in this Comment.")
    external_id: str | None = Field(description="This field can be set to another unique ID. In the case that the C...")
    id: int = Field(description="The unique ID of the Comment.")
    created_at: datetime = Field(description="The time/date the Comment was created.")
    text: str = Field(description="The text of the Comment.")


class Health(BaseModel):
    """The current health status of the Epic."""

    model_config = ConfigDict(populate_by_name=True)

    entity_type: str = Field(description="A string description of this resource.")
    author_id: str | None = Field(default=None, description="The ID of the permission who created or updated the He...")
    epic_id: int | None = Field(default=None, description="The ID of the Epic associated with this Health record.")
    objective_id: int | None = Field(default=None, description="The ID of the Objective associated with this Health...")
    updated_at: datetime | None = Field(default=None, description="The time that the Health record was updated.")
    status: Literal["At Risk", "On Track", "Off Track", "No Health"] = Field(description="The health status of the ...")
    id: str | None = Field(description="The unique ID of the Health record.")
    created_at: datetime | None = Field(default=None, description="The time that the Health record was created.")
    text: str | None = Field(default=None, description="The text of the Health record.")


class EpicStats(BaseModel):
    """A group of calculated values for this Epic."""

    model_config = ConfigDict(populate_by_name=True)

    num_points_done: int = Field(description="The total number of completed points in this Epic.")
    num_related_documents: int = Field(description="The total number of documents associated with this Epic.")
    num_stories_unstarted: int = Field(description="The total number of unstarted Stories in this Epic.")
    num_stories_total: int = Field(description="The total number of Stories in this Epic.")
    last_story_update: datetime | None = Field(description="The date of the last update of a Story in this Epic.")
    num_points_started: int = Field(description="The total number of started points in this Epic.")
    num_points_unstarted: int = Field(description="The total number of unstarted points in this Epic.")
    num_stories_started: int = Field(description="The total number of started Stories in this Epic.")
    num_stories_unestimated: int = Field(description="The total number of Stories with no point estimate.")
    num_stories_backlog: int = Field(description="The total number of backlog Stories in this Epic.")
    num_points_backlog: int = Field(description="The total number of backlog points in this Epic.")
    num_points: int = Field(description="The total number of points in this Epic.")
    num_stories_done: int = Field(description="The total number of done Stories in this Epic.")


class Epic(BaseModel):
    """
    An Epic is a collection of stories that together might make up a release, a objective, or some other large
    initiative that you are working on.
    """

    model_config = ConfigDict(populate_by_name=True)

    app_url: str = Field(description="The Shortcut application url for the Epic.")
    description: str = Field(description="The Epic's description.")
    archived: bool = Field(description="True/false boolean that indicates whether the Epic is archived or not.")
    started: bool = Field(description="A true/false boolean indicating if the Epic has been started.")
    entity_type: str = Field(description="A string description of this resource.")
    labels: list[LabelSlim] = Field(description="An array of Labels attached to the Epic.")
    mention_ids: list[str] = Field(description="`Deprecated:` use `member_mention_ids`.")
    member_mention_ids: list[str] = Field(description="An array of Member IDs that have been mentioned in the Epic ...")
    associated_groups: list[EpicAssociatedGroup] = Field(description="An array containing Group IDs and Group-owned...")
    project_ids: list[int] = Field(description="The IDs of Projects related to this Epic.")
    stories_without_projects: int = Field(description="The number of stories in this epic which are not associated ...")
    completed_at_override: datetime | None = Field(description="A manual override for the time/date the Epic was co...")
    productboard_plugin_id: str | None = Field(description="The ID of the associated productboard integration.")
    started_at: datetime | None = Field(description="The time/date the Epic was started.")
    completed_at: datetime | None = Field(description="The time/date the Epic was completed.")
    objective_ids: list[int] = Field(description="An array of IDs for Objectives to which this epic is related.")
    name: str = Field(description="The name of the Epic.")
    global_id: str
    completed: bool = Field(description="A true/false boolean indicating if the Epic has been completed.")
    comments: list[ThreadedComment] = Field(description="A nested array of threaded comments.")
    productboard_url: str | None = Field(description="The URL of the associated productboard feature.")
    planned_start_date: datetime | None = Field(description="The Epic's planned start date.")
    state: str = Field(description="`Deprecated` The workflow state that the Epic is in.")
    milestone_id: int | None = Field(description="`Deprecated` The ID of the Objective this Epic is related to. Use...")
    requested_by_id: str = Field(description="The ID of the Member that requested the epic.")
    epic_state_id: int = Field(description="The ID of the Epic State.")
    label_ids: list[int] = Field(description="An array of Label ids attached to the Epic.")
    started_at_override: datetime | None = Field(description="A manual override for the time/date the Epic was star...")
    group_id: str | None = Field(description="`Deprecated` The ID of the group to associate with the epic. Use `gro...")
    updated_at: datetime | None = Field(description="The time/date the Epic was updated.")
    group_mention_ids: list[str] = Field(description="An array of Group IDs that have been mentioned in the Epic de...")
    productboard_id: str | None = Field(description="The ID of the associated productboard feature.")
    follower_ids: list[str] = Field(description="An array of UUIDs for any Members you want to add as Followers on ...")
    group_ids: list[str] = Field(description="An array of UUIDS for Groups to which this Epic is related.")
    owner_ids: list[str] = Field(description="An array of UUIDs for any members you want to add as Owners on this n...")
    external_id: str | None = Field(description="This field can be set to another unique ID. In the case that the E...")
    id: int = Field(description="The unique ID of the Epic.")
    health: Health | None = Field(default=None)
    position: int = Field(description="The Epic's relative position in the Epic workflow state.")
    productboard_name: str | None = Field(description="The name of the associated productboard feature.")
    deadline: datetime | None = Field(description="The Epic's deadline.")
    stats: EpicStats
    created_at: datetime | None = Field(description="The time/date the Epic was created.")


class EpicSlim(BaseModel):
    """
    EpicSlim represents the same resource as an Epic but is more light-weight, including all Epic fields except the
    comments array. The description string can be optionally included. Use the [Get Epic](#Get-Epic) endpoint to
    fetch the unabridged payload for an Epic.
    """

    model_config = ConfigDict(populate_by_name=True)

    app_url: str = Field(description="The Shortcut application url for the Epic.")
    description: str | None = Field(default=None, description="The Epic's description.")
    archived: bool = Field(description="True/false boolean that indicates whether the Epic is archived or not.")
    started: bool = Field(description="A true/false boolean indicating if the Epic has been started.")
    entity_type: str = Field(description="A string description of this resource.")
    labels: list[LabelSlim] = Field(description="An array of Labels attached to the Epic.")
    mention_ids: list[str] = Field(description="`Deprecated:` use `member_mention_ids`.")
    member_mention_ids: list[str] = Field(description="An array of Member IDs that have been mentioned in the Epic ...")
    associated_groups: list[EpicAssociatedGroup] = Field(description="An array containing Group IDs and Group-owned...")
    project_ids: list[int] = Field(description="The IDs of Projects related to this Epic.")
    stories_without_projects: int = Field(description="The number of stories in this epic which are not associated ...")
    completed_at_override: datetime | None = Field(description="A manual override for the time/date the Epic was co...")
    productboard_plugin_id: str | None = Field(description="The ID of the associated productboard integration.")
    started_at: datetime | None = Field(description="The time/date the Epic was started.")
    completed_at: datetime | None = Field(description="The time/date the Epic was completed.")
    objective_ids: list[int] = Field(description="An array of IDs for Objectives to which this epic is related.")
    name: str = Field(description="The name of the Epic.")
    global_id: str
    completed: bool = Field(description="A true/false boolean indicating if the Epic has been completed.")
    productboard_url: str | None = Field(description="The URL of the associated productboard feature.")
    planned_start_date: datetime | None = Field(description="The Epic's planned start date.")
    state: str = Field(description="`Deprecated` The workflow state that the Epic is in.")
    milestone_id: int | None = Field(description="`Deprecated` The ID of the Objective this Epic is related to. Use...")
    requested_by_id: str = Field(description="The ID of the Member that requested the epic.")
    epic_state_id: int = Field(description="The ID of the Epic State.")
    label_ids: list[int] = Field(description="An array of Label ids attached to the Epic.")
    started_at_override: datetime | None = Field(description="A manual override for the time/date the Epic was star...")
    group_id: str | None = Field(description="`Deprecated` The ID of the group to associate with the epic. Use `gro...")
    updated_at: datetime | None = Field(description="The time/date the Epic was updated.")
    group_mention_ids: list[str] = Field(description="An array of Group IDs that have been mentioned in the Epic de...")
    productboard_id: str | None = Field(description="The ID of the associated productboard feature.")
    follower_ids: list[str] = Field(description="An array of UUIDs for any Members you want to add as Followers on ...")
    group_ids: list[str] = Field(description="An array of UUIDS for Groups to which this Epic is related.")
    owner_ids: list[str] = Field(description="An array of UUIDs for any members you want to add as Owners on this n...")
    external_id: str | None = Field(description="This field can be set to another unique ID. In the case that the E...")
    id: int = Field(description="The unique ID of the Epic.")
    position: int = Field(description="The Epic's relative position in the Epic workflow state.")
    productboard_name: str | None = Field(description="The name of the associated productboard feature.")
    deadline: datetime | None = Field(description="The Epic's deadline.")
    stats: EpicStats
    created_at: datetime | None = Field(description="The time/date the Epic was created.")


class EpicPaginatedResults(BaseModel):
    """Results schema for paginated Epic listing."""

    model_config = ConfigDict(populate_by_name=True)

    data: list[EpicSlim] = Field(description="Array of Epic objects on the current page")
    next: int | None = Field(description="The next page number if there are more results, or null for the last page")
    total: int = Field(description="The total number of Epics matching the query over all pages")


class EpicSearchResult(BaseModel):
    """
    An Epic in search results. This is typed differently from Epic because the details=slim search argument will
    omit some fields.
    """

    model_config = ConfigDict(populate_by_name=True)

    app_url: str = Field(description="The Shortcut application url for the Epic.")
    description: str | None = Field(default=None, description="The Epic's description.")
    archived: bool = Field(description="True/false boolean that indicates whether the Epic is archived or not.")
    started: bool = Field(description="A true/false boolean indicating if the Epic has been started.")
    entity_type: str = Field(description="A string description of this resource.")
    labels: list[LabelSlim] = Field(description="An array of Labels attached to the Epic.")
    mention_ids: list[str] = Field(description="`Deprecated:` use `member_mention_ids`.")
    member_mention_ids: list[str] = Field(description="An array of Member IDs that have been mentioned in the Epic ...")
    associated_groups: list[EpicAssociatedGroup] = Field(description="An array containing Group IDs and Group-owned...")
    project_ids: list[int] = Field(description="The IDs of Projects related to this Epic.")
    stories_without_projects: int = Field(description="The number of stories in this epic which are not associated ...")
    completed_at_override: datetime | None = Field(description="A manual override for the time/date the Epic was co...")
    productboard_plugin_id: str | None = Field(description="The ID of the associated productboard integration.")
    started_at: datetime | None = Field(description="The time/date the Epic was started.")
    completed_at: datetime | None = Field(description="The time/date the Epic was completed.")
    objective_ids: list[int] = Field(description="An array of IDs for Objectives to which this epic is related.")
    name: str = Field(description="The name of the Epic.")
    global_id: str
    completed: bool = Field(description="A true/false boolean indicating if the Epic has been completed.")
    comments: list[ThreadedComment] | None = Field(default=None, description="A nested array of threaded comments.")
    productboard_url: str | None = Field(description="The URL of the associated productboard feature.")
    planned_start_date: datetime | None = Field(description="The Epic's planned start date.")
    state: str = Field(description="`Deprecated` The workflow state that the Epic is in.")
    milestone_id: int | None = Field(description="`Deprecated` The ID of the Objective this Epic is related to. Use...")
    requested_by_id: str = Field(description="The ID of the Member that requested the epic.")
    epic_state_id: int = Field(description="The ID of the Epic State.")
    label_ids: list[int] = Field(description="An array of Label ids attached to the Epic.")
    started_at_override: datetime | None = Field(description="A manual override for the time/date the Epic was star...")
    group_id: str | None = Field(description="`Deprecated` The ID of the group to associate with the epic. Use `gro...")
    updated_at: datetime | None = Field(description="The time/date the Epic was updated.")
    group_mention_ids: list[str] = Field(description="An array of Group IDs that have been mentioned in the Epic de...")
    productboard_id: str | None = Field(description="The ID of the associated productboard feature.")
    follower_ids: list[str] = Field(description="An array of UUIDs for any Members you want to add as Followers on ...")
    group_ids: list[str] = Field(description="An array of UUIDS for Groups to which this Epic is related.")
    owner_ids: list[str] = Field(description="An array of UUIDs for any members you want to add as Owners on this n...")
    external_id: str | None = Field(description="This field can be set to another unique ID. In the case that the E...")
    id: int = Field(description="The unique ID of the Epic.")
    health: Health | None = Field(default=None)
    position: int = Field(description="The Epic's relative position in the Epic workflow state.")
    productboard_name: str | None = Field(description="The name of the associated productboard feature.")
    deadline: datetime | None = Field(description="The Epic's deadline.")
    stats: EpicStats
    created_at: datetime | None = Field(description="The time/date the Epic was created.")


class EpicSearchResults(BaseModel):
    """The results of the Epic search query."""

    model_config = ConfigDict(populate_by_name=True)

    total: int = Field(description="The total number of matches for the search query. The first 1000 matches can be...")
    data: list[EpicSearchResult] = Field(description="A list of search results.")
    next: str | None = Field(description="The URL path and query string for the next page of search results.")


class EpicState(BaseModel):
    """
    Epic State is any of the at least 3 columns. Epic States correspond to one of 3 types: Unstarted, Started, or
    Done.
    """

    model_config = ConfigDict(populate_by_name=True)

    description: str = Field(description="The description of what sort of Epics belong in that Epic State.")
    entity_type: str = Field(description="A string description of this resource.")
    color: str | None = Field(default=None, description="The hex color for this Epic State.")
    name: str = Field(description="The Epic State's name.")
    global_id: str
    type: str = Field(description="The type of Epic State (Unstarted, Started, or Done)")
    updated_at: datetime = Field(description="When the Epic State was last updated.")
    id: int = Field(description="The unique ID of the Epic State.")
    position: int = Field(description="The position that the Epic State is in, starting with 0 at the left.")
    created_at: datetime = Field(description="The time/date the Epic State was created.")


class EpicWorkflow(BaseModel):
    """
    Epic Workflow is the array of defined Epic States. Epic Workflow can be queried using the API but must be
    updated in the Shortcut UI.
    """

    model_config = ConfigDict(populate_by_name=True)

    entity_type: str = Field(description="A string description of this resource.")
    id: int = Field(description="The unique ID of the Epic Workflow.")
    created_at: datetime = Field(description="The date the Epic Workflow was created.")
    updated_at: datetime = Field(description="The date the Epic Workflow was updated.")
    default_epic_state_id: int = Field(description="The unique ID of the default Epic State that new Epics are assi...")
    epic_states: list[EpicState] = Field(description="A map of the Epic States in this Epic Workflow.")


class GetDoc(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    content_format: Literal["markdown", "html"] | None = Field(default=None, description="Format of the content to ...")


class Icon(BaseModel):
    """
    Icons are used to attach images to Groups, Workspaces, Members, and Loading screens in the Shortcut web
    application.
    """

    model_config = ConfigDict(populate_by_name=True)

    entity_type: str = Field(description="A string description of this resource.")
    id: str = Field(description="The unique ID of the Icon.")
    created_at: datetime = Field(description="The time/date that the Icon was created.")
    updated_at: datetime = Field(description="The time/date that the Icon was updated.")
    url: str = Field(description="The URL of the Icon.")


class Group(BaseModel):
    """A Group."""

    model_config = ConfigDict(populate_by_name=True)

    app_url: str = Field(description="The Shortcut application url for the Group.")
    description: str = Field(description="The description of the Group.")
    archived: bool = Field(description="Whether or not the Group is archived.")
    entity_type: str = Field(description="A string description of this resource.")
    color: str | None = Field(description='The hex color to be displayed with the Group (for example, "#ff0000").')
    num_stories_started: int = Field(description="The number of stories assigned to the group which are in a starte...")
    mention_name: str = Field(description="The mention name of the Group.")
    name: str = Field(description="The name of the Group.")
    global_id: str
    color_key: str | None = Field(description="The color key to be displayed with the Group.")
    num_stories: int = Field(description="The total number of stories assigned to the group.")
    num_epics_started: int = Field(description="The number of epics assigned to the group which are in the started ...")
    updated_at: datetime = Field(description="The last instant when this group was updated.")
    num_stories_backlog: int = Field(description="The number of stories assigned to the group which are in a backlo...")
    id: str = Field(description="The id of the Group.")
    display_icon: Icon
    default_workflow_id: int | None = Field(default=None, description="The ID of the default workflow for stories c...")
    member_ids: list[str] = Field(description="The Member IDs contain within the Group.")
    workflow_ids: list[int] = Field(description="The Workflow IDs contained within the Group.")
    created_at: datetime = Field(description="The instant when this group was created.")


class History(BaseModel):
    """A history item is a group of actions that represent a transactional change to a Story."""

    model_config = ConfigDict(populate_by_name=True)

    actor_name: str | None = Field(default=None, description="The name of the actor that performed the action, if i...")
    changed_at: str = Field(description="The date when the change occurred.")
    primary_id: dict[str, Any] | None = Field(default=None, description="The ID of the primary entity that has chan...")
    references: list[dict[str, Any]] | None = Field(default=None, description="An array of objects affected by the ...")
    actions: list[dict[str, Any]] = Field(description="An array of actions that were performed for the change.")
    member_id: str | None = Field(default=None, description="The ID of the member who performed the change.")
    external_id: str | None = Field(default=None, description="The ID of the webhook that handled the change.")
    id: str = Field(description="The ID representing the change for the story.")
    version: Literal["v1"] = Field(description="The version of the change format.")
    webhook_id: str | None = Field(default=None, description="The ID of the webhook that handled the change.")
    automation_id: str | None = Field(default=None, description="The ID of the automation that performed the change.")


class HistoryActionBranchCreate(BaseModel):
    """An action representing a VCS Branch being created."""

    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    name: str = Field(description="The name of the VCS Branch that was pushed")
    url: str = Field(description="The URL from the provider of the VCS Branch that was pushed")
    action: Literal["create"] = Field(description="The action of the entity referenced.")


class HistoryActionBranchMerge(BaseModel):
    """An action representing a VCS Branch being merged."""

    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    name: str = Field(description="The name of the VCS Branch that was pushed")
    url: str = Field(description="The URL from the provider of the VCS Branch that was pushed")
    action: Literal["merge"] = Field(description="The action of the entity referenced.")


class HistoryActionBranchPush(BaseModel):
    """An action representing a VCS Branch being pushed."""

    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    name: str = Field(description="The name of the VCS Branch that was pushed")
    url: str = Field(description="The URL from the provider of the VCS Branch that was pushed")
    action: Literal["push"] = Field(description="The action of the entity referenced.")


class HistoryActionLabelCreate(BaseModel):
    """An action representing a Label being created."""

    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    action: Literal["create"] = Field(description="The action of the entity referenced.")
    app_url: str = Field(description="The application URL of the Label.")
    name: str = Field(description="The name of the Label.")


class HistoryActionLabelDelete(BaseModel):
    """An action representing a Label being deleted."""

    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    action: Literal["delete"] = Field(description="The action of the entity referenced.")
    name: str = Field(description="The name of the Label.")


class HistoryActionLabelUpdate(BaseModel):
    """An action representing a Label being updated."""

    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    action: Literal["update"] = Field(description="The action of the entity referenced.")


class HistoryActionProjectUpdate(BaseModel):
    """An action representing a Project being updated."""

    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    action: Literal["update"] = Field(description="The action of the entity referenced.")
    app_url: str = Field(description="The application URL of the Project.")
    name: str = Field(description="The name of the Project.")


class HistoryActionPullRequest(BaseModel):
    """An action representing various operations for a Pull Request."""

    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    action: Literal["open", "update", "reopen", "close", "sync", "comment"] = Field(description="The action of the ...")
    number: int = Field(description="The VCS Repository-specific ID for the Pull Request.")
    title: str = Field(description="The title of the Pull Request.")
    url: str = Field(description="The URL from the provider of the VCS Pull Request.")


class HistoryActionStoryCommentCreate(BaseModel):
    """An action representing a Story Comment being created."""

    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    action: Literal["create"] = Field(description="The action of the entity referenced.")
    app_url: str = Field(description="The application URL of the Story Comment.")
    author_id: str = Field(description="The Member ID of who created the Story Comment.")


class HistoryActionStoryCreate(BaseModel):
    """An action representing a Story being created."""

    model_config = ConfigDict(populate_by_name=True)

    app_url: str = Field(description="The application URL of the Story.")
    description: str | None = Field(default=None, description="The description of the Story.")
    started: bool | None = Field(default=None, description="Whether or not the Story has been started.")
    entity_type: str = Field(description="The type of entity referenced.")
    task_ids: list[int] | None = Field(default=None, description="An array of Task IDs on this Story.")
    story_type: Literal["feature", "chore", "bug"] = Field(description="The type of Story; either feature, bug, or ...")
    name: str = Field(description="The name of the Story.")
    completed: bool | None = Field(default=None, description="Whether or not the Story is completed.")
    blocker: bool | None = Field(default=None, description="Whether or not the Story is blocking another Story.")
    epic_id: int | None = Field(default=None, description="The Epic ID for this Story.")
    requested_by_id: str | None = Field(default=None, description="The ID of the Member that requested the Story.")
    iteration_id: int | None = Field(default=None, description="The Iteration ID the Story is in.")
    label_ids: list[int] | None = Field(default=None, description="An array of Labels IDs attached to the Story.")
    group_id: str | None = Field(default=None, description="The Team IDs for the followers of the Story.")
    workflow_state_id: int | None = Field(default=None, description="An array of Workflow State IDs attached to the...")
    object_story_link_ids: list[int] | None = Field(default=None, description="An array of Story IDs that are the o...")
    follower_ids: list[str] | None = Field(default=None, description="An array of Member IDs for the followers of t...")
    owner_ids: list[str] | None = Field(default=None, description="An array of Member IDs that are the owners of th...")
    custom_field_value_ids: list[str] | None = Field(default=None, description="An array of Custom Field Enum Value...")
    id: int = Field(description="The ID of the entity referenced.")
    parent_story_id: int | None = Field(default=None, description="The Story's Parent ID (only applicable if Story ...")
    estimate: int | None = Field(default=None, description="The estimate (or point value) for the Story.")
    subject_story_link_ids: list[int] | None = Field(default=None, description="An array of Story IDs that are the ...")
    action: Literal["create"] = Field(description="The action of the entity referenced.")
    blocked: bool | None = Field(default=None, description="Whether or not the Story is blocked by another Story.")
    project_id: int | None = Field(default=None, description="The Project ID of the Story is in.")
    deadline: str | None = Field(default=None, description="The timestamp representing the Story's deadline.")


class HistoryActionStoryDelete(BaseModel):
    """An action representing a Story being deleted."""

    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    action: Literal["delete"] = Field(description="The action of the entity referenced.")
    name: str = Field(description="The name of the Story.")
    story_type: Literal["feature", "chore", "bug"] = Field(description="The type of Story; either feature, bug, or ...")
    parent_story_id: int | None = Field(default=None, description="The Story's Parent ID (only applicable if Story ...")


class HistoryActionStoryLinkCreate(BaseModel):
    """An action representing a Story Link being created."""

    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    action: Literal["create"] = Field(description="The action of the entity referenced.")
    verb: Literal["blocks", "duplicates", "relates to"] = Field(description="The verb describing the link's relatio...")
    subject_id: int = Field(description="The Story ID of the subject Story.")
    object_id: int = Field(description="The Story ID of the object Story.")


class HistoryActionStoryLinkDelete(BaseModel):
    """An action representing a Story Link being deleted."""

    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    action: Literal["delete"] = Field(description="The action of the entity referenced.")
    verb: Literal["blocks", "duplicates", "relates to"] = Field(description="The verb describing the link's relatio...")
    subject_id: int | None = Field(description="The Story ID of the subject Story.")
    object_id: int | None = Field(description="The Story ID of the object Story.")


class StoryHistoryChangeOldNewStr(BaseModel):
    """A timestamp that represents the Story's deadline."""

    model_config = ConfigDict(populate_by_name=True)

    old: str | None = Field(default=None, description="The old value.")
    new: str | None = Field(default=None, description="The new value.")


class StoryHistoryChangeOldNewInt(BaseModel):
    """The estimate value for the Story"""

    model_config = ConfigDict(populate_by_name=True)

    old: int | None = Field(default=None, description="The old value.")
    new: int | None = Field(default=None, description="The new value.")


class HistoryChangesStoryLink(BaseModel):
    """The changes that have occurred as a result of the action."""

    model_config = ConfigDict(populate_by_name=True)

    verb: StoryHistoryChangeOldNewStr | None = Field(default=None)
    object_id: StoryHistoryChangeOldNewInt | None = Field(default=None)
    subject_id: StoryHistoryChangeOldNewInt | None = Field(default=None)


class HistoryActionStoryLinkUpdate(BaseModel):
    """An action representing a Story Link being updated."""

    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    action: Literal["update"] = Field(description="The action of the entity referenced.")
    verb: Literal["blocks", "duplicates", "relates to"] = Field(description="The verb describing the link's relatio...")
    subject_id: int = Field(description="The Story ID of the subject Story.")
    object_id: int = Field(description="The Story ID of the object Story.")
    changes: HistoryChangesStoryLink


class StoryHistoryChangeOldNewBool(BaseModel):
    """True if the Story has archived, otherwise false."""

    model_config = ConfigDict(populate_by_name=True)

    old: bool | None = Field(default=None, description="The old value.")
    new: bool | None = Field(default=None, description="The new value.")


class StoryHistoryChangeAddsRemovesInt(BaseModel):
    """Task IDs that have been added or removed from the Story."""

    model_config = ConfigDict(populate_by_name=True)

    adds: list[int] | None = Field(default=None, description="The values that have been added.")
    removes: list[int] | None = Field(default=None, description="The values that have been removed")


class StoryHistoryChangeAddsRemovesUuid(BaseModel):
    """Custom Field Enum Value IDs that have been added or removed from the Story."""

    model_config = ConfigDict(populate_by_name=True)

    adds: list[str] | None = Field(default=None, description="The values that have been added.")
    removes: list[str] | None = Field(default=None, description="The values that have been removed")


class StoryHistoryChangeOldNewUuid(BaseModel):
    """The Team ID for the Story."""

    model_config = ConfigDict(populate_by_name=True)

    old: str | None = Field(default=None, description="The old value.")
    new: str | None = Field(default=None, description="The new value.")


class HistoryChangesStory(BaseModel):
    """The changes that have occurred as a result of the action."""

    model_config = ConfigDict(populate_by_name=True)

    description: StoryHistoryChangeOldNewStr | None = Field(default=None)
    archived: StoryHistoryChangeOldNewBool | None = Field(default=None)
    started: StoryHistoryChangeOldNewBool | None = Field(default=None)
    task_ids: StoryHistoryChangeAddsRemovesInt | None = Field(default=None)
    mention_ids: StoryHistoryChangeAddsRemovesUuid | None = Field(default=None)
    story_type: StoryHistoryChangeOldNewStr | None = Field(default=None)
    name: StoryHistoryChangeOldNewStr | None = Field(default=None)
    completed: StoryHistoryChangeOldNewBool | None = Field(default=None)
    blocker: StoryHistoryChangeOldNewBool | None = Field(default=None)
    epic_id: StoryHistoryChangeOldNewInt | None = Field(default=None)
    branch_ids: StoryHistoryChangeAddsRemovesInt | None = Field(default=None)
    commit_ids: StoryHistoryChangeAddsRemovesInt | None = Field(default=None)
    requested_by_id: StoryHistoryChangeOldNewUuid | None = Field(default=None)
    iteration_id: StoryHistoryChangeOldNewInt | None = Field(default=None)
    label_ids: StoryHistoryChangeAddsRemovesInt | None = Field(default=None)
    group_id: StoryHistoryChangeOldNewUuid | None = Field(default=None)
    workflow_state_id: StoryHistoryChangeOldNewInt | None = Field(default=None)
    object_story_link_ids: StoryHistoryChangeAddsRemovesInt | None = Field(default=None)
    follower_ids: StoryHistoryChangeAddsRemovesUuid | None = Field(default=None)
    owner_ids: StoryHistoryChangeAddsRemovesUuid | None = Field(default=None)
    custom_field_value_ids: StoryHistoryChangeAddsRemovesUuid | None = Field(default=None)
    parent_story_id: StoryHistoryChangeOldNewInt | None = Field(default=None)
    estimate: StoryHistoryChangeOldNewInt | None = Field(default=None)
    subject_story_link_ids: StoryHistoryChangeAddsRemovesInt | None = Field(default=None)
    blocked: StoryHistoryChangeOldNewBool | None = Field(default=None)
    project_id: StoryHistoryChangeOldNewInt | None = Field(default=None)
    deadline: StoryHistoryChangeOldNewStr | None = Field(default=None)


class HistoryActionStoryUpdate(BaseModel):
    """An action representing a Story being updated."""

    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    action: Literal["update"] = Field(description="The action of the entity referenced.")
    app_url: str = Field(description="The application URL of the Story.")
    changes: HistoryChangesStory | None = Field(default=None)
    name: str = Field(description="The name of the Story.")
    story_type: Literal["feature", "chore", "bug"] = Field(description="The type of Story; either feature, bug, or ...")
    parent_story_id: int | None = Field(default=None, description="The Story's Parent ID (only applicable if Story ...")


class HistoryActionTaskCreate(BaseModel):
    """An action representing a Task being created."""

    model_config = ConfigDict(populate_by_name=True)

    description: str = Field(description="The description of the Task.")
    entity_type: str = Field(description="The type of entity referenced.")
    mention_ids: list[str] | None = Field(default=None, description="An array of Member IDs that represent who has ...")
    group_mention_ids: list[str] | None = Field(default=None, description="An array of Groups IDs that represent wh...")
    owner_ids: list[str] | None = Field(default=None, description="An array of Member IDs that represent the Task's...")
    id: int = Field(description="The ID of the entity referenced.")
    action: Literal["create"] = Field(description="The action of the entity referenced.")
    complete: bool = Field(description="Whether or not the Task is complete.")
    deadline: str | None = Field(default=None, description="A timestamp that represent's the Task's deadline.")


class HistoryActionTaskDelete(BaseModel):
    """An action representing a Task being deleted."""

    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    action: Literal["delete"] = Field(description="The action of the entity referenced.")
    description: str = Field(description="The description of the Task being deleted.")


class HistoryChangesTask(BaseModel):
    """The changes that have occurred as a result of the action."""

    model_config = ConfigDict(populate_by_name=True)

    complete: StoryHistoryChangeOldNewBool | None = Field(default=None)
    description: StoryHistoryChangeOldNewStr | None = Field(default=None)
    mention_ids: StoryHistoryChangeAddsRemovesUuid | None = Field(default=None)
    owner_ids: StoryHistoryChangeAddsRemovesUuid | None = Field(default=None)


class HistoryActionTaskUpdate(BaseModel):
    """An action representing a Task being updated."""

    model_config = ConfigDict(populate_by_name=True)

    id: int = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    action: Literal["update"] = Field(description="The action of the entity referenced.")
    changes: HistoryChangesTask
    complete: bool | None = Field(default=None, description="Whether or not the Task is complete.")
    description: str = Field(description="The description of the Task.")
    story_id: int = Field(description="The Story ID that contains the Task.")


class HistoryActionWorkspace2BulkUpdate(BaseModel):
    """An action representing a bulk operation within a workspace2."""

    model_config = ConfigDict(populate_by_name=True)

    id: str = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    action: Literal["bulk-update"] = Field(description="The action of the entity referenced.")
    name: str = Field(description="The name of the workspace2 in which the BulkUpdate occurred.")


class HistoryReferenceBranch(BaseModel):
    """A reference to a VCS Branch."""

    model_config = ConfigDict(populate_by_name=True)

    id: dict[str, Any] = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    name: str = Field(description="The name of the entity referenced.")
    url: str = Field(description="The external URL for the Branch.")


class HistoryReferenceCommit(BaseModel):
    """A reference to a VCS Commit."""

    model_config = ConfigDict(populate_by_name=True)

    id: dict[str, Any] = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    message: str = Field(description="The message from the Commit.")
    url: str = Field(description="The external URL for the Branch.")


class HistoryReferenceCustomFieldEnumValue(BaseModel):
    """A reference to a CustomField value asserted on a Story."""

    model_config = ConfigDict(populate_by_name=True)

    id: dict[str, Any] = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    string_value: str | None = Field(description="The custom-field enum value as a string.")
    enum_value_enabled: bool | None = Field(description="Whether or not the custom-field enum value is enabled.")
    field_id: str = Field(description="The public-id of the parent custom-field of this enum value.")
    field_type: str = Field(description="The type variety of the parent custom-field of this enum value.")
    field_name: str = Field(description="The name as it is displayed to the user of the parent custom-field of this...")
    field_enabled: bool = Field(description="Whether or not the custom-field is enabled.")


class HistoryReferenceEpic(BaseModel):
    """A reference to an Epic."""

    model_config = ConfigDict(populate_by_name=True)

    id: dict[str, Any] = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    app_url: str = Field(description="The application URL of the Epic.")
    name: str = Field(description="The name of the entity referenced.")


class HistoryReferenceGeneral(BaseModel):
    """A default reference for entity types that don't have extra fields."""

    model_config = ConfigDict(populate_by_name=True)

    id: dict[str, Any] = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    name: str = Field(description="The name of the entity referenced.")


class HistoryReferenceGroup(BaseModel):
    """A reference to a Group."""

    model_config = ConfigDict(populate_by_name=True)

    id: str = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    name: str = Field(description="The name of the entity referenced.")


class HistoryReferenceIteration(BaseModel):
    """A reference to an Iteration."""

    model_config = ConfigDict(populate_by_name=True)

    id: dict[str, Any] = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    app_url: str = Field(description="The application URL of the Iteration.")
    name: str = Field(description="The name of the entity referenced.")


class HistoryReferenceLabel(BaseModel):
    """A reference to an Label."""

    model_config = ConfigDict(populate_by_name=True)

    id: dict[str, Any] = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    app_url: str = Field(description="The application URL of the Label.")
    name: str = Field(description="The name of the entity referenced.")


class HistoryReferenceProject(BaseModel):
    """A reference to an Project."""

    model_config = ConfigDict(populate_by_name=True)

    id: dict[str, Any] = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    app_url: str = Field(description="The application URL of the Project.")
    name: str = Field(description="The name of the entity referenced.")


class HistoryReferenceStory(BaseModel):
    """A reference to a Story."""

    model_config = ConfigDict(populate_by_name=True)

    id: dict[str, Any] = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    app_url: str = Field(description="The application URL of the Story.")
    name: str = Field(description="The name of the entity referenced.")
    story_type: Literal["feature", "chore", "bug"] = Field(description="If the referenced entity is a Story, either...")
    parent_story_id: int | None = Field(default=None, description="The Story's Parent ID (only applicable if Story ...")


class HistoryReferenceStoryTask(BaseModel):
    """A reference to a Story Task."""

    model_config = ConfigDict(populate_by_name=True)

    id: dict[str, Any] = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    description: str = Field(description="The description of the Story Task.")


class HistoryReferenceWorkflowState(BaseModel):
    """A references to a Story Workflow State."""

    model_config = ConfigDict(populate_by_name=True)

    id: dict[str, Any] = Field(description="The ID of the entity referenced.")
    entity_type: str = Field(description="The type of entity referenced.")
    type: Literal["started", "backlog", "unstarted", "done"] = Field(description='Either "backlog", "unstarted"...')
    name: str = Field(description="The name of the entity referenced.")


class LabelStats(BaseModel):
    """
    A group of calculated values for this Label. This is not included if the slim? flag is set to true for the List
    Labels endpoint.
    """

    model_config = ConfigDict(populate_by_name=True)

    num_related_documents: int = Field(description="The total number of Documents associated this Label.")
    num_epics: int = Field(description="The total number of Epics with this Label.")
    num_stories_unstarted: int = Field(description="The total number of stories unstarted Stories with this Label.")
    num_stories_total: int = Field(description="The total number of Stories with this Label.")
    num_epics_unstarted: int = Field(description="The number of unstarted epics associated with this label.")
    num_epics_in_progress: int = Field(description="The number of in progress epics associated with this label.")
    num_points_unstarted: int = Field(description="The total number of unstarted points with this Label.")
    num_stories_unestimated: int = Field(description="The total number of Stories with no point estimate with this ...")
    num_points_in_progress: int = Field(description="The total number of in-progress points with this Label.")
    num_epics_total: int = Field(description="The total number of Epics associated with this Label.")
    num_stories_completed: int = Field(description="The total number of completed Stories with this Label.")
    num_points_completed: int = Field(description="The total number of completed points with this Label.")
    num_stories_backlog: int = Field(description="The total number of stories backlog Stories with this Label.")
    num_points_total: int = Field(description="The total number of points with this Label.")
    num_stories_in_progress: int = Field(description="The total number of in-progress Stories with this Label.")
    num_points_backlog: int = Field(description="The total number of backlog points with this Label.")
    num_epics_completed: int = Field(description="The number of completed Epics associated with this Label.")


class Label(BaseModel):
    """A Label can be used to associate and filter Stories and Epics, and also create new Workspaces."""

    model_config = ConfigDict(populate_by_name=True)

    app_url: str = Field(description="The Shortcut application url for the Label.")
    description: str | None = Field(description="The description of the Label.")
    archived: bool = Field(description="A true/false boolean indicating if the Label has been archived.")
    entity_type: str = Field(description="A string description of this resource.")
    color: str | None = Field(description='The hex color to be displayed with the Label (for example, "#ff0000").')
    name: str = Field(description="The name of the Label.")
    global_id: str
    updated_at: datetime | None = Field(description="The time/date that the Label was updated.")
    external_id: str | None = Field(description="This field can be set to another unique ID. In the case that the L...")
    id: int = Field(description="The unique ID of the Label.")
    stats: LabelStats | None = Field(default=None)
    created_at: datetime | None = Field(description="The time/date that the Label was created.")


class IterationAssociatedGroup(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    group_id: str = Field(description="The Group ID of the associated group.")
    associated_stories_count: int | None = Field(default=None, description="The number of stories this Group owns i...")


class IterationStats(BaseModel):
    """A group of calculated values for this Iteration."""

    model_config = ConfigDict(populate_by_name=True)

    num_points_done: int = Field(description="The total number of completed points in this Iteration.")
    num_related_documents: int = Field(description="The total number of documents related to an Iteration")
    average_cycle_time: int | None = Field(default=None, description="The average cycle time (in seconds) of comple...")
    num_stories_unstarted: int = Field(description="The total number of unstarted Stories in this Iteration.")
    num_points_started: int = Field(description="The total number of started points in this Iteration.")
    num_points_unstarted: int = Field(description="The total number of unstarted points in this Iteration.")
    num_stories_started: int = Field(description="The total number of started Stories in this Iteration.")
    num_stories_unestimated: int = Field(description="The total number of Stories with no point estimate.")
    num_stories_backlog: int = Field(description="The total number of backlog Stories in this Iteration.")
    average_lead_time: int | None = Field(default=None, description="The average lead time (in seconds) of complete...")
    num_points_backlog: int = Field(description="The total number of backlog points in this Iteration.")
    num_points: int = Field(description="The total number of points in this Iteration.")
    num_stories_done: int = Field(description="The total number of done Stories in this Iteration.")


class Iteration(BaseModel):
    """
    An Iteration is a defined, time-boxed period of development for a collection of Stories. See
    https://help.shortcut.com/hc/en-us/articles/360028953452-Iterations-Overview for more information.
    """

    model_config = ConfigDict(populate_by_name=True)

    app_url: str = Field(description="The Shortcut application url for the Iteration.")
    description: str = Field(description="The description of the iteration.")
    entity_type: str = Field(description="A string description of this resource")
    labels: list[Label] = Field(description="An array of labels attached to the iteration.")
    mention_ids: list[str] = Field(description="`Deprecated:` use `member_mention_ids`.")
    member_mention_ids: list[str] = Field(description="An array of Member IDs that have been mentioned in the Story...")
    associated_groups: list[IterationAssociatedGroup] = Field(description="An array containing Group IDs and Group-...")
    name: str = Field(description="The name of the iteration.")
    global_id: str
    label_ids: list[int] = Field(description="An array of label ids attached to the iteration.")
    updated_at: datetime = Field(description="The instant when this iteration was last updated.")
    group_mention_ids: list[str] = Field(description="An array of Group IDs that have been mentioned in the Story d...")
    end_date: datetime = Field(description="The date this iteration ends.")
    follower_ids: list[str] = Field(description="An array of UUIDs for any Members listed as Followers.")
    group_ids: list[str] = Field(description="An array of UUIDs for any Groups you want to add as Followers. Curren...")
    start_date: datetime = Field(description="The date this iteration begins.")
    status: str = Field(description='The status of the iteration. Values are either "unstarted", "started", or ...')
    id: int = Field(description="The ID of the iteration.")
    stats: IterationStats
    created_at: datetime = Field(description="The instant when this iteration was created.")


class IterationSlim(BaseModel):
    """
    IterationSlim represents the same resource as an Iteration, but is more light-weight. Use the [Get
    Iteration](#Get-Iteration) endpoint to fetch the unabridged payload for an Iteration.
    """

    model_config = ConfigDict(populate_by_name=True)

    app_url: str = Field(description="The Shortcut application url for the Iteration.")
    entity_type: str = Field(description="A string description of this resource")
    labels: list[Label] = Field(description="An array of labels attached to the iteration.")
    mention_ids: list[str] = Field(description="`Deprecated:` use `member_mention_ids`.")
    member_mention_ids: list[str] = Field(description="An array of Member IDs that have been mentioned in the Story...")
    associated_groups: list[IterationAssociatedGroup] = Field(description="An array containing Group IDs and Group-...")
    name: str = Field(description="The name of the iteration.")
    global_id: str
    label_ids: list[int] = Field(description="An array of label ids attached to the iteration.")
    updated_at: datetime = Field(description="The instant when this iteration was last updated.")
    group_mention_ids: list[str] = Field(description="An array of Group IDs that have been mentioned in the Story d...")
    end_date: datetime = Field(description="The date this iteration ends.")
    follower_ids: list[str] = Field(description="An array of UUIDs for any Members listed as Followers.")
    group_ids: list[str] = Field(description="An array of UUIDs for any Groups you want to add as Followers. Curren...")
    start_date: datetime = Field(description="The date this iteration begins.")
    status: str = Field(description='The status of the iteration. Values are either "unstarted", "started", or ...')
    id: int = Field(description="The ID of the iteration.")
    stats: IterationStats
    created_at: datetime = Field(description="The instant when this iteration was created.")


class IterationSearchResults(BaseModel):
    """The results of the Iteration search query."""

    model_config = ConfigDict(populate_by_name=True)

    total: int = Field(description="The total number of matches for the search query. The first 1000 matches can be...")
    data: list[IterationSlim] = Field(description="A list of search results.")
    next: str | None = Field(description="The URL path and query string for the next page of search results.")


class KeyResultValue(BaseModel):
    """The starting value of the Key Result."""

    model_config = ConfigDict(populate_by_name=True)

    numeric_value: str | None = Field(default=None, description="The numeric value, as a decimal string. No more th...")
    boolean_value: bool | None = Field(default=None, description="The boolean value.")


class KeyResult(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str = Field(description="The ID of the Key Result.")
    name: str = Field(description="The name of the Key Result.")
    objective_id: int = Field(description="The Objective to which this Key Result belongs.")
    type: Literal["percent", "boolean", "numeric"] = Field(description="The type of the Key Result (numeric, percen...")
    initial_observed_value: KeyResultValue
    current_observed_value: KeyResultValue
    current_target_value: KeyResultValue
    progress: int = Field(description="The integer percentage of progress toward completion of the Key Result.")


class LinkSubTaskParams(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    story_id: int = Field(description="The ID of the story to link as a sub-task of the parent story")


class MaxSearchResultsExceededError(BaseModel):
    """Error returned when total maximum supported results have been reached."""

    model_config = ConfigDict(populate_by_name=True)

    error: Literal["maximum-results-exceeded"] = Field(description="The name for this type of error, `maximum-resul...")
    message: str = Field(description='An explanatory message: "A maximum of 1000 search results are supported."')
    maximum_results: int = Field(alias="maximum-results", description="The maximum number of search results support...")


class Profile(BaseModel):
    """A group of Member profile details."""

    model_config = ConfigDict(populate_by_name=True)

    entity_type: str = Field(description="A string description of this resource.")
    deactivated: bool = Field(description="A true/false boolean indicating whether the Member has been deactivated ...")
    two_factor_auth_activated: bool | None = Field(default=None, description="If Two Factor Authentication is activ...")
    mention_name: str = Field(description="The Member's username within the Organization.")
    name: str | None = Field(description="The Member's name within the Organization.")
    is_agent: bool | None = Field(default=None, description="Whether this profile is an Agent/Bot user.")
    gravatar_hash: str | None = Field(description="This is the gravatar hash associated with email_address.")
    id: str = Field(description="The unique identifier of the profile.")
    display_icon: Icon
    is_owner: bool = Field(description="A boolean indicating whether this profile is an owner at their associated o...")
    email_address: str | None = Field(description="The primary email address of the Member with the Organization.")


class Member(BaseModel):
    """Details about an individual user within the Workspace."""

    model_config = ConfigDict(populate_by_name=True)

    role: str = Field(description="The Member's role in the Workspace.")
    entity_type: str = Field(description="A string description of this resource.")
    disabled: bool = Field(description="True/false boolean indicating whether the Member has been disabled within t...")
    global_id: str
    state: Literal["partial", "full", "disabled", "imported"] = Field(description="The user state, one of partial, ...")
    updated_at: datetime | None = Field(description="The time/date the Member was last updated.")
    created_without_invite: bool = Field(description="Whether this member was created as a placeholder entity.")
    group_ids: list[str] = Field(description="The Member's group ids")
    id: str = Field(description="The Member's ID in Shortcut.")
    installation_id: str | None = Field(default=None, description="Only set for agents. The installation id associa...")
    profile: Profile
    created_at: datetime | None = Field(description="The time/date the Member was created.")
    replaced_by: str | None = Field(default=None, description="The id of the member that replaces this one when mer...")


class MemberInfoOrganization2(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str


class MemberInfo(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    is_owner: bool
    mention_name: str
    name: str
    role: str
    workspace2: BasicWorkspaceInfo
    organization2: MemberInfoOrganization2


class MilestoneStats(BaseModel):
    """A group of calculated values for this Milestone."""

    model_config = ConfigDict(populate_by_name=True)

    average_cycle_time: int | None = Field(default=None, description="The average cycle time (in seconds) of comple...")
    average_lead_time: int | None = Field(default=None, description="The average lead time (in seconds) of complete...")
    num_related_documents: int = Field(description="The number of related documents to this Milestone.")


class Milestone(BaseModel):
    """
    (Deprecated) A Milestone is a collection of Epics that represent a release or some other large initiative that
    you are working on. Milestones have become Objectives, so you should use Objective-related API resources instead
    of Milestone ones.
    """

    model_config = ConfigDict(populate_by_name=True)

    app_url: str = Field(description="The Shortcut application url for the Milestone.")
    description: str = Field(description="The Milestone's description.")
    archived: bool = Field(description="A boolean indicating whether the Milestone has been archived or not.")
    started: bool = Field(description="A true/false boolean indicating if the Milestone has been started.")
    entity_type: str = Field(description="A string description of this resource.")
    completed_at_override: datetime | None = Field(description="A manual override for the time/date the Milestone w...")
    started_at: datetime | None = Field(description="The time/date the Milestone was started.")
    completed_at: datetime | None = Field(description="The time/date the Milestone was completed.")
    name: str = Field(description="The name of the Milestone.")
    global_id: str
    completed: bool = Field(description="A true/false boolean indicating if the Milestone has been completed.")
    state: str = Field(description="The workflow state that the Milestone is in.")
    started_at_override: datetime | None = Field(description="A manual override for the time/date the Milestone was...")
    updated_at: datetime = Field(description="The time/date the Milestone was updated.")
    categories: list[Category] = Field(description="An array of Categories attached to the Milestone.")
    id: int = Field(description="The unique ID of the Milestone.")
    key_result_ids: list[str] = Field(description="The IDs of the Key Results associated with the Objective.")
    position: int = Field(description="A number representing the position of the Milestone in relation to every oth...")
    stats: MilestoneStats
    created_at: datetime = Field(description="The time/date the Milestone was created.")


class ObjectiveStats(BaseModel):
    """A group of calculated values for this Objective."""

    model_config = ConfigDict(populate_by_name=True)

    average_cycle_time: int | None = Field(default=None, description="The average cycle time (in seconds) of comple...")
    average_lead_time: int | None = Field(default=None, description="The average lead time (in seconds) of complete...")
    num_related_documents: int = Field(description="The number of related documents to this Objective.")


class Objective(BaseModel):
    """
    An Objective is a collection of Epics that represent a release or some other large initiative that you are
    working on.
    """

    model_config = ConfigDict(populate_by_name=True)

    app_url: str = Field(description="The Shortcut application url for the Objective.")
    description: str = Field(description="The Objective's description.")
    archived: bool = Field(description="A boolean indicating whether the Objective has been archived or not.")
    started: bool = Field(description="A true/false boolean indicating if the Objective has been started.")
    entity_type: str = Field(description="A string description of this resource.")
    completed_at_override: datetime | None = Field(description="A manual override for the time/date the Objective w...")
    started_at: datetime | None = Field(description="The time/date the Objective was started.")
    completed_at: datetime | None = Field(description="The time/date the Objective was completed.")
    name: str = Field(description="The name of the Objective.")
    global_id: str
    completed: bool = Field(description="A true/false boolean indicating if the Objectivehas been completed.")
    state: str = Field(description="The workflow state that the Objective is in.")
    started_at_override: datetime | None = Field(description="A manual override for the time/date the Objective was...")
    updated_at: datetime = Field(description="The time/date the Objective was updated.")
    categories: list[Category] = Field(description="An array of Categories attached to the Objective.")
    id: int = Field(description="The unique ID of the Objective.")
    key_result_ids: list[str] = Field(description="The IDs of the Key Results associated with the Objective.")
    position: int = Field(description="A number representing the position of the Objective in relation to every oth...")
    stats: ObjectiveStats
    created_at: datetime = Field(description="The time/date the Objective was created.")


class ObjectiveSearchResult(BaseModel):
    """
    A Milestone in search results. This is typed differently from Milestone because the details=slim search argument
    will omit some fields.
    """

    model_config = ConfigDict(populate_by_name=True)

    app_url: str = Field(description="The Shortcut application url for the Milestone.")
    description: str | None = Field(default=None, description="The Milestone's description.")
    archived: bool = Field(description="A boolean indicating whether the Milestone has been archived or not.")
    started: bool = Field(description="A true/false boolean indicating if the Milestone has been started.")
    entity_type: str = Field(description="A string description of this resource.")
    completed_at_override: datetime | None = Field(description="A manual override for the time/date the Milestone w...")
    started_at: datetime | None = Field(description="The time/date the Milestone was started.")
    completed_at: datetime | None = Field(description="The time/date the Milestone was completed.")
    name: str = Field(description="The name of the Milestone.")
    global_id: str
    completed: bool = Field(description="A true/false boolean indicating if the Milestone has been completed.")
    state: str = Field(description="The workflow state that the Milestone is in.")
    started_at_override: datetime | None = Field(description="A manual override for the time/date the Milestone was...")
    updated_at: datetime = Field(description="The time/date the Milestone was updated.")
    categories: list[Category] = Field(description="An array of Categories attached to the Milestone.")
    id: int = Field(description="The unique ID of the Milestone.")
    key_result_ids: list[str] = Field(description="The IDs of the Key Results associated with the Objective.")
    position: int = Field(description="A number representing the position of the Milestone in relation to every oth...")
    stats: MilestoneStats
    created_at: datetime = Field(description="The time/date the Milestone was created.")


class ObjectiveSearchResults(BaseModel):
    """The results of the Objective search query."""

    model_config = ConfigDict(populate_by_name=True)

    total: int = Field(description="The total number of matches for the search query. The first 1000 matches can be...")
    data: list[ObjectiveSearchResult] = Field(description="A list of search results.")
    next: str | None = Field(description="The URL path and query string for the next page of search results.")


class ProjectStats(BaseModel):
    """A group of calculated values for this Project."""

    model_config = ConfigDict(populate_by_name=True)

    num_stories: int = Field(description="The total number of stories in this Project.")
    num_points: int = Field(description="The total number of points in this Project.")
    num_related_documents: int = Field(description="The total number of documents related to this Project")


class Project(BaseModel):
    """
    Projects typically map to teams (such as Frontend, Backend, Mobile, Devops, etc) but can represent any open-
    ended product, component, or initiative.
    """

    model_config = ConfigDict(populate_by_name=True)

    app_url: str = Field(description="The Shortcut application url for the Project.")
    description: str | None = Field(description="The description of the Project.")
    archived: bool = Field(description="True/false boolean indicating whether the Project is in an Archived state.")
    entity_type: str = Field(description="A string description of this resource.")
    days_to_thermometer: int = Field(description="The number of days before the thermometer appears in the Story su...")
    color: str | None = Field(description="The color associated with the Project in the Shortcut member interface.")
    workflow_id: int = Field(description="The ID of the workflow the project belongs to.")
    name: str = Field(description="The name of the Project")
    global_id: str = Field(description="The Global ID of the Project.")
    start_time: datetime = Field(description="The date at which the Project was started.")
    updated_at: datetime | None = Field(description="The time/date that the Project was last updated.")
    follower_ids: list[str] = Field(description="An array of UUIDs for any Members listed as Followers.")
    external_id: str | None = Field(description="This field can be set to another unique ID. In the case that the P...")
    id: int = Field(description="The unique ID of the Project.")
    show_thermometer: bool = Field(description="Configuration to enable or disable thermometers in the Story summary.")
    team_id: int = Field(description="The ID of the team the project belongs to.")
    iteration_length: int = Field(description="The number of weeks per iteration in this Project.")
    abbreviation: str | None = Field(description="The Project abbreviation used in Story summaries. Should be kept ...")
    stats: ProjectStats
    created_at: datetime | None = Field(description="The time/date that the Project was created.")


class Repository(BaseModel):
    """Repository refers to a VCS repository."""

    model_config = ConfigDict(populate_by_name=True)

    entity_type: str = Field(description="A string description of this resource.")
    name: str | None = Field(description="The shorthand name of the VCS repository.")
    type: Literal["github", "gitlab", "bitbucket"] = Field(description="The VCS provider for the Repository.")
    updated_at: datetime | None = Field(description="The time/date the Repository was updated.")
    external_id: str | None = Field(description="The VCS unique identifier for the Repository.")
    id: int | None = Field(description="The ID associated to the VCS repository in Shortcut.")
    url: str | None = Field(description="The URL of the Repository.")
    full_name: str | None = Field(description="The full name of the VCS repository.")
    created_at: datetime | None = Field(description="The time/date the Repository was created.")


class TypedStoryLink(BaseModel):
    """The type of Story Link. The string can be subject or object."""

    model_config = ConfigDict(populate_by_name=True)

    entity_type: str = Field(description="A string description of this resource.")
    object_id: int = Field(description="The ID of the object Story.")
    verb: str = Field(description='How the subject Story acts on the object Story. This can be "blocks", "duplic...')
    type: str = Field(description="This indicates whether the Story is the subject or object in the Story Link.")
    updated_at: datetime = Field(description="The time/date when the Story Link was last updated.")
    id: int = Field(description="The unique identifier of the Story Link.")
    subject_id: int = Field(description="The ID of the subject Story.")
    subject_workflow_state_id: int = Field(description='The workflow state of the "subject" story.')
    created_at: datetime = Field(description="The time/date when the Story Link was created.")


class SyncedItem(BaseModel):
    """The synced item for the story."""

    model_config = ConfigDict(populate_by_name=True)

    external_id: str = Field(description="The id used to reference an external entity.")
    url: str = Field(description="The url to the external entity.")


class StoryCustomField(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    field_id: str = Field(description="The unique public ID for a CustomField.")
    value_id: str = Field(description="The unique public ID for a CustomFieldEnumValue.")
    value: str = Field(description="A string representation of the value, if applicable.")


class StoryReaction(BaseModel):
    """Emoji reaction on a comment."""

    model_config = ConfigDict(populate_by_name=True)

    emoji: str = Field(description="Emoji text of the reaction.")
    permission_ids: list[str] = Field(description="Permissions who have reacted with this.")


class StoryComment(BaseModel):
    """A Comment is any note added within the Comment field of a Story."""

    model_config = ConfigDict(populate_by_name=True)

    app_url: str = Field(description="The Shortcut application url for the Comment.")
    entity_type: str = Field(description="A string description of this resource.")
    deleted: bool = Field(description="True/false boolean indicating whether the Comment has been deleted.")
    story_id: int = Field(description="The ID of the Story on which the Comment appears.")
    mention_ids: list[str] = Field(description="`Deprecated:` use `member_mention_ids`.")
    author_id: str | None = Field(description="The unique ID of the Member who is the Comment's author.")
    member_mention_ids: list[str] = Field(description="The unique IDs of the Member who are mentioned in the Comment.")
    blocker: bool | None = Field(default=None, description="Marks the comment as a blocker that can be surfaced to ...")
    linked_to_slack: bool = Field(description="Whether the Comment is currently the root of a thread that is linked...")
    updated_at: datetime | None = Field(description="The time/date when the Comment was updated.")
    group_mention_ids: list[str] = Field(description="The unique IDs of the Group who are mentioned in the Comment.")
    external_id: str | None = Field(description="This field can be set to another unique ID. In the case that the C...")
    parent_id: int | None = Field(default=None, description="The ID of the parent Comment this Comment is threaded ...")
    id: int = Field(description="The unique ID of the Comment.")
    position: int = Field(description="The Comments numerical position in the list from oldest to newest.")
    unblocks_parent: bool | None = Field(default=None, description="Marks the comment as an unblocker to its  block...")
    reactions: list[StoryReaction] = Field(description="A set of Reactions to this Comment.")
    created_at: datetime = Field(description="The time/date when the Comment was created.")
    text: str | None = Field(description="The text of the Comment. In the case that the Comment has been deleted, t...")


class Task(BaseModel):
    """A Task on a Story."""

    model_config = ConfigDict(populate_by_name=True)

    description: str = Field(description="Full text of the Task.")
    entity_type: str = Field(description="A string description of this resource.")
    story_id: int = Field(description="The unique identifier of the parent Story.")
    mention_ids: list[str] = Field(description="`Deprecated:` use `member_mention_ids`.")
    member_mention_ids: list[str] = Field(description="An array of UUIDs of Members mentioned in this Task.")
    completed_at: datetime | None = Field(description="The time/date the Task was completed.")
    global_id: str
    updated_at: datetime | None = Field(description="The time/date the Task was updated.")
    group_mention_ids: list[str] = Field(description="An array of UUIDs of Groups mentioned in this Task.")
    owner_ids: list[str] = Field(description="An array of UUIDs of the Owners of this Task.")
    external_id: str | None = Field(description="This field can be set to another unique ID. In the case that the T...")
    id: int = Field(description="The unique ID of the Task.")
    position: int = Field(description="The number corresponding to the Task's position within a list of Tasks on a ...")
    complete: bool = Field(description="True/false boolean indicating whether the Task has been completed.")
    created_at: datetime = Field(description="The time/date the Task was created.")


class StoryStats(BaseModel):
    """The stats object for Stories"""

    model_config = ConfigDict(populate_by_name=True)

    num_related_documents: int = Field(description="The number of documents related to this Story.")


class StorySearchResult(BaseModel):
    """
    A Story in search results. This is typed differently from Story because the details=slim search argument will
    omit some fields.
    """

    model_config = ConfigDict(populate_by_name=True)

    app_url: str = Field(description="The Shortcut application url for the Story.")
    description: str | None = Field(default=None, description="The description of the story.")
    archived: bool = Field(description="True if the story has been archived or not.")
    started: bool = Field(description="A true/false boolean indicating if the Story has been started.")
    story_links: list[TypedStoryLink] = Field(description="An array of story links attached to the Story.")
    entity_type: str = Field(description="A string description of this resource.")
    labels: list[LabelSlim] = Field(description="An array of labels attached to the story.")
    task_ids: list[int] | None = Field(default=None, description="An array of IDs of Tasks attached to the story.")
    mention_ids: list[str] = Field(description="`Deprecated:` use `member_mention_ids`.")
    synced_item: SyncedItem | None = Field(default=None)
    member_mention_ids: list[str] = Field(description="An array of Member IDs that have been mentioned in the Story...")
    story_type: str = Field(description="The type of story (feature, bug, chore).")
    custom_fields: list[StoryCustomField] | None = Field(default=None, description="An array of CustomField value a...")
    linked_files: list[LinkedFile] | None = Field(default=None, description="An array of linked files attached to t...")
    file_ids: list[int] | None = Field(default=None, description="An array of IDs of Files attached to the story.")
    num_tasks_completed: int | None = Field(default=None, description="The number of tasks on the story which are c...")
    workflow_id: int = Field(description="The ID of the workflow the story belongs to.")
    completed_at_override: datetime | None = Field(description="A manual override for the time/date the Story was c...")
    started_at: datetime | None = Field(description="The time/date the Story was started.")
    completed_at: datetime | None = Field(description="The time/date the Story was completed.")
    name: str = Field(description="The name of the story.")
    global_id: str
    completed: bool = Field(description="A true/false boolean indicating if the Story has been completed.")
    comments: list[StoryComment] | None = Field(default=None, description="An array of comments attached to the story.")
    blocker: bool = Field(description="A true/false boolean indicating if the Story is currently a blocker of anoth...")
    branches: list[Branch] | None = Field(default=None, description="An array of Git branches attached to the story.")
    epic_id: int | None = Field(description="The ID of the epic the story belongs to.")
    story_template_id: str | None = Field(description="The ID of the story template used to create this story, or n...")
    external_links: list[str] = Field(description="An array of external links (strings) associated with a Story")
    previous_iteration_ids: list[int] = Field(description="The IDs of the iteration the story belongs to.")
    requested_by_id: str = Field(description="The ID of the Member that requested the story.")
    iteration_id: int | None = Field(description="The ID of the iteration the story belongs to.")
    sub_task_story_ids: list[int] | None = Field(default=None, description="The Story IDs of Sub-tasks attached to ...")
    tasks: list[Task] | None = Field(default=None, description="An array of tasks connected to the story.")
    formatted_vcs_branch_name: str | None = Field(default=None, description="The formatted branch name for this story.")
    label_ids: list[int] = Field(description="An array of label ids attached to the story.")
    started_at_override: datetime | None = Field(description="A manual override for the time/date the Story was sta...")
    group_id: str | None = Field(description="The ID of the group associated with the story.")
    workflow_state_id: int = Field(description="The ID of the workflow state the story is currently in.")
    updated_at: datetime | None = Field(description="The time/date the Story was updated.")
    pull_requests: list[PullRequest] | None = Field(default=None, description="An array of Pull/Merge Requests atta...")
    group_mention_ids: list[str] = Field(description="An array of Group IDs that have been mentioned in the Story d...")
    follower_ids: list[str] = Field(description="An array of UUIDs for any Members listed as Followers.")
    owner_ids: list[str] = Field(description="An array of UUIDs of the owners of this story.")
    external_id: str | None = Field(description="This field can be set to another unique ID. In the case that the S...")
    id: int = Field(description="The unique ID of the Story.")
    lead_time: int | None = Field(default=None, description="The lead time (in seconds) of this story when complete.")
    parent_story_id: int | None = Field(default=None, description="The ID of the parent story to this story (making...")
    estimate: int | None = Field(description="The numeric point estimate of the story. Can also be null, which mean...")
    commits: list[Commit] | None = Field(default=None, description="An array of commits attached to the story.")
    files: list[UploadedFile] | None = Field(default=None, description="An array of files attached to the story.")
    position: int = Field(description="A number representing the position of the story in relation to every other s...")
    blocked: bool = Field(description="A true/false boolean indicating if the Story is currently blocked.")
    project_id: int | None = Field(description="The ID of the project the story belongs to.")
    linked_file_ids: list[int] | None = Field(default=None, description="An array of IDs of LinkedFiles attached to...")
    deadline: datetime | None = Field(description="The due date of the story.")
    stats: StoryStats
    comment_ids: list[int] | None = Field(default=None, description="An array of IDs of Comments attached to the st...")
    cycle_time: int | None = Field(default=None, description="The cycle time (in seconds) of this story when complete.")
    created_at: datetime = Field(description="The time/date the Story was created.")
    moved_at: datetime | None = Field(description="The time/date the Story was last changed workflow-state.")


class StorySearchResults(BaseModel):
    """The results of the Story search query."""

    model_config = ConfigDict(populate_by_name=True)

    total: int = Field(description="The total number of matches for the search query. The first 1000 matches can be...")
    data: list[StorySearchResult] = Field(description="A list of search results.")
    next: str | None = Field(description="The URL path and query string for the next page of search results.")


class SearchResults(BaseModel):
    """The results of the multi-entity search query."""

    model_config = ConfigDict(populate_by_name=True)

    epics: EpicSearchResults | None = Field(default=None)
    stories: StorySearchResults | None = Field(default=None)
    iterations: IterationSearchResults | None = Field(default=None)
    milestones: ObjectiveSearchResults | None = Field(default=None)


class SearchStories(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    archived: bool | None = Field(default=None, description="A true/false boolean indicating whether the Story is i...")
    owner_id: str | None = Field(default=None, description="An array of UUIDs for any Users who may be Owners of th...")
    story_type: Literal["feature", "chore", "bug"] | None = Field(default=None, description="The type of Stories th...")
    epic_ids: list[int] | None = Field(default=None, description="The Epic IDs that may be associated with the Stor...")
    project_ids: list[int] | None = Field(default=None, description="The IDs for the Projects the Stories may be as...")
    updated_at_end: datetime | None = Field(default=None, description="Stories should have been updated on or befor...")
    completed_at_end: datetime | None = Field(default=None, description="Stories should have been completed on or b...")
    workflow_state_types: list[Literal["started", "backlog", "unstarted", "done"]] | None = Field(default=None)
    deadline_end: datetime | None = Field(default=None, description="Stories should have a deadline on or before th...")
    created_at_start: datetime | None = Field(default=None, description="Stories should have been created on or aft...")
    epic_id: int | None = Field(default=None, description="The Epic IDs that may be associated with the Stories.")
    label_name: str | None = Field(default=None, description="The name of any associated Labels.")
    requested_by_id: str | None = Field(default=None, description="The UUID of any Users who may have requested the...")
    iteration_id: int | None = Field(default=None, description="The Iteration ID that may be associated with the St...")
    label_ids: list[int] | None = Field(default=None, description="The Label IDs that may be associated with the St...")
    group_id: str | None = Field(default=None, description="The Group ID that is associated with the Stories")
    workflow_state_id: int | None = Field(default=None, description="The unique IDs of the specific Workflow States...")
    iteration_ids: list[int] | None = Field(default=None, description="The Iteration IDs that may be associated wit...")
    created_at_end: datetime | None = Field(default=None, description="Stories should have been created on or befor...")
    deadline_start: datetime | None = Field(default=None, description="Stories should have a deadline on or after t...")
    group_ids: list[str] | None = Field(default=None, description="The Group IDs that are associated with the Stories")
    owner_ids: list[str] | None = Field(default=None, description="An array of UUIDs for any Users who may be Owner...")
    external_id: str | None = Field(default=None, description="An ID or URL that references an external resource. U...")
    includes_description: bool | None = Field(default=None, description="Whether to include the story description i...")
    estimate: int | None = Field(default=None, description="The number of estimate points associate with the Stories.")
    project_id: int | None = Field(default=None, description="The IDs for the Projects the Stories may be assigned to.")
    completed_at_start: datetime | None = Field(default=None, description="Stories should have been completed on or...")
    updated_at_start: datetime | None = Field(default=None, description="Stories should have been updated on or aft...")


class Story(BaseModel):
    """Stories are the standard unit of work in Shortcut and represent individual features, bugs, and chores."""

    model_config = ConfigDict(populate_by_name=True)

    app_url: str = Field(description="The Shortcut application url for the Story.")
    description: str = Field(description="The description of the story.")
    archived: bool = Field(description="True if the story has been archived or not.")
    started: bool = Field(description="A true/false boolean indicating if the Story has been started.")
    story_links: list[TypedStoryLink] = Field(description="An array of story links attached to the Story.")
    entity_type: str = Field(description="A string description of this resource.")
    labels: list[LabelSlim] = Field(description="An array of labels attached to the story.")
    mention_ids: list[str] = Field(description="`Deprecated:` use `member_mention_ids`.")
    synced_item: SyncedItem | None = Field(default=None)
    member_mention_ids: list[str] = Field(description="An array of Member IDs that have been mentioned in the Story...")
    story_type: str = Field(description="The type of story (feature, bug, chore).")
    custom_fields: list[StoryCustomField] | None = Field(default=None, description="An array of CustomField value a...")
    linked_files: list[LinkedFile] = Field(description="An array of linked files attached to the story.")
    workflow_id: int = Field(description="The ID of the workflow the story belongs to.")
    completed_at_override: datetime | None = Field(description="A manual override for the time/date the Story was c...")
    started_at: datetime | None = Field(description="The time/date the Story was started.")
    completed_at: datetime | None = Field(description="The time/date the Story was completed.")
    name: str = Field(description="The name of the story.")
    global_id: str
    completed: bool = Field(description="A true/false boolean indicating if the Story has been completed.")
    comments: list[StoryComment] = Field(description="An array of comments attached to the story.")
    blocker: bool = Field(description="A true/false boolean indicating if the Story is currently a blocker of anoth...")
    branches: list[Branch] = Field(description="An array of Git branches attached to the story.")
    epic_id: int | None = Field(description="The ID of the epic the story belongs to.")
    story_template_id: str | None = Field(description="The ID of the story template used to create this story, or n...")
    external_links: list[str] = Field(description="An array of external links (strings) associated with a Story")
    previous_iteration_ids: list[int] = Field(description="The IDs of the iteration the story belongs to.")
    requested_by_id: str = Field(description="The ID of the Member that requested the story.")
    iteration_id: int | None = Field(description="The ID of the iteration the story belongs to.")
    sub_task_story_ids: list[int] | None = Field(default=None, description="The Story IDs of Sub-tasks attached to ...")
    tasks: list[Task] = Field(description="An array of tasks connected to the story.")
    formatted_vcs_branch_name: str | None = Field(default=None, description="The formatted branch name for this story.")
    label_ids: list[int] = Field(description="An array of label ids attached to the story.")
    started_at_override: datetime | None = Field(description="A manual override for the time/date the Story was sta...")
    group_id: str | None = Field(description="The ID of the group associated with the story.")
    workflow_state_id: int = Field(description="The ID of the workflow state the story is currently in.")
    updated_at: datetime | None = Field(description="The time/date the Story was updated.")
    pull_requests: list[PullRequest] = Field(description="An array of Pull/Merge Requests attached to the story.")
    group_mention_ids: list[str] = Field(description="An array of Group IDs that have been mentioned in the Story d...")
    follower_ids: list[str] = Field(description="An array of UUIDs for any Members listed as Followers.")
    owner_ids: list[str] = Field(description="An array of UUIDs of the owners of this story.")
    external_id: str | None = Field(description="This field can be set to another unique ID. In the case that the S...")
    id: int = Field(description="The unique ID of the Story.")
    lead_time: int | None = Field(default=None, description="The lead time (in seconds) of this story when complete.")
    parent_story_id: int | None = Field(default=None, description="The ID of the parent story to this story (making...")
    estimate: int | None = Field(description="The numeric point estimate of the story. Can also be null, which mean...")
    commits: list[Commit] = Field(description="An array of commits attached to the story.")
    files: list[UploadedFile] = Field(description="An array of files attached to the story.")
    position: int = Field(description="A number representing the position of the story in relation to every other s...")
    blocked: bool = Field(description="A true/false boolean indicating if the Story is currently blocked.")
    project_id: int | None = Field(description="The ID of the project the story belongs to.")
    deadline: datetime | None = Field(description="The due date of the story.")
    stats: StoryStats
    cycle_time: int | None = Field(default=None, description="The cycle time (in seconds) of this story when complete.")
    created_at: datetime = Field(description="The time/date the Story was created.")
    moved_at: datetime | None = Field(description="The time/date the Story was last changed workflow-state.")


class StoryLink(BaseModel):
    """
    Story links allow you create semantic relationships between two stories. Relationship types are relates to,
    blocks / blocked by, and duplicates / is duplicated by. The format is `subject -> link -> object`, or for
    example "story 5 blocks story 6".
    """

    model_config = ConfigDict(populate_by_name=True)

    entity_type: str = Field(description="A string description of this resource.")
    id: int = Field(description="The unique identifier of the Story Link.")
    subject_id: int = Field(description="The ID of the subject Story.")
    subject_workflow_state_id: int = Field(description='The workflow state of the "subject" story.')
    verb: str = Field(description='How the subject Story acts on the object Story. This can be "blocks", "duplic...')
    object_id: int = Field(description="The ID of the object Story.")
    created_at: datetime = Field(description="The time/date when the Story Link was created.")
    updated_at: datetime = Field(description="The time/date when the Story Link was last updated.")


class StorySlim(BaseModel):
    """
    StorySlim represents the same resource as a Story, but is more light-weight. For certain fields it provides ids
    rather than full resources (e.g., `comment_ids` and `file_ids`) and it also excludes certain aggregate values
    (e.g., `cycle_time`). The `description` field can be optionally included. Use the [Get Story](#Get-Story)
    endpoint to fetch the unabridged payload for a Story.
    """

    model_config = ConfigDict(populate_by_name=True)

    app_url: str = Field(description="The Shortcut application url for the Story.")
    description: str | None = Field(default=None, description="The description of the Story.")
    archived: bool = Field(description="True if the story has been archived or not.")
    started: bool = Field(description="A true/false boolean indicating if the Story has been started.")
    story_links: list[TypedStoryLink] = Field(description="An array of story links attached to the Story.")
    entity_type: str = Field(description="A string description of this resource.")
    labels: list[LabelSlim] = Field(description="An array of labels attached to the story.")
    task_ids: list[int] = Field(description="An array of IDs of Tasks attached to the story.")
    mention_ids: list[str] = Field(description="`Deprecated:` use `member_mention_ids`.")
    synced_item: SyncedItem | None = Field(default=None)
    member_mention_ids: list[str] = Field(description="An array of Member IDs that have been mentioned in the Story...")
    story_type: str = Field(description="The type of story (feature, bug, chore).")
    custom_fields: list[StoryCustomField] | None = Field(default=None, description="An array of CustomField value a...")
    file_ids: list[int] = Field(description="An array of IDs of Files attached to the story.")
    num_tasks_completed: int = Field(description="The number of tasks on the story which are complete.")
    workflow_id: int = Field(description="The ID of the workflow the story belongs to.")
    completed_at_override: datetime | None = Field(description="A manual override for the time/date the Story was c...")
    started_at: datetime | None = Field(description="The time/date the Story was started.")
    completed_at: datetime | None = Field(description="The time/date the Story was completed.")
    name: str = Field(description="The name of the story.")
    global_id: str
    completed: bool = Field(description="A true/false boolean indicating if the Story has been completed.")
    blocker: bool = Field(description="A true/false boolean indicating if the Story is currently a blocker of anoth...")
    epic_id: int | None = Field(description="The ID of the epic the story belongs to.")
    story_template_id: str | None = Field(description="The ID of the story template used to create this story, or n...")
    external_links: list[str] = Field(description="An array of external links (strings) associated with a Story")
    previous_iteration_ids: list[int] = Field(description="The IDs of the iteration the story belongs to.")
    requested_by_id: str = Field(description="The ID of the Member that requested the story.")
    iteration_id: int | None = Field(description="The ID of the iteration the story belongs to.")
    sub_task_story_ids: list[int] | None = Field(default=None, description="The Story IDs of Sub-tasks attached to ...")
    formatted_vcs_branch_name: str | None = Field(default=None, description="The formatted branch name for this story.")
    label_ids: list[int] = Field(description="An array of label ids attached to the story.")
    started_at_override: datetime | None = Field(description="A manual override for the time/date the Story was sta...")
    group_id: str | None = Field(description="The ID of the group associated with the story.")
    workflow_state_id: int = Field(description="The ID of the workflow state the story is currently in.")
    updated_at: datetime | None = Field(description="The time/date the Story was updated.")
    group_mention_ids: list[str] = Field(description="An array of Group IDs that have been mentioned in the Story d...")
    follower_ids: list[str] = Field(description="An array of UUIDs for any Members listed as Followers.")
    owner_ids: list[str] = Field(description="An array of UUIDs of the owners of this story.")
    external_id: str | None = Field(description="This field can be set to another unique ID. In the case that the S...")
    id: int = Field(description="The unique ID of the Story.")
    lead_time: int | None = Field(default=None, description="The lead time (in seconds) of this story when complete.")
    parent_story_id: int | None = Field(default=None, description="The ID of the parent story to this story (making...")
    estimate: int | None = Field(description="The numeric point estimate of the story. Can also be null, which mean...")
    position: int = Field(description="A number representing the position of the story in relation to every other s...")
    blocked: bool = Field(description="A true/false boolean indicating if the Story is currently blocked.")
    project_id: int | None = Field(description="The ID of the project the story belongs to.")
    linked_file_ids: list[int] = Field(description="An array of IDs of LinkedFiles attached to the story.")
    deadline: datetime | None = Field(description="The due date of the story.")
    stats: StoryStats
    comment_ids: list[int] = Field(description="An array of IDs of Comments attached to the story.")
    cycle_time: int | None = Field(default=None, description="The cycle time (in seconds) of this story when complete.")
    created_at: datetime = Field(description="The time/date the Story was created.")
    moved_at: datetime | None = Field(description="The time/date the Story was last changed workflow-state.")


class UnprocessableError(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    message: str


class UnusableEntitlementError(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    reason_tag: Literal["entitlement-violation"] = Field(description="The tag for violating an entitlement action.")
    entitlement_tag: str = Field(description="Short tag describing the unusable entitlement action taken by the user.")
    message: str = Field(description="Message displayed to the user on why their action failed.")


class UpdateCategory(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = Field(default=None, description="The new name of the Category.")
    color: str | None = Field(default=None, description="The hex color to be displayed with the Category (for examp...")
    archived: bool | None = Field(default=None, description="A true/false boolean indicating if the Category has be...")


class UpdateComment(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    text: str = Field(description="The updated comment text.")


class UpdateCustomFieldEnumValue(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str | None = Field(default=None, description="The unique ID of an existing EnumValue within the CustomField...")
    value: str | None = Field(default=None, description="A string value within the domain of this Custom Field.")
    color_key: str | None = Field(default=None, description="A color key associated with this EnumValue within the ...")
    enabled: bool | None = Field(default=None, description="Whether this EnumValue is enabled for its CustomField o...")


class UpdateCustomField(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    enabled: bool | None = Field(default=None, description="Indicates whether the Field is enabled for the Workspac...")
    name: str | None = Field(default=None, description="A collection of objects representing reporting periods for ...")
    values: list[UpdateCustomFieldEnumValue] | None = Field(default=None, description="A collection of EnumValue ob...")
    icon_set_identifier: str | None = Field(default=None, description="A frontend-controlled string that represents...")
    description: str | None = Field(default=None, description="A description of the purpose of this field.")
    before_id: str | None = Field(default=None, description="The ID of the CustomField we want to move this CustomF...")
    after_id: str | None = Field(default=None, description="The ID of the CustomField we want to move this CustomFi...")


class UpdateDoc(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default=None, description="The new title for the document")
    content: str | None = Field(default=None, description="The new content for the document.")
    content_format: Literal["markdown", "html"] | None = Field(default=None, description="Format of content. For in...")


class UpdateStoryContents(BaseModel):
    """Updated attributes for the template to populate."""

    model_config = ConfigDict(populate_by_name=True)

    description: str | None = Field(default=None, description="The description of the story.")
    labels: list[CreateLabelParams] | None = Field(default=None, description="An array of labels to be populated by...")
    story_type: str | None = Field(default=None, description="The type of story (feature, bug, chore).")
    custom_fields: list[CustomFieldValueParams] | None = Field(default=None, description="An array of maps specifyi...")
    file_ids: list[int] | None = Field(default=None, description="An array of the attached file IDs to be populated.")
    name: str | None = Field(default=None, description="The name of the story.")
    epic_id: int | None = Field(default=None, description="The ID of the epic the to be populated.")
    external_links: list[str] | None = Field(default=None, description="An array of external links to be populated.")
    sub_tasks: list[CreateSubTaskParams] | None = Field(default=None, description="An array of maps specifying the ...")
    iteration_id: int | None = Field(default=None, description="The ID of the iteration the to be populated.")
    tasks: list[BaseTaskParams] | None = Field(default=None, description="An array of tasks to be populated by the ...")
    group_id: str | None = Field(default=None, description="The ID of the group to be populated.")
    workflow_state_id: int | None = Field(default=None, description="The ID of the workflow state to be populated.")
    follower_ids: list[str] | None = Field(default=None, description="An array of UUIDs for any Members listed as F...")
    owner_ids: list[str] | None = Field(default=None, description="An array of UUIDs of the owners of this story.")
    estimate: int | None = Field(default=None, description="The numeric point estimate to be populated.")
    project_id: int | None = Field(default=None, description="The ID of the project the story belongs to.")
    linked_file_ids: list[int] | None = Field(default=None, description="An array of the linked file IDs to be popu...")
    deadline: datetime | None = Field(default=None, description="The due date of the story.")


class UpdateEntityTemplate(BaseModel):
    """
    Request parameters for changing either a template's name or any of   the attributes it is designed to pre-
    populate.
    """

    model_config = ConfigDict(populate_by_name=True)

    name: str | None = Field(default=None, description="The updated template name.")
    story_contents: UpdateStoryContents | None = Field(default=None)


class UpdateEpic(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    description: str | None = Field(default=None, description="The Epic's description.")
    archived: bool | None = Field(default=None, description="A true/false boolean indicating whether the Epic is in...")
    labels: list[CreateLabelParams] | None = Field(default=None, description="An array of Labels attached to the Epic.")
    completed_at_override: datetime | None = Field(default=None, description="A manual override for the time/date t...")
    objective_ids: list[int] | None = Field(default=None, description="An array of IDs for Objectives to which this...")
    name: str | None = Field(default=None, description="The Epic's name.")
    planned_start_date: datetime | None = Field(default=None, description="The Epic's planned start date.")
    state: Literal["in progress", "to do", "done"] | None = Field(default=None, description="`Deprecated` The Epic'...")
    milestone_id: int | None = Field(default=None, description="`Deprecated` The ID of the Milestone this Epic is r...")
    requested_by_id: str | None = Field(default=None, description="The ID of the member that requested the epic.")
    epic_state_id: int | None = Field(default=None, description="The ID of the Epic State.")
    started_at_override: datetime | None = Field(default=None, description="A manual override for the time/date the...")
    group_id: str | None = Field(default=None, description="`Deprecated` The ID of the group to associate with the ...")
    follower_ids: list[str] | None = Field(default=None, description="An array of UUIDs for any Members you want to...")
    group_ids: list[str] | None = Field(default=None, description="An array of UUIDS for Groups to which this Epic ...")
    owner_ids: list[str] | None = Field(default=None, description="An array of UUIDs for any members you want to ad...")
    external_id: str | None = Field(default=None, description="This field can be set to another unique ID. In the c...")
    before_id: int | None = Field(default=None, description="The ID of the Epic we want to move this Epic before.")
    after_id: int | None = Field(default=None, description="The ID of the Epic we want to move this Epic after.")
    deadline: datetime | None = Field(default=None, description="The Epic's deadline.")


class UpdateFile(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    description: str | None = Field(default=None, description="The description of the file.")
    created_at: datetime | None = Field(default=None, description="The time/date that the file was uploaded.")
    updated_at: datetime | None = Field(default=None, description="The time/date that the file was last updated.")
    name: str | None = Field(default=None, description="The name of the file.")
    uploader_id: str | None = Field(default=None, description="The unique ID assigned to the Member who uploaded th...")
    external_id: str | None = Field(default=None, description="An additional ID that you may wish to assign to the ...")


class UpdateGroup(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    description: str | None = Field(default=None, description="The description of this Group.")
    archived: bool | None = Field(default=None, description="Whether or not this Group is archived.")
    color: str | None = Field(default=None, description="The color you wish to use for the Group in the system.")
    display_icon_id: str | None = Field(default=None, description="The Icon id for the avatar of this Group.")
    mention_name: str | None = Field(default=None, description="The mention name of this Group.")
    name: str | None = Field(default=None, description="The name of this Group.")
    color_key: str | None = Field(default=None, description="The color key you wish to use for the Group in the sys...")
    default_workflow_id: int | None = Field(default=None, description="The ID of the default workflow for stories c...")
    member_ids: list[str] | None = Field(default=None, description="The Member ids to add to this Group.")
    workflow_ids: list[int] | None = Field(default=None, description="The Workflow ids to add to the Group.")


class UpdateHealth(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    status: Literal["At Risk", "On Track", "Off Track", "No Health"] | None = Field(default=None)
    text: str | None = Field(default=None, description="The description of the Health status.")


class UpdateIteration(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    follower_ids: list[str] | None = Field(default=None, description="An array of UUIDs for any Members you want to...")
    group_ids: list[str] | None = Field(default=None, description="An array of UUIDs for any Groups you want to add...")
    labels: list[CreateLabelParams] | None = Field(default=None, description="An array of Labels attached to the It...")
    description: str | None = Field(default=None, description="The description of the Iteration.")
    name: str | None = Field(default=None, description="The name of this Iteration")
    start_date: str | None = Field(default=None, description="The date this Iteration begins, e.g. 2019-07-01")
    end_date: str | None = Field(default=None, description="The date this Iteration ends, e.g. 2019-07-05.")


class UpdateKeyResult(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = Field(default=None, description="The name of the Key Result.")
    initial_observed_value: KeyResultValue | None = Field(default=None)
    observed_value: KeyResultValue | None = Field(default=None)
    target_value: KeyResultValue | None = Field(default=None)


class UpdateLabel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str | None = Field(default=None, description="The new name of the label.")
    description: str | None = Field(default=None, description="The new description of the label.")
    color: str | None = Field(default=None, description="The hex color to be displayed with the Label (for example,...")
    archived: bool | None = Field(default=None, description="A true/false boolean indicating if the Label has been ...")


class UpdateLinkedFile(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    description: str | None = Field(default=None, description="The description of the file.")
    story_id: int | None = Field(default=None, description="The ID of the linked story.")
    name: str | None = Field(default=None, description="The name of the file.")
    thumbnail_url: str | None = Field(default=None, description="The URL of the thumbnail, if the integration provi...")
    type: Literal["google", "url", "dropbox", "box", "onedrive"] | None = Field(default=None)
    size: int | None = Field(default=None, description="The filesize, if the integration provided it.")
    uploader_id: str | None = Field(default=None, description="The UUID of the member that uploaded the file.")
    url: str | None = Field(default=None, description="The URL of linked file.")


class UpdateMilestone(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    description: str | None = Field(default=None, description="The Milestone's description.")
    archived: bool | None = Field(default=None, description="A boolean indicating whether the Milestone is archived...")
    completed_at_override: datetime | None = Field(default=None, description="A manual override for the time/date t...")
    name: str | None = Field(default=None, description="The name of the Milestone.")
    state: Literal["in progress", "to do", "done"] | None = Field(default=None, description="The workflow state tha...")
    started_at_override: datetime | None = Field(default=None, description="A manual override for the time/date the...")
    categories: list[CreateCategoryParams] | None = Field(default=None, description="An array of IDs of Categories ...")
    before_id: int | None = Field(default=None, description="The ID of the Milestone we want to move this Milestone...")
    after_id: int | None = Field(default=None, description="The ID of the Milestone we want to move this Milestone ...")


class UpdateObjective(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    description: str | None = Field(default=None, description="The Objective's description.")
    archived: bool | None = Field(default=None, description="A boolean indicating whether the Objective is archived...")
    completed_at_override: datetime | None = Field(default=None, description="A manual override for the time/date t...")
    name: str | None = Field(default=None, description="The name of the Objective.")
    state: Literal["in progress", "to do", "done"] | None = Field(default=None, description="The workflow state tha...")
    started_at_override: datetime | None = Field(default=None, description="A manual override for the time/date the...")
    categories: list[CreateCategoryParams] | None = Field(default=None, description="An array of IDs of Categories ...")
    before_id: int | None = Field(default=None, description="The ID of the Objective we want to move this Objective...")
    after_id: int | None = Field(default=None, description="The ID of the Objective we want to move this Objective ...")


class UpdateProject(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    description: str | None = Field(default=None, description="The Project's description.")
    archived: bool | None = Field(default=None, description="A true/false boolean indicating whether the Story is i...")
    days_to_thermometer: int | None = Field(default=None, description="The number of days before the thermometer ap...")
    color: str | None = Field(default=None, description="The color that represents the Project in the UI.")
    name: str | None = Field(default=None, description="The Project's name.")
    follower_ids: list[str] | None = Field(default=None, description="An array of UUIDs for any Members you want to...")
    show_thermometer: bool | None = Field(default=None, description="Configuration to enable or disable thermometer...")
    team_id: int | None = Field(default=None, description="The ID of the team the project belongs to.")
    abbreviation: str | None = Field(default=None, description="The Project abbreviation used in Story summaries. S...")


class UpdateStories(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    archived: bool | None = Field(default=None, description="If the Stories should be archived or not.")
    story_ids: list[int] = Field(description="The Ids of the Stories you wish to update.")
    story_type: Literal["feature", "chore", "bug"] | None = Field(default=None, description="The type of story (fea...")
    move_to: Literal["last", "first"] | None = Field(default=None, description='One of "first" or "last". This ...')
    follower_ids_add: list[str] | None = Field(default=None, description="The UUIDs of the new followers to be added.")
    epic_id: int | None = Field(default=None, description="The ID of the epic the story belongs to.")
    external_links: list[str] | None = Field(default=None, description="An array of External Links associated with ...")
    follower_ids_remove: list[str] | None = Field(default=None, description="The UUIDs of the followers to be removed.")
    requested_by_id: str | None = Field(default=None, description="The ID of the member that requested the story.")
    iteration_id: int | None = Field(default=None, description="The ID of the iteration the story belongs to.")
    custom_fields_remove: list[CustomFieldValueParams] | None = Field(default=None, description="A map specifying a...")
    labels_add: list[CreateLabelParams] | None = Field(default=None, description="An array of labels to be added.")
    group_id: str | None = Field(default=None, description="The Id of the Group the Stories should belong to.")
    workflow_state_id: int | None = Field(default=None, description="The ID of the workflow state to put the storie...")
    before_id: int | None = Field(default=None, description="The ID of the story that the stories are to be moved b...")
    estimate: int | None = Field(default=None, description="The numeric point estimate of the story. Can also be nu...")
    after_id: int | None = Field(default=None, description="The ID of the story that the stories are to be moved be...")
    owner_ids_remove: list[str] | None = Field(default=None, description="The UUIDs of the owners to be removed.")
    custom_fields_add: list[CustomFieldValueParams] | None = Field(default=None, description="A map specifying a Cu...")
    project_id: int | None = Field(default=None, description="The ID of the Project the Stories should belong to.")
    labels_remove: list[CreateLabelParams] | None = Field(default=None, description="An array of labels to be removed.")
    deadline: datetime | None = Field(default=None, description="The due date of the story.")
    owner_ids_add: list[str] | None = Field(default=None, description="The UUIDs of the new owners to be added.")


class UpdateStory(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    description: str | None = Field(default=None, description="The description of the story.")
    archived: bool | None = Field(default=None, description="True if the story is archived, otherwise false.")
    labels: list[CreateLabelParams] | None = Field(default=None, description="An array of labels attached to the st...")
    pull_request_ids: list[int] | None = Field(default=None, description="An array of IDs of Pull/Merge Requests at...")
    story_type: Literal["feature", "chore", "bug"] | None = Field(default=None, description="The type of story (fea...")
    custom_fields: list[CustomFieldValueParams] | None = Field(default=None, description="A map specifying a Custom...")
    move_to: Literal["last", "first"] | None = Field(default=None, description='One of "first" or "last". This ...')
    file_ids: list[int] | None = Field(default=None, description="An array of IDs of files attached to the story.")
    completed_at_override: datetime | None = Field(default=None, description="A manual override for the time/date t...")
    name: str | None = Field(default=None, description="The title of the story.")
    epic_id: int | None = Field(default=None, description="The ID of the epic the story belongs to.")
    external_links: list[str] | None = Field(default=None, description="An array of External Links associated with ...")
    branch_ids: list[int] | None = Field(default=None, description="An array of IDs of Branches attached to the story.")
    commit_ids: list[int] | None = Field(default=None, description="An array of IDs of Commits attached to the story.")
    sub_tasks: list[LinkSubTaskParams] | None = Field(default=None, description="An array of story IDs to attach to...")
    requested_by_id: str | None = Field(default=None, description="The ID of the member that requested the story.")
    iteration_id: int | None = Field(default=None, description="The ID of the iteration the story belongs to.")
    started_at_override: datetime | None = Field(default=None, description="A manual override for the time/date the...")
    group_id: str | None = Field(default=None, description="The ID of the group to associate with this story")
    workflow_state_id: int | None = Field(default=None, description="The ID of the workflow state to put the story in.")
    follower_ids: list[str] | None = Field(default=None, description="An array of UUIDs of the followers of this st...")
    owner_ids: list[str] | None = Field(default=None, description="An array of UUIDs of the owners of this story.")
    parent_story_id: int | None = Field(default=None, description="The parent story id. If you want to unset this v...")
    before_id: int | None = Field(default=None, description="The ID of the story we want to move this story before.")
    estimate: int | None = Field(default=None, description="The numeric point estimate of the story. Can also be nu...")
    after_id: int | None = Field(default=None, description="The ID of the story we want to move this story after.")
    project_id: int | None = Field(default=None, description="The ID of the project the story belongs to.")
    linked_file_ids: list[int] | None = Field(default=None, description="An array of IDs of linked files attached t...")
    deadline: datetime | None = Field(default=None, description="The due date of the story.")


class UpdateStoryComment(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    text: str = Field(description="The updated comment text.")


class UpdateStoryLink(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    verb: Literal["blocks", "duplicates", "relates to"] | None = Field(default=None)
    subject_id: int | None = Field(default=None, description="The ID of the subject Story.")
    object_id: int | None = Field(default=None, description="The ID of the object Story.")


class UpdateTask(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    description: str | None = Field(default=None, description="The Task's description.")
    owner_ids: list[str] | None = Field(default=None, description="An array of UUIDs of the owners of this story.")
    complete: bool | None = Field(default=None, description="A true/false boolean indicating whether the task is co...")
    before_id: int | None = Field(default=None, description="Move task before this task ID.")
    after_id: int | None = Field(default=None, description="Move task after this task ID.")


class WorkflowState(BaseModel):
    """
    Workflow State is any of the at least 3 columns. Workflow States correspond to one of 3 types: Unstarted,
    Started, or Done.
    """

    model_config = ConfigDict(populate_by_name=True)

    description: str = Field(description="The description of what sort of Stories belong in that Workflow state.")
    entity_type: str = Field(description="A string description of this resource.")
    color: str | None = Field(default=None, description="The hex color for this Workflow State.")
    verb: str | None = Field(description="The verb that triggers a move to that Workflow State when making VCS comm...")
    name: str = Field(description="The Workflow State's name.")
    global_id: str
    num_stories: int = Field(description="The number of Stories currently in that Workflow State.")
    type: str = Field(description="The type of Workflow State (Unstarted, Started, or Finished)")
    updated_at: datetime = Field(description="When the Workflow State was last updated.")
    id: int = Field(description="The unique ID of the Workflow State.")
    num_story_templates: int = Field(description="The number of Story Templates associated with that Workflow State.")
    position: int = Field(description="The position that the Workflow State is in, starting with 0 at the left.")
    created_at: datetime = Field(description="The time/date the Workflow State was created.")


class Workflow(BaseModel):
    """
    Workflow is the array of defined Workflow States. Workflow can be queried using the API but must be updated in
    the Shortcut UI.
    """

    model_config = ConfigDict(populate_by_name=True)

    description: str = Field(description="A description of the workflow.")
    entity_type: str = Field(description="A string description of this resource.")
    project_ids: list[float] = Field(description="An array of IDs of projects within the Workflow.")
    states: list[WorkflowState] = Field(description="A map of the states in this Workflow.")
    name: str = Field(description="The name of the workflow.")
    updated_at: datetime = Field(description="The date the Workflow was updated.")
    auto_assign_owner: bool = Field(description="Indicates if an owner is automatically assigned when an unowned st...")
    id: int = Field(description="The unique ID of the Workflow.")
    team_id: int = Field(description="The ID of the team the workflow belongs to.")
    created_at: datetime = Field(description="The date the Workflow was created.")
    default_state_id: int = Field(description="The unique ID of the default state that new Stories are entered into.")


# Rebuild all models to resolve forward references
BaseTaskParams.model_rebuild()
BasicWorkspaceInfo.model_rebuild()
PullRequestLabel.model_rebuild()
PullRequest.model_rebuild()
Branch.model_rebuild()
Category.model_rebuild()
Identity.model_rebuild()
Commit.model_rebuild()
CreateCategory.model_rebuild()
CreateCategoryParams.model_rebuild()
CreateCommentComment.model_rebuild()
CreateDoc.model_rebuild()
CreateLabelParams.model_rebuild()
CustomFieldValueParams.model_rebuild()
CreateSubTaskParams.model_rebuild()
CreateStoryContents.model_rebuild()
CreateEntityTemplate.model_rebuild()
CreateEpic.model_rebuild()
CreateEpicComment.model_rebuild()
CreateEpicHealth.model_rebuild()
CreateGenericIntegration.model_rebuild()
CreateGroup.model_rebuild()
CreateIteration.model_rebuild()
CreateLinkedFile.model_rebuild()
CreateMilestone.model_rebuild()
CreateObjective.model_rebuild()
CreateObjectiveHealth.model_rebuild()
CreateOrDeleteStoryReaction.model_rebuild()
CreateProject.model_rebuild()
CreateStoryLinkParams.model_rebuild()
CreateStoryCommentParams.model_rebuild()
CreateTaskParams.model_rebuild()
CreateStoryParams.model_rebuild()
CreateStories.model_rebuild()
CreateStoryComment.model_rebuild()
RemoveCustomFieldParams.model_rebuild()
RemoveLabelParams.model_rebuild()
CreateStoryFromTemplateParams.model_rebuild()
CreateStoryLink.model_rebuild()
CreateTask.model_rebuild()
CustomFieldEnumValue.model_rebuild()
CustomField.model_rebuild()
DataConflictError.model_rebuild()
DeleteStories.model_rebuild()
DisabledFeatureError.model_rebuild()
Doc.model_rebuild()
DocSlim.model_rebuild()
DocSearchResults.model_rebuild()
LabelSlim.model_rebuild()
LinkedFile.model_rebuild()
StoryContentsTask.model_rebuild()
UploadedFile.model_rebuild()
StoryContents.model_rebuild()
EntityTemplate.model_rebuild()
EpicAssociatedGroup.model_rebuild()
ThreadedComment.model_rebuild()
Health.model_rebuild()
EpicStats.model_rebuild()
Epic.model_rebuild()
EpicSlim.model_rebuild()
EpicPaginatedResults.model_rebuild()
EpicSearchResult.model_rebuild()
EpicSearchResults.model_rebuild()
EpicState.model_rebuild()
EpicWorkflow.model_rebuild()
GetDoc.model_rebuild()
Icon.model_rebuild()
Group.model_rebuild()
History.model_rebuild()
HistoryActionBranchCreate.model_rebuild()
HistoryActionBranchMerge.model_rebuild()
HistoryActionBranchPush.model_rebuild()
HistoryActionLabelCreate.model_rebuild()
HistoryActionLabelDelete.model_rebuild()
HistoryActionLabelUpdate.model_rebuild()
HistoryActionProjectUpdate.model_rebuild()
HistoryActionPullRequest.model_rebuild()
HistoryActionStoryCommentCreate.model_rebuild()
HistoryActionStoryCreate.model_rebuild()
HistoryActionStoryDelete.model_rebuild()
HistoryActionStoryLinkCreate.model_rebuild()
HistoryActionStoryLinkDelete.model_rebuild()
StoryHistoryChangeOldNewStr.model_rebuild()
StoryHistoryChangeOldNewInt.model_rebuild()
HistoryChangesStoryLink.model_rebuild()
HistoryActionStoryLinkUpdate.model_rebuild()
StoryHistoryChangeOldNewBool.model_rebuild()
StoryHistoryChangeAddsRemovesInt.model_rebuild()
StoryHistoryChangeAddsRemovesUuid.model_rebuild()
StoryHistoryChangeOldNewUuid.model_rebuild()
HistoryChangesStory.model_rebuild()
HistoryActionStoryUpdate.model_rebuild()
HistoryActionTaskCreate.model_rebuild()
HistoryActionTaskDelete.model_rebuild()
HistoryChangesTask.model_rebuild()
HistoryActionTaskUpdate.model_rebuild()
HistoryActionWorkspace2BulkUpdate.model_rebuild()
HistoryReferenceBranch.model_rebuild()
HistoryReferenceCommit.model_rebuild()
HistoryReferenceCustomFieldEnumValue.model_rebuild()
HistoryReferenceEpic.model_rebuild()
HistoryReferenceGeneral.model_rebuild()
HistoryReferenceGroup.model_rebuild()
HistoryReferenceIteration.model_rebuild()
HistoryReferenceLabel.model_rebuild()
HistoryReferenceProject.model_rebuild()
HistoryReferenceStory.model_rebuild()
HistoryReferenceStoryTask.model_rebuild()
HistoryReferenceWorkflowState.model_rebuild()
LabelStats.model_rebuild()
Label.model_rebuild()
IterationAssociatedGroup.model_rebuild()
IterationStats.model_rebuild()
Iteration.model_rebuild()
IterationSlim.model_rebuild()
IterationSearchResults.model_rebuild()
KeyResultValue.model_rebuild()
KeyResult.model_rebuild()
LinkSubTaskParams.model_rebuild()
MaxSearchResultsExceededError.model_rebuild()
Profile.model_rebuild()
Member.model_rebuild()
MemberInfoOrganization2.model_rebuild()
MemberInfo.model_rebuild()
MilestoneStats.model_rebuild()
Milestone.model_rebuild()
ObjectiveStats.model_rebuild()
Objective.model_rebuild()
ObjectiveSearchResult.model_rebuild()
ObjectiveSearchResults.model_rebuild()
ProjectStats.model_rebuild()
Project.model_rebuild()
Repository.model_rebuild()
TypedStoryLink.model_rebuild()
SyncedItem.model_rebuild()
StoryCustomField.model_rebuild()
StoryReaction.model_rebuild()
StoryComment.model_rebuild()
Task.model_rebuild()
StoryStats.model_rebuild()
StorySearchResult.model_rebuild()
StorySearchResults.model_rebuild()
SearchResults.model_rebuild()
SearchStories.model_rebuild()
Story.model_rebuild()
StoryLink.model_rebuild()
StorySlim.model_rebuild()
UnprocessableError.model_rebuild()
UnusableEntitlementError.model_rebuild()
UpdateCategory.model_rebuild()
UpdateComment.model_rebuild()
UpdateCustomFieldEnumValue.model_rebuild()
UpdateCustomField.model_rebuild()
UpdateDoc.model_rebuild()
UpdateStoryContents.model_rebuild()
UpdateEntityTemplate.model_rebuild()
UpdateEpic.model_rebuild()
UpdateFile.model_rebuild()
UpdateGroup.model_rebuild()
UpdateHealth.model_rebuild()
UpdateIteration.model_rebuild()
UpdateKeyResult.model_rebuild()
UpdateLabel.model_rebuild()
UpdateLinkedFile.model_rebuild()
UpdateMilestone.model_rebuild()
UpdateObjective.model_rebuild()
UpdateProject.model_rebuild()
UpdateStories.model_rebuild()
UpdateStory.model_rebuild()
UpdateStoryComment.model_rebuild()
UpdateStoryLink.model_rebuild()
UpdateTask.model_rebuild()
WorkflowState.model_rebuild()
Workflow.model_rebuild()
