---
description: Where am I? Prints state. Changes nothing.
---

Read the managed CLAUDE.md checkpoint for the active issue, then read that issue with
the bundled workflow script. Run the full suite quietly.

Print exactly these lines and nothing else:

ISSUE       <n> - <title>
CRITERIA    <done>/<total> done
REMAINING   <criterion id and short name, one per line>
SUITE       <passed> passed, <failed> failed
LAST GREEN  <commit sha and message, or "none committed">
UNCOMMITTED <files changed since last commit, or "clean">
NEXT        <the single next action>

No prose before or after. No explanation. If the checkpoint is missing, print
NO ACTIVE ISSUE and stop.
