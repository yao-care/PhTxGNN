---
layout: default
title: Rifabutin
parent: 僅模型預測 (L5)
nav_order: 290
evidence_level: L5
indication_count: 10
---

# Rifabutin
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

# Rifabutin: From MAC Prophylaxis in AIDS to HIV Infectious Disease

## One-Sentence Summary

Rifabutin (Mycobutin®) is a rifamycin-class antibiotic internationally approved for prevention and treatment of Mycobacterium avium complex (MAC) bacteremia in AIDS/HIV patients, though currently not registered in the Philippines.
The TxGNN model predicts it may be effective for **HIV Infectious Disease** broadly, with **29 clinical trials** and **20 publications** currently supporting this direction.
The evidence level is L1, underpinned by multiple completed Phase 3 RCTs, and FDA/EMA have already approved this indication under the Mycobutin® brand.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Philippines; internationally approved for MAC prophylaxis/treatment in HIV/AIDS patients (Mycobutin®) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L1 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Philippines regulatory database. Based on known information, Rifabutin belongs to the rifamycin class of antibiotics and acts as a bacterial RNA polymerase inhibitor, binding to the β-subunit of RNA polymerase (rpoB) to block transcription in mycobacterial species. It demonstrates particularly high potency against Mycobacterium avium complex (MAC) — the most common opportunistic pathogen causing bacteremia in severely immunocompromised HIV patients with CD4 counts below 200 cells/mm³. Multiple landmark trials in the 1990s established its efficacy for MAC prophylaxis and treatment, leading to FDA and EMA approval as Mycobutin®.

Beyond MAC, rifabutin plays a critical role in HIV/TB coinfection management. HIV-infected patients have an annual TB reactivation risk 10 times higher than HIV-negative individuals, and treating both infections simultaneously requires careful consideration of drug-drug interactions. Rifabutin is a significantly weaker inducer of CYP3A4 compared to rifampicin, making it the preferred rifamycin when patients are receiving protease inhibitor (PI)- or NNRTI-based antiretroviral therapy. This pharmacokinetic advantage means rifabutin can be safely co-administered with most antiretroviral regimens where rifampicin would cause unacceptable reductions in ART drug exposure.

