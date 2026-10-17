---
layout: default
title: Imatinib
parent: Moderate Evidence (L3-L4)
nav_order: 172
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Imatinib: predicted new indication Heart fibrosarcoma (evidence level L4). Approved use: Not stated in the Philippines registration record. The knowledge grap…"
monitor_inn: "Imatinib"
predicted_indications: ["heart fibrosarcoma", "fibroblastic neoplasm", "conventional fibrosarcoma", "kidney fibrosarcoma", "low grade fibromyxoid sarcoma", "liposarcoma", "liver fibrosarcoma", "autosomal recessive familial Mediterranean fever", "ovarian myxoid liposarcoma", "familial rhabdoid tumor"]
---

# Imatinib
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Imatinib: From Gastrointestinal Stromal Tumor and Leukaemia to Heart Fibrosarcoma

## One-Sentence Summary

Imatinib is a tyrosine kinase inhibitor originally used for chronic myeloid leukaemia, gastrointestinal stromal tumour (GIST), systemic mastocytosis, dermatofibrosarcoma protuberans and related conditions.
The TxGNN model's top-ranked prediction is **heart fibrosarcoma**, but this prediction has **no clinical trials** and only **1 publication** (a 2008 drug bulletin) behind it.
Among the top 10 predictions, the better-supported direction is **fibroblastic neoplasm** (mainly DFSP, already an original indication), and **liposarcoma** has the most trial activity (**3 completed Phase 1/2–2 trials**), though with weak mechanistic rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Philippines registration record. The knowledge graph lists CML, GIST, systemic mastocytosis, chronic eosinophilic leukaemia, dermatofibrosarcoma protuberans and hypereosinophilic syndrome |
| Predicted New Indication | Heart fibrosarcoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Cancelled only |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. From the literature, imatinib is a small-molecule inhibitor of the BCR-ABL, KIT and PDGFR tyrosine kinases. This explains its use in CML (BCR-ABL), GIST (KIT/PDGFRA) and DFSP (PDGFB-driven PDGFRB signalling).

For **heart fibrosarcoma**, the link is indirect. The only citation is a 2008 drug bulletin noting that imatinib's new indications were not supported by robust evidence. The plausible pathway runs through the COL1A1-PDGFB fusion seen in DFSP, but cardiac fibrosarcoma is not known to carry this fusion.

Other top-10 predictions differ in strength:

- **Fibroblastic neoplasm (rank 2):** dominated by DFSP, where imatinib is already an original indication. This is largely a restatement of an existing use, not true repurposing. Imatinib helps roughly half of patients with unresectable or metastatic DFSP, so response is not universal.
- **Liposarcoma (rank 6):** soft-tissue sarcoma trials include liposarcoma patients, but liposarcoma is typically driven by MDM2/CDK4 amplification rather than KIT or PDGFR mutations, so the rationale is weak.
- **Other predictions (ranks 3–5, 7–10):** the data show little or no direct support (see the Conclusion).

---

## Clinical Trial Evidence

Heart fibrosarcoma has no registered clinical trials. The trials below are the ones attached to other top-10 predictions and are shown for context only.

