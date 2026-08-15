#!/usr/bin/env python3
"""One-off generator for the /locations/ city pages. Run from repo root."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CITIES = [
    {
        "slug": "dillsburg",
        "name": "Dillsburg",
        "county": "York County",
        "minutes": None,  # HQ
        "character": "Dillsburg is a small borough on the York/Cumberland County line, and it's where Goldenspire is actually based, not a satellite office or a mailing address. Most of the small businesses here run on the same handful of tools: a phone that doesn't stop, a shared inbox, and a calendar someone has to keep updated by hand.",
        "industries": ["construction", "landscaping", "auto-services", "retail"],
        "lat": 40.1223, "lng": -77.0355,
    },
    {
        "slug": "mechanicsburg",
        "name": "Mechanicsburg",
        "county": "Cumberland County",
        "minutes": "15 minutes",
        "character": "Mechanicsburg sits in the middle of Cumberland County's logistics and distribution corridor, with a strong base of professional services and small manufacturers alongside it. Businesses here tend to juggle more moving parts, more vendors, more scheduling, than their headcount would suggest.",
        "industries": ["manufacturing", "professional-services", "financial-services", "insurance"],
        "lat": 40.2126, "lng": -77.0083,
    },
    {
        "slug": "carlisle",
        "name": "Carlisle",
        "county": "Cumberland County",
        "minutes": "20–25 minutes",
        "character": "Carlisle is the Cumberland County seat, home to Dickinson College and the U.S. Army War College, with a mix of manufacturing, logistics along the I-81 corridor, and a busy small-business downtown. That mix means a wide range of intake and scheduling problems, from retail foot traffic to B2B quote requests.",
        "industries": ["manufacturing", "retail", "professional-services", "auto-services"],
        "lat": 40.2011, "lng": -77.1861,
    },
    {
        "slug": "camp-hill",
        "name": "Camp Hill",
        "county": "Cumberland County",
        "minutes": "20 minutes",
        "character": "Camp Hill sits just across the Susquehanna from Harrisburg, with a dense concentration of professional services, healthcare-adjacent businesses, and retail. It's a market where a business's phone and web presence are often the whole first impression, since so much of the competition is a short drive away.",
        "industries": ["professional-services", "financial-services", "retail", "salons"],
        "lat": 40.2337, "lng": -76.9214,
    },
    {
        "slug": "york",
        "name": "York",
        "county": "York County",
        "minutes": "25–30 minutes",
        "character": "York is the York County seat and a historic manufacturing city that's been steadily rebuilding its downtown around small business, professional services, and skilled trades. A lot of the businesses here inherited processes built for a different era and are now trying to modernize without ripping everything out.",
        "industries": ["manufacturing", "construction", "hvac", "law-firms"],
        "lat": 39.9626, "lng": -76.7277,
    },
    {
        "slug": "harrisburg",
        "name": "Harrisburg",
        "county": "Dauphin County",
        "minutes": "25–30 minutes",
        "character": "As Pennsylvania's state capital, Harrisburg has an outsized concentration of law firms, insurance agencies, financial services, and other professional practices, alongside the small businesses that serve that workforce. Intake and follow-up speed matters more here, since clients and prospects usually have several comparable firms to choose from.",
        "industries": ["law-firms", "insurance", "financial-services", "business-brokers"],
        "lat": 40.2732, "lng": -76.8867,
    },
    {
        "slug": "lancaster",
        "name": "Lancaster",
        "county": "Lancaster County",
        "minutes": "50 minutes",
        "character": "Lancaster's economy runs on agriculture, tourism, and a fast-growing base of retail and professional services downtown. It's the furthest of these markets from Dillsburg, which is exactly why most of the engagement happens remotely, on a screen-share, the same way it would for a client in another state.",
        "industries": ["retail", "real-estate", "professional-services", "architecture"],
        "lat": 40.0379, "lng": -76.3055,
    },
]

LOCATION_TEASERS = {'dillsburg': 'Home base. Small-town main street businesses, contractors, and shops running on phone calls and paper.', 'mechanicsburg': 'Cumberland County logistics and distribution corridor, with a growing base of professional services.', 'carlisle': 'County seat with a manufacturing, logistics, and college-town retail mix along the I-81 corridor.', 'camp-hill': 'Dense professional-services and healthcare-adjacent market just across the river from Harrisburg.', 'york': 'Historic manufacturing city rebuilding its downtown around small business and skilled trades.', 'harrisburg': 'State capital with a heavy concentration of law, insurance, and financial-services firms.', 'lancaster': 'Agriculture, tourism, and a fast-growing downtown retail and professional-services scene.'}

INDUSTRY_LABELS = {
    "real-estate": "Real Estate",
    "hvac": "HVAC &amp; Home Services",
    "insurance": "Insurance Agencies",
    "financial-services": "Credit Unions &amp; Financial Services",
    "law-firms": "Law Firms",
    "business-brokers": "Business Brokers",
    "auto-services": "Auto Services",
    "retail": "Retail &amp; Local Shops",
    "architecture": "Architecture &amp; Design",
    "manufacturing": "Manufacturing &amp; Distribution",
    "landscaping": "Landscaping",
    "construction": "Construction",
    "salons": "Salons &amp; Personal Care",
    "professional-services": "Professional Services",
}

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" type="image/png" href="../images/favicon.png">
<title>AI Automation &amp; Business Systems in {name}, PA | Goldenspire Group</title>
<meta name="description" content="Goldenspire Group builds AI automation and business systems for {name}, PA companies: customer intake, scheduling, documents, reviews, and reporting, built around how your business actually runs.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://goldenspiregroup.com/locations/{slug}.html">
<meta property="og:type" content="website">
<meta property="og:title" content="AI Automation &amp; Business Systems in {name}, PA | Goldenspire Group">
<meta property="og:description" content="Goldenspire Group builds AI automation and business systems for {name}, PA companies: customer intake, scheduling, documents, reviews, and reporting.">
<meta property="og:url" content="https://goldenspiregroup.com/locations/{slug}.html">
<meta property="og:site_name" content="Goldenspire Group">
<meta property="og:locale" content="en_US">
<meta property="og:image" content="https://goldenspiregroup.com/images/social-share-banner.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://goldenspiregroup.com/images/social-share-banner.jpg">
<meta name="twitter:title" content="AI Automation &amp; Business Systems in {name}, PA | Goldenspire Group">
<meta name="twitter:description" content="Goldenspire Group builds AI automation and business systems for {name}, PA companies.">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "AI business process automation",
  "name": "AI Automation &amp; Business Systems in {name}, PA",
  "description": "AI-powered automation and business systems consulting serving {name}, {county}, Pennsylvania.",
  "provider": {{
    "@type": "ProfessionalService",
    "name": "Goldenspire Group",
    "url": "https://goldenspiregroup.com",
    "telephone": "+17175022056",
    "email": "info@goldenspiregroup.com",
    "address": {{
      "@type": "PostalAddress",
      "addressLocality": "Dillsburg",
      "addressRegion": "PA",
      "addressCountry": "US"
    }},
    "geo": {{
      "@type": "GeoCoordinates",
      "latitude": 40.1223,
      "longitude": -77.0355
    }}
  }},
  "areaServed": {{
    "@type": "City",
    "name": "{name}, PA",
    "containedInPlace": {{"@type": "AdministrativeArea", "name": "{county}, Pennsylvania"}}
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://goldenspiregroup.com/"}},
    {{"@type": "ListItem", "position": 2, "name": "Locations", "item": "https://goldenspiregroup.com/locations.html"}},
    {{"@type": "ListItem", "position": 3, "name": "{name}, PA", "item": "https://goldenspiregroup.com/locations/{slug}.html"}}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "Do you actually work with businesses in {name}?",
      "acceptedAnswer": {{ "@type": "Answer", "text": "{drive_plain}" }}
    }},
    {{
      "@type": "Question",
      "name": "Do we need to meet in person?",
      "acceptedAnswer": {{ "@type": "Answer", "text": "No. Most calls, planning sessions, and check-ins happen over screen-share. In-person meetings are available on request for {name} and the rest of South Central PA." }}
    }},
    {{
      "@type": "Question",
      "name": "How is this different from hiring a local web designer?",
      "acceptedAnswer": {{ "@type": "Answer", "text": "A website is one piece of what we build, not the whole engagement. Goldenspire designs the systems behind it too: intake, scheduling, document handling, review requests, and reporting, so the site is connected to how the business actually runs instead of sitting on its own." }}
    }},
    {{
      "@type": "Question",
      "name": "What does this cost?",
      "acceptedAnswer": {{ "@type": "Answer", "text": "Every build is scoped to your business after you reach out, so pricing is never one-size-fits-all. Engagements are structured as a flat project fee, not billed hourly, so you know the full cost before any work starts." }}
    }}
  ]
}}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../styles.css">
</head>
<body>

<a href="#main" class="skip-link">Skip to content</a>

<header>
  <nav>
    <a href="../index.html" class="brand" style="text-decoration:none;">
      <img src="../logo.png" class="brand-mark" alt="Goldenspire icon" style="width:22px; height:auto;">
      Goldenspire Group
    </a>
    <ul>
      <li><a href="../services.html">Services</a></li>
      <li><a href="../approach.html">Approach</a></li>
      <li><a href="../about.html">Background</a></li>
      <li><a href="../industries.html">Who We Serve</a></li>
      <li><a href="../locations.html" style="color:var(--brass);">Locations</a></li>
      <li><a href="../blog/index.html">Blog</a></li>
      <li><a href="../contact.html" class="nav-cta">Get in Touch</a></li>
    </ul>
    <button class="menu-toggle" id="menuToggle" aria-label="Toggle menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </nav>
  <div class="nav-scrim" id="navScrim"></div>
</header>

<section class="page-header" id="main">
  <div class="wrap">
    <span class="breadcrumb"><a href="../index.html">Home</a> / <a href="../locations.html">Locations</a> / {name}, PA</span>
    <h1>AI Automation &amp; Business Systems in {name}, PA</h1>
    <p>{drive} Goldenspire builds the same production-grade automation for {name} businesses as anywhere else we work: customer intake, scheduling, documents, reviews, and reporting, built around how your business actually runs.</p>
  </div>
</section>

<section>
  <div class="wrap" style="max-width:760px;">
    <div class="section-head reveal">
      <span class="mono">{name}, {county}</span>
      <h2>What {name}'s business landscape actually looks like.</h2>
      <p>{character}</p>
    </div>

    <div class="section-head reveal" style="margin-top:40px;">
      <span class="mono">Relevant Industries</span>
      <h2>Industries we hear from most in this area.</h2>
      <p>Click through for the specific problems and fixes we see most often in each.</p>
    </div>
    <div class="industries-grid reveal-stagger" style="margin-bottom:8px;">
{industry_links}
    </div>
    <p style="margin-top:8px;"><a href="../industries.html" style="color:var(--brass); font-weight:600;">See all industries we serve &rarr;</a></p>
  </div>
</section>

<section class="background" style="border-top:1px solid var(--line);">
  <div class="wrap" style="max-width:800px;">
    <div class="section-head reveal">
      <span class="mono">Local, But Not Local-Only</span>
      <h2>Based in Dillsburg. Built to work the same way everywhere.</h2>
      <p>Sean works out of Dillsburg, PA and is glad to meet {name} clients face-to-face when it's useful, but the systems themselves don't care about distance. Every build runs on accounts you own, gets tested the same way, and is supported the same way, whether the client is fifteen minutes away or in another state entirely.</p>
    </div>
  </div>
</section>

<section id="location-faq" style="background:var(--parchment-2); border-top:1px solid var(--line);">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="mono">Questions From {name} Businesses</span>
      <h2>What owners in the area ask before reaching out.</h2>
    </div>
    <div class="services-grid reveal-stagger">
      <div class="service-card" style="text-align:left;">
        <h3 style="margin-bottom:8px;">Do you actually work with businesses in {name}?</h3>
        <p style="color:var(--slate); font-size:0.92rem;">{drive_plain}</p>
      </div>
      <div class="service-card" style="text-align:left;">
        <h3 style="margin-bottom:8px;">Do we need to meet in person?</h3>
        <p style="color:var(--slate); font-size:0.92rem;">No. Most calls, planning sessions, and check-ins happen over screen-share. In-person meetings are available on request for {name} and the rest of South Central PA.</p>
      </div>
      <div class="service-card" style="text-align:left;">
        <h3 style="margin-bottom:8px;">How is this different from hiring a local web designer?</h3>
        <p style="color:var(--slate); font-size:0.92rem;">A website is one piece of what we build, not the whole engagement. Goldenspire designs the systems behind it too: intake, scheduling, document handling, review requests, and reporting, so the site is connected to how the business actually runs instead of sitting on its own.</p>
      </div>
      <div class="service-card" style="text-align:left;">
        <h3 style="margin-bottom:8px;">What does this cost?</h3>
        <p style="color:var(--slate); font-size:0.92rem;">Every build is scoped to your business after you reach out, so pricing is never one-size-fits-all. Engagements are structured as a flat project fee, not billed hourly, so you know the full cost before any work starts.</p>
      </div>
    </div>
  </div>
</section>

<section class="page-cta">
  <div class="wrap">
    <h2>Run a business in {name}? Let's talk about yours.</h2>
    <p>Free consultation, no pitch: just a plain conversation about where automation could save you the most time.</p>
    <a href="../contact.html" class="btn btn-primary">Reach out for a free consultation</a>
    <p style="margin-top:16px;"><a href="../readiness.html" style="color:var(--brass); font-weight:600;">Not ready to talk yet? Take the free 2-minute readiness check &rarr;</a></p>
    <p style="margin-top:24px; font-size:0.85rem;"><a href="../locations.html" style="color:var(--slate);">&larr; See all locations we serve</a></p>
  </div>
</section>

<footer>
  <div class="brand">
    <img src="../logo.png" class="brand-mark" alt="Goldenspire icon" style="width:26px; height:auto;">
    Goldenspire Group
  </div>
  <div class="wrap" style="margin-bottom:6px; font-style:italic; color:rgba(241,234,217,0.7);">Enterprise-grade innovation. Built for your size.</div>
  <div class="wrap">&copy; 2026 Goldenspire Group &middot; Dillsburg, PA</div>
  <div class="wrap" style="margin-top:10px; font-size:0.82rem;">
    <a href="../privacy.html" style="color:rgba(241,234,217,0.55); text-decoration:underline; margin:0 10px;">Privacy Policy</a>
    <a href="../terms.html" style="color:rgba(241,234,217,0.55); text-decoration:underline; margin:0 10px;">Terms of Service</a>
  </div>
</footer>

<script>

  // Mobile menu toggle
  (function(){{
    const toggle = document.getElementById('menuToggle');
    const menu = document.querySelector('nav ul');
    const scrim = document.getElementById('navScrim');
    function closeMenu(){{
      toggle.classList.remove('open');
      menu.classList.remove('open');
      scrim.classList.remove('open');
      toggle.setAttribute('aria-expanded','false');
    }}
    function openMenu(){{
      toggle.classList.add('open');
      menu.classList.add('open');
      scrim.classList.add('open');
      toggle.setAttribute('aria-expanded','true');
    }}
    toggle.addEventListener('click', function(){{
      menu.classList.contains('open') ? closeMenu() : openMenu();
    }});
    scrim.addEventListener('click', closeMenu);
    menu.querySelectorAll('a').forEach(function(a){{
      a.addEventListener('click', closeMenu);
    }});
  }})();

  // Header shadow on scroll
  (function(){{
    const header = document.querySelector('header');
    function onScroll(){{
      if(window.scrollY > 8){{ header.classList.add('scrolled'); }}
      else {{ header.classList.remove('scrolled'); }}
    }}
    window.addEventListener('scroll', onScroll, {{passive:true}});
    onScroll();
  }})();

  // Scroll-reveal
  (function(){{
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const targets = document.querySelectorAll('.reveal, .reveal-stagger');
    if(reduced || !('IntersectionObserver' in window)){{
      targets.forEach(function(el){{ el.classList.add('in-view'); }});
      return;
    }}
    const io = new IntersectionObserver(function(entries){{
      entries.forEach(function(entry){{
        if(entry.isIntersecting){{
          entry.target.classList.add('in-view');
          io.unobserve(entry.target);
        }}
      }});
    }}, {{threshold:0, rootMargin:'0px 0px -40px 0px'}});
    targets.forEach(function(el){{ io.observe(el); }});
  }})();

</script>
</body>
</html>
"""

