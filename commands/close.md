---
description: Verify, map evidence to criteria, commit. Does not close remotely.
---

Use the python-uv-gh-workflow skill.

For issue $ARGUMENTS:

1. Confirm the diff is confined to issue scope and the worktree has no unrelated changes.
2. Run and show output for the focused marker, the full suite, and branch coverage.
3. Map every acceptance criterion and safety invariant to a named passing test. List any
   that map to nothing — those are gaps, not completions.
4. State plainly that coverage is evidence of execution, not proof of correctness, and do
   not claim guaranteed safety.
5. Show me the proposed commit message. Do not commit until I approve it.

Do not bump the version, push, tag, or close the issue remotely. Ask me first, separately,
for each of those.
