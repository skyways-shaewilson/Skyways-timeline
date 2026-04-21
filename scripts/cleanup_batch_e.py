#!/usr/bin/env python3
"""
Batch E: Phase 10b card bullet conversions for 9 entries.
Each entry gets a `bullets` array (rendered as <ul class="event-bullets">).
ID 13 and ID 19 get charles_corrections notes for unverified-but-Charles-authority claims.
"""
import json
from pathlib import Path

JSON_PATH = Path(__file__).parent.parent / "Data" / "timeline_events_master.json"

BULLETS_BY_ID = {
    13: [
        "Hybrid-electric + AI-driven flight system",
        "500-mile range, 30-lb payload capacity (V2.5)",
        "Selected from 65 candidate UAS evaluated by Navy (Aug 2019)",
        "24-lb cargo / 65-mile range covers ~80% of critical spare parts needs",
    ],
    19: [
        "Base: $1,429,587.50 (Feb 3, 2022)",
        "P00001: Temperature Controlled Payload (Nov 2022)",
        "P00006: SATCOM",
        "P00004: III MEF demonstration (Mar 2024, +$145,161.72)",
        "Final value: $1,807,149.22 (Mar 2024)",
        "Program target (per Charles): 50 lbs over 250 mi for ship-based logistics — covers ~95% of critical parts by weight",
    ],
    22: [
        "Ship-to-ship cargo delivery",
        "Ship-to-shore cargo delivery",
        "Shore-to-ship cargo delivery",
        "Over 200 nautical miles total",
        "Per NAWCAD (Charles internal): 90% of critical mission failures repairable with under-20-lb payloads",
    ],
    28: [
        "Sept 2023: STRATFI package submitted",
        "Early 2024: USAF AFWERX issued RFP for V3 development",
        "Jun 19, 2024: IDIQ contract FA228024D0003 awarded; 5-year ordering period; $4,999,999 ceiling",
        "Mods #1 + #2: Task Order FA228024F0013 obligations grew to ~$2.2M",
        "Jan 6, 2025: Mod #3 extended CLIN dates (no $ change)",
        "June 2024: STRATFI selection announced → $37M contract awarded May 2025",
    ],
    36: [
        "20 operational flights (10 round trips) over 12 days",
        "Route: Grand Forks AFB ↔ Cavalier Space Force Station, ND",
        "Cargo: 230 lbs total (23 lbs per round trip), including temperature-controlled blood",
        "Altitude: 3,500 ft in controlled airspace",
        "Milestone (per Skyways): first unmanned, fully autonomous BVLOS cargo flights between two U.S. airports",
    ],
    38: [
        "11 flights in a single day",
        "9.4 hours total flight time",
        "466 nautical miles flown",
        "8-minute average turnaround",
        "Zero human intervention",
    ],
    110: [
        "Lead division: NAWCAD Rapid Prototyping and Experimentation Division (RPED)",
        "Partner: PMA-263",
        "Focus: autonomous logistical replenishment (shore-to-ship, ship-to-ship, ship-to-shore)",
        "Builds on: 2019 Blue Water work",
        "Mods added: Project ULTRA Demonstration (May 2025), V3 TCP Development (May 2025)",
    ],
    111: [
        "Mission: shore-to-shore long-range autonomous cargo flights",
        "Route: Grand Forks AFB ↔ Cavalier SFS, North Dakota",
        "Aircraft: V2.6B (Government-furnished, GO/CO) + V3.0 (Skyways-owned, CO/CO)",
        "Sponsor: OUSD Project ULTRA",
        "Total task order: $3.5M (OUSD + Grand Forks County)",
        "Program ceiling: $18.25M → $100M (July 2025)",
    ],
    112: [
        "Aircraft: V3 Block 2",
        "Temperature: maintain 1-6°C (4°C tolerance)",
        "Duration: up to 8 hours",
        "External temp tolerance: up to 35°C",
        "System: end-to-end, powered by onboard alternator",
        "Deliverables: PDR within 6 months, CDR thereafter",
    ],
}

