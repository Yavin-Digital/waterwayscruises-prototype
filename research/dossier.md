# Waterways Cruises & Events: sourced research dossier (Randy)

Status: DRAFT for Growth, not signed off.
- The research gate is OPEN because Google site: discovery is blocked (section 2), with no exception granted.
- The video findings were analyzed externally by JohnWick. We did not watch the video. Its timestamps are cited only as audit claims.

Agency attribution in client-facing material: DPA Branding only.

Confidential economics live only in ../INTERNAL-CONFIDENTIAL-economics.md and must stay out of any client packet.

Source keys are listed in source-register.md:
- S1 = live site crawl 2026-11-06
- S2 = transcript txt
- S3 = Calendly recap in Don's email
- S4 = audit PDF
- S5 = Bob transcript (Mike request)
- S6 = third-party pages

## 1. Request and constraints (verified)
- D01. Mike asked for the build in Bob's chat on Nov 6, 2026. He said "Great. Can we build the prototype?" and then "Make sure it is sleek". This followed his pasting of Don's email (S5, positions about 10274-10278). Map: USE (internal brief).
- D02. Don Pelham (DPA Branding) emailed Mike on Nov 5, 2026 at 1:55 PM CT with the transcript, the audit video and the PDF. He wants to use the transcript for a prototype "he has agreed to take a look at" (S3). Map: USE (internal).
- D03. The meeting was the GDS 30 Minute Meeting on Tue Nov 3, 2026, 12:00-12:30 CST. Attendees: Don Pelham, Hilton Smith (owner) and Matthew Bishop (audit) (S3). Map: USE (internal).
- D04. The prototype is offered at no cost, for comparison with the client's existing redesign. No provider change, commercial agreement, pricing or follow-up meeting was finalized (S3). Map: USE (internal constraint). DROP from client copy.
- D05. The client's own new site is "probably draft 4.0" (S2 00:22:00). It will not use WordPress, and it is managed by their marketing team and existing web specialists (S3). We have not seen it, and it is not a Yavin/DPA artifact. Map: USE (internal). Do not reference its design.
- D06. The booking engine is unresolved. They are evaluating staying with FareHarbor plus "two options" (S2 00:02:24). Map: USE. The prototype checkout is DEMO ONLY, provider-neutral, and takes no real bookings.
- D07. Timeline: "January through the end of February... season starts in May... pre-sell starting in March" (S2 00:50:05). The YEAR is NOT stated. The on-site PDF `2027-Private-Charter-Flyer.pdf` is labeled "2027 private charter rates". That proves the document’s own year label only. It does not state, and cannot be used as, the meeting’s target season year. Map: REWRITE as "ahead of next season [year: client confirmation needed]". Never write "2027" as the meeting’s launch year.
- D08. Gate: Google discovery must complete before sign-off. There is NO exception, and the Orion exception does not apply.

## 2. Discovery status (see url-index.md)
- 131 crawled/checked URLs plus 1 REST-only page: KEEP 91, MERGE 15, DROP 26 including /confirmation/. Verified against references/url-index.md.
- Today's sitemap has 102 entries (101 unique). WP REST: 46 pages, 27 posts, 29 activity (sitemap).
- WP media: unauthenticated REST reports X-WP-Total 1,884 and X-WP-TotalPages 19. Paginating pages 1-19 (per_page=100) returned 1,011 unique public items (page sizes 15-89, never 100). Page 20 returns 400 rest_post_invalid_page_number. The 1,011 set matches the earlier dump exactly (overlap 1,011). Public pagination is exhausted. The remaining 873 counted in the header are not returned to an unauthenticated request (WordPress filters items after the per-page query). No browser or authenticated route was used. Coverage: 1,011/1,884 public listable items (53.7% of the header total). Do not treat the media library as fully downloaded.
- BLOCKER, Google site:waterwayscruises.com: google.com/search from the box returns a JS-required shell ("enablejs"), and WebSearch returned "No results". This is NOT complete. There is no Waterways exception. The Orion exception does not apply. No retries or evasion.
- DuckDuckGo's site: supplement found 16 URLs. One was new and 404s (/seattle-holiday-parade-of-lights-cruises-blog/), plus 3 PDFs (now downloaded and read; see pdf-notes.md).
- Needed: someone with a normal browser runs Google site: to exhaustion, or Mike grants an explicit Waterways-specific exception.

