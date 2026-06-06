---
layout: default
title: Zidovudine
parent: 僅模型預測 (L5)
nav_order: 356
evidence_level: L5
indication_count: 6
---

# Zidovudine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Zidovudine: From HIV Infection to AIDS-Related Complex

## One-Sentence Summary

Zidovudine (AZT/ZDV) is a nucleoside reverse transcriptase inhibitor (NRTI) historically established as the world's first antiretroviral agent for HIV infection, currently not registered in the Philippines.
The TxGNN model predicts it may be effective for **AIDS-Related Complex (ARC)** — the symptomatic pre-AIDS stage of HIV infection — with **50 relevant clinical trials** and **20 publications** directly supporting this indication.
Among 6 predicted indications spanning veterinary and human diseases, ARC (Rank 5) carries the strongest human clinical evidence at Level L1 (multiple completed Phase 3 RCTs), making it the most actionable repurposing candidate for the Philippines context.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV infection (globally approved WHO Essential Medicine; not currently registered in the Philippines) |
| Predicted New Indication | AIDS-Related Complex (ARC) |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs) |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Zidovudine is a thymidine analogue that exerts its antiviral effect after intracellular phosphorylation to its active triphosphate form (ZDV-TP). ZDV-TP acts as a competitive inhibitor of HIV reverse transcriptase and, once incorporated into the growing viral DNA chain, causes premature chain termination — directly blocking the conversion of HIV's RNA genome into double-stranded DNA, an obligatory step for viral replication. This mechanism is fundamentally independent of the clinical disease stage; wherever HIV is replicating, Zidovudine can act.

AIDS-Related Complex (ARC) is a symptomatic phase of HIV infection (historically defined as CD4+ counts below 500 cells/μL with constitutional symptoms such as fever, weight loss, or lymphadenopathy, short of AIDS-defining opportunistic infections; now classified under "symptomatic HIV infection" in modern terminology). The underlying pathology in ARC is identical to AIDS: ongoing HIV replication progressively depletes CD4+ T lymphocytes and dismantles immune function. By suppressing viral replication, Zidovudine allows partial immune reconstitution, reduction of viral load, and delays disease progression — a mechanistic link that is direct, well-understood, and confirmed by decades of clinical data. The landmark Phase 3 trial NCT00001011 (n=538) was explicitly titled "The Safety and Efficacy of Zidovudine in the Treatment of Patients With Early AIDS Related Complex," and the 1987 NEJM trial by Fischl et al. (PMID 3299089) established efficacy in both AIDS and advanced ARC patients in a placebo-controlled design.

