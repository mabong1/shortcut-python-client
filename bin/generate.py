#!/usr/bin/env python3
"""Generate Python client code from Shortcut OpenAPI spec.

Reads shortcut.openapi.json and produces:
- shortcut_python_client/models.py  (Pydantic models for all schemas)
- shortcut_python_client/client.py  (ShortcutClient with typed methods for all endpoints)
"""

import json
import keyword
import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC_PATH = ROOT / "shortcut.openapi.json"
OUTPUT_DIR = ROOT / "shortcut_python_client"


def load_spec() -> dict:
    with open(SPEC_PATH) as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# Naming helpers
# ---------------------------------------------------------------------------


def camel_to_snake(name: str) -> str:
    """Convert camelCase or PascalCase to snake_case."""
    s1 = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def param_name_to_python(name: str) -> str:
    """Convert OpenAPI param names like 'category-public-id' to 'category_public_id'."""
    n = name.replace("-", "_")
    if keyword.iskeyword(n):
        n = n + "_"
    return n


def safe_field_name(name: str) -> str:
    """Make a field name safe for Python."""
    n = name.replace("-", "_")
    if keyword.iskeyword(n):
        n = n + "_"
    return n


# ---------------------------------------------------------------------------
# Type mapping
# ---------------------------------------------------------------------------


def resolve_ref(ref: str) -> str:
    """Extract schema name from $ref string."""
    return ref.split("/")[-1]


def schema_to_type(schema: dict, for_field: bool = True, simple: bool = False, current_model: str | None = None) -> str:
    """Convert an OpenAPI schema to a Python type annotation string.

    Args:
        schema: OpenAPI schema dict.
        for_field: Whether this is for a model field (affects nullable handling).
        simple: If True, use simple types (str instead of Literal) for method signatures.
        current_model: The model currently being generated (to detect self-references).
    """
    if "$ref" in schema:
        ref_name = resolve_ref(schema["$ref"])
        # Quote self-references to avoid NameError at class definition time
        if ref_name == current_model:
            return f'"{ref_name}"'
        return ref_name

    typ = schema.get("type", "object")
    fmt = schema.get("format", "")
    nullable = schema.get("nullable", False)

    if typ == "string":
        if fmt == "date-time":
            base = "datetime"
        elif fmt == "date":
            base = "date"
        elif fmt == "uuid":
            base = "str"
        elif "enum" in schema and not simple:
            values = schema["enum"]
            literal = "Literal[" + ", ".join(repr(v) for v in values) + "]"
            # Fall back to str if the Literal type is too long
            base = literal if len(literal) <= 80 else "str"
        else:
            base = "str"
    elif typ == "integer":
        base = "int"
    elif typ == "number":
        base = "float"
    elif typ == "boolean":
        base = "bool"
    elif typ == "array":
        items = schema.get("items", {})
        item_type = schema_to_type(items, for_field=False, simple=simple, current_model=current_model)
        base = f"list[{item_type}]"
    elif typ == "object":
        additional = schema.get("additionalProperties")
        if additional:
            val_type = schema_to_type(additional, for_field=False, simple=simple, current_model=current_model)
            base = f"dict[str, {val_type}]"
        else:
            base = "dict[str, Any]"
    else:
        base = "Any"

    if nullable and for_field:
        return f"{base} | None"
    return base


# ---------------------------------------------------------------------------
# Model generation
# ---------------------------------------------------------------------------


def generate_models(spec: dict) -> str:
    """Generate Pydantic models for all schemas."""
    schemas = spec.get("components", {}).get("schemas", {})
    lines: list[str] = []

    lines.append('"""Auto-generated Pydantic models from Shortcut OpenAPI spec."""')
    lines.append("")
    lines.append("from datetime import date, datetime  # noqa: F401")
    lines.append("from typing import Any, Literal")
    lines.append("")
    lines.append("from pydantic import BaseModel, ConfigDict, Field")
    lines.append("")
    lines.append("")

    # Topological sort: generate models in dependency order
    order = topological_sort(schemas)

    for name in order:
        schema = schemas[name]
        lines.extend(generate_model_class(name, schema))
        lines.append("")
        lines.append("")

    # Rebuild models at the end to resolve forward references
    lines.append("# Rebuild all models to resolve forward references")
    for name in order:
        lines.append(f"{name}.model_rebuild()")

    lines.append("")
    return "\n".join(lines)


