---
layout: default
title: Oxymetazoline
parent: Moderate Evidence (L3-L4)
nav_order: 268
evidence_level: L4
indication_count: 3
---

# Oxymetazoline
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Oxymetazoline: From Pharyngitis and Common Cold to Nasal Cavity Disease

## One-Sentence Summary

Oxymetazoline is a topical alpha-adrenergic vasoconstrictor, originally used for pharyngitis and the common cold (nasal congestion).
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are **no registered clinical trials** and only **5 indirect publications** (mostly case reports, an animal study, and small clinical studies) to support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pharyngitis, common cold |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, oxymetazoline acts as an agonist at alpha-1 and alpha-2 adrenergic receptors. It also binds several serotonin receptors (5-HT1B, 5-HT1D, 5-HT2C). Applied to the nasal mucosa, it constricts blood vessels, which reduces swelling and congestion and improves nasal patency.

"Nasal cavity disease" is a very broad category and overlaps heavily with the existing common cold and nasal congestion use. The high model score is consistent with this mechanism, but it likely reflects similarity to the original indication rather than a distinct new finding. Specific sub-indications (for example, rhinitis, sinusitis, or mucosal bleeding) would need to be defined before this could be treated as true repurposing.

Two other predictions are worth noting:
- **Acute laryngopharyngitis** (score 99.95%): closely related to the original pharyngitis indication, but there is no clear mechanism for treating laryngeal or pharyngeal inflammation with a nasal vasoconstrictor. There are no trials or literature. Evidence level is L5.
- **Headache disorder** (score 99.04%): has the most relevant clinical signal, a study of intranasal tetracaine plus oxymetazoline in status migrainosus. The combination means oxymetazoline's own contribution cannot be separated. Evidence level is L3.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top prediction (nasal cavity disease):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9929658](https://pubmed.ncbi.nlm.nih.gov/9929658/) | 1998 | Clinical study | Ann N Y Acad Sci | Effects of acute rhinitis (common cold) on olfactory function in 36 subjects, using evoked potentials and acoustic rhinometry |
| [8615587](https://pubmed.ncbi.nlm.nih.gov/8615587/) | 1996 | Animal study | Ann Otol Rhinol Laryngol | Oxymetazoline nose drops in rabbit acute bacterial sinusitis, evaluating the effect on local tissue defense |
| [25496205](https://pubmed.ncbi.nlm.nih.gov/25496205/) | 2015 | Clinical study | J Plast Surg Hand Surg | Nasal patency by acoustic rhinometry in children after cleft lip and palate repair; indirect relevance |
| [28490409](https://pubmed.ncbi.nlm.nih.gov/28490409/) | 2017 | Case series | Am J Rhinol Allergy | Coblation treatment of nasal telangiectasias in hereditary hemorrhagic telangiectasia; indirect relevance |
| [38024464](https://pubmed.ncbi.nlm.nih.gov/38024464/) | 2023 | Case report | Glob Pediatr Health | Rhinoscleroma in a 9-year-old boy; indirect relevance |

For the headache disorder prediction (secondary):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31919839](https://pubmed.ncbi.nlm.nih.gov/31919839/) | 2020 | Clinical study (design to be verified) | Headache | Intranasal 3% tetracaine plus 0.05% oxymetazoline in status migrainosus |
| [23575821](https://pubmed.ncbi.nlm.nih.gov/23575821/) | 2013 | Case report | Cephalalgia | Unilateral nasal pain with migraine features, supporting a nasal-trigeminal link |
| [36425231](https://pubmed.ncbi.nlm.nih.gov/36425231/) | 2022 | Review | Health Psychol Res | Drug interactions with MAO inhibitors; relevant as a safety signal for sympathomimetics |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0368 | Oxymetazoline | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: The TxGNN knowledge graph lists the following conditions as contraindicated or of concern:
  - Cardiovascular: hypertension, heart disease, cardiovascular disease, coronary artery disease, arteriosclerosis, atherosclerosis
  - Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperthyroidism, Graves disease, thyrotoxicosis
  - Urologic: benign prostatic hyperplasia
  - Eye: angle-closure (closed-angle) glaucoma, eye infectious disease, conjunctivitis, vision disorder, blindness
- **Drug Interactions**: The interaction query identified 9 pharmacological targets: alpha-1A/1B/1D and alpha-2A/2B/2C adrenoceptors and 5-HT1B, 5-HT1D, and 5-HT2C receptors. These are receptor targets rather than specific interacting drugs. Literature also flags interaction risk with MAO inhibitors, which may cause hypertensive or headache reactions.
- **Other considerations from the literature**: Prolonged use may cause rebound congestion and possibly rebound headache.

Please refer to the package insert for other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone, with no registered trials and only indirect literature. "Nasal cavity disease" largely overlaps with the existing common cold indication, so it is not a distinct repurposing signal. In addition, the only Philippines registration is cancelled.

**To proceed, the following is needed:**
- Define specific sub-indications within nasal cavity disease (for example, rhinitis, sinusitis, epistaxis)
- Detailed mechanism of action data
- Package insert warnings and contraindications for the Philippines
- Confirmation of the regulatory status and whether a valid registration exists or can be obtained
- For the headache signal: verify the design of the status migrainosus study and separate oxymetazoline's effect from tetracaine
- A safety plan covering cardiovascular risk, MAO inhibitor interactions, and rebound congestion with prolonged use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

