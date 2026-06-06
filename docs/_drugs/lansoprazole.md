---
layout: default
title: Lansoprazole
parent: 僅模型預測 (L5)
nav_order: 197
evidence_level: L5
indication_count: 2
---

# Lansoprazole
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

Using the `txgnn-pipeline` skill — confirmed this is a TxGNN report generation task. Now generating the evaluation report from the Evidence Pack.

---

# Lansoprazole: From Acid-Related Disorders to Duodenogastric Reflux

## One-Sentence Summary

Lansoprazole is a proton pump inhibitor (PPI) widely recognized for treating acid-related conditions such as GERD, peptic ulcer disease, and Zollinger-Ellison syndrome.
The TxGNN model predicts it may be effective for **Duodenogastric Reflux**, with **0 clinical trials** and **2 publications** currently available to support this direction.
Notably, one of those publications raises an active preclinical safety concern that warrants careful review before any clinical advancement.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Philippines; pharmacologically indicated for GERD / Peptic Ulcer Disease |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Lansoprazole is a proton pump inhibitor (PPI) that irreversibly binds H⁺/K⁺-ATPase on the luminal surface of gastric parietal cells, blocking the final step of acid secretion. It is established as a first-line agent for peptic ulcer disease, GERD, *H. pylori* eradication regimens, NSAID-associated GI lesions, and Zollinger-Ellison syndrome — as summarized in PMID 18679668.

Duodenogastric reflux (DGR) is characterized by the retrograde movement of bile acids and pancreatic secretions from the duodenum into the stomach. Unlike GERD, where acid suppression is directly therapeutic, DGR involves an alkaline refluxate — not gastric acid. The mechanistic connection between PPI-mediated acid suppression and DGR is therefore inherently limited: a PPI can reduce co-existing acid injury and symptom overlap, but cannot directly counteract bile-driven mucosal damage, the core pathology of DGR.

Most importantly, PMID 15052437 (a rat DGR model) found that lansoprazole administration in the presence of duodenogastric reflux may actively promote gastric carcinogenesis. This is a meaningful preclinical safety signal in the exact pathological context under consideration, and it must be formally assessed and resolved before this repurposing direction can proceed further.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for duodenogastric reflux.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | European Journal of Clinical Pharmacology | Comprehensive PPI pharmacokinetics and clinical use update; confirms lansoprazole as first-choice therapy for peptic ulcer, *H. pylori*, GERD, NSAID-GI lesions, and Zollinger-Ellison syndrome |
| [15052437](https://pubmed.ncbi.nlm.nih.gov/15052437/) | 2004 | Animal Study | Gastric Cancer | ⚠️ In a rat DGR model, lansoprazole combined with duodenogastric reflux promoted gastric carcinogenesis — an active preclinical safety signal directly relevant to this repurposing hypothesis |

---

## Philippines Market Information

Lansoprazole currently has **no registered products** with the Philippine FDA. No authorization numbers, product names, or approved indications are on record.

---

## Safety Considerations

> ⚠️ **Active Preclinical Safety Signal**: PMID 15052437 demonstrates that lansoprazole may promote gastric carcinogenesis in rats with duodenogastric reflux. Because this signal arises in the exact disease context being evaluated, it constitutes a blocking concern that must be formally risk-assessed before any clinical development can proceed.

All other safety data (key warnings, contraindications, drug interactions) are not available in this evidence pack. Please refer to the approved package insert from a reference jurisdiction (e.g., Taiwan, Japan, USA) for current warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between PPI acid suppression and duodenogastric reflux (a bile-driven, alkaline condition) is weak, no clinical trial evidence exists for this specific indication, and a preclinical study raises a potential carcinogenesis risk in the precise patient population of interest — making further advancement premature without targeted safety investigation.

**To proceed, the following is needed:**

- **Resolve the carcinogenesis signal**: Conduct a formal risk assessment of PMID 15052437 — determine whether the effect is dose-dependent, PPI class-wide, or specific to the DGR microenvironment before any in-human hypothesis testing
- **Establish mechanistic rationale**: Clarify whether any component of DGR pathology (e.g., co-existing acid hypersecretion, H. pylori overlap) could genuinely benefit from PPI suppression, distinguishing it from mere symptomatic co-management
- **Obtain full MOA data**: Query DrugBank API (DB00448) for complete mechanism, targets, and known pharmacodynamics
- **Retrieve safety baseline**: Obtain package insert warnings and contraindications from a reference market (Taiwan TFDA, Japan PMDA, or US FDA) to enable S1 safety pre-screening
- **Survey reference-market regulatory status**: Confirm whether Lansoprazole holds any DGR-adjacent approval (e.g., gastritis, bile reflux gastritis) in Taiwan, Japan, or Korea to establish a regulatory precedent baseline
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

