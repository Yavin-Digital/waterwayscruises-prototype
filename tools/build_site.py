#!/usr/bin/env python3
"""Generate the Waterways Cruises & Events review prototype from the research packet."""

from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path("/workspace")
SOURCE = Path("/tmp/waterways-packet/research/references/source-content.md")
INVENTORY = Path("/tmp/waterways-packet/research/references/content-inventory.md")
BANNER_SRC = ROOT / "tools/prototype-banner-snippet.html"
HOST = "https://waterwayscruises.clientreview.co"

KEEP = [
    "/",
    "/dining-cruises/",
    "/dining-cruises/dinner/",
    "/dining-cruises/weekend-brunch-cruise/",
    "/dining-cruises/supper/",
    "/taco-thursday-seattle-lakes-cruise-tour/",
    "/lunch-cruises/",
    "/cruise-calendar/",
    "/gift-cards/",
    "/holiday-cruises/",
    "/parade-of-lights-cruises/",
    "/thanksgiving-day-cruise/",
    "/holiday-cruises/holiday-dinner-cruise/",
    "/holiday-cruises/holiday-sights-cruise/",
    "/holiday-cruises/christmas-eve-dinner-cruise/",
    "/holiday-cruises/new-years-eve-dinner-cruise/",
    "/new-years-eve-party-cruise/",
    "/willamette-valley-vineyards-wine-pairing-cruise/",
    "/seafair-cruises/",
    "/seafair-party-blue-angels/",
    "/seafair-blue-angels-bbq-lunch-cruise/",
    "/mothers-day-dinner-cruise/",
    "/mothers-day-brunch-cruise/",
    "/holiday-cruises/fathers-day-brunch-cruise/",
    "/fourth-of-july-fireworks-dinner-cruise/",
    "/fourth-of-july-fireworks-party-cruise/",
    "/easter-brunch/",
    "/all-cruises/valentines-day-lunch-cruise/",
    "/valentines-dinner-cruise/",
    "/all-cruises/sip-sunset-valentines-wine-and-sights-cruise/",
    "/all-cruises/fall-foliage-lunch-cruise/",
    "/11-21-26-indiana-uw-sailgating/",
    "/11-07-26-pennstate-uw-sailgating/",
    "/10-09-26-iowa-hawkeyes-uw-sailgating/",
    "/09-06-26-applecup-wsuvsuw-sailgating/",
    "/private-events/",
    "/request-a-proposal/",
    "/groups/",
    "/special-occasions/",
    "/fleet/",
    "/fleet/theemeraldstar/",
    "/fleet/theolympicstar/",
    "/fleet/thedestiny/",
    "/fleet/the-sightseer/",
    "/sightseer-cruises/",
    "/vendor-partnerships/",
    "/nonprofit-partner-program/",
    "/nonprofit-partner-program-application/",
    "/directionsports/",
    "/directionsports/mohai/",
    "/directionsports/carillon-point-marina/",
    "/directionsports/kirkland-marina-park/",
    "/directionsports/shilshole-bay-marina/",
    "/directionsports/bell-harbor-marina/",
    "/directionsports/waterwayshomeport/",
    "/hotel-partners/",
    "/faqs/",
    "/gallery/",
    "/about-us/",
    "/careers/",
    "/about-us/blog/",
    "/memberships/",
    "/contact-us/",
    "/privacy-policy/",
    "/blog/2019-husky-sailgating-cruises/",
    "/blog/2015-seattle-seafair-air-show-logboom/",
    "/blog/weather-alert-cruise-cancellations/",
    "/blog/thanksgiving-day-dinner-blog-2016/",
    "/blog/waterways-celebrates-25th-anniversary/",
    "/blog/winetastingcruiseblog/",
    "/blog/what-should-i-wear-for-a-waterways-cruise/",
    "/blog/10-unique-facts-you-might-not-have-known-about-seattle-washington/",
    "/blog/sunday-supper-dining-cruise/",
    "/blog/holiday-blog-2016/",
    "/blog/seattle-holiday-parade-of-lights-cruises-blog/",
    "/blog/fun-facts-you-might-not-have-known-about-tequila/",
    "/blog/sailgating-the-waterways-way/",
    "/blog/6-ways-to-cruise-through-the-holidays-with-waterways-cruises/",
    "/blog/10-best-things-to-see-and-do-in-fremont-seattle/",
    "/blog/see-seattle-from-a-different-perspective-with-a-waterways-dining-cruise/",
    "/blog/weddings-with-waterways/",
    "/blog/holiday-party-blog/",
    "/blog/whats-the-difference-between-boarding-time-and-departure-time/",
    "/blog/happyhourcruiseblog/",
    "/blog/santa-lunch-cruises-blog/",
    "/blog/seafair-2016-highlights/",
    "/blog/seafair-on-a-yacht/",
    "/blog/sailing-north-from-tahiti-to-seattle/",
    "/blog/big-congratulations-class-of-2017/",
    "/blog/the-great-experiment-we-celebrate-july-4th/",
    "/blog/senior-cruises-senior-blog/",
]

SAIL = {
    "/11-21-26-indiana-uw-sailgating/",
    "/11-07-26-pennstate-uw-sailgating/",
    "/10-09-26-iowa-hawkeyes-uw-sailgating/",
    "/09-06-26-applecup-wsuvsuw-sailgating/",
}
DINING_BOOK = {
    "/dining-cruises/dinner/",
    "/dining-cruises/weekend-brunch-cruise/",
    "/dining-cruises/supper/",
    "/taco-thursday-seattle-lakes-cruise-tour/",
    "/holiday-cruises/holiday-dinner-cruise/",
    "/holiday-cruises/holiday-sights-cruise/",
    "/holiday-cruises/christmas-eve-dinner-cruise/",
    "/holiday-cruises/new-years-eve-dinner-cruise/",
    "/new-years-eve-party-cruise/",
    "/willamette-valley-vineyards-wine-pairing-cruise/",
    "/seafair-cruises/",
    "/seafair-party-blue-angels/",
    "/seafair-blue-angels-bbq-lunch-cruise/",
    "/mothers-day-dinner-cruise/",
    "/mothers-day-brunch-cruise/",
    "/holiday-cruises/fathers-day-brunch-cruise/",
    "/fourth-of-july-fireworks-dinner-cruise/",
    "/fourth-of-july-fireworks-party-cruise/",
    "/easter-brunch/",
    "/all-cruises/valentines-day-lunch-cruise/",
    "/valentines-dinner-cruise/",
    "/all-cruises/sip-sunset-valentines-wine-and-sights-cruise/",
    "/all-cruises/fall-foliage-lunch-cruise/",
    "/thanksgiving-day-cruise/",
    "/parade-of-lights-cruises/",
}
PRIVATE = {
    "/private-events/",
    "/request-a-proposal/",
    "/groups/",
    "/special-occasions/",
    "/fleet/",
    "/fleet/theemeraldstar/",
    "/fleet/theolympicstar/",
    "/fleet/thedestiny/",
    "/fleet/the-sightseer/",
    "/sightseer-cruises/",
    "/vendor-partnerships/",
    "/nonprofit-partner-program/",
    "/nonprofit-partner-program-application/",
}

HERO = {
    "/": ("hero-home.jpg", "Waterways yacht on a Seattle lake, from the live site library"),
    "/dining-cruises/": ("hero-deck.jpg", "Guests on an open deck with the Seattle shoreline behind them"),
    "/dining-cruises/dinner/": ("dinner-toast.jpg", "A guest holding a glass of wine at a set dining table"),
    "/dining-cruises/weekend-brunch-cruise/": ("brunch-plate.jpg", "A brunch plate and a glass of wine on a cruise table"),
    "/dining-cruises/supper/": ("supper-table.jpg", "Guests seated for supper beside the windows"),
    "/taco-thursday-seattle-lakes-cruise-tour/": ("taco-bar.jpg", "A taco bar set beside a sunlit window"),
    "/private-events/": ("wedding-ceremony.jpg", "A ceremony gathering on a yacht deck"),
    "/fleet/": ("emerald-sunset.jpg", "Emerald Star on the water at sunset"),
    "/fleet/theemeraldstar/": ("emerald-sunset.jpg", "Emerald Star on the water at sunset"),
    "/fleet/theolympicstar/": ("olympic-skyline.jpg", "Olympic Star with the Seattle skyline and Space Needle behind it"),
    "/fleet/thedestiny/": ("spring-docked.jpg", "A Waterways yacht docked beside the lake"),
    "/fleet/the-sightseer/": ("sightseer.jpg", "Sightseer on the lake"),
    "/sightseer-cruises/": ("mohai-vessel.jpg", "Sightseer alongside a Seattle dock"),
    "/holiday-cruises/": ("holiday-banner.jpg", "A Waterways yacht dressed for the holidays"),
    "/gallery/": ("gallery-04.jpg", "Guests gathered aboard a Waterways yacht"),
    "/about-us/": ("founders.jpg", "Hilton Smith and Shirley Turnbow, co-founders, from the live About page"),
    "/thanksgiving-day-cruise/": ("thanksgiving.jpg", "Boats and autumn trees along a Seattle harbor"),
    "/new-years-eve-party-cruise/": ("skyline-night.jpg", "Seattle skyline at night reflected on the water"),
    "/holiday-cruises/new-years-eve-dinner-cruise/": ("skyline-night.jpg", "Seattle skyline at night reflected on the water"),
    "/seafair-cruises/": ("blue-angels.jpg", "U.S. Navy Blue Angels in formation"),
    "/seafair-blue-angels-bbq-lunch-cruise/": ("blue-angels.jpg", "U.S. Navy Blue Angels in formation"),
    "/willamette-valley-vineyards-wine-pairing-cruise/": ("wine.jpg", "Wine glasses from the live wine-pairing page"),
    "/groups/": ("corporate-table.jpg", "A group seated together at a table aboard a yacht"),
    "/special-occasions/": ("wedding-ceremony.jpg", "A celebration gathering on a yacht deck"),
    "/contact-us/": ("hero-deck.jpg", "Open deck and lake, from the live site library"),
    "/directionsports/": ("map-dock9.png", "Map of Fishermen's Terminal highlighting Dock 9 and parking zones"),
}

CRUISE_LINKS = {
    "Premier Seattle Dinner Cruise": "/dining-cruises/dinner/",
    "Weekend Brunch Cruise": "/dining-cruises/weekend-brunch-cruise/",
    "Sunday Supper Cruise": "/dining-cruises/supper/",
    "Holiday Dining Cruise | Parade of Lights": "/holiday-cruises/holiday-dinner-cruise/",
    "Holiday Sights Cruise | Parade of Lights": "/holiday-cruises/holiday-sights-cruise/",
    "Christmas Eve Dinner Cruise": "/holiday-cruises/christmas-eve-dinner-cruise/",
    "New Year’s Eve Dinner Cruise": "/holiday-cruises/new-years-eve-dinner-cruise/",
    "New Year's Eve Dinner Cruise": "/holiday-cruises/new-years-eve-dinner-cruise/",
    "New Year’s Eve Party Cruise": "/new-years-eve-party-cruise/",
    "Thanksgiving Day Cruise": "/thanksgiving-day-cruise/",
    "Wine Pairing Cruise with Willamette Valley Vineyards": "/willamette-valley-vineyards-wine-pairing-cruise/",
    "11/21 INDIANA @ UW Sailgating Cruise": "/11-21-26-indiana-uw-sailgating/",
    "11/07/26 – Penn State Nittany Lions @ UW Sailgating": "/11-07-26-pennstate-uw-sailgating/",
    "Valentine’s Day Lunch Cruise": "/all-cruises/valentines-day-lunch-cruise/",
    "The Emerald Star": "/fleet/theemeraldstar/",
    "Emerald Star": "/fleet/theemeraldstar/",
    "The Olympic Star": "/fleet/theolympicstar/",
    "Olympic Star": "/fleet/theolympicstar/",
    "The Destiny": "/fleet/thedestiny/",
    "The Sightseer": "/fleet/the-sightseer/",
}

