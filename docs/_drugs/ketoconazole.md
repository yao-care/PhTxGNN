---
layout: default
title: Ketoconazole
parent: 僅模型預測 (L5)
nav_order: 191
evidence_level: L5
indication_count: 1
---

# Ketoconazole
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

Using **txgnn-pipeline** to guide report generation context, and the system-level Drug Repurposing Evaluation Report prompt (v5) for structure. Now generating the full report.

---

# Ketoconazole: From Antifungal Treatment to Acne

## One-Sentence Summary

Ketoconazole is a broad-spectrum imidazole antifungal agent, also known to suppress steroidogenesis via CYP enzyme inhibition, originally used to treat systemic and superficial fungal infections.
The TxGNN model predicts it may be effective for **Acne (Disease)**, with **1 active clinical trial** and **15 publications** currently supporting this direction.
The mechanistic rationale is well-grounded — ketoconazole acts on both *Malassezia* (a yeast frequently implicated in acne-like eruptions) and androgen biosynthesis pathways — but clinical evidence remains early-stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Antifungal (systemic and superficial fungal infections) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 — Observational studies, mechanistic studies, and reviews |
| Philippines Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, ketoconazole is an imidazole-class antifungal that works by inhibiting the fungal cytochrome P450 enzyme **14α-demethylase**, blocking ergosterol synthesis in fungal cell membranes. In addition, ketoconazole is a potent inhibitor of mammalian steroidogenic enzymes — including **CYP17A1** and **CYP11A1** — thereby suppressing both adrenal and gonadal androgen production. This dual action forms the core of the repurposing rationale.

Acne vulgaris has two major drivers that ketoconazole may address: **sebum overproduction driven by androgens**, and **follicular colonisation by lipophilic yeasts** (particularly *Malassezia furfur* / *Pityrosporum ovale*). Malassezia folliculitis is frequently misdiagnosed as acne vulgaris and may co-exist with it; ketoconazole has an established role in treating this condition. Separately, for androgen-driven acne — common in polycystic ovary syndrome (PCOS) and other hyperandrogenic states — ketoconazole's CYP inhibition could suppress sebum production by reducing circulating androgen levels.

The TxGNN high prediction score (0.9980) partially reflects the close knowledge-graph proximity between *Malassezia*, Pityrosporum folliculitis, and acne. It is important to note that **acne subtype matters**: ketoconazole's benefit is most plausible in Malassezia folliculitis, PCOS-associated acne, and seborrhoea-predominant subtypes, and less established in standard comedonal acne vulgaris caused purely by *Cutibacterium (Propionibacterium) acnes*.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT07237763](https://clinicaltrials.gov/study/NCT07237763) | N/A | Active, Not Recruiting | 52 | Randomised head-to-head comparison of topical ketoconazole 2% cream vs. topical adapalene 0.1% cream for mild comedonal and papulopustular acne over 12 weeks; aims to assess whether ketoconazole is a viable, better-tolerated alternative to retinoids. No results published yet. |

