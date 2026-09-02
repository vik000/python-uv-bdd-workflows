---
description: Show one issue's criteria, invariants and test plan. Changes nothing.
---

Read issue $ARGUMENTS with the bundled workflow script. Do not work from memory.

Print, in this order, nothing else:

ISSUE      <n> - <title>
OBJECTIVE  <one line>

CRITERIA
AC1 <Given/When/Then, one line each>

INVARIANTS
SI1 <one line>

TEST PLAN
<category>  exercised, or N/A: reason

GAPS
<criterion or invariant with no covering test category, or "none">

ESTIMATE   <number> criteria, roughly <number> /green runs

Then stop. Do not branch, register markers or write tests.
