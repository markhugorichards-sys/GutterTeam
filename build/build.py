#!/usr/bin/env python3
"""Static site generator for gutterteam.co.uk.

Usage:  python3 build/build.py
Output: public/ (served by Vercel; see vercel.json)
"""
import csv, json, os, re, shutil, sys
from pathlib import Path
import markdown
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent / "public"
sys.path.insert(0, str(ROOT / "data"))
from sitecfg import SITE, PRICE_BANDS, PRICE_ADDONS, PRICE_SOURCES, SERVICES, GUIDES  # noqa: E402
from areas import AREAS  # noqa: E402
from guides import STATS, GUIDE_BODIES, MET, HSE  # noqa: E402
from proof import JOBS, REVIEWS  # noqa: E402

env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=True, trim_blocks=True, lstrip_blocks=True)
CSS = re.sub(r"\s*\n\s*", "", (ROOT / "templates" / "style.css").read_text())
ORG_ID = SITE["domain"] + "/#org"
PAGES = []  # (path, priority)


def md(text, fmt=None):
    if fmt:
        text = text % fmt
    return markdown.markdown(text, extensions=["tables"])


def ld(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def breadcrumbs(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE["domain"] + u} for i, (n, u) in enumerate(items)]}


def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


ORG = {"@context": "https://schema.org", "@type": "Organization", "@id": ORG_ID, "name": SITE["name"],
       "url": SITE["domain"] + "/", "email": SITE["email"], "logo": SITE["domain"] + "/apple-touch-icon.png",
       "legalName": SITE["operator"],
       "areaServed": [{"@type": "Place", "name": a["name"]} for a in AREAS]}


def write(path, template, priority=0.7, noindex=False, **ctx):
    ctx.setdefault("has_form", not ctx.get("noform"))
    html = env.get_template(template).render(
        site=SITE, css=CSS, path=path, noindex=noindex, services=SERVICES, areas=AREAS,
        guides=GUIDES, bands=PRICE_BANDS, **ctx)
    html = re.sub(r"\n\s*\n+", "\n", html)
    dest = OUT / path.lstrip("/") / "index.html" if path.endswith("/") else OUT / path.lstrip("/")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html)
    if not noindex:
        PAGES.append((path, priority))


