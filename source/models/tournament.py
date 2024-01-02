from tinydb import TinyDB


class Tournament:
    def __init__(
        self,
        name: str,
        location: str,
        start_date: str,
        end_date: str,
        description: str,
        current_round: int,
        rounds: list,
        max_players: int,
        players: list,
        rounds_total=4,
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.current_round = current_round
        self.rounds_total = rounds_total
        self.max_players = max_players
        self.players = players
        self.rounds = rounds

        self.tournament_db = TinyDB("database/tournaments.json")

    def format_tournament(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "current_round": self.current_round,
            "rounds_total": self.rounds_total,
            "max_players": self.max_players,
            "players": self.players,
            "rounds": self.rounds,
        }

    def save_tournament_db(self):
        db = self.tournament_db
        db.insert(self.format_tournament())

    @staticmethod
    def load_tournament_db():
        db = TinyDB("database/tournaments.json")
        db.all()
        tournaments_list = []
        for item in db:
            tournaments_list.append(item)

        return tournaments_list
