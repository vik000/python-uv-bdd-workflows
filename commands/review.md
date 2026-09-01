---
description: Inspect the last change against the issue's safety invariants
---

Use the python-uv-gh-workflow skill.

Review the code written since the last commit against the current issue's safety
invariants. Report against each of these explicitly — say "none found" where that is
true rather than omitting the heading:

1. **Failure direction.** On parse failure, timeout, empty input or model refusal, does
   the default land on the safe side or the convenient side?
2. **Uncertainty path.** Can the system express that it does not know, or is it
   structurally forced to guess?
3. **Swallowed exceptions.** Anything caught and continued without a decision.
4. **Unvalidated model output.** Anything used before it is validated.
5. **Boundary errors.** Off-by-one, empty collection, missing key, None.
6. **Scope divergence.** Anything in the diff the issue did not ask for.
7. **Test assertions.** Do they assert on schema and invariants, or on generated prose?

For each finding, quote the line and state which invariant it threatens. Propose fixes.
Do not apply them until I say so.
