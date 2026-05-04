---
layout: default
title: Flucytosine
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 1
---

# Flucytosine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Flucytosine: From Antifungal Treatment to Bone Paget Disease

## One-Sentence Summary

Flucytosine (5-fluorocytosine) is an antifungal agent conventionally used for systemic fungal infections such as cryptococcal meningitis and invasive candidiasis.
The TxGNN model assigns it a high prediction score (99.04%) for **Bone Paget Disease**,
yet this is supported by **zero clinical trials** and **zero publications** — a classic high-score, zero-evidence pattern arising from graph-walk artifacts in the knowledge graph rather than true biological signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Systemic fungal infections (cryptococcosis, candidiasis) |
| Predicted New Indication | Bone Paget Disease |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Flucytosine exerts its antifungal effect through a highly selective, fungus-specific mechanism: it is taken up by fungal cells via cytosine permease and converted intracellularly by **fungal cytosine deaminase** into 5-fluorouracil (5-FU). 5-FU then inhibits thymidylate synthase and disrupts RNA synthesis, ultimately blocking fungal nucleic acid metabolism. Critically, **human cells do not express cytosine deaminase under normal physiological conditions**, so this conversion — and the resulting pharmacological effect — does not occur in human tissues.

Bone Paget Disease operates through an entirely different set of pathological mechanisms: osteoclast hyperactivation, RANKL/OPG signalling imbalance, aberrant NF-κB pathway activity, *SQSTM1* (p62) gene mutations, and a postulated association with paramyxovirus (measles virus nucleocapsid protein) infection. None of these pathways intersect with flucytosine's known pharmacology.

The TxGNN model's high score (0.9904) most likely reflects an indirect graph-path connection through pyrimidine-metabolism nodes in the knowledge graph — a **graph-walk artifact** rather than a genuine biological signal. This is a prototypical "High-Score, Zero-Evidence" candidate and should not be interpreted as evidence of therapeutic potential in Paget disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Flucytosine is **not currently marketed** in the Philippines. No drug registrations or authorization numbers are on record with the FDA Philippines.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** No TFDA/FDA Philippines package insert data, contraindication records, or drug–drug interaction data were retrievable in this evidence pack. Before any clinical consideration, full prescribing information (including known risks of bone marrow suppression and hepatotoxicity associated with flucytosine) must be reviewed from the originator's current label.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no mechanistic, clinical, or published evidence connecting flucytosine to bone Paget disease; the high TxGNN score is attributable to a knowledge-graph topology artifact (indirect pyrimidine-node linkage) rather than any real pharmacological activity in osteoclast or bone remodelling pathways. Proceeding with this candidate would not be scientifically justifiable at this stage.

**To revisit this candidate, the following would be needed:**

- Identification of a credible mechanistic hypothesis linking flucytosine (or its metabolites) to osteoclast biology, RANKL/OPG signalling, or NF-κB pathway modulation
- At least one published preclinical study (in vitro or in vivo bone model) demonstrating relevant activity
- Clarification of whether the KG link is a known false-positive pattern and documentation in the model's artifact registry
- If a hypothesis emerges: a formal safety review using the complete flucytosine prescribing information (myelosuppression, hepatotoxicity, renal dosing adjustments) before any experimental design is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

