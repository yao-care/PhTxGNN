#!/usr/bin/env python3
"""Generate news monitoring keywords from repurposing predictions.

Creates keyword patterns for monitoring health news related to
drug repurposing candidates.

Usage:
    uv run python scripts/generate_news_keywords.py

Output:
    data/news/keywords.json
"""

import json
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def load_synonyms(filepath: Path) -> dict:
    """Load disease and drug synonyms.

    Args:
        filepath: Path to synonyms.json

    Returns:
        Synonyms dictionary
    """
    if not filepath.exists():
        return {"indication_synonyms": {}, "drug_synonyms": {}}

    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_drug_patterns(drug: str, drug_synonyms: dict) -> list[str]:
    """Generate search patterns for a drug.

    Args:
        drug: Drug name
        drug_synonyms: Drug synonym dictionary

    Returns:
        List of search patterns
    """
    patterns = [drug.lower()]

    # Add synonyms if available
    drug_lower = drug.lower()
    if drug_lower in drug_synonyms:
        patterns.extend([s.lower() for s in drug_synonyms[drug_lower]])

    return list(set(patterns))


def generate_disease_patterns(disease: str, indication_synonyms: dict) -> list[str]:
    """Generate search patterns for a disease.

    Args:
        disease: Disease name
        indication_synonyms: Disease synonym dictionary

    Returns:
        List of search patterns
    """
    patterns = [disease.lower()]

    # Add synonyms if available
    disease_lower = disease.lower()
    if disease_lower in indication_synonyms:
        patterns.extend([s.lower() for s in indication_synonyms[disease_lower]])

    # Also check partial matches
    for key, synonyms in indication_synonyms.items():
        if key in disease_lower or disease_lower in key:
            patterns.extend([s.lower() for s in synonyms])

    return list(set(patterns))


def main():
    print("=" * 60)
    print("Generate News Monitoring Keywords")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    candidates_path = base_dir / "data" / "processed" / "repurposing_candidates.csv.gz"
    synonyms_path = base_dir / "data" / "news" / "synonyms.json"

    if not candidates_path.exists():
        print(f"Error: Candidates file not found: {candidates_path}")
        print("Please run run_kg_prediction.py first.")
        return

    # Load data
    candidates_df = pd.read_csv(candidates_path)
    print(f"Loaded {len(candidates_df)} repurposing candidates")

    synonyms = load_synonyms(synonyms_path)
    print(f"Loaded synonyms for {len(synonyms.get('indication_synonyms', {}))} diseases")
    print(f"Loaded synonyms for {len(synonyms.get('drug_synonyms', {}))} drugs")

    # Extract unique drugs and diseases
    drugs = candidates_df["ingredient"].dropna().unique()
    diseases = candidates_df["potential_indication"].dropna().unique()

    print(f"\nUnique drugs: {len(drugs)}")
    print(f"Unique diseases: {len(diseases)}")

    # Generate keywords
    keywords = {
        "generated_at": datetime.now().isoformat(),
        "description": "News monitoring keywords for PhTxGNN drug repurposing",
        "statistics": {
            "total_drugs": len(drugs),
            "total_diseases": len(diseases),
            "total_pairs": len(candidates_df),
        },
        "drugs": {},
        "diseases": {},
        "pairs": [],
    }

    # Drug keywords
    print("\nGenerating drug keywords...")
    drug_synonyms = synonyms.get("drug_synonyms", {})
    for drug in drugs:
        patterns = generate_drug_patterns(drug, drug_synonyms)
        keywords["drugs"][drug] = {
            "patterns": patterns,
            "count": len(patterns),
        }

    # Disease keywords
    print("Generating disease keywords...")
    indication_synonyms = synonyms.get("indication_synonyms", {})
    for disease in diseases:
        patterns = generate_disease_patterns(disease, indication_synonyms)
        keywords["diseases"][disease] = {
            "patterns": patterns,
            "count": len(patterns),
        }

    # Generate pair-specific patterns (top 100 most common)
    print("Generating pair keywords...")
    pair_counts = candidates_df.groupby(["ingredient", "potential_indication"]).size()
    top_pairs = pair_counts.sort_values(ascending=False).head(100)

    for (drug, disease), count in top_pairs.items():
        drug_patterns = keywords["drugs"].get(drug, {}).get("patterns", [drug.lower()])
        disease_patterns = keywords["diseases"].get(disease, {}).get("patterns", [disease.lower()])

        # Create combined search queries
        queries = []
        for dp in drug_patterns[:3]:  # Limit combinations
            for dsp in disease_patterns[:3]:
                queries.append(f'"{dp}" AND "{dsp}"')

        keywords["pairs"].append({
            "drug": drug,
            "disease": disease,
            "queries": queries[:5],  # Limit to 5 queries
        })

    # Save keywords
    output_dir = base_dir / "data" / "news"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "keywords.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(keywords, f, indent=2, ensure_ascii=False)

    print(f"\nKeywords saved to: {output_file}")

    # Print summary
    print()
    print("Summary:")
    print(f"  Drug patterns: {sum(len(d['patterns']) for d in keywords['drugs'].values())}")
    print(f"  Disease patterns: {sum(len(d['patterns']) for d in keywords['diseases'].values())}")
    print(f"  Pair queries: {len(keywords['pairs'])}")

    # Print sample
    print()
    print("Sample drug keywords:")
    for drug in list(keywords["drugs"].keys())[:3]:
        patterns = keywords["drugs"][drug]["patterns"][:5]
        print(f"  {drug}: {patterns}")

    print()
    print("Sample disease keywords:")
    for disease in list(keywords["diseases"].keys())[:3]:
        patterns = keywords["diseases"][disease]["patterns"][:5]
        print(f"  {disease}: {patterns}")


if __name__ == "__main__":
    main()