def hero_sentence(c):
    if c["minutes"] is None:
        return "Dillsburg is home base &mdash; Sean works out of Dillsburg every day."
    return f"{c['name']} is about {c['minutes']} from Dillsburg."

def faq_presence_answer(c):
    if c["minutes"] is None:
        return "Yes, Dillsburg is where Sean and Goldenspire are actually based, not a satellite market. Most of the engagement still happens remotely or by screen-share, the same way it would for any other client."
    return (f"Yes. Sean is based in Dillsburg, PA, about {c['minutes']} from {c['name']}. "
            "Most of the engagement happens remotely regardless of distance, the same way it would for a client anywhere else.")

os.makedirs(os.path.join(ROOT, "locations"), exist_ok=True)

for c in CITIES:
    industry_links = "\n".join(
        f'      <a class="industry-tag" href="../industries/{slug}.html">{INDUSTRY_LABELS[slug]}</a>'
        for slug in c["industries"]
    )
    html = PAGE_TEMPLATE.format(
        name=c["name"],
        slug=c["slug"],
        county=c["county"],
        drive=hero_sentence(c),
        drive_plain=faq_presence_answer(c),
        character=c["character"],
        industry_links=industry_links,
    )
    path = os.path.join(ROOT, "locations", f"{c['slug']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path)

# ---------------------------------------------------------------------------
# Hub page: locations.html
# ---------------------------------------------------------------------------

HUB_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" type="image/png" href="images/favicon.png">
<title>Locations We Serve in South Central PA | Goldenspire Group</title>
<meta name="description" content="Goldenspire Group is based in Dillsburg, PA and builds AI automation and business systems for companies across Cumberland, York, Dauphin, and Lancaster Counties, plus remote clients nationwide.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://goldenspiregroup.com/locations.html">
<meta property="og:type" content="website">
<meta property="og:title" content="Locations We Serve in South Central PA | Goldenspire Group">
<meta property="og:description" content="Goldenspire Group is based in Dillsburg, PA and builds AI automation and business systems for companies across South Central PA, plus remote clients nationwide.">
<meta property="og:url" content="https://goldenspiregroup.com/locations.html">
<meta property="og:site_name" content="Goldenspire Group">
<meta property="og:locale" content="en_US">
<meta property="og:image" content="https://goldenspiregroup.com/images/social-share-banner.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://goldenspiregroup.com/images/social-share-banner.jpg">
<meta name="twitter:title" content="Locations We Serve in South Central PA | Goldenspire Group">
<meta name="twitter:description" content="Goldenspire Group is based in Dillsburg, PA and builds AI automation and business systems for companies across South Central PA, plus remote clients nationwide.">

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Goldenspire Group",
  "url": "https://goldenspiregroup.com",
  "telephone": "+17175022056",
  "email": "info@goldenspiregroup.com",
  "logo": "https://goldenspiregroup.com/logo.png",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Dillsburg",
    "addressRegion": "PA",
    "addressCountry": "US"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": 40.1223, "longitude": -77.0355 },
  "areaServed": [
    "Dillsburg PA", "Mechanicsburg PA", "Carlisle PA", "Camp Hill PA", "York PA", "Harrisburg PA", "Lancaster PA",
    "Cumberland County PA", "York County PA", "Dauphin County PA", "Lancaster County PA",
    "South Central Pennsylvania", "United States (remote engagements)"
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://goldenspiregroup.com/"},
    {"@type": "ListItem", "position": 2, "name": "Locations", "item": "https://goldenspiregroup.com/locations.html"}
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Don't see my town listed?",
      "acceptedAnswer": { "@type": "Answer", "text": "This page covers the markets we hear from most, not a hard boundary. If you're anywhere in South Central PA, or anywhere else, reach out and we'll tell you honestly whether it's a fit." }
    },
    {
      "@type": "Question",
      "name": "Do I need to be near Dillsburg to work with Goldenspire?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. Sean is based in Dillsburg, PA and enjoys meeting nearby clients face-to-face, but the systems run identically whether you're fifteen minutes away or working with us entirely remotely." }
    }
  ]
}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400;9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>

