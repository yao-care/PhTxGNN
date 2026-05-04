---
layout: default
title: Clotrimazole
parent: 僅模型預測 (L5)
nav_order: 82
evidence_level: L5
indication_count: 3
---

# Clotrimazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Clotrimazole: From Topical Antifungal to Vulvovaginitis

## One-Sentence Summary

Clotrimazole is a synthetic imidazole antifungal agent globally established for treating tinea pedis and oropharyngeal candidiasis, yet currently unregistered in the Philippines.
The TxGNN model predicts it may be effective for **Vulvovaginitis** (candidal), with **over 10 completed clinical trials** and **20 publications** supporting this direction — making it the highest-evidence actionable indication in this multi-indication analysis.
While Acne ranks #1 by TxGNN score (99.86%), it is designated **Hold** due to limited clinical evidence; **Vulvovaginitis** (TxGNN score 99.59%) reaches **L1 evidence level** and earns a **Proceed with Guardrails** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Tinea pedis, oropharyngeal candidiasis (globally established; not registered in Philippines) |
| Predicted New Indication | Vulvovaginitis (Candidal) |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L1 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Proceed with Guardrails** |

> **All TxGNN Predictions in This Pack:**
> | Rank | Indication | TxGNN Score | Evidence Level | Decision |
> |------|------------|------------|----------------|----------|
> | 1 | Acne (disease) | 99.86% | L4 | Hold |
> | 2 | Vulvovaginitis | 99.59% | L1 | Proceed with Guardrails |
> | 3 | Postmenopausal Atrophic Vaginitis | 99.46% | L4 | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on published pharmacological literature, Clotrimazole is an imidazole-class azole antifungal. It inhibits the fungal cytochrome P450 enzyme **lanosterol 14α-demethylase (CYP51)**, which catalyzes a key step in the biosynthesis of ergosterol — the principal sterol that maintains fungal cell membrane integrity. By depleting ergosterol, Clotrimazole causes increased membrane permeability, disruption of membrane-bound enzyme function, and ultimately fungal cell death. This effect is fungistatic at low concentrations and fungicidal at higher local concentrations.

Vulvovaginitis — specifically vulvovaginal candidiasis (VVC) — is caused predominantly by *Candida albicans*, a fungal pathogen entirely dependent on ergosterol biosynthesis for survival. Clotrimazole's direct inhibition of this pathway makes it mechanistically ideal for treating VVC. Topical vaginal formulations (tablets, creams, ovules) achieve high local drug concentrations while minimizing systemic absorption, resulting in a favorable safety profile particularly well-suited for self-administered treatment. Clotrimazole is listed on the **WHO Model List of Essential Medicines** for this indication and routinely serves as the active comparator arm in global VVC clinical trials — a strong indicator of its benchmark status.

Regarding the highest TxGNN-scored prediction (Acne, 99.86%): Clotrimazole does have antifungal activity against *Malassezia furfur*, which causes pityrosporum folliculitis (often called "fungal acne"). However, this is biologically distinct from conventional *C. acnes*-mediated acne vulgaris. The high TxGNN score most likely reflects topological proximity between skin infection nodes in the knowledge graph rather than a validated direct mechanistic pathway for treating standard acne. The single available clinical trial for acne was suspended, and no supporting literature exists — further justifying the Hold recommendation.

---

## Clinical Trial Evidence

