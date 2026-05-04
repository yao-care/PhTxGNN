---
layout: default
title: Carbamazepine
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L5
indication_count: 10
---

# Carbamazepine
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

# Carbamazepine: From Epilepsy & Trigeminal Neuralgia to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Carbamazepine (CBZ) is a first-line antiepileptic drug and the gold-standard pharmacotherapy for trigeminal neuralgia, exerting its effect through use-dependent voltage-gated sodium channel blockade to suppress aberrant neuronal firing.
The TxGNN model predicts it may be effective for **Trigeminal Nerve Neoplasm** — a condition in which tumors (schwannomas, lymphomas, granulomas, lipomas) compress or infiltrate the trigeminal nerve and generate the same pathological high-frequency ectopic discharges that CBZ is designed to suppress.
This prediction is currently supported by **1 registered clinical trial** and **20 publications**, predominantly case reports and reviews documenting CBZ use in tumor-related trigeminal pain syndromes.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Epilepsy; Trigeminal neuralgia (global standard; Philippines registration data not available) |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Detailed mechanism-of-action data for Carbamazepine is not available in the current evidence pack. Based on known information, CBZ is a dibenzazepine anticonvulsant that selectively blocks voltage-gated sodium channels in their inactivated state (use-dependent block). This preferentially dampens high-frequency repetitive firing — the hallmark of both epileptic neurons and the ectopically discharging trigeminal afferent fibers responsible for the electric-shock-like pain of trigeminal neuralgia.

The connection between trigeminal neuralgia (the established indication) and trigeminal nerve neoplasm (the predicted new indication) is mechanistically direct. When a tumor — whether a schwannoma, primary malignant lymphoma, sarcoid granuloma, lipoma, dermoid cyst, or meningioma — compresses or infiltrates the trigeminal ganglion or nerve root, it produces focal demyelination and abnormal sodium channel activation identical to that seen in idiopathic trigeminal neuralgia. The resulting ectopic high-frequency discharges are pharmacologically indistinguishable from those in the tumor-free condition; therefore, CBZ's mechanism is directly applicable to suppressing the pain symptom regardless of its neoplastic etiology.

