---
layout: default
title: Isoflurane
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 7
---

# Isoflurane
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

Using the txgnn-pipeline skill context and the Evidence Pack, I will now generate the report.

---

# Isoflurane: From General Anesthesia to Prinzmetal Angina

## One-Sentence Summary

Isoflurane is a volatile halogenated ether, widely used as an inhaled general anesthetic agent for surgical procedures.
The TxGNN model predicts it may be effective for **Prinzmetal Angina** (vasospastic angina),
with **0 clinical trials** and **0 publications** currently supporting this specific direction — this prediction rests on model inference alone.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | General anesthesia (inhaled volatile anesthetic) |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on known pharmacological information, Isoflurane is a halogenated volatile anesthetic that acts primarily via potentiation of inhibitory GABA-A receptors and inhibition of excitatory NMDA receptors, producing CNS depression, muscle relaxation, and cardiovascular effects. It is also known to activate ATP-sensitive potassium (K_ATP) channels in vascular smooth muscle.

The theoretical basis for the Prinzmetal angina prediction lies in Isoflurane's coronary vasodilatory properties — activation of K_ATP channels and nitric oxide (NO) pathways can relax smooth muscle in coronary arteries, which is the same mechanism targeted when treating vasospastic angina (e.g., calcium channel blockers). In Prinzmetal angina, episodic coronary artery spasm causes transient ischemia, and a vasodilatory agent could theoretically abort or prevent such spasms.

However, this prediction carries a critical mechanistic contradiction: Isoflurane is well-documented to induce **coronary steal syndrome** in patients with coronary artery disease, redistributing blood flow away from ischemic myocardium. This dual — and opposing — cardiovascular effect means the net impact on a patient with active coronary vasospasm is unpredictable and potentially dangerous. There is zero clinical or preclinical evidence supporting this use, and the safety profile in ischemic cardiac populations raises significant concern.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Isoflurane has no registered products with the FDA Philippines. No authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Safety data (key warnings, contraindications, and drug interactions) was not retrievable from available sources at the time of this report. Given Isoflurane's known cardiovascular risk profile — particularly coronary steal syndrome in ischemic heart disease — consultation of the full prescribing information is essential before any off-label exploration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.67%) to Prinzmetal angina, but this is a pure model signal with no clinical trial, observational study, or published literature to support it. Moreover, the mechanistic rationale is internally contradictory — Isoflurane may both relax and redistribute coronary blood flow — introducing a plausible safety hazard rather than a therapeutic opportunity.

**To proceed, the following is needed:**

- **MOA data**: Retrieve full DrugBank mechanism-of-action and pharmacodynamics data for Isoflurane to properly assess the K_ATP / NO pathway contribution versus coronary steal risk
- **Safety data**: Obtain full package insert warnings and contraindications (FDA Philippines / originator label) to evaluate cardiovascular risk in non-surgical settings
- **Preclinical evidence**: Conduct a targeted literature review on Isoflurane + coronary vasospasm / coronary artery spasm in animal models before any clinical hypothesis is formed
- **Philippines regulatory path**: Since Isoflurane is not registered in the Philippines, any repurposing effort would need to address market registration alongside indication expansion
- **Alternative indication consideration**: Within this Evidence Pack, **Migraine Disorder** (rank 7, L4, 12 publications — including direct mechanistic studies on CSD suppression and 2 case reports of general anesthesia for status migrainosus) represents a substantially stronger repurposing signal and may be a more actionable research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

