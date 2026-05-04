---
layout: default
title: Dapsone
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 1
---

# Dapsone
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

# Dapsone: From Leprosy to Pneumocystosis

## One-Sentence Summary

Dapsone is a diaminodiphenyl sulfone antimicrobial agent, historically used as the cornerstone treatment for leprosy and inflammatory dermatological conditions such as dermatitis herpetiformis.
The TxGNN model predicts it may be effective for **Pneumocystosis** (Pneumocystis jirovecii pneumonia, PJP),
with **14 clinical trials** and **19 publications** currently supporting this direction — and notably, this prediction recapitulates an already internationally-validated secondary indication, confirming strong model accuracy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Leprosy; dermatitis herpetiformis (established medical use; no Philippines registration on file) |
| Predicted New Indication | Pneumocystosis (Pneumocystis jirovecii pneumonia) |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L1 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank was not available for this report. Based on published pharmacological literature within this evidence pack, however, Dapsone — a diaminodiphenyl sulfone (DDS) compound — acts by competitively inhibiting **dihydropteroate synthase (DHPS)**, the enzyme that catalyzes folate biosynthesis. This is the same mechanism underpinning its activity against *Mycobacterium leprae* (leprosy). Because *Pneumocystis jirovecii*, the causative fungal pathogen of pneumocystosis, cannot scavenge exogenous folate and relies entirely on de novo synthesis, it is directly and highly sensitive to DHPS inhibition. When Dapsone is co-administered with trimethoprim (a DHFR inhibitor), the combination achieves dual-point blockade of the folate pathway, producing a well-characterised synergistic anti-*Pneumocystis* effect.

The mechanistic bridge from leprosy to pneumocystosis is therefore straightforward: both pathogens share obligate dependence on folate biosynthesis, making Dapsone's core mechanism directly transferable across these biologically distinct infectious disease states. The TxGNN knowledge-graph score of **0.9973** reflects a strong edge chain — Dapsone → antimicrobial/antiprotozoal activity → folate metabolism inhibition → *P. jirovecii* — fully consistent with known pharmacology.

