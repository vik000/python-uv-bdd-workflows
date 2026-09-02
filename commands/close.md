---
description: Verify, map criteria to tests, report. Does not push or close remotely.
---

Read the managed CLAUDE.md checkpoint, or use $ARGUMENTS.

1. Run the focused marker, the full suite, and branch coverage.
2. Print one line per acceptance criterion and safety invariant, in the form
   AC<n> <criterion> -> <test name>, or AC<n> <criterion> -> NO TEST
3. If anything maps to NO TEST, print INCOMPLETE and stop.
4. Confirm the diff is confined to issue scope.
5. Commit anything outstanding with message: CLOSES: Issue #<n> - <title>
6. Clear the managed checkpoint.

State that coverage is evidence of execution, not proof of correctness - one line.

Finish with the status block, then a single line listing what remains undone: push, tag,
version bump, remote close. Do none of them. No prose.
