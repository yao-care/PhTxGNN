---
layout: default
title: Verapamil
parent: Model Prediction Only (L5)
nav_order: 355
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-31
monitor_inn: "Verapamil"
predicted_indications: ["obsolete bundle branch block", "malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "periodic paralysis with transient compartment-like syndrome"]
description: "Verapamil: predicted new indication Obsolete bundle branch block (evidence level L5). Approved use: Not recorded in the local data"
---

# Verapamil
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

## Verapamil: Obsolete bundle branch block
{: .text-alpha }

## One-Sentence Summary

Verapamil is a calcium channel blocker originally used for hypertension, atrial fibrillation, acute coronary syndrome, Prinzmetal angina and ventricular tachycardia.
The TxGNN model predicts it may be effective for **obsolete bundle branch block**, but **no clinical trials and no relevant publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Obsolete bundle branch block |
| TxGNN Prediction Score | 0.9962 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, verapamil is an L-type calcium channel blocker that slows conduction through the atrioventricular (AV) node. Its efficacy in hypertension and arrhythmias is established.

For bundle branch block, however, this mechanism does not support the prediction. Slowing conduction is generally undesirable, or even contraindicated, in conduction-system disease. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The disease term is also obsolete in the ontology.

Other predicted indications were reviewed as well. None has clinical trial support:

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Malignant hypertensive renal disease | 0.9927 | L5 | Extension of the existing hypertension indication; no specific evidence. Malignant hypertension is usually managed with IV agents, and verapamil's negative inotropy and conduction effects limit acute use. |
| 4 | Pulmonary hypertension with unclear multifactorial mechanism | 0.9926 | L5 | Calcium channel blockers help only vasoreactive responders; verapamil is not preferred because of negative inotropy. |
| 5 | Pulmonary hypertension owing to lung disease and/or hypoxia | 0.9926 | L5 | Preclinical plausibility only; most retrieved literature is indirect. Vasodilators may worsen ventilation-perfusion matching. |
| 6 | Braddock syndrome | 0.9915 | L5 | No mechanistic rationale; the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. |
| 7 | Periodic paralysis with transient compartment-like syndrome | 0.9908 | L5 | Calcium channel link conceivable in principle, with no evidence. |

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted indications.

## Literature Evidence

For the top-ranked prediction (obsolete bundle branch block), currently no related literature is available.

The literature retrieved for other predictions is indirect. The most relevant items are preclinical (all for pulmonary hypertension owing to lung disease and/or hypoxia):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24977753](https://pubmed.ncbi.nlm.nih.gov/24977753/) | 2014 | Preclinical | J Trauma Acute Care Surg | Verapamil preserved cytoskeletal function in an in vitro intestinal model after hypoxia-reoxygenation. |
| [21962069](https://pubmed.ncbi.nlm.nih.gov/21962069/) | 2011 | Preclinical | High Alt Med Biol | Studied serotonin-mediated calcium influx through L-type channels in pulmonary arteries of sheep after long-term high-altitude hypoxia. |
| [9768801](https://pubmed.ncbi.nlm.nih.gov/9768801/) | 1998 | Preclinical | Anesth Analg | Ketamine-induced pulmonary vasodilation in isolated rat lung was partly mediated by L-type calcium channels (verapamil used as a probe). |
| [1353873](https://pubmed.ncbi.nlm.nih.gov/1353873/) | 1992 | Review | Pathol Biol | Effectiveness of verapamil, diltiazem and nifedipine for migraine prevention is not firmly demonstrated (unrelated to the predicted indication). |
| [9440591](https://pubmed.ncbi.nlm.nih.gov/9440591/) | 1998 | Review | Chest | Review of multifocal atrial tachycardia, commonly secondary to COPD (arrhythmia, not pulmonary hypertension). |

For malignant renovascular hypertension, two papers were retrieved: [22147655](https://pubmed.ncbi.nlm.nih.gov/22147655/) (2012, Review, aldosterone/renin ratio) and [10224210](https://pubmed.ncbi.nlm.nih.gov/10224210/) (1999, Case report, renal myofibromatosis). Neither provides evidence on verapamil in this condition.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0513 | Verapamil | Not specified | Not specified (status: valid) |


## Safety Considerations

- **Contraindications / disease associations (from the knowledge graph, not label text):** The graph links verapamil to contraindication with many conditions, including aortic stenosis and valve disease, hypotensive disorder, hypertrophic cardiomyopathy, heart failure, atrioventricular block, ventricular tachycardia (including catecholaminergic and incessant infant forms), kidney disease, liver disease, gallbladder disease, neutropenia, agranulocytosis, myasthenia gravis and neuromuscular junction disease, angioedema (several forms), connective tissue, bone and cartilage disease, and renal artery obstruction. These need verification against the official package insert.
- **Drug Interactions:** 100 interactions were found. Among those listed, **loperamide** is rated **Major**. Many are **Moderate**, including corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), metformin, bupropion, aprepitant, acetylsalicylic acid, canagliflozin, cimetidine, clarithromycin and calcium salts. Morphine is rated Minor.
- **Predicted-indication concerns:** Verapamil's conduction-slowing effect is a direct concern for bundle branch block. Its negative inotropy limits use in pulmonary hypertension and acute malignant hypertension. Vasodilation may worsen ventilation-perfusion matching in hypoxic lung disease.

Package insert warnings were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All predictions are model-only (L5, or L4 for hypoxia-related pulmonary hypertension) with no clinical trials. The top prediction, bundle branch block, is mechanistically contradictory because verapamil slows conduction, and its disease term is obsolete.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the DOH-FDA Philippines (currently a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Clinical evidence specific to verapamil in any predicted indication, with preclinical and mechanistic work first for pulmonary hypertension owing to lung disease and/or hypoxia
- Clarification of whether the TxGNN score for obsolete bundle branch block reflects only similarities the model learned between related diseases, not biological evidence
- Confirmation of whether any valid verapamil registration or supply exists in the Philippines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

