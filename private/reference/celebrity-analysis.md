# Celebrity Cruises homepage, design notes

Captured 2026-11-09 from https://www.celebritycruises.com/ with headless Chromium, a desktop Chrome user agent, and a second pass at 390 with an iPhone user agent. The site returned HTTP 200. Screenshots: `celebrity-1440.png`, `celebrity-390.png`, and the first-screen crops beside them. This file is reference only. It is excluded from the public site. Nothing here is copied onto Waterways.

## Header and nav

Desktop is a white bar under a full-width orange promo strip. The promo strip is one line of offer text, a navy “Book now” button, and a close control. Below it, the logo sits at the left, a single row of text links sits in the middle (Find a Cruise, Destinations, Ships, Discover Cruising, Loyalty, Offers, Manage Trip), and the right side holds “Need help?”, search, a heart, and Sign in. Links are small, navy, sentence case, with simple carets. No giant buttons in the link row.

On a phone the same promo strip stacks: offer text, then a navy Book now, then close. Under that, a white bar has a hamburger and search on the left, the logo centered, and an account icon on the right. The link row disappears into the menu.

## Hero

The first screen is a full-bleed photograph (a ship on open water), not a boxed image. Type is centered over the photo, white, in a bold geometric sans. A small white label sits above a very large headline, with a short line under it. An orange button sits in the middle of the photo. A countdown chip floats on the picture. A white booking bar overlaps the bottom edge of the photo and the next section: three fields (Cruising to, Leaving from, Leaving on) with small labels and placeholder values, and an orange “Search cruises” button on the right. The bar is a flat white card with a light shadow.

## Type

The computed family is Poppins (regular and semibold). Body is about 16px, regular. The hero headline is much larger, bold, tight, and mostly uppercase. Section titles below are large, uppercase, and split in two colors (navy, then orange). Small labels are uppercase and lighter. Letter-spacing is mostly normal. Case does the hierarchy more than a serif.

## Color

White page. Navy around `#002859` for text, the Book now button, and a later promo panel. A bright orange, about `#e87435`, for View Cruises, Search, Learn more, and half of the section titles. A pale blue band appears further down. Photography carries the rest of the color.

## Rhythm

The hero is one viewport. The booking bar breaks the bottom edge. Then a row of three tall destination photographs with almost no gap, type and an orange button sitting on the lower part of each photo. Then a full-width navy promo band. Then a section title and a horizontal run of cruise cards. Spacing between those major bands is generous; spacing inside the three-up photo row is tight. The page is dense with offers, but each band is one idea.

## Cards

Destination tiles are full-bleed photos, no border, white type, one orange button. Cruise cards lower on the page are white: a photo on top, then duration, name, ship, port, a price, and a text link. Corners are nearly square. Shadows are light, used on the search bar more than on the cards.

## Imagery

Crops are wide and full-bleed. People and ships fill the frame. The three destination tiles are equal height and edge to edge. Density is high: little empty margin inside a tile, more air between sections.

## Buttons

Primary actions are solid rectangles with almost no radius, white type, either navy or orange. Height is modest on their site (about 14px type). We do not copy that short height; Waterways keeps the 48px target.

## Promo bands

An orange announcement bar at the very top, a sale message painted on the hero, and a navy band mid-page with a second offer. These are marketing modules, not navigation.

## Footer

Not fully in the first screen. The visible chrome below the hero is the cookie bar: a white strip, small type, two text links, and a preferences control. The main footer continues the white ground and navy links.

## Phone versus desktop

The phone drops the link row, centers the logo, and keeps the promo and the hero type stacked and centered. The booking fields move under the hero instead of sitting in one horizontal bar. Buttons become full width. The same sections follow in one column.

## What Waterways should take, and what it must not

Take the structure: white header, logo and a short nav, a full-bleed photo, a large sans headline, a booking bar on the photo, three equal photo tiles, a private-event band, then a short list of sailings and a few reviews.

Do not take their orange, their sale language, their prices, their logos, their ship names, or their photographs. Waterways stays navy, ivory, and gold, with its own logo, lake photographs, and its own cruise names. The booking bar opens the existing Waterways demo, not a copied search.
