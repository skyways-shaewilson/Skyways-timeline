# Source Visibility Rules | Timeline Cards

Canonical rules for how timeline event cards are classified based on their sources, and what banner (if any) renders at the bottom of the card.

Authored Apr 23, 2026. Any change to the classification logic or banner behavior should be reflected here AND in `memory/feedback_internal_marking_style.md`.

---

## The Four States

Every event card resolves to exactly one of these four states:

| State | Trigger | Banner color | Banner text | Public distribution |
|---|---|---|---|---|
| **Internal only** | Source is `Skyways Internal + [contract #, CLIN, mod, PO, or similar non-public reference]`, OR any source starts with `[NOT PUBLIC`. Typical: military contracts without a press release. | **Red** `#d93025` on white | NOT APPROVED FOR PUBLIC DISTRIBUTION | Not approved |
| **Mixed** | At least one public press source validates the card AND the card contains internal-only information not found in any press release. | **Orange** `#c05621` on white | EVENT CONTAINS INTERNAL ONLY INFORMATION NOT IN A PRESS RELEASE | OK to share, scrub or confirm the internal-only details |
| **Charles-only (approved public, no PR)** | Charles Acknin is the only source, OR the source is `Skyways Internal | No Source` / `Skyways Internal | Not Published`. CEO direct attribution is authorized for public release. | **Beige** `#d4c18c` on navy `#0f2f53` | APPROVED FOR PUBLIC USE, NO PRESS RELEASE | OK to share |
| **Fully public** | All sources are external press / articles / gov docs. Or an external source plus a Charles-approved internal note. | No banner | (none) | OK to share |

## Source Classifier (authoritative)

Each source label is classified as one of three types:

1. Label starts with `[NOT PUBLIC` → **internal**
2. Label matches `Skyways Internal [separator] Charles Acknin` where separator is `|`, em dash, en dash, or hyphen → **charles-approved**
3. Label matches `Skyways Internal [separator] No Source` → **charles-approved**
4. Label matches `Skyways Internal [separator] Not Published` → **charles-approved**
5. Label starts with `Skyways Internal` (any other suffix) → **internal**
6. Anything else → **external**

Counts of each type drive the banner:

```
if (any source contains "approved for public"):
  BEIGE banner (explicit override for things like CRADA)
elif (internal > 0 AND external == 0):
  RED banner
elif (internal > 0 AND external > 0):
  ORANGE banner
elif (charles-approved > 0 AND external == 0 AND internal == 0):
  BEIGE banner
else:
  no banner  (fully public)
```

## Source URL Rule

Timeline source drawers may link only to external/public sources: public press, company press releases, public government databases, public government PDFs, public social posts, public corporate profiles, and similar open-web sources.

Internal source labels are allowed for auditability, but internal documents must not be linked from the timeline. Do not add Google Drive, Google Docs, Google Sheets, Slack, Asana, local file, internal repository, or other private artifact URLs to `source_urls` or Firestore source objects. For internal contracts, CLINs, POs, master sheets, or Charles/Tom corrections, keep the source label and leave the URL blank.

This rule applies even when the underlying internal document is unclassified. "Unclassified" is not the same thing as approved for public linking.

## Why these rules

- **Red is the reputational risk state.** Articles citing US government agencies need agency approval to publish if there is no press release. A card citing only a contract number or CLIN is effectively an unpublished government document. Sharing such a card publicly without approval is a real risk; the red banner is a hard-stop warning.
- **Beige is for "no press exists yet, but you can still share."** Charles Acknin is an authorized public spokesperson for Skyways, so his direct attribution is equivalent to a press release for public-distribution purposes. Same for "No Source" and "Not Published" internal notes that aren't sensitive. The beige color signals caution (no PR exists) without signaling risk.
- **Orange is the grey zone.** A public source validates the event, but the card includes detail that isn't in the public source — maybe a specific number, customer name, or internal nuance that Skyways can confirm but the press didn't mention. OK to share the event; scrub or re-confirm the internal-only addendum before quoting.
- **One banner, one visual signal.** Never combine the banner with card borders, recolored title/detail text, or background tints. The banner alone carries the signal.

## Do NOT

- Add red/orange/beige borders around the whole card
- Recolor the title, detail, or tag text
- Add inline pills or stamps in the meta row
- Use background tints or gradients on the card body
- Link internal Google Drive/Docs/Sheets, Slack, Asana, local files, contract PDFs, signed POs, CLINs, or private working docs from a public timeline source drawer

## Code references

- **Source classifier:** `classifySource(label)` in [index.html](../index.html)
- **Banner render:** `renderCard()` in [index.html](../index.html), banner decision tree near the top
- **CSS variants:** `.internal-banner`, `.internal-banner.internal-banner-mixed`, `.internal-banner.internal-banner-approved-public` in [index.html](../index.html) (around line 2080)

## Cross-references

- Memory (live reference for agents): `memory/feedback_internal_marking_style.md`
- Charles-trumps-public policy: `memory/feedback_charles_trumps_public.md`
- Charles feedback archive: `memory/reference_charles_feedback_archive.md`

## Revision history

- **2026-04-23**: Four-state rules formalized with distinct colors (red / orange / beige / no banner). Classifier refactored to 3 buckets (internal / charles-approved / external) from the earlier 2-bucket split. Charles-only cards now show the beige banner (previously showed no banner). Separator regex now accepts `|` in addition to em dash / en dash / hyphen after the em-dash cleanup migrated source labels to pipe format. Contracts stat drawer also gained an "Internal = no public press release found" disclaimer at the bottom to match the Internal pill semantics.
- **2026-05-07**: Added the source URL rule: public timeline drawers may link only to external/public sources. Internal source labels can remain visible for auditability, but internal documents stay unlinked even when they are unclassified.
