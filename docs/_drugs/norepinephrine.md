---
layout: default
title: Norepinephrine
parent: 僅模型預測 (L5)
nav_order: 254
evidence_level: L5
indication_count: 3
---

# Norepinephrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Norepinephrine: From Vasopressor (Septic Shock) to Obstructive Lung Disease

## One-Sentence Summary

Norepinephrine is an endogenous catecholamine and critical care vasopressor used intravenously for hemodynamic support in septic shock and severe hypotension.
The TxGNN model predicts it may be effective for **Obstructive Lung Disease**, supported by mechanistic animal studies and observational data in COPD patients — though no direct therapeutic clinical trials have yet been conducted to validate this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vasopressor for septic shock / severe hypotension (intravenous infusion) |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, norepinephrine is an endogenous catecholamine that acts predominantly as an α1-adrenergic agonist — causing vasoconstriction — with moderate β1-adrenergic activity, and serves as the primary neurotransmitter of the peripheral sympathetic nervous system.

The mechanistic connection to obstructive lung disease rests on noradrenergic control of airway physiology. Sympathetic nerves regulate airway caliber through α1-receptor-mediated constriction of bronchial vasculature, β2-receptor modulation of smooth muscle tone, and neuropeptide co-transmission affecting mucous glands. A landmark 2024 study in *Nature* (PMID 38987587) demonstrated that brainstem DBH⁺ neurons — the primary source of norepinephrine — directly control allergen-induced airway hyperreactivity, mapping a complete allergen circuit from lung to brainstem and back. This provides direct mechanistic grounding for TxGNN's prediction. Supporting this, classic literature confirms that noradrenergic innervation modulates airway caliber in both asthma and COPD through smooth muscle, bronchial vessels, and glandular secretion (PMID 2048831).

