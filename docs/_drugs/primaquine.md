---
layout: default
title: Primaquine
parent: Model Prediction Only (L5)
nav_order: 283
evidence_level: L5
indication_count: 8
---

# Primaquine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Primaquine: From Plasmodium vivax Malaria to Myiasis

## One-Sentence Summary

Primaquine is an 8-aminoquinoline antimalarial, originally used for radical cure of *Plasmodium vivax* malaria.
The TxGNN model predicts it may be effective for **myiasis** (fly-larva infestation), but **no clinical trials and no publications** support this prediction.
The data compiled for this report do show stronger evidence for two other predicted uses, malaria transmission-blocking and *Pneumocystis* pneumonia (see "Other Predicted Indications With Evidence").

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Plasmodium vivax malaria (taken from knowledge-graph indication data, because the local registration lists no indication text) |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Primaquine is known to act on the liver stages (hypnozoites) and gametocytes of malaria parasites. Its efficacy in *P. vivax* malaria is well established.

For myiasis, however, no mechanistic rationale is evident. Myiasis is a tissue infestation by fly larvae, an ectoparasitic condition. Primaquine targets *Plasmodium*, a protozoan blood and liver parasite. The high score appears to reflect closeness to other antiparasitic drugs in the knowledge graph rather than a biological link.

Three related predictions (wound myiasis, creeping myiasis and furuncular myiasis) have nearly identical scores of about 99.73%. They appear to be inherited from the parent term "myiasis" rather than independently supported. Furuncular myiasis is usually managed by larval removal or occlusion, and sometimes ivermectin. Nothing suggests a role for primaquine.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for myiasis.

---

## Literature Evidence

Currently no related literature available for myiasis.

---

## Other Predicted Indications With Evidence

These are not the lead prediction, but they are the only places where the compiled data show meaningful support.

**Malaria (score 99.38%, Evidence Level L1, Proceed with Guardrails).** This is essentially the approved indication family, not a novel repurposing. The transmission-blocking use in falciparum malaria goes beyond the original indication.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01074905](https://clinicaltrials.gov/study/NCT01074905) | Phase 3 | Completed | 655 | Chloroquine/primaquine vs chloroquine vs artesunate for vivax malaria, Thai-Burmese border |
| [NCT00158587](https://clinicaltrials.gov/study/NCT00158587) | Phase 3 | Completed | 150 | Placebo-controlled trial of an 8-week primaquine regimen for vivax malaria |
| [NCT01814683](https://clinicaltrials.gov/study/NCT01814683) | N/A | Completed | 2388 | Multicentre comparison of short vs long course primaquine for radical cure |
| [NCT01906788](https://clinicaltrials.gov/study/NCT01906788) | Phase 4 | Unknown | 250 | Optimal timing of primaquine after artemisinin combination therapy to block transmission |
| [NCT02364583](https://clinicaltrials.gov/study/NCT02364583) | Phase 4 | Unknown | 150 | Safety and pilot efficacy of short-course, high-dose primaquine in children in Papua New Guinea |
| [NCT02802813](https://clinicaltrials.gov/study/NCT02802813) | Phase 1/2 | Completed | 41 | 14-day primaquine for subclinical vivax infection in Laos |

Supporting reviews include [25363455](https://pubmed.ncbi.nlm.nih.gov/25363455/) (2014, Malaria Journal, primaquine risks and benefits), [22152065](https://pubmed.ncbi.nlm.nih.gov/22152065/) (2011, Malaria Journal, primaquine in vivax malaria) and [38123228](https://pubmed.ncbi.nlm.nih.gov/38123228/) (2023, BMJ Global Health, individual patient data meta-analysis in South Asia).

**Pneumocystosis (score 99.32%, Evidence Level L1, Research Question).** Primaquine with clindamycin is an established second-line regimen for mild-to-moderate *Pneumocystis jirovecii* pneumonia. It is mainly used when TMP-SMX cannot be given. Primaquine alone has no supporting evidence.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Phase 3 | Completed | 290 | Dapsone/trimethoprim and clindamycin/primaquine vs TMP-SMX in AIDS-related PCP |
| [NCT00000717](https://clinicaltrials.gov/study/NCT00000717) | N/A | Completed | 50 | Clindamycin plus primaquine for mild-to-moderate PCP in AIDS |
| [NCT07357103](https://clinicaltrials.gov/study/NCT07357103) | Phase 4 | Not yet recruiting | 416 | Ranking of second-line PCP therapies when TMP-SMX cannot be used |

Supporting literature includes [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) (2025, network meta-analysis of PCP regimens in people living with HIV) and [27550993](https://pubmed.ncbi.nlm.nih.gov/27550993/) (2016, ECIL guidelines for PCP in non-HIV haematology patients).

**Toxoplasmosis (score 99.64%, Evidence Level L4, Hold).** Only general protozoan reviews that mention primaquine incidentally were found. There is no toxoplasmosis-specific efficacy data.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0400 | Primaquine | Not stated | Not stated (status: cancelled) |

---

## Safety Considerations

- **Contraindication-related conditions (from knowledge-graph drug-disease links, not label text):** neutropenia, agranulocytosis, G6PD deficiency, hemolytic anemia, methemoglobinemia due to methemoglobin reductase deficiency, glycogen storage disease, cystinuria, galactosemia and pyruvate dehydrogenase E3 deficiency.
- **Hemolysis risk:** Trials and reviews consistently show primaquine can cause hemolysis in G6PD-deficient patients. G6PD testing is needed before any use. Primaquine-induced methemoglobinemia has also been reported.
- **Drug interactions:** 100 interactions were recorded, and the first 20 are summarised here.
  - **Major:** dolasetron.
  - **Moderate:** ondansetron, granisetron, palonosetron, clarithromycin, levofloxacin, famotidine, alosetron, loperamide and several laxatives or bowel-preparation agents.
  - **Minor:** metronidazole.

Please also refer to the package insert for label warnings, which were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The myiasis prediction is supported only by the model score, with no trials, no literature and no plausible mechanism. The high score looks like an ontology-propagation artefact. Primaquine's real evidence lies in malaria, essentially its existing indication, and in *Pneumocystis* pneumonia as a clindamycin combination.

**To proceed, the following is needed:**
- A mechanistic or in vitro/in vivo rationale for activity against fly larvae, which is currently absent.
- Package insert warnings and contraindications.
- Detailed mechanism of action data.
- A decision on whether to redirect the evaluation to the better-supported indications. These are malaria transmission-blocking and *Pneumocystis* pneumonia as a second-line combination, and both would need G6PD screening guardrails.
- Clarification of the regulatory position in the Philippines, since the only registration (PNF-0400) is cancelled.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

