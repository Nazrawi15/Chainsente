#!/usr/bin/env python3
# Simple price oracle simulator that emits signed-like price datapoints (placeholder)
import json, time, sys
def make_feed():
    feed = []
    steps = [
      ("2025-01-01T00:00:00Z", 1023),
      ("2025-01-02T00:00:00Z", 700),
      ("2025-01-03T00:00:00Z", 500),
    ]
    for t,p in steps:
        feed.append({"time":t, "ada_usd_cents":p})
    return feed

if __name__ == '__main__':
    print(json.dumps(make_feed(), indent=2))
