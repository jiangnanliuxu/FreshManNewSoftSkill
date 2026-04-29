# Stitch UI Enhanced Flow

## Positioning

Stitch is an optional Stage 3 enhancement for professional UI generation. It is not required for the skill to work.

## Choice Gate

At Stage 3, ask the user:

```text
Choose UI design method:
1. Codex native UI design
2. Stitch enhanced UI design
```

If unsure, default to Codex native UI design.

## Availability Check

If the user chooses Stitch:

1. Detect whether Stitch MCP tools are available.
2. If available, call `list_projects` or `create_project` to verify access.
3. If unavailable, offer connection guidance or downgrade.

## Stitch MCP Flow

```text
1. Main Agent creates confirmation gate for Stitch design.
2. A Agent turns requirements into a Stitch prompt.
3. Main Agent creates or opens Stitch project.
4. Main Agent generates screens or reads existing screens.
5. User edits design in Stitch if desired.
6. User says "done".
7. Main Agent reads project/screens through MCP.
8. A Agent writes product docs and UI acceptance criteria.
9. B Agent implements frontend from docs.
10. C Agent validates UI against the design and criteria.
```

## Fallback Flow

If Stitch is unavailable:

```text
1. Use Codex native UI design.
2. Or ask user to upload screenshots/exported files.
3. Or defer UI design and continue requirements/technical planning.
```

Record fallback reason in:

```text
docs/11-协同事件日志.md
docs/12-用户确认门禁.md
docs/15-UI交互验收标准.md
```

## Stitch Metadata To Save

```text
Stitch project ID:
Screen IDs:
Design update time:
User confirmation:
Design differences from original requirements:
```

