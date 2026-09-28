#!/bin/bash
set -e
mkdir -p ai-playbook
cat > ai-playbook/register.md <<'EOF'
# Register

| Agent | Grade | Supervisor | Test set |
| --- | --- | --- | --- |
| Invoice matching v2.1 | Recommend | Jo Adams | Yes |

## Invoice matching v2.1

- Identity and purpose: matches supplier invoices to purchase orders for the finance team.
- Grade: Recommend
- Supervisor: Jo Adams
- Test set: invoice-matching v3, 120 cases, last score 96%
- History:
  - 2026-06-02: criteria for Prepare written and signed by Jo Adams
EOF
