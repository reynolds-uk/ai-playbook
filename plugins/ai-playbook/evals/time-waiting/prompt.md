---
name: time-waiting
tags: [where-the-time-goes]
expected_outcome: "Report deleted; letter augmented; prize in the waiting."
max_turns: 25
timeout_seconds: 600
append_system_prompt: "Evaluation run. In every file or folder name a skill asks for, write the word test in place of each date and each name for a business, team, workflow, quarter or agent. For example: ai-playbook/leader-check-test.md, ai-playbook/gate-review-test-test.md, ai-playbook/test-set-test/README.md."
allowed_tools: [Read, Glob, Grep, Skill]
---

Where the time goes, for our commercial policy renewals. The job: get the client renewed on the right cover with no gap. The account handler does about 90 minutes of real work, but it takes 11 days end to end. Steps: a renewal report is generated 60 days out that nobody reads and nothing requires; email the client for updated information; chase twice; re-key the details into three insurer portals; compare quotes in a spreadsheet; write the recommendation letter; team leader sign-off, which sits in an inbox for about two days; send it to the client. Before it: the renewal date. After: the client signs and the policy is bound. I'm Mark Ellis, operations director, and I'm happy with your sort.

I've given you everything I have. Don't ask me anything else: work from this, use "unknown, find out" for anything missing, and write the file.