> **Note:** This trial does not carry a formal clinical phase designation (Phase NA). With only 52 participants and no published results, it provides proof-of-concept interest but cannot yet establish efficacy at an L1 or L2 level.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28111792](https://pubmed.ncbi.nlm.nih.gov/28111792/) | 2017 | Lab Study | *Microbiology and Immunology* | Ketoconazole directly inhibits *Propionibacterium acnes* lipase activity and growth — the key mechanism by which P. acnes metabolises sebum to trigger inflammation; positions ketoconazole as an alternative for antibiotic-resistant acne strains |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In Vitro Study | *Biological & Pharmaceutical Bulletin* | Azole antifungals including ketoconazole demonstrate measurable anti-*P. acnes* activity in vitro; updates earlier azole-acne data with newer agents and confirms class-level activity |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Case Series | *Clinical and Experimental Dermatology* | 62 patients with Pityrosporum folliculitis (frequently misdiagnosed as acne vulgaris) confirmed histologically; ketoconazole used in therapeutic trials, reinforcing its role in yeast-driven acne-like eruptions |
| [8255067](https://pubmed.ncbi.nlm.nih.gov/8255067/) | 1993 | Review | *Keio Journal of Medicine* | Comprehensive review of *Pityrosporum ovale*-associated skin diseases including seborrhoeic dermatitis and folliculitis; establishes the biological link between this yeast and acne-spectrum conditions |
| [12566804](https://pubmed.ncbi.nlm.nih.gov/12566804/) | 2003 | Review | *Dermatology (Basel)* | Systemic acne treatment update; ketoconazole discussed as an anti-androgen option for moderate-to-severe acne, particularly in the context of hormonal acne management |
| [8090657](https://pubmed.ncbi.nlm.nih.gov/8090657/) | 1993 | Clinical Trial | *Polski Tygodnik Lekarski* | Ketoconazole evaluated in PCOS-associated hyperandrogenism; reduction in hirsutism, acne, and seborrhoea observed within 3 months of treatment — directly supporting the anti-androgen acne mechanism |
| [33216275](https://pubmed.ncbi.nlm.nih.gov/33216275/) | 2021 | RCT (Phase 3) | *Pituitary* | Levoketoconazole (the R-enantiomer) demonstrated efficacy in Cushing's syndrome (SONICS trial) including improvement of acne as a clinical sign of hypercortisolism; validates the CYP-mediated cortisol/androgen suppression pathway at trial level |
| [19445767](https://pubmed.ncbi.nlm.nih.gov/19445767/) | 2009 | Review | *BMJ Clinical Evidence* | PCOS review; acne, hirsutism, and seborrhoea are highlighted as androgen-driven features of PCOS, establishing the clinical context in which ketoconazole's anti-androgenic mechanism is most relevant |
| [8629828](https://pubmed.ncbi.nlm.nih.gov/8629828/) | 1996 | Case/Cohort | *Archives of Dermatology* | Neonatal papulopustular facial eruptions associated with *Malassezia furfur* infection; frequently clinically indistinguishable from neonatal acne — underscores the importance of distinguishing Malassezia-driven disease when considering ketoconazole |
| [23600337](https://pubmed.ncbi.nlm.nih.gov/23600337/) | 2013 | Review | *FP Essentials* | Differential diagnosis of neonatal and infantile acne vs. Malassezia-related eruptions reviewed; clinically relevant for patient selection if ketoconazole is to be used in acne management |

---

## Philippines Market Information

Ketoconazole currently has **no registered product authorisations in the Philippines**. The drug is classified as **not marketed** in the local regulatory database.

> For reference on global approved indications and labelling, clinicians should consult the originator (Janssen) product information or the U.S. FDA / EMA label directly. Note that the U.S. FDA withdrew systemic oral ketoconazole from the antifungal market in 2013 due to hepatotoxicity concerns, restricting its systemic use; topical formulations remain available in many markets.

---

## Safety Considerations

Detailed local safety data (warnings, contraindications, drug interactions) are not available in this Evidence Pack. However, several globally recognised safety signals for ketoconazole are clinically important and should be reviewed before proceeding:

- **Hepatotoxicity**: Systemic ketoconazole carries a well-documented risk of serious liver injury (U.S. FDA Black Box Warning for oral formulations). This is the primary reason oral ketoconazole was withdrawn from systemic antifungal use in many markets.
- **CYP3A4 inhibition**: Ketoconazole is a potent inhibitor of CYP3A4 and P-glycoprotein, leading to numerous clinically significant drug-drug interactions.
- **QT prolongation risk**: Co-administration with QT-prolonging drugs requires caution.
- **Topical formulations** (relevant to the identified clinical trial): Topical ketoconazole has a substantially more favourable safety profile than oral, with minimal systemic absorption.

Please refer to the current package insert and local regulatory guidance for the complete safety profile.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the mechanistic case for ketoconazole in acne is scientifically credible — particularly for Malassezia folliculitis and androgen-driven acne — clinical evidence is currently limited to a single small, unpublished randomised trial and a body of mechanistic or indirect observational literature (L3). Additionally, the drug has no Philippines market registration, and critical safety data (including local warnings and DDI profile) are absent from this Evidence Pack.

**To proceed, the following is needed:**

- **Safety data gap closure**: Obtain the complete prescribing information / SmPC for ketoconazole, including hepatotoxicity warnings, contraindications, and CYP3A4 interaction profile (DG001, DG002)
- **Route-of-administration clarification**: Determine whether the intended indication is for **topical** formulations only (lower risk, more feasible) or systemic oral use (higher risk, likely infeasible given FDA hepatotoxicity restrictions)
- **Clinical trial results**: Await and review results from NCT07237763 once completed (expected Dec 2025)
- **Acne subtype specification**: Define the target population precisely — Malassezia folliculitis vs. hormonal (PCOS) acne vs. standard acne vulgaris — as the mechanism and evidence base differ substantially by subtype
- **Philippines regulatory pathway assessment**: Confirm whether a topical ketoconazole formulation could be registered or an existing regional marketing authorisation could be leveraged
- **MOA documentation**: Formally document the dual anti-Malassezia / anti-androgen mechanism to support any regulatory submission or institutional review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