The model's predictions across animal retroviral diseases (Rank 1: feline immunodeficiency virus/FIV; Rank 2: simian immunodeficiency virus/SIV) serve as cross-species mechanistic validation: all three viruses — HIV, FIV, and SIV — are lentiviruses with reverse transcriptase enzymes sharing conserved active sites. Published studies confirm Zidovudine inhibits FIV reverse transcriptase in vitro and reduces plasma virus titers in FIV-infected cats (PMID 7688949), while SIV primate models demonstrate direct ZDV antiviral efficacy (PMID 1489181, 7695293) with resistance mutations (Q151M) identical to those seen in HIV (PMID 9021180). These animal-model predictions are classified as **Research Question** (veterinary scope, no human trial evidence) and should not be confused with the robust human clinical evidence base for ARC. Two other predictions — a rare neurodevelopmental disorder (Rank 3, L5, Hold) and an obsolete hyperlipidemia ontology term (Rank 4, L5, Hold) — lack mechanistic support and are likely knowledge-graph topological artifacts; notably, ZDV's known mitochondrial toxicity (pol-γ inhibition) raises a contraindication concern for the neurodevelopmental indication. The congenital/perinatal HIV indication (Rank 6) also achieves L1 evidence with a "Proceed with Guardrails" recommendation and represents a critical PMTCT (prevention of mother-to-child transmission) application supported by the landmark ACTG 076 trial framework.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00001011](https://clinicaltrials.gov/study/NCT00001011) | Phase 3 | Completed | 538 | Safety and efficacy of ZDV in early ARC: assessed HIV suppression, immune reconstitution, and prevention of AIDS progression; the core RCT directly addressing this indication |
| [NCT00002117](https://clinicaltrials.gov/study/NCT00002117) | Phase 3 | Completed | 528 | Randomized comparison of ddC vs ZDV dose combinations in HIV infection; ZDV arm provided direct ARC/AIDS efficacy and safety data |
| [NCT00001104](https://clinicaltrials.gov/study/NCT00001104) | Phase 3 | Completed | 538 | Placebo-controlled evaluation of ZDV in hemophilic HIV-infected patients; assessed delay in AIDS/ARC progression and ZDV pharmacokinetics |
| [NCT00000736](https://clinicaltrials.gov/study/NCT00000736) | Phase 3 | Completed | 3,200 | ZDV safety and efficacy in asymptomatic HIV infection (n=3,200); compared two doses for preventing ARC and AIDS onset — largest preventive ZDV trial |
| [NCT00000960](https://clinicaltrials.gov/study/NCT00000960) | Phase 3 | Completed | 1,496 | ZDV in HIV-infected pregnant women and newborns (ACTG 076 framework); evaluated intrapartum and neonatal ZDV for mother-to-child HIV transmission prevention |
| [NCT00001075](https://clinicaltrials.gov/study/NCT00001075) | N/A | Completed | 55 | Immunologic consequences of HAART (ritonavir + AZT + 3TC) in moderately advanced HIV-1 disease; evaluated immune reconstitution and viral persistence |
| [NCT00002081](https://clinicaltrials.gov/study/NCT00002081) | N/A | Completed | N/A | Open-label program of ddC + ZDV for advanced HIV disease; observed serious toxicities and antiviral activity of AZT-containing combination therapy |
| [NCT00034086](https://clinicaltrials.gov/study/NCT00034086) | N/A | Completed | 22 | ART intensification immunologic consequences in moderately advanced HIV-1 disease (ACTG 315/375 follow-up); evaluated immune changes with regimen modification |
| [NCT00000986](https://clinicaltrials.gov/study/NCT00000986) | Phase 1 | Completed | 18 | Safety and tolerance of IL-2 combined with ZDV in AIDS/ARC patients (≥6 weeks prior ZDV); assessed immune stimulation on top of NRTI background |
| [NCT00002063](https://clinicaltrials.gov/study/NCT00002063) | N/A | Completed | N/A | AZT vs placebo in ARC: time to AIDS progression or death, CD4 response, and clinical outcomes — foundational ARC-specific efficacy study |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3299089](https://pubmed.ncbi.nlm.nih.gov/3299089/) | 1987 | RCT | N Engl J Med | Landmark placebo-controlled ZDV trial (n=282): significantly reduced mortality and opportunistic infections in patients with AIDS and advanced ARC — basis for global regulatory approval |
| [2677429](https://pubmed.ncbi.nlm.nih.gov/2677429/) | 1989 | RCT | JAMA | Prolonged ZDV therapy (n=229, mean 21 months): 84.5% and 57.6% survival at 12 and 24 months in original ZDV group vs rapid decline in delayed-treatment group |
| [1777174](https://pubmed.ncbi.nlm.nih.gov/1777174/) | 1991 | RCT | AIDS | Double-blind multicenter RCT of ZDV ± acyclovir in ARC (n=199, 8 European countries + Australia): ZDV significantly delayed AIDS-defining opportunistic infections and improved performance status |
| [2159705](https://pubmed.ncbi.nlm.nih.gov/2159705/) | 1990 | RCT | Am J Med | Alternating ZDV/ddC regimens in AIDS and ARC: demonstrated maintained antiviral efficacy with substantially reduced hematologic toxicity compared to ZDV monotherapy |
| [2191113](https://pubmed.ncbi.nlm.nih.gov/2191113/) | 1990 | RCT Sub-analysis | J Acquir Immune Defic Syndr | Quality-of-life sub-analysis of ZDV placebo-controlled trial (n=31): significant QoL improvement on Karnofsky and Quality of Well-Being scales vs placebo |
| [2159707](https://pubmed.ncbi.nlm.nih.gov/2159707/) | 1990 | Phase I/II Clinical Trial | Am J Med | ZDV + ddC combination in AIDS and advanced ARC: Phase I/II evaluation confirming safety and additive antiviral activity of dual NRTI therapy |
| [1894937](https://pubmed.ncbi.nlm.nih.gov/1894937/) | 1991 | Interventional Cohort | J Infect Dis | ZDV therapy improved pneumococcal vaccine antibody responses in AIDS/ARC patients (n=38); ZDV-treated patients showed responses comparable to asymptomatic HIV-infected individuals |
| [1974727](https://pubmed.ncbi.nlm.nih.gov/1974727/) | 1990 | Clinical Study | Rev Infect Dis | Phase I ddI in AIDS/ARC (n=36): 13/18 patients were ZDV-intolerant; established the clinical context that necessitated alternative NRTIs and documented ZDV's hematologic dose-limiting toxicity profile |
| [2224694](https://pubmed.ncbi.nlm.nih.gov/2224694/) | 1990 | Review | CMAJ | Comprehensive review of ZDV efficacy and safety across all stages of HIV infection including ARC; synthesized pivotal trial data for clinical decision-making |
| [2197818](https://pubmed.ncbi.nlm.nih.gov/2197818/) | 1990 | Review | DICP | ZDV update: lower daily dose (500 mg/d) shown comparable in efficacy to higher doses with fewer adverse effects; established as the accepted standard for AIDS/ARC against which all other agents were benchmarked |

---

## Philippines Market Information

Zidovudine currently has **no registered products** in the Philippines. The FDA Philippines has no authorization records on file. This represents a significant access gap: Zidovudine appears on the WHO Model List of Essential Medicines (Core List) and is registered in neighboring countries including Thailand, Indonesia, and Vietnam for HIV treatment and PMTCT programs.

> If pursuing registration, note that the drug is commercially available as Retrovir® (GSK) or as generic formulations (capsules 100 mg, 250 mg; oral solution 10 mg/mL; IV solution 10 mg/mL) in other markets.

---

## Safety Considerations

No Philippines-specific package insert data is available (Data Gap DG001). Based on globally established pharmacology and published safety evidence:

- **Hematologic Toxicity (Primary Safety Concern)**: Dose-dependent myelosuppression is the most clinically significant adverse effect. Anemia and neutropenia are common and may require dose reduction, recombinant erythropoietin support, or treatment discontinuation. Monitoring: CBC with differential every 2–4 weeks for the first 3 months, then monthly.
- **Mitochondrial Toxicity**: Long-term use inhibits mitochondrial DNA polymerase-γ, leading to myopathy (skeletal muscle weakness with elevated CK), lactic acidosis, and hepatic steatosis. These are NRTI class effects but are more pronounced with thymidine analogues (ZDV, d4T). Monitor: creatine kinase, serum lactate, liver function tests (AST, ALT, alkaline phosphatase).
- **Cardiac Safety (Perinatal Context)**: PMID 26687320 and registry data (Antiretroviral Pregnancy Registry) have investigated ZDV prenatal exposure and congenital heart defects; evidence remains inconclusive. Requires specific monitoring in PMTCT programs.
- **Drug Resistance**: Prolonged ZDV monotherapy selects for thymidine analogue mutations (TAMs: M41L, D67N, K70R, L210W, T215Y/F, K219Q/E) and Q151M, cross-reducing susceptibility to other NRTIs. Baseline genotypic resistance testing is required before initiating therapy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Zidovudine has Level L1 evidence (multiple completed Phase 3 RCTs) for both AIDS-Related Complex (ARC) and congenital/perinatal HIV infection, including the directly titled Phase 3 trial NCT00001011 (n=538, specifically addressing early ARC) and the foundational 1987 NEJM publication (PMID 3299089). As a WHO Essential Medicine with over three decades of clinical use, evidence strength is not the limiting factor — the primary barrier to Philippines patient access is the absence of local FDA registration.

**To proceed, the following is needed:**

- **Philippines FDA registration**: Prepare a complete Common Technical Document (CTD) dossier for FDA Philippines market authorization; leverage existing WHO prequalification data and reference country approvals to support the application
- **Package insert localization**: Obtain Philippines-compliant product labeling including complete warnings, contraindications, and prescribing information (resolves Data Gap DG001)
- **MOA documentation**: Retrieve complete mechanism-of-action and pharmacology data from DrugBank API (resolves Data Gap DG002)
- **Hematologic monitoring protocol**: Establish a mandatory CBC monitoring schedule (baseline + every 2–4 weeks for first 3 months, monthly thereafter) as a condition of use
- **Resistance genotyping**: Baseline NRTI genotypic resistance testing for all new initiations (TAMs, K65R, M184V, Q151M)
- **Guideline positioning review**: Zidovudine is now classified as second-line in most international HIV guidelines (WHO 2021, DHHS) due to hematologic toxicity; tenofovir-based regimens are preferred. Philippines ART guideline alignment is required before positioning ZDV in treatment algorithms
- **PMTCT program review**: For the congenital HIV indication (Rank 6, also L1 evidence), review WHO PMTCT Option B+ protocols and dedicated pediatric ZDV dosing data (PMID 8419601; NCT00001007) to determine formulary inclusion for neonatal prophylaxis

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any clinical application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