NAV = [
    ("Dining Cruises", [
        ("Dining Cruises", "/dining-cruises/"),
        ("Premier Seattle Dinner Cruise", "/dining-cruises/dinner/"),
        ("Weekend Brunch Cruise", "/dining-cruises/weekend-brunch-cruise/"),
        ("Sunday Supper Cruise", "/dining-cruises/supper/"),
        ("Taco Thursday", "/taco-thursday-seattle-lakes-cruise-tour/"),
        ("Lunch Cruises", "/lunch-cruises/"),
        ("Cruise Calendar", "/cruise-calendar/"),
        ("Gift Cards", "/gift-cards/"),
    ]),
    ("Seasonal Cruises", [
        ("Holiday Cruises", "/holiday-cruises/"),
        ("Parade of Lights", "/parade-of-lights-cruises/"),
        ("Thanksgiving Day Cruise", "/thanksgiving-day-cruise/"),
        ("Holiday Dinner Cruise", "/holiday-cruises/holiday-dinner-cruise/"),
        ("Holiday Sights Cruise", "/holiday-cruises/holiday-sights-cruise/"),
        ("Christmas Eve Dinner Cruise", "/holiday-cruises/christmas-eve-dinner-cruise/"),
        ("New Year's Eve Dinner Cruise", "/holiday-cruises/new-years-eve-dinner-cruise/"),
        ("New Year's Eve Party Cruise", "/new-years-eve-party-cruise/"),
        ("Wine Pairing Cruise", "/willamette-valley-vineyards-wine-pairing-cruise/"),
        ("Seafair Cruises", "/seafair-cruises/"),
        ("Seafair Party Cruise", "/seafair-party-blue-angels/"),
        ("Seafair BBQ Lunch Cruise", "/seafair-blue-angels-bbq-lunch-cruise/"),
        ("Mother's Day Dinner", "/mothers-day-dinner-cruise/"),
        ("Mother's Day Brunch", "/mothers-day-brunch-cruise/"),
        ("Father's Day Brunch", "/holiday-cruises/fathers-day-brunch-cruise/"),
        ("Fourth of July Dinner", "/fourth-of-july-fireworks-dinner-cruise/"),
        ("Fourth of July Party", "/fourth-of-july-fireworks-party-cruise/"),
        ("Easter Brunch", "/easter-brunch/"),
        ("Valentine's Lunch", "/all-cruises/valentines-day-lunch-cruise/"),
        ("Valentine's Dinner", "/valentines-dinner-cruise/"),
        ("Valentine's Sunset Wine", "/all-cruises/sip-sunset-valentines-wine-and-sights-cruise/"),
        ("Fall Foliage Lunch", "/all-cruises/fall-foliage-lunch-cruise/"),
        ("Sailgating: Indiana at UW", "/11-21-26-indiana-uw-sailgating/"),
        ("Sailgating: Penn State at UW", "/11-07-26-pennstate-uw-sailgating/"),
        ("Sailgating: Iowa at UW", "/10-09-26-iowa-hawkeyes-uw-sailgating/"),
        ("Sailgating: Apple Cup", "/09-06-26-applecup-wsuvsuw-sailgating/"),
    ]),
    ("Private Events", [
        ("Private Events", "/private-events/"),
        ("Request a Proposal", "/request-a-proposal/"),
        ("Groups and deck rentals", "/groups/"),
        ("Special Occasions", "/special-occasions/"),
        ("Fleet", "/fleet/"),
        ("Emerald Star", "/fleet/theemeraldstar/"),
        ("Olympic Star", "/fleet/theolympicstar/"),
        ("Destiny", "/fleet/thedestiny/"),
        ("Sightseer", "/fleet/the-sightseer/"),
        ("Sightseer Cruises", "/sightseer-cruises/"),
        ("Vendor Partnerships", "/vendor-partnerships/"),
        ("Nonprofit Partner Program", "/nonprofit-partner-program/"),
    ]),
    ("Plan Your Visit", [
        ("Directions and ports", "/directionsports/"),
        ("MOHAI", "/directionsports/mohai/"),
        ("Carillon Point Marina", "/directionsports/carillon-point-marina/"),
        ("Kirkland Marina Park", "/directionsports/kirkland-marina-park/"),
        ("Shilshole Bay Marina", "/directionsports/shilshole-bay-marina/"),
        ("Bell Harbor Marina", "/directionsports/bell-harbor-marina/"),
        ("Lake Union Piers", "/directionsports/waterwayshomeport/"),
        ("Hotel Partners", "/hotel-partners/"),
        ("FAQs", "/faqs/"),
        ("Gallery", "/gallery/"),
    ]),
    ("About", [
        ("About Us", "/about-us/"),
        ("Careers", "/careers/"),
        ("Journal", "/about-us/blog/"),
        ("Memberships", "/memberships/"),
        ("Contact", "/contact-us/"),
        ("Privacy", "/privacy-policy/"),
    ]),
]

TESTIMONIALS = [
    ("What a neat experience! Went on a dinner cruise for a friend's birthday...we had a group of 6 and we all had a blast. The accommodations/services were on par and the bonus was the amazing views of a beautiful city...I've lived in Seattle my whole life and it was really neat to see my city through Waterways lens...if you are looking for an all inclusive experience with good food and service in a beautiful setting for an overall good time...try Waterways out.", "Gabriel"),
    ("Had a wonderful time here with my team! They truly make the Unwind Cruises an unforgettable experience. The vibes are incredible, the drinks are tasty, and the views are unmatched! Can't wait to come back and bring my family / friends :)", "Marina"),
    ("We went on a Mother's Day Brunch cruise and had the best time. The staff were super friendly, the captain was good at pointing out and informing the guests of the sights around and with fun facts, and the food was absolutely delicious. The views were gorgeous and couldn't have been better. We had a wonderful time and plan on going for another cruise!!", "Amanda P., Yelp"),
    ("From departure to docking, the dinner cruise was a fun little evening. The views of the Seattle skyline at sunset were just spectacular last night, with the nearly-full moon. Cruising around Lake Union, under the the bridges and through the cut into Lake Washington was amazing. The cocktails were strong and my salmon was tasty. I found the Captain’s light narration to be a perfect accompaniment to a well-organized event. Our server was friendly, quick and just genuinely adorable. I would definitely cruise again and would 10/10 recommend this to anyone.", "Lisa"),
    ("Took the wife on a date day on the waterfront. Decided on this for an activity. It was 100% the best decisions we've made being spontaneous. It was amazing, our second cruise (first was the Christmas cruise, highly recommended!). It was fantastic to see the city I love from the water.", "Mandela"),
    ("The boat was so clean and well set up. There was ample room for us all and a great sun deck area outside. Our food was delicious. The best part by far was the incredibly warm and friendly staff. They all personally greeted us and made sure we were having a good time the entire trip. The owners were even on board with their family as well and it was great to see how well oiled the entire team was. We would definitely recommend a cruise with Waterways to anyone new to town or for any born and raised residents of Seattle like myself.", "Ian H., Yelp"),
]


def esc(value: str) -> str:
    return html.escape(value or "", quote=True)


def dedupe_doubled(text: str) -> str:
    t = re.sub(r"\s+", " ", text).strip()
    if len(t) < 160:
        return t
    half = len(t) // 2
    window = 70
    for shift in range(-40, 41):
        cut = half + shift
        if cut < 80 or cut > len(t) - 80:
            continue
        left, right = t[:cut].strip(), t[cut:].strip()
        if left[:window] == right[:window]:
            return left
    return t


def clean_text(text: str) -> str:
    t = text.replace("\u00a0", " ")
    t = re.sub(r"h\s+ousemade", "housemade", t, flags=re.I)
    t = re.sub(r"Chevron down\s*", "", t)
    t = re.sub(r"Posted in:\s*Tweet Email", "", t)
    t = re.sub(r"\bBEST SELLER\b", "", t)
    t = re.sub(r"SOLD OUT!\s*Add yourself to the wai[st]+list\.?", "", t, flags=re.I)
    t = re.sub(r"This cruise is SOLD OUT!\s*Add yourself to the waitlist, and we will contact you if anything opens up\.?", "", t, flags=re.I)
    t = re.sub(r"\(ALMOST SOLD OUT\)", "", t, flags=re.I)
    t = re.sub(r"\(SOLD OUT\)", "", t, flags=re.I)
    t = re.sub(r"\bSOLD OUT\b", "", t, flags=re.I)
    t = re.sub(r"\(AVAILABLE\)", "", t, flags=re.I)
    t = re.sub(r"20%\s*OFF with Code LOVE26", "", t, flags=re.I)
    t = t.replace("the city’s only dining cruise company", "")
    t = t.replace("the city's only dining cruise company", "")
    t = t.replace("Seattle’s Premier Yachts", "Waterways yachts")
    t = t.replace("Seattle's Premier Yachts", "Waterways yachts")
    t = t.replace("Seattle’s leading dining cruise company", "Waterways Cruises and Events")
    t = t.replace("Seattle's leading dining cruise company", "Waterways Cruises and Events")
    t = t.replace("Seattle’s only upscale dining cruise and event company", "a family-owned dining cruise and event company")
    t = t.replace("Seattle's only upscale dining cruise and event company", "a family-owned dining cruise and event company")
    t = re.sub(r"one of the city[’']s premier venues\s*[—-]\s*", "a Waterways yacht: ", t, flags=re.I)
    t = re.sub(r"Seattle[’']s premier private event venue on the water\.?", "Private events on the water in Seattle.", t, flags=re.I)
    t = re.sub(r"(hosting|accommodating|accommodates)\s+over 60,000 guests (?:a|per) year", "welcoming guests", t, flags=re.I)
    t = re.sub(r"upwards of 60,000 guests per year", "welcoming guests", t, flags=re.I)
    t = re.sub(r"up to 220 guests", "large gatherings", t, flags=re.I)
    t = re.sub(r"up 220 guests", "large gatherings", t, flags=re.I)
    t = re.sub(r",?\s*within 1-2 business days", "", t, flags=re.I)
    t = re.sub(
        r"The minimum for a private charter begins at \$5,200\+\+ in non peak and \$6,500\+\+ in peak season\.\s*",
        "",
        t,
    )
    t = re.sub(r"Please enter a number greater than or equal to 5000 \.?", "", t)
    t = re.sub(r"Please enter a number greater than or equal to 0 \.?", "", t)
    t = re.sub(r"This field is for validation purposes and should be left unchanged\.\s*Δ?", "", t)
    t = t.replace("Powered by FareHarbor", "")
    t = dedupe_doubled(t)
    t = re.sub(r"\s{2,}", " ", t).strip(" -|")
    return t


def kind_of(path: str) -> str:
    if path in SAIL:
        return "sail"
    if path in DINING_BOOK:
        return "dining"
    if path in PRIVATE:
        return "private"
    return "general"


def banner() -> str:
    raw = BANNER_SRC.read_text()
    raw = raw.replace("{ClientName}-SEO-AEO-Compare.html", "/Waterways-SEO-AEO-Compare.html")
    raw = raw.replace('href="{ClientName}-SEO-AEO-Compare.html"', 'href="/Waterways-SEO-AEO-Compare.html"')
    return raw