# Detail-text trims when a card's facts are now in bullets
DETAIL_REWRITES = {
    13: "Two weeks of autonomous Vertical Takeoff and Landing (VTOL) operations on the Navy's newest and most advanced aircraft carrier. V2.5 drone tested on the flight deck of USS Gerald R. Ford.",
    19: "Skyways secured a contract through the Defense Innovation Unit (DIU) for the Blue Water Maritime Logistics UAS program in partnership with the U.S. Navy, Naval Air Warfare Center Aircraft Division (NAWCAD), and Military Sealift Command. The award contract was directly issued by Army Contracting Command, New Jersey (ACC-NJ). DIU partnered with the 4th Fleet and Marine Corps Warfighting Laboratory to develop computer vision technology enabling autonomous navigation and intelligent landing without beacon assistance.",
    22: "Multi-mode cargo delivery operations at Naval Air Station (NAS) Patuxent River. Skyways and Martin UAV demonstrated Vertical Takeoff and Landing (VTOL) cargo delivery capabilities.",
    28: "After submitting the Strategic Funding Increase (STRATFI) package, USAF AFWERX awarded Skyways the basic SBIR Phase 3 IDIQ contract FA228024D0003 in June 2024. The first Task Order FA228024F0013 was awarded simultaneously. STRATFI selection was announced in the same month and ultimately led to the $37M contract in May 2025.",
    36: "Sole Unmanned Aircraft System (UAS) provider for Project ULTRA (UAS Logistics, Traffic, Response and Autonomy), sponsored by the Office of the Under Secretary of Defense (OUSD).",
    38: "V2 operational record demonstrating the operational tempo required for fleet-scale logistics.",
    110: "U.S. Navy Naval Air Warfare Center Aircraft Division (NAWCAD) awarded Skyways the Blue Water Maritime Logistics Unmanned Aircraft System 2.0 (BWUAS 2.0) Prototype Project contract through the Naval Aviation Systems Consortium (NASC), effective May 4, 2023.",
    111: "U.S. Navy NAWCAD added Contract Line Item 0005 (CLIN 0005) to Skyways' BWUAS 2.0 contract via Modification P00002 effective May 23, 2025, funding Skyways' Project ULTRA Demonstration.",
    112: "U.S. Navy NAWCAD added Contract Line Item 0006 (CLIN 0006) to Skyways' BWUAS 2.0 contract via Modification P00002 effective May 23, 2025. CLIN 0006 funds the design and build of an actively temperature-controlled payload proof of concept for the V3 Block 2 aircraft.",
}

# Charles attribution notes for unverified-but-authoritative claims
CHARLES_NOTES_TO_ADD = {
    13: "Round IV: 500 mi range and 30-lb V2.5 payload claims are per Charles internal — not directly confirmed in publicly verified sources (Maritime Executive verified the 65-UAS / 24 lbs / 65 mi / 80% figures).",
    19: "Round IV: DIU Blue Water program target (50 lbs over 250 mi for ~95% of critical parts) is per Charles internal — public sources confirm contract structure but not the specific program target percentage.",
}


def main():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    log = []
    for entry in data:
        eid = entry.get("id")
        if eid in BULLETS_BY_ID:
            entry["bullets"] = BULLETS_BY_ID[eid]
            log.append(f"id={eid}: bullets added ({len(BULLETS_BY_ID[eid])} items)")
        if eid in DETAIL_REWRITES:
            entry["detail"] = DETAIL_REWRITES[eid]
            log.append(f"id={eid}: detail trimmed (facts moved to bullets)")
        if eid in CHARLES_NOTES_TO_ADD:
            corrections = entry.get("charles_corrections", []) or []
            note = CHARLES_NOTES_TO_ADD[eid]
            if not any("Round IV" in c for c in corrections):
                corrections.append(note)
                entry["charles_corrections"] = corrections
                log.append(f"id={eid}: Charles attribution note added")

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print("=== CHANGE LOG ===")
    for l in log:
        print(f"  • {l}")
    print(f"\n{len(log)} edits applied.")


if __name__ == "__main__":
    main()
