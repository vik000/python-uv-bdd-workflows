---
description: Safety check of the last commit. Applies nothing.
---

Read DESIGN-slice<n>.md for the current branch. Inspect the diff of the last commit.

Print one line per heading: the heading, then ok, or the problem with file and line.

FAILURE DIRECTION   on bad input or error, does the default land safe or convenient?
UNCERTAINTY PATH    can it say "I don't know", or is it forced to guess?
SWALLOWED ERRORS    anything caught and continued without a decision
UNVALIDATED OUTPUT  model output used before checking it
BOUNDARY            empty, None, missing key, off-by-one
SCOPE               anything in the diff the design did not ask for
ASSERTIONS          do tests check structure and rules, or generated text?

Then one line per rule from "what must never happen": <rule> holds, or <rule> AT RISK: reason

Then fixes as a numbered list, one line each. Apply nothing. No prose.
