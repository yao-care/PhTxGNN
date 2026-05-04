---
layout: default
title: Bromazepam
parent: 僅模型預測 (L5)
nav_order: 47
evidence_level: L5
indication_count: 1
---

# Bromazepam
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

# Bromazepam: From Anxiolytic Use to Migraine Disorder

## One-Sentence Summary

Bromazepam is a benzodiazepine-class drug primarily used as an anxiolytic and sedative, acting on the central nervous system to reduce anxiety and tension.
The TxGNN model predicts it may have relevance to **Migraine Disorder**; however, the only retrieved clinical trial (1 trial, 0 publications) actually involves bromazepam as a **target of withdrawal** rather than as a treatment — making this prediction mechanistically counter-indicative.
The overall evidence base does not support repurposing, and the recommendation is a firm **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anxiolytic / sedative (benzodiazepine class; no Philippines registration on file) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Bromazepam belongs to the benzodiazepine class and acts as a positive allosteric modulator of GABA-A receptors, enhancing GABAergic inhibitory neurotransmission throughout the central nervous system. In theory, GABAergic modulation has an indirect relationship with migraine pathophysiology: cortical spreading depression (CSD) — the electrophysiological basis of the migraine aura — is partly influenced by the excitation–inhibition balance, and central pain thresholds are modulated by GABAergic tone. This is the mechanistic basis on which the TxGNN model may have generated the prediction.

However, the theoretical link does not translate into a supportive clinical rationale. Benzodiazepines are absent from all major migraine treatment guidelines (acute or preventive) at any line of therapy. More critically, **long-term or frequent benzodiazepine use is a well-established risk factor for Medication Overuse Headache (MOH)** — a condition that worsens migraine frequency and is difficult to reverse. The evidence actually runs in the **opposite direction**: benzodiazepines worsen migraine outcomes at the population level.

Currently, no mechanism-of-action (MOA) data is available in the Evidence Pack. Based on known pharmacology, Bromazepam's GABAergic mechanism provides a theoretical but **counter-indicative** link to migraine disorder. The signal from the TxGNN model likely reflects network proximity in the knowledge graph rather than a genuine therapeutic opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT04410536](https://clinicaltrials.gov/study/NCT04410536) | Phase 4 | Completed | 25 | Home-withdrawal programme combined with behavioural therapy for Medication Overuse Headache (MOH) during COVID-19. **Critical context: Bromazepam's role in this trial is most likely as one of the overused drugs being withdrawn, not as a treatment intervention.** The trial evaluates relapse rates after withdrawal, providing an indirect and inverse signal — benzodiazepine overuse contributes to MOH, and discontinuation is the therapeutic goal. |

> **Note:** The single retrieved trial provides no supportive evidence for bromazepam as a migraine treatment. Its relevance grade is C (indirect/counter-indicative).

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No key warnings, contraindications, or drug interaction data were available in this Evidence Pack. Given that bromazepam is a Schedule IV controlled substance (benzodiazepine), known class-level concerns include dependence, tolerance, withdrawal syndrome, CNS depression, and paradoxical reactions. These concerns are particularly relevant in the context of chronic migraine patients, who are at elevated risk of medication overuse.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high numerical score (99.06%), but the mechanistic and clinical evidence is not only absent — it is actively counter-indicative. Bromazepam is a known contributor to Medication Overuse Headache, the only clinical trial retrieved is about *withdrawing* bromazepam in headache patients, and no published literature supports its use as a migraine treatment. The drug is also not registered in the Philippines, removing any regulatory shortcut.

**To reconsider, the following would be needed:**

- Prospective preclinical data (animal models of CSD or trigeminovascular activation) demonstrating that GABA-A modulation via bromazepam reduces migraine endpoints — this evidence does not currently exist
- A mechanistic explanation for why this specific benzodiazepine would differ from the class-wide pattern of worsening headache with chronic use
- Clarification of MOA data from DrugBank (currently a data gap) to assess whether any unique molecular target could justify differentiation from the benzodiazepine class
- Evidence that the TxGNN knowledge graph edge driving this prediction is not confounded by co-occurrence of "benzodiazepine + headache" in MOH literature (i.e., a signal from harm, not benefit)

> **Bottom line:** This candidate should not advance to safety screening (S1) at this time. The TxGNN score reflects graph topology, not biological plausibility. Reassign to the inactive watchlist.

---

*This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

