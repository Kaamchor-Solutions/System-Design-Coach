# Architecture patterns: conditional choices, not defaults

Use these as decision prompts, not universal prescriptions. A recommendation is strong only when tied to a requirement and an observable reason.

## Monolith or independently deployed services

- Prefer a **modular monolith** when one team owns a cohesive product, a shared deployment is acceptable, boundaries are still changing, and independent scaling/release is not required. Keep modules and data ownership explicit so extraction remains possible.
- Split into **services** when boundaries are stable and there is a concrete need for independent deployment, isolation, ownership, security, or different scaling/reliability profiles—and the team can handle distributed tracing, network failure, versioned contracts, deployment orchestration, and on-call ownership.
- “We might be big later” is not enough. Identify the domain boundary, independent lifecycle, measured bottleneck, failure-isolation need, or regulatory boundary that makes the extra network and operational complexity worthwhile.

## Vertical or horizontal scaling

- **Vertical scaling** (a larger instance) is often the simplest first step for a single process/store when a measured CPU, memory, I/O, or connection bottleneck is addressed by more capacity. Set a ceiling and watch spend/limits; larger hardware is not infinite or automatically highly available.
- **Horizontal scaling** (more instances) helps when work can be split across instances or when availability requires redundancy. It needs an explicit statelessness/session strategy or shared durable state, load balancing, health checks, concurrency control, and a plan for uneven or hot partitions.
- Scale based on representative load tests and production metrics: resource saturation, queue age/depth, p95/p99 latency, error rate, connection pool pressure, or customer demand. State a threshold and an action. Do not claim capacity from architecture diagrams alone.
- For stateful components, scaling out may require sharding, replication, consistency trade-offs, failover, and recovery tests. Mention those costs, not just “add nodes.”

## Queues and event streams (Kafka included)

Introduce asynchronous messaging when the product actually needs work to continue after the caller returns, smoothing of bursts, retryable work, isolation from a slow dependency, durable buffering, fan-out, or ordered event processing. A queue adds delivery semantics, duplicate handling, poison-message handling, backlog monitoring, replay policy, and operational ownership.

- Choose a simple managed task queue/job table for ordinary background tasks if one consumer path, basic retries, and modest throughput suffice.
- Choose a pub/sub service when events need independent subscribers without long-lived replay/history requirements.
- Consider Kafka or a comparable retained event log when measured event throughput, replay from an offset, long retention, partitioned ordering, or many independent consumer groups justifies the extra cluster/schema/partition/lag operations. Do not recommend it as a generic “scalability layer.”
- Specify at-least-once/exactly-once claims carefully. Design consumers idempotently; define duplicate, ordering, retry/backoff, dead-letter, retention, schema evolution, and reconciliation behavior.
- Avoid a queue when synchronous completion is part of the user contract, async processing creates confusing partial states, or a database transaction/outbox and worker is sufficient.

## Data store and cache

- Prefer a relational database when entities have relationships, transactions, constraints, and flexible queries. Prefer document/key-value stores for access patterns and data shape that match their consistency and query limits; explain how query/index patterns and migration will work.
- Separate operational data, analytical data, and blobs only when workload/lifecycle/access requirements justify it. Identify source of truth and which copies can be rebuilt.
- Add a cache only after identifying the expensive repeated read, freshness tolerance, invalidation/expiry strategy, stampede behavior, privacy boundary, and metric that proves it helps. Cache is not a durable source of truth by default.
- State backup, restore testing, retention/deletion, encryption/key management, residency, consistency, and migration plan. “Database is managed” does not answer these questions.

## Security, tenancy, and resilience

- Choose authentication and authorization based on user/tenant roles, data classification, and threat model; do not infer compliance obligations from sector alone.
- Treat identity boundaries, secret storage/rotation, audit events, input validation, rate limits, dependency timeouts, least privilege, tenant isolation, and data deletion as first-class design concerns.
- Use retries only for transient errors and with deadlines, bounded backoff/jitter, idempotency, and a budget. Add circuit breakers or bulkheads only where failure isolation is needed and can be observed/tested.
- Set SLO, RPO (acceptable data loss window), and RTO (acceptable recovery time) from actual product needs. Backups are not proven until restore is tested.

## Every recommendation must state

1. The requirement/evidence it addresses.
2. The simplest viable option and at least one material alternative when a meaningful trade-off exists.
3. Operational, cost, security, and failure-mode consequences.
4. The assumptions and confidence level.
5. The metric, threshold, or change in product/team needs that would justify revisiting it.
