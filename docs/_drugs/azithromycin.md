---
layout: default
title: Azithromycin
parent: 僅模型預測 (L5)
nav_order: 34
evidence_level: L5
indication_count: 10
---

# Azithromycin
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

# Azithromycin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Azithromycin is a broad-spectrum macrolide antibiotic widely used for bacterial respiratory, sexually transmitted, and atypical infections, with additional well-documented immunomodulatory properties.
The TxGNN model's top prediction is **Polyclonal Hyperviscosity Syndrome** (score: 99.81%), though this indication lacks direct mechanistic support and no clinical or preclinical evidence was identified.
This is a **multi-indication evaluation** covering 10 predicted indications; the most evidence-supported repurposing opportunities are **Monoclonal Gammopathy** (rank 7, preclinical mechanistic data) and **Congenital Hematological Disorder / Sickle Cell Disease** (rank 10, two formally registered but withdrawn Phase 1/2 clinical trials).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (macrolide antibiotic; no Philippines FDA registration on file) |
| Predicted New Indication (Top) | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 (top prediction, rank 1); L4 (ranks 4, 7, 9, 10) |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (top prediction) / Research Question (ranks 7 & 10) |

---

## All Predicted Indications — Multi-Indication Overview

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|-------------|----------------|----------|
| 1 | Polyclonal hyperviscosity syndrome | 99.81% | L5 | Hold |
| 2 | Hyperamylasemia | 99.81% | L5 | Hold ⚠️ Mechanistic contradiction |
| 3 | Congenital analbuminemia | 99.79% | L5 | Hold |
| 4 | Punctate epithelial keratoconjunctivitis | 99.78% | L4 | Research Question |
| 5 | Blood group incompatibility | 99.70% | L5 | Hold |
| 6 | Premalignant hematological system disease | 99.64% | L5 | Hold |
| 7 | Monoclonal gammopathy | 99.61% | L4 | Research Question ★ |
| 8 | Hematological disease with acquired peripheral neuropathy | 99.56% | L5 | Hold ⚠️ Safety concern |
| 9 | Septicemic plague | 99.52% | L4 | Research Question |
| 10 | Congenital hematological disorder | 99.40% | L4 | Research Question ★ |

> ★ Most clinically promising for further development. ⚠️ Active safety or mechanistic concerns.

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on well-established pharmacological knowledge, Azithromycin is a macrolide antibiotic that inhibits bacterial protein synthesis by binding the 50S ribosomal subunit. Critically for repurposing purposes, it also exerts **immunomodulatory effects** independent of its antimicrobial action: it suppresses pro-inflammatory cytokines (IL-8, TNF-α), inhibits neutrophil chemotaxis, and — as demonstrated in preclinical studies — blocks lysosomal autophagy flux in mammalian cells.

For the **top-ranked prediction (Polyclonal Hyperviscosity Syndrome)**, the high TxGNN score (0.998) most likely reflects indirect topological connections in the knowledge graph linking macrolide antibiotics → inflammatory pathways → immunoglobulin dysregulation. Polyclonal hyperviscosity is driven by excess polyclonal immunoglobulins arising from infection or chronic inflammation — conditions where Azithromycin has documented anti-inflammatory effects. However, there is no established mechanism by which Azithromycin directly reduces plasma viscosity or immunoglobulin load, and no clinical or preclinical evidence supports this use. This remains a graph-topology artefact rather than a biologically grounded prediction.

The **most mechanistically compelling prediction across the full multi-indication set is Monoclonal Gammopathy (rank 7)**. A direct in vitro and in vivo study (PMID 23546223) demonstrates that Azithromycin blocks autophagy flux, induces endoplasmic reticulum (ER) stress, and markedly sensitises multiple myeloma cells to bortezomib cytotoxicity — a biologically plausible mechanism given that plasma cells in the myeloma-MGUS spectrum are highly dependent on autophagy for protein homeostasis. For **Congenital Hematological Disorder (rank 10)**, specifically sickle cell disease (SCD), Azithromycin's anti-inflammatory properties formed the scientific basis for two formally registered clinical trials aimed at reducing acute chest syndrome (ACS) frequency and improving pulmonary function — both withdrawn before enrolment, likely for operational rather than safety reasons.

---

## Clinical Trial Evidence

