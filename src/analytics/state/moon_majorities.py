from dataclasses import dataclass
from dataclasses import dataclass
from typing import Dict

@dataclass
class MoonMajorities:
    # Count of times moon had majority presence in top 8 results
    c_majorities: int = 0
    f_majorities: int = 0
    h_majorities: int = 0
    # Count of times 2 moons had equal presence in top 8 results
    ties: int = 0
    #Count of times moon had 0 presence in top 8 results
    c_shutouts: int = 0
    f_shutouts: int = 0
    h_shutouts: int = 0

    def __str__(self):
        return (f"C Majorities: {self.c_majorities}, F Majorities: {self.f_majorities}, "
                f"H Majorities: {self.h_majorities}, Ties: {self.ties}, "
                f"C Shutouts: {self.c_shutouts}, F Shutouts: {self.f_shutouts}, H Shutouts: {self.h_shutouts}")


@dataclass
class MoonCount:
    c: int = 0
    f: int = 0
    h: int = 0

    def __getitem__(self, key):
        if key.upper() == "C":
            return self.c
        elif key.upper() == "F":
            return self.f
        elif key.upper() == "H":
            return self.h
        else:
            raise KeyError(key)

    def __setitem__(self, key, value):
        if key.upper() == "C":
            self.c = value
        elif key.upper() == "F":
            self.f = value
        elif key.upper() == "H":
            self.h = value
        else:
            raise KeyError(key)


def update_moon_majorities(moon_count: MoonCount, moon_majorities: MoonMajorities) -> Dict[str, int]:
    """
    Count the number of times each moon appears in the top 8 results of all brackets.

    Args:
        brackets (list): List of Bracket objects containing top 8 results.

    Returns:
        dict: A dictionary with moons as keys and their counts as values.
    """
    if moon_count.c >= 4 and moon_count.f > 0 and moon_count.h > 0:
        moon_majorities.c_majorities += 1
    elif moon_count.f >= 4 and moon_count.c > 0 and moon_count.h > 0:
        moon_majorities.f_majorities += 1
    elif moon_count.h >= 4 and moon_count.c > 0 and moon_count.f > 0:
        moon_majorities.h_majorities += 1
    elif moon_count.c > 0 and moon_count.f > 0 and moon_count.h > 0:
        # If no moon takes at least 4/8 top 8 spots and all moons are present, 2 moons must have a tie.
        moon_majorities.ties += 1

    if moon_count.c == 0:
        moon_majorities.c_shutouts += 1
    if moon_count.f == 0:
        moon_majorities.f_shutouts += 1
    if moon_count.h == 0:
        moon_majorities.h_shutouts += 1

    return moon_majorities
