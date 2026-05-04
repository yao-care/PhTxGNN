---
layout: default
title: Bedaquiline
parent: 僅模型預測 (L5)
nav_order: 38
evidence_level: L5
indication_count: 10
---

# Bedaquiline
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

# Bedaquiline: From MDR Tuberculosis to Bovine Tuberculosis

## One-Sentence Summary

Bedaquiline is a first-in-class diarylquinoline antibiotic approved internationally for multidrug-resistant tuberculosis (MDR-TB) treatment, working by selectively inhibiting the mycobacterial F₀F₁-ATP synthase.
The TxGNN model predicts it may be effective for **Bovine Tuberculosis** (*Mycobacterium bovis* infection) with a score of **99.96%**, supported by **0 clinical trials** and **3 in vitro publications** for this specific indication.
Notably, the second-ranked prediction—**Inactive (Latent) Tuberculosis**—carries significantly stronger clinical evidence (**3 clinical trials** including one Phase 2/3 trial, **20 publications**, Evidence Level L2) and represents the more immediately actionable repurposing opportunity identified in this analysis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Philippines (internationally approved for MDR-TB treatment) |
| Predicted New Indication | Tuberculosis, Bovine (*M. bovis* infection) |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Bedaquiline (also known as TMC207 or R207910) is the first genuinely novel anti-tuberculosis antibiotic mechanism introduced in over 40 years. Based on in vitro selectivity studies (PMID 19075053), its mechanism centers on highly selective inhibition of the **F₀F₁-ATP synthase c subunit** in mycobacteria. The same study demonstrated that human mitochondrial ATP synthase shows more than 20,000-fold lower sensitivity to bedaquiline than mycobacterial ATP synthase—explaining both its potent bactericidal activity and its relative tolerability in humans. Critically, bedaquiline retains activity against **non-replicating (dormant) mycobacteria**, because ATP synthase remains essential for energy maintenance even in metabolically quiescent bacteria; this property is mechanistically relevant to both latent and drug-resistant TB contexts.

*Mycobacterium bovis*, the causative agent of bovine tuberculosis, belongs to the *Mycobacterium tuberculosis* complex (MTBC). Within MTBC, the F₀F₁-ATP synthase c subunit—bedaquiline's primary binding site—is highly conserved at the amino acid sequence level. This structural conservation provides the core mechanistic justification for the TxGNN prediction: activity against *M. tuberculosis* theoretically extrapolates to *M. bovis*. Standardized MIC determination methodology for bedaquiline against *M. tuberculosis* H37Rv has been characterized (PMID 27210281), and assay techniques to prevent drug carryover artifacts have been validated (PMID 18480227)—both essential methodological prerequisites for extending susceptibility testing to *M. bovis*.

There are, however, important caveats. All three supporting publications tested bedaquiline against *M. tuberculosis* only; none directly characterized its activity against *M. bovis*. Moreover, bovine tuberculosis is primarily a veterinary disease and a zoonotic public health concern, not a standard human therapeutic target. The regulatory, logistical, and clinical frameworks for treating *M. bovis* infection in animals or at-risk humans differ substantially from those governing human MDR-TB treatment. The high TxGNN score most likely reflects MTBC family-level clustering in the knowledge graph rather than direct empirical evidence for this specific indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Tuberculosis, Bovine.

---

## Literature Evidence

