---
layout: default
title: Vasopressin
parent: Model Prediction Only (L5)
nav_order: 353
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Vasopressin: predicted new indication Congenital prothrombin deficiency (evidence level L4). Approved use: Not available"
monitor_inn: "Vasopressin"
predicted_indications: ["congenital prothrombin deficiency", "drug-induced osteoporosis"]
---

# Vasopressin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Vasopressin: From Unspecified Original Indication to Congenital Prothrombin Deficiency
{: .text-alpha }

## One-Sentence Summary

Vasopressin is a peptide hormone drug whose original approved indication is not recorded in the data compiled for this report.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**,
but there are **0 clinical trials** and only **3 indirect publications** (none about vasopressin itself, and none about prothrombin deficiency), so the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the only registration has no indication text) |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Vasopressin and its analog desmopressin (DDAVP) are known to stimulate release of von Willebrand factor and factor VIII from endothelial stores through V2 receptor signaling. This is relevant to factor VIII and von Willebrand factor deficiencies.

That mechanism does not plausibly raise prothrombin (factor II) levels, so there is no clear mechanistic bridge to congenital prothrombin deficiency. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The retrieved papers concern acquired hemophilia A and combined factor V/VIII deficiency, and they describe desmopressin rather than vasopressin, so they are indirect evidence at best.

A second prediction, **drug-induced osteoporosis** (score 0.9962), has no clinical trials and no literature. Vasopressin receptors are present on bone cells, but this is preclinical and hypothetical. Vasopressin-related hyponatremia is linked to bone loss and could suggest harm rather than benefit. This prediction rests on the model score alone (L5) and also warrants a Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity Reviews | Reviews diagnosis, causes and treatment of acquired hemophilia A, caused by autoantibodies against factor VIII. Indirect: it is a different disease. |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case report | Rinsho Ketsueki | DDAVP given to a patient with congenital combined factor V and factor VIII deficiency. Describes desmopressin, not vasopressin. |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case report | Rinsho Ketsueki | Cesarean section managed with factor VIII replacement in a pregnant woman with combined factor V and factor VIII deficiency. |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0511 | Vasopressin | Not specified | Not specified (status: valid) |

## Safety Considerations

Please refer to the package insert for safety information.

**Drug Interactions** (100 interactions were identified; examples from the first 20 reviewed):
- **Major**: Dolasetron, Cisapride, Papaverine, Macimorelin
- **Moderate**: Famotidine, Epinephrine, Loperamide, Chlorpropamide, Clarithromycin, Levofloxacin, Ondansetron, Granisetron, Palonosetron, Promethazine, Cilostazol, Heparin, and others
- **Minor**: Metronidazole

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical trials, only indirect literature on other factor deficiencies (and on desmopressin rather than vasopressin), and no plausible mechanism for raising prothrombin. The second prediction has no supporting evidence at all. The only Philippine registration is cancelled, and label-based safety information is missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the DOH-FDA Philippines (currently missing, and blocking safety screening)
- Mechanism of action data for vasopressin (for example from DrugBank)
- Independent mechanistic or preclinical evidence linking vasopressin to prothrombin deficiency, or to drug-induced osteoporosis
- Clarification of the original approved indication and the reason for the registration cancellation
- Review of the major drug interactions (especially QT-prolonging agents) if development is reconsidered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

