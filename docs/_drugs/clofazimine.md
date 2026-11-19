---
layout: default
title: Clofazimine
parent: Model Prediction Only (L5)
nav_order: 79
evidence_level: L5
indication_count: 3
monitor_inn: "Clofazimine"
predicted_indications: ["pneumocystosis", "malaria", "gastrin secretion abnormality"]
last_modified_at: 2026-11-12
description: "Clofazimine: predicted new indication pneumocystosis (evidence level L5). In the Philippines: 1 PNF entry"
---

# Clofazimine
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

## Clofazimine: riminophenazine antimycobacterial agent → pneumocystosis
{: .text-alpha }

## One-Sentence Summary

Clofazimine is a riminophenazine antimycobacterial drug. The TxGNN model predicts it may be effective for **pneumocystosis**, but no clinical trials are registered and none of the 3 publications retrieved studies clofazimine for this disease, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | pneumocystosis |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for clofazimine: "LAMPRENE is an anti-mycobacterial drug. […] Clofazimine exerts a slow bactericidal effect on Mycobacterium leprae (Hansen’s bacillus). Clofazimine inhibits mycobacterial growth and binds preferentially to mycobacterial DNA. Clofazimine also exerts anti-inflammatory properties in treating erythema nodosum leprosum reactions." ([DailyMed: Lamprene (clofazimine) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2e07448f-f888-4747-80ab-570c1b621250), label version 2026-08-17; accessed 2026-11-19.) Clofazimine is known as a riminophenazine antimycobacterial with immunomodulatory and membrane-disrupting properties.

No credible mechanistic link to pneumocystosis is established. *Pneumocystis* is a fungus, and nothing in the compiled data shows clofazimine activity against it. The very high TxGNN score (0.9990) reflects a model-based prediction only and should not be read as evidence of efficacy.

The literature that mentions both topics is incidental. One trial used clofazimine to prevent *Mycobacterium avium* complex infection in AIDS patients, some of whom had previously had *Pneumocystis* pneumonia. One case report describes an AIDS patient with *M. kansasii* lung disease treated with a multidrug regimen that included clofazimine, with trimethoprim-sulfamethoxazole added after *Pneumocystis* pneumonia developed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8501340](https://pubmed.ncbi.nlm.nih.gov/8501340/) | 1993 | Randomized open-label trial | J Infect Dis | Clofazimine as prophylaxis for disseminated *M. avium* complex infection in 110 HIV patients, some with prior *Pneumocystis* pneumonia; does not study pneumocystosis itself |
| [2714863](https://pubmed.ncbi.nlm.nih.gov/2714863/) | 1989 | Case report | Infection | AIDS patient with *M. kansasii* lung disease complicated by *Pneumocystis* pneumonia; recovered on a multidrug regimen including clofazimine, with trimethoprim-sulfamethoxazole added for the pneumonia |
| [11363899](https://pubmed.ncbi.nlm.nih.gov/11363899/) | 1996 | Review | PI Perspective | General update on opportunistic infections; no abstract available |

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Clofazimine | Oral |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 100 interacting drugs were identified. Major-level interactions include cisapride and dolasetron. Moderate-level interactions include famotidine, loperamide, bisacodyl, clarithromycin, levofloxacin, ondansetron, granisetron and palonosetron, as well as several laxatives (picosulfuric acid, polyethylene glycol, castor oil, lactulose, lactitol, magnesium citrate, magnesium hydroxide, glycerin, mineral oil). Metronidazole is listed as a minor interaction.
- Conditions flagged as cautions in the data compiled for this report include liver disease, gallbladder disease, diarrhoeal and other intestinal or digestive disease, active peptic ulcer disease, and splenic disease. These are not taken from label text and need confirmation against the package insert.

Please refer to the package insert for key warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials, no study of clofazimine in pneumocystosis, and no supported mechanism against *Pneumocystis*. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data for clofazimine
- Preclinical evidence of activity against *Pneumocystis*
- Package insert warnings and contraindications from DOH-FDA Philippines
- A safety review covering the flagged liver, gastrointestinal and splenic conditions and the major drug interactions

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for clofazimine are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Lamprene (clofazimine) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2e07448f-f888-4747-80ab-570c1b621250) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

