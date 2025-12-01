#!/usr/bin/env bash
# Placeholder: gathers reports/evidence and zips them for release attachments
OUT=${1:-evidence_bundle.zip}
zip -r "$OUT" reports/evidence
echo "Wrote $OUT"
