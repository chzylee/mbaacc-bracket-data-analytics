import sys
from src.csv_reader import load_brackets_from_csv
from src.analytics.analyzer import run_analytics

def main():
    if len(sys.argv) < 2:
        print("Usage: python analytics.py <path_to_csv>")
        sys.exit(1)

    csv_path = sys.argv[1]
    print(f"Loading brackets from {csv_path}...")
    brackets = brackets = load_brackets_from_csv(csv_path)

    # Filter brackets with more than 20 entrants.
    min_20_entrants = [bracket for bracket in brackets if bracket.total_entrants > 20]

    output = run_analytics(brackets)
    # TODO: Uncomment when full analysis is implemented.
    # min_20_entrants_output = run_analytics(min_20_entrants)

    print(output)
    print("Analysis complete.")

    # TODO: implement CSV output functionality.

if __name__ == "__main__":
    main()
