import sys
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
    brackets = brackets = load_brackets_from_csv(csv_path)

    # Filter brackets with more than 20 entrants.
    min_20_entrants = [bracket for bracket in brackets if bracket.total_entrants >= 20]

    output = run_analytics(brackets)
    min_20_entrants_output = run_analytics(min_20_entrants)

    print(output)
    print(min_20_entrants_output)
    print("Analysis complete.")

    # Write output to CSV
    write_csv_output(output, output_dir)

    if min_20_entrants_output:
        write_csv_output(min_20_entrants_output, output_dir, "20-min-entrants")

if __name__ == "__main__":
    main()
