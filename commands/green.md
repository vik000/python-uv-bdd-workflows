---
description: Implement one scenario. Checks sync. Explains what and why. Commits.
---

Read DESIGN-slice<n>.md and tests/test_slice<n>.py for the current branch.

SYNC CHECK, before anything else. Compare the DESIGN file against its recorded
Published hash:
- No GitHub line          -> print: NOT PUBLISHED - design is local only. Continuing.
- Hash matches            -> print: IN SYNC with #<n>
- Hash differs            -> print: DRIFTED from #<n> - design changed since publish.
                             Name the changed sections, then ask whether to continue or
                             run /publish first. Wait for my answer.

Then pick the next failing scenario, or the one named in $ARGUMENTS.

Before writing anything, print exactly this and nothing more:

SCENARIO   s<n> - <scenario name>
TESTING    <what behaviour this proves, one line>
EXPECT     <what the test asserts, one line>
APPROACH   <how you will implement it, one line>

Then wait for me to say go.

After I say go:
1. Record the current pass count.
2. Implement the minimum for that scenario only. No speculative abstractions. No new
   dependencies without asking. Never modify a test to make it pass.
3. Run the full suite.
4. If anything that was passing is now failing, print REGRESSION with the test names,
   revert, and stop.
5. Commit: slice <n> s<m>: <scenario name>

Then print only:

DONE       s<m> <scenario name>
SCENARIOS  <done>/<total>
REMAINING  <scenario number and name, one per line, or none>
SUITE      <passed> passed, <failed> failed
NEXT       run /green, or run /review
