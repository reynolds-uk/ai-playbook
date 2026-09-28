# Register: the skills in this plugin

The playbook says every AI tool that acts for a business should have a register page, a named person on the hook and a test set. The skills in this plugin are AI tools that act for whoever uses them, so here they are, on the same template as [tool 7](https://github.com/reynolds-uk/ai-playbook/tree/main/tools/07-register).

| Skill | Grade | Supervisor | Test set |
| --- | --- | --- | --- |
| The leader check | Recommend | David Reynolds | Yes, 4 cases |
| Where the time goes | Recommend | David Reynolds | Yes, 1 case |
| Where the revenue is | Recommend | David Reynolds | Yes, 1 case |
| The two columns | Recommend | David Reynolds | Yes, 1 case |
| The test set | Recommend | David Reynolds | Yes, 1 case |
| The register | Recommend | David Reynolds | Yes, 1 case |
| Gate review | Recommend | David Reynolds | Yes, 3 cases |
| Curriculum grid | Recommend | David Reynolds | Yes, 1 case |
| Self-check | Recommend | David Reynolds | Yes, 1 case |

**Last run:** 28 September 2026, plugin v2.0.0, `claude plugin eval`, three runs per case. 13 of the 16 cases passed every run. Three passed two runs in three: the leader check's pointer to the next skill, the register's wording for assumed autonomy, and the test set's README when asked to invent cases (it refused, as it should, but once didn't write the folder). Those three are the next things to fix. Two of the cases check that nothing in the plugin fires on unrelated requests.

**The gap, stated plainly:** sixteen cases is a small set. The playbook says start with thirty. Most skills have one case, and every case was written by me. It grows when someone reports a skill getting something wrong: that report becomes a case, and the case runs on every change from then on.

**Every skill is at Recommend.** It drafts; the person using it decides. None of them acts on anything outside the `ai-playbook/` folder, and none sends anything anywhere.

## The leader check (`leader-check`)

| # | Field | Entry |
| --- | --- | --- |
| 1 | Identity and purpose | The leader check, v2.0.0. Runs the nine-question leader check with a leader or leadership team and writes the one page. |
| 2 | May read, call, write | Reads and writes files in `ai-playbook/` in the person's working folder. Nothing else |
| 3 | Must never | Invent a figure, a customer, a person or a business name. Claim how the business compares with others; reword the board sentence; show the scores. |
| 4 | Grade | Recommend: it drafts, the person decides |
| 5 | Supervisor | David Reynolds |
| 6 | Model per step | Whichever model the person's Claude is using. Re-tested against the test set when a new model is released |
| 7 | Test set | `evals/` v1: `leader-assuming`, `leader-no-strong-ground`, `leader-first-question`, `trigger-honest-read`. Last run 28 September 2026: see above |
| 8 | Cost and health | Runs in the person's own Claude session. Issues opened against the skill are the exception rate |
| 9 | History | v1.0 to v1.5, September 2026: built and revised. v2.0.0, 28 September 2026: the rules found in testing added, and the test set written. Decided by David Reynolds |
| 10 | Flags | Users are told what it does in the README. Nothing is stored outside the person's own folder |

## Where the time goes (`where-the-time-goes`)

| # | Field | Entry |
| --- | --- | --- |
| 1 | Identity and purpose | Where the time goes, v2.0.0. Maps one workflow with the four questions, finds the waiting, sorts every step into delete, automate or augment. |
| 2 | May read, call, write | Reads and writes files in `ai-playbook/` in the person's working folder. Nothing else |
| 3 | Must never | Invent a figure, a customer, a person or a business name. Invent a time; delete a step something requires. |
| 4 | Grade | Recommend: it drafts, the person decides |
| 5 | Supervisor | David Reynolds |
| 6 | Model per step | Whichever model the person's Claude is using. Re-tested against the test set when a new model is released |
| 7 | Test set | `evals/` v1: `time-waiting`. Last run 28 September 2026: see above |
| 8 | Cost and health | Runs in the person's own Claude session. Issues opened against the skill are the exception rate |
| 9 | History | v1.0 to v1.5, September 2026: built and revised. v2.0.0, 28 September 2026: the rules found in testing added, and the test set written. Decided by David Reynolds |
| 10 | Flags | Users are told what it does in the README. Nothing is stored outside the person's own folder |

