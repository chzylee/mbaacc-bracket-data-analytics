import sys
import src.bracket_filters as filters
from src.csv.csv_reader import load_brackets_from_csv
from src.csv.csv_writer import write_csv_output
from src.analytics.analyzer import run_analytics

def main():
    if len(sys.argv) < 2:
        print("Usage: python analytics.py <path_to_csv>")
        sys.exit(1)

    csv_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "csv-output"

    print(f"Loading brackets from {csv_path}...")
    brackets = load_brackets_from_csv(csv_path)

    # Filter brackets with more than 20 entrants.
    min_20_entrants_brackets = filters.get_brackets_with_min_20_entrants(brackets)
    # Get just top 4 results from brackets with more than 20 entrants.
    notable_top_4_brackets = filters.brackets_with_top_4_results(min_20_entrants_brackets)

    output = run_analytics(brackets)
    min_20_entrants_output = run_analytics(min_20_entrants_brackets)
    top_4_output = run_analytics(notable_top_4_brackets)

    print(output)
    print(min_20_entrants_output)
    print(top_4_output)
    print("Analysis complete.")

    # Write output to CSV
    write_csv_output(brackets, output, output_dir, "all-brackets")
    write_csv_output(min_20_entrants_brackets, min_20_entrants_output, output_dir, "20-min-entrants")
    write_csv_output(notable_top_4_brackets, top_4_output, output_dir, "notable-top-4")

if __name__ == "__main__":
    main()
