---
layout: default
title: Lactulose
parent: Model Prediction Only (L5)
nav_order: 196
evidence_level: L5
indication_count: 8
---

# Lactulose
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Lactulose: From Hepatic Encephalopathy to Acute Urate Nephropathy

## One-Sentence Summary

Lactulose is a non-absorbable sugar originally used to treat hepatic encephalopathy, hepatic coma and constipation.
The TxGNN model predicts it may be effective for **acute urate nephropathy**, but there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it currently rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatic encephalopathy, hepatic coma, constipation |
| Predicted New Indication | Acute urate nephropathy |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, lactulose is an osmotic laxative that also acidifies the gut. Its efficacy in hepatic encephalopathy and constipation is established.

Mechanistically, however, no link to acute urate nephropathy can be supported. This condition involves uric acid precipitating in the kidney tubules, typically after tumour lysis. Lactulose has no established role in uric acid production, handling or excretion. The very high model score (99.89%) is not backed by any trial or publication. It is most likely an artefact of the knowledge-graph model rather than a real pharmacological signal, and it should not be treated as a lead without independent evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

| Authorization Number | Product Name | Type | Status |
|---------|------|------|-----------|
| PNF-0275 | Lactulose | Single-ingredient | Cancelled |

The only registration found has been cancelled, so no currently valid lactulose product is registered in the Philippines. Dosage form and approved indication are not recorded for this entry.

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not product label text):** diabetes mellitus, diabetic ketoacidosis, appendicitis, galactosemia, glycogen storage disease, G6PD deficiency, cystinuria, glucose-galactose malabsorption.
- **Drug Interactions:** The interaction search returned 100 entries, almost all rated Moderate. Examples:
  - Abiraterone
  - Tramadol
  - Acetazolamide
  - Hydrocortisone
  - Salbutamol
  - Hydrochlorothiazide
  - Amiloride
  - Amiodarone
  - Arsenic trioxide
  - Propofol
  
  Sodium citrate is rated Minor. Several of these drugs, such as the diuretics and corticosteroids, can cause electrolyte shifts, which matters because lactulose may also cause diarrhoea and fluid or electrolyte loss.

Please refer to the package insert for warnings and further safety information. Package insert data were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (Evidence Level L5) and no plausible mechanism. The only local registration is cancelled.

**To proceed, the following is needed:**
- Any independent evidence, such as preclinical or clinical data, linking lactulose to uric acid handling or tumour lysis-related kidney injury. Without it, this prediction should not be pursued.
- Mechanism of action data from DrugBank.
- The Philippine package insert, for warnings and contraindications.
- Confirmation of whether any lactulose product is currently marketed in the Philippines.

**Note on other predictions:** Among the other predictions compiled for lactulose, **obstructive jaundice** (score 99.53%, Evidence Level L3) has the strongest support. It rests on older clinical and experimental studies of lactulose reducing gut-derived endotoxaemia and postoperative renal dysfunction. One of these is a multicentre randomized study (PMID 2032107, 1991). Later reviews describe the renal-protective effect as not conclusively shown. This is better treated as a research question than as a ready candidate, and it would be a more productive direction to evaluate first.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

