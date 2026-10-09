---
name: model-runs-data-rules
tags: [where-each-model-runs, smoke]
expected_outcome: "Data rules decide where each model runs before cost; the Friday test fails where the instructions live in the vendor's product; decision logged."
max_turns: 25
timeout_seconds: 600
append_system_prompt: "Evaluation run. In every file or folder name a skill asks for, write the word test in place of each date and each name for a business, team, workflow, quarter or agent. For example: ai-playbook/leader-check-test.md, ai-playbook/gate-review-test-test.md, ai-playbook/test-set-test/README.md."
allowed_tools: [Read, Glob, Grep, Skill]
---

Work out where each model should run for our claims intake workflow. We're an insurer, about 800 people, customers in the UK and Germany. The steps:
- Reading the claim form and pulling out the fields: thousands a day, easy to check against the form, wrong answers are cheap to fix.
- Checking the claim against the policy wording: a few hundred a day, costly if wrong.
- Anything involving German customers' medical records: our contract says that data stays in the EU.
- Fraud flags: the model must behave the same way next year, because our auditor tests it annually.
- Writing the decline letter: a person signs every one.

Today every step uses one rented model, and all our prompts live inside the vendor's agent builder. We have no test set yet. I'm Tom Okafor, head of claims operations, and I decide the routing.

I've given you everything I have. Don't ask me anything else: work from this, use "unknown, find out" for anything missing, and write the file.
