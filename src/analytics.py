import sys
from src.csv_reader import load_brackets_from_csv
from src.models.player_result import PlayerResult
from src.models.bracket import Bracket

def main():
    if len(sys.argv) < 2:
        print("Usage: python analytics.py <path_to_csv>")
        sys.exit(1)

    csv_path = sys.argv[1]
    brackets = brackets = load_brackets_from_csv(csv_path)

    for bracket in brackets:
        print("------------------------------------------------------------------------")
        print(f"{bracket}  Results:")
        print(" | ".join(str(player) for player in bracket.top_8_results))
        print("------------------------------------------------------------------------\n")

if __name__ == "__main__":
    main()