## Where the revenue is (`where-the-revenue-is`)

| # | Field | Entry |
| --- | --- | --- |
| 1 | Identity and purpose | Where the revenue is, v2.0.0. Four questions for finding revenue from AI, and a check of how each offer is charged. |
| 2 | May read, call, write | Reads and writes files in `ai-playbook/` in the person's working folder. Nothing else |
| 3 | Must never | Invent a figure, a customer, a person or a business name. Invent a customer, a price or a business name; recommend cutting people. |
| 4 | Grade | Recommend: it drafts, the person decides |
| 5 | Supervisor | David Reynolds |
| 6 | Model per step | Whichever model the person's Claude is using. Re-tested against the test set when a new model is released |
| 7 | Test set | `evals/` v1: `revenue-no-inventions`. Last run 28 September 2026: see above |
| 8 | Cost and health | Runs in the person's own Claude session. Issues opened against the skill are the exception rate |
| 9 | History | v1.0 to v1.5, September 2026: built and revised. v2.0.0, 28 September 2026: the rules found in testing added, and the test set written. Decided by David Reynolds |
| 10 | Flags | Users are told what it does in the README. Nothing is stored outside the person's own folder |

## The two columns (`two-columns`)

| # | Field | Entry |
| --- | --- | --- |
| 1 | Identity and purpose | The two columns, v2.0.0. Sorts claimed AI savings from what reached the accounts, with a named line for every banked saving. |
| 2 | May read, call, write | Reads and writes files in `ai-playbook/` in the person's working folder. Nothing else |
| 3 | Must never | Invent a figure, a customer, a person or a business name. Turn hours or percentages into pounds without a rate the person gave; add the two columns together. |
| 4 | Grade | Recommend: it drafts, the person decides |
| 5 | Supervisor | David Reynolds |
| 6 | Model per step | Whichever model the person's Claude is using. Re-tested against the test set when a new model is released |
| 7 | Test set | `evals/` v1: `two-columns-claims`. Last run 28 September 2026: see above |
| 8 | Cost and health | Runs in the person's own Claude session. Issues opened against the skill are the exception rate |
| 9 | History | New in v2.0.0, 28 September 2026. Decided by David Reynolds |
| 10 | Flags | Users are told what it does in the README. Nothing is stored outside the person's own folder |

## The test set (`test-set`)

| # | Field | Entry |
| --- | --- | --- |
| 1 | Identity and purpose | The test set, v2.0.0. Starts a test set for one agent or workflow: the markers, the mix, the first real cases, the running rule. |
| 2 | May read, call, write | Reads and writes files in `ai-playbook/` in the person's working folder. Nothing else |
| 3 | Must never | Invent a figure, a customer, a person or a business name. Write a case itself, even as a placeholder; suggest sharing the set with the vendors whose models it tests. |
| 4 | Grade | Recommend: it drafts, the person decides |
| 5 | Supervisor | David Reynolds |
| 6 | Model per step | Whichever model the person's Claude is using. Re-tested against the test set when a new model is released |
| 7 | Test set | `evals/` v1: `test-set-no-invented-cases`. Last run 28 September 2026: see above |
| 8 | Cost and health | Runs in the person's own Claude session. Issues opened against the skill are the exception rate |
| 9 | History | New in v2.0.0, 28 September 2026. Decided by David Reynolds |
| 10 | Flags | Users are told what it does in the README. Nothing is stored outside the person's own folder |

## The register (`agent-register`)

| # | Field | Entry |
| --- | --- | --- |
| 1 | Identity and purpose | The register, v2.0.0. Builds or updates one register page per AI agent or tool, with the gaps first. |
| 2 | May read, call, write | Reads and writes files in `ai-playbook/` in the person's working folder. Nothing else |
| 3 | Must never | Invent a figure, a customer, a person or a business name. Accept a team, a role or IT as a supervisor. |
| 4 | Grade | Recommend: it drafts, the person decides |
| 5 | Supervisor | David Reynolds |
| 6 | Model per step | Whichever model the person's Claude is using. Re-tested against the test set when a new model is released |
| 7 | Test set | `evals/` v1: `register-gaps`. Last run 28 September 2026: see above |
| 8 | Cost and health | Runs in the person's own Claude session. Issues opened against the skill are the exception rate |
| 9 | History | v1.0 to v1.5, September 2026: built and revised. v2.0.0, 28 September 2026: the rules found in testing added, and the test set written. Decided by David Reynolds |
| 10 | Flags | Users are told what it does in the README. Nothing is stored outside the person's own folder |

