---
layout: default
title: Trimethoprim
parent: 僅模型預測 (L5)
nav_order: 342
evidence_level: L5
indication_count: 2
---

# Trimethoprim
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Trimethoprim: From Bacterial Infections to Conjunctivitis

## One-Sentence Summary

Trimethoprim is a well-established antibacterial agent that inhibits bacterial dihydrofolate reductase (DHFR), blocking folate synthesis, and has been widely used for urinary tract infections and other bacterial infections.

The TxGNN model predicts it may be effective for **conjunctivitis (disease)** — a prediction strongly aligned with Trimethoprim's existing role as a core component of Polytrim ophthalmic solution (polymyxin B + trimethoprim), with **3 clinical trials** and **20 publications** currently supporting this direction.

> **Note:** The top-ranked TxGNN prediction (punctate epithelial keratoconjunctivitis, score 99.57%) has no clinical trial or literature evidence and is rated **Hold (L5)**. The conjunctivitis indication (rank 2, score 99.17%, L2) is the clinically actionable finding and serves as the primary focus of this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (urinary tract, respiratory tract) |
| Predicted New Indication | Conjunctivitis (disease) |
| TxGNN Prediction Score | 99.17% (conjunctivitis, rank 2) |
| Evidence Level | L2 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Trimethoprim acts by competitively inhibiting bacterial dihydrofolate reductase (DHFR), blocking the folate synthesis pathway essential for bacterial DNA replication and cell growth. This bacteriostatic mechanism provides broad-spectrum coverage against the most common bacterial conjunctivitis pathogens — *Staphylococcus aureus*, *Streptococcus pneumoniae*, and *Haemophilus influenzae*. When combined with polymyxin B (the commercially available formulation marketed as Polytrim), it also achieves bactericidal activity against Gram-negative organisms through synergistic disruption of bacterial cell membranes.

Critically, Trimethoprim is already an established component of Polytrim ophthalmic solution, which has been FDA-approved in the United States and used clinically for bacterial conjunctivitis and blepharitis. The TxGNN model's high prediction score (99.17%) almost certainly reflects this strong existing biological and clinical connection — the model is effectively recovering a known, validated use.

