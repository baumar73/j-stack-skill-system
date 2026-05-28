#!/usr/bin/env python3
from pathlib import Path
import re, sys, json
try:
    import yaml
except Exception:
    yaml = None
root = Path(__file__).resolve().parents[1]
errors = []
rows = []
for p in sorted((root/'skills').glob('*/SKILL.md')):
    content = p.read_text(encoding='utf-8')
    rel = str(p.relative_to(root))
    if not content.startswith('---'):
        errors.append(f'{rel}: missing frontmatter start')
        continue
    m = re.search(r'\n---\s*\n', content[3:])
    if not m:
        errors.append(f'{rel}: missing frontmatter close')
        continue
    fm_text = content[3:3+m.start()]
    if yaml:
        try:
            fm = yaml.safe_load(fm_text)
        except Exception as e:
            errors.append(f'{rel}: yaml parse failed: {e}')
            continue
    else:
        fm = {}
        for line in fm_text.splitlines():
            if ':' in line and not line.startswith(' '):
                k,v = line.split(':',1); fm[k.strip()] = v.strip()
    for key in ('name','description'):
        if key not in fm or not fm[key]:
            errors.append(f'{rel}: missing {key}')
    name = fm.get('name','')
    desc = fm.get('description','')
    if len(name) > 64 or not re.match(r'^[a-z0-9][a-z0-9-]*$', name):
        errors.append(f'{rel}: invalid name {name!r}')
    if len(desc) > 1024:
        errors.append(f'{rel}: description too long')
    if len(content) > 100000:
        errors.append(f'{rel}: content too large')
    body = content.split('\n---\n',1)[1].strip() if '\n---\n' in content else ''
    required = ['## Overview','## When to Use','## GBrain Integration','## Common Pitfalls','## Verification Checklist']
    for marker in required:
        if marker not in body:
            errors.append(f'{rel}: missing {marker}')
    rows.append({'path':rel,'name':name,'description_len':len(desc),'chars':len(content)})
print(json.dumps({'skill_count':len(rows),'errors':errors,'skills':rows}, indent=2))
sys.exit(1 if errors else 0)
