# Fictional worked example: equipment approval

All names, rules and events below are invented. These are synthetic source artifacts, not observations of an application.

## Synthetic source A: permissions

Requester can submit and read their request detail. Approver can decide assigned requests. Admin can reassign pending requests and inspect delivery failures. Requester cannot see the approval queue or admin log.

## Synthetic source B: workflow

Submission creates a pending request and emails the approver. Approval updates the stored status. The request-detail mockup displays status. No requester notification is specified. Pending requests escalate to admin after two business days; the business calendar is unspecified.

## Ledger

| Event/order | Actor | Visible information and knowledge | Expected action / wait exit | Owner / evidence |
|---|---|---|---|---|
| E1: submission | Requester | Pending confirmation | Wait for decision; return trigger unspecified | Requester; [B](#synthetic-source-b-workflow), known |
| E2: email delivered | Approver | Assigned pending request | Approve or reject; decision ends own wait | Approver; [A](#synthetic-source-a-permissions), [B](#synthetic-source-b-workflow); delivery assumed |
| E3: approval stored | Approver | Decision succeeded, assuming confirmation | No further action specified | Approver; B plus assumed confirmation |
| E3: same event | Requester | No new observable event; last known state pending | Still waiting unless voluntarily revisiting detail | Notification unknown in B; no revisit assumed |
| E4: no revisit | Admin | Delivery failures visible; no decision notice specified | No specified intervention for completed request | [A](#synthetic-source-a-permissions), B |

## Finding and counterexample

The specification lacks a requester handoff after approval. Minimal trace: requester submits, leaves; approver approves; requester never reopens detail and receives no other notice. Approval completes but requester remains uninformed. This is a logical gap in the supplied artifacts, not a verified application defect. A specified requester notification or another evidenced return trigger would challenge the finding. Polling the detail page would reveal the decision, so the claim is not that the decision is inaccessible.

## Proposed handoff and acceptance scenarios

Require the service to notify the requester after a committed decision, with request ID, decision and authorized detail link, excluding internal approver notes. Proposed delivery target: five minutes. Record delivery failure and route unresolved failures after fifteen minutes to admin; these times require product approval. Show current state on detail even if a late message describes an older event. Admin owns failed-delivery recovery. Do not equate transport success with human awareness.

- Given approval commits, when the requester returns through the notice, then detail shows the current decision and a permitted next action.
- Given delivery fails, when the proposed fifteen-minute threshold passes, then admin sees a recoverable failure tied to the request and recipient; retry does not change the decision.
- Given a duplicate event, when notification processing retries, then one logical decision remains and duplicate notices are suppressed or clearly correlated.
- Given reassignment before a late approval attempt, when the former approver acts, then current authorization is checked and a rejected stale action cannot change the decision.
- Given a delayed pending message arrives after approval, when opened, then current status is shown rather than a stale pending action.

Decisions remaining: business calendar, rejection/cancellation notices, delivery targets, fallback channel and whether acknowledgment is necessary. These scenarios are proposed checks, not executed tests.
