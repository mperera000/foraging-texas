# House Rules for Foraging Texas Rebuild

You're the engineer. I'm the product manager. Follow these on every change.
The full spec is PLAN.md. The design contract is the approved mockup:
https://claude.ai/code/artifact/05a459b2-bbff-43ec-9f72-407811e3ac2e

## Project status
**NOT LAUNCHING YET.** Build and verify locally only. GitHub repo stays private.
Never set up hosting, buy domains, email anyone, or publish anything for this
project without Malithi's explicit go-ahead. (PLAN.md §13a.)

## Content gate
Original-site text and photos are copyrighted. Anything that could go public ships
only original write-ups + openly licensed photos (credited, license recorded in data).
(PLAN.md §14.)

## How to work
- Think first: before non-trivial code, say what you'll build and ask about anything unclear.
- Keep it simple: static site, no cleverness. No state library, no backend, no CMS.
- Change only what I asked. If you spot something else, tell me, don't do it.
- Use the /design-taste-frontend skill for all UI work.

## How to write code
- One home per concern: plant data only in src/content/plants/, tokens only in src/styles/global.css.
- Same name everywhere: it's a "plant", a "month", a "region" in code and UI alike.
- Handle the sad path: missing photo -> branded placeholder; empty filter result -> friendly empty state.
- Keep layers apart: components never hardcode plant facts; everything reads from content files.
- Self-contained features: month-rail, filters, ticker each live in their own component folder.
- Accessibility is not optional: semantic HTML, alt text from data, visible focus states, AA contrast.
- Pages must be readable with JavaScript disabled; JS is enhancement only.

## Definition of done (every change)
- Build passes, no console errors, content readable with JS disabled.
- Checked at 375px and 1280px widths.
- Matches the mockup's tokens (no new colors, no new fonts).
- Touched only what the task needed.
