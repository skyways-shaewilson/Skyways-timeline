#!/usr/bin/env python3
"""
Fetch authoritative, deduplicated lifetime flight stats from Airtable and write
them to Data/live_stats.json for the Timeline site to consume.

Why dedup: the Airtable base has four flight tables:

  Flights         (SKYWAYS internal — source of truth for Skyways records)
  Merged flights  (pre-joined SKYWAYS + ANA + SKYPORTS rollup)
  ANA flights     (raw)
  Skyports flights(raw)

"Merged flights" already contains SKYWAYS + ANA + SKYPORTS deduplicated —
End User distribution confirms it (SKYWAYS + ANA + SKYPORTS == row count).
However a small tail of recent Skyways flights can be missing from the merge.
To get an archive-complete, non-double-counted total we:

  totals = Merged flights
         + (Flights rows whose "Flight #" is not already in Merged[SKYWAYS])

Output schema (Data/live_stats.json):
  {
    "lifetimeFlights": <int>,
    "flightTimeSec":   <int>,
    "flightTimeHours": <float, 1 decimal>,
    "kmFlown":         <float, 1 decimal>,
    "updatedAt":       "<ISO-8601 UTC>",
    "source": "Airtable base appoHrNhrbURTxmuh — Merged flights + Flights delta"
  }

Credentials are read from .env.local (same convention as the Vercel API route).
Intended to be scheduled on a cron so the static JSON stays fresh; the frontend
polls it, so a cron cadence == effective refresh rate on the UI.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = REPO_ROOT / ".env.local"
OUTPUT_FILE = REPO_ROOT / "Data" / "live_stats.json"

FLIGHTS_TABLE = "tblqPi1dUtTjK1bhk"      # "Flights" — SKYWAYS source of truth
MERGED_TABLE = "tblb3eu5LS3aD9zVi"       # "Merged flights" — SKYWAYS + ANA + SKYPORTS rollup
# ANA / Skyports tables intentionally omitted: they are already contained in Merged.

# Pre-2024 flight archive. Airtable only goes back to Jan 3, 2024, but Skyways
# has been flying since 2017. Charles reviewed the timeline Apr 2026 and said
# lifetime flights were "nearly 3,000" — the delta between that and the live
# Airtable total is the pre-2024 archive count. Hardcoded here so the public
# counter reflects true lifetime, not just 2024-onwards. Pending a full archive
# import into Airtable; update this number if Charles provides a refined count.
PRE_2024_ARCHIVE_FLIGHTS = 1400


def load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    if not ENV_FILE.exists():
        return env
    for line in ENV_FILE.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        env[k.strip()] = v.strip().strip("'").strip('"')
    return env


def fetch_all(base_id: str, table_id: str, pat: str) -> list[dict]:
    """Paginate through an Airtable table and return every record."""
    records: list[dict] = []
    offset: str | None = None
    while True:
        qs = {"pageSize": "100"}
        if offset:
            qs["offset"] = offset
        url = (
            f"https://api.airtable.com/v0/{base_id}/{table_id}?"
            + urllib.parse.urlencode(qs)
        )
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {pat}"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.loads(resp.read().decode())
        records.extend(payload.get("records", []))
        offset = payload.get("offset")
        if not offset:
            break
    return records


def compute_totals(merged: list[dict], flights: list[dict]) -> dict:
    # Deduplicate: start with everything in Merged, then add Flights rows whose
    # Flight # is not already represented on the SKYWAYS side of Merged.
    merged_skyways_fns = {
        r["fields"].get("Flight #")
        for r in merged
        if r["fields"].get("End User") == "SKYWAYS"
        and r["fields"].get("Flight #") is not None
    }
    delta = [
        r
        for r in flights
        if r["fields"].get("Flight #") not in merged_skyways_fns
    ]

    combined = merged + delta

    airtable_flights = len(combined)
    lifetime_flights = airtable_flights + PRE_2024_ARCHIVE_FLIGHTS
    flight_time_sec = int(
        sum((r["fields"].get("Flight time (s)") or 0) for r in combined)
    )
    km_flown = float(
        sum((r["fields"].get("Dist Cruise (km)") or 0) for r in combined)
    )

    return {
        "lifetimeFlights": lifetime_flights,
        "flightTimeSec": flight_time_sec,
        "flightTimeHours": round(flight_time_sec / 3600, 1),
        "kmFlown": round(km_flown, 1),
        "breakdown": {
            "mergedRecords": len(merged),
            "flightsDeltaRecords": len(delta),
            "airtableFlights": airtable_flights,
            "pre2024Archive": PRE_2024_ARCHIVE_FLIGHTS,
        },
    }


def main() -> int:
    env = load_env()
    pat = env.get("AIRTABLE_PAT") or os.environ.get("AIRTABLE_PAT")
    base_id = env.get("AIRTABLE_BASE_ID") or os.environ.get("AIRTABLE_BASE_ID")
    if not pat or not base_id:
        print("ERROR: AIRTABLE_PAT / AIRTABLE_BASE_ID missing (set in .env.local)", file=sys.stderr)
        return 2

    try:
        merged = fetch_all(base_id, MERGED_TABLE, pat)
        flights = fetch_all(base_id, FLIGHTS_TABLE, pat)
    except Exception as e:
        print(f"ERROR: Airtable fetch failed: {e}", file=sys.stderr)
        return 3

    totals = compute_totals(merged, flights)
    totals["updatedAt"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    totals["source"] = (
        f"Airtable base {base_id} — Merged flights + Flights delta (dedup by Flight #)"
    )

    # Monotonic-decrease sanity guard: lifetime counters should never shrink.
    # If Airtable returns a smaller number (corrupted fetch, a table getting
    # wiped, rows deleted by mistake) we refuse to overwrite the snapshot so
    # the site keeps serving the last known-good numbers. Pass --force to
    # override (e.g. after a legitimate correction).
    force = "--force" in sys.argv
    if OUTPUT_FILE.exists() and not force:
        try:
            prev = json.loads(OUTPUT_FILE.read_text())
        except Exception:
            prev = {}
        for key in ("lifetimeFlights", "flightTimeSec", "kmFlown"):
            prev_v = prev.get(key)
            new_v = totals.get(key)
            if prev_v is None or new_v is None:
                continue
            if new_v < prev_v:
                print(
                    f"ERROR: refusing to write — {key} decreased "
                    f"({prev_v} → {new_v}). Re-run with --force if intentional.",
                    file=sys.stderr,
                )
                return 4

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(json.dumps(totals, indent=2) + "\n")
    print(f"Wrote {OUTPUT_FILE.relative_to(REPO_ROOT)}:")
    print(json.dumps(totals, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
