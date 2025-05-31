from collections import defaultdict
from typing import List, Dict, Tuple, Set
from src.models.player_result import PlayerResult

def group_players_by_moon(players: List[PlayerResult]) -> Dict[str, List[PlayerResult]]:
    """
    Filter list of PlayerResults to group players by their moon and ensure no duplicates.
    This function filters out players with the same tag and character within the same moon.
    It returns a dictionary where the keys are moon names and the values are lists of PlayerResult objects.

    Args:
        players (list): List of PlayerResult objects.

    Returns:
        dict: A dictionary with moon names as keys and lists of PlayerResult objects as values.
    """
    players_by_moon = defaultdict(list)
    seen: Dict[str, set[Tuple[str, str]]] = defaultdict(set)
    for player in players:
        key = (player.tag, player.character)
        if key not in seen[player.moon]:
            players_by_moon[player.moon].append(player)
            seen[player.moon].add(key)
    return dict(players_by_moon)

def filter_players_by_tag(players: List[PlayerResult]) -> Set[str]:
    """
    Filter players by their tag ensuring each tag only appears once in the output list.

    Args:
        players (list): List of PlayerResult objects.

    Returns:
        list: A list of PlayerResult objects with unique tags.
    """
    seen = set()
    for player in players:
        if player.tag not in seen:
            seen.add(player.tag)
    return seen
