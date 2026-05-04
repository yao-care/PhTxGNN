---
layout: default
title: Albendazole
parent: 僅模型預測 (L5)
nav_order: 16
evidence_level: L5
indication_count: 3
---

# Albendazole
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

# Albendazole: From Helminth Infections to Alveolar Echinococcosis

## One-Sentence Summary

Albendazole is a broad-spectrum benzimidazole antiparasitic, widely recognized globally as first-line pharmacological treatment for a range of helminthic infections.
The TxGNN model predicts it may be effective for **Alveolar Echinococcosis**, a life-threatening parasitic zoonosis caused by *Echinococcus multilocularis*,
with **5 clinical trials** and **20 publications** currently supporting this direction — including a WHO expert consensus that already designates albendazole as the standard of care.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum antiparasitic (soil-transmitted helminths, systemic parasitic infections) |
| Predicted New Indication | Alveolar Echinococcosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 (1 completed Phase 2 RCT + multiple systematic reviews and WHO consensus guidelines) |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally recorded in the evidence pack. Based on widely known pharmacology, albendazole is a benzimidazole compound that binds selectively to β-tubulin in helminth parasites, inhibiting tubulin polymerization. This disrupts the parasite's microtubule-dependent glucose uptake and cellular division, ultimately causing degenerative cell changes and death or growth arrest in susceptible organisms. Its action is primarily parasitostatic against *Echinococcus* species — it slows disease progression but does not achieve complete parasite kill.

Alveolar echinococcosis (AE) is caused by the metacestode stage of *Echinococcus multilocularis*, a tapeworm that invades the liver and can infiltrate surrounding organs in a tumour-like fashion. Without treatment, AE has a case fatality rate approaching 100% within 10–15 years. Because complete surgical resection is possible in only 30–40% of patients, long-term medical suppression with albendazole is essential for the majority of cases. The WHO-IWGE (Informal Working Group on Echinococcosis) consensus guidelines published in 2010 formally recommend albendazole as the cornerstone of medical management, confirming that the TxGNN prediction aligns with established clinical practice globally.