## 3. Company facts (public, S1)
- D09. Brand name: "Waterways Cruises & Events". Schema and some titles say "Waterways Cruises and Events". Map: USE "Waterways Cruises & Events".
- D10. "Part of Seattle's lake and Puget Sound scene since 1994". It started with one yacht in April 1994 (About). Map: USE.
- D11. Co-founders Shirley Turnbow and Hilton Smith. Hilton Smith is CEO, with a background in real estate and finance and education at Princeton and Stanford (About). Map: USE names and roles. REWRITE the bio [CONFIRM current].
- D12. Fleet of four vessels, "hosting over 60,000 guests a year" (About). Map: keep "four vessels" (USE). The 60,000-guest line is client-published on the About page and should be used only with confirmation (REWRITE the number if it ships without a check). A privately stated individual-passenger figure lives only in ../INTERNAL-CONFIDENTIAL-economics.md; that is a different population from public guests and is not automatically contradictory. Do not put confidential economics in the client-facing dossier, proto, or reports.
- D13. Homepage: "the city's only dining cruise company" (S1 home). Map: REWRITE. This is an unsourced uniqueness claim and should be softened or sourced [CONFIRM]. Comp check (S7, 2026-11-06): the fetched Argosy homepage and private-charters page do not list a dinner-cruise or dining-cruise product. Observed Argosy public products are sightseeing (Harbor, Locks, Sunset, Happy Hour), Christmas Ship, NYE, Husky Sailgating, and Private Charters. seattleboat.tours’ dinner-cruise guide claims Seattle has one dedicated plated dinner cruise and attributes it to Waterways; that is an intermediary claim, not our measurement, and is not used as proof. Do not write that Argosy sells dinner cruises.
- D14. Tagline: "For an Unforgettable Event...Just Add Water."(R) and "For An Unforgettable Experience, Just Add Water(R)" (S1). Map: USE one form [CONFIRM which].
- D15. Based at Fishermen's Terminal. Homeport is Dock 9, 3919 18th Ave W, Seattle WA 98119. The office (by appointment) and mailing address is 4005 20th Ave W Suite 228, Seattle WA 98199 (footer). Map: USE.
- D16. Location labels are not uniform, and a mismatch is a risk rather than proof that one label is false. The footer and the public-dining FAQ name Fishermen’s Terminal Dock 9, 3919 18th Ave W, Seattle WA 98119 as the primary public homeport. The private-events FAQ says the typical homeport is 901 Fairview Ave N in South Lake Union. `/directionsports/waterwayshomeport/` describes Lake Union Piers at that address. Several seasonal product pages (Easter, Valentine’s, fall foliage) still publish that pier as their departure. Accessibility FAQ answers already describe boarding at both ports. Printed PDFs use 901 Fairview (wedding flyer, Suite A-100) and, on the 2027 charter flyer, a header at 901 Fairview plus a footer at 3919 19th Ave W 98119 (the site footer uses 18th Ave W). Map: USE the departure port named on each cruise; REWRITE only generic “our homeport is X” copy after [CONFIRM current ports per cruise and charter]. Do not drop logistics or accessibility answers because they mention Fairview.
- D17. Phone (206) 223-2060. Emails: contact@waterwayscruises.com, events@waterwayscruises.com. Office response Mon-Fri 9:30 am-4:00 pm (FAQ). Map: USE.
- D18. Route: Lake Union and Lake Washington ("subject to boat traffic and weather"). Sights: Space Needle, floating homes, historic bridges, skyline, seaplanes (product pages). Map: USE.
- D19. Affiliations: Passenger Vessel Association GREEN WATERS participant (About) and Visit Seattle member (S6). Map: USE [CONFIRM current].
- D20. Social: Facebook /waterwayscruises, Instagram @waterwayscruises, TikTok @waterwayscruises, TripAdvisor d1130187, Yelp waterways-cruises-seattle. Map: USE links. Activity and follower counts were not checked, so make no claims about them.

