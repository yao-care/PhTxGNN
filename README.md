# PhTxGNN

Philippines drug repurposing predictions using TxGNN.

## Overview

This project uses TxGNN (Therapeutic Genome Network) knowledge graph to predict potential drug repurposing candidates for approved drugs in the Philippines.

## Installation

```bash
uv sync
```

## Usage

```bash
# Prepare external data (vocabularies)
uv run python scripts/prepare_external_data.py

# Process FDA data
uv run python scripts/process_fda_data.py

# Run knowledge graph prediction
uv run python scripts/run_kg_prediction.py

# Generate FHIR resources
uv run python scripts/generate_fhir_resources.py
```

## Disclaimer

This project is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.