def nav_html(path: str) -> str:
    groups = []
    for label, links in NAV:
        items = "\n".join(f'<a href="{href}">{esc(name)}</a>' for name, href in links)
        groups.append(f'<div class="nav-group"><p class="nav-label">{esc(label)}</p>{items}</div>')
    return f"""
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand-lockup" href="/"><img class="logo-full" src="/img/logo-lockup.png" width="168" height="107" alt="Waterways Cruises and Events"><img class="logo-mark" src="/img/logo-mark.png" alt=""></a>
    <div class="header-actions">
      <nav class="desktop-links" aria-label="Primary">
        <a href="/dining-cruises/">Dining</a>
        <a href="/private-events/">Private events</a>
        <a href="/fleet/">Fleet</a>
        <a href="/cruise-calendar/">Calendar</a>
        <a href="/about-us/">About</a>
        {('<a class="btn nav-cta" href="#book">Book</a>' if kind_of(path) == "dining" else '<a class="btn nav-cta" href="/request-a-proposal/">Request a Proposal</a>')}
      </nav>
      <button class="nav-toggle" id="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-sheet">Menu</button>
    </div>
  </div>
  <div class="nav-sheet" id="nav-sheet">
    <div class="wrap mega">
      {''.join(groups)}
    </div>
  </div>
</header>
"""


def footer_html() -> str:
    cols = []
    journal = [("Journal hub", "/about-us/blog/")] + [
        (p.strip("/").split("/")[-1].replace("-", " "), p) for p in KEEP if p.startswith("/blog/")
    ]
    extra_nav = NAV + [
        ("Journal posts", journal),
    ]
    for label, links in extra_nav:
        items = "\n".join(f'<li><a href="{href}">{esc(name)}</a></li>' for name, href in links)
        cols.append(f"<div><h2>{esc(label)}</h2><ul>{items}</ul></div>")
    return f"""
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <h2>Waterways Cruises &amp; Events</h2>
      <p>For An Unforgettable Experience, Just Add Water®</p>
      <p>Fishermen's Terminal Dock 9<br>3919 18th Ave W<br>Seattle, WA 98119</p>
      <p>Office, by appointment, and mailing address:<br>4005 20th Ave W, Suite 228<br>Seattle, WA 98199</p>
      <p><a href="tel:2062232060">(206) 223-2060</a><br>
      <a href="mailto:contact@waterwayscruises.com">contact@waterwayscruises.com</a><br>
      <a href="mailto:events@waterwayscruises.com">events@waterwayscruises.com</a></p>
      <p>
        <a href="https://www.facebook.com/waterwayscruises">Facebook</a> ·
        <a href="https://www.instagram.com/waterwayscruises/">Instagram</a> ·
        <a href="https://www.tiktok.com/@waterwayscruises">TikTok</a> ·
        <a href="https://www.tripadvisor.com/Attraction_Review-g60878-d1130187">TripAdvisor</a> ·
        <a href="https://www.yelp.com/biz/waterways-cruises-seattle">Yelp</a>
      </p>
    </div>
    {''.join(cols)}
  </div>
  <div class="wrap fine">
    <p>© <span id="year">2026</span> Waterways Cruises &amp; Events. <a href="/privacy-policy/">Privacy</a> · <a href="/about-us/blog/">Journal</a> · <a href="/careers/">Careers</a> · <a href="/gift-cards/">Gift Cards</a> · <a href="/brand.html">Brand guide</a></p>
  </div>
</footer>
<script>document.getElementById("year").textContent = new Date().getFullYear();</script>
"""


def phone_bar(path: str) -> str:
    k = kind_of(path)
    if k == "dining":
        left, right = (f'<a href="#book">Book this cruise</a>', '<a href="tel:2062232060">Call</a>')
    elif k in {"sail", "private"}:
        left, right = ('<a href="/request-a-proposal/">Request a Proposal</a>', '<a href="tel:2062232060">Call</a>')
    else:
        left, right = ('<a href="/dining-cruises/">Dining Cruises</a>', '<a href="/request-a-proposal/">Request a Proposal</a>')
    return f'<nav class="phone-bar" aria-label="Quick actions">{left}{right}</nav>'


def org_schema() -> str:
    return """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Organization","@id":"https://waterwayscruises.clientreview.co/#organization","name":"Waterways Cruises & Events","url":"https://waterwayscruises.clientreview.co/","telephone":"+1-206-223-2060","email":"contact@waterwayscruises.com","logo":"https://waterwayscruises.clientreview.co/img/logo-lockup.png","sameAs":["https://www.facebook.com/waterwayscruises","https://www.instagram.com/waterwayscruises/","https://www.tiktok.com/@waterwayscruises","https://www.yelp.com/biz/waterways-cruises-seattle"]}
</script>
"""


def layout(path: str, title: str, description: str, body: str, extra_head: str = "", og: str = "/img/hero-home.jpg") -> str:
    canonical = HOST + ("/" if path == "/" else path)
    desc = re.sub(r"\s+", " ", description).strip()
    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="noindex, nofollow">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{HOST}{og}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="website">
<link rel="icon" href="/img/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;700&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/site.css">
{extra_head}
{org_schema()}
</head>
<body class="{"is-brand" if str(path).endswith("brand.html") else ""}">
<a class="skip" href="#main">Skip to content</a>
{banner()}
{nav_html(path)}
{body}
{footer_html()}
{phone_bar(path)}
<script src="/js/site.js"></script>
</body>
</html>
"""


def hero_block(path: str, h1: str, lede: str, actions: str) -> str:
    img, alt = HERO.get(path, ("hero-home.jpg", "Waterways yacht on a Seattle lake"))
    klass = "hero" if path == "/" else "page-hero with-photo"
    return f"""
<section class="{klass}" style="background-image:url('/img/{img}')">
  <div class="{'hero-inner' if path == '/' else 'wrap'}">
    <p class="eyebrow">For An Unforgettable Experience, Just Add Water®</p>
    <h1>{h1}</h1>
    <p>{lede}</p>
    <div class="btn-row hero-actions">{actions}</div>
  </div>
</section>
"""


def book_widget(cruise_name: str, dinner: bool = False) -> str:
    lobster = ""
    if dinner:
        lobster = '<label class="check"><input type="checkbox" data-enhance value="Steak and lobster entree upgrade"> Steak &amp; Lobster entree upgrade, as offered on the Dinner page</label>'
    return f"""
<section class="band band-paper" id="book">
  <div class="wrap">
    <h2 class="center">Book this cruise</h2>
    <p class="measure center">Demo only. Choose a cruise, then a date, then a party of about 2 to 10, then optional enhancements. Nothing is reserved.</p>
    <div class="book" data-book>
      <div class="steps"><span>Cruise</span><span>Date</span><span>Party</span><span>Enhancements</span><span>Review</span></div>
      <div class="book-step">
        <label>Cruise type
          <select name="cruise" required>
            <option selected>{esc(cruise_name)}</option>
          </select>
        </label>
        <p><button class="btn" type="button" data-next>Continue</button></p>
      </div>
      <div class="book-step">
        <label>Date
          <input name="date" type="date" required>
        </label>
        <p class="quiet">Choose any date. Availability is not shown here.</p>
        <p class="btn-row"><button class="btn btn-ghost" type="button" data-back>Back</button><button class="btn" type="button" data-next>Continue</button></p>
      </div>
      <div class="book-step">
        <label>Party size
          <select name="party" required>
            <option value="">Select</option>
            {''.join(f'<option>{n}</option>' for n in range(2, 11))}
          </select>
        </label>
        <p class="quiet">About 2 to 10 guests. Groups of 10 or more can read the terms on <a href="/groups/">Groups and deck rentals</a>.</p>
        <p class="btn-row"><button class="btn btn-ghost" type="button" data-back>Back</button><button class="btn" type="button" data-next>Continue</button></p>
      </div>
      <div class="book-step">
        <fieldset>
          <legend>Optional enhancements</legend>
          <label class="check"><input type="checkbox" data-enhance value="Rose petals and chocolate-covered strawberries"> Rose petals and chocolate-covered strawberries</label>
          <label class="check"><input type="checkbox" data-enhance value="Guaranteed window table"> Guaranteed window table</label>
          {lobster}
        </fieldset>
        <p class="btn-row"><button class="btn btn-ghost" type="button" data-back>Back</button><button class="btn" type="button" data-next>Review</button></p>
      </div>
      <div class="book-step">
        <div class="form-note" data-review></div>
        <p class="btn-row"><button class="btn btn-ghost" type="button" data-back>Back</button><a class="btn btn-ghost" href="tel:2062232060">Call (206) 223-2060</a></p>
      </div>
    </div>
  </div>
