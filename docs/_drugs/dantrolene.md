---
layout: default
title: Dantrolene
parent: 僅模型預測 (L5)
nav_order: 95
evidence_level: L5
indication_count: 9
---

# Dantrolene
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

# Dantrolene: From Spasticity to Malignant Hyperthermia Susceptibility

## One-Sentence Summary

Dantrolene is a skeletal muscle relaxant originally developed to manage chronic spasticity associated with upper motor neuron disorders (e.g., multiple sclerosis, spinal cord injury, cerebral palsy).
The TxGNN model predicts it may be effective for **Malignant Hyperthermia, Susceptibility to** — a rare but potentially fatal pharmacogenetic crisis triggered by volatile anesthetics or succinylcholine —
with **0 registered clinical trials** and **19 publications** currently supporting this direction, including two major international clinical practice guidelines.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Spasticity (upper motor neuron disorders) |
| Predicted New Indication | Malignant Hyperthermia, Susceptibility to |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L1 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Dantrolene's mechanism centres on direct inhibition of the **RyR1 (Ryanodine Receptor type 1)** calcium release channel located in the sarcoplasmic reticulum of skeletal muscle. By reducing RyR1 open-channel probability, Dantrolene limits the pathological surge of myoplasmic Ca²⁺ that drives uncontrolled muscle hypermetabolism. This suppresses the hallmark features of a malignant hyperthermia (MH) crisis — escalating hyperthermia, rhabdomyolysis, respiratory and metabolic acidosis, and hypercapnia — allowing stabilisation of the patient.

Malignant hyperthermia susceptibility (MHS) is caused in the vast majority of cases by gain-of-function mutations in the *RYR1* gene (>70%) and, less frequently, *CACNA1S*. These mutations lower the activation threshold of the very channel that Dantrolene targets, creating an exceptionally tight mechanistic alignment between drug and disease. Nearly all genetically susceptible individuals carry mutations on this same pathway, making the TxGNN model's high-confidence prediction (99.93%) biologically well-grounded rather than speculative.

It is important to note that, globally, Dantrolene is already the **established standard of care** for MH crisis management. Two major 2021 international guidelines — from the Association of Anaesthetists (UK) and the European Malignant Hyperthermia Group — explicitly define intravenous Dantrolene as the definitive and irreplaceable therapy. The Philippines context is therefore not one of scientific uncertainty, but of **market access**: this critical emergency antidote is currently unregistered and unavailable through formal Philippine regulatory channels, representing a direct patient safety risk in any hospital performing general anaesthesia.

> **Note on MOA data:** Formal mechanism of action data is not available in the current Evidence Pack (Data Gap DG002). The description above is drawn from peer-reviewed mechanistic literature included in the evidence set, particularly Choi et al. 2017 (PNAS, PMID 28373535).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

