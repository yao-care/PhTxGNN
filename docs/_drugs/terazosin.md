---
layout: default
title: Terazosin
parent: 僅模型預測 (L5)
nav_order: 326
evidence_level: L5
indication_count: 10
---

# Terazosin
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

# Terazosin: From Hypertension / Benign Prostatic Hyperplasia to Raynaud Disease

## One-Sentence Summary

Terazosin is a selective α1-adrenergic receptor antagonist used to treat hypertension and benign prostatic hyperplasia (BPH) by relaxing smooth muscle in blood vessels and the prostate.
The TxGNN model identifies it as a repurposing candidate for **Raynaud Disease** (TxGNN score 99.83%), with **1 controlled clinical study** and a mechanistically direct receptor-level rationale supporting this direction.
Among the top-10 TxGNN predictions, Raynaud disease carries the strongest clinical evidence (L3) and the only actionable recommendation in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / Benign Prostatic Hyperplasia |
| Predicted New Indication | Raynaud Disease |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank source included in this evidence pack. Based on established pharmacology, terazosin is a selective α1-adrenergic receptor antagonist. By competitively blocking α1 receptors on vascular smooth muscle and prostatic stroma, it causes vasodilation, reduces peripheral vascular resistance, and relaxes urethral tone — the mechanisms underlying its approval for hypertension and BPH respectively.

Raynaud disease (primary Raynaud phenomenon) is defined by episodic, reversible vasospasm of the digital arteries and arterioles triggered by cold or emotional stress. The core pathophysiology involves α1-adrenergic receptor hyperactivation leading to excessive, sustained vasoconstriction. Terazosin's primary receptor target is therefore in direct opposition to the disease-driving mechanism, making this one of the most mechanistically coherent drug-disease pairs in the entire prediction set. This is not a knowledge-graph topological artefact — it is a genuine pharmacological intersection.

Class-effect precedent further reinforces the rationale: prazosin, the first-generation prototype of the same drug class, has published studies demonstrating benefit in Raynaud phenomenon. Terazosin, as a second-generation agent with an improved half-life (~12 hours) and once-daily dosing, could offer a more convenient therapeutic profile for a chronic condition requiring long-term prophylaxis.

> **Note on other TxGNN predictions in this pack:** Rankings 1–4 (hypotrichosis simplex, congenital hypotrichosis milia, diffuse alopecia areata, alopecia) are almost certainly knowledge-graph topology artefacts — hair disorder nodes cluster together in the TxGNN graph, and terazosin is adjacent due to indirect associations rather than a true mechanistic path. Rankings 5–6 (migraine disorder, migraine with brainstem aura) represent a biologically plausible but speculative hypothesis (cranial vascular α1-mediated tone modulation) with very limited 1990s open-label data and no modern trials. Raynaud disease stands apart as the only prediction with a direct, well-characterised mechanistic link and a controlled human study.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [9273472](https://pubmed.ncbi.nlm.nih.gov/9273472/) | 1997 | Controlled Clinical Study | Minerva cardioangiologica | Terazosin significantly reduced the frequency, intensity, and duration of vasospastic attacks in patients with both idiopathic and secondary Raynaud phenomenon; telethermographic and ultrasonographic findings showed objective improvement |

---

## Philippines Market Information

Terazosin is currently **not registered** in the Philippines. No product authorization records are available (0 active licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Terazosin's α1-adrenergic blockade directly targets the pathophysiological mechanism driving Raynaud vasospasm, and a controlled clinical study provides preliminary human evidence of benefit. Class-effect support from prazosin is well-established. However, the supporting literature is over 25 years old, the study sample sizes are small, and the drug is not currently marketed in the Philippines — all of which require mitigation before clinical adoption.

**To proceed, the following is needed:**
- Retrieve full package insert (key warnings and contraindications) from the Philippine FDA or originator label — required for S1 safety screening (Data Gap DG001, Blocking)
- Confirm mechanism of action via DrugBank API query (Data Gap DG002)
- Drug-drug interaction assessment, particularly with agents commonly co-prescribed in secondary Raynaud (e.g., calcium channel blockers in systemic sclerosis, immunosuppressants)
- Evaluate orthostatic hypotension risk in the Philippine patient population, where combination antihypertensive therapy is common
- Assess Philippine FDA registration pathway for a currently unregistered drug (import licence or new drug application)
- Commission a prospective observational study or small controlled trial in Filipino patients with Raynaud phenomenon to generate contemporary, local-population evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

