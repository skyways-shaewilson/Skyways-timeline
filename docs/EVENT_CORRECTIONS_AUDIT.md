# Event Corrections Audit — Skyways Timeline

## Purpose

Single working document for the event-by-event review of all Firestore events (`skyways_history_and_story` collection, mirrored in `Data/timeline_events_master.json`). Consolidates every known correction from:

1. **Tom Martin ("T-Money"), senior vehicle engineer** — 5 corrections via Slack DM (`D0AMB9XD5UL`) and one public relay in `#brand-and-marketing` reply 32 (Apr 6, 2026)
2. **Charles Acknin, CEO/co-founder** — 40 corrections across three Excel rounds (Round II Mar 19-20, 2026; Round III Mar 24 – Apr 1, 2026) + Slack corrections (Apr 1 – Apr 22, 2026)

Use this as the single-source ledger when going era-by-era through events. Each correction is tagged with: source (Tom / Charles), medium (Slack / Excel Round), date, event ID or title, category (date / dollar / spec / voice / factual / coverage / compliance / structure), magnitude (minor vs. large).

---

## Process Rules (per Shae)

- **Minor / must-make corrections** (grammar, date fixes, dollar typos, small wording): auto-apply.
- **Large discrepancies** (delete entire event, rename founders, restructure the story order, add new events): flag for Shae's approval before touching.
- **Grammar mistakes:** auto-correct.
- Update BOTH `Data/timeline_events_master.json` AND Firestore (`skyways_history_and_story`) per project rule.
- Charles trumps public sources; flag discrepancies inline where needed.

---

## Part 1 — Tom Martin (T-Money) Corrections

Identity: Tom Martin | `tom@skyways.com` | Slack `U04ALK2USCS` | Austin, TX | senior vehicle engineer (titled "Engineeeer" as a joke). Joined Skyways end of 2017. Charles-appointed technical reviewer of timeline history. Authoritative on V2/V3 vehicle specs and post-2017 history; defers to Charles for pre-2017.

Pattern: always pushes back on capability claims that aren't spec-exact. Hedges recollection with "IIRC." Uses V-designations precisely (V2.2 ≠ V2.5 ≠ V3 Block 1). Prefers hard numbers with units (lbs, NM, hz, ft³) and cites source decks by URL.

| # | Date | Event | Original | Tom's correction | Category | Magnitude |
|---|---|---|---|---|---|---|
| T-1 | Apr 2, 2026 (DM) | V3 capability | "carries ~100 lbs of cargo over 1,000 miles" | V3 does 1,000 NM **OR** 100 lbs, not both. Authoritative: 157 NM @ 100 lbs, or ~35 lbs @ 1,000 NM. Source: V3 Blk 2 Tech Exchange slide 49. Global rule: never imply max payload and max range simultaneously. | spec | minor (apply rule everywhere) |
| T-2 | Apr 2, 2026 (DM) | 2018 dev year | Charles said "there has to be something significant in 2018" | 2018 spent evolving V2.2 from barely-carries-payload POC into the vehicle that flew ANTX in early 2019 at ~15 lbs / 50 miles, all-electric. Pre-2017 history is before Tom's time (defer to Charles). | coverage | already addressed in Era 1 events |
| T-3 | Apr 6, 2026 (DM → public) | Event `2017-01` (id=1) "Founded" | "co-founded Skyways in Austin, TX with Chris Craighill after nearly 7 years at Google" reads as if Chris worked at Google | Rewrite so the 7-years-at-Google applies to **Charles only**, not Chris (Chris was at Firefly Aerospace). | factual / voice | minor (wording fix) |
| T-4 | Apr 6, 2026 (DM → public) | Event `2019-10` (V2 Navy-requirement specs) | "30-lb payload (one cubic foot cargo volume), approximately 450 to 500 mile range" | Original Navy request was **20 lbs and 400 NM**, not 30 lb / 450–500 mi. Source article was 2021 by which time the envelope had expanded. Tom hedges "could be wrong." | spec | minor (apply with Tom hedge; confirm with Charles if uncertain) |
| T-5 | Apr 6, 2026 (DM → public) | Event `2021-02` (Ford carrier deck) | "V2.2 drone tested on the flight deck of USS Gerald R. Ford" | Should be **V2.5**, not V2.2. | spec | minor |