def topological_sort(schemas: dict) -> list[str]:
    """Sort schemas so dependencies come before dependents."""
    visited: set[str] = set()
    order: list[str] = []

    def visit(name: str) -> None:
        if name in visited or name not in schemas:
            return
        visited.add(name)
        schema = schemas[name]
        for dep in get_schema_deps(schema):
            visit(dep)
        order.append(name)

    for name in schemas:
        visit(name)
    return order


def get_schema_deps(schema: dict) -> list[str]:
    """Get schema names that this schema depends on."""
    deps = []
    if "$ref" in schema:
        deps.append(resolve_ref(schema["$ref"]))
    for prop in schema.get("properties", {}).values():
        if "$ref" in prop:
            deps.append(resolve_ref(prop["$ref"]))
        if prop.get("type") == "array" and "items" in prop:
            items = prop["items"]
            if "$ref" in items:
                deps.append(resolve_ref(items["$ref"]))
        if prop.get("additionalProperties") and "$ref" in prop["additionalProperties"]:
            deps.append(resolve_ref(prop["additionalProperties"]["$ref"]))
    return deps


def generate_model_class(name: str, schema: dict) -> list[str]:
    """Generate a single Pydantic model class."""
    lines: list[str] = []
    desc = schema.get("description", "")

    lines.append(f"class {name}(BaseModel):")

    if desc:
        safe_desc = desc.replace("\n", " ").strip()
        # Check if single-line docstring fits
        single_line = f'    """{safe_desc}"""'
        if len(single_line) <= 120:
            lines.append(single_line)
        else:
            # Multi-line docstring
            wrapped = textwrap.fill(safe_desc, width=112)
            lines.append('    """')
            for wl in wrapped.splitlines():
                lines.append(f"    {wl}")
            lines.append('    """')
        lines.append("")

    lines.append("    model_config = ConfigDict(populate_by_name=True)")
    lines.append("")

    properties = schema.get("properties", {})
    required_fields = set(schema.get("required", []))

    if not properties:
        lines.append("    pass")
        return lines

    for field_name, field_schema in properties.items():
        python_name = safe_field_name(field_name)
        type_str = schema_to_type(field_schema, current_model=name)
        is_required = field_name in required_fields
        nullable = field_schema.get("nullable", False)
        field_desc = field_schema.get("description", "")

        # Build Field() kwargs
        field_kwargs: list[str] = []

        if python_name != field_name:
            field_kwargs.append(f"alias={field_name!r}")

        if not is_required:
            if nullable or "| None" in type_str:
                type_str = type_str if "| None" in type_str else f"{type_str} | None"
                default = "None"
            else:
                type_str = f"{type_str} | None"
                default = "None"
            field_kwargs.insert(0, f"default={default}")
        elif nullable:
            # Required but nullable
            if "| None" not in type_str:
                type_str = f"{type_str} | None"

        # Build the line without description first to calculate available space
        if field_kwargs:
            kwargs_str = ", ".join(field_kwargs)
            line_without_desc = f"    {python_name}: {type_str} = Field({kwargs_str})"
        else:
            line_without_desc = f"    {python_name}: {type_str}"

        # Add description if it fits, truncating if needed
        if field_desc and field_kwargs:
            escaped_desc = field_desc.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")
            # Calculate max description length: 120 - len(prefix) - len(', description="') - len('")')
            prefix_len = len(line_without_desc) - 1  # -1 for the closing )
            overhead = len(', description="') + len('")')
            max_desc_len = 120 - prefix_len - overhead
            if max_desc_len > 20:
                if len(escaped_desc) > max_desc_len:
                    escaped_desc = escaped_desc[: max_desc_len - 3] + "..."
                field_kwargs.append(f'description="{escaped_desc}"')
                kwargs_str = ", ".join(field_kwargs)
                lines.append(f"    {python_name}: {type_str} = Field({kwargs_str})")
            else:
                # Not enough space for description, skip it
                lines.append(line_without_desc)
        elif field_desc and not field_kwargs:
            # Simple field with just a description
            escaped_desc = field_desc.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")
            candidate = f'    {python_name}: {type_str} = Field(description="{escaped_desc}")'
            if len(candidate) <= 120:
                lines.append(candidate)
            else:
                max_desc_len = 120 - len(f'    {python_name}: {type_str} = Field(description="') - len('")')
                if max_desc_len > 20:
                    escaped_desc = escaped_desc[: max_desc_len - 3] + "..."
                    lines.append(f'    {python_name}: {type_str} = Field(description="{escaped_desc}")')
                else:
                    lines.append(line_without_desc)
        else:
            lines.append(line_without_desc)

    return lines


