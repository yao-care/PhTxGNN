---
layout: default
title: Phenylephrine
parent: Moderate Evidence (L3-L4)
nav_order: 274
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-15
description: "Phenylephrine: predicted new indication Nasal cavity disease (evidence level L4). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "Phenylephrine"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis", "trigeminal autonomic cephalalgia"]
---

# Phenylephrine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Phenylephrine: From Rhinitis and Nasal Congestion to Nasal Cavity Disease

## One-Sentence Summary

Phenylephrine is an alpha-1 adrenergic agonist originally used for conditions such as allergic rhinitis, the common cold, nasopharyngitis, conjunctivitis, and hemorrhoids.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but no clinical trials are registered and the **5 publications** found are mostly reviews, a case report, or studies where phenylephrine is not the focus.
The prediction is largely an extension of existing nasal indications rather than a true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis (also conjunctivitis, headache disorder, hemorrhoid, proctitis, per the knowledge graph); no approved indication text is available for the local registration |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, phenylephrine is an alpha-1 adrenergic agonist. It constricts the blood vessels of the nasal mucosa, which reduces congestion, swelling, and mucosal bleeding.

This is consistent with its established uses in rhinitis and nasopharyngitis. "Nasal cavity disease" is a broad category that largely overlaps with these existing indications, so the very high TxGNN score (99.97%) probably reflects that overlap rather than a new therapeutic discovery.

The literature mentions phenylephrine in combination nasal sprays (for example, Polydexa, which also contains dexamethasone, neomycin, and polymyxin B) and as a topical vasoconstrictor in endoscopic sinus surgery. The titles and abstracts available do not show controlled trials of phenylephrine alone.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37184554](https://pubmed.ncbi.nlm.nih.gov/37184554/) | 2023 | Review | Vestnik otorinolaringologii | Endoscopic assessment of the nasal mucosa after local anti-inflammatory and antibacterial therapy, including Polydexa spray with phenylephrine |
| [37970776](https://pubmed.ncbi.nlm.nih.gov/37970776/) | 2023 | Review | Vestnik otorinolaringologii | Therapy of inflammatory nose and sinus diseases should follow the pathogenesis; the drug should reduce hyperemia, swelling, and mucus |
| [40899890](https://pubmed.ncbi.nlm.nih.gov/40899890/) | 2025 | Experimental/clinical study | Vestnik otorinolaringologii | Safety and efficacy evaluation of Polydexa spray with phenylephrine in acute rhinosinusitis; the abstract notes no prior toxicity data |
| [25133491](https://pubmed.ncbi.nlm.nih.gov/25133491/) | 2014 | RCT (triple blind) | PLoS One | Topical tranexamic acid and bleeding during endoscopic sinus surgery in chronic rhinosinusitis; phenylephrine is not the focus |
| [7378007](https://pubmed.ncbi.nlm.nih.gov/7378007/) | 1980 | Case report | Archives of Ophthalmology | Toxic reactions to intranasal cocaine, with an additional reaction to intranasal phenylephrine in one patient |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0383 | Phenylephrine | Not specified | Not specified (status: cancelled) |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** The TxGNN knowledge graph links phenylephrine to contraindications in hypertension, liver failure and liver disease, kidney disease, epilepsy, chronic obstructive pulmonary disease, peptic ulcer and gastritis, inflammatory bowel disease, hypothyroidism, adrenocortical insufficiency, porphyria, pancreatitis, thrombocytopenia, and psychotic disorders. These come from graph edges and should be checked against an official package insert.
- **Drug Interactions:** 100 interactions were found. The ones listed are all rated Moderate:
  - Antidiabetic agents: acarbose, acetohexamide, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, empagliflozin, glimepiride, glipizide, glyburide, exenatide, dulaglutide, insulin products
  - Anticholinergics: atropine (ophthalmic), clidinium, hyoscyamine
  - Anorectic: diethylpropion
- **Literature note:** One case report describes toxicity after intranasal phenylephrine, and the authors caution against use with hypertensive cardiovascular disease or other sympathomimetics.

Please refer to the package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN score is high, but the evidence is L4 with no registered clinical trials, and the only local registration is cancelled.
- The prediction mostly restates existing nasal indications, so it adds little new value.

**To proceed, the following is needed:**
- Official package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Controlled clinical evidence of phenylephrine in nasal cavity disease, separate from combination sprays
- A clear regulatory pathway, since no registration is currently valid in the Philippines
- Defined route and dosage form for the intended nasal use

---

## Other Predictions Considered

| Predicted Indication | TxGNN Score | Evidence Level | Decision | Comment |
|------|------|------|------|------|
| Acute laryngopharyngitis | 99.97% | L5 | Hold | No trials or literature. Decongestion does not address the infectious or inflammatory cause, so the link is speculative. |
| Trigeminal autonomic cephalalgia | 99.30% | L4 | Hold | The 13 publications are mostly pupillometry studies in cluster headache, paroxysmal hemicrania, and SUNCT, where phenylephrine is a diagnostic probe of sympathetic function, not a treatment. They give no support for therapeutic use. A systemic vasoconstrictor and pressor could also be a concern in headache patients. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

