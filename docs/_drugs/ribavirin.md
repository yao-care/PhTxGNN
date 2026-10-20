---
layout: default
title: Ribavirin
parent: Model Prediction Only (L5)
nav_order: 292
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ribavirin: predicted new indication Chronic hepatitis B virus infection (evidence level L5). Approved use: Chronic hepatitis C virus infection"
monitor_inn: "Ribavirin"
predicted_indications: ["chronic hepatitis B virus infection", "primitive portal vein thrombosis", "hepatoportal sclerosis", "hepatopulmonary syndrome", "early-onset familial noncirrhotic portal hypertension", "idiopathic copper-associated cirrhosis", "hepatic porphyria", "IgG4-related pachymeningitis", "IgG4-related mediastinitis", "IgG4-related mesenteritis"]
---

# Ribavirin
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

# Ribavirin: From Chronic Hepatitis C to Chronic Hepatitis B Virus Infection

## One-Sentence Summary

Ribavirin is an antiviral originally used for chronic hepatitis C virus infection and respiratory syncytial virus infection.
The TxGNN model predicts it may be effective for **chronic hepatitis B virus infection**,
with **15 clinical trials** and **20 publications** compiled, but only one directly on-indication Phase 3 trial (peginterferon plus ribavirin) has been identified and its results are not available.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus infection; respiratory syncytial virus infection (the Philippines licence record carries no approved indication text) |
| Predicted New Indication | Chronic hepatitis B virus infection |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L1 per the automated rule (≥2 completed Phase 3 trials), but see the caveat below: the directly relevant evidence is weaker than this label implies |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

**Caveat on the evidence level:** Several of the completed Phase 3 trials in the list are HCV studies in which ribavirin is only background therapy. Only NCT00114361 (and, partly, NCT00275938) addresses chronic hepatitis B directly, so the effective evidence for this indication is closer to L2 or lower.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available from the source database. Based on known information, ribavirin is a broad-spectrum nucleoside analogue that inhibits IMPDH (inosine monophosphate dehydrogenase) and has immunomodulatory activity. It is established in hepatitis C and RSV, and mechanistically it may be applicable to other viral liver infections.

In hepatitis B, ribavirin has been studied almost exclusively as an add-on to peginterferon. Any benefit is thought to come from immune modulation rather than direct inhibition of HBV polymerase. Ribavirin has no established direct anti-HBV activity, and current HBV standards of care (nucleos(t)ide analogues and peginterferon) do not include it.

The very high TxGNN score probably reflects network proximity between HBV and HCV (shared liver-disease and antiviral neighbours) rather than independent HBV-specific evidence. It should be read as a hypothesis-generating signal, not as confirmation.

## Clinical Trial Evidence

