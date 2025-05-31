import sys
import src.analytics.filters as filters
from src.csv_reader import load_brackets_from_csv
from src.analytics.analyzer import run_analytics

def main():
    if len(sys.argv) < 2:
        print("Usage: python analytics.py <path_to_csv>")
        sys.exit(1)

    csv_path = sys.argv[1]
    print(f"Loading brackets from {csv_path}...")
    brackets = brackets = load_brackets_from_csv(csv_path)

    min_20_entrants = filters.get_brackets_with_over_20_entrants(brackets)

    full_analysis = run_analytics(brackets)
    min_20_entrants_analysis = run_analytics(min_20_entrants)

    # TODO: Implement further analysis or output of results
    print("Analysis complete.")

if __name__ == "__main__":
    main()