**Unresolved / pending Tom:** Apr 23, 2026 (today), Shae re-pinged Tom with latest timeline + source drawer. Tom gave `:eyes:` reaction, no corrections yet.

---

## Part 2 — Charles Acknin Excel Round Corrections

40 total corrections across Round II (Mar 19-20, 2026, 33 comments) + Round III (Mar 24 – Apr 1, 2026, 7 NEW comments on V.3 sheet). Source files:
- `Skyways Timeline/Data/Timeline Data/Skyways_Timeline_Data - Charles Comment Round II.xlsx`
- `Skyways Timeline/Data/Timeline Data/Skyways_Timeline_Data - Charles Comment Round III.xlsx`

### 2A. By Era

#### Era 1 — Founding (2016-2018)

| # | Source | Event / ID | Correction | Magnitude |
|---|---|---|---|---|
| C-1 | R2 CA#1 | id=1 "Founded" (2017-01) | Remove **Anurag Sabbarwal** from co-founders. Only Charles and Chris Craighill. | minor |
| C-2 | R2 CA#2 | id=2 "YC S17 Batch" (2017-06) | Remove "debt financing" from detail (no debt until 2025). | minor |
| C-3 | R2 CA#3 | "Firefly Shop" (if present) | Firefly shop was Q1-Q2 2017 only; first own office = Manor, **May 2017**, 5,000 SF. Remove "Dual-Hybrid" from any pre-2019 copy (all-electric until USN OTA Aug 2019). | minor-medium |
| C-4 | R2 CA#4 | id=100 Seed rolling close | Remove PitchBook "$29M total raised" figure ("all mixed up and wrong"). Skyways raised continually over several years. Reference: fundraising master sheet https://docs.google.com/spreadsheets/d/1nRoMRs-aUTIuL1b7hVmp62XHTR3cgSlRExFyzH6Lwss | minor |
| C-5 | R2 CA#5 | (if present) "Seed closed Jan 2018" | Collapse into single rolling-close event (already in id=100). | minor |
| C-6 | R2 CA#6 | "Early prototyping begins" | Do NOT date Dual-Hybrid to Mar 2018 — Dual-Hybrid started END of 2019. Correct sequence: Jan 2019 apply ANTX2019, Mar 2019 win ANTX2019 vs Boeing with V2.2 all-electric, Aug 2019 USN OTA for hybrid conversion. ANTX funnel: 65 identified, 19 responded, 6 invited, 2 showed. | medium (spec+date) |
| C-7 | R2 CA#7 | "Manor Office move" | Manor = **May 2017**, not Jul 2018. Office timeline: Summer 2016 SF apartment, Q1 2017 Firefly shop + Briggs test site, May 2017 Manor 5k SF, Apr 2021 Cross Park Dr 10k SF, May 2024 Tech Ridge 25k SF. | minor |
| C-19 | R2 V.2 #1 | id=100 seed investors | Investor list wrong. **Remove UpHonest Capital** ("we had to remove them"). **Outlander + MVP only came in 2021+**, not seed-era. | minor |
| C-20 | R2 V.2 #2 | id=7 USMC/GTRI PO | Date = **End of 2017** (first-ever contract). Not "~2020." Navy Blue Water only happened later in 2019. | already fixed |
| C-34 | R3 V.3 #1 | id=103 V1 Summer 2016 | ADD V1 full spec: VTOL fixed-wing quadplane, 5 electric motors, COTS foam wing modified for VTOL. A-B-C-A autonomous mission (pickup at B, deliver at C). Endurance <30 min, cargo 2 lbs. Early precision-landing code on Companion Computer. ADD: "My dad, also passionate about aviation, flew to SF multiple times in 2016 to help me build V1 and essentially as my unofficial co-founder." Flight testing Pacifica + Livermore. V1 A-B-C-A video: https://youtu.be/Gz8sRWUiw7o | medium (adds content; already mostly in id=103) |
| C-35 | R3 V.3 #2 | id=1 (2017-01) | STRUCTURE: Move Charles-bio paragraph ("born near Airbus HQ in southern France, ex-Google") OUT of the Jan 2017 founding row and INTO the Summer 2016 V1 row (id=103) as the opening. Timeline should OPEN with Charles + V1 + his dad, not with the incorporation. | **large — needs approval** |
| C-36 | R3 V.3 #3 | gap | ADD 2018 events (ALREADY ADDED as id=107, id=105, id=106). Confirm those rows cover: V2.0 X8 12ft wingspan first composite airframe (still hanging at Tech Ridge), 2H 2017 started V2.1 & V2.2 18ft wingspan 140-lb AUW (crashed a lot), Apr 2018 first two V2.2 for USMC driven to NM for White Sands BVLOS with NMSU + GTRI + USMC (first-ever BVLOS, >60mi, all-electric). | already addressed; audit for completeness |