## 4. Fleet (S1 /fleet/)
- D21. Emerald Star: 105 ft, two interior salons, two open-air decks, two granite-topped bars. Map: USE.
- D22. Olympic Star: 90 ft, two dining salons, a deluxe bar upstairs, an outdoor deck and a built-in buffet. Map: USE.
- D23. Destiny: 64 ft, up to 30 guests for a buffet and 40 for a reception (site fleet copy). The 2027 charter flyer says up to 25 guests for buffet dining and 40 for a reception. Map: USE the vessel and reception figure; [CONFIRM] current buffet capacity (25 vs 30).
- D24. Sightseer: 70 ft (meta). 100 guests for a reception in warmer months, 60 in colder months, 48 seated; no plated dining. It departs MOHAI (FAQ). Map: USE.
- D25. Visit Seattle lists max seated 130 and max reception 220 (S6). These are third-party figures. Map: DROP unless the client confirms.

## 5. Two products (S2, S3: the key strategic requirement)
- D26. Private whole-boat charters and events are relationship-led and quote-based. Today they run through the Request a Proposal form, which promises a reply "within 1-2 business days" (RFP page) or 24-48 hours (FAQ). Map: USE the separate inquiry path. REWRITE to reconcile the response time [CONFIRM].
- D27. The RFP fields are: event type (Corporate, Wedding, Rehearsal Dinner, School, Special Occasion, Memorial, Other), contact details, date, guest count, time window (afternoon back by 3:00 PM; evening boarding from 5:30 PM) and budget. Map: USE these as the demo form fields. No submission.
- D28. Semi-private options: upper deck rentals and public buyouts (FAQ, /groups/). Map: USE inside the private path.
- D29. Individual dining cruises are booked self-serve. The client's stated self-serve flow is cruise type, then date, then party (2-10 typical), then optional enhancements after the core choice (S2, S3). Map: USE as the demo checkout sequence.
- D30. Current core dining products:
  - Premier Seattle Dinner Cruise: 2.5 h, plated, ages 13+, Wed-Sat; summer 7:00-9:30 pm from May 1, winter 6:00-8:30 pm from Oct 1.
  - Weekend Brunch Cruise: 2 h, buffet, all ages.
  - Sunday Supper Cruise: 2 h, buffet, all ages; select Sundays.
  - Taco Thursday: 2 h.
  - Map: USE.
- D31. Seasonal and event cruises: Thanksgiving (Nov 26), Parade of Lights (Holiday Dinner, Holiday Sights), Christmas Eve Dinner (Dec 24), NYE Dinner (Dec 31, 9:30 pm-12:30 am, 16+), NYE Party (21+), Willamette Valley Wine Pairing (Mar 4), Husky sailgating (11/21 Indiana; 11/07 Penn State SOLD OUT), plus Seafair, Mother's Day, Easter, Valentine's, Father's Day and July 4 pages. Map: USE current dates. Past dates: REWRITE as evergreen "annual" pages or retire [CONFIRM].
- D32. Add-ons already exist in copy, for example "Rose petals and chocolate-covered strawberries... select the Add-On checkbox" and "guaranteed window table" upgrades. The Dinner page offers a Steak & Lobster entree upgrade. Map: USE as the enhancement step examples. Prices only from live pages [CONFIRM current].
- D33. Group tickets: 10+ save 10%, 65% deposit, 15% auto-gratuity, single payment, final count due 14 business days before (/groups/). Map: REWRITE. Keep the facts in the policy section but do not lead with discounts.
- D34. Discount-led pages: memberships (5 Unwind Cruises for $200, "$314.52 value"), partner promo pages (Do206, Curiocity, concierge), and "special offers". Map: REWRITE or DROP. The requirement is premium, not discount-first (S2/S3). Memberships stay as a secondary loyalty item [CONFIRM active].
- D35. Gift cards are sold via a FareHarbor item (412031). Map: USE as a demo link only.
- D36. Nonprofit Partner Program: 40% off the hourly fee at "Lakeside Event Space", plus Nonprofit of the Month. The relationship between Lakeside Event Space and Waterways is UNKNOWN. Map: REWRITE [CONFIRM the venue exists and is current]. The URL is KEEP.
- D37. Policies (FAQ): cake-cutting $2/person ($3 wedding/tiered), gratuity 20%+ recommended on charters, a decor rules list, accessibility boarding notes, entree selections final 2 business days prior. Map: USE.

