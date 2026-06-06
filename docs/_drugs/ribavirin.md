---
layout: default
title: Ribavirin
parent: 僅模型預測 (L5)
nav_order: 289
evidence_level: L5
indication_count: 10
---

# Ribavirin
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

# Ribavirin: From Hepatitis C to Chronic Hepatitis B Virus Infection

## One-Sentence Summary

Ribavirin is a broad-spectrum antiviral nucleoside analog, established as a backbone of pegylated-interferon-based combination therapy for Hepatitis C.
The TxGNN model predicts it may be effective for **Chronic Hepatitis B Virus Infection** with a score of **99.86%**; however, the 50 clinical trials and 20 publications retrieved are predominantly HCV-specific, and a fundamental mechanistic concern — ribavirin targets RNA viruses while HBV is a DNA virus — puts this prediction in serious question.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hepatitis C (pegylated interferon combination therapy) |
| Predicted New Indication | Chronic Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on well-established pharmacology, ribavirin is a synthetic guanosine nucleoside analog that inhibits inosine monophosphate dehydrogenase (IMPDH), depleting intracellular GTP pools and thereby suppressing viral RNA synthesis. This mechanism is highly active against RNA viruses — most prominently HCV — but does not directly target HBV DNA polymerase (a reverse transcriptase), which is the molecular target for standard HBV antivirals such as tenofovir and entecavir.

Hepatitis B and Hepatitis C both cause chronic viral hepatitis with significant liver disease burden, and both have historically been treated with interferon-alpha-based regimens. In the TxGNN knowledge graph, ribavirin sits at a node densely connected to interferon-based hepatitis treatment pathways, which are topologically proximate to HBV disease clusters. This explains the high prediction score — but shared treatment context in a knowledge graph does not translate to direct anti-HBV efficacy. The 50 retrieved clinical trials illustrate this problem clearly: not a single trial tests ribavirin specifically against HBV monoinfection.

There is one narrow clinical scenario where ribavirin has intersected with HBV: patients co-infected with both HCV and HBV, where PegIFN + Ribavirin is deployed to treat the HCV component, sometimes resulting in indirect modulation of HBV replication. Notably, a 2000 editorial in the *Journal of Gastroenterology* directly questioned whether ribavirin is effective for chronic HBV — more than two decades later, this question remains unanswered because supporting evidence never materialized. The current standard of care for chronic HBV (nucleos(t)ide analogs) does not include ribavirin.

---

## Clinical Trial Evidence

