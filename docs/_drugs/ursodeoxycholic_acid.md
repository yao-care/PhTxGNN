---
layout: default
title: Ursodeoxycholic Acid
parent: Model Prediction Only (L5)
nav_order: 348
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
monitor_inn: "Ursodeoxycholic acid"
predicted_indications: ["homozygous familial hypercholesterolemia"]
description: "Ursodeoxycholic Acid: predicted new indication Homozygous familial hypercholesterolemia (evidence level L5). Approved use: Not recorded in the local data"
---

# Ursodeoxycholic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Ursodeoxycholic Acid: Homozygous familial hypercholesterolemia
{: .text-alpha }

## One-Sentence Summary

Ursodeoxycholic acid (UDCA) is a bile acid originally used for gallstone disease (cholelithiasis, cholecystolithiasis, choledocholithiasis), primary biliary cholangitis and Reynolds syndrome.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia (HoFH)**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, UDCA is a bile acid used in hepatobiliary disease. Its efficacy in gallstone disease and primary biliary cholangitis is established, and it may act on bile acid and cholesterol handling.

A plausible but unverified rationale is that UDCA affects cholesterol homeostasis. It may reduce intestinal cholesterol absorption, decrease hepatic cholesterol secretion into bile, and modulate bile acid synthesis and FXR signaling. This would link the original indications, which involve cholesterol and bile metabolism, to a lipid disorder.

However, the mechanistic link is weak. HoFH is driven mainly by absent or defective LDL receptor function (LDLR, and less often APOB, PCSK9 or LDLRAP1 variants). Modulating bile acid pathways is unlikely to compensate for the lack of LDL receptor activity. The high score of 0.9986 comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0503 | Ursodeoxycholic Acid | Not specified | Not specified (status: valid) |


---

## Safety Considerations

- **Drug Interactions**: The interaction query was completed, with 100 interactions recorded in total. The 20 retrieved entries include:
  - **Minor**: cyclosporine, aluminum hydroxide, magaldrate
  - **Level unclassified**: cyanocobalamin, calcitriol, folic acid, pravastatin, ramipril, lorazepam, tramadol, fluconazole, oseltamivir, erythromycin, sildenafil, pantoprazole, citalopram, moxifloxacin, nelfinavir, glimepiride, indinavir

  Aluminum-containing antacids are the practical interactions to note among the minor ones, and the unclassified entries need severity review before any use.

For warnings and contraindications, please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials or literature (L5). The mechanistic link is weak, because HoFH stems mainly from defective LDL receptors, which bile acid modulation is unlikely to correct. The only Philippines registration is cancelled, and package insert safety data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines (blocking gap for safety screening)
- Detailed mechanism of action data (MOA) from DrugBank
- The basis of the TxGNN model (deep learning) prediction, to test whether any plausible mechanism exists
- Preclinical or literature evidence of UDCA's effect on LDL cholesterol in familial hypercholesterolemia
- Severity classification of the unclassified drug interactions, especially with statins such as pravastatin
- Clarification of the registration status and available dosage forms in the Philippines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

