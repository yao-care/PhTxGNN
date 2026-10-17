---
layout: default
title: Zolpidem
parent: Model Prediction Only (L5)
nav_order: 362
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Zolpidem: predicted new indication Sleep disorder, initiating and maintaining sleep (evidence level L5). Approved use: Insomnia"
monitor_inn: "Zolpidem"
predicted_indications: ["sleep disorder, initiating and maintaining sleep", "benign paroxysmal torticollis of infancy", "agoraphobia"]
---

# Zolpidem
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

# Zolpidem: From Insomnia to Sleep Disorder (Initiating and Maintaining Sleep)

## One-Sentence Summary

Zolpidem is a sedative-hypnotic originally used to treat insomnia.
The TxGNN model predicts it may be effective for **sleep disorder, initiating and maintaining sleep**, which is essentially the same condition as its original use, so this is not a true repurposing.
There are **no registered clinical trials** in the compiled data, but **19 publications** (including network meta-analyses, guidelines and one Phase 3 RCT using zolpidem as a comparator) discuss this use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Insomnia (approved indication text is not available in the Philippines registration record) |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L1 (see note below) |
| Philippines Market Status | ✗ Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Proceed with Guardrails (see note below) |

**Note on the evidence level:** The L1 rating comes from the compiled scoring. It rests on a Phase 3 RCT in which zolpidem was only the active comparator, plus network meta-analyses and guidelines, not on completed Phase 3 trials registered for this prediction. Treat it as a high-level but indirect rating.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, zolpidem is a positive allosteric modulator of the GABA-A receptor with preferential affinity for the alpha-1 subunit. This produces sedative-hypnotic effects that shorten sleep latency.

Difficulty initiating and maintaining sleep is the core feature of insomnia, the drug's original indication. The very high TxGNN score reflects this overlap rather than a new therapeutic discovery. Reviews in the literature list zolpidem alongside zaleplon, zopiclone and eszopiclone as GABA-A modulators with an established evidence base in insomnia.

Other predicted indications were also reviewed. Both have only model-based support (L5) and are rated **Hold**:
- **Benign paroxysmal torticollis of infancy** (score 99.26%): no clear mechanistic link, and zolpidem is not appropriate for infants.
- **Agoraphobia** (score 99.25%): only a weak, indirect GABAergic link. Zolpidem has minimal anxiolytic activity, guidelines favour SSRIs/SNRIs and cognitive behavioural therapy, and dependence risk is a concern in anxious populations.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | RCT (Phase 3) | JAMA Netw Open | Lemborexant compared with placebo and zolpidem extended-release in older adults with insomnia; zolpidem served as the active comparator |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Network meta-analysis | Lancet | Comparative effects of drug treatments for acute and long-term management of adult insomnia |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | Network meta-analysis | J Manag Care Spec Pharm | Efficacy and safety of lemborexant compared with other insomnia treatments |
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Guideline | J Clin Sleep Med | American Academy of Sleep Medicine recommendations for drug treatment of chronic insomnia, reviewed drug by drug |
| [39923608](https://pubmed.ncbi.nlm.nih.gov/39923608/) | 2025 | Guideline (expert consensus) | Sleep Med | European guidance on switching or deprescribing hypnotics for chronic insomnia; lists zolpidem among recommended options |
| [41187937](https://pubmed.ncbi.nlm.nih.gov/41187937/) | 2025 | Guideline (safety) | Arq Neuropsiquiatr | Brazilian guideline on Z-drug abuse and dependence; use recommended for no longer than four weeks |
| [29487083](https://pubmed.ncbi.nlm.nih.gov/29487083/) | 2018 | Review | Pharmacol Rev | Z-drugs are approved for insomnia with a strong evidence base, but cause cognitive impairment, tolerance, rebound insomnia, falls and dependence |
| [22424586](https://pubmed.ncbi.nlm.nih.gov/22424586/) | 2012 | Review | Expert Opin Pharmacother | Zolpidem is a benzodiazepine receptor agonist and the most widely prescribed hypnotic in the US |
| [16696581](https://pubmed.ncbi.nlm.nih.gov/16696581/) | 2006 | Review | CNS Drugs | Zolpidem extended-release is indicated for difficulty with sleep onset and/or maintenance; two 3-week randomised trials assessed efficacy |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review | Clin Ther | Safety and efficacy of sleep medicines in older adults |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0529 | Zolpidem | Not specified | Not specified (status: cancelled) |

This is the only registration on record, and it is cancelled. No currently valid product is registered in the Philippines.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (disease associations from the TxGNN knowledge graph, not label text): liver disease, gallbladder disease, obstructive sleep apnoea and other sleep apnoea syndromes, congenital central hypoventilation syndrome, amnestic disorders and retrograde amnesia, substance-related disorders and substance abuse/dependence, anxiety disorder, neurotic disorder, dysthymic disorder, and attention deficit hyperactivity disorder.
- **Drug Interactions**: 100 interactions were found. The major-severity ones shown are with **morphine** and **liposomal morphine** (additive central nervous system and respiratory depression is the expected concern). Moderate-severity interactions include bupropion, aprepitant, dexamethasone, cimetidine, clarithromycin, metoclopramide, miconazole, clotrimazole, dronabinol, nabilone, opium and sibutramine.
- **Literature-based concerns**: cognitive impairment, tolerance, rebound insomnia on discontinuation, falls and injuries in older adults, car accidents, abuse and dependence.

Package insert warnings and contraindications for the Philippines were not available, so please refer to the package insert for label safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for sleep disorder, initiating and maintaining sleep only; **Hold** for the other two predicted indications)

**Rationale:**
- The predicted indication is effectively zolpidem's established use in insomnia, supported by guidelines and network meta-analyses. However, the only Philippines registration is cancelled, and the package insert safety data are missing, so it cannot be treated as ready for use.

**To proceed, the following is needed:**
- Verify the regulatory status in the Philippines and confirm whether a valid registration exists or a new one is needed
- Obtain and review the Philippines package insert (warnings, contraindications, dosage forms, approved indications)
- Obtain DrugBank mechanism of action data to replace the general-knowledge description above
- Set a safety plan covering short-term use limits, dependence and abuse risk, falls in older adults, and combinations with opioids and other central nervous system depressants
- Do not pursue benign paroxysmal torticollis of infancy or agoraphobia without new mechanistic and clinical evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