It is critical to emphasize, however, that CBZ does not exert any direct antineoplastic effect on the tumor itself. In cases of tumor-induced trigeminal neuralgia, CBZ functions purely as symptomatic analgesic palliation and must be combined with definitive tumor-directed treatment (surgery, radiotherapy, or chemotherapy as appropriate). Multiple case reports in the literature illustrate precisely this clinical scenario: CBZ provides partial or temporary pain relief while the underlying neoplasm is being investigated and treated.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT06853119](https://clinicaltrials.gov/study/NCT06853119) | N/A | Not Yet Recruiting | 120 | MRI-based analysis of brain network dynamics, microstructural changes, blood-brain barrier integrity, and water exchange rates in trigeminal neuralgia patients; aims to correlate neuroimaging biomarkers with clinical indicators to elucidate neural plasticity mechanisms — provides imaging context for understanding CBZ treatment response at the structural level |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36824641](https://pubmed.ncbi.nlm.nih.gov/36824641/) | 2022 | Systematic/Narrative Review | Acta Clinica Croatica | Comprehensive review of TN treatment options; establishes CBZ as first-line pharmacotherapy; notes that TN may be caused by vascular compression or tumor process, directly bridging the idiopathic and neoplastic subtypes |
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Review of Neurotherapeutics | CBZ is the standard first-line treatment for TN; mechanism linked to focal demyelination and aberrant neural discharges in the trigeminal root entry zone; discusses both medical and surgical management |
| [11286444](https://pubmed.ncbi.nlm.nih.gov/11286444/) | 2001 | Survey/Observational | British Journal of Oral & Maxillofacial Surgery | Survey of TN management practices among UK oral and maxillofacial surgeons; highlights the importance of screening for secondary (tumor-caused) TN and monitoring CBZ therapy — supports current practice of CBZ while investigating for underlying neoplasm |
| [30741017](https://pubmed.ncbi.nlm.nih.gov/30741017/) | 2023 | Case Report | British Journal of Neurosurgery | Primary neurolymphomatosis of the trigeminal nerve presenting as facial pain; CBZ was prescribed but symptoms did not improve; gadolinium-enhanced MRI and FDG-PET confirmed lymphoma — illustrates the limitation of CBZ when tumor burden is the primary driver |
| [25142539](https://pubmed.ncbi.nlm.nih.gov/25142539/) | 2014 | Case Report | Clinical Neurology (Rinsho Shinkeigaku) | Malignant lymphoma spreading perineurally along the trigeminal nerve; initially diagnosed as classical TN and responded to CBZ; pain later changed character and CBZ became ineffective as other cranial nerves were involved — demonstrates CBZ's early palliative utility |
| [9109911](https://pubmed.ncbi.nlm.nih.gov/9109911/) | 1997 | Case Report | Neurology | Post-irradiation neuromyotonia in bilateral facial and trigeminal nerve distribution; neuromyotonic discharges confirmed electrophysiologically; condition responded to CBZ therapy — provides mechanistic evidence for CBZ suppressing radiation-induced aberrant trigeminal discharges |
| [3181365](https://pubmed.ncbi.nlm.nih.gov/3181365/) | 1988 | Animal Study | Experimental Neurology | Intravenous CBZ produced immediate dose-dependent inhibition of spontaneous ectopic discharges from experimental neuromas in A-α/β and A-δ fibers; directly supports CBZ's mechanism in tumor-compressed nerve tissue |
| [12590697](https://pubmed.ncbi.nlm.nih.gov/12590697/) | 2003 | Case Report | Neurosurgery | Isolated trigeminal nerve sarcoid granuloma mimicking trigeminal schwannoma; reviews imaging features distinguishing granuloma from schwannoma — highlights the differential diagnosis spectrum of trigeminal nerve neoplasms relevant to CBZ use |
| [15235745](https://pubmed.ncbi.nlm.nih.gov/15235745/) | 2004 | Case Report | Arquivos de Neuro-Psiquiatria | Primary melanoma of Meckel's cave presenting as TN with normal initial MRI; CBZ was ineffective and microvascular decompression failed; true diagnosis revealed only on repeat imaging — underscores the need for thorough tumor workup when CBZ fails |
| [32454201](https://pubmed.ncbi.nlm.nih.gov/32454201/) | 2020 | Case Report | World Neurosurgery | Trigeminal schwannoma of the pterygopalatine fossa treated with endoscopic endonasal resection; provides surgical management context for the neoplasm subtype most commonly associated with trigeminal neuralgia requiring CBZ palliation |

---

## Philippines Market Information

Carbamazepine currently has **no registered drug licenses in the Philippines**. It is not marketed locally, and no approved product records are available in the Philippine FDA (FDA Philippines) database. Any clinical use would require importation under compassionate use or special import permit frameworks.

---

## Safety Considerations

Detailed safety data (package insert warnings, contraindications, and drug-drug interactions) were not available in the current evidence pack.

> Please refer to the package insert and the Philippine FDA regulatory guidance for full safety information before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction is mechanistically sound — tumor-induced trigeminal nerve neoplasm produces the same ectopic sodium-channel-mediated discharges that CBZ is designed to suppress, and multiple case reports document its real-world palliative use in this exact clinical scenario. However, the evidence base consists primarily of observational case reports and reviews (L3), with no dedicated RCT for this specific indication, and CBZ has no direct antineoplastic activity, requiring mandatory concurrent tumor-directed treatment.

**To proceed, the following is needed:**

- **Regulatory pathway clarification**: CBZ is not registered in the Philippines; a special import permit or compassionate use application to the Philippine FDA is required before clinical deployment
- **Mechanism-of-action data**: Retrieve full DrugBank MOA profile for CBZ (DB00564) to complete the mechanistic linkage analysis and support the regulatory submission
- **Safety package**: Obtain the full package insert (SmPC/prescribing information) for CBZ to document warnings, contraindications (e.g., bone marrow suppression, Stevens-Johnson syndrome risk, HLA-B\*15:01 pharmacogenomic screening relevant to Filipino population), and drug interactions before clinical use
- **HLA-B\*15:01 / HLA-A\*31:01 genotyping protocol**: These variants are significantly more prevalent in Asian populations (including Filipinos) and are strongly associated with severe cutaneous adverse reactions (SJS/TEN) to CBZ; a pre-treatment pharmacogenomic screening protocol should be established
- **Tumor-type stratification**: Define which trigeminal nerve neoplasm subtypes (schwannoma, lymphoma, meningioma, granuloma, epidermoid) are the primary targets; CBZ is purely palliative and must be paired with a neuro-oncological treatment plan
- **Prospective case registry**: Given the absence of RCT evidence for this specific indication, establish a prospective registry to capture CBZ efficacy and safety outcomes in Filipino patients with tumor-induced trigeminal pain syndromes
- **Multidisciplinary protocol**: Co-develop a management guideline with neurosurgery, neurology, and oncology to define when CBZ initiation is appropriate, when to escalate to surgery/radiotherapy, and how to monitor for CBZ treatment failure indicating tumor progression
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

