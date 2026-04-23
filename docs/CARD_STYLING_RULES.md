# Event Card Styling Rules

Standing rules for every timeline card, existing or future. Paired with `SOURCE_VISIBILITY_RULES.md` (which handles banner color) and `TIMELINE_REVIEW.md` (source-quality criteria).

Authored Apr 23, 2026 after auditing 65 cards and finding six that needed bullet restructuring plus several with stale arrow characters.

---

## Title Convention: `Hook | Why it matters`

Every card title follows this pattern: the hook sits left of a pipe separator and the "why it matters" signal sits to the right. A third pipe is allowed for additional context when useful.

**Hook (left of first pipe) = the single most important short phrase.**

- **Money events (contracts + funding):** the dollar amount is ALWAYS the hook. No exceptions. `$37M | USAF STRATFI | Path to Program of Record`, not `USAF STRATFI | $37M`.
- **Milestone events:** the event name or platform version. `V3 Block 0 | Full-Scale First Flight`, `Carrier Deck Trials | USS Gerald R. Ford`.
- **Defense events:** the exercise / program name, first-of-kind, or named counterpart. `ANTX 2019 | Skyways Beats Boeing`, `JMSDF | First Autonomous Resupply to Destroyer Akizuki`.

**Why (right of first pipe) = the significance.**

Pick one of:
- First-of-kind ("First 60-Mile BVLOS")
- Named customer or program ("USAF STRATFI", "USMC/GTRI")
- Specific wow stat ("Zero Skyways Personnel Aboard", "10 Bags of Blood, 300+ Miles")
- Strategic unlock ("Path to Program of Record", "Connectivity Leap")
- Explicit dollar signal when not already in hook ("$13M Series A | Thursday Ventures Leads")

**Avoid in titles:**
- Filler verbs: "Start of," "End of," "Added," "Accelerates," "Expansion" (unless factually the defining action)
- Insider contract numbers: the prime contract ID belongs in the detail field, not the title. `Navy DLA Order | DGPS Integration`, not `Navy DLA PO | DGPS (SPE8EJ21D0022 PO 0408)`
- Vague descriptors: "Platform Development," "Connectivity Added," "Team Expansion"

**Examples of the convention applied:**

| Before | After | Why |
|---|---|---|
| Series A | $13M (Thursday Ventures Lead) | $13M Series A | Thursday Ventures Leads | Money in hook |
| Start of Seed Fundraising | Rolling Close | $1M Seed Round Begins | Rolling Close | Money in hook, filler dropped |
| V2 Platform Development Accelerates | V2 Specs Set by Navy | 20 lb / 400 NM | Concrete spec replaces buzzword |
| Leadership Team Expansion | Leadership Expansion | Three Senior Hires | Count signals investment level |
| Starlink Connectivity Added | Starlink Aboard | Connectivity Leap | "Aboard" shows it's operational |
| USMC V2.2 Delivery & White Sands BVLOS Demo | First 60-Mile BVLOS at White Sands | V2.2 Delivered to USMC | First-of-kind promoted to hook |

---

## 1. Bullets vs. Prose

Use the `ev.bullets` array when:

- The card has **3+ parallel items** that repeat a pattern (contract mods, line items, named hires, equipment categories, timeline phases)
- The items would otherwise read as a run-on list inside the detail paragraph
- Each item can stand alone without connective tissue

Keep content in `ev.detail` prose when:

- The card is narrative, emotional, or story-driven (founder origin, first-flight moments, mission arcs)
- The information doesn't decompose into parallel items (a single claim with supporting context)
- The detail is short enough to read cleanly as one paragraph (under ~60 words)
- Items require connective words to make sense ("because," "then," "until")

Reference examples on the live site:

| Card | Pattern | Why it works |
|---|---|---|
| id=7 USMC/GTRI ($272K) | intro + 2 PO bullets + closing | Two POs are parallel, line items are distinct |
| id=9 Navy OTA ($575K to $2M) | intro + 4 mod bullets | Four modifications, each a discrete milestone |
| id=43 Leadership Expansion | intro + 4 hire bullets | Four named hires, parallel structure |
| id=103 V1 Origin | prose only (no bullets) | Emotional story, Charles's dad context |
| id=29 JMSDF First Resupply | prose only | Sequential narrative with connective flow |

## 2. Bullet Formatting Rules

**Preferred pattern: `Label: value`**

Most existing bulleted cards use this pattern. The label is bold-weighted by the reader because of the colon. Keep labels short (one to four words) and values terse.

```
Route: Grand Forks AFB to Cavalier SFS, North Dakota
Aircraft: V3 Block 2
Sponsor: OUSD Project ULTRA
```

**Also acceptable: plain descriptive**

When there is no natural label and the bullet is a full short phrase.

```
11 flights in a single day
9.4 hours total flight time
466 nautical miles of flight
```

**Not acceptable: ambiguous mixed patterns**

Within a single card, pick one pattern and stick to it. Don't mix label:value with plain descriptive unless there is a strong reason.

