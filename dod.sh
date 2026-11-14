#!/usr/bin/env bash
# Pack 63b definition of done. Run from the playbook repo root after apply-63b.py.
fail=0
ok(){ if eval "$2"; then echo "PASS  $1"; else echo "FAIL  $1"; fail=1; fi; }
ok "README intro reframed"            'grep -q "for the people who run a business and have to decide where AI goes" README.md'
ok "plugin README intro reframed"     'grep -q "for the people who run a business and have to decide where AI goes" plugins/ai-playbook/README.md'
ok "no 'whoever owns AI in a business' left in README or marketplace" '! grep -q "whoever owns AI in a business" README.md .claude-plugin/marketplace.json plugins/ai-playbook/README.md'
ok "README no longer repeats test results" '! grep -q "thirteen passed" README.md'
ok "register says two cases not run"  'grep -q "have not been run yet" plugins/ai-playbook/REGISTER.md'
ok "changelog has v2.1.2"             'grep -q "^## v2.1.2" CHANGELOG.md'
ok "versions are 2.1.2"               'grep -q "\"version\": \"2.1.2\"" .claude-plugin/marketplace.json && grep -q "\"version\": \"2.1.2\"" plugins/ai-playbook/.claude-plugin/plugin.json'
ok "JSON files parse"                 'node -e "JSON.parse(require(\"fs\").readFileSync(\".claude-plugin/marketplace.json\"));JSON.parse(require(\"fs\").readFileSync(\"plugins/ai-playbook/.claude-plugin/plugin.json\"))"'
ok "no day-first dates left in prose" '! grep -rnE "(^|[^0-9a-z])[0-9]{1,2} (September|October|November) 20[0-9]{2}" README.md CHANGELOG.md plugins/ai-playbook/REGISTER.md examples/README.md examples/leader-check.md'
ok "no skill file changed"            '[ -z "$(git diff --name-only | grep SKILL.md)" ]'
ok "relative links in README resolve" 'grep -oE "\]\(([^)#h][^)]*)\)" README.md | sed -E "s/^\]\(//;s/\)$//" | while read p; do [ -e "$p" ] || { echo "missing: $p"; exit 1; }; done'
[ $fail = 0 ] && echo "ALL PASS" || echo "SOME FAILED"; exit $fail
