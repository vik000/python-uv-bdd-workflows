# Risk-based pytest strategy

Select the broadest evidence appropriate to the behaviour and risk. Every category in the issue must
be `Required` or `N/A — <specific reason>`.

## Behavioural evidence

### BDD acceptance tests

Exercise each Given/When/Then criterion through the most representative stable boundary. Mark every
issue-owned acceptance test with `@pytest.mark.issue_<number>`.

### Unit tests

Cover decision logic, calculations and transformations with small deterministic tests. Avoid testing
private implementation details when a stable public behaviour is available.

### Boundary-value and limit-transition tests

Identify every constrained dimension and test immediately below, exactly at and immediately above its
meaningful limits. Include zero/one/empty, minimum/maximum, inclusive/exclusive cutoffs, collection and
payload sizes, pagination ends, numeric precision and overflow, date/time cutoffs, time zones and DST
transitions when applicable. Use equivalence partitions to select representative interior values.

### Edge and corner-case tests

Test rare but valid combinations that are not necessarily limits: duplicate or reordered events,
simultaneous actions, repeated calls, partial optional data, unusual Unicode, stale state, empty-but-
valid collections, single-element collections, cross-field interactions, ambiguous values and legal
state sequences that are unlikely in the happy path. Distinguish these from malformed or prohibited
inputs so valid unusual behaviour is not accidentally rejected.

### Negative and malformed input

Test missing, corrupt, contradictory, unauthorized, stale and unexpected input. Assert explicit
failure behaviour and absence of unsafe side effects.

### Property-based tests

Use generated examples for parsers, transformations, numerical logic, serialization and invariant-
heavy code. State the property before choosing a generator. Retain discovered failures as examples.

### State-transition and invariant tests

Cover every permitted transition, rejected transition, terminal state and invariant across sequences.
Use model-based tests when state combinations are large.

## Boundary evidence

### Contract and schema tests

Verify request/response schemas, required fields, compatibility, error contracts and serialization.
Pin external examples or schemas when they are the source of truth.

### Integration tests

Exercise real adapters against controlled dependencies when mocks cannot prove configuration,
transaction, persistence or protocol behaviour.

### Concurrency and idempotency

Test duplicate delivery, races, ordering, cancellation, retries and atomicity where work may overlap.

### Resilience

Inject timeouts, partial failure, rate limits and unavailable dependencies. Assert bounded retries,
observable failure and fail-safe behaviour.

### Security, authorization and privacy

Test role and ownership boundaries, object-level access, input handling, secret redaction, audit events
and absence of sensitive information in errors or logs. Security tooling does not replace threat
modelling or specialist review.

## Confidence gates

### Regression

Run the complete suite after focused tests. Treat newly flaky tests as failures requiring diagnosis.

### Coverage

Use statement and branch coverage to find unexecuted decisions. Prefer 100% coverage of newly added
risk-bearing branches when practical, but never optimize assertions merely to reach a percentage.

### Mutation testing

Use mutation testing for concentrated business and safety logic. Investigate surviving mutants;
exclude only equivalent or irrelevant mutants with recorded justification.

### Static evidence

Run the project's formatter/linter, type checker, dependency audit and security scanner when present.
Record exact commands and versions so results are reproducible.

## Traceability

Maintain an acceptance-criterion/safety-invariant to test mapping in the issue. A test can carry more
than one issue marker when it provides genuine shared regression evidence, but do not relabel unrelated
tests to inflate issue coverage.

Passing tests demonstrate evidence under tested conditions. They cannot guarantee safe behaviour in
all operating conditions or replace intended-use validation and risk management.
