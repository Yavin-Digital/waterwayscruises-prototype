# PROTOTYPE BRIEF: Waterways Cruises & Events (slug waterwayscruises)

To: Proton Bob (Prototype). CC: JohnWick (Task Manager).
From: Randy (Research), Friday Nov 6, 2026, America/Chicago (CT).
Status: **DRAFT. NOT SIGNED OFF. BUILD HELD.**

This file is a complete build packet written so work can start the moment Research signs off. It does **not** authorize HTML, production publish, live-site changes, client contact, spend, or OS writes. Parent delivers it only after sign-off.

Where this brief and `marketing-plan.md` differ, **this brief wins**. Differences are the Research overrides in `growth-review.md` (C1-C7). Max's strategy is accepted; those overrides stop live booking embeds, invented sailgating tickets, packed home menus, and "stale homeport" overwrites.

## Why build is held

Required Google `site:waterwayscruises.com` discovery is **OPEN** and not complete (dossier D08). From the box, google.com/search returned a JS-required shell and WebSearch returned no results. There is **no Waterways exception**. The Orion exception does not apply and must not be reused. No retries or evasion. Off-Google-index URLs may still be missing.

Sign-off and build authorization need one of: someone with a normal browser runs Google `site:` to exhaustion, or Mike grants an explicit Waterways-specific exception. Other unknowns below are labeled placeholders. They do not invent facts; they also do not, by themselves, hold this draft.

Agency attribution in client-facing chrome: **DPA Branding only**.

---

## Inputs (read before building, after sign-off)

- `references/dossier.md` (D01-D47)
- `references/url-index.md` (KEEP 91 / MERGE 15 / DROP 26 including `/confirmation/`)
- `references/content-inventory.md` (**736** block rows: **682 USE / 27 REWRITE / 27 DROP**). This is the block-level content map. Do not silently change those tags.
- `references/source-content.md`, `references/source-assets.md`, `references/assets/`, `references/files/` (three on-site PDFs) and `references/pdf-notes.md`
- `references/audit-claim-verification.md`, `SEO-AEO-Audit.md` (live **38/64**; proto unscored)
- `references/seo-aeo-report-plan.md`, `references/seo-aeo-compare-facts.md`
- `marketing-plan.md` (Max, provisional) and `growth-review.md` (this pressure-test)
- `INTERNAL-CONFIDENTIAL-economics.md` exists for internal exclusion only. Do not open it to write client copy. Do not quote it.

House rules: prefer the client's words; sourced REWRITE and clearly labeled draft recommendation copy are allowed when inventory marks REWRITE; never unsupported claims or invented metrics; no emojis; MARCO; mobile first; contact no one.

Expected review host after a future repo exists: waterwayscruises.clientreview.co (or the Yavin convention at the time). No proto repo exists yet.

---

## 1. Project goal

