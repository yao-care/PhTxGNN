---
layout: default
title: Itraconazole
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 1
---

# Itraconazole
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

以下是根據 Evidence Pack 產生的完整評估報告：

---

# Itraconazole: From Fungal Infections to Pneumocystosis

## One-Sentence Summary

Itraconazole is a triazole antifungal agent established for the treatment of systemic fungal infections including aspergillosis, histoplasmosis, and candidiasis.
The TxGNN model predicts it may be effective for **Pneumocystosis** (*Pneumocystis jirovecii* pneumonia, PCP), with **0 clinical trials** and **20 publications** associated with this direction — however, mechanistic analysis reveals this high-scoring prediction (99.34%) is almost certainly a **false positive** driven by a structural bias in the knowledge graph, not genuine therapeutic potential.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Systemic fungal infections (aspergillosis, histoplasmosis, candidiasis) |
| Predicted New Indication | Pneumocystosis (*Pneumocystis jirovecii* Pneumonia) |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L4 — Mechanistic/preclinical studies; no clinical trial support |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

At first glance, the prediction seems plausible: itraconazole is an antifungal, and *Pneumocystis jirovecii* is classified as a fungus. However, this surface-level match conceals a fundamental biological incompatibility. **Itraconazole works by inhibiting CYP51 (lanosterol 14α-demethylase)**, the enzyme that synthesises ergosterol — the sterol found in fungal cell membranes. Since ergosterol is absent from human cells, azole antifungals can selectively kill fungi without harming the host.

The critical issue is that *P. jirovecii* is highly atypical among fungi: **it does not synthesise ergosterol at all**. Instead, it scavenges and incorporates cholesterol directly from host tissues into its own membrane. This means itraconazole's entire mechanism has no target to bind in *P. jirovecii*. A 2003 mechanistic study characterising the *Pneumocystis carinii* CYP51/Erg11 enzyme (PMID 12606318) confirmed that the organism carries CYP51 sequence variants identical to those found in azole-resistant fungi — consistent with intrinsic, class-wide azole insensitivity. There is no pharmacological workaround for this incompatibility.

The standard of care for PCP is **trimethoprim-sulfamethoxazole (TMP-SMX)**, which targets dihydropteroate synthase in the folate synthesis pathway — a metabolic route *P. jirovecii* cannot substitute with host-derived folate. Clinical guidelines (PMID 21418688) do not include itraconazole or any azole as a treatment or prophylaxis option for PCP. The TxGNN score of 0.9934 most likely reflects the knowledge graph incorrectly generalising from "azole antifungal → treats fungal disease" without encoding the unique biology of *P. jirovecii*, producing a structurally plausible but clinically invalid repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The retrieved publications address opportunistic fungal infections and immunocompromised populations broadly. None document itraconazole efficacy against *P. jirovecii*. The most mechanistically significant paper (PMID 12606318) explains precisely *why* azoles fail against this organism.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | RCT | HIV Medicine | Phase III double-blind RCT of itraconazole capsules for prevention of deep fungal infections in HIV-positive patients; primary endpoint was broad fungal prophylaxis, not PCP specifically — no efficacy signal against *P. jirovecii* |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review/Guideline | BMJ Clinical Evidence | HIV primary and secondary prophylaxis for opportunistic infections; confirms TMP-SMX as the only recommended agent for PCP prophylaxis — itraconazole not listed |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Comprehensive review of therapy and prophylaxis for systemic protozoan and fungal infections; itraconazole not indicated for *Pneumocystis* treatment |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Curr Clin Topics Infect Dis | Infection prophylaxis in bone marrow transplant recipients; TMP-SMX established as standard for PCP prevention in transplant settings |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Semin Respir Infect | Infections after lung transplantation; PCP prevention and management overview — azoles not recommended for PCP |
| [12606318](https://pubmed.ncbi.nlm.nih.gov/12606318/) | 2003 | Mechanistic | Am J Respir Cell Mol Biol | Characterisation of *P. carinii* CYP51/Erg11 enzyme; two of 13 potential azole-resistance sites in *P. carinii* CYP51 are identical to confirmed azole-resistant organisms — **directly explains intrinsic itraconazole insensitivity** |
| [30429396](https://pubmed.ncbi.nlm.nih.gov/30429396/) | 2018 | Observational | Indian J Med Microbiol | Respiratory fungal pathogen profiles comparing immunocompetent vs. immunocompromised hosts; susceptibility data underscores azole inefficacy against *P. jirovecii* |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Retrospective Cohort | Transplantation Proceedings | Invasive fungal infections after kidney transplantation; itraconazole used for non-PCP fungal infections — PCP managed separately with TMP-SMX |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case Report | Frontiers in Immunology | *Talaromyces marneffei* and *P. jirovecii* co-infection in a child with STAT1 mutation; TMP-SMX used for the PCP component — itraconazole not applicable |
| [8967681](https://pubmed.ncbi.nlm.nih.gov/8967681/) | 1996 | Case Report | Annals of Internal Medicine | Uveitis associated with rifabutin prophylaxis and itraconazole therapy in an HIV patient; documents itraconazole use for MAC/fungal co-prophylaxis context, not PCP |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Itraconazole's mechanism of action — CYP51/ergosterol inhibition — has no valid target in *Pneumocystis jirovecii* because this organism lacks ergosterol entirely. There is zero clinical trial evidence supporting this use, and the published mechanistic literature (PMID 12606318) explicitly confirms azole insensitivity in *P. jirovecii* at the molecular level. The TxGNN score of 99.34% is a knowledge graph false positive, not a therapeutic signal.

**To proceed, the following is needed:**

- **No further development** of itraconazole for pneumocystosis is warranted; mechanistic incompatibility is definitive and well-documented
- If broader PCP treatment research is the goal, repurposing candidates should target the folate pathway (dihydropteroate synthase, DHFR), *P. jirovecii* β-glucan synthesis (caspofungin has shown some activity), or cell wall stress mechanisms
- The TxGNN pipeline should consider implementing a **post-processing exclusion rule** for azole antifungal × *Pneumocystis* combinations, flagging them as structurally predicted false positives prior to evidence collection
- Obtain official itraconazole package insert (Philippines FDA) to complete the safety data gaps (DG001) and DrugBank MOA entry (DG002) for completeness of the drug-level record, even though they do not change this recommendation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

