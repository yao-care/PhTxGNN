---
layout: default
title: Sulfacetamide
parent: 僅模型預測 (L5)
nav_order: 317
evidence_level: L5
indication_count: 10
---

# Sulfacetamide
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

# Sulfacetamide: From Bacterial Conjunctivitis to Otitis Externa

## One-Sentence Summary

Sulfacetamide is a topical sulfonamide antibiotic historically used for bacterial conjunctivitis and superficial ocular surface infections.
While the TxGNN model's highest-scoring prediction is **Postinfectious Vasculitis** (rank #1), that candidate carries no supporting evidence and a mechanistic safety concern — sulfonamides can themselves trigger drug-induced vasculitis.
**Otitis Externa** (TxGNN rank #3, score 99.99%) is the highest-evidence repurposing candidate in this pack, supported by **2 double-blind RCTs** from the 1970s–1980s; this report focuses on Otitis Externa as the most actionable opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial conjunctivitis / topical antibacterial (not registered in Philippines) |
| Predicted New Indication | Otitis Externa |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Sulfacetamide is a sulfonamide-class bacteriostatic antibiotic. Sulfonamides work by competitively inhibiting dihydropteroate synthase (DHPS), blocking bacterial folate synthesis and halting DNA replication in susceptible organisms. This mechanism is effective against the gram-positive and gram-negative species most commonly responsible for external ear canal infections, including *Staphylococcus aureus*, *Streptococcus* species, and some *Pseudomonas* strains.

Otitis externa is primarily a bacterial (and occasionally fungal) infection of the external auditory canal — a moist, closed surface directly accessible to topical antimicrobial therapy. This delivery context aligns exactly with sulfacetamide's established ophthalmic use: both the conjunctival sac and the ear canal are topically accessible surfaces where systemic absorption is unnecessary. The same bacteriostatic mechanism that clears conjunctivitis can plausibly suppress bacterial overgrowth in the ear canal.

Historical clinical practice confirms this rationale. Sodium Sulamyd 30% solution (a sulfacetamide preparation) was used for otitis externa as early as the 1950s. Subsequently, combination ear drops containing trimethoprim-sulphacetamide-polymyxin B (TSP) were evaluated in randomised trials in the 1970s–1980s, demonstrating efficacy superior to trimethoprim-polymyxin alone and comparable to gentamicin. Detailed MOA data was not available from DrugBank in this evidence pack; the above mechanistic description draws on established pharmacological knowledge for sulfonamide-class antibiotics.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for Sulfacetamide in otitis externa.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [6269476](https://pubmed.ncbi.nlm.nih.gov/6269476/) | 1981 | RCT (Double-Blind) | Annales d'oto-laryngologie | TSP (trimethoprim-sulphacetamide-polymyxin B) vs TP (trimethoprim-polymyxin B) ear drops in 68 patients with otitis externa, otorrhoea, or mastoid infections: TSP achieved 88.6% success vs 60.6% for TP (statistically significant) |
| [207210](https://pubmed.ncbi.nlm.nih.gov/207210/) | 1978 | RCT (Double-Blind) | Annales d'oto-laryngologie | TSP ear drops vs gentamicin ear drops in 100 otorrhoea cases (external otitis, perforated otitis media, mastoid/postoperative infections): TSP 84% positive results (42/50), gentamicin 80% (40/50) — non-inferior performance |
| [13095457](https://pubmed.ncbi.nlm.nih.gov/13095457/) | 1953 | Case Series | Eye, Ear, Nose & Throat Monthly | Sodium Sulamyd 30% solution applied directly to otitis externa and chronic otitis media; earliest documented use of sulfacetamide as an ear preparation |
| [14867160](https://pubmed.ncbi.nlm.nih.gov/14867160/) | 1951 | Case Report | Vestnik Otorinolaringologii | Sulfacyl-sodium (sodium sulfacetamide) in chronic suppurative otitis media and external auditory canal inflammation; early Russian-language clinical documentation |

---

## Philippines Market Information

Sulfacetamide is currently **not registered** with the Philippine Food and Drug Administration. No marketing authorizations are on record for any dosage form or indication.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Additional safety signal identified in the literature search:** A case report (PMID [3157322](https://pubmed.ncbi.nlm.nih.gov/3157322/), *American Journal of Ophthalmology*, 1985) documented **erythema multiforme major** in a pediatric patient following topical sodium sulfacetamide administration for conjunctivitis. The patient had no documented sulfonamide allergy, and prior systemic TMP-SMX exposure had been uneventful. This highlights that topical sulfonamides can trigger severe systemic hypersensitivity reactions — sulfonamide allergy history must be explicitly screened before use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two double-blind RCTs demonstrate that sulphacetamide-containing ear drops achieve 84–89% clinical success in otitis externa — comparable to gentamicin and statistically superior to trimethoprim-polymyxin B alone. The mechanistic rationale is direct and consistent with sulfacetamide's established topical antibacterial use. However, sulfacetamide was tested as part of the TSP combination (not as a standalone agent), both pivotal trials are over 40 years old, and the drug is not currently registered in the Philippines.

**To proceed, the following is needed:**

- Retrieve complete MOA and safety data from DrugBank (DB00634) to fill Data Gaps DG001 and DG002
- Confirm whether standalone sulfacetamide otic preparations have been studied in modern trials; commission a targeted systematic review if not
- Benchmark against current Philippine standard-of-care for otitis externa (fluoroquinolone ear drops such as ciprofloxacin/ofloxacin) to establish a non-inferiority target
- Assess Philippines FDA regulatory pathway for a new topical otic formulation registration
- Design mandatory sulfonamide hypersensitivity screening protocol before any clinical application, given the erythema multiforme signal
- Clarify whether TSP combination synergy is essential or if sulfacetamide alone achieves equivalent efficacy — this determines whether a monotherapy or fixed-dose combination should be developed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

