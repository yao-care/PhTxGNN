---
layout: default
title: Fluoxetine
parent: 僅模型預測 (L5)
nav_order: 148
evidence_level: L5
indication_count: 10
---

# Fluoxetine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Fluoxetine: From Major Depressive Disorder to Schizotypal Personality Disorder

## One-Sentence Summary

Fluoxetine is a well-established selective serotonin reuptake inhibitor (SSRI) widely used for major depression, OCD, panic disorder, and bulimia nervosa.
The TxGNN model ranks **Schizotypal Personality Disorder** as its top predicted new indication (score: 99.92%),
currently supported by **no registered clinical trials** but **11 publications**—primarily open-label and retrospective studies—providing indirect mechanistic and clinical evidence for this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | SSRI antidepressant; established use in major depression, OCD, panic disorder, bulimia nervosa |
| Predicted New Indication | Schizotypal Personality Disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 (observational studies and narrative reviews) |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Fluoxetine is a selective serotonin reuptake inhibitor (SSRI) that potently and selectively blocks the serotonin transporter (SERT), increasing synaptic serotonin concentrations and enhancing serotonergic neurotransmission throughout the central nervous system. Detailed pharmacological data was not available in this evidence pack, but fluoxetine's mechanism is well-characterized through decades of clinical use and published literature—including evidence of long-term 5-HT1A autoreceptor desensitization, BDNF/CREB pathway activation, and hippocampal neurogenesis.

Schizotypal Personality Disorder (ScPD) is a cluster A personality disorder characterized by cognitive-perceptual distortions (magical thinking, ideas of reference), social anxiety, eccentric behavior, and frequent comorbid depression and anxiety. Serotonergic dysregulation has been proposed as one contributing mechanism in ScPD—particularly for its anxiety, impulsivity, and affective symptom dimensions. Fluoxetine's increase in synaptic 5-HT may attenuate social anxiety, reduce affective instability, and address comorbid depression. There is also indirect mechanistic support via 5-HT2A receptor-mediated modulation of quasi-psychotic perceptual symptoms.

However, the core quasi-psychotic features of ScPD (perceptual distortions, referential thinking) are thought to be driven primarily by dopaminergic dysregulation—a pathway not directly targeted by SSRIs. The TxGNN prediction most likely reflects shared phenotypic nodes between ScPD and anxiety or mood disorders where fluoxetine is already established, rather than a direct mechanistic fit to ScPD's full symptom profile. The only prospective clinical data identified is a small 22-patient open-label trial (Markovitz et al., 1991) that enrolled mixed borderline/schizotypal patients, and no dedicated controlled trials exist. The evidence supports further research rather than clinical deployment at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Fluoxetine in Schizotypal Personality Disorder.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [1853957](https://pubmed.ncbi.nlm.nih.gov/1853957/) | 1991 | Open-label trial | Am J Psychiatry | 22-patient 12-week fluoxetine trial in borderline/schizotypal PD; significant reductions in self-injury and Hopkins Symptom Checklist scores, suggesting potential benefit across both diagnoses |
| [9448667](https://pubmed.ncbi.nlm.nih.gov/9448667/) | 1998 | Retrospective cohort | J Clin Psychiatry | Comprehensive psychopharmacology review in borderline and schizotypal PD; no single agent of choice, but SSRIs may benefit selected patients depending on symptom presentation |
| [29955451](https://pubmed.ncbi.nlm.nih.gov/29955451/) | 2016 | Narrative review | Ment Health Clin | Review of pharmacological treatment across all cluster A personality disorders; SSRIs discussed for management of anxiety and affective symptoms in schizotypal PD |
| [8227492](https://pubmed.ncbi.nlm.nih.gov/8227492/) | 1993 | Expert review | J Clin Psychopharmacol | Conceptual framework for pharmacotherapy of personality disorders; reviews SSRI evidence and highlights target-symptom approach in borderline and schizotypal PD |
| [12214786](https://pubmed.ncbi.nlm.nih.gov/12214786/) | 2002 | Clinical cohort | Psychol Med | Personality disorders assessed before and after fluoxetine treatment in depressed outpatients; examines whether PD diagnoses change across antidepressant treatment |
| [9664779](https://pubmed.ncbi.nlm.nih.gov/9664779/) | 1998 | Case report | Psychosomatics | Transient psychosis with psychogenic polydipsia in a schizotypal patient taking fluoxetine—an important safety signal for SSRI use in this population |
| [15209835](https://pubmed.ncbi.nlm.nih.gov/15209835/) | 2004 | Clinical study | Aust NZ J Psychiatry | Personality traits and treatment outcomes compared in bipolar II and major depression; schizotypal features identified as a prognostic factor affecting treatment response |
| [7635854](https://pubmed.ncbi.nlm.nih.gov/7635854/) | 1995 | Clinical study | J Clin Psychiatry | Predictors of SSRI response in OCD; schizotypal features were associated with poorer SSRI treatment outcome—a finding with direct implications for ScPD |
| [33634761](https://pubmed.ncbi.nlm.nih.gov/33634761/) | 2021 | Case report | CNS Neurol Disord Drug Targets | Asenapine treatment for catatonia in a patient with schizotypal PD and COVID-19-related septic shock; illustrates the complexity of pharmacological management in acute ScPD presentations |
| [18805590](https://pubmed.ncbi.nlm.nih.gov/18805590/) | 2009 | Prospective cohort | J Affect Disord | 18-month depression treatment follow-up; personality disorder comorbidity (including schizotypal features) identified as a predictor of relapse and treatment resistance |

---

## Philippines Market Information

Fluoxetine is currently **not registered in the Philippines**. No product authorizations, approved dosage forms, or licensed indications are on record with the Philippine Food and Drug Administration. Any clinical use would require formal regulatory registration prior to deployment.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Additional note:** One case report (PMID [9664779](https://pubmed.ncbi.nlm.nih.gov/9664779/)) documented transient psychosis in a schizotypal patient receiving fluoxetine, suggesting that SSRI-induced behavioral activation or disinhibition may pose particular risks in this population. This should be factored into any future clinical trial design.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The serotonergic mechanism of fluoxetine is biologically plausible for specific symptom dimensions of schizotypal personality disorder—particularly social anxiety, affective instability, and impulsivity—but the core quasi-psychotic symptoms of ScPD are primarily dopamine-driven and fall outside SSRI pharmacological reach. The current evidence base (one small open-label trial plus observational and review literature, zero controlled trials) classifies this as a research question, not a clinically actionable repurposing candidate at this time.

**To proceed, the following is needed:**
- Formal fluoxetine pharmacological profile and adverse event data (resolve Data Gap DG002 via DrugBank API)
- Philippines-specific safety documentation including package insert warnings and contraindications (resolve Data Gap DG001)
- At least one Phase 2, placebo-controlled RCT in patients with a primary schizotypal personality disorder diagnosis, using validated ScPD symptom scales as primary endpoints
- Target symptom clarification: future trials should prespecify whether the intervention targets anxiety/affective dimensions versus core perceptual-cognitive symptoms
- Prospective evaluation of the SSRI-associated psychosis risk signal (PMID 9664779) before proceeding
- **Strategic note:** Other indications predicted in this same evidence pack show substantially stronger evidence—agoraphobia (L2, Proceed with Guardrails), phobic disorder (L2, Proceed with Guardrails), and melancholia (L1, Proceed with Guardrails)—and may represent higher-priority repurposing pathways for fluoxetine in the Philippines market context.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