## 6. Audiences (S2, S3, S1)
- D38. Private: corporate events, weddings and rehearsal dinners, celebrations, school events, memorials. Map: USE.
- D39. Dining: couples and date nights ("Best Romantic Dining" title), families (all-ages buffets), visitors (Hotel Partners page), and locals marking milestones. Map: USE. The discovery gap is broad "date night" and "family activity" searches (S3).
- D40. Sports fans (UW sailgating) and seasonal celebrants. Map: USE.

## 7. Proof (S1)
- D41. The homepage carries 6 testimonials (Gabriel, Marina, Amanda P. "Yelp", and others), and Private Events carries event testimonials. The origin of each is unknown apart from those labeled. Map: USE the verbatim text with attribution as shown, but DROP the Product/aggregateRating markup.
- D42. Visit Seattle listing (S6). Map: USE as an affiliation [CONFIRM].
- D43. No review counts or star ratings may be shown unless they come from a live, citable profile at build time. The third-party "4.8" mentioned by Don in the transcript is not verified. Map: DROP.

## 8. Site audit summary (S1; see ../SEO-AEO-Audit.md and audit-claim-verification.md)
- D44. The live score is 38/64 on the house rubric. Map: USE (internal; client version via DPA).
- D45. The supplied audit's draft/duplicate pages now return 404. The sitemap shrank from the 117 claimed to 102 entries. Map: USE as a "stale since Nov 3" note. Do not claim these issues are current.
- D46. Confirmed current issues: identical duplicate contact and MOHAI URLs; an indexable /search/ route; Product self-review schema; mixed LocalBusiness address; breadcrumb-only cruise schema; stale FAQ homeport; heavy originals (Fremont lake-union.jpg is 3.94 MB, empty alt); 360/680 imgs with no or empty alt; shared sailgating meta. Map: USE.

## 9. Third-party visibility (S6)
- D47. seattleboat.tours runs a Seattle boat-tour comparison and dinner-cruise guide pages that feature Waterways and link to a GetYourGuide affiliate listing. Map: USE as evidence of intermediary presence. Make NO claim about lost bookings or rank.

## 10. Comps (fetched 2026-11-06; raw/comps/)
| # | Comp | Pages fetched | Observed pattern | Resemble | Do not copy |
|---|---|---|---|---|---|
| C1 | Argosy Cruises (Seattle, direct) | https://www.argosycruises.com/ | H1 "Experience Seattle from the water"; nav splits "Buy Tickets" vs "Private Charters / Request a Quote"; Group Tickets; Organization + WebSite JSON-LD | Clear ticket vs charter split | Volume sightseeing tone, tour-first positioning |
| C2 | City Cruises Boston (national dining operator) | https://www.cityexperiences.com/boston/city-cruises/ | "Groups & Private Events" separate from BOOK NOW; Manage Booking; FAQ + testimonials; Gift Cards | Booking management, FAQ block | Discount banners, cart-first clutter |
| C3 | Canlis (Seattle fine dining, adjacent premium hospitality) | https://canlis.com/ and https://canlis.com/private-events/ | Restrained nav (Reserve / Gift Cards / Private Events); heritage line "family-owned fine dining, since 1950"; private rooms as named spaces | Premium restraint, heritage voice, private spaces as rooms (maps to vessels) | Its type and brand |
| C4 | Kenmore Air (Seattle experiences, adjacent) | https://kenmoreair.com/ | "Book Flights" primary; travel-guide editorial for discovery; Organization JSON-LD | Editorial guides for broad discovery (date-night/family content) | Airline-scale nav |
| E1 | seattleboat.tours (intermediary, evidence only) | https://seattleboat.tours/ + 2 guide URLs | FAQPage/ItemList/Offer schema; answers "Is there a dinner cruise in Seattle?" | Answer-first FAQ structure, on our own site | Affiliate framing |
Argosy dinner-cruise claim: not supported by the fetched Argosy pages (see D13). Do not use Argosy as a dining-cruise contradiction.
Not reachable: City Experiences Chicago/London dining URLs returned 404 and were not used.

