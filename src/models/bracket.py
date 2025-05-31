from dataclasses import dataclass

@dataclass
class Bracket:
    name: str
    date: str
    total_entrants: int
    top_8_results: list = None

    def __str__(self):
        return f"{self.name} ({self.date}) - {self.total_entrants} entrants"

    def __repr__(self):
        return f"Bracket(name={self.name}, date={self.date}, total_entrants={self.total_entrants}, top_8_results={self.top_8_results})"
