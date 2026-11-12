---
layout: default
title: Salbutamol
parent: Model Prediction Only (L5)
nav_order: 305
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-12
monitor_inn: "Salbutamol"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "anaphylaxis", "common cold", "atopic conjunctivitis", "anorectal stricture"]
description: "Salbutamol: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Salbutamol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Salbutamol: Papillary conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Salbutamol is a beta-2 adrenergic agonist, originally used for asthma and bronchial disease.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but **no clinical trials and no publications** were found for this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 (model prediction only) |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 2) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Salbutamol belongs to the beta-2 agonist class. Its efficacy in asthma and bronchial disease comes from relaxing airway smooth muscle.

Beta-2 agonism could also plausibly dampen mast cell mediator release in allergic eye disease. Papillary conjunctivitis is an allergic or inflammatory eye condition, so a link is conceivable. This is speculative and is not supported by any evidence retrieved for papillary conjunctivitis itself.

Older preclinical work on a related condition, atopic conjunctivitis, reported that topical salbutamol suppressed immediate allergic conjunctivitis in guinea pigs (PMID 3666475). That is indirect, animal-only evidence and does not establish efficacy in humans. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Salbutamol (as sulfate) | Oral, Inhalation, Breath Actuated MDI, Resp. Soln. |
| Ipratropium + Salbutamol | Inhalation, Inhalation (MDI), Resp. Soln. |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

No ophthalmic (eye) route is documented either, and route compatibility for the proposed indication has not been assessed.

<!-- review:begin ph-lic-20261031-salbutamol-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The only record is cancelled, and no dosage form or approved indication text is on file. No ophthalmic (eye) route is documented either, and route compatibility for the proposed indication has not been assessed." Removed: it said the PNF entries were cancelled, discontinued, or not current, which did not match the PNF data (the Philippine National Formulary as of 2026-10-31). The PNF lists 2 entries for this drug, 2 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261031-salbutamol-1 -->

## Safety Considerations

No package insert warnings or contraindications are available for the Philippine registration. The items below come from other sources.

- **Knowledge-graph contraindications** (not label text): hypertension, long QT syndrome, heart conduction disease, sudden cardiac arrest, myocardial ischemia, coronary artery disease, epilepsy, potassium deficiency, diabetes mellitus, diabetic ketoacidosis, metabolic or other acidosis, hyperthyroidism (including Graves disease and thyrotoxicosis), benign prostatic hyperplasia, bladder neck obstruction, ocular hypertension, and angle-closure glaucoma.
  - The two glaucoma-related entries (ocular hypertension, angle-closure glaucoma) deserve particular attention if any ocular use were considered.
- **Drug interactions** (100 interactions recorded; main ones shown):
  - Moderate: epinephrine, clarithromycin, cisapride, isometheptene, famotidine, bisacodyl, castor oil, diethylpropion.
  - Moderate, with antidiabetic agents: acarbose, acetohexamide, albiglutide, alogliptin, canagliflozin, chlorpropamide, dapagliflozin.
  - Minor: corticosteroids (hydrocortisone, beclomethasone, betamethasone, budesonide, dexamethasone).
- **Other**: a case report describes anaphylaxis to salbutamol itself (PMID 18447148), so hypersensitivity is a recognized, if rare, concern.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for papillary conjunctivitis is supported only by a high model score (L5). There are no trials or publications, and the mechanism is speculative.

<!-- review:begin ph-lic-20261106-salbutamol-2 -->

> **Review correction (2026-11-06)**: Originally stated: "There are no trials or publications, and the mechanism is speculative. The product is also not currently registered in the Philippines." Removed: it conflicted with the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 2 entries for this drug, 2 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-salbutamol-2 -->

**To proceed, the following is needed:**
- Preclinical or early human studies of topical or ocular salbutamol in papillary or allergic conjunctivitis, including ocular safety (intraocular pressure, glaucoma risk)
- Mechanism of action data and an assessment of route compatibility (an ophthalmic formulation)
- Package insert warnings and contraindications, plus the registration status and regulatory pathway in the Philippines

**Other predictions in the data compiled for this report** have more evidence than papillary conjunctivitis:
- **Obstructive lung disease (L1):** it includes a completed Phase 3 trial (n=1,118) of an ipratropium/salbutamol combination. This is largely an extension of the original respiratory use rather than true repurposing.
- **Anaphylaxis (L3):** its only Phase 3 trial was terminated early (n=24).

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "The only record is cancelled, and no dosage form or approved indication text is on file" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |
| 2026-11-06 | Removed: "The product is also not currently registered in the Philippines" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

