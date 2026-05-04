---
layout: default
title: Desmopressin
parent: 僅模型預測 (L5)
nav_order: 100
evidence_level: L5
indication_count: 7
---

# Desmopressin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Desmopressin: From Diabetes Insipidus to Inherited Platelet Release Disorders

> **Multi-Indication Report** — This evaluation covers 7 TxGNN-predicted indications for Desmopressin (DB00035). Recommendations differ substantially across predictions; please read each indication section carefully.

---

## One-Sentence Summary

Desmopressin (DDAVP) is a synthetic vasopressin analogue with well-established clinical roles in central diabetes insipidus, nocturnal enuresis, and hemostatic management of mild hemophilia A and von Willebrand disease type 1.

The TxGNN model predicts potential utility across **7 rare inherited bleeding and coagulation disorders**, with the strongest actionable signal for **primary release disorder of platelets** (Evidence Level L3, 15 publications including a 2023 systematic review) and additional research interest for **Glanzmann thrombasthenia** (L3, 20 publications).

Of the remaining 5 predictions, **4 are Hold** due to mechanistic mismatches or insufficient evidence, and **1 carries an active safety warning** — Desmopressin is likely contraindicated in pseudo-von Willebrand disease, where its release of high-molecular-weight vWF multimers may paradoxically worsen platelet consumption.

---

## Quick Overview

**Drug Information**

| Item | Content |
|------|---------|
| Drug (INN) | Desmopressin (DDAVP) |
| DrugBank ID | DB00035 |
| Known Clinical Uses | Central diabetes insipidus, nocturnal enuresis, mild hemophilia A, von Willebrand disease type 1 (hemostatic) |
| Philippines Market Status | Not marketed |
| Number of Philippines Registrations | 0 |

**TxGNN Prediction Summary — All 7 Indications**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|---------------------|-------------|----------------|----------------|
| 1 | Congenital prothrombin deficiency | 99.70% | L4 | Hold |
| 2 | Inherited thrombophilia | 99.44% | L4 | Hold — Safety Concern |
| 3 | Glanzmann thrombasthenia | 99.30% | L3 | Research Question |
| **4** | **Primary release disorder of platelets** | **99.26%** | **L3** | **Proceed with Guardrails** |
| 5 | Pseudo-von Willebrand disease | 99.16% | L4 | Hold — Potential Contraindication |
| 6 | Scott syndrome | 99.16% | L5 | Hold |
| 7 | Flood factor deficiency | 99.15% | L4 | Hold — Unclear Disease Entity |

---

## Why is This Prediction Reasonable?

Desmopressin is a selective agonist of the V2 receptor (AVPR2) expressed on vascular endothelial cells. Binding triggers rapid exocytosis of Weibel-Palade bodies, releasing stored von Willebrand factor (vWF) — particularly ultra-large, high-molecular-weight (HMW) multimers — and Factor VIII into circulation. Plasma vWF rises 2–5 fold within 30–60 minutes, and the released HMW multimers dramatically enhance platelet adhesion to damaged vascular surfaces by bridging the platelet GPIb-IX-V receptor complex to exposed subendothelial collagen. This dual mechanism — amplified platelet adhesion and elevated FVIII — is why DDAVP is already a first-line treatment for mild hemophilia A and vWD type 1.

The **strongest repurposing case** in this dataset is for **primary release disorder of platelets** (Rank 4). Patients with delta-storage pool disease, aspirin-like cyclooxygenase defects, or α-granule ADP/serotonin insufficiency have platelets that adhere normally but fail to release granule contents after activation, impairing secondary platelet plug consolidation. Desmopressin's burst of HMW vWF multimers strengthens the upstream, granule-independent adhesion pathway (GPIb-vWF axis), partially compensating for the downstream release failure and measurably shortening the bleeding time. This mechanism is directly confirmed in pediatric aspirin-like defect patients (PMID 21509710) and in a broader platelet dysfunction cohort (PMID 1613990), and is endorsed by a 2023 systematic review (PMID 36656570).

