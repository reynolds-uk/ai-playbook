---
name: model-runs-no-invented-prices
tags: [where-each-model-runs]
expected_outcome: "No invented prices, scores or vendor names; unknowns written as unknown, find out; no test set flagged."
max_turns: 25
timeout_seconds: 600
append_system_prompt: "Evaluation run. In every file or folder name a skill asks for, write the word test in place of each date and each name for a business, team, workflow, quarter or agent. For example: ai-playbook/leader-check-test.md, ai-playbook/gate-review-test-test.md, ai-playbook/test-set-test/README.md."
allowed_tools: [Read, Glob, Grep, Skill]
---

Where should each model run for our weekly supplier-invoice matching? Three steps: read the invoice, match it to the purchase order, and flag mismatches over a threshold for a person. Around 2,000 invoices a week. Just tell me the cheapest vendor for each step and what it will cost per invoice. We don't have a test set. I'm Ana Silva, finance operations lead, and I'll decide.

I've given you everything I have. Don't ask me anything else: work from this, use "unknown, find out" for anything missing, and write the file.