</section>
"""


def closing(path: str) -> str:
    k = kind_of(path)
    if k == "dining":
        return """<section class="band band-navy"><div class="wrap center"><h2>Reserve a table</h2><p>This is a preview. No ticket is issued.</p><div class="btn-row center"><a class="btn btn-light" href="#book">Book this cruise</a><a class="btn btn-ghost" style="color:#fff;border-color:#fff" href="tel:2062232060">Call</a></div><p><a href="/private-events/">Need the whole boat? Private charters</a></p></div></section>"""
    if k in {"sail", "private"}:
        return """<section class="band band-navy"><div class="wrap center"><h2>Plan a private event</h2><p>Whole-boat, upper-deck, and buyout requests use a proposal. This form does not send.</p><div class="btn-row center"><a class="btn btn-light" href="/request-a-proposal/">Request a Proposal</a><a class="btn btn-ghost" style="color:#fff;border-color:#fff" href="tel:2062232060">Call</a></div><p><a href="/dining-cruises/">Need a table instead? Dining cruises</a></p></div></section>"""
    return """<section class="band band-navy"><div class="wrap center"><h2>Two ways aboard</h2><div class="btn-row center"><a class="btn btn-light" href="/dining-cruises/">Dining Cruises</a><a class="btn btn-ghost" style="color:#fff;border-color:#fff" href="/private-events/">Private Charters</a></div></div></section>"""


def format_menu(text: str) -> str:
    t = esc(text)
    t = re.sub(r"(First Course|Second Course|Third Course|Your choice of entrée:)", r"<br><strong>\1</strong><br>", t)
    t = t.replace("-or-", "<br>")
    t = t.replace("*MENU IS SUBJECT TO CHANGE*", "<br><em>Menu is subject to change.</em>")
    t = t.replace("*menu subject to change*", "<br><em>Menu is subject to change.</em>")
    return f'<div class="menu"><div class="menu-block"><p>{t}</p></div></div>'


def render_prose(heading: str, text: str) -> str:
    if not text:
        return ""
    menuish = "MENU IS SUBJECT TO CHANGE" in text.upper() or "First Course" in text or heading.lower().endswith("menu")
    body = format_menu(text) if menuish else f"<p>{esc(text)}</p>"
    if heading in CRUISE_LINKS:
        href = CRUISE_LINKS[heading]
        return f'<article class="card"><h3><a class="title" href="{href}">{esc(heading)}</a></h3><div class="meta">{body}</div><p><a href="{href}">View this cruise</a></p></article>'
    return f"<h2>{esc(heading)}</h2>{body}"


def parse_source() -> dict:
    text = SOURCE.read_text()
    parts = re.split(r"\n## (https://[^\n]+)\n", text)
    pages = {}
    for i in range(1, len(parts), 2):
        url = parts[i].strip()
        body = parts[i + 1]
        path = re.sub(r"^https://(?:www\.)?waterwayscruises.com", "", url)
        path = path.split("?")[0]
        if not path.endswith("/") and path != "":
            # keep blog slugs which already end with /
            if not path.endswith("/"):
                path = path + "/"
        if path == "":
            path = "/"
        title = (re.search(r"^Title:\s*(.*)$", body, re.M) or [None, ""])[1]
        # fix
        m_title = re.search(r"^Title:\s*(.*)$", body, re.M)
        m_meta = re.search(r"^Meta:\s*(.*)$", body, re.M)
        m_dec = re.search(r"^Decision \(url\):\s*(\w+)", body, re.M)
        sections = []
        chunks = re.split(r"\n### ", body)
        for ch in chunks[1:]:
            head, _, rest = ch.partition("\n")
            sections.append((head.strip(), rest.strip()))
        pages[path] = {
            "title": m_title.group(1).strip() if m_title else path,
            "meta": m_meta.group(1).strip() if m_meta else "",
            "decision": m_dec.group(1) if m_dec else "",
            "sections": sections,
        }
    return pages


def h1_for(path: str, page: dict) -> str:
    overrides = {
        "/": "Dining cruises and private events on Seattle's lakes.",
        "/groups/": "Groups and deck rentals",
        "/memberships/": "Memberships",
        "/privacy-policy/": "Privacy Policy",
        "/dining-cruises/dinner/": "Premier Seattle Dinner Cruise",
        "/contact-us/": "Contact Us",
        "/request-a-proposal/": "Request a Proposal",
        "/cruise-calendar/": "Cruise Calendar",
        "/gift-cards/": "Gift Cards",
        "/faqs/": "Frequently Asked Questions",
        "/about-us/blog/": "Journal",
    }
    if path in overrides:
        return overrides[path]
    for heading, body in page["sections"]:
        if heading not in {"(intro)", "Google Map", "Link Gallery"} and heading.strip():
            if len(heading) < 90:
                return heading
    live = page["title"].split("|")[0].strip()
    return live or "Waterways Cruises & Events"


def title_for(path: str, h1: str) -> str:
    if path == "/":
        return "Waterways Cruises & Events | Dining Cruises in Seattle"
    name = h1
    if "seattle" not in name.lower():
        name = f"{name} in Seattle"
    return f"{name} | Waterways Cruises & Events"


def meta_for(path: str, page: dict, h1: str) -> str:
    if path == "/":
        return "Waterways Cruises & Events offers dining cruises and private charters on Lake Union and Lake Washington in Seattle, from Fishermen's Terminal. Book a public cruise or request a proposal for a private event."
    if path in SAIL:
        return f"{h1}. A full-vessel buyout. Request a proposal or call."
    meta = clean_text(page["meta"])
    meta = meta.replace("only", "").replace("  ", " ")
    if "seattle" not in meta.lower():
        meta = meta.rstrip(".") + " Seattle."
    return meta[:300]


ICON_RE = re.compile(
    r"(Calendar Dates?|Clock Duration|Map Marker Departure Location|Map Marker Departure|Map Marker Location|Food Includes|Glass Includes|User Ages|Dress Code Attire|Info Attire)\s*:?",
    re.I,
)
ICON_LABELS = {
    "calendar dates": "Dates",
    "calendar date": "Date",
    "clock duration": "Duration",
    "map marker departure location": "Departure",
    "map marker departure": "Departure",
    "map marker location": "Departure",
    "food includes": "Includes",
    "glass includes": "Toast",
    "user ages": "Ages",
    "dress code attire": "Attire",
    "info attire": "Attire",
}


def soften_heading(heading: str) -> str:
    letters = [c for c in heading if c.isalpha()]
    if len(letters) > 8 and sum(c.isupper() for c in letters) / len(letters) > 0.7:
        lower = heading.lower()
        return lower[0].upper() + lower[1:]
    return heading


def parse_quick(text: str):
    matches = list(ICON_RE.finditer(text))
    if len(matches) < 1:
        return None
    facts = []
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        value = text[match.end():end].strip(" :|-")
        key = re.sub(r"\s+", " ", match.group(1)).lower()
        facts.append([ICON_LABELS.get(key, match.group(1).title()), value])
    prose = ""
    label, value = facts[-1]
    if len(value) > 120:
        cut = re.search(r"\.\s+[A-Z]", value[24:])
        zip_cut = re.search(r"\b\d{5}\b", value)
        if cut:
            idx = 24 + cut.end() - 1
            prose = value[idx:].strip()
            facts[-1][1] = value[:idx].strip()
        elif zip_cut and zip_cut.end() < 220:
            facts[-1][1] = value[: zip_cut.end()].strip(" |-")
            prose = value[zip_cut.end():].strip(" |-")
        else:
            short = re.match(r"(.{1,80}?)(\s+[A-Z][a-z].{30,})", value)
            if short:
                facts[-1][1] = short.group(1).strip()
                prose = short.group(2).strip()
    return facts, prose


def facts_html(facts) -> str:
    cells = "".join(f'<div class="fact"><span>{esc(label)}</span>{esc(value)}</div>' for label, value in facts)
    return f'<div class="facts">{cells}</div>'


def includes_html(text: str) -> str:
    text = text.strip()
    if text.startswith("Two-and-a-half-hour cruise"):
        items = [
            "Two-and-a-half-hour cruise on Lake Union and Lake Washington (cruising on Lake Washington is subject to boat traffic and weather).",
            "Your own private table",
            "Prosecco or sparkling cider toast upon boarding",
            "Delicious plated dinner*",
            "Captain’s light narration of sights",
            "Ages 13+",
            "Breathtaking views of Seattle’s most iconic sights, including: the Space Needle, charming floating homes, historic bridges, the stunning city skyline, waterfront landmarks, seaplanes",
        ]
        notes = [
            "Book for a group of 10 or more to save 10% off your tickets.",
            "Full-service bar available for the purchase of specialty cocktails, wine, beer, and non-alcoholic beverages.",
            "Entree selections for our dinner cruises are final. Please contact our office at least 2 business days prior to your cruise if you need to update your selection.",
        ]
        lis = "".join(f"<li>{esc(item)}</li>" for item in items)
        paras = "".join(f"<p>{esc(note)}</p>" for note in notes)
        return f'<ul class="includes">{lis}</ul>{paras}'
    parts = [part.strip() for part in re.split(r"(?<=\.)\s+(?=[A-Z])", text) if part.strip()]
    if len(parts) < 2:
        return f"<p>{esc(text)}</p>"
    return "<ul class=\"includes\">" + "".join(f"<li>{esc(item)}</li>" for item in parts) + "</ul>"


def menu_fingerprint(text: str) -> str:
    folded = re.sub(r"\s+", " ", text.lower())
    found = re.search(r"first course\s+(.{30})", folded)
    return found.group(1) if found else folded[:80]


def split_seasons(text: str):
    parts = re.split(r"(?=(?:Fall/Winter|Spring/Summer)\s+Dinner Menu)", text)
    seasons = [part.strip() for part in parts if "first course" in part.lower()]
    return seasons or ([text.strip()] if "first course" in text.lower() else [])


def render_menu_season(text: str) -> str:
    title = ""
    match = re.match(r"((?:Fall/Winter|Spring/Summer)\s+Dinner Menu(?:\s*\([^)]+\))?)", text)
    body = text
    if match:
        title = match.group(1).strip()
        body = text[match.end():].strip()
    body = re.sub(r"\*+\s*menu is subject to change\s*\*+", "", body, flags=re.I)
    key = ""
    key_match = re.search(r"\((?:v|veg|gf|df)\)\s*=.*$", body, flags=re.I)
    if key_match:
        key = key_match.group(0).strip()
        body = body[: key_match.start()].strip()
    chunks = re.split(r"\s*(First Course|Second Course|Third Course)\s*", body)
    html_out = ""
    if title:
        html_out += f"<h2>{esc(title)}</h2>"
    if chunks[0].strip():
        html_out += f'<p class="menu-lead">{esc(chunks[0].strip())}</p>'
    names = chunks[1::2]
    contents = chunks[2::2]
    for name, content in zip(names, contents):
        label = name[:1].upper() + name[1:].lower()
        html_out += f"<h3>{esc(label)}</h3>"
        content = re.sub(r"^Your choice of entrée:\s*", "", content.strip())
        if name.lower().startswith("second"):
            dishes = re.split(r"\s+-or-\s+", content)
            if len(dishes) == 1:
                dishes = re.split(
                    r"\s+(?=(?:Chicken Marsala|Vegetable Lasagna|Pan Roasted|Sunburst Squash|Steak & Lobster))",
                    content,
                )
            html_out += "".join(f'<p class="dish">{esc(dish.strip())}</p>' for dish in dishes if dish.strip())
        else:
            html_out += f'<p class="dish">{esc(content.strip())}</p>'
    if key:
        html_out += f'<p class="menu-key">{esc(key)}</p>'
    html_out += '<p class="menu-note">Menu is subject to change.</p>'
    return f'<div class="menu">{html_out}</div>'


def private_events_html(pages: dict) -> str:
    page = pages["/private-events/"]
    sections = {heading: clean_text(body) for heading, body in page["sections"]}
    opening = sections.get("Unique, Fun, and Memorable Events", "")
    occasion = []
    photos = {
        "Corporate Events": "/img/corporate-table.jpg",
        "Weddings": "/img/wedding-ceremony.jpg",
        "Celebrations": "/img/gallery-04.jpg",
    }
    alts = {
        "Corporate Events": "Colleagues seated at a table during a private event",
        "Weddings": "A ceremony on the deck",
        "Celebrations": "Guests gathered aboard a yacht",
    }
    for name in ("Corporate Events", "Weddings", "Celebrations"):
        text = sections.get(name, "")
        if text:
            occasion.append(
                f'<article class="room"><img src="{photos[name]}" alt="{esc(alts[name])}"><h3>{esc(name)}</h3><p>{esc(text)}</p></article>'
            )
    fleet_photos = {
        "The Emerald Star": ("/img/emerald-sunset.jpg", "Emerald Star on the water at sunset", "/fleet/theemeraldstar/"),
        "The Olympic Star": ("/img/olympic-skyline.jpg", "Olympic Star with the Seattle skyline", "/fleet/theolympicstar/"),
        "The Destiny": ("/img/spring-docked.jpg", "A Waterways yacht docked beside the lake", "/fleet/thedestiny/"),
        "The Sightseer": ("/img/sightseer.jpg", "Sightseer on the lake", "/fleet/the-sightseer/"),
    }
    rooms = []
    for heading, body in pages.get("/fleet/", {}).get("sections", []):
        text = clean_text(body)
        if heading in fleet_photos and text:
            src, alt, href = fleet_photos[heading]
            rooms.append(
                f'<article class="room"><a href="{href}"><img src="{src}" alt="{esc(alt)}"><h3>{esc(heading)}</h3></a><p>{esc(text)}</p></article>'
            )
    quotes_raw = ""
    for heading, body in page["sections"]:
        text = clean_text(body)
        if text.startswith("Everyone was so kind"):
            quotes_raw = text
    quote_bits = [bit.strip() for bit in re.split(r"(?=Incredible Cruise Event Experience!|We took Waterways)", quotes_raw) if bit.strip()]
    quotes = "".join(f"<blockquote><p>{esc(bit)}</p></blockquote>" for bit in quote_bits)
    corporate = ['<h2 id="corporate">Corporate events</h2>']
    first = True
    for heading, body in pages.get("/corporate/", {}).get("sections", []):
        text = clean_text(body)
        if not text:
            continue
        if heading == "Events with Waterways":
            corporate.append(f"<h3>{esc(heading)}</h3><p>{esc(text)}</p>")
        elif first:
            corporate.append(f"<p>{esc(text)}</p>")
            first = False
        else:
            corporate.append(f"<h3>{esc(soften_heading(heading))}</h3><p>{esc(text)}</p>")
    corporate.append('<p><a href="/files/2026-Private-Catering-Menus.pdf">2026 Private Catering Menus (PDF)</a><br><a href="/files/2026-Wedding-Packages-Flyer.pdf">2026 Wedding Packages Flyer (PDF)</a><br><a href="/files/2027-Private-Charter-Flyer.pdf">2027 Private Charter Flyer (PDF)</a></p>')
    return f"""
