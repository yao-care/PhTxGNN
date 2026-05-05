---
layout: default
title: Pilocarpine
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 1
---

# Pilocarpine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Pilocarpine: From Glaucoma Management to Primary Hereditary Glaucoma

## One-Sentence Summary

Pilocarpine is a well-established muscarinic receptor (M3) agonist, classically used to reduce intraocular pressure (IOP) in open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**, a genetically determined subtype characterised by structural defects of the trabecular meshwork.
Currently, **no clinical trials** and **no publications** specifically supporting this repurposing direction are available, placing evidence at the lowest tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Open-angle glaucoma / ocular hypertension (well-known pharmacological use; no Philippines registration record available) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Pilocarpine acts as a direct muscarinic M3 receptor agonist. By contracting the ciliary muscle, it mechanically opens the trabecular meshwork, increases aqueous humor outflow, and lowers intraocular pressure (IOP). This mechanism maps directly onto the core pathological driver of all glaucoma subtypes — elevated IOP — which explains why the TxGNN knowledge-graph model assigned an exceptionally high prediction score of 0.9983.

Primary hereditary glaucoma covers genetically defined subtypes including congenital glaucoma (typically driven by *CYP1B1* mutations) and juvenile open-angle glaucoma (JOAG, typically *MYOC* mutations). In these forms the trabecular network has a developmental structural defect present from birth or early life, rather than an acquired one. While pilocarpine's cholinergic mechanism is biologically plausible for IOP reduction, structural and developmental trabecular abnormalities may substantially attenuate the drug's pressure-lowering response. Surgical intervention (goniotomy, trabeculotomy) remains the established standard of care for most hereditary glaucoma presentations, with pharmacotherapy playing only an adjunctive or temporising role.

The TxGNN prediction is therefore mechanistically grounded — pilocarpine targets the same biological node (IOP) that is dysregulated in hereditary glaucoma — but the specific structural substrate of the disease introduces an important caveat. Whether the cholinergic mechanism retains sufficient efficacy in the context of genetically abnormal trabecular tissue requires dedicated experimental and clinical validation before any repurposing decision can be made.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Pilocarpine currently holds **no registered products** with the Philippines FDA. There are no authorisation records, no approved indications on file, and no market presence to draw upon. Any future repurposing programme would need to navigate a full regulatory registration pathway in the Philippines from the outset.

---

## Safety Considerations

No safety data were retrievable for this report (warnings, contraindications, and drug–drug interaction records are all absent from the current Evidence Pack).

> Please refer to the official package insert and DrugBank entry (DB01085) for complete safety information prior to any clinical or regulatory use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although pilocarpine has a well-understood and directly relevant mechanism for IOP reduction, there is currently zero clinical or published evidence specifically supporting its use in primary hereditary glaucoma (L5). The genetically driven structural trabecular defects characteristic of this subtype may substantially limit drug response, and surgery — not pharmacotherapy — is the accepted standard treatment. Proceeding without foundational evidence would be premature.

**To proceed, the following is needed:**

- **Literature gap-fill**: Conduct a systematic PubMed / Embase search for pilocarpine (or cholinergic agents broadly) in congenital glaucoma, CYP1B1-associated glaucoma, and JOAG to determine whether any indirect evidence exists
- **Mechanism validation**: Assess in preclinical or ex-vivo trabecular models whether M3-agonism retains IOP-lowering activity in the presence of CYP1B1 / MYOC mutations
- **Clinical trial landscape review**: Screen ClinicalTrials.gov and ICTRP for broader pilocarpine ophthalmic trials that may enrol hereditary-glaucoma subpopulations
- **Safety data retrieval**: Download the Philippine FDA (or international) package insert PDF and DrugBank API record to populate warnings, contraindications, and DDI profile (currently all Data Gap / Blocking severity per DG001)
- **MOA data retrieval**: Query DrugBank API (DB01085) to formally document mechanism of action for regulatory submissions (DG002, High severity)
- **Philippines regulatory pathway**: Engage FDA Philippines on the registration requirements for a novel ophthalmic indication given current zero-license status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

