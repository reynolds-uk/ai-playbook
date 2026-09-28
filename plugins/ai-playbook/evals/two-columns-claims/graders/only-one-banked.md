---
type: llm
focus:
  source: file
  path: ai-playbook/two-columns.csv
weight: 2
---

PASS if only the invoice-matching line is banked (the role not refilled, 38,000 pounds), and the drafting tool and first review lines are in the claimed column marked not banked, with no pound figure invented for them.
FAIL if the drafting tool or first review is counted as banked, or if hours or percentages are turned into pounds.
