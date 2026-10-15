# Pilot: Power BI Simulator Skills repository

**Purpose:** exercise the System Design Coach skill on a real, read-only public repository.  
**Source:** [Kaamchor-Solutions/PowerBI-Simulator-Skills](https://github.com/Kaamchor-Solutions/PowerBI-Simulator-Skills)  
**Review date:** 2026-10-15  
**Boundary:** the source checkout was cloned read-only for inspection and tests; no source files, remote branches, releases, or settings were changed.

This pilot treats the public repository as a product/codebase review. It does not claim the inferred PRD is an approved product brief. The architecture describes the software actually present and distinguishes observed behavior from recommendations. No service, API, database, event broker, cloud deployment, or production traffic model is assumed.

## Documents

1. [Requirements baseline (PRD-style)](01-prd.md)
2. [High-level architecture](02-hld.md)
3. [Data-flow diagram](03-dfd.md)
4. [Low-level design](04-lld.md)
5. [Architecture decisions](05-adrs.md)
6. [Security, operations, risks, and validation](06-operations-risk-validation.md)
7. [Pilot evaluation](../pilot-evaluation.md)

## Evidence reviewed

Repository `README.md`, `SKILL.md`, `SYSTEM_PROMPT.md`, the helper runtime reference and methods/limitations, `scripts/analyze.py`, `scripts/bi_report.py`, archive builder, tests, CI workflow, sample output, release-review and smoke-test documentation. The current checkout's own test suite was run once, scoped to its `tests/` directory. This is a static/repository-level review, not a live model evaluation, performance benchmark, threat-model workshop, or production audit.