<p>{esc(opening)}</p>
<div class="room-grid">{''.join(occasion)}</div>
<h2>The fleet</h2>
<div class="room-grid">{''.join(rooms)}</div>
<h2>Guest notes</h2>
<div class="quotes">{quotes}</div>
{''.join(corporate)}
"""


def section_html(path: str, page: dict, pages: dict) -> str:
    if path == "/private-events/":
        return private_events_html(pages)
    blocks = []
    seen = set()
    seen_menus = set()
    for heading, raw in page["sections"]:
        text = clean_text(raw)
        key = (heading, text[:180])
        if key in seen:
            continue
        seen.add(key)
        if heading in {"Google Map", "Link Gallery", "Follow Waterways Cruises on Instagram!"}:
            continue
        if heading == "(intro)" and (not text or text.lower() in {"best seller", "sold out"}):
            continue
        if not text and heading in {"Meet Our Fleet", "Catering Menus", "Beverage Options", "Preferred Vendors", "Directions & Ports", "Wedding Enhancements", "Packages & Enhancements"}:
            continue
        if path == "/about-us/" and heading == "About Our Founders":
            blocks.append("""
<h2>About our founders</h2>
<p>Waterways Cruises &amp; Events has been part of Seattle’s lake and Puget Sound scene since 1994. We started with one yacht in April 1994 and have grown into a fleet of four vessels for weddings, rehearsal dinners, corporate events, celebrations, and public dining cruises.</p>
<p>Co-founders Shirley Turnbow and Hilton Smith lead Waterways. Hilton Smith is CEO.</p>
""")
            continue
        if path == "/fleet/thedestiny/" and "30 guests" in text:
            blocks.append(render_prose(heading, text))
            continue
        if not text:
            continue
        if heading == "Quick Details" or len(ICON_RE.findall(text)) >= 2:
            parsed = parse_quick(text)
            if parsed:
                facts, prose = parsed
                blocks.append("<h2>Quick details</h2>")
                blocks.append(facts_html(facts))
                if prose:
                    blocks.append(f"<p>{esc(prose)}</p>")
                continue
        if heading == "Cruise Includes":
            blocks.append("<h2>Cruise includes</h2>")
            blocks.append(includes_html(text))
            continue
        if "first course" in text.lower():
            fresh = []
            for season in split_seasons(text):
                mark = menu_fingerprint(season)
                if mark in seen_menus:
                    continue
                seen_menus.add(mark)
                fresh.append(season)
            if fresh:
                blocks.append("".join(render_menu_season(season) for season in fresh))
            continue
        blocks.append(render_prose(soften_heading(heading), text))
    if path == "/dining-cruises/dinner/" and "/food-and-bar/dessert/" in pages:
        blocks.append('<h2 id="dessert-2020">Desserts</h2>')
        for heading, raw in pages["/food-and-bar/dessert/"]["sections"]:
            text = clean_text(raw)
            if text:
                blocks.append(render_prose(heading, text))
    return "\n".join(blocks)


def faq_html(pages: dict) -> tuple[str, str]:
    rows = []
    for line in INVENTORY.read_text().splitlines():
        if not line.startswith("| B"):
            continue
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cols) < 6:
            continue
        if cols[1].rstrip("/") != "https://waterwayscruises.com/faqs":
            continue
        rows.append({"id": cols[0], "q": cols[2], "kind": cols[4], "decision": cols[5]})
    questions = [r for r in rows if r["kind"] == "copy"]
    blob = " ".join(clean_text(body) for _, body in pages["/faqs/"]["sections"])
    blob = re.sub(r"\s+", " ", blob)
    parts = []
    schema_entities = []
    current_group = "Policies"
    q_index = {r["q"]: i for i, r in enumerate(questions)}
    # group headings in order
    groups = [r["q"] for r in rows if r["kind"] == "heading" and r["q"] != "Frequently Asked Questions"]
    positions = []
    for q in questions:
        pos = blob.find(q["q"])
        positions.append(pos)
    for i, q in enumerate(questions):
        start = positions[i]
        if start < 0:
            answer = "The published answer was not recovered from the source extract."
        else:
            end = len(blob)
            for later in positions[i + 1 :]:
                if later > start:
                    end = later
                    break
            answer = blob[start + len(q["q"]) : end].strip(" :-")
            answer = dedupe_doubled(answer)
        if q["id"] == "B0049":
            answer = (
                "Private events leave from the port named for that charter. "
                "Public dining cruises primarily leave from Fishermen's Terminal Dock 9, 3919 18th Ave W, Seattle, WA 98119. "
                "Sightseer departs the Museum of History and Industry (MOHAI), 860 Terry Ave N, Seattle, WA 98109, Slip 6. "
                "Other ports are listed on the directions pages."
            )
        # assign group: last group heading that appears before this question in the inventory
        parts.append(f"<details><summary>{esc(q['q'])}</summary><p>{esc(answer)}</p></details>")
        schema_entities.append(
            '{"@type":"Question","name":'
            + json_str(q["q"])
            + ',"acceptedAnswer":{"@type":"Answer","text":'
            + json_str(answer)
            + "}}"
        )
    group_note = "".join(f"<h2>{esc(g)}</h2>" if False else "" for g in groups)
    # Insert group headings by walking rows
    rendered = ['<div class="faq">']
    qi = 0
    for r in rows:
        if r["kind"] == "heading" and r["q"] != "Frequently Asked Questions":
            rendered.append(f"<h2>{esc(r['q'])}</h2>")
        elif r["kind"] == "copy":
            rendered.append(parts[qi])
            qi += 1
    rendered.append("</div>")
    schema = (
        '<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
        + ",".join(schema_entities)
        + "]}</script>"
    )
    return "\n".join(rendered), schema, len(questions)


def json_str(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'


def home_body() -> str:
    proof = "\n".join(
        f"<blockquote><p>{esc(quote)}</p><footer>{esc(name)}</footer></blockquote>"
        for quote, name in TESTIMONIALS[:3]
    )
    return f"""
<section class="dest-row">
  <a href="/dining-cruises/dinner/">
    <img src="/img/dinner-toast.jpg" alt="A guest holding a glass of wine at a set dining table">
    <span class="shade"></span>
    <span class="dest-copy">
      <h2>Dinner</h2>
      <p>2.5 hours · plated · ages 13+</p>
      <span class="btn">View dinner</span>
    </span>
  </a>
  <a href="/dining-cruises/weekend-brunch-cruise/">
    <img src="/img/brunch-plate.jpg" alt="A brunch plate on a cruise table">
    <span class="shade"></span>
    <span class="dest-copy">
      <h2>Brunch</h2>
      <p>2 hours · buffet · all ages</p>
      <span class="btn">View brunch</span>
    </span>
  </a>
  <a href="/holiday-cruises/">
    <img src="/img/holiday-lights.jpg" alt="Boats with holiday lights on the water at night">
    <span class="shade"></span>
    <span class="dest-copy">
      <h2>Seasonal</h2>
      <p>Parade of Lights, Thanksgiving, New Year’s Eve</p>
      <span class="btn">View seasonal</span>
    </span>
  </a>
</section>
<section class="band sail-band">
  <div class="wrap">
    <h2 class="center">Cruises on the lakes</h2>
    <div class="sail-grid">
      <a class="sail-card" href="/dining-cruises/dinner/">
        <img src="/img/dinner-spread.jpg" alt="Several dinner plates and wine glasses on a table">
        <div>
          <h3>Premier Seattle Dinner Cruise</h3>
          <p>Wednesdays to Saturdays. Summer 7:00 to 9:30 pm. Winter 6:00 to 8:30 pm.</p>
          <span>View cruise</span>
        </div>
      </a>
      <a class="sail-card" href="/dining-cruises/weekend-brunch-cruise/">
        <img src="/img/brunch-table.jpg" alt="A brunch table set with food">
        <div>
          <h3>Weekend Brunch Cruise</h3>
          <p>2 hours, brunch buffet, all ages.</p>
          <span>View cruise</span>
        </div>
      </a>
      <a class="sail-card" href="/dining-cruises/supper/">
        <img src="/img/supper-table.jpg" alt="A supper table set aboard a Waterways yacht">
        <div>
          <h3>Sunday Supper Cruise</h3>
          <p>2 hours, dinner buffet, all ages, select Sundays.</p>
          <span>View cruise</span>
        </div>
      </a>
      <a class="sail-card" href="/holiday-cruises/holiday-sights-cruise/">
        <img src="/img/holiday-lights.jpg" alt="Boats with holiday lights on the water at night">
        <div>
          <h3>Holiday Sights Cruise</h3>
          <p>Parade of Lights, from the water.</p>
          <span>View cruise</span>
        </div>
      </a>
    </div>
  </div>
</section>
<section class="band band-navy fleet-band">
  <div class="wrap">
    <p class="eyebrow">Private events and charters</p>
    <h2>The yacht, for your guests.</h2>
    <p class="measure">Weddings, corporate evenings, and celebrations aboard Emerald Star, Olympic Star, Destiny, and Sightseer. Departing Fishermen’s Terminal.</p>
    <p><a class="btn btn-light" href="/private-events/">Plan a private event</a></p>
    <div class="fleet-row">
      <a href="/fleet/theemeraldstar/"><img src="/img/emerald-sunset.jpg" alt="Emerald Star on the water at sunset"><h3>Emerald Star</h3><p>105 ft</p></a>
      <a href="/fleet/theolympicstar/"><img src="/img/olympic-skyline.jpg" alt="Olympic Star with the Seattle skyline"><h3>Olympic Star</h3><p>90 ft</p></a>
      <a href="/fleet/thedestiny/"><img src="/img/spring-docked.jpg" alt="A Waterways yacht docked beside the lake"><h3>Destiny</h3><p>64 ft</p></a>
      <a href="/fleet/the-sightseer/"><img src="/img/sightseer.jpg" alt="Sightseer on the lake"><h3>Sightseer</h3><p>Historic</p></a>
    </div>
  </div>
</section>
<section class="band">
  <div class="wrap">
    <h2 class="center">From our guests</h2>
    <div class="review-grid">{proof}</div>
  </div>
</section>
"""


def home_finder() -> str:
    party = "".join(f'<option value="{n}">{n}</option>' for n in range(2, 11))
    return f"""
<section class="hero finder-hero" style="background-image:url('/img/emerald-sunset.jpg')">
  <div class="hero-inner center">
    <p class="eyebrow">Lake Union · Lake Washington</p>
    <h1>Cruises on Seattle’s lakes.</h1>
    <p class="hero-sub">Dining cruises and private charters from Fishermen’s Terminal.</p>
  </div>
  <form class="find-bar" data-find>
    <label>Cruise
      <select name="cruise" required>
        <option value="dinner">Premier Dinner</option>
        <option value="brunch">Weekend Brunch</option>
        <option value="supper">Sunday Supper</option>
        <option value="seasonal">Seasonal cruises</option>
        <option value="private">Private charter</option>
      </select>
    </label>
    <label>Date
      <input name="date" type="date">
    </label>
    <label>Party
      <select name="party">
        <option value="">Guests</option>
        {party}
      </select>
    </label>
    <button class="btn" type="submit">Find a cruise</button>
  </form>
</section>
"""




def form_shell(intro: str, fields: str, submit: str) -> str:
    return f"""
