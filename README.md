![Spiral](docs/readme-banner.svg)

# Spiral

**Before the Build. Between the People.**

Spiral helps product managers, designers and engineers find gaps in multi-person workflows before building. Rehearse handoffs, notifications, ownership and recovery one role at a time.

## The Problem

Some work passes between people: a request, an approval, a support case. Each person sees only part of the picture.

A plan can have a gap that nobody notices until the product is built. For example, a manager approves a request, but nothing tells the person who asked.

## What This Does About It

Spiral is a skill: a folder of instructions you add to an AI agent. Before you build, it walks through the process one person at a time. For each person it tracks what they can see, what they can do and what they are waiting for.

You get a timeline linked back to your documents, a list of what each handoff needs (a handoff is when work passes to the next person), and test scenarios. Spiral keeps what your documents say apart from what it had to assume.

**Example.** In the project’s made-up example, the plan never says the person who asked gets told after approval. Spiral flags that gap. It calls it a gap in the documents, not a bug in a real app.

## Put It to Work

- **Approvals:** who knows a decision is complete, and which version was approved?
- **Support handoffs:** who owns the request while a specialist or next shift takes over?
- **Collaborative work:** what changed while someone was away, and what needs their attention?
- **Delayed or out-of-order events:** which state is current, who can resolve a conflict, and how does work resume?

Spiral tracks what each role can see and do. You receive a source-linked event timeline, handoff requirements and acceptance scenarios that distinguish facts from assumptions.

## Rehearse a Workflow

Install [spiral-workflow-rehearsal](skills/spiral-workflow-rehearsal/SKILL.md) in an agent that supports skills. Bring roles, permissions, workflow rules, mockups or notification templates—whichever exist.

[Installation and updates](INSTALL.md) · [Validation fixtures and results](validation/README.md)

```text
Use $spiral-workflow-rehearsal to rehearse this approval workflow.
Track what requester, approver and admin can see, do and wait for.
Include a late approval and a failed notification.
```

[Follow the fictional approval example](skills/spiral-workflow-rehearsal/references/fictional-approval.md) · [Research foundations](skills/spiral-workflow-rehearsal/references/research.md)

## Part of the Hex Men Collection

[Hex Men](https://github.com/jongos/Hex-Men) is a directory of independent projects by Jon Gosier. Each project stands on its own; these are its members.

| Project | What It Does |
|---|---|
| [Hex Men](https://github.com/jongos/Hex-Men) | Directory of independent projects |
| [Dazzler](https://github.com/jongos/Dazzler) | Create and refine expressive visual interfaces |
| [Longshot](https://github.com/jongos/Longshot) | Independently test rendered UI tasks and provide replayable evidence |
| [Style Science](https://github.com/jongos/style-science) | Provide inspectable design reasoning, constraints and evidence |
| **Spiral** (this repository) | Rehearse role-limited asynchronous workflows before building |
| [Shatterstar](https://github.com/jongos/Shatterstar) | Propose reversible evidence-backed simplification while preserving important tasks |
| [Mojo](https://github.com/jongos/Mojo) | Remove repetition, needless nuance and overly cautious language from AI outputs |
| [Colossus](https://github.com/jongos/Colossus) | Inventory selected developer workspaces read-only and surface evidence-backed questions |

## Further Reading

[Detailed project reference](REFERENCE.md) · [Landing page](https://jongos.github.io/Spiral/) · [Page preview notes](REFERENCE.md#landing-page-source)

## License

Created by Jon Gosier. Original work is Apache-2.0; bundled Inter and League Gothic font files retain their own licenses and notices (see `docs/fonts/`). See [LICENSE](LICENSE).
