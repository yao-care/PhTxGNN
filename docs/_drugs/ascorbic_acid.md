---
layout: default
title: Ascorbic Acid
parent: 僅模型預測 (L5)
nav_order: 29
evidence_level: L5
indication_count: 10
---

# Ascorbic Acid
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

# Ascorbic Acid: From Vitamin C Deficiency to Injury

## One-Sentence Summary

Ascorbic acid (Vitamin C, DrugBank ID: DB00126) is an essential water-soluble vitamin universally recognized for preventing and treating scurvy and vitamin C deficiency.
The TxGNN model predicts it may be effective across **10 diverse disease categories**; the most actionable repurposing candidate is **Injury** (trauma, burns, and surgical injury), supported by **multiple clinical trials including Phase 3** and **20+ publications** documenting its antioxidant and tissue-repair mechanisms.
Overall evidence strength varies widely across the 10 predictions — from L1 (vitamin deficiency disorder, the primary indication) to L5 (five rare or ultra-rare diseases with zero supporting evidence).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vitamin C deficiency / Scurvy (no Philippines regulatory record on file) |
| Primary Predicted New Indication | Injury (burn, trauma, surgical injury) |
| TxGNN Prediction Score | 99.60% (Rank 4 among top 10 predictions) |
| Evidence Level | L2 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Prediction Landscape Overview

The TxGNN model generated 10 ranked predictions. This report focuses on the most actionable repurposing candidate (**Injury, Rank 4**); the full prediction landscape is summarised below.

| Rank | Disease | TxGNN Score | Evidence Level | Decision |
|------|---------|-------------|----------------|----------|
| 1 | Non-syndromic esophageal malformation | 99.96% | L5 | Hold |
| 2 | Esophageal disease | 99.90% | L3 | Research Question |
| 3 | Congenital prothrombin deficiency | 99.70% | L5 | Hold |
| **4** | **Injury** | **99.60%** | **L2** | **Proceed with Guardrails** |
| 5 | Biotin metabolic disease | 99.52% | L4 | Hold |
| 6 | Perinatal disease | 99.47% | L2 | Proceed with Guardrails |
| 7 | Segmental odontomaxillary dysplasia | 99.47% | L5 | Hold |
| 8 | Florid cemento-osseous dysplasia | 99.47% | L5 | Hold |
| 9 | Disease by subcellular system affected | 99.47% | L5 | Hold |
| 10 | Vitamin deficiency disorder | 99.47% | L1 | Proceed with Guardrails |

> **Important context:** Ranks 1, 3, 7, 8, and 9 have zero clinical trials and zero literature — these are Hold recommendations driven by model prediction alone. Rank 10 (vitamin deficiency disorder) achieves the strongest L1 evidence, but this represents the **established primary indication** for ascorbic acid, not a repurposing opportunity.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on well-established pharmacology, ascorbic acid (Vitamin C) functions through three mechanisms that are highly relevant to injury:

**Antioxidant and free-radical scavenging.** Severe trauma, burns, and surgery trigger systemic oxidative stress — a cascade of reactive oxygen species (ROS) that exacerbates secondary tissue damage beyond the initial insult. Ascorbic acid is the principal water-soluble antioxidant in human plasma, directly neutralising superoxide, hydroxyl radicals, and peroxynitrite. Plasma vitamin C levels drop precipitously within hours of critical injury, indicating rapidly elevated demand. Replenishing this deficit, particularly through intravenous administration that achieves pharmacological concentrations, may attenuate secondary injury.

**Collagen synthesis cofactor.** Ascorbic acid is an indispensable cofactor for prolyl hydroxylase and lysyl hydroxylase — the enzymes responsible for hydroxylation and crosslinking of collagen fibres. Without adequate vitamin C, collagen maturation is impaired, directly slowing wound healing, tendon repair, and bone regeneration. An RCT demonstrated that vitamin C-enriched gelatin supplementation before intermittent exercise significantly augments collagen synthesis (PMID: 27852613), providing direct evidence for this mechanism in musculoskeletal injury recovery.

**Anti-capillary-leak and anti-inflammatory effects.** In high-dose intravenous protocols used in burn resuscitation, ascorbic acid reduces microvascular permeability by inhibiting neutrophil-mediated endothelial injury. This decreases tissue oedema, reduces fluid resuscitation requirements, and lessens respiratory complications following large burns. Multiple retrospective studies and early-phase trials confirm reduced fluid requirements with high-dose IV vitamin C in severe burn injury. The difference between repurposing potential in burns versus other critical illness (e.g., the null result in septic shock from the LOVIT trial) underscores the importance of precise patient selection.

---

## Clinical Trial Evidence

