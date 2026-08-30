---
name: python-uv-gh-workflow
description: Plan and deliver traceable Python work from GitHub Issues using uv, pytest, BDD acceptance criteria, TDD, per-issue pytest markers, managed CLAUDE.md checkpoints, verification evidence, and semantic version increments. Use when creating issues from requirements, starting or resuming an issue, writing tests for an issue, implementing a Python issue, checking coverage and safety evidence, or completing and versioning issue-scoped work.
---

# Python uv GitHub workflow

Treat GitHub Issues as the requirements source of truth. Use `CLAUDE.md` only as a managed
checkpoint. Use `uv` for every Python environment, dependency, tool and test command.

Resolve `scripts/workflow.py`, `assets/feature-issue.md`, and the references relative to this
`SKILL.md` before running commands.

## Select the operation

- Requirements or an unstructured specification: create issues.
- Existing issue, new session, or resume request: start/resume the issue.
- Request to create tests: write the issue's failing tests.
- Request to implement: perform the TDD loop one acceptance slice at a time.
- Request to validate: execute the verification gates.
- Request to finish: bump the version, record evidence, commit and close only after confirmation.

Read [references/issue-schema.md](references/issue-schema.md) before creating or interpreting an
issue. Read [references/test-strategy.md](references/test-strategy.md) before writing tests or
declaring verification complete.

## Create issues

1. Clarify the objective, users, externally observable behaviour, failure behaviour and constraints.
2. Split work into independently testable vertical slices. Do not create layer-by-layer issues.
3. Copy `assets/feature-issue.md` to a temporary file and fill every section. Mark a test category
   `N/A` only with a concrete reason.
4. Include Given/When/Then acceptance scenarios, safety invariants and explicit out-of-scope items.
5. Create each issue through the bundled script:

```bash
uv run python <skill-dir>/scripts/workflow.py issue create \
  --title "Feature: ..." --body-file /tmp/issue.md
```

The script creates the issue, injects `issue_<number>` and prints the focused pytest command.

## Start or resume an issue

1. Read the issue; do not rely on remembered or duplicated requirements:

```bash
uv run python <skill-dir>/scripts/workflow.py issue view <number>
```

2. Verify the issue is open, internally consistent and small enough for one version increment.
3. Create or switch to `issue-<number>-<short-slug>` after confirming the worktree is safe.
4. Register the marker in the target project's `pyproject.toml`:

```bash
uv run python <skill-dir>/scripts/workflow.py marker ensure <number>
```

5. Update the managed `CLAUDE.md` checkpoint with phase `RED`, the branch, version and next action.
   Never overwrite content outside the managed block.

## Write tests first

1. Convert each acceptance scenario into a pytest test marked `@pytest.mark.issue_<number>`.
2. Add the most comprehensive applicable lower-level tests from the test-strategy matrix.
3. Prefer observable behaviour over implementation details.
4. Run the focused marker and prove that new tests fail for the intended missing behaviour:

```bash
uv run pytest -m issue_<number> -v
```

5. If a test passes before implementation, explain whether the behaviour already exists or the test
   is ineffective. Do not call it a valid RED phase without evidence.

## Implement one slice

1. Choose one failing acceptance scenario.
2. Implement the minimum behaviour required to pass it; do not add speculative abstractions.
3. Run the focused marker, then all tests changed or directly affected.
4. Review generated code for unsafe defaults, exception swallowing, boundary errors and divergence
   from the issue.
5. Refactor only while tests remain green. Repeat RED → GREEN → REFACTOR.
6. Update the checkpoint after every material phase transition.

## Verify

Run the commands declared in the issue. At minimum require:

```bash
uv sync
uv run pytest -m issue_<number> -v
uv run pytest -v
uv run pytest --cov --cov-branch
```

Require static analysis, type checking, security checks, mutation testing, integration tests and
domain validation when the issue marks them applicable. Coverage is evidence of execution, not proof
of correctness. Do not claim guaranteed safety.

Map every acceptance criterion and safety invariant to named passing tests. Record exact commands,
tool versions and results in the issue before completion.

## Finish and version

1. Confirm the diff is confined to issue scope and the worktree contains no unrelated changes.
2. Ask the user to confirm the verification evidence and intended version impact.
3. Default to `patch`; use `minor` for backward-compatible capability and `major` for a breaking
   contract. Bump with the bundled script, which delegates to `uv version`:

```bash
uv run python <skill-dir>/scripts/workflow.py version bump patch
```

4. Re-run focused and full verification after the version change.
5. Commit only scoped files with `CLOSES: Issue #<number> — <title> (v<version>)`.
6. Create a `v<version>` tag only when the commit is on the repository's intended release line.
7. Ask immediately before pushing, closing the issue or creating a remote tag unless the user's
   request already explicitly authorizes those actions.
8. Clear the managed checkpoint after successful completion.

Never treat a version increment, passing test suite, branch coverage percentage or mutation score as
a substitute for clinical safety validation, risk management or required human review.

