import csv
import os
from datetime import datetime

from src.analytics.output import AnalysisOutput

def write_moon_majorities_to_csv(moon_majorities: dict, output_filepath: str):
    if not moon_majorities:
        print("No moon majorities to write to CSV.")
        return

    with open(output_filepath, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=moon_majorities.keys())
        writer.writeheader()
        writer.writerow(moon_majorities)


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

def write_csv_output(output: AnalysisOutput, output_dir: str, file_distinguisher: str="") -> None:
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

    write_moon_majorities_to_csv(
        output.get_moon_majorities_dict(),
        os.path.join(today_output_dir, f"{identifier}moon-majorities.csv")
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
