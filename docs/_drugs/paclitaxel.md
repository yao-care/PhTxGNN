---
layout: default
title: Paclitaxel
parent: Model Prediction Only (L5)
nav_order: 269
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
monitor_inn: "Paclitaxel"
predicted_indications: ["parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
description: "Paclitaxel: predicted new indication Parameningeal embryonal rhabdomyosarcoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Paclitaxel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Paclitaxel: Parameningeal embryonal rhabdomyosarcoma
{: .text-alpha }

## One-Sentence Summary

Paclitaxel is a microtubule-stabilizing cytotoxic drug, originally used for ovarian cancer.
with **40 clinical trials** and **20 publications** currently listed for this direction. Most of the trials are Phase 1/2 combination studies, and paclitaxel is already a mainstream breast cancer treatment, so this is not a novel repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Parameningeal embryonal rhabdomyosarcoma |
| TxGNN Prediction Score | 0.9973 |
| Evidence Level | L5 (L1 for the ER-positive breast cancer sub-node) |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, paclitaxel is a taxane that stabilizes microtubules. This blocks mitotic spindle disassembly and causes G2/M arrest and apoptosis in rapidly dividing tumor cells.

Ovarian and breast cancers are both common solid tumors treated with cytotoxic chemotherapy. Taxanes are widely accepted, evidence-based components of therapy for advanced breast and ovarian carcinomas (Lancet 2000 review). Paclitaxel's antimitotic action does not depend on hormone receptor status, so it is also expected to work in ER-negative, ER-positive and hormone-resistant disease.

The prediction is therefore reasonable, but it largely reflects established clinical practice. The supplied trials for this disease node are mostly Phase 2 or combination studies, and none is a Phase 3 trial specific to this node.

## Clinical Trial Evidence

The list below shows 10 of the trials compiled for this disease node (40 in total).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Phase 3 | Completed | Not reported | Paclitaxel with or without gemcitabine in unresectable, locally recurrent or metastatic breast cancer |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | Completed | 652 | Taxane plus lapatinib vs trastuzumab as first-line therapy in HER2-positive metastatic breast cancer |
| [NCT00075270](https://clinicaltrials.gov/study/NCT00075270) | Phase 3 | Completed | 580 | Lapatinib plus paclitaxel vs paclitaxel alone in first-line advanced or metastatic breast cancer |
| [NCT00553358](https://clinicaltrials.gov/study/NCT00553358) | Phase 3 | Completed | 455 | NeoALTTO: neoadjuvant lapatinib and/or trastuzumab plus paclitaxel in HER2-positive breast cancer |
| [NCT01822314](https://clinicaltrials.gov/study/NCT01822314) | Phase 3 | Completed | 632 | Neoadjuvant nab-paclitaxel vs solvent-based paclitaxel, then anthracycline regimens, measuring pathological complete response |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Phase 3 | Completed | 478 | Dose-dense FE75C followed by docetaxel vs paclitaxel as adjuvant therapy in node-positive breast cancer |
| [NCT00513292](https://clinicaltrials.gov/study/NCT00513292) | Phase 3 | Completed | 280 | Neoadjuvant FEC then paclitaxel plus trastuzumab vs the reverse sequence in HER2-positive operable breast cancer |
| [NCT00006120](https://clinicaltrials.gov/study/NCT00006120) | Phase 2 | Unknown | Not reported | Randomized comparison of two schedules of docetaxel or paclitaxel in metastatic breast cancer |
| [NCT00003539](https://clinicaltrials.gov/study/NCT00003539) | Phase 2 | Completed | 50 | Weekly paclitaxel plus trastuzumab in metastatic breast cancer; single-arm |
| [NCT05020860](https://clinicaltrials.gov/study/NCT05020860) | Phase 2 | Recruiting | 185 | Whether clinical response predicts pathological response after neoadjuvant therapy |

## Literature Evidence

The list below shows 10 of the 20 publications compiled for this disease node.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22331946](https://pubmed.ncbi.nlm.nih.gov/22331946/) | 2012 | Phase 3 trial | J Clin Oncol | Weekly paclitaxel vs docetaxel combined with capecitabine in operable breast cancer, measuring relapse-free survival |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Phase 2 trial | Cancer | Doxorubicin plus paclitaxel in metastatic breast carcinoma; efficacy and toxicity, with attention to prior adjuvant anthracycline |
| [10791395](https://pubmed.ncbi.nlm.nih.gov/10791395/) | 2000 | Review | Lancet | Taxanes are accepted evidence-based therapy for advanced breast, lung and ovarian carcinoma; paclitaxel approved in the USA for adjuvant node-positive breast cancer |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug Ther Bull | Paclitaxel and docetaxel in breast and ovarian cancer; licence extended to metastatic breast cancer |
| [7904376](https://pubmed.ncbi.nlm.nih.gov/7904376/) | 1993 | Review | Semin Oncol Nurs | Overview of paclitaxel development and mechanism |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Clinical study | Cancer | Paclitaxel in multimodality treatment of inflammatory breast carcinoma |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Translational study | Nat Commun | TEKT4 germline variations linked to breast cancer resistance to paclitaxel |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Computational/preclinical | Chem Biol Drug Des | Paclitaxel combinations against breast carcinoma and in vivo biomarkers |
| [20665703](https://pubmed.ncbi.nlm.nih.gov/20665703/) | 2011 | Preclinical | J Cell Physiol | ZD6474 enhances paclitaxel antiproliferative and apoptotic effects in breast carcinoma cells |
| [9445630](https://pubmed.ncbi.nlm.nih.gov/9445630/) | 1997 | Review | Gynakol Geburtshilfliche Rundsch | New drugs in breast carcinoma therapy |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0370 | Paclitaxel | Not specified | Not specified (status: valid) |


## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane, microtubule stabilizer) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver and renal function, peripheral neuropathy assessment, hypersensitivity monitoring during infusion |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please also refer to the package insert warnings and precautions.

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interactions in total; 20 are shown in the data compiled for this report. Most are of moderate severity. Moderate-level examples include aprepitant, rolapitant, cimetidine, clarithromycin, clotrimazole, miconazole, dexamethasone, eliglustat, metronidazole, tinidazole, rosuvastatin, simvastatin and troglitazone. Minor-level examples are ascorbic acid and levofloxacin. Several others, such as glimepiride, doxycycline, morphine, metformin and omeprazole, have an unknown level.
- **Knowledge-graph contraindication signals** (not from label text): neutropenia, agranulocytosis, thrombocytopenia, anemia, liver disease, kidney disease, peripheral neuropathy, myocardial infarction, sudden cardiac arrest, hyperbilirubinemia, Gilbert syndrome, asthma, diabetes mellitus, diabetic ketoacidosis, psoriasis, hypotensive disorder, and several psychiatric disorders. These need confirmation against the package insert.
- Literature in the compiled data also describes paclitaxel-associated pneumonitis, uveitis, corneal epithelial lesions, periarticular thenar erythema with onycholysis, and taxane-induced polyneuropathy.

The package insert warnings and contraindications could not be obtained, so please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Paclitaxel has extensive Phase 2 and Phase 3 trial activity and long-standing guideline use in breast cancer, so the biological plausibility is strong. However, this is an established use rather than a new repurposing finding. The Philippines registration is cancelled and the package insert safety data is missing.

**To proceed, the following is needed:**
- Obtain the package insert warnings and contraindications from DOH-FDA Philippines (a blocking data gap for safety screening)
- Obtain detailed mechanism of action data (for example from DrugBank)
- Select a Phase 3 trial specific to paclitaxel efficacy in breast cancer, since most listed trials test combination partners
- Define a safety monitoring plan covering myelosuppression, neuropathy, hypersensitivity and drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