*(Evidence for primary prediction: Tuberculosis, Bovine)*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [27210281](https://pubmed.ncbi.nlm.nih.gov/27210281/) | 2016 | In vitro / Methodological | Médecine et Maladies Infectieuses | Characterized the impact of different in vitro culture conditions (medium, inoculum, incubation time) on bedaquiline MIC against *M. tuberculosis* H37Rv; essential methodology for extending susceptibility testing to MTBC members including *M. bovis* |
| [19075053](https://pubmed.ncbi.nlm.nih.gov/19075053/) | 2009 | In vitro / Basic Science | Antimicrobial Agents and Chemotherapy | Demonstrated >20,000-fold selectivity of bedaquiline (TMC207) for mycobacterial ATP synthase over human mitochondrial ATP synthase; also showed low sensitivity in bovine heart mitochondria, confirming selectivity for the mycobacterial target and establishing the mechanistic foundation for MTBC-wide coverage |
| [18480227](https://pubmed.ncbi.nlm.nih.gov/18480227/) | 2008 | In vitro / Methodological | Journal of Clinical Microbiology | Validated BSA-supplemented media to prevent bedaquiline drug carryover in ex vivo bacterial titrations from mouse organs and patient sputa; critical methodological control for in vivo and clinical susceptibility studies |

---

## Philippines Market Information

Bedaquiline is **not currently registered** in the Philippines. There are no product authorizations recorded in the local regulatory database.

For reference, bedaquiline (brand name **Sirturo®**) has received regulatory approval in several major jurisdictions:

| Jurisdiction | Approval Year | Approved Indication |
|-------------|--------------|---------------------|
| US FDA | 2012 (adults); extended to pediatric use | MDR-TB, as part of combination therapy |
| EMA | 2014 | MDR-TB, as part of combination therapy |
| WHO Essential Medicines | 2019 (added); 2022 (guidance updated) | All forms of RR/MDR-TB |

A regulatory application, special access scheme, or compassionate use program would be required before any clinical use in the Philippines.

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Blocking Data Gap (DG001):** Philippines-specific prescribing information has not yet been retrieved. This gap prevents formal safety evaluation and must be resolved before clinical feasibility assessment can proceed. The recommended remediation is to download and parse the originator package insert PDF from the relevant regulatory agency (e.g., FDA Philippines or the US Sirturo® label as a reference standard).

---

## Conclusion and Next Steps

### Rank 1 — Tuberculosis, Bovine

**Decision: Research Question**

**Rationale:**
The mechanistic link is scientifically plausible: bedaquiline's target (F₀F₁-ATP synthase c subunit) is conserved across all MTBC members including *M. bovis*. However, no clinical trials exist for this specific indication, all available evidence is in vitro and methodological (not direct *M. bovis* testing), and the primary disease context is veterinary/zoonotic rather than standard human therapeutics.

**To proceed, the following is needed:**
- Direct in vitro susceptibility testing of bedaquiline against *M. bovis* reference strains using standardized MIC methodology
- Assessment of the zoonotic TB clinical context to determine whether human treatment scenarios warrant further investigation
- Collaboration with veterinary infectious disease specialists and public health authorities on the zoonotic TB management framework

---

### Rank 2 — Inactive (Latent) Tuberculosis — **Highest Priority Actionable Finding**

**Decision: Proceed with Guardrails**

**Rationale:**
The BREACH-TB trial ([NCT06568484](https://clinicaltrials.gov/study/NCT06568484), seamless Phase 2/3, n=2,530) is directly testing a 4-week bedaquiline regimen versus standard regimens for TB preventive therapy in people living with HIV and high-risk close contacts of DS/RR-TB patients. Bedaquiline's unique activity against dormant mycobacteria, supported by a mouse model of TB preventive therapy (PMID 34939891) and multiple mechanistic reviews, provides strong biological rationale. This is the most actionable repurposing direction in this analysis.

**To proceed, the following is needed:**
- **Safety gap resolution (DG001 — Blocking):** Retrieve international prescribing information (US Sirturo® label) to document QTc prolongation monitoring protocols, hepatotoxicity management guidance, and CYP3A4 drug-drug interaction risk assessment
- **MOA documentation (DG002 — High):** Formally confirm bedaquiline's ATP synthase inhibition mechanism via DrugBank API query for regulatory dossier completeness
- **Regulatory pathway assessment:** Evaluate special access schemes or compassionate use mechanisms in the Philippines for bedaquiline in a preventive therapy context
- **Trial monitoring:** Track BREACH-TB (NCT06568484) primary completion, anticipated September 2027; results will provide definitive Phase 2/3 efficacy and safety data for latent TB preventive use
- **WHO guideline alignment:** Review 2022 WHO consolidated guidelines on TB treatment for current recommendations on bedaquiline in preventive therapy, and assess how updated guidance may support a Philippines regulatory submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

