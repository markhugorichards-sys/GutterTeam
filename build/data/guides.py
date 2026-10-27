MET = "https://www.metoffice.gov.uk/research/climate/maps-and-data/location-specific-long-term-averages/u10hb5"
HSE = "https://www.hse.gov.uk/STATISTICS/fatals-overview.htm"
EHS13 = "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/445372/Chapter_1_Stock_profile.pdf"
AGEING = "https://www.ageing-better.org.uk/sites/default/files/2020-03/Accompanying-data-reference-report.pdf"
FANT = "https://www.fantasticservices.com/cost-guides/cleaning/gutter-cleaning/"
MYB = "https://www.mybuilder.com/fascias-soffits-guttering/price-guides/gutter-cleaning-cost"
T2B = "https://www.trade2base.com/blog/gutter-cleaning-costs-uk"
ABI = "https://www.abi.org.uk/news/news-articles/2025/7/insurance-support-tops-150-million-for-homes-affected-by-subsidence/"
NDEV = "https://www.northdevon.gov.uk/media/305338/georgeham-mp-cmyk.pdf"
RUSH = "https://www.rushmoor.gov.uk/media/2fhiysal/conservation-areas-overview-document-june-2025.pdf"
WAV = "https://www.waverley.gov.uk/portals/0/documents/services/planning-and-building/planning-strategies-and-policies/farnham%20ca.pdf"
HFLEET = "https://www.hart.gov.uk/sites/default/files/2022-11/ucds_fleet_text_1a_-_2010.pdf"
NFLEET = "https://www.hart.gov.uk/sites/default/files/2022-11/north_fleet_accessible.pdf"
SH = "https://www.surreyheath.gov.uk/sites/default/files/2023-05/WUASPD%20Adopted.pdf"
HYAT = "https://www.hart.gov.uk/sites/default/files/2022-11/ucds_yateley_text_-_2010.pdf"
HBW = "https://www.hart.gov.uk/sites/default/files/2022-11/ucds_blackwater_text_-_2010.pdf"
HHW = "https://www.hart.gov.uk/sites/default/files/2022-11/ucds_hartley_wintney_text_-_2010.pdf"
HHOOK = "https://www.hart.gov.uk/sites/default/files/2025-04/ucds_hook_text_-_2010.pdf"
WFLEET = "https://en.wikipedia.org/wiki/Fleet,_Hampshire"
SAND = "https://en.wikipedia.org/wiki/Sandhurst_to_Owlsmoor_Bogs_and_Heaths"
QEB = "https://en.wikipedia.org/wiki/Queen_Elizabeth_Barracks,_Church_Crookham"
ZEB = "https://www.geograph.org.uk/photo/2893275"
SOUTHW = "https://en.wikipedia.org/wiki/Southwood,_Hampshire"
ALD = "https://www.rushmoor.gov.uk/media/rr3lomgg/3-1-3_das_chapter_3.pdf"

