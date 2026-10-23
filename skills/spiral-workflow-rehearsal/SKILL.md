---
name: spiral-workflow-rehearsal
description: Rehearse multi-person asynchronous workflows before building to uncover missing ownership, information, notifications, waiting states and recovery paths. Use with role permissions, workflow specs or mockups; not for human behavior simulation or live multi-user testing.
---

# Spiral workflow rehearsal

Reason through the experience of each actor separately, then reconcile their handoffs. This is logical experience rehearsal, not evidence of how people will behave.

## Establish the model

Inventory supplied artifacts with stable source links and section, screen or line locators. Record versions when available. Distinguish **known** (explicitly sourced), **inferred** (deduced, with premises), **assumed** (a chosen scenario condition) and **unknown**. Never invent a link or treat missing documentation as proof that implementation lacks a feature.

Map each role's permissions, visible state, available messages, expected actions and waiting conditions. Include the service as an event producer when useful. Keep private notes, administrative state and other roles' screens out of an actor's knowledge until an authorized observable event conveys them. Track visibility separately from whether delivery or reading is established; sent does not mean received or understood.

## Rehearse handoffs

Walk one ordinary path and relevant failure paths using event order and elapsed time. For each event record who owns the next action, what information reaches them, what they can do, what they wait for and what ends that wait. Identify deadlines, time zones or business-calendar assumptions, escalation recipients and terminal states.

Challenge consequential handoffs with delay, retry, duplicate delivery, reassignment and out-of-order events. Preserve authorization boundaries after role changes. Check stale messages against current state, idempotent actions, cancellation and recovery ownership. Do not assume instant delivery, shared knowledge or that an admin silently repairs a gap.

For each suspected gap, give a minimal counterexample trace and the evidence that would disprove it. If a hidden notification or screen could resolve it, report an evidence gap rather than a confirmed defect. Stop expanding scenarios when additional paths do not expose a distinct handoff risk; list material unexamined cases.

## Deliver

- A source register and actor/permission map with known, inferred, assumed and unknown distinctions.
- A source-linked actor/event ledger: event and time/order; actor; visible information and knowledge delta; expected action; wait and exit condition; owner; evidence or assumption ID. Separate rows where actors know different things.
- Prioritized gaps with counterexamples, consequences, confidence and disconfirming evidence needed.
- Concrete handoff requirements specifying trigger, authorized recipient, minimum information, delivery surface, timing, acknowledgment or fallback, escalation and recovery owner. Label proposed behavior as proposed.
- Given/When/Then acceptance scenarios for ordinary and disrupted paths, plus unresolved product decisions. Criteria must be observable; do not claim a proposed scenario has passed.

Keep recommendations within the requested workflow. Invocation authorizes analysis, not sending messages, changing permissions or editing implementation. Longshot can test rendered interfaces and Dazzler can create them; neither is a dependency of this skill.

Read the [fictional approval example](references/fictional-approval.md) when a concrete ledger and counterexample would help.