The table lists the trials most relevant to hepatitis B first. Many other registered trials are HCV studies and offer only indirect evidence.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00114361](https://clinicaltrials.gov/study/NCT00114361) | Phase 3 | Completed | 138 | PARC study: peginterferon alfa-2a plus ribavirin vs peginterferon alone in HBeAg-negative chronic HBV. The most directly relevant trial; results not available in the compiled data |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Phase 2/3 | Completed | 120 | Pilot of interferon alpha-2b plus ribavirin in chronic hepatitis B |
| [NCT03759782](https://clinicaltrials.gov/study/NCT03759782) | Phase 3 | Unknown | 24 | Pilot of ribavirin added to nucleos(t)ide analogue therapy in HBV, exploring immune modulation |
| [NCT00154869](https://clinicaltrials.gov/study/NCT00154869) | Phase 3 | Unknown | 320 | Peginterferon alfa-2a plus ribavirin in HCV/HBV co-infection vs HCV mono-infection |
| [NCT00117533](https://clinicaltrials.gov/study/NCT00117533) | Phase 4 | Unknown | 20 | Pilot of peginterferon alfa-2b plus ribavirin in dual HBV and hepatitis D infection |
| [NCT02219477](https://clinicaltrials.gov/study/NCT02219477) | Phase 3 | Completed | 36 | Ombitasvir/paritaprevir/ritonavir ± dasabuvir plus ribavirin in HCV with decompensated cirrhosis (indirect) |
| [NCT01447420](https://clinicaltrials.gov/study/NCT01447420) | Phase 4 | Completed | 129 | Peginterferon plus ribavirin and IL-28B expression in genotype 1 HCV (indirect) |
| [NCT01195181](https://clinicaltrials.gov/study/NCT01195181) | Phase 4 | Completed | 506 | HCV surveillance and antiviral-use program; does not test ribavirin in HBV (indirect) |
| [NCT01425970](https://clinicaltrials.gov/study/NCT01425970) | Phase 2 | Terminated | 210 | INX-08189 with peginterferon and ribavirin in HCV genotype 2/3; terminated early (indirect) |
| [NCT01795911](https://clinicaltrials.gov/study/NCT01795911) | Phase 2 | Completed | 165 | Peginterferon lambda with ribavirin and direct-acting antivirals in HCV; ribavirin is background therapy (indirect) |

Five further trials (all HCV-focused or without a relevance assessment) are not listed in order to keep the table to the 10 most relevant.

## Literature Evidence

The compiled literature consists mainly of narrative reviews on HBV/HCV co-infection and no randomised trials were found.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | HCV/HBV co-infection; peginterferon plus ribavirin was previously recommended for co-infected patients with positive HCV RNA |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World J Gastroenterol | Treatment and outcomes of dual HCV/HBV infection; higher risk of liver disease progression than mono-infection |
| [16838649](https://pubmed.ncbi.nlm.nih.gov/16838649/) | 2006 | Review | Nihon Rinsho | HCV-HBV infection; peginterferon alfa-2b plus ribavirin is the most effective initial HCV regimen |
| [25048716](https://pubmed.ncbi.nlm.nih.gov/25048716/) | 2015 | Review | Hepatology | Immunological aspects of antiviral therapy in chronic HBV and HCV |
| [26284971](https://pubmed.ncbi.nlm.nih.gov/26284971/) | 2015 | Review | Curr Opin Virol | IL28B genotype effects on HBV and HCV treatment response, including peginterferon plus ribavirin in HCV |
| [25232239](https://pubmed.ncbi.nlm.nih.gov/25232239/) | 2014 | Review | World J Gastroenterol | IL28B polymorphism and HBV infection outcomes |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | Review | Expert Rev Anti Infect Ther | Treatment options for chronic hepatitis B and C in children |
| [11160766](https://pubmed.ncbi.nlm.nih.gov/11160766/) | 2001 | Review (not formally classified) | Annu Rev Med | Treatment strategies for chronic hepatitis B and C (interferon, lamivudine) |
| [11929032](https://pubmed.ncbi.nlm.nih.gov/11929032/) | 2002 | Review | Indian J Pediatr | Management of chronic HBV and HCV infections |
| [24379612](https://pubmed.ncbi.nlm.nih.gov/24379612/) | 2013 | Review | World J Gastroenterol | Prevention of hepatocellular carcinoma in chronic HBV and HCV infection |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0419 | Ribavirin | Not recorded | Not recorded (status: cancelled) |

## Safety Considerations

No package insert warnings or contraindications were available in the data compiled for this report, so please refer to the package insert for safety information.

**Disease-level contraindication signals (knowledge graph, not label text):** The knowledge graph links ribavirin to contraindications in the following groups. These should be verified against the official label.
- **Blood disorders:** sickle cell anaemia, haemolytic anaemia, other anaemias, haemoglobinopathy, pancytopenia, inherited aplastic anaemia
- **Cardiovascular disease:** myocardial infarction, coronary artery disease, myocardial ischaemia, atherosclerosis
- **Lung disease:** COPD, asthma, interstitial lung disease, sarcoidosis
- **Liver, kidney and other conditions:** cirrhosis of the liver, impaired renal function, autoimmune hepatitis, pancreatitis, periodontitis

**Drug interactions:** The interaction screen returned 100 potential interacting drugs, but none has a severity grading (all "Unknown"). Examples include pantoprazole, omeprazole, metformin, glimepiride, morphine, prednisone and amphotericin B. These need clinical review before any use.

**Observation from the literature:** Several case reports describe porphyria cutanea tarda emerging during peginterferon/ribavirin therapy, which suggests ribavirin may be a trigger rather than a treatment for that condition.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Ribavirin has no established direct anti-HBV activity and is not part of current HBV standards of care. The only on-indication Phase 3 trial (NCT00114361) has no available results, and the very high TxGNN score likely reflects HCV/HBV network proximity.
- Ribavirin's only Philippines registration is cancelled, and no label-based safety data were available.

**To proceed, the following is needed:**
- Published results and control-arm details of NCT00114361, plus the outcomes of NCT00275938 and NCT03759782
- Comparison against current HBV standard of care (nucleos(t)ide analogues, peginterferon)
- Detailed mechanism of action data and evidence of an HBV-specific benefit
- Package insert warnings and contraindications, with severity grading of the drug interaction list
- Clarification of the regulatory status in the Philippines, since the only registration is cancelled

**Other predicted indications:** The other nine predicted indications (including primitive portal vein thrombosis, hepatoportal sclerosis, hepatopulmonary syndrome, hepatic porphyria and several IgG4-related diseases) have no clinical trials and no supporting literature of therapeutic benefit. Their recommendation is **Hold**.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

