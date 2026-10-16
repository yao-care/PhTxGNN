---
layout: default
title: Propofol
parent: High Evidence (L1-L2)
nav_order: 284
evidence_level: L2
indication_count: 5
last_modified_at: 2026-10-15
description: "Propofol: predicted new indication Migraine disorder (evidence level L2). Approved use: Not recorded in the Philippines license data (general anesthesia/seda…"
monitor_inn: "Propofol"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "Prinzmetal angina", "nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome"]
---

# Propofol
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **5** 
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

# Propofol: From General Anesthesia to Migraine Disorder

## One-Sentence Summary

Propofol is an intravenous anesthetic and sedative agent. No approved indication text is recorded for its single Philippines registration, so the original use is inferred from its known role as a general anesthetic.
The TxGNN model predicts it may be effective for **migraine disorder**, with **3 clinical trials** and **19 publications** currently supporting this direction, including several randomized trials in emergency department settings.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Philippines license data (general anesthesia/sedation is the known use of propofol) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L2 |
| Philippines Market Status | ✗ Cancelled only (no valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Propofol is known to be a GABA-A receptor positive allosteric modulator, and its efficacy as an anesthetic and sedative is well established.

Enhanced GABAergic inhibition may suppress cortical spreading depression and trigeminovascular pain signaling, both central to migraine. A preclinical study showed that propofol hemisuccinate suppresses cortical spreading depression (PMID 22390898), supporting this link. The high TxGNN score is consistent with the clinical signal seen in emergency department studies.

Use at the doses studied is confined to monitored settings such as the emergency department, because of the risks of sedation, respiratory depression, and hypotension.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Phase 2/3 | Completed | 74 | Low-dose propofol as abortive therapy for pediatric migraine in the emergency department; the most directly relevant trial |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | NA | Completed | 40 | Low-dose propofol infusion as an abortive treatment in pediatric migraine; also evaluates safe dosing limits and duration of effect |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | NA | Terminated | 12 | Low-dose propofol for severe refractory migraine in the emergency department; ended early, so little efficacy information |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33070469](https://pubmed.ncbi.nlm.nih.gov/33070469/) | 2021 | RCT | Emerg Med Australas | Propofol vs placebo for early resolution of acute migraine in adult ED patients (double-blind) |
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | RCT | J Emerg Med | Low-dose propofol for pediatric migraine; small studies suggest efficacy with a favorable side-effect profile and possibly shorter length of stay |
| [32705801](https://pubmed.ncbi.nlm.nih.gov/32705801/) | 2020 | Pilot RCT | Emerg Med Australas | Procedural-sedation-dose propofol vs standard therapy for initial migraine management in the ED |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | RCT | Arch Acad Emerg Med | Sumatriptan plus propofol vs sumatriptan alone in acute migraine |
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | RCT | Arch Acad Emerg Med | Propofol + granisetron vs propofol + metoclopramide for symptom management of acute migraine |
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | Systematic Review | Acad Emerg Med | Reviews the safety and efficacy of propofol for acute migraine in the ED; evidence is limited |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guideline | Headache | 2025 American Headache Society update on parenteral drugs for acute migraine in the ED |
| [39364614](https://pubmed.ncbi.nlm.nih.gov/39364614/) | 2024 | Systematic Review / Network Analysis | Headache | Compares parenteral agents for reducing relapse after severe acute migraine |
| [27454834](https://pubmed.ncbi.nlm.nih.gov/27454834/) | 2016 | Review | Expert Rev Neurother | Drug profile of sub-anesthetic propofol in refractory migraine |
| [10759925](https://pubmed.ncbi.nlm.nih.gov/10759925/) | 2000 | Clinical report | Headache | Reports unusual effectiveness of IV propofol in intractable migraine in an outpatient headache center |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0401 (cancelled) | Propofol | Not recorded | Not recorded |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from a drug-disease network, not label text): epilepsy, hypotensive disorder, respiratory failure, intracranial arteriosclerosis, inherited lipid metabolism disorder, familial hyperlipidemia.
- **Drug Interactions**: 100 interactions were found in total. Most listed ones are Moderate, including famotidine, clarithromycin, levofloxacin, morphine, ondansetron, granisetron, dolasetron, cisapride, loperamide, and several laxatives (bisacodyl, lactulose, magnesium citrate, magnesium hydroxide). Metronidazole is rated Minor.
- **Use-setting caution**: Sedation, respiratory depression, and hypotension risks mean use should be limited to monitored settings.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2/3 trial and several randomized trials in the emergency department support propofol for acute migraine, which fits evidence level L2. However, the only Philippines registration is cancelled, the studied use needs monitored care, and the key trial is not a confirmed Phase 3 RCT.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- A valid registration route or product pathway, since the existing license is cancelled
- A protocol limiting use to monitored settings with sedation, respiratory, and blood pressure monitoring
- Review of the knowledge-graph contraindication signals (epilepsy, hypotension, respiratory failure) against patient selection criteria

---

## Other Predicted Indications (Brief)

| Predicted Indication | Evidence Level | Decision | Note |
|------|------|------|------|
| Migraine with brainstem aura | L3 | Research Question | Evidence is extrapolated from general migraine; no subtype-specific trials; caution advised given brainstem effects |
| Prinzmetal angina | L4 | Hold | Only case reports of anesthesia-induced coronary spasm, which suggest a safety signal rather than benefit |
| Nephrogenic syndrome of inappropriate antidiuresis | L5 | Hold | Computational prediction only, with no plausible mechanism evident |
| Tourette syndrome | L4 | Hold | Evidence concerns sedation during deep brain stimulation surgery, not treatment of tics |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

