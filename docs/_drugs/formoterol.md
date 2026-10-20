---
layout: default
title: Formoterol
parent: Model Prediction Only (L5)
nav_order: 157
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Formoterol: predicted new indication Respiratory malformation (evidence level L5). Approved use: Pulmonary emphysema, intrinsic asthma, allergic asthma"
monitor_inn: "Formoterol"
predicted_indications: ["respiratory malformation", "bronchitis", "Rienhoff syndrome"]
---

# Formoterol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Formoterol: From Pulmonary Emphysema and Asthma to Respiratory Malformation

## One-Sentence Summary

Formoterol is a long-acting beta2-agonist bronchodilator, originally used for obstructive airway disease such as pulmonary emphysema and asthma.
The TxGNN model predicts it may be effective for **respiratory malformation**, but there are **0 clinical trials** and **9 publications** (none addressing this condition) behind that prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary emphysema, intrinsic asthma, allergic asthma (from knowledge-graph indication data; the local licence record has no indication text) |
| Predicted New Indication | Respiratory malformation |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for formoterol were not available in the data compiled for this report. From general pharmacology, formoterol is a long-acting beta2-adrenoceptor agonist that relaxes airway smooth muscle. Its efficacy in asthma and emphysema is well established.

That mechanism does not clearly extend to the predicted indication. Respiratory malformation is a structural, developmental condition, and a bronchodilator acts on airway muscle tone and cannot correct a structural defect. The retrieved literature concerns asthma and COPD, with incidental hits on Down syndrome cognition, post-COVID small airway disease, and allergic bronchopulmonary mycosis.

The high score most likely reflects overlap with obstructive airway disease terms in the knowledge graph, not a real mechanistic link. This should be treated as a computational prediction only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the publications below studies respiratory malformation. They were retrieved because of formoterol and respiratory terms.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40840693](https://pubmed.ncbi.nlm.nih.gov/40840693/) | 2026 | RCT (systematic review and meta-analysis) | J Am Pharm Assoc | Compares budesonide/glycopyrrolate/formoterol with glycopyrrolate/formoterol for safety and efficacy in COPD. |
| [35115339](https://pubmed.ncbi.nlm.nih.gov/35115339/) | 2022 | RCT | Eur Respir J | Randomised crossover trial comparing repeated-dose budesonide/formoterol with salbutamol in stable adult asthma (bronchodilator, cardiovascular and adverse effects). |
| [22541245](https://pubmed.ncbi.nlm.nih.gov/22541245/) | 2012 | RCT | J Allergy Clin Immunol | Long-term safety and asthma control of budesonide/formoterol in African American patients with asthma. |
| [14738234](https://pubmed.ncbi.nlm.nih.gov/14738234/) | 2004 | RCT | Eur Respir J | Formoterol protects against platelet-activating factor-induced effects in asthma (12 patients). |
| [20528601](https://pubmed.ncbi.nlm.nih.gov/20528601/) | 2010 | Review | J Asthma | Reviews budesonide/formoterol pMDI for persistent asthma. |
| [24842803](https://pubmed.ncbi.nlm.nih.gov/24842803/) | 2014 | Review | Prog Neuropsychopharmacol Biol Psychiatry | Neurotransmitter-based strategies for cognitive dysfunction in Down syndrome (incidental hit). |
| [35034195](https://pubmed.ncbi.nlm.nih.gov/35034195/) | 2022 | Physiology study | Eur J Appl Physiol | Respiratory muscle and neural drive responses to increased mechanical load in COPD during sleep. |
| [37691104](https://pubmed.ncbi.nlm.nih.gov/37691104/) | 2023 | Case report | J Med Case Rep | Small airway disease in long COVID, followed over three years. |
| [41686546](https://pubmed.ncbi.nlm.nih.gov/41686546/) | 2026 | Case report | Medicine | Schizophyllum commune-associated allergic bronchopulmonary mycosis after lung cancer surgery. |

---

## Philippines Market Information

| Authorization Number | Product Name | Status |
|---------|------|------|
| PNF-0207 | Formoterol | Cancelled |

The only registration is cancelled, so formoterol has no currently valid registration in the Philippines. No dosage form or approved indication text is recorded for this licence.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN graph, not label text): hypertension and hypertensive disorder, long QT syndrome (including familial), epilepsy, liver disease, gallbladder disease, measles, herpes simplex virus keratitis, and a broad group of pituitary and growth hormone deficiency conditions (e.g., hypopituitarism, Kallmann syndrome, Sheehan syndrome).
- **Drug Interactions**: The query returned 100 interactions in total; the 20 shown were all Moderate or Minor.
  - Moderate interactions include antidiabetic agents (acarbose, alogliptin, albiglutide, canagliflozin, chlorpropamide, dapagliflozin, dulaglutide, empagliflozin), QT-relevant agents (cisapride, clarithromycin, dolasetron), sympathomimetics (ephedrine, isometheptene, diethylpropion), and famotidine.
  - Minor interactions include corticosteroids (beclomethasone, betamethasone, budesonide, dexamethasone).

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction rests on a very high model score alone, with no clinical trials and no supporting literature, and a bronchodilator has no plausible mechanism for correcting a structural malformation.
- For context, the other high-scoring predictions for formoterol mostly confirm existing uses. Asthma and obstructive lung disease have strong Phase 3 evidence, and "bronchitis" maps indirectly to COPD trials. None of that evidence supports respiratory malformation.

**To proceed, the following is needed:**
- Mechanism-of-action data for formoterol and a defined biological rationale for a structural respiratory defect.
- Any preclinical or clinical evidence in respiratory malformation, or a clearer definition of the target population.
- The Philippines package insert warnings and contraindications.
- Clarification of why the only Philippines registration was cancelled, and whether a valid product would be available.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