# Statistics asset. Each row: section, figure, statement, source title, url.
STATS = [
 # Rainfall
 ["Rainfall", "808 mm", "Average annual rainfall for the Met Office's southern England region, 1991 to 2020.", "Met Office: regional climate averages 1991-2020 (England S)", MET],
 ["Rainfall", "86 to 87 mm", "Average monthly rainfall in October, November and December in southern England, the wettest months of the year and the same months the leaves fall.", "Met Office: regional climate averages 1991-2020 (England S)", MET],
 ["Rainfall", "53 mm", "Average rainfall in March and April, the driest months in the southern England series and the easiest time of year for spring gutter work.", "Met Office: regional climate averages 1991-2020 (England S)", MET],
 ["Rainfall", "129 days", "Average number of days a year with at least 1 mm of rain in southern England.", "Met Office: regional climate averages 1991-2020 (England S)", MET],
 ["Rainfall", "38 days", "Days with 1 mm or more of rain across October, November and December combined in southern England, close to a third of the year's rain days in three months.", "Met Office: regional climate averages 1991-2020 (England S)", MET],
 ["Rainfall", "42 days", "Average days of air frost per year in southern England. Water trapped by a blocked gutter can freeze and stress joints and brackets.", "Met Office: regional climate averages 1991-2020 (England S)", MET],
 # Costs
 ["Costs", "£60 to £180", "Typical UK price range for a professional gutter clean on a typical house in 2026.", "Fantastic Services: gutter cleaning cost guide (2026)", FANT],
 ["Costs", "20 to 30%", "Typical uplift on gutter cleaning prices in London and the South East compared with elsewhere.", "Fantastic Services: gutter cleaning cost guide (2026)", FANT],
 ["Costs", "£4 to £12", "Typical price per linear metre for larger or awkward gutter runs.", "MyBuilder: gutter cleaning costs", MYB],
 ["Costs", "£70 to £130", "Average standard clean cost range for South East England.", "MyBuilder: gutter cleaning costs", MYB],
 ["Costs", "£150 to £425+", "Range for larger or harder-to-reach gutter cleaning jobs.", "MyBuilder: gutter cleaning costs", MYB],
 ["Costs", "£60 to £100", "Typical 2026 trade price for a semi-detached house, as published for gutter cleaning businesses.", "Trade2Base: gutter cleaning prices UK (2026)", T2B],
 # Safety
 ["Safety", "35", "Workers killed by falls from height in Great Britain in 2024/25, the most common cause of fatal injury at work.", "HSE: fatal injuries in Great Britain 2024/25", HSE],
 ["Safety", "Over 25%", "Share of all worker deaths in 2024/25 caused by falls from height.", "HSE: fatal injuries in Great Britain 2024/25", HSE],
 # Housing stock
 ["Housing stock", "56%", "Share of England's housing stock built before 1965. Older homes are more likely to have ageing or original rainwater goods.", "Centre for Ageing Better, from the English Housing Survey 2017-18", AGEING],
 ["Housing stock", "37%", "Share of England's housing stock built before the end of the Second World War.", "Centre for Ageing Better, from the English Housing Survey 2017-18", AGEING],
 ["Housing stock", "35%", "Share of terraced homes in England built before 1919.", "English Housing Survey 2013: stock profile", EHS13],
 ["Housing stock", "59%", "Share of semi-detached homes built between 1919 and 1964.", "English Housing Survey 2013: stock profile", EHS13],
 ["Housing stock", "100+ years", "Working life that well-maintained cast iron rainwater goods can achieve.", "North Devon Council: conservation area management plan (rainwater goods)", NDEV],
 # Insurance
 ["Insurance", "Over £150m", "Insurance support paid to homes affected by subsidence in the first half of 2025.", "Association of British Insurers (July 2025)", ABI],
 # Local
 ["Local housing", "9", "Conservation areas in Rushmoor (Aldershot and Farnborough) as of June 2025, including Farnborough Hill and Farnborough Street, both designated in 2025.", "Rushmoor: conservation areas overview (June 2025)", RUSH],
 ["Local housing", "1987", "Year South Farnborough was designated a conservation area.", "Rushmoor: conservation areas overview (June 2025)", RUSH],
 ["Local housing", "387", "Listed buildings counted in Farnham, whose Georgian core was built on mid-1700s hop-growing wealth.", "Waverley: Farnham conservation area", WAV],
 ["Local housing", "1970", "Year the Farnham town centre conservation area was established.", "Waverley: Farnham conservation area", WAV],
 ["Local housing", "1994", "Year North Fleet became a conservation area. An Article 4 direction has applied since 1998.", "Hart: North Fleet Conservation Area appraisal", NFLEET],
 ["Local housing", "About 1,850", "Homes built at Elvetham Heath, Fleet, between about 2000 and 2008.", "Hart: Urban Characterisation and Density Study, Fleet (2010)", HFLEET],
 ["Local housing", "20 ha", "Nature reserve at Elvetham Heath, alongside retained mature trees and woodland.", "Hart: Urban Characterisation and Density Study, Fleet (2010)", HFLEET],
 ["Local housing", "Around 80%", "Share of Blackwater North made up of 1960s to 1980s estates.", "Hart: Urban Characterisation and Density Study, Blackwater (2010)", HBW],
 ["Local housing", "Around 70%", "Share of Hawley (Blackwater South) made up of later 20th-century housing.", "Hart: Urban Characterisation and Density Study, Blackwater (2010)", HBW],
 ["Local housing", "1970s", "Decade Heatherside, Camberley, was built by Bovis Homes on former heathland.", "Surrey Heath: Western Urban Area Character SPD (2012)", SH],
 ["Local housing", "1950s", "Decade the Old Dean estate in Camberley was built.", "Surrey Heath: Western Urban Area Character SPD (2012)", SH],
 ["Local housing", "1980s", "Decade the Southwood estate was built on the former Southwood Camp and Cove Radio Station site.", "Wikipedia: Southwood, Hampshire", SOUTHW],
 ["Local housing", "1961 to 1969", "Years Aldershot's barracks were substantially rebuilt.", "Rushmoor: Wellesley design and access statement", ALD],
 ["Local housing", "2000", "Year the Gurkhas left Queen Elizabeth Barracks, Church Crookham, before the site was redeveloped for housing.", "Wikipedia: Queen Elizabeth Barracks, Church Crookham", QEB],
 # Local trees and water
 ["Local trees and water", "Largest", "Fleet Pond is the largest freshwater lake in Hampshire.", "Wikipedia: Fleet, Hampshire", WFLEET],
 ["Local trees and water", "20 acres", "Size of Zebon Copse, broadleaved woodland inside the Zebon estate, Church Crookham, next to the Basingstoke Canal.", "Geograph: Zebon Copse", ZEB],
 ["Local trees and water", "16th century", "Zebon Copse's 38 ancient-woodland indicator plants suggest woodland on the site since at least the 1500s.", "Geograph: Zebon Copse", ZEB],
 ["Local trees and water", "85.8 ha", "Size of the Sandhurst to Owlsmoor Bogs and Heaths SSSI on Sandhurst's northern edge.", "Wikipedia: Sandhurst to Owlsmoor Bogs and Heaths", SAND],
 ["Local trees and water", "Pine plantations", "Camberley's wooded estates survive from 19th-century pine plantations, with many protected trees.", "Surrey Heath: Western Urban Area Character SPD (2012)", SH],
 ["Local trees and water", "Oak lines", "Hartley Wintney's Common is defined by regimented lines of oak trees.", "Hart: Urban Characterisation and Density Study, Hartley Wintney (2010)", HHW],
 ["Local trees and water", "Horse chestnut", "Dorchester Road in Hook's historic core has a horse chestnut avenue.", "Hart: Urban Characterisation and Density Study, Hook (2010)", HHOOK],
 ["Local trees and water", "Yateley Lakes", "Much of the River Blackwater valley floor north of Yateley is flooded gravel workings.", "Hart: Urban Characterisation and Density Study, Yateley (2010)", HYAT],
]

