---
layout: default
title: Calcitriol
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 7
---

# Calcitriol
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

# Calcitriol: From Hypoparathyroidism to Hereditary Hypophosphatemic Rickets

## One-Sentence Summary

Calcitriol (1,25-dihydroxyvitamin D₃) is the biologically active form of vitamin D, internationally prescribed for hypoparathyroidism and renal osteodystrophy in which the body's capacity to synthesize active vitamin D is impaired.
The TxGNN model predicts it may be effective for **Hereditary Hypophosphatemic Rickets** — particularly X-linked Hypophosphatemia (XLH) — with **7 clinical trials** and **20 publications** currently supporting this direction.
Although calcitriol is already established as conventional therapy for XLH in many countries, this prediction identifies a formal repurposing pathway for the Philippines market where the drug currently holds no registration.

> **Note on top-ranked prediction:** TxGNN's rank #1 result was "obsolete vitamin D deficiency" (score 99.96%), which returned zero trials and zero literature. This is entirely due to an expired ORDO/HPO ontology term, not a true evidence gap — the mechanistic connection between calcitriol and vitamin D deficiency is self-evident. The report therefore focuses on **rank #7 (Hereditary Hypophosphatemic Rickets)**, which carries the strongest actionable evidence (L2).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no Philippines registration; internationally used for hypoparathyroidism and renal osteodystrophy) |
| Predicted New Indication | Hereditary Hypophosphatemic Rickets (X-linked Hypophosphatemia, XLH) |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L2 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not returned from the DrugBank query for this assessment. Based on well-established pharmacology, Calcitriol is the terminal bioactive metabolite of the vitamin D pathway — produced in the proximal renal tubule from 25-hydroxyvitamin D (calcidiol) by the enzyme CYP27B1 (1α-hydroxylase). It exerts its effects by binding to the nuclear Vitamin D Receptor (VDR), initiating transcriptional programs that govern intestinal calcium and phosphate absorption, renal reabsorption of filtered calcium, PTH secretion from the parathyroid gland, and bone mineralization via osteoblast-osteoclast signaling.

In Hereditary Hypophosphatemic Rickets — primarily X-linked Hypophosphatemia (XLH), caused by loss-of-function mutations in *PHEX* — pathological overproduction of the phosphaturic hormone FGF23 from osteocytes simultaneously drives two deficits: renal phosphate wasting (hyperphosphaturia → chronic hypophosphatemia) and suppression of CYP27B1, resulting in inappropriately low circulating calcitriol despite normal or elevated PTH. Supplementing exogenous calcitriol therefore directly corrects both limbs of the metabolic disturbance — restoring intestinal phosphate absorption efficiency and overcoming the FGF23-mediated block on calcitriol synthesis — which constitutes the mechanistic rationale for its use.

