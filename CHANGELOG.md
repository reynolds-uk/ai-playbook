# Changelog

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
