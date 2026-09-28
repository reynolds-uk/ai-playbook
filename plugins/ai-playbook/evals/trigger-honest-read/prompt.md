---
name: trigger-honest-read
tags: [triggering]
expected_outcome: "Leader check fires."
max_turns: 6
timeout_seconds: 600
append_system_prompt: "Evaluation run. In every file or folder name a skill asks for, write the word test in place of each date and each name for a business, team, workflow, quarter or agent. For example: ai-playbook/leader-check-test.md, ai-playbook/gate-review-test-test.md, ai-playbook/test-set-test/README.md."
allowed_tools: [Read, Glob, Grep, Skill]
---

Can you give me an honest read on how AI is going in our business? I run a 200-person accountancy firm. Five minutes, max.
