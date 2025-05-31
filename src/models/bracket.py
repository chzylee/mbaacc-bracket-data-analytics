from dataclasses import dataclass

@dataclass
class Bracket:
    name: str
    date: str
    total_entrants: int
    # Source CSV includes top 8 results as default.
    # Filtering for analytics may change the set of finalists results to look at (e.g. top 4 only).
    finalists_results: list = None

    def __str__(self):
        return f"{self.name} ({self.date}) - {self.total_entrants} entrants"

    def __repr__(self):
        return f"Bracket(name={self.name}, date={self.date}, total_entrants={self.total_entrants}, top_8_results={self.finalists_results})"

    def print_results(self):
        print("------------------------------------------------------------------------")
        print(f"{self}  Results:")
        if self.finalists_results:
            print(" | ".join(str(player) for player in self.finalists_results))
        else:
            print("No results available.")
        print("------------------------------------------------------------------------\n")
