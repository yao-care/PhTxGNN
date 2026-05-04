---
layout: default
title: Delamanid
parent: 僅模型預測 (L5)
nav_order: 99
evidence_level: L5
indication_count: 7
---

# Delamanid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Delamanid: From Multidrug-Resistant Tuberculosis to Tuberculosis, Bovine

## One-Sentence Summary

Delamanid is a bicyclic nitroimidazole antibiotic approved in multiple countries for the treatment of multidrug-resistant pulmonary tuberculosis (MDR-TB) in adults.
The TxGNN model predicts it may be effective for **Tuberculosis, Bovine** (caused by *Mycobacterium bovis*),
with **0 clinical trials** and **1 publication** currently supporting this specific direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multidrug-resistant pulmonary tuberculosis (MDR-TB) — not registered in the Philippines; based on international approval profile |
| Predicted New Indication | Tuberculosis, Bovine |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Delamanid (OPC-67683) is a bicyclic nitroimidazole that exerts its antibacterial effect by inhibiting mycobacterial cell wall synthesis — specifically by blocking the production of methoxy-mycolic acid and keto-mycolic acid, two essential lipid components of the *Mycobacterium* cell wall. This disruption is selectively lethal to mycobacteria and forms the basis of its approved use against *Mycobacterium tuberculosis* in MDR-TB.

*Mycobacterium bovis*, the causative agent of bovine tuberculosis and zoonotic TB in humans, is phylogenetically closely related to *M. tuberculosis* and shares the same cell wall architecture, including conserved mycolic acid biosynthetic pathways. Because Delamanid targets a pathway that is structurally and functionally conserved across *Mycobacterium* species, its activity against *M. bovis* is biologically plausible. The genus-level mechanistic overlap provides a reasonable theoretical basis for this TxGNN prediction.

One publication in the evidence base (PMID 39487429) used whole-genome sequencing to characterize drug resistance and genetic diversity in human *M. bovis* isolates from zoonotic TB — this highlights both the clinical importance of this pathogen and the need for novel therapeutic options, further lending contextual support to the prediction, even though the paper does not directly study Delamanid.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Tuberculosis, Bovine.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39487429](https://pubmed.ncbi.nlm.nih.gov/39487429/) | 2024 | Genomic Study | BMC Genomics | WGS analysis of *M. bovis* isolates from zoonotic human TB cases; characterized circulating genotypes, virulence determinants, and drug resistance profiles — underscoring the complexity of treatment and the need for effective anti-*M. bovis* agents |

---

## Philippines Market Information

Delamanid is not currently registered with the Philippine FDA. There are no product authorizations on file in the Philippines regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While Delamanid's mechanism is biologically consistent with potential activity against *M. bovis*, the current evidence base for this specific indication is limited to a single genomic background paper with no direct treatment data, and the drug has no regulatory presence in the Philippines.

**To proceed, the following is needed:**
- **Regulatory pathway**: Establish a pathway for Philippine FDA registration of Delamanid before any new indication can be pursued
- **Direct efficacy data**: In vitro minimum inhibitory concentration (MIC) studies and in vivo animal model data for Delamanid against *M. bovis* strains
- **Clinical evidence**: Identify or initiate clinical studies evaluating Delamanid in zoonotic or bovine-origin TB in humans
- **MOA confirmation**: Retrieve full mechanism of action data from DrugBank (DB11637) to formally confirm mycolic acid pathway activity across *Mycobacterium* species
- **Safety profile**: Download and parse the full package insert (TFDA/EMA) to extract warnings, contraindications, and drug interaction data
- **Broader TB context review**: The rank-3 predicted indication (Inactive Tuberculosis / latent TB) has 2 active Phase 2/3 clinical trials and 20 publications and may represent a stronger near-term repurposing candidate worth evaluating in a separate report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

