---
layout: default
title: Letrozole
parent: High Evidence (L1-L2)
nav_order: 201
evidence_level: L1
indication_count: 4
last_modified_at: 2026-10-28
monitor_inn: "Letrozole"
predicted_indications: ["nipple carcinoma", "Ehrlich tumor carcinoma", "breast fibrocystic disease", "benign mammary dysplasia"]
description: "Letrozole: predicted new indication Nipple carcinoma (evidence level L1). Approved use: Not recorded in the local data"
---

# Letrozole
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **4** 
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

## Letrozole: Nipple carcinoma
{: .text-alpha }

## One-Sentence Summary

Letrozole is a nonsteroidal aromatase inhibitor. The Philippines license record does not state an approved indication, but the drug is established in hormone receptor-positive breast cancer.
This is effectively a confirmation of a known use rather than a new repurposing, so the signal mainly checks the model rather than opening a new indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nipple carcinoma |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L1 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, letrozole is a nonsteroidal aromatase inhibitor. It blocks the conversion of androgens to estrogens and so reduces estrogen-driven tumour growth in hormone receptor-positive breast cancer.

The predicted indication is not truly new. Phase 3 trials, including MONALEESA-2 (ribociclib plus letrozole) and PALOMA-2 (palbociclib plus letrozole), use letrozole as the endocrine backbone. The "Cancelled only" market status and the missing original-indication field are probably data gaps in the registration record and should be verified.

Other predictions in the list vary in strength:
- **Estrogen-receptor positive breast cancer** has the same strong support (L1).
- **Hormone-resistant breast carcinoma, bilateral breast carcinoma and gene-expression-defined breast carcinoma** have partial support (L2). Letrozole is mostly a combination backbone or a stratification context in these.
- **Estrogen-receptor negative breast cancer, nipple carcinoma, Ehrlich tumour, fibrocystic disease and benign mammary dysplasia** are weak or unsupported (L4–L5). The trials returned for ER-negative disease are actually in ER+ populations, which likely reflects disease-label mapping noise.

---

## Clinical Trial Evidence

