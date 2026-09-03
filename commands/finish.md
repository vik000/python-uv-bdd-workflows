---
description: Close out a slice. Verifies, bumps version, then asks before each remote action.
---

Finish slice $ARGUMENTS. If no argument is given, default to the slice on the current
branch. Say which one in one line and let me override it.

STEP 1 - verify. Print one line per scenario:
s<n> <scenario name> -> <test name> PASS, or -> NO TEST, or -> FAILING

If any line says NO TEST or FAILING, print INCOMPLETE with the count and STOP.
Do not bump, push or close incomplete work.

STEP 2 - print the evidence:

SUITE     <passed> passed, <failed> failed
COVERAGE  <branch coverage>
SCOPE     <files changed, or "outside issue scope: ...">

State in one line that coverage is evidence of execution, not proof of correctness.

STEP 3 - print one line per rule from "what must never happen" in the DESIGN file:
<rule> covered by <test name>, or <rule> NOT COVERED

If any rule is NOT COVERED, say so plainly and ask whether I want to proceed anyway.

STEP 4 - commit anything outstanding: CLOSES: slice <n> - <name>

STEP 5 - bump the version with the bundled workflow script. Patch by default. Tell me the
old and new version and let me change the level before you run it.

STEP 6 - ask me these ONE AT A TIME, waiting for a separate yes to each. Do none of them
without an explicit yes:

1. Push the branch?
2. Close GitHub issue #<n>?
3. Tag the version?

Print only:

FINISHED  slice <n> - <name>
VERSION   <old> -> <new>
PENDING   <anything I declined, one per line, or none>
NEXT      <single next action>
