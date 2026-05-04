---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 168
evidence_level: L5
indication_count: 7
---

# Ibuprofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Ibuprofen: From Anti-inflammatory/Analgesic Use to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ibuprofen is a widely used non-steroidal anti-inflammatory drug (NSAID), primarily indicated for pain relief, fever reduction, and management of inflammatory conditions such as osteoarthritis and rheumatoid arthritis.
The TxGNN model predicts it may be effective for **Acromesomelic Dysplasia, Hunter-Thompson Type**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anti-inflammatory, analgesic, antipyretic (NSAID) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 (Model prediction only) |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ibuprofen is a non-selective cyclooxygenase (COX-1/COX-2) inhibitor. By blocking the COX enzymes, it reduces the synthesis of prostaglandins—lipid mediators that drive inflammation, pain, and fever. This mechanism makes Ibuprofen one of the most widely prescribed NSAIDs worldwide for musculoskeletal pain, headache, dysmenorrhoea, osteoarthritis, and rheumatoid arthritis.

Acromesomelic dysplasia, Hunter-Thompson type, is a rare autosomal recessive skeletal disorder caused by loss-of-function mutations in the **GDF5** (growth/differentiation factor 5) gene. It results in severe shortening of the middle and distal segments of the limbs due to abnormal cartilage and bone development. The pathology is fundamentally a structural, genetically-determined skeletal malformation rather than an inflammatory process.

The mechanistic link between Ibuprofen's COX inhibition and GDF5-driven skeletal dysplasia is **very weak**. While prostaglandin signalling does play a role in bone metabolism and chondrocyte biology, there is no established evidence that NSAID therapy can correct or modify the congenital cartilage/bone developmental defects characteristic of this condition. At best, Ibuprofen could offer non-specific symptomatic relief for any accompanying joint pain, but this does not constitute a disease-modifying repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the combination of Ibuprofen and acromesomelic dysplasia, Hunter-Thompson type. Searches were conducted on ClinicalTrials.gov and ICTRP (queried 2026-03-09) with zero results.

---

## Literature Evidence

Currently no related literature available. A PubMed search (queried 2026-03-09) for Ibuprofen in the context of acromesomelic dysplasia, Hunter-Thompson type returned zero results.

---

## Philippines Market Information

Ibuprofen currently has **no registered products** with the Philippines FDA in this dataset. Despite being one of the most widely available OTC medications globally, no license records were found in the current data extract.

---

## Additional Predicted Indications Overview

Since the top-ranked indication lacks supporting evidence, the following table summarises all 7 TxGNN predictions for context:

| Rank | Predicted Disease | TxGNN Score | Evidence Level | Mechanistic Link | Recommendation |
|------|------------------|-------------|----------------|-----------------|----------------|
| 1 | Acromesomelic dysplasia, Hunter-Thompson type | 99.74% | L5 | Very weak (GDF5 mutation; COX inhibition irrelevant to skeletal malformation) | Hold |
| 2 | Brachyolmia-amelogenesis imperfecta syndrome | 99.71% | L5 | Very weak (genetic structural defect of spine and enamel) | Hold |
| 3 | Myosclerosis | 99.68% | L5 | Weak to moderate (fibrotic process may involve COX-2, but no direct evidence) | Hold |
| 4 | Brachyolmia | 99.67% | L5 | Very weak (TRPV4/SLC26A2 mutations; vertebral dysplasia) | Hold |
| 5 | Brachydactyly-syndactyly syndrome | 99.66% | L5 | Very weak (HOXD13/GDF5 mutations; congenital limb malformation) | Hold |
| 6 | Pseudoachondroplasia | 99.66% | L5 | Weak (COMP mutation; early-onset OA is already an existing NSAID indication) | Hold |
| 7 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.60% | L5 | Very weak (multisystem developmental anomaly) | Hold |

**Notable pattern:** All 7 predictions are rare genetic skeletal/developmental disorders. The TxGNN model appears to be clustering Ibuprofen with musculoskeletal conditions broadly, but these are congenital structural defects rather than inflammatory conditions amenable to COX inhibition.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: Ibuprofen is a well-characterised NSAID with known class-level risks including gastrointestinal bleeding, cardiovascular events (with prolonged use), and renal impairment. Full safety data was not available in this evidence pack and should be sourced from the product label or DrugBank.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All seven predicted indications are rare genetic skeletal dysplasias with **zero clinical trial evidence** and **zero literature support** (Evidence Level L5). The mechanistic links between Ibuprofen's COX-inhibition and the underlying genetic pathologies (GDF5, COMP, TRPV4, HOXD13 mutations) are uniformly very weak. These predictions likely reflect a graph-level artefact in TxGNN's knowledge graph rather than genuine repurposing opportunities.

**To proceed, the following would be needed:**
- Detailed mechanism of action data (MOA) to formally assess COX/prostaglandin pathway intersection with GDF5 and other implicated signalling cascades
- Preclinical evidence (in vitro or animal models) demonstrating any effect of NSAIDs on skeletal dysplasia phenotypes
- Philippines FDA regulatory data (package insert warnings, contraindications) to complete the safety assessment
- Consider deprioritising this candidate in favour of drugs with stronger mechanistic rationale for rare skeletal disorders

---

*Disclaimer: This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

