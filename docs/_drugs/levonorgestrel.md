---
layout: default
title: Levonorgestrel
parent: 僅模型預測 (L5)
nav_order: 205
evidence_level: L5
indication_count: 6
---

# Levonorgestrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Levonorgestrel: From Contraception to Acne

## One-Sentence Summary

Levonorgestrel (LNG) is a synthetic progestogen widely used in hormonal contraception — including oral contraceptive pills, intrauterine systems (IUS), and implants. The TxGNN model predicts it may be effective for **Acne (disease)**, with **5 clinical trials** and **20 publications** retrieved in this direction. However, mechanistic analysis reveals a fundamental paradox: LNG's high intrinsic androgenic activity is more likely to *worsen* acne than improve it, and the clinical evidence to date derives entirely from LNG-containing *combination* oral contraceptives where the co-administered ethinylestradiol (EE) drives the anti-acne effect — not LNG itself.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hormonal contraception (oral, intrauterine, implant) — not registered in the Philippines per this evidence pack |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as Data Gap DG002). Based on established pharmacological knowledge, Levonorgestrel is a 19-nortestosterone-derived synthetic progestogen with **high androgenic potency** — it binds androgen receptors with meaningful affinity, stimulates sebaceous gland secretion, and upregulates 5α-reductase activity. These are precisely the mechanisms that drive acne pathogenesis, not its resolution.

In combined oral contraceptives (COCs) containing both LNG and ethinylestradiol (EE), the EE component raises sex hormone-binding globulin (SHBG), which in turn lowers free circulating androgens. This anti-androgenic net effect is responsible for any observed acne improvement in LNG-containing COC users. The benefit is attributable to EE, not to LNG. Clinical comparative studies (e.g., EE/chlormadinone acetate vs EE/levonorgestrel) consistently show that switching from LNG-containing to anti-androgenic progestin-containing COCs *improves* acne outcomes — implying LNG is the less favourable progestin for acne-prone women.

