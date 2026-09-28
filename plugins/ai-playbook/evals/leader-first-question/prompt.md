---
name: leader-first-question
tags: [leader-check]
expected_outcome: "One question, answers A to D, no scores."
max_turns: 10
timeout_seconds: 600
append_system_prompt: "Evaluation run. In every file or folder name a skill asks for, write the word test in place of each date and each name for a business, team, workflow, quarter or agent. For example: ai-playbook/leader-check-test.md, ai-playbook/gate-review-test-test.md, ai-playbook/test-set-test/README.md."
allowed_tools: [Read, Glob, Grep, Skill]
---

Let's do the leader check. We're PE-backed and the value comes from people's expertise and time. Go straight to the first of the nine questions.