> ⚠️ **Important**: None of the 50 retrieved trials evaluate ribavirin as primary treatment for HBV monoinfection. All trials are HCV-specific. NCT02339337 is the only trial that enrolled HBV co-infected subjects.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02339337](https://clinicaltrials.gov/study/NCT02339337) | Phase 4 | Completed | 203 | Tailored PegIFN + Ribavirin in HCV/HBV dual-infected patients (HBeAg-negative); the sole retrieved trial enrolling HBV-positive subjects; genotype-guided vs. fixed-duration therapy |
| [NCT00215891](https://clinicaltrials.gov/study/NCT00215891) | Phase 3 | Completed | 300 | PEG-Intron + Ribavirin for chronic HCV in HIV-coinfected patients; comparing 48 vs. 72 weeks of therapy for sustained virologic response (SVR) |
| [NCT00100659](https://clinicaltrials.gov/study/NCT00100659) | Phase 3 | Completed | 114 | PegIFN alfa-2a ± Ribavirin in pediatric chronic HCV; established safety and efficacy profile in children |
| [NCT01425203](https://clinicaltrials.gov/study/NCT01425203) | Phase 3 | Completed | 238 | Boceprevir + PegIFN alfa-2b + Ribavirin for HCV genotype 1 in Russian population; treatment-naïve and prior-failure patients |
| [NCT00703118](https://clinicaltrials.gov/study/NCT00703118) | Phase 3 | Completed | 663 | Telaprevir (two regimens, with and without delayed start) + PegIFN + Ribavirin for chronic HCV GT1 after prior treatment failure |
| [NCT00048724](https://clinicaltrials.gov/study/NCT00048724) | Phase 3 | Completed | 631 | PEG-Intron maintenance vs. no treatment for HCV-related compensated cirrhosis in patients unresponsive to IFN + Ribavirin |
| [NCT00575224](https://clinicaltrials.gov/study/NCT00575224) | Phase 4 | Completed | 60 | Pegasys + Copegus (ribavirin) for Asian patients with HCV genotypes 6, 7, 8, and 9; comparing 24- vs. 48-week duration |
| [NCT00237484](https://clinicaltrials.gov/study/NCT00237484) | Phase 3 | Completed | 89 | Infliximab induction + PegIFN/Ribavirin for HCV genotype 1 patients with elevated TNF-α; evaluating immune modulation on SVR |
| [NCT01529073](https://clinicaltrials.gov/study/NCT01529073) | Phase 2 | Unknown | 45 | PegIFN + Ribavirin + Nitazoxanide for HCV genotype 4 / HIV co-infection; antiviral activity vs. historical PegIFN + RBV cohort |
| [NCT00720434](https://clinicaltrials.gov/study/NCT00720434) | Phase 2 | Completed | 35 | PF-00868554 (HCV NS5B polymerase inhibitor) + PegIFN + Ribavirin; standard-of-care combination as treatment backbone |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10832679](https://pubmed.ncbi.nlm.nih.gov/10832679/) | 2000 | Editorial/Review | J Gastroenterol | Directly poses "Is ribavirin treatment really effective for chronic hepatitis B?" — evidence was inconclusive in 2000; no robust anti-HBV activity was demonstrated |
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | HCV/HBV co-infection management: PegIFN + Ribavirin recommended for HCV-RNA-positive co-infected patients; now largely superseded by DAA-based regimens |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World J Gastroenterol | Updates on dual HCV/HBV treatment; viral load dynamics determine treatment prioritization; ribavirin relevant only for the HCV component |
| [27433078](https://pubmed.ncbi.nlm.nih.gov/27433078/) | 2016 | Review | World J Gastroenterol | IFN-α ± ribavirin as prototype HCV/HBV therapy; transition to DAAs; ribavirin explicitly lacks standalone anti-HBV activity |
| [18804888](https://pubmed.ncbi.nlm.nih.gov/18804888/) | 2008 | Review | J Hepatol | "Treatment of HBV/HCV co-infection: still a challenge"; ribavirin deployed only for the HCV component of co-infection management |
| [19669238](https://pubmed.ncbi.nlm.nih.gov/19669238/) | 2009 | Review | Hepatol Intl | Dual HBV/HCV infection: viral interactions and clinical management; PegIFN + RBV indicated only when HCV is the dominant active virus |
| [25048716](https://pubmed.ncbi.nlm.nih.gov/25048716/) | 2015 | Review | Hepatology | Immunological basis of antiviral therapy for HBV and HCV; interferon-stimulated genes as treatment predictors; ribavirin discussed exclusively in HCV context |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | Review | Expert Rev Anti-Infect Ther | Treatment options for chronic HBV and HCV in children; IFN-α (without ribavirin) is the backbone for pediatric HBV therapy; ribavirin confined to HCV arm |
| [11160766](https://pubmed.ncbi.nlm.nih.gov/11160766/) | 2001 | Review | Annu Rev Med | Treatment strategies for chronic HBV and HCV; clearly separates IFN + lamivudine for HBV from IFN + Ribavirin for HCV — distinct therapeutic paradigms |
| [15864105](https://pubmed.ncbi.nlm.nih.gov/15864105/) | 2005 | Review | Curr Opin Infect Dis | HBV and HCV infections in children; natural history and therapy; ribavirin role confined to HCV treatment |

---

## Philippines Market Information

Ribavirin is not currently registered with the Philippine FDA (0 approved products). There is no local market presence for any ribavirin-containing product.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **⚠️ Adverse Effect Signal — Hepatic Porphyria (TxGNN Rank #7 Prediction)**: Analysis of the evidence retrieved for the rank-7 prediction (hepatic porphyria) found 16 publications documenting that PegIFN + Ribavirin combination therapy is a **known inducer** of Porphyria Cutanea Tarda (PCT), not a treatment for it. The mechanistic direction is reversed: ribavirin/IFN therapy has been shown to trigger porphyrin accumulation, particularly in patients with underlying iron overload or hereditary hemochromatosis variants (HFE H63D). This is an important safety flag — patients with pre-existing hepatic porphyria risk factors should be regarded as a high-risk or contraindicated group if ribavirin were ever to be evaluated for HBV indications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score of 99.86% is almost certainly a knowledge graph artifact: ribavirin and HBV treatment nodes share interferon-based hepatitis pathway proximity in the KG, not a direct mechanistic or clinical link. Ribavirin is an RNA-targeted antiviral; HBV is a partially double-stranded DNA virus requiring reverse-transcriptase-targeting agents (tenofovir, entecavir). Not one retrieved clinical trial enrolled HBV monoinfection patients for ribavirin treatment, and literature spanning 2000–2020 consistently places ribavirin outside HBV treatment guidelines. Proceeding with development would require building an evidence base essentially from scratch against a target where biological rationale is weak.

**To proceed, the following is needed:**

- **Preclinical HBV validation**: In vitro evidence of ribavirin activity against HBV replication (IMPDH inhibition theoretically depletes GTP available for HBV cccDNA transcription — this requires experimental testing, currently absent)
- **Philippine FDA package insert acquisition**: Full contraindication and warning profile, particularly regarding teratogenicity (Pregnancy Category X) and hemolytic anemia risk
- **Drug interaction (DDI) profile**: DDI data was not retrieved; essential before any combination evaluation with established HBV nucleos(t)ide analogs
- **KG subgraph review**: Audit TxGNN graph to confirm whether the high score reflects interferon-pathway node overlap rather than a true drug–disease mechanistic association
- **Regulatory feasibility assessment**: Zero Philippine registrations means any new indication would require a full de novo filing — a high barrier given the currently weak mechanistic and clinical rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

