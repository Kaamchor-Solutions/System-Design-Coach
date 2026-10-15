# Design workflow and evidence handling

Use this reference for substantial projects. Keep small scripts and low-risk features concise; do not produce documents merely to fill a checklist.

## 1. Establish an evidence baseline

### Existing repository

Inspect what is available and relevant: README/user journeys, source entry points, languages/frameworks, dependency manifests, APIs, persistence, queue/cache usage, auth boundaries, deployment/infrastructure manifests, CI, tests, observability, and release process. Search before assuming a technology is absent. Prefer narrow reads over scanning secrets, generated data, or irrelevant large files.

For every important statement, classify it:

- **Observed:** directly supported by code, config, test, documentation, or a user statement; identify the path/source.
- **Inferred:** likely but not directly confirmed; state the reasoning and confidence.
- **Proposed:** target-state design, not current implementation.
- **Unknown:** not discoverable from permitted access; say how it affects the design and how to answer it.

Never interpret a README promise as proof that runtime behavior works. Prefer code/tests and label documentation-only claims accordingly. A static inspection does not prove performance, production operation, data privacy across the model provider, or live cloud configuration.

### New product or feature

Start with the actor, job-to-be-done, current workaround, happy path, failure path, and definition of success. Capture scope, out-of-scope behavior, constraints, supported clients/regions, integrations, ownership, and lifecycle (build, operate, retire). Ask only a few questions at a time and prioritize answers that change the design.

## 2. Baseline the workload and NFRs

Request useful ranges, not false precision:

- users/tenants, active concurrency, requests or events per second (average, peak, burst duration), payload sizes, read/write mix, and growth horizon;
- latency goals (including percentile), availability window, consistency expectations, and acceptable data loss or recovery time;
- data sensitivity, residency/retention/deletion obligations, access roles, and audit needs;
- team skill/size, operational coverage, deployment constraints, budget range, and external dependencies.

For every NFR, record its source, confidence, target or `TBD`, and verification method. A value from a standard or prior design is not automatically the user's target. If key numbers are unavailable, present a conservative first-release assumption plus a sensitivity range and a test/measurement plan. Do not claim the system can meet an unmeasured target.

## 3. Bound the solution space

First find the smallest design that satisfies the confirmed requirements. Compare alternatives only where the decision is consequential. A useful comparison records: requirement fit, user/developer impact, failure modes, data consistency, security boundary, operational skill/on-call load, cost drivers, migration/exit cost, and conditions to revisit.

Prefer incremental evolution: start with a modular monolith or single-process tool when appropriate; introduce independently deployed services, queues, or caches only to solve a named problem. Record both what is needed now and the evidence that would justify a later change. Avoid making a future-scale assumption part of the first release without an explicit requirement.

## 4. Draw system and data views

- **Context/HLD:** people and external systems, product boundary, main components and protocols, identity boundary, and key stores.
- **DFD:** sources, processors, stores, actors, sensitive data, trust boundaries, and labeled flow direction/protocol. Call out retention, deletion, backups, and any third-party/model-provider processing.
- **Sequence/LLD:** important use case with validation, auth, success response, error/timeout/retry paths, idempotency, and state changes.

Keep the diagram proportional to complexity. Use Mermaid when the target can render it, make diagram labels readable, and check every component and edge against the prose. A diagram is a model, not proof of an implementation.

## 5. Produce actionable detail

For each service/module define responsibility, owner, inputs/outputs, data ownership, interfaces and versions, authorization, error contract, retry/idempotency behavior, rate/resource limits, dependencies, and deployment boundary. For data define entity/table grain, keys, constraints/indexes, consistency/transaction needs, schema migration/backfill and rollback. State validation, observability signals, release/rollback, backup/restore, and disaster recovery as actual proposed runbooks or mark them TBD.

Keep an assumptions/open-questions list. Assign each important risk an evidence-based likelihood/impact rationale, mitigation/owner, leading signal, and fallback. Distinguish verified behavior from a design proposal and from a future test.

## 6. Make the human handoff useful

Lead with the recommended option and why it is proportionate. Explain acronyms in one line. State what will happen if the system grows beyond its current design, including the metric or operational signal that triggers change. Keep alternatives available, note what is deliberately deferred, and make decisions needing user input explicit rather than burying them in prose.
