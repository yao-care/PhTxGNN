---
layout: default
title: Desmopressin
parent: Model Prediction Only (L5)
nav_order: 102
evidence_level: L5
indication_count: 6
monitor_inn: "Desmopressin"
predicted_indications: ["congenital prothrombin deficiency", "inherited thrombophilia", "Glanzmann thrombasthenia", "primary release disorder of platelets", "Scott syndrome", "flood factor deficiency"]
last_modified_at: 2026-10-28
description: "Desmopressin: predicted new indication congenital prothrombin deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Desmopressin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Desmopressin: Synthetic vasopressin analogue → congenital prothrombin deficiency
{: .text-alpha }

## One-Sentence Summary

Desmopressin is a synthetic vasopressin analogue that is registered in the Philippines.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, with a score of 0.9970.
There are **no registered clinical trials** and only **1 publication** (a 1993 general review), so the evidence is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | congenital prothrombin deficiency |
| TxGNN Prediction Score | 0.9970 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, desmopressin raises plasma factor VIII and von Willebrand factor by releasing them from endothelial cells, which improves primary hemostasis.

Prothrombin (factor II) is not known to be released through this pathway, so there is no clear mechanistic rationale for congenital prothrombin deficiency. The only literature is a 1993 general review of congenital bleeding disorders and it does not study this disease directly. The high score probably reflects the model's proximity to other bleeding disorders rather than a specific effect. Because no cited study addresses this disease itself, the evidence level is L5.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7684674](https://pubmed.ncbi.nlm.nih.gov/7684674/) | 1993 | Review | Drugs | General overview of rational treatment options for common inherited bleeding disorders (haemophilia A, von Willebrand disease); does not address prothrombin deficiency specifically |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0136 | Desmopressin | Not recorded | Not recorded |

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction database. The main ones are:
  - **Major**: hydrocortisone, triamcinolone, dexamethasone, beclomethasone dipropionate, betamethasone, budesonide, prednisolone, prednisone
  - **Moderate**: epinephrine, loperamide, morphine (including liposomal), opium, chlorpropamide
  - **Minor**: acetylsalicylic acid
- **Conditions flagged as contraindicated or to be avoided in the drug-disease records**: hypertension, coronary artery disease, impaired renal function, cystic fibrosis, allergic and vasomotor rhinitis, pharyngitis, common cold, respiratory tract infection, polydipsia, dipsogenic diabetes insipidus and water intoxication. These come from database records, not from the package insert.
- Hyponatremia and, rarely, arterial thrombotic events are known concerns with desmopressin use in bleeding disorders.

Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial, no disease-specific study and no clear mechanistic link between desmopressin and congenital prothrombin deficiency. The model score alone is not enough to justify further work.

**To proceed, the following is needed:**
- Any direct clinical or preclinical evidence in prothrombin (factor II) deficiency
- A defined mechanistic rationale, since the VWF/FVIII release pathway does not act on prothrombin
- Detailed mechanism of action data
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Local licence details (dosage form, approved indication)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

