# Agent Contracts

## Main Agent

Owns:

- Intent parsing.
- Complexity mode selection.
- Stage routing.
- User confirmation gates.
- Exception and rollback decisions.
- Final delivery summary.

Must not:

- Code before reading state.
- Develop before MVP and technical plan are confirmed.
- Release before P0 tests pass.
- Hide unfinished work.

## A Agent

Owns:

- Requirements questions.
- P0/P1/P2 decomposition.
- Product pages and flows.
- UI/interaction acceptance criteria.
- Product side of change requests.
- A -> B handoff.

Must not:

- Modify code.
- Modify development log.
- Decide change insertion alone.

## B Agent

Owns:

- Module breakdown.
- Code implementation.
- Development log.
- Completeness check.
- Recovery inspection.
- B -> C handoff.

Must not:

- Develop unclear requirements.
- Bypass module lock.
- Change acceptance criteria without Main/A approval.
- Skip logs or tests.

## C Agent

Owns:

- Test plan.
- Test cases.
- Functional, exception, regression, build, and UI tests.
- Defect reports.
- C -> Main handoff.

Must not:

- Modify production code directly.
- Test modules that are not ready.
- Ignore failed P0 tests.

## Handoff Templates

### A -> B

```markdown
## A -> B Handoff
Module:
Requirements:
Pages:
Business rules:
Fields:
API needs:
Data needs:
Acceptance criteria:
Non-negotiable:
Can simplify:
Open questions:
```

### B -> C

```markdown
## B -> C Handoff
Module:
Implemented:
Changed files:
Run command:
Build command:
Test focus:
Known gaps:
Development log:
```

### C -> Main

```markdown
## C -> Main Handoff
Module:
Test conclusion:
Passed:
Failed:
Blocking issues:
Suggested repair order:
Can proceed:
Can release:
Report path:
```

