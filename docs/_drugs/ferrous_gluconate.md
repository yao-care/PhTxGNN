---
layout: default
title: Ferrous Gluconate
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 5
---

# Ferrous Gluconate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Ferrous Gluconate: From Iron Deficiency Anemia to Plummer-Vinson Syndrome

## One-Sentence Summary

Ferrous gluconate is a divalent iron (Fe²⁺) salt supplement belonging to the ferrous salt pharmacological class, traditionally used to correct iron deficiency anemia. The TxGNN model predicts it may be effective for **Plummer-Vinson Syndrome (PVS)** — a rare condition in which chronic iron deficiency drives pharyngo-esophageal mucosal atrophy and esophageal web formation — with a prediction score of **99.94%**. Currently, **no dedicated clinical trials or publications** specifically testing ferrous gluconate in PVS have been identified, though the mechanistic rationale is exceptionally strong: ferrous salt supplementation is already the established first-line treatment for PVS as a drug class.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Iron deficiency anemia (standard pharmacological class use; no Philippine regulatory registration available) |
| Predicted New Indication | Plummer-Vinson Syndrome |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 (Mechanistic / Class-Effect Basis) |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Plummer-Vinson Syndrome (PVS) — also known as Patterson-Kelly Syndrome — presents as a clinical triad of iron deficiency anemia, progressive dysphagia, and pharyngo-esophageal webs. The underlying mechanism is well-established: chronic iron depletion leads to atrophic changes in the pharyngo-esophageal mucosa, resulting in web formation at the post-cricoid region. Because iron deficiency is the root cause, iron repletion is universally recognized as the cornerstone of PVS management, capable of reversing esophageal webs, restoring mucosal integrity, and resolving dysphagia without the need for surgical dilation in many cases.

Currently, detailed mechanism of action (MOA) data for Ferrous gluconate (DB14488) is not available in the system. Based on established pharmacology, ferrous gluconate belongs to the ferrous salt class and delivers divalent iron (Fe²⁺) that is efficiently absorbed in the duodenum and proximal jejunum via the divalent metal transporter 1 (DMT1). This mechanism directly addresses the pathological iron depletion that underlies PVS. The high TxGNN knowledge graph score (0.9994) reflects this mechanistic alignment along the pathway: ferrous iron supplementation → restoration of systemic iron stores → reversal of PVS mucosal atrophy and esophageal webs.

While no compound-specific RCTs or publications linking ferrous gluconate to PVS were retrieved, this prediction represents a well-supported **class-effect extrapolation**. Other members of the ferrous salt class — including ferrous sulfate and ferrous fumarate — have documented use in PVS management, and ferrous gluconate, as a pharmacologically equivalent member, is expected to share this therapeutic profile. The primary evidence gap is the absence of DB14488-specific clinical data, rather than any mechanistic implausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ferrous gluconate in Plummer-Vinson Syndrome.

---

## Literature Evidence

Currently no related literature available specifically examining Ferrous gluconate in the context of Plummer-Vinson Syndrome.

---

## Philippines Market Information

Ferrous gluconate (DB14488) is currently **not marketed in the Philippines**. No drug registration licenses were identified in the Philippine FDA database.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|--------------|-------------|---------------------|
| — | No registered products found | — | — |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic alignment between ferrous gluconate and Plummer-Vinson Syndrome is highly compelling — PVS is an iron-deficiency-driven condition for which ferrous salt supplementation is the established standard of care at the drug-class level, and the TxGNN knowledge graph score of 99.94% directly reflects this biological plausibility. The current evidence ceiling of L4 is driven not by mechanistic uncertainty, but by a gap in compound-specific clinical data for DB14488; the drug class as a whole has well-documented efficacy in PVS.

**To proceed, the following is needed:**

- **Compound-specific literature review:** Conduct a targeted search for ferrous gluconate specifically in PVS case series and observational studies, distinguishing DB14488 from other ferrous salts (ferrous sulfate, ferrous fumarate) in the literature
- **MOA data retrieval:** Query the DrugBank API to obtain the full pharmacological profile of DB14488 (Data Gap DG002 — High severity)
- **Safety profile completion:** Download and parse the Philippine FDA (or equivalent regional) package insert to obtain formal warnings and contraindications (Data Gap DG001 — Blocking severity); until resolved, this prevents formal safety screening (Stage S1)
- **Drug interaction check:** Re-run DDI query using alternative databases (e.g., DrugBank interactions module, Lexicomp) as the initial query returned no results
- **Regulatory pathway assessment:** Since ferrous gluconate is not currently registered in the Philippines, evaluate the regulatory pathway required for product introduction if clinical development is pursued; note that ferrous salt products are widely available in other markets and the regulatory burden may be low
- **Class-evidence bridging document:** Prepare a class-effect justification document compiling evidence from other ferrous salts in PVS to support an extrapolation argument for DB14488 during any future regulatory submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

