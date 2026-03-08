#!/usr/bin/env python3
"""Generate FHIR R4 Resources

Generate FHIR format resource files from prediction results.

Usage:
    uv run python scripts/generate_fhir_resources.py

Prerequisites:
    Run run_kg_prediction.py first

Output:
    docs/fhir/metadata
    docs/fhir/MedicationKnowledge/*.json
    docs/fhir/ClinicalUseDefinition/*.json
"""

import json
import re
from datetime import datetime
from pathlib import Path

import pandas as pd


# Philippine configuration
BASE_URL = "https://phtxgnn.github.io"

JURISDICTION = {
    "coding": [{
        "system": "urn:iso:std:iso:3166",
        "code": "PH",
        "display": "Philippines"
    }]
}


def slugify(text: str) -> str:
    """Convert text to URL-safe slug."""
    # Convert to lowercase and replace spaces/special chars with hyphens
    slug = text.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)  # Remove multiple hyphens
    slug = slug.strip("-")
    return slug[:100]  # Limit length


def generate_capability_statement() -> dict:
    """Generate CapabilityStatement (metadata)."""
    return {
        "resourceType": "CapabilityStatement",
        "id": "phtxgnn-fhir-server",
        "url": f"{BASE_URL}/fhir/metadata",
        "version": "1.0.0",
        "name": "PhTxGNNFHIRServer",
        "title": "PhTxGNN FHIR Server",
        "status": "active",
        "experimental": True,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "publisher": "PhTxGNN Project",
        "description": "Philippine drug repurposing predictions using TxGNN knowledge graph",
        "kind": "instance",
        "fhirVersion": "4.0.1",
        "format": ["json"],
        "rest": [{
            "mode": "server",
            "resource": [
                {
                    "type": "MedicationKnowledge",
                    "interaction": [{"code": "read"}, {"code": "search-type"}],
                    "searchParam": [
                        {"name": "code", "type": "token"},
                        {"name": "status", "type": "token"}
                    ]
                },
                {
                    "type": "ClinicalUseDefinition",
                    "interaction": [{"code": "read"}, {"code": "search-type"}],
                    "searchParam": [
                        {"name": "type", "type": "token"},
                        {"name": "subject", "type": "reference"}
                    ]
                }
            ]
        }]
    }


def generate_medication_knowledge(
    drug_name: str,
    drugbank_id: str,
    evidence_level: str = "L5"
) -> dict:
    """Generate MedicationKnowledge resource."""
    slug = slugify(drug_name)
    return {
        "resourceType": "MedicationKnowledge",
        "id": slug,
        "meta": {
            "profile": [f"{BASE_URL}/fhir/StructureDefinition/phtxgnn-medication"]
        },
        "status": "active",
        "code": {
            "coding": [
                {
                    "system": "https://www.drugbank.ca/drugs",
                    "code": drugbank_id,
                    "display": drug_name
                },
                {
                    "system": f"{BASE_URL}/drugs",
                    "code": slug,
                    "display": drug_name
                }
            ],
            "text": drug_name
        },
        "intendedJurisdiction": [JURISDICTION],
        "extension": [{
            "url": f"{BASE_URL}/fhir/StructureDefinition/evidence-level",
            "valueCode": evidence_level
        }]
    }


def generate_clinical_use_definition(
    drug_name: str,
    drugbank_id: str,
    indication: str,
    evidence_level: str = "L5"
) -> dict:
    """Generate ClinicalUseDefinition resource."""
    drug_slug = slugify(drug_name)
    indication_slug = slugify(indication)
    resource_id = f"{drug_slug}-{indication_slug}"

    return {
        "resourceType": "ClinicalUseDefinition",
        "id": resource_id,
        "meta": {
            "profile": [f"{BASE_URL}/fhir/StructureDefinition/phtxgnn-indication"]
        },
        "type": "indication",
        "status": "active",
        "subject": [{"reference": f"MedicationKnowledge/{drug_slug}"}],
        "indication": {
            "diseaseSymptomProcedure": {
                "concept": {
                    "coding": [{
                        "system": "http://snomed.info/sct",
                        "display": indication
                    }],
                    "text": indication
                }
            }
        },
        "extension": [
            {
                "url": f"{BASE_URL}/fhir/StructureDefinition/evidence-level",
                "valueCode": evidence_level
            },
            {
                "url": f"{BASE_URL}/fhir/StructureDefinition/prediction-source",
                "valueString": "TxGNN Knowledge Graph"
            }
        ]
    }


