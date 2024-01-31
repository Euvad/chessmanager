class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = None

    def play_match(self, result):
        self.result = result

    def to_serializable(self):
        return {
            "player1": self.player1.id,  # Convertir player1 en entier
            "player2": self.player2.id,  # Convertir player2 en entier
            "result": self.result,
        }

    @classmethod
    def from_dict(cls, match_data, players):
        player1_id = match_data["player1"]
        player2_id = match_data["player2"]
        result = match_data["result"]

        player1 = next((player for player in players if player.id == player1_id), None)
        player2 = next((player for player in players if player.id == player2_id), None)

        if player1 is None or player2 is None:
            raise ValueError(f"Player not found for match data: {match_data}")

        match_obj = cls(player1, player2)
        match_obj.play_match(result)
        return match_obj
