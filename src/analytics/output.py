from dataclasses import dataclass
from typing import List, Set, Dict, Tuple

@dataclass
class AnalysisOutput:
    """
    Class to hold the output of the analysis.

    Data will go into CSV output.
    """

    c_moon_majorities: int
    f_moon_majorities: int
    h_moon_majorities: int
    c_moon_shutouts: int
    f_moon_shutouts: int
    h_moon_shutouts: int
    moon_ties: int

    c_moon_players: Set[str]
    f_moon_players: Set[str]
    h_moon_players: Set[str]

    c_character_totals: Dict[str, int] = None
    f_character_totals: Dict[str, int] = None
    h_character_totals: Dict[str, int] = None

    c_character_counts: Dict[str, int] = None
    f_character_counts: Dict[str, int] = None
    h_character_counts: Dict[str, int] = None

    c_char_representation: List[Tuple[str, str]] = None
    f_char_representation: List[Tuple[str, str]] = None
    h_char_representation: List[Tuple[str, str]] = None

    def __str__(self):
        def stringify_dict(d):
            if not d:
                return ""
            return ", ".join(f"{k}: {v}" for k, v in d.items())

        def stringify_tuples(tuples):
            if not tuples:
                return ""
            return ", ".join(f"({a}: {b})" for a, b in tuples)

        # Return a neatly formatted string representation
        return (
            "******************************************************\n"
            f"C Moon Majorities: {self.c_moon_majorities}\n"
            f"F Moon Majorities: {self.f_moon_majorities}\n"
            f"H Moon Majorities: {self.h_moon_majorities}\n"
            f"C Moon Shutouts: {self.c_moon_shutouts}\n"
            f"F Moon Shutouts: {self.f_moon_shutouts}\n"
            f"H Moon Shutouts: {self.h_moon_shutouts}\n"
            f"Moon Ties: {self.moon_ties}\n"
            f"C Moon Players: {self.c_moon_players}\n"
            f"F Moon Players: {self.f_moon_players}\n"
            f"H Moon Players: {self.h_moon_players}\n"
            f"C Character Totals: [ {stringify_dict(self.c_character_totals)} ]\n"
            f"F Character Totals: [ {stringify_dict(self.f_character_totals)} ]\n"
            f"H Character Totals: [ {stringify_dict(self.h_character_totals)} ]\n"
            f"C Unique Character Counts: [ {stringify_dict(self.c_character_counts)} ]\n"
            f"F Unique Character Counts: [ {stringify_dict(self.f_character_counts)} ]\n"
            f"H Unique Character Counts: [ {stringify_dict(self.h_character_counts)} ]\n"
            f"C Character Representation: [ {stringify_tuples(self.c_char_representation)} ]\n"
            f"F Character Representation: [ {stringify_tuples(self.f_char_representation)} ]\n"
            f"H Character Representation: [ {stringify_tuples(self.h_char_representation)} ]\n"
            "******************************************************"
        )
