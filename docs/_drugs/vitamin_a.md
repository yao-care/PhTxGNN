---
layout: default
title: Vitamin A
parent: 僅模型預測 (L5)
nav_order: 354
evidence_level: L5
indication_count: 10
---

# Vitamin A
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

# Vitamin A: From Nutritional Deficiency to Congenital Prothrombin Deficiency

## One-Sentence Summary

Vitamin A (retinol) is an essential fat-soluble micronutrient clinically used in the prevention and treatment of vitamin A deficiency, night blindness, and immune dysfunction, with its active metabolite retinoic acid also used in dermatological and oncological conditions.
The TxGNN model predicts it may be effective for **Congenital Prothrombin Deficiency** (hereditary Factor II deficiency), with a prediction score of **99.97%**.
However, **no supporting clinical trials or literature** directly link Vitamin A to this indication, and the mechanistic basis is biologically implausible — this prediction most likely reflects indirect knowledge graph linkages between vitamins and the coagulation pathway rather than a genuine repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vitamin A deficiency; night blindness; immune dysfunction; epithelial maintenance |
| Predicted New Indication | Congenital Prothrombin Deficiency |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Vitamin A in this context. Based on known information, Vitamin A (retinol) is the precursor to retinoic acid, which exerts its biological effects primarily through nuclear retinoic acid receptors (RAR) and retinoid X receptors (RXR). These receptors regulate a broad range of genes involved in cellular differentiation, epithelial integrity, immune modulation, and — via its active metabolite all-trans retinoic acid (ATRA) — cell cycle arrest and apoptosis in specific malignancies.

Congenital prothrombin deficiency is a rare autosomal recessive bleeding disorder caused by mutations in the F2 gene, resulting in reduced synthesis or function of prothrombin (Factor II). Prothrombin is a **Vitamin K–dependent** coagulation factor; its biological activation requires carboxylation of glutamate residues by Vitamin K–dependent carboxylase — a mechanism entirely distinct from Vitamin A/RAR/RXR signaling. There is no established biochemical pathway by which retinol or retinoic acid would enhance prothrombin gene expression or correct Factor II deficiency.

The TxGNN model's high-confidence prediction is therefore likely an artifact of indirect connections in the knowledge graph (e.g., broad "vitamin → gene regulation → coagulation" linkages), rather than direct biological plausibility. This prediction should be treated as a hypothesis-generating signal that requires mechanistic validation before further development.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00562783](https://clinicaltrials.gov/study/NCT00562783) | Phase 2 | Completed | 90 | Vitalliver in decompensated cirrhosis — intervention is not Vitamin A; no direct relevance to prothrombin deficiency |
| [NCT04384341](https://clinicaltrials.gov/study/NCT04384341) | N/A | Recruiting | 480 | PHILEOS study: haemophilia and bone mineral density — studies Factor VIII/IX deficiency, not Factor II; Vitamin A not evaluated |
| [NCT02392767](https://clinicaltrials.gov/study/NCT02392767) | N/A | Completed | 25 | Multi-vitamin dietary supplement for endothelial function in hypertension — unrelated to congenital coagulation disorders |
| [NCT00168077](https://clinicaltrials.gov/study/NCT00168077) | Phase 3 | Completed | 40 | BERIPLEX P/N (prothrombin complex concentrate) for acquired Factor II/VII/IX/X deficiency — intervention is prothrombin concentrate, not Vitamin A |
| [NCT03534752](https://clinicaltrials.gov/study/NCT03534752) | N/A | Completed | 220 | Retrospective registry of adult inborn errors of metabolism in French-speaking Switzerland — observational only, no Vitamin A intervention |

> **Note:** None of these trials investigate Vitamin A for congenital prothrombin deficiency. All five trials were incidentally retrieved and are assessed as Grade C relevance (not directly applicable).

---

## Literature Evidence

Currently no related literature available for Vitamin A in congenital prothrombin deficiency.

---

## Philippines Market Information

Vitamin A (DB00162) currently has no registered products with the Philippine FDA. No authorization records, dosage forms, or approved indications are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Known general considerations for Vitamin A: teratogenicity risk at high doses (particularly in pregnancy), hepatotoxicity with chronic excessive intake, and potential for hypervitaminosis A (headache, bone pain, liver damage). Formal Philippines-specific warnings and contraindications are unavailable pending package insert review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical, mechanistic, or translational evidence supporting Vitamin A in congenital prothrombin deficiency. The TxGNN score (99.97%), while superficially high, reflects indirect knowledge graph connectivity — Vitamin A's RAR/RXR signaling has no known influence on Vitamin K–dependent Factor II synthesis, and the five retrieved clinical trials are all irrelevant to this indication.

**To proceed, the following is needed:**

- Identify a biologically plausible link between Vitamin A/retinoic acid signaling (RAR/RXR) and Factor II (prothrombin) gene expression — no such mechanism is currently known
- Commission preclinical studies (hepatocyte models, F2-knockout mice) to test whether retinoid supplementation affects prothrombin levels
- Obtain Vitamin A mechanism of action (MOA) data from DrugBank API to identify any coagulation-related gene targets
- Review Philippines FDA package insert and TFDA package insert for full safety profile (warnings, contraindications)
- Consider prioritizing higher-evidence TxGNN predictions instead: **cell proliferation disorder** (Rank 5, L2, Proceed with Guardrails), **perinatal disease** (Rank 7, L2, Proceed with Guardrails), and **radiation or chemically induced disorder** (Rank 10, L2, Proceed with Guardrails) all show substantially stronger clinical evidence bases for Vitamin A repurposing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

