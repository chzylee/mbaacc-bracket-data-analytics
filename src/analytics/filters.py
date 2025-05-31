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
    seen = set()
    for player in players:
        key = (player.tag, player.moon, player.character)
        print(f"Processing player: {player.tag}, Moon: {player.moon}, Character: {player.character}")
        if key not in seen:
            print(f"Adding {player.tag} {player.character} to {player.moon}-moon")
            seen.add(key)
            players_by_moon[player.moon].append(player)
        else:
            print(f"Skipping duplicate player: {player.tag}, Moon: {player.moon}, Character: {player.character}")
    return dict(players_by_moon)

def filter_players_by_tag(players: List[PlayerResult]) -> List[PlayerResult]:
    """
    Filter players by their tag ensuring each tag only appears once in the output list.

    Args:
        players (list): List of PlayerResult objects.

    Returns:
        list: A list of PlayerResult objects with unique tags.
    """
    seen = set()
    unique_players = []
    for player in players:
        if player.tag not in seen:
            seen.add(player.tag)
            unique_players.append(player)
    return unique_players

def filter_unique_players_and_characters(players: List[PlayerResult]) -> List[Tuple[str, str]]:
    """
    Filter players to ensure each player is unique by tag and character.

    Args:
        players (list): List of PlayerResult objects.

    Returns:
        list: List of tuples containing unique player tag and character pairs from the list of players.
    """
    seen = set()
    player_char_pairs = []

    for player in players:
        key = (player.tag, player.moon, player.character)
        if key not in seen:
            seen.add(key)
            full_char_name = f"{player.moon}-{player.character}"
            player_char_pairs.append((player.tag, full_char_name))

    return player_char_pairs