#### Era 2 — Earning the Navy (2019-2022)

| # | Source | Event / ID | Correction | Magnitude |
|---|---|---|---|---|
| C-8 | R2 CA#8 | Ship-to-Ship Jul 2021 | ADD framing: "This was all done directly by our customer, the US Navy. No Skyways employees were on those ships. This was a major achievement." | minor (voice) |
| C-9 | R2 CA#9 | SBIR Phase II Jul 2022 | Change "V3 early-stage design" → "V2" (Phase II was all V2 at first). | minor (spec) |
| C-21 | R2 V.2 #3 | "Navy OTA Spiral follow-on" | Hybrid propulsion was the INITIAL 2019 Navy OTA contract scope (not a later spiral). Spiral dev 2020+ was for folding wings etc. | minor-medium (restructure detail) |
| C-22 | R2 V.2 #4 | "V2 Flight Testing Apr 2020" | Remove SkyNav reference (SkyNav = Q2 2023). Remove Starlink reference (Starlink = end 2024). | minor (spec/date) |
| C-23 | R2 V.2 #5 | "SBIR Phase I Feb 2021" | Rephrase "that would lead to $37M" → "that would eventually lead to the USAF awarding Skyways a $37M contract." | minor (voice) |
| C-24 | R2 V.2 #6 | "First Commercial Customer — Offshore O&G (Jun 2021)" | **DELETE this entire event.** Real commercial ops didn't start until 2025. Charles doesn't know who "unnamed oil-and-gas customer" is. | **large — needs approval (but Charles clear: delete)** |
| C-25 | R2 V.2 #7 | Ship-to-Ship Jul 2021 | CV detail wrong. Precland (CV for final landing only) demo'ed 2019. Full Computer Vision Ship Intercept (CVSI) first demo'ed Nov 2024 on USN ship in Gulf of Mexico ("no other company has ever done this"). REMOVE 2021 CV intercept claim. | medium (spec + add Nov 2024 CVSI event) |
| C-26 | R2 V.2 #8 | "DIU/USN/NAMD contract" | Dated ~2023 is wrong. DIU contract/OTA won in **2022**. Refs: https://drive.google.com/drive/folders/1crUdAexYQCpU2RPWEx5tMxzqgovXdIkD | minor (date) |
| C-37 | R3 V.3 #4 | "V2 Platform Development Accelerates Oct 2019" | Remove "(foldable)" from 2019 V2 wingspan spec — folding wings came later, not in 2019 scope. | minor (spec) |

#### Era 3 — V3 and Allies (2023-2024)

