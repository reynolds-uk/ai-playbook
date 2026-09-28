# How I run it: an AI playbook

Working tools for whoever owns AI in a business: where to point it, how to prove it works, who's on the hook, and how to keep the judgement a business runs on. By David Reynolds. The reasoning behind every tool is at [ai.valuecreator.io](https://ai.valuecreator.io).

**Use it in Claude.** Nine of the exercises are a Claude plugin: each one interviews you, one question at a time, and writes a page you can keep. In Claude Code:

```
claude plugin marketplace add reynolds-uk/ai-playbook
claude plugin install ai-playbook@ai-playbook
```

Then ask for what you need, in plain words: "how is our AI going?", "who's accountable for the AI acting for us?", "are these savings real?". [What the plugin does](plugins/ai-playbook/README.md).

**Or use the files.** Everything below is plain markdown. It works in any assistant, or on paper.

## Two ways in

**If you lead a business.** Start with [the leader check](leader-check.md): nine plain questions, five minutes, nothing to look up. There's a web version at [ai.valuecreator.io/where-you-are](https://ai.valuecreator.io/where-you-are). Every tool folder opens with a one-page README in plain English, so you can see what each one is for without reading the working files.

**If you're the one building it.** Start with [the self-check](self-check.md): thirty statements you can only tick if you can show the evidence. Then use the working files in each tool folder with your own team.

The same material serves both readers. The leader needs to know what to ask for and why. The builder needs the files. Most of my career has been spent between those two people.

I'm optimistic about AI. This is how I'd get the value out of it without losing the judgement a business runs on.

## The eleven tools

In the order I use them. Most take an afternoon. The last column is the plugin skill that runs it with you, where there is one.

| | Tool | What it's for | Files | In Claude |
| --- | --- | --- | --- | --- |
| **Aim it** | | | | |
| 1 | [The four questions](tools/01-four-questions/) | Find where the time really goes before choosing where to point AI | `canvas.md` | `where-the-time-goes` |
| 2 | [Delete, automate, augment](tools/02-delete-automate-augment/) | Sort every step before building anything | `sort.md` | `where-the-time-goes` |
| 3 | [Stages and gates](tools/03-stages-and-gates/) | One workflow at a time, with a go or stop decision at each stage | `gate-sheet.md` | |
| **Prove it** | | | | |
| 4 | [The two columns](tools/04-two-columns/) | Keep what AI is said to save apart from what reaches the accounts | `claimed-banked.csv` | `two-columns` |
| 5 | [The test set](tools/05-test-set/) | Your own cases, with the right answers marked | `method.md`, `case-template.md` | `test-set` |
| 6 | [The grades and the gates](tools/06-grades-and-gates/) | Let software earn autonomy against a written standard | `criteria.md`, `override-analysis.md` | `gate-review` |
| 7 | [The register](tools/07-register/) | One page per agent, and a named person on the hook | `register-template.md`, `.csv` | `agent-register` |
| **Keep it** | | | | |
| 8 | [The curriculum exercise](tools/08-curriculum/) | Keep the work that teaches | `grid.md`, `tasks.csv` | `curriculum-grid` |
| 9 | [The model, step by step](tools/09-model-routing/) | The cheapest model that passes your tests, per step | `per-step.md` | |
| 10 | [The first ninety days](tools/10-first-ninety-days/) | Start on a Monday | `plan-small.md`, `plan-large.md` | |
| 11 | [Who owns it](tools/11-who-owns-it/) | What the role owns and what it's measured on | `role-brief.md` | |

Also: [the leader check](leader-check.md) (`leader-check`), [the self-check](self-check.md) (`self-check`), [where the revenue is](where-the-revenue-is.md) (`where-the-revenue-is`), and [the layer you own](architecture/the-layer-you-own.md), a reference architecture for putting AI into a services business. For a worked example of the curriculum exercise, see [A junior's week](https://ai.valuecreator.io/read/a-juniors-week).

## What the plugin keeps

Every skill writes into one folder, `ai-playbook/`, and reads what's already there. The gate review adds to the register's history. The self-check looks for your register and test sets. Each decision you make goes into `ai-playbook/decisions.md`: the date, the decision, who made it and on what evidence. That folder is the start of [the layer you own](architecture/the-layer-you-own.md).

To see what the pages look like before you install anything, [examples/](examples/) has one from each of four skills, made for fictional businesses.

## The playbook runs its own playbook

The playbook says every AI tool needs a test set, a register page and a named person on the hook. The plugin is an AI tool, so it has all three:

- **A test set:** [sixteen cases](plugins/ai-playbook/evals/) with the right outcome marked, run with `claude plugin eval` on every change. On 28 September 2026, thirteen passed every run and three passed two runs in three. The register says which, and they're the next things to fix.
- **A register:** [one page per skill](plugins/ai-playbook/REGISTER.md). Every skill is at Recommend: it drafts, you decide.
- **A named person:** me.

The set is small, and I say so in the register. It grows every time someone reports a skill getting something wrong.

## Sized for you

Every tool works for a team of five or a group of five thousand. Where the advice differs, the file says so, under **Small team** and **Large business**. If you're under about fifty people, one person can own all of this alongside the day job.

## Using the files with any assistant

The templates are plain markdown. Paste one in with your own material (a process description, a task list, a spreadsheet of past cases) and ask the assistant to fill it in with you. Two cautions. Don't paste anything confidential into a tool your business doesn't control. And the assistant can draft the grid or the register, but the judgements in them (what a task taught, what good looks like, who's accountable) have to be yours.

## Helping with it

If a tool or a skill didn't work for you, [tell me how it went](https://github.com/reynolds-uk/ai-playbook/issues/new?template=i-used-a-tool.md), or report [a skill getting something wrong](https://github.com/reynolds-uk/ai-playbook/issues/new?template=skill-got-it-wrong.md): each report becomes a test case. If you're technical and want to change something, [CONTRIBUTING.md](CONTRIBUTING.md) says how. Or find me on [LinkedIn](https://www.linkedin.com/in/davidreynolds/).

## Licence

[CC BY 4.0](LICENSE). Use it, change it, share it, including commercially. Credit it as: *David Reynolds, How I run it, ai.valuecreator.io*. Every page the plugin writes ends with that credit.
