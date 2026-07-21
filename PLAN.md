# Merriwether's Foraging Texas — Rebuild Plan

A portfolio redesign concept of foragingtexas.com. This document is the instruction manual
for the AI coding tool that builds it. Approved mockup: https://claude.ai/code/artifact/05a459b2-bbff-43ec-9f72-407811e3ac2e

---

## 1. The Problem

Foragingtexas.com holds twenty years of trusted foraging knowledge trapped in a 2008
Blogger layout: a sidebar of ~300 blue text links, no search, no filtering, no mobile
experience. The content is gold; the container is unusable by modern standards.

**The real problem this project solves:** Malithi needs a portfolio piece that proves to
future clients she can take a dated, content-heavy site and modernize it, both visually
and structurally.

## 2. The Vision

A "living field guide": warm, photographic, and organized around the one question a
forager actually has: *what's ripening right now?* Design language locked in the approved
mockup: cream paper, deep forest green, chartreuse accents, amber color-blocks, Young
Serif display type, arched photo frames, real photography.

## 3. The Goal (three lines)

1. **Accomplish:** a published portfolio piece with obvious before/after drama that makes
   a stranger say "I want that done to my site."
2. **Instead of today:** two shipped projects, neither of which demonstrates the very
   sellable "modernize an existing site" skill.
3. **Why now:** client hunting is starting; the portfolio needs its anchor piece.

**Success test:** show old site + new site to someone for 30 seconds; they get it instantly.

## 4. Who It's For

- **Primary:** potential clients (small businesses / solo experts with dated sites) skimming a portfolio.
- **Secondary:** the demo must also genuinely work for its fictional user, a Texas forager
  on a phone, in a field, deciding if a berry is worth picking.
- **The owner:** Dr. Mark "Merriwether" Vorderbruggen. The finished demo gets emailed to him (see §14).

## 5. User Flows

### Happy path
Land on Today page → see current month + "peaking now" photos → tap a plant →
scan the At-a-glance facts panel (What/How/When/Where/Value) → read the caution box →
read harvesting prose → back to browse → filter by Type/Use/Region/In-season → next plant.

### Rough day
- **Slow connection in a field:** pages are static HTML, images lazy-load with sized
  placeholders; facts panel is text and renders first. No JS required to read a plant page.
- **JS fails/blocked:** browse page still renders all plants server-side; filters are
  progressive enhancement.
- **Dead link / missing plant:** custom 404 in the design language pointing to browse + search.

### Edge cases
- Month with few plants in season (January): "leaner month" note, show year-round plants (yaupon, sassafras).
- Plant with no photo yet: branded placeholder block, never a broken image.
- 300-entry scale: browse grid paginates or lazy-renders past 60 cards; filters stay instant (client-side index).
- Sharing: every plant page has proper OG meta so links unfurl with the photo.

## 6. Features

### V1 (build now)
- Today page: month rail (12 months, current auto-selected), "peaking now" / "last chance" rows, in-season ticker
- Browse page: card grid, filters (type, use, region, in-season-now), count
- Plant page: photo, facts panel, caution box, prose sections, similar-plants row
- ~25 plant entries from open data (see content gate, §14)
- Safety block + disclaimer footer + YouTube/original-site links + photo credits
- Responsive (mobile-first field use), accessible (WCAG AA), SEO meta + sitemap
- Portfolio case-study page: before/after screenshots + write-up

### V2+ (later)
- Clickable Texas ecoregion map as a browse mode
- Full 300-plant dataset (requires owner permission or sustained open-data effort)
- Search-as-you-type
- "Near me" geolocation filtering
- Classes/workshops calendar section (exists on original site)

## 7. System Architecture

```
Visitor's browser
   │
   ▼
Static site on CDN (Vercel)                  ← deployed from GitHub on every push
   ├─ Pages pre-built by Astro at deploy time
   ├─ Plant content: one JSON/MD file per plant  ← THE SWAPPABLE CONTENT LAYER
   ├─ Photos: optimized at build time (Astro assets)
   └─ Small JS islands: month rail, filters, ticker (everything readable without them)
```

No database, no auth, no server. Content lives in `src/content/plants/*.json`; changing
the dataset never touches components. This is the copyright-gate design: swap 25 files,
ship.

## 8. Tech Stack

| Tool | Job | Why | Cost |
|---|---|---|---|
| Astro | Static site framework | Content-collection sites are its exact sweet spot; ships ~zero JS by default | Free |
| Tailwind v4 | Styling | Matches design-taste-frontend workflow | Free |
| Young Serif (self-hosted) + system sans | Type | Locked in mockup; OFL license | Free |
| GitHub | Code home + ownership | Own your code, walk anytime | Free |
| Vercel | Hosting + CDN | Already used on her other projects; auto-detects Astro | Free |
| Domain (optional) | e.g. foragingtexas-concept.com | Portfolio polish | ~$12/yr |

