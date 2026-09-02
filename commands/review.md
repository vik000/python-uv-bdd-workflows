---
description: Safety inspection of the last commit. Applies nothing.
---

Read the managed CLAUDE.md checkpoint, then re-read the issue with the bundled workflow
script so invariants come from the source of truth.

Inspect the diff of the last commit. For each heading print one line: the heading, then
either ok or the finding with file and line.

1. FAILURE DIRECTION - on parse failure, timeout, empty input or refusal, does the
   default land safe or convenient?
2. UNCERTAINTY PATH - can it express "I don't know", or is it forced to guess?
3. SWALLOWED EXCEPTIONS - caught and continued without a decision.
4. UNVALIDATED OUTPUT - model output used before validation.
5. BOUNDARY - off-by-one, empty collection, missing key, None.
6. SCOPE - anything in the diff the issue did not ask for.
7. ASSERTIONS - do tests assert on schema and invariants, or on generated prose?

Then one line per safety invariant: SI<n> holds, or SI<n> at risk: reason

Propose fixes as a numbered list, one line each. Apply nothing.

Finish with the status block. No prose.
