# Quick-start design note

Use this for an early idea or small, low-risk change—especially when the builder is new to system design. Aim for one page. Keep the important evidence and safety boundaries; omit technical detail that does not change a decision. A [fictional worked example](quick-start-example.md) shows one way to fill this in.

**Status:** [Idea / Current-state review / Proposed change]  
**Date / evidence boundary:** [Date; files, user statements, or other sources actually inspected]

## 1. Who needs what, and how will we know it helps?

[In everyday words: person → need → useful outcome. Add one observable success check or mark it TBD.]

## 2. What do we know, and what are we assuming?

- **Observed facts:** [User-stated needs or evidence; cite a file/path or source.]
- **Inferences:** [What the evidence suggests but does not directly prove; cite the source and confidence.]
- **Assumptions / unknowns:** [What is not confirmed, why it matters, and how to check it.]
- **Questions that could change the design:** [Ask only these; proceed with bounded assumptions for the rest.]

## 3. What is the smallest useful solution?

[Describe the proposed first version in plain language. Name what is deliberately not included yet and the evidence that would justify adding it.]

## 4. Where does information go?

[Write a short flow such as “person → app → saved list on this device,” or add a tiny diagram. State what data is stored, who can access it, and whether it leaves the device or crosses a third-party boundary. Treat titles, URLs, names, and metadata as potentially sensitive. Do not infer privacy from local storage or from a link being public. Label the flow as observed or proposed.]

## 5. What could go wrong, and what is the main trade-off?

[Name the most relevant failure and user-visible response. Include the material security/privacy concern and a mitigation or open question. Compare one meaningful alternative if the choice matters; explain its downside.]

## 6. How will we check it, and what happens next?

[One acceptance check or small test, what it cannot prove, the next step, and the person/decision needed.]

**Terms:** [Explain technical terms on first use in everyday language; avoid acronyms when they add no value.]

## When to expand this note

Use the full architecture pack when the design has several important integrations or trust boundaries, sensitive data or access rules, background work and retries, migrations or complex failure recovery, material availability/capacity/cost commitments, or when the user asks for implementation-ready detail. Do not expand it just to fill templates.
