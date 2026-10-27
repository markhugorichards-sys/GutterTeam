SITE = {
    "name": "The Gutter Team",
    "domain": "https://www.gutterteam.co.uk",
    "email": "hello@gutterteam.co.uk",
    "region": "Farnborough, Fleet, Camberley, Farnham and the surrounding towns",
    "web3forms_key": "f03e6971-acd6-4945-9fe1-6ba1ce434425",
    "indexnow_key": "4f9c2e7a1b8d4c6e9a3f5b7d2e1c8a6f",
    # Paste the Google Business Profile "Ask for reviews" link here once the
    # profile is verified. /review then forwards straight to it.
    "google_review_url": "",
    "operator": "HHR Holdings Ltd",
    "updated": "27 October 2026",
    "updated_iso": "2026-10-27",
}

# Typical market price bands (GBP, per visit, standard clear and downpipe check).
# Compiled from published 2026 UK price guides, with the South East uplift those
# guides describe. These are estimates for planning, not quotes.
PRICE_BANDS = [
    {"key": "terraced", "label": "Terraced house (2 storey)", "low": 65, "high": 100},
    {"key": "semi", "label": "Semi-detached house (2 storey)", "low": 80, "high": 125},
    {"key": "detached", "label": "Detached house (2 storey)", "low": 110, "high": 190},
    {"key": "bungalow", "label": "Bungalow or chalet bungalow", "low": 60, "high": 105},
    {"key": "three", "label": "Three-storey house or town house", "low": 140, "high": 250},
    {"key": "flat", "label": "Low-rise flats or maisonette block", "low": 150, "high": 400},
]
PRICE_ADDONS = [
    {"key": "conservatory", "label": "Conservatory or porch roof gutters", "low": 15, "high": 40},
    {"key": "extension", "label": "Rear extension or garage gutters", "low": 15, "high": 35},
    {"key": "fascia", "label": "Fascia and soffit wash at the same visit", "low": 40, "high": 100},
    {"key": "neglect", "label": "Not cleaned for 3+ years (heavy build-up)", "low": 15, "high": 50},
]
PRICE_SOURCES = [
    ["Fantastic Services: gutter cleaning cost guide (2026)", "https://www.fantasticservices.com/cost-guides/cleaning/gutter-cleaning/"],
    ["MyBuilder: gutter cleaning costs", "https://www.mybuilder.com/fascias-soffits-guttering/price-guides/gutter-cleaning-cost"],
    ["Trade2Base: gutter cleaning prices UK (2026)", "https://www.trade2base.com/blog/gutter-cleaning-costs-uk"],
    ["Pure Seal Services: gutter cleaning costs in the UK", "https://puresealservices.co.uk/gutter-cleaning-costs-in-the-uk-how-much-should-you-expect-to-pay-in-2025/"],
]