However, it is important to note that virtually all supporting clinical trial and literature evidence involves the **combination product** (Polytrim = polymyxin B + trimethoprim), not trimethoprim as a standalone ophthalmic agent. This distinction is clinically meaningful: a trimethoprim-only ophthalmic formulation would require additional validation before regulatory submission, and the more practical repurposing pathway is likely via the polymyxin B combination.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00581542](https://clinicaltrials.gov/study/NCT00581542) | Phase 4 | Completed | 124 | Single-blind RCT directly comparing Polytrim (polymyxin B + trimethoprim) ophthalmic solution vs. moxifloxacin for pediatric conjunctivitis ("pink eye"); investigates whether both treatments are equally effective for this indication |
| [NCT00168532](https://clinicaltrials.gov/study/NCT00168532) | Phase 3 | Completed | 218 | Double-blind placebo-controlled RCT evaluating prophylactic antibiotics (including trimethoprim) during measles infection in Guinea-Bissau to reduce post-measles pneumonia and complications; conjunctivitis was not the primary endpoint — indirect background evidence only |
| [NCT03187834](https://clinicaltrials.gov/study/NCT03187834) | Phase 4 | Completed | 252 | Observational study measuring antibiotic resistance and microbiome changes in children in rural Burkina Faso following antibiotic exposure; trimethoprim functions as an environmental exposure variable rather than an intervention for conjunctivitis — very low direct relevance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [19043945](https://pubmed.ncbi.nlm.nih.gov/19043945/) | 2008 | RCT (Multicenter) | J Pediatr Ophthalmol Strabismus | Multicenter head-to-head comparison of polymyxin B/trimethoprim vs. 0.5% moxifloxacin for speed of clinical efficacy in bacterial conjunctivitis; most directly relevant clinical trial for this indication |
| [30007329](https://pubmed.ncbi.nlm.nih.gov/30007329/) | 2018 | Systematic Review & Meta-analysis | J Pediatric Infect Dis Soc | Meta-analysis of antibiotic treatments — including trimethoprim — for neonatal chlamydial conjunctivitis; provides high-level evidence on trimethoprim's role in neonatal conjunctivitis management |
| [6204534](https://pubmed.ncbi.nlm.nih.gov/6204534/) | 1984 | Controlled Clinical Evaluation | Am J Ophthalmol | Early controlled clinical evaluation of trimethoprim-containing ophthalmic solutions (combined with sulfacetamide and polymyxin B) in patients with bacterial conjunctivitis or blepharitis; establishes foundational efficacy and safety data for trimethoprim ophthalmic formulations |
| [8595639](https://pubmed.ncbi.nlm.nih.gov/8595639/) | 1995 | Prospective Clinical Survey | Clin Ther | Prospective survey of children with acute bacterial conjunctivitis treated with trimethoprim-polymyxin B ophthalmic solution; supports empiric coverage against *H. influenzae* and *S. pneumoniae*, the most common pediatric pathogens |
| [16491721](https://pubmed.ncbi.nlm.nih.gov/16491721/) | 2006 | Clinical Review | J Pediatr Ophthalmol Strabismus | Reviews recommended guidelines for controlling epidemic bacterial conjunctivitis (*S. pneumoniae*), emphasizing agents that minimize symptoms and shorten the infectious period; contextualizes role of antibiotic selection |
| [20084257](https://pubmed.ncbi.nlm.nih.gov/20084257/) | 2001 | Clinical Review | Paediatr Child Health | Comprehensive review of etiology, clinical features, and management of acute infectious conjunctivitis in children; provides clinical framework for appropriate antibiotic selection including trimethoprim combinations |
| [24892274](https://pubmed.ncbi.nlm.nih.gov/24892274/) | 2015 | Case Report | Ophthal Plast Reconstr Surg | Case report of chronic conjunctivitis from *Nocardia nova* on a silicone stent successfully managed with trimethoprim/sulfamethoxazole; illustrates trimethoprim's utility in atypical or resistant ocular bacterial infections |
| [34943657](https://pubmed.ncbi.nlm.nih.gov/34943657/) | 2021 | Retrospective Cohort | Antibiotics (Basel) | Analysis of methicillin-susceptible *S. aureus* (MSSA) ocular infections from Chang Gung Memorial Hospital (Taiwan, 2010–2017); provides regional molecular epidemiology context relevant to antibiotic selection for ocular surface infections |
| [10537781](https://pubmed.ncbi.nlm.nih.gov/10537781/) | 1999 | Case Series / Review | Curr Opin Ophthalmol | Review of ocular manifestations of cat-scratch disease (*Bartonella henselae*), including Parinaud's oculoglandular syndrome; background reference for bacterial conjunctivitis differential diagnosis |
| [6120925](https://pubmed.ncbi.nlm.nih.gov/6120925/) | 1982 | Veterinary Case Series | J Am Vet Med Assoc | Reports keratoconjunctivitis sicca (KCS) in 14 dogs treated with sulfonamides (including sulfadiazine + trimethoprim); serves as an adverse effect signal — note this is a veterinary study and requires caution in human extrapolation |

---

## Philippines Market Information

Trimethoprim currently has no registered products with the Philippine FDA (0 authorizations). The drug is not marketed in the Philippines as either a standalone formulation or as part of a registered ophthalmic combination product.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (conjunctivitis indication)

**Rationale:**
Trimethoprim's ophthalmic combination product (Polytrim) has a well-established clinical track record for bacterial conjunctivitis, supported by a completed Phase 4 RCT, a systematic review and meta-analysis, and multiple controlled clinical evaluations. The mechanism directly covers common conjunctivitis pathogens, and the TxGNN prediction aligns with approved uses in other markets (US FDA). However, the evidence base is for the **polymyxin B + trimethoprim combination**, not trimethoprim monotherapy, and the drug currently has zero Philippines market presence.

**To proceed, the following is needed:**

- **Formulation decision:** Clarify whether the intended repurposing target is trimethoprim monotherapy or the Polytrim combination (polymyxin B + trimethoprim) — existing evidence strongly favors the combination, and this determines the regulatory pathway
- **Philippines registration strategy:** Evaluate whether to pursue FDA Philippines registration for an ophthalmic trimethoprim-containing product (standalone or combination), given zero current local presence
- **Mechanism of action data:** Obtain formal MOA documentation from DrugBank (currently a data gap) to support regulatory submissions and prescriber communications
- **Safety review:** Conduct a systematic review of trimethoprim ophthalmic safety, particularly regarding the KCS (keratoconjunctivitis sicca) risk signal observed in sulfonamide co-administration (PMID 6120925) and Stevens-Johnson syndrome risk associated with trimethoprim class
- **Local epidemiology assessment:** Characterize the conjunctivitis etiology mix in the Philippines (viral vs. bacterial, and dominant bacterial pathogens) to define the patient population most likely to benefit and to support market sizing
- **Top-ranked prediction (punctate epithelial keratoconjunctivitis, 99.57%):** Currently rated **Hold (L5)** — no clinical trials or literature support this indication, and the mechanistic link is weak (the condition is primarily viral or toxic in etiology). Mechanistic studies would be needed before proceeding.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

