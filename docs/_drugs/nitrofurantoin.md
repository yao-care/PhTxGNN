---
layout: default
title: Nitrofurantoin
parent: Model Prediction Only (L5)
nav_order: 253
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Nitrofurantoin: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not stated in the registration record"
monitor_inn: "Nitrofurantoin"
predicted_indications: ["rheumatoid arthritis", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "diabetic nephropathy", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "sclerosing cholangitis", "methemoglobinemia, alpha type", "gout", "methemoglobinemia"]
---

# Nitrofurantoin
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

# Nitrofurantoin: From Urinary Tract Infection (Original Use Not Recorded in the Local Registry) to Rheumatoid Arthritis

## One-Sentence Summary

Nitrofurantoin is an antibacterial drug, but the Philippine registration record compiled for this report does not state its approved indication.
The TxGNN model predicts it may be effective for **rheumatoid arthritis** with a very high score, yet there are **0 clinical trials** and no publications showing a therapeutic benefit. The retrieved literature mainly describes adverse events, so the evidence is **model prediction only**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration record |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Nitrofurantoin is known as an antibacterial used for urinary tract infections, but the data compiled for this report do not record a mechanism or an approved indication, and no plausible anti-rheumatic mechanism is documented.

The TxGNN score is very high (0.999), but the literature does not support a therapeutic effect. The retrieved papers describe nitrofurantoin-associated pulmonary fibrosis, its interaction with methotrexate in patients with rheumatoid arthritis, and a study on antibiotic use and rheumatoid arthritis flares. These are safety signals, not evidence of benefit. The model association probably reflects co-occurrence of the drug and the disease in the literature, such as lung disease or infections in people with rheumatoid arthritis, rather than a true treatment effect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Cohort (self-controlled case series) | Scientific Reports | Studied the association between antibiotic use and flares in a newly diagnosed rheumatoid arthritis cohort (n = 31,992); examines flare risk, not treatment benefit |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case report | Cureus | A 94-year-old woman on long-term methotrexate developed irreversible pulmonary fibrosis after nitrofurantoin for urinary infections |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Medical Journal | Drug-induced pulmonary fibrosis; lists nitrofurantoin as a cause and rheumatoid arthritis as a predisposing disease |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du Praticien | Drug-induced interstitial lung disease; nitrofurantoin named among implicated antibiotics |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | Poor prognosis in rheumatoid arthritis patients hospitalised for interstitial lung fibrosis; not specific to nitrofurantoin |

None of these studies shows that nitrofurantoin treats rheumatoid arthritis.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0350 | Nitrofurantoin | Not recorded | Not recorded (status: cancelled) |

## Safety Considerations

- **Disease-related cautions (from the TxGNN knowledge graph, not label text)**: the knowledge graph links nitrofurantoin to contraindication relationships with many conditions, including:
  - Renal: impaired renal function, anuria
  - Hepatic: drug-induced liver injury, hepatitis, obstructive jaundice, biliary tract disease
  - Pulmonary: interstitial lung disease, pulmonary fibrosis
  - Neurological: peripheral neuropathy, optic neuritis
  - Metabolic and nutritional: G6PD deficiency, diabetes mellitus, diabetic ketoacidosis, vitamin B deficiency, vitamin B12 deficiency
  - Gastrointestinal: *Clostridium difficile* colitis
- **Drug Interactions**: the interaction query returned 100 records; the main ones listed are:
  - Moderate: metronidazole, balsalazide, picosulfuric acid, naltrexone, rosuvastatin, simvastatin
  - Minor: anticholinergics (atropine, hyoscyamine, scopolamine, dicyclomine and similar) and magnesium-containing antacids
- **Relevance to the predicted indication**: the literature reports pulmonary fibrosis, including a case with methotrexate, which is commonly used in rheumatoid arthritis. This is a notable concern for this population.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The score is high, but there are no clinical trials and no literature showing benefit. The available evidence points to harm (pulmonary toxicity, methotrexate interaction), and there is no plausible mechanism.
- The only Philippine registration is cancelled, with no recorded indication.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible anti-rheumatic rationale
- Package insert warnings and contraindications from the Philippine regulator
- Preclinical or clinical studies showing benefit in rheumatoid arthritis
- A pulmonary and hepatic safety assessment for patients on methotrexate or other disease-modifying drugs
- Clarification of the registration status and approved indication of the cancelled license
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

