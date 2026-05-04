---
layout: default
title: Pyridostigmine
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 7
---

# Pyridostigmine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Pyridostigmine: From Myasthenia Gravis to Myasthenia Gravis with Thymus Hyperplasia

## One-Sentence Summary

Pyridostigmine is an acetylcholinesterase (AChE) inhibitor widely used globally as a first-line symptomatic treatment for myasthenia gravis (MG), though it is not currently registered in the Philippines.
The TxGNN model predicts it may be effective for **Myasthenia Gravis with Thymus Hyperplasia** — a specific subtype characterized by anti-AChR IgG antibodies and hyperactivated thymic germinal centers —
with **3 publications** currently supporting this direction, and no dedicated clinical trials registered for this specific subtype.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Philippines (globally established for Myasthenia Gravis) |
| Predicted New Indication | Myasthenia Gravis with Thymus Hyperplasia |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L2 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Pyridostigmine acts as an acetylcholinesterase (AChE) inhibitor at the neuromuscular junction (NMJ). By blocking the enzyme responsible for breaking down acetylcholine (ACh), it raises ACh concentration in the synaptic cleft, thereby compensating for the reduced availability and functional impairment of ACh receptors (AChR) caused by autoimmune attack. Although detailed mechanism of action data was not available from regulatory filings, this pharmacological profile is well-characterized in the published literature and is consistent with the repurposing rationale described in the Evidence Pack.

Myasthenia gravis with thymus hyperplasia is an immunologically distinct MG subtype: hyperactivated thymic germinal centers drive AChR-specific Th2/Tfh cell expansion, sustaining B cell–mediated anti-AChR IgG production (present in approximately 85% of these patients). While Pyridostigmine does not directly suppress thymic activity or the underlying autoimmune cascade, it addresses the downstream functional consequence — impaired neuromuscular transmission — making it directly applicable as a symptomatic agent regardless of the thymic trigger.

In clinical practice, Pyridostigmine is the cornerstone of symptomatic management in anti-AChR–positive MG, used in combination with thymectomy and immunosuppressive therapy (corticosteroids, azathioprine). This combined-modality approach is well-established and directly relevant to the thymus hyperplasia subtype, where surgical and immunological control may take weeks to months to achieve full effect. Pyridostigmine bridges that gap by providing immediate neuromuscular symptom relief.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Pyridostigmine in Myasthenia Gravis with Thymus Hyperplasia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34225443](https://pubmed.ncbi.nlm.nih.gov/34225443/) | 2021 | Review | Molecular Medicine Reports | Comprehensive review of MG pathology, autoimmunity, and genomic/epigenetic mechanisms; covers multiple MG subtypes including thymus hyperplasia–associated forms; highlights anti-AChR antibody as the central pathological driver |
| [18053719](https://pubmed.ncbi.nlm.nih.gov/18053719/) | 2008 | Case Series | Neuromuscular Disorders | MuSK-positive MG patient with confirmed thymus hyperplasia presenting with dropped head syndrome; distinguishes thymic pathology between AChR-positive and MuSK-positive MG subtypes; relevant to treatment planning for thymus hyperplasia cases |
| [25683765](https://pubmed.ncbi.nlm.nih.gov/25683765/) | 2015 | Prospective Cohort | Journal of Neurology | Retrospective analysis of 39 non-thymomatous late-onset MG patients post-thymectomy; reports 2-year outcomes including MGFA classification changes; provides context for combined thymectomy + pharmacological management in this population |

---

## Philippines Market Information

Pyridostigmine is currently not registered with the Philippine Food and Drug Administration (FDA). No product authorizations are on record, and the drug has no approved indications or licensed dosage forms in the Philippines at this time.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings, contraindications, and drug interaction data were not available in this Evidence Pack. Retrieval from the Philippine FDA package insert and DrugBank is recommended before any clinical or regulatory action. In particular, attention should be paid to the known risk of cholinergic crisis with overdose, and to the contraindication in MuSK-antibody–positive MG patients, in whom Pyridostigmine may paradoxically worsen neuromuscular symptoms.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Pyridostigmine is the internationally recognized first-line symptomatic agent for anti-AChR–positive MG, including the thymus hyperplasia subtype. The mechanistic rationale is strong, clinical practice across multiple high-income countries firmly supports its use in this population, and the TxGNN prediction score of 99.76% is consistent with established pharmacological evidence. The primary barriers are regulatory (not marketed in the Philippines) and informational (safety data gaps).

**To proceed, the following is needed:**
- **Philippine FDA registration**: Initiate a product registration application; no existing license is on file, making this a prerequisite for any local clinical use.
- **Safety data retrieval**: Obtain full package insert warnings and contraindications from the Philippine FDA or DrugBank API to close the current data gap before S1 safety screening can proceed.
- **Drug interaction assessment**: The DDI query returned no results; a formal pharmacist-led interaction review is required, especially for patients on immunosuppressants, corticosteroids, or muscle relaxants.
- **Antibody subtyping prerequisite**: Confirm anti-AChR antibody status prior to prescribing. MuSK-antibody–positive patients should not receive Pyridostigmine without specialist oversight, as it may aggravate symptoms in that subtype.
- **Neonatal and pediatric dosing protocol**: If use is extended to neonatal MG (Rank 2 predicted indication), a weight-based dosing protocol must be established given immature renal clearance in newborns.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

