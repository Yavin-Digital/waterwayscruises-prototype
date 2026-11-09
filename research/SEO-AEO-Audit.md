# Waterways Cruises & Events: live-site SEO/AEO audit (house 32-check rubric)

Internal working audit. Client-facing attribution: DPA Branding only.
Live site: https://waterwayscruises.com/ (WordPress VIP, FareHarbor booking embeds).

Evidence was captured 2026-11-06 around 4:50 to 5:00 PM CT. It is in references/raw/: crawl.json, html/, sitemaps, wp-json dumps, lh-home.json, lh-brunch.json, cls-lab.json.

Scores measure checklist readiness only. They say nothing about rankings, traffic, search volume or bookings. The claims from the supplied third-party audit are tested separately in references/audit-claim-verification.md.

Rubric: the same 32-check house rubric used on LEAD Foundation, Tribes Church and Salt and Light. Each check scores 0, 1 or 2. For this business, C5 reads as departures/directions, and E2 as trust signals (since-1994 claim, PVA Green Waters, reviews, privacy).

## Score

Live: 38 / 64 (59%)

| Area | Score | Max |
|---|---|---|
| A. Crawl and indexability | 10 | 16 |
| B. On-page | 8 | 16 |
| C. Local | 9 | 12 |
| D. Schema and AEO | 9 | 16 |
| E. Performance and trust | 2 | 4 |
| Total | 38 | 64 |

## A. Crawl and indexability (10/16)

| # | Check | Score | Evidence |
|---|---|---|---|
| A1 | HTTPS and single host | 1 | https://www. 301s to the apex. http:// returned 500 (Pingora) from the box, which may be an egress artifact; recheck. |
| A2 | robots.txt allows crawl + sitemap | 2 | Disallows only /edit/, /fhbr-console/ and /cdn-cgi/, plus a named bad-bot list (incl. Yandex, Baidu, SeznamBot). The sitemap is declared. |
| A3 | XML sitemap clean | 1 | Index with 3 children: 102 entries / 101 unique (/gift-cards/ is in both page and activity). Draft/duplicate routes were removed after Nov 3. Still listed: 2015-2017 posts, past-date events (Valentine's, Easter, Mother's Day 2026), discount/partner landings, and both privacy pages. |
| A4 | Canonicals correct | 1 | Self-canonical everywhere, but duplicates each self-canonicalize: /contact-us/ = /about-us/contact-us/; /directions/mohai/ = /directionsports/mohai/; /blog/ vs /about-us/blog/; 2 privacy pages; /search/{term}. |
| A5 | No thin/empty indexable pages | 1 | Several pages are near the chrome-only word count (about 460 words including nav/footer): /gift-cards/, /gallery/, /lunch-cruises-information/, /unwind-concierge-ticket-entry/. |
| A6 | Descriptive slugs | 1 | Good: /dining-cruises/dinner/. Weak: /directionsports/, /fleet/theolympicstar/, /11-21-26-indiana-uw-sailgating/, /silvercloud/, /special-offers-and-promotions-for-public-cruises-hot-tub-boats/. |
| A7 | No broken links | 1 | 8 internal links resolve to 404 (see audit-claim-verification, additional findings). |
| A8 | AI crawler access | 2 | No GPTBot/ClaudeBot/PerplexityBot/Google-Extended blocks. |

## B. On-page (8/16)

| # | Check | Score | Evidence |
|---|---|---|---|
| B1 | Unique titles | 1 | 9 duplicate-title clusters, mostly from duplicate URLs and the blog pagination. |
| B2 | Titles carry what + where | 1 | Strong: "Seattle Dinner Cruise - Best Romantic Dining". Many are "X / Waterways Cruises" with no Seattle (Gift Cards, FAQ, Fleet, Memberships). |
| B3 | Meta descriptions | 1 | Present on every 200 page, but there are 10 duplicate clusters, including 4 sailgating pages sharing one. |
| B4 | One clear H1 | 1 | The homepage H1 is the logo image (alt "Waterways Cruises and Events"). /about-us/privacy-policy/ has 0; /privacy-policy/ has 3. Most others have 1. |
| B5 | Heading hierarchy | 1 | Section headings exist, but many are empty labels with no body text ("Meet Our Fleet", "Catering Menus", "Link Gallery"). |
| B6 | Image alt | 0 | 360 of 680 img tags have empty (251) or missing (109) alt. |
| B7 | Internal linking | 1 | The mega-menu reaches products. Body cross-links to 404s exist, and the FAQ points to /departure-ports/, which overlaps /directionsports/. |
| B8 | Content depth | 2 | Dinner page 1,301 words with full seasonal menus; FAQ 4,781 words; Careers 3,137; Hotel Partners 2,042. |

## C. Local (9/12)

