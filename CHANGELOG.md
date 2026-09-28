# Changelog

## v2.0 · September 2026

The playbook now runs its own playbook, and the plugin was tested end to end before release.

- **A test set for the plugin.** Sixteen cases in [plugins/ai-playbook/evals](plugins/ai-playbook/evals/), each with the right outcome marked, run with `claude plugin eval` on every change. On 28 September 2026, thirteen passed every one of three runs and three passed two in three.
- **A register for the plugin.** [REGISTER.md](plugins/ai-playbook/REGISTER.md) has one page per skill: grade, supervisor, test set, what it must never do. Every skill is at Recommend.
- **Two new skills.** `/ai-playbook:test-set` starts a test set with your own real cases, and won't invent one. `/ai-playbook:two-columns` sorts claimed savings from what reached the accounts. The plugin now has nine skills.
- **One folder, and a record of decisions.** Every skill writes into `ai-playbook/` and reads what's already there. The gate review adds to the register's history. Each decision goes into `ai-playbook/decisions.md` with the date, who decided and on what evidence.
- **Fixes from testing every skill with realistic users:**
  - One question per turn in every skill, with clickable choices where Claude offers them.
  - The leader check labels answers A to D and never shows a score. When nothing scores well, the board sentence says there's no strong ground yet, rather than naming a strength.
  - The register gives the gaps in five minutes, then writes full pages for the riskiest agents first.
  - Nothing a regulation, standard, contract or client requires is put in Delete, in the curriculum grid or in where the time goes.
  - No invented names, prices or cases; "to confirm" where a name is missing.
  - A reminder not to paste confidential material, in every skill that takes your material.
  - Plain writing rules, and a credit line at the foot of every page a skill writes.
  - Descriptions tuned so plain requests find the right skill: eight of eight in testing, and nothing fires on unrelated requests.
- **A README inside the plugin**, for listing in Anthropic's plugin directory, and a front page that says how to install in the first screen.
- **Examples.** [examples/](examples/) has a page from each of four skills, made for fictional businesses.
- **An issue template for a skill getting something wrong.** Every report becomes a test case.

## v1.5 · September 2026

- Two new skills in the Claude plugin: `/ai-playbook:leader-check`, which runs the nine-question leader check and writes the one page, and `/ai-playbook:where-the-revenue-is`.
- [Where the revenue is](where-the-revenue-is.md): four questions for finding revenue from AI, not only savings, and a check of how you charge. It goes with [Pay for the outcome](https://ai.valuecreator.io/read/pay-for-the-outcome).
- The curriculum grid uses the same box names as the site and the diagram: automate it, a person decides, delete it, keep a share. It links to a worked example, [A junior's week](https://ai.valuecreator.io/read/a-juniors-week).
- [CONTRIBUTING.md](CONTRIBUTING.md), a template for suggesting a change, and a pull request template.
- The leader check wording matches the web version.

## v1.4 · September 2026

- The leader check matches the web version again. Question 2 now asks whether AI shows up in your plan as savings, as new revenue, or both, and how you charge for it. Deleting steps before automating moves into the top answer to question 1, and into [delete, automate, augment](tools/02-delete-automate-augment/).
- A team question on revenue, and a pointer to [Pay for the outcome](https://ai.valuecreator.io/read/pay-for-the-outcome).

## v1.3 · September 2026

- A new model no longer sends an agent back to Observe. It is re-tested against the test set and keeps its grade only if it passes. A change to what an agent may touch or look up still starts it again at Observe. The register, the criteria, the gate review and the self-check all say the same thing.
- The test set: your own people write it, vendors' tools may run it, and it isn't shared with the vendors whose models it tests. Worded the same way everywhere.
- Plainer, more careful wording in the READMEs, and fewer absolute claims.
- The leader check scores "gut feel" below "if a pilot looks good", to match the web version, and says question 5 isn't scored.
- Worked examples: a workflow column and placeholders in the register CSV, placeholders in the two-columns CSV, an example row in the curriculum task list, and short definitions of the agent standard and the scorecard in the ninety-day plans.
- The plugin version now matches the release.

## v1.2 · September 2026

- The repository is now reynolds-uk/ai-playbook, and the README says plainly what it is: my AI playbook for whoever owns AI in a business. The old address redirects here.
- The plugin and its marketplace are renamed to match: install with `claude plugin marketplace add reynolds-uk/ai-playbook`, then `claude plugin install ai-playbook@ai-playbook`. The skills are now `/ai-playbook:where-the-time-goes` and so on.

## v1.1 · September 2026

- The register template now includes a worked example, as a page and as a row in the CSV.
- A short issue template for telling me how a tool worked in your business.
- One line in the README on where I stand: optimistic about AI.

## v1.0 · September 2026

First public version. Eleven tools, the leader check, the self-check, the services reference architecture, and a Claude plugin with five skills.
