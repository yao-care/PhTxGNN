---
layout: default
title: Delamanid
parent: Model Prediction Only (L5)
nav_order: 101
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Delamanid: predicted new indication Tuberculosis, bovine (evidence level L5). Approved use: Multidrug-resistant tuberculosis"
---

# Delamanid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Delamanid: From Multidrug-Resistant Tuberculosis to Bovine Tuberculosis

## One-Sentence Summary

Delamanid was originally used to treat multidrug-resistant tuberculosis (MDR-TB).
The TxGNN model predicts it may be effective for **bovine tuberculosis** (a *Mycobacterium bovis* infection), but there are **0 clinical trials** and only **1 publication**, which is a molecular epidemiology survey and not a delamanid study.
The evidence is currently model prediction only, so this candidate is on hold.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multidrug-resistant tuberculosis |
| Predicted New Indication | Tuberculosis, bovine |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 (see the note below) |
| Philippines Market Status | Cancelled only (registration cancelled) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

*Note: The evidence level for the top prediction is L4 as compiled for this report. The data contain no trials and no delamanid-specific studies for it, so in practice the support is close to prediction only.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. The following is based on the mechanistic assessment in that data. Delamanid is a nitro-dihydro-imidazooxazole prodrug. It is activated inside *M. tuberculosis* by the Ddn enzyme (deazaflavin-dependent nitroreductase) and inhibits mycolic acid synthesis, which disrupts the cell wall.

Bovine tuberculosis is caused by *Mycobacterium bovis*, a member of the *M. tuberculosis* complex. Mycolic acid synthesis is conserved across this complex, so activity is biologically plausible. However, the data contain no delamanid-specific susceptibility or clinical data for *M. bovis*. *M. bovis* is also intrinsically resistant to pyrazinamide, which matters when building combination regimens.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for bovine tuberculosis.

*Other predicted indications:* One trial relates to "inactive tuberculosis" (rank 3). [NCT05766267](https://clinicaltrials.gov/study/NCT05766267) (Phase 2/3, active, not recruiting, 288 participants) is the CRUSH-TB study of short-course regimens in pulmonary TB. It studies active pulmonary TB, not latent or inactive TB. It is only indirectly relevant to the predicted indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39487429](https://pubmed.ncbi.nlm.nih.gov/39487429/) | 2024 | Cohort | BMC Genomics | Whole-genome sequencing of *M. bovis* isolates from zoonotic TB to characterize genotypes, virulence and drug resistance. It is not a delamanid study. |

---

## Philippines Market Information

The only registration is cancelled. No dosage form, manufacturer or approved indication text is recorded for it.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0134 | Delamanid | Not recorded | Not recorded (status: cancelled) |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, and the mechanism is plausible because *M. bovis* belongs to the *M. tuberculosis* complex. However, there are no trials, no delamanid-specific data, and no mechanism of action or safety data in the compiled records. In the Philippines the only registration has been cancelled.

**To proceed, the following is needed:**
- Delamanid susceptibility (MIC) data for *M. bovis* isolates
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications from DOH-FDA Philippines
- Clarification of the cancelled registration status and the product's availability in the Philippines
- Any clinical or case-level data on delamanid use in *M. bovis* disease

---

### Other Predicted Indications (Brief Notes)

| Predicted Indication | Evidence Level | Notes |
|------|------|------|
| Tuberculous ascites | L5 | No trials or literature. Penetration into peritoneal fluid is unknown. |
| Inactive tuberculosis | L2 | One Phase 2/3 trial, but it studies active pulmonary TB and the record does not confirm that delamanid is in the regimen. Latent infection is not directly tested. Suggested as a research question. |
| Tuberculosis, avian | L5 | *M. avium* complex is not expected to respond reliably to delamanid. No supporting data. |
| Tuberculoma | L4 | Only a general neurotuberculosis review. CNS penetration is not demonstrated. |
| Allergic urticaria | L5 | No credible mechanistic link. Likely a spurious prediction. |
| Cutaneous tuberculosis | L4 | References concern adverse drug reactions to anti-TB therapy, not treatment with delamanid. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

