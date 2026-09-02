---
description: Where am I? Changes nothing.
---

Find the current branch, its DESIGN file and its test file. Run the suite quietly.

Print only:

SLICE      <n> - <name>
SCENARIOS  <done>/<total>
REMAINING  <scenario number and name, one per line>
SUITE      <passed> passed, <failed> failed
LAST       <commit sha and message>
UNCOMMITTED <files, or clean>
NEXT       <single next action>

If there is no branch or design file, print NO ACTIVE SLICE and stop.
