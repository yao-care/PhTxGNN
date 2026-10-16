---
layout: default
title: Clofazimine
parent: Model Prediction Only (L5)
nav_order: 79
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Clofazimine: predicted new indication Pneumocystosis (evidence level L5). Approved use: Leprosy, multibacillary leprosy, pyoderma gangrenosum"
monitor_inn: "Clofazimine"
predicted_indications: ["pneumocystosis", "malaria", "gastrin secretion abnormality"]
---

# Clofazimine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Clofazimine: From Leprosy to Pneumocystosis

## One-Sentence Summary

Clofazimine is an antimycobacterial drug originally used for leprosy (including multibacillary leprosy) and pyoderma gangrenosum.
The TxGNN model predicts it may be effective for **pneumocystosis**,
but there are **0 clinical trials** and only **3 publications** (none directly showing benefit against Pneumocystis), so the prediction rests almost entirely on the model.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Leprosy, multibacillary leprosy, pyoderma gangrenosum (from the knowledge graph; no approved indication text is available for the local registration) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (registration no longer valid) |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on general knowledge, clofazimine is a riminophenazine antimycobacterial with immunomodulatory and membrane-disrupting properties. It has an established role in leprosy and is also used in drug-resistant tuberculosis regimens.

The link to pneumocystosis is weak. Pneumocystis is a fungus, and nothing in the data compiled for this report shows clofazimine activity against it. The very high TxGNN score (0.999) is a graph-based prediction only. The literature that mentions both clofazimine and Pneumocystis involves AIDS patients who were at risk of or had Pneumocystis pneumonia, but clofazimine was given for mycobacterial infections, not for Pneumocystis.

Other candidate predictions for this drug (malaria and gastrin secretion abnormality) are similarly weak. Malaria has only in vitro evidence on clofazimine analogues, and gastrin secretion abnormality has no supporting data at all.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8501340](https://pubmed.ncbi.nlm.nih.gov/8501340/) | 1993 | Randomized open-label trial | J Infect Dis | Clofazimine as prophylaxis for disseminated *M. avium* complex in 110 HIV patients (prior Pneumocystis pneumonia or CD4 ≤100); the study concerned MAC, not Pneumocystis |
| [2714863](https://pubmed.ncbi.nlm.nih.gov/2714863/) | 1989 | Case report | Infection | AIDS patient with *M. kansasii* lung disease complicated by Pneumocystis pneumonia; recovered on a regimen that included clofazimine, with trimethoprim-sulfamethoxazole added for Pneumocystis |
| [11363899](https://pubmed.ncbi.nlm.nih.gov/11363899/) | 1996 | Review | PI Perspective | General update on opportunistic infections; no abstract available |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0107 | Clofazimine | Not specified | Not specified (status: cancelled) |

---

## Safety Considerations

- **Contraindications (knowledge graph associations, not label text)**: liver disease, gallbladder disease, diarrheal disease, active peptic ulcer disease, digestive system disease, intestinal disease, splenic infarction, splenic disease, hypersplenism.
- **Drug Interactions**: 100 interactions were identified; the main ones listed here are from the first 20 reviewed.
  - **Major**: cisapride, dolasetron
  - **Moderate**: famotidine, loperamide, bisacodyl, clarithromycin, levofloxacin, granisetron, ondansetron, palonosetron, and several laxatives (picosulfuric acid, polyethylene glycol, castor oil, glycerin, lactitol, lactulose, magnesium citrate, magnesium hydroxide, mineral oil)
  - **Minor**: metronidazole

  The major interactions involve other drugs that can affect heart rhythm, so QT-related risk deserves attention.

Package insert warnings were not available; please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5). No clinical trials exist, and the available literature does not show clofazimine acting against Pneumocystis. There is also no credible mechanistic link, and the only local registration has been cancelled.

**To proceed, the following is needed:**
- Mechanism of action data for clofazimine, and evidence of any activity against Pneumocystis (in vitro or animal studies)
- Package insert warnings and contraindications from the Philippines FDA
- Clarification of the cancelled registration status and available dosage forms
- Review of the QT-related interaction risk and the gastrointestinal and hepatic contraindications before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

