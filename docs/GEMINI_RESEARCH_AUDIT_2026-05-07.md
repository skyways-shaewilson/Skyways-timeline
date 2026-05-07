# Gemini Research Audit | 2026-05-07

Reviewed input: Gemini share `https://gemini.google.com/share/60473458d5a3`, plus Shae's pasted full report content.

Purpose: determine whether the Gemini forensic research adds new source coverage, reveals missing sources, or requires timeline adjustments.

## Bottom Line

No date, amount, or milestone timeline adjustment is required from the Gemini report.

One source-visibility adjustment is justified: FA228024D0003 should be treated as public in the contracts drawer. The parent IDIQ, requirement name, and ceiling are publicly confirmed by AFRL. The task-order obligation detail remains internally sourced in the event card.

One local source-description cleanup was also required: the media mention summary for the Austin American-Statesman / DroneXL-derived facility profile had repeated the already-debunked `250,000 sq ft` typo. Charles's correction supersedes this; the correct facility size remains `25,000 sq ft`.

## New Learning Worth Saving

| Finding | Status | Action |
|---|---|---|
| AFRL Active OTSB-SB Contracts PDF publicly lists `FA228024D0003` for Skyways. | New public source captured. | Add AFRL PDF to event `id=28` source URLs. |
| AFRL PDF confirms requirement name `Rapid Cargo Resupply`, UEI `DATMBHX83MN7`, ultimate completion `2029-06-19`, and total contract value `$4,999,999.00`. | Useful source detail. | Add event `id=28` bullet and mark the contracts drawer row as `Public`. |
| AFRL PDF does not confirm task order `FA228024F0013` obligations or Mods #1/#2 math. | Still internal. | Keep approx. `$2.2M obligated` sourced to internal task-order records. |

Primary source: [AFRL Portfolio Active Contracts as of 22 Sep 2025](https://www.afrl.af.mil/Portals/90/Documents/SB/AFRL_Active_OTSB-SB_Contracts.pdf?ver=0Nqv4Y75fMtqdXzHORfaiA%3D%3D).

## Already Captured Sources

| Claim Area | Current Coverage | Notes |
|---|---|---|
| USAF SBIR Phase I `FA8649-21-P-0539` | Captured in event `id=14` via SBIR.gov Award #191434. | No change. |
| USAF SBIR Phase II `FA8649-22-P-0719` | Captured in event `id=20` via SBIR.gov Award #195821. | SBIR also lists Daniel Feldman / skyborncreative as historical business contact; not timeline-worthy. |
| Navy Blue Water OTA `N00421-19-9-0007` | Captured in event `id=9` via NASC, Janes, and USNI. | No change. |
| USMC/GTRI, DIU/USN OTA, DLA PO lines, NAWCAD BWUAS 2.0 base | Captured as internal contract records, with public relationship/program support where available. | Updated after follow-on check: Federal Compass publicly lists `N004212390013` / NAWCAD BWUAS 2.0 Prototype Project for Skyways; MSC publicly documents Skyways with NAWCAD, USMC, MSC, and Blue Water Logistics UAS at Fleet Battle Problem 23-1. DLA Skyways-specific PO line items remain internal. |
| STRATFI / `$37M` AFWERX contract | Captured in event `id=34` via SBIR.gov Award #220016, BusinessWire, and DroneLife. | `$3,550,613` is the public SBIR component of the larger `$37M` STRATFI structure, not a new standalone timeline event. |
| V2/V3 public capabilities and production ramp | Captured via BusinessWire, DroneLife, Austin American-Statesman/DroneXL, and internal correction docs. | Keep internal V3 spec rule: 100 lb payload OR 1,000 nautical mile range, not both simultaneously. |
| Tech Ridge / Giddings footprint | Captured in event `id=33`. | Charles correction supersedes public/AI repeats of `250,000 sq ft`; correct size is `25,000 sq ft`. |
| Cost comparison | Captured in `docs/STATS_AUDIT.md` from DroneXL. | `$1,000/hr` V2 vs `$30,000/hr` helicopter is already resolved. |

## Rejected Drift From Gemini

| Gemini Claim | Decision | Reason |
|---|---|---|
| `250,000-square-foot facility` | Reject. | Already debunked. Charles correction and local audit establish `25,000 sq ft`. |
| `$3,550,613` as a separate STRATFI grant/event | Reject as standalone event. | It is the SBIR.gov listed amount inside the broader `$37M` STRATFI structure already captured in `id=34`. |
| V3 carries `100 pounds` over `1,000 miles` as a combined capability | Do not use in timeline copy. | Standing Charles/Tom rule says payload and max range are separate: 157 NM with 100 lb payload OR approx. 35 lb cargo at 1,000 NM. |
| `Center Ridge` as replacement for `Tech Ridge` event naming | Reject. | `500 Center Ridge Dr Ste 200` is the federal/SBIR address. The timeline facility event remains `Tech Ridge | 25,000 SF North Austin HQ`. |
| `$95M IDIQ` rumor | No action. | Gemini found no evidence, and the timeline does not include this claim. Keep out unless a primary source appears. |

## Required Timeline Adjustments

Completed:

- Event `id=28`: added AFRL public PDF as a source for the parent FA228024D0003 IDIQ.
- Event `id=28`: clarified that the AFRL source covers the parent contract, while the approx. `$2.2M` task-order obligation remains internal.
- Event `id=25`: added the official Military Sealift Command release confirming Skyways' public Blue Water Logistics UAS work with NAWCAD, USMC, MSC, and USNS Patuxent during Fleet Battle Problem 23-1.
- Event `id=19` and `id=25`: added `(no contract value mentioned)` to relationship/program source labels that do not substantiate the ledger dollar values.
- Event `id=110`: added Federal Compass as a public source for the parent NAWCAD BWUAS 2.0 Prototype Project award `N004212390013`; kept the `$479,052.96` base line-item amount internally sourced.
- Contracts drawer: changed the FA228024D0003 row source pill from `Internal` to `Public`; the AFRL PDF link belongs in the event card source list.
- Contracts drawer: changed the NAWCAD BWUAS 2.0 base row source pill from `Internal` to `Public` because the parent award identifier/program is externally indexed.
- Media mention source summary: corrected `250,000 sq ft` back to `25,000 sq ft`.

Not required:

- No new event card.
- No date change.
- No contracts total change.
- No replacement of Charles/Tom corrections with public-source or AI-generated wording.
