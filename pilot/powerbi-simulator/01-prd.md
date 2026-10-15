# Requirements baseline: Power BI-Style Analysis Helper

**Status:** review exercise; inferred from the public repository, not an owner-approved roadmap.  
**Date / source revision:** 2026-10-15; public `main` checkout at review time.  
**Labels:** Observed = repository evidence; Inferred = reasonable interpretation; TBD = not established.

## 1. Summary

**Observed:** the repository provides a provider-neutral instruction/skill package for Power BI-style analytics and an optional Python CLI helper that performs constrained inventory, declared-key checks, and simple aggregate calculations on supported files. It is explicitly not Microsoft Power BI and does not run general DAX/M, open PBIX/PBIP, connect to a tenant, render native visuals, or publish reports (`README.md`, `SKILL.md`, `docs/methods-and-limitations.md`).

**Inferred user outcome:** help non-expert builders understand accessible tabular data and plan a simple analytics model/report while making the limits and provenance of calculations clear. This review does not define or approve a future roadmap.

## 2. Users and core journeys

| User/actor | Need | Repository evidence | Success evidence |
|---|---|---|---|
| Non-expert analyst / learner | Ask an AI to explain tables, suggest a semantic model, and outline a report without claiming unsupported Power BI behavior | `README.md`, `SYSTEM_PROMPT.md` | Can follow demo instructions and distinguish observed facts from proposals |
| AI host or coding harness | Load instructions and, when available, run the helper on authorized files | `docs/using-with-llms.md`, `SKILL.md` | Correctly states tool/file access; uses only documented operations |
| Developer/releaser | Run deterministic checks and package an explicit allowlisted source archive | `.github/workflows/tests.yml`, `scripts/build_archive.py`, `release-manifest.txt` | Tests and archive verification pass; source files remain unchanged |

## 3. Scope

**Observed in current repository:** markdown skill/protocols/references/templates, Python CLI scripts, fabricated CSV examples, automated tests, CI test matrix, and a deterministic ZIP archive builder.

**Out of scope per project documentation:** Power BI Desktop/Service parity, tenant access, native visual rendering, general DAX or M execution, PBIX/PBIP parsing, refresh/publish, and arbitrary enterprise-scale calculations.

**Not established:** hosted SaaS/API, multiple tenants, end-user authentication, persistent server-side data, production SLO, paying customers, operating budget, target workload, or live model-provider conformance.

## 4. Functional requirements reflected by current behavior

| ID | Requirement/capability | Evidence/status | Acceptance evidence |
|---|---|---|---|
| FR-01 | Guide an LLM through accessible tabular-data inspection and model/report reasoning | Observed in `SKILL.md` and `SYSTEM_PROMPT.md`; runtime host capability varies | Static instruction review; live model behavior not verified here |
| FR-02 | Inventory supported CSV/TSV/TAB and XLSX sources with bounded, transparent metadata | Observed in `references/companion-runtime.md` and `scripts/analyze.py` | Repository tests and documented limits |
| FR-03 | Audit explicitly declared direct one-to-many keys and compute a constrained aggregate subset | Observed; not a full relationship engine or DAX/M runtime | `tests/` and published smoke-test report |
| FR-04 | Build a Markdown report with aggregate completion status | Observed in `scripts/bi_report.py` | Unit tests; status must be inspected, not equated with exit 0 in tolerant mode |
| FR-05 | Build release archive from explicit approved-file manifest | Observed in `scripts/build_archive.py` and `release-manifest.txt` | Archive tests and release-review documentation |

## 5. Non-functional requirements and gaps

| ID | Attribute | Evidence/target | Confidence | Verification / next evidence |
|---|---|---|---|---|
| NFR-01 | Resource safety for inputs | Observed defaults: 128 MiB per source, 100,000 scanned rows, 256 columns; configurable ceilings documented. These are guardrails, not throughput targets. | High for code/docs | Tests cover boundary/error behavior; representative memory/time benchmark not run |
| NFR-02 | Privacy | Helper docs say source data is not transmitted; samples are opt-in; output can still be sensitive. Host-provider handling varies. | High for documented helper; host path TBD | Review every output and host privacy setting; no live provider used |
| NFR-03 | Portability | CI declares Python 3.10–3.13 on Ubuntu; this review directly ran Python 3.12.3 only. | High for declared matrix, partial runtime verification | Run matrix on CI and test installation guidance across target hosts/OSes |
| NFR-04 | Performance / availability / recovery | No service SLA, latency target, RPO, or RTO found. | TBD / not applicable to current local CLI as service targets | If product becomes hosted, obtain requirements and load/failure data first |
| NFR-05 | Accuracy / engine parity | Explicitly not Power BI parity; limited helper results are deterministic for documented operations but do not validate DAX/M. | High for declared boundary | Independent calculations and real Power BI tests only where relevant |

## 6. Open questions (only for future product changes)

Before converting this local package into a hosted service or adding new capabilities, ask: Is there a real need for hosted execution? Which providers and data-sharing boundaries are required? What scale, latency, retention, reliability, budget, and compliance targets exist? Which operations must be exact? These questions do not block a review of the current local package.

## 7. Approval boundary

This is a read-only architecture pilot. It does not approve edits, new infrastructure, new product claims, or deployment. Any future roadmap and external service require product-owner decisions based on actual demand.
