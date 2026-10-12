#!/bin/bash
# ============================================================
# The Gutter Team — Deploy to Vercel
# Run this ONCE from inside the gutter-farnborough folder:
#   cd /path/to/gutter-farnborough
#   bash deploy-to-vercel.sh
#
# Requirements: Node.js installed (https://nodejs.org)
# Your Vercel project: gutterteam-co-uk
# Your domain:         www.gutterteam.co.uk
# ============================================================

set -e

echo ""
echo "================================================"
echo "  The Gutter Team — Vercel Deployment Script"
echo "================================================"
echo ""

# Check Node/npm
if ! command -v node &>/dev/null; then
  echo "ERROR: Node.js is required. Download from https://nodejs.org"
  exit 1
fi

# Install Vercel CLI if needed
if ! command -v vercel &>/dev/null; then
  echo "Installing Vercel CLI..."
  npm install -g vercel
fi

echo "Step 1: Log in to Vercel (browser will open)..."
vercel login

echo ""
echo "Step 2: Linking project..."
vercel link \
  --project prj_SZ2ZciA2LP72ceStkZFtvu6s9hfv \
  --scope   markhugorichards-2828s-projects \
  --yes

echo ""
echo "Step 3: Deploying to production..."
vercel deploy \
  --prod \
  --scope markhugorichards-2828s-projects \
  --yes \
  --name gutterteam-co-uk \
  --no-clipboard \
  --build-env VERCEL_OUTPUT_DIRECTORY=.

echo ""
echo "================================================"
echo "  DONE! Your site is live on Vercel."
echo "  Visit: https://www.gutterteam.co.uk"
echo "================================================"
echo ""
echo "Next steps:"
echo "  1. Replace 01252 000 000 with your real phone number in all HTML files"
echo "  2. Set up Google Business Profile: https://business.google.com"
echo "  3. Submit sitemap in Google Search Console"
echo "  4. Enable Vercel Analytics in your dashboard (free)"
