---
layout: default
title: Tobramycin
parent: Moderate Evidence (L3-L4)
nav_order: 338
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-28
description: "Tobramycin: predicted new indication Exposure keratitis (evidence level L4). Approved use: Bacterial meningitis, uveitis, conjunctivitis…"
monitor_inn: "Tobramycin"
predicted_indications: ["exposure keratitis", "non-human animal disease", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "epidemic keratoconjunctivitis"]
---

# Tobramycin
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

## Tobramycin: From Bacterial Eye and Central Nervous System Infections to Exposure Keratitis
{: .text-alpha }

## One-Sentence Summary

Tobramycin is an aminoglycoside antibiotic, originally used for bacterial infections such as conjunctivitis, uveitis, Staphylococcus aureus infection and bacterial meningitis.
The TxGNN model predicts it may be effective for **exposure keratitis**, but there are **no registered clinical trials** and only indirect literature (**8 publications**, mostly case reports and in vitro studies) behind this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial meningitis, uveitis, conjunctivitis, Staphylococcus aureus infection and related conditions (the registration record lists no approved indication text) |
| Predicted New Indication | Exposure keratitis |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L4 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, tobramycin is an aminoglycoside with broad activity against Gram-negative bacteria and Staphylococcus aureus, and it is already used topically for bacterial eye infections. Mechanistically, it may be applicable to exposure keratitis.

Exposure keratitis occurs when the cornea is not adequately protected, for example when the eyelids cannot close. The damaged surface is prone to secondary bacterial infection, which gives an antibacterial rationale for tobramycin.

There are important caveats. The available literature concerns bacterial keratitis (contact lens-related, MRSA, multidrug-resistant organisms), not exposure keratitis itself. One in vitro study (PMID 2707046) reports that aminoglycosides, including tobramycin, are toxic to corneal epithelial cells. This is a concern in a cornea that is already compromised.

Other predictions in the list have weaker support. Examples are non-human animal disease, postinfectious vasculitis, post-infectious syndrome, Chagas cardiomyopathy and infection-related hemolytic uremic syndrome. Several of these have no plausible antibacterial mechanism, and in hemolytic uremic syndrome the kidney risk is a clear adverse signal. Two further predictions, otitis externa and infective urethral stricture, rest on indirect evidence only.

## Clinical Trial Evidence

Currently no clinical trials are registered for exposure keratitis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42842711](https://pubmed.ncbi.nlm.nih.gov/42842711/) | 2026 | Retrospective cohort | Cornea | Compares outcomes of MRSA and MSSA Staphylococcus aureus keratitis (indirect evidence) |
| [2707046](https://pubmed.ncbi.nlm.nih.gov/2707046/) | 1989 | In vitro study | Current Eye Research | Four aminoglycosides, including tobramycin, were toxic to rabbit corneal epithelial cells (safety concern) |
| [17228760](https://pubmed.ncbi.nlm.nih.gov/17228760/) | 2006 | In vitro study | Nippon Ganka Gakkai Zasshi | Compared minimum inhibitory concentration and postantibiotic effect of eye drops against isolates from infectious keratitis in Japan |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Case report | Ophthalmology | Contact lens-related Bacillus cereus keratitis |
| [34987857](https://pubmed.ncbi.nlm.nih.gov/34987857/) | 2021 | Case report | Oxford Medical Case Reports | Multidrug-resistant Shewanella algae keratitis in a patient who could not close his eyes |
| [12861116](https://pubmed.ncbi.nlm.nih.gov/12861116/) | 2003 | Case report | Eye & Contact Lens | Bilateral MRSA keratitis after photorefractive keratectomy |
| [14574976](https://pubmed.ncbi.nlm.nih.gov/14574976/) | 2003 | Case report | Yan Ke Xue Bao | Paracentral corneal dellen as a rare sign of Graves ophthalmopathy |
| [42358321](https://pubmed.ncbi.nlm.nih.gov/42358321/) | 2026 | In vitro study (veterinary) | Frontiers in Veterinary Science | Effect of fluorometholone on antibiotic susceptibility of canine ocular bacteria |

None of these studies directly tests tobramycin in exposure keratitis.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0490 | Tobramycin | Not specified | Not specified (registration valid) |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: The TxGNN knowledge graph links tobramycin to contraindications in several disease groups:
  - Kidney disease, nephrocalcinosis
  - Myasthenia gravis and other neuromuscular junction disorders
  - Parkinson disease and parkinsonian disorders
  - Glaucoma and ocular hypertension
  - Herpes simplex virus keratitis, viral and fungal eye infections, ocular tuberculosis, ophthalmic herpes zoster
  - Diabetes mellitus and diabetic ketoacidosis
  - Clostridium difficile colitis and perinatal necrotizing enterocolitis
- **Drug Interactions**: 100 interactions were found. The main ones are:
  - **Major**: magnesium sulfate, mannitol
  - **Moderate**: other aminoglycosides (neomycin, kanamycin), vancomycin, amphotericin B, proton pump inhibitors, aspirin and mesalazine-type drugs
- **Other safety signals from the literature**: Corneal epithelial toxicity (PMID 2707046) is directly relevant to exposure keratitis. Ototoxicity and kidney toxicity are class concerns for aminoglycosides.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but it is supported only by model output and indirect literature (case reports and in vitro data), with no trials in exposure keratitis. Corneal toxicity is a concern in this setting. The only Philippines registration is cancelled, and no package insert data are available, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Mechanism of action data (for example from DrugBank)
- Clinical or well-designed preclinical data on tobramycin in exposure keratitis, including corneal epithelial safety
- Confirmation of an available topical ophthalmic product, since the only registration is cancelled and lists no dosage form
- A comparison with existing standard care for exposure keratitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

