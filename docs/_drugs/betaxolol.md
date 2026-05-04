---
layout: default
title: Betaxolol
parent: 僅模型預測 (L5)
nav_order: 41
evidence_level: L5
indication_count: 1
---

# Betaxolol
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

# Betaxolol: From Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Betaxolol is a selective β1-adrenergic receptor blocker conventionally used for hypertension and open-angle glaucoma management.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**,
with **0 clinical trials** and **0 publications** currently identified for this specific indication — making this a purely model-driven hypothesis at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indications on file in the Philippines (not marketed) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 (Model prediction only — no clinical trials or literature identified) |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory file. However, based on the pharmacological profile captured in the evidence pack, Betaxolol is a **selective β1-adrenergic receptor antagonist** that acts on the ciliary body of the eye. By blocking β1 receptors, it suppresses adenylyl cyclase activity, reduces cyclic AMP (cAMP) synthesis, and ultimately decreases aqueous humor production by approximately 20–35% — translating into a measurable reduction in intraocular pressure (IOP). This pathway is summarised as: **β1-AR → adenylyl cyclase ↓ → cAMP ↓ → aqueous humor production ↓ → IOP ↓**.

Primary hereditary glaucoma is a genetically defined disease driven primarily by mutations in **CYP1B1** and **MYOC** genes, which cause structural abnormalities of the trabecular meshwork and anterior chamber angle. The result is impaired aqueous drainage — not reduced production — causing IOP to climb and ultimately damaging the optic nerve. While Betaxolol's mechanism addresses the production side rather than the drainage obstruction, reducing production load still provides a clinically relevant IOP-lowering effect even when drainage is structurally impaired. The TxGNN model likely captures this shared final common pathway (elevated IOP → optic nerve injury) as a strong mechanistic link.

An additional dimension that strengthens this prediction is Betaxolol's partial calcium channel blocking activity, which is absent in non-selective beta-blockers such as timolol. This property may confer **direct neuroprotection** to retinal ganglion cells, a property of particular long-term value in a hereditary, progressive condition like primary hereditary glaucoma. Furthermore, its β1 selectivity reduces the risk of bronchospasm, making it comparatively safer in paediatric patients and those with respiratory comorbidities — a relevant consideration given the early-onset nature of hereditary glaucoma.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Betaxolol in primary hereditary glaucoma.

---

## Literature Evidence

Currently no related literature available for Betaxolol specifically in primary hereditary glaucoma.

---

## Philippines Market Information

Betaxolol is currently not registered or marketed in the Philippines. No authorization records are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a very high prediction score (99.74%) and the underlying mechanistic rationale — IOP reduction through β1-receptor blockade plus potential neuroprotection — is scientifically coherent for a hereditary glaucoma indication. However, no clinical trials or publications specific to primary hereditary glaucoma were identified, placing this at Evidence Level L5. The evidence base is insufficient to support any regulatory or commercial action at this time.

**To proceed, the following is needed:**

- **Literature deep-dive**: Broaden the search to include Betaxolol in paediatric glaucoma, congenital glaucoma, and CYP1B1/MYOC mutation carriers to determine whether adjacent evidence exists
- **Mechanism of action data**: Retrieve the full DrugBank MOA entry (Data Gap DG002) to formally confirm pharmacological classification and receptor selectivity profile
- **Package insert / safety data**: Obtain the TFDA or originator label (Data Gap DG001) to complete the safety screening required for Stage S1
- **IOP-lowering comparator data**: Assess whether existing open-angle glaucoma trial data for Betaxolol can serve as a bridge dataset for the hereditary subtype
- **Preclinical / genetic model evidence**: Commission a systematic literature review for Betaxolol in CYP1B1 or MYOC animal models, which could elevate this to L4 and justify a formal feasibility study
- **Philippines regulatory pathway**: Since Betaxolol has no Philippines registration, an initial registration for the established glaucoma indication would need to precede any repurposing effort
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

