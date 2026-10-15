---
layout: default
title: Pyrazinamide
parent: Model Prediction Only (L5)
nav_order: 287
evidence_level: L5
indication_count: 10
---

# Pyrazinamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Pyrazinamide: From Tuberculosis to Infectious Otitis Media

## One-Sentence Summary

Pyrazinamide is an anti-tuberculosis drug, originally used for pulmonary tuberculosis and tuberculous meningitis.
The TxGNN model predicts it may be effective for **infectious otitis media**, but there are currently **no clinical trials** and **no publications** directly supporting this prediction. This is a model-only (L5) signal, and the evidence for the related middle ear conditions is limited to case reports of tuberculous ear infection.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis, meningeal tuberculosis, tuberculous meningitis (the license record has no approved indication text) |
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pyrazinamide is a first-line anti-tuberculosis agent. It is a prodrug that is converted to pyrazinoic acid by mycobacterial pyrazinamidase, so it acts specifically against *Mycobacterium tuberculosis*.

The prediction for infectious otitis media is therefore hard to support mechanistically. Pyrazinamide has no activity against the usual causes of otitis media (*S. pneumoniae*, *H. influenzae*, *M. catarrhalis*). The high score most likely reflects the drug's closeness to tuberculous otitis in the knowledge graph, not a real mechanistic link.

The other highly ranked ear-related predictions fall into two groups:
- **Tuberculous subset only:** Middle ear disease, chronic otitis media and suppurative otitis media have case reports where pyrazinamide was part of standard multidrug anti-TB therapy. This is an on-label use of the drug for extrapulmonary TB, not a new repurposing mechanism.
- **No plausible mechanism:** Otosalpingitis, non-suppurative otitis media, allergic otitis media, middle ear cholesterol granuloma and infectious otitis interna are driven by non-mycobacterial processes (Eustachian tube dysfunction, allergy, foreign-body reaction). They have no supporting data.

The Lyme disease prediction (rank 9) is a hypothesis only. The idea is that pyrazinamide targets dormant persister cells, and a similar concept has been discussed for *Borrelia*. The retrieved literature, however, concerns dapsone and a general review, not pyrazinamide data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for infectious otitis media or for any of the other top-ranked predictions.

---

## Literature Evidence

There is no literature for the top prediction (infectious otitis media). The table below shows the most relevant publications retrieved for related predictions, all of which are low-tier evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26785789](https://pubmed.ncbi.nlm.nih.gov/26785789/) | 2013 | Case report | Int J Mycobacteriol | A 55-year-old woman with nasal and middle ear TB was treated with rifampicin, isoniazid and pyrazinamide for 9 months. No recurrence after one year. |
| [15168420](https://pubmed.ncbi.nlm.nih.gov/15168420/) | 2004 | Case report | Am J Kidney Dis | Tuberculous otitis media in a renal transplant recipient, diagnosed after recurrent chronic otitis media was treated repeatedly with empiric antibiotics. |
| [41783873](https://pubmed.ncbi.nlm.nih.gov/41783873/) | 2026 | Case report | Cureus | Tuberculous otitis media is rare and often diagnosed late. The report describes a case presenting with otorrhea. |
| [8011030](https://pubmed.ncbi.nlm.nih.gov/8011030/) | 1994 | Case series | Laryngo-Rhino-Otologie | Twelve patients had tuberculosis first found in the head and neck area, one of them in the middle ear. |
| [2527907](https://pubmed.ncbi.nlm.nih.gov/2527907/) | 1989 | Review | Infect Dis Clin North Am | A general review of new uses for older antibiotics, including pyrazinamide. It is not specific to ear disease or Lyme disease. |
| [21439219](https://pubmed.ncbi.nlm.nih.gov/21439219/) | 2011 | Animal study | J Am Assoc Lab Anim Sci | Torticollis occurred in some TB-infected mice, including some on pyrazinamide-containing regimens. Not relevant to human ear disease. |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0407 | Pyrazinamide | Not specified | Not specified (registration cancelled) |

---

## Safety Considerations

Please refer to the package insert for safety information. Label warnings and contraindications were not available for this report.

- **Disease associations from the knowledge graph (not label text):** The knowledge graph links pyrazinamide with possible contraindications in liver failure and acute liver failure, liver disease, hepatitis, porphyria (including inherited porphyria and porphyrin metabolism disease), gout, diabetes mellitus, diabetic ketoacidosis, gallbladder disease, peripheral neuropathy and other peripheral nervous system disease, substance abuse or dependence, and slow acetylator status. These should be confirmed against an authoritative label.
- **Drug Interactions:** 56 interactions were identified. Two are rated Moderate: picosulfuric acid and naltrexone. Others, such as streptomycin, metronidazole, prednisone, amphotericin B, omeprazole, pantoprazole and morphine, have no assigned severity level.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top prediction rests on a model score alone, with no trials or literature. The drug has no plausible activity against common otitis media pathogens.
- The only supporting evidence is case reports of tuberculous ear infection, which are already covered by pyrazinamide's standard use in TB. In addition, the Philippines registration is cancelled.

**To proceed, the following is needed:**
- Mechanism of action data and a clear rationale for any non-tuberculous ear indication.
- The package insert warnings and contraindications from the DOH-FDA Philippines, which are needed for safety screening.
- If the interest is TB of the ear, a focused review of extrapulmonary TB guidelines, since this is an existing use and not a repurposing opportunity.
- Confirmation of the current Philippines registration status, since the only record is cancelled.
- Any further exploration of the Lyme disease hypothesis would need laboratory data on pyrazinamide against *Borrelia* first.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

