# The test set

**Small team:** one per workflow, start with thirty cases. **Large business:** one per workflow per market, start with fifty and grow it.

## In plain terms

A set of real cases from your own work, with the right answer marked by the people qualified to judge. It's the real answer to "how do you know it works?", and it's what lets you test a new model in a day rather than a quarter. Vendors' tools can run your tests. They never write them, and you don't share the cases with the vendors whose models they test.

## What to ask for

The set, its version, who marked it, and the score of the last run. Ask whether it has been shared with any vendor whose models it tests. The answer should be no.

The reasoning is in [Earned autonomy](https://ai.valuecreator.io/read/control#test-set).

## Files

- [`method.md`](method.md): how to build and keep it.
- [`case-template.md`](case-template.md): one case.

In Claude, `/ai-playbook:test-set` starts a test set with you: the markers, the mix and the first real cases.
