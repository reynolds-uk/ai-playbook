---
name: self-check-strict
tags: [self-check]
expected_outcome: "2 of 6."
max_turns: 25
timeout_seconds: 600
append_system_prompt: "Evaluation run. In every file or folder name a skill asks for, write the word test in place of each date and each name for a business, team, workflow, quarter or agent. For example: ai-playbook/leader-check-test.md, ai-playbook/gate-review-test-test.md, ai-playbook/test-set-test/README.md."
allowed_tools: [Read, Glob, Grep, Skill]
---

Self-check me, Aim it section only, and score just that section. Timed the whole workflow end to end: sort of, for some projects. Know what happens five minutes before and after: yes, from sitting with the repairs team, notes in our wiki. Deleted steps before automating: we're working on it. Stop criteria written before work started: no. Baseline taken before building: mostly. Have stopped something and said so: yes, the chatbot pilot, the email to the board is dated 3 March.

I've given you everything I have. Don't ask me anything else: work from this, use "unknown, find out" for anything missing, and write the file.
