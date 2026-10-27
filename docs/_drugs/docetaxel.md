---
layout: default
title: Docetaxel
parent: Model Prediction Only (L5)
nav_order: 114
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Docetaxel: predicted new indication Female breast carcinoma (evidence level L5). Approved use: Non-small cell lung cancer, prostate cancer, head and neck cancer…"
monitor_inn: "Docetaxel"
predicted_indications: ["Ewing sarcoma", "well-differentiated fetal adenocarcinoma of the lung", "primary pulmonary lymphoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "pulmonary blastoma", "rhabdomyosarcoma (disease)", "embryonal extrahepatic bile duct rhabdomyosarcoma", "parameningeal embryonal rhabdomyosarcoma"]
---

# Docetaxel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Docetaxel: From Non-Small Cell Lung, Prostate, Gastric, Head and Neck, and Breast Cancer to Female Breast Carcinoma
{: .text-alpha }

## One-Sentence Summary

Docetaxel is a taxane chemotherapy originally used for non-small cell lung cancer, prostate cancer, head and neck cancer, gastric cancer and breast cancer.
The TxGNN model ranks **female breast carcinoma** as its top prediction, which is in fact an existing use, and **43 clinical trials** and **20 publications** are listed for it.
Because breast carcinoma is already a listed original indication, this is an on-label confirmation rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung cancer, prostate cancer, head and neck cancer, gastric cancer, breast cancer (the Philippine license record contains no indication text) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 (see note below) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Proceed with Guardrails |

Note: the data compiled for this report show several completed Phase 3 trials in breast cancer, such as NCT00003519, NCT00021255, NCT00003782, NCT00333775, NCT00887536 and NCT00002707, where docetaxel is part of the regimen. Most of these have not been individually graded for relevance, so the L1 level should be confirmed on review.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Docetaxel is a taxane, a class that stabilises microtubules and causes cells to stop dividing (mitotic arrest). This is the same mechanism that underlies its established use in breast cancer.

Breast carcinoma is already among docetaxel's original indications, so the model is confirming a known use rather than finding a new one. Published pivotal and early-breast-cancer data, such as the ABC trials (PMID 28398846), support this.

The other top predictions are mostly related cancers: sarcomas, rare lung tumours and rhabdomyosarcoma subtypes. Only Ewing sarcoma, small cell lung carcinoma and rhabdomyosarcoma have any trial evidence, and it is limited. Those are better treated as research questions than as established indications.

---

## Clinical Trial Evidence

The table lists the most relevant trials among 43 for female breast carcinoma. Completed Phase 3 trials are shown first, then the trials graded A or B for relevance.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003782](https://clinicaltrials.gov/study/NCT00003782) | Phase 3 | Completed | 5351 | Adjuvant AC-T vs AT vs ATC in node-positive breast cancer |
| [NCT00021255](https://clinicaltrials.gov/study/NCT00021255) | Phase 3 | Completed | 3222 | AC-T vs AC-TH vs TCH in HER2-positive operable breast cancer |
| [NCT00003519](https://clinicaltrials.gov/study/NCT00003519) | Phase 3 | Completed | 2778 | Adriamycin/Taxotere vs Adriamycin/Cytoxan, adjuvant setting |
| [NCT00002707](https://clinicaltrials.gov/study/NCT00002707) | Phase 3 | Completed | 2411 | Preoperative AC with or without docetaxel before or after surgery |
| [NCT00887536](https://clinicaltrials.gov/study/NCT00887536) | Phase 3 | Completed | 1613 | TC plus bevacizumab vs TC alone vs TAC in HER2-negative breast cancer |
| [NCT00333775](https://clinicaltrials.gov/study/NCT00333775) | Phase 3 | Completed | 736 | Bevacizumab plus docetaxel vs docetaxel plus placebo, first-line metastatic |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | Completed | 652 | Taxane plus lapatinib vs trastuzumab in HER2-positive metastatic breast cancer |
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Phase 2 | Completed | 148 | Randomised carboplatin vs docetaxel in metastatic breast cancer (graded A) |
| [NCT00003352](https://clinicaltrials.gov/study/NCT00003352) | Phase 2 | Completed | 89 | Doxorubicin, docetaxel and cyclophosphamide in advanced breast cancer (graded A) |
| [NCT00003953](https://clinicaltrials.gov/study/NCT00003953) | Phase 2 | Completed | 39 | Preoperative dose-dense doxorubicin then docetaxel (graded B) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | RCT | J Clin Oncol | ABC trials: docetaxel plus cyclophosphamide (TC) compared with standard taxane-anthracycline regimens in early breast cancer |
| [30340871](https://pubmed.ncbi.nlm.nih.gov/30340871/) | 2019 | Phase 2 | Clin Breast Cancer | S-1 with low-dose docetaxel as neoadjuvant therapy for operable breast cancer |
| [9364543](https://pubmed.ncbi.nlm.nih.gov/9364543/) | 1997 | Review | Oncology (Williston Park) | Docetaxel with vinorelbine in metastatic breast and lung cancer |
| [10791395](https://pubmed.ncbi.nlm.nih.gov/10791395/) | 2000 | Review | Lancet | Taxanes are evidence-based components of therapy for advanced breast, lung and ovarian cancer |
| [12868800](https://pubmed.ncbi.nlm.nih.gov/12868800/) | 2003 | Review | Breast Cancer Res Treat | Docetaxel-anthracycline combinations in metastatic breast cancer |
| [9775340](https://pubmed.ncbi.nlm.nih.gov/9775340/) | 1998 | Review | Am J Health Syst Pharm | Pharmacology, trials and adverse effects of docetaxel in metastatic breast cancer |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Phase 2 | Cancer | Capecitabine with docetaxel and epirubicin as first-line therapy in advanced breast cancer |
| [16020974](https://pubmed.ncbi.nlm.nih.gov/16020974/) | 2005 | Phase 2 | Oncology | Weekly docetaxel and gemcitabine as first-line therapy for metastatic breast cancer |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Retrospective | Anti-Cancer Drugs | Association of adjuvant docetaxel-based chemotherapy with breast cancer-related lymphedema |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0153 | Docetaxel | Not recorded | Not recorded (registration cancelled) |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane, microtubule stabiliser) |
| Myelosuppression Risk | High. Neutropenia, thrombocytopenia and anaemia appear among the contraindicated conditions in the knowledge graph |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Complete blood count with differential, liver function including bilirubin, renal function, signs of neuropathy and fluid retention |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: liver disease, gallbladder disease, hyperbilirubinaemia (including Gilbert syndrome), thrombocytopenia, neutropenia, agranulocytosis, anaemia, peripheral neuropathy and neuritis, diarrhoeal disease, stomatitis, pulmonary oedema and cardiac tamponade.
- **Drug Interactions**: 100 interactions were identified. The most important:
  - **Major**: clarithromycin.
  - **Moderate**: aprepitant, rolapitant, cimetidine, metronidazole, tinidazole, miconazole, eliglustat, rosuvastatin, simvastatin and troglitazone.
  - **Minor**: dexamethasone, prednisolone, prednisone and levofloxacin.
- **Literature signals**: interstitial pneumonitis (PMID 17921105) and fluid retention or lymphoedema (PMID 27997437).

The package insert warnings and contraindications for the Philippine product were not available, so please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Breast carcinoma is already an established docetaxel indication, supported by large Phase 3 adjuvant and metastatic trials, so efficacy is not in doubt.
- The Philippine registration is cancelled, and the package insert, mechanism data and Philippine label indications are missing, so any use needs controls.

**To proceed, the following is needed:**
- Confirmation of the evidence level, with individual relevance grading of the Phase 3 trials.
- A current valid Philippine registration, or an alternative supply route, since the only licence is cancelled.
- The Philippine package insert for warnings and contraindications, which blocks safety screening.
- Detailed mechanism of action data from DrugBank.
- A haematological and hepatic monitoring plan, plus interaction management, especially for strong CYP3A4 inhibitors such as clarithromycin.

**Other predictions:** Ewing sarcoma, small cell lung carcinoma and rhabdomyosarcoma are research questions (L2), mainly supported by small gemcitabine-docetaxel Phase 2 studies or by NSCLC data that do not transfer directly. The remaining predictions are on Hold, with at most case reports or no evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