The TxGNN graph model likely identified LNG's association with acne through its knowledge graph proximity to female hormonal pathways and dermatological outcomes. This is a plausible graph-traversal artefact rather than a direct biological signal. As a standalone treatment for acne — without co-administered EE — LNG presents a mechanistic contradiction. Any further development in this indication would require robust evidence that LNG alone, at therapeutically relevant doses, reduces acne lesion counts without the confounding effect of estrogen.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01650168](https://clinicaltrials.gov/study/NCT01650168) | N/A | Completed | 101,498 | Large prospective cohort comparing NOMAC-E2 COC vs LNG-containing COC for safety; provides comparative dermatological side-effect profiles including skin-related outcomes for LNG-OC users |
| [NCT00480532](https://clinicaltrials.gov/study/NCT00480532) | N/A | Completed | 131 | Doxycycline adjunct to continuous COC to reduce unscheduled bleeding; acne mentioned only as a known doxycycline indication — LNG's independent effect on acne not assessable |
| [NCT05570786](https://clinicaltrials.gov/study/NCT05570786) | Phase 2 | Completed | 100 | RCT of subdermal gestrinone pellet for endometriosis-associated pelvic pain; androgenic progestin context is informative for mechanism but primary endpoint is not acne |
| [NCT00161226](https://clinicaltrials.gov/study/NCT00161226) | N/A | Terminated | 44 | LNG-IUS for endometrial cancer prevention in obese women aged 40–50; trial terminated early; acne noted as a systemic side effect of oral progestins in background — not a therapeutic target |
| [NCT05492487](https://clinicaltrials.gov/study/NCT05492487) | Phase 2 | Unknown | 60 | Mirena (LNG-IUS) vs megestrol for atypical endometrial hyperplasia in fertility-preserving setting; acne data, if any, would only appear in secondary safety endpoints |

> **Note:** None of the identified trials prospectively evaluated LNG as a primary treatment for acne. The closest evidence (NCT01650168) is a comparative safety cohort, not an efficacy trial for acne.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [12196750](https://pubmed.ncbi.nlm.nih.gov/12196750/) | 2002 | RCT | J Am Acad Dermatol | Randomized placebo-controlled trial of EE 20 µg + LNG 100 µg OC for moderate acne; EE/LNG improved biochemical markers of androgenicity, suggesting net anti-androgenic effect of the *combination* — driven by EE-mediated SHBG elevation |
| [6084924](https://pubmed.ncbi.nlm.nih.gov/6084924/) | 1984 | Clinical Study | Acta Derm Venereol | Serum testosterone and SHBG in 54 female acne patients treated with desogestrel/EE or LNG/EE OCs; pretreatment androgen abnormality in 57% of patients; both combinations reduced free testosterone, but the estrogen component is the common driver |
| [15025547](https://pubmed.ncbi.nlm.nih.gov/15025547/) | 2004 | Review | Drugs | EE/chlormadinone acetate was significantly more effective than EE/LNG 0.03/0.15 mg for treating mild-to-moderate papulopustular acne — directly implying LNG is the less favourable progestin for acne management |
| [21895044](https://pubmed.ncbi.nlm.nih.gov/21895044/) | 2011 | Review | Am J Clin Dermatol | EE/chlormadinone acetate for dermatological benefits including acne, hirsutism, and seborrhea; positions anti-androgenic progestins as superior to androgenic progestins like LNG for pilosebaceous disorders |
| [16796485](https://pubmed.ncbi.nlm.nih.gov/16796485/) | 2006 | Review | J Womens Health | Drospirenone (anti-androgenic, antimineralocorticoid) vs LNG and MPA; drospirenone reduces acne and hirsutism while LNG does not — LNG used as the less favourable reference progestin |
| [7825629](https://pubmed.ncbi.nlm.nih.gov/7825629/) | 1995 | Review/Mechanistic | Am J Med | Androgenicity of progestins: 19-nortestosterone-derived progestins (including LNG) retain androgenic receptor binding activity; explains why LNG-containing preparations may worsen androgen-sensitive conditions |
| [14688179](https://pubmed.ncbi.nlm.nih.gov/14688179/) | 2004 | Clinical Study | Hum Reprod | LNG-IUS for endometriosis symptom management; supports LNG's progestogenic efficacy via intrauterine route but is unrelated to acne |
| [32909630](https://pubmed.ncbi.nlm.nih.gov/32909630/) | 2020 | Cochrane Review | Cochrane Database Syst Rev | LNG-IUS for endometrial hyperplasia; comprehensive systematic review confirming LNG's endometrial antiproliferative properties — does not address acne |
| [11727177](https://pubmed.ncbi.nlm.nih.gov/11727177/) | 2001 | Review | Semin Reprod Med | LNG-releasing IUS: mechanisms and clinical outcomes; background reading on LNG pharmacology |
| [10652979](https://pubmed.ncbi.nlm.nih.gov/10652979/) | 1999 | Cohort Study | Hum Reprod Update | VTE risk with LNG-containing COCs vs third-generation progestins; LNG COCs show lower VTE risk — safety context, not acne-specific |

---

## Philippines Market Information

Levonorgestrel is **not registered** in the Philippines according to this evidence pack (0 active licenses, market status: Not Marketed). No product authorization data is available for tabulation.

> Globally, LNG-containing products include emergency contraception (Plan B, Postinor), levonorgestrel-releasing IUS (Mirena, Liletta), and combination oral contraceptives. If Philippine registration status requires verification, a direct query to the Food and Drug Administration Philippines (FDA-PH) online drug database is recommended.

---

## Safety Considerations

Please refer to the package insert for safety information. All safety fields in this evidence pack are flagged as Data Gap (DG001: TFDA package insert warnings/contraindications unavailable; DDI data: not found in query). The following general considerations are relevant based on LNG's pharmacology:

- **Androgenic effects**: Acne, hirsutism, and seborrhea may occur or worsen, particularly with high-dose or progestin-only preparations — this is mechanistically counterproductive to the predicted indication
- **Thromboembolic risk**: LNG-containing COCs are associated with venous thromboembolism, though LNG-containing formulations carry lower VTE risk than some third-generation progestins
- **Hormonal effects**: Irregular bleeding, mood changes, weight changes; breast tenderness

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's prediction of Levonorgestrel for acne treatment is mechanistically contradicted by LNG's well-established androgenic activity — a property that promotes, rather than suppresses, androgen-driven skin pathology. All clinical evidence showing acne improvement derives from LNG *combined* with ethinylestradiol (EE), where EE's SHBG-elevating effect drives the benefit. Comparative studies consistently rank LNG as an *inferior* progestin for acne-prone women relative to anti-androgenic progestins (drospirenone, chlormadinone, cyproterone). The Philippines regulatory pathway is also blocked by zero current registrations.

**To proceed, the following is needed:**
- A clinical study isolating the effect of LNG *alone* (without EE) on acne lesion counts — no such study currently exists
- Mechanistic studies clarifying whether any specific LNG dose or route (e.g., intrauterine, with minimal systemic exposure) could achieve a net anti-androgenic or sebosuppressive effect
- Resolution of Data Gaps DG001 (package insert safety data) and DG002 (complete MOA characterization) before any safety assessment can be completed
- Philippines FDA registration review and local regulatory pathway assessment before any market entry planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

