from typing import List
from src.models.bracket import Bracket

def get_brackets_with_min_20_entrants(brackets: List[Bracket]) -> List[Bracket]:
    """
    Filters the list of brackets to only include those with at least 20 entrants.

    Args:
        brackets (list): List of Bracket objects.

    Returns:
        list: Filtered list of Bracket objects with at least 20 entrants.
    """
    return [bracket for bracket in brackets if bracket.total_entrants >= 20]

def brackets_with_top_4_results(brackets: List[Bracket]) -> List[Bracket]:
    """
    Returns a copy of list of brackets with all results filtered to only include top 4 results.

    Args:
        brackets (list): List of Bracket objects.

    Returns:
        list: Filtered list of Bracket objects with top 4 results.
    """
    filtered_brackets = [
        Bracket(
            name=bracket.name,
            date=bracket.date,
            total_entrants=bracket.total_entrants,
            finalists_results=[r for r in bracket.finalists_results if 1 <= r.placement <= 4]
        )
        for bracket in brackets
    ]
    return filtered_brackets
