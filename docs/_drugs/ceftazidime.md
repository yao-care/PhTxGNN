---
layout: default
title: Ceftazidime
parent: 僅模型預測 (L5)
nav_order: 64
evidence_level: L5
indication_count: 10
---

# Ceftazidime
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

# Ceftazidime: From Gram-Negative Bacterial Infections to Urinary Tract Infection

## One-Sentence Summary

Ceftazidime is a third-generation cephalosporin antibiotic with proven bactericidal activity against gram-negative pathogens, particularly multidrug-resistant *Pseudomonas aeruginosa* and ESBL-producing Enterobacterales.
Among 10 TxGNN-predicted indications, **Urinary Tract Infection (UTI)** emerges as the most clinically actionable, carrying a prediction score of **99.41%** and backed by **multiple completed Phase 2 RCTs** and **20 publications** — the strongest evidence in this Evidence Pack.
However, Ceftazidime is currently **not registered in the Philippines**, making regulatory approval the primary barrier to local adoption rather than any scientific concern.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gram-negative bacterial infections (IV antibiotic; not registered in Philippines) |
| Predicted New Indication | Urinary Tract Infection (UTI) — TxGNN Rank #4 |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L2 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Ceftazidime exerts its antibacterial effect by binding to penicillin-binding proteins (PBPs), inhibiting bacterial cell wall synthesis and triggering cell lysis. Its defining clinical advantage is exceptional activity against aerobic gram-negative bacilli — including *Escherichia coli*, *Klebsiella pneumoniae*, *Pseudomonas aeruginosa*, *Enterobacter* spp., and *Proteus* spp. — organisms that collectively cause the vast majority of complicated urinary tract infections (cUTIs). Critically, Ceftazidime is predominantly excreted unchanged through the kidneys, achieving urine drug concentrations that consistently exceed minimum inhibitory concentrations (MICs) for susceptible uropathogens. This pharmacokinetic profile makes it mechanistically ideal for treating cUTI.

The UTI prediction is not a theoretical stretch. Ceftazidime has been used globally for cUTIs for decades, and its more recent combination with avibactam (CAZ-AVI, marketed as Avycaz® and Zavicefta®) has further extended coverage to ESBL- and KPC-producing organisms — pathogens that are increasingly prevalent in Asia and represent a major treatment challenge in hospital settings. Multiple Phase 2 RCTs have directly evaluated Ceftazidime/CAZ-AVI specifically in cUTI settings, including pyelonephritis and carbapenem-resistant cases. The drug is approved for this indication by the US FDA, EMA, and regulatory authorities in South Korea, Japan, and China.

A note on TxGNN ranking: UTI appears at rank #4 rather than #1 because the knowledge graph model assigned high scores to mechanistically implausible candidates (ranks #1–3 are false positives: polyclonal hyperviscosity syndrome, congenital analbuminemia, and hyperamylasemia). UTI is the **only prediction in this pack** that meets criteria for clinical advancement — combining strong mechanistic rationale, Phase 2 RCT evidence, and established global regulatory approval. The absence of Philippines registration is a **regulatory gap, not a scientific one**.

---

## Predicted Indications Overview

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Assessment |
|------|---------|-------------|----------------|----------------|------------|
| 1 | Polyclonal hyperviscosity syndrome | 99.51% | L5 | Hold | False positive — no mechanistic or clinical link to β-lactam antibiotics |
| 2 | Hyperamylasemia | 99.51% | L4 | Hold | Indirect class effect only (antibiotic prophylaxis post-ERCP); not a primary indication |
| 3 | Congenital analbuminemia | 99.48% | L5 | Hold | False positive — genetic metabolic disease with no antibiotic relevance |
| **4** | **Urinary tract infection** | **99.41%** | **L2** | **Proceed with Guardrails** | **Strong mechanistic support; multiple completed Phase 2 RCTs; globally approved** |
| 5 | Epiglottitis | 99.39% | L4 | Hold | Not first-line; one literature report documents cephalosporin resistance |
| 6 | Ureaplasma urethritis | 99.27% | L5 | Hold | Intrinsic β-lactam resistance — mechanistically excluded |
| 7 | Gonococcal urethritis | 99.27% | L4 | Hold | Not first-line; WHO/CDC guidelines mandate ceftriaxone |
| 8 | Blood group incompatibility | 99.26% | L5 | Hold | False positive — immunohematologic disorder; no antibiotic relevance |
| 9 | Infectious otitis media | 99.19% | L3 | Research Question | Moderate evidence for Pseudomonas-driven CSOM; no registered clinical trials |
| 10 | Peptostreptococcus infection | 99.17% | L4 | Hold | Weak anaerobic coverage; only supporting data is a 1981 in vitro study |

---

## Clinical Trial Evidence

