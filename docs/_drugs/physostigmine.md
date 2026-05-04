---
layout: default
title: Physostigmine
parent: 僅模型預測 (L5)
nav_order: 176
evidence_level: L5
indication_count: 1
---

# Physostigmine
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

# Physostigmine: From Anticholinergic Antidote to Primary Hereditary Glaucoma

## One-Sentence Summary

Physostigmine is a reversible acetylcholinesterase (AChE) inhibitor historically used as an antidote for anticholinergic poisoning and as an early miotic agent for open-angle glaucoma.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma** with a prediction score of **99.59%**,
however there are currently **no registered clinical trials** and **no supporting publications** specific to this indication — the evidence rests entirely on mechanistic plausibility.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Philippines; historically used as anticholinergic antidote and miotic/IOP-lowering agent |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Physostigmine reversibly inhibits acetylcholinesterase (AChE), preventing the breakdown of acetylcholine (ACh) at synaptic junctions. In the eye, the resulting accumulation of ACh activates Muscarinic M3 receptors on the ciliary muscle, triggering ciliary muscle contraction and pupillary miosis. This mechanical action widens the open surface area of the trabecular meshwork, reduces aqueous humor outflow resistance, and lowers intraocular pressure (IOP). This cascade — **AChE inhibition → ↑ACh → M3 activation → trabecular meshwork dilation → ↓IOP** — is one of the most well-characterized mechanisms in ophthalmic pharmacology and formed the basis for physostigmine's historical clinical use in glaucoma.

Primary hereditary glaucoma (caused by mutations in genes such as *CYP1B1*, *LTBP2*, and *TEK*) shares a core pathological mechanism: impaired aqueous humor drainage leading to chronically elevated IOP and progressive optic nerve damage. Because physostigmine acts directly downstream of the aqueous outflow pathway — independent of the upstream genetic defect — the TxGNN model's prediction carries strong mechanistic plausibility. The drug is essentially targeting the final common pathological step (elevated IOP) rather than the specific genetic cause.

That said, meaningful limitations must be acknowledged. Primary hereditary glaucoma predominantly presents in infants and young children (congenital/infantile onset), raising serious pediatric safety concerns due to physostigmine's narrow therapeutic index and risk of systemic cholinergic toxicity. Furthermore, in genetic forms of glaucoma, structural trabecular meshwork dysgenesis (e.g., Barkan's membrane) may mechanically limit the effectiveness of miotics. Contemporary clinical guidelines overwhelmingly prioritize surgical intervention (goniotomy, trabeculotomy) as first-line therapy; pharmacological IOP lowering serves only as a bridge or adjunct. These factors substantially constrain the translational path for this candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Physostigmine currently has **no registered drug products** with the Food and Drug Administration of the Philippines. No active license records are on file.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---|---|---|---|
| — | — | — | No registrations found |

---

## Safety Considerations

Detailed warnings, contraindications, and drug interaction data were not available in the current Evidence Pack. Please refer to the official package insert for complete safety information.

> **Known pharmacological safety signals to be aware of prior to any further evaluation:** Physostigmine carries a well-documented risk of **cholinergic toxicity** (bradycardia, bronchospasm, excessive secretions, seizures) due to its systemic AChE inhibitory activity. Contraindications generally include asthma/COPD, mechanical gastrointestinal or urinary tract obstruction, bradycardia, and concomitant use with depolarizing neuromuscular blockers. In pediatric populations — the primary affected group in hereditary glaucoma — systemic absorption from ophthalmic preparations raises heightened concern. A full safety assessment from the DrugBank record and relevant package inserts is an essential prerequisite before advancing this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the mechanistic rationale connecting physostigmine's IOP-lowering action to primary hereditary glaucoma is pharmacologically coherent and the TxGNN prediction score is high (99.59%), the complete absence of clinical trial data and disease-specific literature, combined with zero Philippines market presence and significant unresolved pediatric safety concerns, means this candidate cannot advance beyond hypothesis generation at this stage.

**To proceed, the following is needed:**

- **Literature gap-fill:** Systematic review of physostigmine and related miotics (pilocarpine, carbachol) in congenital and hereditary glaucoma — both historical and modern evidence
- **Pediatric safety assessment:** Evaluate systemic absorption, dosing feasibility, and cholinergic toxicity risk specifically in infants and children
- **Genetic subtype analysis:** Determine whether *CYP1B1* / *LTBP2* / *TEK* mutation subtypes respond differentially to miotic agents given their distinct trabecular meshwork pathologies
- **Formulation compatibility review:** Assess whether a topical ophthalmic formulation (drops/gel) can achieve therapeutic IOP reduction while minimizing systemic exposure in pediatric patients
- **MOA data retrieval:** Obtain complete mechanism of action details from DrugBank API (DG002 remediation)
- **Safety data retrieval:** Retrieve and parse the official package insert for warnings and contraindications (DG001 remediation — currently Blocking severity)
- **Philippines regulatory pathway:** If preclinical evidence is supportive, initiate preliminary assessment of the FDA Philippines registration pathway for an orphan/rare disease indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

