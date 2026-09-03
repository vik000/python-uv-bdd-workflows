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

First, exactly seven lines. Each strictly one line, no wrapping, no prose:

PROPOSAL  <what the PoC does, in plain words, one sentence>
SHAPE     <what it physically is: importable module, CLI script, local service. State what it is NOT: no I/O, no persistence, no network. Say how it is exercised: pytest, command line, HTTP call.>
COVERS    <the functionality these slices deliver, comma separated, four items maximum>
EXCLUDES  <what a reasonable reader might expect but will not get, comma separated>
APPROACH  <how it works mechanically: the key data shape and the key operation>
DEMO      <the call and what comes back: signature -> result>
POC       <which slice(s) are the PoC, and how many hardening slices follow>

SHAPE decides the smallest artefact that demonstrates the capability. Default to an
importable module exercised by tests unless the brief demands otherwise. Never propose a
service, API or persistence layer the brief did not ask for.

APPROACH must name the actual mechanism, not restate the goal. Say "map labels to ranks,
sort by (rank, timestamp) on a copy", not "sorts requests correctly". If I cannot picture
the implementation from that line, it is not specific enough.

EXCLUDES is not a list of everything absent. It is the two or three things a reader would
otherwise assume are included.

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
