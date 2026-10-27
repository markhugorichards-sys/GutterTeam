# The Gutter Team (gutterteam.co.uk)

Static site generated from `build/`. Vercel serves `public/` (see `vercel.json`).

## Edit and rebuild

```
python3 build/build.py     # needs: pip install jinja2 markdown
```

Commit both `build/` and `public/`. Vercel deploys `public/` as-is (no build step).

| What | Where |
|---|---|
| Area pages (the area sheet) | `build/data/areas.py` (also exported to `area-sheet.csv`) |
| Services, prices, site settings | `build/data/sitecfg.py` |
| Guides and statistics | `build/data/guides.py` |
| Real job photos and reviews | `build/data/proof.py` (+ images in `build/static/images/jobs/`) |
| Google review link for the QR card | `google_review_url` in `sitecfg.py` |
| Printable review card | `ops/review-card.pdf` (QR points to /review/) |

## Rules
- No phone numbers, no invented reviews, ratings, job counts or credentials.
- Prices are market bands (estimates), confirmed by the partner before booking.
- Every local fact in `areas.py` must trace to a URL in that area's `sources`.
- IndexNow: `.github/workflows/indexnow.yml` submits changed pages on push to main; run it manually with scope `all` after big changes.