<div class="form-card">
  <p class="form-note">Preview only. This form is not connected to Waterways, to an email service, or to a booking system.</p>
  {intro}
  <form data-preview id="proposal" novalidate>
    {fields}
    <button class="btn" type="submit">{submit}</button>
    <p class="form-note" data-form-note hidden></p>
  </form>
</div>
"""


def rfp_body() -> str:
    fields = """
<label>Type of event
  <select name="event-type" required>
    <option value="">Select</option>
    <option>Corporate</option><option>Wedding</option><option>Rehearsal Dinner</option>
    <option>School</option><option>Special Occasion</option><option>Memorial</option><option>Other</option>
  </select>
</label>
<label>Company, organization, or party name <input name="org" required></label>
<label>First name <input name="first" required autocomplete="given-name"></label>
<label>Last name <input name="last" required autocomplete="family-name"></label>
<label>Email <input name="email" type="email" required autocomplete="email"></label>
<label>Phone <input name="phone" type="tel" required autocomplete="tel"></label>
<label>Preferred date <input name="date" type="date" required></label>
<label>Estimated guests <input name="guests" type="number" min="1" required></label>
<label>Time window
  <select name="time" required>
    <option value="">Select</option>
    <option>Afternoon, back by 3:00 PM</option>
    <option>Evening, boarding from 5:30 PM</option>
  </select>
</label>
<label>Budget <input name="budget" required></label>
<label>How did you find us?
  <select name="source">
    <option>Internet search</option><option>Online ads</option><option>Return customer</option>
    <option>Referral</option><option>Social media</option><option>Email</option><option>Brochure</option>
    <option>Concierge</option><option>Industry event</option><option>Other</option>
  </select>
</label>
<label>Accommodations
  <select name="hotel">
    <option>No</option>
    <option>Not sure</option>
    <option>Yes. Silver Cloud</option>
  </select>
</label>
<label>Referral or promo code <input name="promo"></label>
<label>Comments <textarea name="comments"></textarea></label>
"""
    downloads = """
<h2>Published flyers</h2>
<ul>
<li><a href="/files/2026-Private-Catering-Menus.pdf">2026 catering menus</a></li>
<li><a href="/files/2026-Wedding-Packages-Flyer.pdf">2026 upper deck and buyout / wedding packages flyer</a></li>
<li><a href="/files/2027-Private-Charter-Flyer.pdf">2027 Private Charter Flyer</a></li>
</ul>
"""
    return form_shell("<p>Tell us about the event. This preview does not send it.</p>", fields, "Review proposal") + downloads


def contact_body(page: dict) -> str:
    fields = """
<label>Name <input name="name" required autocomplete="name"></label>
<label>Email <input name="email" type="email" required></label>
<label>Phone <input name="phone" type="tel"></label>
<label>Message <textarea name="message" required></textarea></label>
"""
    return """
<div class="facts">
  <div class="fact"><span>Homeport, as published</span>Fishermen's Terminal Dock 9, 3919 18th Ave W, Seattle WA 98119</div>
  <div class="fact"><span>Office and mailing, as published</span>4005 20th Ave W, Suite 228, Seattle WA 98199. By appointment.</div>
  <div class="fact"><span>Phone</span><a href="tel:2062232060">(206) 223-2060</a></div>
  <div class="fact"><span>Email</span><a href="mailto:contact@waterwayscruises.com">contact@waterwayscruises.com</a><br><a href="mailto:events@waterwayscruises.com">events@waterwayscruises.com</a></div>
</div>
<p class="center"><a class="map-link" href="https://www.google.com/maps/search/?api=1&amp;query=3919+18th+Ave+W+Seattle+WA+98119">Map to Dock 9</a></p>
""" + form_shell("<p>Questions about a cruise or a visit.</p>", fields, "Review message")


def careers_form() -> str:
    fields = """
<label>Name <input name="name" required></label>
<label>Email <input name="email" type="email" required></label>
<label>Phone <input name="phone" type="tel"></label>
<label>Position <input name="role" required></label>
<label>Note <textarea name="note"></textarea></label>
"""
    return "<h2>Employment application</h2>" + form_shell(
        "<p>Send a resume to the address on the job. This preview does not email it.</p>",
        fields,
        "Review application",
    )


def nonprofit_form() -> str:
    fields = """
<label>Organization <input name="org" required></label>
<label>Contact name <input name="name" required></label>
<label>Email <input name="email" type="email" required></label>
<label>Phone <input name="phone" type="tel"></label>
<label>501(c)(3) status <select name="status" required><option value="">Select</option><option>We can provide proof</option><option>Not yet</option></select></label>
<label>Event idea <textarea name="idea" required></textarea></label>
"""
    return form_shell("<p>Nonprofit Partner Program application. Preview only.</p>", fields, "Review application")


def gift_body() -> str:
    fields = """
<label>Demo amount, USD <input name="amount" type="number" min="1" required></label>
<p class="quiet">Enter an amount. Nothing is charged.</p>
<label>Recipient name <input name="to" required></label>
<label>Your email <input name="email" type="email" required></label>
<label>Note <textarea name="note"></textarea></label>
"""
    return """
<p class="measure">A gift card toward a public Waterways cruise in Seattle. Gift cards apply to cruise tickets, not to purchases on board.</p>
<p>Gift cards, as the FAQ states, apply to public cruise tickets and are not valid for onboard purchases.</p>
""" + form_shell("<p>Demo gift purchase. No code is issued.</p>", fields, "Review gift card") + """
<section class="band"><div class="wrap book" data-book>
<p class="quiet">Review the gift card here. No payment fields.</p>
</div></section>
"""


def calendar_body() -> str:
    rows = [
        ("Premier Seattle Dinner Cruise", "Wednesdays to Saturdays. Summer from May 1, 7:00 to 9:30 pm. Winter from October 1, 6:00 to 8:30 pm.", "/dining-cruises/dinner/"),
        ("Weekend Brunch Cruise", "2 hours, brunch buffet, all ages.", "/dining-cruises/weekend-brunch-cruise/"),
        ("Sunday Supper Cruise", "2 hours, dinner buffet, all ages, select Sundays.", "/dining-cruises/supper/"),
        ("Taco Thursday", "2 hours. Departure as printed on that page.", "/taco-thursday-seattle-lakes-cruise-tour/"),
        ("Thanksgiving Day Cruise", "November 26, as published.", "/thanksgiving-day-cruise/"),
        ("Holiday Dinner Cruise", "Parade of Lights.", "/holiday-cruises/holiday-dinner-cruise/"),
        ("Holiday Sights Cruise", "Parade of Lights.", "/holiday-cruises/holiday-sights-cruise/"),
        ("Christmas Eve Dinner Cruise", "December 24.", "/holiday-cruises/christmas-eve-dinner-cruise/"),
        ("New Year's Eve Dinner Cruise", "December 31, ages 16+.", "/holiday-cruises/new-years-eve-dinner-cruise/"),
        ("New Year's Eve Party Cruise", "December 31, ages 21+.", "/new-years-eve-party-cruise/"),
        ("Wine Pairing Cruise", "March 4, as published.", "/willamette-valley-vineyards-wine-pairing-cruise/"),
    ]
    links = "\n".join(f'<a href="{href}"><strong>{esc(name)}</strong><br>{esc(blurb)}</a>' for name, blurb, href in rows)
    return f"""
<p class="measure center">Date-first entry for public dining. Pick a cruise, then continue in the demo booking path on that page. No cell is marked sold out, and no live inventory is loaded.</p>
<div class="calendar-list">{links}</div>
"""


def memberships_body(page: dict) -> str:
    text = ""
    for _, raw in page["sections"]:
        text += " " + clean_text(raw)
    text = dedupe_doubled(text)
    parts = text.split("( $314.52 value)")
    if len(parts) >= 3:
        tail = parts[-1]
        star = tail.find("*Can be used")
        terms = tail[star:] if star >= 0 else ""
        text = parts[0] + "( $314.52 value)" + parts[1] + terms
    return f"""
<h2>Unwind membership</h2>
<p>{esc(text)}</p>
<p>This page describes the published membership. It is not a checkout.</p>
"""


def gallery_body() -> str:
    shots = [
        ("emerald-sunset.jpg", "Emerald Star on the water at sunset"),
        ("olympic-skyline.jpg", "Olympic Star with the Seattle skyline and Space Needle"),
        ("dinner-plate.jpg", "A plated dinner from a Waterways dining cruise"),
        ("dinner-spread.jpg", "Several dinner plates and wine glasses on a table"),
        ("brunch-table.jpg", "A brunch table set with food"),
        ("brunch-juice.jpg", "A hand holding a glass of orange juice"),
        ("gallery-01.jpg", "Flowers in a vase on a table"),
        ("gallery-02.jpg", "A plated dish from a Waterways event"),
        ("gallery-03.jpg", "A plate of food on a dining table"),
        ("gallery-04.jpg", "Guests seated together aboard a yacht"),
        ("gallery-05.jpg", "A couple standing at the rail"),
        ("gallery-06.jpg", "A bridge crossing above the water, seen from the cruise"),
        ("wedding-ceremony.jpg", "A ceremony on the deck with a harp"),
        ("corporate-table.jpg", "Colleagues seated at a table during a private event"),
        ("holiday-lights.jpg", "Boats with holiday lights on the water at night"),
        ("christmas-table.jpg", "A holiday table with roses, ornaments, and glassware"),
        ("bartender.jpg", "A bartender shaking a cocktail behind the bar"),
        ("sightseer.jpg", "Sightseer on the lake"),
    ]
    figs = "\n".join(
        f'<figure><img src="/img/{fn}" alt="{esc(alt)}" width="1200" height="800"></figure>'
        for fn, alt in shots
    )
    return f'<div class="gallery">{figs}</div>'


def journal_hub(pages: dict) -> str:
    posts = [p for p in KEEP if p.startswith("/blog/")]
    cards = []
    for path in posts:
        page = pages[path]
        h1 = h1_for(path, page)
        lead = ""
        for heading, raw in page["sections"]:
            text = clean_text(raw)
            if text:
                lead = text[:220].rsplit(" ", 1)[0] + "…"
                break
        cards.append(f'<article class="card"><h3><a class="title" href="{path}">{esc(h1)}</a></h3><p>{esc(lead)}</p></article>')
    return f"<div class=\"grid cols-2\">{''.join(cards)}</div>"


def nonprofit_hold(text_html: str) -> str:
    return """
