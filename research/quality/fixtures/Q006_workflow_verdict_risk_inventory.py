#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, re

ROOT = Path('.github/workflows')
PATTERNS = {
    'pipeline_tee': re.compile(r'\|\s*tee(?:\s|$)'),
    'continue_on_error': re.compile(r'continue-on-error\s*:\s*true', re.I),
    'or_true': re.compile(r'\|\|\s*true(?:\s|$)'),
    'set_plus_e': re.compile(r'\bset\s+\+e\b'),
    'trap': re.compile(r'\btrap\b'),
    'exit_zero': re.compile(r'\bexit\s+0\b'),
    'always': re.compile(r'if\s*:\s*always\(\)'),
}

files = sorted([*ROOT.glob('*.yml'), *ROOT.glob('*.yaml')])
assert files, 'no workflow files found'
rows=[]
for p in files:
    text=p.read_text(encoding='utf-8')
    for n,line in enumerate(text.splitlines(),1):
        for kind,rx in PATTERNS.items():
            if rx.search(line):
                rows.append({'file':str(p),'line':n,'kind':kind,'text':line.strip()})
manifest={
    'workflow_count':len(files),
    'workflow_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
    'risk_hits':rows,
}
Path('q006-workflow-verdict-risk-inventory.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
print(f'Q006_WORKFLOW_COUNT={len(files)}')
print(f'Q006_RISK_HIT_COUNT={len(rows)}')
for r in rows:
    print(f"{r['kind']}\t{r['file']}:{r['line']}\t{r['text']}")
print('Q006_WORKFLOW_VERDICT_RISK_INVENTORY_PASS')
