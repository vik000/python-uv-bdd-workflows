---
description: Propose slices as a short table, ordered PoC first. A suggestion, not a plan.
---

Read BRIEF.md, or use $ARGUMENTS as the brief.

A slice is VERTICAL. It runs end to end on its own and produces a visible result with no
other slice built. Never split by layer, step, phase, or stage of one operation.

Test every candidate slice against all four. Discard any that fails:

1. Could I demonstrate this alone, with nothing else built?
2. Does it take real input and produce real output a person can see?
3. If I deleted every other slice, would this still do something useful?
4. Is it a behaviour, not a component?

Wrong - these are steps of one function, not slices:
  validate input / build the lookup map / sort the list / handle edge cases

Right - each runs alone and adds visible behaviour:
  sort a queue by priority / reject invalid priorities / tie-break oldest first

Classify every slice as exactly one of:
- PoC     the capability the brief actually asks for. Usually one slice, at most two.
          Building only these must produce a working demonstration.
- HARDEN  makes the capability trustworthy: validation, immutability, determinism,
          boundaries, failure behaviour.

Order the table PoC first, then HARDEN by descending risk.

Print ONLY the following, nothing else.

First, exactly two lines:

PROPOSAL  <one sentence: what the PoC does, in plain words>
POC       slice(s) <n>, then <n> hardening slices

Then the table:

| # | Type | Slice | Input -> Output | Riskiest thing |
|---|------|-------|-----------------|----------------|

Rules for the table:
- Type is PoC or HARDEN.
- Slice name: a behaviour, five words maximum. Not a noun phrase for a component.
- Input -> Output: concrete, one short line, real values. No prose.
- Riskiest thing: what could go wrong, six words maximum.
- Three to five rows. Readable in under sixty seconds.

Then:

GAPS
<what the brief leaves unanswered, or what these slices do not cover. One line each,
three maximum. If none, write "none".>

NEXT
<what would come after these slices, one line each, three maximum.>

Then one line, exactly this:
These are suggestions. Tell me what to change, drop or add.

Create nothing. Write no files. Do not defend the proposal or explain your reasoning
unless asked.
