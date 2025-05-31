from typing import List, Dict
import src.analytics.filters as filters
from src.models.bracket import Bracket
from src.models.player_result import PlayerResult
from src.analytics.data.character_counts import CharacterCounts, count_character_occurrences
from src.analytics.data.moon_majorities import MoonMajorities, MoonCount, update_moon_majorities
from src.analytics.output import AnalysisOutput

def run_analytics(brackets: List[Bracket]) -> AnalysisOutput:
    moon_majorities = MoonMajorities()
    all_player_results = []

    for bracket in brackets:
        bracket.print_results()
        moon_count = MoonCount() # Init state of moon count for each bracket.
        for result in bracket.top_8_results:
            all_player_results.append(PlayerResult(
                tag=result.tag,
                moon=result.moon,
                character=result.character,
                placement=result.placement
            ))
            moon_count[result.moon] += 1
        update_moon_majorities(moon_count, moon_majorities)

    players_by_moon = filters.group_players_by_moon(all_player_results)
    c_all_players = players_by_moon.get("C", [])
    f_all_players = players_by_moon.get("F", [])
    h_all_players = players_by_moon.get("H", [])

    # Every moon *should* have at least one player, but default to [] if not.
    c_unique_players = filters.filter_players_by_tag(c_all_players)
    f_unique_players = filters.filter_players_by_tag(f_all_players)
    h_unique_players = filters.filter_players_by_tag(h_all_players)

    char_counts = CharacterCounts.from_player_results(all_player_results)
    c_unique_counts = count_character_occurrences(c_unique_players)
    f_unique_counts = count_character_occurrences(f_unique_players)
    h_unique_counts = count_character_occurrences(h_unique_players)

    c_char_representation = filters.filter_unique_players_and_characters(c_all_players)
    f_char_representation = filters.filter_unique_players_and_characters(f_all_players)
    h_char_representation = filters.filter_unique_players_and_characters(h_all_players)

    return AnalysisOutput(
        c_moon_majorities= moon_majorities.c_majorities,
        f_moon_majorities= moon_majorities.f_majorities,
        h_moon_majorities= moon_majorities.h_majorities,
        c_moon_shutouts= moon_majorities.c_shutouts,
        f_moon_shutouts= moon_majorities.f_shutouts,
        h_moon_shutouts= moon_majorities.h_shutouts,
        moon_ties= moon_majorities.ties,
        c_moon_players=[p.tag for p in c_unique_players],
        f_moon_players=[p.tag for p in f_unique_players],
        h_moon_players=[p.tag for p in h_unique_players],
        c_character_totals=char_counts.c_counts,
        f_character_totals=char_counts.f_counts,
        h_character_totals=char_counts.h_counts,
        c_character_counts=c_unique_counts,
        f_character_counts=f_unique_counts,
        h_character_counts=h_unique_counts,
        c_char_representation=c_char_representation,
        f_char_representation=f_char_representation,
        h_char_representation=h_char_representation
    )