# ---------------------------------------------------------------------------
# Client generation
# ---------------------------------------------------------------------------


def generate_client(spec: dict) -> str:
    """Generate the ShortcutClient class with all API methods."""
    lines: list[str] = []

    lines.append('"""Auto-generated Shortcut API client."""')
    lines.append("")
    lines.append("from typing import Any")
    lines.append("")
    lines.append("import httpx")
    lines.append("")
    lines.append("from shortcut_python_client.models import (")

    # Collect all model names used in endpoints
    model_names = collect_used_models(spec)
    for name in sorted(model_names):
        lines.append(f"    {name},")
    lines.append(")")
    lines.append("")
    lines.append("")
    lines.append('BASE_URL = "https://api.app.shortcut.com"')
    lines.append("")
    lines.append("")
    lines.append("class ShortcutClient:")
    lines.append('    """Python client for the Shortcut REST API v3."""')
    lines.append("")
    lines.append("    def __init__(self, api_token: str, *, base_url: str = BASE_URL, timeout: float = 30.0) -> None:")
    lines.append('        """Initialize the client.')
    lines.append("")
    lines.append("        Args:")
    lines.append("            api_token: Your Shortcut API token.")
    lines.append("            base_url: API base URL (default: https://api.app.shortcut.com).")
    lines.append("            timeout: Request timeout in seconds.")
    lines.append('        """')
    lines.append("        self._client = httpx.Client(")
    lines.append("            base_url=base_url,")
    lines.append('            headers={"Shortcut-Token": api_token, "Content-Type": "application/json"},')
    lines.append("            timeout=timeout,")
    lines.append("        )")
    lines.append("")
    lines.append("    def close(self) -> None:")
    lines.append('        """Close the underlying HTTP client."""')
    lines.append("        self._client.close()")
    lines.append("")
    lines.append('    def __enter__(self) -> "ShortcutClient":')
    lines.append("        return self")
    lines.append("")
    lines.append("    def __exit__(self, *args: Any) -> None:")
    lines.append("        self.close()")
    lines.append("")
    lines.append("    def _request(")
    lines.append("        self,")
    lines.append("        method: str,")
    lines.append("        path: str,")
    lines.append("        *,")
    lines.append("        json: Any = None,")
    lines.append("        params: dict[str, Any] | None = None,")
    lines.append("    ) -> httpx.Response:")
    lines.append('        """Make an authenticated request to the Shortcut API."""')
    lines.append("        response = self._client.request(method, path, json=json, params=params)")
    lines.append("        response.raise_for_status()")
    lines.append("        return response")
    lines.append("")

    # Generate methods for each endpoint
    for path, methods in spec["paths"].items():
        for method, details in methods.items():
            if method not in ("get", "post", "put", "delete"):
                continue
            lines.extend(generate_method(path, method, details))
            lines.append("")

    return "\n".join(lines)


def collect_used_models(spec: dict) -> set[str]:
    """Collect all model names referenced by API endpoints."""
    models: set[str] = set()
    for _path, methods in spec["paths"].items():
        for method, details in methods.items():
            if method not in ("get", "post", "put", "delete"):
                continue
            # Request body
            if "requestBody" in details:
                content = details["requestBody"].get("content", {}).get("application/json", {})
                schema = content.get("schema", {})
                if "$ref" in schema:
                    models.add(resolve_ref(schema["$ref"]))
            # Response
            for code in ("200", "201"):
                resp = details.get("responses", {}).get(code, {})
                if "content" in resp:
                    rs = resp["content"].get("application/json", {}).get("schema", {})
                    if "$ref" in rs:
                        models.add(resolve_ref(rs["$ref"]))
                    elif rs.get("type") == "array" and "$ref" in rs.get("items", {}):
                        models.add(resolve_ref(rs["items"]["$ref"]))
    return models