| Trial Number | Phase | Status | Enrollment | Key Findings | Linked Prediction |
|---------|------|------|------|---------|------|
| [NCT00031915](https://clinicaltrials.gov/study/NCT00031915) | Phase 2 | Completed | Not reported | Imatinib in metastatic or unresectable soft tissue and bone sarcomas; no subtype-specific results supplied | Liposarcoma |
| [NCT00154388](https://clinicaltrials.gov/study/NCT00154388) | Phase 2 | Completed | 185 | Exploratory basket study in life-threatening rare malignancies linked to imatinib-sensitive kinases; only indirect support | Liposarcoma, kidney fibrosarcoma |
| [NCT00006357](https://clinicaltrials.gov/study/NCT00006357) | Phase 1/2 | Completed | 91 | Dose-finding and efficacy study in recurrent or refractory soft tissue sarcoma; efficacy in liposarcoma not specified | Liposarcoma |

All three trials are non-randomized and none is specific to a single sarcoma subtype.

---

## Literature Evidence

**Heart fibrosarcoma (top-ranked prediction):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Review | Prescrire International | Drug bulletin on imatinib's expanded indications; concludes the evidence for the new indications was not robust |

**Selected evidence for related predictions:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39904126](https://pubmed.ncbi.nlm.nih.gov/39904126/) | 2025 | Guideline | Eur J Cancer | European interdisciplinary DFSP guideline (2024 update); discusses imatinib for unresectable or metastatic disease |
| [19451433](https://pubmed.ncbi.nlm.nih.gov/19451433/) | 2009 | Phase II trial | J Clin Oncol | Multicentre phase II trial of imatinib across 10 sarcoma subtypes using a Bayesian hierarchical model |
| [42062942](https://pubmed.ncbi.nlm.nih.gov/42062942/) | 2026 | Cohort | BMC Cancer | 153 Chinese DFSP patients; evaluates Mohs surgery with postoperative imatinib and COL1A1::PDGFB fusion prevalence |
| [25852058](https://pubmed.ncbi.nlm.nih.gov/25852058/) | 2015 | Preclinical | Mol Cancer Ther | CDKN2A/p16 loss implicates CDK4 as a target in imatinib-resistant DFSP |
| [40558511](https://pubmed.ncbi.nlm.nih.gov/40558511/) | 2025 | Preclinical | Cells | Patient-derived DFSP cell lines used to predict imatinib sensitivity; resistance emerges in 10–50% of cases |
| [30901500](https://pubmed.ncbi.nlm.nih.gov/30901500/) | 2019 | Preclinical | Drug Dev Res | Imatinib plus dexketoprofen in liposomes or nanocochleates against fibrosarcoma cells |
| [16158966](https://pubmed.ncbi.nlm.nih.gov/16158966/) | 2005 | Immunohistochemistry/genetic analysis | Anticancer Res | c-kit expression in dedifferentiated and well-differentiated liposarcomas |
| [12702540](https://pubmed.ncbi.nlm.nih.gov/12702540/) | 2003 | Report | Ann Oncol | Potential use of imatinib in c-KIT-expressing ocular melanoma and liposarcoma |
| [30096127](https://pubmed.ncbi.nlm.nih.gov/30096127/) | 2018 | Case report | Anticancer Drugs | Imatinib-induced DRESS in a DFSP patient, managed with desensitization (a safety signal) |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0243 | Imatinib | Not stated | Not stated (status: cancelled) |

The only registration is cancelled, so no valid imatinib product is currently registered in the Philippines according to the data compiled for this report.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. The knowledge graph lists neutropenia, thrombocytopenia, agranulocytosis and anaemia as contraindication-related conditions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC, liver function, renal function, fluid status and cardiac status (based on the contraindication-related conditions below) |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

No package insert warnings or contraindications are available in the data compiled for this report. The following come from the knowledge graph and are not label text:

- **Knowledge-graph contraindication-related conditions:** liver failure and liver disease; kidney disease; congestive heart failure, heart failure, heart valve disease, coronary artery disease, congenital heart disease, pericardial effusion and hemopericardium; pulmonary edema and brain edema; hypertension; thrombocytopenia, neutropenia, agranulocytosis and anaemia; diabetes mellitus and diabetic ketoacidosis; hyperbilirubinemia and Gilbert syndrome; active peptic ulcer disease; gallbladder disease; hypophosphatemia; obesity disorders.
- **Drug interactions:** 100 interactions were found. The first 20 retrieved include two **Major** interactions, with **eliglustat** and **naloxegol**. Moderate interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), clarithromycin, cimetidine, aprepitant, morphine, naltrexone, naldemedine, proton pump inhibitors (lansoprazole, dexlansoprazole), and antidiabetic agents (pioglitazone, glimepiride, saxagliptin).
- **Case report signal:** imatinib-induced DRESS (drug reaction with eosinophilia and systemic symptoms) has been reported, including in a DFSP patient.

For authoritative safety information, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction, heart fibrosarcoma, has no trials and only one non-robust drug bulletin, giving an L4 evidence level. The mechanism is unestablished, since a PDGFB fusion driver is not known in cardiac fibrosarcoma.
- Among the top 10, only fibroblastic neoplasm (DFSP-dominated, L3, Proceed with Guardrails) has meaningful support, but DFSP is already an approved use. Liposarcoma has L2 trial activity but weak mechanistic rationale, so it is best treated as a research question. Ranks 3, 4 and 7 are L4 (indirect or off-target evidence), and ranks 5 and 8–10 are L5 (prediction only).
- The only Philippines registration is cancelled, which adds a regulatory hurdle.

**To proceed, the following is needed:**
- Mechanism-of-action data for imatinib from DrugBank
- Package insert warnings and contraindications from DOH-FDA Philippines (a blocking gap for safety screening)
- Tumour-specific evidence (case series, molecular profiling for PDGFB fusions, KIT or PDGFR alterations) for heart fibrosarcoma
- Subtype-specific results from NCT00031915, NCT00006357 and NCT00154388 for sarcoma subtypes
- A decision on the registration status of imatinib in the Philippines, including whether a currently valid product exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

