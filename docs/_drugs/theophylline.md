---
layout: default
title: Theophylline
parent: Model Prediction Only (L5)
nav_order: 334
evidence_level: L5
indication_count: 6
monitor_inn: "Theophylline"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis"]
last_modified_at: 2026-10-28
description: "Theophylline: predicted new indication Thrombotic disease (evidence level L5). Approved use: Asthma"
---

# Theophylline
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

## Theophylline: From Asthma to Thrombotic Disease
{: .text-alpha }

## One-Sentence Summary

Theophylline is a bronchodilator whose relations recorded in the knowledge graph cover asthma, bronchitis, emphysema and other airway diseases.
The TxGNN model predicts it may be useful for **thrombotic disease**, but there are **no clinical trials** and **no publication that directly studies theophylline for this disease**, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma (relation recorded in the knowledge graph; the local licence record contains no indication text) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 0.9962 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, theophylline inhibits phosphodiesterases and blocks adenosine receptors. Higher cAMP in platelets could in theory reduce platelet aggregation, which would give a plausible but unproven link to thrombosis.

The original uses of theophylline are in the airways (asthma, bronchitis, emphysema), and these are very different from thrombotic disease. The retrieved literature does not test theophylline as an antithrombotic. The papers cover ticlopidine pharmacokinetics, platelet biomarker assays, sample-processing methods and a theophylline detection sensor. The very high score (0.9962) is a computational prediction only and has no clinical support here.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No retrieved publication tests theophylline for thrombotic disease. The items below are the closest to the topic, and they are background only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clinical Pharmacokinetics | Pharmacokinetics of ticlopidine, an antiplatelet drug; not about theophylline |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Critical Reviews in Biochemistry | Thromboxane A2 and prostacyclin in platelets and vessels; prostacyclin raises platelet cAMP, which is the pathway theophylline could affect |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Laboratory/Methods | British Journal of Haematology | Platelet factor 4 assay; theophylline is used only as a sample-preparation additive |
| [32824700](https://pubmed.ncbi.nlm.nih.gov/32824700/) | 2020 | Laboratory/Methods | Cells | Effect of anticoagulation and sample processing on blood microRNA measurement |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Laboratory/Methods | Analytica Chimica Acta | Aptasensor for theophylline detection; no thrombosis data |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0484 | Theophylline | Not specified | Not specified |

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** contraindication relations are recorded for hypertension, liver failure and liver disease, epilepsy, kidney disease, peptic ulcer disease, hypothyroidism, diabetes mellitus and diabetic ketoacidosis, porphyria, thrombocytopenia, neutropenia and agranulocytosis, open-angle glaucoma, benign prostatic hyperplasia, anxiety and psychotic disorders, and gallbladder disease. Thrombocytopenia is relevant to any antithrombotic use.
- **Drug Interactions:** 100 interactions were found. Among those listed, **bupropion** is rated Major. Moderate ones include H2 blockers and omeprazole (famotidine, ranitidine, cimetidine, rabeprazole), clarithromycin, tetracyclines (doxycycline, tetracycline, minocycline), corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), activated charcoal, and bowel-preparation products. Ephedrine is rated Minor.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based only on the model score. There are no registered trials and no study that tests theophylline for thrombotic disease, so the evidence level is L5. The mechanism (raised platelet cAMP) is plausible, but it is unproven for this use.

**To proceed, the following is needed:**
- Mechanism of action data and package insert warnings and contraindications for the Philippines product
- Preclinical or ex vivo data showing that theophylline inhibits platelet aggregation or thrombus formation at safe plasma levels
- A safety assessment of theophylline's narrow therapeutic window and its interactions in patients likely to take antithrombotic drugs
- A review of other predicted indications, because the nasal cavity disease prediction has direct human challenge-study evidence (PMID 9648963) and may be a better research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

