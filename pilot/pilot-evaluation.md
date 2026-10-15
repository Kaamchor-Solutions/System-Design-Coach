# Pilot evaluation: System Design Coach on Power BI Simulator Skills

**Date:** 2026-10-15  
**Source case:** [Kaamchor-Solutions/PowerBI-Simulator-Skills](https://github.com/Kaamchor-Solutions/PowerBI-Simulator-Skills)  
**Source boundary:** read-only clone; original repository was not modified.  
**Test boundary:** this is a human/agent-applied document pilot and local regression test run, not a live coding-agent provider benchmark.

## Result

**Pilot outcome: PASS for an initial public release, with follow-up validation still needed.** The process produced a complete, grounded design pack and resisted the most obvious overengineering trap. It treated the repository as a provider-neutral instruction package plus an optional bounded local CLI—not as a hosted data platform. It recommended no Kafka, microservices, Kubernetes, database, or horizontal scaling because the inspected evidence supplied no requirement for them.

## Evaluation criteria

| Criterion | Result | Evidence |
|---|---|---|
| Stay within read-only boundary | PASS | Pilot files are separate under this draft; no source file changes or GitHub actions. |
| Inspect implementation, tests, CI, docs, and limits | PASS | Reviewed skill/prompt, helper runtime, analyzer/report-builder/archive entrypoints, representative tests, CI workflow, smoke report, docs and sample output. |
| Separate fact, proposal, inference, and unknown | PASS | All pilot documents label current-state evidence versus proposed decisions; NFR and workload gaps remain TBD. |
| Recommend appropriate complexity | PASS | Recommends local bounded execution and measurement; explicitly rejects speculative Kafka/microservices/Kubernetes. |
| Explain vertical/horizontal scaling and messaging conditionally | PASS | Revisit triggers require measured bottlenecks or future product needs, not “scale just in case.” |
| Deliver requested artifact categories | PASS | PRD-style requirements, HLD, DFD, LLD, ADRs, risk/security/operations/capacity/validation are present. |
| Educate a first-time builder | PASS | Human-readable explanation of why no service/queue is warranted and how to identify future triggers. |
| Avoid invented targets and proof claims | PASS | No SLO, traffic, price, performance, provider privacy, or production claims invented; exact test scope stated. |
| Validate the source case | PASS with stated limits | Target-scoped suite: 86 passed, 89 subtests, Python 3.12.3. No CI matrix, benchmark, or live LLM evaluation. |
| Surface contradictions in source evidence | PASS with follow-up | `analyze.py` pins Decimal rounding to `ROUND_HALF_EVEN` and a test verifies independence from ambient modes, while `docs/methods-and-limitations.md` says the active rounding mode is used. This is recorded as R-06; source files were not changed. |

## Findings and refinements

1. **The design coach needs stronger scoping than a diagram generator.** The pilot confirmed value in identifying what the repository is not (no hosted API/tenant platform) and not filling unknowns with standard-sounding infrastructure.
2. **A “PRD for an existing repository” must be explicitly qualified.** The pilot labels its requirements as inferred from public docs, not approved by maintainers. This distinction is now part of the pack.
3. **Test evidence needs environment and collection scope.** An initial workspace-root pytest call collided with other sibling checkouts; targeting the case repository's `tests/` passed. The draft records both, rather than suppressing the issue.
4. **Portability and user permission must remain explicit.** A pasted repository URL does not guarantee the coding agent can fetch linked references or run code. Public repository creation, code edits, infrastructure, and deployment are distinct from design.
5. **Source evidence can conflict.** The pilot found a rounding-mode mismatch between helper implementation/tests and a limitations document. The new skill should preserve such conflicts as actionable risks, not silently choose or change the upstream behavior.
6. **Ownership must be explicit.** No maintainer follow-up owner was assigned in this read-only exercise; the pilot risk register records this as unassigned rather than inventing an owner.
7. **Post-release validation remains.** The release destination and license are settled: [Kaamchor-Solutions/System-Design-Coach](https://github.com/Kaamchor-Solutions/System-Design-Coach), MIT License. Exercise the skill with an actual supported coding-agent host for linked-reference loading and plain-language teaching; this remains future validation, not a claim already proven by the pilot.

## Overall assessment

This initial public release is not universally validated. The first pilot shows that the document workflow can produce a useful, right-sized design from one mature repository, not that every coding agent will invoke it correctly or consistently. The recorded R-06 rounding discrepancy remains a follow-up against the separate read-only source project and was not fixed by this release.
