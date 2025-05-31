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

    def get_moon_majorities_dict(self):
        return {
            "C Majorities": self.c_moon_majorities,
            "F Majorities": self.f_moon_majorities,
            "H Majorities": self.h_moon_majorities,
            "C Shutouts": self.c_moon_shutouts,
            "F Shutouts": self.f_moon_shutouts,
            "H Shutouts": self.h_moon_shutouts,
            "Moon Ties": self.moon_ties
        }

    def get_moon_players_dict(self):
        return {
            "C Players": sorted(self.c_moon_players),
            "F Players": sorted(self.f_moon_players),
            "H Players": sorted(self.h_moon_players)
        }

    def get_character_totals_dict(self):
        return {
            "C Char Names": list(self.c_character_totals.keys()) if self.c_character_totals else [],
            "C Totals": list(self.c_character_totals.values()) if self.c_character_totals else [],
            "F Char Names": list(self.f_character_totals.keys()) if self.f_character_totals else [],
            "F Char Totals": list(self.f_character_totals.values()) if self.f_character_totals else [],
            "H Char Names": list(self.h_character_totals.keys()) if self.h_character_totals else [],
            "H Char Totals": list(self.h_character_totals.values()) if self.h_character_totals else []
        }

    def get_character_counts_dict(self):
        return {
            "C Char Names": list(self.c_character_counts.keys()) if self.c_character_counts else [],
            "C Counts": list(self.c_character_counts.values()) if self.c_character_counts else [],
            "F Char Names": list(self.f_character_counts.keys()) if self.f_character_counts else [],
            "F Counts": list(self.f_character_counts.values()) if self.f_character_counts else [],
            "H Char Names": list(self.h_character_counts.keys()) if self.h_character_counts else [],
            "H Counts": list(self.h_character_counts.values()) if self.h_character_counts else []
        }

    def get_character_representation_dict(self):
        return {
            "C Players": [tag for tag, char in self.c_char_representation] if self.c_char_representation else [],
            "C Chars": [char for tag, char in self.c_char_representation] if self.c_char_representation else [],
            "F Players": [tag for tag, char in self.f_char_representation] if self.f_char_representation else [],
            "F Chars": [char for tag, char in self.f_char_representation] if self.f_char_representation else [],
            "H Players": [tag for tag, char in self.h_char_representation] if self.h_char_representation else [],
            "H Chars": [char for tag, char in self.h_char_representation] if self.h_char_representation else []
        }
