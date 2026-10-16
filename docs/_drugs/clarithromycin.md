---
layout: default
title: Clarithromycin
parent: Model Prediction Only (L5)
nav_order: 76
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Clarithromycin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Bacterial infections (infectious otitis media, bacterial pneumonia…"
---

# Clarithromycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Clarithromycin: From Respiratory and Soft-Tissue Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Clarithromycin is a macrolide antibiotic, originally used to treat bacterial infections such as pneumonia, sinusitis, otitis media, and streptococcal and staphylococcal infections.
The TxGNN model predicts it may be effective for **Hyperamylasemia**, but there are **0 clinical trials** and only **1 publication** (a case report with no therapeutic link), so the prediction rests almost entirely on the computational model.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (infectious otitis media, bacterial pneumonia, streptococcal and staphylococcal infections, maxillary sinusitis, Mycoplasma and Chlamydia pneumonia) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 (model prediction with no supporting studies; the single case report is not therapeutic evidence) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, clarithromycin is a macrolide antibiotic whose efficacy in bacterial respiratory infections is established, but no mechanistic route to hyperamylasemia has been identified.

The only publication found is a 2004 Japanese case report of *Mycobacterium abscessus* lung infection complicated by primary macroamylasemia. Clarithromycin was most likely used there as an anti-mycobacterial agent. Any link to elevated amylase is incidental and does not show therapeutic benefit. The high TxGNN score is therefore a computational signal only and should not be read as clinical support.

Other predictions for this drug (polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility) also lack trials and literature. The one comparatively plausible candidate is punctate epithelial keratoconjunctivitis. Macrolides have anti-inflammatory effects on the meibomian glands, and a 2024 observational study supports this indirectly. It is a research question, not a validated indication.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15228140](https://pubmed.ncbi.nlm.nih.gov/15228140/) | 2004 | Case report | Nihon Kokyuki Gakkai Zasshi | A 76-year-old man with *M. abscessus* lung infection and primary macroamylasemia; no demonstrated therapeutic effect on amylase |

Currently no related clinical trials are registered.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0104 | Clarithromycin | Not specified | Not specified (status: cancelled) |

The only registration found has been cancelled, so no valid single-ingredient or combination product is currently registered.

## Safety Considerations

- **Contraindications and risk conditions (from the knowledge graph, not label text)**:
  - Cardiac: long QT syndrome, torsades de pointes, ventricular tachycardia (including catecholaminergic polymorphic and incessant infant forms)
  - Hepatic: liver failure, liver disease, cholestasis (including benign recurrent and familial intrahepatic forms), gallbladder disease
  - Metabolic: porphyria (inherited and other porphyrin metabolism diseases)
  - Others: kidney disease, myasthenia gravis and other neuromuscular junction diseases, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, osteoporosis, bone fracture, infectious mononucleosis, chronic Epstein-Barr virus infection syndrome
- **Drug Interactions**: The interaction query returned 100 records; the first 20 reviewed include:
  - Major: abemaciclib, fentanyl, acalabrutinib
  - Moderate: paclitaxel, tramadol, nifedipine, famotidine, formoterol, ethinylestradiol, hydrocortisone, afatinib, abiraterone, among others
  - Minor: dolutegravir, zidovudine, loratadine

  Clarithromycin is a strong CYP3A4 inhibitor, so interactions with CYP3A4 substrates deserve particular attention.

Please refer to the package insert for key warnings and the official contraindication list.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. No clinical trials exist, and the only publication is an incidental case report with no therapeutic link. The only Philippines registration is cancelled, and the safety profile (QT prolongation, hepatic risk, many CYP3A4 interactions) calls for caution.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible mechanistic link between clarithromycin and amylase or pancreatic pathology
- Confirmation of whether the amylase finding in the case report was an adverse event or a coincidence
- Package insert warnings and contraindications from the DOH-FDA Philippines, and clarification of the cancelled registration's status
- Preclinical or exploratory clinical data, if the indication is to be pursued
- Consider prioritising punctate epithelial keratoconjunctivitis as a research question, since its mechanistic rationale is stronger
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