**Length**

- Each bullet aims for under 80 characters
- If a bullet runs longer than two lines on mobile, split it into two or rewrite
- Bullets are not paragraphs; if connective tissue is needed, move the content back to prose

## 3. Never in a Bullet (or Anywhere User-Visible)

- Em dashes (`—`), en dashes (`–`)
- Arrows in any direction: `→` `←` `↔` `⇄` `⇐` `⇒`. Replace with:
  - `to` for directional ("A to B")
  - `and` for bidirectional ("A and B")
  - `leading to the` for cause/effect ("X leading to the Y")
  - `through` for range progression
- HTML tags. Bullet strings are HTML-escaped by the renderer (`esc()`), so `<strong>`, `<b>`, etc. render as literal text. Don't try.

## 4. Content Relevance Rule

Every bullet and every detail sentence must describe **something Skyways did, earned, delivered, or directly experienced**.

Do NOT include on a Skyways card:

- **Parent-program ceiling figures that aren't Skyways' money.** A government IDIQ program ceiling or a Navy BWUAS 2.0 program budget is not a Skyways achievement. Mentioning "$100M program ceiling" on a $361K Skyways CLIN misleads readers into thinking Skyways has access to $100M.
- **Industry context unless Skyways is the subject.** "The autonomous drone market grew to $X billion" has no place on a Skyways contract card.
- **Partner performance that isn't Skyways-attributed.** If another company did the work, don't claim credit inline.

Case study (Apr 23, 2026): a "Program ceiling: $18.25M to $100M (July 2025)" bullet was removed from `id=111 CLIN 0005 Project ULTRA` because the ceiling refers to the Navy's BWUAS 2.0 program budget, not Skyways' own contract growth.

## 5. Version Designations

Use the clean conceptual name in user-visible copy. Internal nomenclature like "Block 2L" stays internal.

| User-visible | Internal shorthand (don't use) |
|---|---|
| V3 Block 0 | V3B0, V3.0 |
| V3 Block 1 | V3B1, V3.1 |
| V3 Block 2 | V3B2, V3.2 for production Block 2 |
| V3.2 | V3 Block 2L |
| V2.6 | V2.6, V2.6b (spec-exact when needed) |

## 6. V3 Capability Claims (Charles + Tom's standing rule)

NEVER state V3 max payload and max range simultaneously. The correct framing:

> 157 nautical miles range with 100 lb payload, OR approximately 35 lb cargo at 1,000 nautical miles.

Always "or," never "and." Any bullet or detail making claims about V3 specs must respect this rule. Reference: `memory/reference_tom_martin_feedback.md`.

## 7. Source Labels

- Use `|` as the separator (not em dash): `Skyways Internal | Charles Acknin`
- Public sources: `Publisher | Article Title (Month Year)`
- Internal with no press: `Skyways Internal | [person role]`
- Banner color handled automatically by classifier — see `SOURCE_VISIBILITY_RULES.md`

## 8. Card-Review Checklist (before shipping any new or edited card)

- [ ] Detail reads well as prose OR bullets are properly structured
- [ ] If bullets: pattern is consistent within the card (all label:value OR all plain)
- [ ] No em dashes, en dashes, or arrows anywhere in user-visible text
- [ ] Every bullet describes a Skyways action, earning, or direct experience
- [ ] V3 capability claims use `or` not `and`
- [ ] Version designations use the clean public form
- [ ] Source labels use `|` separator
- [ ] Source mix classified correctly (red / orange / beige / no banner per SOURCE_VISIBILITY_RULES.md)
- [ ] Banner color matches the classification

## Card-Review Checklist | Title Step

Before shipping a new card, confirm the title:
- [ ] Follows `Hook | Why it matters` pattern
- [ ] Money events have the dollar amount in the hook
- [ ] No filler verbs ("Start of," "End of," "Added," "Accelerates")
- [ ] No insider contract numbers
- [ ] No em/en dashes or arrows
- [ ] Under ~65 characters preferred (for mobile-friendly display)

## Scope Note | Internal Audit Fields

The `charles_corrections` array on event docs is an internal audit trail recording WHICH correction was applied in which round. It is never rendered on the live timeline. Em dashes, arrows, and other no-copy characters are tolerated inside `charles_corrections` entries (you'll often see them when quoting Charles verbatim). All the rules above apply to user-rendered fields: `title`, `detail`, `tag`, `date_display`, `sources`, and `bullets`.

## Revision History

- **2026-04-23**: Initial file. Documented bullet patterns, arrow prohibition, content-relevance rule, version-designation preference, V3 capability rule, review checklist. Case study of the Project ULTRA program-ceiling bullet removal. Scope note clarifying that `charles_corrections` audit-log field is exempt from the character rules.
- **2026-04-23 (evening)**: Added `Hook | Why it matters` title convention. 24 titles retitled across the 65-event corpus to apply the convention, with money always in the hook for money events.
