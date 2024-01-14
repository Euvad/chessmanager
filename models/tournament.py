from tinydb import TinyDB
from models.round import Round


class Tournament:
    def __init__(
        self,
        id: int,
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
        self.id = id
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
            "id": self.id,
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
        self.id = db.insert(self.format_tournament())
        db.update({"id": self.id}, doc_ids=[self.id])

    def update_attribute(self, attribute, value):
        setattr(self, attribute, value)
        db = self.tournament_db
        db.update({attribute: value}, doc_ids=[self.id])

    def update_tournament_db(self):
        db = self.tournament_db
        db.update({"rounds": self.rounds}, doc_ids=[self.id])
        db.update({"players": self.players}, doc_ids=[self.id])
        db.update({"current_round": self.current_round}, doc_ids=[self.id])

    @staticmethod
    def load_tournament_db():
        db = TinyDB("database/tournaments.json")
        db.all()
        tournaments_list = []
        for item in db:
            tournaments_list.append(item)

        return tournaments_list
