# Scope: Waterways Cruises & Events review build

Client: Waterways Cruises & Events (waterwayscruises.com), Seattle. Owner: Hilton Smith.
Asked by Mike Montes on November 9, 2026. Built as a no-cost DPA Branding review prototype to set beside the client’s own redesign. That redesign is unseen and is not described here.
Agency credit on the build: DPA Branding, mike@dpabranding.com.

This file matches the files in the repository. It is not a production launch and it does not change waterwayscruises.com.

On-page working notes (rights, drafts, confirm labels, and source commentary) are not on the public HTML. They live in `NOTES.md` and in this file. The prototype banner is the only disclaimer on the pages.

## Discovery gap (D08)

Google `site:waterwayscruises.com` discovery is **not complete**. From the research environment, google.com/search returned a JavaScript shell and web search returned no results. There is no Waterways exception on the research record, and this build does not claim the index is finished. Off-index URLs may still be missing. If more public URLs appear later, each one needs a genuine alias (301 at launch) or a gone/404 decision. They must not be sent to Home by default.

Mike’s November 9 request is the instruction to build anyway, with this gap written down.

## What shipped

91 KEEP addresses from `references/url-index.md`, one page each, at the live slug.

Also on the review host, and not part of the 91:

- `brand.html` and `Waterways-Brand-Standards.pdf` (US Letter, 8 pages)
- `404.html` for unknown addresses
- `Waterways-SEO-AEO-Compare.html`, `Waterways-SEO-Summary.html`, `Waterways-SEO-InDepth.html`, `Waterways-SEO-Gap-Report.html` (honest pending reports; live rubric stays 38/64; prototype column is not scored)
- 12 alias notes for MERGE urls (see below). This static host cannot emit HTTP 301. Each note is noindex, names the destination, and is marked “designed for go-live: HTTP 301.”

Every HTML page is `noindex, nofollow`. That is the review-build rule, including Christmas Eve. A public launch would use index,follow unless the client says otherwise (Confirm 26).

`seo-aeo-compare-facts.md` is in the repo root and is excluded from the GitHub Pages build so the public URL 404s.

## KEEP count

url-index KEEP rows: **91**. Prototype pages at those paths: **91**. None dropped.

Recount used by the brief: 8 dining cores + 13 private/fleet/vendor + 16 brand/visit + 1 memberships + 26 seasonal + 27 journal posts = 91.

## MERGE (alias notes, not extra KEEP pages)

| From | To | Why |
|---|---|---|
| `/about-us/contact-us/` | `/contact-us/` | Identical contact page |
| `/directions/mohai/` | `/directionsports/mohai/` | Identical MOHAI page |
| `/about-us/privacy-policy/` | `/privacy-policy/` | Second privacy text. Which text is legally current is still open |
| `/departure-ports/` | `/directionsports/` | Directions hub already lists the ports |
| `/corporate/` | `/private-events/#corporate` | Unique corporate copy is on Private Events |
| `/food-and-bar/dessert/` | `/dining-cruises/dinner/#dessert-2020` | 2020 dessert list, labeled, not a replacement menu |
| `/blog/`, `/blog/page/2/`, `/blog/page/3/`, `/about-us/blog/page/2/`, `/about-us/blog/page/3/` | `/about-us/blog/` | One journal hub. Posts stay at `/blog/{slug}/` |
| `/dining-cruises/sunday-supper-cruise/` | `/dining-cruises/supper/` | Already the live alias |

Bare `/fleet` and `/about-us` are the directory URLs GitHub Pages serves with a trailing slash.

## DROP (no page; not redirected to Home, About, or Dining)

These return the branded 404 on GitHub Pages. HTTP 410 is designed for go-live where the brief prefers gone. This host’s missing-file response is 404.

Promo landings still live on the production site, left out here: `/do206-offer/`, `/special-offers-and-promotions-for-public-cruises-hot-tub-boats/`, `/promotions-dining-cruises-concierge/`, `/unwind-concierge-ticket-entry/`.

`/lunch-cruises-information/` is a thin flyer leftover. `/silvercloud/` is a test page (“Free Breakfast: Test”) and is not folded into Hotel Partners. `/search/Seattle` and `/search/` are search routes and are not pages. `/confirmation/` is a booking utility and is not a page.

Named missing URLs from the November 3 audit or internal links, still absent: `/corporate/corporate-event-packages-draft/`, `/corporate/corporate-enhancements-duplicate/`, `/special-occasions/party-enhancements-draft/`, `/wedding-enhancements-duplicate/`, `/winter-sale-google/`, `/winter-sale-soc/`, `/promotions-googlead/`, `/groupflyerpromotion/`, `/black-friday-private/`, `/dining-cruises/dinner-cruise-winter/`, `/unwind-cruise-series/`, `/all-cruises/sip-sunset-summer-wine-and-sights-cruise/`, `/lake-union-sightseeing-cruise/`, `/private-events/special-occasions/special-occasion-packages/`, `/food-and-bar`, `/corporate/corporate-packages/`, `/directions/fishermens-terminal/`.

