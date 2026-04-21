#!/usr/bin/env python3
"""Add V3 Block 2L (V3.2) Q4 2026 placeholder card to timeline_events_master.json."""
import json
from pathlib import Path

JSON_PATH = Path(__file__).parent.parent / "Data" / "timeline_events_master.json"

NEW_ENTRY = {
    "id": 114,
    "year": "2026",
    "date": "2026-12",
    "title": "V3 Block 2L (V3.2) | Forthcoming",
    "category": "product",
    "detail": "Next iteration in the V3 family beyond V3 Block 2. Details TBD; entry will be filled with full specs and milestone context once the build phase begins. This placeholder ensures the iteration list in the '20+ UAVs Built' stat menu is auditable against the timeline.",
    "tag": "Product | V3",
    "sources": [
        "Skyways Internal — Charles Acknin (V3.2 / V3 Block 2L planned for Q4 2026; placeholder pending more information)"
    ],
    "charles_corrections": [],
    "source_urls": {},
    "sort_date": "2026-12",
    "source_thumbnails": {
        "Skyways (V3 hover)": "https://www.skyways.com/_astro/v3-hover.BZwWRBFB_t27Og.webp"
    },
    "thumbnail_status": "fallback_v3_hover",
    "date_display": "2026-12"
}


def main():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Check if id=114 already exists
    if any(e.get("id") == 114 for e in data):
        print("ID 114 already exists; skipping.")
        return

    data.append(NEW_ENTRY)

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Added entry id=114: {NEW_ENTRY['title']}")
    print(f"Total entries: {len(data)}")


if __name__ == "__main__":
    main()
