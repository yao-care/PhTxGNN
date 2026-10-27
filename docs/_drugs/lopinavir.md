---
layout: default
title: Lopinavir
parent: Model Prediction Only (L5)
nav_order: 212
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Lopinavir: predicted new indication Feline acquired immunodeficiency syndrome . Simian immunodeficiency v… (evidence level L5). Approved use: HIV infection, AIDS"
monitor_inn: "Lopinavir"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Lopinavir
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

## Lopinavir: From HIV Infection to Simian Immunodeficiency Virus Infection
{: .text-alpha }

## One-Sentence Summary

Lopinavir is an HIV-1 protease inhibitor, originally used to treat HIV infection and AIDS.
The TxGNN model's top-ranked prediction is feline acquired immunodeficiency syndrome. However, this is a veterinary indication with no supporting studies. The best-supported prediction is **simian immunodeficiency virus (SIV) infection**, with **0 clinical trials** and **3 preclinical animal publications**. This is a non-human disease, so the evidence is indirect and offers little direct clinical repurposing value.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infection, AIDS |
| Predicted New Indication | Feline acquired immunodeficiency syndrome (rank 1, no supporting studies). Simian immunodeficiency virus infection (rank 2, preclinical studies only) is discussed in detail below. |
| TxGNN Prediction Score | 99.90% (both rank 1 and rank 2) |
| Evidence Level | L5 for the rank 1 prediction (model prediction only). L4 for the rank 2 prediction (preclinical studies). |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, lopinavir is an HIV-1 protease inhibitor. Its efficacy in HIV infection and AIDS is established, and mechanistically it may be applicable to related lentiviral infections.

Feline immunodeficiency virus (FIV) and simian immunodeficiency virus (SIV) are lentiviruses related to HIV. A protease-targeting mechanism is therefore plausible. However, viral proteases differ in substrate specificity and inhibitor sensitivity, so cross-activity cannot be assumed. This is especially true for FIV, for which no studies were found.

The three SIV-related publications are macaque studies. They show that antiretroviral combinations can be tested in primate lentivirus models. One of them built a chimeric virus (SHIV) carrying the HIV-1 protease gene so that protease inhibitors could be tested in vivo. These studies support mechanistic plausibility and model utility, not clinical benefit in humans. SIV and FIV are not human diseases.

The third-ranked prediction, a rare neurodevelopmental disorder with ataxic gait, absent speech and decreased cortical white matter, has no identified mechanistic link to protease inhibition. Its high score likely reflects knowledge-graph associations. Lopinavir's limited CNS penetration is a further concern.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For simian immunodeficiency virus infection (no literature was found for the other two predictions):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Preclinical animal study (macaque) | Journal of Virology | Four cynomolgus macaques infected with SIVmac251 received a 7-day course of quadruple antiretroviral therapy. The study used the treatment to examine viral decay dynamics. |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Preclinical model construction (SHIV, rhesus macaque) | Microbes and Infection | Built a SHIV carrying the HIV-1 protease gene. Its growth was blocked by a protease inhibitor in cell culture. Two infected macaques developed weak but long-lasting infection, so the model may be useful for testing protease inhibitors. |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Preclinical animal study (monkey) | Journal of Virological Methods | Two SHIV 89.6P-infected rhesus macaques received oral AZT, 3TC and lopinavir/ritonavir for 28 days. The study assessed the effect on the peripheral blood CD8 subset. |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0294 | Lopinavir | Not specified | Not specified (status: cancelled) |

## Safety Considerations

Please refer to the package insert for safety information.

The following items come from drug-disease contraindication links in the TxGNN knowledge graph. They are not label text and should be confirmed against the official package insert:
- **Cardiac and conduction conditions**: long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, heart conduction disease, atrioventricular block, myocardial ischemia, coronary artery disease, cardiomyopathy
- **Liver and biliary conditions**: liver disease, cirrhosis, gallbladder disease, hyperbilirubinemia, Gilbert syndrome, chronic hepatitis B and C infection
- **Metabolic conditions**: hyperglycemia, diabetes mellitus, diabetic ketoacidosis, hypertriglyceridemia, familial combined hyperlipidemia, potassium deficiency
- **Other**: pancreatitis, hemophilia

**Drug Interactions** (65 interactions recorded; selected examples):
- **Major**: dolasetron, papaverine
- **Moderate**: ondansetron, palonosetron, levofloxacin, metformin, dapagliflozin, acarbose, famotidine, and several laxatives (bisacodyl, castor oil, lactulose, lactitol, glycerin, magnesium citrate, magnesium hydroxide, mineral oil, phenolphthalein)
- **Minor**: cimetidine, clotrimazole

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top predictions are for animal lentivirus infections (feline and simian) and have no direct human clinical repurposing value. The evidence is limited to a model prediction (L5) and three preclinical macaque studies (L4). The only Philippines registration is cancelled.

**To proceed, the following is needed:**
- Confirmation that a human indication of interest exists. The current top predictions are non-human diseases.
- Mechanism of action data for lopinavir.
- The Philippines package insert warnings and contraindications.
- Clarification of the status of registration PNF-0294 and whether any lopinavir product is currently marketed in the Philippines.
- For the neurodevelopmental disorder prediction, target or pathway validation and an assessment of CNS penetration before any further consideration.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

