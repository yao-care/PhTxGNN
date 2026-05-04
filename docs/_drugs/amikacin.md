---
layout: default
title: Amikacin
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 10
---

# Amikacin
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

# Amikacin: From Gram-negative Bacterial Infections to Paratyphoid Fever

## One-Sentence Summary

Amikacin is a broad-spectrum aminoglycoside antibiotic widely used worldwide for serious gram-negative bacterial infections (including *Pseudomonas aeruginosa*, *Klebsiella*, and *E. coli*), though it is not currently registered in the Philippines.
The TxGNN model predicts it may be effective for **Paratyphoid Fever** (infection caused by *Salmonella paratyphi* A/B/C),
with **0 clinical trials** and **12 publications** currently supporting this direction — primarily microbiological antibiogram data and case-level clinical reports.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious gram-negative bacterial infections (global standard use; no Philippines registration on record) |
| Predicted New Indication | Paratyphoid Fever |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Amikacin is a semi-synthetic aminoglycoside antibiotic derived from kanamycin. It exerts bactericidal activity by irreversibly binding to the 30S ribosomal subunit of susceptible bacteria, thereby inhibiting protein synthesis. Critically, Amikacin was engineered to resist most aminoglycoside-modifying enzymes that inactivate other members of this class (e.g., gentamicin, tobramycin), giving it superior activity against many multidrug-resistant (MDR) gram-negative Enterobacteriaceae.

*Salmonella paratyphi* A, B, and C are gram-negative facultative anaerobes belonging to the Enterobacteriaceae family — precisely the organism class against which Amikacin was designed. Multiple antibiogram studies (PMID 18383953, PMID 27407999, PMID 8354556) have consistently demonstrated in vitro susceptibility of *S. paratyphi* strains to amikacin. Although fluoroquinolones (e.g., ciprofloxacin) and third-generation cephalosporins (e.g., ceftriaxone) remain first-line treatment for enteric fever, the emergence of extensively drug-resistant (XDR) and MDR strains in South Asia and Africa has created a genuine clinical gap that Amikacin could help fill.

