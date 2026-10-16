# Architecture-pack guide

Use this folder as a starting point for a project-specific design pack. Copy the relevant files into a clearly named location in the target project (for example, `docs/system-design/`) only if the user authorized file creation there. Keep the pilot/read-only output separate from the original repository. Replace bracketed prompts, remove genuinely irrelevant sections with a brief reason, and link related decisions rather than duplicating conflicting facts.

## Recommended files

| File | Purpose |
|---|---|
| `quick-start.md` | Plain-language, one-page design note for an early idea or small, low-risk change |
| `quick-start-example.md` | Fictional worked example of the compact note, including facts, assumptions, data flow, and limits |
| `01-prd.md` | Problem, users, requirements, acceptance, constraints, measurable NFRs |
| `02-hld.md` | Context and component architecture, choices, boundaries and alternatives |
| `03-dfd.md` | Data sources, flows, stores, processors, trust boundaries and lifecycle |
| `04-lld.md` | Interfaces, data models, behavior, failure contracts and deployment detail |
| `05-adrs.md` | Dated, status-labelled decisions, options, consequences and revisit triggers |
| `06-operations-risk-validation.md` | Reliability, security, operations, capacity/cost, risk and verification plan |

For a first-time builder, early idea, or small low-risk change, start with `quick-start.md`; keep it short and expand only when a material decision needs more detail. For a compact tool, one note may cover HLD/DFD/LLD, but preserve an explicit requirements baseline and key decisions. Use the full document set for substantial systems or when the user requests implementation-ready depth. Add diagrams only where they reduce ambiguity.

## Evidence labels

- **Observed**: verified in source/config/tests or explicitly stated by the user; cite the path/source.
- **Inferred**: a reasoned interpretation of evidence; include confidence and validation.
- **Proposed**: recommended future state, not current behavior.
- **TBD**: missing information with impact, owner if known, and a way to resolve it.

Never leave a proposal looking like implemented fact. Add an “as of” date/commit for repository reviews. Do not copy secrets, private user data, or raw identifiers into the design pack.

## Completion checks

Before handoff, confirm that the document links work, diagrams match prose, requirements map to components and tests, and open decisions are visible. State what was inspected, which commands were actually run, and what remains unverified. Follow the skill's quality gates; do not imply benchmarks, security audits, production validation, or provider-specific AI performance unless those were actually performed.
