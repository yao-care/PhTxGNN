---
layout: default
title: Adenosine
parent: Model Prediction Only (L5)
nav_order: 16
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Adenosine: predicted new indication Obsolete bundle branch block (evidence level L5). Approved use: Ventricular tachycardia"
monitor_inn: "Adenosine"
predicted_indications: ["obsolete bundle branch block"]
---

# Adenosine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Adenosine: From Ventricular Tachycardia to Obsolete Bundle Branch Block

## One-Sentence Summary

Adenosine was originally used for ventricular tachycardia (VT).
The TxGNN model predicts it may be effective for **obsolete bundle branch block**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
The prediction most likely reflects an ontology artifact rather than a real clinical opportunity. A second, more plausible candidate, catecholaminergic polymorphic ventricular tachycardia (CPVT), is discussed below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ventricular tachycardia (from the knowledge graph; the Philippines registration has no indication text) |
| Predicted New Indication | Obsolete bundle branch block |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Adenosine is known to act on A1 receptors in the atrioventricular (AV) node, slowing conduction, which is why it is used in arrhythmia management.

For the top prediction, this mechanism does not fit well. "Obsolete bundle branch block" is a deprecated ontology term, not a distinct clinical entity. Slowing conduction would not plausibly treat a bundle branch conduction defect, and AV nodal blockade could worsen conduction disease. Adenosine is used diagnostically to unmask conduction abnormalities. The very high score (0.9994) is a knowledge-graph output only, and it is likely an artifact of ontology mapping.

**Second-ranked prediction: catecholaminergic polymorphic ventricular tachycardia (CPVT).** Its score is 99.42%, and it is the more plausible candidate. CPVT is driven by abnormal sarcoplasmic reticulum calcium release (RyR2, CASQ2, TECRL variants) that triggers adrenergic-dependent delayed afterdepolarizations. Adenosine opposes beta-adrenergic stimulation through A1 receptor signaling and may suppress this cAMP-dependent triggered activity. This is plausible, but the evidence is indirect. It would support acute termination at most, not a treatment indication. Standard CPVT management (beta-blockers, flecainide, sympathetic denervation, ICD) is already well established.

## Clinical Trial Evidence

Currently no related clinical trials registered, for either the top prediction or the CPVT prediction.

## Literature Evidence

There is no literature for the top prediction (obsolete bundle branch block). The table below covers the second-ranked prediction, CPVT, and lists the most relevant items.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18313614](https://pubmed.ncbi.nlm.nih.gov/18313614/) | 2008 | Case report | Heart Rhythm | Adenosine triphosphate (ATP, not adenosine) terminated bidirectional VT in one CPVT patient. This supports acute termination only. |
| [40165484](https://pubmed.ncbi.nlm.nih.gov/40165484/) | 2025 | Consensus statement | Europace | Consensus on pharmacological provocation testing in cardiac electrophysiology. Describes diagnostic use, not treatment. |
| [21699856](https://pubmed.ncbi.nlm.nih.gov/21699856/) | 2011 | Case series | Heart Rhythm | Abnormal post-pacing repolarization in CPVT with an RyR2 mutation. |
| [18368865](https://pubmed.ncbi.nlm.nih.gov/18368865/) | 2007 | Review | J Assoc Physicians India | Recognition and management of VT in structurally normal hearts. |
| [39148245](https://pubmed.ncbi.nlm.nih.gov/39148245/) | 2024 | Review | Paediatr Anaesth | Pediatric arrhythmias for anesthesiologists. |
| [15324613](https://pubmed.ncbi.nlm.nih.gov/15324613/) | 2004 | Review | Curr Treat Options Cardiovasc Med | Management options for syncope. |
| [38776406](https://pubmed.ncbi.nlm.nih.gov/38776406/) | 2024 | Preclinical | Cardiovasc Res | PDE2A and PDE4B gene therapy improves heart failure and arrhythmias in mice by modulating cAMP compartmentation. |
| [41691612](https://pubmed.ncbi.nlm.nih.gov/41691612/) | 2026 | Preclinical | J Physiol | Human cardiac-neural microtissues suggest CPVT also involves the sympathetic neuron. |
| [35577932](https://pubmed.ncbi.nlm.nih.gov/35577932/) | 2022 | Preclinical | Commun Biol | TECRL deficiency causes abnormal mitochondrial function in cardiomyocytes. |
| [30209242](https://pubmed.ncbi.nlm.nih.gov/30209242/) | 2018 | Preclinical | Sci Transl Med | Sarcoplasmic reticulum calcium leak contributes to arrhythmia but not to heart failure progression. |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0006 | Adenosine | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Disease contraindications (knowledge-graph edges, not label text):** the following conditions are linked to adenosine as contraindications.
  - Respiratory: chronic obstructive pulmonary disease, asthma (including intrinsic and allergic forms), pulmonary emphysema, respiratory failure.
  - Conduction and rhythm: atrioventricular block, sick sinus syndrome (including the familial form).
  - Valve and structural: aortic stenosis (including aortic valve disease and supravalvular forms), mitral valve stenosis, pulmonary valve insufficiency.
  - Coronary and pericardial: acute coronary syndrome, coronary artery disease, pericarditis.
  - Autonomic and blood pressure: hypotensive disorder, autonomic nervous system disease, Horner syndrome.
- **Drug interactions:** 100 interactions were identified, and the main ones are listed here. The Major ones are **cisapride, dolasetron and papaverine**. Moderate ones include famotidine, clarithromycin, granisetron, levofloxacin, ondansetron and palonosetron. Several are QT-prolonging drugs, which warrants attention in patients with arrhythmias. The rest are of unknown severity.

Please refer to the package insert for key warnings and label contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top prediction, obsolete bundle branch block, is a deprecated ontology term with no trials or literature, and adenosine's mechanism could worsen conduction disease. The prediction should not be pursued.
- The CPVT prediction is mechanistically plausible, but the only direct evidence is a single case report using ATP. Established therapies already exist.
- The only Philippines registration is cancelled, and the package insert safety data is not available.

**To proceed, the following is needed:**
- Confirm the ontology mapping of "obsolete bundle branch block" and discard it if it is not a valid clinical entity.
- Detailed mechanism of action data (MOA).
- Philippines package insert warnings and contraindications, from the DOH-FDA Philippines website.
- If CPVT is pursued, prospective or controlled data on adenosine itself, and a comparison against standard therapy.
- Review of the cancelled registration status and available formulations and routes.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

