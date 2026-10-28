---
layout: default
title: Ritonavir
parent: Model Prediction Only (L5)
nav_order: 299
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Ritonavir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infection / AIDS"
monitor_inn: "Ritonavir"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Ritonavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Ritonavir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Ritonavir is an HIV protease inhibitor, originally used for HIV infection/AIDS and hepatitis C virus infection.
The TxGNN model's top-ranked prediction is feline acquired immunodeficiency syndrome. However, the best-supported prediction is **simian immunodeficiency virus (SIV) infection**, with **0 clinical trials** and **10 publications** (all preclinical or indirect). This report therefore covers SIV infection as the lead candidate and also notes the other two predictions.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection / AIDS; chronic hepatitis C virus infection (the Philippines registration has no indication text on file) |
| Predicted New Indication | Simian immunodeficiency virus infection (rank 1 by score is feline acquired immunodeficiency syndrome, which has no supporting evidence) |
| TxGNN Prediction Score | 0.9992 (the same for the top two predictions) |
| Evidence Level | L5 (preclinical studies only); feline AIDS and the neurodevelopmental disorder are L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Based on known information, ritonavir is an HIV-1 protease inhibitor, also used at low dose as a pharmacokinetic booster through CYP3A4 inhibition. Its efficacy in HIV infection is established.

SIV is a lentivirus closely related to HIV, and its protease is susceptible to HIV-1 protease inhibitors. An in vitro study found ritonavir inhibited SIVmac239 with an EC50 of about 13 nM, compared with about 25 nM for HIV-1. This gives a plausible mechanistic link.

There is little repurposing gain, though. SIV infection is an animal model disease with no direct human clinical indication. Its value is as a translational model for HIV, which is already an approved use.

The other two predictions are weaker:
- **Feline AIDS:** FIV is a lentivirus, so protease inhibition is plausible in principle. But FIV protease differs from HIV-1 protease in substrate specificity and inhibitor sensitivity. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases such as HIV/AIDS, not biological evidence.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter:** No plausible mechanistic link is evident. This is a rare genetic disorder unrelated to ritonavir's known actions. The identical score (0.9992) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered, for any of the three predicted indications.

## Literature Evidence

The table lists the most relevant publications for SIV infection. All are preclinical or in vitro; none is a human RCT.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro | Antimicrob Agents Chemother | SIVmac239 was inhibited by indinavir, saquinavir and ritonavir (EC50 about 13 nM for ritonavir), comparable to HIV-1 |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro | Antivir Ther | Susceptibility of HIV-2, SIV and SHIV to 16 approved anti-HIV drugs, with implications for treatment and post-exposure prophylaxis |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Preclinical (macaque) | J Virol Methods | Oral HAART including lopinavir/ritonavir in SHIV-infected macaques, assessing effects on the CD8 subset (2 animals) |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Preclinical (macaque) | J Virol | Rapid viral decay in SIV-infected macaques given quadruple antiretroviral therapy |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Preclinical (macaque) | PLoS Pathog | A highly intensified multidrug ART regimen gave long-term viral suppression and a restricted reservoir in a simian AIDS model |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Preclinical (macaque) | PLoS One | Suppressive combination ART plus the HDAC inhibitor SAHA in SIV-infected rhesus macaques |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Review/Preclinical | mBio | Lentiviruses persist in the brain despite effective ART |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Preclinical | Microbes Infect | A novel SHIV with an HIV-1 protease gene, a tool for in vivo testing of protease inhibitors in macaques |

Most of these studies used combination regimens, so ritonavir-specific effects cannot be isolated. No literature was supplied for feline AIDS or the neurodevelopmental disorder.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0428 | Ritonavir | Not specified | Not specified (registration valid) |

## Safety Considerations

**Contraindications flagged by the knowledge graph** (these come from knowledge-graph drug-disease edges, not package insert text):
- **Cardiac:** long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, heart conduction disease, atrioventricular block, cardiomyopathy (including hypertrophic), myocardial ischemia, coronary artery disease, endomyocardial fibrosis
- **Liver and pancreas:** liver disease, cirrhosis, pancreatitis, gallbladder disease, hyperbilirubinemia (including Gilbert syndrome), chronic hepatitis B virus infection
- **Metabolic:** diabetes mellitus, hyperglycemia, diabetic ketoacidosis, hypertriglyceridemia, familial combined hyperlipidemia, gout/hyperuricemia, potassium deficiency
- **Bleeding:** hemophilia

**Drug interactions:** 100 interactions were found in total. The 20 retrieved include these major-level ones:
- Loperamide
- Triamcinolone
- Budesonide

Moderate-level examples include metformin, acarbose, alogliptin, albiglutide, canagliflozin, chlorpropamide, hydrocortisone, dexamethasone, betamethasone, bupropion, aprepitant, clarithromycin, metronidazole, alosetron and lorcaserin. The interactions with antidiabetic drugs are noteworthy given the hyperglycemia flag above.

Package insert warnings and contraindications for the Philippines are not available. Please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The high TxGNN scores (about 0.9992) are not backed by any clinical trial. For SIV infection, the preclinical data support plausibility, but SIV is an animal model disease with no human indication, so the repurposing gain is minimal. Feline AIDS and the neurodevelopmental disorder have no supporting evidence.
- The only Philippines registration is cancelled, and the safety profile is substantial (cardiac, hepatic, metabolic and interaction concerns).
- SIV infection is best treated as a research question for translational HIV modelling, not a development candidate.

**To proceed, the following is needed:**
- Detailed mechanism-of-action data
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Ritonavir-specific (not combination-regimen) data in SIV or FIV models
- A target-level rationale before considering the neurodevelopmental disorder
- Clarification of the current Philippines registration status and approved indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

