# Low-level design: current helper package

**Status:** current-state repository review, not a proposed rewrite.  
**Date/source:** 2026-10-15; files in the public checkout.  
**Limit:** no changes made to application code.

## 1. Modules and boundaries

| Module | Responsibility | Inputs/outputs | Evidence |
|---|---|---|---|
| `SKILL.md`, `SYSTEM_PROMPT.md` | Provider-neutral workflow, trust boundary, capability limitations | User task/context → instructions for an LLM | Source files; live model not tested |
| `protocols/`, `references/` | Task-specific procedures and helper JSON/runtime contract | Linked Markdown | Static repository review |
| `scripts/analyze.py` | Validate JSON request, load supported files, inventory/audit/aggregate, format JSON/Markdown | Config + referenced files → result object/output | Source; tests |
| `scripts/bi_report.py` | Execute multiple requests, collect per-analysis status, write Markdown report | Request JSON → report file and status | Source; tests |
| `scripts/build_archive.py` | Read explicit release manifest, reject unsafe paths/symlinks, build deterministic ZIP | Source files → ZIP and digest | Source; tests and smoke report |
| `tests/` and `.github/workflows/tests.yml` | Unit/contract/conformance checks on CI matrix | Synthetic fixtures → pass/fail | Static review; local suite executed on Python 3.12.3 |

## 2. Analyzer interface and data behavior

The JSON request supports `inventory`, `model_audit`, and `aggregate` actions. Input files are CSV, TSV/TAB, and XLSX; XLSX is read from cached cell values, not recalculated formulas. Relationship audits cover only explicitly declared direct one-to-many key uniqueness/referential integrity. Aggregates implement a finite listed set of operations, filters `eq`/`neq`/`in`, and restricted arithmetic expressions; general Python evaluation is not used for expressions.

Validation checks unknown fields/types and duplicate JSON keys before source loading; structured errors include stable codes/paths for documented classes. Sampling is opt-in and limited. The helper defines per-source byte/row/column limits, with configurable maxima; XLSX uncompressed size, expression length/AST, decimal token, and arithmetic precision also have hard bounds. These bounds prevent unbounded inputs in documented cases but do not constitute a sandbox against hostile local processes or a throughput benchmark.

## 3. Report semantics

`bi_report.py` creates a Markdown report. In tolerant mode it can return exit code 0 even when the report status is PARTIAL/FAILED; consumers must inspect the status and per-analysis results. `--fail-on-invalid` exits 2 unless the report is complete and non-empty. Report writes and archive writes include safety checks described by source/docs. Never infer “all analyses succeeded” from “file written” alone.

## 4. Dependencies and execution

CSV/TSV paths use Python standard library; XLSX requires `openpyxl` from `scripts/requirements.txt`. The helper is a local synchronous command-line process in the documented usage. No API server, job queue, persistent database, authentication service, or central session state is evident in the inspected code. The calling host may or may not have repository/file access and an execution runtime.

## 5. Failure and validation paths

Expected request/file errors produce structured results or concise CLI errors; the report builder records per-analysis outcomes. A model audit with invalid integrity state must not be treated as a trustworthy aggregate. Resource-limit errors fail rather than silently truncate.

**Rounding evidence rechecked 2026-10-17 at upstream main `6ba6cced33af1c910b98885c306c879c2a69863f`:** [`_with_decimal_context` in `analyze.py`](https://github.com/Kaamchor-Solutions/PowerBI-Simulator-Skills/blob/6ba6cced33af1c910b98885c306c879c2a69863f/scripts/analyze.py#L519-L540) pins division/mean arithmetic to `ROUND_HALF_EVEN`; the [ambient-mode regression test `test_division_is_independent_of_all_ambient_rounding_modes`](https://github.com/Kaamchor-Solutions/PowerBI-Simulator-Skills/blob/6ba6cced33af1c910b98885c306c879c2a69863f/tests/test_analyze.py#L440-L452) passes (1 test, 8 subtests). The [methods page](https://github.com/Kaamchor-Solutions/PowerBI-Simulator-Skills/blob/6ba6cced33af1c910b98885c306c879c2a69863f/docs/methods-and-limitations.md#L16) says division uses the active Decimal rounding mode (half-even by default). A normal standalone command-line run uses half-even, so this is not evidence that its default results are wrong. An embedded caller means another Python program importing the helper; it may set a custom Decimal context (Python's numeric precision and rounding settings), but this helper overrides the rounding setting. The mismatch concerns the documented contract for such callers, not proof of incorrect default output. The source checkout remains unchanged in this read-only pilot.

Other tests cover malformed requests, file edge cases, precision, output safety, and fabricated-data behavior. None of these imply DAX/Power BI parity or production-scale capacity.

## 6. Recommended next checks (not executed)

Benchmark representative synthetic input sizes while measuring runtime and peak RSS; verify every currently documented command on the supported Python matrix; exercise install instructions on the intended AI/coding hosts; and inspect/validate host-provider privacy behavior separately. Do not use confidential customer data for a benchmark or public fixture.
