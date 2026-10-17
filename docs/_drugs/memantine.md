---
layout: default
title: Memantine
parent: Model Prediction Only (L5)
nav_order: 222
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Memantine: predicted new indication Pulmonary hypertension (evidence level L5). Approved use: Not available"
monitor_inn: "Memantine"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "kyphoscoliotic heart disease", "migraine with brainstem aura"]
---

# Memantine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Memantine: From an Unspecified Original Indication to Pulmonary Hypertension

## One-Sentence Summary

Memantine is an NMDA receptor antagonist. Its original approved indication is not recorded in the Philippines registration data compiled for this report. The TxGNN model's top-ranked prediction is **pulmonary hypertension**, but it has **0 clinical trials** and only **2 loosely related publications** behind it. The best-supported candidate among the predictions is **migraine disorder**, with **1 completed Phase 3 trial** and **more than 15 publications**.

> **Note:** The data compiled for this report ranks pulmonary hypertension first by TxGNN score. Migraine disorder is a close second (99.52% vs. 99.54%) and has far stronger supporting evidence. The sections below cover the top prediction, then compare it with the other predictions where useful.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the registration record has no indication text) |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 (model prediction only) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

**Other predictions for comparison:**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|------|------|------|------|
| 1 | Pulmonary hypertension | 99.54% | L5 | Hold |
| 2 | Migraine disorder | 99.52% | L1 (nominal) | Proceed with Guardrails |
| 3 | Kyphoscoliotic heart disease | 99.43% | L5 | Hold |
| 4 | Migraine with brainstem aura | 99.41% | L4 | Research Question |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Memantine is generally known as a non-competitive NMDA receptor antagonist, but this report does not rely on a recorded mechanism.

**Pulmonary hypertension (top prediction):** The link is weak. One retrieved paper (PMID 33500723) notes that the glutamate/NMDA receptor axis has been implicated in acute lung injury, pulmonary arterial hypertension and diabetes, but it is a preclinical study about insulin sensitivity and lipid metabolism. The other paper describes a Phase 1 study of MN-08, a nitrate derivative of memantine under development for pulmonary arterial hypertension. That is a different product and does not test memantine itself. The high score is a model prediction with no direct clinical support.

**Migraine disorder (best-supported alternative):** Glutamate signalling and NMDA receptor-mediated cortical spreading depression and central sensitization contribute to migraine. Memantine could plausibly reduce this neuronal hyperexcitability. Several reviews support this rationale. Even so, the evidence is limited: one commentary is titled "Memantine for migraine: big promise but little evidence."

## Clinical Trial Evidence

**Pulmonary hypertension:** Currently no related clinical trials registered.

**Migraine disorder (for reference):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04698525](https://clinicaltrials.gov/study/NCT04698525) | Phase 3 | Completed | 33 | Memantine vs. sodium valproate for prophylaxis of episodic migraine. The trial is small and uses an active comparator without a placebo. |

## Literature Evidence

**Pulmonary hypertension:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33500723](https://pubmed.ncbi.nlm.nih.gov/33500723/) | 2021 | Preclinical/Mechanistic | Theranostics | NMDA receptor activation regulates insulin sensitivity and lipid metabolism. Pulmonary hypertension is mentioned only as background. |
| [41739394](https://pubmed.ncbi.nlm.nih.gov/41739394/) | 2026 | Phase 1 PK/Safety | Clin Drug Investig | Safety and pharmacokinetics of MN-08, a nitrate derivative of memantine, in healthy Chinese volunteers. It is a different product and not disease-specific. |

**Migraine disorder (for reference, most relevant of the retrieved papers):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33961371](https://pubmed.ncbi.nlm.nih.gov/33961371/) | 2021 | Meta-analysis of RCTs | Clin Neuropharmacol | Memantine vs. placebo in migraine patients. The authors note efficacy remains controversial. |
| [34352118](https://pubmed.ncbi.nlm.nih.gov/34352118/) | 2021 | Systematic review | Headache | Efficacy and safety of memantine for prophylaxis of episodic migraine. |
| [36869904](https://pubmed.ncbi.nlm.nih.gov/36869904/) | 2023 | Review | Naunyn-Schmiedebergs Arch Pharmacol | Memantine and ketamine as potential anti-migraine agents. |
| [25159002](https://pubmed.ncbi.nlm.nih.gov/25159002/) | 2014 | Review | Ann Pharmacother | Efficacy and safety of memantine for preventing primary headache disorders. |
| [34510445](https://pubmed.ncbi.nlm.nih.gov/34510445/) | 2021 | Commentary | Headache | "Big promise but little evidence" for memantine in migraine. |
| [17901918](https://pubmed.ncbi.nlm.nih.gov/17901918/) | 2007 | Retrospective study | J Headache Pain | Retrospective review of 60 patients given memantine for migraine prevention. |
| [40978493](https://pubmed.ncbi.nlm.nih.gov/40978493/) | 2025 | Network meta-analysis | Front Pharmacol | Comparison of oral preventive medications for migraine in adults. |
| [39467289](https://pubmed.ncbi.nlm.nih.gov/39467289/) | 2024 | Clinical practice guideline | Ann Intern Med | 2023 VA/DoD guideline for treatment and prevention of migraine and tension-type headache. |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0308 | Memantine | Not recorded | Not recorded (status: cancelled) |

The only registration on record has been cancelled, so no valid single-ingredient or combination registration currently exists.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** liver disease, gallbladder disease, and impaired renal function disease.
- **Drug Interactions:** 100 interactions were found in total. The main ones listed:
  - **Moderate:** anticholinergic agents, including hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, methscopolamine, propantheline, scopolamine, trospium and mepenzolate.
  - **Minor:** ranitidine, metformin, cimetidine and potassium citrate.
  - **Level unknown:** glimepiride, doxycycline, lansoprazole, loperamide, famotidine and acetylsalicylic acid.

Please refer to the package insert for label-based warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold** (for pulmonary hypertension, the top-ranked prediction)

**Rationale:**
- The score is very high, but no clinical trial supports pulmonary hypertension and the two retrieved papers do not test memantine for this condition. The only registration in the Philippines is cancelled.
- Migraine disorder is a much stronger candidate (**Proceed with Guardrails**). Its Phase 3 L1 grade is nominal because the trial enrolled only 33 patients and used an active comparator. Kyphoscoliotic heart disease should also be held, and migraine with brainstem aura is a research question supported only indirectly.

**To proceed, the following is needed:**
- Preclinical or clinical data showing memantine itself acts on pulmonary hypertension, separate from the MN-08 derivative.
- Published results from NCT04698525, ideally confirmed in a larger placebo-controlled migraine trial.
- Detailed mechanism of action data.
- Package insert warnings and contraindications from the DOH-FDA Philippines, which are required for safety screening.
- Clarification of the cancelled registration status and the original approved indication in the Philippines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

