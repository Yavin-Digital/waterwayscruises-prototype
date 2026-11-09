# Four-report plan (Waterways) - built after proto pages exist

House standard (NC Utility). Port the tooling from Yavin-Digital/ncutility-prototype. Restyle to the Waterways brand tokens from brand.html. DPA Branding is the only attribution.

1. Waterways-SEO-AEO-Compare.html: live vs proto rows from the facts ledger F01-F20+. Filters: Side-by-side / Live / Proto, SEO / AEO. Expandable "why it matters". Links to the 3 reports.
2. Waterways-SEO-Summary.html: one page for Hilton, with plain-language top 5. No traffic or ranking promises.
3. Waterways-SEO-InDepth.html: technical, on-page, local/NAP (homeport vs office, multi-port departures), schema (Organization @id, LocalBusiness, Event/TouristTrip+Offer per cruise, FAQPage, no self-review), AEO (date-night/family answer content), IA (two paths), assets (weight, alt), plus a section "Supplied audit claims: verified / stale / unverified" summarizing audit-claim-verification.md.
4. Waterways-SEO-Gap-Report.html: live gaps, what the proto fixes, "Designed for go-live, add at launch" items.
5. Facts ledger seo-aeo-compare-facts.md at repo root, returning 404 on the site.

Proto scoring happens only after the build. The re-score follows each Bob fix round. Verification steps: headless Chrome at 390/768/1280, zero console errors, report URLs 200, .md 404.
Do not include: confidential economics, invented metrics, provider selection, real booking.
