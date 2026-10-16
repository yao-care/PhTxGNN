---
layout: default
title: Chloroquine
parent: Model Prediction Only (L5)
nav_order: 73
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Chloroquine: predicted new indication Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis (evidence level L5). Approved use: Rheumatoid arthritis, systemic lupus erythematosus, mal…"
monitor_inn: "Chloroquine"
predicted_indications: ["rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "rheumatoid nodulosis", "juvenile chronic polyarthritis", "juvenile idiopathic arthritis"]
---

# Chloroquine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Chloroquine: From Rheumatoid Arthritis and Malaria to Rheumatoid Factor-Positive Polyarticular Juvenile Idiopathic Arthritis

## One-Sentence Summary

Chloroquine is an antimalarial and antirheumatic drug, originally used for malaria, rheumatoid arthritis and lupus erythematosus.
The TxGNN model predicts it may be effective for **rheumatoid factor-positive polyarticular juvenile idiopathic arthritis**,
but currently there are **0 registered clinical trials** and only **1 indirectly related publication** (a study of leflunomide, not chloroquine) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, systemic lupus erythematosus, malaria (per the knowledge graph; the Philippines registration has no indication text) |
| Predicted New Indication | Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, chloroquine is an established antimalarial and antirheumatic agent. Its efficacy in adult rheumatoid arthritis has been recognised, and mechanistically it may be applicable to RF-positive polyarticular JIA.

Its immunomodulatory effects (lysosomal and autophagy inhibition, reduced antigen presentation, reduced TLR signalling and cytokine production) could plausibly extend to this condition, which shares features with adult seropositive rheumatoid arthritis. The high TxGNN score probably reflects this closeness to the approved rheumatoid arthritis indication.

This is a plausibility argument only. No clinical evidence for chloroquine in this specific condition was found.

Other predictions in the same disease family:
- **Rheumatoid nodulosis** (99.33%): likely reflects network proximity to rheumatoid arthritis. No direct mechanism is supported, and the literature consists of case reports, mostly on methotrexate-induced nodulosis.
- **Juvenile chronic polyarthritis** (99.32%): an older term for JIA. Antimalarials were historically used as slow-acting antirheumatic drugs in children, but the literature is old, and one report describes third-degree atrioventricular block under chloroquine.
- **Juvenile idiopathic arthritis** (99.22%): has the largest body of literature (20 records), but most concerns other drugs, historical descriptions, or hydroxychloroquine in other conditions.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top prediction (RF-positive polyarticular JIA):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24334641](https://pubmed.ncbi.nlm.nih.gov/24334641/) | 2014 | Prospective cohort | J Rheumatol | Long-term real-life experience with leflunomide in JIA. It does not study chloroquine, so it offers only indirect context. |

For the broader juvenile arthritis predictions, the most relevant publications are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18021335](https://pubmed.ncbi.nlm.nih.gov/18021335/) | 2007 | Pharmacokinetic study | J Clin Pharm Ther | Compared methotrexate pharmacokinetics in JIA patients on methotrexate alone versus methotrexate plus chloroquine. |
| [2047820](https://pubmed.ncbi.nlm.nih.gov/2047820/) | 1991 | Review | Schweiz Med Wochenschr | Therapeutic strategy in 119 patients with juvenile chronic arthritis. Chloroquine is discussed among the disease-modifying drugs. |
| [7409700](https://pubmed.ncbi.nlm.nih.gov/7409700/) | 1980 | Review | Fortschr Med | Historical review of drug therapy in juvenile chronic polyarthritis, covering the effects and side effects of gold, D-penicillamine, chloroquine and azathioprine. |
| [4608161](https://pubmed.ncbi.nlm.nih.gov/4608161/) | 1974 | Clinical study | Scand J Rheumatol | Dosage of chloroquine and hydroxychloroquine in children with juvenile rheumatoid arthritis and lupus, guided by serum concentrations. |
| [9523387](https://pubmed.ncbi.nlm.nih.gov/9523387/) | 1998 | Case report | Rev Rhum (Engl Ed) | Third-degree atrioventricular block under chloroquine therapy in a woman with juvenile-onset arthritis (safety signal). |
| [1450810](https://pubmed.ncbi.nlm.nih.gov/1450810/) | 1992 | Case report | Br J Rheumatol | Chloroquine-induced vitiligo in a patient with juvenile-onset rheumatoid arthritis (safety signal). |

None of these is a controlled trial of chloroquine in JIA.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0096 | Chloroquine | Not specified | Not specified (status: cancelled) |

## Safety Considerations

No package insert warnings or contraindications were available for this report. The following is based on the drug-disease contraindication links in the knowledge graph, not on label text:

- **Contraindication-related conditions (knowledge graph)**:
  - Eye and hearing: eye disease, retinal disease, retinitis, vision disorder, blindness, scotoma, hearing disorder
  - Blood: neutropenia, agranulocytosis, leukopenia, anaemia, G6PD deficiency
  - Metabolic: porphyria, glycogen storage disease, cystinuria, galactosemia
  - Organ and other: epilepsy, liver disease, gallbladder disease, psoriasis, substance abuse/dependence
- **Safety signals in the literature**: a case of third-degree atrioventricular block and a case of vitiligo during chloroquine therapy in patients with juvenile arthritis.
- **Drug interactions**: 100 interactions were identified. Major-level interactions include:
  - Agalsidase beta
  - Bupropion
  - Cisapride
  - Clarithromycin
  - Dolasetron
  - Granisetron

  Moderate-level interactions include:
  - Antidiabetic drugs (glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide, human insulin)
  - Famotidine and cimetidine
  - Antacids (aluminium hydroxide, calcium carbonate, attapulgite)
  - Loperamide, aprepitant and metronidazole

Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but it rests on model proximity to adult rheumatoid arthritis, with no registered trials and no direct chloroquine efficacy data in JIA (evidence level L5 for this top prediction). Chloroquine's registration in the Philippines is cancelled, and hydroxychloroquine and biologics are currently preferred, which further limits practical development.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the DOH-FDA Philippines (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A systematic review of antimalarial (chloroquine and hydroxychloroquine) use in JIA, with attention to paediatric dosing and ocular and cardiac safety
- A comparison with hydroxychloroquine as a potentially more suitable route
- Clarification of the regulatory pathway, given that the only registration is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

