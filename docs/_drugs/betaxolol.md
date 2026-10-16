---
layout: default
title: Betaxolol
parent: Model Prediction Only (L5)
nav_order: 43
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Betaxolol: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Hypertension, open-angle glaucoma, ocular hypertension"
---

# Betaxolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Betaxolol: From Hypertension and Open-Angle Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Betaxolol is a beta-1 selective adrenergic blocker originally used for hypertension, open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, open-angle glaucoma, ocular hypertension (the Philippines licence record contains no indication text) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, betaxolol is a beta-1 selective adrenergic antagonist. It is already used for open-angle glaucoma and ocular hypertension, and it lowers intraocular pressure (IOP) by reducing aqueous humour production.

Elevated IOP is also a key driver of optic neuropathy in primary hereditary glaucoma, so a plausible mechanistic link exists. However, the very high score (0.997) likely reflects the close similarity to the approved glaucoma indications in the knowledge graph rather than independent evidence.

There are also limits to how far this applies. Primary hereditary glaucoma, including congenital and juvenile forms, often involves anatomical angle abnormalities that are treated surgically. Topical beta-blockers are generally only adjunctive. In children, systemic absorption of a beta-blocker also raises safety concerns such as bradycardia and bronchospasm.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0049 | Betaxolol | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (drug–disease contraindication links, not package insert text): 
  - Respiratory: asthma (including intrinsic and allergic asthma), pulmonary emphysema, bronchial disease
  - Cardiac: atrioventricular block and atrioventricular dissociation
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, hypoglycaemia
  - Neuromuscular: myasthenia gravis and neuromuscular junction disease
  - Tumours: phaeochromocytoma and related adrenal or paraganglioma tumours
  - Other: kidney disease, liver disease, gallbladder disease, psoriasis, anxiety and related mood disorders
- **Drug Interactions**: The interaction screen returned 100 records; the 20 reviewed are mostly Moderate, with a few Minor. Notable Moderate interactions include:
  - Epinephrine
  - Corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide)
  - Anticholinergics (atropine, hyoscyamine)
  - Bupropion
  - Morphine
  - Acetohexamide
  - Calcium salts

  Minor interactions include acetylsalicylic acid, aluminium hydroxide and attapulgite.
- Package insert warnings and contraindications were not available for this report. Please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications (Evidence Level L5). The only registration in the Philippines is cancelled. The proposed indication is typically managed surgically, and paediatric systemic beta-blockade carries safety risks.

**To proceed, the following is needed:**
- Search for and assess clinical or observational evidence of betaxolol in primary hereditary glaucoma, including paediatric data
- Obtain the package insert warnings and contraindications from DOH-FDA Philippines
- Obtain mechanism of action data (for example from DrugBank)
- Clarify why the registration was cancelled and whether any ophthalmic formulation is available in the Philippines
- Develop a safety plan for paediatric and high-risk groups (asthma, cardiac conduction disorders, diabetes)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

