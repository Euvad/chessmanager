from tinydb import TinyDB
from models.round import Round
import time


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

        # Extraire les identifiants des joueurs
        player_ids = [player.id for player in self.players]

        tournament_data = self.format_tournament()
        tournament_data["players"] = player_ids

        self.id = db.insert(tournament_data)
        db.update({"id": self.id}, doc_ids=[self.id])

    def update_attribute(self, attribute, value):
        setattr(self, attribute, value)
        db = self.tournament_db
        db.update({attribute: value}, doc_ids=[self.id])

    def update_tournament_db(self):
        db = self.tournament_db

        # Sérialiser les rounds avant chaque mise à jour
        serialized_rounds = [
            round_ if isinstance(round_, dict) else round_.to_serializable()
            for round_ in self.rounds
        ]

        # Mettre à jour la base de données avec les informations mises à jour
        db.update(
            {
                "rounds": serialized_rounds,
                "players": self.players,
                "current_round": self.current_round,
            },
            doc_ids=[self.id],
        )

    @classmethod
    def from_dict(cls, data):
        from models.player import Player

        return cls(
            id=data["id"],
            name=data["name"],
            location=data["location"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            description=data["description"],
            current_round=data["current_round"],
            rounds_total=data["rounds_total"],
            max_players=data["max_players"],
            players=data["players"],
            rounds=[
                Round.from_dict(round_data, Player.get_player_db())
                for round_data in data["rounds"]
            ],
        )

    @staticmethod
    def load_tournament_db():
        db = TinyDB("database/tournaments.json")
        tournaments_list = []

        for item in db:
            tournament = Tournament.from_dict(item)
            tournaments_list.append(tournament)

        return tournaments_list
