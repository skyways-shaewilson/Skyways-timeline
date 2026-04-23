#!/usr/bin/env python3
"""
Batch F:
  1. Title standardization (6 contract entries)
  2. Add 3 DLA PO timeline cards (SATCOMv2, Intelligen, DGPS under SPE8EJ21D0022)
"""
import json
from pathlib import Path

JSON_PATH = Path(__file__).parent.parent / "Data" / "timeline_events_master.json"

TITLE_REWRITES = {
    "SBIR Phase I | $47,775":
        "$47,775 | USAF SBIR Phase I",
    "SBIR Phase II | $749,711":
        "$749,711 | USAF SBIR Phase II",
    "$2,200,000 Obligated / $4,999,999 Ceiling | USAF SBIR Phase 3 IDIQ + STRATFI Selection":
        "$2,200,000 | USAF SBIR Phase 3 IDIQ + STRATFI Selection ($4,999,999 Ceiling)",
    "$37M U.S. Air Force STRATFI Contract":
        "$37M | U.S. Air Force STRATFI Contract",
    "Navy LP-CRADA | Aircraft Lease Agreement (V2 AV1-3)":
        "Aircraft Lease Agreement | Navy LP-CRADA (V2 AV1-3)",
    "RWE Offshore Wind Farm, Baltic Sea, Germany":
        "Commercial Contract | RWE Offshore Wind Farm (Baltic Sea, Germany)",
}

DLA_PO_ENTRIES = [
    {
        "id": 115,
        "year": "2023",
        "date": "2023-03",
        "title": "Navy DLA PO | DGPS (SPE8EJ21D0022)",
        "category": "contracts",
        "detail": "Defense Logistics Agency (DLA) Purchase Order under prime contract SPE8EJ21D0022 (Noble Supply & Logistics). Skyways component / supply role. Funded item: Differential Global Positioning System (DGPS). Effective March 15, 2023. Dollar amount not yet documented in available records.",
        "tag": "Contract | U.S. Navy / DLA",
        "sources": [
            "Skyways Internal — Contract SPE8EJ21D0022 (DLA prime via Noble Supply & Logistics; PO dated Mar 15, 2023; component supplier role; dollar amount pending documentation)",
            "TAA Transmittal Letter (Mar 24, 2025)"
        ],
        "charles_corrections": [],
        "source_urls": {},
        "sort_date": "2023-03",
        "source_thumbnails": {
            "Skyways (V2 aboard ship)": "https://www.skyways.com/_astro/v2-aboard-ship.Dm1shnLv_ZVithb.webp"
        },
        "thumbnail_status": "fallback_v2_ship",
        "date_display": "2023-03"
    },
    {
        "id": 116,
        "year": "2023",
        "date": "2023-05",
        "title": "Navy DLA PO | SATCOMv2 (SPE8EJ21D0022)",
        "category": "contracts",
        "detail": "Defense Logistics Agency (DLA) Purchase Order under prime contract SPE8EJ21D0022 (Noble Supply & Logistics). Skyways component / supply role. Funded item: Satellite Communications version 2 (SATCOMv2). Effective May 26, 2023. Dollar amount not yet documented in available records.",
        "tag": "Contract | U.S. Navy / DLA",
        "sources": [
            "Skyways Internal — Contract SPE8EJ21D0022 (DLA prime via Noble Supply & Logistics; PO dated May 26, 2023; component supplier role; dollar amount pending documentation)",
            "TAA Transmittal Letter (Mar 24, 2025)"
        ],
        "charles_corrections": [],
        "source_urls": {},
        "sort_date": "2023-05",
        "source_thumbnails": {
            "Skyways (V2 aboard ship)": "https://www.skyways.com/_astro/v2-aboard-ship.Dm1shnLv_ZVithb.webp"
        },
        "thumbnail_status": "fallback_v2_ship",
        "date_display": "2023-05"
    },
    {
        "id": 117,
        "year": "2023",
        "date": "2023-06",
        "title": "Navy DLA PO | Intelligen (SPE8EJ21D0022)",
        "category": "contracts",
        "detail": "Defense Logistics Agency (DLA) Purchase Order under prime contract SPE8EJ21D0022 (Noble Supply & Logistics). Skyways component / supply role. Funded item: Intelligen (autonomous flight stack component). Effective June 15, 2023. Dollar amount not yet documented in available records.",
        "tag": "Contract | U.S. Navy / DLA",
        "sources": [
            "Skyways Internal — Contract SPE8EJ21D0022 (DLA prime via Noble Supply & Logistics; PO dated Jun 15, 2023; component supplier role; dollar amount pending documentation)",
            "TAA Transmittal Letter (Mar 24, 2025)"
        ],
        "charles_corrections": [],
        "source_urls": {},
        "sort_date": "2023-06",
        "source_thumbnails": {
            "Skyways (V2 aboard ship)": "https://www.skyways.com/_astro/v2-aboard-ship.Dm1shnLv_ZVithb.webp"
        },
        "thumbnail_status": "fallback_v2_ship",
        "date_display": "2023-06"
    },
]


def main():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    log = []

    # 1. Title rewrites
    for entry in data:
        old = entry.get("title", "")
        if old in TITLE_REWRITES:
            entry["title"] = TITLE_REWRITES[old]
            log.append(f"id={entry['id']}: '{old}' -> '{entry['title']}'")

    # 2. Append DLA POs (skip if id already exists)
    existing_ids = {e.get("id") for e in data}
    for new_entry in DLA_PO_ENTRIES:
        if new_entry["id"] in existing_ids:
            log.append(f"id={new_entry['id']}: already exists, skipping")
            continue
        data.append(new_entry)
        log.append(f"id={new_entry['id']}: ADDED '{new_entry['title']}'")

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print("=== CHANGE LOG ===")
    for l in log:
        print(f"  • {l}")
    print(f"\nTotal entries now: {len(data)}")


if __name__ == "__main__":
    main()
