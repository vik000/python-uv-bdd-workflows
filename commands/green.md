---
description: Implement the minimum for one acceptance criterion
---

Use the python-uv-gh-workflow skill.

Implement exactly one failing acceptance scenario — the highest-risk one still failing,
unless I name a different one in $ARGUMENTS.

Constraints:

- Minimum behaviour to pass that scenario. No speculative abstractions.
- No new dependencies without asking me first.
- Do not modify tests to make them pass.
- Do not touch files outside the issue's scope.

Then run the focused marker, show me the output, and show me the diff. Stop.
