# The plugin's test set

Eighteen cases, each a real request with the right outcome marked, run with `claude plugin eval`. It follows [the test-set method](../../../tools/05-test-set/method.md): cases chosen because they're where a skill could go wrong, answers marked in advance, run on every change.

| Case | What it checks |
| --- | --- |
| `leader-assuming` | An unchecked agent puts the business in Assuming, and the start is the test set |
| `leader-no-strong-ground` | When every area is a gap, the board sentence doesn't invent a strength |
| `leader-first-question` | One question at a time, answers labelled A to D, no scores shown |
| `gate-cluster-not-yet` | A cluster of overrides means "not yet"; a re-tested model doesn't demote; the register and decisions are updated |
| `gate-skip-to-act` | Grades are earned one at a time |
| `gate-criteria-after` | Criteria written after measuring can't be earned against |
| `register-gaps` | A team is not a supervisor; acting without a test set is assumed autonomy |
| `curriculum-required-work` | Work a standard requires is never deleted |
| `model-runs-data-rules` | Data rules decide where a model runs before cost; the Friday test fails while the prompts live in the vendor's product |
| `model-runs-no-invented-prices` | No invented prices or vendor picks; a choice can't be proved without a test set |
| `time-waiting` | The prize is in the waiting; the unread report goes; the judgement stays with a person |
| `revenue-no-inventions` | No invented names or prices |
| `two-columns-claims` | Only a saving with a named line is banked |
| `test-set-no-invented-cases` | The skill won't make cases up, even when asked |
| `self-check-strict` | "Sort of" and "working on it" don't count |
| `trigger-honest-read` | A plain request finds the right skill |
| `not-triggered-recipe`, `not-triggered-code` | Nothing fires on unrelated requests |

## Running it

From `plugins/ai-playbook`:

```
claude plugin eval . --allow-tools Write Edit --scaffold
```

Each case runs three times with the plugin and three times without, so you can see what the plugin adds. Some checks look for the files the skills write (`ai-playbook/register.md`, say), so part of the difference is the plugin's folder rather than better judgement; the cases judged on the answer alone are the fairer comparison. A full run costs roughly ten US dollars at list price.

The `--scaffold` flag lets `gate-cluster-not-yet` start from a register page, using the script in its folder. Cases pin file names to the word `test` so the checks know where to look.

## Adding a case

When a skill gets something wrong, that's a case: the request, what should have happened, and a check for it. Open an issue with the "A skill got it wrong" template, or add the folder and send a pull request.
