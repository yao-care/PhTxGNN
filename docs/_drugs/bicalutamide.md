---
layout: default
title: Bicalutamide
parent: Moderate Evidence (L3-L4)
nav_order: 44
evidence_level: L4
indication_count: 10
last_modified_at: 2026-11-12
description: "Bicalutamide: predicted new indication Hypertrichosis (evidence level L4). Approved use: Not recorded in the Philippines registration data"
monitor_inn: "Bicalutamide"
predicted_indications: ["hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "Ambras type hypertrichosis universalis congenita", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "leprosy", "multiple endocrine neoplasia", "pulmonary hypertension", "female breast carcinoma", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Bicalutamide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Bicalutamide: From Androgen Receptor Blockade to Hypertrichosis
{: .text-alpha }

## One-Sentence Summary

Bicalutamide is a nonsteroidal androgen receptor (AR) antagonist. The registration data compiled for this report do not record its original approved indication.
The TxGNN model predicts it may be useful for **hypertrichosis**, but there are **0 clinical trials** and only **1 publication**, which is a commentary letter, supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Philippines registration data |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 0.9969 |
| Evidence Level | L4 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled database record. Bicalutamide is known as a nonsteroidal AR antagonist. Androgen signalling drives terminal hair growth in androgen-sensitive areas of the body, so blocking the AR is plausible for hirsutism-like or drug-induced hypertrichosis.

The only supporting literature is a commentary on a retrospective review of 35 patients. That review looked at bicalutamide for minoxidil-induced hypertrichosis in female pattern hair loss. This is indirect, secondary evidence, and no primary trial data were available for this report.

The rationale is weaker for congenital forms of hypertrichosis. These are not clearly androgen-mediated, so the high model score should not be read as evidence of benefit across all hypertrichosis types.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35304167](https://pubmed.ncbi.nlm.nih.gov/35304167/) | 2022 | Comment/Letter | Journal of the American Academy of Dermatology | Commentary on a retrospective review of 35 patients using bicalutamide for minoxidil-induced hypertrichosis in female pattern hair loss. No abstract or primary data were available. |

---

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Bicalutamide | Oral |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

---

## Safety Considerations

- **Disease associations from the knowledge graph (not label text):** The TxGNN knowledge graph links bicalutamide to contraindication-type relationships with the following conditions. These should be checked against the official package insert.
  - Liver disease and drug-induced liver injury
  - Gallbladder disease
  - Hyperglycaemia, diabetes mellitus and diabetic ketoacidosis
  - Anaemia, including macrocytic anaemia
  - Interstitial lung disease
- **Drug Interactions:** The interaction query returned 100 interactions in total, and the first 20 were reviewed.
  - **Major:** cisapride and dolasetron.
  - **Moderate:** famotidine, loperamide, aprepitant, bisacodyl, budesonide (including nasal), castor oil, clarithromycin, eliglustat, glycerin, granisetron, lactitol, lactulose, levofloxacin, magnesium citrate, magnesium hydroxide and mineral oil.
  - **Minor:** metronidazole.

<!-- review:begin ph-lic-20261106-bicalutamide-3 -->

> **Review correction (2026-11-06)**: Originally stated: "Dosage form and approved indication are not recorded for this authorization." Removed: its description of the Philippine products did not match the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-bicalutamide-3 -->

Please refer to the package insert for warnings and label-based contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score and a single commentary letter, with no clinical trials. The mechanistic link is plausible only for androgen-driven or drug-induced hypertrichosis.

<!-- review:begin ph-lic-20261106-bicalutamide-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug is marketed in the Philippines, with 1 valid license out of 1, and the mechanistic link is plausible only for androgen-driven or drug-induced hypertrichosis." Removed: the number or status of PNF entries stated here did not match the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-bicalutamide-2 -->

For context, a lower-ranked prediction in the same data, **female breast carcinoma** (score 0.9911), has stronger support. It has one active Phase 2 trial (NCT03650894, bicalutamide with nivolumab and ipilimumab) and substantial preclinical literature on AR-positive triple-negative breast cancer. It was assessed at evidence level L2 with a "Proceed with Guardrails" recommendation, and may be a better candidate for further evaluation.

**To proceed, the following is needed:**
- The primary study behind the commentary (the 35-patient retrospective review) and any controlled data in hypertrichosis
- Clarification of which hypertrichosis subtype is targeted (drug-induced or androgen-related versus congenital)
- Detailed mechanism of action data
- The original approved indication and package insert warnings, contraindications and dosage forms from the DOH-FDA Philippines record
- A safety plan covering liver function and the major drug interactions

<!-- review:begin ph-lic-20261031-bicalutamide-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The original approved indication and package insert warnings, contraindications and dosage forms from the DOH-FDA Philippines record / Confirmation of regulatory status, since the only registration found is cancelled" Removed: it said the PNF entries were cancelled, discontinued, or not current, which did not match the PNF data (the Philippine National Formulary as of 2026-10-31). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261031-bicalutamide-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "Confirmation of regulatory status, since the only registration found is cancelled" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |
| 2026-11-06 | Removed: "he drug is marketed in the Philippines, with 1 valid license out of 1, and t" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |
| 2026-11-06 | Removed: "Dosage form and approved indication are not recorded for this authorization" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

