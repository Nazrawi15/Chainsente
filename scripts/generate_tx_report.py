#!/usr/bin/env python3
# Example to process replay-output.json and generate a tx-report CSV
import sys, json, csv
if len(sys.argv)<3:
    print('usage: generate_tx_report.py replay.json out.csv')
    sys.exit(1)
with open(sys.argv[1]) as f:
    data=json.load(f)
with open(sys.argv[2],'w',newline='') as out:
    w=csv.writer(out)
    w.writerow(['time','ltv_bp','liquidation_sell_lovelace'])
    for s in data:
        l = ''
        if s.get('liquidation'):
            l = s['liquidation']['sell_lovelace']
        w.writerow([s['time'], s['ltv_bp'], l])
print('wrote', sys.argv[2])