<a href="#main" class="skip-link">Skip to content</a>

<header>
  <nav>
    <a href="index.html" class="brand" style="text-decoration:none;">
      <img src="logo.png" class="brand-mark" alt="Goldenspire icon" style="width:22px; height:auto;">
      Goldenspire Group
    </a>
    <ul>
      <li><a href="services.html">Services</a></li>
      <li><a href="approach.html">Approach</a></li>
      <li><a href="about.html">Background</a></li>
      <li><a href="industries.html">Who We Serve</a></li>
      <li><a href="locations.html" style="color:var(--brass);">Locations</a></li>
      <li><a href="blog/index.html">Blog</a></li>
      <li><a href="contact.html" class="nav-cta">Get in Touch</a></li>
    </ul>
    <button class="menu-toggle" id="menuToggle" aria-label="Toggle menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </nav>
  <div class="nav-scrim" id="navScrim"></div>
</header>

<section class="page-header" id="main">
  <div class="wrap">
    <span class="breadcrumb"><a href="index.html">Home</a> / Locations</span>
    <h1>Based in Dillsburg, PA. Working across South Central PA and beyond.</h1>
    <p>Sean works out of Dillsburg every day, and Goldenspire is glad to meet clients face-to-face across Cumberland, York, Dauphin, and Lancaster Counties. Most of the work happens remotely regardless of distance, so a client five minutes away and a client five states away get the same build. Click any location below for what we see most often in that market.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="industries-grid reveal-stagger" style="margin-bottom:56px;">
{tag_links}
    </div>

    <div class="section-head reveal">
      <span class="mono">By Location</span>
      <h2>What we see, market by market.</h2>
      <p>Every business is different, but the local economy shapes which problems show up most. Illustrative context based on the region, not claims about a specific past client.</p>
    </div>
    <div class="services-grid reveal-stagger">
{cards}
    </div>
  </div>
