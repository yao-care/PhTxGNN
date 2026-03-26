#!/usr/bin/env python3
"""Check Philippine FDA for drug registration information.

Note: The Philippine FDA does not currently provide a public API.
This script provides a framework for future integration when/if
an API becomes available, or for web scraping if permitted.

Current functionality:
- Generates FDA verification URLs for manual checking
- Outputs drug registration status from local PNF data

Usage:
    uv run python scripts/check_pfda.py [--drug DRUG]
    uv run python scripts/check_pfda.py --batch
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

import pandas as pd

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


# Philippine FDA drug database URL (for manual verification)
PFDA_SEARCH_URL = "https://verification.fda.gov.ph/drugprodlist_search.php"


def generate_verification_url(drug: str) -> str:
    """Generate Philippine FDA verification URL for a drug.

    Args:
        drug: Drug name to search

    Returns:
        URL for manual verification
    """
    # Note: This URL structure may change - verify with actual FDA website
    return f"{PFDA_SEARCH_URL}?search={quote(drug)}"


def check_pnf_status(drug: str) -> dict:
    """Check if a drug is in the Philippine National Formulary.

    Args:
        drug: Drug name to check

    Returns:
        PNF status information
    """
    base_dir = Path(__file__).parent.parent
    pnf_path = base_dir / "data" / "raw" / "ph_fda_drugs.json"

    if not pnf_path.exists():
        return {
            "drug": drug,
            "in_pnf": False,
            "error": "PNF data not found. Run process_fda_data.py first.",
        }

    with open(pnf_path, "r", encoding="utf-8") as f:
        pnf_data = json.load(f)

    # Handle both list and dict formats
    if isinstance(pnf_data, dict):
        drugs = pnf_data.get("drugs", [])
    else:
        drugs = pnf_data

    # Search for drug
    drug_upper = drug.upper()
    matches = []

    for d in drugs:
        ingredient = d.get("ingredient", "").upper()
        brand = d.get("brand_name", "").upper()

        if drug_upper in ingredient or drug_upper in brand:
            matches.append(d)

    return {
        "drug": drug,
        "in_pnf": len(matches) > 0,
        "matches": matches,
        "verification_url": generate_verification_url(drug),
    }


def check_single(drug: str) -> dict:
    """Check Philippine FDA status for a single drug.

    Args:
        drug: Drug name

    Returns:
        Status information
    """
    print(f"\nChecking Philippine FDA status for: {drug}")
    print("-" * 60)

    result = check_pnf_status(drug)

    if result["in_pnf"]:
        print(f"Found in Philippine National Formulary (PNF)")
        print(f"Matches: {len(result['matches'])}")
        for match in result["matches"][:5]:
            print(f"  - {match.get('brand_name', 'N/A')} ({match.get('license_id', 'N/A')})")
    else:
        print("Not found in Philippine National Formulary")

    print(f"\nManual verification URL:")
    print(f"  {result['verification_url']}")

    return result


def check_batch() -> list[dict]:
    """Check Philippine FDA status for all repurposing candidate drugs.

    Returns:
        List of results
    """
    base_dir = Path(__file__).parent.parent
    candidates_path = base_dir / "data" / "processed" / "repurposing_candidates.csv.gz"

    if not candidates_path.exists():
        print(f"Error: Candidates file not found: {candidates_path}")
        print("Please run run_kg_prediction.py first.")
        return []

    # Load candidates
    candidates_df = pd.read_csv(candidates_path)
    print(f"Loaded {len(candidates_df)} repurposing candidates")

    # Get unique drugs
    drugs = candidates_df["ingredient"].dropna().unique()
    print(f"Checking {len(drugs)} unique drugs...\n")

    results = []
    pnf_count = 0

    for drug in drugs:
        result = check_pnf_status(drug)
        results.append(result)

        status = "PNF" if result["in_pnf"] else "---"
        print(f"[{status}] {drug}")

        if result["in_pnf"]:
            pnf_count += 1

    print(f"\nSummary:")
    print(f"  Total drugs: {len(drugs)}")
    print(f"  In PNF: {pnf_count} ({pnf_count/len(drugs)*100:.1f}%)")

    # Save results
    output_dir = base_dir / "data" / "evidence"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"pfda_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\nResults saved to: {output_file}")

    # Generate verification URLs file
    urls_file = output_dir / "pfda_verification_urls.txt"
    with open(urls_file, "w", encoding="utf-8") as f:
        f.write("Philippine FDA Drug Verification URLs\n")
        f.write("=" * 60 + "\n\n")
        f.write("Note: Manual verification required - no public API available\n\n")
        for drug in drugs:
            f.write(f"{drug}:\n")
            f.write(f"  {generate_verification_url(drug)}\n\n")

    print(f"Verification URLs saved to: {urls_file}")

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Check Philippine FDA drug registration status"
    )
    parser.add_argument("--drug", type=str, help="Drug name to check")
    parser.add_argument("--batch", action="store_true", help="Check all repurposing candidate drugs")

    args = parser.parse_args()

    print("=" * 60)
    print("Philippine FDA Drug Status Checker")
    print("=" * 60)
    print()
    print("Note: Philippine FDA does not provide a public API.")
    print("This tool checks against local PNF data and provides")
    print("verification URLs for manual checking.")
    print()

    if args.batch:
        check_batch()
    elif args.drug:
        check_single(args.drug)
    else:
        # Demo mode
        print("Demo mode: Checking 'metformin'")
        check_single("metformin")


if __name__ == "__main__":
    main()