## 11. Design direction (MARCO, sleek per Mike)
- Existing brand only. The logo is at https://waterwayscruises.com/wp-content/uploads/sites/3749/2025/02/Untitled-1000-x-1000-px-e1740170974160.png. Colors and fonts are to be extracted by Bob at the brand.html gate.
- Use real official photography only, with no AI imagery. Stock-named files are flagged in source-assets.md.
- Full-bleed photo hero; dark "ink/slate/water" rooms with the accent used sparingly as jewelry; generous air; refined type; mobile-first 12-column; centered measures.
- Phone: the first screen has the two-path choice (Dining Cruises / Private Charters), each with one CTA.

## 12. Content map overrides (see the reviewed content-inventory.md)
- Homepage "city's only dining cruise company": REWRITE the uniqueness clause; keep the rest of the hero.
- Registered tagline "For An Unforgettable Experience, Just Add Water®": USE.
- FAQ Q/A are split (46 questions). Policies, booking, accessibility, logistics, gift-card redemption, charter inquiry, and office answers are USE at full length. The private-events “typical homeport is 901 Fairview” answer is REWRITE (consistency risk; confirm). Accessibility answers that name both ports are USE.
- Cruise product pages that publish Lake Union Piers / 901 Fairview as their own departure: USE as that cruise’s port [CONFIRM], not a global overwrite.
- "SOLD OUT" / waitlist: REWRITE to remove live availability from the demo; keep the product.
- "BEST SELLER" badges may be omitted as optional chrome; do not rewrite the product paragraph for that badge alone.
- Menus (dinner, brunch, supper, holiday) and the 2026 catering PDF: USE verbatim.
- Careers job descriptions and the application form: USE on Careers.
- Gift-card embed, cruise calendar, maps, Instagram embed, RFP/contact/careers/nonprofit forms: USE as functions (demo only for checkout/submit).
- Hotel Partners list: USE [outbound links unverified].
- Confidential economics: never appear in this dossier as client-facing proof.

## 13. Dossier claim map summary
Claims D01-D47 (47), amended 2026-11-06 for D07 (PDF year ≠ meeting year), D12 (60k is not an automatic contradiction), D13 (Argosy dinner-cruise claim removed), and D16 (location risk, not stale proof). Primary tags still sit on those 47 rows: most are USE; D07/D12-number/D13 uniqueness/D26 response-time/D33-D34 are REWRITE in whole or part; D04 (no-cost prototype offer), D25 (Visit Seattle capacity), and D43 (unverified 4.8) stay DROP from client copy. D08 is the open Google site: gate (n/a as copy). Internal-only (not client copy): D01-D05, D08, and anything in INTERNAL-CONFIDENTIAL-economics.md.

## 14. Open confirmations (client via Don/Mike; Randy does not contact)
1. Target season year.
2. Current homeport(s) per cruise.
3. The 60,000 guests and "only dining cruise company" claims.
4. Tagline form.
5. Lakeside Event Space.
6. RFP response time.
7. Photo rights (all), especially stock-named files.
8. Active memberships and promos.
9. Which privacy page is current.
10. Google Business Profile URL.
11. Hours for schema.
12. Booking-provider decision (stays open; demo only).
