# Tool Capabilities

## Principle

Tools are enhancements. Always detect availability before use and provide a fallback.

## Planned Scripts

### scripts/init_project_docs.py

Creates project docs for `light`, `standard`, or `strict` mode.

Example:

```bash
python software-dev-guide/scripts/init_project_docs.py --project-path /path/to/project --mode standard --project-name "Student Manager" --project-type "web app"
```

### scripts/validate_harness_state.py

Checks required docs, pending gates, unresolved exceptions, unverified rollbacks, locks, and traceability matrix issues.

Example:

```bash
python software-dev-guide/scripts/validate_harness_state.py --project-path /path/to/project --mode standard
```

### scripts/find_next_task.py

Finds next safe action from docs.

Example:

```bash
python software-dev-guide/scripts/find_next_task.py --project-path /path/to/project
```

## Optional MCP Enhancements

Stitch MCP may provide:

```text
create_project
generate_screen_from_text
edit_screens
generate_variants
list_projects
list_screens
get_project
get_screen
apply_design_system
```

If unavailable, downgrade to Codex native design, screenshots, exported design files, or manual design notes.

