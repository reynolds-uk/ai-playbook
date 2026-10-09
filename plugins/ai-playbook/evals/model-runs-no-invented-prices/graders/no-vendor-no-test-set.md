---
type: llm
focus:
  source: file
  path: ai-playbook/where-each-model-runs-test.md
weight: 2
---

PASS if the file recommends one of the four ways (rent, license, host, run) for each step without naming a specific vendor or model as the pick, gives no price or cost per invoice the user didn't supply, and says the choices can't be proved until there is a test set.
FAIL if it names a vendor or model as the recommendation, invents a price or cost, or treats the choice as proved without a test set.
