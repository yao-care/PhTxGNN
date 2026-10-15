---
layout: default
title: Theophylline
parent: Model Prediction Only (L5)
nav_order: 334
evidence_level: L5
indication_count: 7
---

# Theophylline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Theophylline: From Asthma and Chronic Airway Disease to Thrombotic Disease

## One-Sentence Summary

Theophylline is a long-established bronchodilator used for asthma, bronchitis, emphysema and other airway diseases.
The TxGNN model predicts it may be effective for **thrombotic disease**, but this rests on a model prediction alone: there are **0 clinical trials** and **19 retrieved publications**, none of which shows an antithrombotic effect of theophylline.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, bronchitis, pulmonary emphysema and related airway or lung diseases (from the knowledge graph; no indication text is recorded on the local licence) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 (model prediction only) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Theophylline is a non-selective phosphodiesterase (PDE) inhibitor and an adenosine receptor antagonist. In airway smooth muscle, these actions produce bronchodilation, which is the basis of its original use.

In platelets, PDE inhibition raises cAMP, which can in theory reduce platelet aggregation. Platelets are central to arterial thrombosis, so this is a plausible, though purely theoretical, reason for the model to link theophylline with thrombotic disease. Related experimental work, such as the milrinone and adenosine platelet study (PMID 8981060), shows that raising cAMP can inhibit platelet responses. That study did not test theophylline.

The retrieved literature does not close this gap. It is mostly about platelet biomarkers, blood-sampling methods (where theophylline is only an additive in collection tubes), ticlopidine pharmacokinetics and a theophylline detection sensor. The older studies on a theophylline derivative (theophylline nicotinate) in peripheral and cerebral vascular disease are not studies of theophylline itself. The high TxGNN score therefore remains an unconfirmed hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the retrieved publications evaluates theophylline as an antithrombotic treatment. The most relevant items are listed below. Summaries for items with no abstract are based on the title only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clinical Pharmacokinetics | Pharmacokinetics of ticlopidine, an antiplatelet drug; does not involve theophylline |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Critical Reviews in Biochemistry | Thromboxane A2 and prostacyclin in platelets and atherosclerosis; prostacyclin acts by raising platelet cAMP, the pathway theophylline could in theory influence |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Unclassified | General Pharmacology | Milrinone (a PDE inhibitor) and adenosine reduce human platelet aggregation through cAMP; theophylline not tested |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Unclassified | British Journal of Haematology | Platelet factor 4 assay; theophylline is only an ingredient of the sample anticoagulant |
| [29220362](https://pubmed.ncbi.nlm.nih.gov/29220362/) | 2017 | Unclassified | PLoS One | Optimized plasma preparation for platelet-stored molecules; a methods paper |
| [6241135](https://pubmed.ncbi.nlm.nih.gov/6241135/) | 1984 | Unclassified | Cor et Vasa | T-lymphocyte subsets in vascular disease; theophylline is used as a laboratory marker, not as a treatment |
| [4776567](https://pubmed.ncbi.nlm.nih.gov/4776567/) | 1973 | Unclassified | Minerva Cardioangiologica | Theophylline nicotinate derivative in chronic obliterating peripheral arteriopathy (title only; a different compound) |
| [5136470](https://pubmed.ncbi.nlm.nih.gov/5136470/) | 1971 | Unclassified | Cardiologia Pratica | Cardiocirculatory effects of a theophylline nicotinate ester in cerebral and peripheral angiopathy (title only; a different compound) |
| [5605983](https://pubmed.ncbi.nlm.nih.gov/5605983/) | 1967 | Unclassified | Annali di Ottalmologia e Clinica Oculistica | Theophylline nicotinate in retinal vascular disease (title only; a different compound) |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Analytical/sensor method | Analytica Chimica Acta | Electrochemical aptasensor for theophylline detection; no therapeutic data |

---

## Philippines Market Information

| Authorization Number | Product Name | Type | Status |
|---------|------|------|-----------|
| PNF-0484 | Theophylline | Single-ingredient | Cancelled |

There is no valid registration in the Philippines. The dosage form and approved indication are not recorded for this licence.

---

## Safety Considerations

- **Contraindication flags from the knowledge graph** (not taken from a package insert): hypertension, liver failure and liver disease, kidney disease, epilepsy, anxiety and other mental disorders (psychotic and schizoaffective disorders), porphyria, hypothyroidism, peptic ulcer disease, open-angle glaucoma, diabetes and diabetic ketoacidosis, benign prostatic hyperplasia, thrombocytopenia, neutropenia and agranulocytosis, gallbladder disease, and dermatitis herpetiformis.
  - Thrombocytopenia is directly relevant to a thrombosis or antiplatelet use.
  - These flags need confirmation against an official label.
- **Drug Interactions**: 100 interactions were recorded in total, and the 20 listed in the compiled data are described here.
  - **Major**: bupropion.
  - **Moderate**: H2 blockers and proton pump inhibitors (famotidine, ranitidine, cimetidine, omeprazole, rabeprazole), tetracyclines (doxycycline, tetracycline, minocycline), corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide), clarithromycin, activated charcoal and bowel-preparation products (picosulfuric acid, polyethylene glycol with electrolytes).
  - **Minor**: ephedrine, including nasal ephedrine.
- Theophylline has a narrow therapeutic window, and serum level monitoring is generally needed. Please refer to the package insert for full warnings.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction for thrombotic disease has no clinical trials and no supporting literature.
- The only support is a theoretical platelet cAMP mechanism.
- Practical use is further limited by theophylline's narrow therapeutic index, extensive drug interactions and cancelled market status in the Philippines.

**To proceed, the following is needed:**
- Preclinical or in vitro data showing that theophylline, at clinically achievable concentrations, inhibits platelet aggregation or thrombus formation.
- Any human data on theophylline's effect on thrombotic events or platelet function.
- Official package insert warnings and contraindications from the DOH-FDA Philippines, which are not yet available.
- A confirmed mechanism of action record for the drug.
- A safety and monitoring plan covering the narrow therapeutic range, CYP1A2-related variability and key interactions.

For context, other predicted indications for theophylline have stronger support. Obstructive lung disease is essentially the original use and has Phase 3 trials. Allergic rhinitis, within nasal cavity disease, has a Phase 2 trial and a small challenge study. Both are better candidates for further evaluation than thrombotic disease.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

