from typing import List, Dict
import src.analytics.filters as filters
from src.models.bracket import Bracket
from src.models.player_result import PlayerResult
from src.analytics.state.moon_majorities import MoonMajorities, MoonCount, update_moon_majorities


def run_analytics(brackets: List[Bracket]) -> None:
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
            print(f"moon_count[{result.moon}] = {moon_count[result.moon]}")

        print(f"C Moon Count: {moon_count['C']}")
        print(f"F Moon Count: {moon_count['F']}")
        print(f"H Moon Count: {moon_count['H']}")
        update_moon_majorities(moon_count, moon_majorities)

    players_by_moon = filters.group_players_by_moon(all_player_results)
    # Every moon *should* have at least one player, but default to [] if not.
    c_player_tags = filters.filter_players_by_tag(players_by_moon.get("C", []))
    f_player_tags = filters.filter_players_by_tag(players_by_moon.get("F", []))
    h_player_tags = filters.filter_players_by_tag(players_by_moon.get("H", []))

    print(f"C Players ({len(c_player_tags)} total): {c_player_tags}")
    print(f"F Players ({len(f_player_tags)} total): {f_player_tags}")
    print(f"H Players ({len(h_player_tags)} total): {h_player_tags}")

    print(f"Moon Majorities: {moon_majorities}")