The following trials are the most directly relevant to Ascorbic Acid in Injury (Rank 4 prediction):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04138394](https://clinicaltrials.gov/study/NCT04138394) | Phase 3 | Suspended | 666 | VICToRY Trial: High-dose IV vitamin C (66 mg/kg/h × 24 h) vs. placebo in critically ill burn patients — evaluating organ dysfunction, survival, and recovery rate; currently suspended pending interim analysis |
| [NCT03680274](https://clinicaltrials.gov/study/NCT03680274) | Phase 3 | Completed | 872 | LOVIT Trial: High-dose IV vitamin C vs. placebo in septic ICU patients — primary endpoint mortality or persistent organ dysfunction at 28 days; results showed no significant benefit in septic shock, highlighting indication-specificity concerns |
| [NCT03218280](https://clinicaltrials.gov/study/NCT03218280) | N/A | Unknown | 100 | Antioxidant therapy in critically ill polytrauma patients (SIRS/ARDS/sepsis) — directly evaluates vitamin C's impact on oxidative and inflammatory biomarkers and clinical outcomes |
| [NCT03166956](https://clinicaltrials.gov/study/NCT03166956) | N/A | Completed | 41 | Double-blind RCT of enteral glutamine + vitamin C in surgical ICU patients — assessed IL-6 levels and clinical outcomes including infection rate and wound healing |
| [NCT04921189](https://clinicaltrials.gov/study/NCT04921189) | Phase 2 | Completed | 160 | STAR Trial: Steroid + thiamine + ascorbic acid during post-resuscitation after out-of-hospital cardiac arrest — assessing neurological recovery and whole-body ischaemia-reperfusion injury |
| [NCT00879723](https://clinicaltrials.gov/study/NCT00879723) | Phase 1 | Completed | 28 | Burn micronutrient repletion pilot — characterises the relationship between vitamin C supplementation and health outcomes (fluid balance, organ function) in adult burn patients |
| [NCT05555576](https://clinicaltrials.gov/study/NCT05555576) | N/A | Recruiting | 464 | Double-blind RCT: Vitamin C vs. placebo for reducing opioid consumption after acute musculoskeletal injury in the emergency department — primary endpoint morphine-equivalent consumption over 2 weeks |
| [NCT02762331](https://clinicaltrials.gov/study/NCT02762331) | Phase 1 | Terminated | 6 | High-dose ascorbic acid in cardiac surgery patients to reduce post-operative atrial fibrillation — Phase 1 safety pilot; terminated due to recruitment difficulties, pharmacokinetic data obtained |
| [NCT01897792](https://clinicaltrials.gov/study/NCT01897792) | Phase 2 | Terminated | 11 | Vitamins C and E for coagulopathy and nosocomial pneumonia after severe trauma — terminated early due to slow enrolment; provides preliminary safety data |
| [NCT04344184](https://clinicaltrials.gov/study/NCT04344184) | Phase 2 | Completed | 47 | SAFE EVICT CORONA-ALI: Safety of 96-hour IV vitamin C infusion (50 mg/kg/6h) in hypoxaemic patients — establishes Phase 2 safety and pharmacodynamic profile for high-dose IV protocols |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27852613](https://pubmed.ncbi.nlm.nih.gov/27852613/) | 2017 | RCT | Am J Clin Nutr | Vitamin C-enriched gelatin supplementation before intermittent activity significantly augments collagen synthesis — directly supports VC's cofactor role in musculoskeletal injury repair |
| [31440996](https://pubmed.ncbi.nlm.nih.gov/31440996/) | 2020 | Review | Neurocritical Care | High-dose IV ascorbic acid in traumatic brain injury (TBI) — reviews secondary injury mechanisms and the emerging case for VC as neuroprotective adjunct |
| [33675075](https://pubmed.ncbi.nlm.nih.gov/33675075/) | 2021 | Review | JPEN | Ascorbic acid in the acute care setting — comprehensive evidence review across trauma, burns, sepsis, and critical illness; discusses optimal IV dosing and monitoring |
| [32141505](https://pubmed.ncbi.nlm.nih.gov/32141505/) | 2020 | Retrospective | J Burn Care Res | High-dose (66 mg/kg/h) vs. low-dose (3.5 g/day) ascorbic acid in severely burned adults — high-dose protocol demonstrated safety with a trend toward reduced fluid requirements |
| [21131846](https://pubmed.ncbi.nlm.nih.gov/21131846/) | 2011 | Retrospective | J Burn Care Res | Burn resuscitation with high-dose ascorbic acid (40 patients) — reduced fluid requirements, less body weight gain, and reduced mechanical ventilation requirements; supports translation from Japanese literature |
| [31631076](https://pubmed.ncbi.nlm.nih.gov/31631076/) | 2020 | Cohort | Ann Thorac Cardiovasc Surg | Corticosteroids + ascorbic acid + thiamine combination improves oxygenation after thoracoscopic esophagectomy — surgical injury model with direct clinical endpoints |
| [32466098](https://pubmed.ncbi.nlm.nih.gov/32466098/) | 2020 | Animal Study | Cells | Ascorbic acid promotes functional restoration after spinal cord injury via epigenetic modulation of DNA methylation — preclinical evidence for CNS injury application |
| [12643856](https://pubmed.ncbi.nlm.nih.gov/12643856/) | 2003 | Observational | J Surg Res | Ascorbic acid dynamics in seriously ill and injured patients — documents acute depletion after trauma/surgery and early evidence for benefit from high-level early supplementation |
| [37199082](https://pubmed.ncbi.nlm.nih.gov/37199082/) | 2023 | Animal Study | Clin Exp Pharmacol Physiol | Melatonin + ascorbic acid combination protects against sepsis-induced lung injury in rats — demonstrates synergistic antioxidant and anti-inflammatory effects in a systemic injury model |
| [25977448](https://pubmed.ncbi.nlm.nih.gov/25977448/) | 2015 | Experimental | J Appl Physiol | Ascorbic acid abrogates microparticle generation and vascular endothelial injuries associated with high-pressure exposure — decompression and barotrauma injury model |

---

## Philippines Market Information

Ascorbic acid currently has **zero active registrations** in the Philippines FDA database (market status: Not Marketed).

This finding almost certainly reflects a **data gap** rather than actual market absence. Ascorbic acid (Vitamin C) is one of the most widely distributed nutritional supplements and pharmaceutical products globally, available in multiple dosage forms (tablets, oral solutions, injectables, effervescent formulations). A direct query of the [FDA Philippines online verification portal](https://www.fda.gov.ph/) is strongly recommended to confirm current registration status before any regulatory or commercial decisions are made.

---

## Safety Considerations

Specific safety data (package insert warnings, contraindications, drug-drug interactions) were not available in the current evidence pack. Based on established pharmacological knowledge:

- **Renal risk at high doses**: Doses exceeding 1–2 g/day may increase urinary oxalate excretion and raise the risk of calcium oxalate nephrolithiasis, particularly in patients with renal impairment or a prior history of kidney stones. This is clinically significant for high-dose IV protocols (>10 g/day) used in burn resuscitation.
- **Esophageal mucosal injury**: Solid oral tablet formulations can cause localised esophageal injury and drug-induced strictures when swallowed without adequate fluid, or in patients with oesophageal dysmotility (PMID: 3606243, PMID: 131047). This is also relevant to the Rank 2 esophageal disease prediction — ascorbic acid is itself a documented cause of oesophageal injury in the literature.
- **Gastrointestinal intolerance**: High oral doses commonly produce osmotic diarrhoea, nausea, and abdominal cramping above the threshold of individual bowel tolerance (typically 2–4 g/day orally).
- **Potential prooxidant effects**: In the presence of free transition metal ions (iron, copper), very high concentrations of ascorbic acid can paradoxically generate hydroxyl radicals via the Fenton reaction — a consideration for patients with iron overload conditions.

Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (Injury indication — burns, trauma, surgical injury)

**Rationale:**
Ascorbic acid has a strong biologically plausible mechanism in injury (antioxidant protection, collagen synthesis, reduced capillary leak), plasma depletion is well-documented after severe trauma, and retrospective burn data are encouraging. However, the Phase 3 LOVIT trial (n=872) showed no benefit in septic shock, and the Phase 3 VICToRY burn trial (n=666) remains suspended — indicating that the benefit is likely highly dependent on injury subtype, dose, route, and timing of administration.

**To proceed, the following is needed:**

- **Await VICToRY trial results** (NCT04138394, burns, Phase 3, n=666) — this is the pivotal trial for the burn indication; do not make broad recommendations until these data are available
- **Stratify by injury subtype**: burns and surgical injury appear most biologically plausible; TBI shows preclinical promise but lacks Phase 3 human data; polytrauma results are heterogeneous
- **Define dosing protocol**: high-dose IV (66 mg/kg/h × 24 h) vs. standard supplementation have very different evidence bases and safety profiles
- **Verify Philippines registration status** directly via FDA Philippines portal — the current zero-registration finding is most likely a data artefact
- **Obtain full package insert** from the relevant regulatory authority (e.g., TFDA or Philippines FDA) to complete safety, contraindication, and interaction assessment
- **Conduct pharmacoeconomic analysis** in the Philippines healthcare context — ascorbic acid is low-cost and generically available, which strengthens the case for proceeding if efficacy is confirmed in the appropriate subpopulation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

