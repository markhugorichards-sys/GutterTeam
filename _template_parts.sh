#!/bin/bash

head_open() {
  local title="$1"
  local desc="$2"
  local canonical="$3"
  local kw="$4"
  cat << EOF
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>$title</title>
<meta name="description" content="$desc">
<meta name="keywords" content="$kw">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://www.thegutterteam.co.uk$canonical">
<meta name="geo.region" content="GB-HAM">
<meta property="og:title" content="$title">
<meta property="og:description" content="$desc">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_GB">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%231D3557'/%3E%3Cpath d='M7 12h18M7 12c0 3.2 1.6 5 5 5h8c3.4 0 5-1.8 5-5' stroke='%232A9D8F' stroke-width='2' stroke-linecap='round' fill='none'/%3E%3Cpath d='M13 17v8h6v-8' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' fill='none'/%3E%3C/svg%3E">
<meta name="theme-color" content="#1D3557">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
EOF
}
