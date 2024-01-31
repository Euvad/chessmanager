class Round:
    def __init__(self, round_number):
        self.round_number = round_number
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def to_serializable(self):
        return {
            "round_number": self.round_number,
            "matches": [match.to_serializable() for match in self.matches],
        }

    @classmethod
    def from_dict(cls, data, players):
        from models.match import Match

        round_obj = cls(data["round_number"])
        round_obj.matches = [
            Match.from_dict(match_data, players) for match_data in data["matches"]
        ]
        return round_obj