Crucially, this is not a speculative repurposing. Dapsone is already included as a **first-line alternative prophylactic agent** in the ECIL-5 evidence-based guidelines for PCP prevention in patients with haematological malignancies and HSCT recipients (Grade A-II recommendation), and is endorsed by the IDSA for HIV-associated PCP prophylaxis when TMP-SMX is not tolerated. Multiple large Phase 3 RCTs conducted through the AIDS Clinical Trials Group (ACTG) in the 1990s established its efficacy for both treatment and primary/secondary prophylaxis. TxGNN has accurately reproduced a validated clinical reality — which is the strongest possible validation of the model's predictive value.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000802](https://clinicaltrials.gov/study/NCT00000802) | Phase 3 | Completed | 700 | Head-to-head RCT comparing daily Dapsone vs Atovaquone for PCP prophylaxis in HIV patients (CD4 ≤200/mm³) intolerant to TMP/SMX; large-scale, directly relevant efficacy trial |
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Phase 3 | Completed | 290 | Dapsone/Trimethoprim vs Clindamycin/Primaquine vs TMP-SMX for treatment of mild-to-moderate PCP in AIDS; established Dapsone/TMP as effective oral treatment alternative |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Phase 3 | Completed | 600 | Compared three anti-PCP prophylaxis regimens (including Dapsone) plus AZT for primary prevention in advanced HIV; also assessed protection against toxoplasmosis |
| [NCT00001028](https://clinicaltrials.gov/study/NCT00001028) | Phase 3 | Completed | 400 | Dapsone (three times weekly) vs aerosolized pentamidine for PCP prophylaxis in TMP/SMX-intolerant HIV patients; confirmed Dapsone dosing schedule and comparative efficacy |
| [NCT00002283](https://clinicaltrials.gov/study/NCT00002283) | N/A | Completed | N/A | Randomized prospective study comparing Dapsone + trimethoprim vs TMP-SMX for first-episode PCP in AIDS patients; evaluated outpatient treatment suitability and adverse event rates |
| [NCT02550080](https://clinicaltrials.gov/study/NCT02550080) | Phase 4 | Unknown | 3,130 | Prospective HLA-B\*1301 genetic pre-screening study to reduce Dapsone Hypersensitivity Syndrome (DHS) incidence; large-scale real-world safety study spanning multiple Dapsone indications including PJP |
| [NCT00002120](https://clinicaltrials.gov/study/NCT00002120) | Phase 1 | Completed | 20 | Explored Trimetrexate + Dapsone + leucovorin vs TMP-SMX for moderately severe PCP in AIDS; characterised pharmacokinetics and established early safety profile of combination |
| [NCT00000739](https://clinicaltrials.gov/study/NCT00000739) | Phase 1 | Completed | 96 | Daily vs weekly oral Dapsone for PCP prophylaxis in HIV-infected infants and children; generated paediatric pharmacokinetic data and dosing guidance |
| [NCT00141037](https://clinicaltrials.gov/study/NCT00141037) | Phase 1/2 | Completed | 130 | Steroid-free immunosuppression in paediatric renal transplant; Dapsone used as routine PCP prophylaxis component, providing real-world safety context in non-HIV immunocompromised children |
| [NCT04328688](https://clinicaltrials.gov/study/NCT04328688) | N/A | Completed | 30 | Clindamycin–TMP/SMX for PCP after solid organ transplantation; Dapsone referenced as established second-line alternative, supporting its role across immunocompromised populations beyond HIV |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38583518](https://pubmed.ncbi.nlm.nih.gov/38583518/) | 2024 | Systematic Review / Network Meta-analysis | Clinical Microbiology and Infection | Network meta-analysis of RCTs comparing all PCP prophylaxis regimens (TMP-SMX, Dapsone-based, pentamidine, atovaquone) in people living with HIV; provides the most current quantitative comparative efficacy and safety estimates |
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Systematic Review / Network Meta-analysis | Clinical Microbiology and Infection | Network meta-analysis of RCTs evaluating PCP treatment regimens in PLHIV; synthesises contemporary evidence including Dapsone-containing combinations |
| [27550992](https://pubmed.ncbi.nlm.nih.gov/27550992/) | 2016 | Clinical Practice Guideline | Journal of Antimicrobial Chemotherapy | ECIL-5 evidence-based recommendations for PCP prophylaxis in haematological malignancies and HSCT; Dapsone recommended as first-line alternative to TMP-SMX (Grade A-II) |
| [9675476](https://pubmed.ncbi.nlm.nih.gov/9675476/) | 1998 | Review | Clinical Infectious Diseases | Authoritative review of Dapsone for PCP prevention and treatment; covers DHPS inhibition mechanism, oral bioavailability (70–80%), PK/PD profile in alveolar fluid, and synergistic activity with trimethoprim |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Narrative Review | Expert Opinion on Pharmacotherapy | Updated comprehensive review of PJP prevention and treatment across all immunocompromised host categories; practical drug selection guidance including Dapsone regimens |
| [11155588](https://pubmed.ncbi.nlm.nih.gov/11155588/) | 2001 | Pharmacological Review | Dermatologic Clinics | Dual overview of Dapsone and sulfapyridine mechanisms; confirms Dapsone as the most important anti-leprosy drug and key PCP prophylaxis agent in HIV disease |
| [8605054](https://pubmed.ncbi.nlm.nih.gov/8605054/) | 1995 | Comparative Clinical Study | AIDS (London) | Three-arm study comparing aerosolized pentamidine, cotrimoxazole, and Dapsone-pyrimethamine for primary PCP prophylaxis; assessed efficacy, toxoplasmosis prevention, and survival |
| [9606476](https://pubmed.ncbi.nlm.nih.gov/9606476/) | 1998 | Safety Case Series | Annals of Pharmacotherapy | Methemoglobinemia in a patient receiving Dapsone for PCP prophylaxis; documents this clinically important adverse effect and the need for haemoglobin monitoring |
| [32714715](https://pubmed.ncbi.nlm.nih.gov/32714715/) | 2020 | Case Report | Cureus | Dapsone-induced hypoxia via methemoglobinemia; reinforces the necessity of SpO₂ monitoring and clinical awareness of this rare but serious complication during Dapsone therapy |
| [18971152](https://pubmed.ncbi.nlm.nih.gov/18971152/) | 2008 | Narrative Review | Journal of the Formosan Medical Association | Taiwan-focused review of PJP pathophysiology, reclassification of the organism as a fungus, diagnosis, and treatment; provides Asia-Pacific regional clinical context |

---

## Philippines Market Information

Dapsone currently has **no registered drug products with the Philippines FDA**. There are no authorization numbers, brand names, or approved indications on file.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | No registrations found | — | — |

Should clinical deployment be considered, a Philippines FDA registration pathway (new drug application, or a special access / compassionate use mechanism) would be a prerequisite before institutional use.

---

## Safety Considerations

Package insert safety data (local warnings and contraindications) were not available in this evidence pack.

> Please refer to the package insert for safety information.

Two additional safety signals are well-documented in the literature included in this evidence pack and warrant proactive clinical attention:

- **Methemoglobinemia**: Dapsone can oxidize haemoglobin to methaemoglobin, causing dose-dependent cyanosis and hypoxia. Baseline G6PD screening and periodic SpO₂/methaemoglobin monitoring are strongly advised (PMID [9606476](https://pubmed.ncbi.nlm.nih.gov/9606476/), [32714715](https://pubmed.ncbi.nlm.nih.gov/32714715/)).
- **Dapsone Hypersensitivity Syndrome (DHS)**: Strongly associated with the **HLA-B\*1301** allele (prevalent in Asian populations). Prospective genetic pre-screening has been studied in a large Phase 4 trial (NCT02550080, n=3,130) and may substantially reduce DHS incidence.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for Dapsone in pneumocystosis is exceptionally strong — four completed Phase 3 RCTs (total n>1,900), two recent systematic reviews with network meta-analyses, and explicit guideline endorsement at Grade A-II (ECIL-5). The primary barrier to deployment in the Philippines is not evidence strength, but the absence of local market registration and the need for a formal safety monitoring plan.

**To proceed, the following is needed:**
- Establish a Philippines FDA registration or special access pathway for Dapsone
- Obtain and review the local package insert to document full warnings, contraindications, and drug interactions
- Implement a **methemoglobinemia monitoring protocol**: baseline G6PD screen, then periodic SpO₂ and methaemoglobin assessment during therapy
- Evaluate feasibility of **HLA-B\*1301 pre-screening** given high allele frequency in Filipino and Southeast Asian populations, to mitigate Dapsone Hypersensitivity Syndrome risk
- Define the target patient population (HIV/AIDS with CD4 <200/mm³; solid organ transplant; haematological malignancy/HSCT) and select the appropriate prophylaxis or treatment dosing regimen accordingly
- Complete a formal drug interaction review, particularly with trimethoprim (combination partner), rifampicin, and antiretrovirals commonly co-administered in HIV management
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

