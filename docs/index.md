---
layout: default
title: Home
nav_order: 1
---

# PhTxGNN Drug Repurposing Reports

Philippine drug repurposing predictions using TxGNN knowledge graph.

{: .warning }
> **Disclaimer**: These predictions are for research purposes only. They do not constitute medical advice and require clinical validation before any clinical application.

## Overview

PhTxGNN analyzes drugs from the Philippine National Formulary (PNF) using the TxGNN knowledge graph to identify potential new therapeutic uses for existing medications.

### Key Statistics

| Metric | Value |
|--------|-------|
| PNF Drugs Analyzed | 529 |
| DrugBank Mapping Rate | 85.4% |
| Drug-Indication Pairs | 3,322 |
| Unique Drugs with Indications | 338 |
| Unique Diseases | 880 |

## Data Sources

- **Philippine National Formulary (PNF)**: Essential Medicines List, 8th Edition (2022)
- **TxGNN Knowledge Graph**: Drug-disease relationship predictions
- **DrugBank**: Drug identifier mapping

## Quick Links

- [FHIR API](/fhir/metadata) - Access predictions via FHIR R4 API
- [SMART App](/smart/launch.html) - Launch SMART on FHIR application

## How It Works

1. **Drug Extraction**: Extract drug names from PNF-EML 2022
2. **DrugBank Mapping**: Map drug names to standard DrugBank identifiers
3. **TxGNN Prediction**: Use knowledge graph to find potential indications
4. **FHIR Export**: Generate FHIR R4 resources for interoperability

## Contact

For questions or feedback, please open an issue on GitHub.

---

*Last updated: {{ site.time | date: "%Y-%m-%d" }}*
