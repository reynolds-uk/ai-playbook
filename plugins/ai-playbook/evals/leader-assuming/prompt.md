---
name: leader-assuming
tags: [leader-check, smoke]
expected_outcome: "Assuming; start with the test set and one name per tool; next skill is test-set."
max_turns: 25
timeout_seconds: 600
append_system_prompt: "Evaluation run. In every file or folder name a skill asks for, write the word test in place of each date and each name for a business, team, workflow, quarter or agent. For example: ai-playbook/leader-check-test.md, ai-playbook/gate-review-test-test.md, ai-playbook/test-set-test/README.md."
allowed_tools: [Read, Glob, Grep, Skill]
---

Run the leader check for us. We're a PE-backed accountancy and advisory firm, about 220 people, and the value comes from people's expertise and time.

My answers to the nine questions:
1. We start from what vendors pitch and whoever is keenest.
2. Only as savings, counted in hours.
3. We have estimates of hours saved, nothing in the accounts.
4. Mostly the vendor's word that it's accurate.
5. It acts on its own on some work: an invoice agent posts supplier invoices under 2,000 pounds with nobody checking.
6. No one is named. IT sort of looks after it.
7. We haven't thought about it.
8. Our people and our client relationships.
9. If a pilot looks good, we roll it out.

I've given you everything I have. Don't ask me anything else: work from this, use "unknown, find out" for anything missing, and write the file.
