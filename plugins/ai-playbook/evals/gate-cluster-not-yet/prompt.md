---
name: gate-cluster-not-yet
tags: [gate-review, smoke]
expected_outcome: "Not yet: fix the Kestrel cluster; model change doesn't demote; register history and decisions updated."
max_turns: 25
timeout_seconds: 600
append_system_prompt: "Evaluation run. In every file or folder name a skill asks for, write the word test in place of each date and each name for a business, team, workflow, quarter or agent. For example: ai-playbook/leader-check-test.md, ai-playbook/gate-review-test-test.md, ai-playbook/test-set-test/README.md."
allowed_tools: [Read, Glob, Grep, Skill]
---

Gate review for our invoice matching agent, v2.1. It's at Recommend and we want it at Prepare. The criteria were written on 2 June, before we measured anything: at least 90% acceptance over at least 400 invoices, and no single cluster above 20% of overrides. Evidence: 94% acceptance over 612 invoices. 37 overrides, and 21 of them are from one supplier, Kestrel Freight, whose invoice layout changed in August. We swapped to a newer model in September and re-ran the 120-case test set: 96%, up from 95%. No permission changes. Jo Adams, the supervisor, makes the call.

I've given you everything I have. Don't ask me anything else: work from this, use "unknown, find out" for anything missing, and write the file.