Calcitriol combined with oral neutral phosphate has been the established conventional therapy for XLH for over four decades, documented in landmark NEJM and JCI publications and endorsed in current Lancet reviews as the standard approach in regions where burosumab (the newer anti-FGF23 monoclonal antibody) is unavailable or unaffordable. For the Philippines, where burosumab access is likely constrained by cost, formalizing calcitriol's repurposing pathway addresses a direct and unmet clinical need for this pediatric rare disease population.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|------------|------|--------|-----------|------------|
| [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) | Early Phase 1 | Active, Not Recruiting | 20 | **Calcitriol monotherapy in XLH** — the only registered trial investigating calcitriol alone (without phosphate supplementation) for XLH; assesses serum phosphate, skeletal mineralization, nephrocalcinosis risk, and growth in children over 12 months with dose escalation in the first 3 months |
| [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) | Phase 4 | Unknown | 100 | **High vs. low-dose calcitriol + neutral phosphate in XLH children** — Phase 4 comparative effectiveness trial to establish evidence-based weight-adjusted dosing for active vitamin D metabolites; largest calcitriol-specific trial in the dataset |
| [NCT04846647](https://clinicaltrials.gov/study/NCT04846647) | N/A | Completed | 260 | Observational study of inappropriate FGF23 secretion in hypophosphatemia — enrolls XLH and related genetic forms; confirms calcitriol suppression by FGF23 as the central disease mechanism; largest sample in dataset (n=260) |
| [NCT06046820](https://clinicaltrials.gov/study/NCT06046820) | Phase 3 | Active, Not Recruiting | 27 | Phase 3 trial of INZ-701 in ENPP1 deficiency — calcitriol used as background standard-of-care, confirming its ongoing role as active comparator in the XLH-spectrum trial landscape |
| [NCT01526304](https://clinicaltrials.gov/study/NCT01526304) | N/A | Unknown | 150 | Cross-sectional study of FGF23, Klotho, and Sclerostin in kidney stone formers — provides mechanistic background on the FGF23–calcitriol axis in renal mineral handling |
| [NCT06921720](https://clinicaltrials.gov/study/NCT06921720) | N/A | Not Yet Recruiting | 65 | ³¹P-spectroscopy ATP measurement in phosphate diabetes (XLH) — metabolic imaging study; expected completion May 2027 |
| [NCT00844740](https://clinicaltrials.gov/study/NCT00844740) | N/A | Withdrawn | 0 | Cinacalcet in familial hypophosphatemic rickets — withdrawn before enrollment; trial background explicitly states calcitriol + phosphate as the standard against which alternatives were to be compared |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|--------|------------|
| [39181153](https://pubmed.ncbi.nlm.nih.gov/39181153/) | 2024 | Review | *Lancet* | Definitive XLH review — characterizes FGF23 excess driving calcitriol deficiency; establishes calcitriol + phosphate as conventional therapy and baseline comparator for burosumab trials |
| [40295317](https://pubmed.ncbi.nlm.nih.gov/40295317/) | 2025 | Clinical Review | *Calcified Tissue International* | Current XLH diagnosis and treatment — details calcitriol synthesis suppression by FGF23 and the pharmacological rationale for replacement therapy; most recent clinical guidance |
| [6252463](https://pubmed.ncbi.nlm.nih.gov/6252463/) | 1980 | Clinical Study | *New England Journal of Medicine* | **Landmark RCT-equivalent** — calcitriol vs. ergocalciferol vs. phosphate alone in 11 children with vitamin D-resistant rickets; calcitriol raised serum levels above normal and increased intestinal phosphate absorption, establishing combination therapy |
| [3839245](https://pubmed.ncbi.nlm.nih.gov/3839245/) | 1985 | Clinical Study | *Journal of Clinical Investigation* | High-dose calcitriol (68 ng/kg/day) healed osteomalacia in XLH patients — demonstrated that sustained high calcitriol concentrations are required for osteomalacia reversal beyond rickets healing |
| [36446330](https://pubmed.ncbi.nlm.nih.gov/36446330/) | 2022 | Review | *Hormone Research in Paediatrics* | Comprehensive rickets, vitamin D, and calcium/phosphate metabolism review — historical treatment context from sunshine therapy to calcitriol; authoritative pediatric reference |
| [29292875](https://pubmed.ncbi.nlm.nih.gov/29292875/) | 2017 | Cohort Study | *Pediatric Endocrinology Reviews* | Spontaneous growth and early calcitriol + phosphate therapy effect in XLH — height data from 127 patients at 49 centres; largest real-world growth dataset |
| [35226335](https://pubmed.ncbi.nlm.nih.gov/35226335/) | 2022 | Cohort Study | *J Endocrinological Investigation* | Segmental growth analysis in hereditary hypophosphatemic rickets from birth to adulthood under calcitriol-based therapy — demonstrates persistent leg growth deficit |
| [2492895](https://pubmed.ncbi.nlm.nih.gov/2492895/) | 1989 | Clinical Study | *Calcified Tissue International* | Bone mineral density in 17 children with familial hypophosphatemia after calcitriol + phosphate — longitudinal DXA-like measurements at 6-month intervals |
| [38988138](https://pubmed.ncbi.nlm.nih.gov/38988138/) | 2024 | Review | *J Bone and Mineral Research* | Hypophosphatemic rickets and short stature — current management algorithm including calcitriol-based regimen; pediatric clinical guidance |
| [17117305](https://pubmed.ncbi.nlm.nih.gov/17117305/) | 2006 | Review | *Arq Bras Endocrinol Metab* | Hereditary hypophosphatemic conditions and osteomalacia — pathophysiology of renal phosphate wasting and inappropriately low calcitriol as the shared mechanism across XLH subtypes |

---

## Philippines Market Information

Calcitriol is **not currently registered with the FDA Philippines**. No marketing authorization records exist.

> ⚠️ Access to calcitriol in the Philippines would require a Special Access Permit (SAP) or physician-initiated compassionate use application through the FDA Philippines Drug Access Program.

---

## Safety Considerations

No Philippines-specific package insert data is available due to the absence of local drug registration. Based on internationally established safety information for calcitriol:

- **Hypercalcemia**: The most clinically significant adverse effect; requires regular serum calcium monitoring, particularly during dose titration
- **Nephrocalcinosis**: A recognized long-term complication of high-dose calcitriol use in XLH — renal ultrasound monitoring at 6–12 month intervals is standard practice in XLH management protocols
- **Secondary Hyperparathyroidism**: Documented complication of combined calcitriol + phosphate therapy in XLH; PTH should be monitored alongside calcium

Please refer to the international package insert and DrugBank (DB00136) for complete warnings, contraindications, and drug interaction data.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Calcitriol's role in Hereditary Hypophosphatemic Rickets (XLH) is mechanistically unambiguous and clinically established — it corrects the FGF23-driven calcitriol deficiency that is the biochemical hallmark of the disease. Evidence includes a Phase 4 comparative trial (NCT03820518, n=100), a dedicated calcitriol monotherapy XLH trial (NCT03748966), landmark publications in NEJM (1980) and JCI (1985), and endorsement in a 2024 Lancet disease review. For the Philippines, where burosumab is likely cost-prohibitive, this represents a pharmacologically sound and evidence-supported treatment option for a rare pediatric disease population currently without a registered therapeutic.

**To proceed, the following is needed:**
- **Safety data**: Download and parse calcitriol's international package insert to complete warnings, contraindications, and drug interaction profile (currently blocking S1 safety evaluation)
- **MOA data**: Query DrugBank API for DB00136 to formally document mechanism of action
- **Philippines regulatory pathway**: Identify the most appropriate access mechanism (Special Access Permit vs. compassionate use vs. full registration dossier)
- **Monitoring protocol**: Formalize a Philippines-adapted monitoring plan covering serum calcium, urinary calcium, renal function (eGFR), and renal ultrasound for nephrocalcinosis
- **Combination therapy availability**: Confirm local availability of oral neutral phosphate for standard XLH combination regimen
- **Dosing review**: Determine whether high-dose (NCT03820518 protocol) or calcitriol monotherapy (NCT03748966) approach is preferred based on local clinical infrastructure
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

