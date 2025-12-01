#!/usr/bin/env python3
# Simple script to read replay-output.json and produce a small HTML summary (placeholder)
import json,sys
if len(sys.argv)<2:
    print('usage: build_dashboard.py replay-output.json')
    sys.exit(1)
with open(sys.argv[1]) as f:
    data=json.load(f)
html=['<html><body><h1>Chainsente Replay Dashboard</h1><table border=1>']
html.append('<tr><th>time</th><th>ada_usd_cents</th><th>ltv_bp</th><th>liquidation</th></tr>')
for s in data:
    html.append(f"<tr><td>{s['time']}</td><td>{s['ada_usd_cents']}</td><td>{s['ltv_bp']}</td><td>{s.get('liquidation','')}</td></tr>")
html.append('</table></body></html>')
open('dashboard.html','w').write('\n'.join(html))
print('dashboard.html written')
