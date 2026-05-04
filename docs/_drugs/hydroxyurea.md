---
layout: default
title: Hydroxyurea
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 10
---

# Hydroxyurea
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

# Hydroxyurea: From Myeloproliferative Disorders to Female Breast Carcinoma

## One-Sentence Summary

Hydroxyurea is a ribonucleotide reductase inhibitor historically used for myeloproliferative disorders (chronic myeloid leukemia, polycythemia vera, essential thrombocythemia) and sickle cell disease.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**,
with **0 clinical trials** and **20 publications** currently supporting this direction — though most literature is preclinical or dates from the 1990s.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no Philippines registration data) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 — Preclinical studies and mechanism studies only |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Hydroxyurea (hydroxycarbamide) is an antimetabolite that inhibits ribonucleotide reductase (RNR), the enzyme responsible for converting ribonucleotides to deoxyribonucleotides. By depleting the deoxyribonucleotide pool, it arrests DNA synthesis in rapidly dividing cells. This mechanism is the basis for its established use in chronic myeloid leukemia, polycythemia vera, essential thrombocythemia, and sickle cell disease (where it increases fetal hemoglobin production).

The rationale for predicting efficacy against female breast carcinoma rests on Hydroxyurea's ability to inhibit DNA replication in proliferating tumor cells. Breast carcinoma, as a highly proliferative solid tumor, could theoretically be susceptible to RNR inhibition. Historical Phase I studies from the 1990s explored Hydroxyurea as a component of multi-drug chemotherapy regimens (with 5-FU, cisplatin, and radiation) in advanced solid tumors including breast cancer. More recently, in-silico studies have explored lipid-conjugated Hydroxyurea derivatives targeting the PI3K/AKT/mTOR pathway in breast cancer.

