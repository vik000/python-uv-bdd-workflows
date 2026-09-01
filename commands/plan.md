---
description: Review one issue's test plan and safety invariants before any code
---

Use the python-uv-gh-workflow skill.

Read issue $ARGUMENTS with the bundled workflow script. Do not work from memory or
from anything summarised earlier in this session.

Show me, and nothing else:

1. Objective and scope, in one line each.
2. Every acceptance criterion, as Given/When/Then.
3. Every safety invariant.
4. The test strategy: which categories are exercised, and for each marked N/A, the
   stated reason.
5. Any acceptance criterion or invariant with no corresponding test category — call
   these out explicitly as gaps.

Then stop. Do not branch, register markers or write tests. Wait for my approval.
