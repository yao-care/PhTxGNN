---
layout: default
title: Capecitabine
parent: Model Prediction Only (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Capecitabine: predicted new indication Gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS) (evidence level L5). Approved use: Gastric cancer, metastasis from malignant tumour of colo"
monitor_inn: "Capecitabine"
predicted_indications: ["gastric adenocarcinoma and proximal polyposis of the stomach", "signet ring cell gastric adenocarcinoma", "gastric tubular adenocarcinoma", "gastric cardia adenocarcinoma"]
---

# Capecitabine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Capecitabine: From Gastric Cancer to Gastric Tubular Adenocarcinoma

## One-Sentence Summary

Capecitabine is an oral fluoropyrimidine chemotherapy originally used for gastric cancer and colon cancer metastases.
Of the ten new indications the TxGNN model predicts, this report focuses on the top-ranked one, **gastric adenocarcinoma and proximal polyposis of the stomach**, which has no supporting trials or publications. The best-supported prediction is **gastric tubular adenocarcinoma**, backed by **20 publications** (including multiple Phase 3 RCTs) but no registered clinical trial. This is essentially an on-label use under a histologic label rather than true repurposing.

> Note: The top-ranked prediction (rank 1) has no evidence. The sections below therefore present rank 1 in the overview and the best-supported predictions in the evidence sections.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric cancer, metastasis from malignant tumour of colon (approved indication text not available for the Philippines registration) |
| Predicted New Indication (rank 1) | Gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS) |
| Best-Supported Prediction | Gastric tubular adenocarcinoma (rank 3) |
| TxGNN Prediction Score | 99.94% (rank 1); 99.94% (rank 3) |
| Evidence Level | L5 (rank 1); L1 (rank 3, gastric tubular adenocarcinoma) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold (rank 1); Proceed with Guardrails (rank 3) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, capecitabine is an oral fluoropyrimidine antimetabolite that is converted in the body to 5-fluorouracil (5-FU), which inhibits thymidylate synthase and disrupts DNA synthesis. Its efficacy in gastric cancer is established, and it is mechanistically applicable to other gastric adenocarcinoma subtypes.

All ten predictions are histologic types or anatomical subsites of gastric cancer, so they relate closely to the original indication:

- **Gastric tubular adenocarcinoma** is the most common histology of gastric adenocarcinoma. Capecitabine-containing regimens (CAPOX/XELOX, for example) have been tested in Phase 3 trials in gastric cancer overall. The evidence applies to gastric cancer as a whole rather than specifically to tubular histology.
- **Gastric cardia adenocarcinoma** has two completed Phase 2 trials of capecitabine-based regimens.
- **Signet ring cell adenocarcinoma** is a gastric cancer subtype, but it is often considered less chemosensitive, which weakens the inference.
- **GAPPS (rank 1)** is a rare hereditary syndrome. Its adenocarcinoma component overlaps with gastric cancer, but nothing directly supports a capecitabine benefit.
- **Malignant gastric granular cell tumour (rank 10)** is a rare mesenchymal tumour that is biologically different from adenocarcinoma, so extrapolation is unsupported.

---

## Clinical Trial Evidence