COMMON_FAQS = [
    ["Do I need to be home?", "Usually not. If side gates can be left unlocked, the gutters can be cleared and the photos sent afterwards."],
    ["How is the price confirmed?", "You describe your home in the form and get a confirmed price by email before anything is booked. If a repair is found during the visit, it is photographed and priced separately, never added without your agreement."],
]
HOME_FAQS = [
    ["How much does gutter cleaning cost?", "Typical local prices run from about £65 to £100 for a terraced house, £80 to £125 for a semi and £110 to £190 for a detached house, depending on access and build-up. The price estimator gives a closer range for your home."],
    ["How often should gutters be cleaned?", "Once a year for most homes, ideally after leaf fall. Homes under oak, horse chestnut or pine usually need two visits a year."],
    ["Who does the work?", "Your enquiry goes to one vetted gutter specialist covering your area, who replies with a price and carries out the work. Your details aren't shared with anyone else."],
] + COMMON_FAQS


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(ROOT / "static", OUT)

    # Home
    write("/", "home.html", 1.0, title="Gutter Cleaning Farnborough, Fleet & Camberley | The Gutter Team",
          desc="Gutter cleaning, downpipe unblocking and gutter repairs in Farnborough, Fleet, Camberley, Farnham and nearby. Typical prices published, price confirmed by email, photos every visit.",
          faqs=HOME_FAQS, jobs=JOBS,
          schema=[ld(ORG), ld({"@context": "https://schema.org", "@type": "WebSite", "name": SITE["name"], "url": SITE["domain"] + "/", "publisher": {"@id": ORG_ID}}), ld(faq_ld(HOME_FAQS))])

    # Services
    svc_cards = "".join(f'<a class="card" href="/services/{s["slug"]}/"><h3>{s["name"]}</h3><p>{s["short"]}</p><span class="more">Read more</span></a>' for s in SERVICES)
    write("/services/", "page.html", 0.9, title="Gutter Services: Cleaning, Repairs, Downpipes and Guards | The Gutter Team",
          desc="Gutter cleaning, downpipe unblocking, gutter repairs, gutter guards, fascia cleaning and maintenance plans across Farnborough, Fleet, Camberley and Farnham.",
          h1="Gutter services", lead="Everything to do with the gutters and downpipes on your home, priced up front and photographed on the day.",
          crumbs=[["Services", ""]], body="", extra=f'<div class="grid3">{svc_cards}<a class="card" href="/landlords/"><h3>Landlords and agents</h3><p>Scheduled cleans and dated photo records across a portfolio.</p><span class="more">Read more</span></a></div>',
          schema=[ld(breadcrumbs([["Home", "/"], ["Services", "/services/"]]))])
    for s in SERVICES:
        path = f"/services/{s['slug']}/"
        write(path, "page.html", 0.9 if s["slug"] == "gutter-cleaning" else 0.8, title=f"{s['title']} | The Gutter Team", desc=s["desc"],
              h1=s["name"], lead=s["lead"], crumbs=[["Services", "/services/"], [s["name"], ""]], body=md(s["body"]), faqs=s["faqs"] + COMMON_FAQS,
              area=s["name"], service=s["name"].replace("Fascia and Soffit Cleaning","Fascia and soffit cleaning").replace("Annual Maintenance Plans","Annual maintenance plan"),
              schema=[ld({"@context": "https://schema.org", "@type": "Service", "name": s["name"], "serviceType": s["name"], "description": s["desc"],
                          "provider": {"@id": ORG_ID}, "areaServed": [{"@type": "Place", "name": a["name"]} for a in AREAS], "url": SITE["domain"] + path}),
                      ld(breadcrumbs([["Home", "/"], ["Services", "/services/"], [s["name"], path]])), ld(faq_ld(s["faqs"] + COMMON_FAQS))])

    land_body = md("""
## What landlords and agents get

- **A dated photo record** of each property's gutters, before and after, for your maintenance file
- **Scheduled visits** timed to the trees over each roof, without you chasing anyone
- **Tenant-friendly access**: most work needs only exterior access, so tenants rarely need to be home
- **Repairs priced separately** and approved by you before work starts
- **One email thread** per portfolio rather than per property

## Why gutters matter for lettings

Overflowing gutters are a common cause of damp complaints. Repairs to the structure and exterior of a let home, including drains and gutters, are usually the landlord's responsibility under section 11 of the Landlord and Tenant Act 1985. A dated photo record shows the gutters were maintained.

## Getting a portfolio price

Send the postcodes and property types in the enquiry form, or email a list. You'll get a price for each property and a suggested visit schedule.
""")
    write("/landlords/", "page.html", 0.8, title="Gutter Cleaning for Landlords and Letting Agents | The Gutter Team",
          desc="Scheduled gutter cleaning with dated before and after photo records for landlords and letting agents across Farnborough, Fleet, Camberley and Farnham.",
          h1="Gutter cleaning for landlords and agents", lead="Scheduled cleans, dated photo records and repairs approved by you, across one property or a whole portfolio.",
          crumbs=[["Landlords and agents", ""]], body=land_body, area="Landlord", service="Annual maintenance plan",
          page_sources=[["Landlord and Tenant Act 1985, section 11 (legislation.gov.uk)", "https://www.legislation.gov.uk/ukpga/1985/70/section/11"]],
          schema=[ld(breadcrumbs([["Home", "/"], ["Landlords", "/landlords/"]]))])

    # Areas
    by_slug = {a["slug"]: a for a in AREAS}
    area_cards = "".join(f'<a class="card" href="/areas/{a["slug"]}/"><h3>{a["name"]}</h3><p>{", ".join(a["postcodes"])} &middot; {a["county"]}</p><p style="margin-top:6px">{", ".join(n for n, _ in a["micro"][:3])}</p><span class="more">Gutter cleaning in {a["name"]}</span></a>' for a in AREAS)
    write("/areas/", "page.html", 0.9, title="Areas Covered: Gutter Cleaning in Hampshire, Surrey and Berkshire | The Gutter Team",
          desc="Gutter cleaning across Farnborough, Cove, Aldershot, Ash Vale, Fleet, Church Crookham, Camberley, Frimley, Farnham, Yateley, Sandhurst, Blackwater, Hartley Wintney and Hook.",
          h1="Areas covered", lead="14 towns across north-east Hampshire, west Surrey and south Berkshire. Each page explains what local roofs and trees mean for your gutters.",
          crumbs=[["Areas", ""]], body="", extra=f'<div class="grid3">{area_cards}</div>',
          schema=[ld(breadcrumbs([["Home", "/"], ["Areas", "/areas/"]]))])
    for a in AREAS:
        path = f"/areas/{a['slug']}/"
        faqs = a["faqs"] + COMMON_FAQS
        jobs = [j for j in JOBS if j["area"] == a["slug"]]
        revs = [r for r in REVIEWS if r["area"] == a["slug"]]
        pc = " ".join(a["postcodes"])
        write(path, "area.html", 0.8, title=f"Gutter Cleaning {a['name']} {pc} | Prices and Local Guide | The Gutter Team",
              desc=f"Gutter cleaning in {a['name']} ({', '.join(a['postcodes'])}): typical local prices, what {a['name']} roofs and trees mean for your gutters, and a price by email. Photos every visit.",
              a=a, faqs=faqs, common_faqs=COMMON_FAQS, jobs=jobs, reviews=revs, nearby=[by_slug[n] for n in a["nearby"]],
              schema=[ld({"@context": "https://schema.org", "@type": "Service", "name": f"Gutter cleaning in {a['name']}", "serviceType": "Gutter cleaning",
                          "provider": {"@id": ORG_ID}, "url": SITE["domain"] + path,
                          "areaServed": {"@type": "Place", "name": a["name"], "address": {"@type": "PostalAddress", "addressLocality": a["name"], "addressRegion": a["county"], "addressCountry": "GB"},
                                         "geo": {"@type": "GeoCoordinates", "latitude": a["lat"], "longitude": a["lon"]}},
                          "offers": {"@type": "AggregateOffer", "priceCurrency": "GBP", "lowPrice": min(b["low"] for b in PRICE_BANDS), "highPrice": max(b["high"] for b in PRICE_BANDS)}}),
                      ld(breadcrumbs([["Home", "/"], ["Areas", "/areas/"], [a["name"], path]])), ld(faq_ld(faqs))])

    # Advice hub
    gcards = "".join(f'<a class="card" href="/advice/{g["slug"]}/"><h3>{g["name"]}</h3><p>{g["short"]}</p><span class="more">Read the guide</span></a>' for g in GUIDES)
    write("/advice/", "page.html", 0.7, title="Gutter Advice and Guides | The Gutter Team",
          desc="Practical gutter guides: prices, how often to clean, warning signs, pine needles, cast iron gutters, gutter vacuums and sourced statistics.",
          h1="Gutter advice", lead="Straight answers about gutters, with sources, so you can decide what your home needs.",
          crumbs=[["Advice", ""]], body="", extra=f'<div class="grid3">{gcards}</div>',
          schema=[ld(breadcrumbs([["Home", "/"], ["Advice", "/advice/"]]))])

    fmt = {"met": MET, "hse": HSE, "sh": "https://www.surreyheath.gov.uk/sites/default/files/2023-05/WUASPD%20Adopted.pdf",
           "ndev": "https://www.northdevon.gov.uk/media/305338/georgeham-mp-cmyk.pdf",
           "wav": "https://www.waverley.gov.uk/portals/0/documents/services/planning-and-building/planning-strategies-and-policies/farnham%20ca.pdf"}
    for slug, g in GUIDE_BODIES.items():
        path = f"/advice/{slug}/"
        write(path, "page.html", 0.7, title=f"{g['title']} | The Gutter Team", desc=g["desc"], h1=g["h1"], lead=g["lead"], updated=True,
              crumbs=[["Advice", "/advice/"], [g["h1"], ""]], body=md(g["body"], fmt), og_type="article",
              schema=[ld({"@context": "https://schema.org", "@type": "Article", "headline": g["h1"], "description": g["desc"], "dateModified": SITE["updated_iso"],
                          "author": {"@id": ORG_ID}, "publisher": {"@id": ORG_ID}, "mainEntityOfPage": SITE["domain"] + path}),
                      ld(breadcrumbs([["Home", "/"], ["Advice", "/advice/"], [g["h1"], path]]))])

    build_cost_page()
    build_stats_page()

    # Company pages
    about_body = md(f"""
## What The Gutter Team is

The Gutter Team is a local gutter service covering {SITE['region']}. It's operated by {SITE['operator']}. When you send an enquiry, it goes to **one vetted gutter specialist covering your area**, who replies with a price and carries out the work. Your details aren't sold on or sent to a list of companies.

## How we keep it honest

- **Prices in the open.** Typical price bands are published on every area page, and your exact price is confirmed by email before booking.
- **Photos on every job.** Before and after photos are sent the same day.
- **No invented reviews or ratings.** Reviews only appear on this site when they come from real local customers, with their permission.
- **Local knowledge, with sources.** Area pages draw on council character studies and other published sources, which are linked so you can check them.

## Contact

Email [{SITE['email']}](mailto:{SITE['email']}) or use the form on this page.
""")
    write("/about/", "page.html", 0.5, title="About The Gutter Team", desc="How The Gutter Team works: one vetted local gutter specialist per area, open pricing, and before and after photos on every job.",
          h1="About The Gutter Team", lead="A straightforward way to get your gutters cleared by a vetted local specialist, priced up front.", crumbs=[["About", ""]], body=about_body,
          schema=[ld(ORG), ld(breadcrumbs([["Home", "/"], ["About", "/about/"]]))])
    write("/contact/", "page.html", 0.6, title="Contact The Gutter Team | Get a Gutter Cleaning Price",
          desc="Get a gutter cleaning, repair or downpipe price by email. Covering Farnborough, Fleet, Camberley, Farnham and nearby towns.",
          h1="Get a price", lead="Fill in the form and you'll get a reply by email, usually the same working day. No phone call needed.",
          crumbs=[["Contact", ""]], body=md(f"Prefer email? Write to [{SITE['email']}](mailto:{SITE['email']}) with your postcode, property type and what you need."),
          schema=[ld(breadcrumbs([["Home", "/"], ["Contact", "/contact/"]]))])
    write("/thank-you/", "page.html", noindex=True, noform=True, title="Enquiry received | The Gutter Team", desc="Thanks for your enquiry.",
          h1="Thanks, your enquiry has been sent", lead="You'll get a reply by email, usually the same working day. Check your spam folder if nothing arrives.",
          body=md("While you wait:\n\n- [See typical prices and the estimator](/advice/gutter-cleaning-cost/)\n- [How often gutters need cleaning](/advice/how-often-clean-gutters/)\n- [Back to the home page](/)"), schema=[])
    write("/privacy/", "page.html", 0.2, noform=True, title="Privacy Notice | The Gutter Team", desc="How The Gutter Team uses the information you send through the enquiry form.",
          h1="Privacy notice", lead=f"How {SITE['operator']}, trading as {SITE['name']}, uses your information.", body=md(PRIVACY), schema=[])
    write("/terms/", "page.html", 0.2, noform=True, title="Terms of Use | The Gutter Team", desc="Terms of use for gutterteam.co.uk.",
          h1="Terms of use", lead="The basics of using this website.", body=md(TERMS), schema=[])

    # Review route used by the printed QR card
    review_url = SITE["google_review_url"]
    if review_url:
        rbody = f'<p><a class="btn" href="{review_url}">Leave a Google review</a></p><p>Thank you. It takes about 30 seconds and helps neighbours find a reliable gutter service.</p>'
        head_refresh = review_url
    else:
        rbody = md(f"Thanks for choosing The Gutter Team. Our Google profile is being set up. In the meantime, please send a sentence or two about your visit, and before and after photos if you took any, to [{SITE['email']}](mailto:{SITE['email']}?subject=My%20gutter%20visit). With your permission, we'll add it to the page for your town.")
        head_refresh = ""
    write("/review/", "page.html", noindex=True, noform=True, title="Leave a review | The Gutter Team", desc="Tell us how your gutter visit went.",
          h1="How did we do?", lead="Your feedback helps other local homeowners choose with confidence.", body=rbody, schema=[])
    if head_refresh:
        p = OUT / "review" / "index.html"
        p.write_text(p.read_text().replace("<head>", f'<head><meta http-equiv="refresh" content="0;url={head_refresh}">', 1))

    write("/404.html", "page.html", noindex=True, noform=True, title="Page not found | The Gutter Team", desc="Page not found.",
          h1="Page not found", lead="That page has moved or doesn't exist.", body=md("Try the [home page](/), [areas covered](/areas/) or [prices](/advice/gutter-cleaning-cost/)."), schema=[])

    finish()


