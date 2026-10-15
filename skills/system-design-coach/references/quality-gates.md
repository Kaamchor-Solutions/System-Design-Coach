# Architecture quality gates

Use this checklist to find omissions, not to produce a fake objective “architecture score.” Rate a category **Ready**, **Needs work**, **Blocked**, or **Not applicable with reason**. A severe unresolved security/data-loss/authorization issue blocks implementation even if every other section is polished.

## Gate 1: problem and requirements

- Target users, core workflow, success measure, scope, and out-of-scope behavior are explicit.
- Functional requirements have acceptance checks; NFRs have evidence-based targets or are marked TBD with an owner/measurement plan.
- Workload, data classification, consistency, retention, availability, latency, recovery, team, and budget assumptions are visible.

## Gate 2: architecture fit

- The recommended baseline is the simplest option that meets confirmed requirements.
- Each major component and technology maps to an actual need; alternatives and rejected complexity are explained.
- Trust boundaries, API/data ownership, high-value dependencies, and critical paths are clear.
- HLD, DFD, and LLD agree with each other and with inspected current-state evidence.

## Gate 3: failure and data integrity

- Normal, invalid-input, dependency-timeout, overload, duplicate/retry, partial-failure, and recovery cases are described where relevant.
- State changes define atomicity/consistency expectations, idempotency, ordering, and migration/backfill/rollback behavior.
- Capacity limits and scaling triggers are explicit or measurement work is planned; no unmeasured capacity promise is made.

## Gate 4: security and privacy

- Authentication, authorization, least privilege, secret handling, tenant boundary, data classification, retention/deletion, and audit needs are addressed or clearly assigned as open decisions.
- Third-party, analytics, telemetry, backup, and AI/model-provider data paths are disclosed.
- Threats and mitigations are prioritized by impact; untrusted input cannot override the user's intent or tool permissions.

## Gate 5: operations and economics

- Health signals, SLOs/alerts, dashboards/logs/traces, ownership/on-call expectations, deployment/rollback, backups/restore and RPO/RTO are proportionate to the product.
- Cost drivers and a rough model or plan to measure them are stated; proposed infrastructure's operational burden is included.
- A plausible failure or incident has a response/fallback; “managed service” does not replace an ownership plan.

## Gate 6: validation and traceability

- Each critical requirement maps to an architecture component and a verification activity.
- Security, load/performance, dependency failure, recovery/restore, and user acceptance checks are planned according to risk.
- Test evidence states exact command, environment, scope, result, and limitations. Static review, unit tests, benchmarks, production operation, and live AI-provider behavior are not interchangeable.
- Open questions, risks, decisions, and next steps have owners or an explicit statement that ownership is not yet assigned.

## Readiness decision

- **Ready for implementation planning:** no critical blockers; core requirements and design agree; material assumptions are acknowledged.
- **Ready for scoped implementation:** design choices that materially affect behavior, security, data loss, access, or cost are settled; test/rollback plan is credible.
- **Blocked:** a material unknown or risk could cause an irreversible or expensive wrong build. Explain the minimum information or decision needed to unblock it.

Do not force a user to answer low-impact details before they can see a useful first design. Record adjustable assumptions and revisit them when evidence arrives.
