---
layout: default
title: Irbesartan
parent: Model Prediction Only (L5)
nav_order: 183
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Irbesartan: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension, diabetic nephropathy"
monitor_inn: "Irbesartan"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
---

# Irbesartan
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

# Irbesartan: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Irbesartan is an angiotensin II receptor blocker (AT1 antagonist) originally used for hypertension and diabetic nephropathy.
The TxGNN model ranks **malignant renovascular hypertension** first (score 99.31%), but the best-supported prediction is **pulmonary hypertension owing to lung disease and/or hypoxia**, which has **0 clinical trials** and **11 publications**, almost all preclinical or indirect.
Overall, the evidence is at the model-prediction and early preclinical stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, diabetic nephropathy (the Philippines registration record contains no approved indication text) |
| Predicted New Indication | Malignant renovascular hypertension (rank 1); pulmonary hypertension owing to lung disease and/or hypoxia (rank 3, the only prediction with literature) |
| TxGNN Prediction Score | 99.31% (rank 1); 99.25% (rank 3) |
| Evidence Level | L5 for rank 1; L4 for rank 3 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, irbesartan is an AT1 receptor antagonist. Its efficacy in hypertension and diabetic nephropathy is established, and mechanistically it may be applicable to conditions driven by renin-angiotensin system (RAS) activation.

**Rank 1, malignant renovascular hypertension:** Renovascular hypertension is strongly driven by RAS activation, so AT1 blockade is biologically plausible. However, in bilateral renal artery stenosis or a solitary functioning kidney, ARBs can precipitate acute kidney injury. The knowledge graph also lists renal artery obstruction as a contraindication. The high score is a computational prediction only.

**Rank 3, pulmonary hypertension owing to lung disease and/or hypoxia:** Hypoxia activates local RAS and AT1 signalling, contributing to vasoconstriction, tissue remodelling and cardiomyocyte injury. Preclinical studies show irbesartan protects cardiomyocytes under hypoxic stress, reduces sleep-apnoea-induced cardiac apoptosis, and improves pulmonary artery lesions in rat models of chronic mountain sickness and high-altitude pulmonary hypertension. No human outcome data in pulmonary hypertension were identified.

**Ranks 2 and 4:** Malignant hypertensive renal disease is biologically plausible given irbesartan's diabetic nephropathy indication, but malignant hypertension is an emergency usually managed with titratable parenteral agents. Pulmonary hypertension with unclear multifactorial mechanism has no literature and no clear mechanistic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the four predicted indications.

---

## Literature Evidence

The table covers the rank 3 prediction (pulmonary hypertension owing to lung disease and/or hypoxia), the only one with literature. Entries are ordered by relevance, with irbesartan-specific studies first. Several retrieved papers concern other agents and are low relevance (see note below the table).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34286497](https://pubmed.ncbi.nlm.nih.gov/34286497/) | 2021 | Animal study | Eur Rev Med Pharmacol Sci | Irbesartan explored for improving high-altitude pulmonary hypertension in rats via intestinal flora and oxidative stress |
| [34147903](https://pubmed.ncbi.nlm.nih.gov/34147903/) | 2021 | Animal study | Biomed Pharmacother | Irbesartan ameliorated pulmonary artery lesions in a rat chronic mountain sickness model, via cholesterol metabolism |
| [34626328](https://pubmed.ncbi.nlm.nih.gov/34626328/) | 2022 | Animal/preclinical | Sleep Breath | Irbesartan attenuated chronic intermittent hypoxia-induced cardiac apoptosis and upregulated Sirtuin 1 |
| [35288835](https://pubmed.ncbi.nlm.nih.gov/35288835/) | 2022 | Review | Inflammopharmacology | Reviews pleiotropic effects of AT1 receptor antagonists in hypoxia induced by cardiac ischaemia |
| [30356256](https://pubmed.ncbi.nlm.nih.gov/30356256/) | 2018 | In vitro/preclinical | PLoS One | Irbesartan protected cardiomyocytes from hypoxia-induced inflammatory and oxidative injury |
| [17142340](https://pubmed.ncbi.nlm.nih.gov/17142340/) | 2007 | Preclinical | Am J Physiol Heart Circ Physiol | Irbesartan inhibited coronary angiogenesis stimulated by chronic intermittent hypoxia in neonatal rats |
| [15526904](https://pubmed.ncbi.nlm.nih.gov/15526904/) | 2004 | Preclinical (indirect) | Renal Failure | Irbesartan ameliorated cyclosporine nephrotoxicity in rats |
| [30525078](https://pubmed.ncbi.nlm.nih.gov/30525078/) | 2018 | Preclinical (indirect) | Regen Ther | ARB pretreatment abolished the benefit of adipose-derived stem cell sheets after myocardial infarction |

Note: three further retrieved papers (PMIDs 38621945, 25907932, 39155928) concern herbal extracts or roxadustat rather than irbesartan and were omitted as not relevant.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0260 | Irbesartan | Not specified | Not specified (status: cancelled) |

---

## Safety Considerations

No label-based warnings or contraindications were available. The following come from knowledge-graph contraindication links, not from package insert text.

- **Contraindication links (knowledge graph):** angioedema (including hereditary and RAS-blocker-induced forms), pancreatitis, systemic lupus erythematosus, renal artery obstruction, anuria, hypotensive disorders, hepatic coma/encephalopathy, diabetes-related conditions including diabetic ketoacidosis, gout and hyperuricaemia, hypercalcaemia and hyperparathyroidism, potassium deficiency, rhabdomyolysis and myopathy.
- **Drug Interactions:** 100 interactions were found. Major-level interactions in the listed sample are **potassium citrate** and **potassium bicarbonate** (hyperkalaemia risk). Moderate-level interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), insulins, acetylsalicylic acid, morphine, bupropion, aprepitant, dronabinol and several bowel-preparation agents.
- **Indication-specific caution:** ARBs can cause acute kidney injury in bilateral renal artery stenosis or a solitary functioning kidney, which is directly relevant to renovascular hypertension.

Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four predictions rest on computational scores of about 99%. None has clinical trials, and the only literature (for hypoxia-related pulmonary hypertension) is preclinical or indirect. Irbesartan's Philippines registration is cancelled, and the renovascular prediction carries a notable renal safety concern.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank
- Package insert warnings and contraindications from DOH-FDA Philippines (currently a blocking gap for safety screening)
- Controlled clinical evidence, or at least pilot human studies, in pulmonary hypertension due to lung disease or hypoxia
- Safety assessment for renovascular hypertension, particularly renal artery stenosis
- Clarification of the regulatory pathway given that the only Philippines registration is cancelled
- Route and formulation compatibility assessment for the proposed indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

