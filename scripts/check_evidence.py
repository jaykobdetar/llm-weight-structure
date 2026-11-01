#!/usr/bin/env python3
"""Verify only the bytes of the included evidence; performs no model work."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
manifest = json.loads((ROOT / 'evidence' / 'MANIFEST.json').read_text(encoding='utf-8'))
failures = []
for entry in manifest['entries']:
    target = (ROOT / entry['file']).resolve()
    if not target.is_relative_to(ROOT / 'evidence') or not target.is_file():
        failures.append(entry['file'] + ': missing or outside evidence')
        continue
    data = target.read_bytes()
    if len(data) != entry['bytes'] or hashlib.sha256(data).hexdigest() != entry['sha256']:
        failures.append(entry['file'] + ': size/hash mismatch')
if failures:
    raise SystemExit('\n'.join(failures))
print(f"OK: {len(manifest['entries'])} included evidence files match their manifest")
