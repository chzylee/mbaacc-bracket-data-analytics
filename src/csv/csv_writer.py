import csv
import os
from datetime import datetime
from typing import List
from src.models.bracket import Bracket
from src.analytics.output import AnalysisOutput

def write_brackets_to_csv(brackets: List[Bracket], output_filepath: str):
    if not brackets:
        print("No brackets to write to CSV.")
        return

    header = [
        "Bracket Name", "Date", "Total Entrants",
        "1st Tag", "1st Moon", "1st Char",
        "2nd Tag", "2nd Moon", "2nd Char",
        "3rd Tag", "3rd Moon", "3rd Char",
        "4th Tag", "4th Moon", "4th Char",
        "5th Tag 1", "5th Moon 1", "5th Char 1",
        "5th Tag 2", "5th Moon 2", "5th Char 2",
        "7th Tag 1", "7th Moon 1", "7th Char 1",
        "7th Tag 2", "7th Moon 2", "7th Char 2"
    ]

    with open(output_filepath, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for bracket in brackets:
            row = [
                bracket.name,
                bracket.date,
                bracket.total_entrants,
            ]
            # Add each placement's data in order
            # Ensure you have exactly 8 PlayerResult objects in the correct order
            for i in range(8):
                if i < len(bracket.finalists_results):
                    player = bracket.finalists_results[i]
                    row.extend([player.tag, player.moon, player.character])
                else:
                    row.extend(["", "", ""])
            writer.writerow(row)


def write_player_placement_counts_to_csv(player_placement_counts: dict, output_filepath: str):
    if not player_placement_counts:
        print("No player placement counts to write to CSV.")
        return

    players = player_placement_counts.get("Player Tag", [])
    characters = player_placement_counts.get("Character", [])
    placements = player_placement_counts.get("Placement", [])
    counts = player_placement_counts.get("Count", [])

    with open(output_filepath, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(list(player_placement_counts.keys()))
        for row in zip(players, characters, placements, counts):
            writer.writerow(row)


def write_player_char_counts_to_csv(player_char_counts: dict, output_filepath: str):
    if not player_char_counts:
        print("No player occurrences to write to CSV.")
        return

    players = player_char_counts.get("Player Tag", [])
    characters = player_char_counts.get("Character", [])
    counts = player_char_counts.get("Count", [])

    with open(output_filepath, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(list(player_char_counts.keys()))
        for row in zip(players, characters, counts):
            writer.writerow(row)


def write_player_counts_to_csv(player_counts: dict, output_filepath: str):
    if not player_counts:
        print("No player counts to write to CSV.")
        return

    players = player_counts.get("Player Tag", [])
    counts = player_counts.get("Count", [])

    with open(output_filepath, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(list(player_counts.keys()))
        for row in zip(players, counts):
            writer.writerow(row)


def write_moon_majorities_to_csv(moon_majorities: dict, output_filepath: str):
    if not moon_majorities:
        print("No moon majorities to write to CSV.")
        return

    with open(output_filepath, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=moon_majorities.keys())
        writer.writeheader()
        writer.writerow(moon_majorities)


def write_moon_counts_to_csv(moon_counts: dict, output_filepath: str):
    if not moon_counts:
        print("No moon counts to write to CSV.")
        return

    with open(output_filepath, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=moon_counts.keys())
        writer.writeheader()
        writer.writerow(moon_counts)


def write_moon_players_to_csv(players: dict, output_filepath: str):
    if not players:
        print("No players to write to CSV.")
        return

    c_players = players.get("C Players", [])
    f_players = players.get("F Players", [])
    h_players = players.get("H Players", [])
    max_len = max(len(c_players), len(f_players), len(h_players))

    # Pad lists so they're all the same length
    c_players += [""] * (max_len - len(c_players))
    f_players += [""] * (max_len - len(f_players))
    h_players += [""] * (max_len - len(h_players))

    with open(output_filepath, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(list(players.keys()))
        for row in zip(c_players, f_players, h_players):
            writer.writerow(row)


def write_character_totals_to_csv(char_totals: dict, output_filepath: str):
    if not char_totals:
        print("No totals to write to CSV.")
        return

    c_char_names = char_totals.get("C Char Names", [])
    c_counts = char_totals.get("C Totals", [])
    f_char_names = char_totals.get("F Char Names", [])
    f_counts = char_totals.get("F Char Totals", [])
    h_char_names = char_totals.get("H Char Names", [])
    h_counts = char_totals.get("H Char Totals", [])
    max_len = max(len(c_char_names), len(f_char_names), len(h_char_names))
    max_len = max(max_len, len(c_counts), len(f_counts), len(h_counts))

    # Pad lists so they're all the same length
    c_char_names += [""] * (max_len - len(c_char_names))
    c_counts += [""] * (max_len - len(c_counts))
    f_char_names += [""] * (max_len - len(f_char_names))
    f_counts += [""] * (max_len - len(f_counts))
    h_char_names += [""] * (max_len - len(h_char_names))
    h_counts += [""] * (max_len - len(h_counts))

    with open(output_filepath, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(list(char_totals.keys()))
        for row in zip(c_char_names, c_counts, f_char_names, f_counts, h_char_names, h_counts):
            writer.writerow(row)


def write_character_counts_to_csv(char_counts: dict, output_filepath: str):
    if not char_counts:
        print("No character counts to write to CSV.")
        return

    c_char_names = char_counts.get("C Char Names", [])
    c_counts = char_counts.get("C Counts", [])
    f_char_names = char_counts.get("F Char Names", [])
    f_counts = char_counts.get("F Counts", [])
    h_char_names = char_counts.get("H Char Names", [])
    h_counts = char_counts.get("H Counts", [])
    max_len = max(len(c_char_names), len(f_char_names), len(h_char_names))
    max_len = max(max_len, len(c_counts), len(f_counts), len(h_counts))

    # Pad lists so they're all the same length
    c_char_names += [""] * (max_len - len(c_char_names))
    c_counts += [""] * (max_len - len(c_counts))
    f_char_names += [""] * (max_len - len(f_char_names))
    f_counts += [""] * (max_len - len(f_counts))
    h_char_names += [""] * (max_len - len(h_char_names))
    h_counts += [""] * (max_len - len(h_counts))

    with open(output_filepath, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(list(char_counts.keys()))
        for row in zip(c_char_names, c_counts, f_char_names, f_counts, h_char_names, h_counts):
            writer.writerow(row)


def write_character_representation_to_csv(char_representation: dict, output_filepath: str):
    if not char_representation:
        print("No character representation to write to CSV.")
        return

    c_players = char_representation.get("C Players", [])
    c_chars = char_representation.get("C Chars", [])
    f_players = char_representation.get("F Players", [])
    f_chars = char_representation.get("F Chars", [])
    h_players = char_representation.get("H Players", [])
    h_chars = char_representation.get("H Chars", [])
    max_len = max(len(c_players), len(f_players), len(h_players))
    max_len = max(max_len, len(c_chars), len(f_chars), len(h_chars))

    # Pad lists so they're all the same length
    c_players += [""] * (max_len - len(c_players))
    c_chars += [""] * (max_len - len(c_chars))
    f_players += [""] * (max_len - len(f_players))
    f_chars += [""] * (max_len - len(f_chars))
    h_players += [""] * (max_len - len(h_players))
    h_chars += [""] * (max_len - len(h_chars))

    with open(output_filepath, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(list(char_representation.keys()))
        for row in zip(c_players, c_chars, f_players, f_chars, h_players, h_chars):
            writer.writerow(row)


def write_csv_output(brackets: List[Bracket], output: AnalysisOutput, output_dir: str, file_distinguisher: str="") -> None:
    """
    Writes the analysis output to a CSV file.

    :param output: output from analysis.
    :param output_path: Path to the output CSV file.
    :param file_distinguisher: Optional distinguisher for the output file names.
    """
    if not output:
        print("No output to write to CSV.")
        return

    today_date = datetime.now().strftime("%Y%m%d")
    today_output_dir = f"{today_date}-{output_dir}"
    # Create the directory if it doesn't exist
    os.makedirs(today_output_dir, exist_ok=True)

    identifier = f"{file_distinguisher}-" if file_distinguisher else ""

    write_brackets_to_csv(
        brackets,
        os.path.join(today_output_dir, f"{identifier}brackets.csv")
    )

    write_player_placement_counts_to_csv(
        output.get_player_placement_counts_dict(),
        os.path.join(today_output_dir, f"{identifier}player-placement-counts.csv")
    )
    write_player_char_counts_to_csv(
        output.get_player_occurrences_dict(),
        os.path.join(today_output_dir, f"{identifier}player-occurrences.csv")
    )
    write_player_counts_to_csv(
        output.get_player_counts_dict(),
        os.path.join(today_output_dir, f"{identifier}player-counts.csv")
    )
    write_moon_majorities_to_csv(
        output.get_moon_majorities_dict(),
        os.path.join(today_output_dir, f"{identifier}moon-majorities.csv")
    )
    write_moon_counts_to_csv(
        output.get_moon_counts_dict(),
        os.path.join(today_output_dir, f"{identifier}moon-counts.csv")
    )
    write_moon_players_to_csv(
        output.get_moon_players_dict(),
        os.path.join(today_output_dir, f"{identifier}moon-players.csv")
    )
    write_character_totals_to_csv(
        output.get_character_totals_dict(),
        os.path.join(today_output_dir, f"{identifier}character-totals.csv")
    )
    write_character_counts_to_csv(
        output.get_character_counts_dict(),
        os.path.join(today_output_dir, f"{identifier}character-counts.csv")
    )
    write_character_representation_to_csv(
        output.get_character_representation_dict(),
        os.path.join(today_output_dir, f"{identifier}character-representation.csv")
    )

    print(f"Results written to {today_output_dir}")