</section>

<section class="photo-break reveal">
  <img src="images/downtown-main-street.jpg" alt="Small-town Main Street with local independent storefronts" loading="lazy" width="700" height="393">
  <div class="photo-break-content">
    <span class="mono">Local Roots, Not a Local Ceiling</span>
    <p>"Being based in Dillsburg means I know what a Main Street business actually deals with. It doesn't mean that's the only kind of business we build for."</p>
    <div class="attribution">Sean, Goldenspire Group</div>
  </div>
</section>

<section id="locations-faq" style="background:var(--parchment-2); border-top:1px solid var(--line);">
  <div class="wrap">
    <div class="section-head reveal">
      <span class="mono">Questions About Coverage</span>
      <h2>What business owners ask about where we work.</h2>
    </div>
    <div class="services-grid reveal-stagger">
      <div class="service-card" style="text-align:left;">
        <h3 style="margin-bottom:8px;">Don't see my town listed?</h3>
        <p style="color:var(--slate); font-size:0.92rem;">This page covers the markets we hear from most, not a hard boundary. If you're anywhere in South Central PA, or anywhere else, reach out and we'll tell you honestly whether it's a fit.</p>
      </div>
      <div class="service-card" style="text-align:left;">
        <h3 style="margin-bottom:8px;">Do I need to be near Dillsburg to work with Goldenspire?</h3>
        <p style="color:var(--slate); font-size:0.92rem;">No. Sean is based in Dillsburg, PA and enjoys meeting nearby clients face-to-face, but the systems run identically whether you're fifteen minutes away or working with us entirely remotely.</p>
      </div>
    </div>
  </div>
