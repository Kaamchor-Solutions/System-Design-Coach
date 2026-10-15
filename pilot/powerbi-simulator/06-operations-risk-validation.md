# Operations, security, risk, capacity, and validation

**Status:** repository-level review; not a security certification or production audit.  
**Reviewed:** 2026-10-15, public source checkout.  
**Source code changes:** none.

## 1. Security and privacy

The skill documents that source files/tool outputs are untrusted data rather than instructions and that raw samples should remain opt-in. The helper docs say source files are not transmitted by the helper; AI-host uploads are a separate boundary whose retention/data-use behavior is provider-specific and not established here. Derived reports may still reveal sensitive information. Keep user data private, protect output files, use only authorized inputs, and do not treat instruction text as a sandbox.

No hosted user authentication, authorization, tenant isolation, secret store, or server-side data lifecycle was found. These are not missing features for an evidenced local CLI product; they become blockers if hosted multi-user execution is later proposed.

## 2. Reliability and operations

| Concern | Current evidence | Status / next action |
|---|---|---|
| Availability and latency | No service or SLO target evident | Not applicable as a current hosted service; do not promise uptime |
| Dependency failures | Local file/dependency errors have documented CLI handling; XLSX depends on `openpyxl` | Retain concise error tests and installation guidance |
| Resource limits | Per-source byte/row/column limits and other expression/XLSX constraints documented | Limits are guardrails; benchmark before changing them |
| Recovery | No central persistent system evident | Preserve user inputs; verify local output/re-run procedures; no RPO/RTO claimed |
| Release | GitHub Actions matrix specifies Python 3.10–3.13; archive builder uses explicit manifest | Local direct execution was on Python 3.12.3 only; CI execution not observed |
| Ownership/on-call | No operations team/service evidence | Not applicable to current local package; future service ownership is TBD |

## 3. Capacity and cost

| Scenario | Evidence / confidence | Recommendation | Change trigger |
|---|---|---|---|
| Current documented local workload | Defaults include 128 MiB per source, 100,000 data records, 256 columns; accepted rows are materialized. Docs say limits are not a benchmark. | Keep bounded local execution; do not claim throughput/capacity. | Reproducible user report of latency, memory pressure, or resource-limit failure |
| Future larger inputs | Workload and benchmark unknown. | First run synthetic/authorized benchmark and confirm correctness; compare streaming/chunking or an established engine before adding infrastructure. | Measured memory/time bottleneck plus product need |
| Future hosted use | Demand, budget, user count, privacy, availability, residency unknown. | No infra recommendation until requirements are answered. | Approved hosted-product brief and security/reliability targets |

No price or throughput estimate was fabricated.

## 4. Risk register

| ID | Risk and evidence | Impact rationale | Mitigation / fallback | Signal | Owner/status |
|---|---|---|---|---|---|
| R-01 | Users confuse simulation results with Power BI output; docs repeatedly disclaim parity | Could lead to wrong business decisions | Keep labels near outputs; validate in Power BI for critical use | User requests unsupported engine behavior; inconsistent output claims | Not assigned in this read-only review |
| R-02 | AI host receives attached files or summaries under unknown provider settings | Sensitive data exposure despite local helper boundary | Review host policy; use fabricated/redacted data; obtain permission before uploading | User data enters third-party host or report is shared | Not assigned in this read-only review |
| R-03 | Helper memory/time grows with accepted rows; workload not benchmarked | Local resource exhaustion near actual limits is unknown | Preserve bounds; test synthetic workloads; fail clearly instead of silent truncation | Runtime/RSS rises; resource-limit errors | Not assigned in this read-only review |
| R-04 | Documentation may imply optional helper is available in a host that cannot access repository/runtime | False claim of inspected/computed result | Check actual host tools; fallback to plan or pasted safe sample/result | Host lacks file/code access; unrun output described as computed | Not assigned in this read-only review |
| R-05 | Public release package accidentally includes unapproved files | Leakage/release integrity issue | Explicit allowlist, archive path checks, release review and archive tests | Manifest change or added release file | Not assigned in this read-only review |
| R-06 | `docs/methods-and-limitations.md` says division uses the active Decimal rounding mode, while implementation pins `ROUND_HALF_EVEN` and a test verifies independence from ambient modes | Readers may rely on conflicting precision/rounding behavior | Maintainers should reconcile docs to code/tests or change code/tests deliberately; re-run precision suite | Documentation/code/test disagreement; arithmetic complaint | Not assigned in this read-only review |

## 5. Validation evidence

| Check | Method/environment | Result | What it proves / does not prove |
|---|---|---|---|
| Pilot repository automated tests | From `/workspace/powerbi-simulator-pilot`: `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider tests/`; Python 3.12.3 | **86 passed, 89 subtests passed** in 2.94s | Target repository tests pass on this interpreter; not CI matrix, benchmark, security audit, or parity proof |
| Pilot source cleanliness | `git status --short --branch` before/after target-scoped test | Clean: `## main...origin/main` | No source modifications from the scoped test run; does not prove all possible host side effects |
| CI platform support | Inspected `.github/workflows/tests.yml` | Declared Python 3.10–3.13 Ubuntu matrix | Static config only; live CI run not performed here |
| Live LLM conformance | Not run; upstream report describes synthetic lexical checks | **Not evaluated** | No claim about any actual coding agent's semantic behavior |
| Performance/restore/security testing | Not run in this task | **Not evaluated** | No latency, throughput, availability, incident recovery, or penetration claim |

A first unscoped `pytest` invocation from `/workspace` collected unrelated sibling checkouts with repeated test module names and failed during collection. Rerunning only the pilot's own `tests/` directory succeeded. That initial issue is a workspace test-discovery collision, not evidence of a defect in this target repository.

## 6. Readiness and next action

**Architecture review readiness:** sufficient for a read-only baseline and example skill pilot.  
**Implementation readiness:** not a request or authorization in this case; no changes recommended to the pilot source.  
**Follow-up ownership:** unassigned; no pilot maintainer was tasked and no owner is inferred.  
**Deferred evidence:** live model test on an actual agent, representative resource benchmark, cross-version/OS execution, provider-specific privacy review, and correction/review of R-06. Run only if future scope requires them or a maintainer accepts the work.