**Build rule:** frontend work uses the `/design-taste-frontend` skill. No third-party
wrappers for anything; there are no integrations to wrap anyway.

## 9. Data Model

One file per plant (`src/content/plants/agarita.json`):

```json
{
  "name": "Agarita",
  "latin": "Mahonia trifoliolata",
  "family": "Barberry",
  "abundance": "common",
  "type": "Shrub",
  "uses": ["Fruit"],
  "regions": ["Central", "West"],
  "months": [4, 5],
  "flowerMonths": [2, 3],
  "facts": { "what": "...", "how": "...", "when": "...", "where": "...", "value": "..." },
  "caution": "Stiff spines on every leaf tip...",
  "sections": [{ "title": "Harvesting", "body": "..." }],
  "photos": [{ "src": "...", "alt": "...", "credit": "...", "license": "CC BY-SA 4.0" }],
  "similar": ["yaupon-holly"]
}
```

Every photo carries credit + license fields; the footer credits render from data.

## 10. House Rules for the AI (put in CLAUDE.md)

```markdown
# House Rules for Foraging Texas Rebuild

You're the engineer. I'm the product manager. Follow these on every change.

## How to work
- Think first: before non-trivial code, say what you'll build and ask about anything unclear.
- Keep it simple: static site, no cleverness. No state library, no backend, no CMS.
- Change only what I asked. If you spot something else, tell me, don't do it.
- Use the /design-taste-frontend skill for all UI work. The mockup is the design contract.

## How to write code
- One home per concern: plant data only in src/content/plants/, tokens only in the theme file.
- Same name everywhere: it's a "plant", a "month", a "region" in code and UI alike.
- Handle the sad path: missing photo → branded placeholder; empty filter result → friendly empty state.
- Keep layers apart: components never hardcode plant facts; everything reads from content files.
- Self-contained features: month-rail, filters, ticker each live in their own component folder.
- Accessibility is not optional: semantic HTML, alt text from data, visible focus states, AA contrast.

## Definition of done (every change)
- Build passes, no console errors, works with JS disabled for reading content.
- Checked at 375px and 1280px widths.
- Matches the mockup's tokens (no new colors, no new fonts).
- Touched only what the task needed.
```

## 11. Integrations

None in V1. The YouTube link is a plain anchor. This is deliberate: zero moving parts.

## 12. Cost Breakdown

$0/month. Optional domain ~$12/year. There is no architecture cost trap here because
there is no server and no database; the CDN free tier covers portfolio traffic thousands
of times over.

## 13. Timeline

- **Days 1–2:** setup, data layer, 25 entries migrated to open data
- **Days 3–5:** design system + three page types to mockup parity
- **Days 6–7:** polish, a11y pass, SEO, local production build
- **Later, when ready (see §13a):** deploy, case-study page, Merriwether email
- Total to "done on my machine": **~1–1.5 weeks** part-time.

## 13a. NOT LAUNCHING YET (current status)

Malithi is not ready to put this site live. Until she says otherwise:

- **Everything is built and verified locally** (`npm run dev` / `npm run build && npm run preview`). The finished site runs entirely on her machine.
- **GitHub repo stays PRIVATE.** Push for backup, never for publishing. (A private repo is invisible to the world; going public later is one setting.)
- **No hosting setup, no domain purchase, no Merriwether email, no community posts.** Phases 6b and 7 below are parked.
- The nice part of the static-site choice: "going live later" is a 15-minute step (connect repo → deploy), and nothing built now has to change. There is no penalty for waiting.
- **What "done" means for now:** the full site working locally + a folder of screenshots/screen-recording for showing people in person or privately.

## 14. The Content Gate (do not skip)

- **Private build:** real site content may be used locally as a working dataset.
- **Anything public** (deploy, portfolio, artifact shared beyond this session) ships ONLY:
  original write-ups in Malithi's own words + openly licensed photos (Wikimedia Commons /
  USDA), credited, **or** content used with Merriwether's written permission.
- **The email (send when demo is polished):** short, warm, link to the live demo:
  "I'm a web developer, longtime fan of the site. I rebuilt it as a design concept.
  Want it? No strings." Best case: blessing/testimonial/first client story. No reply in
  2 weeks: publish with the concept disclaimer and swapped content, exactly as built.
- Footer always carries: "A redesign concept... not the official site" + safety disclaimer.

## 15. Distribution (the portfolio is the product)