</section>

<section class="page-cta">
  <div class="wrap">
    <h2>Don't see your town?</h2>
    <p>This list covers our most common markets, not a hard limit. Reach out and let's talk about where you're based.</p>
    <a href="contact.html" class="btn btn-primary">Reach out for a free consultation</a>
    <p style="margin-top:16px;"><a href="readiness.html" style="color:var(--brass); font-weight:600;">Not ready to talk yet? Take the free 2-minute readiness check &rarr;</a></p>
  </div>
</section>

<footer>
  <div class="brand">
    <img src="logo.png" class="brand-mark" alt="Goldenspire icon" style="width:26px; height:auto;">
    Goldenspire Group
  </div>
  <div class="wrap" style="margin-bottom:6px; font-style:italic; color:rgba(241,234,217,0.7);">Enterprise-grade innovation. Built for your size.</div>
  <div class="wrap">&copy; 2026 Goldenspire Group &middot; Dillsburg, PA</div>
  <div class="wrap" style="margin-top:10px; font-size:0.82rem;">
    <a href="privacy.html" style="color:rgba(241,234,217,0.55); text-decoration:underline; margin:0 10px;">Privacy Policy</a>
    <a href="terms.html" style="color:rgba(241,234,217,0.55); text-decoration:underline; margin:0 10px;">Terms of Service</a>
  </div>
