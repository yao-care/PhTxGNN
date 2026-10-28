---
layout: default
title: Lopinavir
parent: Model Prediction Only (L5)
nav_order: 212
evidence_level: L5
indication_count: 3
monitor_inn: "Lopinavir"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-23
description: "Lopinavir: predicted new indication Simian immunodeficiency virus infection (evidence level L5). Approved use: HIV infectious disease and AIDS"
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

Lopinavir is an HIV-1 protease inhibitor; its original uses are HIV infectious disease and AIDS.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus infection**, but this is essentially an animal-model counterpart of the original HIV use.
Currently there are **0 clinical trials** and **3 publications** (all non-human primate studies), so the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease and AIDS (relation recorded in the knowledge graph; no approved indication text is available in the local licence record) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Lopinavir is generally known as an HIV-1 protease inhibitor. SIV is a closely related lentivirus whose protease is structurally similar to that of HIV-1, so a mechanistic link is plausible.

The relationship between the original and new indication is close, since both are lentiviral infections. However, SIV infection is an animal-model disease in macaques, not a new human indication. It therefore offers little in terms of genuine human repurposing value.

The three publications are all preclinical primate studies, and none of them tests lopinavir alone against SIV infection in a controlled way. They involved antiretroviral combinations or a chimeric SHIV virus. Because no cited study directly addresses this disease with lopinavir as a clearly evaluated agent, the evidence level is held at L5.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Preclinical animal study (non-human primate) | Journal of virology | Rapid viral decay in SIV-infected macaques given quadruple antiretroviral therapy over 7 days |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Preclinical animal study (chimeric SHIV in rhesus macaques) | Microbes and infection | Built a novel SHIV carrying an HIV-1 protease gene, proposed as a tool for testing protease inhibitors in vivo |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Preclinical animal study (non-human primate, HAART) | Journal of virological methods | Oral AZT, 3TC and lopinavir/ritonavir in two SHIV-infected macaques; looked at effects on the CD8 subset |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0294 | Lopinavir | Not specified | Not specified |

## Safety Considerations

- **Contraindication-type relations recorded in the knowledge graph** (not label text): long QT syndrome, familial long QT syndrome, torsades de pointes, sudden cardiac arrest, heart conduction disease, atrioventricular block, pancreatitis, liver disease, cirrhosis of liver, chronic hepatitis B and C virus infection, hyperbilirubinemia, Gilbert syndrome, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, hypertriglyceridemia, familial combined hyperlipidemia, potassium deficiency disease, gallbladder disease, coronary artery disease, myocardial ischemia, cardiomyopathy and hemophilia.
- **Drug Interactions**: 65 interactions were found in total. Examples of major-level interactions are **dolasetron** and **papaverine**. Moderate-level examples include ondansetron, palonosetron, levofloxacin, metformin, dapagliflozin, acarbose, famotidine, and several laxatives (bisacodyl, lactulose, lactitol, castor oil, magnesium citrate, magnesium hydroxide, mineral oil, glycerin, phenolphthalein). Minor-level examples include cimetidine and clotrimazole.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by non-human primate studies of an animal model of HIV. There are no human clinical trials, and SIV infection is not a human disease, so it does not offer a real new human indication. The prediction score is high, but the evidence level is L5. The package insert data are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Philippines FDA, to enable safety screening
- Mechanism of action data for lopinavir
- Approved indication text and dosage form for licence PNF-0294
- A clear rationale for why an SIV model indication would be relevant to human repurposing; otherwise consider other predicted indications with human disease relevance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

