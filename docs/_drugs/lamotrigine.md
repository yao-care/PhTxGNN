---
layout: default
title: Lamotrigine
parent: 僅模型預測 (L5)
nav_order: 196
evidence_level: L5
indication_count: 9
---

# Lamotrigine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Lamotrigine: From Epilepsy to Trigeminal Neuralgia

## One-Sentence Summary

Lamotrigine is a broad-spectrum antiseizure medication well established globally for epilepsy and bipolar disorder, but not currently registered in the Philippines.
The TxGNN model's most clinically meaningful prediction is **Trigeminal Neuralgia**, supported by **4 clinical trials** and **19 publications** — with the 2019 European Academy of Neurology guideline explicitly listing lamotrigine as a second-line option.
The top-ranked TxGNN prediction (trigeminal nerve neoplasm, Rank 1) has been identified as a knowledge graph topology artifact and is not clinically actionable.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy and bipolar disorder (not registered in the Philippines) |
| Predicted New Indication | Trigeminal Neuralgia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Philippines Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack. Based on established pharmacological knowledge, lamotrigine is a broad-spectrum antiseizure medication that works primarily by blocking voltage-gated sodium (Na⁺) channels in a state-dependent (use-dependent) manner. By stabilizing hyperexcitable neuronal membranes and preventing rapid repetitive firing, it also reduces pathological glutamate release at synapses — a mechanism directly applicable to neuropathic pain conditions.

Trigeminal neuralgia is one of the most painful conditions known, characterized by paroxysmal, electric shock-like facial pain caused by ectopic discharges in the trigeminal nerve. The trigeminal ganglion highly expresses Nav1.7 and Nav1.3 voltage-gated Na⁺ channels. Lamotrigine's blockade of these channels can suppress the ectopic discharges responsible for pain paroxysms and reduce glutamate release at the spinal trigeminal nucleus caudalis. This mechanism closely parallels carbamazepine — the standard first-line treatment for trigeminal neuralgia — but with potentially greater channel selectivity and a more favorable tolerability profile, particularly in patients with multiple sclerosis.

This is not merely a theoretical connection. The European Academy of Neurology (EAN) 2019 guideline explicitly recommends lamotrigine as a second-line option for trigeminal neuralgia. Completed Phase 2/3 trial data directly comparing lamotrigine to carbamazepine exist, and real-world case reports confirm its successful use in refractory patients. The TxGNN prediction reflects an established, evidence-backed off-label application rather than a speculative hypothesis.