| # | Check | Score | Evidence |
|---|---|---|---|
| C1 | NAP on every page | 2 | Footer: (206) 223-2060, contact@, homeport Dock 9 3919 18th Ave W 98119, office 4005 20th Ave W Ste 228 98199. |
| C2 | NAP consistent | 1 | The FAQ still says homeport 901 Fairview Ave N. Visit Seattle lists 4005 20th Ave W with ZIP 98119 vs 98199 on site. Schema mixes dock + office ZIP. |
| C3 | Google Business Profile with reviews | 0 | Not verified. The footer links a Google search, not a profile. Google discovery is blocked (see url-index). Unknown, not absent. |
| C4 | Tap-to-call | 2 | tel:2062232060 is in the footer. |
| C5 | Departures / directions path | 2 | Dedicated pages per port: Fishermen's Terminal, MOHAI, Carillon Point, Kirkland Marina Park, Shilshole, Bell Harbor, Chandler's Cove (legacy), with Google Maps links. |
| C6 | Service-area content | 2 | Lake Union / Lake Washington routes and Seattle sights are named across the product pages. |

## D. Schema and AEO (9/16)

| # | Check | Score | Evidence |
|---|---|---|---|
| D1 | Organization / LocalBusiness | 1 | Present but flawed: " Dock 9" street, office ZIP, no @id on LocalBusiness, empty hours, telephone without +1. |
| D2 | Person schema for leaders | 0 | None. Co-founders are named in About text only. |
| D3 | FAQ content + FAQPage | 2 | /faqs/ has FAQPage JSON-LD and long answers. Accuracy issues are scored under D6. |
| D4 | Article / Event / Product for offers | 1 | Posts have Article (non-ISO datePublished, Organization author, no publisher). Cruise and event pages have BreadcrumbList only: no Event/TouristTrip/Offer. The homepage misuses Product for self-reviews. |
| D5 | Entity clarity | 1 | Homepage copy states who/where/what ("the city's only dining cruise company", Fishermen's Terminal, Lake Union / Lake Washington). The H1 is a logo, and there is no mainEntity. |
| D6 | Freshness | 1 | Events are current through Dec 2026 and the Mar 4 wine cruise. Stale: FAQ homeport, 2015-2017 posts, past events still in the sitemap. |
| D7 | Language | 2 | lang="en-US". |
| D8 | Social / Open Graph | 1 | og:image is missing on 8 pages. |

## E. Performance and trust (2/4)

| # | Check | Score | Evidence |
|---|---|---|---|
| E1 | Mobile performance | 1 | Lighthouse 12 mobile (local, simulated throttle, single run each): home perf 60, LCP 4.4 s, TBT 940 ms, CLS 0.052, 4,667 KiB; brunch perf 51, LCP 8.6 s, TBT 600 ms, CLS 0.054. These are lab numbers, not CrUX field data. |
| E2 | Trust signals | 1 | Present: since 1994 and co-founders named, PVA Green Waters, Visit Seattle membership, TripAdvisor/Yelp links, privacy policy. Weakened by Product self-review stars and the duplicate privacy pages. |

## Prioritized gaps (prototype should design for these; launch items labeled "add at launch")

High
1. Two buyer paths are not separated at the entry point: private whole-boat charter (Request a Proposal) vs individual dining tickets (FareHarbor). The prototype needs a top-level split.
2. Schema: one Organization/LocalBusiness with @id, full homeport PostalAddress (3919 18th Ave W 98119), separate office ContactPoint, +1 phone, and hours [CONFIRM]. Remove the Product self-review. Add Event/TouristTrip + Offer per cruise. Add launch items.
3. Departures truth: rewrite the FAQ homeport from current client-confirmed data, plus a per-cruise departure field.
4. Duplicate URLs: 301 /about-us/contact-us/ to /contact-us/, /directions/mohai/ to /directionsports/mohai/; one blog hub; one privacy page [CONFIRM]. noindex /search/*. Add launch items.
5. Image weight and alt: responsive sizes, descriptive alt from page context.

Medium
6. Homepage text H1 (dining cruises + private events on Seattle's lakes).
7. Unique meta per event; Seattle in titles.
8. Retire past-date events from the sitemap; refresh or archive 2015-2017 posts.
9. Fix internal links to 404s.

Low
10. OG images on 8 pages; ISO dates and publisher on Article.

No proto scoring yet. The proto side gets scored only after Bob ships pages.


## Independent re-check (2026-11-06, later the same afternoon CT)

The 38/64 total and the area subtotals (10 + 8 + 9 + 9 + 2) were re-added and match. Sampled evidence against `references/raw/`:
- Sitemap children still 46 + 29 + 27 = 102 entries (A3).
- Lighthouse 12 files still read home performance 0.60 / LCP 4.4 s / TBT 940 ms / CLS 0.052 / 4,667 KiB, and brunch 0.51 / LCP 8.6 s / TBT 600 ms / CLS 0.054 (E1). These are lab numbers, not field data, and not the video’s claimed CLS 0.61 or 66.1 MB aggregate.
- FAQPage JSON-LD is present on `/faqs/` with 46 questions (D3).
- Image alts: on unique HTTP 200 HTML files this review counted 714 img tags, 268 empty alt and 113 missing alt (381 without usable alt). The first-pass 360/680 figure used a slightly different page set. B6 remains 0 either way.
- Video metrics from JohnWick’s timestamped queue are third-party claims; this re-check does not repeat them as measurements we made.

The live score stays 38/64. Proto scoring waits for pages.
