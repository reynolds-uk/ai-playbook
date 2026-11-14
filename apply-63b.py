#!/usr/bin/env python3
"""Pack 63b · playbook repo (reynolds-uk/ai-playbook): wording, honest test claims, ordinal dates.
Run from the repo root. Exact-string edits, atomic, rerun guard."""
import re, sys, pathlib, json
ROOT = pathlib.Path.cwd()
rd = lambda p: (ROOT / p).read_text(encoding="utf-8")

if "## v2.1.2" in rd("CHANGELOG.md"):
    print("Pack 63b already applied. Nothing changed."); sys.exit(1)

OLD_INTRO = "Working tools for whoever owns AI in a business: where to point it,"
NEW_INTRO = "Working tools for the people who run a business and have to decide where AI goes: where to point it,"

EDITS = [
 ("README.md", OLD_INTRO, NEW_INTRO),
 ("plugins/ai-playbook/README.md", OLD_INTRO, NEW_INTRO),
 (".claude-plugin/marketplace.json",
  "working tools for whoever owns AI in a business, as a Claude plugin.",
  "working tools for the people who run a business and have to decide where AI goes, as a Claude plugin."),
 (".claude-plugin/marketplace.json", '"version": "2.1.1"', '"version": "2.1.2"'),
 ("plugins/ai-playbook/.claude-plugin/plugin.json", '"version": "2.1.1"', '"version": "2.1.2"'),
 # README: stop repeating results that age; the register is the one place for them
 ("README.md",
  "run with `claude plugin eval` on every change. On 28 September 2026, thirteen passed every run and three passed two runs in three. The register says which, and they're the next things to fix.",
  "run with `claude plugin eval`. The [register](plugins/ai-playbook/REGISTER.md) is the one place that says when it was last run, what passed and what didn't, including what still fails."),
 # Register: say plainly which cases have not been run
 ("plugins/ai-playbook/REGISTER.md",
  "Two of the cases check that nothing in the plugin fires on unrelated requests.",
  "Two of the cases check that nothing in the plugin fires on unrelated requests. Two further cases, `model-runs-data-rules` and `model-runs-no-invented-prices`, were added in v2.1 and have not been run yet."),
 ("CHANGELOG.md", "# Changelog\n",
  "# Changelog\n\n## v2.1.2 · November 2026\n\n- **Wording only.** The playbook is now described for the people who run a business and have to decide where AI goes, not only whoever owns it day to day. The README no longer repeats the test results: the [register](plugins/ai-playbook/REGISTER.md) is the one place they live, and it now says which two cases have not been run yet. Dates in prose use ordinals. No skill changed.\n"),
]

ORD = lambda n: f"{n}{'th' if 11 <= n % 100 <= 13 else {1:'st',2:'nd',3:'rd'}.get(n % 10,'th')}"
DATE = re.compile(r"\b(\d{1,2}) (September|October|November) (20\d\d)\b")
ORD_FILES = ["README.md", "CHANGELOG.md", "plugins/ai-playbook/REGISTER.md", "examples/README.md", "examples/leader-check.md"]

staged = {}
for f, old, new in EDITS:
    t = staged.get(f, rd(f))
    n = t.count(old)
    if n != 1:
        print(f"FAIL: expected one match in {f}, found {n}: {old[:80]}"); sys.exit(2)
    staged[f] = t.replace(old, new)
for f in ORD_FILES:
    t = staged.get(f, rd(f))
    staged[f] = DATE.sub(lambda m: f"{ORD(int(m.group(1)))} {m.group(2)} {m.group(3)}", t)
for f in staged:
    if f.endswith(".json"): json.loads(staged[f])
for f, t in staged.items():
    (ROOT / f).write_text(t, encoding="utf-8")
print(f"Pack 63b applied to {len(staged)} files.")