<p>Waterways Cruises and Events is honored to support local nonprofits that create a positive impact in our community.</p>
<p>Registered 501(c)(3) organizations can open an application. Proof of nonprofit status is part of eligibility.</p>
<p><a class="btn" href="/nonprofit-partner-program-application/">Open the application</a></p>
"""


def page_body(path: str, pages: dict) -> tuple[str, str]:
    page = pages[path]
    h1 = h1_for(path, page)
    extra = ""
    if path == "/":
        main = '<main id="main">' + home_finder() + home_body() + "\n</main>"
        return main, extra
    if path == "/faqs/":
        faq, schema, count = faq_html(pages)
        extra = schema
        top = hero_block(path, h1, "Policies, tickets, accessibility, food, gift cards, and private events.", '<a class="btn btn-light" href="/contact-us/">Contact</a><a class="btn btn-line" href="tel:2062232060">Call</a>')
        main = f'<main id="main">{top}<section class="band"><div class="wrap prose">{faq}<p><a href="/blog/whats-the-difference-between-boarding-time-and-departure-time/">Boarding time and departure time</a></p></div></section>{closing(path)}</main>'
        return main, extra
    actions = '<a class="btn btn-light" href="/dining-cruises/">Dining Cruises</a><a class="btn btn-line" href="/private-events/">Private Charters</a>'
    if kind_of(path) == "dining":
        actions = '<a class="btn btn-light" href="#book">Book this cruise</a><a class="btn btn-line" href="tel:2062232060">Call</a>'
    if kind_of(path) in {"private", "sail"}:
        actions = '<a class="btn btn-light" href="/request-a-proposal/">Request a Proposal</a><a class="btn btn-line" href="tel:2062232060">Call</a>'
    lede = esc(meta_for(path, page, h1)[:220])
    top = hero_block(path, esc(h1), lede, actions)
    inner = ""
    if path == "/request-a-proposal/":
        inner = rfp_body()
    elif path == "/contact-us/":
        inner = contact_body(page)
    elif path == "/gift-cards/":
        inner = gift_body()
    elif path == "/cruise-calendar/":
        inner = calendar_body()
    elif path == "/memberships/":
        inner = memberships_body(page)
    elif path == "/gallery/":
        inner = gallery_body()
    elif path == "/about-us/blog/":
        inner = journal_hub(pages)
    elif path == "/nonprofit-partner-program/":
        inner = nonprofit_hold("")
    elif path == "/nonprofit-partner-program-application/":
        inner = nonprofit_form()
    elif path == "/privacy-policy/":
        prose = section_html(path, page, pages)
        inner = prose
    else:
        inner = section_html(path, page, pages)
        if path == "/careers/":
            inner += careers_form()
        if path == "/fleet/thedestiny/":
            pass
    book = ""
    if path in DINING_BOOK:
        book = book_widget(h1, dinner=path == "/dining-cruises/dinner/")
    if path in SAIL:
        inner += '<p>These sailgating cruises are full-vessel buyouts. Request a proposal or call.</p>'
    main = f'<main id="main">{top}<section class="band"><div class="wrap prose">{inner}</div></section>{book}{closing(path)}</main>'
    if path.startswith("/blog/"):
        extra = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Article","headline":{json_str(h1)},"publisher":{{"@type":"Organization","name":"Waterways Cruises & Events"}},"mainEntityOfPage":"{HOST}{path}"}}</script>'
    return main, extra


def write_page(path: str, html_doc: str) -> None:
    if path == "/":
        dest = ROOT / "index.html"
    elif path.endswith(".html"):
        dest = ROOT / path.lstrip("/")
    else:
        dest = ROOT / path.strip("/") / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html_doc)


def redirect_page(src: str, dest: str, reason: str) -> None:
    canonical = HOST + dest
    body = f"""
<main id="main" class="band">
  <div class="wrap measure center">
    <h1>This address has moved</h1>
    <p>{esc(reason)}</p>
    <p><a class="btn" href="{dest}">Continue</a></p>
  </div>
</main>
"""
    doc = layout(src, "Moved | Waterways Cruises & Events", reason, body)
    doc = doc.replace(f'href="{HOST}{src if src != "/" else "/"}"', f'href="{canonical}"', 1)
    # force canonical
    doc = re.sub(r'<link rel="canonical" href="[^"]+">', f'<link rel="canonical" href="{canonical}">', doc, count=1)
    doc = doc.replace("</head>", f'<meta http-equiv="refresh" content="0; url={dest}"></head>', 1)
    write_page(src, doc)


def seo_pages() -> None:
    facts = (ROOT / "seo-aeo-compare-facts.md").read_text().splitlines()
    rows = []
    for line in facts:
        if not line.startswith("| F"):
            continue
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cols) < 4:
            continue
        rows.append(cols)
    tr = "\n".join(
        f"<tr><td>{esc(c[0])}</td><td>{esc(c[1])}</td><td>{esc(c[2])}</td><td>Not scored. The review pages exist. This file does not assign a prototype score.</td></tr>"
        for c in rows
    )
    compare_body = f"""
<main id="main">
  <section class="page-hero"><div class="wrap"><p class="eyebrow">DPA Branding</p><h1>SEO / AEO compare</h1>
  <p>Live checklist beside this prototype. The prototype column has no score. No traffic or ranking promise is made.</p></div></section>
  <section class="band"><div class="wrap">
    <p><a href="/Waterways-SEO-Summary.html">Summary</a> · <a href="/Waterways-SEO-InDepth.html">In depth</a> · <a href="/Waterways-SEO-Gap-Report.html">Gap report</a></p>
    <div style="overflow-x:auto">
    <table>
      <thead><tr><th>ID</th><th>Check</th><th>Live fact</th><th>Prototype</th></tr></thead>
      <tbody>{tr}</tbody>
    </table>
    </div>
    <h2>Why it matters</h2>
    <p>The live site scored 38 of 64 on the house rubric dated 2026-11-06. That number describes the current site. It is not a forecast, and it is not a score for this prototype.</p>
  </div></section>
</main>
"""
    style = "<style>table{border-collapse:collapse;width:100%;font-size:1rem}td,th{border-top:1px solid rgba(8,9,14,.12);text-align:left;padding:10px;vertical-align:top}th{font-family:Montserrat,sans-serif;font-weight:400}</style>"
    write_page("/Waterways-SEO-AEO-Compare.html", layout("/Waterways-SEO-AEO-Compare.html", "SEO / AEO Compare | Waterways Cruises & Events", "Live facts beside an unscored prototype column.", compare_body, style))

    summary = """
<main id="main"><section class="page-hero"><div class="wrap"><p class="eyebrow">For Hilton Smith</p><h1>SEO summary</h1>
<p>Plain language. No traffic promise and no ranking promise. The prototype is not scored.</p></div></section>
<section class="band"><div class="wrap prose">
<ol>
<li>The live checklist is 38 of 64, measured 2026-11-06. This prototype does not replace that number.</li>
<li>Guests see two doors: a public dining cruise, or a private charter proposal.</li>
<li>Contact and MOHAI each have one address on this site.</li>
<li>The homepage has a text heading.</li>
<li>Search results, promo leftovers, and the booking utility are not pages here.</li>
</ol>
<p><a href="/Waterways-SEO-AEO-Compare.html">Open the compare ledger</a></p>
</div></section></main>
"""
    write_page("/Waterways-SEO-Summary.html", layout("/Waterways-SEO-Summary.html", "SEO Summary | Waterways Cruises & Events", "Five plain-language notes for Hilton Smith. The prototype is not scored.", summary))

    depth = """
<main id="main"><section class="page-hero"><div class="wrap"><h1>SEO in depth</h1><p>The live picture, and what this static site carries. It is not a prototype score.</p></div></section>
<section class="band"><div class="wrap prose">
<h2>Technical</h2>
<p>Live baseline from the house audit: area A 10 of 16. The live site had an indexable search route and duplicate URLs. This site has no search route, one contact URL, and one MOHAI URL.</p>
<h2>On-page</h2>
<p>Live area B 8 of 16. The four sailgating pages here each have their own description. The homepage has a text H1.</p>
<h2>Local and NAP</h2>
<p>Live area C 9 of 12. Footer phone, email, Dock 9, and the office address are on every page. Each cruise keeps the departure named on that cruise.</p>
<h2>Schema and AEO</h2>
<p>Live area D 9 of 16. Product self-review stars are not used. FAQPage is present on the FAQ. Organization is present without a street address.</p>
<h2>Two paths</h2>
<p>Public dining and private charter inquiry are separate journeys. Sailgating uses the proposal path.</p>
<h2>Assets</h2>
<p>Images are the live library, resized down, with alt text. The 3.9 MB Fremont lake-union.jpg file is not shipped. Stock-named Getty and iStock files are not shipped.</p>
<h2>Supplied audit claims</h2>
<p>The November 3 audit is a third-party record. Video CLS 0.61 and a 66.1 MB aggregate are third-party claims. The live Lighthouse 12 lab notes are the baseline: home performance 60, LCP 4.4 s, TBT 940 ms, CLS 0.052, 4,667 KiB; brunch performance 51, LCP 8.6 s, TBT 600 ms, CLS 0.054. This page does not invent a prototype lab score.</p>
</div></section></main>
"""
    write_page("/Waterways-SEO-InDepth.html", layout("/Waterways-SEO-InDepth.html", "SEO In Depth | Waterways Cruises & Events", "Sourced live findings and unscored prototype design notes.", depth))

    gap = """
<main id="main"><section class="page-hero"><div class="wrap"><h1>Gap report</h1><p>Live gaps, what this site changes, and what waits. Nothing here is marked pass.</p></div></section>
<section class="band"><div class="wrap prose">
<h2>On this site</h2>
<ul>
<li>Two doors on the first screen.</li>
<li>Text H1 on the homepage. One H1 on privacy.</li>
<li>Unique titles and descriptions, including the four sailgating pages.</li>
<li>No Product self-review and no star display.</li>
<li>Each cruise keeps the departure named on that page.</li>
<li>Promo and test URLs are not pages.</li>
</ul>
<h2>Later</h2>
<ul>
<li>Server redirects for old addresses.</li>
<li>A street address in schema once the office and dock lines are settled.</li>
<li>Offer details on each cruise.</li>
<li>Founder profiles in schema.</li>
<li>Article dates.</li>
<li>A booking system. None is embedded.</li>
</ul>
<p>Live rubric: 38 of 64. Prototype rubric: not scored.</p>
</div></section></main>
"""
    write_page("/Waterways-SEO-Gap-Report.html", layout("/Waterways-SEO-Gap-Report.html", "SEO Gap Report | Waterways Cruises & Events", "Live gaps, review-build changes, and launch-only items. Prototype not scored.", gap))


def not_found() -> None:
    body = """
<main id="main" class="band">
  <div class="wrap measure center">
    <p class="eyebrow">404</p>
    <h1>That page is not here</h1>
    <p>The address is missing. Try one of these.</p>
    <div class="btn-row center">
      <a class="btn" href="/">Home</a>
      <a class="btn btn-ghost" href="/dining-cruises/">Dining Cruises</a>
      <a class="btn btn-ghost" href="/private-events/">Private Events</a>
      <a class="btn btn-ghost" href="/request-a-proposal/">Request a Proposal</a>
      <a class="btn btn-ghost" href="/contact-us/">Contact</a>
      <a class="btn btn-ghost" href="/faqs/">FAQs</a>
    </div>
  </div>
</main>
"""
    write_page("/404.html", layout("/404.html", "Page not found | Waterways Cruises & Events", "That page is not here.", body))


def sitemap(paths: list[str]) -> None:
    urls = []
    for path in paths:
        loc = HOST + ("/" if path == "/" else path)
        urls.append(f"  <url><loc>{loc}</loc></url>")
    xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n" + "\n".join(urls) + "\n</urlset>\n"
    (ROOT / "sitemap.xml").write_text(xml)
    (ROOT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\nDisallow: /edit/\nDisallow: /fhbr-console/\nDisallow: /cdn-cgi/\n\nSitemap: https://waterwayscruises.clientreview.co/sitemap.xml\n"
    )
    (ROOT / "CNAME").write_text("waterwayscruises.clientreview.co\n")
    (ROOT / "_config.yml").write_text(
        "title: Waterways Cruises & Events review\n"
        "exclude:\n"
        "  - seo-aeo-compare-facts.md\n"
        "  - research\n"
        "  - references\n"
        "  - tools\n"
        "  - SCOPE.md\n"
        "  - PROJECT_GUIDE.md\n"
        "  - README.md\n"
        "  - NOTES.md\n"
        "  - private\n"
    )


def brand_page() -> None:
    body = r"""