def generate_method(path: str, method: str, details: dict) -> list[str]:
    """Generate a single API method."""
    lines: list[str] = []

    op_id = details.get("operationId", "")
    method_name = camel_to_snake(op_id)
    summary = details.get("summary", "")
    description = details.get("description", "")

    # Parse path params and query params
    path_params: list[dict] = []
    query_params: list[dict] = []
    for param in details.get("parameters", []):
        if param["in"] == "path":
            path_params.append(param)
        elif param["in"] == "query":
            query_params.append(param)

    # Request body
    body_type: str | None = None
    body_is_required = False
    if "requestBody" in details:
        content = details["requestBody"].get("content", {}).get("application/json", {})
        schema = content.get("schema", {})
        if "$ref" in schema:
            body_type = resolve_ref(schema["$ref"])
        body_is_required = details["requestBody"].get("required", False)

    # Response type
    return_type = "None"
    return_model: str | None = None
    is_list = False
    for code in ("200", "201"):
        resp = details.get("responses", {}).get(code, {})
        if "content" in resp:
            rs = resp["content"].get("application/json", {}).get("schema", {})
            if "$ref" in rs:
                return_model = resolve_ref(rs["$ref"])
                return_type = return_model
            elif rs.get("type") == "array" and "$ref" in rs.get("items", {}):
                return_model = resolve_ref(rs["items"]["$ref"])
                return_type = f"list[{return_model}]"
                is_list = True
            break
        elif code in details.get("responses", {}):
            return_type = "None"
            break

    # Build method signature
    sig_parts: list[str] = ["self"]

    # Path params (always required)
    for p in path_params:
        pname = param_name_to_python(p["name"])
        ptype = "int" if p.get("schema", {}).get("type") == "integer" else "str"
        sig_parts.append(f"{pname}: {ptype}")

    # Body param
    if body_type:
        if body_is_required:
            sig_parts.append(f"data: {body_type}")
        else:
            sig_parts.append(f"data: {body_type} | None = None")

    # Query params (keyword-only after *)
    if query_params:
        sig_parts.append("*")
        for p in query_params:
            pname = param_name_to_python(p["name"])
            ptype = schema_to_type(p.get("schema", {}), for_field=False, simple=True)
            if not p.get("required", False):
                sig_parts.append(f"{pname}: {ptype} | None = None")
            else:
                sig_parts.append(f"{pname}: {ptype}")

    # Build method signature, breaking lines if too long
    sig = ", ".join(sig_parts)
    one_line = f"    def {method_name}({sig}) -> {return_type}:"
    if len(one_line) <= 120:
        lines.append(one_line)
    else:
        lines.append(f"    def {method_name}(")
        for part in sig_parts:
            lines.append(f"        {part},")
        lines.append(f"    ) -> {return_type}:")

    # Docstring
    doc = summary or description
    if doc:
        lines.append(f'        """{doc}"""')

    # Build path with substitutions
    api_path = path
    for p in path_params:
        placeholder = "{" + p["name"] + "}"
        python_var = param_name_to_python(p["name"])
        api_path = api_path.replace(placeholder, "{" + python_var + "}")

    if path_params:
        lines.append(f'        path = f"{api_path}"')
    else:
        lines.append(f'        path = "{api_path}"')

    # Query params dict
    if query_params:
        lines.append("        params: dict[str, Any] = {}")
        for p in query_params:
            pname = param_name_to_python(p["name"])
            original_name = p["name"]
            lines.append(f"        if {pname} is not None:")
            lines.append(f'            params["{original_name}"] = {pname}')

    # Build request call
    req_kwargs: list[str] = [f'"{method.upper()}"', "path"]
    if body_type:
        lines.append("        json_data = (")
        lines.append('            data.model_dump(mode="json", by_alias=True, exclude_none=True)')
        lines.append("            if data is not None")
        lines.append("            else None")
        lines.append("        )")
        req_kwargs.append("json=json_data")
    if query_params:
        req_kwargs.append("params=params")

    req_call = ", ".join(req_kwargs)

    if return_type == "None":
        lines.append(f"        self._request({req_call})")
    elif is_list:
        lines.append(f"        response = self._request({req_call})")
        lines.append(f"        return [{return_model}.model_validate(item) for item in response.json()]")
    else:
        lines.append(f"        response = self._request({req_call})")
        lines.append(f"        return {return_model}.model_validate(response.json())")

    return lines


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    spec = load_spec()

    # Generate models
    models_code = generate_models(spec)
    models_path = OUTPUT_DIR / "models.py"
    models_path.write_text(models_code)
    print(f"Generated {models_path}")

    # Generate client
    client_code = generate_client(spec)
    client_path = OUTPUT_DIR / "client.py"
    client_path.write_text(client_code)
    print(f"Generated {client_path}")


if __name__ == "__main__":
    main()