*Top 10 trials for UTI indication, ordered by relevance grade (A → B → C).*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04882085](https://clinicaltrials.gov/study/NCT04882085) | Phase 4 | Completed | 60 | Open-label RCT: CAZ-AVI vs best available therapy for carbapenem-resistant gram-negative infections (including cUTI) in Chinese adults; efficacy and safety primary endpoints |
| [NCT00690378](https://clinicaltrials.gov/study/NCT00690378) | Phase 2 | Completed | 137 | Multicenter prospective RCT: NXL104/Ceftazidime vs comparator for complicated UTI in hospitalized adults; primary efficacy study for this combination |
| [NCT00921024](https://clinicaltrials.gov/study/NCT00921024) | Phase 2 | Completed | 129 | Double-blind RCT: IV CXA-101 vs Ceftazidime comparator for cUTI including pyelonephritis; safety and efficacy co-primary endpoints |
| [NCT02497781](https://clinicaltrials.gov/study/NCT02497781) | Phase 2 | Completed | 97 | Single-blind RCT: CAZ-AVI vs cefepime in pediatric patients (3 months–18 years) with cUTI; safety, tolerability, PK, and clinical efficacy assessed |
| [NCT04628572](https://clinicaltrials.gov/study/NCT04628572) | N/A | Completed | 189 | Retrospective real-world study (India): CAZ-AVI treatment patterns, effectiveness, and safety for gram-negative infections including UTI; reflects routine clinical practice |
| [NCT05258851](https://clinicaltrials.gov/study/NCT05258851) | Phase 3 | Terminated | 29 | Non-inferiority RCT: CAZ-AVI vs colistin for CRE infections in critically ill patients; terminated early due to enrollment challenges — provides limited but relevant Phase 3 data |
| [NCT05733104](https://clinicaltrials.gov/study/NCT05733104) | N/A | Recruiting | 600 | Post-marketing surveillance (South Korea): Safety and effectiveness of Zavicefta® (CAZ-AVI) for cUTI, complicated intra-abdominal infection, and nosocomial pneumonia |
| [NCT01601093](https://clinicaltrials.gov/study/NCT01601093) | Phase 2 | Suspended | 288 | Ceftazidime + Sulbactam (2:1) for respiratory and urinary tract acute bacterial infections; currently suspended — provides context on Ceftazidime-based combination strategies |
| [NCT03147807](https://clinicaltrials.gov/study/NCT03147807) | N/A | Completed | 75 | ICU de-escalation study: BetaLACTA test-guided switch from carbapenems to Ceftazidime/other β-lactams in UTI, pneumonia, and bloodstream infections |
| [NCT01430910](https://clinicaltrials.gov/study/NCT01430910) | Phase 1 | Completed | 43 | PK/DDI study of CAZ-AVI: pharmacokinetics of avibactam and ceftazidime administered separately vs combined IV; provides dose-optimization foundation for UTI |

---

## Literature Evidence

*Top 10 publications for UTI indication, prioritized by study quality (Tier 1 → 2).*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39817442](https://pubmed.ncbi.nlm.nih.gov/39817442/) | 2025 | Systematic Review / Meta-analysis | J Comp Effectiveness Res | Network meta-analysis of cUTI treatment options including pyelonephritis; CAZ-AVI demonstrates superior outcomes for ESBL/carbapenem-resistant uropathogens versus standard therapy |
| [38688353](https://pubmed.ncbi.nlm.nih.gov/38688353/) | 2024 | Expert Guideline / Practice Review | Int J Antimicrob Agents | Italian-French consensus guideline for MDR gram-negative bacilli; CAZ-AVI explicitly recommended for ESBL- and KPC-producing UTI when other agents fail |
| [33618353](https://pubmed.ncbi.nlm.nih.gov/33618353/) | 2021 | Retrospective Multicenter Cohort | Clin Infect Dis | 9-center Italian cohort study of CAZ-AVI for KPC-producing *Klebsiella* infections (including UTI); reports clinical cure rates, microbiological eradication, and 30-day mortality |
| [32094128](https://pubmed.ncbi.nlm.nih.gov/32094128/) | 2020 | Retrospective Comparative Cohort | Antimicrob Agents Chemother | Head-to-head comparison of CAZ-AVI vs meropenem-vaborbactam for CRE infections; comparable clinical outcomes with both agents in non-UTI settings — provides systemic comparative context |
| [26289307](https://pubmed.ncbi.nlm.nih.gov/26289307/) | 2015 | Narrative Review | Pharmacotherapy | Comprehensive review of CAZ-AVI at approval: mechanism of avibactam's β-lactamase inhibition, antimicrobial spectrum, PK/PD, and clinical evidence for approved indications including cUTI |
| [3906585](https://pubmed.ncbi.nlm.nih.gov/3906585/) | 1985 | Pharmacology Review | Pharmacotherapy | Foundational pharmacology of Ceftazidime: activity against *Pseudomonas*, renal PK profile, and documented therapeutic indications including UTI — establishes the scientific basis |
| [35787918](https://pubmed.ncbi.nlm.nih.gov/35787918/) | 2022 | Observational / Registry | Int J Antimicrob Agents | International registry data on novel antibiotics (CAZ-AVI, meropenem-vaborbactam, imipenem-relebactam) for MDR gram-negative infections; clinical outcomes stratified by infection type |
| [39934901](https://pubmed.ncbi.nlm.nih.gov/39934901/) | 2025 | Systematic Review / Meta-analysis | Antimicrob Resist Infect Control | Global trends in CAZ-AVI resistance in gram-negative bacteria; critical for patient selection criteria and resistance stewardship planning in new markets |
| [30219824](https://pubmed.ncbi.nlm.nih.gov/30219824/) | 2019 | Clinical Guidance Review | Clin Infect Dis | Renal dose adjustment guidance for Ceftazidime/CAZ-AVI: risk of reduced clinical response in acute kidney injury patients — directly actionable for cUTI dosing protocols |
| [40530972](https://pubmed.ncbi.nlm.nih.gov/40530972/) | 2025 | PK/PD Modeling | Antimicrob Agents Chemother | Population PK/PD model for aztreonam-avibactam dose optimization for cUTI/cIAI/HAP; methodologically relevant for the avibactam-containing class including CAZ-AVI |

---

## Philippines Market Information

Ceftazidime is currently **not registered in the Philippines**. No product authorization records are available.

| Item | Details |
|------|---------|
| Philippines Market Status | Not Marketed |
| Total Registered Products | 0 |
| Available Dosage Forms | None (no local product authorization exists) |

> **Global registration context**: Ceftazidime monotherapy and CAZ-AVI (Avycaz® — US/AstraZeneca; Zavicefta® — EU/AstraZeneca) are approved by the US FDA, European EMA, and regulatory agencies in South Korea (MFDS), Japan (PMDA), and China (NMPA) for complicated urinary tract infections including pyelonephritis. A separate New Drug Application to the Philippine Food and Drug Administration (FDA Philippines) would be required for local market entry.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note**: Formal safety data (package insert warnings, contraindications, drug-drug interactions) was not available in the current Evidence Pack for the Philippines context. Based on Ceftazidime's established pharmacological class profile, the following areas should be reviewed prior to any clinical application:
> - **Hypersensitivity**: Cross-reactivity with other β-lactam antibiotics (penicillins, cephalosporins, carbapenems) — obtain full allergy history before use
> - **Neurological toxicity**: Encephalopathy, myoclonus, and seizures reported — risk substantially elevated in renal impairment without appropriate dose reduction
> - **Drug-drug interactions**: Nephrotoxicity risk increases with concurrent aminoglycosides, vancomycin, or loop diuretics — monitor renal function
> - **Clostridioides difficile**: As with all broad-spectrum antibiotics, risk of C. difficile-associated diarrhea (CDAD) exists — prescribers should apply antibiotic stewardship principles

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ceftazidime (especially as CAZ-AVI) has robust Phase 2 RCT-level evidence for complicated UTI caused by gram-negative organisms including ESBL- and carbapenem-resistant strains, global regulatory approval in multiple major markets, and a well-understood pharmacokinetic profile that makes it mechanistically ideal for urinary tract indications. The sole critical barrier in the Philippines is the absence of local regulatory registration — the clinical and scientific justification is fully established.

**To proceed, the following is needed:**

- **Regulatory pathway**: Initiate a New Drug Application (NDA) to the Philippine FDA for Ceftazidime and/or Ceftazidime-Avibactam (Avycaz®/Zavicefta®), leveraging existing US FDA and EMA approval dossiers for accelerated review
- **Safety dossier**: Retrieve and review the full package insert (TFDA or EMA SmPC) to document complete warnings, contraindications, and drug-drug interactions for the Philippines prescribing context
- **Mechanism data supplement**: Query DrugBank API (DB00438) to fill the MOA data gap and complete the mechanistic rationale documentation
- **Local resistance surveillance**: Obtain Philippines-specific antibiogram data for UTI pathogens (*E. coli*, *Klebsiella*, *Pseudomonas*) from PhilHealth or DOH to assess whether ESBL/carbapenem-resistant rates justify CAZ-AVI over simpler β-lactam options
- **Health economics assessment**: Compare CAZ-AVI acquisition cost against currently available alternatives (meropenem, imipenem-cilastatin, piperacillin-tazobactam) in the Philippine hospital formulary context
- **Phase 3 evidence gap**: Note that no completed Phase 3 RCT specifically for cUTI is currently available (NCT05258851 was terminated at N=29); this gap should be explicitly addressed and acknowledged in any regulatory submission or formulary application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

