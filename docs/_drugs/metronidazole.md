---
layout: default
title: Metronidazole
parent: Model Prediction Only (L5)
nav_order: 234
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Metronidazole: predicted new indication Pneumocystosis (evidence level L5). Approved use: Peritonitis, endocarditis, anaerobic bacterial infections, giardiasis…"
monitor_inn: "Metronidazole"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis", "ulcerative proctosigmoiditis", "nocardiosis", "postmenopausal atrophic vaginitis", "Cryptococcal meningitis", "papillary conjunctivitis", "myiasis", "cap polyposis", "ulceration of vulva"]
---

# Metronidazole
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

# Metronidazole: From Anaerobic and Protozoal Infections to Pneumocystosis

## One-Sentence Summary

Metronidazole is an antimicrobial originally used for anaerobic bacterial infections, giardiasis, bacterial vaginosis, and related conditions.
The TxGNN model predicts it may be effective for **pneumocystosis**,
but **no clinical trials** and only **10 publications** (reviews and case reports, none showing efficacy against Pneumocystis) are available, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peritonitis, endocarditis, anaerobic bacterial infections, giardiasis, bacterial vaginosis, rosacea, intracranial abscess and others (the Philippines registration record has no indication text) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Metronidazole is generally known as a nitroimidazole antimicrobial that works against anaerobic bacteria and protozoa after its nitro group is reduced inside the organism.

That mechanism does not carry over to pneumocystosis. *Pneumocystis* is a fungus and lacks this activation pathway, and the retrieved literature gives no credible mechanistic link. The very high TxGNN score is most likely an artifact of the knowledge graph, which groups metronidazole with antiprotozoal drugs. The retrieved papers are general antiparasitic reviews and HIV opportunistic infection reports in which metronidazole treated a co-existing infection such as amoebiasis, not Pneumocystis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clin Proc | Overview of antiparasitic agents; no evidence of metronidazole for Pneumocystis |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | Am Fam Physician | Metronidazole is a drug of choice for amoebic colitis and trichomoniasis; trimethoprim-sulfamethoxazole is listed for pneumocystis pneumonia |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clin Pharmacokinet | Pharmacokinetic rationale for antiprotozoal therapy |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clin Pharm | Treatment of infectious complications of AIDS |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Top Antivir Med | HIV-related opportunistic infections remain relevant; no metronidazole role shown |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review | Rev Infect Dis | Critique of antimicrobial prophylaxis trials |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case report | Am Rev Respir Dis | Pneumocystis and CMV pneumonia in a previously healthy adult who had earlier received metronidazole |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case report | Kansenshogaku Zasshi | Two AIDS patients; metronidazole treated amoebic dysentery, not Pneumocystis |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case report | J Formos Med Assoc | Colon perforation in an AIDS patient with CMV and amoebic colitis |
| [42178576](https://pubmed.ncbi.nlm.nih.gov/42178576/) | 2026 | Case report | J Med Case Rep | Streptococcus intermedius cerebellar abscess as first presentation of sarcoidosis |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0324 | Metronidazole | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Contraindications / disease associations from the knowledge graph** (not label text): liver failure, liver disease, epilepsy, kidney disease, hematologic disease, neutropenia, agranulocytosis, leukopenia, blood coagulation disease, peripheral neuropathy and other peripheral nervous system disease, brain disease, optic nerve disease, congestive heart failure, diabetes mellitus, diabetic ketoacidosis, gout, gallbladder disease, dermatitis, substance abuse/dependence, and others.
- **Drug Interactions** (100 interactions found; examples):
  - **Major**: Ethanol
  - **Moderate**: Paclitaxel, Adalimumab, Trastuzumab emtansine, Ethinylestradiol, Estradiol, Butalbital, Amobarbital, Amiodarone, Celecoxib, Loperamide
  - **Minor**: Abiraterone, Tramadol, Famotidine, Salbutamol, Alfuzosin, Amisulpride, Amitriptyline, Anagrelide, Propofol

Please also refer to the package insert for warnings, as label-based safety information was not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. There are no clinical trials, and the literature contains no evidence that metronidazole treats Pneumocystis. Mechanistically it is implausible, and the only Philippines registration has been cancelled.

**To proceed, the following is needed:**
- Mechanistic or in vitro evidence of metronidazole activity against *Pneumocystis*, which is currently lacking
- Detailed mechanism of action data (MOA)
- Philippines package insert warnings and contraindications
- Confirmation of the registration status and approved indications of the cancelled authorization

**Other predictions worth considering:**
Among the other predicted indications, those with limited case-level support (cap polyposis, ulcerative proctosigmoiditis, ulceration of vulva, myiasis as supportive wound care) are better framed as research questions than as repurposing candidates. They are supported only by case reports, reviews, or indirect rationale, with no controlled data.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

