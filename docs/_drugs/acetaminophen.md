---
layout: default
title: Acetaminophen
parent: 僅模型預測 (L5)
nav_order: 12
evidence_level: L5
indication_count: 1
---

# Acetaminophen
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

# Acetaminophen: From Analgesic/Antipyretic to Migraine with Brainstem Aura

## One-Sentence Summary

Acetaminophen (paracetamol) is a widely used over-the-counter analgesic and antipyretic, indicated for the relief of mild-to-moderate pain and fever.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura (MBA)**,
with **0 clinical trials** and **20 publications** currently supporting this research direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Mild-to-moderate pain and fever relief (analgesic/antipyretic) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacological properties, Acetaminophen is a centrally acting analgesic and antipyretic whose efficacy in general migraine is well-established, providing a reasonable mechanistic foundation for exploring its use in migraine with brainstem aura.

The mechanistic rationale linking Acetaminophen to MBA involves three proposed pathways: **(1) Central COX-3 inhibition** — Acetaminophen reduces prostaglandin E2 synthesis in the cerebrospinal fluid, potentially dampening nociceptive signaling in the brainstem, which is the primary anatomical site of injury in MBA; **(2) Descending serotonin pathway activation** — via 5-HT3 receptors, Acetaminophen engages descending pain-inhibitory circuits in which the brainstem serves as a critical relay station, directly relevant to the brainstem involvement characteristic of MBA pathology; **(3) Possible endocannabinoid modulation** — indirect inhibition of fatty acid amide hydrolase (FAAH) may contribute to additional analgesic effects.

However, MBA involves a unique pathological process — cortical spreading depression (CSD) extending into the brainstem and cerebellar peduncles — that may require more potent vascular or neurological interventions (e.g., triptans). Acetaminophen's direct impact on this CSD-driven mechanism currently lacks MBA-specific research validation. None of the 20 identified publications address MBA as a distinct cohort, limiting the extrapolation from general migraine evidence to this specific subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Acetaminophen specifically in migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Systematic Review / Clinical Guideline | *Headache* | American Headache Society updated evidence assessment of acute migraine pharmacotherapies; provides evidence grading for acetaminophen-based regimens as first-line options |
| [11318886](https://pubmed.ncbi.nlm.nih.gov/11318886/) | 2001 | Comparative Clinical Trial | *Headache* | Head-to-head comparison of acetaminophen combination (isometheptene + dichloralphenazone) versus sumatriptan for mild-to-moderate migraine with or without aura |
| [9482363](https://pubmed.ncbi.nlm.nih.gov/9482363/) | 1998 | Randomized Controlled Trial | *Archives of Neurology* | Three double-blind, placebo-controlled trials assessing the acetaminophen + aspirin + caffeine (AAC) combination; demonstrated significant headache pain relief versus placebo |
| [10321417](https://pubmed.ncbi.nlm.nih.gov/10321417/) | 1999 | RCT Analysis | *Clinical Therapeutics* | Retrospective pooled analysis of 3 placebo-controlled RCTs on AAC combination for menstruation-associated migraine; efficacy comparable to non-menstrual migraine episodes |
| [39493026](https://pubmed.ncbi.nlm.nih.gov/39493026/) | 2024 | Review | *Cureus* | Review of abortive and prophylactic therapies for migraine in pregnancy; acetaminophen highlighted as the preferred first-line symptomatic option given its safety profile |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Narrative Review | *Handbook of Clinical Neurology* | Covers status migrainosus as a complication of migraine with or without aura; examines treatment approaches including analgesics |
| [30470274](https://pubmed.ncbi.nlm.nih.gov/30470274/) | 2019 | Review | *Neurologic Clinics* | Headache management in pregnancy and puerperium; explicitly identifies acetaminophen as first-line symptomatic treatment across migraine subtypes |
| [37123778](https://pubmed.ncbi.nlm.nih.gov/37123778/) | 2023 | Review | *Cureus* | Migraine treatment during pregnancy and breastfeeding; discusses role of analgesics including acetaminophen across migraine stages including aura |
| [33525313](https://pubmed.ncbi.nlm.nih.gov/33525313/) | 2021 | Review | *Neurology International* | Contextualizes acetaminophen and NSAIDs as standard non-prescription first-line agents for mild-to-moderate migraine within the broader acute treatment landscape |
| [36197571](https://pubmed.ncbi.nlm.nih.gov/36197571/) | 2022 | Literature Review | *Current Pain and Headache Reports* | Examines post-COVID headache mechanisms and treatment; discusses overlap with primary headache disorders and analgesic use including acetaminophen |

---

## Philippines Market Information

Acetaminophen currently has **no registered products** in the Philippines FDA database (0 authorizations, market status: Not Marketed).

> Acetaminophen (paracetamol) is a globally recognized OTC analgesic available in most international markets; however, no registration records were returned from the Philippines FDA query conducted for this report. Independent verification via the Philippines FDA online portal is recommended before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although acetaminophen is an established first-line analgesic for general migraine supported by clinical guidelines and RCT data (L3), there are no registered clinical trials or dedicated studies specifically addressing **migraine with brainstem aura** as a distinct subtype — and the existing 20 publications do not differentiate MBA from broader migraine cohorts. The absence of Philippines market registration and MBA-specific evidence precludes a recommendation for immediate clinical deployment.

**To proceed, the following is needed:**
- Dedicated observational studies or sub-group analyses from existing migraine RCTs that stratify outcomes by MBA versus non-MBA patients
- Mechanism of action (MOA) data from DrugBank to formally confirm the COX-3 / descending serotonin pathway hypothesis in the brainstem context
- Philippines FDA registration and official package insert to assess local safety warnings, contraindications, and approved dose ranges
- Hepatotoxicity risk monitoring protocol appropriate for migraine management settings (frequency and duration of acetaminophen use)
- Clarification of whether triptans' historical caution in basilar-type migraine creates a therapeutic niche where acetaminophen's non-vasoconstrictive mechanism offers a clinical advantage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

