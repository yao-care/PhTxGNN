---
layout: default
title: Nalidixic Acid
parent: Model Prediction Only (L5)
nav_order: 246
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-30
description: "Nalidixic Acid: predicted new indication Conjunctivitis (evidence level L4). Approved use: Not stated in the registration data (class use: bacterial infections)"
monitor_inn: "Nalidixic acid"
predicted_indications: ["conjunctivitis", "sclerosing cholangitis", "rheumatoid arthritis", "infectious otitis media"]
---

# Nalidixic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Nalidixic Acid: From Bacterial Infection to Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Nalidixic acid is a first-generation quinolone antibiotic. The Philippines registration data compiled for this report do not state an approved indication, so the original use is inferred from its drug class.
The TxGNN model predicts it may be effective for **conjunctivitis**, with **0 clinical trials** and **5 publications** retrieved. None of these publications evaluates nalidixic acid as a treatment for conjunctivitis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data (class use: bacterial infections) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 0.9983 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Nalidixic acid is a first-generation quinolone, a class known to inhibit bacterial DNA gyrase (topoisomerase II) and topoisomerase IV. This is general class knowledge, not data from the compiled records. Through this action, it could plausibly act against susceptible Gram-negative bacteria that cause bacterial conjunctivitis.

However, the link is weak. The retrieved literature concerns enteric pathogens (Shigella, Yersinia) and does not address eye infection. Later fluoroquinolones have much better ocular penetration and a broader spectrum, and widespread quinolone resistance reduces the rationale for nalidixic acid. The high TxGNN score is a computational prediction only.

Other predicted indications are weaker still:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Note |
|---|---|---|---|---|
| 2 | Sclerosing cholangitis | 0.9963 | L5 | No trials or literature. Any link through gut microbiota is speculative. |
| 3 | Rheumatoid arthritis | 0.9941 | L5 | The only article is an unrelated observational study of oral Staphylococcus colonization. |
| 4 | Infectious otitis media | 0.9904 | L5 | The only article studies ofloxacin, a different drug, so it is indirect class-level evidence. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17446289](https://pubmed.ncbi.nlm.nih.gov/17446289/) | 2007 | Microbiological characterization | J Med Microbiol | A novel Shigella dysenteriae serovar from patients with diarrhoea in Bangladesh. Not related to conjunctivitis. |
| [15824427](https://pubmed.ncbi.nlm.nih.gov/15824427/) | 2005 | Microbiological characterization | J Med Microbiol | Isolation of Shigella boydii provisional serovar E16553 from diarrhoeal patients. Not related to conjunctivitis. |
| [16914657](https://pubmed.ncbi.nlm.nih.gov/16914657/) | 2006 | Resistance survey | J Med Microbiol | Over 60% of Shigella sonnei isolates were resistant to nalidixic acid. This points to resistance limits. |
| [9442487](https://pubmed.ncbi.nlm.nih.gov/9442487/) | 1997 | Laboratory study | Microb Drug Resist | A 70-kb plasmid in epidemic Shigella dysenteriae type 1 and its role in drug resistance and virulence. |
| [3206956](https://pubmed.ncbi.nlm.nih.gov/3206956/) | 1988 | Laboratory study | Zh Mikrobiol Epidemiol Immunobiol | Invasiveness and cytotoxicity in Yersinia attenuation. Nalidixic acid-resistant mutants were used as laboratory tools. |

None of these articles tests nalidixic acid against conjunctivitis.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0338 | Nalidixic Acid (valid) | Not stated | Not stated |

---

## Safety Considerations

- **Disease associations from the knowledge graph (not label text)**: The TxGNN knowledge graph lists contraindication links with these conditions:
  - Neurological: epilepsy, peripheral neuropathy, peripheral nervous system disease, central nervous system disease, nervous system disorder, narcolepsy-cataplexy syndrome, Balo concentric sclerosis, X-linked adrenoleukodystrophy
  - Porphyrias: porphyria, inherited porphyria, porphyrin metabolism disease
  - Liver and gallbladder: liver disease, gallbladder disease
  - Tendon and joint: tendinitis, periarthritis, exostosis
  - Gastrointestinal: Clostridium difficile colitis, perinatal necrotizing enterocolitis
  - Metabolic: G6PD deficiency, glycogen storage disease, cystinuria, galactosemia
- **Drug Interactions**: The interaction query returned 100 records, and 20 are shown in the compiled data. **Major** interactions include:
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone
  - Bupropion
  - Chlorpropamide

  **Moderate** interactions include:
  - Antidiabetic agents: acarbose, alogliptin, saxagliptin, canagliflozin, dapagliflozin, albiglutide
  - Aspirin, balsalazide, alosetron
  - Calcium and citrate preparations
  - Polyethylene glycol electrolyte solution

Label-based warnings and contraindications from the package insert are not available. Please refer to the package insert for these.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction rests mainly on a computational score. No clinical trials exist, and none of the retrieved literature tests nalidixic acid for conjunctivitis.
- The drug's only Philippines registration is cancelled.
- Newer fluoroquinolones are better suited to eye infections, and quinolone resistance is widespread.
- The safety profile includes neurological and tendon-related concerns.

**To proceed, the following is needed:**
- Mechanism of action data confirmed from DrugBank
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Evidence of nalidixic acid activity against ocular pathogens, such as susceptibility data or ocular penetration studies
- A comparison with currently available ophthalmic fluoroquinolones to show any added value
- Clarification of the cancelled registration status and whether any formulation suitable for ophthalmic use exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

