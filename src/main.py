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

    analysis_results = run_analytics(brackets)

    # TODO: Implement further analysis or output of results
    print("Analysis complete.")

if __name__ == "__main__":
    main()
