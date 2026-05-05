---
layout: default
title: Moxifloxacin
parent: 僅模型預測 (L5)
nav_order: 194
evidence_level: L5
indication_count: 10
---

# Moxifloxacin
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

Using `txgnn-pipeline` skill — confirmed this is a TxGNN report generation task. Proceeding with Drug Repurposing Evaluation Report (v5) format.

---

# Moxifloxacin: From Bacterial Infections to Bubonic Plague

## One-Sentence Summary

Moxifloxacin is a fourth-generation fluoroquinolone antibiotic, established in clinical practice for community-acquired pneumonia, acute sinusitis, skin infections, and complicated intra-abdominal infections.
The TxGNN model's most evidence-supported prediction points to **Bubonic Plague** (*Yersinia pestis* infection), backed by **6 preclinical publications** including animal challenge models and in vitro pharmacodynamic studies confirming potent bactericidal activity.
Of the 10 predicted indications, 9 cluster around haematological diseases and are assessed as knowledge-graph co-occurrence artefacts; bubonic plague stands as the sole prediction with an established mechanistic rationale and an evidence rating of L3.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (community-acquired pneumonia, sinusitis, skin and soft-tissue infections) — not currently registered in the Philippines |
| Predicted New Indication | Bubonic Plague (*Yersinia pestis* infection) |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on well-established pharmacology, moxifloxacin is a fluoroquinolone antibiotic that inhibits **bacterial DNA gyrase (topoisomerase II)** and **topoisomerase IV** — the two enzymes responsible for managing DNA supercoiling and strand passage during replication. This dual-target bactericidal mechanism is directly relevant to *Yersinia pestis*, which expresses both target enzymes and is known to be highly susceptible to fluoroquinolones. Multiple in vitro pharmacodynamic studies confirm that moxifloxacin achieves MIC values against *Y. pestis* well within clinically attainable plasma concentrations.

Moxifloxacin's broader antibacterial spectrum overlaps substantially with the pathogen profile relevant to plague: it is effective against intracellular Gram-negative organisms, and its excellent tissue penetration mirrors the requirements for treating systemic *Y. pestis* bacteraemia. Fluoroquinolones are already recognised by the US CDC and WHO as acceptable alternative agents for plague when traditional first-line drugs (streptomycin, gentamicin) are unavailable. Moxifloxacin has appeared explicitly in FDA labelling guidance for plague indications in markets where it is registered.

From a practical standpoint relevant to the Philippines, moxifloxacin offers once-daily oral dosing and high oral bioavailability — properties that are particularly valuable in outbreak or bioterrorism preparedness scenarios where parenteral administration may be logistically constrained.

> **Note on other predicted indications:** Ranks 1–9 primarily predict haematological diseases (hyperamylasemia, monoclonal gammopathy, congenital blood disorders, etc.). The repurposing rationale in the Evidence Pack explicitly flags these as likely **knowledge-graph co-occurrence artefacts** — patients with haematological diseases frequently receive antibiotics for infectious complications, generating false edges in the KG. None of these predictions carry mechanistic support or actionable evidence; all are rated L5 or L4 with a **Hold** recommendation.

---

## Clinical Trial Evidence

Currently no clinical trials specifically evaluating moxifloxacin for bubonic plague have been registered on ClinicalTrials.gov or ICTRP.

