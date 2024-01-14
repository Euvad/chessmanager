import time


class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = None

    def play_match(self, result):
        self.result = result

    def to_serializable(self):
        return {"player1": self.player1, "player2": self.player2, "result": self.result}
