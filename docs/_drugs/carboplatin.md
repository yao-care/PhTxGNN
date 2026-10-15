---
layout: default
title: Carboplatin
parent: High Evidence (L1-L2)
nav_order: 62
evidence_level: L2
indication_count: 10
---

# Carboplatin
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Carboplatin: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Carboplatin is a platinum-based chemotherapy drug, originally used to treat ovarian cancer and related ovarian tumours.
The TxGNN model predicts it may be effective for **female breast carcinoma**,
with **43 clinical trials** and **20 publications** compiled for this direction. Most trials test carboplatin as part of a combination regimen, and the strongest listed trial is a randomized Phase 2 study.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (including ovarian adenocarcinoma and ovarian germ cell tumours; the Philippines registration record carries no indication text) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 |
| Philippines Market Status | Cancelled only (no valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, carboplatin is a DNA-crosslinking platinum agent. Its efficacy in ovarian cancer is established, and mechanistically it may be applicable to breast cancer.

Tumours with homologous recombination deficiency, such as BRCA-mutated breast cancer and triple-negative breast cancer (TNBC), are particularly sensitive to platinum-induced DNA damage. This overlaps with the hereditary breast and ovarian cancer syndrome listed among carboplatin's original indications. Combination with PARP inhibitors such as veliparib is also mechanistically synergistic.

An important caveat: the strongest listed trial is a randomized Phase 2 study (NCT00321633), supported by several Phase 1/2 combination studies. The randomized neoadjuvant studies in the literature (GeparSixto, CALGB 40603, BrighTNess) are cited here by title and abstract only, and their results have not been independently verified. For that reason, no completed Phase 3 evidence is counted in the L2 rating for breast cancer.

## Clinical Trial Evidence

The compiled data lists 43 trials. The most relevant are shown below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Phase 2 | Completed | 148 | Randomized comparison of carboplatin vs docetaxel in metastatic genetic (BRCA) breast cancer; directly tests carboplatin as a single agent |
| [NCT05020860](https://clinicaltrials.gov/study/NCT05020860) | Phase 2 | Recruiting | 185 | Neoadjuvant therapy in early breast cancer; correlates clinical response with pathologic response (carboplatin within a combination regimen) |
| [NCT00616967](https://clinicaltrials.gov/study/NCT00616967) | Phase 2 | Active, not recruiting | 68 | Double-blind trial of carboplatin + nab-paclitaxel with or without vorinostat as preoperative chemotherapy in HER2-negative breast cancer |
| [NCT00535119](https://clinicaltrials.gov/study/NCT00535119) | Phase 1 | Completed | 107 | Veliparib with carboplatin and paclitaxel in advanced solid tumours; supports PARP-inhibitor/platinum safety |
| [NCT00021255](https://clinicaltrials.gov/study/NCT00021255) | Phase 3 | Completed | 3,222 | Adjuvant AC-T vs AC-TH vs docetaxel/carboplatin/trastuzumab (TCH) in HER2-positive operable breast cancer |
| [NCT00047255](https://clinicaltrials.gov/study/NCT00047255) | Phase 3 | Completed | 263 | Docetaxel + trastuzumab with or without carboplatin as first-line therapy in HER2-amplified advanced breast cancer |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | Completed | 961 | GeparOcto: two dose-dense neoadjuvant approaches in high-risk early breast cancer, one including carboplatin |
| [NCT01208480](https://clinicaltrials.gov/study/NCT01208480) | Phase 2 | Completed | 45 | Neoadjuvant bevacizumab, docetaxel and carboplatin in triple-negative breast cancer |
| [NCT00003612](https://clinicaltrials.gov/study/NCT00003612) | Phase 2 | Completed | 92 | Randomized paclitaxel, carboplatin and trastuzumab as first-line therapy in HER2-overexpressing metastatic breast cancer |
| [NCT06291064](https://clinicaltrials.gov/study/NCT06291064) | Phase 2 | Recruiting | 85 | Epirubicin/cyclophosphamide followed by docetaxel + carboplatin in Nigerian women with TNBC |

Note that in the Phase 3 trials above, carboplatin is part of a combination or an experimental arm; these trials do not isolate carboplatin's own effect, and their results are not provided in the compiled data.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24794243](https://pubmed.ncbi.nlm.nih.gov/24794243/) | 2014 | RCT (Phase 2) | Lancet Oncol | GeparSixto: adding carboplatin to neoadjuvant therapy in triple-negative and HER2-positive early breast cancer |
| [29501363](https://pubmed.ncbi.nlm.nih.gov/29501363/) | 2018 | RCT (Phase 3) | Lancet Oncol | BrighTNess: veliparib plus carboplatin, or carboplatin alone, added to standard neoadjuvant chemotherapy in TNBC |
| [35044810](https://pubmed.ncbi.nlm.nih.gov/35044810/) | 2022 | RCT (Phase 2) | J Clin Oncol | CALGB 40603: long-term outcomes of adding carboplatin or bevacizumab to neoadjuvant chemotherapy in TNBC |
| [33208340](https://pubmed.ncbi.nlm.nih.gov/33208340/) | 2021 | RCT (Phase 2) | Clin Cancer Res | NeoSTOP: anthracycline-free vs anthracycline-containing neoadjuvant carboplatin regimens in TNBC |
| [41436191](https://pubmed.ncbi.nlm.nih.gov/41436191/) | 2025 | RCT (Phase 3) | BMJ | CITRINE: adjuvant carboplatin-intensified vs standard chemotherapy in high-risk early TNBC |
| [41115255](https://pubmed.ncbi.nlm.nih.gov/41115255/) | 2026 | RCT (Phase 3) | J Clin Oncol | Adding carboplatin to sequential taxane-anthracycline neoadjuvant chemotherapy in TNBC |
| [40817986](https://pubmed.ncbi.nlm.nih.gov/40817986/) | 2025 | Randomized Phase 2 | Breast Cancer Res Treat | Single-agent carboplatin vs carboplatin plus everolimus in advanced TNBC |
| [38492276](https://pubmed.ncbi.nlm.nih.gov/38492276/) | 2024 | Review | Breast | Platinum chemotherapy in early TNBC; improves pathological complete response, long-term survival effect not fully clarified |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Review | Pharmacol Res | Targeted and cytotoxic inhibitors used in breast cancer treatment |
| [16720915](https://pubmed.ncbi.nlm.nih.gov/16720915/) | 2006 | Review | Med Oncol | Paclitaxel-carboplatin combination in advanced breast cancer: evidence for synergy, efficacy and safety |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0077 | Carboplatin | Not recorded | Not recorded (status: cancelled) |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (platinum-based DNA-crosslinking agent) |
| Myelosuppression Risk | High (the knowledge graph links carboplatin with thrombocytopenia, neutropenia, leukopenia and anaemia as cautions) |
| Emetogenicity Classification | Moderate (general category for carboplatin; please confirm against the package insert) |
| Monitoring Items | Complete blood count with differential, renal and liver function, hearing and neurological assessment |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindications / cautions (from knowledge graph links, not label text)**: kidney disease, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, leukopenia, anaemia, blood coagulation disease, peripheral neuropathy and other peripheral nervous system disease, hearing and auditory system disorders, and functional visual loss.
- **Drug Interactions**: 100 interactions were found. Most are Moderate, including proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, pantoprazole, rabeprazole, dexlansoprazole), aminoglycoside and glycopeptide antibiotics (kanamycin, neomycin, streptomycin, vancomycin), nitroimidazoles (metronidazole, tinidazole) and statins (rosuvastatin, simvastatin). Levofloxacin is Minor. Several others, such as calcitriol, glimepiride and doxycycline, are of unknown level.

Please also refer to the package insert for official warnings.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Breast cancer has a randomized Phase 2 trial of carboplatin as a single agent, plus multiple randomized neoadjuvant studies in TNBC and HER2-positive disease, and a plausible mechanism via DNA-damage sensitivity. However, much of the evidence is for combination regimens, and the local registration is cancelled, so a go-forward decision needs care.

**Other predictions in brief:**
- **Adult germ cell tumour** (score 99.24%, L3): Phase 2 high-dose regimens and a systematic review exist, but carboplatin's role relative to cisplatin is debated. Treat as a research question.
- **Endometrial mixed adenocarcinoma** (score 99.20%, L1 by trial design): two Phase 3 trials use carboplatin/paclitaxel as the backbone, but they test the added agent rather than carboplatin itself, so histology-specific outcomes must be confirmed.
- **Endometrial mucinous adenocarcinoma** (L3): limited to two small Phase 1 studies; research question.
- **Cervical mucinous adenocarcinoma** (L4): one small Phase 1 trial and case reports; hold.
- **Rectal, colonic, gallbladder, extrahepatic bile duct mucinous adenocarcinoma, and villoglandular endometrial endometrioid adenocarcinoma**: prediction only, or only irrelevant case reports; hold.

**To proceed, the following is needed:**
- Verification of design and results of the neoadjuvant randomized trials (GeparSixto, CALGB 40603, BrighTNess, CITRINE) and clarification of whether carboplatin's own contribution can be isolated
- Package insert warnings and contraindications (the Philippines label data are currently unavailable)
- Detailed mechanism of action data (MOA)
- Clarification of the cancelled Philippines registration and the route to a valid authorization
- A safety monitoring plan, especially for myelosuppression, renal impairment, neuropathy and ototoxicity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