## Gate review (`gate-review`)

| # | Field | Entry |
| --- | --- | --- |
| 1 | Identity and purpose | Gate review, v2.0.0. Checks whether an agent has earned its grade against criteria written in advance, including an override analysis. |
| 2 | May read, call, write | Reads and writes files in `ai-playbook/` in the person's working folder. Nothing else |
| 3 | Must never | Invent a figure, a customer, a person or a business name. Lower a threshold to make an agent pass; skip a grade. |
| 4 | Grade | Recommend: it drafts, the person decides |
| 5 | Supervisor | David Reynolds |
| 6 | Model per step | Whichever model the person's Claude is using. Re-tested against the test set when a new model is released |
| 7 | Test set | `evals/` v1: `gate-cluster-not-yet`, `gate-skip-to-act`, `gate-criteria-after`. Last run 28 September 2026: see above |
| 8 | Cost and health | Runs in the person's own Claude session. Issues opened against the skill are the exception rate |
| 9 | History | v1.0 to v1.5, September 2026: built and revised. v2.0.0, 28 September 2026: the rules found in testing added, and the test set written. Decided by David Reynolds |
| 10 | Flags | Users are told what it does in the README. Nothing is stored outside the person's own folder |

## Curriculum grid (`curriculum-grid`)

| # | Field | Entry |
| --- | --- | --- |
| 1 | Identity and purpose | Curriculum grid, v2.0.0. Sorts a team's junior work by what it's worth and what it taught, and records which work is kept for people. |
| 2 | May read, call, write | Reads and writes files in `ai-playbook/` in the person's working folder. Nothing else |
| 3 | Must never | Invent a figure, a customer, a person or a business name. Delete work a regulation, standard, contract or client requires; recommend cutting people. |
| 4 | Grade | Recommend: it drafts, the person decides |
| 5 | Supervisor | David Reynolds |
| 6 | Model per step | Whichever model the person's Claude is using. Re-tested against the test set when a new model is released |
| 7 | Test set | `evals/` v1: `curriculum-required-work`. Last run 28 September 2026: see above |
| 8 | Cost and health | Runs in the person's own Claude session. Issues opened against the skill are the exception rate |
| 9 | History | v1.0 to v1.5, September 2026: built and revised. v2.0.0, 28 September 2026: the rules found in testing added, and the test set written. Decided by David Reynolds |
| 10 | Flags | Users are told what it does in the README. Nothing is stored outside the person's own folder |

## Self-check (`self-check`)

| # | Field | Entry |
| --- | --- | --- |
| 1 | Identity and purpose | Self-check, v2.0.0. Runs the thirty-point self-check, counting only statements with evidence. |
| 2 | May read, call, write | Reads and writes files in `ai-playbook/` in the person's working folder. Nothing else |
| 3 | Must never | Invent a figure, a customer, a person or a business name. Count "sort of" or "working on it" as a tick. |
| 4 | Grade | Recommend: it drafts, the person decides |
| 5 | Supervisor | David Reynolds |
| 6 | Model per step | Whichever model the person's Claude is using. Re-tested against the test set when a new model is released |
| 7 | Test set | `evals/` v1: `self-check-strict`. Last run 28 September 2026: see above |
| 8 | Cost and health | Runs in the person's own Claude session. Issues opened against the skill are the exception rate |
| 9 | History | v1.0 to v1.5, September 2026: built and revised. v2.0.0, 28 September 2026: the rules found in testing added, and the test set written. Decided by David Reynolds |
| 10 | Flags | Users are told what it does in the README. Nothing is stored outside the person's own folder |

## The rules for changing a skill

- Any change to what a skill may read or write is a new version, and its cases are re-run before it's released.
- A new model doesn't change a skill's grade, but the whole test set is re-run against it.
- A skill that fails a case isn't released until it passes, or until the case is changed on the record in the changelog, with the reason.

Made with How I run it, by David Reynolds · ai.valuecreator.io · CC BY 4.0
