from typing import List, Dict
from src.models.bracket import Bracket


def run_analytics(brackets: List[Bracket]) -> Dict[str, int]:
    for bracket in brackets:
        print("------------------------------------------------------------------------")
        print(f"{bracket}  Results:")
        print(" | ".join(str(player) for player in bracket.top_8_results))
        print("------------------------------------------------------------------------\n")
