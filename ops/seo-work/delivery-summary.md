# Delivery summary

## Research
Source: Google Search Console via Windsor.ai, 27 Oct to 23 Nov 2026, sc-domain:gutterteam.co.uk. Facts:
- 1 click (brand), roughly 1,300 impressions. Average positions 30 to 75 for "gutter cleaning [town]".
- Homepage ranked for other towns because its title named them: "gutter cleaning camberley" split homepage (125 impr, pos 43.6) vs /areas/camberley/ (120, 35.8); "gutter cleaning fleet" homepage only (110, 32.2); "gutter cleaning frimley" homepage (40) and /services/ (30). "gutter cleaning farnborough" homepage pos 70.
- /areas/farnham/ drew install intent with no matching page: cast iron gutter installation farnham (18, pos 28), concrete gutters farnham (41, 56), upvc gutter installation farnham (14), gutter repairs farnham (24).
- "gutter cleaning near me" pos 13 to 15.
- SERP (OpenSEO, UK desktop, 24 Nov): local pack plus directories (Checkatrade, Yell, Yelp, Bark, Facebook) dominate; few dedicated local sites. Map pack needs the partner's real GBP.
Keyword volumes: not available (OpenSEO credits exhausted). No volumes are claimed anywhere.

## Audit
- 26 titles over 70 characters and 8 descriptions over 160.
- Homepage and /services/gutter-cleaning/ titles named several towns, competing with area pages.
- Price answer sat low on area pages; no question-form H2s.
- No Markdown representations; llms.txt had no navigation hints.
- Cost page Article schema lacked a description.

## Changes
- Homepage retargeted to Farnborough only: title, description, eyebrow, H1, answer-first lede with price bands, question H2s.
- Area pages (13): title "Gutter Cleaning [Town] [postcodes] | Local Prices", answer-first lede (semi and detached bands), question H2s for coverage, housing, trees, problems and price.
- /services/gutter-cleaning/ retitled to the service (no towns). Long titles/descriptions trimmed; brand suffix dropped automatically when a title exceeds 70 characters.
- New /services/gutter-replacement/ (per-metre costs by material, repair vs replace, concrete gutters, consent), sourced to MyJobQuote, Checkatrade, Pure Seal, less.co.uk, Bark. Added to the form's service list.
- Farnham and Aldershot area pages: repairs, replacement and concrete gutter section linking to the new page.
- Markdown discovery profile: /index.md equivalent for every indexable page generated from the same build, /sitemap.md content map, llms.txt navigation sentences and .md links, robots.txt and sitemap.xml comment hints, `<link rel="alternate" type="text/markdown">` on each page. vercel.json serves .md as text/markdown UTF-8 with X-Robots-Tag noindex so the HTML stays canonical.

## Release
Checks run locally: one H1 per page, JSON-LD parses, no broken internal links, every sitemap.md / llms.txt link resolves, titles ≤70, descriptions ≤160, no duplicate titles, mobile screenshots of home, Fleet and replacement pages. Lighthouse was not run this time.

## Follow-up
- Re-measure GSC around 22 Dec 2026: homepage vs area page split for Camberley, Fleet, Frimley; Farnham install queries landing on /services/gutter-replacement/.
- The partner Google Business Profile remains the main lever for the map pack.
