---
layout: default
title: Rifabutin
parent: Model Prediction Only (L5)
nav_order: 293
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
monitor_inn: "Rifabutin"
predicted_indications: ["HIV infectious disease", "multiple endocrine neoplasia", "sclerosing cholangitis", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "conjunctivitis", "leprosy", "endocarditis", "pneumocystosis", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection"]
description: "Rifabutin: predicted new indication HIV infectious disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Rifabutin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Rifabutin: HIV infectious disease
{: .text-alpha }

## One-Sentence Summary

Rifabutin is a rifamycin antibiotic that acts against mycobacteria.
The TxGNN model predicts it may be useful for **HIV infectious disease**. The studies compiled for this report (more than 30 registered trials and about 20 publications) mostly address tuberculosis or *Mycobacterium avium* complex (MAC) in people living with HIV, or drug interactions with antiretrovirals. None of them treats HIV infection itself, so the evidence level is **L5**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Rifabutin is a rifamycin that inhibits mycobacterial RNA polymerase (the rpoB target). It has no known direct antiretroviral activity.

The link to HIV is indirect. People with advanced HIV are prone to mycobacterial opportunistic infections, namely MAC and tuberculosis, and rifabutin is used in these settings. It is a weaker inducer of the liver enzyme CYP3A4 than rifampin. That makes it easier to combine with some antiretrovirals, such as protease inhibitors, although dose adjustment is still needed.

The high model score probably reflects this close association with HIV-related care. The evidence supports HIV-associated mycobacterial disease, not treatment of HIV infection. Any further work would need to define the indication as HIV-associated MAC or TB rather than HIV infection.

---

## Clinical Trial Evidence

None of the registered trials tests rifabutin as a treatment for HIV infection itself. The trials below involve people with HIV and concern opportunistic mycobacterial infections or drug interactions.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002101](https://clinicaltrials.gov/study/NCT00002101) | Phase 3 | Completed | 450 | Clarithromycin/ethambutol with rifabutin (two doses) or placebo for MAC bacteremia in AIDS |
| [NCT00001047](https://clinicaltrials.gov/study/NCT00001047) | Phase 3 | Completed | 400 | Four regimens, including clarithromycin with ethambutol and either rifabutin or clofazimine, for disseminated MAC in AIDS |
| [NCT00001030](https://clinicaltrials.gov/study/NCT00001030) | Phase 3 | Completed | 1100 | Clarithromycin vs rifabutin vs both for preventing MAC bacteremia in HIV with CD4 ≤100 |
| [NCT00002122](https://clinicaltrials.gov/study/NCT00002122) | Phase 3 | Completed | 720 | Azithromycin and rifabutin, alone and combined, for preventing disseminated MAC in HIV |
| [NCT00001995](https://clinicaltrials.gov/study/NCT00001995) | Not labeled | Completed | 200 | Double-blind trial of a rifabutin regimen for MAC bacteremia in AIDS |
| [NCT00001058](https://clinicaltrials.gov/study/NCT00001058) | Phase 2 | Completed | 246 | Clarithromycin combined with rifabutin, ethambutol, or both for disseminated MAC in AIDS |
| [NCT00023361](https://clinicaltrials.gov/study/NCT00023361) | Not labeled | Completed | 215 | Intermittent rifabutin-based regimen for HIV-related tuberculosis |
| [NCT00651066](https://clinicaltrials.gov/study/NCT00651066) | Phase 2 | Completed | 47 | Rifabutin pharmacokinetics with antiretroviral therapy in TB/HIV (Vietnam) |
| [NCT00640887](https://clinicaltrials.gov/study/NCT00640887) | Phase 2 | Completed | 48 | Rifabutin pharmacokinetics with antiretroviral therapy in TB/HIV (South Africa) |
| [NCT00001023](https://clinicaltrials.gov/study/NCT00001023) | Not labeled | Completed | 91 | Safety, tolerance and pharmacokinetics of rifabutin with clarithromycin or azithromycin in HIV |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33294914](https://pubmed.ncbi.nlm.nih.gov/33294914/) | 2021 | Cohort | J Antimicrob Chemother | Rifabutin pharmacokinetics and safety in TB/HIV-coinfected children on lopinavir/ritonavir; an earlier study was stopped early because of severe neutropenia |
| [31139825](https://pubmed.ncbi.nlm.nih.gov/31139825/) | 2019 | Cohort | J Antimicrob Chemother | Safety and efficacy of rifabutin in HIV/TB-coinfected children on lopinavir/ritonavir-based ART; treatment-limiting neutropenia reported in earlier work |
| [39037240](https://pubmed.ncbi.nlm.nih.gov/39037240/) | 2024 | Pharmacokinetic study | Antimicrob Agents Chemother | Population pharmacokinetics and dose optimization of rifabutin in HIV/TB children on lopinavir/ritonavir |
| [36377436](https://pubmed.ncbi.nlm.nih.gov/36377436/) | 2023 | Modeling study | Clin Infect Dis | Managing interactions between long-acting cabotegravir/rilpivirine and inducers such as rifabutin |
| [36385424](https://pubmed.ncbi.nlm.nih.gov/36385424/) | 2023 | Pharmacokinetic model | Br J Clin Pharmacol | Population pharmacokinetic model of the dolutegravir–rifabutin interaction |
| [17181373](https://pubmed.ncbi.nlm.nih.gov/17181373/) | 2006 | Review | Drugs | Practical therapeutic approach to TB/HIV co-infection, including rifamycin and antiretroviral interactions |
| [28233512](https://pubmed.ncbi.nlm.nih.gov/28233512/) | 2017 | Review | Microbiol Spectr | Overview of tuberculosis associated with HIV infection |
| [9093233](https://pubmed.ncbi.nlm.nih.gov/9093233/) | 1997 | Review | Med Clin North Am | Nontuberculous mycobacterial infections, with MAC as the most common systemic bacterial infection in AIDS |
| [8785257](https://pubmed.ncbi.nlm.nih.gov/8785257/) | 1996 | Review | Clin Infect Dis | Rifabutin in pulmonary TB, including HIV-infected patients |
| [11996607](https://pubmed.ncbi.nlm.nih.gov/11996607/) | 2002 | Review | Arch Intern Med | Update on rifampin and rifabutin drug interactions |

---

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Rifabutin | Oral |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 entries. The 20 shown in the compiled data include one major interaction, with **eliglustat**. Most of the rest are moderate: doxycycline, clarithromycin, metronidazole, aprepitant, morphine, pioglitazone, saxagliptin, linagliptin, chlorpropamide, acetohexamide, and several corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone) and vitamin D analogues (cholecalciferol, calcifediol, calcitriol). Dolasetron is minor.
- **Antiretroviral interactions**: Trials and publications show clinically important interactions with protease inhibitors, cabotegravir/rilpivirine, dolutegravir and other antiretrovirals. Dose adjustment is required.
- **Haematological and ocular effects**: The cited literature reports treatment-limiting neutropenia in children on protease-inhibitor-based ART, and uveitis, especially with certain co-medications.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Rifabutin is established in HIV-associated mycobacterial disease, but no cited study treats HIV infection itself, so the prediction is supported only at the L5 (model prediction) level. The high score appears to reflect this association rather than antiretroviral activity.

**To proceed, the following is needed:**
- A clearly defined indication, such as HIV-associated MAC or TB, assessed separately from HIV infection
- Mechanism-of-action data
- Package insert warnings and contraindications for the local product
- A plan for managing interactions with antiretrovirals
- Haematological monitoring (neutropenia) and ocular monitoring (uveitis)

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "Confirm the original approved indication and the registration pathway, since the only license is cancelled" | No longer present after the report was regenerated (2026-11-12: the report was regenerated in 2026-11 and no longer contains this statement; was: Corrected) | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