</footer>

<script>

  // Mobile menu toggle
  (function(){
    const toggle = document.getElementById('menuToggle');
    const menu = document.querySelector('nav ul');
    const scrim = document.getElementById('navScrim');
    function closeMenu(){
      toggle.classList.remove('open');
      menu.classList.remove('open');
      scrim.classList.remove('open');
      toggle.setAttribute('aria-expanded','false');
    }
    function openMenu(){
      toggle.classList.add('open');
      menu.classList.add('open');
      scrim.classList.add('open');
      toggle.setAttribute('aria-expanded','true');
    }
    toggle.addEventListener('click', function(){
      menu.classList.contains('open') ? closeMenu() : openMenu();
    });
    scrim.addEventListener('click', closeMenu);
    menu.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', closeMenu);
    });
  })();

  // Header shadow on scroll
  (function(){
    const header = document.querySelector('header');
    function onScroll(){
      if(window.scrollY > 8){ header.classList.add('scrolled'); }
      else { header.classList.remove('scrolled'); }
    }
    window.addEventListener('scroll', onScroll, {passive:true});
    onScroll();
  })();

  // Scroll-reveal
  (function(){
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const targets = document.querySelectorAll('.reveal, .reveal-stagger');
    if(reduced || !('IntersectionObserver' in window)){
      targets.forEach(function(el){ el.classList.add('in-view'); });
      return;
    }
    const io = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(entry.isIntersecting){
          entry.target.classList.add('in-view');
          io.unobserve(entry.target);
        }
      });
    }, {threshold:0, rootMargin:'0px 0px -40px 0px'});
    targets.forEach(function(el){ io.observe(el); });
  })();

</script>
</body>
</html>
"""

tag_links = "\n".join(
    f'      <a class="industry-tag" href="locations/{c["slug"]}.html">{c["name"]}, PA</a>'
    for c in CITIES
)
cards = "\n".join(
    f'''      <a class="service-card industry-teaser" style="text-align:left; display:block; text-decoration:none;" href="locations/{c["slug"]}.html">
        <h3 style="margin-bottom:14px;">{c["name"]}, PA</h3>
        <span class="mono" style="color:var(--brass); display:block; margin:0 0 6px;">{c["county"]}</span>
        <p style="margin-bottom:0; color:var(--slate); font-size:0.92rem;">{LOCATION_TEASERS[c["slug"]]}</p>
        <span style="display:inline-block; margin-top:16px; color:var(--brass); font-weight:600; font-size:0.88rem;">See what we build here &rarr;</span>
      </a>'''
    for c in CITIES
)
hub_html = HUB_TEMPLATE.replace('{tag_links}', tag_links).replace('{cards}', cards)
hub_path = os.path.join(ROOT, "locations.html")
with open(hub_path, "w", encoding="utf-8") as f:
    f.write(hub_html)
print("wrote", hub_path)
