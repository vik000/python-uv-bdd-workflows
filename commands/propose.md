---
description: Propose slices as a short table. A suggestion, not a plan.
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

Slice 1 must be the thickest: the single capability closest to what the brief actually
asks for. Later slices add behaviour to it, never assemble it.

Propose three to five such slices. Print ONLY a table, nothing before or after:

| # | Slice | Input -> Output | Riskiest thing |
|---|-------|-----------------|----------------|

Rules for the table:
- Slice name: a behaviour, five words maximum. Not a noun phrase for a component.
- Input -> Output: concrete, one short line, real values. No prose.
- Riskiest thing: what could go wrong, six words maximum.
- The whole table must be readable in under sixty seconds.

Then one line, exactly this:
These are suggestions. Tell me what to change, drop or add.

Create nothing. Write no files. Do not defend the proposal or explain your reasoning
unless asked.
