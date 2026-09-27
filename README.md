# How I run it: an AI playbook

Working tools for the future of work: where to point AI, how to prove it works, who's on the hook, and how to keep the judgement a business runs on.

By David Reynolds. The reasoning behind every tool is written up at [ai.valuecreator.io](https://ai.valuecreator.io). This repository is the part you can pick up and use.

I'm optimistic about AI. This is my playbook for the person who owns AI in a business, whatever the title: chief AI officer, chief digital officer, operating partner or founder. The tools are how I'd get the value out of AI without losing the judgement a business runs on.

## Two ways in

**If you lead a business.** Start with [the leader check](leader-check.md): nine plain questions, five minutes, nothing to look up. There's a web version at [ai.valuecreator.io/where-you-are](https://ai.valuecreator.io/where-you-are). Every tool folder opens with a one-page README in plain English, so you can see what each one is for without reading the working files.

**If you're the one building it.** Start with [the self-check](self-check.md): thirty statements you can only tick if you can show the evidence. Then use the working files in each tool folder with your own team. Or install the Claude plugin below, which runs five of the exercises with you.

The same material serves both readers. The leader needs to know what to ask for and why. The builder needs the files. Most of my career has been spent between those two people.

## The eleven tools

In the order I use them. Most take an afternoon.

| | Tool | What it's for | Files |
| --- | --- | --- | --- |
| **Aim it** | | | |
| 1 | [The four questions](tools/01-four-questions/) | Find where the time really goes before choosing where to point AI | `canvas.md` |
| 2 | [Delete, automate, augment](tools/02-delete-automate-augment/) | Sort every step before building anything | `sort.md` |
| 3 | [Stages and gates](tools/03-stages-and-gates/) | One workflow at a time, with a go or stop decision at each stage | `gate-sheet.md` |
| **Prove it** | | | |
| 4 | [The two columns](tools/04-two-columns/) | Keep what AI is said to save apart from what reaches the accounts | `claimed-banked.csv` |
| 5 | [The test set](tools/05-test-set/) | Your own cases, with the right answers marked | `method.md`, `case-template.md` |
| 6 | [The grades and the gates](tools/06-grades-and-gates/) | Let software earn autonomy against a written standard | `criteria.md`, `override-analysis.md` |
| 7 | [The register](tools/07-register/) | One page per agent, and a named person on the hook | `register-template.md`, `.csv` |
| **Keep it** | | | |
| 8 | [The curriculum exercise](tools/08-curriculum/) | Keep the work that teaches | `grid.md`, `tasks.csv` |
| 9 | [The model, step by step](tools/09-model-routing/) | The cheapest model that passes your tests, per step | `per-step.md` |
| 10 | [The first ninety days](tools/10-first-ninety-days/) | Start on a Monday | `plan-small.md`, `plan-large.md` |
| 11 | [Who owns it](tools/11-who-owns-it/) | What the role owns and what it's measured on | `role-brief.md` |

There's also [the layer you own](architecture/the-layer-you-own.md): how I'd put AI into a services business, as a reference architecture.

## Sized for you

Every tool works for a team of five or a group of five thousand. Where the advice differs, the file says so under **Small team** and **Large business**. If you're under about fifty people, one person can own all of this alongside the day job.

## Using it with an AI assistant

The templates are plain markdown, so they work in any assistant or none. Paste a template in with your own material (a process description, a task list, a spreadsheet of past cases) and ask it to fill the template in with you. Two cautions. Don't paste anything confidential into a tool your business doesn't control. And the assistant can draft the grid or the register, but the judgements in them (what a task taught, what good looks like, who's accountable) have to be yours.

## The Claude plugin

This repository is also a Claude Code plugin marketplace. The plugin turns five of the tools into skills that interview you and write the file.

```
claude plugin marketplace add reynolds-uk/ai-playbook
claude plugin install ai-playbook@ai-playbook
```

Then, in a session: `/ai-playbook:where-the-time-goes`, `/ai-playbook:curriculum-grid`, `/ai-playbook:agent-register`, `/ai-playbook:gate-review` or `/ai-playbook:self-check`.

These are early. If one doesn't do what you expected, open an issue and tell me.

## Licence

[CC BY 4.0](LICENSE). Use it, change it, share it, including commercially. Credit it as: *David Reynolds, How I run it, ai.valuecreator.io*.

## Feedback

If you've used a tool, [tell me how it went](../../issues/new?template=i-used-a-tool.md): what you changed to make it fit, and what didn't work. A sentence each is plenty. Or find me on [LinkedIn](https://www.linkedin.com/in/davidreynolds/).
