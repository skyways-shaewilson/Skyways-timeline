# Session Log

Running chronicle of meaningful work on the Skyways Timeline site. One entry per working session. Most-recent first.

---

## 2026-04-23 (afternoon) — Mobile UX overhaul, CRADA reclassification

### What shipped

**Mobile search behavior**
- `.search-input` mobile font-size bumped to 16px to prevent iOS Safari's auto-zoom on focus. The zoom was horizontally clipping the left edge of every card (e.g. "Skyways" rendering as "ys"). 16px is the Safari threshold — anything below triggers magnification.
- `body.search-focused` class toggled on input focus / non-empty query. Collapses hero + stats banner, trims card chrome (hides thumbnail bg, bullets, value number, internal banner) so matching cards stack compactly above the keyboard while keeping title + detail readable.
- `clearSearch()` blurs instead of re-focusing, then calls an explicit sync so tapping the X, hitting Escape, or clicking a filter category cleanly exits search and brings the normal view back. Previously the re-focus kept the page in search mode.
- `navigateMatch()` uses `visualViewport.height` to detect an open keyboard and scrolls matches ~25% down the visible-above-keyboard area so the sticky search nav stays reachable after tapping prev/next.

**Mobile drawer placement (stat drawers + event-card source drawers)**
- Rule established and saved to memory as `feedback_mobile_drawer_placement.md` after three rounds of correction: **every drawer on mobile anchors under its trigger, never a bottom sheet, never floating.**
- `pinDrawer()` for stat drawers: source-list drawers (stats 2-5) stay absolute-positioned under their stat via CSS; JS sets inline `max-height = visualViewport.bottom - drawerTop - 20px` so the bottom scrollbar always stays above Safari's dynamic URL bar.
- Contracts-table drawer (wider, needs the full viewport width): `position: fixed` with EXPLICIT `top = stat.bottom + 8px` and `left: 8px / right: 8px`. No more `top: auto + bottom: 16px` bottom-sheet behavior.
- `positionSourceMenuMobile()` for event-card source drawers: clears inline styles on open, measures trigger rect, shifts horizontally if overflow-right, caps max-height dynamically, and triggers `window.scrollBy({ top: triggerTop - 120, behavior: 'smooth' })` when available below < 180px so the card moves higher and the drawer has room to open downward. Re-measures max-height after the smooth scroll settles (~380ms).
- Mobile scroll-dismiss listener removed for source drawers — the auto-scroll we just triggered would instantly close the drawer we just opened. Desktop scroll-dismiss unchanged.

**Filter legend**
- `pointer-events: none` on `.legend-x` and its SVG so taps always bubble to the parent `.legend-item` onclick. Previously the tiny X icon could capture the hit-test and feel like "only the X unselects".
- Mobile `.legend-item` padding bumped to `8px 4px` so the full filter button is a comfortable 32px tap target.
- `-webkit-tap-highlight-color: transparent` for cleaner iOS feedback.

**Stat banner polish**
- Label "Cost of Helicopter" renamed to "Helicopter cost" (shorter, reduces overlap risk).
- `.stat-value` and `.stat-label` on mobile get `min-width: 0` and `width: 100%` — flex children default to `min-width: min-content` which defeats the `minmax(0, 1fr)` grid cap. The longer labels ("Helicopter cost", "Navy Relationship") were overflowing into adjacent columns despite `overflow: hidden + text-overflow: ellipsis`.

**CRADA reclassification**
- NSLP-CRADA aircraft lease (id=113) was marked **Public** in the $46M+ contracts table, but Skyways has no press release or news coverage. The only public-release authorization is the CRADA document's own Article 19.
- Contracts-table row: `src-public` → `src-internal`.
- ID 113 source: `"Contract on File (Navy NSLP-CRADA, publicly releasable)"` → `"Skyways Internal — Contract on File (NSLP-CRADA, approved for public use)"`. Triggers `isInternalSource()` so the internal banner path fires.
- ID 113 detail last sentence: "Per Article 19, the agreement is approved for public use. No press release has been issued."
- New banner variant `internal-banner-approved-public`. `renderCard()` detects `/approved for public/i` in any source label and swaps the default "NOT APPROVED FOR PUBLIC DISTRIBUTION" copy for a clearer "APPROVED FOR PUBLIC USE, NO PRESS RELEASE". Same red styling, just different text.
- Firestore synced via `set(merge=True)` so `thumbnail` and `source_thumbnails` stayed intact.

