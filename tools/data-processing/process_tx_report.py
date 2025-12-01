#!/usr/bin/env python3
# Lightweight script to assemble tx report CSV from a JSON replay output
import sys, json, csv
if len(sys.argv)<3:
    print('usage: process_tx_report.py replay.json out.csv')
    sys.exit(1)
with open(sys.argv[1]) as f:
    data=json.load(f)
with open(sys.argv[2],'w',newline='') as out:
    w=csv.writer(out)
    w.writerow(['time','ada_usd_cents','collateral_usd_cents','ltv_bp','liquidation'])
    for s in data:
        w.writerow([s['time'], s['ada_usd_cents'], s['collateral_usd_cents'], s['ltv_bp'], s.get('liquidation','')])
print('wrote', sys.argv[2])
