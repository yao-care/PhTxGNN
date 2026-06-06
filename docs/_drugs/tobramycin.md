---
layout: default
title: Tobramycin
parent: 僅模型預測 (L5)
nav_order: 334
evidence_level: L5
indication_count: 10
---

# Tobramycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Tobramycin: From Bacterial Infections to Exposure Keratitis

## One-Sentence Summary

Tobramycin is an aminoglycoside antibiotic with well-established bactericidal activity against Gram-negative organisms, historically used in the treatment of serious bacterial infections including pneumonia, septicemia, and urinary tract infections.
The TxGNN model predicts it may be effective for **Exposure Keratitis**, with **2 clinical trials** and **7 publications** retrieved in this evidence review — though both trials are only indirectly related to this specific indication.
The mechanistic basis is plausible (secondary bacterial infection prevention on a compromised corneal surface), but dedicated clinical evidence is currently absent.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Serious Gram-negative bacterial infections (pneumonia, septicemia, UTI; no Philippines registration found) |
| Predicted New Indication | Exposure Keratitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Tobramycin is an aminoglycoside antibiotic — its bactericidal efficacy against serious Gram-negative infections, particularly *Pseudomonas aeruginosa*, has been established for decades across multiple infection sites, and mechanistically may be applicable to ocular surface infections.

Exposure keratitis (lagophthalmos-related keratopathy) develops when incomplete eyelid closure causes chronic corneal desiccation and epithelial breakdown. This damaged surface is highly vulnerable to secondary bacterial colonisation, with *Pseudomonas aeruginosa* and *Staphylococcus aureus* being the most common pathogens encountered. Tobramycin ophthalmic preparations carry demonstrably low MICs against both organisms, making prophylactic or therapeutic use mechanistically logical. The case of bacterial keratitis in a vegetative-state patient with lagophthalmos (PMID 34987857) directly illustrates this clinical scenario.

A meaningful safety signal complicates this prediction: an in vitro study (PMID 2707046) showed that tobramycin — alongside other aminoglycosides — inhibits corneal epithelial cell proliferation in a concentration- and time-dependent manner. Applying a cytotoxic agent to an already-compromised corneal epithelium introduces genuine risk, and no clinical trial has yet directly evaluated this trade-off in the exposure keratitis population. Validation in a controlled setting is therefore a prerequisite before proceeding.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06200727](https://clinicaltrials.gov/study/NCT06200727) | NA | Unknown | 170 | Platelet-rich fibrin (PRF) membrane for ophthalmic diseases including corneal ulcer and glaucoma; tobramycin is not the investigational agent — relevance to tobramycin + exposure keratitis is indirect at best |
| [NCT05313828](https://clinicaltrials.gov/study/NCT05313828) | N/A | Unknown | 40 | Various treatment modalities for HSV dendritic keratitis; tobramycin, if included, would serve only as an adjunctive antibacterial agent rather than a primary study drug |

> **Note:** Neither trial directly evaluates tobramycin for exposure keratitis. Both are included as the closest available evidence; they do not constitute direct clinical support for this indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2707046](https://pubmed.ncbi.nlm.nih.gov/2707046/) | 1989 | In Vitro Study | Current Eye Research | Tobramycin and three other aminoglycosides tested on rabbit corneal epithelial cell cultures; concentration- and duration-dependent cytotoxicity observed — important safety signal for topical ophthalmic use |
| [17228760](https://pubmed.ncbi.nlm.nih.gov/17228760/) | 2006 | In Vitro / Pharmacodynamic Study | Nippon Ganka Gakkai Zasshi | MIC and post-antibiotic effect of antibiotic eyedrops against infectious keratitis isolates from Japanese national surveillance; tobramycin included among comparators |
| [34987857](https://pubmed.ncbi.nlm.nih.gov/34987857/) | 2021 | Case Report | Oxford Medical Case Reports | MDR *Shewanella algae* bacterial keratitis in a vegetative-state patient unable to close his eyes (lagophthalmos); demonstrates how exposure-type corneal compromise leads to secondary bacterial keratitis |
| [12861116](https://pubmed.ncbi.nlm.nih.gov/12861116/) | 2003 | Case Report | Eye & Contact Lens | Bilateral MRSA keratitis following photorefractive keratectomy; underscores the Gram-positive pathogen dimension of post-procedural/compromised corneal infections |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Case Report | Ophthalmology | First reported contact lens-related *Bacillus cereus* keratitis with confirmed genetic identity between corneal and lens case isolates |
| [33847093](https://pubmed.ncbi.nlm.nih.gov/33847093/) | 2021 | Retrospective Cohort | Polish Journal of Veterinary Sciences | Feline ocular toxoplasmosis (60 cases); limited direct relevance to human exposure keratitis but tobramycin cited within the treatment protocol |
| [14574976](https://pubmed.ncbi.nlm.nih.gov/14574976/) | 2003 | Case Report | Eye Science | Paracentral corneal dellen in Graves ophthalmopathy — an exposure-type corneal complication mechanistically similar to lagophthalmos-related exposure keratitis; tobramycin used as part of ocular surface management |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Specific concern identified from literature:** PMID 2707046 documents aminoglycoside-induced corneal epithelial cytotoxicity in vitro. In the context of exposure keratitis — where the epithelium is already compromised — prolonged topical tobramycin use may delay epithelial healing. This risk should be explicitly evaluated in any future clinical study design.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for tobramycin in exposure keratitis is currently limited to indirect case reports and an in vitro cytotoxicity study (L4); no dedicated prospective trial exists, and a biologically plausible harm signal (aminoglycoside epithelial toxicity) has not been clinically resolved. This combination — absent positive clinical data plus an unresolved safety question — does not yet support active development or repurposing pursuit.

**To proceed, the following is needed:**
- Retrieve full mechanism of action data from DrugBank (DG002, classified as High severity)
- Obtain Philippines FDA package insert for approved warnings and contraindications (DG001, Blocking severity) — currently prevents completion of the S1 safety screen
- Drug interaction profile (DDI query returned no results; independent verification recommended)
- Prospective clinical study specifically evaluating topical tobramycin in exposure keratitis patients with documented secondary bacterial infection risk
- Comparative safety data on short-term versus prolonged topical aminoglycoside use on damaged corneal epithelium
- Assessment of alternative topical antibiotics (e.g., fluoroquinolones) with superior corneal safety profiles as comparators

---

> **Broader context note:** While exposure keratitis ranks first in TxGNN predictions for this evidence pack, the strongest overall clinical evidence for tobramycin repurposing lies in **post-bacterial disorder (rank 5, L1)** — corresponding to inhaled tobramycin for *Pseudomonas aeruginosa* management in cystic fibrosis and non-CF bronchiectasis, where multiple completed Phase 3 RCTs exist and tobramycin inhalation solution (TOBI®) holds regulatory approval in multiple jurisdictions. Decision-makers evaluating this candidate should weigh the full prediction landscape before prioritising resources.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

