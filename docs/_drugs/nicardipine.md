---
layout: default
title: Nicardipine
parent: Model Prediction Only (L5)
nav_order: 251
evidence_level: L5
indication_count: 4
monitor_inn: "Nicardipine"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "Braddock syndrome"]
last_modified_at: 2026-10-30
description: "Nicardipine: predicted new indication Pulmonary hypertension owing to lung disease and/or hypoxia (evidence level L5). Approved use: Hypertensive disorder / hypertension"
---

# Nicardipine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Nicardipine: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia
{: .text-alpha }

## One-Sentence Summary

Nicardipine is a calcium channel blocker whose use in hypertensive disorders is recorded in the knowledge graph. The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia**, but **no clinical trials** are registered and only **one animal study** (1988) directly examines nicardipine in hypoxic pulmonary vasoconstriction. This prediction is therefore a computational hypothesis with very limited supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder / hypertension (relation recorded in the knowledge graph; no approved indication text is available in the local licence record) |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 0.9926 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Number of Approvals | 1 (single-ingredient registration) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on general pharmacology, nicardipine is a dihydropyridine L-type calcium channel blocker that relaxes vascular smooth muscle and lowers blood pressure.

Hypoxic pulmonary vasoconstriction depends partly on calcium influx into pulmonary arterial smooth muscle, so blocking calcium channels is mechanistically plausible. One retrieved study (PMID 3132192, 1988) examined nicardipine's effect on regional hypoxic pulmonary vasoconstriction in dogs.

There are important counterpoints. Systemic vasodilation may impair ventilation-perfusion matching and worsen gas exchange in lung disease, and calcium channel blockers are generally not recommended for pulmonary hypertension due to lung disease. The score is a computational prediction only, and no clinical data support benefit in patients.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Most retrieved publications are preclinical or off-topic. The table lists the more relevant ones. None is a randomized trial in pulmonary hypertension.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3132192](https://pubmed.ncbi.nlm.nih.gov/3132192/) | 1988 | Preclinical / physiology (dogs) | Br J Anaesth | Studied nicardipine's effect on regional hypoxic pulmonary vasoconstriction in open-chest dogs, including under controlled cardiac output; the only study found directly on nicardipine and this mechanism |
| [19035721](https://pubmed.ncbi.nlm.nih.gov/19035721/) | 2008 | Clinical study | J Neurosurg | IV nicardipine and brain tissue oxygenation in hypertensive emergencies in acute brain disease; not pulmonary hypertension |
| [2693295](https://pubmed.ncbi.nlm.nih.gov/2693295/) | 1989 | Review | Fundam Clin Pharmacol | Calcium antagonists in the central nervous system, including use in cerebral ischaemia and hypoxia; not pulmonary |
| [22366846](https://pubmed.ncbi.nlm.nih.gov/22366846/) | 2012 | Preclinical (mice) | Anesth Analg | Hypotension induced by nimodipine or nicardipine vs nitroglycerin and memory; not pulmonary |
| [14751848](https://pubmed.ncbi.nlm.nih.gov/14751848/) | 2004 | Preclinical (rat) | Am J Physiol Lung Cell Mol Physiol | 5-HT-induced calcium influx in small intrapulmonary artery; background on pulmonary vascular calcium signalling |
| [3288055](https://pubmed.ncbi.nlm.nih.gov/3288055/) | 1988 | Review | Ann N Y Acad Sci | Cardiomyocyte pathophysiology; background only |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0346 | Nicardipine | Not specified | Not specified in the record |

---

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The knowledge graph links nicardipine to contraindication relations with liver disease, gallbladder disease, hypotensive disorder, impaired renal function, intracerebral haemorrhage, cerebral infarction, cerebrovascular disorder, cerebral artery occlusion and brain stem infarction. These are not confirmed by package insert text and need verification.
- **Drug Interactions:** 100 interactions were found in the interaction database. Shown here are examples only. One is Major: **dolasetron**. Moderate examples include hydrocortisone, bupropion, aprepitant, triamcinolone, morphine, acetylsalicylic acid, dexamethasone, betamethasone, budesonide, cimetidine, canagliflozin, dapagliflozin, empagliflozin, magnesium sulfate and miconazole.
- **Disease-specific concern:** Systemic vasodilation may worsen gas exchange in patients with lung disease.

For label-based warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score and a single 1988 animal study. No study directly addresses nicardipine in pulmonary hypertension due to lung disease or hypoxia in humans, so the evidence level is L5. Calcium channel blockers are generally not recommended in this setting, and there is a physiological risk of worsened gas exchange.

**To proceed, the following is needed:**
- Mechanism-of-action data from DrugBank
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Human haemodynamic and gas-exchange studies, or registered trials, in this patient group
- Review of guideline positions on calcium channel blockers in pulmonary hypertension due to lung disease
- Confirmation of the dosage forms and approved indication for registration PNF-0346

---

*Other predictions (all Hold, L5, no trials or literature):* pulmonary hypertension with unclear multifactorial mechanism (0.9926), malignant hypertensive renal disease (0.9913; overlaps with existing blood-pressure-lowering use and is not a distinct repurposing signal), and Braddock syndrome (0.9903; no mechanistic rationale; the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

