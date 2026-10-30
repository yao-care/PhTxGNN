---
layout: default
title: Tramadol
parent: Model Prediction Only (L5)
nav_order: 342
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-30
monitor_inn: "Tramadol"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "juvenile idiopathic arthritis", "juvenile arthritis due to defect in LACC1", "rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis"]
description: "Tramadol: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Not recorded in the local data"
---

# Tramadol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Tramadol: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Tramadol is an analgesic whose original indications are osteoarthritis and related joint disease.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare skeletal disorder,
but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, tramadol is an opioid/SNRI-type analgesic. It has been used for musculoskeletal pain such as osteoarthritis, but it is a symptomatic treatment and not a disease-modifying one.

Acromesomelic dysplasia, Hunter-Thompson type, is a rare skeletal dysplasia caused by defects in the CDMP1/GDF5 pathway. Tramadol has no known effect on this pathway. At most, it could offer symptomatic pain relief in a disease that affects the bones and joints. The high model score is therefore not backed by a mechanistic link.

The other top-ranked predictions show the same pattern. They include brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, brachyolmia, pseudoachondroplasia, spondyloarthropathy, juvenile idiopathic arthritis, LACC1-related juvenile arthritis, rheumatoid nodulosis, and RF-positive polyarticular juvenile idiopathic arthritis. All are at evidence level L5 with no supporting trials. The only linked paper (PMID 20799760, for juvenile idiopathic arthritis) concerns the NSAID ketoprofen, not tramadol, so it is not direct evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the lead prediction.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0494 | Tramadol | Not specified | Not specified (registration valid) |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these are model-graph associations, not package insert text): hypertension, liver failure, liver disease, cirrhosis, epilepsy, anxiety and neurotic disorders, dysthymic disorder, diabetes mellitus, diabetic ketoacidosis, substance abuse/dependence, substance-related disorder, alcohol withdrawal, substance withdrawal syndrome, hyperlipidemia, respiratory failure, paracetamol poisoning, serotonin syndrome, pseudotumor cerebri, intracranial hypertension, Wernicke-Korsakoff syndrome, gallbladder disease, and central nervous system infections.
- **Drug Interactions**: 100 interactions were found. The first 20 listed include these **Major** ones: alvimopan, bupropion, cisapride, dexfenfluramine, diethylpropion, dolasetron, dronabinol, ephedrine, and fenfluramine. **Moderate** ones include atropine, bisacodyl, cimetidine, clarithromycin, famotidine, and eliglustat.
- **Pediatric use**: Several predicted indications are juvenile arthritis conditions. Opioid use in children carries safety concerns, including CYP2D6-related risks.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials, no literature, and no plausible disease-modifying mechanism. The only registration in the Philippines has been cancelled, and the safety profile (opioid, serotonergic, and seizure risks) argues against pursuing a rare-disease indication without supporting evidence.

**To proceed, the following is needed:**
- Mechanism of action data and a biological rationale linking tramadol to the GDF5/CDMP1 pathway
- Preclinical or clinical evidence for the predicted indication (or a decision to focus on a symptomatic pain indication instead)
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Clarification of the regulatory status, since the only registration is cancelled
- A safety assessment for the target population, especially children
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