| # | Source | Event / ID | Correction | Magnitude |
|---|---|---|---|---|
| C-27 | R2 V.2 #9 | "V3 Next-Gen Revealed Mar 2024" | V3 timeline: 2021 initial concept, 2022 subscale (Oct 2022 first flights), 2022-2025 V3 Block 0 full-scale (first flew early 2023, upgraded to Block 1 config, still flying), 2022-today V3 Block 1 (first flew early 2024, still flying), 2023-today V3 Block 2 (first article build scheduled Jun 2026). Real V3 resources began mid-2023. V3 specs are 157 NM @ 100 lbs OR 35 lbs @ 1,000 NM (NEVER both simultaneously). | medium (aligns with Tom T-1) |
| C-28 | R2 V.2 #10 | "RIMPAC 2024 (Jun 2024)" | "Six UAS" is WRONG — there were **three Skyways V2.6 aircraft** on USS Curtis Wilbur DDG-54. | minor (count fix) |
| C-29 | R2 V.2 #11 | "III MEF Operations" | WRONG LOCATION — not Okinawa, Japan. DIU put Skyways on contract to demo TCP (Temperature Controlled Payload) with USMC III MEF, which actually happened **in the US**. 6-hour / 300+ mile flight keeping 10 bags of blood at 3-6 °C. Ref deck: https://docs.google.com/presentation/d/1dE6P1A2Vf7oIlt4TNG11nQ8Mo5Q8FX0AcSQQtI-L-Go/edit | **large — needs approval (location is a big correction already reflected in some places)** |
| C-30 | R2 V.2 #12 | "USAF SBIR Phase 3 IDIQ Jun 2024" | Replace "(initial millions)" with crisper phrasing — e.g., "multi-million-dollar Phase 3 IDIQ." | minor (voice) |
| C-39 | R3 V.3 #6 | "RIMPAC 2024" | Remove PteroDynamics X-P4 mention from detail ("they're completely irrelevant with an all-electric drone that can only fly 60 miles"). | minor (voice / competitive) |
| C-10 | R2 CA#10 | "SBIR Phase II STRATFI $3.55M (Mar 2025)" | No such $3.55M figure. Full STRATFI timeline: ~Sep 2023 submit package, Feb 2024 USAF AFWERX RFP (no STRATFI term yet), **Jun 2024** Phase 3 IDIQ awarded + STRATFI selection notification, **May 2025** STRATFI contract awarded $37M. Remove this event or replace with a clean "Jun 2024 IDIQ + STRATFI Selection" event. | medium |
| C-11 | R2 CA#11 | "Austin Center Ridge Dr 25k SF May 2025" | Wrong date (May 2024, not May 2025) AND wrong name (it's Tech Ridge). | minor |

#### Era 4 — Program & Public (2025-2026)

| # | Source | Event / ID | Correction | Magnitude |
|---|---|---|---|---|
| C-12 | R2 CA#12 | "$37M STRATFI Jun 2025" | DELETE "Total known government contract value exceeds $41M" — "no idea where that's coming from, total total is $37M." | minor |
| C-13 | R2 CA#13 | "$5M Leonid Debt Facility Jun 2025" | Split into TWO events: (a) $7M equity raise for STRATFI 1:1:2 match, (b) $5M Leonid Capital Partners debt (cashflow management). Not "$7M including debt." | medium |
| C-14 | R2 CA#14 | "Project ULTRA Aug 2025" | Sponsor = **OUSD** (not USD(A&S)). ADD: "flights were BVLOS flights, in the National Airspace System (NAS)." | minor |
| C-15 | R2 CA#15 | "RWE Offshore Wind Sep-Oct 2025" | ADD missing earlier beats: **Feb 2025 Skyports first international delivery** and **Apr 2025 ANA first delivery**. 2025 was first year of commercial customers taking deliveries. | **large — adds two events (awaits Jessica sign-off for ANA row per C-16)** |
| C-16 | R2 CA#16 | "ANA Partnership Oct 2025" | Coordinate with Jessica before publishing. ANA hasn't wanted this public due to US DoD ties. | **large — compliance hold** |
| C-17 | R2 CA#17 | "Leadership Expansion Jan 2026" | "~30 employees" → **~39** (end-of-2025 headcount, verify with Anthony). "Plans to double in 2026" is OK if verified. | minor |
| C-31 | R2 V.2 #13 | "$37M STRATFI May 2025" | Reframe around Program of Record. STRATFI is a pathway to PoR; Skyways was selected as the only cargo-drone company. Ref: https://a16z.com/dod-contracting-for-startups-101/ | minor-medium (voice) |
| C-32 | R2 V.2 #14 | "~$7M STRATFI Match Jun 2025" | Was $7M + $5M (two raises), NOT $7M-including-debt. Same instruction as C-13. | minor (dup of C-13) |
| C-33 | R2 V.2 #15 | "First International Deliveries Feb-Apr 2025" | DELETE last sentence ("transition from demonstration to customers flying their own aircraft") — Navy had been flying their own Skyways aircraft for years before 2025. | minor (voice) |