However, Hydroxyurea has never achieved standalone clinical efficacy in breast cancer. Its historical role was limited to combination regimens that are no longer standard of care. The preclinical evidence (valproic acid–HU synergy, nanoparticle delivery systems) remains at the laboratory stage, and no clinical trials are currently registered for this specific indication. The TxGNN prediction score is high (99.97%), but this reflects network topology proximity rather than validated clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for Hydroxyurea in female breast carcinoma.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | Phase I | Am J Clin Oncol | Phase I study of allopurinol/5-FU/leucovorin followed by HU in advanced GI and breast cancer; established feasibility of the HALF regimen |
| [1733549](https://pubmed.ncbi.nlm.nih.gov/1733549/) | 1992 | Phase I/II | Cancer Chemother Pharmacol | 5-FU, leucovorin, HU with escalating cisplatin + radiotherapy in advanced solid tumors; established MTD and pharmacology |
| [2245491](https://pubmed.ncbi.nlm.nih.gov/2245491/) | 1990 | Pilot Study | Cancer Chemother Pharmacol | Cisplatin preceded by cytarabine + HU as DNA repair inhibitors; pilot study based on in-vitro synergy model |
| [7914447](https://pubmed.ncbi.nlm.nih.gov/7914447/) | 1994 | Clinical Study | Bone Marrow Transplant | High-dose cyclophosphamide/thiotepa/HU (18 g/m²) with autologous stem cell rescue as consolidation for metastatic breast cancer |
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | In-silico/Preclinical | Drug Res | In-silico design of HU–lipid conjugates targeting PI3K/AKT/mTOR pathway for breast cancer; improved lipophilicity and cellular uptake predicted |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | Preclinical | DNA Repair | Valproic acid (0.5 mM) sensitizes breast cancer cells to HU by inhibiting RPA2 hyperphosphorylation-mediated DNA repair |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | Preclinical | DNA Repair | 2-hexyl-4-pentynoic acid as VPA analog sensitizes breast carcinoma cells to HU via RPA2 pathway disruption |
| [34661718](https://pubmed.ncbi.nlm.nih.gov/34661718/) | 2022 | Preclinical | Naunyn-Schmiedeberg's Arch Pharmacol | HU-loaded Fe₃O₄/SiO₂/chitosan nanoparticles showed pH-dependent release and cell cycle arrest in MCF-7 breast cancer cells |
| [31338966](https://pubmed.ncbi.nlm.nih.gov/31338966/) | 2019 | Preclinical | J Cell Mol Med | Berberine attenuates XRCC1-mediated base excision repair and sensitizes breast cancer cells to HU and other chemotherapeutic agents |
| [27504932](https://pubmed.ncbi.nlm.nih.gov/27504932/) | 2017 | Preclinical | J Cell Physiol | Characterization of chemoresistance of breast MCF-7 cancer cells to HU under prolonged serum starvation conditions |

## Philippines Market Information

Hydroxyurea is currently **not marketed** in the Philippines. No FDA Philippines registration records are available.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Antimetabolite — Ribonucleotide reductase inhibitor) |
| Myelosuppression Risk | High (dose-limiting toxicity; neutropenia, thrombocytopenia, and anemia are common) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (weekly during dose escalation, monthly at stable dose), liver function, renal function, reticulocyte count |
| Handling Protection | Must follow cytotoxic drug handling regulations; capsules should not be opened — if powder contacts skin or mucous membranes, wash immediately |

## Safety Considerations

> Please refer to the package insert for safety information. Safety data (warnings, contraindications, drug interactions) were not available in this evidence pack.

---

## Additional Predicted Indications Overview

Beyond female breast carcinoma, TxGNN identified 9 additional predicted indications. Of these, the **sickle cell disease variants** (ranks 2–6) are the most clinically relevant, as Hydroxyurea is already an established treatment for sickle cell anemia (HbSS). The oncology predictions (ranks 7–10) lack any supporting evidence.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|---------------------|-------------|---------------|---------------|
| 1 | Female Breast Carcinoma | 99.97% | L4 | Hold |
| 2 | Sickle Cell–Hemoglobin C Disease (HbSC) | 99.67% | L2 | Proceed with Guardrails |
| 3 | HPFH–Sickle Cell Disease Syndrome | 99.67% | L5 | Hold |
| 4 | Sickle Cell–Hemoglobin E Disease (HbSE) | 99.67% | L3 | Research Question |
| 5 | Sickle Cell–Hemoglobin D Disease (HbSD) | 99.67% | L4 | Hold |
| 6 | Sickle Cell–Beta-Thalassemia | 99.67% | L3 | Proceed with Guardrails |
| 7 | Cervical Adenosarcoma | 99.40% | L5 | Hold |
| 8 | Colon Mucinous Adenocarcinoma | 99.32% | L5 | Hold |
| 9 | Rectum Mucinous Adenocarcinoma | 99.31% | L5 | Hold |
| 10 | Gallbladder Mucinous Adenocarcinoma | 99.28% | L5 | Hold |

### Highlight: Sickle Cell–Hemoglobin C Disease (Rank 2)

The strongest repurposing opportunity is **HbSC disease**, supported by **11 clinical trials** and **19 publications**, including a landmark 2025 NEJM Evidence trial (PMID [39647172](https://pubmed.ncbi.nlm.nih.gov/39647172/)).

**Key trials:**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00532883](https://clinicaltrials.gov/study/NCT00532883) | Phase 2 | Terminated | 44 | HU and magnesium pidolate alone/combined in HbSC; evaluated red cell density and pain frequency |
| [NCT02336373](https://clinicaltrials.gov/study/NCT02336373) | Phase 2 | Terminated | 32 | SC Youth Treatment with HU Effects; assessed HU benefit in clinically severe HbSC children |
| [NCT02640573](https://clinicaltrials.gov/study/NCT02640573) | Phase 2 | Terminated | 1 | Treatment of adult HbSC patients with HU |
| [NCT03128515](https://clinicaltrials.gov/study/NCT03128515) | Phase 3 | Completed | 187 | NOHARM-MTD: Optimizing HU dosing in children with SCA in malaria-endemic areas |
| [NCT03474965](https://clinicaltrials.gov/study/NCT03474965) | Phase 2 | Completed | 117 | Crizanlizumab ± HU in pediatric SCD patients with vaso-occlusive crisis |
| [NCT03763656](https://clinicaltrials.gov/study/NCT03763656) | Phase 1/2 | Completed | 33 | PK study of oral HU solution in children with SCA (including HbSC subtypes) |

**Key literature:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39647172](https://pubmed.ncbi.nlm.nih.gov/39647172/) | 2025 | RCT | NEJM Evidence | Hydroxyurea for children and adults with HbSC disease; first major efficacy trial |
| [36047926](https://pubmed.ncbi.nlm.nih.gov/36047926/) | 2022 | Systematic Review | Cochrane Database Syst Rev | Updated Cochrane review of HU for sickle cell disease; comprehensive efficacy/safety assessment |
| [26615793](https://pubmed.ncbi.nlm.nih.gov/26615793/) | 2016 | Clinical Study | Am J Hematol | Effects of HU treatment specifically for HbSC patients; documented laboratory and clinical response |
| [22949140](https://pubmed.ncbi.nlm.nih.gov/22949140/) | 2013 | Clinical Study | Pediatr Blood Cancer | Long-term HU response in children with severe HbSC; increased MCV/HbF, reduced ACS and hospitalization |
| [36799926](https://pubmed.ncbi.nlm.nih.gov/36799926/) | 2023 | Observational | Blood Advances | Most adults with severe HbSC are untreated with HU; documents unmet need in Ghana |
| [11464988](https://pubmed.ncbi.nlm.nih.gov/11464988/) | 2001 | Clinical Study | J Pediatr Hematol Oncol | HU therapy in pediatric HbSC; modest laboratory benefit documented |

### Highlight: Sickle Cell–Beta-Thalassemia (Rank 6)

Also strongly supported, with **4 clinical trials** and **2 publications**. International guidelines already recommend HU for this subtype.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10326220](https://pubmed.ncbi.nlm.nih.gov/10326220/) | 1999 | Clinical Trial | Pediatr Hematol Oncol | HU efficacy in preventing vaso-occlusive crises in children with severe SCA and Sβ-thalassemia (n=19) |

---

## Conclusion and Next Steps

**Decision: Hold** (for the primary prediction — female breast carcinoma)

**Rationale:**
Hydroxyurea's prediction for female breast carcinoma is based on its general anti-proliferative mechanism. However, all clinical evidence is from the 1990s in multi-drug regimens that are no longer standard of care, and recent research is limited to preclinical/in-silico studies. No clinical trials are currently registered. The drug is also not marketed in the Philippines.

**The more actionable repurposing opportunities are the sickle cell disease variants (ranks 2 and 6)**, where HU has established mechanistic rationale (HbF induction) and growing clinical trial evidence — particularly HbSC disease following the 2025 NEJM Evidence trial.

**To proceed, the following is needed:**
- **For breast carcinoma (Hold):**
  - Obtain detailed MOA data from DrugBank
  - Await results of ongoing preclinical studies (HU–lipid conjugates, nanoparticle delivery)
  - Monitor for any new clinical trial registrations
- **For HbSC disease (Proceed with Guardrails):**
  - Confirm Philippines regulatory pathway for Hydroxyurea importation/registration
  - Obtain full results from the 2025 NEJM Evidence trial (PMID 39647172)
  - Obtain package insert safety data (warnings, contraindications, DDI)
  - Assess local sickle cell disease prevalence in the Philippines
- **For Sβ-thalassemia (Proceed with Guardrails):**
  - Confirm alignment with WHO Essential Medicines List recommendations
  - Establish dosing and monitoring protocols for this subtype

---

*Disclaimer: This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

