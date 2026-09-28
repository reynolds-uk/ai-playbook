---
name: gate-skip-to-act
tags: [gate-review]
expected_outcome: "Corrects to Prepare and asks for criteria."
max_turns: 10
timeout_seconds: 600
append_system_prompt: "Evaluation run. In every file or folder name a skill asks for, write the word test in place of each date and each name for a business, team, workflow, quarter or agent. For example: ai-playbook/leader-check-test.md, ai-playbook/gate-review-test-test.md, ai-playbook/test-set-test/README.md."
allowed_tools: [Read, Glob, Grep, Skill]
---

Our invoice-matching agent has been at Recommend for three months and it's been great. Is it ready to act on its own?
