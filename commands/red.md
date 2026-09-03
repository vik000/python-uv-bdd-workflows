---
description: Design the test scenarios together, then write them.
---

Read DESIGN-slice$ARGUMENTS.md. If it does not exist, tell me to run /design first and stop.

STEP 1 - propose scenarios. Print ONLY a table:

| # | Scenario | Given | Expect |
|---|----------|-------|--------|

Rules:
- One row per behaviour worth proving. Aim for four to eight rows total.
- Cover: the normal case, one malformed input, one uncertainty case, and every rule from
  "what must never happen".
- Each cell: one short line. No prose anywhere.

Then one line: Add, remove or change any row. Say "go" when it is right.

STEP 2 - only after I say go:
1. Create branch slice-$ARGUMENTS if not on it.
2. Write one test per approved row, in tests/test_slice$ARGUMENTS.py.
3. Name each test test_s<scenario number>_<short name> so the name maps to the table.
4. Give every test a one-line docstring in exactly this form, using the same words as the
   approved table row:
   s<n> | Given <given> | Expect <expect>
   The table row, the test name, the docstring and the commit message must all say the
   same thing. Do not paraphrase between them.
5. Mark every test @pytest.mark.slice$ARGUMENTS.
6. Register the marker in pyproject.toml if not present.
7. Stub any missing module so the suite collects. Never leave import errors.
8. Run the suite. Commit: slice $ARGUMENTS: failing tests

Print only:

SCENARIOS  <n> written
SUITE      <passed> passed, <failed> failed
NEXT       run /green
