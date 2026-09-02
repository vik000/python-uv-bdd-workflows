---
description: Inspect the last change against the issue's safety invariants
---

Use the python-uv-gh-workflow skill.

**Read the managed CLAUDE.md checkpoint** to identify the active issue, then re-read that
issue with the bundled workflow script so the invariants come from the source of truth
rather than from memory.

Review the code written since the last commit. Report against every heading below
explicitly — say "none found" where that is true rather than omitting the heading:

1. **Failure direction.** On parse failure, timeout, empty input or model refusal, does
   the default land on the safe side or the convenient side?
2. **Uncertainty path.** Can the system express that it does not know, or is it
   structurally forced to guess?
3. **Swallowed exceptions.** Anything caught and continued without a decision.
4. **Unvalidated model output.** Anything used before it is validated.
5. **Boundary errors.** Off-by-one, empty collection, missing key, None.
6. **Scope divergence.** Anything in the diff the issue did not ask for.
7. **Test assertions.** Do they assert on schema and invariants, or on generated prose?

Then map each of the issue's safety invariants to the finding that threatens it, or state
that it holds.

For each finding, quote the line and name the invariant at risk. Propose fixes. Update the
checkpoint phase to `REVIEW` with the outcome as the last result.

Do not apply any fix until I say so.
