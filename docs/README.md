# Skyways Timeline | Docs Folder Map

Working documentation for the Skyways Timeline project. Each file has a specific purpose: a few are living reference docs (read first to orient), others are working ledgers used for a specific phase of work and kept for history.

Project-level rules and architecture live in the root-level [CLAUDE.md](../CLAUDE.md) and agent-facing memory files live under `~/.claude/projects/…/memory/`. This folder is for project-scoped working docs.

---

## Living reference docs (read these to orient)

| File | What it is | When to use it |
|---|---|---|
| [PRD.md](PRD.md) | Product Requirements Doc for the timeline site. Canonical description of scope, audience, content model, visual design, and success criteria. | Any time you're about to change what the timeline IS (not just how it's styled). New section, new stat, new era, new audience. |
| [FIRESTORE_SCHEMA.md](FIRESTORE_SCHEMA.md) | Firestore `skyways_history_and_story` collection schema: fields, types, required vs. optional, doc ID format, field-by-field description. | Any time you're adding a new event, renaming a field, or writing a sync script. Pair with the rules in CLAUDE.md. |
| [TIMELINE_REVIEW.md](TIMELINE_REVIEW.md) | Standing review criteria for event copy: voice, acronyms, date format, source quality, categorization rules. | Before committing any event-detail edit or adding a new card. |
| [SITE_VERIFICATION.md](SITE_VERIFICATION.md) | Post-deploy verification checklist: stats banner values, filter categories, mobile layout, source drawers, contract totals. | After any Firestore sync, banner update, or Vercel deploy. Run through this before declaring a change shipped. |
| [SOURCE_VISIBILITY_RULES.md](SOURCE_VISIBILITY_RULES.md) | Canonical four-state source classification (internal / mixed / charles-approved / fully public) with banner colors (red / orange / beige / none) and the classifier regex. | Any time you add a new event, a new source, or change how a card is flagged for public distribution. Authoritative reference paired with `memory/feedback_internal_marking_style.md`. |

## Working ledgers (scope-specific, kept for history)

| File | What it is | When it's useful |
|---|---|---|
| [EVENT_CORRECTIONS_AUDIT.md](EVENT_CORRECTIONS_AUDIT.md) | Consolidated ledger of every correction Charles Acknin (CEO) and Tom Martin (senior vehicle engineer, "T-Money") gave across 3 Excel rounds + Slack, with per-item verification status. Created during the Apr 23, 2026 event audit. | Any time you're about to respond to a new Charles or Tom correction, OR before publishing any timeline change that touches historical events. Confirms no past ruling has been forgotten. |
| [STORYTELLING_GAPS.md](STORYTELLING_GAPS.md) | 20-gap ranked backlog of what the timeline still needs to feel like a great investor + public story. Five P0 gaps expanded (capital efficiency, Charles's hobby-kit origin, mission impact, Program of Record glossary, competitive moat). | When prioritizing next narrative-content work, pitching investor content, or scoping marketing sprints. |
| [STATS_AUDIT.md](STATS_AUDIT.md) | Line-by-line audit of every claim in the stats banner and stat drawers against a verifiable source. Used for the Apr 23 contracts-drawer truth-up. | When banner values change, when a new stat is added, or when a viewer pushes back on a claim. |
| [ACTION_PLAN_NEWSROOM_SYNC.md](ACTION_PLAN_NEWSROOM_SYNC.md) | Multi-step plan for syncing updates between the Skyways newsroom (Sanity) and the timeline. Tracks individual event enrichments with Sanity sources. | When adding newsroom-originated content to the timeline, or auditing whether newsroom changes have propagated. |
| [TIMELINE_MIGRATION_PLAN.md](TIMELINE_MIGRATION_PLAN.md) | Historical migration plan covering the JSON → Firestore move, the Apr 21 cleanup tiers, and the Charles Round I–III response plan. | Reference. Most items are resolved; the doc records the order of operations so future migrations can borrow the structure. |

## Session logs

| File | What it is |
|---|---|
| [SESSION_LOG_2026-04-23.md](SESSION_LOG_2026-04-23.md) | Running log of the Apr 23, 2026 work day: contract audit and deep-search, storytelling overhaul (era titles + taglines + year headlines), event correction audit, CVSI event addition, em-dash cleanup. Commits + rationale + follow-ups. |

Future session logs should follow the `SESSION_LOG_YYYY-MM-DD.md` naming convention and cover the same structure: what landed (with commit hashes), issues resolved, memory updates, open threads.

---

## How the pieces relate

```
PRD.md                 ←  the WHY + WHAT of the site
    │
    ├─ FIRESTORE_SCHEMA.md     ←  the DATA shape
    ├─ TIMELINE_REVIEW.md      ←  the COPY rules
    └─ SITE_VERIFICATION.md    ←  the CHECK list after shipping

Corrections & gaps (event-level work):
    ├─ EVENT_CORRECTIONS_AUDIT.md   ←  what Charles & Tom said
    ├─ STATS_AUDIT.md               ←  what the banner claims vs. truth
    └─ STORYTELLING_GAPS.md         ←  what's missing from the story

History:
    ├─ TIMELINE_MIGRATION_PLAN.md   ←  how we got here
    ├─ ACTION_PLAN_NEWSROOM_SYNC.md ←  newsroom integration
    └─ SESSION_LOG_YYYY-MM-DD.md    ←  daily audit trail
```

## Conventions

- All files use Markdown. Headings H1 for title, H2 for major sections, H3 for sub-sections.
- Dates in body copy use `YYYY-MM-DD` or `Month DD, YYYY`, never abbreviations.
- Dollar figures include the literal `$` and thousands separators.
- **No em dashes, en dashes, or arrows** (per project-wide rule). Use `|`, hyphen, comma, period, or the word "to" instead.
- Source citations link to the canonical source URL, or mark as "Skyways Internal | [person]" when no public source exists.
