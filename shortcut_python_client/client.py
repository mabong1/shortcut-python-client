"""Auto-generated Shortcut API client."""

from typing import Any

import httpx

from shortcut_python_client.models import (
    Category,
    CreateCategory,
    CreateCommentComment,
    CreateDoc,
    CreateEntityTemplate,
    CreateEpic,
    CreateEpicComment,
    CreateEpicHealth,
    CreateGenericIntegration,
    CreateGroup,
    CreateIteration,
    CreateLabelParams,
    CreateLinkedFile,
    CreateMilestone,
    CreateObjective,
    CreateObjectiveHealth,
    CreateProject,
    CreateStories,
    CreateStoryComment,
    CreateStoryFromTemplateParams,
    CreateStoryLink,
    CreateStoryParams,
    CreateTask,
    CustomField,
    DeleteStories,
    Doc,
    DocSearchResults,
    DocSlim,
    EntityTemplate,
    Epic,
    EpicPaginatedResults,
    EpicSearchResults,
    EpicSlim,
    EpicWorkflow,
    GetDoc,
    Group,
    Health,
    History,
    Iteration,
    IterationSearchResults,
    IterationSlim,
    KeyResult,
    Label,
    LinkedFile,
    Member,
    MemberInfo,
    Milestone,
    Objective,
    ObjectiveSearchResults,
    Project,
    Repository,
    SearchResults,
    SearchStories,
    Story,
    StoryComment,
    StoryLink,
    StoryReaction,
    StorySearchResults,
    StorySlim,
    Task,
    ThreadedComment,
    UpdateCategory,
    UpdateComment,
    UpdateCustomField,
    UpdateDoc,
    UpdateEntityTemplate,
    UpdateEpic,
    UpdateFile,
    UpdateGroup,
    UpdateHealth,
    UpdateIteration,
    UpdateKeyResult,
    UpdateLabel,
    UpdateLinkedFile,
    UpdateMilestone,
    UpdateObjective,
    UpdateProject,
    UpdateStories,
    UpdateStory,
    UpdateStoryComment,
    UpdateStoryLink,
    UpdateTask,
    UploadedFile,
    Workflow,
)

BASE_URL = "https://api.app.shortcut.com"


