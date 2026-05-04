---
layout: default
title: Capreomycin
parent: 僅模型預測 (L5)
nav_order: 56
evidence_level: L5
indication_count: 10
---

# Capreomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Capreomycin: From Tuberculosis to Gout

## One-Sentence Summary

Capreomycin is a cyclic polypeptide antibiotic used as a second-line agent for drug-resistant tuberculosis treatment, particularly in multi-drug resistant TB (MDR-TB) regimens.
The TxGNN model predicts it may be effective for **Gout**, with **0 clinical trials** and **0 publications** currently supporting this direction — placing the evidence at the lowest tier of confidence.
This prediction is considered a likely noise association rather than a genuine therapeutic opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Second-line anti-tuberculosis agent (MDR-TB / XDR-TB) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Capreomycin is a cyclic polypeptide antibiotic belonging to the tuberactinomycin family. Its established efficacy against *Mycobacterium tuberculosis* — particularly drug-resistant strains — has been proven in clinical practice, and it works by inhibiting bacterial ribosomal protein synthesis. However, this mechanism has no known relevance to gout pathophysiology.

Gout is fundamentally a disease of uric acid metabolism: hyperuricemia leads to monosodium urate crystal deposition in joints, triggering acute inflammatory arthritis. The two principal therapeutic targets are xanthine oxidase (reducing uric acid production) and renal urate transporters (enhancing uric acid excretion). Capreomycin has no known interaction with either pathway.

The most plausible explanation for this TxGNN prediction is a **reverse causal path within the knowledge graph**: Capreomycin is known to cause nephrotoxicity → renal impairment reduces uric acid clearance → elevated serum uric acid → gout. This represents a drug *side-effect* pathway, not a therapeutic one. The model may have traversed this adverse-effect node in the KG and interpreted it as a treatment signal — a classic form of noise association.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Capreomycin is not registered or marketed in the Philippines. No product licenses on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers**: Package insert data (TFDA/regulatory label warnings and contraindications) was not available at the time of this report generation. Before any further evaluation, the full prescribing information should be retrieved. Known class-level concerns for Capreomycin include nephrotoxicity, ototoxicity (auditory and vestibular), electrolyte disturbances (hypokalemia, hypocalcemia, hypomagnesemia), and neuromuscular blockade — these are clinically significant and highly relevant given the proposed indication involves a patient population that may have comorbid renal impairment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Capreomycin carry L5 evidence (model prediction only, zero supporting clinical trials or publications), and the top prediction — gout — has no mechanistic basis; the predicted link most likely reflects Capreomycin's own nephrotoxicity as a confounding path in the knowledge graph rather than any genuine therapeutic potential.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking)**: Retrieve the full prescribing information / package insert from the FDA Philippines or a reference regulatory authority (e.g., US FDA, EMA) to conduct the S1 safety pre-screen before any further evaluation.
- **Resolve DG002 (High)**: Confirm Capreomycin's mechanism of action via DrugBank API to formally assess mechanistic plausibility for all 10 predicted indications.
- **Review all 10 predictions as a batch**: The predicted disease set is dominated by musculoskeletal/skeletal genetic disorders (osteoarthritis, brachydactyly-syndactyly, pseudoachondroplasia, acromesomelic dysplasia, colobomatous microphthalmia) with no biologically credible link to an antibacterial agent — this pattern strongly suggests systematic false-positive clustering around skeletal KG nodes and warrants a model-level quality review.
- **Consider meningococcal infection (Rank 8) for a separate micro-assessment**: Among all 10 predictions, this is the only indication where Capreomycin's antibiotic class has at least theoretical relevance (antibacterial MOA vs. bacterial pathogen), though no MIC data or clinical efficacy data for *N. meningitidis* currently exists.
- **Do not advance to clinical evaluation** without completing the above steps; the current evidence base does not support investment in any of the predicted indications at this time.

---

> ⚠️ **Disclaimer**: This report is intended for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