def main():
    print("=" * 60)
    print("Generate FHIR R4 Resources")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    fhir_dir = base_dir / "docs" / "fhir"

    # Create directories
    (fhir_dir / "MedicationKnowledge").mkdir(parents=True, exist_ok=True)
    (fhir_dir / "ClinicalUseDefinition").mkdir(parents=True, exist_ok=True)

    # 1. Generate CapabilityStatement
    print("1. Generating CapabilityStatement...")
    metadata = generate_capability_statement()
    with open(fhir_dir / "metadata", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    print("   Saved: docs/fhir/metadata")

    # 2. Load prediction results
    print("\n2. Loading prediction results...")
    candidates_path = base_dir / "data" / "processed" / "repurposing_candidates.csv"

    if not candidates_path.exists():
        print(f"   Prediction results not found: {candidates_path}")
        print("   Please run run_kg_prediction.py first")
        return

    candidates = pd.read_csv(candidates_path)
    print(f"   Loaded {len(candidates)} predictions")

    # 3. Generate MedicationKnowledge
    print("\n3. Generating MedicationKnowledge resources...")

    # Get unique drugs with their DrugBank IDs
    drugs_df = candidates[["ingredient", "drugbank_id"]].drop_duplicates()
    drugs_df = drugs_df[drugs_df["drugbank_id"].notna()]

    for _, row in drugs_df.iterrows():
        drug_name = row["ingredient"]
        drugbank_id = row["drugbank_id"]

        resource = generate_medication_knowledge(drug_name, drugbank_id)
        slug = slugify(drug_name)
        filepath = fhir_dir / "MedicationKnowledge" / f"{slug}.json"

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(resource, f, indent=2, ensure_ascii=False)

    print(f"   Generated {len(drugs_df)} MedicationKnowledge resources")

    # 4. Generate ClinicalUseDefinition
    print("\n4. Generating ClinicalUseDefinition resources...")
    count = 0

    for _, row in candidates.iterrows():
        drug_name = row.get("ingredient", "")
        drugbank_id = row.get("drugbank_id", "")
        indication = row.get("potential_indication", "")

        if drug_name and drugbank_id and indication:
            resource = generate_clinical_use_definition(
                drug_name, drugbank_id, indication
            )

            drug_slug = slugify(drug_name)
            indication_slug = slugify(indication)
            filename = f"{drug_slug}-{indication_slug}.json"
            filepath = fhir_dir / "ClinicalUseDefinition" / filename

            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(resource, f, indent=2, ensure_ascii=False)
            count += 1

    print(f"   Generated {count} ClinicalUseDefinition resources")

    # 5. Generate summary index
    print("\n5. Generating index...")
    index = {
        "resourceType": "Bundle",
        "id": "phtxgnn-index",
        "type": "collection",
        "timestamp": datetime.now().isoformat(),
        "total": len(drugs_df) + count,
        "entry": [
            {"resource": {"resourceType": "MedicationKnowledge", "count": len(drugs_df)}},
            {"resource": {"resourceType": "ClinicalUseDefinition", "count": count}}
        ]
    }
    with open(fhir_dir / "index.json", "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    print()
    print("=" * 60)
    print("Done!")
    print("=" * 60)
    print()
    print(f"FHIR resources saved to: {fhir_dir}")
    print()
    print("Summary:")
    print(f"  - MedicationKnowledge: {len(drugs_df)}")
    print(f"  - ClinicalUseDefinition: {count}")
    print()
    print("DISCLAIMER: These predictions are for research purposes only.")
    print("They do not constitute medical advice and require clinical validation.")


if __name__ == "__main__":
    main()
