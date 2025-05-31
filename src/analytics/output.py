from dataclasses import dataclass
from typing import List, Set

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

    def __str__(self):
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
            "******************************************************"
        )

