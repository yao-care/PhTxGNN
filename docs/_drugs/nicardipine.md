---
layout: default
title: Nicardipine
parent: Model Prediction Only (L5)
nav_order: 251
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Nicardipine: predicted new indication Pulmonary hypertension owing to lung disease and/or hypoxia (evidence level L5). Approved use: Hypertension / hypertensive disorder"
---

# Nicardipine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Nicardipine: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Nicardipine is a calcium channel blocker originally used to treat hypertension and hypertensive disorders.
The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia**,
but currently there are **0 clinical trials** and only **indirect, mostly preclinical literature** (about 20 publications retrieved, one directly relevant physiological study in dogs) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension / hypertensive disorder (from the TxGNN knowledge graph; no approved indication text is available for the Philippine registration) |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia (the top-ranked prediction is "pulmonary hypertension with unclear multifactorial mechanism", which has no supporting evidence; this one has the strongest supporting literature) |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L4 (preclinical or physiological evidence only) |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, nicardipine is a dihydropyridine L-type calcium channel blocker. It relaxes vascular smooth muscle and causes vasodilation, which is the basis of its use in hypertension.

Hypoxic pulmonary vasoconstriction is a calcium-dependent process, so blocking calcium channels could in theory reduce pulmonary vascular tone. A 1988 physiological study in dogs (PMID 3132192) examined this effect directly and is the most relevant item found.

There are important cautions. Systemic vasodilators can inhibit hypoxic pulmonary vasoconstriction, which may worsen ventilation-perfusion matching and gas exchange in lung disease. They can also cause systemic hypotension. The net clinical benefit is therefore uncertain. The remaining retrieved papers are mostly off-topic (cardiomyocyte, brain, and in vitro cell studies), and the TxGNN score is a computational prediction only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No clinical studies in pulmonary hypertension were found. The table lists the most relevant retrieved items.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3132192](https://pubmed.ncbi.nlm.nih.gov/3132192/) | 1988 | Physiological/experimental study | British Journal of Anaesthesia | Effects of nicardipine on regional hypoxic pulmonary vasoconstriction in 14 open-chest dogs; higher doses increased cardiac output, so a second group was studied with controlled cardiac output. |
| [19035721](https://pubmed.ncbi.nlm.nih.gov/19035721/) | 2008 | Clinical study | Journal of Neurosurgery | IV nicardipine in hypertensive emergencies in acute brain disease and its effect on cerebral oxygenation (not pulmonary hypertension). |
| [2693295](https://pubmed.ncbi.nlm.nih.gov/2693295/) | 1989 | Review | Fundamental & Clinical Pharmacology | Calcium antagonists act on the central nervous system and have been used in cerebral ischaemia, vasospasm and hypoxia. |
| [1735870](https://pubmed.ncbi.nlm.nih.gov/1735870/) | 1992 | Review | Journal of Post Anesthesia Nursing | Acute postoperative hypertension in patients with pre-existing hypertension (systemic, not pulmonary). |
| [3288055](https://pubmed.ncbi.nlm.nih.gov/3288055/) | 1988 | Review | Annals of the New York Academy of Sciences | Cardiomyocyte pathophysiology and calcium loss under pathological stimuli. |
| [14751848](https://pubmed.ncbi.nlm.nih.gov/14751848/) | 2004 | Preclinical | Am J Physiol Lung Cell Mol Physiol | 5-HT-induced calcium influx in rat small intrapulmonary artery, relevant to pulmonary vasoconstriction mechanisms. |
| [22366846](https://pubmed.ncbi.nlm.nih.gov/22366846/) | 2012 | Preclinical | Anesthesia and Analgesia | Nimodipine-induced hypotension and memory in mice (mainly nimodipine, not nicardipine). |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0346 | Nicardipine | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Disease-related cautions (knowledge graph, not label text)**: The TxGNN knowledge graph lists contraindication relationships with liver disease, gallbladder disease, hypotensive disorder, impaired renal function, intracerebral haemorrhage, cerebral infarction, ischaemic stroke susceptibility, cerebrovascular disorder, cerebral artery occlusion and brain stem infarction.
- **Drug Interactions**: 100 interactions were found in the DDI database. Most are Moderate. One is Major: **dolasetron**. Moderate examples include hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone, bupropion, aprepitant, morphine, acetylsalicylic acid, cimetidine, miconazole, magnesium sulfate, and the SGLT2 inhibitors canagliflozin, dapagliflozin and empagliflozin.
- **Indication-specific concern**: In pulmonary hypertension and lung disease, systemic hypotension and worsened gas exchange are possible.

Please also refer to the package insert for full warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score and indirect preclinical or physiological evidence. There are no clinical trials, and a plausible mechanism of harm (loss of hypoxic pulmonary vasoconstriction, systemic hypotension). The only Philippine registration is cancelled, so there is currently no marketed product.

Other predicted indications (malignant hypertensive renal disease, malignant renovascular hypertension) largely overlap with the existing hypertension use and have no supporting evidence. For Braddock syndrome, no mechanistic link is evident.

**To proceed, the following is needed:**
- Mechanism of action data
- Clinical studies or systematic reviews of calcium channel blockers in pulmonary hypertension due to lung disease or hypoxia
- Package insert warnings and contraindications
- Confirmation of whether any valid nicardipine registration exists in the Philippines, with dosage form and approved indications
- A safety assessment covering hypotension, gas exchange and the listed interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

