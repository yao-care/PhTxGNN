---
layout: default
title: Privacy Policy
nav_order: 95
permalink: /privacy-policy/
description: "PhTxGNN privacy policy: a static site with no accounts or forms; it uses Google Analytics 4 analytics cookies for usage statistics."
---

# Privacy Policy

<div class="key-takeaway">
This is a static site — no registration and no forms. It uses Google Analytics 4 analytics cookies to compile usage statistics.
</div>

---

## What we collect

<p class="key-answer" data-question="Does PhTxGNN collect personal data?">
<strong>Only usage statistics, through Google Analytics 4.</strong> This site is hosted on GitHub Pages as a purely static site.
There is no account system and there are no forms, and we do not collect names, email addresses or medical
records. The site uses Google Analytics 4 analytics cookies to compile usage statistics (pages viewed, referrer,
scroll depth and time on page). The cookies are set when a page loads; search terms, form contents and URL
query strings are not sent.
</p>

---

## Third-party services

The site uses the following third-party resources, which may log access according to their own
policies:

| Service | Purpose | Privacy policy |
|---------|---------|----------------|
| GitHub Pages | Site hosting | [GitHub Privacy Statement](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement) |
| Google Analytics 4 (www.googletagmanager.com, google-analytics.com) | Visit statistics (pages viewed, referrer); uses analytics cookies. Search terms, form contents and URL query strings are not sent. | [Google Privacy Policy](https://policies.google.com/privacy) |
| cdn.jsdelivr.net | Script libraries: d3 charts on every page; Fuse.js name matching and the SMART on FHIR client on the SMART pages | [jsDelivr Privacy Policy](https://www.jsdelivr.com/terms/privacy-policy-jsdelivr-net) |
| clinicaltrials.gov | Clinical-trial lookup on the SMART pages: only when you ask for trials, the drug and indication names are sent to the ClinicalTrials.gov API | [NLM Web Policies](https://www.nlm.nih.gov/web_policies.html) |
| rxnav.nlm.nih.gov | SMART app: the RxNorm codes of the medications read from your EHR are sent to the NLM RxNav API to look up ingredient names (no patient identifiers) | [NLM Web Policies](https://www.nlm.nih.gov/web_policies.html) |

When you actively launch the SMART on FHIR app, it requests medication data from your electronic
health record system. Patient identity and EHR data are <strong>not sent to this site's servers</strong> (this is a
static site with no backend) and are not stored by this site. To match drug names, the app sends the
medications' RxNorm codes to the US National Library of Medicine's RxNav service; these codes contain no
patient identifiers. When you ask for clinical trials, the drug and indication names are sent to ClinicalTrials.gov.

---

<!-- privacy-law:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改；法規與連結見 .claude/privacy_text_20261119.py）-->
## Applicable law

For visitors in the Philippines the relevant law is the [Data Privacy Act of 2012 (Republic Act No. 10173)](https://lawphil.net/statutes/repacts/ra2012/ra_10173_2012.html) and its implementing rules, enforced by the [National Privacy Commission](https://privacy.gov.ph/). The site collects no names or health records; the usage data from Google Analytics 4 cookies is the only personal information involved.

## Your rights and how to use them

- Right to be informed and to object to processing.
- Right to access and to correct (rectify) your data.
- Right to erasure or blocking, and to data portability.
- Right to lodge a complaint with the National Privacy Commission.

Requests: service@yao.care (there are no accounts, so tell us the date and pages of your visit). Analytics cookies can be blocked or deleted in your browser.

## Copyright and data sources

Site texts are protected under the [Intellectual Property Code of the Philippines (Republic Act No. 8293)](https://lawphil.net/statutes/repacts/ra1997/ra_8293_1997.html). The site's code is published under the MIT License in the [GitHub repository](https://github.com/yao-care/PhTxGNN); report texts are © 藥提醒科技有限公司 (yao.care).

Data sources used on this site and their terms:

- **TxGNN** data (Harvard Dataverse): CC0 1.0; cite Huang et al., *Nature Medicine* 2024.
- **ClinicalTrials.gov**, **PubMed**: [ClinicalTrials.gov terms](https://clinicaltrials.gov/about-site/terms-conditions), [NCBI policies](https://www.ncbi.nlm.nih.gov/home/about/policies/).
- **DrugBank**: [DrugBank](https://go.drugbank.com/) licence terms, non-commercial use.
- **Local dataset** – [Philippine National Formulary](https://www.doh.gov.ph/philippine-national-formulary), published by Department of Health (Philippines); reuse is governed by the publisher's terms, and this site does not grant any further rights.

<!-- privacy-law:end -->

---

## Changes to this policy

Any changes will be published directly on this page.

---

## About the Developer

This platform is developed and operated by **藥提醒科技有限公司** (yao.care). See the
<a href="{{ '/about/' | relative_url }}">About</a> page for the full company and methodology background.

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
This report is for academic research reference only and <strong>does not constitute medical advice</strong>. Always follow your physician's instructions; never adjust medication on your own. Any drug repurposing decision requires full clinical validation and regulatory review.
<br><br>
<small>Reviewed by: 藥提醒科技有限公司 (yao.care)</small>
</div>
