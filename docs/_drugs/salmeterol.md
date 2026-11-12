---
layout: default
title: Salmeterol
parent: Model Prediction Only (L5)
nav_order: 307
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
monitor_inn: "Salmeterol"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome", "atopic eczema"]
description: "Salmeterol: predicted new indication Respiratory malformation (evidence level L5). Approved use: Not recorded in the local data"
---

# Salmeterol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Salmeterol: Respiratory malformation
{: .text-alpha }

## One-Sentence Summary

Salmeterol is an inhaled long-acting beta2-adrenergic agonist (bronchodilator). The TxGNN model predicts it may be relevant to **respiratory malformation**, with a score of **0.9991**. No clinical trial or publication in the data compiled for this report studies this disease directly, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Respiratory malformation |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Salmeterol belongs to the long-acting beta2-agonist class. Drugs in this class relax airway smooth muscle and may improve mucociliary clearance.

The link to respiratory malformation is indirect. These effects are symptomatic. They may help airway function or secretion clearance in some chronic respiratory conditions, but they do not correct structural malformation. The high score probably reflects the model's closeness between the drug and respiratory diseases in general, not an established causal mechanism. The prediction should be treated as a hypothesis, not as support for clinical use.

## Clinical Trial Evidence

No registered trial studies respiratory malformation. The two trials below were retrieved as the closest matches, and both address different conditions.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00005110](https://clinicaltrials.gov/study/NCT00005110) | Not applicable | Suspended | Not reported | Long-term salmeterol vs albuterol or placebo, inhaled twice daily for 6 months, in cystic fibrosis. A different disease from the prediction. |
| [NCT01681979](https://clinicaltrials.gov/study/NCT01681979) | Not specified | Completed | 1 | Asthma treatment in pregnancy and adverse pregnancy outcomes. A single participant, so not informative for this prediction. |

## Literature Evidence

No publication addresses respiratory malformation directly. The items below are the closest related reports.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34902004](https://pubmed.ncbi.nlm.nih.gov/34902004/) | 2022 | RCT | JAMA Pediatrics | Inhaled corticosteroids alone or combined with long-acting beta2-agonists for reduced lung function in preterm-born children. This is a related lung-function problem, not a malformation. |
| [20703071](https://pubmed.ncbi.nlm.nih.gov/20703071/) | 2010 | Case report | Arerugi | An 18-year-old with primary ciliary dyskinesia who was long treated as having asthma. It illustrates ciliary dysfunction but does not test salmeterol. |

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Fluticasone (as propionate) + Salmeterol (as xinafoate) | Inhalation, Inhalation (DPI), Inhalation (MDI) |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: The data compiled for this report list 100 interaction records. Examples by level:
  - **Major**: clarithromycin.
  - **Moderate**: epinephrine, isometheptene, diethylpropion, dolasetron, famotidine, and several glucose-lowering drugs (acarbose, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, empagliflozin, albiglutide, dulaglutide).
  - **Minor**: corticosteroids such as hydrocortisone, dexamethasone, budesonide and beclomethasone.

Please refer to the package insert for warnings and contraindications. The local package insert has not yet been reviewed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The score is high (0.9991), but no trial or publication studies respiratory malformation directly, and the proposed mechanism is indirect and symptomatic. The evidence level is therefore L5.

**To proceed, the following is needed:**
- Mechanism of action data and a defined biological rationale linking beta2-agonism to the malformation phenotype
- Clinical or preclinical studies in respiratory malformation
- Review of the local package insert for warnings and contraindications (including the major interaction with clarithromycin)
- The approved indication and dosage form

<!-- review:begin ph-lic-20261106-salmeterol-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The approved indication and dosage form for licence PNF-xxxx" Removed: the number or status of PNF entries stated here did not match the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. "PNF-xxxx" stands for a code an earlier version of this site's software assigned to the record; the PNF has no entry numbers, so the code is not shown. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-salmeterol-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "for licence PNF-xxxx" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