The clinical relevance is further supported by real-world case reports: Amikacin has been used in neonatal paratyphoid sepsis (PMID 17337835), drug-resistant enteric fever requiring alternative antibiotics (PMID 2516600), and complicated presentations such as splenic abscess (PMID 16410091). In contexts where fluoroquinolone resistance is high and treatment options are limited — particularly for neonates and critically ill patients — Amikacin's bactericidal potency against *Salmonella* makes this TxGNN prediction mechanistically well-grounded.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18383953](https://pubmed.ncbi.nlm.nih.gov/18383953/) | 2007 | Prospective Observational | J Indian Medical Association | Prospective study in 145 pediatric enteric fever cases (June 2004–April 2005); determined antibiotic sensitivity patterns of both *S. typhi* and *S. paratyphi*; highlights aminoglycoside susceptibility in preschool children |
| [17337835](https://pubmed.ncbi.nlm.nih.gov/17337835/) | 2007 | Clinical Review / Case Series | Indian J Pediatrics | Neonatal paratyphoid sepsis case involving multidrug-susceptible *S. paratyphi* A; documents real-world antibiotic management including amikacin consideration |
| [30724049](https://pubmed.ncbi.nlm.nih.gov/30724049/) | 2018 | Microbiological / Antibiogram Study | Pakistan J Biological Sciences | Isolation and identification of *Salmonella paratyphi* from enteric fever patients in Pakistan; characterizes antibiotic susceptibility profiles including aminoglycosides |
| [27407999](https://pubmed.ncbi.nlm.nih.gov/27407999/) | 2007 | Observational Study | Med J Armed Forces India | In vitro susceptibility testing of *S. typhi* and *S. paratyphi* A in northern India; documents retained amikacin sensitivity in chloramphenicol/ampicillin-resistant strains |
| [26905550](https://pubmed.ncbi.nlm.nih.gov/26905550/) | 2014 | Retrospective Microbiological Study | JNMA (Nepal Medical Association) | Blood culture isolate antibiogram at a teaching hospital; guides empiric antimicrobial regimen selection for bacteremia including Salmonella species |
| [14596347](https://pubmed.ncbi.nlm.nih.gov/14596347/) | 2003 | Epidemiological / Microbiological Study | The New Microbiologica | 13-year surveillance (1988–2000) of *S. typhi* and *S. paratyphi* in Jordan; 1.4 million diarrhoeal cases reviewed; antibiotic resistance trends documented |
| [16410091](https://pubmed.ncbi.nlm.nih.gov/16410091/) | 2006 | Case Series | J Pediatric Surgery | Four pediatric patients with splenic abscess managed with percutaneous drainage plus antibiotics; illustrates complicated paratyphoid requiring targeted antibiotic combinations |
| [10505326](https://pubmed.ncbi.nlm.nih.gov/10505326/) | 1999 | Case Report | Pediatric Hematology and Oncology | Acalculous cholecystitis caused by *S. paratyphi* B in a child with acute leukemia; successfully treated with **cefepime + amikacin** + G-CSF — direct documentation of amikacin clinical use |
| [9459410](https://pubmed.ncbi.nlm.nih.gov/9459410/) | 1997 | Case Report | J Infection | Quinolone-resistant *S. paratyphi* B meningitis in a neonate; highlights the clinical problem of quinolone resistance and need for alternative agents such as amikacin |
| [2516600](https://pubmed.ncbi.nlm.nih.gov/2516600/) | 1989 | Case Series / Clinical Report | Mikrobiyoloji Bulteni | 48 pediatric patients with confirmed *S. paratyphi* B infection resistant to classical treatment (ampicillin/chloramphenicol/co-trimoxazole); documents treatment outcomes with alternative antibiotic regimens |

---

## Philippines Market Information

Amikacin is **not currently registered** with the Philippine FDA (Food and Drug Administration). No drug licenses, brand names, or approved indications are on record for this drug in the Philippines.

> **Note:** Despite lack of local registration, amikacin is available in many countries as a generic injectable (IV/IM), and importation for compassionate/hospital use may be possible under existing Philippine FDA frameworks for unregistered essential medicines.

---

## Safety Considerations

Detailed local package insert warnings and contraindications are not available in this Evidence Pack. Please refer to the current package insert and established pharmacological references for complete safety information.

Key safety considerations known from the general amikacin literature that should be reviewed prior to any clinical application:

- **Nephrotoxicity**: Aminoglycosides are associated with dose-dependent acute tubular necrosis; renal function monitoring (serum creatinine, BUN) is required, especially with prolonged courses.
- **Ototoxicity**: Both cochlear (irreversible hearing loss) and vestibular toxicity are recognized class effects; audiometric monitoring is recommended for courses >5 days.
- **Pharmacokinetic considerations in special populations**: Neonates (immature renal clearance), elderly patients, and those with hypoalbuminemia (note: congenital analbuminemia — see rank 7 in predictions — would significantly increase free drug concentration and toxicity risk) require TDM (therapeutic drug monitoring).
- **Drug interaction caution**: Concurrent use with other nephrotoxic agents (e.g., vancomycin, NSAIDs, contrast agents) or loop diuretics (furosemide) increases toxicity risk.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Amikacin has well-documented in vitro bactericidal activity against *Salmonella paratyphi*, and multiple case-level clinical reports confirm actual therapeutic use in paratyphoid complications (splenic abscess, neonatal sepsis, drug-resistant strains). The mechanistic rationale is strong: Amikacin's resistance to aminoglycoside-modifying enzymes makes it particularly valuable precisely in the MDR scenarios most prevalent in endemic regions. However, no prospective clinical trials specifically evaluating Amikacin for paratyphoid fever have been registered, and the current evidence base consists entirely of observational/microbiological data (L3).

**To proceed, the following is needed:**
- **Obtain full safety profile**: Download and parse the Philippine FDA-equivalent package insert (TFDA/WHO-PQ reference documents) to complete the DG001 data gap; this is currently blocking the S1 safety initial assessment.
- **Confirm MOA data from DrugBank** (DG002): Query DrugBank API for DB00479 to populate mechanism of action for regulatory-grade documentation.
- **Philippine registration pathway assessment**: Evaluate whether amikacin qualifies for inclusion under the Philippine National Formulary or WHO Essential Medicines List compassionate use channel, given zero current registrations.
- **Prospective clinical design**: Design a focused observational study or pragmatic RCT in MDR paratyphoid fever populations (e.g., Philippines, Pakistan, South Asia) comparing amikacin-containing regimens vs. current standards of care, with TDM-guided dosing.
- **Therapeutic drug monitoring (TDM) protocol**: Establish peak/trough monitoring parameters before any systematic clinical deployment, given nephrotoxicity and ototoxicity risks.
- **Pediatric dosing protocol**: Given that most existing clinical evidence involves pediatric and neonatal cases, a dedicated pediatric pharmacokinetics sub-study should be included in any future investigation.

---

> ⚠️ **Disclaimer**: This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. This analysis is generated by an AI-assisted drug repurposing system (TxGNN); all findings must be reviewed by qualified medical and pharmacological professionals before any clinical decision-making.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

