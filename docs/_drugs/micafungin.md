---
layout: default
title: Micafungin
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 1
---

# Micafungin
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

Using the `txgnn-pipeline` skill to orient the task — this is a report-generation step in the TxGNN pipeline, drawing on an Evidence Pack to produce a pharmacist-facing repurposing evaluation. I'll now generate the report.

---

# Micafungin: From Invasive Candidiasis to Urinary Tract Infection

## One-Sentence Summary

Micafungin is an echinocandin antifungal used to treat invasive candidiasis and aspergillosis in immunocompromised patients.
The TxGNN model predicts it may be effective for **Urinary Tract Infection** (specifically fungal/Candida UTI),
with **0 clinical trials** and **13 publications** currently supporting this direction — the majority being case reports and small retrospective studies.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Invasive candidiasis / aspergillosis (based on known drug class; not registered in the Philippines) |
| Predicted New Indication | Urinary Tract Infection (Candida UTI) |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Micafungin is an echinocandin antifungal that works by inhibiting **β-1,3-D-glucan synthase**, an enzyme essential for fungal cell wall construction. By blocking cell wall synthesis, micafungin exerts fungicidal activity against *Candida* spp. — the same genus responsible for the majority of fungal urinary tract infections (candiduria). The mechanistic target is therefore directly relevant to the predicted indication.

The challenge is pharmacokinetic rather than mechanistic. Echinocandins including micafungin have very low urinary excretion rates (< 5%), meaning urinary drug concentrations are typically well below the therapeutic threshold. This is why current IDSA guidelines recommend fluconazole — not echinocandins — as first-line therapy for *Candida* UTI. Micafungin's value in this setting has historically been regarded as limited by poor bladder penetration.

However, a 2016 pharmacokinetic study (PMID 27424599) reported that urinary micafungin levels in certain patients may still exceed the MIC for common *Candida* species, and a growing set of case reports documents clinical success specifically in fluconazole-resistant or fluconazole-intolerant cases (e.g., *C. krusei*, *C. glabrata*, *C. auris*). The TxGNN score of 99.03% most likely reflects the model's recognition of micafungin's broad anti-*Candida* activity rather than a UTI-specific pharmacological advantage. This represents a **niche salvage scenario** rather than a general indication expansion.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [27587066](https://pubmed.ncbi.nlm.nih.gov/27587066/) | 2016 | Retrospective Cohort | Int Urol Nephrol | Rates of candiduria elimination in micafungin-treated hospitalized patients; documents activity against azole-resistant strains despite low urine concentrations |
| [35146837](https://pubmed.ncbi.nlm.nih.gov/35146837/) | 2022 | Retrospective Case Series | Pediatrics Int | Critically ill children in PICU with hospital-acquired *Candida* UTI treated with micafungin; treatment success and species-specific outcomes reported |
| [27424599](https://pubmed.ncbi.nlm.nih.gov/27424599/) | 2016 | PK/PD Study | Int J Antimicrob Agents | 6 patients (4 fluconazole-resistant) successfully treated; urinary micafungin concentrations may exceed *Candida* MIC thresholds — supports therapeutic drug monitoring approach |
| [26937340](https://pubmed.ncbi.nlm.nih.gov/26937340/) | 2016 | Case Series | Med Mycol Case Rep | 5 patients received parenteral micafungin ≥ 6 days; all achieved candiduria resolution within 30 days of treatment completion |
| [29109159](https://pubmed.ncbi.nlm.nih.gov/29109159/) | 2018 | Multi-institutional Retrospective | Antimicrob Agents Chemother | 305 hospitalized patients studied; documents widespread antifungal overuse for asymptomatic candiduria; current guidelines advise against treatment without symptoms |
| [39781278](https://pubmed.ncbi.nlm.nih.gov/39781278/) | 2025 | Epidemiological / Susceptibility | Ther Adv Infect Dis | *Candida* species distribution and antifungal susceptibility in UTI and vulvovaginal candidiasis in Vietnam (2023); regional susceptibility data relevant to treatment selection |
| [31111613](https://pubmed.ncbi.nlm.nih.gov/31111613/) | 2019 | Case Report | Transplant Infect Dis | Chronic symptomatic *C. krusei* UTI in a transplant recipient (intrinsically fluconazole-resistant); eradicated with high-dose micafungin — illustrates salvage role |
| [38827222](https://pubmed.ncbi.nlm.nih.gov/38827222/) | 2024 | Case Report | Front Pediatrics | *C. glabrata* UTI in a premature neonate in NICU; micafungin used due to limited alternatives; successful outcome documented |
| [33520520](https://pubmed.ncbi.nlm.nih.gov/33520520/) | 2020 | Case Report | Cureus | *C. auris* UTI in a nursing home patient; case highlights the emerging challenge of multidrug-resistant *Candida* in urinary infections |
| [38681664](https://pubmed.ncbi.nlm.nih.gov/38681664/) | 2024 | Case Report | Med Mycol Case Rep | Unilateral renal fungus ball caused by *C. glabrata* — sensitive to micafungin; resolved with combined antifungal therapy and endoscopic extraction |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Micafungin has no Philippines registration, zero prospective clinical trials targeting *Candida* UTI, and its current evidence base consists entirely of case reports and small retrospective studies. The fundamental pharmacokinetic limitation — poor urinary penetration (< 5% urinary excretion) — remains the central unresolved obstacle and is not adequately addressed by the available data.

**To proceed, the following is needed:**

- **Philippines registration:** Currently not marketed; regulatory pathway must be established before any local use
- **Pharmacokinetic data:** Formal PK study demonstrating that urinary micafungin concentrations reliably exceed *Candida* MIC thresholds in the target population (e.g., critically ill, renal-impaired patients)
- **Prospective clinical trial:** Controlled comparison of micafungin vs. fluconazole in symptomatic *Candida* UTI, with pre-specified enrollment criteria for fluconazole-resistant or fluconazole-intolerant cases
- **Safety profile:** Package insert warnings, contraindications, and drug interaction data (currently unavailable in this Evidence Pack)
- **MOA documentation:** Formal DrugBank API retrieval to complete mechanistic analysis
- **Target population definition:** Identify the specific subgroup (fluconazole-resistant *Candida*, azole-intolerant patients, transplant recipients) where micafungin would offer a genuine clinical advantage over established first-line agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

