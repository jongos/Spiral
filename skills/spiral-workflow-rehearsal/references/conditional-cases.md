# Conditional cases and proposed validation

All cases are fictional. Names, timing, rules and outcomes are invented; no application or people were tested. Read only the case relevant to the workflow. The full [approval example](fictional-approval.md) shows the ledger format.

## Revision-sensitive approval

An author submits v4 and an approver signs it off. The author makes v5; the publisher sees v5 with an unchanged, unversioned Approved badge. The rules do not state whether approval survives edits. This exposes a missing specification, not a prediction about what the approver notices.

Candidate repair: bind approval evidence to the reviewed version, define which changes require new review and expose release eligibility. Formatting-only exceptions are human policy decisions. Candidate criterion: a substantive edit cannot be presented to the publisher as authorized by the older approval.

## Support shift handoff

A frontline agent sends a case to a specialist queue. The customer sees Escalated; the shift ends. No rule assigns responsibility while a specialist has not accepted the case. A shared inbox and sent message do not establish an owner.

Candidate repair: keep an accountable owner until reassignment is accepted, transfer concise context and define the customer-visible next update and escalation trigger. Separate internal notes from customer messages. Candidate criterion: every nonterminal state has an authorized responsible role and an observable stalled-handoff recovery route.

## Marketplace acceptance and expiry

A request expires at 14:00 and can be accepted by a provider or canceled by the customer while pending. Near expiry, acceptance and cancellation are recorded; the actors receive different notices first. No authoritative state or precedence rule exists in the synthetic specification.

This is a conditional conflict; the reviewer cannot choose a legitimate winner. Candidate repair: define transition ordering and current-state checks on reopening notices; name an authorized resolver and effect-specific recovery if work has begun. Candidate criterion: late messages do not present incompatible commitments as simultaneously current. Cancellation must not be assumed to undo completed effects.

## Proposed synthetic validation, not executed

Prepare tiny invented fixtures and expected findings independently. Pair each flawed case with a corrected control to check for invented defects. No private data, live tools, messages or transactions are necessary.

| Dimension | Seeded gap | Corrected control |
|---|---|---|
| Knowledge isolation | B needs information visible only to A | An authorized disclosure reaches B before the action |
| Ownership transfer | Queue notice without pending ownership | Existing owner remains accountable until acceptance |
| Version freshness | v1 approval shown as applicable to v2 | Approval version and edit policy are explicit |
| Waiting/detection | Absent actor; no observer or timeout | Observer, trigger, authorized alternate and next state supplied |
| Recovery | External effect followed by failure; generic cancel flag | Effect-specific recovery, owner and irreversibility stated |
| Coherent negative control | No seeded gap in a small complete specification | Reviewer reports no manufactured critical defect; unknowns stay questions |

A future review could record seeded-gap detection, unsupported claims, actor-information leakage, source traceability and whether a proposed repair addresses the cause without expanding permissions. Compare repeated reviews and independent domain-expert judgments. These are proposed dimensions, not measured performance or thresholds. Passing fixtures would establish only behavior on those fixtures, not real-world predictive validity.