<main id="main">
  <header class="cover"><div class="cover-card">
    <img src="/img/logo-lockup.png" alt="Waterways Cruises and Events">
    <p class="eyebrow">Visual identity standards</p>
    <h1>Waterways Cruises &amp; Events</h1>
    <p class="cover-kicker">Brand Guide</p>
    <p class="cover-tagline">For An Unforgettable Experience, Just Add Water®</p>
    <p class="cover-credit">November 9, 2026<br>Prepared by DPA Branding<br><a href="mailto:mike@dpabranding.com">mike@dpabranding.com</a></p>
  </div></header>
  <div class="download-bar wrap">
    <a class="btn" href="/Waterways-Brand-Standards.pdf" download>Download Brand Standards PDF</a>
    <p>Each logo file has its own download below. There is no combined asset pack.</p>
  </div>
  <section class="band" id="logo"><div class="wrap">
    <p class="section-label">Section 01</p>
    <h2>Logo</h2>
    <p class="lede">Two files: the full lockup, and the gold mark. Use them whole.</p>
    <div class="logo-grid">
      <figure class="tile tile-paper"><img src="/img/logo-lockup.png" alt="Full-color lockup on paper"><figcaption>Lockup on paper</figcaption></figure>
      <figure class="tile tile-white"><img src="/img/logo-lockup.png" alt="Full-color lockup on white"><figcaption>Lockup on white</figcaption></figure>
      <figure class="tile tile-navy"><img src="/img/logo-mark.png" alt="Gold mark on navy"><figcaption>Mark on navy</figcaption></figure>
      <figure class="tile tile-ink"><img src="/img/logo-lockup.png" alt="Full-color lockup on ink"><figcaption>Lockup on ink</figcaption></figure>
    </div>
    <p><a class="btn" href="/img/logos/waterways-logo-lockup.png" download>Download lockup PNG</a> <a class="btn btn-ghost" href="/img/logos/waterways-logo-mark.png" download>Download mark PNG</a></p>
    <div class="grid cols-2">
      <div><h3>Clear space</h3><p>Keep at least the height of the gold waves clear on every side. Do not crowd the mark with type.</p></div>
      <div><h3>Minimum size</h3><p>Do not display the full lockup below 160 pixels wide. The mark file is 187 by 147 pixels. Do not scale it up.</p></div>
    </div>
    <h3>Do</h3>
    <ul>
      <li>Use the lockup on paper, white, or ink.</li>
      <li>Use the gold mark when the ground is navy.</li>
      <li>Leave the files whole.</li>
    </ul>
    <h3>Do not</h3>
    <ul>
      <li>Do not stretch, rotate, recolor, outline, or add a shadow.</li>
      <li>Do not place the lockup on a busy photograph without a solid field.</li>
      <li>Do not redraw the waves or set the name in a different face.</li>
    </ul>
  </div></section>
  <section class="band band-paper" id="color"><div class="wrap">
    <p class="section-label">Section 02</p>
    <h2>Color</h2>
    <p class="lede">Navy, water, mist, paper, ink, and the gold of the mark.</p>
    <div class="swatches">
      <div class="swatch" style="background:#0e3060;color:#fff"><strong>Navy</strong><span>#0e3060</span></div>
      <div class="swatch" style="background:#a5c2c9;color:#000"><strong>Water</strong><span>#a5c2c9</span></div>
      <div class="swatch" style="background:#89adc5;color:#000"><strong>Mist</strong><span>#89adc5</span></div>
      <div class="swatch" style="background:#f5f7f9;color:#08090e"><strong>Paper</strong><span>#f5f7f9</span></div>
      <div class="swatch" style="background:#08090e;color:#fff"><strong>Ink</strong><span>#08090e</span></div>
      <div class="swatch" style="background:#ffffff;color:#000;border:1px solid #d7d3d3"><strong>White</strong><span>#ffffff</span></div>
      <div class="swatch" style="background:#000000;color:#fff"><strong>Black</strong><span>#000000</span></div>
      <div class="swatch" style="background:#c0995e;color:#08090e"><strong>Gold</strong><span>#c0995e</span></div>
    </div>
    <p>Gold is jewelry: a rule, a small label, the mark. It is not body text. Navy carries buttons and headings. Water and mist are grounds, not text on white.</p>
  </div></section>
  <section class="band" id="type"><div class="wrap">
    <p class="section-label">Section 03</p>
    <h2>Typography</h2>
    <p class="lede">Headlines and text are Manrope. Headlines are bold. Text is regular.</p>
    <p class="display-sample">Dining cruises and private events on Seattle's lakes.</p>
    <p class="body-sample">Experience Seattle from a new perspective with Waterways Cruises &amp; Events. Based in Fishermen's Terminal, we offer experiences on Lake Union and Lake Washington, from public dining cruises to fully private charters and events.</p>
    <p>Body text is 18px on a phone and 20px on a wide screen. Buttons use Manrope.</p>
  </div></section>
  <section class="band band-paper" id="buttons"><div class="wrap">
    <p class="section-label">Section 04</p>
    <h2>Buttons</h2>
    <p class="lede">Navy fill with white type. The hover state inverts. Every target is at least 48 pixels tall. On a phone, a pair of actions stacks full width.</p>
    <p class="btn-row"><a class="btn" href="#buttons">Primary action</a><a class="btn btn-ghost" href="#buttons">Secondary action</a></p>
    <div class="tile tile-navy" style="padding:24px;margin-top:18px"><a class="btn btn-light" href="#buttons">On navy</a></div>
  </div></section>
  <section class="band" id="voice"><div class="wrap prose">
    <p class="section-label">Section 05</p>
    <h2>Voice and tone</h2>
    <p>The line is “For An Unforgettable Experience, Just Add Water®”. Write in sentence case. Sound like a host on the lake: specific, calm, and hospitable.</p>
    <p>Say dining cruise, private charter, yacht, Lake Union, Lake Washington, and Fishermen’s Terminal. Keep menus in menu language, with the dietary tags the kitchen published.</p>
    <p>Do not claim the company is the only dining cruise in the city. Do not print star ratings. Do not invent a guest count, a season year, or a reply window.</p>
    <p>No emoji. No exclamation stacks. No discount lead.</p>
  </div></section>
  <section class="band band-paper" id="usage"><div class="wrap prose">
    <p class="section-label">Section 06</p>
    <h2>Usage</h2>
    <ul>
      <li>Use the photographs already on these pages. Do not caption them as agency photography.</li>
      <li>Do not add stock-named files.</li>
      <li>Do not generate images. Do not enlarge a file past its pixel size.</li>
      <li>The charter flyer keeps its printed title, 2027 Private Charter Flyer.</li>
      <li>Agency credit on client-facing pages is DPA Branding, mike@dpabranding.com.</li>
    </ul>
    <p class="credit-line">Prepared by DPA Branding · <a href="mailto:mike@dpabranding.com">mike@dpabranding.com</a></p>
  </div></section>
</main>
"""
    extra = """
<style>
.cover{min-height:calc(100vh - 80px);display:flex;align-items:center;justify-content:center;padding:32px 16px 48px}
.cover-card{width:min(920px,100%);background:#08090e;color:#f5f7f9;padding:40px 32px}
.cover-card img{width:min(440px,100%);height:auto;margin-bottom:24px}
.cover-kicker{font-family:Manrope,sans-serif;font-size:1.25rem;margin:8px 0}
.cover-tagline{color:#fff;font-size:1.15rem}
.cover-credit{color:#c5ced6}
.cover-credit a{color:#fff}
.section-label{letter-spacing:.16em;text-transform:uppercase;color:#0e3060;font-family:Manrope,sans-serif;font-size:14px}
.download-bar{display:flex;flex-wrap:wrap;gap:12px;align-items:center;padding:18px 0}
.logo-grid,.swatches{display:grid;grid-template-columns:1fr;gap:16px}
.tile{padding:28px 20px;margin:0}
.tile img{max-width:280px;height:auto}
.tile-paper{background:#f5f7f9}
.tile-white{background:#fff;border:1px solid rgba(8,9,14,.12)}
.tile-navy{background:#0e3060;color:#fff}
.tile-ink{background:#08090e;color:#fff}
.tile figcaption{margin-top:12px;font-size:.95rem}
.swatch{min-height:140px;padding:16px;display:flex;flex-direction:column;justify-content:flex-end;gap:4px}
.swatch span{font-size:.9rem}
.display-sample{font-family:Manrope,sans-serif;font-weight:700;font-size:clamp(2rem,4vw,3rem);line-height:1.15;letter-spacing:-.02em}
.body-sample{font-size:1.125rem;max-width:68ch}
@media(min-width:640px){.logo-grid,.swatches{grid-template-columns:1fr 1fr}}
@media(min-width:1024px){.swatches{grid-template-columns:1fr 1fr 1fr 1fr}}
@page { size: letter; margin: 0.7in; }
@media print {
  #proto-banner, .site-header, .site-footer, .phone-bar, .skip, .download-bar, .nav-toggle { display: none !important; }
  body { padding-top: 0 !important; padding-bottom: 0 !important; background: #fff; font-size: 11pt; }
  .cover { min-height: auto; break-after: page; display: flex; }
  .cover-card { margin-inline: auto; }
  .band { break-before: page; }
  .logo-grid, .swatches, .grid, .tile, .spec { break-inside: avoid; }
  .tile img, .cover-card img { max-height: 160px; width: auto; }
  .tile-navy img { max-height: 90px; }
}
</style>
"""
    doc = layout("/brand.html", "Waterways Cruises & Events — Brand Guide", "Brand standards taken from the live Waterways site CSS and the official logo files. Prepared by DPA Branding.", body, extra, "/img/logo-lockup.png")
    (ROOT / "brand.html").write_text(doc)


def main() -> None:
    pages = parse_source()
    missing = [p for p in KEEP if p not in pages]
    if missing:
        raise SystemExit("Missing source pages: " + ", ".join(missing))
    built = []
    for path in KEEP:
        page = pages[path]
        h1 = h1_for(path, page)
        body, extra = page_body(path, pages)
        og = "/img/" + HERO.get(path, ("hero-home.jpg", ""))[0]
        doc = layout(path, title_for(path, h1), meta_for(path, page, h1), body, extra, og)
        write_page(path, doc)
        built.append(path)
    redirects = [
        ("/about-us/contact-us/", "/contact-us/", "The contact page lives at one address."),
        ("/directions/mohai/", "/directionsports/mohai/", "MOHAI directions live with the other ports."),
        ("/about-us/privacy-policy/", "/privacy-policy/", "Privacy lives at one address."),
        ("/departure-ports/", "/directionsports/", "Departure ports live on the directions hub."),
        ("/corporate/", "/private-events/#corporate", "Corporate copy now sits inside Private Events."),
        ("/food-and-bar/dessert/", "/dining-cruises/dinner/#dessert-2020", "The 2020 dessert list is labeled on the dinner page and does not replace the current menu."),
        ("/blog/", "/about-us/blog/", "The journal hub is the sitemap address."),
        ("/blog/page/2/", "/about-us/blog/", "Journal pagination is not a separate page."),
        ("/blog/page/3/", "/about-us/blog/", "Journal pagination is not a separate page."),
        ("/about-us/blog/page/2/", "/about-us/blog/", "Journal pagination is not a separate page."),
        ("/about-us/blog/page/3/", "/about-us/blog/", "Journal pagination is not a separate page."),
        ("/dining-cruises/sunday-supper-cruise/", "/dining-cruises/supper/", "Sunday Supper already resolves to this address."),
    ]
    for src, dest, reason in redirects:
        redirect_page(src, dest, reason)
    not_found()
    seo_pages()
    brand_page()
    sitemap(built + ["/brand.html", "/Waterways-SEO-AEO-Compare.html", "/Waterways-SEO-Summary.html", "/Waterways-SEO-InDepth.html", "/Waterways-SEO-Gap-Report.html"])
    print(f"KEEP pages: {len(built)}")
    print(f"redirects: {len(redirects)}")


if __name__ == "__main__":
    main()