No registered trials were found for the rank 1 prediction or for gastric tubular adenocarcinoma. The trials below relate to other predicted subtypes.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00040859](https://clinicaltrials.gov/study/NCT00040859) | Phase 2 | Completed | 48 | Oxaliplatin plus capecitabine in metastatic adenocarcinoma of the oesophagus, gastro-oesophageal junction and gastric cardia (cardia adenocarcinoma) |
| [NCT00938470](https://clinicaltrials.gov/study/NCT00938470) | Phase 2 | Completed | 73 | Randomised extended neoadjuvant therapy (docetaxel, oxaliplatin, capecitabine, fluorouracil and radiation) in locally advanced oesophageal, junction and cardia adenocarcinoma |
| [NCT01295086](https://clinicaltrials.gov/study/NCT01295086) | N/A | Completed | 27 | Dose-finding of docetaxel, oxaliplatin and capecitabine plus trastuzumab in HER2-positive non-resectable oesophageal, cardia or gastric cancer |
| [NCT02494583](https://clinicaltrials.gov/study/NCT02494583) | Phase 3 | Completed | 763 | Pembrolizumab with or without cisplatin plus 5-FU or capecitabine versus chemotherapy in advanced gastric/GEJ adenocarcinoma (gastric body carcinoma; not site-specific) |
| [NCT07091227](https://clinicaltrials.gov/study/NCT07091227) | Phase 2 | Not yet recruiting | 66 | AK112 plus chemotherapy as neoadjuvant treatment in signet ring cell-containing gastric/GEJ adenocarcinoma; capecitabine not confirmed |
| [NCT00021047](https://clinicaltrials.gov/study/NCT00021047) | Phase 1/2 | Completed | Not reported | Epirubicin, carboplatin and capecitabine in adult solid tumours (general safety data) |
| [NCT00010023](https://clinicaltrials.gov/study/NCT00010023) | Phase 1 | Completed | Not reported | Capecitabine plus cisplatin in advanced digestive system cancer (dose-finding) |

---

## Literature Evidence

The table lists the most relevant publications for gastric tubular adenocarcinoma (rank 3), the best-supported prediction, plus the key capecitabine-specific papers for other subtypes.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22226517](https://pubmed.ncbi.nlm.nih.gov/22226517/) | 2012 | RCT (Phase 3) | Lancet | CLASSIC: adjuvant capecitabine plus oxaliplatin after D2 gastrectomy in stage II-IIIB gastric cancer |
| [34252374](https://pubmed.ncbi.nlm.nih.gov/34252374/) | 2021 | RCT (Phase 3) | Lancet Oncol | RESOLVE: perioperative SOX versus postoperative CapOx in locally advanced gastric/GEJ cancer after D2 gastrectomy |
| [39952264](https://pubmed.ncbi.nlm.nih.gov/39952264/) | 2025 | RCT (Phase 3) | Lancet Oncol | RESOLVE final report with updated survival data |
| [30982686](https://pubmed.ncbi.nlm.nih.gov/30982686/) | 2019 | RCT (Phase 2/3) | Lancet | FLOT4: FLOT versus ECF/ECX perioperative chemotherapy in resectable gastric/GEJ adenocarcinoma |
| [37524953](https://pubmed.ncbi.nlm.nih.gov/37524953/) | 2023 | RCT (Phase 3) | Nat Med | GLOW: zolbetuximab plus CAPOX in CLDN18.2-positive gastric/GEJ adenocarcinoma |
| [37875143](https://pubmed.ncbi.nlm.nih.gov/37875143/) | 2023 | RCT (Phase 3) | Lancet Oncol | KEYNOTE-859: pembrolizumab plus chemotherapy in HER2-negative advanced gastric cancer |
| [34102137](https://pubmed.ncbi.nlm.nih.gov/34102137/) | 2021 | RCT (Phase 3) | Lancet | CheckMate 649: nivolumab plus chemotherapy in advanced gastric, GEJ and oesophageal adenocarcinoma |
| [29372626](https://pubmed.ncbi.nlm.nih.gov/29372626/) | 2018 | Phase 3 re-analysis | Asia Pac J Clin Oncol | Capecitabine/cisplatin versus 5-FU/cisplatin in Chinese patients with advanced gastric cancer (ML17032) |
| [16303863](https://pubmed.ncbi.nlm.nih.gov/16303863/) | 2006 | Phase 2 | Ann Oncol | Oxaliplatin plus capecitabine in metastatic oesophageal, junction and gastric cardia adenocarcinoma |
| [42026044](https://pubmed.ncbi.nlm.nih.gov/42026044/) | 2026 | Phase 2 | Nat Commun | Neoadjuvant toripalimab plus CapeOX in EBV-associated gastric/GEJ adenocarcinoma (17 patients) |

Most of these Phase 3 trials test regimens in gastric cancer overall, and several (such as the immunotherapy trials) mainly evaluate the added agent rather than capecitabine. CLASSIC and RESOLVE are the most directly relevant to capecitabine.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0071 | Capecitabine | Not specified | Not specified (registration cancelled) |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine antimetabolite, oral prodrug of 5-FU) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. The knowledge graph lists neutropenia, thrombocytopenia, agranulocytosis and anaemia among conditions of concern |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver function (bilirubin), renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

No package insert warnings or contraindications were available in the data compiled for this report.

- **Conditions of concern (from the drug-disease knowledge graph, not label text)**: liver disease, gallbladder disease, thrombocytopenia, infectious disease, neutropenia, agranulocytosis, coronary artery disease, anaemia (including macrocytic anaemia), hyperbilirubinaemia (including hereditary forms and Gilbert syndrome), impaired renal function, sudden cardiac arrest, heart conduction disease, necrotizing enterocolitis, stomatitis and **dihydropyrimidine dehydrogenase (DPD) deficiency**.
- **Drug Interactions**: 100 interactions were identified; the main ones listed are:
  - **Moderate**: metronidazole, tinidazole
  - **Minor**: aluminium hydroxide, levofloxacin, magaldrate, magnesium carbonate, magnesium hydroxide, magnesium oxide
  - Others, including pantoprazole, omeprazole, lansoprazole, metformin, glimepiride, simvastatin, morphine, prednisone, hydrocortisone, doxycycline, atropine and dolasetron, have an unclassified severity level.

Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold for the top-ranked prediction (GAPPS); Proceed with Guardrails for gastric tubular adenocarcinoma**

**Rationale:**
- The rank 1 prediction has a very high TxGNN score but no trials or literature (L5), and it is a rare hereditary syndrome with no direct evidence of capecitabine benefit, so it should be held.
- Gastric tubular adenocarcinoma has Phase 3 RCT support (L1), such as CLASSIC and RESOLVE, but that evidence applies to gastric cancer overall and is effectively on-label use. Gastric cardia adenocarcinoma has two completed Phase 2 trials (L2), and the other subtypes have weak or indirect evidence.
- The only Philippines registration (PNF-0071) is cancelled, so no valid local product is currently marketed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Philippines FDA (currently missing, and a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Confirmation that the Phase 3 evidence applies to the specific histologic subtype, with biomarker selection (HER2, CLDN18.2, PD-L1) where relevant
- A pre-treatment DPD deficiency testing and haematological monitoring plan
- Clarification of the regulatory pathway, since there is no active local registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

