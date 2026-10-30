---
layout: default
title: Piperacillin
parent: Model Prediction Only (L5)
nav_order: 278
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-30
monitor_inn: "Piperacillin"
predicted_indications: ["rheumatoid arthritis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "sclerosing cholangitis", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "diabetic nephropathy", "WHIM syndrome"]
description: "Piperacillin: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not recorded in the local data"
---

# Piperacillin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Piperacillin: Rheumatoid arthritis
{: .text-alpha }

## One-Sentence Summary

Piperacillin is a beta-lactam antibiotic that inhibits bacterial cell wall synthesis. The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are **0 clinical trials** and **15 publications** (all case reports, reviews or cohort studies of infections or adverse events in RA patients, none showing treatment of RA itself). The prediction is a model output only and has no clinical support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Piperacillin is a beta-lactam antibiotic, which acts by inhibiting bacterial cell wall synthesis, and it is used against bacterial infections.

A plausible mechanistic link to rheumatoid arthritis could not be identified. Rheumatoid arthritis is an autoimmune disease, and piperacillin has no known immunomodulatory activity relevant to it. The retrieved publications describe piperacillin or related antibiotics being used for infections in RA patients (for example septic shock, prosthetic joint infection and pericarditis), or describe adverse events of other RA drugs such as methotrexate pancytopenia. These reflect antibiotic use in people who happen to have RA, not treatment of RA.

The high TxGNN score (0.9994) should therefore be read as a model-based signal only. It is not supported by clinical or mechanistic evidence.

Other predicted indications were also reviewed (colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome, sclerosing cholangitis, osteoarthritis susceptibility, diabetic nephropathy, WHIM syndrome and others). All are Evidence Level L5, with no plausible mechanistic link and no supporting trials.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these publications tests piperacillin as a treatment for rheumatoid arthritis. The ten most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33987340](https://pubmed.ncbi.nlm.nih.gov/33987340/) | 2021 | Cohort | Ann Transl Med | Prevalence and clinical features of antibiotic-associated drug-induced liver injury |
| [41257433](https://pubmed.ncbi.nlm.nih.gov/41257433/) | 2026 | Cohort (predictive model) | Br J Clin Pharmacol | Predictive risk model for eosinophilia in patients treated with ampicillin/sulbactam or piperacillin/tazobactam |
| [38343452](https://pubmed.ncbi.nlm.nih.gov/38343452/) | 2024 | Case report | Proc (Bayl Univ Med Cent) | Low-dose methotrexate toxicity with pancytopenia in an RA patient, treated with leucovorin rescue |
| [34178513](https://pubmed.ncbi.nlm.nih.gov/34178513/) | 2021 | Case report | Cureus | Pancytopenia from low-dose methotrexate in RA |
| [37599303](https://pubmed.ncbi.nlm.nih.gov/37599303/) | 2023 | Case report | Orthopadie (Heidelberg) | Haemophilus influenzae prosthetic knee infection in an RA patient; piperacillin/tazobactam used for pneumonia |
| [41268563](https://pubmed.ncbi.nlm.nih.gov/41268563/) | 2025 | Case report | Front Immunol | Severe atypical bullous erysipelas caused by E. coli in an immunosuppressed RA patient |
| [40119266](https://pubmed.ncbi.nlm.nih.gov/40119266/) | 2025 | Case report/Review | BMC Infect Dis | Septic shock caused by drug-resistant Edwardsiella tarda |
| [36945293](https://pubmed.ncbi.nlm.nih.gov/36945293/) | 2023 | Case report | Cureus | Recurrent isolated pleural effusions in an RA patient in remission for nine years |
| [22605835](https://pubmed.ncbi.nlm.nih.gov/22605835/) | 2012 | Case report | BMJ Case Rep | Purulent pericarditis in an RA patient on etanercept; empirical piperacillin-tazobactam started |
| [1921823](https://pubmed.ncbi.nlm.nih.gov/1921823/) | 1991 | Case report | Med J Aust | Pancytopenia after accidental methotrexate overdose in RA |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0388 (cancelled) | Piperacillin | Not specified | Not specified |


---

## Safety Considerations

- **Drug Interactions**: 81 interactions were identified in the database query. The main ones by severity:
  - **Major**: Vancomycin
  - **Moderate**: Doxycycline, Tetracycline, Minocycline, Kanamycin, Streptomycin, Picosulfuric acid
  - **Minor**: Clarithromycin
  - Several others (for example pantoprazole, morphine, prednisone, simvastatin, omeprazole) have an unclassified severity level.
- **Other considerations**: Piperacillin is associated with drug-induced liver injury, and it requires renal dose adjustment, which matters in patients with kidney disease.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials, no literature showing efficacy in RA, and no plausible mechanistic link between a bacterial cell wall inhibitor and an autoimmune joint disease. The only Philippines registration has also been cancelled.

**To proceed, the following is needed:**
- Mechanistic evidence for a link between piperacillin and RA pathways (the MOA data are currently missing)
- Preclinical or clinical studies that directly test piperacillin for RA
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Clarification of the registration status and approved indications in the Philippines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