## Content handling

USE blocks from `references/content-inventory.md` are carried at the wording in `research` source extract (menus, policies, fleet, careers, journal, hotel list, FAQ). The FAQ page has 46 questions.

REWRITE, and only these kinds of changes:

- Home uniqueness clause removed. The held line is marked UNIQUENESS CLAIM.
- Sold-out, waitlist, and “best seller” badges removed from the demo.
- “Seattle’s Premier Yachts” and “one of the city’s premier venues” softened. Captain posting no longer says “leading” or “only upscale.”
- Lunch hub does not lead with code LOVE26.
- Memberships keeps the published 2025 Unwind terms under a pending-active notice and does not lead the navigation.
- Sailgating sold-out lines removed. Those four pages ask for a proposal, because the FAQ says public sailgating is a buyout (Confirm 20).
- Private-events FAQ homeport answer is a draft consistency note. Sightseer / MOHAI and the accessibility answers that name both ports stay.
- Global “Book now” is the in-site demo, not a vendor embed.

The 60,000-guest figure is not printed. Destiny buffet is not chosen between 30 and 25. “Up to 220 guests” is not printed as a current capacity. Charter and wedding dollar amounts are not restated as current; the three official PDFs are linked. Lakeside Event Space’s 40% offer is not shown as current. Founder names and roles are on About; education and earlier-career detail is held.

Privacy is the long live policy under one H1, labeled pending legal review.

Forms and the dining demo say preview only. They do not send, do not collect a card, and do not announce a successful booking or a received proposal.

## Brand tokens

Taken from the live site on November 9, 2026. Nothing else was added.

| Token | Value | Source |
|---|---|---|
| Navy | `#0e3060` | CSS `--primary-color` |
| Water | `#a5c2c9` | CSS `--secondary-color` |
| Mist | `#89adc5` | CSS `--banner-button-bg-color` |
| Paper | `#f5f7f9` | Live stylesheet |
| Ink | `#08090e` | Live stylesheet |
| White | `#ffffff` | CSS menu background |
| Black | `#000000` | CSS menu text |
| Gold | `#c0995e` | Average opaque gold pixel in the official lockup |
| Headlines | Montserrat, weight 400 | CSS `--font-headline-name` and `--font-headline-weight` |
| Body | ABeeZee, weight 400 | CSS `--font-body-name` and `--font-body-weight` |

Logo files, unmodified: `img/logos/waterways-logo-lockup.png` (the 1000×637 file named in the brief) and `img/logos/waterways-logo-mark.png` (the header mark). No white wordmark was published, so none was drawn.

Photographs are the live library, requested at a display width of 1400 or smaller and not enlarged. Stock-named Getty and iStock files are omitted. `lake-union.jpg` (3,943,949 bytes, empty alt) is omitted. Rights are pending. Captions do not say the pictures are the agency’s.

## Open holds

- D08 Google `site:` discovery, above
- Photo rights for the whole library
- NAP current, including 18th Ave W on the site footer versus 19th Ave W on the 2027 flyer footer, and 901 Fairview on some pages and PDFs
- Homeport per cruise (Dock 9, MOHAI, and Lake Union Piers all appear in print)
- Season year. 2027 is only the charter flyer’s document year
- Destiny buffet capacity, 30 on the fleet page versus 25 on the flyer. Reception 40 matches
- Guest count 60,000
- Uniqueness and ranking phrases
- Which registered tagline is primary
- RFP response time (1–2 business days on the form versus 24–48 hours in the FAQ)
- Lakeside Event Space and the 40% fee
- Whether memberships are still active after the 2025 Unwind season
- Which privacy text is legally current
- Google Business Profile URL
- Office hours for schema
- Booking provider (undecided; no vendor is embedded)
- Charter and wedding package dollars
- Special-occasions capacity, including any third-party 220 / 130 figures
- Hilton Smith and Shirley Turnbow biographies beyond names and roles
- Affiliations still current (PVA Green Waters, Visit Seattle)
- Whether past seasonal pages stay evergreen
- Form destination, when a real send is allowed
- Hotel partner list, including Silver Cloud, outbound links not rechecked
- Confirm 20 before any public sailgating ticket
- Confirm 34 before treating 2020 dessert items as current

Confidential economics, billing, and private ledgers are not in this repository and not on the public build.
