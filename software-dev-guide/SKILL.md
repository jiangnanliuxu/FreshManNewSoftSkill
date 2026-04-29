---
name: software-dev-guide
description: Guide beginner or non-technical users through a controlled, document-driven software development lifecycle. Use when the user wants to build software, a website, app, mini program, backend system, dashboard, automation tool, course project, or digital product and needs step-by-step requirements analysis, product design, UI design choices including optional Stitch MCP, module planning, development, interruption recovery, change handling, testing, rollback, release preparation, or final delivery documentation.
---

# Software Dev Guide

## Operating Rule

Use this skill as a harness, not as a free-form checklist. Do not jump directly into coding. First identify the user's intent, project path, complexity mode, available docs, unresolved gates, current module, and next safe action.

Every meaningful conclusion must be persisted into project docs. Do not rely on chat memory for project state.

## Quick Start

1. Ask whether this is a new project, an existing project, a change request, a test request, a release request, or a delivery-document request.
2. Identify the project path. If the project has no `docs/`, initialize docs with `scripts/init_project_docs.py`.
3. Select complexity mode:
   - `light`: single page, static site, small homework, no backend.
   - `standard`: course project, mini program, dashboard, CRUD app, small backend.
   - `strict`: real launch, multi-role permissions, sensitive data, frequent changes.
4. Run or conceptually apply `scripts/validate_harness_state.py` before development, testing, release, or recovery.
5. Use `scripts/find_next_task.py` to determine the next safe action when continuing a project.
6. Advance only one unit per turn: one question group, one module, one test batch, one change request, one rollback, or one delivery package.

## Core Loop

Follow this loop every turn:

```text
ParseIntent -> LoadState -> SelectMode -> ValidateGuards -> RouteStage -> DispatchAgent -> ExecuteOneUnit -> Persist -> Report
```

Use these roles:

- Main Agent: project control, routing, mode selection, gates, exceptions, rollback, final decisions.
- A Agent: requirements, product design, UI/interaction standards, change decomposition.
- B Agent: module breakdown, implementation, completeness check, development log, recovery checks.
- C Agent: test plan, test execution, UI/interaction validation, defects, release verification.

If sub-agents are unavailable, perform the roles sequentially as the Main Agent while preserving the same handoff contracts.

## Stage Routing

| Stage | Name | Owner | Exit Condition |
| --- | --- | --- | --- |
| 0 | Identify state and mode | Main | Intent, project path, mode, next stage known |
| 1 | Project positioning | A | User can describe project in 1-3 sentences |
| 2 | Requirements analysis | A | MVP and priorities confirmed |
| 3 | Product/UI design | A / optional Stitch | Pages, flow, UI acceptance criteria confirmed |
| 4 | Technical plan | Main / B | Stack, structure, commands confirmed |
| 5 | Development | B | P0 modules developed and logged |
| 6 | Testing | C | P0 tests pass or defects are routed back |
| 7 | Release prep and delivery | Main / B / C | Release checklist and delivery package complete |

Special entries:

- Continue development: run recovery checks, inspect logs and code, then resume.
- New requirement: pause current work, create a change request, ask for insertion confirmation.
- Rollback or cancel: create rollback record, confirm with user, update docs and tests.
- State mismatch: create exception record and pause normal progress.
- Final delivery: generate `docs/16-最终交付包说明.md`.

## UI Design Choice

At Stage 3, ask the user to choose:

1. Codex native UI design: fast, no external dependency.
2. Stitch enhanced UI design: higher-quality UI workflow if Stitch MCP is available.

If the user chooses Stitch:

1. Detect whether Stitch MCP tools are available.
2. If available, create or locate a Stitch project, generate/read screens, and write the result into product docs.
3. If unavailable, guide connection or downgrade to Codex native design, uploaded screenshots, exported files, or manual design notes.

Stitch is an enhancement, not a hard dependency.

See `references/stitch-ui-flow.md` for details.

## Required Docs

Project docs live in `docs/`:

```text
00-项目状态总览.md
01-项目需求说明书.md
02-产品页面与业务流程.md
03-技术方案与模块拆分.md
04-开发任务看板.md
05-开发日志.md
06-测试计划.md
07-测试报告.md
08-上线检查清单.md
09-需求变更记录.md
10-需求模块测试追踪矩阵.md
11-协同事件日志.md
12-用户确认门禁.md
13-异常处理记录.md
14-回滚与撤销记录.md
15-UI交互验收标准.md
16-最终交付包说明.md
```

Use only the docs required by the selected mode. See `references/document-schemas.md`.

## Guardrails

Do not proceed when any of these are true:

- A required user confirmation gate is pending.
- A module is locked by another role.
- An unresolved exception exists.
- A rollback is pending verification.
- A P0 requirement has no module or test mapping.
- Development is requested before MVP and technical plan are confirmed.
- Testing is requested before implementation handoff exists.
- Release is requested before P0 tests pass.

## Scripts

Use scripts when available:

```text
scripts/init_project_docs.py       Create docs templates for light/standard/strict mode.
scripts/validate_harness_state.py  Check doc consistency and guard status.
scripts/find_next_task.py          Decide the next safe action.
```

Scripts are helpers. If a script fails, explain the failure, record an exception if it affects project state, then continue with the best safe fallback.

## References

- `references/harness.md`: full control loop, stage routing, mode rules.
- `references/document-schemas.md`: doc templates and status schemas.
- `references/agent-contracts.md`: role responsibilities, permissions, handoffs.
- `references/tool-capabilities.md`: scripts and optional MCP capability rules.
- `references/stitch-ui-flow.md`: Stitch enhanced UI design workflow and fallback.

