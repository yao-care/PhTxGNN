---
layout: default
title: Bedaquiline
parent: Model Prediction Only (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Bedaquiline: predicted new indication Inactive tuberculosis (evidence level L5). Approved use: Pulmonary tuberculosis"
monitor_inn: "Bedaquiline"
predicted_indications: ["vulvovaginal candidiasis", "fascioliasis", "urea cycle disorder", "esophageal candidiasis"]
---

# Bedaquiline
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

# Bedaquiline: From Multidrug-Resistant Tuberculosis to Inactive Tuberculosis

## One-Sentence Summary

Bedaquiline is an anti-tuberculosis drug originally used for pulmonary tuberculosis and multidrug-resistant tuberculosis (MDR-TB).
The TxGNN model predicts it may be effective for **inactive tuberculosis** (including latent infection and prevention in contacts),
with **3 clinical trials** (all ongoing or not yet recruiting, none with results) and **19 publications** (mostly reviews) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis; multidrug-resistant tuberculosis |
| Predicted New Indication | Inactive tuberculosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L2 (based on trial design; see note below) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

Note: the top-ranked prediction by score is "tuberculosis, bovine" (99.96%), but it has only an in vitro methodology paper (L4, Hold). Inactive tuberculosis is the best-supported prediction and is the focus of this report. The L2 grade rests on the design of ongoing Phase 2/3 trials, not on reported outcomes, so it should be read cautiously.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the literature, bedaquiline inhibits the ATP synthase of *Mycobacterium tuberculosis* (the AtpE subunit). A 2021 *Nature* paper describes the structure of mycobacterial ATP synthase bound to bedaquiline, and a 2024 review covers F-ATP synthase inhibitors.

Inactive (latent) TB is caused by the same organism that bedaquiline already treats in active MDR-TB. Dormant, non-replicating bacteria depend on energy metabolism, which is the pathway bedaquiline blocks. Using the drug to treat latent infection or to prevent disease in high-risk contacts is therefore a plausible extension of its approved use. The BREACH-TB trial tests exactly this idea, using 4 weeks of bedaquiline for prevention.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06568484](https://clinicaltrials.gov/study/NCT06568484) | Phase 2/3 | Recruiting | 2530 | BREACH-TB: open-label non-inferiority trial of 4 weeks of bedaquiline vs standard regimen to prevent TB disease over 72 weeks in people living with HIV and high-risk close contacts. No results yet. |
| [NCT05766267](https://clinicaltrials.gov/study/NCT05766267) | Phase 2/3 | Active, not recruiting | 288 | CRUSH-TB: 17-week bedaquiline-based regimens (with moxifloxacin, pyrazinamide, plus rifabutin or delamanid) vs standard 6-month treatment. Studies active pulmonary TB, so only indirectly relevant. |
| [NCT07069582](https://clinicaltrials.gov/study/NCT07069582) | Phase 1 | Not yet recruiting | 60 | Single-dose pharmacokinetic study of anti-TB drugs, including bedaquiline, in plasma and breast milk of breastfeeding women. Informs exposure and safety only. |

## Literature Evidence

No randomized controlled trials were found. The most relevant publications are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33299175](https://pubmed.ncbi.nlm.nih.gov/33299175/) | 2021 | Structural study | Nature | Structure of mycobacterial ATP synthase bound to bedaquiline; the drug can sterilize latent *M. tuberculosis*. |
| [28625141](https://pubmed.ncbi.nlm.nih.gov/28625141/) | 2018 | Review | Recent Pat Anti-Infect Drug Discov | Bedaquiline as a basis for shorter and better anti-TB regimens. |
| [39766559](https://pubmed.ncbi.nlm.nih.gov/39766559/) | 2024 | Review | Antibiotics (Basel) | F-ATP synthase inhibitors and targets in *M. tuberculosis*, including dormant bacteria. |
| [36915977](https://pubmed.ncbi.nlm.nih.gov/36915977/) | 2022 | Review | Zhejiang Da Xue Xue Bao Yi Xue Ban | Progress in diagnosis and treatment of latent TB infection. |
| [33837535](https://pubmed.ncbi.nlm.nih.gov/33837535/) | 2021 | Review | Clin Pharmacol Ther | Treatment of TB, with differences between latent and active disease therapy. |
| [29580819](https://pubmed.ncbi.nlm.nih.gov/29580819/) | 2018 | Review | Lancet Infect Dis | Progress in new drugs, shorter regimens and host-directed therapies. |
| [38003836](https://pubmed.ncbi.nlm.nih.gov/38003836/) | 2023 | Review | Pathogens | Pediatric drug-resistant TB, with bedaquiline-based regimens and preventive strategies. |
| [39301910](https://pubmed.ncbi.nlm.nih.gov/39301910/) | 2025 | Review | Infect Disord Drug Targets | Bedaquiline delivery systems for MDR-TB; notes activity against persistent or latent forms. |
| [39887565](https://pubmed.ncbi.nlm.nih.gov/39887565/) | 2025 | Review | Respirology | Clinical update on TB as a disease spectrum, including subclinical disease. |
| [28776518](https://pubmed.ncbi.nlm.nih.gov/28776518/) | 2017 | Review | Int J Mycobacteriol | Drugs targeting non-replicating TB bacilli. |

## Philippines Market Information

One registration was found (PNF-0043, Bedaquiline, single-ingredient product). It is **cancelled**, and the dosage form and approved indication are not listed. No currently valid registration exists in the data compiled for this report. This status may be a data artifact and should be verified with the DOH-FDA Philippines.

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 interacting drugs. Examples of **Major** interactions: dexamethasone, clarithromycin, dolasetron, palonosetron, picosulfuric acid, sodium sulfate, and polyethylene glycol (3350 with electrolytes). **Moderate** examples: acarbose, famotidine, doxycycline, minocycline, tetracycline, pioglitazone, loperamide, bupropion, bisacodyl, chenodeoxycholic acid, oxandrolone, oxymetholone, and naltrexone.
- **Other points raised in the predicted-indication analysis** (not from package insert data): QT prolongation risk, hepatotoxicity monitoring, and the need for resistance surveillance.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Bedaquiline's mechanism is plausible for inactive TB, and a large Phase 2/3 prevention trial (BREACH-TB) is under way. However, no trial results exist yet, the literature is mainly reviews, and the Philippines registration is cancelled. The evidence supports further evaluation, not clinical adoption.

**To proceed, the following is needed:**
- Results from BREACH-TB (NCT06568484), the key trial for this indication
- Package insert warnings and contraindications from the DOH-FDA Philippines (a blocking gap for safety screening)
- Confirmation of the registration status of PNF-0043
- Detailed mechanism of action data from DrugBank
- A safety plan covering QT monitoring, liver function, drug interaction screening (especially CYP3A4 inducers and inhibitors), and resistance surveillance

**Other predictions (for reference):**
- Tuberculoma: L4, research question only (case reports of bedaquiline-based regimens in CNS TB; CNS penetration is limited).
- Bovine TB, tuberculous ascites, cutaneous TB: Hold (evidence is in vitro or tangential safety literature).
- Avian TB, vulvovaginal candidiasis, fascioliasis, urea cycle disorder, esophageal candidiasis: Hold (prediction score only; for the non-mycobacterial conditions, no plausible mechanism and likely knowledge-graph artifacts).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

