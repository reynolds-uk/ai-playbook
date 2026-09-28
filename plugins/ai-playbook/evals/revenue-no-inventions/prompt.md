---
name: revenue-no-inventions
tags: [where-the-revenue-is, smoke]
expected_outcome: "No invented names or prices; contract check flagged."
max_turns: 25
timeout_seconds: 600
append_system_prompt: "Evaluation run. In every file or folder name a skill asks for, write the word test in place of each date and each name for a business, team, workflow, quarter or agent. For example: ai-playbook/leader-check-test.md, ai-playbook/gate-review-test-test.md, ai-playbook/test-set-test/README.md."
allowed_tools: [Read, Glob, Grep, Skill]
---

Where the revenue is, for our employment law firm: 40 people, we advise mid-size employers. We charge by the hour, plus fixed fees for contract templates. Across about 300 clients we can see which HR policies lead to tribunal claims, but we've never joined that data up. We produce annual pay-gap reports as numbers. We record time in six-minute units against matter types. I don't know what clients would pay for anything new. Tests: re-price tribunal defence, owned by me, Helen Brook, and stop if none of the first three clients will discuss a fixed fee. New product: a tribunal risk score, owned by Helen Brook too, stop if the first five clients shown it aren't interested.

I've given you everything I have. Don't ask me anything else: work from this, use "unknown, find out" for anything missing, and write the file.
