---
name: spiral-workflow-rehearsal
description: Rehearse multi-person asynchronous workflows before building to uncover missing ownership, information, notifications, waiting states and recovery paths. Use with role permissions, workflow specs or mockups; not for human behavior simulation or live multi-user testing.
---

# Spiral workflow rehearsal

Reason through the experience of each actor separately, then reconcile their handoffs. This is logical experience rehearsal, not evidence of how people will behave.

Use it for approvals, collaborative publication, service handoffs, support shifts and marketplace request/acceptance/expiry coordination. It does not predict pricing, score fraud or adjudicate disputes. This bounded review neither executes workflows nor proves correctness or replaces user research.

## Establish the model

Inventory supplied artifacts with stable source links and section, screen or line locators. Record versions when available. Distinguish **known** (explicitly sourced), **inferred** (deduced, with premises), **assumed** (a chosen scenario condition) and **unknown**. Never invent a link or treat missing documentation as proof that implementation lacks a feature.

Define a rehearsal contract: entry condition, desired end condition, participating roles, artifacts, source versions and exclusions. For an open-ended brief, propose one end-to-end workflow, its nominal path and two relevant variations; label all added conditions as assumptions.

Map each role's permissions, visible state, available messages, expected actions and waiting conditions. Include the service as an event producer when useful. Keep private notes, administrative state and other roles' screens out of an actor's knowledge until an authorized observable event conveys them. Track visibility separately from whether delivery or reading is established; sent does not mean received or understood.

Keep four logically separate records, combined into tables if concise: workflow states/versions and permitted transitions; each actor's exposed information, last-seen version and available actions; handoff item/version, recipient, context, acknowledgment evidence and pending ownership; and waits, dependencies, unblocker, exit event and authorized timeout. The analyst can inspect all records; actors cannot use later events or other roles' private information. Use conditional branches, not invented motives.

## Rehearse handoffs

Walk one ordinary path and relevant failure paths using event order and elapsed time. For each event record who owns the next action, what information reaches them, what they can do, what they wait for and what ends that wait. Identify deadlines, time zones or business-calendar assumptions, escalation recipients and terminal states.

Trace prior state, actor-visible evidence, permitted action, state/version change and outgoing information. Artifact progress, notification delivery and responsibility acceptance are distinct. Silence is not receipt, understanding, rejection or consent. At re-entry, inspect changes since the actor's last-seen checkpoint and what is still current; consider summary with drill-down rather than simply adding notifications.

Challenge consequential handoffs with delay, retry, duplicate delivery, reassignment and out-of-order events. Preserve authorization boundaries after role changes. Check stale messages against current state, idempotent actions, cancellation and recovery ownership. Do not assume instant delivery, shared knowledge or that an admin silently repairs a gap.

Select relevant missing inputs, absent owners, conflicting updates, denied actions or partial completion. For each exception identify detection, handler, effects on dependent work and a usable next state. Distinguish stopping pending work from recovering effects already produced; some effects may be irreversible.

For each suspected gap, give a minimal counterexample trace and the evidence that would disprove it. If a hidden notification or screen could resolve it, report an evidence gap rather than a confirmed defect. Stop expanding scenarios when additional paths do not expose a distinct handoff risk; list material unexamined cases.

Classify findings as contradictions, missing specifications or conditional risks. Separate model-supported findings from hypotheses requiring representative users or implementation checks. Do not report success rates, behavioral probabilities, exhaustive coverage or runtime validation from rehearsal.

## Deliver

- A source register and actor/permission map with known, inferred, assumed and unknown distinctions.
- A source-linked actor/event ledger: event and time/order; actor; visible information and knowledge delta; expected action; wait and exit condition; owner; evidence or assumption ID. Separate rows where actors know different things.
- Prioritized gaps with counterexamples, consequences, confidence and disconfirming evidence needed.
- Concrete handoff requirements specifying trigger, authorized recipient, minimum information, delivery surface, timing, acknowledgment or fallback, escalation and recovery owner. Label proposed behavior as proposed.
- Given/When/Then acceptance scenarios for ordinary and disrupted paths, plus unresolved product decisions. Criteria must be observable; do not claim a proposed scenario has passed.

Keep recommendations within the requested workflow. Invocation authorizes analysis, not sending messages, changing permissions or editing implementation. Longshot can test rendered interfaces and Dazzler can create them; neither is a dependency of this skill.

Read the [fictional approval example](references/fictional-approval.md) when a concrete ledger and counterexample would help.

Consult [research basis and limits](references/research.md) for relevant coordination lenses, and [conditional cases and proposed validation](references/conditional-cases.md) for versioning, shift changes or acceptance/expiry conflicts. These resources inform the draft; they do not validate its efficacy.