class ShortcutClient:
    """Python client for the Shortcut REST API v3."""

    def __init__(self, api_token: str, *, base_url: str = BASE_URL, timeout: float = 30.0) -> None:
        """Initialize the client.

        Args:
            api_token: Your Shortcut API token.
            base_url: API base URL (default: https://api.app.shortcut.com).
            timeout: Request timeout in seconds.
        """
        self._client = httpx.Client(
            base_url=base_url,
            headers={"Shortcut-Token": api_token, "Content-Type": "application/json"},
            timeout=timeout,
        )

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> "ShortcutClient":
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()

    def _request(
        self,
        method: str,
        path: str,
        *,
        json: Any = None,
        params: dict[str, Any] | None = None,
    ) -> httpx.Response:
        """Make an authenticated request to the Shortcut API."""
        response = self._client.request(method, path, json=json, params=params)
        response.raise_for_status()
        return response

    def list_categories(self) -> list[Category]:
        """List Categories"""
        path = "/api/v3/categories"
        response = self._request("GET", path)
        return [Category.model_validate(item) for item in response.json()]

    def create_category(self, data: CreateCategory) -> Category:
        """Create Category"""
        path = "/api/v3/categories"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return Category.model_validate(response.json())

    def get_category(self, category_public_id: int) -> Category:
        """Get Category"""
        path = f"/api/v3/categories/{category_public_id}"
        response = self._request("GET", path)
        return Category.model_validate(response.json())

    def update_category(self, category_public_id: int, data: UpdateCategory) -> Category:
        """Update Category"""
        path = f"/api/v3/categories/{category_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("PUT", path, json=json_data)
        return Category.model_validate(response.json())

    def delete_category(self, category_public_id: int) -> None:
        """Delete Category"""
        path = f"/api/v3/categories/{category_public_id}"
        self._request("DELETE", path)

    def list_category_milestones(self, category_public_id: int) -> list[Milestone]:
        """List Category Milestones"""
        path = f"/api/v3/categories/{category_public_id}/milestones"
        response = self._request("GET", path)
        return [Milestone.model_validate(item) for item in response.json()]

    def list_category_objectives(self, category_public_id: int) -> list[Milestone]:
        """List Category Objectives"""
        path = f"/api/v3/categories/{category_public_id}/objectives"
        response = self._request("GET", path)
        return [Milestone.model_validate(item) for item in response.json()]

    def list_custom_fields(self) -> list[CustomField]:
        """List Custom Fields"""
        path = "/api/v3/custom-fields"
        response = self._request("GET", path)
        return [CustomField.model_validate(item) for item in response.json()]

    def get_custom_field(self, custom_field_public_id: str) -> CustomField:
        """Get Custom Field"""
        path = f"/api/v3/custom-fields/{custom_field_public_id}"
        response = self._request("GET", path)
        return CustomField.model_validate(response.json())

    def update_custom_field(self, custom_field_public_id: str, data: UpdateCustomField) -> CustomField:
        """Update Custom Field"""
        path = f"/api/v3/custom-fields/{custom_field_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("PUT", path, json=json_data)
        return CustomField.model_validate(response.json())

    def delete_custom_field(self, custom_field_public_id: str) -> None:
        """Delete Custom Field"""
        path = f"/api/v3/custom-fields/{custom_field_public_id}"
        self._request("DELETE", path)

    def list_docs(self) -> list[DocSlim]:
        """List Docs"""
        path = "/api/v3/documents"
        response = self._request("GET", path)
        return [DocSlim.model_validate(item) for item in response.json()]

    def create_doc(self, data: CreateDoc) -> DocSlim:
        """Create Doc"""
        path = "/api/v3/documents"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return DocSlim.model_validate(response.json())

    def get_doc(self, doc_public_id: str, *, content_format: str | None = None) -> Doc:
        """Get Doc"""
        path = f"/api/v3/documents/{doc_public_id}"
        params: dict[str, Any] = {}
        if content_format is not None:
            params["content_format"] = content_format
        response = self._request("GET", path, params=params)
        return Doc.model_validate(response.json())

    def update_doc(self, doc_public_id: str, data: UpdateDoc) -> Doc:
        """Update Doc"""
        path = f"/api/v3/documents/{doc_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("PUT", path, json=json_data)
        return Doc.model_validate(response.json())

    def delete_doc(self, doc_public_id: str, data: GetDoc) -> None:
        """Delete Doc"""
        path = f"/api/v3/documents/{doc_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        self._request("DELETE", path, json=json_data)

    def list_document_epics(self, doc_public_id: str) -> list[EpicSlim]:
        """List Document Epics"""
        path = f"/api/v3/documents/{doc_public_id}/epics"
        response = self._request("GET", path)
        return [EpicSlim.model_validate(item) for item in response.json()]

    def link_document_to_epic(self, doc_public_id: str, epic_public_id: int) -> None:
        """Link Document to Epic"""
        path = f"/api/v3/documents/{doc_public_id}/epics/{epic_public_id}"
        self._request("PUT", path)

    def unlink_document_from_epic(self, doc_public_id: str, epic_public_id: int) -> None:
        """Unlink Document from Epic"""
        path = f"/api/v3/documents/{doc_public_id}/epics/{epic_public_id}"
        self._request("DELETE", path)

    def list_entity_templates(self) -> list[EntityTemplate]:
        """List Entity Templates"""
        path = "/api/v3/entity-templates"
        response = self._request("GET", path)
        return [EntityTemplate.model_validate(item) for item in response.json()]

    def create_entity_template(self, data: CreateEntityTemplate) -> EntityTemplate:
        """Create Entity Template"""
        path = "/api/v3/entity-templates"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return EntityTemplate.model_validate(response.json())

    def disable_story_templates(self) -> None:
        """Disable Story Templates"""
        path = "/api/v3/entity-templates/disable"
        self._request("PUT", path)

    def enable_story_templates(self) -> None:
        """Enable Story Templates"""
        path = "/api/v3/entity-templates/enable"
        self._request("PUT", path)

    def get_entity_template(self, entity_template_public_id: str) -> EntityTemplate:
        """Get Entity Template"""
        path = f"/api/v3/entity-templates/{entity_template_public_id}"
        response = self._request("GET", path)
        return EntityTemplate.model_validate(response.json())

    def update_entity_template(self, entity_template_public_id: str, data: UpdateEntityTemplate) -> EntityTemplate:
        """Update Entity Template"""
        path = f"/api/v3/entity-templates/{entity_template_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("PUT", path, json=json_data)
        return EntityTemplate.model_validate(response.json())

    def delete_entity_template(self, entity_template_public_id: str) -> None:
        """Delete Entity Template"""
        path = f"/api/v3/entity-templates/{entity_template_public_id}"
        self._request("DELETE", path)

    def get_epic_workflow(self) -> EpicWorkflow:
        """Get Epic Workflow"""
        path = "/api/v3/epic-workflow"
        response = self._request("GET", path)
        return EpicWorkflow.model_validate(response.json())

    def list_epics(self, *, includes_description: bool | None = None) -> list[EpicSlim]:
        """List Epics"""
        path = "/api/v3/epics"
        params: dict[str, Any] = {}
        if includes_description is not None:
            params["includes_description"] = includes_description
        response = self._request("GET", path, params=params)
        return [EpicSlim.model_validate(item) for item in response.json()]

    def create_epic(self, data: CreateEpic) -> Epic:
        """Create Epic"""
        path = "/api/v3/epics"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return Epic.model_validate(response.json())

    def list_epics_paginated(
        self,
        *,
        includes_description: bool | None = None,
        page: int | None = None,
        page_size: int | None = None,
    ) -> EpicPaginatedResults:
        """List Epics Paginated"""
        path = "/api/v3/epics/paginated"
        params: dict[str, Any] = {}
        if includes_description is not None:
            params["includes_description"] = includes_description
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["page_size"] = page_size
        response = self._request("GET", path, params=params)
        return EpicPaginatedResults.model_validate(response.json())

    def get_epic(self, epic_public_id: int) -> Epic:
        """Get Epic"""
        path = f"/api/v3/epics/{epic_public_id}"
        response = self._request("GET", path)
        return Epic.model_validate(response.json())

    def update_epic(self, epic_public_id: int, data: UpdateEpic) -> Epic:
        """Update Epic"""
        path = f"/api/v3/epics/{epic_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("PUT", path, json=json_data)
        return Epic.model_validate(response.json())

    def delete_epic(self, epic_public_id: int) -> None:
        """Delete Epic"""
        path = f"/api/v3/epics/{epic_public_id}"
        self._request("DELETE", path)

    def list_epic_comments(self, epic_public_id: int) -> list[ThreadedComment]:
        """List Epic Comments"""
        path = f"/api/v3/epics/{epic_public_id}/comments"
        response = self._request("GET", path)
        return [ThreadedComment.model_validate(item) for item in response.json()]

    def create_epic_comment(self, epic_public_id: int, data: CreateEpicComment) -> ThreadedComment:
        """Create Epic Comment"""
        path = f"/api/v3/epics/{epic_public_id}/comments"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return ThreadedComment.model_validate(response.json())

    def create_epic_comment_comment(
        self,
        epic_public_id: int,
        comment_public_id: int,
        data: CreateCommentComment,
    ) -> ThreadedComment:
        """Create Epic Comment Comment"""
        path = f"/api/v3/epics/{epic_public_id}/comments/{comment_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return ThreadedComment.model_validate(response.json())

    def get_epic_comment(self, epic_public_id: int, comment_public_id: int) -> ThreadedComment:
        """Get Epic Comment"""
        path = f"/api/v3/epics/{epic_public_id}/comments/{comment_public_id}"
        response = self._request("GET", path)
        return ThreadedComment.model_validate(response.json())

    def update_epic_comment(self, epic_public_id: int, comment_public_id: int, data: UpdateComment) -> ThreadedComment:
        """Update Epic Comment"""
        path = f"/api/v3/epics/{epic_public_id}/comments/{comment_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("PUT", path, json=json_data)
        return ThreadedComment.model_validate(response.json())

    def delete_epic_comment(self, epic_public_id: int, comment_public_id: int) -> None:
        """Delete Epic Comment"""
        path = f"/api/v3/epics/{epic_public_id}/comments/{comment_public_id}"
        self._request("DELETE", path)

    def list_epic_documents(self, epic_public_id: int) -> list[DocSlim]:
        """List Epic Documents"""
        path = f"/api/v3/epics/{epic_public_id}/documents"
        response = self._request("GET", path)
        return [DocSlim.model_validate(item) for item in response.json()]

    def get_epic_health(self, epic_public_id: int) -> Health:
        """Get Epic Health"""
        path = f"/api/v3/epics/{epic_public_id}/health"
        response = self._request("GET", path)
        return Health.model_validate(response.json())

    def create_epic_health(self, epic_public_id: int, data: CreateEpicHealth) -> Health:
        """Create Epic Health"""
        path = f"/api/v3/epics/{epic_public_id}/health"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return Health.model_validate(response.json())

    def list_epic_healths(self, epic_public_id: int) -> list[Health]:
        """List Epic Healths"""
        path = f"/api/v3/epics/{epic_public_id}/health-history"
        response = self._request("GET", path)
        return [Health.model_validate(item) for item in response.json()]

    def list_epic_stories(self, epic_public_id: int, *, includes_description: bool | None = None) -> list[StorySlim]:
        """List Epic Stories"""
        path = f"/api/v3/epics/{epic_public_id}/stories"
        params: dict[str, Any] = {}
        if includes_description is not None:
            params["includes_description"] = includes_description
        response = self._request("GET", path, params=params)
        return [StorySlim.model_validate(item) for item in response.json()]

    def get_external_link_stories(self, *, external_link: str) -> list[StorySlim]:
        """Get External Link Stories"""
        path = "/api/v3/external-link/stories"
        params: dict[str, Any] = {}
        if external_link is not None:
            params["external_link"] = external_link
        response = self._request("GET", path, params=params)
        return [StorySlim.model_validate(item) for item in response.json()]

    def list_files(self) -> list[UploadedFile]:
        """List Files"""
        path = "/api/v3/files"
        response = self._request("GET", path)
        return [UploadedFile.model_validate(item) for item in response.json()]

    def upload_files(self) -> list[UploadedFile]:
        """Upload Files"""
        path = "/api/v3/files"
        response = self._request("POST", path)
        return [UploadedFile.model_validate(item) for item in response.json()]

    def get_file(self, file_public_id: int) -> UploadedFile:
        """Get File"""
        path = f"/api/v3/files/{file_public_id}"
        response = self._request("GET", path)
        return UploadedFile.model_validate(response.json())

    def update_file(self, file_public_id: int, data: UpdateFile) -> UploadedFile:
        """Update File"""
        path = f"/api/v3/files/{file_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("PUT", path, json=json_data)
        return UploadedFile.model_validate(response.json())

    def delete_file(self, file_public_id: int) -> None:
        """Delete File"""
        path = f"/api/v3/files/{file_public_id}"
        self._request("DELETE", path)

    def list_groups(self, *, archived: bool | None = None) -> list[Group]:
        """List Groups"""
        path = "/api/v3/groups"
        params: dict[str, Any] = {}
        if archived is not None:
            params["archived"] = archived
        response = self._request("GET", path, params=params)
        return [Group.model_validate(item) for item in response.json()]

    def create_group(self, data: CreateGroup) -> Group:
        """Create Group"""
        path = "/api/v3/groups"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return Group.model_validate(response.json())

    def get_group(self, group_public_id: str) -> Group:
        """Get Group"""
        path = f"/api/v3/groups/{group_public_id}"
        response = self._request("GET", path)
        return Group.model_validate(response.json())

    def update_group(self, group_public_id: str, data: UpdateGroup) -> Group:
        """Update Group"""
        path = f"/api/v3/groups/{group_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("PUT", path, json=json_data)
        return Group.model_validate(response.json())

    def list_group_stories(
        self,
        group_public_id: str,
        *,
        limit: int | None = None,
        offset: int | None = None,
    ) -> list[StorySlim]:
        """List Group Stories"""
        path = f"/api/v3/groups/{group_public_id}/stories"
        params: dict[str, Any] = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        response = self._request("GET", path, params=params)
        return [StorySlim.model_validate(item) for item in response.json()]

    def update_health(self, health_public_id: str, data: UpdateHealth) -> Health:
        """Update Health"""
        path = f"/api/v3/health/{health_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("PUT", path, json=json_data)
        return Health.model_validate(response.json())

    def create_generic_integration(self, data: CreateGenericIntegration) -> None:
        """Create Generic Integration"""
        path = "/api/v3/integrations/webhook"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        self._request("POST", path, json=json_data)

    def get_generic_integration(self, integration_public_id: int) -> None:
        """Get Generic Integration"""
        path = f"/api/v3/integrations/webhook/{integration_public_id}"
        self._request("GET", path)

    def delete_generic_integration(self, integration_public_id: int) -> None:
        """Delete Generic Integration"""
        path = f"/api/v3/integrations/webhook/{integration_public_id}"
        self._request("DELETE", path)

    def list_iterations(self) -> list[IterationSlim]:
        """List Iterations"""
        path = "/api/v3/iterations"
        response = self._request("GET", path)
        return [IterationSlim.model_validate(item) for item in response.json()]

    def create_iteration(self, data: CreateIteration) -> Iteration:
        """Create Iteration"""
        path = "/api/v3/iterations"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return Iteration.model_validate(response.json())

    def disable_iterations(self) -> None:
        """Disable Iterations"""
        path = "/api/v3/iterations/disable"
        self._request("PUT", path)

    def enable_iterations(self) -> None:
        """Enable Iterations"""
        path = "/api/v3/iterations/enable"
        self._request("PUT", path)

    def get_iteration(self, iteration_public_id: int) -> Iteration:
        """Get Iteration"""
        path = f"/api/v3/iterations/{iteration_public_id}"
        response = self._request("GET", path)
        return Iteration.model_validate(response.json())

    def update_iteration(self, iteration_public_id: int, data: UpdateIteration) -> Iteration:
        """Update Iteration"""
        path = f"/api/v3/iterations/{iteration_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("PUT", path, json=json_data)
        return Iteration.model_validate(response.json())

    def delete_iteration(self, iteration_public_id: int) -> None:
        """Delete Iteration"""
        path = f"/api/v3/iterations/{iteration_public_id}"
        self._request("DELETE", path)

    def list_iteration_stories(
        self,
        iteration_public_id: int,
        *,
        includes_description: bool | None = None,
    ) -> list[StorySlim]:
        """List Iteration Stories"""
        path = f"/api/v3/iterations/{iteration_public_id}/stories"
        params: dict[str, Any] = {}
        if includes_description is not None:
            params["includes_description"] = includes_description
        response = self._request("GET", path, params=params)
        return [StorySlim.model_validate(item) for item in response.json()]

    def get_key_result(self, key_result_public_id: str) -> KeyResult:
        """Get Key Result"""
        path = f"/api/v3/key-results/{key_result_public_id}"
        response = self._request("GET", path)
        return KeyResult.model_validate(response.json())

    def update_key_result(self, key_result_public_id: str, data: UpdateKeyResult) -> KeyResult:
        """Update Key Result"""
        path = f"/api/v3/key-results/{key_result_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("PUT", path, json=json_data)
        return KeyResult.model_validate(response.json())

    def list_labels(self, *, slim: bool | None = None) -> list[Label]:
        """List Labels"""
        path = "/api/v3/labels"
        params: dict[str, Any] = {}
        if slim is not None:
            params["slim"] = slim
        response = self._request("GET", path, params=params)
        return [Label.model_validate(item) for item in response.json()]

    def create_label(self, data: CreateLabelParams) -> Label:
        """Create Label"""
        path = "/api/v3/labels"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return Label.model_validate(response.json())

    def get_label(self, label_public_id: int) -> Label:
        """Get Label"""
        path = f"/api/v3/labels/{label_public_id}"
        response = self._request("GET", path)
        return Label.model_validate(response.json())

    def update_label(self, label_public_id: int, data: UpdateLabel) -> Label:
        """Update Label"""
        path = f"/api/v3/labels/{label_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("PUT", path, json=json_data)
        return Label.model_validate(response.json())

    def delete_label(self, label_public_id: int) -> None:
        """Delete Label"""
        path = f"/api/v3/labels/{label_public_id}"
        self._request("DELETE", path)

    def list_label_epics(self, label_public_id: int) -> list[EpicSlim]:
        """List Label Epics"""
        path = f"/api/v3/labels/{label_public_id}/epics"
        response = self._request("GET", path)
        return [EpicSlim.model_validate(item) for item in response.json()]

    def list_label_stories(self, label_public_id: int, *, includes_description: bool | None = None) -> list[StorySlim]:
        """List Label Stories"""
        path = f"/api/v3/labels/{label_public_id}/stories"
        params: dict[str, Any] = {}
        if includes_description is not None:
            params["includes_description"] = includes_description
        response = self._request("GET", path, params=params)
        return [StorySlim.model_validate(item) for item in response.json()]

    def list_linked_files(self) -> list[LinkedFile]:
        """List Linked Files"""
        path = "/api/v3/linked-files"
        response = self._request("GET", path)
        return [LinkedFile.model_validate(item) for item in response.json()]

    def create_linked_file(self, data: CreateLinkedFile) -> LinkedFile:
        """Create Linked File"""
        path = "/api/v3/linked-files"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return LinkedFile.model_validate(response.json())

    def get_linked_file(self, linked_file_public_id: int) -> LinkedFile:
        """Get Linked File"""
        path = f"/api/v3/linked-files/{linked_file_public_id}"
        response = self._request("GET", path)
        return LinkedFile.model_validate(response.json())

    def update_linked_file(self, linked_file_public_id: int, data: UpdateLinkedFile) -> LinkedFile:
        """Update Linked File"""
        path = f"/api/v3/linked-files/{linked_file_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("PUT", path, json=json_data)
        return LinkedFile.model_validate(response.json())

    def delete_linked_file(self, linked_file_public_id: int) -> None:
        """Delete Linked File"""
        path = f"/api/v3/linked-files/{linked_file_public_id}"
        self._request("DELETE", path)

    def get_current_member_info(self) -> MemberInfo:
        """Get Current Member Info"""
        path = "/api/v3/member"
        response = self._request("GET", path)
        return MemberInfo.model_validate(response.json())

    def list_members(self, *, org_public_id: str | None = None, disabled: bool | None = None) -> list[Member]:
        """List Members"""
        path = "/api/v3/members"
        params: dict[str, Any] = {}
        if org_public_id is not None:
            params["org-public-id"] = org_public_id
        if disabled is not None:
            params["disabled"] = disabled
        response = self._request("GET", path, params=params)
        return [Member.model_validate(item) for item in response.json()]

    def get_member(self, member_public_id: str, *, org_public_id: str | None = None) -> Member:
        """Get Member"""
        path = f"/api/v3/members/{member_public_id}"
        params: dict[str, Any] = {}
        if org_public_id is not None:
            params["org-public-id"] = org_public_id
        response = self._request("GET", path, params=params)
        return Member.model_validate(response.json())

    def list_milestones(self) -> list[Milestone]:
        """List Milestones"""
        path = "/api/v3/milestones"
        response = self._request("GET", path)
        return [Milestone.model_validate(item) for item in response.json()]

    def create_milestone(self, data: CreateMilestone) -> Milestone:
        """Create Milestone"""
        path = "/api/v3/milestones"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return Milestone.model_validate(response.json())

    def get_milestone(self, milestone_public_id: int) -> Milestone:
        """Get Milestone"""
        path = f"/api/v3/milestones/{milestone_public_id}"
        response = self._request("GET", path)
        return Milestone.model_validate(response.json())

    def update_milestone(self, milestone_public_id: int, data: UpdateMilestone) -> Milestone:
        """Update Milestone"""
        path = f"/api/v3/milestones/{milestone_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("PUT", path, json=json_data)
        return Milestone.model_validate(response.json())

    def delete_milestone(self, milestone_public_id: int) -> None:
        """Delete Milestone"""
        path = f"/api/v3/milestones/{milestone_public_id}"
        self._request("DELETE", path)

    def list_milestone_epics(self, milestone_public_id: int) -> list[EpicSlim]:
        """List Milestone Epics"""
        path = f"/api/v3/milestones/{milestone_public_id}/epics"
        response = self._request("GET", path)
        return [EpicSlim.model_validate(item) for item in response.json()]

    def list_objectives(self) -> list[Objective]:
        """List Objectives"""
        path = "/api/v3/objectives"
        response = self._request("GET", path)
        return [Objective.model_validate(item) for item in response.json()]

    def create_objective(self, data: CreateObjective) -> Objective:
        """Create Objective"""
        path = "/api/v3/objectives"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return Objective.model_validate(response.json())

    def get_objective(self, objective_public_id: int) -> Objective:
        """Get Objective"""
        path = f"/api/v3/objectives/{objective_public_id}"
        response = self._request("GET", path)
        return Objective.model_validate(response.json())

    def update_objective(self, objective_public_id: int, data: UpdateObjective) -> Objective:
        """Update Objective"""
        path = f"/api/v3/objectives/{objective_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("PUT", path, json=json_data)
        return Objective.model_validate(response.json())

    def delete_objective(self, objective_public_id: int) -> None:
        """Delete Objective"""
        path = f"/api/v3/objectives/{objective_public_id}"
        self._request("DELETE", path)

    def list_objective_epics(self, objective_public_id: int) -> list[EpicSlim]:
        """List Objective Epics"""
        path = f"/api/v3/objectives/{objective_public_id}/epics"
        response = self._request("GET", path)
        return [EpicSlim.model_validate(item) for item in response.json()]

    def get_objective_health(self, objective_public_id: int) -> Health:
        """Get Objective Health"""
        path = f"/api/v3/objectives/{objective_public_id}/health"
        response = self._request("GET", path)
        return Health.model_validate(response.json())

    def create_objective_health(self, objective_public_id: int, data: CreateObjectiveHealth) -> Health:
        """Create Objective Health"""
        path = f"/api/v3/objectives/{objective_public_id}/health"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return Health.model_validate(response.json())

    def list_objective_healths(self, objective_public_id: int) -> list[Health]:
        """List Objective Healths"""
        path = f"/api/v3/objectives/{objective_public_id}/health-history"
        response = self._request("GET", path)
        return [Health.model_validate(item) for item in response.json()]

    def list_projects(self) -> list[Project]:
        """List Projects"""
        path = "/api/v3/projects"
        response = self._request("GET", path)
        return [Project.model_validate(item) for item in response.json()]

    def create_project(self, data: CreateProject) -> Project:
        """Create Project"""
        path = "/api/v3/projects"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return Project.model_validate(response.json())

    def get_project(self, project_public_id: int) -> Project:
        """Get Project"""
        path = f"/api/v3/projects/{project_public_id}"
        response = self._request("GET", path)
        return Project.model_validate(response.json())

    def update_project(self, project_public_id: int, data: UpdateProject) -> Project:
        """Update Project"""
        path = f"/api/v3/projects/{project_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("PUT", path, json=json_data)
        return Project.model_validate(response.json())

    def delete_project(self, project_public_id: int) -> None:
        """Delete Project"""
        path = f"/api/v3/projects/{project_public_id}"
        self._request("DELETE", path)

    def list_stories(self, project_public_id: int, *, includes_description: bool | None = None) -> list[StorySlim]:
        """List Stories"""
        path = f"/api/v3/projects/{project_public_id}/stories"
        params: dict[str, Any] = {}
        if includes_description is not None:
            params["includes_description"] = includes_description
        response = self._request("GET", path, params=params)
        return [StorySlim.model_validate(item) for item in response.json()]

    def list_repositories(self) -> list[Repository]:
        """List Repositories"""
        path = "/api/v3/repositories"
        response = self._request("GET", path)
        return [Repository.model_validate(item) for item in response.json()]

    def get_repository(self, repo_public_id: int) -> Repository:
        """Get Repository"""
        path = f"/api/v3/repositories/{repo_public_id}"
        response = self._request("GET", path)
        return Repository.model_validate(response.json())

    def search(
        self,
        *,
        query: str,
        page_size: int | None = None,
        detail: str | None = None,
        next: str | None = None,
        entity_types: list[str] | None = None,
    ) -> SearchResults:
        """Search"""
        path = "/api/v3/search"
        params: dict[str, Any] = {}
        if query is not None:
            params["query"] = query
        if page_size is not None:
            params["page_size"] = page_size
        if detail is not None:
            params["detail"] = detail
        if next is not None:
            params["next"] = next
        if entity_types is not None:
            params["entity_types"] = entity_types
        response = self._request("GET", path, params=params)
        return SearchResults.model_validate(response.json())

    def search_documents(
        self,
        *,
        title: str,
        archived: bool | None = None,
        created_by_me: bool | None = None,
        followed_by_me: bool | None = None,
        page_size: int | None = None,
        next: str | None = None,
    ) -> DocSearchResults:
        """Search Documents"""
        path = "/api/v3/search/documents"
        params: dict[str, Any] = {}
        if title is not None:
            params["title"] = title
        if archived is not None:
            params["archived"] = archived
        if created_by_me is not None:
            params["created_by_me"] = created_by_me
        if followed_by_me is not None:
            params["followed_by_me"] = followed_by_me
        if page_size is not None:
            params["page_size"] = page_size
        if next is not None:
            params["next"] = next
        response = self._request("GET", path, params=params)
        return DocSearchResults.model_validate(response.json())

    def search_epics(
        self,
        *,
        query: str,
        page_size: int | None = None,
        detail: str | None = None,
        next: str | None = None,
        entity_types: list[str] | None = None,
    ) -> EpicSearchResults:
        """Search Epics"""
        path = "/api/v3/search/epics"
        params: dict[str, Any] = {}
        if query is not None:
            params["query"] = query
        if page_size is not None:
            params["page_size"] = page_size
        if detail is not None:
            params["detail"] = detail
        if next is not None:
            params["next"] = next
        if entity_types is not None:
            params["entity_types"] = entity_types
        response = self._request("GET", path, params=params)
        return EpicSearchResults.model_validate(response.json())

    def search_iterations(
        self,
        *,
        query: str,
        page_size: int | None = None,
        detail: str | None = None,
        next: str | None = None,
        entity_types: list[str] | None = None,
    ) -> IterationSearchResults:
        """Search Iterations"""
        path = "/api/v3/search/iterations"
        params: dict[str, Any] = {}
        if query is not None:
            params["query"] = query
        if page_size is not None:
            params["page_size"] = page_size
        if detail is not None:
            params["detail"] = detail
        if next is not None:
            params["next"] = next
        if entity_types is not None:
            params["entity_types"] = entity_types
        response = self._request("GET", path, params=params)
        return IterationSearchResults.model_validate(response.json())

    def search_milestones(
        self,
        *,
        query: str,
        page_size: int | None = None,
        detail: str | None = None,
        next: str | None = None,
        entity_types: list[str] | None = None,
    ) -> ObjectiveSearchResults:
        """Search Milestones"""
        path = "/api/v3/search/milestones"
        params: dict[str, Any] = {}
        if query is not None:
            params["query"] = query
        if page_size is not None:
            params["page_size"] = page_size
        if detail is not None:
            params["detail"] = detail
        if next is not None:
            params["next"] = next
        if entity_types is not None:
            params["entity_types"] = entity_types
        response = self._request("GET", path, params=params)
        return ObjectiveSearchResults.model_validate(response.json())

    def search_objectives(
        self,
        *,
        query: str,
        page_size: int | None = None,
        detail: str | None = None,
        next: str | None = None,
        entity_types: list[str] | None = None,
    ) -> ObjectiveSearchResults:
        """Search Objectives"""
        path = "/api/v3/search/objectives"
        params: dict[str, Any] = {}
        if query is not None:
            params["query"] = query
        if page_size is not None:
            params["page_size"] = page_size
        if detail is not None:
            params["detail"] = detail
        if next is not None:
            params["next"] = next
        if entity_types is not None:
            params["entity_types"] = entity_types
        response = self._request("GET", path, params=params)
        return ObjectiveSearchResults.model_validate(response.json())

    def search_stories(
        self,
        *,
        query: str,
        page_size: int | None = None,
        detail: str | None = None,
        next: str | None = None,
        entity_types: list[str] | None = None,
    ) -> StorySearchResults:
        """Search Stories"""
        path = "/api/v3/search/stories"
        params: dict[str, Any] = {}
        if query is not None:
            params["query"] = query
        if page_size is not None:
            params["page_size"] = page_size
        if detail is not None:
            params["detail"] = detail
        if next is not None:
            params["next"] = next
        if entity_types is not None:
            params["entity_types"] = entity_types
        response = self._request("GET", path, params=params)
        return StorySearchResults.model_validate(response.json())

    def create_story(self, data: CreateStoryParams) -> Story:
        """Create Story"""
        path = "/api/v3/stories"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return Story.model_validate(response.json())

    def create_multiple_stories(self, data: CreateStories) -> list[StorySlim]:
        """Create Multiple Stories"""
        path = "/api/v3/stories/bulk"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return [StorySlim.model_validate(item) for item in response.json()]

    def update_multiple_stories(self, data: UpdateStories) -> list[StorySlim]:
        """Update Multiple Stories"""
        path = "/api/v3/stories/bulk"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("PUT", path, json=json_data)
        return [StorySlim.model_validate(item) for item in response.json()]

    def delete_multiple_stories(self, data: DeleteStories) -> None:
        """Delete Multiple Stories"""
        path = "/api/v3/stories/bulk"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        self._request("DELETE", path, json=json_data)

    def create_story_from_template(self, data: CreateStoryFromTemplateParams) -> Story:
        """Create Story From Template"""
        path = "/api/v3/stories/from-template"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return Story.model_validate(response.json())

    def query_stories(self, data: SearchStories) -> list[StorySlim]:
        """Query Stories"""
        path = "/api/v3/stories/search"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return [StorySlim.model_validate(item) for item in response.json()]

    def get_story(self, story_public_id: int) -> Story:
        """Get Story"""
        path = f"/api/v3/stories/{story_public_id}"
        response = self._request("GET", path)
        return Story.model_validate(response.json())

    def update_story(self, story_public_id: int, data: UpdateStory) -> Story:
        """Update Story"""
        path = f"/api/v3/stories/{story_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("PUT", path, json=json_data)
        return Story.model_validate(response.json())

    def delete_story(self, story_public_id: int) -> None:
        """Delete Story"""
        path = f"/api/v3/stories/{story_public_id}"
        self._request("DELETE", path)

    def list_story_comment(self, story_public_id: int) -> list[StoryComment]:
        """List Story Comment"""
        path = f"/api/v3/stories/{story_public_id}/comments"
        response = self._request("GET", path)
        return [StoryComment.model_validate(item) for item in response.json()]

    def create_story_comment(self, story_public_id: int, data: CreateStoryComment) -> StoryComment:
        """Create Story Comment"""
        path = f"/api/v3/stories/{story_public_id}/comments"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return StoryComment.model_validate(response.json())

    def get_story_comment(self, story_public_id: int, comment_public_id: int) -> StoryComment:
        """Get Story Comment"""
        path = f"/api/v3/stories/{story_public_id}/comments/{comment_public_id}"
        response = self._request("GET", path)
        return StoryComment.model_validate(response.json())

    def update_story_comment(
        self,
        story_public_id: int,
        comment_public_id: int,
        data: UpdateStoryComment,
    ) -> StoryComment:
        """Update Story Comment"""
        path = f"/api/v3/stories/{story_public_id}/comments/{comment_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("PUT", path, json=json_data)
        return StoryComment.model_validate(response.json())

    def delete_story_comment(self, story_public_id: int, comment_public_id: int) -> None:
        """Delete Story Comment"""
        path = f"/api/v3/stories/{story_public_id}/comments/{comment_public_id}"
        self._request("DELETE", path)

    def create_story_reaction(self, story_public_id: int, comment_public_id: int) -> list[StoryReaction]:
        """Create Story Reaction"""
        path = f"/api/v3/stories/{story_public_id}/comments/{comment_public_id}/reactions"
        response = self._request("POST", path)
        return [StoryReaction.model_validate(item) for item in response.json()]

    def delete_story_reaction(self, story_public_id: int, comment_public_id: int) -> None:
        """Delete Story Reaction"""
        path = f"/api/v3/stories/{story_public_id}/comments/{comment_public_id}/reactions"
        self._request("DELETE", path)

    def unlink_comment_thread_from_slack(self, story_public_id: int, comment_public_id: int) -> StoryComment:
        """Unlink Comment thread from Slack"""
        path = f"/api/v3/stories/{story_public_id}/comments/{comment_public_id}/unlink-from-slack"
        response = self._request("POST", path)
        return StoryComment.model_validate(response.json())

    def story_history(self, story_public_id: int) -> list[History]:
        """Story History"""
        path = f"/api/v3/stories/{story_public_id}/history"
        response = self._request("GET", path)
        return [History.model_validate(item) for item in response.json()]

    def list_story_sub_tasks(self, story_public_id: int) -> list[StorySlim]:
        """List Story Sub tasks"""
        path = f"/api/v3/stories/{story_public_id}/sub-tasks"
        response = self._request("GET", path)
        return [StorySlim.model_validate(item) for item in response.json()]

    def create_task(self, story_public_id: int, data: CreateTask) -> Task:
        """Create Task"""
        path = f"/api/v3/stories/{story_public_id}/tasks"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return Task.model_validate(response.json())

    def get_task(self, story_public_id: int, task_public_id: int) -> Task:
        """Get Task"""
        path = f"/api/v3/stories/{story_public_id}/tasks/{task_public_id}"
        response = self._request("GET", path)
        return Task.model_validate(response.json())

    def update_task(self, story_public_id: int, task_public_id: int, data: UpdateTask) -> Task:
        """Update Task"""
        path = f"/api/v3/stories/{story_public_id}/tasks/{task_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("PUT", path, json=json_data)
        return Task.model_validate(response.json())

    def delete_task(self, story_public_id: int, task_public_id: int) -> None:
        """Delete Task"""
        path = f"/api/v3/stories/{story_public_id}/tasks/{task_public_id}"
        self._request("DELETE", path)

    def create_story_link(self, data: CreateStoryLink) -> StoryLink:
        """Create Story Link"""
        path = "/api/v3/story-links"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("POST", path, json=json_data)
        return StoryLink.model_validate(response.json())

    def get_story_link(self, story_link_public_id: int) -> StoryLink:
        """Get Story Link"""
        path = f"/api/v3/story-links/{story_link_public_id}"
        response = self._request("GET", path)
        return StoryLink.model_validate(response.json())

    def update_story_link(self, story_link_public_id: int, data: UpdateStoryLink) -> StoryLink:
        """Update Story Link"""
        path = f"/api/v3/story-links/{story_link_public_id}"
        json_data = data.model_dump(mode="json", by_alias=True, exclude_none=True) if data is not None else None
        response = self._request("PUT", path, json=json_data)
        return StoryLink.model_validate(response.json())

    def delete_story_link(self, story_link_public_id: int) -> None:
        """Delete Story Link"""
        path = f"/api/v3/story-links/{story_link_public_id}"
        self._request("DELETE", path)

    def list_workflows(self) -> list[Workflow]:
        """List Workflows"""
        path = "/api/v3/workflows"
        response = self._request("GET", path)
        return [Workflow.model_validate(item) for item in response.json()]

    def get_workflow(self, workflow_public_id: int) -> Workflow:
        """Get Workflow"""
        path = f"/api/v3/workflows/{workflow_public_id}"
        response = self._request("GET", path)
        return Workflow.model_validate(response.json())