### Lessons learned

1. **iOS input font-size < 16px triggers auto-zoom**, which clips cards horizontally. Hard rule: mobile inputs that get focused must be 16px minimum.
2. **`calc(100dvh - N)` alone is insufficient for absolute-positioned drawers.** CSS max-height caps total height but can't know WHERE the drawer starts. Use JS + `visualViewport` at open time.
3. **Flex children need explicit `min-width: 0` to respect grid `minmax(0, 1fr)`.** The default `min-width: min-content` beats `max-width: 100%` and `overflow: hidden + ellipsis`.
4. **Bottom-sheet positioning reads as "floating/disconnected" on mobile.** Anchor drawers under their trigger. (Corrected three times in this session before the rule stuck. Saving the memory file on correction #3 turned the cycle around — correction #4, applied to a different drawer type, landed on first commit.)
5. **Auto-scroll + scroll-dismiss are incompatible.** When `positionSourceMenuMobile` scrolls the page up to make room, a scroll-dismiss listener would close the drawer that just opened. Disable one or the other on mobile.
6. **Claude Preview's serve.py is sandbox-restricted.** Fall back to `python3 -m http.server <port>` + `curl | grep` for fast verification.
7. **Writing the rule to memory mid-session stops the repeat cycle.** After correction #3 on drawer placement, writing `feedback_mobile_drawer_placement.md` with explicit pre-commit grep checks + mental test matrix meant correction #4 landed right.

### Steps that worked well (keep doing)

- **Parallel tool calls for memory reads** — batching 5 file reads at once cut the discovery phase to one round-trip.
- **TodoWrite for multi-item work** — each user message added new items to a shared list; progress stayed visible and no item got lost.
- **Scheduled wakeups for Vercel verification** — `ScheduleWakeup` with `curl | grep -c "<unique-new-string>"` after each push verified deploy without polling or asking the user to refresh.
- **`set(merge=True)` for Firestore partial updates** — kept `thumbnail` and `source_thumbnails` intact while surgically updating `sources` and `detail`.
- **Bash verification script after each batch of edits** — scripted `python3 | grep` checks against the served HTML caught typos and missing changes before pushing.

### Steps that wasted time (avoid repeating)

- Re-attempting bottom-sheet positioning for the stat contracts-table after Shae said "too high" — should have landed on under-stat the first time.
- Starting with static `calc(100dvh - N)` instead of JS-driven visualViewport — added an extra correction round.
- Trusting the commit `git diff --stat` numbers without checking what actually landed (one commit shipped only 14 insertions when I expected 150+; turned out Shae's remote had my edits already via a merge, so the diff was small but the state was correct).

### Follow-ups / open items

- `feedback_mobile_drawer_placement.md` rule is enforced via grep, but consider adding a CI check (`.claude/hooks/`) so future edits can't reintroduce `bottom: 16px` inside a mobile drawer rule.
- "Navy Relationship" label on mobile is still close to the column width even after the `min-width: 0` fix — if overlap returns, consider shortening to "Navy Partner" or similar (not requested yet).
- The `internal-banner-approved-public` variant currently uses the same red styling as the warning banners. Shae may want a distinct color (amber / teal) later to visually separate "approved but internal" from "not approved" — ask if she flags it.

---

## 2026-04-22 (continued) → 2026-04-23 — Drawer stutter, hero redesign, Drive sweep, thumbnail dedup, typography scrub

### What shipped

**Scroll / stutter (finally nailed)**
- Found and killed the real stutter sources on trackpad slow scroll:
  1. `.year-gradient-overlay` had `transition: background 1s ease` + per-scroll-frame `style.background = ...` — every scroll frame kicked off a 1-second animated repaint of a full-viewport fixed element. Removed transition, added `transform: translateZ(0)` to promote to its own compositor layer.
  2. `.year-label` had `transition: opacity 0.15s, transform 0.15s` while the scroll handler wrote those same properties every frame — 60 overlapping 150ms animations per second per label. Removed transition; JS drives the values directly.
  3. `.dashboard-title-area` had a 400ms `grid-template-rows` transition on minimize (layout-affecting, re-ran layout pipeline for 13 frames). Removed.
  4. `.dashboard-hero` had `transition: gap 0.4s` (flex gap is layout-affecting). Removed.
  5. `.war-room-panel` had `transition: all 0.4s` — "all" silently animates every layout property. Scoped to `opacity, transform` only.
- Added hysteresis on minimize: `scrollY > 4` to minimize, `scrollY > 0` to stay minimized, restore only at exact top. Prevents trackpad momentum from re-triggering the 220ms transition near the boundary.
- `content-visibility: auto` + `contain-intrinsic-size: 1px 900px` on `.year-section` — off-screen year blocks are skipped for layout and paint. Biggest single scroll-perf win on this card-heavy page.
- `.drawer-active` class on the sticky header: while any stat drawer is open, layout-affecting header transitions are zeroed (`.brand-bar`, `.logo-wrap`, `.hero-section`, `.stats-banner-inner`, `.stat-value`). The drawer's `top: 100%` anchor otherwise slides every frame during the 220ms minimize animation, reading as stutter.
- Removed the scroll-close handler on stat drawers — its rAF close animation was fighting the browser's scroll animation. Drawer lives in a sticky header, travels with the viewport, doesn't need auto-close.

**Stat drawer behavior**
- Hover-reveal switched from CSS `:hover` to JS `mouseenter` + 120ms `mouseleave`-delay hide, because `visibility: hidden` + `pointer-events: none` on the hidden menu blocks the `::after` bridge from catching cursor traversal across the 8px gap.
- Tap-toggle generalized from `#contractsStat` only to every `.stat` via `bindStatMenus` IIFE.
- `pinDrawer(stat)` — on open, set `position: fixed` with a dynamic `top: rect.bottom + 8px`, `left: rect.left` (or right-anchored for stats 4/5), and `max-height: calc(100vh - top - 24px)`. The inner `.contracts-grid` now actually scrolls because the shell's max-height is derived from the drawer's real viewport distance.
- `overscroll-behavior: contain` on every drawer + inner scroll area so wheel events at the scroll boundary don't chain to the page.
- Hover zone tightened from the full 1/5-grid-cell to the `.stat-value` / `.stat-label` text ink via explicit `width: max-content; max-width: 100%;`.

**Hero section redesign**
- `.hero-section { height: 25vh; min-height: 200px; overflow: hidden; }` on landing. Main header capped at 25% of viewport.
- `.sticky-header.minimized .hero-section { height: 200px; }` — on scroll, hero collapses to a 200px image band. ~333% height increase over the previous padding-only 60px minimized hero, so the V3 aircraft becomes the dominant visual.
- Hero background is `aircraft_header.jpg` at `background-size: 400%` with a horizontal navy gradient (0.94→0.22) so the title stays legible on the left and the V3 shows through on the right.
- Removed the old V3 showcase card element (260×160 framed photo between title and telemetry) — replaced by the full-bleed background treatment.
- Removed the AUTONOMOUS AIR NETWORK eyebrow and the 28px lime hairline under the h1. Just `<h1>History &amp; Timeline</h1>` + subtitle now. Used `History&nbsp;&amp; Timeline` so the h1 wraps as "HISTORY &" / "TIMELINE" instead of the 3-line HISTORY / & / TIMELINE that was happening at narrower widths.
- Subtitle splits onto two lines from desktop down to 720px (`9 Years of Flying.` / `Built for the Mission.`); mobile collapses to one line.

**Telemetry panel**
- "SYS OVERRIDE: OFF" (confusing, negative, whole-pill blink) replaced with `LIVE` + a pulsing green status dot. Only the dot breathes; text is steady.
- `.tel-sub` column descriptors now wrap inside their grid column (`max-width: 100%; overflow-wrap: break-word`). No more overflow when "AUTONOMOUS FLIGHT DURATION" ran wider than its column.
- Telemetry footer relabelled `FLIGHT LOG  LAST PULL <date> · <time>`. Bumped from 8px/55% opacity to 10px/70% with a lime hairline border-top so the timestamp is actually readable. Removed the fake `NET: 42ms` counter and its setInterval (cosmetic, not real data).
- Added vertical lime hairlines between the three telemetry items so each TITLE / VALUE / DESCRIPTION trio reads as its own compartment.
- Telemetry panel stays inline with the title down to 720px; below that, stacks vertically (was 1024px — too eager).
- Telemetry panel hides entirely (`display: none`) on minimize, so the minimized-hero aircraft band carries the full width.

**Stats row + filter legend**
- Stats banner row: `gap: 0 32px` with a 1px divider in the middle of each gap (16px breathing room on either side) — reads as data-panel separators without crowding.
- Filter legend converted from flex to a 5-column CSS grid matching `.stats-row`, so each filter sits directly under its stat counterpart. No per-item padding; grid gap handles separation.
- Filter row stays on one line at every breakpoint.
- Tablet stats-row pinned at 5 columns (was 3) — consistency with desktop and mobile.

**Event cards**
- Replaced the round 12px category dot with a 4px full-height colored line running down the card's left edge. Rounds into the card's corners (8px standard, 10px highlight). Single-column grid now; `.event-dot` is `position: absolute` inside `.event-card`.
- Hover: bar widens 4 → 6px with a soft category-colored glow (`box-shadow: 6px 0 18px -4px rgba(..., 0.55)`).
- Left padding bumped across breakpoints (24/28/20/22) to make room for the bar; internal-banner negative margins track the new paddings so the red strip still reaches the card's left edge.
- Internal banner: `margin-top: 14px` (was -4px) so it doesn't overlap the `.event-meta` row above (tag + sources dropdown).

**Site polish**
- Scroll progress hairline: 2px lime bar pinned to the top of the viewport, fills left→right as the user scrolls. `transform: scaleX(p)` only, last-value-cached, so cheap.
- H1 refined: `font-size: 56px; font-weight: 700; letter-spacing: 0.5px; word-spacing: -0.05em;` so "HISTORY & TIMELINE" reads as one composed phrase, not three disconnected words.
- Year-label dialed from 800/-1px to 700/-0.5px to match the h1 refinement.
- `.event-date` + search placeholder moved gray-50 → gray-75 (3.37:1 → 7.8:1 on white, AA pass).
- Search input: `aria-label`, `type="search"`. Filter legend items: `role/tabindex/aria-pressed`, Enter/Space handlers, `:focus-visible` outline.
- Memory leak fix: card-tint `mouseover`/`mouseout` listeners moved out of `extractCardColors` (which was called on every render) into a single module-scope IIFE.
- ResizeObserver on `#stickyHeader` replaces per-scroll-frame `getBoundingClientRect` reads for year-label offset sync.
- `updateYearLabels` split into three passes: read all rects → compute styles → write all styles. One layout pass per scroll frame instead of N.

**Drive sweep — new contract findings (April 22)**
- STRATFI option exercises weren't in the archive:
  - FA22802599523 P00001 (Aug 6 2025): **+$1,581,645** obligated → $11.04M total
  - FA22802599523 P00002 (Mar 24 2026): **+$1,327,101.46** obligated → $12.37M total of $37M ceiling
- Correction on BWUAS 2.0 breakdown: base is **$294,443.20** (not $479,052.96). P00001 (Apr 8 2024) added $184,609.76 for MPU-5 + RIMPAC24 CLINs 0003+0004, bringing it to $479,052.96. P00002 added $1,344,682.79 for CLIN 0005 + 0006, bringing it to $1,823,735.75 total.
- Commercial revenue contracts not previously tracked:
  - Skyports / RWE NRE (Jun 2025): $302,157.07
  - ANA JMSDF Service Agreement (Apr 2024): per quotation
  - ANA JASDF Service Agreement (Oct 2024): $397,372.64
  - ANA 2025 Non-Recurring Engineering: $2,804,869.86 (Y1 + Y2)
  - DSV 2026 MSA: in progress
- Gaps that remain: DLA PO individual amounts (SATCOMv2 / Intelligen / DGPS under SPE8EJ21D0022), STRATFI ALIN-level dollar breakouts (0007, 0019, 0020, 0045, 0060 — check `STRATFI Master Sheet.xlsx`), no Phase 3 IDIQ mods beyond #3, no DIU W15QKN mods beyond P00004, no NASA / ARPA-E / DoT contracts.

**Thumbnail dedup (April 22)**
- Before: 21 unique thumbnails across 64 cards (v2-aboard-ship used 12x, v3-hover 9x, Drone Girl DSC01482 5x, etc.). 1 card had no thumbnail.
- After: 64 unique thumbnails / 64 cards / 0 repeats.
- Method: each repeat group kept one most-contextual card (v2-aboard-ship on the JMSDF destroyer card, v3-hover on V3 Block 1 First Flight, Drone Girl photo on the Nov 2025 Demo Day article card, etc.). Other cards got either (a) a better source article photo already sitting unused in their own `source_thumbnails` dict, or (b) a unique asset from the Skyways newsroom's Sanity CDN (`cdn.sanity.io/images/zlpq6b94/production/…`).
- Every URL HEAD-verified 2xx.

**Typography scrub (April 23)**
- Zero em dashes, en dashes, or arrow symbols in any user-visible copy: stat drawers, source link labels, contracts-table rows, Firestore `title` / `detail` / `tag` / `date_display`. CSS/JS comments are exempt (not rendered).
- Replacements: comma for list-item separators, hyphen for date ranges (`2019-22`), pipe (`|`) for "Publisher | Title" source labels and title / subtitle separators, "to" / "through" for arrows.
- Five Firestore docs scrubbed (ids 12, 29, 115, 116, 117). Local `Data/timeline_events_master.json` synced to match.

### Deploy state
- Vercel-GitHub integration was stale through most of the session; multiple empty-commit triggers eventually took effect, and `content-visibility`, `pinDrawer`, `LAST PULL`, `aircraft_header`, `min-height: 25vh` all verified live on `skyways-timeline.vercel.app` via `curl | grep` at session end.
- Known risk: Vercel may go stale again if the integration drifts. Default verification after any copy / data push: `curl -s "https://skyways-timeline.vercel.app/?cb=$(date +%s)" | grep -c "<unique-string-from-commit>"`.

### What's queued for next session
- **Reconnect Vercel-GitHub integration** so future pushes auto-deploy without manual redeploy dance. (Was on the earlier `/loop` check-in list; still open.)
- **Update the `$46M+` banner math to reflect STRATFI P00002** — current obligated is $12.37M, not the $3.55M SBIR portion in the current card copy. Decide whether the banner shows ceiling ($37M) or obligated.
- **Write timeline cards for the two STRATFI option exercises** (Aug 2025, Mar 2026) and the BWUAS 2.0 P00001 MPU-5/RIMPAC mod (Apr 2024).
- **Add commercial contract cards** (Skyports/RWE, ANA JMSDF/JASDF, ANA 2025 NRE) if the timeline's scope should include private-revenue customers alongside the $46M+ US-gov total.
- **Pull STRATFI Master Sheet for ALIN-level breakdowns** (file `1gqFisVpo7jR2GAabKZ5wZCDDSiNnOVGo` in Drive).
- **Correct the archive memory** for BWUAS 2.0 base ($294,443.20 not $479,052.96) — happening in this commit.

### Commits landed this session (most recent first)
- `ad5bc8a` — Scrub em dashes, en dashes, arrows from user-visible copy
- `9ec54ad` — De-duplicate every event card thumbnail (64 unique)
- `725231f` — Document thumbnail dedup rule in CLAUDE.md
- `1163577` — Hero minimalism + replace card dots with left-edge accent bars
- `9ebdad8` — Cut scroll stutter: hysteresis on minimize + content-visibility on year sections
- `d1edd26` — Make contracts-table grid actually scrollable
- `9f49d34` — Pin ALL stat drawers on desktop, not just contracts
- `1ac1019` — Stop internal banner from overlapping the card's meta row
- `6ec1bc2` — V3 aircraft as hero bg at 400%; revert hero padding
- `12c66ae` — Remove V3 showcase + keep "&" glued to "History"
- `2d67022` — Hero: 25vh on landing; 333% taller aircraft band on minimize
- `775bc13` — Kill trackpad slow-scroll stutter sources (real ones this time)
- `e3f4a7c` — Freeze layout transitions while drawer is open + grid-align filter row
- `6407030` — Contain stat-drawer scroll so wheel doesn't chain to the page
- `5935bcb` — Compartment spacing + telemetry columns + legible LAST PULL
- `5c6ca28` — Anchor stat drawers directly under their stat at every breakpoint
- `20ef70a` — Hide the whole telemetry panel when the header minimizes
- `d070937` — Tighten stat hover zone + stop drawer from spilling into neighbor stat
- `3d54d61` — Alignment, hover, and responsive polish
- `eba83a4` — Hero + filter + telemetry layout refinements
- `e3d0ff4` — Pushed sitewide UI/UX sweep (a11y, contrast, stutter, stat handler, V3 showcase)
- `34068fb` — Add V3 showcase image in the expanded hero (later removed in `12c66ae`)
- earlier: scroll-pattern iterations (`100/20`, `4/0`, smooth transitions, hysteresis/no-hysteresis)
