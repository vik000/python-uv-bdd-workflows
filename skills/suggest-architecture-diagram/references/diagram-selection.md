# Diagram selection

Choose the smallest view that answers the immediate design question.

| Dominant question | Primary Mermaid view | Emphasize |
|---|---|---|
| What are the system boundaries and responsibilities? | `flowchart` | Actors, containers, stores, external systems, trust boundaries |
| What happens during one request or agent run? | `sequenceDiagram` | Ordering, ownership, timeouts, retries, escalation |
| Which transitions are valid? | `stateDiagram-v2` | Events, guards, invalid and terminal states |
| How is durable information related? | `erDiagram` | Identity, cardinality, retention-sensitive records |
| Where does software run? | `flowchart` grouped by deployment zone | Runtime zones, networks, secrets, observability |

## Selection rules

- Prefer a boundary/container flowchart for a broad feature specification.
- Prefer a sequence diagram when failures or agent/tool interactions are the main uncertainty.
- Prefer a state diagram when requirements use statuses, events, approvals or escalations.
- Prefer an ER diagram only when data ownership and relationships drive the design.
- Do not start with deployment unless placement, latency, residency or isolation is a stated constraint.

## Cognitive-load rules

- Keep the primary diagram near 5–12 nodes.
- Use subgraphs for trust zones or responsibility boundaries, not decorative grouping.
- Put requirement or issue IDs in short node/edge labels where they provide traceability.
- Show the primary happy path and the most important fail-safe path.
- Omit framework names unless the specification constrains them.
- Put detailed alternatives and unresolved questions outside the diagram.

## Safety-relevant systems

Make uncertainty, human review, authorization, audit and failure states visible when applicable. Use a
neutral “safe fallback” or “human escalation” node rather than implying an automated decision is
clinically authoritative. A diagram is a reasoning aid, not assurance evidence.

