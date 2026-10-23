#!/usr/bin/env bash
# Download the Sudden Cardiac Death Holter records listed in records.txt into data/
# (header, signal and beat annotation files).
set -euo pipefail
cd "$(dirname "$0")"
BASE=https://physionet-open.s3.amazonaws.com/sddb/1.0.0   # PhysioNet open-data mirror (physionet.org is slow)
mkdir -p data
grep -v '^#' records.txt | awk 'NF {print $1}' | while read -r rec; do
    for ext in hea dat ari atr; do
        [ -f "data/$rec.$ext" ] || curl -sfo "data/$rec.$ext" "$BASE/$rec.$ext" || true   # atr exists for 12 records only
    done
    echo "$rec"
done
