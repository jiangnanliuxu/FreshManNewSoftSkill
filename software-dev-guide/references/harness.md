# Software Dev Guide Harness

## Purpose

This reference defines the control harness for a document-driven multi-agent software development workflow. It turns user intent into a bounded next action, writes state into docs, and prevents uncontrolled jumps between requirements, development, testing, release, and delivery.

## Main Loop

```text
ParseIntent -> LoadState -> SelectMode -> ValidateGuards -> RouteStage -> DispatchAgent -> ExecuteOneUnit -> Persist -> Report
```

Each turn should move only one unit:

- One group of 3-5 questions.
- One flow/page group.
- One module.
- One test batch.
- One change request.
- One rollback.
- One final delivery package.

## Complexity Modes

| Mode | Use When | Control Level |
| --- | --- | --- |
| light | single-page, static, small homework, no backend | fast, minimal docs |
| standard | course project, mini program, CRUD, small backend | complete core docs |
| strict | real launch, roles/permissions, sensitive data, frequent changes | full gates and logs |

Mode may be upgraded by the Main Agent when project risk increases. Downgrading requires user confirmation.

## Stage Routing

| Stage | Name | Owner | Entry | Exit |
| --- | --- | --- | --- | --- |
| 0 | Identify state and mode | Main | skill triggered | intent/path/mode known |
| 1 | Project positioning | A | new or vague project | project goal summarized |
| 2 | Requirements analysis | A | goal known | MVP confirmed |
| 3 | Product/UI design | A / Stitch | MVP confirmed | pages and UI criteria confirmed |
| 4 | Technical plan | Main/B | product design known | stack and commands confirmed |
| 5 | Development | B | guards pass | module logged and ready for test |
| 6 | Testing | C | module ready | pass or defect routed |
| 7 | Release/delivery | Main/B/C | P0 tests pass | checklist and delivery package done |

## Special Entries

| Entry | Trigger | Required Action |
| --- | --- | --- |
| Recovery | "continue", "resume" | read state, logs, matrix; inspect current module |
| Change request | "add feature" | pause, record CR, decompose, ask insertion decision |
| Exception | state mismatch | pause normal flow, record EX, reconcile |
| Rollback | "remove", "go back" | record RB, confirm, update docs and tests |
| Delivery | "hand in", "demo", "final docs" | generate final delivery package |

## Guard Checks

Stop normal progress if:

- Required confirmation is pending.
- Current module is locked by another role.
- Unresolved exception exists.
- Unverified rollback exists.
- P0 requirement has no module/test link.
- P0 test is not passed before release.

## Reporting Format

Every turn should end with:

```text
Current mode:
Current stage:
State read:
This turn:
Docs updated:
Blockers:
Next step:
Need user confirmation:
```

