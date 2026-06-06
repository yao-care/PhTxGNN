---
layout: default
title: Sumatriptan
parent: 僅模型預測 (L5)
nav_order: 318
evidence_level: L5
indication_count: 1
---

# Sumatriptan
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

# Sumatriptan: From Acute Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Sumatriptan is a selective serotonin 5-HT1B/1D receptor agonist widely established for the acute treatment of migraine attacks, including migraine with and without aura.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura (MBwA)** — a distinct migraine subtype previously termed basilar-type migraine — with **no registered clinical trials** but **18 publications** offering indirect mechanistic and clinical evidence.
However, this prediction carries a critical safety caveat: triptans have historically been listed as a relative contraindication in MBwA due to concerns over posterior-circulation vasoconstriction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute migraine (with or without aura) |
| Predicted New Indication | Migraine with Brainstem Aura (MBwA) |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Sumatriptan is a selective agonist at the vascular 5-HT1B/1D receptors. Its primary mechanism involves constriction of dilated intracranial blood vessels and inhibition of neuropeptide release (notably CGRP and Substance P) from perivascular trigeminal axons in the dura mater. This dual action on the trigeminovascular system is the cornerstone of its efficacy in acute migraine.

Migraine with Brainstem Aura (MBwA) shares the same core trigeminovascular pathophysiology as common migraine, but its aura symptoms — dysarthria, diplopia, ataxia, tinnitus, and decreased level of consciousness — arise from the brainstem and posterior circulation rather than from the cortex. Because the underlying neuronal and vascular pathways overlap significantly with those targeted by sumatriptan, the TxGNN model's high prediction score is mechanistically coherent. Real-world reports (e.g., PMID 11903526) confirm that some clinicians have used triptans in basilar migraine with apparent benefit.

The critical qualification is that MBwA's involvement of the posterior circulation creates a theoretical vasospasm risk that led the International Headache Society (pre-2004 guidelines) to categorize triptans as a relative contraindication. This concern has since been questioned — a 2001 case series found triptans were used without documented adverse events — but no prospective randomised data exist for MBwA specifically. The prediction is therefore plausible but requires formal safety investigation before any clinical recommendation can be made.

---

## Clinical Trial Evidence

Currently no clinical trials specifically investigating Sumatriptan in Migraine with Brainstem Aura are registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11903526](https://pubmed.ncbi.nlm.nih.gov/11903526/) | 2001 | Case Series / Report | *Headache* | Directly addresses triptans in **basilar migraine** (MBwA) and migraine with prolonged aura; reports on real-world use of triptans in patients with prominent neurological symptoms |
| [1313746](https://pubmed.ncbi.nlm.nih.gov/1313746/) | 1992 | RCT | *Cephalalgia* | Double-blind, placebo-controlled RCT assessing sumatriptan 200 mg oral in **migraine with aura**; demonstrated 70–85% efficacy rates |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Observational Study | *Neurology* | Systematically compared sumatriptan outcomes in migraine with aura vs. without aura; found **reduced efficacy** in the aura subgroup — directly relevant to MBwA safety/efficacy inference |
| [23657930](https://pubmed.ncbi.nlm.nih.gov/23657930/) | 2014 | RCT | *Phytotherapy Research* | Double-blind RCT (n=100) comparing ginger powder vs. sumatriptan in acute migraine without aura; comparable efficacy with fewer side effects reported for ginger |
| [11318886](https://pubmed.ncbi.nlm.nih.gov/11318886/) | 2001 | Comparative Study | *Headache* | Compared sumatriptan succinate vs. isometheptene/dichloralphenazone/acetaminophen combination in mild-to-moderate migraine with or without aura |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Systematic Review | *Headache* | American Headache Society evidence assessment of acute migraine pharmacotherapies; establishes sumatriptan as a first-line agent with high evidence grade |
| [8536293](https://pubmed.ncbi.nlm.nih.gov/8536293/) | 1995 | Review | *Cephalalgia* | Comprehensive review of sumatriptan's mechanism (5-HT1 vasoconstriction and neuropeptide inhibition) and clinical experience in migraine and cluster headache |
| [9556832](https://pubmed.ncbi.nlm.nih.gov/9556832/) | 1998 | Review | *Schweiz Med Wochenschr* | Discusses migraine treatment (with and without aura), acute vs. preventive strategies, and notes that sumatriptan is not clearly superior to analgesics in group studies |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | *Handbook of Clinical Neurology* | Reviews status migrainosus (>72h attacks), a severe migraine complication — contextualises the spectrum of migraine severity where triptans are used |
| [27910087](https://pubmed.ncbi.nlm.nih.gov/27910087/) | 2017 | Review | *Headache* | Review of treatment options for menstrual migraine, including triptan use in hormonally-triggered aura-positive subtypes |

---

## Philippines Market Information

Sumatriptan currently has **no drug product registrations** with the Philippine Food and Drug Administration (FDA Philippines). The drug is not commercially available through licensed domestic channels.

---

## Safety Considerations

Detailed local package insert data (warnings and contraindications) are not available for the Philippine market, as the product is not registered. The following safety concern is directly relevant to the predicted indication and is drawn from the repurposing rationale:

- **Critical Safety Flag — Posterior Circulation Vasospasm Risk**: MBwA involves the brainstem and posterior circulation. Triptans cause vasoconstriction of cranial vessels; applying this mechanism to the posterior circulation raises a theoretical risk of brainstem ischemia. Pre-2004 IHS guidelines listed basilar-type migraine as a contraindication for triptans. While this restriction has been softened and real-world triptan use in MBwA has not consistently demonstrated harm, the lack of prospective safety data means this risk cannot be dismissed.

For full prescribing information (warnings, contraindications, drug interactions), consult the originator package insert from a jurisdiction where sumatriptan is registered (e.g., US FDA label, EMA SmPC).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials have specifically evaluated sumatriptan in Migraine with Brainstem Aura, and the evidence base (L4) consists entirely of indirect literature — including reviews and studies in related but distinct migraine subtypes. More critically, a well-documented historical safety concern (posterior-circulation vasoconstriction risk) has not been adequately resolved by prospective data, making clinical use in MBwA premature without further investigation.

**To proceed, the following is needed:**

- **Safety evidence**: Prospective or registry-based data specifically in MBwA patients treated with sumatriptan, documenting vascular adverse events
- **Mechanism clarification**: Formal MOA data (DrugBank/literature) confirming receptor expression profile in posterior-circulation neurons vs. cortical trigeminovascular system
- **Guideline review**: Current IHS/AHS position on triptan use in MBwA (post-2013 reclassification); assess whether the historic contraindication has been formally lifted
- **Philippine regulatory pathway**: If evidence supports proceeding, file for FDA Philippines registration; identify a licensed importer or local distributor willing to pursue registration
- **Clinical trial design**: If mechanistic and safety signals are positive, design a small Phase 2 RCT or prospective registry study in MBwA patients to establish efficacy and safety as a primary endpoint
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

