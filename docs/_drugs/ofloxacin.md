---
layout: default
title: Ofloxacin
parent: Model Prediction Only (L5)
nav_order: 261
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ofloxacin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Typhoid fever, salmonellosis, paratyphoid fever…"
monitor_inn: "Ofloxacin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder", "punctate epithelial keratoconjunctivitis"]
---

# Ofloxacin
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

# Ofloxacin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Ofloxacin is a fluoroquinolone antibiotic originally used for bacterial infections such as typhoid fever, urinary tract infection, bronchitis and bacterial pneumonia.
The TxGNN model's top-ranked prediction is **hyperamylasemia**, but there are **0 clinical trials** and **0 publications** supporting it, so this is a model-only prediction.
Among the other top-10 predictions, **septicemic plague** has the most supporting data (11 publications, all preclinical or in vitro).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Typhoid fever, salmonellosis, paratyphoid fever, urinary tract infection, bronchitis, bacterial pneumonia and other bacterial infections (the Philippines registration record has no indication text) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Ofloxacin is a fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV. Currently, detailed mechanism of action data is not available in the compiled data, but this is the well-known class mechanism.

For the top-ranked prediction, hyperamylasemia, there is **no plausible mechanistic link**. Ofloxacin has no known role in amylase regulation, so the high score appears to be a graph-based artifact. The same applies to most other top-10 predictions (polyclonal hyperviscosity syndrome, congenital analbuminemia, blood group incompatibility, premalignant and congenital haematological conditions, monoclonal gammopathy). Fluoroquinolones also carry a peripheral neuropathy warning, which argues against benefit in the predicted neuropathy-associated haematological disease.

Two lower-ranked predictions are more biologically sensible:
- **Septicemic plague (rank 8):** *Yersinia pestis* is highly susceptible to ofloxacin in vitro, and mouse and primate models suggest treatment and prophylaxis benefit. This is an extension of the antibacterial spectrum rather than true repurposing, and the evidence is entirely preclinical.
- **Punctate epithelial keratoconjunctivitis (rank 10):** Ophthalmic ofloxacin treats bacterial conjunctivitis and keratitis, but the only retrieved paper is a case report on an allergic vernal shield ulcer and does not show an ofloxacin-specific benefit. The ophthalmic route also differs from the systemic context.

## Clinical Trial Evidence

Currently no related clinical trials registered for hyperamylasemia, or for any of the top-10 predicted indications.

## Literature Evidence

No related literature is available for hyperamylasemia. The most relevant publications are for the plague prediction (rank 8), all preclinical or in vitro:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9517950](https://pubmed.ncbi.nlm.nih.gov/9517950/) | 1998 | Animal study | Antimicrob Agents Chemother | Mouse model of pneumonic plague used to compare antibiotic treatments |
| [16127904](https://pubmed.ncbi.nlm.nih.gov/16127904/) | 2002 | Animal study | Antibiot Khimioter | Ofloxacin (MIC 0.08 mg/L) was effective for prophylaxis and treatment of experimental plague in mice, and less effective against strains lacking fraction I and mouse toxin |
| [8203841](https://pubmed.ncbi.nlm.nih.gov/8203841/) | 1994 | Animal study | Antimicrob Agents Chemother | Ofloxacin was active in vitro and was compared with other antibiotics in a mouse model of systemic *Y. pestis* infection |
| [11871319](https://pubmed.ncbi.nlm.nih.gov/11871319/) | 2001 | Animal study | Antibiot Khimioter | Primate model of bubonic plague established to evaluate antibacterials |
| [10987101](https://pubmed.ncbi.nlm.nih.gov/10987101/) | 2000 | Animal study | Antibiot Khimioter | Ofloxacin and other fluoroquinolones interfered with post-vaccine immunity in mice, and combined emergency and specific prophylaxis was explored |
| [8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/) | 1995 | In vitro | Antimicrob Agents Chemother | Ceftriaxone and ciprofloxacin were most active against 78 *Y. pestis* strains, followed by ofloxacin and ampicillin |
| [8913481](https://pubmed.ncbi.nlm.nih.gov/8913481/) | 1996 | In vitro | Antimicrob Agents Chemother | Ofloxacin and levofloxacin were highly active against 100 human isolates (MIC90 < 0.03 µg/mL) |
| [18644132](https://pubmed.ncbi.nlm.nih.gov/18644132/) | 2008 | In vitro | BMC Microbiol | Screening for resistance determinants in *Y. pestis* |
| [13677133](https://pubmed.ncbi.nlm.nih.gov/13677133/) | 2003 | In vitro | Antibiot Khimioter | Formation of rifampicin- and quinolone-resistant plague mutants |
| [19121669](https://pubmed.ncbi.nlm.nih.gov/19121669/) | 2008 | In vitro | Trans R Soc Trop Med Hyg | High-level fluoroquinolone resistance in *Burkholderia pseudomallei* (a related organism, not plague) |

Other predictions have only incidental papers: PMID [22808724](https://pubmed.ncbi.nlm.nih.gov/22808724/) (streptococcal identification, unrelated to blood group incompatibility), PMID [11858365](https://pubmed.ncbi.nlm.nih.gov/11858365/) (a 2002 case report of *S. lugdunensis* discitis treated with ofloxacin in a myeloma patient, not evidence for monoclonal gammopathy), and PMID [16670489](https://pubmed.ncbi.nlm.nih.gov/16670489/) (a 2006 vernal shield ulcer case report).

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0357 | Ofloxacin | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Contraindications / cautions (from the knowledge graph, not label text):** long QT syndrome, torsades de pointes, liver failure and liver disease, drug-induced liver injury, epilepsy, kidney disease and impaired renal function, tendinitis and other tendon disorders, myasthenia gravis and neuromuscular junction disease, peripheral neuropathy, diabetes mellitus and diabetic ketoacidosis, rhabdomyolysis, *Clostridium difficile* colitis, thrombocytopenia, leukopenia, anaemia, and potassium deficiency.
- **Drug Interactions (100 recorded; examples):**
  - Major: hydrocortisone, dexamethasone, betamethasone, triamcinolone (corticosteroids, with tendon-related risk), bupropion, chlorpropamide
  - Moderate: antidiabetic drugs (metformin, pioglitazone, acarbose, alogliptin, canagliflozin, albiglutide), famotidine, loperamide, acetylsalicylic acid, balsalazide, bisacodyl, and calcium and potassium salts

Please also refer to the package insert for full safety information, which was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, hyperamylasemia, rests on a model score alone, with no trials, no literature and no mechanistic link. Ofloxacin's Philippines registration is cancelled, so no valid local product exists. Plague is the only biologically plausible prediction (L4, "Research Question"), but its evidence is preclinical, and other fluoroquinolones such as ciprofloxacin and levofloxacin are more practical candidates.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines
- Mechanism of action data from DrugBank
- For plague: human clinical data, and a comparison with currently registered fluoroquinolones
- For any indication: confirmation of whether a valid ofloxacin product (systemic or ophthalmic) is available in the Philippines
- De-prioritising the other predictions with no mechanistic link unless new evidence appears
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

