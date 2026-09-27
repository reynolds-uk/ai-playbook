---
name: gate-review
description: "Check whether an AI agent has earned its grade (Observe, Recommend, Prepare, Act) against criteria written in advance, including an override analysis. Use when deciding whether to promote or demote an agent."
---

# Gate review

You are helping someone decide whether an agent has earned its grade, using David Reynolds's grades and gates. Be precise and plain.

## Steps

1. Ask which agent and version, what grade it holds now, and for the written criteria for the next grade. If no criteria were written before measuring started, say that nothing above Observe can be earned against a bar set afterwards, help them write criteria now, and stop the review there.
2. Ask for the evidence the criteria need:
   - Observe to Recommend: agreement rate with the person's decision, and over how many cases
   - Recommend to Prepare: acceptance rate, plus the overrides (see step 3)
   - Prepare to Act: approval without material changes over a set period, a clean test-set run, a supervisor's signature and a way to reverse its actions
3. Override analysis, for the gate out of Recommend: ask for the overridden cases and the reasons. If they cluster, the agent is wrong in a fixable way: fix it before promoting. If they're scattered, the people disagree with each other: that's the finding.
4. Check the automatic demotion triggers: drift against the test set, too many exceptions, a new market or team, any change to permissions or retrieval. Any one of them means back to Observe. A new model is different: it re-runs the test set, and the agent keeps its grade only if it passes.
5. Give the verdict in one line: earned, not yet (with exactly what's missing), assumed (holds a grade the evidence doesn't support), or demote. Write `gate-review-<agent>-<date>.md` with the criteria, the evidence, the verdict and the entry to add to the register's history.

## Rules

- Never lower a threshold to make an agent pass.
- Record the decision and the person who made it.
