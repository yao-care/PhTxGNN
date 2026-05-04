---
layout: default
title: Pyrazinamide
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 10
---

# Pyrazinamide
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

# Pyrazinamide: From Tuberculosis to Infectious Otitis Media

## One-Sentence Summary

Pyrazinamide is a cornerstone antibiotic in the standard first-line tuberculosis regimen (HRZE: isoniazid, rifampicin, pyrazinamide, ethambutol), used specifically against *Mycobacterium tuberculosis*.
The TxGNN model predicts it may be effective for **Infectious Otitis Media**, with **0 clinical trials** and **0 publications** directly supporting this direction.
Critically, all 10 top-ranked predictions for this drug cluster around ear infections — a pattern strongly consistent with a knowledge graph traversal artifact rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Tuberculosis (first-line therapy, part of HRZE four-drug regimen) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, Pyrazinamide is a prodrug that is activated by *M. tuberculosis* pyrazinamidase into its active form, pyrazinoic acid. Pyrazinoic acid disrupts the membrane potential and energy metabolism of *M. tuberculosis* in its semi-dormant, acidic intracellular environment — a mechanism that is highly specific to mycobacteria. Pyrazinamide has no meaningful antibacterial activity against the typical pathogens responsible for infectious otitis media (*Streptococcus pneumoniae*, *Haemophilus influenzae*, *Moraxella catarrhalis*), making a direct mechanistic bridge implausible.

The apparent connection between Pyrazinamide and otitis media stems from a rare and well-documented clinical entity: **tuberculous otitis media**, in which *M. tuberculosis* spreads hematogenously or via the Eustachian tube to the middle ear, producing an atypical form of chronic otitis media (accounting for fewer than 0.1% of all otitis media cases). The literature retrieved across all ear-disease indications (ranks 2–10) describes exactly this scenario — standard anti-TB therapy including pyrazinamide used to treat TB manifesting in the ear. This is not drug repurposing; it is the original tuberculosis indication presenting in an unusual anatomical site.

This case illustrates a known failure mode of knowledge graph–based prediction: when a drug is strongly connected to a disease node (TB) that in turn has secondary edges to related conditions (ear infections as extrapulmonary TB manifestations), the model can assign high prediction scores to those secondary nodes. The uniform clustering of all 10 top predictions around ear diseases — with TxGNN scores above 99% — is a hallmark signature of this artifact pattern, not a genuine biological repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Pyrazinamide in infectious otitis media.

> **Data Quality Alert:** During evidence collection for rank 9 (Lyme disease), trial **NCT05473520** was retrieved. Upon review, this is a Phase 3 trial of adjunctive *doxycycline* as host-directed therapy for **pulmonary tuberculosis** — it does not involve Pyrazinamide as the study drug, has no relation to Lyme disease or otitis media, and represents a retrieval artifact. It must not be counted as supporting evidence for any predicted indication in this report.

---

## Literature Evidence

Currently no literature directly supporting Pyrazinamide as a treatment for infectious otitis media.

> **Contextual Note:** Across related ear-disease indications (ranks 2, 4, 5, 10), a total of 15 publications were retrieved. All describe **tuberculous otitis media** — an extremely rare extrapulmonary TB manifestation. Representative publications include:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26785789](https://pubmed.ncbi.nlm.nih.gov/26785789/) | 2013 | Case Report | Int J Mycobacteriology | Female patient with nasal and middle ear TB confirmed by PCR; treated with rifampicin + isoniazid + **pyrazinamide** (25 mg/kg) for 9 months; no recurrence at 1-year follow-up |
| [21532520](https://pubmed.ncbi.nlm.nih.gov/21532520/) | 2011 | Case Series | Otology & Neurotology | TB as a rare cause of otitis media; study highlights variable clinical presentation and importance of early detection for treatment outcome |
| [18852993](https://pubmed.ncbi.nlm.nih.gov/18852993/) | 2008 | Review/Case Series | Brazilian J Otorhinolaryngology | TB is a rare cause of chronic suppurative otitis media; patients present with multiple tympanic membrane perforations, discharge, and progressive hearing loss |
| [41783873](https://pubmed.ncbi.nlm.nih.gov/41783873/) | 2026 | Case Report | Cureus | Recent case of tuberculous otitis media in low-TB-prevalence region; underscores delayed diagnosis risk and irreversible complications |
| [12680299](https://pubmed.ncbi.nlm.nih.gov/12680299/) | 2003 | Case Series | Anales Otorrinolaringologicos | 3 cases of tuberculous otitis media; anti-TB medical therapy effective; diagnosis frequently delayed due to resemblance to common otitis media |

**All retrieved literature confirms pyrazinamide use within standard TB therapy for a rare TB manifestation — not evidence of independent repurposing.**

---

## Safety Considerations

Please refer to the package insert for safety information.

> Pyrazinamide carries well-established risks that should be considered in any future evaluation: **hepatotoxicity** (dose-dependent, requires liver function monitoring), **hyperuricemia** (with risk of acute gout attacks), and **arthralgia**. Complete TFDA package insert warnings and contraindications data were not available in this evidence pack (Data Gap DG001). Formal Drug-Drug Interaction data was also not retrieved (query returned no results).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN predictions for Pyrazinamide cluster exclusively around ear infections at evidence levels L4–L5, and mechanistic analysis confirms that Pyrazinamide's bactericidal activity is specific to *M. tuberculosis* — it has no activity against the pathogens that cause common infectious otitis media. The retrieved literature confirms this pattern is entirely explained by tuberculous otitis media (a rare TB manifestation), not independent repurposing. Pyrazinamide is additionally not registered in the Philippines market, and no safety data is currently available for a formal risk assessment.

**To proceed, the following is needed:**
- Retrieve full MOA and safety data from DrugBank (DB00339) and TFDA package insert to rule out any pleiotropic or immunomodulatory effects not yet characterized
- Evaluate whether Pyrazinamide's TxGNN predictions should be flagged as a **KG-artifact cluster** to improve pipeline output quality (all top-10 predictions in one disease category with uniform "Hold" outcomes is a strong quality signal)
- No further clinical evidence collection for ear-disease indications is recommended without a mechanistic rationale independent of its anti-TB activity
- If future DrugBank review reveals novel non-mycobacterial mechanisms, re-evaluation against a broader set of predicted indications would be warranted

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

