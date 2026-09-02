---
description: Verify, map evidence to criteria, commit locally. Does not push or close remotely.
---

Use the python-uv-gh-workflow skill.

**Read the managed CLAUDE.md checkpoint** to identify the active issue, or use $ARGUMENTS
if I gave a number. Re-read that issue with the bundled workflow script.

1. Confirm the diff is confined to issue scope and the worktree has no unrelated changes.
   If anything unrelated is staged, stop and show me before going further.
2. Run and show output for the focused marker, the full suite, and branch coverage.
3. Map every acceptance criterion and safety invariant to a named passing test. List any
   that map to nothing — those are gaps, not completions. If there are gaps, stop here and
   tell me; do not commit incomplete work as if it were done.
4. State plainly that coverage is evidence of execution, not proof of correctness. Do not
   claim guaranteed safety.
5. Show me the proposed commit message, then commit the scoped files. Use the form
   `CLOSES: Issue #<number> — <title>`.
6. Clear the managed checkpoint.
7. Tell me what remains: pushing, tagging, bumping the version, and closing the issue
   remotely. Do none of them.

Ask me before any push, tag, version bump or remote issue close — separately, one at a time.
