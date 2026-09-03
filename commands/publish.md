---
description: Publish designed slices to GitHub as full issues. Detects drift. Asks first.
---

The DESIGN file is the source of truth. GitHub is a published record of it. Nothing on
GitHub is ever read back into a design.

Argument handling:
- /publish <n>    that slice only
- /publish all    every slice with a DESIGN file
- /publish        the lowest-numbered slice with a DESIGN file, scenarios written, and no
                  GitHub number recorded. Say which one you chose in one line.

For each slice in scope, determine its state:
- NEW       no "GitHub:" line in the DESIGN file
- IN SYNC   has a GitHub number, and the recorded design hash matches the file now
- DRIFTED   has a GitHub number, but the design has changed since it was published

Fill assets/feature-issue.md from the skill using ONLY what I already decided. Map it as
follows - invent nothing:

- Objective            <- the OBJECTIVE paragraph of the DESIGN file
- Scope / In scope     <- what goes in, what comes out
- Scope / Out of scope <- my answer to "out of scope"
- Assumptions          <- the FITS line of the DESIGN file
- Acceptance criteria  <- one Given/When/Then per approved scenario row, numbered to
                          match the scenario numbers in the test docstrings
- Safety invariants    <- my answers to "what must never happen"
- Failure & uncertainty<- my answers to "malformed or empty" and "uncertain"
- Test strategy        <- mark Required only for categories the written tests actually
                          cover. Mark every other category "N/A - toy scale, single
                          session" or a truer reason. Never mark Required for a category
                          with no test behind it.
- Traceability         <- the pytest marker, the focused command, and each scenario
                          number mapped to its test name

STEP 1 - print a state table and stop:

| Slice | Title | State | Action |
|-------|-------|-------|--------|

Action is "create issue", "update #<n>", or "nothing - in sync".
For any DRIFTED slice, print underneath it the specific sections that changed, one line
each. Do not print the whole diff.

Then one line: Say "go" to apply, or name the slices to skip.

STEP 2 - only after I say go, for each approved slice:
- NEW:     create the issue, then write two lines at the top of the DESIGN file:
           GitHub: #<n>
           Published: <sha256 of the design file content at publish time, first 12 chars>
- DRIFTED: update the existing issue body, then rewrite the Published hash.
- IN SYNC: do nothing.

Never create a second issue for a slice that already has a number recorded.

Print only:

CREATED  <issue number and title, one per line, or none>
UPDATED  <issue number and title, one per line, or none>
IN SYNC  <slice numbers, or none>
NEXT     <single next action>

Do not push the branch. Do not close anything.