SERVICES = [
 {
  "slug": "gutter-cleaning", "name": "Gutter Cleaning", "short": "Full clearance of every gutter run, outlets checked, and photos before and after.",
  "title": "Gutter Cleaning in Farnborough, Fleet and Camberley",
  "desc": "Professional gutter cleaning across Farnborough, Fleet, Camberley, Farnham and nearby towns. Every run cleared, downpipes checked, and photos sent after the visit.",
  "lead": "Every gutter run on the property is cleared, including the short runs on bays, porches, extensions and dormers that are easy to miss. Outlets and downpipes are checked for flow, and you get photos so you can see the result without climbing a ladder.",
  "body": """
## What a standard clean includes

- **All gutter runs**: main eaves, rear additions, bay and porch roofs, dormers and garages
- **Outlets and downpipes**: checked for flow, with blockages at the outlet cleared
- **Debris removed**: bagged and taken away, or left for your garden waste bin if you prefer
- **Condition notes**: leaking joints, loose brackets or sagging sections are pointed out, with photos
- **Before and after photos**: sent on the day

## How the gutters are reached

Most two-storey homes are cleaned from the ground using a high-reach gutter vacuum, usually with a camera on the pole so the inside of the gutter can be seen and photographed. Some properties need ladders or access equipment, such as three-storey houses, conservatory roofs or awkward valleys. The method is agreed with you before the visit.

## How often

Once a year suits most homes, ideally after the leaves have fallen in late November or December. Homes under trees, especially pines, oaks or horse chestnuts, usually need two visits. Each area page explains what local trees and roofs mean for your street.

## What it costs

See the [price guide](/advice/gutter-cleaning-cost/) for typical bands by property type and a quick estimator. The price is confirmed before any work is booked.
""",
  "faqs": [
   ["Do I need to be at home?", "Usually not. If the side gates can be left unlocked, the gutters can be cleared and photos sent afterwards."],
   ["What if a repair is needed?", "Any problem found during the clean is photographed and priced separately. Nothing extra is done without your agreement."],
   ["Will you clear the downpipes too?", "Outlets and the top of each downpipe are cleared and flow is checked. A fully blocked downpipe that needs rodding is quoted as downpipe unblocking."],
  ],
 },
 {
  "slug": "downpipe-unblocking", "name": "Downpipe Unblocking", "short": "Blocked downpipes cleared from the top or the shoe, then flow-tested.",
  "title": "Downpipe Unblocking in Farnborough and Surrounding Areas",
  "desc": "Blocked downpipe? Downpipes cleared and flow-tested across Farnborough, Fleet, Camberley and Farnham. Find out the likely cause and what clearing involves.",
  "lead": "A gutter that overflows at one corner, even when it looks clean, usually has a blocked downpipe. The pipe is cleared from the outlet or the shoe, then flushed so you can see water running freely.",
  "body": """
## Signs of a blocked downpipe

- Water spilling over the gutter next to the downpipe outlet during rain
- Gurgling, or water bubbling out of joints partway down the pipe
- A damp patch or green staining on the wall behind the pipe
- Plants growing out of the hopper or the top of the pipe

## Common causes locally

Pine needles are the main culprit in Camberley, Sandhurst, Yateley and the heath-side streets. They wash down and compact into a plug. Moss and roof grit from older concrete tile roofs is the next most common cause, followed by tennis balls and bird nests.

## What clearing involves

The blockage is located, cleared with rods or a jetting attachment, and the pipe is flushed and flow-tested. If the pipe discharges into an underground drain that is also blocked, you'll be told, because that's usually a drainage job rather than a gutter job.
""",
  "faqs": [
   ["Is a blocked downpipe urgent?", "It can be. Water pouring down a wall in heavy rain soaks brickwork and can cause damp inside. If you see water coming over the gutter next to the downpipe, get it looked at soon."],
   ["Can downpipe unblocking be done at the same visit as a clean?", "Yes. Most downpipe blockages are found and cleared during a standard gutter clean."],
  ],
 },
 {
  "slug": "gutter-repairs", "name": "Gutter Repairs", "short": "Leaking joints resealed, brackets replaced, sagging runs realigned.",
  "title": "Gutter Repairs: Leaking Joints, Brackets and Sagging Gutters",
  "desc": "Gutter repairs across Farnborough, Fleet, Camberley and Farnham: leaking joints resealed, brackets replaced and sagging runs realigned. Priced before work starts.",
  "lead": "Most gutter problems are small and cheap to fix if caught early: a dripping joint, a slipped bracket, a run that has lost its fall. Repairs are priced from photos where possible, and nothing is done without your agreement.",
  "body": """
## Common repairs

| Problem | Typical fix |
|---|---|
| Dripping joint or union | Clean and reseal, or replace the union |
| Sagging section | Add or replace brackets and reset the fall |
| Cracked or split section | Replace the section with a matching profile |
| Water missing the gutter | Adjust the gutter line or fit a deflector |
| Rusting cast iron joint | Clean back, seal and repaint |

## Matching parts

The area has gutters of every age, from Georgian cast iron in Farnham to 1980s uPVC in Southwood and 2000s systems at Elvetham Heath. Matching the profile (half round, square, ogee or deep flow) and the colour matters. Mismatched parts are a common cause of repeat leaks.

## Listed buildings and conservation areas

Like-for-like repairs don't change the appearance of a building. Changing material or profile on a listed building, or on a front elevation covered by an Article 4 direction, can need consent. Check with your council first. The area pages list the conservation areas in each town.
""",
  "faqs": [
   ["Repair or replace?", "If the run is straight and the brackets are sound, resealing and part replacement costs far less than a new system. Full replacement makes sense when the plastic has gone brittle or several sections are failing."],
   ["Can a repair be priced from photos?", "Often, yes. Attach a description in the enquiry form and the reply will say whether photos are enough or a look in person is needed."],
  ],
 },
 {
  "slug": "gutter-guards", "name": "Gutter Guards", "short": "Brush, mesh or foam guards fitted where they genuinely reduce clearing.",
  "title": "Gutter Guards: Do They Work, and Which Type Suits Your Trees?",
  "desc": "Honest advice on gutter guards for homes under trees in Farnborough, Fleet and Camberley: which types suit oak leaves and which struggle with pine needles.",
  "lead": "Gutter guards can cut the number of cleans a home under trees needs, but none of them makes a gutter maintenance-free. The right type depends on the trees over your roof.",
  "body": """
## Which guard for which trees

| Main debris | What tends to work | What struggles |
|---|---|---|
| Large broadleaf (oak, horse chestnut, sycamore) | Fine mesh covers, brush guards | Open foam inserts that hold wet leaves on top |
| Pine needles | Fine micro-mesh | Brush guards and coarse mesh, where needles thread through and lodge |
| Moss and roof grit | Little helps. Treat the roof moss instead | All types, because grit passes through |

## The honest trade-off

Guards keep large leaves out, but fine debris still gets in, and debris sitting on top of the guard has to be cleared. Under pine, which covers much of Camberley, Sandhurst, Yateley and Hawley, many guards need clearing almost as often as an open gutter does.

## Before fitting

Gutters are cleaned and any leaks fixed before guards go on. Fitting a guard over a dirty or leaking gutter seals the problem in.
""",
  "faqs": [
   ["Will guards mean I never need a clean?", "No. They reduce how often you need one, but guards and the gutter beneath still need checking, usually once a year."],
   ["Are guards worth it under pine trees?", "Only fine micro-mesh is reliably worth it under pine. Brush guards often trap needles."],
  ],
 },
 {
  "slug": "fascia-soffit-cleaning", "name": "Fascia and Soffit Cleaning", "short": "uPVC fascias, soffits and gutter faces washed back to clean white.",
  "title": "Fascia and Soffit Cleaning",
  "desc": "Fascia, soffit and gutter-face cleaning for uPVC rooflines across Farnborough, Fleet, Camberley and Farnham. Best booked with a gutter clean to save a second visit.",
  "lead": "Green algae and black streaks on fascias and the outside face of gutters are cosmetic, but they make a house look neglected. A wash at the same visit as a gutter clean is the cheapest way to do it.",
  "body": """
## What's cleaned

- uPVC fascia boards and soffits
- The outside face of the gutters and downpipes
- Bargeboards on gable ends

## When it's worth doing

Before selling or letting a property, after scaffolding has come down, or when green growth has built up on the shaded north side of the house.

## What it won't fix

Painted timber fascias that are flaking or soft need repair and redecoration, not washing. Any rotten timber found during the visit is pointed out.
""",
  "faqs": [
   ["Can this be done at the same time as gutter cleaning?", "Yes, and that's the most cost-effective way. See the price guide for typical add-on costs."],
  ],
 },
 {
  "slug": "annual-maintenance", "name": "Annual Maintenance Plans", "short": "Scheduled cleans each year, with a dated photo record.",
  "title": "Annual Gutter Maintenance Plans",
  "desc": "Scheduled annual or twice-yearly gutter cleaning for homes, landlords and managing agents across Farnborough, Fleet, Camberley and Farnham, with a dated photo record.",
  "lead": "If your home is under trees or you manage several properties, a scheduled plan takes gutter cleaning off your to-do list. Visits are booked at the right time of year for the trees over each roof, and each visit leaves a dated photo record.",
  "body": """
## How a plan works

1. Agree the visit pattern: once a year in winter, or twice a year (winter and spring) for homes under trees
2. Visits are booked in automatically, with a reminder before each one
3. Before and after photos and condition notes are sent after each visit
4. Any repair needed is priced separately, never added automatically

## Who it suits

- Homes under oak, horse chestnut or pine
- Landlords who need a maintenance record for each property
- Older owners who'd rather not chase a tradesperson each year
""",
  "faqs": [
   ["Can I cancel a plan?", "Yes. Plans are rolling and can be stopped at any time."],
  ],
 },
]

GUIDES = [
 {"slug": "gutter-cleaning-cost", "name": "Gutter cleaning cost and price estimator", "short": "Typical price bands for each property type, add-ons, and a quick estimate."},
 {"slug": "how-often-clean-gutters", "name": "How often should gutters be cleaned?", "short": "Frequency by tree type and roof, with local timing."},
 {"slug": "signs-gutters-need-cleaning", "name": "Signs your gutters need cleaning", "short": "What to look for from the ground before damage starts."},
 {"slug": "pine-needles-in-gutters", "name": "Pine needles in gutters", "short": "Why needles are the hardest local debris and what to do about them."},
 {"slug": "cast-iron-gutters", "name": "Cast iron gutters on period homes", "short": "Care, repair and consent for older properties."},
 {"slug": "skyvac-gutter-cleaning", "name": "Gutter vacuums explained", "short": "How ground-level vacuum cleaning works and when ladders are still needed."},
 {"slug": "gutter-cleaning-statistics-uk", "name": "Gutter cleaning data and local housing facts", "short": "Sourced figures on costs, rainfall, damage and local housing stock."},
]
