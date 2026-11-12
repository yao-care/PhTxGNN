---
layout: default
title: Mupirocin
parent: Model Prediction Only (L5)
nav_order: 243
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
description: "Mupirocin: predicted new indication Pleural empyema (evidence level L5). Approved use: Impetigo, bullous impetigo"
monitor_inn: "Mupirocin"
predicted_indications: ["pleural empyema (disease)", "punctate epithelial keratoconjunctivitis"]
---

# Mupirocin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Mupirocin: From Impetigo to Pleural Empyema
{: .text-alpha }

## One-Sentence Summary

Mupirocin is a topical antibiotic originally used to treat impetigo and bullous impetigo.
The TxGNN model predicts it may be effective for **pleural empyema**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Impetigo, bullous impetigo |
| Predicted New Indication | Pleural empyema |
| TxGNN Prediction Score | 0.9949 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, mupirocin is a topical antibiotic that inhibits bacterial isoleucyl-tRNA synthetase. It is mainly active against Gram-positive organisms such as *Staphylococcus aureus*, including MRSA. Its efficacy in impetigo, a skin infection commonly caused by these organisms, is established.

Pleural empyema is often caused by similar Gram-positive bacteria, so a pathogen-level link is plausible. However, this link is speculative. Mupirocin is formulated for topical use and is not suitable for systemic or intrapleural delivery. There is no established pharmacokinetic route for it to reach the pleural space. The prediction is supported only by the model score.

A second predicted indication, punctate epithelial keratoconjunctivitis (score 0.9910), is also at Evidence Level L5 with a Hold recommendation. This condition is often viral (adenovirus), which an antibacterial mechanism would not be expected to address. Mupirocin is also not formulated for ophthalmic use, so ocular tolerability is unknown.

---

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Mupirocin | Cream, Ointment |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

---

## Safety Considerations

- **Disease-level contraindication signal (knowledge graph, not label text)**: dermatitis

- **Drug Interactions**: The interaction screen returned 100 potentially interacting drugs, but none has a severity grade (all are "Unknown"). Examples include calcitriol, clotrimazole, morphine, metformin, pantoprazole, omeprazole, vancomycin, triamcinolone, prednisone, simvastatin, and rosuvastatin. These entries should be reviewed and graded before any clinical use.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high TxGNN score, with no clinical trials or literature. Mupirocin's topical formulation has no established route for pleural delivery.

<!-- review:begin ph-lic-20261031-mupirocin-1 -->

> **Review correction (2026-10-31)**: Originally stated: "Mupirocin's topical formulation has no established route for pleural delivery. In addition, the only Philippines registration is cancelled." Removed: it said the PNF entries were cancelled, discontinued, or not current, which did not match the PNF data (the Philippine National Formulary as of 2026-10-31). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261031-mupirocin-1 -->

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Detailed mechanism of action data
- Preclinical or clinical evidence for pleural empyema, including pleural penetration data and a feasible route of administration
- Grading of the drug interactions (currently all "Unknown")

<!-- review:begin ph-lic-20261031-mupirocin-2 -->

> **Review correction (2026-10-31)**: Originally stated: "Grading of the drug interactions (currently all "Unknown") / Clarification of the regulatory status, since the only registration is cancelled" Removed: it said the PNF entries were cancelled, discontinued, or not current, which did not match the PNF data (the Philippine National Formulary as of 2026-10-31). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261031-mupirocin-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "In addition, the only Philippines registration is cancelled" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |
| 2026-10-31 | Removed: "Clarification of the regulatory status, since the only registration is cancelled" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

