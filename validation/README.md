# Synthetic validation

All inputs are fictional. `cases.json` contains five flawed/control pairs and
one coherent negative control. Source IDs are local to each case. Order is logical
event order; no real messages or transactions are executed.

`expectations.json` is the separately stored grading rubric. It is deliberately
not included in evaluation input. Each pair differs in one source rule so that a
correction can be tested without changing the rest of the scenario.

## Run the repository checks

Requires Python 3.9+ and its standard library:

```text
python -B -m unittest discover -s tests -v
```

These checks validate fixture structure, pair isolation, rubric references,
portable skill packaging and local documentation links. They do not execute a
language model or grade its reasoning.

## Evaluate the skill

Give a fresh reviewer only the unchanged core SKILL.md and one case from
`cases.json`, without expectations, pair labels or earlier responses. Ask:

> Rehearse this bounded workflow using Spiral. Cite source IDs; separate known
> events from assumptions. Return an actor/event ledger, classified gaps with
> counterexamples and disconfirming evidence, proposed handoff requirements,
> observable acceptance scenarios and unresolved decisions. Do not execute actions.

Save the raw response before grading against `expectations.json`. Check required
findings, forbidden conclusions, source traceability, role knowledge boundaries,
and whether repairs preserve permissions. Controls should not receive the paired
defect. Additional valid findings require source evidence, not automatic rejection.

Record model, skill hash, prompt, case ID, response and reviewer identity. Repeat
in fresh contexts and use an independent reviewer before reporting detection or
false-positive rates. This initial session authored the fixtures and inspected
the rubric, so its [manual walkthrough](REVIEW-2026-10-24.md) is an unblinded
consistency check, not an independent benchmark or an automatic pass for the skill.

A subsequent [separate-agent blinded run](blind-2026-10-24/RESULTS.md) preserved
raw responses before rubric grading. It detected the five seeded gaps and
reported no supported gap in six controls, with one classification difference.
Its one-context and instruction-enforced blinding limits are documented there.