A critical nuance is that in COPD patients, plasma norepinephrine concentrations are significantly elevated and inversely correlated with arterial oxygen saturation (PMID 6777857; PMID 9009625) — indicating that sympathetic overactivation is a pathophysiological feature of disease, not simply a biomarker. This raises an important clinical question: should the therapeutic strategy aim to supplement norepinephrine, to modulate the noradrenergic axis (e.g., via DBH inhibition), or to exploit the brainstem NE circuit for airway control? The overlap with established β2-agonist therapy — which targets the same adrenergic pathway — must be explicitly addressed before a repurposing strategy can be defined. Direct exogenous norepinephrine for airway disease has not been clinically tested.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT02360865](https://clinicaltrials.gov/study/NCT02360865) | N/A | Completed | 18 | Mechanisms of exercise intolerance in COPD — measured NE as a marker of Muscular Sympathetic Nerve Activity; provides mechanistic data on NE's physiological role in COPD vascular regulation during exertion |
| [NCT02564406](https://clinicaltrials.gov/study/NCT02564406) | N/A | Completed | 35 | Extracorporeal CO₂ removal in severe COPD patients refusing intubation — NE used as vasopressor support, reflecting real-world clinical application in end-stage COPD management |
| [NCT01536587](https://clinicaltrials.gov/study/NCT01536587) | Phase 4 | Completed | 32 | Salmeterol bronchodilation and autonomic nervous system in COPD GOLD II–III — assessed sympathetic activity reduction via microneurography; directly relevant to noradrenergic pathway modulation in obstructive disease |
| [NCT01219738](https://clinicaltrials.gov/study/NCT01219738) | N/A | Completed | 20 | Non-genomic effects of inhaled budesonide on adrenergic agonist transport in airway vascular smooth muscle — explicitly studies locally released norepinephrine from noradrenergic nerves in airway tissue; supports NE's direct role in airway physiology |

> **Note:** No clinical trials were identified that directly test norepinephrine as a therapeutic intervention for obstructive lung disease. The above trials provide mechanistic context, not efficacy evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38987587](https://pubmed.ncbi.nlm.nih.gov/38987587/) | 2024 | Animal/Mechanistic | *Nature* | DBH⁺ brainstem neurons (primary NE source) directly control allergen-induced airway hyperreactivity; maps full neuroimmune circuit lung → nTS → lung — strongest mechanistic support for this prediction |
| [2048831](https://pubmed.ncbi.nlm.nih.gov/2048831/) | 1991 | Mechanistic Review | *Am Rev Respir Dis* | Noradrenergic nerves regulate airway caliber in both asthma and COPD via smooth muscle tone, bronchial vasculature, and mucous glands; noradrenergic innervation contributes to airway narrowing |
| [1617386](https://pubmed.ncbi.nlm.nih.gov/1617386/) | 1992 | Mechanistic Review | *Br Med Bull* | NE and neuropeptide-Y mediate sympathetic vasoconstriction of tracheobronchial vasculature in asthma; details the subepithelial capillary network regulation |
| [6777857](https://pubmed.ncbi.nlm.nih.gov/6777857/) | 1980 | Observational | *Scand J Clin Lab Invest* | Plasma noradrenaline significantly elevated in COPD patients, inversely correlated with arterial O₂ saturation — quantifies sympathetic overactivation as a disease component |
| [9009625](https://pubmed.ncbi.nlm.nih.gov/9009625/) | 1996 | Observational | *Monaldi Arch Chest Dis* | Elevated adrenaline and noradrenaline in early COPD with right heart involvement; neuroendocrine hormonal dysregulation present before clinical cardiac failure |
| [29030339](https://pubmed.ncbi.nlm.nih.gov/29030339/) | 2018 | Observational | *Am J Physiol Heart Circ* | Impaired functional sympatholysis (attenuated α-adrenergic vasoconstriction blunting) in COPD patients during exercise; demonstrates that NE pathway responsiveness is altered in COPD |
| [35870527](https://pubmed.ncbi.nlm.nih.gov/35870527/) | 2022 | Observational | *Environ Pollut* | Air pollution triggers dysregulation of sympathetic-adrenal medullary (SAM) axis including NE in COPD patients, linking environmental triggers to noradrenergic pathway activation |
| [40064568](https://pubmed.ncbi.nlm.nih.gov/40064568/) | 2025 | Review | *Allergology Int* | Neuroimmune mechanisms in type 2 skin and airway inflammation; noradrenergic–immune crosstalk in barrier tissues underlies asthma pathophysiology |
| [24486056](https://pubmed.ncbi.nlm.nih.gov/24486056/) | 2014 | Review | *Semin Immunol* | Sympathetic nervous system–immune system interaction; NE modulates inflammatory homeostasis through adrenergic receptors on immune cells — relevant to NE's immunomodulatory role in airway inflammation |
| [28950943](https://pubmed.ncbi.nlm.nih.gov/28950943/) | 2017 | Review | *Adv Immunol* | β2-adrenoceptor function in asthma — documents the adrenergic axis as established therapeutic target and raises safety concerns about long-term agonism; provides critical clinical context for differentiating NE repurposing from existing therapies |

---

## Philippines Market Information

Norepinephrine (DrugBank ID: DB00368) currently has **no registered products** in the Philippines FDA database. There are zero active licenses or marketing authorizations on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Regulatory note:** Philippine FDA package insert data was identified as a blocking data gap (DG001). Safety evaluation cannot proceed until TFDA/PhFDA prescribing information is retrieved and parsed. The Philippines FDA website should be consulted for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model identifies a mechanistically plausible link through noradrenergic control of airway physiology — anchored by a high-impact 2024 *Nature* study demonstrating that DBH⁺ NE neurons directly regulate allergen-induced airway hyperreactivity — but all available clinical evidence is indirect: norepinephrine functions as a hemodynamic support agent or biomarker in COPD trials, not as a direct therapeutic intervention for airway obstruction. With zero Philippines market registrations, no direct therapeutic clinical trials, and a critical unresolved question about the specific repurposing hypothesis (NE supplementation vs. pathway modulation), the evidence is insufficient to advance beyond a research question at this stage.

**To proceed, the following is needed:**

- **Define the therapeutic hypothesis precisely:** Supplementing exogenous NE, modulating DBH⁺ neuronal activity, or targeting downstream noradrenergic receptors are mechanistically distinct strategies requiring separate development paths
- **Preclinical proof-of-concept studies** in obstructive lung disease animal models specifically testing the therapeutic hypothesis (distinct from existing COPD biomarker studies)
- **Differentiation from β2-agonist therapy:** Since salmeterol, formoterol, and related drugs already exploit the same adrenergic pathway, the repurposing rationale must demonstrate added value or a non-overlapping mechanism
- **MOA data retrieval** from DrugBank (Data Gap DG002) to confirm receptor binding profile and enable mechanistic analysis
- **Philippines FDA package insert** retrieval (Data Gap DG001) to complete safety and contraindication profiling before any clinical stage evaluation

---

> **Other Predicted Indications (for reference):**
> TxGNN also flagged **Respiratory Malformation** (rank 2, score 99.84%, L4) — supported by mechanistic evidence that NE system disruption impairs respiratory circuit development (Rett syndrome/Mecp2 mouse models), with a developmental rather than therapeutic repurposing angle. **Rienhoff Syndrome** (rank 3, score 99.83%, L5) was assessed as **Hold** — no mechanistic link between the TGFB3 pathway and NE was identified; the prediction likely reflects indirect knowledge graph associations.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

