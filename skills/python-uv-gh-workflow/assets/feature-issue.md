## Objective

<!-- What user or system outcome must change, and why? -->

## Scope

### In scope

-

### Out of scope

-

## Assumptions and dependencies

-

## Acceptance criteria

### Scenario 1 —

```gherkin
Given
When
Then
```

## Safety invariants

<!-- Conditions that must never be violated. Include fail-safe behaviour. -->

-

## Failure and uncertainty behaviour

-

## Test strategy

Mark each category **Required** or **N/A — reason**.

| Category | Decision | Planned evidence |
|---|---|---|
| BDD acceptance | Required | |
| Unit | | |
| Boundary/equivalence partitions | | |
| Negative/malformed input | | |
| Property-based | | |
| State transition/invariant | | |
| Contract/schema | | |
| Integration | | |
| Concurrency/idempotency | | |
| Timeout/retry/degraded service | | |
| Security/authorization/privacy | | |
| Regression | Required | Full suite |
| Mutation testing | | |

## Traceability

- GitHub issue: #{{ISSUE_NUMBER}}
- Pytest marker: `@pytest.mark.{{PYTEST_MARKER}}`
- Focused command: `{{FOCUSED_TEST_COMMAND}}`
- Requirement/test mapping:
  - AC1 →
  - SI1 →

## Version impact

- [x] Patch — default issue completion
- [ ] Minor — backward-compatible capability
- [ ] Major — breaking contract

## Completion evidence

- [ ] Focused marker passes
- [ ] Full regression suite passes
- [ ] Applicable coverage and quality gates pass
- [ ] Acceptance criteria mapped to tests
- [ ] Safety invariants mapped to tests
- [ ] Diff reviewed for issue scope
- [ ] Version incremented with `uv version`
- [ ] Exact commands and results recorded

