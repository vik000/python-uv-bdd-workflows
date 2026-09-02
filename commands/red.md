---
description: Branch, marker, checkpoint, failing tests. Reports state.
---

For issue $ARGUMENTS:

1. Read the issue with the bundled workflow script.
2. Print the acceptance criteria as a numbered list before writing anything. This is the
   list every later command reports progress against.
3. Confirm the worktree is clean, create branch issue-$ARGUMENTS-<short-slug>.
4. Register the pytest marker via the bundled workflow script.
5. Set the managed CLAUDE.md checkpoint: issue, title, branch, phase RED, criteria total,
   next action.
6. Write tests marked with the issue marker covering every acceptance criterion and safety
   invariant. Keep them in as few files as the test-strategy categories allow. Every test
   name must make clear which criterion it covers.
7. If a test imports a module that does not exist yet, create a minimal stub so the suite
   collects. Import errors abort collection and hide the real state - never leave them.
8. Run the full suite.
9. Commit with message: Issue #$ARGUMENTS: failing tests

Write no implementation logic. Finish with these lines and nothing else:

ISSUE      <n> - <title>
CRITERIA   0/<total> done
REMAINING  <criterion id and short name, one per line>
SUITE      <passed> passed, <failed> failed
COMMITTED  <sha> <message>
NEXT       run /green
