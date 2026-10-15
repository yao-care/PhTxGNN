---
layout: default
title: Mesalazine
parent: Model Prediction Only (L5)
nav_order: 225
evidence_level: L5
indication_count: 7
---

# Mesalazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Mesalazine: From Ulcerative Colitis to Rheumatoid Arthritis

## One-Sentence Summary

Mesalazine (5-aminosalicylic acid) was originally used to treat ulcerative colitis and other inflammatory bowel conditions.
The TxGNN model's top-ranked prediction is a rare genetic disorder, **congenital hypotrichosis with juvenile macular dystrophy**, which has no supporting evidence. The best-supported candidate is **rheumatoid arthritis** (rank 3), which has **0 clinical trials** and only indirect literature. This report covers the top prediction and the best-supported alternative.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ulcerative colitis, inflammatory bowel disease, ulcerative proctosigmoiditis (the Philippines licence record contains no approved indication text) |
| Predicted New Indication (top-ranked) | Congenital hypotrichosis with juvenile macular dystrophy |
| Best-Supported Alternative | Rheumatoid arthritis (rank 3) |
| TxGNN Prediction Score | 99.65% (top-ranked); 99.57% (rheumatoid arthritis) |
| Evidence Level | L5 (top-ranked); L4 (rheumatoid arthritis) |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Mesalazine is generally understood to be an anti-inflammatory agent acting locally in the gut, with effects on prostaglandin and leukotriene synthesis, NF-kB signalling and antioxidant activity. These actions are the basis of its effectiveness in ulcerative colitis.

**Top-ranked prediction (congenital hypotrichosis with juvenile macular dystrophy):** No plausible mechanistic link was found. This is a rare genetic disorder caused by CDH3 (cadherin-3) mutation, affecting hair follicles and the retina. Anti-inflammatory activity has no relevance to this defect. The high score is a knowledge-graph output only.

**Rheumatoid arthritis:** Mesalazine is the active moiety released from sulfasalazine, an established disease-modifying antirheumatic drug. However, the antirheumatic effect of sulfasalazine is generally attributed to its sulfapyridine moiety rather than to mesalazine, so efficacy of mesalazine alone is not supported. The high score likely reflects the sulfasalazine relationship in the knowledge graph.

**Other predictions:** Osteoarthritis has a conceptually plausible link through low-grade synovial inflammation, but support is limited to one computational study. Osteoarthritis susceptibility, seborrheic keratosis, vulvar inverted follicular keratosis and pseudoachondroplasia have no identified mechanistic link and no evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the seven predicted indications.

---

## Literature Evidence

The table below covers rheumatoid arthritis, the best-supported alternative. None of these papers shows efficacy of mesalazine in rheumatoid arthritis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7588084](https://pubmed.ncbi.nlm.nih.gov/7588084/) | 1995 | Review | Drugs | Review of sulfasalazine as a DMARD in rheumatoid arthritis. Sulfasalazine splits into sulfapyridine and mesalazine, and which part is the active principle remains uncertain. |
| [7904547](https://pubmed.ncbi.nlm.nih.gov/7904547/) | 1993 | Review | Clin Pharmacokinet | Pharmacokinetics of slow-acting antirheumatic drugs, including sulfasalazine. Clinical effects are delayed by several months and response varies. |
| [7781502](https://pubmed.ncbi.nlm.nih.gov/7781502/) | 1995 | Review (drug monograph) | Dtsch Med Wochenschr | Drug monograph on mesalazine (no abstract available). |
| [12235076](https://pubmed.ncbi.nlm.nih.gov/12235076/) | 2002 | Pharmacovigilance review | Gut | Re-evaluation of serious adverse reactions to sulphasalazine and mesalazine from spontaneous reports. |
| [42565551](https://pubmed.ncbi.nlm.nih.gov/42565551/) | 2026 | Cohort | Rheumatology (Oxford) | Medication use and pregnancy outcomes in women with immune-mediated inflammatory diseases. |
| [41443863](https://pubmed.ncbi.nlm.nih.gov/41443863/) | 2026 | Case report | Intern Med | 5-ASA-induced colitis in a patient with rheumatoid arthritis. This is an adverse event report, not evidence of benefit. |
| [31830393](https://pubmed.ncbi.nlm.nih.gov/31830393/) | 2019 | Case report | G Ital Nefrol | DRESS syndrome with acute renal failure after sulfasalazine and mesalazine in a patient with rheumatoid arthritis. |

For osteoarthritis, the only linked paper is [PMID 38491514](https://pubmed.ncbi.nlm.nih.gov/38491514/) (2024, J Transl Med), a computational transcriptomic study identifying potential therapeutic targets. It is hypothesis-generating and offers no clinical evidence. The other five predictions have no related literature.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0312 | Mesalazine | Not recorded | Not recorded (status: cancelled) |

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** kidney disease, interstitial nephritis, lipoid nephrosis, pyoureter, liver disease, gallbladder disease, neutropenia, agranulocytosis, anaemia (including macrocytic anaemia) and pyloric stenosis.
- **Drug interactions:** 100 interactions were identified in total. Those listed here are examples from the first 20 returned, which includes one **Major** interaction with human botulinum neurotoxin A/B immune globulin and another **Major** with cidofovir.
  - Moderate interactions include NSAIDs (ketorolac, ibuprofen, celecoxib, bromfenac), nephrotoxic agents (acyclovir, amphotericin B and its formulations, amikacin, bacitracin, capreomycin, cisplatin), azathioprine, anisindione, and sulfonylureas (acetohexamide, chlorpropamide).
  - Many of these combinations raise concern about kidney toxicity.
- **Literature signals:** The retrieved reports describe hypersensitivity reactions to 5-ASA, including colitis and DRESS syndrome with acute renal failure.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction has no trials, no literature and no plausible mechanism, so the high TxGNN score is not supported by evidence.
- Rheumatoid arthritis, the best-supported alternative, rests only on indirect sulfasalazine-related literature, with no evidence that mesalazine alone is effective.
- Mesalazine currently has no valid registration in the Philippines (its only licence is cancelled).

**To proceed, the following is needed:**
- Package insert warnings and contraindications, to complete safety screening
- Mechanism of action data from DrugBank
- Direct clinical evidence (trials or well-designed studies) for any shortlisted indication, especially rheumatoid arthritis and osteoarthritis
- Clarification of regulatory status, since the only licence is cancelled
- Renal and haematological safety review, given the knowledge-graph flags and the interaction profile
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