#### Era 5 — Scaling (2027+)

No event-level Excel corrections (upcoming era).

### 2B. New Events Charles Wants Added (not in current 64)

| # | Event | Era | Magnitude |
|---|---|---|---|
| N-1 | Summer 2016 V1 + Charles bio + dad co-founder (MERGE with id=103) | 1 | medium (enrich existing) |
| N-2 | Feb 2025 Skyports First International Delivery | 4 | **large — needs approval** |
| N-3 | Apr 2025 ANA First Delivery | 4 | **large — Jessica sign-off required** |
| N-4 | Nov 2024 CVSI (Computer Vision Ship Intercept) Gulf of Mexico demo | 3 | **large — needs approval** |
| N-5 | End-of-2024 Starlink Integration (own event) | 3 | medium |
| N-6 | Jun 2024 SBIR Phase 3 IDIQ + STRATFI Selection (standalone) | 3 | medium (replaces C-10 "$3.55M" row) |

### 2C. Sources to ADD (per Charles)

- Fundraising master sheet: https://docs.google.com/spreadsheets/d/1nRoMRs-aUTIuL1b7hVmp62XHTR3cgSlRExFyzH6Lwss
- USMC/GTRI Drive folder: https://drive.google.com/drive/folders/1t-le78CkMLCC9CyVO-ocg1M5W8QdYL2W
- USN OTA follow-ons Drive folder: https://drive.google.com/drive/folders/1zttPYwgd9uVGe_uzxiQnW1FcY-EeJLj9
- DIU/USN/NAMD Drive folder: https://drive.google.com/drive/folders/1crUdAexYQCpU2RPWEx5tMxzqgovXdIkD
- V1 A-B-C-A video: https://youtu.be/Gz8sRWUiw7o
- TCP demo deck: https://docs.google.com/presentation/d/1dE6P1A2Vf7oIlt4TNG11nQ8Mo5Q8FX0AcSQQtI-L-Go
- a16z STRATFI / PoR reference: https://a16z.com/dod-contracting-for-startups-101/

### 2D. Sources / claims to REMOVE

- PitchBook "$29M total raised" (row 6: "wrong")
- "$3.55M STRATFI" figure (row 23: "not sure where coming from")
- "$41M total known government contract value" (row 25: "no idea where that's coming from" — $37M total total)
- "Unnamed oil-and-gas customer" Jun 2021 event (delete entire row)
- Anurag Sabbarwal from any co-founder list
- UpHonest Capital from investor lists
- "Dual-Hybrid" from any pre-Q3 2019 copy (all-electric until then)
- PteroDynamics X-P4 from RIMPAC 2024 detail

---

## Part 3 — Charles Slack Corrections (cross-reference)

Already consolidated in `memory/reference_charles_feedback_archive.md`. Key event-relevant items:

- **V1 origin** (Apr 1, 2026 DM): Started with a Skywalker X-5 hobby kit, added 2 carbon fiber booms, installed VTOL propulsion (4 motors, not 8). No CAD until V2.1. Usable content for id=103 detail.
- **V3B2 cargo bay**: 7 cu ft, not 5 (Oct 18, 2025).
- **Facility dates**: Cross Park Apr 2021, Tech Ridge May 2024 — consistent with Excel corrections.
- **JMSDF resupply**: Aug 2024, not Jul — already applied.
- **Culture quotes** (Feb 21, 2026): integrity, proactive, do what we said, can-do, never give up, "build the future of aviation." Usable for future copy, not event-level fix.
- **No "pivot," only "next phase"** (Apr 14, 2026). Applies to any copy near the public-emergence period.
- **SAS correction** (Apr 22, 2026): SAS was NOT Skyways' first major defense industry event — AUVSI and EDRC came first. If any event names SAS as first, remove that framing.

---

