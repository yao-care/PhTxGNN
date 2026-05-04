---
layout: default
title: Clindamycin
parent: 僅模型預測 (L5)
nav_order: 75
evidence_level: L5
indication_count: 6
---

# Clindamycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Clindamycin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Clindamycin is a lincosamide antibiotic with well-established efficacy against serious bacterial infections caused by anaerobic organisms and gram-positive cocci, including skin, soft tissue, and respiratory infections.
The TxGNN model predicts it may have activity against **Punctate Epithelial Keratoconjunctivitis (PEK)**, with **0 clinical trials** and **0 publications** currently supporting this direction — this is a model-only prediction with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (anaerobic, gram-positive; skin, soft tissue, respiratory) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Clindamycin is a lincosamide antibiotic that inhibits bacterial protein synthesis by binding to the 50S ribosomal subunit, thereby blocking peptide elongation. It demonstrates broad activity against anaerobic bacteria, gram-positive cocci (*Staphylococcus aureus*, *Streptococcus* spp.), and select protozoa such as *Toxoplasma gondii*. Its established clinical roles include treatment of skin and soft tissue infections, pelvic inflammatory disease, bacterial vaginosis, and — in combination with other agents — malaria and toxoplasmosis.

Punctate epithelial keratoconjunctivitis is predominantly driven by viral pathogens (most commonly adenovirus), dry eye disease, or drug toxicity — not primary bacterial infection. The mechanistic basis for applying Clindamycin to PEK is therefore weak. Although a secondary bacterial superinfection of a compromised ocular surface could theoretically create a limited niche for antibiotic use, no published clinical studies or preclinical data have investigated Clindamycin specifically for this condition.

The TxGNN model's high prediction score (99.97%) most likely reflects network-level proximity in the knowledge graph rather than established biological plausibility. In the absence of any supporting clinical, epidemiological, or mechanistic evidence, this prediction must be treated with considerable caution, and further validation is required before any translational steps are considered.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Clindamycin currently has **no product authorizations** on record with the Philippine FDA. There are no registered products to list.

> **Note:** This may reflect a data gap in the current dataset. Clindamycin is a widely available antibiotic globally; a direct query to the Philippine FDA (FDA PH) database is recommended to confirm market status.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data including key warnings, contraindications, and drug interactions were not available in this evidence pack. The Philippine FDA product monograph or the DrugBank entry for DB01190 should be consulted prior to any clinical planning.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, punctate epithelial keratoconjunctivitis is primarily a viral or non-infectious condition whose pathophysiology has no meaningful alignment with Clindamycin's antibacterial mechanism of action. The complete absence of clinical trials, human literature, and mechanistic bridging data places this candidate at Evidence Level L5 — the lowest tier — and does not currently justify further investment.

**To proceed, the following is needed:**

- **MOA clarification:** Retrieve Clindamycin's full mechanism of action from DrugBank (DB01190) to confirm whether any anti-inflammatory or non-antibacterial pathway could be relevant to PEK
- **Subtype analysis:** Determine whether any bacterial-etiology PEK subtype exists in which Clindamycin's spectrum of activity would apply (e.g., staphylococcal marginal keratitis vs. classic viral PEK)
- **Safety data:** Download and parse the Philippine FDA package insert (or TFDA/EMA/US FDA label) to populate warnings, contraindications, and DDI data currently missing
- **Philippines registration verification:** Directly query the FDA PH database to confirm whether Clindamycin products are in fact unregistered or whether a data ingestion gap exists
- **Exploratory literature search:** Broaden the PubMed query to include terms such as "clindamycin ophthalmic," "clindamycin ocular surface," and "clindamycin conjunctivitis" to rule out any indirect supporting evidence before formally closing this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