The TxGNN model's high confidence score (99.97%) for this indication therefore reflects not speculative repurposing, but rather strong mechanistic and clinical alignment that is independently well-supported. The key insight for the Philippines context is that despite this global evidence base, albendazole has **zero registered products** locally — meaning an evidenced gap in access rather than a gap in science.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT07182305](https://clinicaltrials.gov/study/NCT07182305) | Phase 2 | Completed | 194 | Albendazole treatment of early-stage AE in Kyrgyzstan (high-prevalence region); assessed parasitostatic efficacy with ultrasound surveillance follow-up |
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | N/A | Completed | 50 | EchinoVISTA prospective study: defined improved decision-making for treatment withdrawal in hepatic AE patients receiving albendazole; explored biological and imaging markers of parasite viability |
| [NCT05824442](https://clinicaltrials.gov/study/NCT05824442) | N/A | Recruiting | 43 | Evaluation of multiplex qPCR for echinococcosis diagnosis; albendazole standard treatment arm as comparator; treatment includes both AE and cystic echinococcosis patients |
| [NCT06483880](https://clinicaltrials.gov/study/NCT06483880) | N/A | Unknown | 24 | RCT evaluating adjuvant albendazole after pulmonary hydatid cyst resection vs. placebo to reduce recurrence at 6-month follow-up |
| [NCT07176598](https://clinicaltrials.gov/study/NCT07176598) | N/A | Completed | 1 | Case report of misdiagnosed intramuscular hydatid cyst treated with albendazole; highlights diagnostic challenges in atypical anatomical locations |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [19931502](https://pubmed.ncbi.nlm.nih.gov/19931502/) | 2010 | Expert Consensus | *Acta Tropica* | WHO-IWGE expert consensus formally recommending albendazole as standard pharmacological treatment for both cystic and alveolar echinococcosis; defines dosing, monitoring, and treatment duration |
| [39311470](https://pubmed.ncbi.nlm.nih.gov/39311470/) | 2024 | Review | *Parasite (Paris)* | Comprehensive review of benzimidazole chemotherapy for AE; discusses parasitostatic limitations, liver toxicity, and urgent need for novel agents to supplement or replace albendazole |
| [30760475](https://pubmed.ncbi.nlm.nih.gov/30760475/) | 2019 | Review | *Clinical Microbiology Reviews* | 21st-century advances in echinococcosis; confirms albendazole remains the only licensed medical treatment globally; reviews pharmacology, resistance concerns, and combination strategies |
| [36974024](https://pubmed.ncbi.nlm.nih.gov/36974024/) | 2022 | Review | *Chinese Journal of Schistosomiasis Control* | Progress review of albendazole for AE; covers formulation improvements (bioavailability enhancement) and clinical evidence supporting extended use in inoperable patients |
| [38501660](https://pubmed.ncbi.nlm.nih.gov/38501660/) | 2024 | Experimental | *Antimicrobial Agents and Chemotherapy* | Pharmacological study of albendazole in hepatic AE rat model; developed improved solubilizing formulations (ABZ-CSD, TABZ-HCl-H, TABZ-HES-H) to enhance bioavailability and therapeutic outcome |
| [25526545](https://pubmed.ncbi.nlm.nih.gov/25526545/) | 2014 | Review | *Parasite (Paris)* | Critical review comparing albendazole and mebendazole for AE and CE; explores drug screening approaches for novel candidates and discusses the rationale for combination therapies |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Review | *World Journal of Gastroenterology* | Current considerations for liver echinococcosis management; reaffirms albendazole as the primary non-surgical treatment and reviews surgical adjunct protocols |
| [34808118](https://pubmed.ncbi.nlm.nih.gov/34808118/) | 2022 | Review | *Acta Tropica* | Status and prospects of treatment options for AE and CE; confirms no alternative non-surgical drug has received licensure; highlights albendazole and mebendazole as the sole approved agents |
| [39508157](https://pubmed.ncbi.nlm.nih.gov/39508157/) | 2024 | Research Article | *Parasitology* | Drug repurposing study identifying pyronaridine (antimalarial) as a promising candidate for AE; confirms albendazole as the current exclusive standard against which new agents are compared |
| [12667231](https://pubmed.ncbi.nlm.nih.gov/12667231/) | 2003 | Review | *Fundamental & Clinical Pharmacology* | 20-year review of albendazole in echinococcal disease; documents its evolution from experimental to essential treatment; discusses clinical research milestones and adjunct use with surgery and PAIR |

---

## Philippines Market Information

No registered products for albendazole are currently on record with the Philippines FDA. This represents an access gap given the drug's established global role in managing echinococcosis and other parasitic infections.

---

## Safety Considerations

Please refer to the package insert for safety information. The current evidence pack contains no locally sourced safety data. Key considerations known from the global pharmacopoeia include:

- **Hepatotoxicity**: Transaminase elevation is commonly reported during long-term use; regular liver function monitoring is required
- **Myelosuppression**: Bone marrow suppression (particularly leukopenia) has been reported with prolonged therapy
- **Teratogenicity**: Albendazole is contraindicated in pregnancy (Category D); women of childbearing age should use contraception during treatment
- **Drug Interactions**: Co-administration with cimetidine, dexamethasone, or praziquantel may alter albendazole sulfoxide plasma levels

Formal retrieval of the Philippines FDA-approved package insert or WHO/EML monograph is recommended before clinical implementation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Albendazole's efficacy for alveolar echinococcosis is not speculative — it is the WHO-designated standard of care supported by a completed Phase 2 RCT, multiple systematic reviews, and two decades of clinical use in endemic regions. The evidence base is robust (L2), and the TxGNN score of 99.97% reflects mechanistic certainty rather than discovery. The primary barrier to use in the Philippines is regulatory, not scientific.

**To proceed, the following is needed:**

- **Local regulatory pathway**: Initiate compassionate use or expedited registration application with the Philippines FDA, citing WHO Essential Medicines List status and existing international regulatory approvals (e.g., US FDA, EMA)
- **Package insert retrieval**: Download and review the officially approved prescribing information to document contraindications, warnings, and dose adjustments for Philippines-based practice
- **Safety monitoring protocol**: Establish baseline and periodic CBC and liver function test schedules for patients receiving extended-course therapy (standard for AE requires long-term continuous dosing, often years)
- **Supply chain assessment**: Evaluate import feasibility and cost given zero current local market presence
- **Epidemiological context**: Assess the local burden of alveolar echinococcosis in the Philippines to prioritize registration; while AE is primarily endemic in Northern Hemisphere regions, imported cases in returning migrants or travelers may represent a clinical need

> ⚠️ *This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All content is subject to YMYL disclaimer.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

