# Blinded evaluation — October 24, 2026

The separate reviewer found all five seeded gaps and reported no supported gap
in the five corrected controls or the coherent negative control. This is one
reviewer run across 11 small synthetic cases, not an estimate of production
accuracy. The unchanged core skill needs no revision on this evidence.

## Protocol and evidence

- Reviewer: separate agent `blind_evaluator`, started with `fork_turns=none`.
  Same inherited model as the parent; no model override. This is independent
  response generation, not a different model or an external human review.
- Inputs: an exact core skill copy and shuffled cases with neutral IDs. Rubric,
  original IDs, mapping, prior walkthrough and reference supplements withheld.
- The reviewer was instructed to read only the two inputs, treat cases
  independently, and save the entire response before grading. It attested to
  those read limits. Filesystem access was not technically restricted to them.
- A follow-up requested concise completion and reiterated no extra reads; no
  expected findings or grading feedback were supplied during evaluation.
- The parent graded against the existing rubric only after the response was
  complete. No retries, response edits or rubric changes were made.
- [Raw response](response.md), [input cases](input/cases.json),
  [skill snapshot](input/SKILL.txt), [ID mapping](mapping.json),
  [hashes and protocol](protocol.json), [original rubric](../expectations.json).
  The skill snapshot was renamed from .md to .txt after completion, preserving
  bytes; raw response records its original read path.

## Case grading

This is semantic grading by the parent, not an automated grader. “Match” means
the seeded issue or its resolution was identified; it does not assert every
proposed implementation detail is necessary.

| Blind case | Original case | Reviewer finding | Rubric assessment |
|---|---|---|---|
| 01 | version-b | No supported gap; v2 gate defeats stale approval | Match |
| 02 | ownership-a | Explicit ownerless interval; conditional risk, plus missing recovery activation | Issue detected; classification differs |
| 03 | knowledge-a | Missing authorized disclosure evidence/specification | Match |
| 04 | waiting-a | Missing detection-to-recovery handoff | Match |
| 05 | ownership-b | A remains accountable; dispatcher recovery conditional on elapsed time | Match |
| 06 | recovery-b | Operator recovery preserves completed dispatch | Match |
| 07 | recovery-a | Missing effect-specific owner/state; cancellation is not rollback | Match |
| 08 | complete-a | No gap; no additional notification needed for explicit current-state read | Match |
| 09 | waiting-b | Timer and dispatcher provide recovery; decision not yet complete | Match |
| 10 | version-a | Approved-version-only policy contradicts v2 release using v1 approval | Match |
| 11 | knowledge-b | Authorized summary read before decision resolves disclosure gap | Match |

The ownership classification difference is defensible: the fixture explicitly
defines an ownerless interval without declaring a continuous-ownership invariant.
The reviewer calls its consequence a conditional risk, while the rubric treats
the missing interim responsibility rule as a missing specification. Neither
asserts an observed application failure. Preserve this nuance in future grading;
the rubric has not been changed to accommodate the result.

## Quality observations

All 11 responses include source/role context, an actor/event ledger, findings or
an explicit no-gap conclusion, counterexample challenges and disconfirming
evidence, proposed handoffs, acceptance scenarios and unresolved scope. Source
locators use case/source IDs rather than fabricated links.

No listed forbidden conclusion was observed. In particular, the reviewer did not
give B private knowledge, equate delivery with acceptance, claim cancellation
reversed dispatch, guarantee return, assume silent admin recovery, or impose
notifications on the complete negative control.

The reviewer also handled underspecified timing correctly: case 05 does not
establish that 30 minutes passed; case 04's 60-minute event is not an existing
timeout rule. It distinguished permitted publication from completed publication
and recovery reassignment from final resolution.

Some recommendations go beyond the minimum fix: read acknowledgments/gates in
case 03 and richer handoff surfaces in several controls. They are labeled as
proposals, not established requirements or new findings. Reviewers should still
test whether such additions are proportionate. This is a recommendation-quality
question, not evidence of actor-information leakage or a missed seeded gap.

## Limits and next step

One agent saw all cases in one context. Labels were hidden and order shuffled,
but paired scenarios remain recognizable. Instructions required independent
case analysis; this is weaker than fresh isolated contexts for every case.
The grader authored the fixtures and is not an independent blinded grader.
The core skill alone was tested; optional supplements and automatic skill
discovery were excluded. There are no repeated trials or real application runs.

Next evaluation should use fresh per-case contexts and longer conflicting
artifacts, stale authorization, duplicate events and acceptance/expiry races.
Keep the core unchanged until those tests reveal a reproducible instruction gap.
