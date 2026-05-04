---
layout: default
title: Clarithromycin
parent: 僅模型預測 (L5)
nav_order: 74
evidence_level: L5
indication_count: 5
---

# Clarithromycin
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

# Clarithromycin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Clarithromycin is a macrolide antibiotic broadly used for respiratory tract infections, *H. pylori*-associated peptic disease, and non-tuberculous mycobacterial (NTM) infections.
The TxGNN model predicts it may be effective for **Hyperamylasemia**, with **0 clinical trials** and **1 publication** currently supporting this direction.
Overall evidence is extremely limited, and this prediction is likely an artefact of an indirect knowledge graph connection rather than a genuine therapeutic relationship.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (respiratory tract, *H. pylori*, NTM) — Philippines registration data unavailable |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established clinical pharmacology, Clarithromycin is a macrolide antibiotic that inhibits bacterial protein synthesis by binding to the 50S ribosomal subunit. It also possesses anti-inflammatory and immunomodulatory properties — notably suppression of the NF-κB pathway and reduction of pro-inflammatory cytokines — which have driven interest in its use beyond conventional anti-infective indications. It is a core component of *Mycobacterium avium* complex (MAC) treatment regimens and *H. pylori* eradication therapy.

Hyperamylasemia, however, is not an independent treatable disease entity; it is a biochemical finding (elevated serum amylase) that reflects pancreatic or salivary gland injury from a variety of underlying causes. There is no known pharmacological pathway by which Clarithromycin would directly regulate amylase secretion, amylase clearance, or the broad spectrum of conditions that cause elevated amylase.

The high TxGNN score most likely originates from an indirect knowledge graph chain: *Mycobacterium abscessus* pulmonary infection → pancreatic involvement → elevated serum amylase. Because Clarithromycin is a primary agent in *M. abscessus* treatment regimens, the model has drawn a coincidental association rather than a biologically direct therapeutic link. This prediction should be treated as a probable false positive pending further mechanistic review.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [15228140](https://pubmed.ncbi.nlm.nih.gov/15228140/) | 2004 | Case Report | Nihon Kokyuki Gakkai Zasshi (Japanese Respiratory Society) | A 76-year-old man with *M. abscessus* pulmonary infection who coincidentally also had primary macroamylasemia. Clarithromycin was used as part of the anti-mycobacterial regimen — **not** as a treatment for elevated amylase. The presence of hyperamylasemia was incidental; this paper does not support Clarithromycin as a therapy for hyperamylasemia. |

---

## Philippines Market Information

Clarithromycin currently has **no registered drug authorizations** in the Philippines FDA database. No product entries are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Hyperamylasemia is a biochemical marker, not a discrete treatable condition, and no mechanistic basis exists for Clarithromycin to reduce serum amylase or address the wide range of underlying causes. The sole literature hit describes an incidental clinical co-occurrence; the high TxGNN score almost certainly reflects a spurious knowledge graph pathway via NTM-related pancreatic pathophysiology rather than a genuine drug–disease relationship.

**To proceed, the following is needed:**

- **Clarify the true intended target**: If the research question is whether Clarithromycin can treat NTM-related secondary hyperamylasemia specifically (rather than hyperamylasemia in general), a redesigned evidence search targeting that narrower clinical scenario may yield more meaningful results.
- **Obtain MOA data**: Full mechanism of action data from DrugBank (DG002 remediation) is needed to confirm or refute any plausible biochemical link to amylase regulation.
- **Obtain Philippines safety data**: Philippines FDA package insert data (DG001 remediation) — including warnings and contraindications — must be retrieved before any clinical evaluation stage can begin.
- **Consider higher-ranked biologically plausible candidates**: Among the five TxGNN predictions in this pack, **Rank 4 (Punctate Epithelial Keratoconjunctivitis / MRKC)** carries a stronger mechanistic rationale (anti-staphylococcal activity + NF-κB suppression improving meibomian gland function) and an L4 evidence signal from a 2024 Japanese observational study; this candidate may merit a dedicated evidence search before hyperamylasemia is prioritized further.

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