## Part 4 — Magnitude Summary (for Shae's triage)

### Auto-apply (minor / grammar / small factual)

- T-3: Fix Chris/Google attribution on id=1 (grammar + factual)
- T-4: V2 Navy spec 20lb/400NM on id=42 (or whichever row)
- T-5: V2.2 → V2.5 on Ford carrier deck row (id=15 or similar)
- C-1: Remove Anurag from id=1 (but coordinate with C-35 structural move)
- C-2: Remove "debt financing" from id=2 detail
- C-3: Remove "Dual-Hybrid" from any pre-2019 row; fix Firefly-shop vs Manor dates
- C-4: Remove PitchBook $29M figure from id=100
- C-7: Manor date = May 2017
- C-8: ADD Navy-did-this framing on Ship-to-Ship
- C-9: V3 → V2 on SBIR Phase II Jul 2022
- C-11: Tech Ridge date May 2024 (not May 2025)
- C-12: Delete $41M claim from $37M STRATFI row
- C-14: OUSD sponsor (not USD(A&S)); add BVLOS/NAS framing to Project ULTRA
- C-17: 30 → 39 employees (verify with Anthony first)
- C-19: Fix investor list (remove UpHonest, move Outlander+MVP to 2021+)
- C-22: Remove SkyNav + Starlink from 2020 rows
- C-23: Rephrase SBIR Phase I voice
- C-26: DIU date 2022 (not ~2023)
- C-27: Apply V3 capability rule (OR not AND); fix V3 timeline beats
- C-28: RIMPAC count = 3 Skyways V2.6 (not 6)
- C-30: Replace "initial millions" on Phase 3 IDIQ row
- C-32/C-13: Split $7M equity + $5M Leonid (duplicated correction)
- C-33: Delete "transition to customers flying their own" sentence on 2025 Int'l row
- C-37: Remove "(foldable)" from 2019 V2 spec
- C-39: Remove PteroDynamics from RIMPAC detail

### Flag for approval (large / structural / compliance)

- **C-35:** Move Charles-bio paragraph from id=1 to id=103 (reorders the story's opening)
- **C-24:** DELETE id=? "First Commercial Customer — Offshore O&G Jun 2021" row entirely
- **C-29:** Confirm III MEF location correction (US not Okinawa) if not already applied
- **C-15 / N-2:** ADD Feb 2025 Skyports First International Delivery event
- **C-16 / N-3:** ADD Apr 2025 ANA First Delivery event AND coordinate with Jessica on any ANA publish
- **N-4:** ADD Nov 2024 CVSI demo (Gulf of Mexico, USN, first-of-kind) event
- **N-5:** ADD End-2024 Standalone Starlink integration event
- **N-6:** ADD Jun 2024 SBIR Phase 3 IDIQ + STRATFI Selection (standalone event, replacing any $3.55M row)
- **C-10:** Delete/replace any "$3.55M STRATFI" row

### Pending re-verification

- Tom's Apr 23, 2026 re-review (he reacted with `:eyes:` but hasn't returned corrections)
- Anthony's confirmation on end-2025 headcount (C-17)
- Jessica's sign-off on any ANA-related publish (C-16)

---

## Part 5 — Verification Audit Results (Apr 23, 2026)

Automated + manual sweep of `Data/timeline_events_master.json` (64 events) against every correction above. Feedback dates taken into account: Charles Excel Mar 19 – Apr 1, 2026; Tom Slack Apr 2 – Apr 6, 2026. Review date: Apr 23, 2026.

### ✓ Honored (past feedback reflected in current data)

