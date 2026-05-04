---
layout: default
title: Dextromethorphan
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L5
indication_count: 6
---

# Dextromethorphan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Dextromethorphan: From Cough Suppression to Nasal Cavity Disease

## One-Sentence Summary

Dextromethorphan (DXM) is a widely used antitussive agent that suppresses cough via NMDA receptor antagonism in the brainstem cough centre.
The TxGNN model predicts it may be effective for **Nasal Cavity Disease**, with **1 clinical trial** retrieved and **0 publications** currently supporting this direction — though the retrieved trial targets Major Depressive Disorder, not nasal cavity disease directly, and should be interpreted with caution.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Antitussive (cough suppression) — no Philippines FDA registration found |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L2 (see note in Clinical Trial section) |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmacological knowledge, Dextromethorphan acts as a non-competitive NMDA receptor antagonist and Sigma-1 receptor agonist. Its proven efficacy as an antitussive — suppressing the brainstem cough centre — shares overlapping neural circuitry with upper airway sensory processing, which makes the mechanistic jump to nasal cavity pathology conceptually plausible.

Nasal cavity disease encompasses a spectrum of conditions — allergic rhinitis, vasomotor rhinitis, nasal polyps, and chronic rhinosinusitis — many of which involve neurogenic mucosal inflammation and hyperreactivity. DXM's NMDA antagonism may dampen afferent sensory signalling from nasal mucosa and reduce neurogenic inflammation. Separately, Sigma-1 receptor agonism has been associated in preclinical studies with immunomodulatory activity, including modulation of mast cell calcium signalling and T-cell activation, which could theoretically attenuate mucosal immune responses.

That said, the biological plausibility remains largely theoretical. Nasal cavity disease frequently has structural, infectious, or IgE-mediated aetiologies for which DXM has no established therapeutic activity. The high TxGNN score likely reflects anatomical proximity in the knowledge graph — DXM's nasal cavity node sits adjacent to upper respiratory tract nodes — rather than a fully validated disease-modifying mechanism. No direct preclinical or clinical studies targeting nasal cavity disease with DXM have been identified.

---

## Clinical Trial Evidence

> ⚠️ **Important caveat:** The single retrieved trial (NCT06958692) is designed for **Major Depressive Disorder (MDD)**, not nasal cavity disease. It was retrieved based on the drug name "Dextromethorphan" and likely represents a retrieval artefact. The Evidence Pack's L2 rating reflects the existence of an ongoing Phase 3 trial for DXM (as part of a combination product), but this trial provides no direct evidence for nasal cavity disease. True evidence level for this indication is closer to **L5**.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06958692](https://clinicaltrials.gov/study/NCT06958692) | Phase 3 | Recruiting | 388 | Multicenter, randomized, double-blind, placebo-controlled trial evaluating DXM + bupropion sustained-release tablets in Chinese adult patients with **Major Depressive Disorder** — not nasal cavity disease |

---

## Literature Evidence

Currently no related literature available for Dextromethorphan in nasal cavity disease.

---

## Philippines Market Information

Dextromethorphan is currently **not registered** with the Philippines FDA. No product authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: Philippines FDA package insert warnings, contraindications, and drug interaction data were not available at the time of this report (Data Gaps DG001 and DG002). This is classified as a **Blocking** gap for formal safety screening.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN model assigns a very high prediction score (99.98%) for DXM in nasal cavity disease, and the NMDA antagonism / Sigma-1 agonism mechanism is biologically plausible for upper airway neurogenic inflammation. However, no direct clinical or literature evidence exists for this indication, the single retrieved trial addresses Major Depressive Disorder rather than nasal cavity disease, and DXM is not currently registered in the Philippines — meaning significant regulatory and evidence gaps must be addressed before any formal repurposing decision.

**To proceed, the following is needed:**

- **Targeted evidence search:** Commission a structured literature review (PubMed, EMBASE) specifically querying DXM against rhinitis, nasal hyperreactivity, and neurogenic nasal inflammation
- **Mechanism of action data:** Retrieve full MOA from DrugBank API (Data Gap DG002) to confirm whether NMDA/Sigma-1 pharmacology has documented upper airway effects
- **Safety dossier:** Download Philippines FDA package insert PDF and parse warnings and contraindications (Data Gap DG001 — currently Blocking)
- **Preclinical evidence review:** Assess whether any in vitro or animal studies have evaluated DXM's effect on nasal mucosal tissue or NMDA receptor activity in the upper airway
- **Regulatory feasibility:** Determine Philippines FDA pathway for market entry, given zero existing registrations
- **Trial re-classification:** Confirm that NCT06958692 does not contain any nasal cavity sub-endpoints before excluding it as indirect evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

