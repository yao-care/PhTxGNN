---
layout: default
title: Nystatin
parent: 僅模型預測 (L5)
nav_order: 256
evidence_level: L5
indication_count: 10
---

# Nystatin
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

# Nystatin: From Candidiasis to Vulvovaginitis

## One-Sentence Summary

Nystatin is a well-established polyene antifungal antibiotic used globally since the 1950s for treating candidiasis of the oral cavity, intestinal tract, and skin, though it is currently not marketed in the Philippines.
The TxGNN model predicts it may be effective for **Vulvovaginitis**, with **0 registered clinical trials** and **20 publications** currently supporting this direction — reflecting a market introduction opportunity rather than a novel mechanistic discovery, as Nystatin is already approved for vulvovaginal candidiasis in the US, EU, and many other jurisdictions.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Candidiasis (global approval; not currently registered in Philippines) |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Nystatin is a polyene macrolide antifungal that acts by binding to **ergosterol**, a key structural lipid in fungal cell membranes. This binding creates pores that disrupt membrane integrity, causing leakage of intracellular contents and fungal cell death. Because mammalian cell membranes contain cholesterol rather than ergosterol, Nystatin has high selectivity for fungi. Nystatin is poorly absorbed systemically when applied topically or taken orally, making it ideally suited for local mucosal infections where high local concentrations can be achieved safely.

Vulvovaginitis — particularly vulvovaginal candidiasis (VVC) — is most commonly caused by *Candida albicans*, which accounts for 85–90% of cases. This is precisely the organism Nystatin targets with fungicidal potency. The mechanistic match between the drug's mode of action and the dominant pathogen in this disease is direct and well-established. In fact, Nystatin was first introduced for VVC treatment in the 1950s, and remains an approved therapy by the US FDA, EMA, and other major regulatory bodies — particularly as a second-line option in azole-resistant cases (including fluconazole-resistant strains of *C. albicans*, *C. glabrata*, and *C. krusei*).

The high TxGNN prediction score (99.92%) reflects both the mechanistic alignment captured in the underlying knowledge graph and the extensive global evidence base. The reason vulvovaginitis appears as a "predicted new indication" in this context is specifically that **Nystatin has no Philippines FDA registration**, making this a regulatory gap rather than an evidence gap. The clinical science supporting this use case is mature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Nystatin × Vulvovaginitis.

> **Note:** Evidence query returned 0 trials on ClinicalTrials.gov and ICTRP. This is consistent with the drug's well-established status — mature drugs with long clinical histories frequently lack recent prospective trials, as the evidence base is primarily drawn from decades of observational and review literature.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25775428](https://pubmed.ncbi.nlm.nih.gov/25775428/) | 2015 | Systematic Review | BMJ Clinical Evidence | Comprehensive evidence summary for VVC; *C. albicans* causes 85–90% of cases; antifungal treatment options including Nystatin discussed in full |
| [21774671](https://pubmed.ncbi.nlm.nih.gov/21774671/) | 2011 | Systematic Review | J Women's Health | Systematic review of non-albicans Candida resistance to azoles; Nystatin identified as clinically relevant alternative for recurrent VVC unresponsive to azoles |
| [39771534](https://pubmed.ncbi.nlm.nih.gov/39771534/) | 2024 | Review | Pharmaceutics | Current management of fluconazole-resistant VVC; Nystatin highlighted alongside boric acid and newer agents (oteseconazole, ibrexafungerp) as viable alternative |
| [21718579](https://pubmed.ncbi.nlm.nih.gov/21718579/) | 2010 | Systematic Review | BMJ Clinical Evidence | Updated clinical evidence summary; establishes treatment hierarchy for VVC including Nystatin as an option |
| [19454049](https://pubmed.ncbi.nlm.nih.gov/19454049/) | 2007 | Systematic Review | BMJ Clinical Evidence | Confirms Nystatin role in VVC treatment; notes imidazoles and triazoles have largely supplanted it as first-line agents |
| [12228137](https://pubmed.ncbi.nlm.nih.gov/12228137/) | 2002 | Review | BMJ | Overview of VVC diagnosis and management; discusses Nystatin in clinical context |
| [20406393](https://pubmed.ncbi.nlm.nih.gov/20406393/) | 2011 | Clinical Study | Mycoses | 287 Candida isolates from 283 patients with complicated VVC; nystatin susceptibility correlated with clinical outcomes; E-test used to evaluate susceptibility |
| [16047929](https://pubmed.ncbi.nlm.nih.gov/16047929/) | 2005 | Clinical Study | Ceska Gynekologie | Combined vaginal nifuratel + nystatin products evaluated for mixed/miscellaneous vulvovaginal infections; clinical outcomes reported |
| [30359236](https://pubmed.ncbi.nlm.nih.gov/30359236/) | 2018 | Animal Study | BMC Microbiology | In rat VVC model, Nystatin enhanced mucosal immune response against *C. albicans* and preserved vaginal epithelial ultrastructure; mechanism beyond direct fungicidal activity suggested |
| [32104010](https://pubmed.ncbi.nlm.nih.gov/32104010/) | 2020 | In Vitro Study | Infection and Drug Resistance | Nystatin showed activity against fluconazole-resistant *C. albicans* isolates from VVC patients; downregulation of SAP1–3 virulence genes observed |

---

## Philippines Market Information

Nystatin currently has **no registered products** with the Philippines FDA. No authorization numbers, brand names, or approved indications are on file.

This absence represents a market gap rather than a safety or efficacy concern. Nystatin vaginal formulations (tablets, suppositories, cream) are commercially available in many neighboring markets and could be registered through standard ASEAN harmonized regulatory pathways.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No Philippines FDA package insert data or DrugBank warning/contraindication data were available at the time of this report. Detailed safety data should be obtained from the originator's global dossier (US FDA label or EMA SmPC) prior to any regulatory submission.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Nystatin's mechanism of action directly targets the primary pathogen in vulvovaginal candidiasis, and the drug has been in continuous clinical use for this indication globally for over 70 years with a well-characterized safety profile. The absence of a Philippines registration is a regulatory gap, not a scientific or safety barrier — the evidence base supporting this use is substantive and the international regulatory precedent is clear.

**To proceed, the following is needed:**

- **Philippines FDA registration dossier**: Prepare a reference-country application citing US FDA or EMA approvals for vaginal Nystatin formulations
- **MOA documentation**: Obtain detailed mechanism of action data from DrugBank (DB00646) for the regulatory submission
- **Local safety data**: Download and parse the originator's package insert (US FDA label / EMA SmPC) to populate warnings, contraindications, and drug interaction sections
- **Dosage form selection**: Confirm which formulation(s) — vaginal tablet, suppository, or cream — are most commercially viable and have existing manufacturing authorization for the Philippines market
- **Post-marketing surveillance plan**: Prepare a pharmacovigilance plan per Philippines FDA requirements, with attention to azole-resistant candidiasis prevalence in the local population
- **YMYL disclaimer**: All patient-facing materials must include the statement: *"For research reference only. This does not constitute medical advice. Results require clinical validation before application."*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

