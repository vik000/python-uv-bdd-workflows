---
description: Branch, register the marker, set the checkpoint, write failing tests only
---

Use the python-uv-gh-workflow skill.

For issue $ARGUMENTS:

1. Read the issue with the bundled workflow script. Do not rely on remembered or
   summarised requirements.
2. Confirm the worktree is clean, then create branch `issue-$ARGUMENTS-<short-slug>`.
3. Register the pytest marker via the bundled workflow script.
4. **Set the managed CLAUDE.md checkpoint** with the issue number, title, branch, phase
   `RED`, and next action. This is what makes the work resumable — never skip it.
5. Convert every acceptance scenario into a test marked `@pytest.mark.issue_$ARGUMENTS`.
   Add the most comprehensive applicable lower-level tests from the test-strategy matrix.
   Prefer observable behaviour over implementation details.
6. Run the focused marker and show me the output.
7. For each failing test, state which missing behaviour causes the failure. If any test
   passes before implementation, say whether the behaviour already exists or the test is
   ineffective — do not call this a valid RED phase without evidence.
8. Update the checkpoint's next action to name the acceptance criterion to implement first.

Write no implementation code. Stop after the failing run.
