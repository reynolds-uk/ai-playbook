# AI playbook

Working tools for whoever owns AI in a business: where to point it, how to prove it works, who's on the hook, and how to keep the judgement a business runs on. By David Reynolds. The reasoning behind each tool is at [ai.valuecreator.io](https://ai.valuecreator.io).

Each skill interviews you in plain English, one question at a time, and writes a page you can keep or take into a meeting. It suggests; you decide. It never invents a figure, a customer or a name: anything you don't know is written down as "unknown, find out".

## Start here

- **If you lead a business:** ask for the leader check. Nine plain questions, five minutes, and one page with where you stand, one place to start and a sentence for your board.
- **If you're the one building it:** ask for the self-check. Thirty statements that only count if you can show the evidence.

You don't need the skill names. Asking "how is our AI going?" or "who is accountable for the AI acting in our name?" is enough.

## The ten skills

| Skill | What it does |
| --- | --- |
| Leader check | Nine questions and one page: where you stand, one place to start, three questions for the team, a sentence for the board |
| Where the time goes | One workflow end to end, the waiting found, and every step sorted into delete, automate or augment |
| Where the revenue is | Four questions for finding revenue, not only savings, and a check of how you charge |
| The two columns | What AI is said to save, kept apart from what reached the accounts |
| The test set | Your own real cases, with the right answers marked by your best people |
| The register | One page per AI agent or tool acting for you, with a named person on the hook |
| Gate review | Whether an agent has earned its grade, against criteria written in advance |
| Curriculum grid | Which junior work to keep for people, because it's how they learn |
| Where each model runs | Which model each step of a workflow uses, and whether it's rented, licensed, hosted or run in-house |
| Self-check | Thirty statements that only count with evidence |

## What it keeps

Every skill writes into one folder, `ai-playbook/`, where you're working, and reads what's already there. The register, the test sets, the two columns and the pages build on each other. Each decision you make is added to `ai-playbook/decisions.md`: the date, the decision, who made it and on what evidence. Over time that folder becomes the record your AI runs on and a competitor can't buy.

## What it does and doesn't do

- It only reads and writes files in the `ai-playbook/` folder. It has no code, no connectors and no network calls, and it sends nothing anywhere.
- Don't paste anything confidential into a tool your business doesn't control. Describe the work instead; the skills remind you.
- The judgements are yours. The skills draft the grid, the register or the page; what a task taught, what good looks like and who's accountable have to come from you.

## Tested like the rest of the playbook

The plugin has its own test set, as the playbook says every AI tool should: eighteen cases with the right outcome marked, run on every change with `claude plugin eval`. The register of the skills themselves, with their grade and last results, including what still fails, is in [REGISTER.md](https://github.com/reynolds-uk/ai-playbook/blob/main/plugins/ai-playbook/REGISTER.md).

## More

The full playbook, eleven tools as plain markdown templates, is at [github.com/reynolds-uk/ai-playbook](https://github.com/reynolds-uk/ai-playbook). Free to use under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If a skill doesn't do what you expected, [tell me](https://github.com/reynolds-uk/ai-playbook/issues/new?template=i-used-a-tool.md).