> **⚠️ Note on Rank 1 Prediction (Trigeminal Nerve Neoplasm):** The TxGNN model's highest-ranked output (score 99.97%) was "trigeminal nerve neoplasm." This has been identified as a **knowledge graph topology artifact** — the high score reflects the graph's semantic proximity between the "trigeminal neuralgia" and "trigeminal nerve neoplasm" nodes (both share the trigeminal nerve anatomical pathway), not any anti-tumor mechanism of lamotrigine. Lamotrigine has no known antineoplastic activity. This prediction is classified **Hold (L5 / S0)** and excluded from the main clinical analysis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) | Phase 2/3 | Completed | 21 | Direct head-to-head comparison of lamotrigine vs carbamazepine (gold standard) in trigeminal neuralgia — the most rigorous comparative trial available for this indication |
| [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) | N/A | Completed | 20 | Double-blind, placebo-controlled add-on study of Lamictal (lamotrigine) in trigeminal neuralgia — evaluates attack frequency reduction and tolerability vs placebo |
| [NCT00243152](https://clinicaltrials.gov/study/NCT00243152) | N/A | Completed | 6 | fMRI-based study of lamotrigine effects on neuropathic facial pain — provides neuroimaging evidence for central mechanism of action |
| [NCT04996199](https://clinicaltrials.gov/study/NCT04996199) | Phase 4 | Unknown | 132 | Carbamazepine vs oxcarbazepine for trigeminal neuralgia — active research context; no lamotrigine arm |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | European Journal of Neurology | EAN guideline on trigeminal neuralgia — explicitly lists lamotrigine as a second-line pharmacological option with formal evidence grading |
| [37892981](https://pubmed.ncbi.nlm.nih.gov/37892981/) | 2023 | Systematic Review | Biomedicines | Umbrella review of TN drug therapies; evaluates efficacy and tolerability of lamotrigine alongside other anticonvulsants |
| [21621166](https://pubmed.ncbi.nlm.nih.gov/21621166/) | 2011 | Clinical Study | Journal of the Chinese Medical Association | Direct comparison of lamotrigine vs carbamazepine efficacy and side-effect profile in trigeminal neuralgia patients |
| [30081317](https://pubmed.ncbi.nlm.nih.gov/30081317/) | 2018 | Case Report | Multiple Sclerosis and Related Disorders | Refractory TN in an MS patient successfully managed with pregabalin + lamotrigine combination — real-world evidence for combination use |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Review of Neurotherapeutics | 2024 update on TN pharmacotherapy; discusses the role of lamotrigine and newer agents as alternatives to carbamazepine |
| [34108244](https://pubmed.ncbi.nlm.nih.gov/34108244/) | 2021 | Review | Practical Neurology | Practical clinical guide to TN — covers new diagnostic criteria and medical vs surgical treatment decision-making |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Molecular Pain | Comprehensive pathophysiology-to-pharmacotherapy review; explains the Na⁺ channel mechanisms underlying lamotrigine's applicability to TN |
| [30178160](https://pubmed.ncbi.nlm.nih.gov/30178160/) | 2018 | Review | Drugs | Evidence-based review of current and innovative pharmacological options for both typical and atypical trigeminal neuralgia |
| [34003166](https://pubmed.ncbi.nlm.nih.gov/34003166/) | 2021 | Review | Neurology India | Medical management of TN — discusses the therapeutic role of lamotrigine in the treatment algorithm |
| [25864062](https://pubmed.ncbi.nlm.nih.gov/25864062/) | 2015 | Review | Neurosciences | Update on neuropathic pain treatment and surgical options for TN; pharmacotherapy review includes lamotrigine |

---

## Philippines Market Information

Lamotrigine is currently **not registered or marketed in the Philippines**. No product authorizations were found in the Philippines FDA database. Any clinical use would require a compassionate use permit or special import authorization.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Lamotrigine's sodium channel–blocking mechanism directly addresses the pathophysiology of trigeminal neuralgia, and this is not speculative — the EAN 2019 guideline formally lists it as a second-line option, and completed Phase 2/3 trial data comparing it head-to-head with carbamazepine are available. The L2 evidence base is sufficient to justify further development and clinical consideration, contingent on the gaps below being addressed.

**To proceed, the following is needed:**

- **Full safety review**: Retrieve and review the lamotrigine package insert — particularly the serious skin reaction risk (Stevens-Johnson syndrome, toxic epidermal necrolysis), the mandatory slow dose titration schedule, and interactions with hepatic enzyme inducers/inhibitors (e.g., carbamazepine, valproate)
- **Philippines regulatory pathway**: Confirm import permit, compassionate use authorization, or registration requirements for a drug currently not marketed in the Philippines
- **Drug interaction assessment**: Conduct a formal DDI review with medications commonly co-prescribed in TN (carbamazepine, oxcarbazepine, pregabalin, tricyclic antidepressants)
- **Dose titration protocol**: Develop a clinical protocol for slow lamotrigine uptitration appropriate for TN management, including interim pain control strategy given titration duration
- **Larger confirmatory evidence**: The core comparative trial (NCT00913107, n=21) is small; a larger RCT or meta-analysis specifically addressing lamotrigine vs carbamazepine would be needed to upgrade evidence from L2 to L1 for registration purposes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