- **First 10 "users":** target clients and peers. Concrete moves, in order:
  1. Publish the case study on the portfolio (before/after opens the page).
  2. Email Merriwether (owner blessing is the jackpot outcome).
  3. Post the before/after to one design community (e.g. r/web_design showcase or a
     design Slack/Discord) framed as "unsolicited redesign of a beloved 2008 Blogger site."
  4. LinkedIn/X post with the two screenshots side by side.
- **Growth loop:** none pretended. A portfolio piece grows by being shown; the case-study
  page IS the shareable unit. Metric: inquiries that mention the foraging piece.

## 16. Riskiest Assumption

"A redesign concept of a niche foraging site will impress general clients."
**Cheap test (before over-polishing):** once the Today page looks real, show it with the
old site side-by-side to 5 people (ideally 2 small-business owners). If they don't react,
the case-study framing (not the build) needs work: lead harder with before/after.

## 17. Before Launch Checklist

- [ ] Content gate satisfied (§14): no copied text/photos in the public build
- [ ] Photo credits + licenses rendered in footer
- [ ] Safety disclaimer on every plant page + footer
- [ ] Lighthouse: performance ≥ 90 mobile, a11y ≥ 95
- [ ] OG meta + favicon + sitemap + robots.txt
- [ ] Custom 404
- [ ] Run the three audits: security (minimal surface, still check headers/links),
      scalability (image weights, lazy-loading), production readiness (broken links, missing alts)

## 18. Build Phases with Checkpoints

**Phase 0 · Send-ahead** — Draft (don't yet send) the Merriwether email and park it in
the repo. *No checkpoint needed.*

**Phase 1 · Foundation** — Astro project, **private** GitHub repo, CLAUDE.md house rules,
tokens file from the mockup (colors, Young Serif @font-face, radii). No hosting setup.
> 🔖 CHECKPOINT: `npm run dev` shows a hello-world page with the tokens applied; repo
> pushed and confirmed private.

**Phase 2 · Data layer** — plant schema, 25 entries written in original words from open
data (USDA PLANTS, field-guide facts), photo pipeline (Commons downloads + credits file).
> 🔖 CHECKPOINT: `npm run build` renders 25 plant pages from data alone. Verify: add a
> 26th dummy plant file, page appears; delete it, page disappears. Nothing else changed.

**Phase 3 · Plant page** — the At-a-glance facts panel, caution box, prose, photos,
similar-plants row. This page first: it's where the content lives.
> 🔖 CHECKPOINT: Agarita page matches mockup at 375px and 1280px. Verify with screenshots
> against the mockup side by side.

**Phase 4 · Browse + filters** — grid of arched cards, filter pills, in-season logic,
empty state. Server-rendered list, JS enhancement for filtering.
> 🔖 CHECKPOINT: filters combine correctly; disable JS and confirm all plants still render.

**Phase 5 · Today page** — hero, month rail, ticker, peaking/last-chance rows, safety block.
> 🔖 CHECKPOINT: change month → rows and ticker re-sort. Auto-selects real current month.

**Phase 6 · Polish** — a11y pass, perf pass (image weights!), SEO meta, OG images,
404, favicon. Local production build (`npm run build && npm run preview`). Capture the
screenshot/recording set for private showing.
> 🔖 CHECKPOINT: Lighthouse mobile ≥ 90/95 against the local preview; screenshots folder done.

--- PARKED UNTIL MALITHI SAYS "GO LIVE" ---

**Phase 6b · Deploy (parked)** — connect the private repo to Vercel, optional
domain. ~15 minutes; nothing above changes.
> 🔖 CHECKPOINT: live URL loads; share a plant link, unfurl looks right.

**Phase 7 · The case study (parked)** — portfolio page: before/after hero, 3 design
decisions explained, link to live demo. Send the Merriwether email. Run the §16
five-person test.
> 🔖 CHECKPOINT: case study read by one real human who isn't you.

## 19. Open Questions

- Domain name for the demo (subdomain of portfolio vs. standalone)?
- Does the portfolio itself exist yet as a site to host the case study? (If not, that's
  its own small project and this piece is its first entry.)
- Merriwether's answer (email in Phase 7) determines V2 content scope.

## 20. Words Worth Knowing (session glossary)

- **Static site:** every page is pre-built as plain HTML at deploy time; nothing computed per-visitor. Fast, free, unhackable-ish.
- **Content collection:** a folder of structured files (one per plant) that the framework turns into pages.
- **Data URI / inlined asset:** a file embedded directly inside the HTML as text (used in the mockup so the artifact needs no external requests).
- **Progressive enhancement:** the page works without JavaScript; JS only makes it nicer.
- **OG meta:** the tags that control how a link looks when pasted into chats/social.
- **CC BY-SA etc.:** Creative Commons licenses; free to use with credit (and share-alike where noted).
