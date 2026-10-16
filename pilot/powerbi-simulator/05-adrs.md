# Architecture decision records: pilot review

These are review observations and proposals, not owner-approved roadmap decisions. Current design choices are labelled **Observed**; recommendations are **Proposed**.

## ADR-01: Keep the product portable and provider-neutral

- **Status:** Observed design choice; retain recommendation proposed.
- **Context:** `SKILL.md`, `SYSTEM_PROMPT.md`, and `docs/using-with-llms.md` describe use across different AI hosts and state that actual file/code access varies.
- **Decision:** Keep the instructions and helper separable; do not bind the whole product to one provider API without user evidence.
- **Alternatives:** Provider-specific plugin/extension. It might improve integration in that host but narrows reuse and may require additional permissions/API maintenance.
- **Consequences:** Provider-neutral documentation is portable but cannot promise every host will load all files or run the helper.
- **Reversibility / exit:** A future host adapter can remain optional, leaving the provider-neutral core intact. Do not claim the adapter works on a host until tested there.
- **Validation:** Test the install/use workflow on specific target hosts; live model-provider conformance was not run in this pilot.
- **Revisit trigger:** Repeated user demand for an integration and a documented host permission/data policy.

## ADR-02: Keep deterministic analytics local and bounded

- **Status:** Observed design choice; retain recommendation proposed.
- **Context:** `scripts/analyze.py` implements a constrained set of file checks and calculations; docs explicitly disclaim DAX/M execution and Power BI parity.
- **Decision:** Retain the small deterministic helper for supported local workflows, with input guardrails and explicit error/result contracts.
- **Alternatives:** Depend on the real Power BI engine or a broader analytics engine for parity/scale. Those have different installation, licensing, data, and host requirements and are not implied by this repository.
- **Consequences:** The helper remains understandable/reproducible for its subset; unsupported work must be labelled uncomputed or run in a compatible authorized environment.
- **Reversibility / exit:** Keeping the helper optional and local limits commitment. Replacing it later is easier while callers retain a stable request/result contract; broader schemas or engine dependencies would add migration and licensing costs.
- **Validation:** Local tests passed as detailed in the operations/validation file; independent benchmark and real Power BI validation not run in this task.
- **Revisit trigger:** Documented user workload/feature requirements exceed the supported subset or measured performance envelope.

## ADR-03: No database, queue, or service for the current repository

- **Status:** Proposed recommendation based on observed scope; no new component added.
- **Context:** Inspected entrypoints are local CLIs and instruction files; no hosted service, persistent user state, asynchronous product job, multi-consumer stream, or tenant scale requirement was found.
- **Decision:** Do not add a service, DB, queue, Kafka, or orchestration platform for the current package.
- **Alternatives:** A hosted API with database and background tasks could enable central execution, but adds authentication, tenancy, privacy, retention, monitoring, operations, reliability, and cost obligations.
- **Consequences:** The current local workflow remains simpler and host/user-controlled; it will not offer centralized execution or service-level guarantees.
- **Reversibility / exit:** This choice remains easy to revisit while no hosted user state exists. Adding persistent state later would create migration, retention, and deletion obligations; validate an approved hosted need before accumulating that commitment.
- **Revisit trigger:** Approved hosted-product requirements with data boundaries, demand, workload, SLO, staffing, budget, and compliance clarified.