Rebuild the live Waterways Cruises & Events site (https://waterwayscruises.com/, WordPress VIP with FareHarbor embeds today, live SEO 38/64) into a full, mobile-first **HTML prototype** that:

1. Ships every **91 KEEP** URL as its own page at official density (full menus, full policies, full fleet copy, full editorial). Hubs index children; they do not replace them. No silent KEEP drops. No short-card substitution for a KEEP page.
2. Makes two equal doors obvious on the first phone screen: **Dining Cruises** (self-serve public table) and **Private Charters** (whole-boat inquiry). Premium hospitality on Seattle's lakes, not a sightseeing discounter and not a generic experiences marketplace.
3. Demonstrates the client's stated public flow: **cruise type, then date, then party (about 2-10), then optional enhancements**. Demonstrates a separate Request a Proposal path for whole-boat and semi-private demand. Both are DEMO ONLY.
4. Holds unverified uniqueness, guest-count, season year, ports, capacities, flyer dollars, and photo ownership behind placeholders. Does not pick a booking provider.
5. Removes promo leftovers, search-result routes, test pages, and named 404 drafts with **true HTTP 410 or genuine HTTP 404** — never a 200 soft-404, never a blanket 301 into Home, About, or Dining.
6. Fixes High and Medium live SEO items that static HTML can carry; labels launch-only items "Designed for go-live, add at launch." Does **not** score the unbuilt proto. After KEEP pages exist, Randy builds the four SEO/AEO report pages plus the non-public facts ledger.

Mike asked that it be sleek (S5). Visual bar is MARCO (Moment, Air, Restraint, Craft, Overdeliver) using the existing brand and official imagery only.

---

## 2. Client understanding

- Brand: Waterways Cruises & Events (schema sometimes "Waterways Cruises and Events"). Use **Waterways Cruises & Events** (D09).
- Live host reviewed: https://waterwayscruises.com/ (S1, 2026-11-06).
- Part of Seattle's lake and Puget Sound scene since 1994; started with one yacht in April 1994 (About). Co-founders Shirley Turnbow and Hilton Smith; Hilton Smith is CEO. Names and roles USE; bios [HILTON / SHIRLEY BIOS].
- Four vessels: Emerald Star (105 ft), Olympic Star (90 ft), Destiny (64 ft), Sightseer (70 ft in meta). Sightseer: 48 seated; reception 100 in warmer months / 60 in colder months; no plated dining; MOHAI departure as published (D24) [CONFIRM]. Destiny reception 40 is consistent; buffet is [DESTINY BUFFET CAPACITY] (site 30 vs 2027 flyer 25).
- Public footer homeport: Fishermen's Terminal Dock 9, 3919 18th Ave W, Seattle WA 98119. Office (by appointment) and mailing: 4005 20th Ave W Suite 228, Seattle WA 98199. Phone (206) 223-2060. Emails contact@waterwayscruises.com and events@waterwayscruises.com. Other live pages and PDFs also name 901 Fairview Ave N / Lake Union Piers and, on the 2027 flyer footer, 3919 19th Ave W. Use the departure printed on each cruise. Do not invent one global overwrite ([HOMEPORT PER CRUISE], [NAP CURRENT]).
- Two products (S2/S3): (1) private whole-boat charters and events, quote-based through Request a Proposal; upper-deck rentals and public buyouts sit on this path; (2) individual dining cruises, self-serve.
- Core dining: Premier Seattle Dinner Cruise (2.5 h, plated, ages 13+, Wed-Sat; summer 7:00 to 9:30 pm from May 1, winter 6:00 to 8:30 pm from Oct 1); Weekend Brunch (2 h, buffet, all ages); Sunday Supper (2 h, buffet, all ages, select Sundays); Taco Thursday (2 h). Seasonal and event pages listed in the sitemap stay full pages.
- Booking provider undecided (FareHarbor today plus "two options"). Prototype checkout is provider-neutral and takes no real bookings (D06).
- The client's own redesign ("probably draft 4.0") has not been seen. Do not mention, compare, or react to it.
- The 2027 charter flyer is labeled "2027 private charter rates". That is the document year only. Never write 2027 as the meeting's January-February / March / May season year ([SEASON YEAR], D07).
- Prototype offer, meeting process, and commercial terms are internal (D01-D05). DROP from client copy.

---

## 3. Audiences (priority)

Sizes unknown; no analytics in the packet.

1. Date-night and couples diners (public door; stated discovery gap). Served by Home, `/dining-cruises/`, `/dining-cruises/dinner/`, calendar, gift cards, Valentine's pages, FAQ dress and seating answers.
2. Families and multi-generational locals (public door; stated discovery gap). Served by brunch, supper, taco Thursday, holiday sights, Thanksgiving, and other all-ages pages, plus FAQ children and logistics answers.
3. Celebrants booking a table, not a boat (party about 2-10). Public FAQ special-occasions answers (decor, cake) plus dining enhancements. `/special-occasions/` itself is a private-celebration page and stays on the charter path.
4. Visitors and hotel guests. Hotel Partners, Directions, dining hub, calendar, gift cards.
5. Whole-boat private charter planners: corporate, weddings and rehearsal dinners, celebrations, school events, memorials (RFP types). Private Events, fleet-as-rooms, catering PDF, wedding packages after [CHARTER RATES], vendors, groups/buyouts, demo RFP.
6. Sports fans and seasonal celebrants (sailgating, Seafair, holidays, wine pairing), using the matching KEEP pages. Sailgating follows the FAQ buyout rule until Confirm 20.
7. Operators, applicants, and partners: Careers, vendors, nonprofit program, Contact, Privacy.

Home presents both doors as peers. Every public dining page ends at the demo book path or Call. Every private page ends at Request a Proposal or Call, not at a dining checkout.

---

## 4. Positioning and primary message

Their frame, in their words: "For An Unforgettable Experience, Just Add Water®" (home) and "For an Unforgettable Event...Just Add Water."® (private events). Confirm [TAGLINE FORM]; prefer the home Experience line until then. Do not invent a slogan that replaces the registered mark.

Positioning line (NEW COPY, review only, never the H1, needs client approval): "Dining cruises and private yacht events on Seattle's lakes, since 1994."

Recommended home text H1 (the live H1 is the logo image): "Dining cruises and private events on Seattle's lakes." Line under H1: the live home body with the uniqueness clause removed: "Experience Seattle from a new perspective with Waterways Cruises & Events. Based in Fishermen's Terminal, we offer experiences on Lake Union and Lake Washington, from public dining cruises to fully private charters and events." Hold "the city's only dining cruise company" as [UNIQUENESS CLAIM].

First mobile screen (390x844), readable type and spacing, not a packed fold:
1. Brand and chosen tagline (or the approved text H1).
2. One lakes-and-two-doors descriptor. No uniqueness clause, no 60,000, no season year.
3. Two peer actions: **Dining Cruises** → `/dining-cruises/`; **Private Charters** → `/private-events/`.

Immediately below that viewport: substantial teasers for Dinner, Weekend Brunch, and Sunday Supper (name, duration, meal style, ages, one live sentence) linking to full pages; upcoming seasonal cruises without SOLD OUT or waitlist; Private Events teaser using the live paragraph; six homepage testimonials verbatim with published attribution and no stars; Instagram embed if it stays official and light. Do not paste entire menus onto Home.

Persistent header on every page: logo (to `/`), menu, Dining Cruises (to `/dining-cruises/`), Request a Proposal (to `/request-a-proposal/`). Phone sticky bar after the hero: Dining Cruises | Request a Proposal; on a dining product page, Book this cruise (demo) | Call. Two actions maximum. Hidden at 1024 and up.

Title pattern: Home "Waterways Cruises & Events / Dining Cruises in Seattle". Inner pages: "[Product] in Seattle / Waterways Cruises & Events" when Seattle is missing today (Gift Cards, FAQ, Fleet, Memberships, and similar). Unique meta per sailgating and event page. Default Dinner title without treating "Best Romantic Dining" as an award unless Confirm 37 says to keep those words.

Home meta: Waterways Cruises & Events offers dining cruises and private charters on Lake Union and Lake Washington in Seattle, from Fishermen's Terminal. Book a public cruise or request a proposal for a private event. No "only", no 60,000, no unverified stars.

---

## 5. Conversion rules (demo only)

### Journey A — whole-boat private inquiry
Home or nav → Private Events (or corporate section, wedding packages, special occasions, groups/buyout) → fleet vessel as a room → catering / vendors / ports → Request a Proposal (demo form, no send). Semi-private upper-deck rentals and public buyouts stay here. FAQ charter answers (cake-cutting $2/person and $3 wedding/tiered, 20%+ recommended gratuity, decor lists) support the inquiry. No dining checkout on this path. Response-time sentence uses [RFP RESPONSE TIME].

### Journey B — self-serve dining
Home or nav → Dining Cruises hub or a named product or Cruise Calendar → **cruise type → date → party size (2-10 typical) → optional enhancements** (examples already in copy: rose petals and chocolate-covered strawberries, guaranteed window table, Steak & Lobster on Dinner) → review. Gift cards are a side door into this path. Groups of 10+ may use `/groups/` terms without being forced into a charter.

### Demo implementation (override C1)
- Front-end only. No POST to the client, to Constant Contact, to FareHarbor, or to any other vendor.
- Do not iframe, redirect to, or call fareharbor.com. Header flow 1011559 and gift-card item 412031 document the live site only.
- No live availability, SOLD OUT, waitlist, or scraped "current" ticket prices.
- No credit card, CVV, billing address for payment, wallet, or bank fields. The review step summarizes the demo selection and states that no ticket was issued and no payment was taken.
- No fake "we received your proposal" or "your tickets are confirmed" success.
- Provider chrome is generic. DROP "Powered by FareHarbor" (B0732).
- Sailgating (override C2): the four dated 2026 pages default to Request a Proposal and Call until Confirm 20 says they are publicly ticketed. The FAQ currently says public sailgating is not offered and those cruises are full-vessel buyouts. Do not invent a public ticket.

RFP demo fields from the live form: event type (Corporate, Wedding, Rehearsal Dinner, School, Special Occasion, Memorial, Other), contact details, date, guest count, time window (afternoon back by 3:00 PM; evening boarding from 5:30 PM), budget, how they found us, accommodations, referral/promo, comments. Contact, careers, and nonprofit forms likewise: visible fields, no send.

Secondary CTA: Call (206) 223-2060 as `tel:2062232060`. Dining pages may offer a quiet text link to Private Events when a party outgrows a table; private pages may offer Dining Cruises for planners who only need a table. Do not swap the primary button.

---

## 6. Full sitemap and page jobs

All 91 KEEP URLs ship at their live slugs. Grouped nav (toggles, not dead-end parents). On phones the menu sheet lists the group label and then every child.

- Dining Cruises: `/dining-cruises/`; `/dining-cruises/dinner/`; `/dining-cruises/weekend-brunch-cruise/`; `/dining-cruises/supper/`; `/taco-thursday-seattle-lakes-cruise-tour/`; `/lunch-cruises/`; `/cruise-calendar/`; `/gift-cards/`.
- Seasonal Cruises: `/holiday-cruises/`; `/parade-of-lights-cruises/`; `/thanksgiving-day-cruise/`; `/holiday-cruises/holiday-dinner-cruise/`; `/holiday-cruises/holiday-sights-cruise/`; `/holiday-cruises/christmas-eve-dinner-cruise/`; `/holiday-cruises/new-years-eve-dinner-cruise/`; `/new-years-eve-party-cruise/`; `/willamette-valley-vineyards-wine-pairing-cruise/`; `/seafair-cruises/`; `/seafair-party-blue-angels/`; `/seafair-blue-angels-bbq-lunch-cruise/`; `/mothers-day-dinner-cruise/`; `/mothers-day-brunch-cruise/`; `/holiday-cruises/fathers-day-brunch-cruise/`; `/fourth-of-july-fireworks-dinner-cruise/`; `/fourth-of-july-fireworks-party-cruise/`; `/easter-brunch/`; `/all-cruises/valentines-day-lunch-cruise/`; `/valentines-dinner-cruise/`; `/all-cruises/sip-sunset-valentines-wine-and-sights-cruise/`; `/all-cruises/fall-foliage-lunch-cruise/`; `/11-21-26-indiana-uw-sailgating/`; `/11-07-26-pennstate-uw-sailgating/`; `/10-09-26-iowa-hawkeyes-uw-sailgating/`; `/09-06-26-applecup-wsuvsuw-sailgating/`.
- Private Events: `/private-events/`; `/request-a-proposal/`; `/groups/`; `/special-occasions/`; `/fleet/` plus `/fleet/theemeraldstar/`, `/fleet/theolympicstar/`, `/fleet/thedestiny/`, `/fleet/the-sightseer/`; `/sightseer-cruises/`; `/vendor-partnerships/`; `/nonprofit-partner-program/` (application linked from that page, not required in the top nav).
- Plan Your Visit: `/directionsports/` plus `/directionsports/mohai/`, `/directionsports/carillon-point-marina/`, `/directionsports/kirkland-marina-park/`, `/directionsports/shilshole-bay-marina/`, `/directionsports/bell-harbor-marina/`, `/directionsports/waterwayshomeport/`; `/hotel-partners/`; `/faqs/`; `/gallery/`.
- About: `/about-us/`; `/careers/`; `/about-us/blog/`; `/memberships/` (secondary; only if [MEMBERSHIPS ACTIVE], otherwise a short retired notice at the same URL until the client picks a redirect); `/contact-us/`; `/privacy-policy/`.

Footer on every page: full text sitemap of every proto URL; [NAP CURRENT]; tel link; both emails; [HOURS] after confirm; D20 social links with no follower counts; Privacy; Journal; Careers; Gift Cards; Request a Proposal; Dining Cruises; rendered copyright year (a copyright year is not [SEASON YEAR]). No indexable search route. No FareHarbor lock-in.

### Page jobs (density bar: full official copy)

| Page | Path | Job |
|---|---|---|
| Home | `/` | Name the company, the lakes, and the two doors. Hero per section 4. Popular-cruise teasers (not full menus). Seasonal list without live availability. Private Events teaser. Six testimonials verbatim, no Product stars. Instagram embed. |
| Dining Cruises hub | `/dining-cruises/` | Self-serve front door. Full live hub copy. Links into full product pages. Strip SOLD OUT on the Sunday Supper teaser (B0299). |
| Premier Seattle Dinner Cruise | `/dining-cruises/dinner/` | Flagship plated date-night product. Times, ages 13+, Wed-Sat, summer and winter hours, both seasonal dinner menus verbatim, Steak & Lobster upgrade, enhancements after the core choice, departure as published, demo book widget. |
| Weekend Brunch Cruise | `/dining-cruises/weekend-brunch-cruise/` | All-ages brunch buffet. Complete brunch menu, times, departure, demo book widget. |
| Sunday Supper Cruise | `/dining-cruises/supper/` | All-ages supper buffet and complete menu. `/dining-cruises/sunday-supper-cruise/` already 301s here. |
| Taco Thursday | `/taco-thursday-seattle-lakes-cruise-tour/` | Midweek all-ages dining cruise. Full route copy and taco-bar menu. Departure as printed on that page (currently Dock 9); FAQ's MOHAI note for "Seattle Lakes Taco Bar" is [HOMEPORT PER CRUISE], not an overwrite. Demo book widget. |
| Lunch Cruises hub | `/lunch-cruises/` | Lunch index. Do not lead with a promo code (B0243). Strip SOLD OUT on the Valentine's lunch teaser (B0244). Child pages stay separate. |
| Cruise Calendar | `/cruise-calendar/` | Date-first self-serve entry. Provider-neutral demo calendar. No live sold-out cells. |
| Gift Cards | `/gift-cards/` | Demo gift purchase (provider-neutral). FAQ redemption answers stay on FAQs (not valid onboard; public cruises only). |
| Private Events | `/private-events/` | Charter front door. Full live sections; fleet links to four vessel pages; catering menus at 2026 PDF length; vendors; wedding packages after [CHARTER RATES]. Soften "Seattle's Premier Yachts" (B0149). Harvest unique `/corporate/` copy into a Corporate section. |
| Request a Proposal | `/request-a-proposal/` | Primary private conversion. Demo form only. Keep flyer download labels (2026 catering, 2026 upper deck/buyout, 2027 charter flyer as a document labeled 2027). |
| Groups and deck rentals | `/groups/` | Semi-private path plus group-ticket terms (10%, 65% deposit, 15% auto-gratuity, single payment, 14-business-day final count) as policy. Do not title the nav item "Group Discounts". Buyout CTA goes to Request a Proposal. |
| Special Occasions | `/special-occasions/` | Private celebration narrative at full length. Hold "up to 220 guests" as [SPECIAL OCCASIONS CAPACITY]. |
| Fleet hub | `/fleet/` | Vessel index with full descriptions and links to four detail pages. Destiny buffet uses [DESTINY BUFFET CAPACITY]; reception 40 ships. |
| Emerald Star | `/fleet/theemeraldstar/` | 105 ft vessel as a room. Full copy and official photos (rights pending). |
| Olympic Star | `/fleet/theolympicstar/` | 90 ft vessel as a room. Full copy. |
| Destiny | `/fleet/thedestiny/` | 64 ft intimate vessel. Buffet held; reception up to 40. |
| Sightseer | `/fleet/the-sightseer/` | Historic vessel. 48 seated; reception 100/60; no plated dining; MOHAI as published. |
| Sightseer Cruises | `/sightseer-cruises/` | Sightseer product / history page. Do not collapse into the fleet card. |
| Vendor Partnerships | `/vendor-partnerships/` | Full partner categories and blurbs. |
| Nonprofit Partner Program | `/nonprofit-partner-program/` | Full page. [LAKESIDE EVENT SPACE] held. Link to the application. |
| Nonprofit application | `/nonprofit-partner-program-application/` | Demo application, no send. |
| Memberships | `/memberships/` | Secondary loyalty at full length if [MEMBERSHIPS ACTIVE]; do not lead Home or nav with the $200 / $314.52 value stack. |
| About Us | `/about-us/` | Heritage, founders, team, affiliations at full length. [GUEST COUNT 60K] hidden until approved. Bios [HILTON / SHIRLEY BIOS]. |
| Careers | `/careers/` | Full job descriptions (Cruise Manager, Prep Cook, Captain, Server, Bartender) and demo application. Soften "Seattle's leading" / "only upscale" (B0178, B0179). Keep published duties and pay ranges. Apply-to addresses as published unless Confirm 23 changes them. |
| Contact Us | `/contact-us/` | NAP, map, demo contact form (no send). `/about-us/contact-us/` 301s here. |
| FAQs | `/faqs/` | All 46 questions at full length (56 inventory rows: H1 + 9 groups + 46 Q/A). Only B0049 (private-events typical homeport) is REWRITE; keep Sightseer / MOHAI facts. Accessibility answers that name both ports are USE. Gift-card, Groupon, and promo answers stay as redemption policy. |
| Privacy Policy | `/privacy-policy/` | The text the client names as current ([PRIVACY CANONICAL]); one H1. `/about-us/privacy-policy/` 301s here after confirm. |
| Gallery | `/gallery/` | Official gallery only; [PHOTO RIGHTS]; descriptive alt. No AI. |
| Directions and Ports hub | `/directionsports/` | Dock 9 directions and map plus links to every child port. `/departure-ports/` 301s here. |
| MOHAI | `/directionsports/mohai/` | Sightseer dock and parking. `/directions/mohai/` 301s here. |
| Carillon Point Marina | `/directionsports/carillon-point-marina/` | Full directions and map. |
| Kirkland Marina Park | `/directionsports/kirkland-marina-park/` | Full directions and map as published. |
| Shilshole Bay Marina | `/directionsports/shilshole-bay-marina/` | Full directions and map as published. |
| Bell Harbor Marina | `/directionsports/bell-harbor-marina/` | Full directions and map. |
| Lake Union Piers / Chandler's Cove | `/directionsports/waterwayshomeport/` | Full live copy for 901 Fairview / Lake Union Piers. Do not delete because other pages name Dock 9. |
| Hotel Partners | `/hotel-partners/` | Full published lists. Do not absorb `/silvercloud/`. Outbound links unverified. |
| Journal hub | `/about-us/blog/` | Sitemap canonical hub. List all 27 KEEP posts with title, a short excerpt from each post's own lead, and the full post URL. `/blog/` and pagination MERGE here. Individual `/blog/{slug}/` posts stay KEEP. |
| 404 | (system) | Branded recover links: Home, Dining Cruises, Private Events, Request a Proposal, Contact, FAQs. Genuine HTTP 404 or 410 for DROP URLs. |

Seasonal, holiday, and dated event pages (26 KEEP URLs listed in the nav above): each is a full product page with the official menu or includes list, times, ages, departure as printed on that page, and a demo book widget — except the four sailgating pages, which default to Request a Proposal until Confirm 20. Strip SOLD OUT, waitlist, and live-availability assertions. BEST SELLER badges may be omitted. Unique title and meta per page. Christmas Eve is live robots index,nofollow (Confirm 26); default the proto to index,follow like sibling holiday pages unless the client says otherwise. Do not use GettyImages-1066947368 on the NYE Party page unless [PHOTO RIGHTS] clears it.

Journal posts (27 KEEP URLs; full article each; do not shorten):
`/blog/2019-husky-sailgating-cruises/`, `/blog/2015-seattle-seafair-air-show-logboom/`, `/blog/weather-alert-cruise-cancellations/`, `/blog/thanksgiving-day-dinner-blog-2016/`, `/blog/waterways-celebrates-25th-anniversary/`, `/blog/winetastingcruiseblog/`, `/blog/what-should-i-wear-for-a-waterways-cruise/`, `/blog/10-unique-facts-you-might-not-have-known-about-seattle-washington/`, `/blog/sunday-supper-dining-cruise/`, `/blog/holiday-blog-2016/`, `/blog/seattle-holiday-parade-of-lights-cruises-blog/`, `/blog/fun-facts-you-might-not-have-known-about-tequila/`, `/blog/sailgating-the-waterways-way/`, `/blog/6-ways-to-cruise-through-the-holidays-with-waterways-cruises/`, `/blog/10-best-things-to-see-and-do-in-fremont-seattle/`, `/blog/see-seattle-from-a-different-perspective-with-a-waterways-dining-cruise/`, `/blog/weddings-with-waterways/`, `/blog/holiday-party-blog/`, `/blog/whats-the-difference-between-boarding-time-and-departure-time/`, `/blog/happyhourcruiseblog/`, `/blog/santa-lunch-cruises-blog/`, `/blog/seafair-2016-highlights/`, `/blog/seafair-on-a-yacht/`, `/blog/sailing-north-from-tahiti-to-seattle/`, `/blog/big-congratulations-class-of-2017/`, `/blog/the-great-experiment-we-celebrate-july-4th/`, `/blog/senior-cruises-senior-blog/`.

Refresh date, byline, and alt as needed. Do not ship Fremont `lake-union.jpg` at 3,943,949 bytes with empty alt. Do not use iStock-625902660 on the senior post unless [PHOTO RIGHTS] clears it. Old event recaps stay as articles; noindex or retire only after Confirm 25.

Recount: 8 dining cores + 13 private/fleet/vendor + 16 brand/visit + 1 memberships + 26 seasonal + 27 posts = 91.

### Product-page reading order
1. One text H1 using the live product name (do not shorten it).
2. Quick details as published: duration, meal style, ages, times, departure named on that page.
3. Full opening argument, verbatim.
4. Full menu or "cruise includes" list, verbatim, including dietary tags and "menu subject to change."
5. Enhancements already offered on that page, after the core choice.
6. Logistics: boarding vs departure (link the journal post and the FAQ), directions to the matching port page, accessibility to the FAQ answers that already name both ports.
7. Related cruises that already exist as links, without sold-out language.
8. Demo book widget (or Request a Proposal on sailgating until Confirm 20).
9. Closing band: Book this cruise (demo) plus Call on dining pages; Request a Proposal plus Call on private and fleet pages.

Fleet detail pages follow the same density rule: full vessel description, official photos, held capacities, link to Request a Proposal. A three-line card on Private Events is not a substitute.

---

## 7. Redirect and removal map

KEEP slugs stay put. Genuine aliases get 301s. Promo, draft, search, test, and leftover pages must not 301 into Home, About, or a generic dining hub.

Genuine 301s:
- `/about-us/contact-us/` → `/contact-us/`
- `/directions/mohai/` → `/directionsports/mohai/`
- `/about-us/privacy-policy/` → `/privacy-policy/` after [PRIVACY CANONICAL]
- `/departure-ports/` → `/directionsports/`
- `/corporate/` → `/private-events/` (harvest unique corporate copy first; hash optional)
- `/food-and-bar/dessert/` → fold into dining menus, especially `/dining-cruises/dinner/`. Do not overwrite a current menu. Add only missing 2020 items, labeled as from that page, or hold them (Confirm 34).
- `/blog/`, `/blog/page/2/`, `/blog/page/3/`, `/about-us/blog/page/2/`, `/about-us/blog/page/3/` → `/about-us/blog/`
- `/dining-cruises/sunday-supper-cruise/` → `/dining-cruises/supper/` (already 301s)
- `/fleet`, `/about-us`, bare host → `/fleet/`, `/about-us/`, `/`
- `/lunch-cruises-information/` → 410 preferred; 301 to `/lunch-cruises/` only if inbound links need a target

https://www. already 301s to the apex. http:// returned 500 from the audit box (Confirm 29); then 301 http to https. Leave robots disallows for `/edit/`, `/fhbr-console/`, `/cdn-cgi/`.

410 preferred or genuine HTTP 404 (never 200 soft-404; never "this page moved to Home"):
- Live promo landings: `/do206-offer/`, `/special-offers-and-promotions-for-public-cruises-hot-tub-boats/`, `/promotions-dining-cruises-concierge/`, `/unwind-concierge-ticket-entry/`
- `/silvercloud/` (placeholder "Free Breakfast: Test"). Do not 301 to `/hotel-partners/` unless Confirm 24 says Silver Cloud remains a partner
- `/search/Seattle` and `/search/`: noindex and remove the WebSite SearchAction target
- `/confirmation/` (REST-only booking utility): noindex
- Named 404s: `/corporate/corporate-event-packages-draft/`, `/corporate/corporate-enhancements-duplicate/`, `/special-occasions/party-enhancements-draft/`, `/wedding-enhancements-duplicate/`, `/winter-sale-google/`, `/winter-sale-soc/`, `/promotions-googlead/`, `/groupflyerpromotion/`, `/black-friday-private/`, `/dining-cruises/dinner-cruise-winter/`, `/unwind-cruise-series/`, `/all-cruises/sip-sunset-summer-wine-and-sights-cruise/`, `/lake-union-sightseeing-cruise/`, `/private-events/special-occasions/special-occasion-packages/`, `/food-and-bar`, `/corporate/corporate-packages/`, `/directions/fishermens-terminal/`

If Google `site:` later reveals more public URLs, classify each as a genuine alias (301) or orphan/promo/draft (410 or genuine 404) before launch. Do not default new URLs to a Home 301. That incompleteness is why this map cannot be signed off.

---

## 8. Content map

Block-level map: `references/content-inventory.md` (736 rows). Every USE block ships on the destination named there, at full wording, with heading levels cleaned to one H1 and a sane H2/H3 tree. Do not silently retag rows.

REWRITE on the proto (keep the section, change the risky part): B0061 home uniqueness; B0063-B0064 home sold-out/waitlist; B0149 Private Events ranking heading; B0178-B0179 Careers Captain uniqueness; B0243-B0244 lunch promo and sold-out teaser; B0280 Memberships discount-led lead (keep terms); B0299 dining-hub Sunday Supper sold-out; B0435, B0436, B0445, B0530, B0553, B0554 sailgating sold-out fragments; B0573, B0580, B0588, B0621, B0628, B0637, B0644 Mother's Day / Valentine's sold-out intros; B0661 Thanksgiving 2016 blog sold-out fragment; B0724 global sailgate banner (rotate to a current dated event); B0727 global Book Now (provider-neutral demo); B0049 FAQ private-events typical homeport.

DROP: inventory page-level DROP rows, footer FareHarbor credit (B0732), Product self-review markup, unverified 4.8 stars (D43), Visit Seattle capacity unless confirmed (D25), no-cost prototype-offer and meeting process (D01-D05, D08), AI imagery, confidential economics.

### Dossier lines (D01-D47)

| Lines | Decision |
|---|---|
| D01-D05, D08 | Internal only. DROP from client copy. |
| D06 | USE as the demo-only, provider-undecided constraint. |
| D07 | REWRITE: process timeline with [SEASON YEAR] unknown. 2027 is the flyer label only. |
| D09-D11 names/roles, D14 tagline (one form), D15 NAP, D17 contact, D18 route and sights, D19-D20 after confirm | USE |
| D11 bios | REWRITE pending [HILTON / SHIRLEY BIOS] |
| D12 | USE "four vessels". [GUEST COUNT 60K] held. Do not cite internal passenger figures. |
| D13 | REWRITE uniqueness. Do not write that Argosy sells (or does not sell) dinner cruises in client copy. |
| D16 | Per-cruise published ports USE; generic "our homeport is X" REWRITE after confirm. Not proof that Fairview is false. |
| D21-D24 | USE, with [DESTINY BUFFET CAPACITY] and Sightseer plated/MOHAI confirms. |
| D25 | DROP unless confirmed. |
| D26-D32 | USE two paths, RFP fields, products, enhancements. D26 response time [RFP RESPONSE TIME]. D31 past dates [PAST SEASONAL PAGES]. D32 prices after confirm. |
| D33 | USE group terms as policy; do not lead with discount. |
| D34 | Promo landings DROP from nav. Memberships secondary [MEMBERSHIPS ACTIVE]. |
| D35 | Gift cards as a demo, not a live FareHarbor embed. |
| D36 | KEEP URL; [LAKESIDE EVENT SPACE]. |
| D37 | USE FAQ policy facts at full length. |
| D38-D40 | USE audience map. |
| D41 | USE verbatim testimonials; DROP Product/aggregateRating. |
| D42 | USE as affiliation after confirm. |
| D43 | DROP unverified 4.8 and invented stars. |
| D44-D46 | Internal audit facts. Design for the confirmed live issues. Do not restate video CLS 0.61 or 66.1 MB as our measurements. D46's "stale FAQ homeport" is treated as inconsistent labels per D16. |
| D47 | Intermediary presence only. No lost-booking or rank claims. |

---

## 9. Official assets and provenance

- Logo: `https://waterwayscruises.com/wp-content/uploads/sites/3749/2025/02/Untitled-1000-x-1000-px-e1740170974160.png`. Colors and fonts extracted by Bob at the `brand.html` gate from the live site. Existing brand only.
- On-page images listed in `references/source-assets.md` (318 unique on-page URLs). Local copies may exist under `references/assets/`.
- WP media: unauthenticated REST header 1,884; public pagination exhausted at 1,011 unique items. Do not treat the library as complete (Confirm 27).
- Provenance Unknown until [PHOTO RIGHTS]. Do not caption images as "our photography" until cleared. Site hosting is not ownership.
- STOCK-named files (GettyImages-*, iStock*, shutterstock*, AdobeStock*, and commercial "stock" filenames) are DROP unless the client confirms license. Known KEEP-page hits: GettyImages-1066947368 on `/new-years-eve-party-cruise/`; iStock-625902660 on `/blog/senior-cruises-senior-blog/`.
- No AI imagery.
- Compress heavy originals. `lake-union.jpg` is 3,943,949 bytes with empty alt.
- Descriptive alt on every image (audit B6; recount 381/714 without usable alt on unique 200 pages).
- On-site PDFs in `references/files/`: 2026 Private Catering Menus (USE at full length on Private Events); 2026 Wedding Packages Flyer (Anchor / First Mate / Captain's after [CHARTER RATES]); 2027 Private Charter Flyer (document year 2027 only; starting-at rates after [CHARTER RATES]). Notes in `references/pdf-notes.md`.
- Maps, gallery, and Instagram embed: USE as functions if official and light. Calendar and gift-card purchase: provider-neutral demos, not live vendor widgets.

---

## 10. Visual direction (MARCO, sleek, mobile first)

Extract the live wordmark, type, and color at `brand.html` before other pages (house brand gate). Dark ink / slate / water rooms. Brand accent used sparingly as jewelry. Full-bleed official photo heroes. Generous vertical air. Refined type. Sentence-case headings where the live page shouts. Centered measures inside wide bands (wrap about 82%). 12-column, mobile-first. Breakpoints at 640 and 1024 only add columns. Below 640: single column, full-width buttons at least 44px tall, body at least 16px. Header about 60px sticky; bottom bar about 64px with safe-area padding. When content does not fill the width (a short paragraph, a form, two buttons), center it. No stacks of small rounded color cards with fat white gutters. Vessels read as named rooms. Menus read as restaurant menus, not icon grids.

Performance: compressed images, fixed dimensions, no leftover slider weight. Cite live lab numbers only as a baseline to beat (home Lighthouse 12 mobile performance 60, LCP 4.4 s, TBT 940 ms, CLS 0.052, 4,667 KiB; brunch performance 51, LCP 8.6 s, TBT 600 ms, CLS 0.054). Do not invent a proto score. Video CLS 0.61 and 66.1 MB are unverified third-party claims.

### Comps (fetched 2026-11-06; render each URL before using it). Adapt principles, not designs. Do not clone layouts, metrics, product names, photography, or type.

1. Argosy Cruises (https://www.argosycruises.com/ and the fetched private-charters page). Learn the ticket vs charter split. Do not copy sightseeing-tour voice. Do not write that Argosy sells dinner cruises; do not use Argosy to prove Waterways is "the only" dining cruise company.
2. City Cruises Boston (https://www.cityexperiences.com/boston/city-cruises/). Learn Groups & Private Events kept separate from BOOK NOW, visible FAQ, gift cards as a utility. Do not copy discount banners or cart-first clutter.
3. Canlis (https://canlis.com/ and https://canlis.com/private-events/). Learn restrained nav, heritage voice, private rooms as named spaces (maps to vessels). Do not copy its type, color, grid, or brand.
4. Kenmore Air (https://kenmoreair.com/). Learn editorial guides for discovery. Keep and refresh existing journal guides (what to wear; boarding vs departure; see Seattle from the water). Do not invent new guides. Do not copy airline-scale nav.

seattleboat.tours is evidence of intermediary Q&A, not a visual brand to resemble. Do not copy affiliate framing or claim intercepted bookings. City Experiences Chicago/London dining URLs returned 404 and are out of scope.

---

## 11. Verified facts vs holds

Ship from live official copy after the REWRITE rules above: since 1994 and April start; four named vessels and their non-conflicting descriptions; core and seasonal product details as published on each page; route language; footer NAP pending [NAP CURRENT]; phone and both emails; 46 FAQ answers except B0049's typical-homeport clause; testimonials as attributed; social profile URLs without counts.

Placeholders (hide the whole block at launch if still unanswered; never print a guess):
[SEASON YEAR], [HOMEPORT PER CRUISE], [DESTINY BUFFET CAPACITY], [GUEST COUNT 60K], [UNIQUENESS CLAIM], [TAGLINE FORM], [RFP RESPONSE TIME], [LAKESIDE EVENT SPACE], [MEMBERSHIPS ACTIVE], [PRIVACY CANONICAL], [GBP URL], [HOURS], [BOOKING PROVIDER], [PHOTO RIGHTS], [CHARTER RATES], [SPECIAL OCCASIONS CAPACITY], [HILTON / SHIRLEY BIOS], [AFFILIATIONS], [PAST SEASONAL PAGES], [FORM DESTINATION], [NAP CURRENT], [HOTEL PARTNERS].

Numbered client confirms are in `marketing-plan.md` section 14 (items 1-38). Use those numbers (growth-review C6). Additional standing holds: confidential economics; draft 4.0 non-comparison; video metrics as third-party claims only; Google discovery not complete.

Held off the proto without confirmation (section 15 of the plan, restated): the meeting's season year; any use of 2027 except as the charter flyer's document title; ranking phrases; 60,000 guests; Destiny buffet 25 vs 30 (do not pick); Special Occasions 220 and Visit Seattle 130/220; flyer dollars until approved; memberships as current if the 2025 Unwind season is over; Lakeside Event Space and the 40% fee until approved; a single global homeport overwrite; Product self-review stars and the unverified 4.8; follower counts; ownership captions on uncleared or stock-named files; AI images; FareHarbor named as the chosen future provider; confidential economics; any comparison to draft 4.0; any statement that Google discovery is complete.

---

## 12. SEO / AEO the pages should be designed for (not a proto score)

Live baseline: 38/64 (A 10/16, B 8/16, C 9/12, D 9/16, E 2/4). Confirmed current issues include duplicate contact and MOHAI URLs, an indexable `/search/` route, Product self-review schema, mixed LocalBusiness address, breadcrumb-only cruise schema, inconsistent homeport labels, heavy originals, empty or missing alt at scale, and shared sailgating meta. Design to fix what static HTML can carry.

- One text H1 per page; unique title and meta per page. Home stops using the logo as the only H1. Privacy drops from 3 H1s to 1.
- Organization / LocalBusiness JSON-LD with @id, full homeport PostalAddress once [HOMEPORT PER CRUISE] and [NAP CURRENT] agree, separate office ContactPoint at 4005 20th Ave W Suite 228, 98199, telephone in +1 format, and [HOURS]. Remove Product self-review. Add Event or TouristTrip plus Offer per cruise at launch. Person schema for named founders after bios are confirmed.
- FAQPage on `/faqs/` using the visible 46 answers (rewrite B0049 for accuracy).
- Article JSON-LD on journal posts with ISO dates and publisher (add at launch if needed).
- Self-canonicals; clean XML sitemap of real proto URLs only (`/gift-cards/` once). noindex search and remove SearchAction.
- OG image and description on every page, including the eight now missing them.
- `lang="en-US"` may stay. Do not add AI-crawler blocks (audit A8 = 2).
- Label robots/sitemap/JSON-LD that are launch-only as "Designed for go-live, add at launch" when they are absent from static HTML.

Never mark launch-only items Pass. Never score unbuilt features.

---

## 13. Four-report plan (after KEEP proto pages exist)

House standard (NC Utility tooling, restyled to Waterways tokens from `brand.html`). DPA Branding is the only attribution. Details: `references/seo-aeo-report-plan.md`. Seeded live facts: `references/seo-aeo-compare-facts.md` (F01-F20). Expand the ledger as pages ship. The PROTO column stays "Pending build" until pages exist.

1. `Waterways-SEO-AEO-Compare.html` — live vs proto rows from the facts ledger. Filters: Side-by-side / Live / Proto, SEO / AEO. Expandable "why it matters." Links to the three reports.
2. `Waterways-SEO-Summary.html` — one page for Hilton; plain-language top 5. No traffic or ranking promises.
3. `Waterways-SEO-InDepth.html` — technical, on-page, local/NAP (homeport vs office, multi-port departures), schema, AEO (date-night/family answers), IA (two paths), assets, plus "Supplied audit claims: verified / stale / unverified" from `audit-claim-verification.md`.
4. `Waterways-SEO-Gap-Report.html` — live gaps, what the proto fixes, "Designed for go-live, add at launch."
5. `seo-aeo-compare-facts.md` at the repo root, **not served** (must 404 on the site).

Proto banner: link Compare next to Performance. Presentation / deck SEO and AEO slides: link the same Compare file as the deep dive. Randy builds the reports after pages exist and re-scores after each Bob fix round. Verification: headless Chrome at 390/768/1280, zero console errors, report URLs 200, facts ledger 404.

Do not include confidential economics, invented metrics, provider selection, or real booking in the reports.

---

## 14. Build order (after sign-off only)

1. `brand.html` plus CSS tokens (blocking brand gate).
2. Global chrome: two-path header, footer sitemap, demo states.
3. Home, Dining Cruises hub, Dinner / Brunch / Supper, Private Events, Request a Proposal, Fleet plus four vessels.
4. Remaining dining, seasonal, directions, FAQ, About, Careers, Contact, Privacy, Gallery, Hotel Partners, Groups, Special Occasions, Vendors, Nonprofit pair, Memberships, Gift Cards, Calendar.
5. 27 journal posts at full length.
6. 301/410 map and branded 404.
7. Wire SEO/AEO Compare into the banner beside Performance, and from the Presentation SEO/AEO slides, once Randy ships those files.

---

## 15. Constraints (absolute)

- No real bookings, payments, or form sends.
- No live FareHarbor (or other vendor) default.
- No client, Don, or DPA email from this workstream unless Mike says so.
- No OS client or task creates.
- No production changes.
- No AI imagery.
- No confidential economics in any client-facing file.
- No comparison to the unseen draft 4.0 redesign.
- No claim that Google discovery is complete.
- No proto SEO score until pages exist.
- Existing brand and official imagery only.

This brief is a draft. It is not Research sign-off and not authorization to build.
