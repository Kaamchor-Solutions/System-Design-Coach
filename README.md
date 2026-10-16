# System Design Coach

A provider-neutral Agent Skill that helps an AI coding agent turn a software idea or existing repository into an understandable, evidence-led system design—before the builder commits to an implementation. It produces a right-sized document pack (PRD, HLD, DFD, LLD, ADRs, risks, and validation plan), explains trade-offs in plain language, and checks whether each recommendation fits the actual needs.

> **Core rule:** design for stated requirements and evidence, not fashion. Kafka, microservices, Kubernetes, caches, and horizontal scaling are options—not defaults.

## Try the skill with an AI coding agent

If the agent supports the Agent Skills convention, install the complete [`skills/system-design-coach/`](skills/system-design-coach/) directory according to that agent's current skill instructions. Keep its `SKILL.md`, `references/`, and `templates/` together. If it cannot install a skill, provide `SKILL.md` and the linked references/templates to the agent as project instructions; access to this repository or a pasted URL does not guarantee the agent can read every file.

Then ask, for example:

> Use the System Design Coach skill to inspect this repository read-only. First describe what the software actually does and its current architecture. Then make a right-sized PRD and architecture pack in a separate `docs/system-design/` folder. Distinguish observed facts from assumptions and proposed changes. Explain the important trade-offs for a first-time builder. Do not edit application code or deploy anything.

The skill works for new products, major features, and existing-system architecture reviews. It is designed to be useful to coding agents that can read a repository and create files; the host's actual repository, shell, and file permissions still apply.

## What's included

- [`skills/system-design-coach/SKILL.md`](skills/system-design-coach/SKILL.md) — the provider-neutral workflow and trigger metadata.
- [`skills/system-design-coach/references/`](skills/system-design-coach/references/) — detailed workflow, architecture-pattern guidance, and quality gates.
- [`skills/system-design-coach/templates/architecture-pack/`](skills/system-design-coach/templates/architecture-pack/) — includes a plain-language [quick-start note](skills/system-design-coach/templates/architecture-pack/quick-start.md) and [fictional worked example](skills/system-design-coach/templates/architecture-pack/quick-start-example.md), plus full templates for requirements, HLD, DFD, LLD, decisions, and risk/validation.
- [`pilot/powerbi-simulator/`](pilot/powerbi-simulator/) — a read-only trial on the public Power BI Simulator Skills repository. It is an example design output, not a modification or endorsement of that project.
- [`tests/`](tests/) and [`.github/workflows/tests.yml`](.github/workflows/tests.yml) — portable package checks and a Python-version CI matrix.

## Design principles

1. **Evidence before diagrams:** inspect code, tests, CI, deployment/configuration, and documented limits; state what was and was not available.
2. **Trade-offs over tech lists:** compare reasonable options, including doing less, and identify the point at which a design should change.
3. **No invented certainty:** unknown demand, budget, compliance, availability, and performance remain open questions until evidenced.
4. **Teach the why:** explain the purpose, downside, and operational cost of each major component in everyday language.
5. **A design is not a deployment:** do not edit code, provision cloud resources, publish, or deploy unless the user asked for that scope and any important unresolved choice has been settled.

## Release

This initial public release is available at [Kaamchor-Solutions/System-Design-Coach](https://github.com/Kaamchor-Solutions/System-Design-Coach) under the [MIT License](LICENSE). Copyright © 2026 Kaamchor Solutions.

The pilot is a first evidence-based design-document exercise, not a live coding-agent/provider benchmark, production/security audit, or universal validation of every host. See the [pilot result](pilot/PILOT-RESULT.md) and [full evaluation](pilot/pilot-evaluation.md) for scope, limitations, and recorded follow-ups.
