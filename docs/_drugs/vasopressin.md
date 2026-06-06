---
layout: default
title: Vasopressin
parent: 僅模型預測 (L5)
nav_order: 349
evidence_level: L5
indication_count: 2
---

# Vasopressin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Vasopressin: From Vasopressor Support to Congenital Prothrombin Deficiency

## One-Sentence Summary

Vasopressin (arginine vasopressin, AVP) is an endogenous antidiuretic hormone and vasopressor, clinically used for vasodilatory shock, diabetes insipidus, and variceal bleeding.
The TxGNN model predicts it may be effective for **Congenital Prothrombin Deficiency**,
with **0 clinical trials** and **3 publications** currently supporting this direction — though none directly address Factor II deficiency, and the mechanistic link remains weak.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in Philippines regulatory data (clinically known: vasodilatory shock, diabetes insipidus, variceal bleeding) |
| Predicted New Indication | Congenital Prothrombin Deficiency |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L4 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Vasopressin is an endogenous nonapeptide hormone acting through three receptor subtypes: V1a (vascular smooth muscle contraction), V1b (pituitary ACTH release), and V2 (renal water reabsorption and endothelial release of von Willebrand factor/Factor VIII from Weibel-Palade bodies). Its synthetic analog DDAVP (desmopressin) is already used in mild hemophilia A and von Willebrand disease precisely because V2 activation triggers vWF and Factor VIII release — forming the pharmacological basis for coagulation-adjacent predictions.

However, congenital prothrombin deficiency is a Factor II (prothrombin) deficiency, a coagulation pathway node that sits entirely outside the direct V2-mediated vWF/Factor VIII release mechanism. Boosting vWF or Factor VIII does not compensate for a Factor II deficit, making the mechanistic overlap very limited.

The TxGNN high prediction score most likely reflects graph-topological proximity — coagulation disorder nodes are clustered in the knowledge graph, and Vasopressin's connection to hemostatic pathways via DDAVP creates neighborhood overlap with Factor II deficiency nodes. This is a common pattern in knowledge-graph models and does not imply pharmacological specificity. The retrieved literature, which covers combined Factor V/VIII deficiency and DDAVP rather than Factor II, further supports this interpretation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity Reviews | Comprehensive review of Acquired Hemophilia A (autoantibodies against Factor VIII); covers diagnosis, aetiology, and treatment options — not specific to prothrombin deficiency or Vasopressin |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case Report | Rinsho Ketsueki | A 43-year-old male with congenital combined Factor V and Factor VIII deficiency treated with DDAVP; documents V2-mediated vWF/Factor VIII release as a hemostatic mechanism — relevant to analog mechanism but not to Factor II |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case Report | Rinsho Ketsueki | Cesarean section in a patient with combined Factor V/Factor VIII deficiency managed with Factor VIII concentrate; demonstrates replacement therapy approach — does not address Factor II (prothrombin) deficiency |

> **Note:** None of the retrieved publications directly address congenital prothrombin (Factor II) deficiency or the use of Vasopressin/DDAVP in this condition. Evidence relevance is indirect at best.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN prediction score is high (99.63%), the mechanistic link between Vasopressin and congenital prothrombin (Factor II) deficiency is weak — Vasopressin's hemostatic pathway acts on vWF/Factor VIII release, not on prothrombin synthesis or activation. No clinical trials exist, the three retrieved publications address adjacent coagulopathies rather than Factor II specifically, and critical safety data (package insert, contraindications, MOA) are unavailable for a complete evaluation.

**To proceed, the following is needed:**
- Identify whether any preclinical data links V1/V2 receptor signaling to prothrombin (Factor II) expression or activity
- Clarify whether the TxGNN prediction is driven by mechanism or by graph-topological proximity to other coagulation disorder nodes
- Retrieve the full package insert (Philippines/TFDA) to complete the safety assessment (currently Blocking data gap)
- Query DrugBank API for complete MOA data (currently High-severity data gap)
- Consider whether DDAVP (desmopressin), as a more selective V2-targeting analog with an established hemostasis record, would be a more appropriate repurposing candidate than Vasopressin itself
- If rationale is strengthened, design a focused literature search specifically for "vasopressin OR desmopressin AND prothrombin deficiency OR factor II deficiency"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

