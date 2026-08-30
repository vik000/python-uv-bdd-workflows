# Issue schema

Use one issue for one independently verifiable version increment.

## Quality rules

- State observable outcomes, not implementation instructions, unless an implementation constraint is
  genuinely required.
- Define both in-scope and out-of-scope behaviour.
- Make assumptions visible and falsifiable.
- Express acceptance criteria as concrete Given/When/Then scenarios.
- Include at least one failure, uncertainty or invalid-input scenario when the feature accepts input.
- Add safety invariants separately from ordinary acceptance criteria.
- Require every test category to be assessed; permit `N/A` only with a reason.
- Reserve a traceability section for the injected issue number and pytest marker.
- Declare semantic-version impact. Default to patch.

## Vertical slicing

Prefer issues that cross the minimum required boundaries to produce a useful behaviour. Avoid issues
such as “create database,” “add service layer,” or “write API” when none is independently valuable.

A good issue can be explained, tested, implemented, reviewed and versioned without depending on an
unmerged sibling issue.

## Acceptance criteria

Use deterministic statements. Avoid “works correctly,” “handles errors,” “is secure,” or “supports
all cases.” Identify specific inputs, state, outputs, side effects and prohibited outcomes.

## Safety invariants

Describe properties that must remain true across valid, invalid and degraded conditions. Examples:

- Uncertain clinical classification is never silently treated as low risk.
- An authorization failure never reveals whether a patient record exists.
- A timed-out dependency never produces fabricated clinical data.
- Repeated delivery of the same event never duplicates a clinical action.

The issue must not claim these are guaranteed merely because their tests pass.

