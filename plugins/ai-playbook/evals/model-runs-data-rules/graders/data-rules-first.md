---
type: llm
focus:
  source: file
  path: ai-playbook/where-each-model-runs-test.md
weight: 2
---

PASS if all of these hold:
- the German medical-records step is licensed in an EU region or hosted, not sent to a model wherever the vendor chooses;
- the fraud-flag step is hosted (or otherwise pinned) so the business decides when the version changes;
- the high-volume extraction step goes to the cheapest model that passes, such as a small hosted model;
- the Friday test is marked as failing because the prompts live in the vendor's agent builder and there is no test set, and the file says what has to move;
- the decline letter stays with a person.
FAIL if cost decides any step ahead of a data rule, or the Friday test is passed despite the prompts sitting in the vendor's product.
