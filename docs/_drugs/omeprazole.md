---
layout: default
title: Omeprazole
parent: 僅模型預測 (L5)
nav_order: 261
evidence_level: L5
indication_count: 2
---

# Omeprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Omeprazole: From Acid-Related GI Disorders to Duodenogastric Reflux

## One-Sentence Summary

Omeprazole is a proton pump inhibitor (PPI), widely recognized as a first-line treatment for acid-related gastrointestinal conditions including peptic ulcer disease, GERD, and *Helicobacter pylori* eradication regimens.
The TxGNN model predicts it may be effective for **Duodenogastric Reflux**,
with **1 clinical trial** and **20 publications** currently supporting this direction — though the mechanistic picture is mixed and carries an unresolved safety signal regarding cancer risk potentiation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Peptic ulcer / GERD / *H. pylori* eradication (standard pharmacological use; no Philippines FDA registration on file) |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L3 |
| Philippines Market Status | Not Registered |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this Evidence Pack. Based on known pharmacology, Omeprazole is the archetypal H⁺/K⁺-ATPase inhibitor, suppressing gastric acid secretion by irreversibly blocking the final common step of acid production in gastric parietal cells. It is an established first-line agent for peptic ulcer disease, gastroesophageal reflux disease (GERD), and triple-therapy *H. pylori* eradication regimens.

Duodenogastric reflux (DGR) refers to the retrograde flow of duodenal contents — primarily bile acids and pancreatic enzymes — into the stomach. While Omeprazole cannot directly block bile reflux (which is alkaline by nature), it has been hypothesized to reduce overall mucosal damage in mixed acid-bile reflux by lowering the acid component, and has been studied particularly in Barrett's esophagus patients where both acid and bile exposure contribute to disease progression. Clinical observational data (PMID 9824338, PMID 10994616) confirm that omeprazole does reduce DGR to some extent, though the bile component persists.

However, the mechanistic case cuts both ways. Animal model studies (PMID 10389684, PMID 33027361) raise a specific concern: gastric acid suppression combined with DGR may **potentiate** gastric carcinogenesis, likely by altering intragastric microbiome composition and promoting nitrosamine formation in an alkaline, bile-rich environment. This unresolved tension — modest acid-pathway benefit versus potential cancer-risk promotion — is the primary basis for a **Hold** recommendation until human RCT data clarifies the risk-benefit balance in this specific indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT02685150](https://clinicaltrials.gov/study/NCT02685150) | N/A | Completed | 157 | Diagnostic imaging study using Endoscopic Tri-Modal Imaging (NBI/AFI/WLI) to differentiate functional dyspepsia from reflux disease (acid and bile reflux). No interventional Omeprazole treatment arm; provides indirect evidence on DGR characterization but does not assess therapeutic benefit. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|------------|
| [9824338](https://pubmed.ncbi.nlm.nih.gov/9824338/) | 1998 | Prospective RCT-like | *Gut* | Omeprazole 20 mg BID reduces both duodenogastric and gastro-oesophageal bile reflux in Barrett's oesophagus; DGR decreased but not eliminated — key evidence that PPIs modulate but do not abolish bile reflux. |
| [10994616](https://pubmed.ncbi.nlm.nih.gov/10994616/) | 2000 | Prospective Observational | *Scand J Gastroenterol* | Long-term omeprazole may reduce antral DGR in Barrett's patients; however, the resulting high intragastric pH may paradoxically increase cytotoxicity of remaining duodenal refluxate on foregut mucosa. |
| [16641575](https://pubmed.ncbi.nlm.nih.gov/16641575/) | 2006 | Prospective Cohort (Pediatric) | *J Pediatr Gastroenterol Nutr* | PPI therapy (omeprazole-based) reduces oesophageal bile reflux in children with refractory symptoms; supports use as part of DGR management in paediatric populations. |
| [11552908](https://pubmed.ncbi.nlm.nih.gov/11552908/) | 2001 | Prospective Comparative | *Aliment Pharmacol Ther* | Pantoprazole (PPI class) effectively reduces acid reflux but has limited impact on the bile component of DGR in oesophagitis patients — highlights the class-wide limitation of PPIs against bile reflux. |
| [9841990](https://pubmed.ncbi.nlm.nih.gov/9841990/) | 1998 | Prospective Comparative | *J Gastrointest Surg* | Medical acid suppression reduces acid exposure but not bile reflux in Barrett's esophagus; Nissen fundoplication proved superior for controlling the bile component, suggesting surgery may be needed for full DGR management. |
| [11232672](https://pubmed.ncbi.nlm.nih.gov/11232672/) | 2001 | Observational | *Am J Gastroenterol* | PPI therapy normalizes acid but not bile reflux in Barrett's esophagus; combined acid+bile exposure correlates with severity of mucosal disease, reinforcing the partial-efficacy argument for PPIs in DGR. |
| [19491829](https://pubmed.ncbi.nlm.nih.gov/19491829/) | 2009 | Observational | *Am J Gastroenterol* | GERD patients failing once-daily PPI showed significantly higher duodenogastroesophageal reflux (DGER) than responders; identifies DGER as a distinct mechanism of PPI treatment failure. |
| [33027361](https://pubmed.ncbi.nlm.nih.gov/33027361/) | 2020 | Animal (Rat Model) | *Acta Cir Bras* | Omeprazole did not protect against gastric adenocarcinoma induced by DGR in rats; raises concern about the interaction between acid suppression and bile-induced carcinogenesis in the DGR context. |
| [10389684](https://pubmed.ncbi.nlm.nih.gov/10389684/) | 1999 | Animal (Rat Model) | *Dig Dis Sci* | Gastric acid blockade with omeprazole combined with DGR produced significantly higher gastric carcinoma rates than DGR alone in rats — the primary preclinical safety signal against this repurposing direction. |
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | *Eur J Clin Pharmacol* | Comprehensive PPI pharmacokinetics and clinical use review; confirms class-wide indication for acid-related disorders while noting limitations in non-acid reflux components. |

---

## Philippines Market Information

No Philippines FDA registrations are on file for Omeprazole in this dataset.

> **Note:** This likely represents a data gap rather than true non-availability. Omeprazole is a WHO Essential Medicine and is commercially available in most global markets. A manual verification against the Philippine FDA online drug registration database (www.fda.gov.ph) is strongly recommended before drawing any conclusions about local market status.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Critical signal from preclinical literature:** Animal studies (PMID 10389684, PMID 33027361) specifically demonstrate that omeprazole in the setting of duodenogastric reflux may **promote rather than prevent** gastric carcinogenesis. This is mechanistically plausible (alkaline stomach + altered microbiome → nitrosamine formation) and has not been definitively refuted in human data. This signal is a deciding factor in the Hold recommendation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Omeprazole can partially reduce the acid component of mixed reflux, but it does not address bile reflux — the primary driver of DGR pathology — and preclinical evidence raises a credible, unresolved concern that acid suppression combined with DGR may potentiate gastric carcinogenesis. The available human evidence is limited to observational studies in Barrett's esophagus patients (not DGR as a primary endpoint), which is insufficient to define a positive risk-benefit ratio for this specific repurposing direction.

**To proceed, the following is needed:**
- Philippines FDA registration status verification via manual database search
- Mechanism of action data retrieval from DrugBank API (currently a data gap)
- Human clinical trial data specifically targeting DGR as a primary endpoint with Omeprazole (no such trial currently registered)
- Human observational data addressing the carcinogenesis safety signal identified in rat models — particularly long-term PPI use in populations with confirmed DGR
- Clarification of the dose and treatment duration required to achieve clinically meaningful DGR reduction in humans
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