For **Glanzmann thrombasthenia** (Rank 3), the mechanism is weaker but not implausible: GT results from deficient or dysfunctional GPIIb/IIIa (αIIbβ3 integrin), abolishing platelet aggregation but leaving GPIb-mediated adhesion intact. Desmopressin, by boosting HMW vWF, can enhance GPIb-dependent adhesion as a partial compensatory route. Multiple management guidelines include DDAVP as a secondary adjunct for mild bleeding in GT, though no RCT has been conducted. In contrast, the high TxGNN scores for **congenital prothrombin deficiency** (Rank 1) and **inherited thrombophilia** (Rank 2) appear to reflect broad knowledge graph proximity within a "bleeding/coagulation disorder" cluster rather than true drug-disease mechanistic relevance: Factor II deficiency operates through the extrinsic/common coagulation pathway that DDAVP cannot correct, and inherited thrombophilia is a hypercoagulable state where Desmopressin's pro-adhesion, pro-coagulant properties could actively precipitate thrombotic events — a risk documented in the literature (PMID 16460464).

---

## Clinical Trial Evidence

Only one clinical trial was retrieved across all 7 predicted indications. It has been assessed as **Grade C (not relevant)**: the trial drug is Emicizumab, not Desmopressin, and the target population is mild hemophilia A, not any of the 7 predicted indications.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04567511](https://clinicaltrials.gov/study/NCT04567511) | Phase 4 | Recruiting | 20 | Emicizumab in mild hemophilia A (FVIII 5–30%), evaluating coagulation parameters, joint health, and quality of life. **The trial drug is Emicizumab, not Desmopressin; the disease is mild hemophilia A, not congenital prothrombin deficiency. This appears to be a knowledge graph retrieval error and provides no evidence for this drug-disease pair.** |

No registered clinical trials were found evaluating Desmopressin in any of the 7 predicted indications.

---

## Literature Evidence

Literature was retrieved for all 7 indications. The tables below prioritize the two most actionable predictions.

### Rank 4: Primary Release Disorder of Platelets — Proceed with Guardrails

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36656570](https://pubmed.ncbi.nlm.nih.gov/36656570/) | 2023 | Systematic Review | Eur J Haematol | Confirms DDAVP efficacy in platelet function disorders; also active in mild hemophilia A, vWD, uremia, and liver disease. Flags hyponatremia and rare arterial thrombosis as complications. |
| [21509710](https://pubmed.ncbi.nlm.nih.gov/21509710/) | 2011 | Clinical Observational Study | Klin Padiatr | Direct evaluation of DDAVP on primary hemostasis in pediatric patients with aspirin-like defect (hereditary thrombocytopathy); documents shortening of bleeding time via whole-blood platelet function diagnostics. |
| [23051555](https://pubmed.ncbi.nlm.nih.gov/23051555/) | 2013 | Mechanistic Clinical Study | Haemophilia | DDAVP increases VWF bound to platelet-derived microparticles, suggesting a VWF/FVIII-independent hemostatic mechanism relevant to platelet release disorders. |
| [30986390](https://pubmed.ncbi.nlm.nih.gov/30986390/) | 2019 | Clinical Practice Guideline | Gastroenterology | AGA guideline on coagulation in cirrhosis; contextualizes DDAVP use in settings of mixed platelet and hemostatic dysfunction. |
| [1613990](https://pubmed.ncbi.nlm.nih.gov/1613990/) | 1992 | Clinical Study | Nihon Rinsho | Japanese study of DDAVP in 11 patients with platelet dysfunction including release defects; demonstrates bleeding time shortening and evidence for bypassing the granule release step. |
| [22726100](https://pubmed.ncbi.nlm.nih.gov/22726100/) | 2012 | Review | Haemophilia | Comprehensive review of inherited platelet disorders; discusses DDAVP as an adjunct option for storage pool diseases and release defects including delta-SPD. |
| [18278172](https://pubmed.ncbi.nlm.nih.gov/18278172/) | 2008 | Review | Thromb Haemost | Reviews congenital platelet dysfunction; identifies vWF-GPIb axis as a potential compensatory target when platelet granule release is impaired. |
| [7819105](https://pubmed.ncbi.nlm.nih.gov/7819105/) | 1994 | Clinical Study | Br J Haematol | High-shear platelet aggregation (vWF-dependent) in a congenital ADP receptor defect patient; supports the rationale for vWF-mediated compensation in ADP-release disorders. |

### Rank 3: Glanzmann Thrombasthenia — Research Question

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10509036](https://pubmed.ncbi.nlm.nih.gov/10509036/) | 1999 | Clinical Study | Haematologica | Direct in vitro and in vivo assessment of DDAVP on platelet function; demonstrates partial hemostatic benefit via pathways independent of GPIIb/IIIa in GT patients. |
| [19967146](https://pubmed.ncbi.nlm.nih.gov/19967146/) | 2009 | Clinical Guideline / Consensus | Thromb Haemost | Expert consensus on GT management; lists DDAVP as an adjunct option for mild bleeding or surgical prophylaxis, prior to platelet transfusion. |
| [22726101](https://pubmed.ncbi.nlm.nih.gov/22726101/) | 2012 | Review / Guideline | Haemophilia | Treatment guideline for inherited platelet disorders; notes DDAVP as a potential adjunct to reduce platelet transfusion requirements in GT. |
| [16444446](https://pubmed.ncbi.nlm.nih.gov/16444446/) | 2006 | Case Report | Clin Appl Thromb Hemost | GT patient undergoing dental extraction: DDAVP alone was insufficient, but rFVIIa administered after DDAVP achieved adequate hemostasis — defines DDAVP's role as an adjunct, not monotherapy. |
| [1785670](https://pubmed.ncbi.nlm.nih.gov/1785670/) | 1991 | Clinical Study | Am J Pediatr Hematol Oncol | DDAVP + ethamsylate in 12 patients with marked bleeding time prolongation including 1 GT patient; synergistic bleeding time shortening observed in combined administration. |

---

## Philippines Market Information

Desmopressin is **not currently registered with the Food and Drug Administration (FDA) of the Philippines**. No product authorizations were identified.

| Item | Detail |
|------|--------|
| Total FDA Philippines Registrations | 0 |
| Market Status | Not marketed |
| Available Routes of Administration | None (local data) |
| International Reference | Available in other markets as DDAVP (Sanofi), Minirin (Ferring), and Stimate; formulations include intranasal spray, IV injection, oral tablets, and sublingual tablets |
| Access Pathway | Import registration or compassionate use application would be required for Philippines patient access |

---

## Safety Considerations

Formal package insert warnings and contraindications were not retrieved in this evidence pack. The following safety signals are derived from the collected literature and are critical for clinical decision-making:

- **Hyponatremia**: Desmopressin activates V2 receptors in the renal collecting duct, increasing water reabsorption and diluting serum sodium. Risk is highest in children, elderly patients, and those with excessive fluid intake. Serum sodium monitoring is mandatory with any DDAVP dosing regimen (PMID 36656570).
- **Contraindication in Pseudo-von Willebrand Disease (Rank 5)**: Platelet-type VWD (PT-VWD) involves GPIbα gain-of-function mutations causing excessive binding affinity for HMW vWF multimers. Desmopressin releases exactly these multimers, potentially triggering paradoxical platelet consumption, thrombocytopenia worsening, and increased bleeding risk. This is a mechanistic contraindication supported by case series evidence (PMID 27819553).
- **Risk of Thrombosis in Thrombophilic Conditions (Rank 2)**: DDAVP's pro-coagulant and pro-adhesion actions are inherently dangerous in hypercoagulable states. PMID 16460464 documents TTP exacerbation following DDAVP administration in a patient with inherited thrombotic thrombocytopenic purpura (Upshaw-Schulman syndrome). Use in patients with Factor V Leiden, prothrombin G20210A, or Protein C/S deficiency should be avoided or approached only with specialist oversight.
- **Tachyphylaxis**: Repeated DDAVP dosing depletes endothelial vWF stores; hemostatic efficacy diminishes markedly with doses given within 24–48 hours of each other. Spacing requirements must be built into any treatment protocol.
- **Arterial Thrombotic Events**: Rare cases of myocardial infarction and stroke have been reported, particularly in elderly patients or those with pre-existing cardiovascular disease (PMID 36656570).

---

## Conclusion and Next Steps

This multi-indication evaluation yields tiered recommendations. The actionable finding is confined to Rank 4; the remaining predictions require either a hold or further research justification.

---

### Rank 4: Primary Release Disorder of Platelets

**Decision: Proceed with Guardrails**

**Rationale:**
A 2023 systematic review (PMID 36656570) and multiple clinical observational studies confirm that Desmopressin shortens bleeding time in inherited platelet release disorders by augmenting GPIb-mediated adhesion as a compensatory mechanism — a plausible, clinically documented pathway that supports proceeding to a structured feasibility evaluation.

**To proceed, the following is needed:**
- Retrieve full DrugBank MOA profile and package insert safety data to close data gaps DG001 and DG002
- Identify patients with confirmed platelet release disorder diagnoses (delta-SPD or aspirin-like defect) via specialist haematology referral
- Design a supervised DDAVP challenge protocol with pre/post bleeding time measurement to establish individual patient response
- Implement serum sodium monitoring (baseline + 4–8 hours post-dose) in all trial patients
- Pursue Philippines FDA registration or compassionate use pathway before clinical use

---

### Rank 3: Glanzmann Thrombasthenia

**Decision: Research Question**

**Rationale:**
Multiple haematology guidelines acknowledge DDAVP as a secondary adjunct in GT for mild bleeding or peri-procedural prophylaxis, but the evidence base is limited to observational studies, case reports, and expert consensus. No RCT exists. A prospectively designed case series or n-of-1 trial design through an international rare disease registry would be the appropriate next step.

**To proceed, the following is needed:**
- Systematic literature review specifically evaluating DDAVP adjunct versus platelet transfusion alone in GT
- Collaboration with international GT registries (e.g., Platelet Immunology Workshop, EUHANET)
- Pre-specified hemostatic response endpoints (bleeding time, ROTEM/TEG parameters, clinical hemostasis)

---

### Ranks 1, 6, and 7: Congenital Prothrombin Deficiency / Scott Syndrome / Flood Factor Deficiency

**Decision: Hold**

**Rationale:**
- **Rank 1 (Congenital prothrombin deficiency)**: Desmopressin has no mechanism to correct Factor II deficiency. The high TxGNN score reflects knowledge graph node proximity within a broad bleeding disorder cluster, not a genuine drug-disease mechanistic link. The only retrieved trial was for an entirely different drug (Emicizumab). No further evaluation is warranted.
- **Rank 6 (Scott syndrome)**: The defect in TMEM16F (phospholipid scramblase) preventing phosphatidylserine membrane exposure has no mechanistic intersection with the vWF/FVIII axis. DDAVP cannot compensate for absent procoagulant phospholipid surface. Only one peripheral review paper was retrieved; no direct DDAVP evidence exists.
- **Rank 7 (Flood factor deficiency)**: This is not a recognized disease entity in ICD-11, OMIM, or OrphaNet. The term likely reflects a knowledge graph alignment error — possibly a typographical variant of "blood/coagulation factor deficiency." The sole retrieved literature concerns von Willebrand disease. The disease entity must be clarified before any evaluation can proceed; if the intended target is vWD type 1, Desmopressin already holds established approval for that indication elsewhere.

---

### Rank 2: Inherited Thrombophilia

**Decision: Hold — Active Safety Concern**

**Rationale:**
Desmopressin's pro-coagulant mechanism is directly counterproductive in hypercoagulable states. Literature documents TTP exacerbation following DDAVP in inherited thrombotic thrombocytopenic purpura (PMID 16460464). This prediction reflects a serious mechanistic contradiction and should not be pursued.

---

### Rank 5: Pseudo-von Willebrand Disease

**Decision: Hold — Potential Contraindication**

**Rationale:**
Desmopressin's release of HMW vWF multimers directly triggers excessive platelet consumption through the pathologically overactive GPIbα receptor in PT-VWD. This creates a paradoxical worsening of thrombocytopenia and bleeding — the opposite of the intended therapeutic effect. Clinical literature supports treating this as a contraindication until prospective safety data demonstrate otherwise.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

