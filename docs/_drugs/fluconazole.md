---
layout: default
title: Fluconazole
parent: 僅模型預測 (L5)
nav_order: 142
evidence_level: L5
indication_count: 1
---

# Fluconazole
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

# Fluconazole: From Fungal Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Fluconazole is a second-generation triazole antifungal agent, widely used in the treatment of systemic and superficial fungal infections by blocking ergosterol biosynthesis in fungal cell membranes.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis (PEK)**,
however, **no clinical trials or published literature** currently support this repurposing hypothesis — the prediction rests entirely on knowledge graph topology, placing it at model-prediction-only level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Fungal infections (systemic and superficial) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Fluconazole is a second-generation triazole antifungal. Its mechanism centres on selective inhibition of the fungal cytochrome P450 enzyme CYP51 (lanosterol 14α-demethylase), which is a rate-limiting step in ergosterol biosynthesis. Without ergosterol, the fungal cell membrane loses structural integrity and the organism cannot survive. This mechanism is highly selective for fungal cells over mammalian cells, which is why Fluconazole has a favourable systemic safety profile.

Punctate Epithelial Keratoconjunctivitis (PEK) is a clinical syndrome defined by scattered punctate lesions on the corneal epithelium. The aetiology is broad: adenoviral or herpes simplex virus infection accounts for the majority of cases, followed by toxic/drug-induced reactions, Thygeson's superficial punctate keratitis (an immune-mediated entity), and dry eye disease. Fungal keratoconjunctivitis is a less common but recognised cause and can present with a PEK-like picture — this is the conceptual bridge the knowledge graph has likely exploited.

The high TxGNN score (0.992) most plausibly reflects an indirect graph path: **Fluconazole → fungal infection → ocular fungal infection → PEK**, rather than a direct mechanistic or clinical link. Because fungal aetiology represents only a minority fraction of all PEK cases, and because there is zero clinical trial or literature evidence specifically supporting this repurposing direction, the prediction should be interpreted as a hypothesis-generating signal rather than a validated therapeutic opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.24%), the proposed mechanistic link is indirect and disease-subtype-specific — Fluconazole's antifungal activity would only be relevant to the fungal-caused subset of PEK, which is a minority of all cases. Combined with zero supporting clinical trials, zero supporting publications, and no current registration in the Philippines, the evidence base is insufficient to advance this candidate.

**To proceed, the following is needed:**
- **Aetiology stratification**: Clarify whether the target PEK population is specifically of confirmed fungal origin; if so, this may fall under Fluconazole's existing antifungal indications and not require formal repurposing
- **Literature deep-dive**: Conduct a broader PubMed search for Fluconazole in ocular fungal infections (fungal keratitis, fungal endophthalmitis) with PEK as a clinical presentation to surface any indirect case-level evidence
- **MOA data**: Retrieve complete mechanism of action data from DrugBank (DB00196) to refine the biological plausibility assessment
- **Safety data**: Download the Philippine package insert (or FDA-approved label) to complete the key warnings, contraindications, and drug–drug interaction profile
- **Formulation assessment**: Determine whether an ophthalmic-route formulation of Fluconazole (eye drops or intravitreal) is commercially available or feasible, given that systemic Fluconazole does achieve ocular penetration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