| ID | Correction | Evidence |
|---|---|---|
| T-3 | Chris/Google attribution clean | id=1 uses period to separate Chris from Google clause |
| T-4 | 2019 V2 Navy spec 20lb / 400NM | id=10 "20-lb payload (one cubic foot) or approximately 400 nautical mile range" |
| T-5 | Ford carrier deck V2.5 | id=13 "V2.5 drone tested on the flight deck" |
| C-1 | Anurag removed from co-founders | Not in any detail; only Charles + Chris |
| C-2 | "debt financing" removed from YC row | id=2 detail has no debt-financing mention |
| C-4 | PitchBook $29M removed | No $29M figure anywhere in corpus |
| C-8 | Ship-to-ship: Navy-did-this framing | id=15 "entirely by U.S. Navy personnel with no Skyways employees" |
| C-10 | $3.55M STRATFI removed | No $3.55M figure; id=28 correctly framed as Jun 2024 IDIQ + STRATFI Selection |
| C-11 | Tech Ridge date May 2024, name correct | No "Center Ridge" or May 2025 anywhere |
| C-12 | $41M "total known" removed | No $41M figure in corpus |
| C-14 | ULTRA sponsor = OUSD | id=36 "sponsored by the Office of the Under Secretary of Defense (OUSD)" |
| C-17 | Headcount 30 removed | id=43 no longer mentions "~30 employees" (claim removed; number pending Anthony) |
| C-19 | UpHonest removed from investor list | No UpHonest anywhere in corpus |
| C-24 | Unnamed oil-and-gas 2021 row deleted | No surviving row |
| C-26 | DIU contract dated 2022 | id=19 shows 2022-02 "Blue Water \| DIU/USN OTA" |
| C-27 | V3 timeline + capability OR/AND | id=10 frames as "or"; no "1,000 miles / 100 lbs" conflation |
| C-28 | RIMPAC count "3 Skyways V2.6" | id=27 leads with "Skyways aircraft (3 of 6 total..." |
| C-33 | International Deliveries last sentence removed | id=39 detail ends appropriately |
| C-37 | "foldable" removed from 2019 row | No "foldable" in id=10 |
| N-2 | Skyports Feb 2025 event present | id=39 names Skyports Feb 2025 + ANA Apr 2025 |
| N-3 | ANA Apr 2025 delivery present | id=39 + id=41 covers both beats |
| N-5 | Starlink end-2024 standalone | id=32 "Starlink Connectivity Added" (2024-12) |
| N-6 | Jun 2024 IDIQ + STRATFI Selection | id=28 "USAF SBIR Phase 3 IDIQ + STRATFI Selection" |

### ✗ Still NOT honored (these are the gaps)

| ID | Correction | Current State | Action |
|---|---|---|---|
| **C-39** | Remove PteroDynamics X-P4 from RIMPAC (Charles Round III, Apr 1) | id=27 still says "3 of 6 total UAS launched alongside PteroDynamics X-P4" | **AUTO-FIX** — Charles already ruled, wording-only change |
| **C-29** | III MEF TCP demo happened stateside, not Okinawa; add 6hr / 300+ mi / 10 bags blood 3-6°C spec | id=31 still says "III MEF, the U.S. Marine Corps command in Okinawa" (ambiguous); demo specs missing | **AUTO-FIX** — Charles already ruled, factual clarification + spec add |
| **N-4** | ADD Nov 2024 CVSI (Computer Vision Ship Intercept) Gulf of Mexico demo (Charles Round II V.2, Mar 20) | No CVSI event in corpus | **FLAG FOR APPROVAL** — adding a new event is more than a correction |

### ⚠️ Pending external verification (not a gap, but flagged)

| ID | Correction | Status |
|---|---|---|
| C-17 | Headcount "~39 at end of 2025" | Claim currently absent. Pending Anthony confirmation, then can add. |
| C-16 | ANA Partnership Oct 2025 publish | Published at id=41. Presumably Jessica previously signed off; worth confirming once more before next press cycle. |

### Feedback-date relevance note

All Charles Excel feedback is 3–5 weeks old (Mar 19 – Apr 1, 2026). No later Charles Slack message has contradicted or superseded any earlier correction. His Apr 1 "pretty cool and emotional" comment suggests the then-current state was overall satisfying to him, which is consistent with the audit finding that most corrections were successfully applied in the interim.

Tom's feedback is 2–3 weeks old (Apr 2 – Apr 6, 2026). All three of his still-unresolved-on-that-date items (T-3 Chris/Google, T-4 Navy spec, T-5 Ford V2.5) now show as honored. His Apr 23 `:eyes:` reaction is an in-progress re-review; no new corrections yet.
