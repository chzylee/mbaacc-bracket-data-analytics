from typing import List, Dict
import src.analytics.filters as filters
from src.models.bracket import Bracket
from src.models.player_result import PlayerResult
from src.analytics.state.moon_majorities import MoonMajorities, MoonCount, update_moon_majorities
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
    # Every moon *should* have at least one player, but default to [] if not.
    c_player_tags = filters.filter_players_by_tag(players_by_moon.get("C", []))
    f_player_tags = filters.filter_players_by_tag(players_by_moon.get("F", []))
    h_player_tags = filters.filter_players_by_tag(players_by_moon.get("H", []))

    return AnalysisOutput(
        c_moon_majorities= moon_majorities.c_majorities,
        f_moon_majorities= moon_majorities.f_majorities,
        h_moon_majorities= moon_majorities.h_majorities,
        c_moon_shutouts= moon_majorities.c_shutouts,
        f_moon_shutouts= moon_majorities.f_shutouts,
        h_moon_shutouts= moon_majorities.h_shutouts,
        moon_ties= moon_majorities.ties,
        c_moon_players=c_player_tags,
        f_moon_players=f_player_tags,
        h_moon_players=h_player_tags
    )