No clinical trials were identified for Polyclonal Hyperviscosity Syndrome (rank 1).

The table below presents all trials identified across the full multi-indication analysis, ordered by clinical relevance:

| Trial Number | Indication (Rank) | Phase | Status | Enrollment | Key Findings |
|-------------|-------------------|-------|--------|------------|--------------|
| [NCT02630394](https://clinicaltrials.gov/study/NCT02630394) | Congenital haematological disorder (10) | Phase 1 | Withdrawn | 0 | Azithromycin prophylaxis to prevent Acute Chest Syndrome (ACS) in SCD patients — primary hypothesis: immunomodulatory/anti-inflammatory reduction of recurrent ACS. Withdrawn before enrolment; reason not reported in registry |
| [NCT02960503](https://clinicaltrials.gov/study/NCT02960503) | Congenital haematological disorder (10) | Phase 1/2 | Withdrawn | 0 | Macrolide therapy (including Azithromycin) to improve FEV1 in adult SCD patients; aimed to reduce pulmonary inflammation underlying obstructive lung disease and pulmonary hypertension in SCA. Withdrawn before enrolment |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | Congenital haematological disorder (10) | N/A | Recruiting | 5,000 | Paediatric pharmacokinetics, pharmacodynamics, and safety of understudied drugs administered per standard of care; Azithromycin is among the drugs studied. Provides background PK/safety data only — not a repurposing efficacy trial |
| [NCT04294641](https://clinicaltrials.gov/study/NCT04294641) | Congenital haematological disorder (10) | Phase 2 | Completed | 10 | Front-line ibrutinib (not Azithromycin) for newly diagnosed chronic GVHD; low direct relevance — likely retrieved due to database disease-classification overlap with haematological disorders |

---

## Literature Evidence

No literature was identified for Polyclonal Hyperviscosity Syndrome (rank 1).

The table below presents the most relevant publications identified across all predicted indications, prioritised by evidence tier and mechanistic relevance:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [23546223](https://pubmed.ncbi.nlm.nih.gov/23546223/) | 2013 | Preclinical (In vitro + In vivo) | International Journal of Oncology | **★ Most relevant.** Azithromycin blocks autophagy flux (↑LC3B-II, ↑p62) and sensitises multiple myeloma cell lines to bortezomib via ER stress-mediated CHOP induction — direct mechanistic basis for monoclonal gammopathy repurposing (rank 7) |
| [26408070](https://pubmed.ncbi.nlm.nih.gov/26408070/) | 2015 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Antibiotic prophylaxis for preventing lower respiratory tract infections in high-risk children (≤12 years); provides systematic background for antibiotic use in congenital haematological disorder populations (rank 10) |
| [8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/) | 1995 | In vitro susceptibility study | Antimicrobial Agents and Chemotherapy | MIC data for 14 antibiotics against 78 *Y. pestis* strains; Azithromycin showed inhibitory activity — relevant to septicemic plague (rank 9). Note: ceftriaxone and ciprofloxacin were more active |
| [12698575](https://pubmed.ncbi.nlm.nih.gov/12698575/) | 2002 | Animal Study (In vivo) | Antibiotics and Chemotherapy | Azithromycin demonstrated highest efficacy among tested agents in experimental brucellosis model, normalising bactericidal activity in peripheral blood — supports gram-negative intracellular pathogen activity (rank 9 context) |
| [32826651](https://pubmed.ncbi.nlm.nih.gov/32826651/) | 2021 | Case Report | Cornea | Microsporidia (*Encephalitozoon hellem*) keratoconjunctivitis in immunocompetent adult, diagnosed by metagenomic deep sequencing; Azithromycin used as anti-microsporidial adjunct — indirect support for punctate epithelial keratoconjunctivitis (rank 4) |
| [22825522](https://pubmed.ncbi.nlm.nih.gov/22825522/) | 2012 | Case Report | Tumori | Multiple myeloma patient with bisphosphonate-related ONJ treated with local ozone gas plus Azithromycin 500 mg/day — incidental exposure data; low direct relevance to monoclonal gammopathy as primary treatment (rank 7) |
| [33389938](https://pubmed.ncbi.nlm.nih.gov/33389938/) | 2020 | Case Report | Turkish Journal of Ophthalmology | *Bartonella henselae* neuroretinitis in a POEMS syndrome (monoclonal gammopathy) patient — Azithromycin indicated for *Bartonella* treatment; documents co-infection in monoclonal gammopathy context but does not address underlying disease (rank 7) |

---

## Philippines Market Information

Azithromycin has **no registered pharmaceutical products** with the Philippines FDA. There are no authorization records, approved indications, or dosage form data available for this jurisdiction.

---

## Safety Considerations

Safety data from the Evidence Pack is not available (Philippines FDA package insert not retrieved; DDI query returned no results).

Based on published pharmacological knowledge relevant to the predicted indications, the following safety signals warrant attention during any repurposing evaluation:

- **QT Interval Prolongation:** Azithromycin is a known risk factor for cardiac arrhythmia via QT prolongation, particularly in patients with electrolyte imbalances, pre-existing cardiac conditions, or concurrent QT-prolonging medications. This is a critical contraindication consideration for rank 8 (hematological disease with acquired peripheral neuropathy), where affected patients may be receiving neurotoxic or cardiotoxic combination regimens.
- **Drug-Induced Hyperamylasaemia / Pancreatitis Risk:** Azithromycin has documented associations with elevated serum amylase and drug-induced pancreatitis. This makes the rank 2 prediction (Hyperamylasaemia as a treatment target) mechanistically contradictory — Azithromycin is more likely to worsen than resolve this condition.
- **Peripheral Neuropathy Risk:** Case reports exist for macrolide-associated peripheral neuropathy. In patients with rank 8 disease (acquired peripheral neuropathy in haematological disease), use requires particular caution.

> For complete warnings, contraindications, and drug interactions, retrieve the Philippines FDA-approved package insert and DrugBank full safety profile.

---

## Conclusion and Next Steps

**Decision: Hold (Rank 1 — Polyclonal Hyperviscosity Syndrome) / Research Question (Ranks 7 & 10)**

**Rationale:**
The top TxGNN-ranked prediction (Polyclonal Hyperviscosity Syndrome) lacks mechanistic plausibility and any supporting evidence, warranting a Hold. However, Azithromycin's autophagy-inhibition mechanism provides a preclinically validated rationale for **Monoclonal Gammopathy** (combination sensitisation with bortezomib), and its anti-inflammatory properties have been tested — though not completed — in **Sickle Cell Disease** (congenital hematological disorder), making these two indications the priority targets for further development.

**To proceed with high-priority indications, the following is needed:**

- **Data Gaps to Resolve First:**
  - Retrieve Philippines FDA package insert for complete warnings and contraindications (currently Blocking Data Gap — prevents S1 safety evaluation)
  - Query DrugBank API for full MOA documentation (currently High-severity Data Gap — required for mechanistic analysis)
  - Conduct a formal DDI review (current DDI query returned zero results, which is likely a retrieval failure given Azithromycin's known CYP3A4 interactions and QT-prolonging potential)

- **For Monoclonal Gammopathy (Rank 7 — Research Question ★):**
  - Design a Phase 1/2 basket trial evaluating Azithromycin + bortezomib in relapsed/refractory multiple myeloma
  - Specify ER stress biomarkers (CHOP, GRP78, p-eIF2α) as secondary endpoints to confirm the autophagy-inhibition mechanism in vivo
  - Conduct additional preclinical work in primary myeloma cells and patient-derived xenograft models

- **For Congenital Hematological Disorder / SCD (Rank 10 — Research Question ★):**
  - Contact PIs of NCT02630394 and NCT02960503 to determine specific reasons for trial withdrawal before any redesign
  - If withdrawal was operational (funding/recruitment) rather than safety-related, a redesigned feasibility study with refined endpoints (ACS frequency at 12 months, IL-8/TNF-α as biomarkers) is warranted
  - Review the Cochrane systematic review (PMID 26408070) for relevant antibiotic prophylaxis evidence applicable to the SCD population

- **Indications to Exclude from Further Evaluation:**
  - Rank 2 (Hyperamylasaemia): mechanistic contradiction — exclude
  - Rank 8 (Haematological disease with acquired peripheral neuropathy): active safety concern (QT prolongation + potential neuropathy risk in an already neuropathic population) — exclude pending formal safety review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

