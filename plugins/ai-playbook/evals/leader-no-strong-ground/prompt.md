---
name: leader-no-strong-ground
tags: [leader-check]
expected_outcome: "Piloting; the board sentence says there's no strong ground yet."
max_turns: 25
timeout_seconds: 600
append_system_prompt: "Evaluation run. In every file or folder name a skill asks for, write the word test in place of each date and each name for a business, team, workflow, quarter or agent. For example: ai-playbook/leader-check-test.md, ai-playbook/gate-review-test-test.md, ai-playbook/test-set-test/README.md."
allowed_tools: [Read, Glob, Grep, Skill]
---

Leader check please. We're an established logistics business, value comes from making, moving or selling things.

1. What vendors suggest.
2. Only as savings.
3. We don't track it.
4. Anecdotes and spot checks.
5. It drafts, and people decide.
6. For some of it, informally.
7. We assume they'll pick it up.
8. Not much.
9. Gut feel and enthusiasm.

I've given you everything I have. Don't ask me anything else: work from this, use "unknown, find out" for anything missing, and write the file.