def build_cost_page():
    path = "/advice/gutter-cleaning-cost/"
    opts = "".join(f'<option value="{b["key"]}" data-low="{b["low"]}" data-high="{b["high"]}">{b["label"]}</option>' for b in PRICE_BANDS)
    adds = "".join(f'<label class="chk"><input type="checkbox" data-low="{x["low"]}" data-high="{x["high"]}"> {x["label"]} (+&pound;{x["low"]} to &pound;{x["high"]})</label>' for x in PRICE_ADDONS)
    addrows = "".join(f'<tr><td>{x["label"]}</td><td>+&pound;{x["low"]} to &pound;{x["high"]}</td></tr>' for x in PRICE_ADDONS)
    bandrows = "".join(f'<tr><td>{b["label"]}</td><td>&pound;{b["low"]} to &pound;{b["high"]}</td></tr>' for b in PRICE_BANDS)
    est = f"""
<h2 style="font-family:'EB Garamond',Georgia,serif;font-size:1.9rem;margin:8px 0 16px;color:var(--navy)">Price estimator</h2>
<div class="est">
<div class="card"><label for="est-type">Property type</label><select id="est-type">{opts}</select>
<p style="font-weight:600;font-size:.85rem;margin:6px 0 8px">Anything extra?</p>{adds}</div>
<div class="result" aria-live="polite"><p>Likely price range for one visit</p><div class="big" id="est-out">&pound;80 to &pound;125</div>
<p>An estimate from published market bands, not a quote. Your price is confirmed by email before booking.</p>
<p style="margin-top:14px"><a class="btn" href="#enquire">Get my confirmed price</a></p></div>
</div>
<script>(function(){{var s=document.getElementById('est-type'),o=document.getElementById('est-out'),c=document.querySelectorAll('.est input[type=checkbox]');s.value='semi';function u(){{var opt=s.options[s.selectedIndex],l=+opt.dataset.low,h=+opt.dataset.high;c.forEach(function(x){{if(x.checked){{l+=+x.dataset.low;h+=+x.dataset.high}}}});o.textContent='\\u00a3'+l+' to \\u00a3'+h}}s.addEventListener('change',u);c.forEach(function(x){{x.addEventListener('change',u)}});u()}})();</script>
"""
    body = md(f"""
## Typical prices by property type

These bands are for a standard visit: every gutter run cleared, outlets and downpipes checked, and before and after photos.

<div class="tablewrap"><table><thead><tr><th>Property</th><th>Typical price per visit</th></tr></thead><tbody>{bandrows}</tbody></table></div>

## Common add-ons

<div class="tablewrap"><table><thead><tr><th>Extra</th><th>Typical extra cost</th></tr></thead><tbody>{addrows}</tbody></table></div>

## What moves the price

- **Height and access.** Three-storey homes, sloping gardens and locked or narrow side access take longer.
- **Build-up.** Gutters left for several years, especially under pine, take far longer to clear.
- **Extras on the roofline.** Conservatories, porches, bays, dormers and extensions all add short runs.

## How these figures were put together

Published 2026 UK guides put a typical clean at £60 to £180, with London and the South East running roughly 20 to 30% higher ([Fantastic Services]({PRICE_SOURCES[0][1]})). MyBuilder gives £70 to £130 for a standard clean in the South East ([MyBuilder]({PRICE_SOURCES[1][1]})). The bands above apply that regional uplift to the national ranges by property type. They're market estimates, not a price list, and VAT treatment varies because many small firms aren't VAT registered.

## Why very cheap quotes carry risk

Falls from height were the most common cause of fatal injury at work in Great Britain in 2024/25 ([HSE]({HSE})). Proper equipment and insurance cost money. Before booking anyone, ask what equipment they'll use and for a copy of their public liability certificate.
""")
    faqs = [["Is the estimate the price I'll pay?", "No. It's a range based on market bands. You get a confirmed price by email before anything is booked."],
            ["Do prices include VAT?", "It depends on the firm. Many small gutter businesses aren't VAT registered. Your confirmed price will say."]] + COMMON_FAQS
    write(path, "page.html", 0.9, title="Gutter Cleaning Cost 2026: Local Prices and Estimator | The Gutter Team",
          desc="What gutter cleaning costs in Farnborough, Fleet, Camberley and Farnham in 2026: typical prices by property type, add-on costs and an instant estimator.",
          h1="Gutter cleaning cost and price estimator", lead="Typical local prices by property type, what moves the price, and a quick estimator, all before you ask anyone for a quote.",
          crumbs=[["Advice", "/advice/"], ["Gutter cleaning cost", ""]], updated=True, body=est + body, faqs=faqs, page_sources=PRICE_SOURCES + [["HSE: fatal injuries 2024/25", HSE]],
          area="Price estimator",
          schema=[ld({"@context": "https://schema.org", "@type": "Article", "headline": "Gutter cleaning cost and price estimator", "dateModified": SITE["updated_iso"],
                      "author": {"@id": ORG_ID}, "publisher": {"@id": ORG_ID}, "mainEntityOfPage": SITE["domain"] + path}),
                  ld(breadcrumbs([["Home", "/"], ["Advice", "/advice/"], ["Gutter cleaning cost", path]])), ld(faq_ld(faqs))])


