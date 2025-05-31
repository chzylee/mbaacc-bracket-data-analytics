from dataclasses import dataclass
from typing import Dict, List
from collections import defaultdict
from src.models.player_result import PlayerResult

@dataclass
class CharacterCounts:
    c_counts: Dict[str, int]
    f_counts: Dict[str, int]
    h_counts: Dict[str, int]

    @staticmethod
    def from_player_results(player_results: List[PlayerResult]) -> 'CharacterCounts':
        c_counts = count_character_occurrences([p for p in player_results if p.moon == 'C'])
        f_counts = count_character_occurrences([p for p in player_results if p.moon == 'F'])
        h_counts = count_character_occurrences([p for p in player_results if p.moon == 'H'])
        return CharacterCounts(c_counts=c_counts, f_counts=f_counts, h_counts=h_counts)


def count_character_occurrences(player_results: List[PlayerResult]) -> Dict[str, int]:
    counts = defaultdict(int)
    for player in player_results:
        counts[player.character] += 1

    return dict(counts)
