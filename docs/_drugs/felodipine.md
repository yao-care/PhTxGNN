---
layout: default
title: Felodipine
parent: Model Prediction Only (L5)
nav_order: 138
evidence_level: L5
indication_count: 5
monitor_inn: "Felodipine"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-10-28
description: "Felodipine: predicted new indication Pulmonary hypertension owing to lung disease and/or hypoxia (evidence level L5). Approved use: Not recorded in the local data"
---

# Felodipine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Felodipine: Pulmonary hypertension owing to lung disease and/or hypoxia
{: .text-alpha }

## One-Sentence Summary

Felodipine is a calcium channel blocker whose original use is hypertension (a relation recorded in the knowledge graph).
The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia**,
but **no clinical trials** are registered and the **9 publications** retrieved are all preclinical studies that do not examine this disease directly.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, felodipine is an L-type calcium channel blocker with strong arterial vasodilatory activity. Hypoxic pulmonary vasoconstriction partly depends on calcium influx into pulmonary arterial smooth muscle, so a theoretical mechanistic link exists with lowering pulmonary vascular tone.

The link has important limits. The retrieved literature covers hypoxia or anoxia-reoxygenation in rat kidney tubules, human atrial muscle, cerebral arteries, neutrophils and rodent behaviour. None of it studies pulmonary hypertension. Calcium channel blockers are also generally not recommended for pulmonary hypertension due to lung disease, because they can worsen ventilation-perfusion matching and gas exchange. The very high TxGNN score is a computational prediction only.

Other predicted indications are weaker still:
- Pulmonary hypertension with unclear multifactorial mechanism (0.9991): no trials or literature. Calcium channel blockers help only a small subset of vasoreactive patients with pulmonary arterial hypertension.
- Malignant hypertensive renal disease (0.9990): close to the original use, but no specific evidence, and felodipine is not a first-line agent for hypertensive emergencies.
- Braddock syndrome (0.9988): no support; likely a network-propagation artifact.
- Chronic pulmonary heart disease (0.9919): only indirect 1980s haemodynamic studies (see below).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the publications below directly studies pulmonary hypertension owing to lung disease or hypoxia. They are all preclinical hypoxia/anoxia studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8160846](https://pubmed.ncbi.nlm.nih.gov/8160846/) | 1994 | Preclinical (vascular) | Am J Physiol | A prior anoxic episode weakened anoxia-induced vasorelaxation of rat aortic rings |
| [8584414](https://pubmed.ncbi.nlm.nih.gov/8584414/) | 1995 | Preclinical (rat tubules) | Pflugers Arch | Felodipine protected rat proximal tubules from hypoxic injury through a calcium-independent mechanism |
| [9431863](https://pubmed.ncbi.nlm.nih.gov/9431863/) | 1997 | Preclinical (human atrial tissue) | Int J Cardiol | Felodipine protected human atrial muscle from hypoxia-reoxygenation dysfunction in vitro |
| [3142891](https://pubmed.ncbi.nlm.nih.gov/3142891/) | 1988 | Preclinical (cerebral arteries) | J Cereb Blood Flow Metab | Vasodilators affected reoxygenation and calcium-induced contractions of dog cerebral arteries |
| [8394565](https://pubmed.ncbi.nlm.nih.gov/8394565/) | 1993 | Preclinical (cellular) | Pflugers Arch | Calcium channel blockers including felodipine affected anoxia-induced rises in intracellular calcium in rabbit tubule cells |
| [8110031](https://pubmed.ncbi.nlm.nih.gov/8110031/) | 1993 | Preclinical (animal behaviour) | Arch Int Pharmacodyn Ther | Nicardipine, felodipine and nifedipine affected passive avoidance behaviour in intact and hypoxia-exposed rats |
| [3961832](https://pubmed.ncbi.nlm.nih.gov/3961832/) | 1986 | Preclinical (cerebral blood flow) | Stroke | Nifedipine and felodipine depressed the rise in rat cerebral blood flow during anoxia |
| [3343292](https://pubmed.ncbi.nlm.nih.gov/3343292/) | 1988 | Preclinical (rat cortex) | J Cereb Blood Flow Metab | Both agents suppressed hypoxia-evoked adenosine and inosine release in rat cortex |
| [9864178](https://pubmed.ncbi.nlm.nih.gov/9864178/) | 1999 | Preclinical (neutrophil) | Blood | Nitric oxide augmented free radical generation by rat neutrophils after hypoxia-reoxygenation |

For the related prediction *chronic pulmonary heart disease*, only indirect haemodynamic data exist: an acute and long-term haemodynamic study of felodipine in severe COPD ([2838319](https://pubmed.ncbi.nlm.nih.gov/2838319/), 1988, Eur Respir J) reported reductions in pulmonary vascular resistance (18%) and systemic vascular resistance (33%) with increased cardiac output. A heart failure haemodynamic study ([2487551](https://pubmed.ncbi.nlm.nih.gov/2487551/), 1989) and a review of calcium antagonists in hypertension ([3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/), 1988) are also available. None provides controlled outcome evidence.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0186 | Felodipine | Not stated | Not stated |

The licence is a single-ingredient product and is currently valid. The record carries no indication text, so no approved indication can be confirmed from local data.

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text)**: the graph lists contraindication relations with kidney disease, liver disease, gallbladder disease, angioedema (several types), neutropenia and agranulocytosis, aortic stenosis, hypotensive disorder, hypertrophic cardiomyopathy, renal artery obstruction, myocardial infarction, coronary artery disease and atherosclerosis. These should be verified against the package insert.
- **Drug Interactions**: 100 interactions were found. Dolasetron is rated **Major**. Examples of Moderate interactions include cimetidine, clarithromycin, aprepitant, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), bupropion, morphine, acetylsalicylic acid, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin) and magnesium sulfate.
- **Disease-specific concern**: calcium channel blockers can worsen ventilation-perfusion matching and gas exchange in pulmonary hypertension due to lung disease.

Warnings and contraindications from the package insert were not available; please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score and a plausible vasodilatory mechanism only. No cited study directly addresses pulmonary hypertension owing to lung disease or hypoxia, so the evidence level is L5. Calcium channel blockers are also generally discouraged in this setting because of possible gas-exchange worsening.

**To proceed, the following is needed:**
- Clinical studies (ideally controlled) of felodipine in pulmonary hypertension owing to lung disease or hypoxia, including gas exchange and oxygenation outcomes
- Mechanism of action data and the package insert warnings and contraindications from DOH-FDA Philippines
- A review of the knowledge-graph contraindication relations against label text
- Approved indication text and dosage form for licence PNF-0186
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

