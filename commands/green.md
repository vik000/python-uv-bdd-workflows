---
description: Implement the minimum for one acceptance criterion
---

Use the python-uv-gh-workflow skill.

**Read the managed CLAUDE.md checkpoint first** to identify the active issue, branch and
marker. Do not infer them from conversation history. If the checkpoint is missing or
disagrees with the current branch, stop and tell me — do not guess which issue this is.

Re-read that issue with the bundled workflow script before writing anything.

Implement exactly one failing acceptance scenario — the one named in the checkpoint's
next action, unless I name a different one in $ARGUMENTS.

Constraints:

- Minimum behaviour to pass that scenario. No speculative abstractions.
- No new dependencies without asking me first.
- Do not modify tests to make them pass.
- Do not touch files outside the issue's scope.

Then:

1. Run the focused marker and show me the output.
2. Show me the diff.
3. Update the checkpoint: phase `GREEN`, last verified command and result, and the next
   action.

Stop. Do not refactor, commit or start the next criterion.
