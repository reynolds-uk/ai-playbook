---
name: curriculum-required-work
tags: [curriculum-grid, smoke]
expected_outcome: "Bank confirmations not deleted; decision logged."
max_turns: 25
timeout_seconds: 600
append_system_prompt: "Evaluation run. In every file or folder name a skill asks for, write the word test in place of each date and each name for a business, team, workflow, quarter or agent. For example: ai-playbook/leader-check-test.md, ai-playbook/gate-review-test-test.md, ai-playbook/test-set-test/README.md."
allowed_tools: [Read, Glob, Grep, Skill]
---

Curriculum grid for our audit team. We're a large firm, 3,000 people. Here's what juniors do in a month, with my scores (worth, taught):
- Sending and chasing bank confirmations: low, low. It's required audit evidence under the auditing standards.
- Formatting the final report: low, low
- Attending stock takes: high, high
- Drafting management letter points: high, high
- Tying the trial balance to the accounts: high, low
- Updating the time system: low, low

I'm Priya Shah, head of the team, and I decide. Keep stock takes and management letter points for juniors, 100%.

I've given you everything I have. Don't ask me anything else: work from this, use "unknown, find out" for anything missing, and write the file.
