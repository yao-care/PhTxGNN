---
layout: default
title: Biperiden
parent: 僅模型預測 (L5)
nav_order: 43
evidence_level: L5
indication_count: 10
---

# Biperiden
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Biperiden: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Biperiden (Akineton) is a selective M1 muscarinic acetylcholine receptor antagonist, classically used to treat Parkinson's disease and drug-induced extrapyramidal side effects. The TxGNN model ranks **Rasmussen Subacute Encephalitis** as the top predicted new indication (score 99.94%); however, **no clinical trials or publications** currently support this direction. Across all 10 predicted indications, the evidence base is thin and several predictions are mechanistically implausible or even contraindicated — a critical caution for downstream decision-making.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in regulatory data (original_indications field is empty; Biperiden is historically indicated for Parkinson's disease and drug-induced extrapyramidal symptoms) |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Biperiden is a selective M1 muscarinic acetylcholine receptor (mAChR) antagonist. It restores the dopamine/acetylcholine balance in the striatum — the pathophysiological basis of Parkinson's disease and antipsychotic-induced extrapyramidal reactions — by blocking excess cholinergic activity.

Rasmussen subacute encephalitis is a progressive, autoimmune-mediated chronic encephalitis driven by anti-GluR3 (glutamate receptor) antibodies, resulting in unilateral hemispheric inflammation, intractable focal epilepsy, and progressive hemiplegia. The pathophysiology is fundamentally immune-mediated, not cholinergic. While the cholinergic system has an indirect modulatory role in neuroinflammation (e.g., the vagal anti-inflammatory reflex), there is no established theoretical or experimental basis for blocking M1 receptors as a therapeutic strategy in Rasmussen encephalitis.

The most probable explanation for the high TxGNN score is **topological proximity** in the knowledge graph: Biperiden's node cluster neighbours many CNS disease nodes (Parkinson's, encephalitis, movement disorders), inflating scores for neurological conditions without reflecting true biological relevance. This is a known limitation of graph-based predictions for drugs with broad CNS connectivity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Biperiden in Rasmussen Subacute Encephalitis.

---

## Literature Evidence

Currently no related literature available for Biperiden in Rasmussen Subacute Encephalitis.

---

## Philippines Market Information

Biperiden has **no registered product licenses** in the Philippines as of the data cutoff (2026-04-04). The drug is not marketed and has no active regulatory authorizations on record.

---

## Safety Considerations

Safety profile data (package insert warnings, contraindications, drug interaction database) was not available in this evidence pack. Please refer to the official package insert for complete safety information.

> **Note for reviewers**: Given Biperiden's known anticholinergic class effects (urinary retention, tachycardia, blurred vision, cognitive impairment in elderly, hyperthermia risk), any future clinical consideration must include a full contraindication screen — particularly in elderly patients and those with cognitive disorders. Of the 10 predictions in this pack, at least **2 represent mechanistic contraindications** (Lewy body dementia and ADHD — see Supplementary Observations below).

---

## Supplementary Observations: Full Top-10 Prediction Landscape

The following table summarises all 10 TxGNN-ranked predictions to provide a complete picture of the mechanistic plausibility landscape:

| Rank | Predicted Indication | Score | Evidence Level | Decision | Mechanistic Assessment |
|------|---------------------|-------|---------------|----------|----------------------|
| 1 | Rasmussen Subacute Encephalitis | 99.94% | L5 | Hold | No mechanistic link; likely KG topology artefact |
| 2 | Myelitis | 99.92% | L5 | Hold | Possibly useful only for secondary bladder spasticity (symptom, not disease-modifying) |
| 3 | PLA2G6-associated neurodegeneration (PLAN) | 99.88% | L5 | Hold | Dystonia component may offer indirect link; no PLAN-specific evidence |
| 4 | Transaldolase Deficiency | 99.84% | L5 | Hold | No biological intersection with M1 blockade; KG cluster artefact |
| 5 | Fructose-1,6-bisphosphatase Deficiency | 99.81% | L5 | Hold | Metabolic disorder; no mechanistic basis |
| 6 | PSP-Corticobasal Syndrome | 99.81% | L5 | Hold | Theoretical tauopathy rationale offset by high cognitive worsening risk |
| 7 | **Juvenile Parkinson's Disease (Hunt)** | **99.73%** | **L3** | **Research Question** | **Highest plausibility** — mechanistically identical to adult Parkinson's (M1 blockade restores striatal DA/ACh balance); evidence extrapolated from adult PD |
| 8 | Lewy Body Dementia | 99.73% | L4 | Hold | ⚠️ **Likely contraindicated** — M1 blockade worsens cognition in cholinergic-deficient LBD |
| 9 | ADHD | 99.72% | L4 | Hold | ⚠️ Biperiden appears only as **rescue therapy** for methylphenidate-induced dyskinesia, not ADHD treatment |
| 10 | X-linked Intellectual Disability-Ataxia-Apraxia Syndrome | 99.69% | L5 | Hold | No mechanistic support; anticholinergics may worsen ataxia and cognition |

**Key takeaway**: Among all 10 predictions, only **Juvenile Parkinson's Disease (Rank 7)** carries a plausible mechanistic rationale and reaches L3 evidence (by extrapolation from well-established adult Parkinson's data). The remaining 9 predictions are either unsupported (L5) or actively contraindicated on mechanistic grounds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Rasmussen Subacute Encephalitis, 99.94%) has zero supporting clinical trials or literature and lacks a credible mechanistic link to Biperiden's M1 antagonist mechanism. The high score most likely reflects knowledge graph topology rather than true repurposing potential. Importantly, the drug is not marketed in the Philippines, adding a significant regulatory barrier to any repurposing path.

**To proceed with any further evaluation, the following is needed:**

- **MOA data**: Retrieve full pharmacology profile from DrugBank API (DB00810) to formally document the M1-selective mechanism and known off-target effects
- **Package insert data**: Download and parse official FDA/EMA/PMDA label to extract current approved indications, warnings, and contraindications
- **Redirect focus**: Redirect attention from Rank 1 (Rasmussen encephalitis) to **Rank 7 (Juvenile Parkinson's Disease)**, the only prediction with a plausible mechanistic rationale — and clarify whether this represents a true repurposing opportunity or an underserved paediatric subpopulation of the existing indication
- **Mechanistic contraindication flag**: Formally document Lewy Body Dementia (Rank 8) and ADHD (Rank 9) as **predicted contraindications** rather than repurposing opportunities; these findings should feed back into the TxGNN model calibration as negative training signal
- **Philippines regulatory pathway**: Confirm whether a new drug application would be required for market entry, and identify any regional distributors or compassionate-use pathways if the Juvenile PD direction proceeds

---

*This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application. Data cutoff: 2026-04-04.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

