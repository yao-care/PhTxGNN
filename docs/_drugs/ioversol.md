---
layout: default
title: Ioversol
parent: 僅模型預測 (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
---

# Ioversol
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

---

# Ioversol: From Diagnostic Imaging Agent to Osteoarthritis Susceptibility

## One-Sentence Summary

Ioversol is a nonionic, low-osmolar, water-soluble iodinated contrast medium widely used in diagnostic procedures such as angiography, urography, and CT enhancement — with no formal registered indication in the Philippines. The TxGNN model ranks **Osteoarthritis Susceptibility** as its top predicted new indication (score: 99.67%), but this prediction is mechanistically implausible, as osteoarthritis susceptibility is a genetic risk phenotype rather than a treatable clinical disease entity. There are currently **0 clinical trials** and **0 publications** directly linking Ioversol to osteoarthritis susceptibility; the nearest supporting evidence for osteoarthritis (rank #2) involves a structurally distinct iodinated compound (Lipiodol) performing an embolization function that Ioversol is physically incapable of replicating.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered indication in the Philippines |
| Predicted New Indication | Osteoarthritis Susceptibility (TxGNN Rank #1) |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on established pharmacology, Ioversol (commercially known as Optiray®) is a second-generation nonionic iodinated contrast medium. It distributes into extracellular fluid and is rapidly cleared by glomerular filtration without meaningful metabolism. Unlike conventional drugs, Ioversol does not bind to a receptor or enzyme — its imaging utility derives entirely from X-ray attenuation by iodine atoms. It has no pharmacodynamic target and therefore no conventional mechanism through which "drug repurposing" in the traditional sense would apply.

**The top TxGNN prediction is mechanistically implausible.** "Osteoarthritis susceptibility" represents genetic predisposition driven by variants in loci such as GDF5, ALDH1A2, and TGFB1 — these govern cartilage development and degradation at the genomic level. A water-soluble contrast agent excreted within hours of administration has no known capacity to modulate gene expression, epigenetic regulation, or chondrocyte differentiation pathways. This is not a treatable phenotype via pharmacological agents of this class.

The model's predictions most likely arise from knowledge graph connections between iodinated compounds and musculoskeletal conditions, possibly due to structural or categorical conflation between Ioversol (water-soluble, half-life ~2 hours, no embolization capacity) and Lipiodol (oil-based, lipophilic ethiodized oil, currently under active investigation as a Genicular Artery Embolization agent for knee osteoarthritis pain). These are fundamentally different compounds with incompatible physical and pharmacological properties. The rank #2 prediction (osteoarthritis) has more clinical grounding, but suffers from the same compound-identity problem — all supporting trials use Lipiodol, not Ioversol.

---

## Clinical Trial Evidence

> ⚠️ **No clinical trials were found for the top-ranked prediction (Osteoarthritis Susceptibility).** The trials below are retrieved from the rank #2 prediction (Osteoarthritis) and all test **Lipiodol or the GAE procedure** as the intervention — Ioversol is not the active therapeutic agent. Relevance to Ioversol is indirect at best.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06497140](https://clinicaltrials.gov/study/NCT06497140) | Phase 3 | Recruiting | 130 | Randomized sham-controlled multicenter trial of Genicular Artery Embolization (GAE) for symptomatic knee osteoarthritis. Evaluates the embolization procedure itself; Ioversol, if used, would serve only as a guiding contrast agent rather than the active therapeutic component. |
| [NCT04733092](https://clinicaltrials.gov/study/NCT04733092) | Phase 1 | Completed | 22 | Prospective study of Lipiodol emulsion embolization for inflammatory hypervascularization in knee joint/abarticular pain. Completed Phase 1 provides early safety data for the oil-based embolization concept. Uses Lipiodol, not Ioversol. |
| [NCT06611007](https://clinicaltrials.gov/study/NCT06611007) | Phase 1/2 | Recruiting | 15 | Safety and efficacy evaluation of Lipiodol® arterial embolization in symptomatic digital (hand) osteoarthritis refractory to conventional treatment. Expands embolization approach from knee to hand joints; estimated completion July 2028. |
| [NCT06859164](https://clinicaltrials.gov/study/NCT06859164) | Phase 2 | Recruiting | 50 | NIH-NIAMS funded sham-controlled pilot study (SHAM-PAIN) of GAE for reduction of knee OA pain at 3 months, measured by the KOOS pain subscore. Assesses enrollment feasibility and magnitude of pain response between GAE and sham intervention. |

---

## Literature Evidence

> ⚠️ No publications directly linking Ioversol to osteoarthritis or osteoarthritis susceptibility were identified. The publication below is from the rank #2 prediction (Osteoarthritis) and concerns Lipiodol-based GAE.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [38102013](https://pubmed.ncbi.nlm.nih.gov/38102013/) | 2024 | Phase 1 RCT | Diagnostic and Interventional Imaging | LipioJoint-1 trial: evaluates safety and efficacy of transient Genicular Artery Embolization using an ethiodized oil-based emulsion for knee osteoarthritis. Provides proof-of-concept for iodinated oil-based embolization in OA pain relief, but the active agent is Lipiodol — not Ioversol. |

---

## Safety Considerations

Please refer to the package insert for safety information. As Ioversol is not currently registered in the Philippines, prescribers should consult the manufacturer's prescribing information (e.g., Optiray® package insert) directly for complete warnings, contraindications, and drug interactions. General iodinated contrast medium safety considerations — including risk of contrast-induced nephropathy, hypersensitivity and anaphylactoid reactions, and special precautions in patients with sickle cell disease or renal impairment — should be reviewed prior to any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction targets a genetic risk phenotype (osteoarthritis susceptibility) that is fundamentally not amenable to pharmacological intervention with a contrast agent, and zero clinical or mechanistic evidence supports this repurposing direction for Ioversol; the nearest existing evidence involves a chemically distinct oil-based compound (Lipiodol) performing an embolization function that water-soluble Ioversol is incapable of replicating.

**To proceed, the following is needed:**
- **Knowledge graph audit:** Investigate whether TxGNN's knowledge graph conflates Ioversol with Lipiodol or other iodinated contrast compounds within musculoskeletal disease nodes — if confirmed, this constitutes a model misclassification requiring correction upstream
- **Safety documentation:** Obtain the current Optiray® (Ioversol) prescribing information to complete the mandatory safety assessment (key warnings, contraindications, DDI)
- **Mechanistic feasibility check:** If the question of iodinated contrast agents in OA is worth pursuing, design dedicated in vitro studies to examine whether iodine species modulate synoviocyte inflammation or chondrocyte metabolism at clinically relevant concentrations
- **Philippines registration review:** Confirm current regulatory pathway and registration requirements for Ioversol in the Philippines before considering any clinical application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

