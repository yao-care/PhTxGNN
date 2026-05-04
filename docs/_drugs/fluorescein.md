---
layout: default
title: Fluorescein
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 10
---

# Fluorescein
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

# Fluorescein: From Ophthalmic Diagnostic Dye to Prinzmetal Angina

## One-Sentence Summary

Fluorescein (DB00693) is a xanthene fluorescent dye used exclusively as a diagnostic imaging agent in ophthalmic and vascular fluorescein angiography — it has no currently approved therapeutic indication.
The TxGNN model predicts it may be effective for **Prinzmetal Angina** (variant angina caused by coronary artery vasospasm),
with **0 clinical trials** and **0 publications** currently supporting this direction.
Despite a striking prediction score of 99.81%, this appears to be a knowledge graph artifact rather than a genuine repurposing signal — mechanistic and clinical evidence is entirely absent.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved therapeutic indication; used as ophthalmic/vascular diagnostic dye (fluorescein angiography) |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank or other sources. Based on known information, Fluorescein is a xanthene-class fluorescent organic dye (C₂₀H₁₂O₅) administered intravenously or topically as a diagnostic agent. Its clinical role is confined to imaging: after injection, it circulates through blood vessels and fluoresces under blue excitation light, allowing real-time visualization of retinal, choroidal, and other vascular structures. It carries no approved therapeutic indication in any jurisdiction.

Prinzmetal angina (variant angina) is a distinct clinical entity caused by episodic coronary artery vasospasm rather than fixed atherosclerotic obstruction. Established treatments work by relaxing vascular smooth muscle — typically via calcium channel blockade (amlodipine, diltiazem) or nitrate-mediated vasodilation. There is no identified pharmacological mechanism by which fluorescein could inhibit vasospasm, modulate calcium channels, protect vascular endothelium, or reduce sympathetic tone in coronary arteries.

The TxGNN model's high score (0.998, rank 1,828 out of all predictions) almost certainly reflects a **knowledge graph artifact**: fluorescein angiography is routinely used to evaluate cardiovascular and retinal vascular pathology, generating numerous graph co-occurrence edges between the "Fluorescein" node and cardiovascular disease nodes. The model may be interpreting diagnostic co-presence as a therapeutic relationship — a well-documented false-positive pattern in graph-based drug repurposing approaches. The absence of any supporting literature or trial further confirms this interpretation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Fluorescein in Prinzmetal Angina.

---

## Literature Evidence

Currently no related literature available for Fluorescein in Prinzmetal Angina.

---

## Philippines Market Information

Fluorescein (DB00693) currently has no registered drug products with the Philippine FDA and is not marketed in the Philippines. No authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Fluorescein has no plausible mechanism of action for Prinzmetal angina, zero supporting clinical trials or publications, and is not available on the Philippine market. The 99.81% TxGNN prediction score is a knowledge graph artifact arising from widespread diagnostic co-use of fluorescein angiography in vascular medicine — not a therapeutic signal.

**To proceed, the following would be needed:**
- Basic pharmacological characterization: investigate whether fluorescein or any metabolite produces any measurable effect on vascular smooth muscle tone, L-type calcium channels, or coronary endothelial function in vitro
- Full mechanism of action (MOA) data retrieval from DrugBank API and primary literature
- Pre-clinical proof-of-concept studies (animal vasospasm models) before any clinical consideration
- Complete safety profile review for systemic exposure doses relevant to a therapeutic context (current diagnostic intravenous doses are very low; therapeutic dosing would be undefined)
- Clarification of the KG graph topology to determine whether the Fluorescein–cardiovascular disease edges are diagnostic or therapeutic in origin, which may inform model retraining

> ⚠️ **Research Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any application. All predictions scored L5 carry no clinical evidence and should not be advanced without rigorous preclinical investigation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

