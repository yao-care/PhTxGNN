---
layout: default
title: Mannitol
parent: 僅模型預測 (L5)
nav_order: 213
evidence_level: L5
indication_count: 10
---

# Mannitol
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

The txgnn-pipeline skill is focused on data pipeline operations; the report format is defined by my system prompt. Proceeding with report generation now.

---

# Mannitol: From Intracranial Hypertension to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Mannitol is a classical osmotic diuretic with well-established intravenous use for reducing cerebral edema and intracranial pressure, and inhaled use as a bronchial challenge agent.
The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**,
with **0 clinical trials** and **1 publication** currently available to support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Intracranial hypertension / cerebral edema (no Philippines registration on file) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Mannitol is a non-metabolizable polyol that is freely filtered at the renal glomerulus and not reabsorbed by tubular cells. This property makes it an osmotic diuretic: after IV administration, it raises plasma osmolarity, draws intracellular water into the vascular compartment, and obligates free-water excretion in the tubular lumen independent of antidiuretic hormone (ADH) signaling. This mechanism underpins its use in reducing cerebral edema and intracranial hypertension, acute glaucoma, and acute water intoxication — all conditions where rapid reduction of free-water burden is the goal.

Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) is a rare X-linked disorder caused by constitutively activating mutations in the V2 vasopressin receptor gene (*AVPR2*). Unlike SIADH, where ADH is secreted inappropriately, NSIAD involves the receptor itself firing without ligand, causing persistent urinary concentration and dilutional hyponatremia. Critically, V2 antagonists (e.g., tolvaptan) are ineffective in NSIAD because the defect lies downstream of ligand binding.

The theoretical bridge to Mannitol lies precisely here: osmotic diuresis bypasses the V2 receptor axis entirely. By increasing tubular osmolarity through a receptor-independent route, Mannitol could in principle drive free-water excretion and correct hyponatremia in NSIAD patients who cannot be treated with tolvaptan. This mechanism is analogous to how Mannitol is employed in acute water intoxication. However, NSIAD is a chronic condition requiring sustained management, and Mannitol is not suited for chronic use due to risks of rebound, electrolyte depletion, and renal toxicity. The prediction therefore represents a mechanistically plausible but clinically unvalidated hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Clinical Review | European Journal of Internal Medicine | Describes 10 common diagnostic pitfalls in hyponatremia evaluation — relevant to the differential diagnosis of NSIAD vs. SIADH, but does not evaluate Mannitol as a treatment for NSIAD |

---

## Philippines Market Information

Mannitol (DrugBank ID: DB00742) currently has **no registered products** with the Philippines FDA. No authorization numbers or approved indications are available to report.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting evidence for Mannitol in NSIAD is a single indirect clinical review on hyponatremia evaluation pitfalls (L4); no clinical trials targeting this indication exist, and Mannitol has no current Philippines registration, making any development pathway premature.

**To proceed, the following is needed:**

- Obtain and review the TFDA package insert to characterize key warnings, contraindications, and known toxicities (Data Gap DG001 — Blocking)
- Retrieve full DrugBank MOA entry to formally document the osmotic diuresis mechanism and receptor-independent pathway (Data Gap DG002 — High)
- Conduct a focused literature search for Mannitol or osmotic diuretics specifically in NSIAD or V2-gain-of-function hyponatremia case series
- Assess feasibility of chronic osmotic diuretic use in the NSIAD population (electrolyte monitoring burden, renal function requirements, route limitations)
- Evaluate alternative Philippines regulatory pathways or analogous approved products before committing to a local development plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

