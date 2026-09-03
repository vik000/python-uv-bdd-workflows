---
description: Publish designed slices to GitHub as full issues. Asks first.
---

Publish slice $ARGUMENTS. If no argument is given, default to the lowest-numbered slice
that has a DESIGN file, has no GitHub number recorded, and has scenarios written. Say
which one you chose and why in one line, and let me override it.

For each slice to publish, fill assets/feature-issue.md from the skill using ONLY what I
already decided. Map it as follows - invent nothing:

- Objective            <- PURPOSE line of the DESIGN file
- Scope / In scope     <- what goes in, what comes out
- Scope / Out of scope <- my answer to "out of scope"
- Assumptions          <- FITS line of the DESIGN file
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

STEP 1 - print the filled issue body and stop. Then one line:
Say "go" to create this issue, or tell me what to change.

STEP 2 - only after I say go:
1. Create the GitHub issue with the slice name as title and the filled template as body.
2. Record at the top of the DESIGN file: GitHub: #<n>
3. Never create a second issue for a slice that already has a number recorded.

Print only:

CREATED  #<n> <title>
NEXT     <single next action>

Do not push the branch. Do not close anything.
