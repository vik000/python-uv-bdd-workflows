---
description: Branch, register the marker, write failing tests only
---

Use the python-uv-gh-workflow skill.

For issue $ARGUMENTS:

1. Confirm the worktree is clean, then create branch `issue-$ARGUMENTS-<short-slug>`.
2. Register the pytest marker via the bundled workflow script.
3. Convert every acceptance scenario into a test marked `@pytest.mark.issue_$ARGUMENTS`.
   Add the most comprehensive applicable lower-level tests from the test-strategy matrix.
   Prefer observable behaviour over implementation details.
4. Run the focused marker and show me the output.
5. For each failing test, state which missing behaviour causes the failure. If any test
   passes before implementation, say whether the behaviour already exists or the test is
   ineffective — do not call this a valid RED phase without evidence.

Write no implementation code. Stop after the failing run.