The TxGNN prediction therefore captures a biologically coherent relationship: rifabutin's role spans MAC prophylaxis, MAC treatment, and TB co-treatment — all within the HIV infectious disease framework. The knowledge graph nodes linking rifabutin to HIV reflect this established clinical reality, which is why the evidence base is exceptionally strong (L1) and the prediction score approaches 100%.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT00002267](https://clinicaltrials.gov/study/NCT00002267) | NA | Completed | 750 | Double-blind, placebo-controlled RCT assessing rifabutin monotherapy for prevention of MAC bacteremia in AIDS patients with CD4 ≤ 200; primary endpoints include incidence of MAC and survival benefit |
| [NCT00002101](https://clinicaltrials.gov/study/NCT00002101) | Phase 3 | Completed | 450 | Three-arm RCT comparing clarithromycin/ethambutol with placebo, rifabutin 300 mg, or rifabutin 450 mg for MAC bacteremia in AIDS; primary endpoint: ≥2-log CFU reduction sustained through 16 weeks |
| [NCT00001030](https://clinicaltrials.gov/study/NCT00001030) | Phase 3 | Completed | 1,100 | Prospective RCT comparing clarithromycin alone vs. rifabutin alone vs. combination for prevention of MAC bacteremia in HIV patients with CD4 ≤ 100 cells/mm³; also captured survival and quality of life |
| [NCT00001047](https://clinicaltrials.gov/study/NCT00001047) | Phase 3 | Completed | 400 | Open-label RCT comparing clarithromycin + ethambutol + rifabutin vs. clarithromycin + ethambutol + clofazimine at two clarithromycin doses for disseminated MAC in AIDS patients |
| [NCT00002122](https://clinicaltrials.gov/study/NCT00002122) | Phase 3 | Completed | 720 | RCT evaluating azithromycin and rifabutin alone or combined for MAC prevention; secondary arm assessed daily vs. weekly fluconazole for deep fungal infection prevention |
| [NCT00001995](https://clinicaltrials.gov/study/NCT00001995) | NA | Completed | 200 | Double-blind RCT of rifabutin-containing regimen to eradicate or reduce MAC organisms in AIDS patients; assessed symptom improvement and survival outcomes |
| [NCT03478033](https://clinicaltrials.gov/study/NCT03478033) | NA | Unknown | 230 | Prospective multicenter cohort comparing standard rifampicin vs. rifabutin-based TB treatment in HIV/AIDS patients with pulmonary TB; evaluates antiviral efficacy and drug-drug interactions with ART |
| [NCT00651066](https://clinicaltrials.gov/study/NCT00651066) | Phase 2 | Completed | 47 | Phase II PK trial in Vietnam evaluating rifabutin as a rifampicin replacement in HIV/TB coinfected patients on various ART regimens; supports rifabutin as preferred rifamycin with PI/NNRTI-based ART |
| [NCT01601626](https://clinicaltrials.gov/study/NCT01601626) | Phase 2 | Terminated | 71 | Phase 2b RCT comparing double-dose LPV/r + rifampin vs. standard-dose LPV/r + rifabutin ± raltegravir in HIV-1 patients requiring PI-based ART and active TB treatment; terminated early, data limited |
| [NCT00810446](https://clinicaltrials.gov/study/NCT00810446) | N/A | Completed | 72 | Japanese regulatory post-marketing commitment surveillance of Mycobutin® in HIV-infected patients; collected real-world safety data including unknown adverse reactions over 9 years |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [23828580](https://pubmed.ncbi.nlm.nih.gov/23828580/) | 2013 | Systematic Review | Cochrane Database Syst Rev | Meta-analysis comparing rifamycins (rifampicin, rifabutin, rifapentine) vs. isoniazid for TB prevention in HIV-negative high-risk individuals; supports rifabutin as an effective LTBI prophylaxis option with shorter treatment duration and comparable completion rates |
| [25404581](https://pubmed.ncbi.nlm.nih.gov/25404581/) | 2014 | Systematic Review | Evidence-Based Child Health | Cochrane review update on rifamycins vs. isoniazid for TB prophylaxis; reaffirms rifabutin efficacy in latent TB prevention, supporting use as an isoniazid alternative |
| [33294914](https://pubmed.ncbi.nlm.nih.gov/33294914/) | 2021 | Cohort/PK Study | J Antimicrob Chemother | PK and safety of rifabutin in HIV/TB coinfected children receiving lopinavir/ritonavir-based second-line ART; highlights neutropenia risk and limited pediatric dosing data |
| [31139825](https://pubmed.ncbi.nlm.nih.gov/31139825/) | 2019 | Cohort | J Antimicrob Chemother | Safety and efficacy evaluation of rifabutin in HIV/TB coinfected children on PI-based ART; treatment-limiting neutropenia in 2/6 patients underscores need for hematologic monitoring |
| [25281400](https://pubmed.ncbi.nlm.nih.gov/25281400/) | 2015 | PK Study | J Antimicrob Chemother | Short-term safety and pharmacokinetics of rifabutin with lopinavir/ritonavir in young HIV-infected children (≤5 years); characterizes DDI profile to guide pediatric dosing strategies |
| [28233512](https://pubmed.ncbi.nlm.nih.gov/28233512/) | 2017 | Review | Microbiol Spectrum | Comprehensive review of TB-HIV coinfection; describes bidirectional disease synergy and positions rifabutin as the recommended rifamycin for patients on PI-based ART regimens |
| [21726477](https://pubmed.ncbi.nlm.nih.gov/21726477/) | 2009 | Review | BMJ Clin Evid | Evidence-based review on treating TB in HIV patients; establishes rifabutin as preferred over rifampicin when patients receive PI-based ART, based on superior DDI profile |
| [7736687](https://pubmed.ncbi.nlm.nih.gov/7736687/) | 1995 | PK Review | Clin Pharmacokinet | Landmark pharmacokinetics review of rifabutin; characterizes oral bioavailability (~20%), extensive tissue distribution, and CYP3A4 induction profile compared to rifampicin |
| [40310456](https://pubmed.ncbi.nlm.nih.gov/40310456/) | 2025 | Review | PNAS | Review of next-generation rifamycins; discusses rifabutin's current role in NTM infections and its CYP3A4 induction profile relative to newer rifamycin analogs under development |
| [9459473](https://pubmed.ncbi.nlm.nih.gov/9459473/) | 1998 | Observational | JAMA | HIV Outpatient Study (HOPS) showing possible effectiveness of clarithromycin + rifabutin as chemoprophylaxis for cryptosporidiosis in HIV disease, suggesting additional opportunistic infection benefit |

---

## Philippines Market Information

Rifabutin currently has **no registered products** with the Philippine FDA. No license records are available for any brand or formulation in the Philippines.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs (NCT00002101 n=450, NCT00001030 n=1,100, NCT00001047 n=400, NCT00002122 n=720) provide L1 evidence supporting rifabutin's efficacy in HIV-associated MAC disease, and the drug is already FDA- and EMA-approved as Mycobutin®. The Philippines currently has no registered product, but the international evidence base is exceptionally mature and the clinical need in HIV-infected patients is well-established.

**To proceed, the following is needed:**
- Philippine FDA registration application, including submission of existing international approval dossiers (FDA USA, EMA) for bridging review
- Full prescribing information (package insert) with complete warnings, contraindications, and drug interaction listings — currently unavailable for this evidence pack
- Mechanism of action documentation from DrugBank or equivalent source (currently a high-severity data gap)
- Drug-drug interaction management protocol for co-administration with antiretroviral agents, particularly protease inhibitors (lopinavir/ritonavir, darunavir/ritonavir) and integrase inhibitors (dolutegravir, cabotegravir)
- Safety monitoring plan addressing known rifabutin toxicities: ophthalmologic monitoring for uveitis (especially when combined with clarithromycin or azole antifungals) and hematologic monitoring (CBC for neutropenia/thrombocytopenia)
- Identification of a Philippine distribution partner and assessment of cold-chain/specialty pharmacy infrastructure for access through HIV treatment programs (e.g., Pilipinas CEAP, DOH HIV treatment hubs)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