> **Indirect safety signal from trials:** [NCT07023029](https://clinicaltrials.gov/study/NCT07023029) — a completed Phase 1 cardiac repolarisation study for Etavopivat (sickle cell disease) — used moxifloxacin as the **positive QTc-prolongation control arm**. This confirms moxifloxacin's well-characterised cardiac conduction effect and is a clinically relevant safety signal for any future plague treatment protocol, particularly in patients with concurrent QT-prolonging conditions.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [21115791](https://pubmed.ncbi.nlm.nih.gov/21115791/) | 2011 | In Vitro PK/PD Model | *Antimicrobial Agents and Chemotherapy* | Hollow-fibre PK/PD model demonstrates moxifloxacin optimally kills *Y. pestis* and suppresses resistance emergence; dosing regimen derived |
| [21486959](https://pubmed.ncbi.nlm.nih.gov/21486959/) | 2011 | In Vitro PK/PD Comparative | *Antimicrobial Agents and Chemotherapy* | Comparative efficacy of multiple antibiotics against *Y. pestis*; moxifloxacin among top-performing regimens relative to streptomycin gold standard |
| [15555886](https://pubmed.ncbi.nlm.nih.gov/15555886/) | 2004 | Animal Model / In Vitro | *International Journal of Antimicrobial Agents* | Full protection in BALB/c mice against systemic and pneumonic plague with oral moxifloxacin; efficacy comparable to ciprofloxacin up to 30 h post-aerosol challenge |
| [20052916](https://pubmed.ncbi.nlm.nih.gov/20052916/) | 2009 | Animal Model Comparative | *Antibiotiki i khimioterapiia* | Moxifloxacin ED₅₀ of 5.5–14.0 mg/kg in mice challenged with ~1,000 LD₅₀ of *Y. pestis*; active against both FI⁺ and FI⁻ strain phenotypes |
| [29623187](https://pubmed.ncbi.nlm.nih.gov/29623187/) | 2018 | Adverse Event Case Report | *Therapeutic Advances in Drug Safety* | FDA labelling explicitly lists **plague** as an approved moxifloxacin indication; case report contextualises QT/tinnitus adverse effect risk in elderly patients |
| [26210091](https://pubmed.ncbi.nlm.nih.gov/26210091/) | 2015 | Case Report | *Ticks and Tick-Borne Diseases* | Tularemia (*Francisella tularensis*) case from China; contextualises fluoroquinolone role in rare intracellular Gram-negative infections with mechanistic parallels to *Y. pestis* |

---

## Philippines Market Information

Moxifloxacin is currently **not registered** with the FDA Philippines. There are no active product licences on file and the drug has no approved indications in the Philippines.

For reference, moxifloxacin is marketed internationally under brand names such as **Avelox** (Bayer) and **Vigamox** (ophthalmic formulation), with regulatory approvals covering bacterial pneumonia, sinusitis, skin infections, intra-abdominal infections, and plague in several jurisdictions including the US FDA, EMA, and others. A new drug registration application to the FDA Philippines would be required before any clinical use.

---

## Safety Considerations

Full safety data (warnings, contraindications) is not available in this Evidence Pack. Please refer to the original package insert for complete safety information.

The following signals are noted from indirect evidence within this pack:

- **QT Prolongation:** Moxifloxacin served as the **positive QTc-prolongation control** in NCT07023029, confirming its cardiac conduction effect. This is a critical consideration in patients with pre-existing cardiac disease, electrolyte imbalances, or concurrent use of other QT-prolonging agents.
- **FDA-Restricted Use Class:** A 2018 publication (PMID [29623187](https://pubmed.ncbi.nlm.nih.gov/29623187/)) references the FDA's recommendation to restrict fluoroquinolone use to specific serious infections — including plague — owing to the risk of disabling and potentially irreversible adverse effects such as peripheral neuropathy, tendinopathy, and CNS effects.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Moxifloxacin has well-characterised preclinical bactericidal activity against *Yersinia pestis*, and fluoroquinolones are already recognised by the US CDC as alternative first-line agents for plague. While no clinical trial data exists, the preclinical evidence base and established regulatory acceptance in other markets provide sufficient foundation for further evaluation, particularly given that traditional first-line agents (streptomycin) have limited availability in the Philippines.

**To proceed, the following is needed:**

- **Blocking — Package insert review:** Obtain and parse the full prescribing information (warnings, contraindications, drug interactions) before any clinical or regulatory action
- **Cardiac safety protocol:** Mandatory QTc monitoring plan given confirmed QT-prolongation risk; establish contraindication criteria for high-risk cardiac patients
- **Philippines FDA registration pathway:** Initiate pre-submission consultation with the FDA Philippines; assess whether existing US FDA or EMA approval can expedite review
- **Epidemiological justification:** Document the incidence and public health risk of plague (and *Y. pestis*-related bioterrorism preparedness needs) in the Philippines to support the regulatory submission
- **Resistance surveillance:** Review fluoroquinolone resistance patterns in *Y. pestis* strains circulating in or relevant to Southeast Asia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

