from dataclasses import dataclass
from typing import Dict, List
from collections import defaultdict
from src.models.player_result import PlayerResult

@dataclass
class PlayerPlacementCount:
    tag: str
    character: str
    placement: int
    count: int

def count_player_placements(player_results: List[PlayerResult]) -> List[PlayerPlacementCount]:
    """
    Counts the number of placements for each player and character combination.
    Characters are identified by their moon and character name.

    Args:
        player_results (List[PlayerResult]): List of PlayerResult objects.

    Returns:
        List[PlayerPlacementCount]: List of PlayerPlacementCount objects with counts.
    """
    counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

    for player in player_results:
        full_char_name = f"{player.moon}-{player.character}"
        counts[player.tag][full_char_name][player.placement] += 1

    result = []
    for tag, char_dict in counts.items():
        for character, placement_dict in char_dict.items():
            for placement, count in placement_dict.items():
                result.append(PlayerPlacementCount(tag=tag, character=character, placement=placement, count=count))

    return result


@dataclass
class PlayerCount:
    tag: str
    character: str
    count: int

def count_player_occurrences(player_results: List[PlayerResult]) -> List[PlayerCount]:
    """
    Counts the number of occurrences for each player and character combination.
    Characters are identified by their moon and character name.

    Args:
        player_results (List[PlayerResult]): List of PlayerResult objects.

    Returns:
        List[PlayerCount]: List of PlayerCount objects with counts.
    """
    counts = defaultdict(lambda: defaultdict(int))

    for player in player_results:
        full_char_name = f"{player.moon}-{player.character}"
        counts[player.tag][full_char_name] += 1

    result = []
    for tag, char_dict in counts.items():
        for character, count in char_dict.items():
            result.append(PlayerCount(tag=tag, character=character, count=count))

    return result
