#!/usr/bin/env python3
"""Check ClinicalTrials.gov for clinical trial evidence.

Queries ClinicalTrials.gov API for clinical trials related to
drug repurposing candidates.

Usage:
    uv run python scripts/check_clinicaltrials.py [--drug DRUG] [--disease DISEASE]
    uv run python scripts/check_clinicaltrials.py --batch

Examples:
    uv run python scripts/check_clinicaltrials.py --drug metformin --disease cancer
    uv run python scripts/check_clinicaltrials.py --batch --limit 10
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from phtxgnn.collectors.clinicaltrials import ClinicalTrialsCollector


def check_single(drug: str, disease: str | None = None) -> dict:
    """Check ClinicalTrials.gov for a single drug-disease pair.

    Args:
        drug: Drug name
        disease: Disease name (optional)

    Returns:
        Search results
    """
    collector = ClinicalTrialsCollector(max_results=20)
    result = collector.search(drug, disease)

    print(f"\nSearching ClinicalTrials.gov for: {drug}" + (f" + {disease}" if disease else ""))
    print("-" * 60)

    if not result.success:
        print(f"Error: {result.error_message}")
        return result.to_dict()

    trials = result.data
    print(f"Found {len(trials)} clinical trials\n")

    for i, trial in enumerate(trials[:10], 1):
        print(f"{i}. [{trial['id']}] {trial['title'][:80]}...")
        print(f"   Phase: {trial['phase']} | Status: {trial['status']}")
        print(f"   Country: {trial['country']} | Enrollment: {trial['enrollment']}")
        print(f"   URL: {trial['url']}")
        print()

    return result.to_dict()


def check_batch(limit: int = 50) -> list[dict]:
    """Check ClinicalTrials.gov for all repurposing candidates.

    Args:
        limit: Maximum number of candidates to check

    Returns:
        List of results
    """
    base_dir = Path(__file__).parent.parent
    candidates_path = base_dir / "data" / "processed" / "repurposing_candidates.csv"

    if not candidates_path.exists():
        print(f"Error: Candidates file not found: {candidates_path}")
        print("Please run run_kg_prediction.py first.")
        return []

    # Load candidates
    candidates_df = pd.read_csv(candidates_path)
    print(f"Loaded {len(candidates_df)} repurposing candidates")

    # Get unique drug-disease pairs
    pairs = candidates_df[["ingredient", "potential_indication"]].drop_duplicates()
    pairs = pairs.head(limit)
    print(f"Checking {len(pairs)} unique drug-disease pairs...\n")

    collector = ClinicalTrialsCollector(max_results=10)
    results = []
    trials_found = 0

    for i, row in pairs.iterrows():
        drug = row["ingredient"]
        disease = row["potential_indication"]

        print(f"[{len(results)+1}/{len(pairs)}] {drug} + {disease}...", end=" ")

        result = collector.search(drug, disease)
        results.append(result.to_dict())

        if result.success and result.data:
            n_trials = len(result.data)
            trials_found += n_trials
            print(f"Found {n_trials} trials")
        else:
            print("No trials found")

    print(f"\nTotal: {trials_found} trials found across {len(pairs)} queries")

    # Save results
    output_dir = base_dir / "data" / "evidence"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"clinicaltrials_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False, default=str)

    print(f"\nResults saved to: {output_file}")

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Check ClinicalTrials.gov for clinical trial evidence"
    )
    parser.add_argument("--drug", type=str, help="Drug name to search")
    parser.add_argument("--disease", type=str, help="Disease name to search")
    parser.add_argument("--batch", action="store_true", help="Check all repurposing candidates")
    parser.add_argument("--limit", type=int, default=50, help="Max candidates to check in batch mode")

    args = parser.parse_args()

    print("=" * 60)
    print("ClinicalTrials.gov Evidence Checker")
    print("=" * 60)

    if args.batch:
        check_batch(args.limit)
    elif args.drug:
        check_single(args.drug, args.disease)
    else:
        # Demo mode
        print("\nDemo mode: Searching for 'metformin + cancer'")
        check_single("metformin", "cancer")


if __name__ == "__main__":
    main()
