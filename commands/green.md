---
description: Implement one acceptance criterion. Commits. Reports state.
---

Read the managed CLAUDE.md checkpoint for the active issue, branch and marker. Do not
infer them from conversation. If it is missing or disagrees with the current branch,
print CHECKPOINT MISMATCH with both values and stop.

Re-read the issue with the bundled workflow script.

Before writing anything, print one line:
IMPLEMENTING AC<n> - <short name>  (<done>/<total> criteria complete)

Then record the current full-suite pass count.

Implement exactly that one criterion - the next unimplemented one, or the one named in
$ARGUMENTS. Minimum behaviour. No speculative abstractions. No new dependencies without
asking. Do not modify tests to make them pass. Do not touch files outside issue scope.

Then:

1. Run the full suite.
2. If any test that was passing before is now failing, print REGRESSION with the test
   names, revert your changes, and stop. Do not proceed.
3. If clean, commit the scoped files with message: Issue #<n> AC<m>: <short name>
4. Update the checkpoint: phase, last verified command and result, next action.

Finish with these lines and nothing else:

ISSUE      <n> - <title>
CRITERIA   <done>/<total> done
REMAINING  <criterion id and short name, one per line, or "none">
SUITE      <passed> passed, <failed> failed
COMMITTED  <sha> <message>
NEXT       <the single next action, or "run /close">

No explanation of what you did beyond those lines.
