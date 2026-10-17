---
layout: default
title: Dipyridamole
parent: Moderate Evidence (L3-L4)
nav_order: 112
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Dipyridamole: predicted new indication Prinzmetal angina (evidence level L4). Approved use: Atrial fibrillation"
monitor_inn: "Dipyridamole"
predicted_indications: ["stroke disorder", "thrombotic disease", "sick sinus syndrome 2, autosomal dominant", "transient ischemic attack (disease)", "sarcoglycanopathy", "Wildervanck syndrome", "macrocephaly, dysmorphic facies, and psychomotor retardation", "lateral sinus thrombosis", "cavernous sinus thrombosis"]
---

# Dipyridamole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Dipyridamole: From Atrial Fibrillation to Prinzmetal Angina

## One-Sentence Summary

Dipyridamole is a drug that, according to the knowledge graph, was originally associated with atrial fibrillation.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but this is the top-ranked prediction with the weakest support: **no clinical trials** and only **10 publications**, mostly diagnostic or case-level, are available.
Note that the better-supported predictions for this drug are **stroke disorder** and **transient ischemic attack** (see the end of this report).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation (from the knowledge graph; no approved indication text is available for the Philippines registration) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for dipyridamole was not available in the structured drug record. From the published literature, dipyridamole inhibits adenosine reuptake and phosphodiesterase, which raises extracellular adenosine and cyclic nucleotide levels and produces coronary vasodilation.

Prinzmetal (variant) angina is caused by coronary vasospasm. In principle a vasodilator might seem relevant. However, the retrieved literature mostly describes dipyridamole as a **diagnostic stress agent** rather than a treatment. One report (PMID 3421166) describes coronary vasospasm triggered when dipyridamole stress was terminated with aminophylline. Dipyridamole could also theoretically worsen ischemia through coronary steal. There is therefore no clear therapeutic rationale, and there is a possible safety concern.

## Clinical Trial Evidence

Currently no related clinical trials registered for Prinzmetal angina.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [633593](https://pubmed.ncbi.nlm.nih.gov/633593/) | 1978 | Observational | Jpn Circ J | 26 patients with rest angina (13 with variant angina) were given several drugs including dipyridamole 50 mg to examine effects on attacks; propranolol tended to aggravate attacks |
| [3190956](https://pubmed.ncbi.nlm.nih.gov/3190956/) | 1988 | Observational | Br Heart J | Reproducibility of exercise testing in patients with exercise-induced ST elevation and differing responses to the dipyridamole test |
| [3421166](https://pubmed.ncbi.nlm.nih.gov/3421166/) | 1988 | Observational | Am J Cardiol | Aminophylline termination of dipyridamole stress triggered coronary vasospasm in variant angina |
| [16630456](https://pubmed.ncbi.nlm.nih.gov/16630456/) | 2006 | Observational | Zhonghua Xin Xue Guan Bing Za Zhi | Clinical features of atypical coronary artery spasm compared with typical spasm |
| [14060538](https://pubmed.ncbi.nlm.nih.gov/14060538/) | 1963 | Case report | Naika | Case of variant form of angina pectoris (no abstract available) |
| [2022043](https://pubmed.ncbi.nlm.nih.gov/2022043/) | 1991 | Review | Circulation | Pathophysiological basis of noninvasive functional evaluation of coronary stenosis, including dipyridamole testing |
| [6779029](https://pubmed.ncbi.nlm.nih.gov/6779029/) | 1981 | Diagnostic study | Jpn Circ J | Dipyridamole-loading thallium-201 imaging for detecting coronary artery disease (diagnostic accuracy 66%) |

None of these studies shows a therapeutic benefit of dipyridamole in Prinzmetal angina.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0150 | Dipyridamole | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: kidney disease, liver disease, gallbladder disease, thrombocytopenia, peptic ulcer disease, hypotensive disorder, gout, acute coronary syndrome, myocardial infarction, hemophilia, anemia, and others.
- **Drug Interactions**: 100 interactions were found in the DDI database. Moderate-level interactions include dexfenfluramine, sibutramine and fenfluramine. Others, including aspirin, cimetidine, metformin, omeprazole, morphine and simvastatin, are listed with an unknown severity level.
- **Specific concern for this indication**: possible vasospasm and coronary steal (see above).

Please refer to the package insert for label warnings and contraindications, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For Prinzmetal angina, no clinical trials exist, the literature is largely diagnostic or anecdotal, and there is a possible safety concern. The only Philippines registration is cancelled.

**To proceed, the following is needed:**
- Mechanism of action data
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Controlled clinical evidence of benefit (and safety) in vasospastic angina

### Better-Supported Alternatives for This Drug

| Predicted Indication | Score | Evidence Level | Decision | Basis |
|------|------|------|------|------|
| Stroke disorder | 99.95% | L1 | Proceed with Guardrails | ESPRIT (NCT00161070, n=4,500) and meta-analyses/Cochrane reviews support aspirin plus dipyridamole over aspirin alone |
| Transient ischemic attack | 99.87% | L1 | Proceed with Guardrails | Same evidence base as for stroke |

Guardrails for these two indications: use dipyridamole in combination with aspirin rather than alone, monitor for headache, GI intolerance and bleeding, use caution in severe coronary disease, and consider alternatives such as clopidogrel or cilostazol per current guidelines. Because the only Philippines registration is cancelled, regulatory status would also need to be addressed.

Other predictions, including thrombotic disease (L4, research question), sick sinus syndrome, sarcoglycanopathy, Wildervanck syndrome, macrocephaly syndrome and venous sinus thromboses (L5), rest on model scores alone or indirect literature and are not supported.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