def build_stats_page():
    path = "/advice/gutter-cleaning-statistics-uk/"
    sections, rows = [], {}
    for sec, fig, stmt, st, su in STATS:
        if sec not in rows:
            sections.append(sec); rows[sec] = []
        rows[sec].append((fig, stmt, st, su))
    toc = "".join(f'<li><a href="#{s.lower().replace(" ", "-")}">{s}</a> ({len(rows[s])})</li>' for s in sections)
    tables = ""
    for s in sections:
        tr = "".join(f'<tr><td style="white-space:nowrap;font-weight:600">{f}</td><td>{t}</td><td><a href="{u}" rel="noopener">{st}</a></td></tr>' for f, t, st, u in rows[s])
        tables += f'<h2 id="{s.lower().replace(" ", "-")}">{s}</h2><div class="tablewrap"><table><thead><tr><th>Figure</th><th>What it means</th><th>Source</th></tr></thead><tbody>{tr}</tbody></table></div>'
    n = len(STATS)
    srcs = sorted({(r[3], r[4]) for r in STATS})
    body = f"""
<div class="note"><strong>{n} sourced data points</strong> on rainfall, costs, safety, national housing stock and the local housing and trees across the 14 towns we cover. Each figure links to its source. <a href="/data/gutter-statistics.csv" download>Download the CSV</a>.</div>
<h2>Key findings</h2>
<ul>
<li>October to December is both leaf-fall season and the wettest quarter in southern England, averaging about 86 to 87 mm of rain a month (Met Office, 1991 to 2020).</li>
<li>Typical UK gutter cleaning costs £60 to £180, with the South East around 20 to 30% higher.</li>
<li>Falls from height caused 35 worker deaths in Great Britain in 2024/25, the most common cause of fatal injury at work.</li>
<li>Locally, housing ranges from Farnham's listed Georgian core to large 1960s to 1980s estates, which make up around 80% of Blackwater North.</li>
</ul>
<h2>Contents</h2><ul>{toc}</ul>
{tables}
<h2>Methodology</h2>
<p>Figures were compiled in October 2026 from primary and official sources where available: the Met Office, HSE, the English Housing Survey, the Association of British Insurers, and council conservation area appraisals and urban character studies for Rushmoor, Hart, Surrey Heath and Waverley. Price figures come from published consumer and trade price guides and are estimates, not official statistics. Regional climate figures are 30-year averages for the Met Office's southern England region rather than a single local station. Local housing figures come from council studies of different dates, noted against each source. They describe character, not current counts.</p>
<h2>Limitations</h2>
<p>Price guides vary in method and sample, and they aren't independently audited. Council character studies date from 2010 to 2025 and may not reflect every recent development. Where a source is a secondary summary of official data, such as the Centre for Ageing Better's use of the English Housing Survey, it's labelled as such.</p>
<h2>Using these figures</h2>
<p>You're welcome to cite any figure on this page. Please credit the original source shown and link to this page as "The Gutter Team, gutter cleaning data and local housing facts". The compiled table is available under CC BY 4.0. Spotted an error or a newer figure? Email <a href="mailto:{SITE['email']}">{SITE['email']}</a>. Next review: January 2027.</p>
"""
    write(path, "page.html", 0.8, title=f"Gutter Cleaning Statistics UK 2026: {n} Sourced Figures and Local Data | The Gutter Team",
          desc=f"{n} sourced figures on gutter cleaning costs, UK rainfall, work-at-height safety, housing stock age and local housing and trees across north-east Hampshire and west Surrey.",
          h1="Gutter cleaning data and local housing facts", lead=f"{n} sourced figures on rainfall, costs, safety and housing, plus a local dataset for the 14 towns we cover. Free to cite.",
          crumbs=[["Advice", "/advice/"], ["Statistics", ""]], updated=True, body=body, page_sources=[list(x) for x in srcs], og_type="article",
          schema=[ld({"@context": "https://schema.org", "@type": "Dataset", "name": "Gutter cleaning data and local housing facts", "description": f"{n} sourced figures on gutter costs, rainfall, safety and housing for north-east Hampshire and west Surrey.",
                      "url": SITE["domain"] + path, "license": "https://creativecommons.org/licenses/by/4.0/", "creator": {"@id": ORG_ID}, "dateModified": SITE["updated_iso"],
                      "distribution": {"@type": "DataDownload", "encodingFormat": "text/csv", "contentUrl": SITE["domain"] + "/data/gutter-statistics.csv"}}),
                  ld({"@context": "https://schema.org", "@type": "Article", "headline": "Gutter cleaning data and local housing facts", "dateModified": SITE["updated_iso"], "author": {"@id": ORG_ID}, "publisher": {"@id": ORG_ID}}),
                  ld(breadcrumbs([["Home", "/"], ["Advice", "/advice/"], ["Statistics", path]]))])
    (OUT / "data").mkdir(exist_ok=True)
    with open(OUT / "data" / "gutter-statistics.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["section", "figure", "statement", "source", "source_url"]); w.writerows(STATS)


PRIVACY = f"""
**Who we are.** {SITE['operator']} (company number 17177195, ICO registration ZC132343), trading as {SITE['name']}. Contact: [{SITE['email']}](mailto:{SITE['email']}).

**What we collect.** When you use the enquiry form: your name, email address, postcode, property type, the service you need and anything you write in the message box.

**Why.** To arrange a price and visit for the gutter work you asked about. The lawful basis is taking steps at your request before entering into a contract.

**Who we share it with.** Your enquiry is passed to **one** gutter specialist covering your area so they can reply with a price and carry out the work. It isn't sold, and it isn't sent to multiple firms. Form submissions are processed by our form provider, Web3Forms, and delivered by email.

**How long we keep it.** Enquiries are kept for up to 24 months, then deleted, unless you become a customer, in which case records are kept as long as needed for accounting and legal purposes.

**Analytics and cookies.** This site doesn't set advertising or tracking cookies.

**Your rights.** You can ask to see, correct or delete your data, or object to its use, by emailing us. You can also complain to the Information Commissioner's Office at ico.org.uk.
"""
TERMS = f"""
This website is operated by {SITE['operator']}, trading as {SITE['name']}. Prices shown are typical market estimates, not quotes. Your price is confirmed by the gutter specialist before any work is booked, and the contract for the work is between you and that specialist. Guides on this site are general information. For listed buildings, conservation areas or structural concerns, check with your council or a qualified professional. Content on the statistics page may be cited under the attribution terms stated on that page.
"""


def finish():
    # sitemap
    urls = "".join(f'<url><loc>{SITE["domain"]}{p}</loc><lastmod>{SITE["updated_iso"]}</lastmod><priority>{pr:.1f}</priority></url>' for p, pr in PAGES if p != "/404.html")
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /thank-you/\n\nSitemap: {SITE['domain']}/sitemap.xml\n")
    (OUT / f"{SITE['indexnow_key']}.txt").write_text(SITE["indexnow_key"])
    lines = [f"# {SITE['name']}", "", f"> Gutter cleaning, downpipe unblocking and gutter repairs across {SITE['region']}. Enquiries by email go to one vetted local gutter specialist per area. Typical prices are published and confirmed before booking.", "",
             "## Prices", f"- [Gutter cleaning cost and estimator]({SITE['domain']}/advice/gutter-cleaning-cost/): " + "; ".join(f"{b['label']} £{b['low']}-£{b['high']}" for b in PRICE_BANDS), "",
             "## Services"] + [f"- [{s['name']}]({SITE['domain']}/services/{s['slug']}/): {s['short']}" for s in SERVICES] + ["", "## Areas"] + \
            [f"- [{a['name']}]({SITE['domain']}/areas/{a['slug']}/): {', '.join(a['postcodes'])}, {a['county']}" for a in AREAS] + ["", "## Guides"] + \
            [f"- [{g['name']}]({SITE['domain']}/advice/{g['slug']}/)" for g in GUIDES] + ["", f"Contact: {SITE['email']}"]
    (OUT / "llms.txt").write_text("\n".join(lines) + "\n")
    # Area sheet export (the "Google Sheet" of locations)
    with open(ROOT.parent / "area-sheet.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["area", "url", "county", "council", "postcodes", "micro_location", "micro_notes", "housing_eras", "trees", "water", "best_time", "sources"])
        for a in AREAS:
            for n, d in a["micro"]:
                w.writerow([a["name"], f"{SITE['domain']}/areas/{a['slug']}/", a["county"], a["council"], " ".join(a["postcodes"]), n, d,
                            "; ".join(e for e, _ in a["housing"]), a["trees"], a["water"], a["timing"], " | ".join(u for _, u in a["sources"])])
    print(f"Built {len(PAGES)} indexable pages into {OUT}")


if __name__ == "__main__":
    build()