> **Context:** The absence of registered RCTs reflects the ethical and practical impossibility of conducting placebo-controlled trials for a life-threatening, acute anesthetic emergency. Evidence for Dantrolene in MH has accumulated through decades of emergency case reports, observational data, and expert consensus rather than formal RCTs.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33399225](https://pubmed.ncbi.nlm.nih.gov/33399225/) | 2021 | Clinical Practice Guideline | *Anaesthesia* | Association of Anaesthetists guideline: formally defines MH as a progressive life-threatening hypermetabolic reaction; positions IV Dantrolene as the definitive treatment alongside trigger removal and supportive care |
| [33131754](https://pubmed.ncbi.nlm.nih.gov/33131754/) | 2021 | International Consensus Guideline | *British Journal of Anaesthesia* | European Malignant Hyperthermia Group consensus: comprehensive perioperative management protocols for MH-susceptible patients; Dantrolene recommended for both prophylaxis and crisis intervention |
| [26238698](https://pubmed.ncbi.nlm.nih.gov/26238698/) | 2015 | Systematic Review | *Orphanet Journal of Rare Diseases* | Detailed review of MH epidemiology (1:10,000–1:250,000 anaesthetics), RYR1/CACNA1S genetics, clinical presentation, and Dantrolene as the only specific pharmacological rescue agent |
| [39171998](https://pubmed.ncbi.nlm.nih.gov/39171998/) | 2024 | Comprehensive Review | *Critical Care Medicine* | Expert narrative review focusing on MH in critically ill patients; summarises clinical epidemiology, Dantrolene dosing protocols, and ICU management challenges |
| [28373535](https://pubmed.ncbi.nlm.nih.gov/28373535/) | 2017 | Mechanistic Study | *Proceedings of the National Academy of Sciences* | Elucidates Dantrolene's precise mechanism: requires Mg²⁺ co-factor to suppress RyR1-mediated Ca²⁺ transients in MH-susceptible muscle; directly confirms RyR1 as the drug's target |
| [32008650](https://pubmed.ncbi.nlm.nih.gov/32008650/) | 2020 | Narrative Review | *Anesthesiology Clinics* | Updated MH review: autosomal dominant inheritance with variable penetrance, mortality improvement with early Dantrolene administration, current diagnostic algorithms |
| [33863282](https://pubmed.ncbi.nlm.nih.gov/33863282/) | 2021 | Observational Study | *BMC Anesthesiology* | Outcomes in settings where Dantrolene is unavailable (including China): highlights higher mortality, management challenges, and the urgent need for improved drug access in underserved healthcare systems |
| [40597248](https://pubmed.ncbi.nlm.nih.gov/40597248/) | 2025 | Bibliometric Analysis | *Orphanet Journal of Rare Diseases* | Global MH research trends 1975–2024; identifies Dantrolene availability as the single most critical determinant of reduced MH mortality across healthcare systems worldwide |
| [17456235](https://pubmed.ncbi.nlm.nih.gov/17456235/) | 2007 | Review | *Orphanet Journal of Rare Diseases* | Foundational review of MH genetics, incidence, and clinical features; establishes the RYR1 mutation framework underpinning both diagnosis and Dantrolene-based treatment |
| [9798607](https://pubmed.ncbi.nlm.nih.gov/9798607/) | 1998 | Review | *Lancet* | Classic Lancet overview: establishes MH as an inherited skeletal muscle membrane disorder; documents Dantrolene's specific therapeutic role and describes triggering by exercise, heat, and anaesthetic agents |

---

## Philippines Market Information

Dantrolene (DrugBank ID: DB01219) is currently **not registered** with the Philippine Food and Drug Administration (PFDA). No product licences are on record under any brand name or dosage form.

> This represents a critical clinical access gap. Dantrolene is the only pharmacological antidote for malignant hyperthermia — a life-threatening emergency that can occur in any hospital operating theatre. Its non-availability through formal regulatory channels means Philippine anaesthesiologists currently lack a registered emergency rescue medication for this condition.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Data Gap Notice:** PFDA package insert warnings, contraindications, and formal drug interaction data were not retrievable in this Evidence Pack (Data Gaps DG001 and DG002). Before any procurement or clinical deployment, the full prescribing information from an approved jurisdiction (e.g., FDA USA Dantrium®, EMA, or TGA Australia) must be reviewed. Key known concerns from published literature include hepatotoxicity risk with chronic oral use, muscle weakness, and the need for weight-based IV dosing in acute crisis settings.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dantrolene is the globally established, guideline-mandated antidote for malignant hyperthermia — a potentially fatal anesthetic emergency with no other proven pharmacological rescue option. Its absence from the Philippine market is a patient safety issue of the highest urgency, particularly given that MH crises can occur in any hospital performing general anaesthesia. The evidence base, while not RCT-derived (ethically impractical for this indication), is supported by two international clinical practice guidelines (2021), decades of observational and mechanistic data, and a near-perfect mechanistic alignment between Dantrolene's RyR1 target and the RYR1 mutation-driven pathophysiology of MH susceptibility.

**To proceed, the following is needed:**
- Retrieve full prescribing information (package insert) from FDA USA (Dantrium® / Revonto®) or EMA to document contraindications, hepatotoxicity monitoring requirements, and drug-drug interactions
- Obtain formal mechanism of action data from DrugBank API (remediation for Data Gap DG002)
- Identify Philippine regulatory pathway: evaluate feasibility of emergency/compassionate use authorisation or full product registration with PFDA
- Conduct supply chain feasibility assessment for IV Dantrolene formulation (powder for reconstitution) in Philippine tertiary hospital settings — including cold chain, reconstitution requirements, and minimum stock levels per operating theatre
- Engage the Philippine Society of Anesthesiologists (PSA) to quantify annual MH incidence and identify priority hospitals (high surgical volume) for initial stock placement
- Develop a hospital-level MH crisis protocol template incorporating Dantrolene dosing (IV 2.5 mg/kg initial dose, repeat as needed) and monitoring guidelines aligned with the 2021 international consensus
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

