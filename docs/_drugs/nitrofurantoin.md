---
layout: default
title: Nitrofurantoin
parent: 僅模型預測 (L5)
nav_order: 251
evidence_level: L5
indication_count: 10
---

# Nitrofurantoin
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

# Nitrofurantoin: From Urinary Tract Infection to Rheumatoid Arthritis

## One-Sentence Summary

Nitrofurantoin is a nitrofuran-class antibacterial agent with decades of established use for acute uncomplicated urinary tract infections (UTIs). The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with **0 clinical trials** and **12 publications** currently identified — however, critically, the available literature reveals Nitrofurantoin as a **documented harm contributor** in RA patients rather than a viable therapeutic candidate, and the prediction appears to reflect a reverse safety signal rather than a genuine treatment opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (globally established use; no Philippines registration on file) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data sources queried. Based on well-established pharmacology, Nitrofurantoin is a prodrug activated by bacterial flavoproteins through intracellular reduction. This generates reactive intermediates that disrupt multiple bacterial targets simultaneously — bacterial DNA, ribosomal proteins, and cell wall synthesis — making resistance development unlikely. This mechanism is specific to prokaryotic cellular machinery and has no recognized anti-inflammatory or immunomodulatory activity relevant to rheumatoid arthritis.

The TxGNN knowledge graph likely constructed a link between Nitrofurantoin and RA through shared pathological territory rather than a direct therapeutic mechanism. RA patients frequently develop interstitial lung disease (RA-ILD), and Nitrofurantoin is a well-documented cause of drug-induced pulmonary fibrosis — creating a co-occurrence pattern in the clinical literature that graph-based models can misinterpret as a therapeutic signal. A 2022 case report (PMID 35145797) documents irreversible pulmonary fibrosis in a 94-year-old RA patient receiving concurrent Methotrexate and Nitrofurantoin — the combination of two pulmonary-toxic agents in a patient already at risk for RA-ILD is an active safety hazard, not a treatment rationale.

A theoretically indirect pathway exists: certain antibiotics have been shown to influence RA disease activity through gut microbiome modulation (PMID 31222078), and this self-controlled case series demonstrated that antibiotic exposure correlated with RA flare timing. However, that study examined antibiotics as a drug class using CPRD GOLD population data and did not isolate Nitrofurantoin-specific effects. Given Nitrofurantoin's known pulmonary and hepatic toxicity profile — particularly when combined with standard RA therapies — pursuing this hypothesis would carry substantial patient safety risk without any supporting mechanistic evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case Report | Cureus | RA patient on long-term Methotrexate developed irreversible pulmonary fibrosis after Nitrofurantoin was added for chronic UTI — documents active synergistic harm signal |
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Self-controlled Case Series | Scientific Reports | Antibiotic exposure associated with RA flare risk in 31,992-patient CPRD cohort; class-level association, no Nitrofurantoin-specific data |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort/Retrospective | Chest | Poor prognosis documented in RA patients hospitalized for interstitial lung fibrosis; contextualizes severity of pulmonary overlap risk |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Medical Journal | Nitrofurantoin explicitly listed among drugs causing pulmonary fibrosis; mechanism attributed to chronic administration |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du praticien | Nitrofurantoin categorized as a causative antibiotic in drug-induced interstitial lung disease; various clinical patterns described |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case Report | Cureus | Autoimmune hepatitis workup: Nitrofurantoin and methyldopa listed as medications to rule out as causes; RA and thyroiditis co-appear as autoimmune context |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Case Report | Revue de pneumologie clinique | Gold salt-induced pneumonia with CD4 alveolitis in RA patient — relevant parallel showing how RA drugs themselves can cause drug-ILD, compounding risk |
| [4608019](https://pubmed.ncbi.nlm.nih.gov/4608019/) | 1974 | Review | Der Internist | Early synopsis of alveolitis and pulmonary fibrosis etiologies; foundational context |
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | Clinical Study | Acta Medica Scandinavica | Short-term Nitrofurantoin therapy and one-year follow-up for bacteriuria in middle-aged women; establishes Nitrofurantoin's primary UTI use context |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case Report | Annales de dermatologie et de vénéréologie | Nitrofurantoin cited as a known cause of drug-induced sialadenitis; illustrates broad organ-level adverse effect profile |

---

## Philippines Market Information

Nitrofurantoin is currently not registered with the Philippine FDA. There are no licensed pharmaceutical products on record in the Philippines regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Evidence-derived safety alert (from literature review):** Although formal Philippines regulatory safety data is unavailable, the published literature assembled for this prediction contains critical safety signals that directly affect the RA patient population: (1) Nitrofurantoin is a recognized cause of drug-induced pulmonary fibrosis — when combined with Methotrexate, the most commonly used first-line RA DMARD, irreversible pulmonary fibrosis has been documented (PMID 35145797); (2) RA patients are already at elevated baseline risk for interstitial lung disease (RA-ILD), meaning Nitrofurantoin exposure creates a synergistic hazard; (3) Nitrofurantoin can induce methemoglobin formation via photoactivation, posing additional risk in patients on multiple medications; (4) when creatinine clearance falls below 30 mL/min — a threshold frequently reached in patients with long-standing RA or concurrent diabetic nephropathy — urinary drug concentrations become subtherapeutic while toxic metabolite accumulation increases peripheral neuropathy risk.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score of 99.89% reflects knowledge graph connectivity, not therapeutic validity — every piece of literature identified connects Nitrofurantoin to rheumatoid arthritis as a **causative agent of harm** (drug-induced pulmonary fibrosis overlapping with RA-ILD) rather than as a treatment, and the drug lacks any anti-inflammatory or immunomodulatory mechanism of action.

**Broader pattern across all 10 predicted indications:**
This Evidence Pack reveals a consistent pattern across all TxGNN-predicted indications for Nitrofurantoin — in most cases, the knowledge graph has mistaken drug-induced adverse event co-occurrence for therapeutic signal:

- **Methemoglobinemia / Methemoglobinemia (alpha type)** (Ranks 8 & 10): Nitrofurantoin is a documented *cause* of methemoglobin formation (PMID 3176031); repurposing is actively contraindicated.
- **Sclerosing Cholangitis** (Rank 7): Nitrofurantoin is a known cause of drug-induced liver injury including cholestatic hepatitis; the drug is the *perpetrator*, not the treatment.
- **Diabetic Nephropathy** (Rank 4): Literature describes antibiotic resistance patterns in UTI complicating DN — not Nitrofurantoin as a DN therapy. Active contraindication exists when CrCl <30 mL/min.
- **Genetic/developmental syndromes** (Ranks 2, 3, 5, 6): No mechanistic plausibility. Likely graph artifacts from shared anatomical nodes (urinary tract, renal, ocular).
- **Gout** (Rank 9): Single tangential pyelonephritis review; no therapeutic link.

**To proceed with any re-evaluation, the following is needed:**
- Formal MOA retrieval from DrugBank API (DG002 remediation) to confirm whether any off-target anti-inflammatory activity has been characterized
- Philippines FDA package insert download and parsing (DG001 remediation) to obtain official warnings and contraindications
- A hypothesis-specific literature search for Nitrofurantoin and microbiome-mediated RA modulation, restricted to studies with Nitrofurantoin-specific (not class-level) endpoints
- Pre-clinical toxicology review to determine whether any sub-antimicrobial dose range could exhibit immunomodulatory effects without pulmonary or hepatic toxicity — a prerequisite before any in vitro or animal studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

