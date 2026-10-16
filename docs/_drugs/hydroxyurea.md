---
layout: default
title: Hydroxyurea
parent: Moderate Evidence (L3-L4)
nav_order: 168
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Hydroxyurea: predicted new indication Female breast carcinoma (evidence level L4). Approved use: Melanoma, sickle cell anemia…"
monitor_inn: "Hydroxyurea"
predicted_indications: ["female breast carcinoma", "sickle cell-hemoglobin c disease syndrome", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "sickle cell-hemoglobin E disease syndrome", "sickle cell-hemoglobin d disease syndrome", "sickle cell-beta-thalassemia disease syndrome", "cervical adenosarcoma", "colon mucinous adenocarcinoma", "rectum mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma"]
---

# Hydroxyurea
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Hydroxyurea: From Melanoma and Sickle Cell Anemia to Female Breast Carcinoma

## One-Sentence Summary

Hydroxyurea is an antineoplastic drug originally used for melanoma, sickle cell anemia, and ovarian cancer.
The TxGNN model predicts it may be effective for **female breast carcinoma**, but the data compiled for this report contain **no clinical trials** and **20 publications**, which are mostly preclinical or only loosely related.
A far better-supported alternative within the same prediction list is **sickle cell-hemoglobin C disease (HbSC)**, which has **1 clinical trial** and a **2025 NEJM Evidence publication** (see the note below the Quick Overview).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Melanoma, sickle cell anemia, hereditary persistence of fetal hemoglobin, ovarian cancer (the Philippines license record has no approved-indication text) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Cancelled only (no valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

**Note on other predictions:** The top-ranked prediction (breast carcinoma) has the weakest evidence among the first six. The HbSC prediction (rank 2, TxGNN score 99.67%) reaches Evidence Level L2 with a recommendation of **Proceed with Guardrails**. The remaining predictions (HPFH-sickle, sickle-HbE, sickle-HbD, and four rare tumors) are mostly Hold or Research Question.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, hydroxyurea inhibits ribonucleotide reductase, which depletes the dNTP pool and induces DNA replication stress. Cancer cells with defective DNA repair or high replication stress may be especially sensitive to this effect.

Preclinical papers support a plausible link to breast cancer. They cover replication-stress biology, RPA2 hyperphosphorylation, valproic acid sensitization of breast cancer cells to hydroxyurea, and ATR inhibition in breast and ovarian cancer cell lines. Hydroxyurea's established activity in ovarian cancer and melanoma also makes extension to another hormone-related solid tumor reasonable in principle.

However, the evidence stops at the mechanistic and laboratory level. The only clinical papers are old phase 1 combination chemotherapy studies in mixed solid tumors, with 1991 and 1992 publication dates. A lipid-conjugate drug design paper is in-silico only. No breast-cancer-specific clinical trial was found.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for female breast carcinoma.

For reference, the one directly relevant trial in the broader prediction list is for HbSC disease:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00532883](https://clinicaltrials.gov/study/NCT00532883) | Phase 2 | Terminated | 44 | Hydroxyurea and magnesium pidolate, alone and combined, to reduce red cell density and pain episodes in HbSC disease; early termination limits conclusions |

---

## Literature Evidence

Most relevant publications for female breast carcinoma (clinical studies first, then preclinical):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1733549](https://pubmed.ncbi.nlm.nih.gov/1733549/) | 1992 | Phase 1/2 | Cancer Chemother Pharmacol | 5-FU, leucovorin, hydroxyurea, and escalating cisplatin with radiotherapy in advanced solid tumors (mixed tumors) |
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | Phase 1 | Am J Clin Oncol | Allopurinol, 5-FU, leucovorin, then hydroxyurea in 20 patients with advanced GI and breast cancer |
| [30159181](https://pubmed.ncbi.nlm.nih.gov/30159181/) | 2018 | Case report | Case Rep Hematol | Management of coexisting breast cancer and essential thrombocythemia |
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | In-silico | Drug Res | Design of hydroxyurea lipid conjugates targeting PI3K/AKT/mTOR for breast cancer |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | Preclinical | DNA Repair | Valproic acid sensitizes breast cancer cells to hydroxyurea by inhibiting RPA2-mediated DNA repair |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | Preclinical | DNA Repair | 2-hexyl-4-pentynoic acid as a potential breast carcinoma therapeutic acting on the same DNA repair pathway |
| [21730979](https://pubmed.ncbi.nlm.nih.gov/21730979/) | 2011 | Preclinical | Br J Cancer | ATR inhibitor NU6027 in breast and ovarian cancer cell lines |
| [37777742](https://pubmed.ncbi.nlm.nih.gov/37777742/) | 2023 | Preclinical | Mol Cancer | EYA4 promotes breast cancer progression through replication stress avoidance |

Several other retrieved papers are only tangentially relevant (for example cervical cancer chemoradiation and a meningioma case report) and are not listed.

**Evidence for the HbSC prediction (rank 2):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39647172](https://pubmed.ncbi.nlm.nih.gov/39647172/) | 2025 | Clinical study | NEJM Evidence | Safety and efficacy of hydroxyurea in children and adults with HbSC |
| [36047926](https://pubmed.ncbi.nlm.nih.gov/36047926/) | 2022 | Cochrane review | Cochrane Database Syst Rev | Hydroxyurea for sickle cell disease overall |
| [26615793](https://pubmed.ncbi.nlm.nih.gov/26615793/) | 2016 | Cohort | Am J Hematol | Effects of hydroxyurea in patients with HbSC |
| [22949140](https://pubmed.ncbi.nlm.nih.gov/22949140/) | 2013 | Cohort | Pediatr Blood Cancer | In 15 children with severe HbSC, hydroxyurea raised MCV and HbF and reduced acute chest syndrome and pain hospitalizations; thrombocytopenia was the main side effect |
| [36799926](https://pubmed.ncbi.nlm.nih.gov/36799926/) | 2023 | Cohort | Blood Adv | Most adults with severe HbSC are not treated with hydroxyurea, indicating an unmet need |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0236 | Hydroxyurea | Not specified | Not specified (status: cancelled) |

The only registration on record has been cancelled, so there is currently no valid marketed hydroxyurea product in the Philippines according to the data compiled for this report.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite, ribonucleotide reductase inhibitor) |
| Myelosuppression Risk | High. Thrombocytopenia is the main side effect reported in HbSC pediatric data, and the knowledge graph also links the drug to leukopenia and anemia contraindications |
| Emetogenicity Classification | Low (general knowledge for oral hydroxyurea; please confirm against the package insert) |
| Monitoring Items | CBC with differential, platelet count, liver and renal function |
| Handling Protection | Follow cytotoxic drug handling regulations; please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Contraindications (knowledge graph, not label text):** kidney disease, pyoureter, thrombocytopenia, anemia, macrocytic anemia, leukopenia, cutaneous vasculitis.
- **Drug Interactions:** The interaction screen returned 100 potential interacting drugs. Most are of unknown severity. The only graded entry shown is levofloxacin (Minor). Others include doxycycline, amphotericin B, hydrocortisone, famotidine, acetylsalicylic acid, pantoprazole, metformin, omeprazole, morphine, simvastatin, vancomycin, and prednisone. A full interaction review is needed before any clinical use.
- **Additional guardrails (from the HbSC analysis):** monitor myelosuppression, and consider teratogenicity and fertility.

Please refer to the package insert for key warnings and label contraindications.

---

## Conclusion and Next Steps

**Decision: Hold** (for female breast carcinoma)

**Rationale:**
- The TxGNN score is high (99.97%), but support is limited to preclinical mechanistic work and old mixed-tumor phase 1 studies. There is no breast-cancer-specific trial, and no valid Philippines registration exists.
- By contrast, **HbSC disease** merits a separate evaluation with **Proceed with Guardrails** (Evidence Level L2), supported by a terminated Phase 2 trial, a 2025 NEJM Evidence publication, and observational data.

**To proceed, the following is needed:**
- For breast carcinoma: breast-specific clinical data (at least a well-designed phase 2 trial), and a defined patient subgroup, such as tumors with defective homologous recombination or high replication stress.
- Detailed mechanism of action data.
- The Philippines package insert (warnings and contraindications), and a new or reinstated registration, since the only license is cancelled.
- A myelosuppression monitoring plan and a full drug interaction review.
- For HbSC: full review of the NEJM Evidence results and the reasons NCT00532883 was terminated.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