### Vulvovaginitis (Primary Indication — L1 Evidence)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00755053](https://clinicaltrials.gov/study/NCT00755053) | Phase 3 | Completed | 466 | Investigator-blinded, active-controlled non-inferiority study comparing Clotrimazole 500 mg ovule vs 500 mg vaginal tablet in vaginal candidiasis; established formulation equivalence — highest-grade direct evidence for this indication. |
| [NCT02180828](https://clinicaltrials.gov/study/NCT02180828) | Phase 4 | Completed | 240 | Case-controlled RCT comparing Clotrimazole vaginal tablet vs oral Fluconazole for severe VVC; evaluated comparative efficacy and safety of the two first-line treatment options. |
| [NCT00313131](https://clinicaltrials.gov/study/NCT00313131) | Phase 3 | Completed | 1,524 | Large effectiveness trial (West Africa) comparing single-dose Tinidazole+Fluconazole vs standard Metronidazole + 3-day vaginal Clotrimazole for syndromic vaginal discharge in primary care; supports Clotrimazole's real-world effectiveness. |
| [NCT02242695](https://clinicaltrials.gov/study/NCT02242695) | Phase 4 | Completed | 150 | Double-blind comparison of Clotrimazole 100 mg (Canesten) vs dequalinium chloride 10 mg (Fluomizin) in VVC; confirmed post-marketing efficacy and patient satisfaction. |
| [NCT04699240](https://clinicaltrials.gov/study/NCT04699240) | Phase 4 | Completed | 140 | Prospective RCT: Clotrimazole vaginal tablet + oral *Lactobacillus* vs Clotrimazole alone for preventing VVC recurrence; assessed adjunctive probiotic benefit. |
| [NCT03005353](https://clinicaltrials.gov/study/NCT03005353) | Phase 2/3 | Completed | 100 | Clotrimazole as active comparator vs cumin seed extract vaginal suppositories for candidal VVC; confirms standard-of-care status as treatment benchmark. |
| [NCT03599323](https://clinicaltrials.gov/study/NCT03599323) | Post-marketing | Completed | 1,033 | Large observational safety study of Clotrimazole 1% cream (Empecid L) for vaginal yeast infection under pharmacist guidance; confirmed real-world tolerability and safety profile. |
| [NCT01230814](https://clinicaltrials.gov/study/NCT01230814) | Phase 2 | Completed | 234 | Monthly Metronidazole + Miconazole (same imidazole class) suppositories vs placebo for preventing recurrent vaginal infections in HIV-negative women; supports class-level efficacy for VVC prevention. |
| [NCT06835361](https://clinicaltrials.gov/study/NCT06835361) | Phase 2/3 | Recruiting | 264 | International RCT comparing Clotrimazole + Lactulose combination suppositories vs Canesten (Clotrimazole monotherapy) in candidal vulvovaginitis; superiority design with ongoing enrollment (completion: Nov 2025). |
| [NCT02860845](https://clinicaltrials.gov/study/NCT02860845) | Phase 4 | Completed | 48 | Pilot multicenter study comparing boric acid + probiotic vaginal capsules vs pharmacological reference controls (including Clotrimazole) for vulvovaginitis. |

### Acne (TxGNN Rank 1 — Limited Evidence)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspended | 80 | Triple combination cream (Beclomethasone + Gentamicin + Clotrimazole) vs comparator in acne with contaminated dermatosis; trial was suspended and Clotrimazole's individual contribution cannot be isolated from the combination. |

---

## Literature Evidence

### Vulvovaginitis (Primary Indication)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [41765149](https://pubmed.ncbi.nlm.nih.gov/41765149/) | 2026 | RCT | Complementary Therapies in Medicine | Head-to-head RCT comparing Clotrimazole vaginal cream vs *Prangos ferulacea* (Jashir) cream for VVC; assessed clinical manifestations and laboratory mycological outcomes — most recent direct RCT for this indication. |
| [39824974](https://pubmed.ncbi.nlm.nih.gov/39824974/) | 2025 | RCT (Triple-blinded) | Scientific Reports | Triple-blinded equivalence RCT (n=126): Mycozin vs Clotrimazole 1% vaginal cream for VVC; rigorous blinding design confirms Clotrimazole as the equivalence benchmark in antifungal cream comparisons. |
| [30565745](https://pubmed.ncbi.nlm.nih.gov/30565745/) | 2019 | RCT | Mycoses | RCT evaluating probiotics + lactoferrin as maintenance therapy in recurrent VVC; Clotrimazole served as standard-of-care comparator, supporting its central role in recurrence management protocols. |
| [2644595](https://pubmed.ncbi.nlm.nih.gov/2644595/) | 1989 | Clinical Trial | Obstetrics and Gynecology | Landmark prospective double-blind RCT (n=42): Clotrimazole 500 mg weekly induced clinical remission in 90.4% of women with recurrent candidal vaginitis; monthly prophylaxis significantly reduced long-term recurrence. |
| [3895960](https://pubmed.ncbi.nlm.nih.gov/3895960/) | 1985 | RCT | American Journal of Obstetrics and Gynecology | Open RCT (n=199) across three clinics: single-dose Clotrimazole 500 mg demonstrated equivalent efficacy to 6-day 100 mg regimen in candidal VVC; established the evidence base for simplified single-dose dosing. |
| [24863842](https://pubmed.ncbi.nlm.nih.gov/24863842/) | 2014 | Narrative Review | Journal of Applied Microbiology | Comprehensive review of Clotrimazole's history, mechanism (ergosterol synthesis inhibition), clinical spectrum (tinea pedis, VVC, oropharyngeal candidiasis), and emerging pharmacological properties beyond antifungal activity. |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Systematic Review | Journal of Women's Health | Systematic review on boric acid and azole-based treatments for recurrent VVC; provides comparative framework and supports azole class (including Clotrimazole) as primary therapy, particularly for non-albicans species. |
| [25976001](https://pubmed.ncbi.nlm.nih.gov/25976001/) | 2015 | Basic Science | Journal of Medical Microbiology | Investigated Clotrimazole antifungal activity against *C. albicans* across growth phases, carbon sources, and morphologies; lactate in vaginal formulations may modulate drug sensitivity and local pH — mechanistic insight for formulation design. |
| [40464716](https://pubmed.ncbi.nlm.nih.gov/40464716/) | 2025 | Review | Expert Review of Anti-Infective Therapy | Expert review on current and future non-invasive azole antifungals for VVC; positions Clotrimazole within the therapeutic landscape alongside newer agents (oteseconazole, ibrexafungerp) and identifies remaining unmet needs in recurrent VVC. |
| [39419780](https://pubmed.ncbi.nlm.nih.gov/39419780/) | 2024 | Observational Study | Journal of Applied Microbiology | Characterized Clotrimazole-induced shifts in vaginal bacteriome and lipid metabolism in VVC patients; elucidated microbial recovery mechanisms and metabolomic changes following antifungal treatment. |

---

## Philippines Market Information

Clotrimazole currently has **no registered products** with the Philippines FDA. No license records exist.

This is a notable gap given Clotrimazole's WHO essential medicine status and its widespread OTC availability throughout ASEAN and other neighboring markets (Taiwan, Singapore, Thailand, Malaysia). There is no authorization table to display.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No drug-drug interaction records were returned from the DDI database query. Philippines FDA prescribing information is unavailable due to the absence of any local registration. Based on published literature, topical and vaginal formulations of Clotrimazole have minimal systemic absorption, substantially limiting systemic adverse effects and interaction potential with co-administered drugs. For regulatory submission purposes, full safety documentation should be obtained from approved prescribing information in reference jurisdictions (US FDA, EMA) prior to dossier preparation.

---

## Conclusion and Next Steps

### Primary Indication — Vulvovaginitis

**Decision: Proceed with Guardrails**

**Rationale:**
Clotrimazole is a globally established first-line treatment for vulvovaginal candidiasis with WHO essential medicine status, supported by multiple completed Phase 3/4 trials (including NCT00755053, n=466 and NCT02180828, n=240) and a robust literature base. Its absence from the Philippines market represents an unmet clinical need rather than an evidence or safety concern.

**To proceed, the following is needed:**
- Clarify Philippines FDA regulatory pathway (new drug application vs. OTC switch classification under RA 9711)
- Compile a registration dossier using reference jurisdiction approvals (US FDA, EMA) under ASEAN Common Technical Dossier (ACTD) format
- Secure GMP-compliant manufacturing documentation or identify a licensed local importer/distributor
- Specify target formulation(s): vaginal tablet (100 mg / 500 mg), vaginal cream (1%), or ovule — each may require a separate application
- Address the safety data gap: obtain and review full product labeling (warnings, contraindications, pregnancy category) from an approved reference market before submission

---

### Secondary Indication — Acne (disease)

**Decision: Hold**

**Rationale:**
The high TxGNN score (99.86%) most likely reflects knowledge graph topological proximity between skin infection disease nodes, not a validated biological pathway for acne vulgaris. The sole relevant trial (NCT01244256) was suspended, involves a three-drug combination that prevents isolating Clotrimazole's individual contribution, and targets contaminated dermatosis rather than classic acne. No supporting literature was identified.

**To reconsider this indication, the following is needed:**
- Mechanistic studies distinguishing Clotrimazole's activity against *Malassezia furfur* (fungal/pityrosporum folliculitis) vs. *C. acnes* (bacterial acne vulgaris)
- A dedicated prospective clinical trial for pityrosporum folliculitis as a clearly defined, separate indication from acne vulgaris

---

### Tertiary Indication — Postmenopausal Atrophic Vaginitis

**Decision: Research Question**

**Rationale:**
The primary driver of atrophic vaginitis is estrogen deficiency causing vaginal mucosal atrophy and elevated pH; Clotrimazole addresses secondary fungal infections but cannot resolve the underlying atrophic pathology. Only one tangentially related trial (NCT04292704, UNKNOWN status, CO2 laser as primary intervention) was identified, with no supporting literature. The TxGNN prediction likely arises from high node overlap with vulvovaginitis in the knowledge graph.

**To explore further:**
- Prospective study of Clotrimazole in postmenopausal women with VVC-complicated atrophic vaginitis as a distinct patient subgroup
- Assess whether combined vaginal estrogen + Clotrimazole is superior to antifungal monotherapy in this population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

