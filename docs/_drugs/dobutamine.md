---
layout: default
title: Dobutamine
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 10
---

# Dobutamine
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

# Dobutamine: From Acute Heart Failure to Alopecia

## One-Sentence Summary

Dobutamine is a potent β1-adrenergic agonist inotrope used in intensive care settings for acute decompensated heart failure and cardiogenic shock.
The TxGNN model ranks **Alopecia** as its top predicted repurposing candidate (score 99.85%), with **0 clinical trials** and **2 incidentally retrieved publications** — however, mechanistic analysis reveals that all top-10 predictions represent knowledge graph noise paths rather than genuine therapeutic opportunities.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute decompensated heart failure / cardiogenic shock (not registered in Philippines) |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on established pharmacology, Dobutamine is a synthetic catecholamine that primarily acts as a β1-adrenergic receptor agonist, producing positive inotropic (increased myocardial contractility) and chronotropic effects. It is administered intravenously in ICU settings to augment cardiac output in acute decompensated heart failure. It is not used in any outpatient or chronic disease setting.

The predicted connection to alopecia appears to originate from a knowledge graph noise path. The most likely route runs through Minoxidil — a drug known for both vasodilation and hair-growth promotion — creating an indirect shared node around "adrenergic/vascular effects." This is a false mechanistic bridge: Dobutamine's β1-adrenergic stimulation has no known regulatory role in the hair follicle growth cycle, and its partial α1-adrenergic activity could theoretically impair follicular blood flow through cutaneous vasoconstriction — the pharmacological opposite of what Minoxidil does.

This same noise-path pattern appears across all 10 top predictions, which cluster into two groups: hair conditions (alopecia, hypotrichosis simplex, congenital hypotrichosis, diffuse alopecia areata, hypertrichosis) and vascular/neurological disorders (open-angle glaucoma, primary hereditary glaucoma, Raynaud disease, headache disorder, migraine). Most critically, headache is a **documented side effect** of dobutamine — not a treatment target — and its appearance as a repurposing candidate clearly indicates that these predictions reflect KG co-occurrence artifacts rather than therapeutic signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Dobutamine in alopecia.

---

## Literature Evidence

The 2 retrieved publications are not directly relevant to dobutamine as a treatment for alopecia. Both were captured due to keyword co-occurrence in the search system, not because they demonstrate any therapeutic relationship.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [41046802](https://pubmed.ncbi.nlm.nih.gov/41046802/) | 2025 | Case Report (Veterinary) | Journal of Veterinary Cardiology | Feline minoxidil intoxication causing congestive heart failure; dobutamine used for haemodynamic support of the cat — retrieved due to shared drug node with minoxidil (a hair-loss drug), not as alopecia treatment evidence |
| [17505274](https://pubmed.ncbi.nlm.nih.gov/17505274/) | 2007 | Case Report | Pediatric Emergency Care | Colchicine poisoning in a child; hair loss appeared in the recovery phase as a known complication of colchicine toxicity — dobutamine not mentioned as a treatment for hair loss at any point |

---

## Philippines Market Information

Dobutamine currently has no registered products in the Philippines. No authorization numbers, brand names, or approved indications are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Clinical note:** Headache is a documented adverse effect during dobutamine stress echocardiography, reported across a large retrospective safety series of 3,011 procedures ([PMID 9137218](https://pubmed.ncbi.nlm.nih.gov/9137218/)). This is directly relevant when interpreting TxGNN predictions linking dobutamine to headache disorder (rank #8) and migraine disorder (rank #10) — those predictions reflect a pharmacovigilance signal (drug-causes-headache), not a therapeutic one.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN top predictions for Dobutamine are rated L5 (model prediction only) with zero supporting clinical trials and no plausible mechanistic basis. The top prediction cluster (alopecia, hypotrichosis variants, hypertrichosis) likely emerges from an indirect KG connection through Minoxidil, while headache and migraine predictions arise from pharmacovigilance co-occurrence — a known failure mode where side-effect nodes are misread as therapeutic targets. Dobutamine is a short-acting IV agent administered exclusively in monitored ICU/hospital settings, which further makes chronic or outpatient non-cardiac indications structurally implausible for repurposing.

**To proceed, the following is needed:**

- Retrieve Dobutamine's full MOA documentation from DrugBank to formally document β1/β2/α1 receptor binding ratios
- Download the original package insert (or equivalent regulatory document) to establish the official approved indication and capture all warnings and contraindications
- Re-examine whether any cardiac-adjacent indications (e.g., specific subtypes of cardiogenic shock, right heart failure, post-cardiotomy syndrome) appear among lower-ranked TxGNN predictions with genuine mechanistic support
- Apply noise-path filtering to the KG before re-running predictions — specifically removing edges formed through indirect "side-effect" co-occurrence and shared vascular nodes with unrelated drugs (e.g., Minoxidil)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

