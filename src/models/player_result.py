from dataclasses import dataclass

@dataclass
class PlayerResult:
    tag: str
    placement: int
    moon: str
    character: str


    def get_placement_str(self):
        if self.placement == 1:
            return "1st"
        elif self.placement == 2:
            return "2nd"
        elif self.placement == 3:
            return "3rd"
        else:
            return f"{self.placement}th"

    def __str__(self):
        return f"{self.tag} - {self.get_placement_str()} place {self.moon}-{self.character}"

    def __repr__(self):
        return f"PlayerResult(tag={self.tag}, moon={self.moon}, character={self.character}, placement={self.placement})"