Ten of the most relevant trials for female breast carcinoma are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02941926](https://clinicaltrials.gov/study/NCT02941926) | Phase 3 | Completed | 3246 | COMPLEEMENT-1: ribociclib plus letrozole in HR+/HER2- advanced breast cancer, giving large-scale safety and efficacy data |
| [NCT02600923](https://clinicaltrials.gov/study/NCT02600923) | Phase 3 | Completed | 131 | Palbociclib plus letrozole in postmenopausal women with HR+/HER2- advanced disease (access study in Latin America) |
| [NCT01740427](https://clinicaltrials.gov/study/NCT01740427) | Phase 3 | Completed | 666 | PALOMA-2: palbociclib plus letrozole versus placebo plus letrozole as first-line therapy |
| [NCT00433589](https://clinicaltrials.gov/study/NCT00433589) | Phase 3 | Completed | 6600 | MINDACT: 70-gene signature to guide adjuvant chemotherapy; letrozole is part of the endocrine therapy |
| [NCT00382070](https://clinicaltrials.gov/study/NCT00382070) | Phase 3 | Unknown | 3966 | Five years of letrozole versus placebo after prior endocrine therapy, with disease-free survival as endpoint |
| [NCT03425838](https://clinicaltrials.gov/study/NCT03425838) | Phase 3 | Active, not recruiting | 1050 | SONIA: aromatase inhibitor plus CDK4/6 inhibitor in first line versus second line; results not yet available |
| [NCT00908531](https://clinicaltrials.gov/study/NCT00908531) | Phase 3 | Terminated | 123 | DBCG: four months of letrozole versus upfront surgery; terminated early, so limited power |
| [NCT03439046](https://clinicaltrials.gov/study/NCT03439046) | Phase 3 | Terminated | 287 | BioItaLEE: molecular features on ribociclib plus letrozole in first line |
| [NCT04272801](https://clinicaltrials.gov/study/NCT04272801) | Phase 2 | Active, not recruiting | 84 | Pre-operative endocrine therapy window in women 65 and older to inform radiation decisions |
| [NCT01439711](https://clinicaltrials.gov/study/NCT01439711) | Phase 2 | Completed | 108 | Neoadjuvant letrozole in ER+ ductal carcinoma in situ |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35263519](https://pubmed.ncbi.nlm.nih.gov/35263519/) | 2022 | RCT | N Engl J Med | Overall survival benefit of ribociclib plus letrozole in advanced breast cancer |
| [29718092](https://pubmed.ncbi.nlm.nih.gov/29718092/) | 2018 | RCT | Ann Oncol | Updated MONALEESA-2 efficacy and safety of ribociclib plus letrozole |
| [30632023](https://pubmed.ncbi.nlm.nih.gov/30632023/) | 2019 | RCT | Breast Cancer Res Treat | PALOMA-2 extended follow-up: palbociclib plus letrozole, progression-free survival HR 0.58 at initial analysis |
| [36243120](https://pubmed.ncbi.nlm.nih.gov/36243120/) | 2022 | Review | Life Sci | Pharmacology, toxicity and therapeutic uses of letrozole |
| [17912633](https://pubmed.ncbi.nlm.nih.gov/17912633/) | 2007 | Review | Breast Cancer Res Treat | Discovery and mechanism of action of letrozole as a third-generation aromatase inhibitor |
| [21364577](https://pubmed.ncbi.nlm.nih.gov/21364577/) | 2011 | Review | Br J Cancer | Clinical differences between anastrozole and letrozole |
| [17544670](https://pubmed.ncbi.nlm.nih.gov/17544670/) | 2007 | Review | Breast | Extended adjuvant letrozole, based on the MA-17 trial |
| [10514021](https://pubmed.ncbi.nlm.nih.gov/10514021/) | 1999 | Review | Drug Saf | Risks and benefits of aromatase inhibitors in postmenopausal breast cancer |
| [29229198](https://pubmed.ncbi.nlm.nih.gov/29229198/) | 2017 | Preclinical | Arch Med Res | Raloxifene plus letrozole in breast cancer cell lines, aimed at bone adverse effects |
| [19250202](https://pubmed.ncbi.nlm.nih.gov/19250202/) | 2009 | Preclinical | Ann N Y Acad Sci | Letrozole sustained growth inhibition longer than tamoxifen in an intratumoral aromatase model |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0281 | Letrozole | Not stated | Not stated (status: valid) |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted endocrine therapy (nonsteroidal aromatase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Low; please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Low; please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function, bilirubin, bone density; blood count when combined with CDK4/6 inhibitors |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Conditions flagged in the knowledge graph (not label text)**: The TxGNN knowledge graph links letrozole with liver failure, cirrhosis of liver, osteoporosis (including postmenopausal osteoporosis), hyperbilirubinaemia (including hereditary forms and Gilbert syndrome), and cerebrovascular disorder. These come from drug-disease contraindication edges and need confirmation against the package insert.
- **Drug Interactions**: The interaction screen returned 100 interacting drugs. Most are of unclassified severity. The only one rated moderate is aprepitant. Others listed include calcitriol, glimepiride, the proton pump inhibitors lansoprazole, omeprazole and pantoprazole, famotidine, metformin, simvastatin, prednisone, morphine and acetylsalicylic acid.
- **Bone health**: Aromatase inhibition lowers estrogen. One preclinical study explored raloxifene to counter bony adverse effects, and a phase 2 trial studied zoledronic acid for aromatase inhibitor-associated musculoskeletal symptoms (NCT01194440).

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Multiple completed Phase 3 RCTs (MONALEESA-2, PALOMA-2, COMPLEEMENT-1) support letrozole as the endocrine backbone in HR+ breast cancer, so evidence for female breast carcinoma is L1.
- The use is an established standard of care rather than a novel repurposing. The Philippines registration is cancelled, with no indication text recorded, so the regulatory status must be clarified before any local use.

**To proceed, the following is needed:**
- Confirm why the Philippines registration PNF-0281 was cancelled, and whether a valid registration exists or must be filed
- Obtain the package insert, with its warnings and contraindications, from the Philippines FDA
- Obtain formal mechanism of action data from DrugBank
- Set up a safety monitoring plan covering liver function, bone density and cardiovascular or cerebrovascular risk
- Limit use to HR+ disease, as there is no supporting evidence in ER-negative disease, nipple carcinoma, benign breast conditions or the Ehrlich tumour model
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

