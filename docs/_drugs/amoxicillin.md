---
layout: default
title: Amoxicillin
parent: Model Prediction Only (L5)
nav_order: 26
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Amoxicillin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Urinary tract infection, infectious otitis media…"
---

# Amoxicillin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Amoxicillin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Amoxicillin is a beta-lactam antibiotic, originally used to treat bacterial infections such as urinary tract infection, otitis media, pneumonia and pharyngitis.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
The score comes from a graph-based computation only, with no actual studies behind it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, infectious otitis media, streptococcal infection, bacterial pneumonia, staphylococcal infection, pharyngitis (the local registration record has no indication text, so this is taken from the knowledge-graph indication list) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Amoxicillin is known to be a beta-lactam antibacterial that inhibits bacterial cell wall synthesis, and its efficacy in common bacterial infections is well established.

Polyclonal hyperviscosity syndrome, however, is driven by elevated serum immunoglobulins, not by a bacterial pathogen. No plausible mechanistic link to amoxicillin could be identified. The high score (99.63%, rank 3006) most likely reflects patterns in the knowledge graph rather than a real pharmacological relationship. The same is true of the other top-ranked predictions, such as hyperamylasemia and congenital analbuminemia, which also have no supporting studies.

### Other Predicted Indications Reviewed

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Hyperamylasemia | 99.63% | L5 | No mechanistic link, no studies |
| 3 | Congenital analbuminemia | 99.59% | L5 | No plausible mechanism, likely a network artifact |
| 4 | Blood group incompatibility | 99.40% | L4 | One case report of an infection complicating transplantation, indirect only |
| 5 | Premalignant hematological system disease | 99.29% | L5 | No mechanism, no studies |
| 6 | Monoclonal gammopathy | 99.22% | L4 | Indirect evidence only (infections in immunocompromised patients) |
| 7 | Hematological disease associated with an acquired peripheral neuropathy | 99.14% | L5 | No mechanism, no studies |
| 8 | Septicemic plague | 99.13% | L4 | Biologically plausible, but only laboratory and animal data; flagged as a research question |

Septicemic plague is the only one of these with a plausible link, because *Yersinia pestis* is a Gram-negative bacterium. Even so, beta-lactams are not first-line agents for plague, and guideline-preferred drugs (aminoglycosides, fluoroquinolones, tetracyclines) have stronger support.

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top predicted indication, polyclonal hyperviscosity syndrome.

For reference, one trial was found for a lower-ranked prediction (monoclonal gammopathy), and it does not support repurposing:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00062231](https://clinicaltrials.gov/study/NCT00062231) | Not applicable | Terminated | 351 | Compared moxifloxacin alone with ciprofloxacin plus amoxicillin/clavulanic acid for fever in low-risk neutropenic cancer patients. The population and indication differ from monoclonal gammopathy. |

## Literature Evidence

Currently no related literature is available for polyclonal hyperviscosity syndrome.

The most relevant publications found for the lower-ranked prediction, septicemic plague, are listed below. They are mostly laboratory or animal studies:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8203841](https://pubmed.ncbi.nlm.nih.gov/8203841/) | 1994 | Animal study | Antimicrob Agents Chemother | Amoxicillin was active in vitro against *Yersinia pestis* and was tested alongside other antibiotics in a mouse model of systemic infection |
| [21628541](https://pubmed.ncbi.nlm.nih.gov/21628541/) | 2011 | In vitro | Antimicrob Agents Chemother | Compared antibiotics commonly used for human plague against intracellular *Y. pestis* |
| [3957763](https://pubmed.ncbi.nlm.nih.gov/3957763/) | 1986 | Case report | J Am Vet Med Assoc | A cat with bubonic plague was treated successfully with amoxicillin plus streptomycin |
| [30563467](https://pubmed.ncbi.nlm.nih.gov/30563467/) | 2018 | In vitro | BMC Microbiol | Rapid susceptibility testing and beta-lactam-induced cell shape changes in threat pathogens including *Y. pestis* |
| [35619805](https://pubmed.ncbi.nlm.nih.gov/35619805/) | 2022 | Case report | Front Public Health | Disseminated nocardiosis in a patient with macroglobulinemia; an infection in an immunocompromised host, not treatment of the underlying disease |
| [40350274](https://pubmed.ncbi.nlm.nih.gov/40350274/) | 2025 | Case report | Rinsho Ketsueki | *Campylobacter lari* bacteremia during treatment of pure red cell aplasia after ABO-mismatched transplantation; indirect evidence only |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0018 | Amoxicillin | Not specified | Not specified (status: cancelled) |

This is the only registration on record, and it is cancelled. No currently valid single-ingredient or combination registration was found.

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these are graph associations, not package insert text): long QT syndrome, torsades de pointes, ventricular tachycardia, liver failure, liver disease, cholestasis, porphyria, kidney disease, *Clostridium difficile* colitis, myasthenia gravis, osteoporosis, bone fracture, infectious mononucleosis, and others.
- **Drug Interactions** (100 interactions recorded; examples shown):
  - **Major**: Methotrexate; live cholera vaccine (*Vibrio cholerae* CVD 103-HgR)
  - **Moderate**: Doxycycline, minocycline, demeclocycline, ethinylestradiol, estradiol, anisindione, dicoumarol, mycophenolate mofetil, entecavir, balsalazide, and live probiotic products
  - **Minor**: Allopurinol, amiloride, azithromycin, clarithromycin, erythromycin

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predicted indication, polyclonal hyperviscosity syndrome, has no clinical trials, no publications and no plausible mechanism, so the high score is not enough to justify action. Amoxicillin also has no currently valid registration in the Philippines.

**To proceed, the following is needed:**
- Detailed mechanism of action data, and a credible mechanistic rationale for the predicted indication
- Any preclinical or clinical evidence in polyclonal hyperviscosity syndrome
- The package insert (warnings and contraindications) for safety screening
- Clarification of the cancelled registration status if local supply is considered
- If a lead is wanted, septicemic plague is the only prediction with a plausible link. It should be treated as a research question, and would need comparison against guideline-preferred agents.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