GUIDE_BODIES = {
"how-often-clean-gutters": {
 "title": "How Often Should Gutters Be Cleaned? Local Guide by Tree and Roof Type",
 "desc": "How often to clean gutters in Farnborough, Fleet, Camberley and Farnham: once or twice a year depending on oak, pine and horse chestnut cover, with the best months to book.",
 "h1": "How often should gutters be cleaned?",
 "lead": "Once a year suits most homes. Homes under trees usually need twice. The trees over your roof matter more than the house itself, and locally that means oak, horse chestnut and pine.",
 "body": """
## The short answer

| Situation | How often | When |
|---|---|---|
| Open estate, no trees near the roof | Once a year | Late November to January |
| Broadleaf trees nearby (oak, horse chestnut, sycamore) | Twice a year | After leaf fall, then spring |
| Pine or fir over the roof | Two to three times a year | Winter, spring, and late summer if needed |
| Gutter guards fitted | Check once a year | Winter |

## Why timing matters more than frequency

In southern England, October, November and December are both the wettest months and the months the leaves come down, averaging about 86 to 87 mm of rain each ([Met Office](%(met)s)). A clean in September leaves the gutters exposed to the whole leaf drop. A clean once the trees are bare clears the lot before the rest of winter.

## Local tree patterns

- **Oak** (Hartley Wintney Common, Zebon Copse, Fleet streets): one heavy drop from October to early December, plus acorns. Clean after it finishes.
- **Horse chestnut** (Hook's Dorchester Road avenue): big, wet leaves that pack down hard.
- **Pine** (Camberley's Wooded Hills, Sandhurst, Hawley, Yateley's southern edge): needles fall all year and mat together. Plan for more than one visit.
- **Lime** (Hartley Wintney's Brackley Avenue): seeds and sticky deposits in summer.

The [area pages](/areas/) go street by street.
""" },
"signs-gutters-need-cleaning": {
 "title": "Signs Your Gutters Need Cleaning: What to Check From the Ground",
 "desc": "Seven signs your gutters need cleaning that you can check safely from the ground, and which ones mean you should book soon.",
 "h1": "Signs your gutters need cleaning",
 "lead": "You don't need a ladder to tell whether gutters need attention. Most warning signs can be seen from the garden or the pavement, especially during or just after rain.",
 "body": """
## Check during rain

1. **Water spilling over the front edge.** The most obvious sign. A blockage or a full gutter.
2. **Water pouring next to a downpipe.** Usually a blocked outlet or downpipe rather than a full gutter.
3. **Dripping from joints.** Failing seals, often on systems 25 or more years old.

## Check in dry weather

4. **Plants growing out of the gutter.** There's enough soil in there to grow seedlings.
5. **Sagging runs.** Weight from wet debris, or failed brackets.
6. **Staining on brickwork or fascias** below the gutter line.
7. **Damp patches inside** on upper walls or ceilings near the eaves.

## Don't climb

Falls from height were the most common cause of fatal injury to workers in Great Britain in 2024/25, causing 35 deaths ([HSE](%(hse)s)). A ground-level check plus photos from a professional visit is safer.
""" },
"pine-needles-in-gutters": {
 "title": "Pine Needles in Gutters: Why They Block and What to Do",
 "desc": "Pine needles are the hardest gutter debris in Camberley, Sandhurst, Yateley and Hawley. Why they mat together, why guards struggle, and how often to clean.",
 "h1": "Pine needles in gutters",
 "lead": "If you live near pine, you've probably found that your gutters block faster than your neighbours' on open estates. That's not bad luck. Pine needles behave differently from leaves.",
 "body": """
## Where this matters locally

Camberley's wooded estates survive from 19th-century pine plantations ([Surrey Heath](%(sh)s)). Sandhurst is framed by woods, heaths and fir plantations. Hawley has roads named Fir Drive and Birch Drive, and tree-work applications in South Farnborough regularly involve protected pines.

## Why needles are worse than leaves

- **They fall all year**, not in one autumn drop, so a single winter clean doesn't keep them clear.
- **They knit together** into a mat that holds water and silt.
- **They slip through guards.** Needles thread through brush guards and coarse mesh, then lodge.
- **They plug downpipes.** Needles wash into the outlet and compact.

## What works

1. Plan two or three cleans a year rather than one
2. If you want guards, use fine micro-mesh only
3. Make sure downpipes are cleared and flow-tested, not just the gutter
4. Ask for photos so you can see the condition inside the gutter
""" },
"cast-iron-gutters": {
 "title": "Cast Iron Gutters on Period Homes: Care, Repair and Consent",
 "desc": "How to look after cast iron gutters on period homes in Farnham, Fleet and Farnborough: cleaning, resealing, painting, and when listed building consent applies.",
 "h1": "Cast iron gutters on period homes",
 "lead": "Farnham's Georgian centre, Fleet's Edwardian streets and South Farnborough's villas still have cast iron gutters on many houses. Looked after, cast iron outlasts plastic by decades. Neglected, it rusts at the joints and leaks.",
 "body": """
## Why it's worth keeping

Correctly maintained cast iron rainwater goods can last more than 100 years, and traditional half-round and ogee profiles are still made ([North Devon Council conservation guidance](%(ndev)s)). Plastic can become brittle in sunlight and rarely lasts as long.

## Routine care

- **Clean once or twice a year.** Standing water and wet debris speed up corrosion.
- **Reseal joints** when they drip. Cast iron joints are bolted and sealed, and old sealant fails.
- **Keep it painted.** Paint is what protects the iron. Repaint when you see rust bloom.

## Listed buildings and conservation areas

Farnham has 387 listed buildings ([Waverley](%(wav)s)). North Fleet is a conservation area with an Article 4 direction. Like-for-like cleaning and repair don't change appearance. Replacing cast iron with plastic, or changing the profile, on a listed building usually needs listed building consent, so check with the council first.
""" },
"skyvac-gutter-cleaning": {
 "title": "Gutter Vacuums Explained: Ground-Level Gutter Cleaning",
 "desc": "How ground-level gutter vacuum systems with camera poles work, what they're good at, and when ladders or access equipment are still needed.",
 "h1": "Gutter vacuums explained",
 "lead": "Most professional gutter cleaning on two-storey homes is now done from the ground with a high-reach vacuum. SkyVac is one well-known brand. Here's how these systems work and where they reach their limits.",
 "body": """
## How it works

A powerful industrial vacuum is connected to lightweight carbon-fibre or aluminium poles that reach the gutter from the ground. A camera at the top of the pole shows the operator the inside of the gutter on a screen, so they can see what's been removed and take before and after photos.

## Strengths

- No ladder against your gutters or fascias
- Wet and dry debris removed, including silt
- Camera photos of the gutter interior as proof of work

## Limits

- **Three-storey and taller buildings** may need more reach or access equipment
- **Conservatory and flat roofs** often need a different approach
- **Compacted, years-old blockages** may need hand clearing
- **Downpipes** still need clearing from the outlet or the shoe

## Ask before booking

Ask which method will be used for your property and whether photos are included. A professional will tell you if your roof needs something other than a vacuum.
""" },
}
