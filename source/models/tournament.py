from tinydb import TinyDB


class Tournament:
    def __init__(
        self,
        t_id: int,
        name: str,
        location: str,
        start_date: str,
        end_date: str,
        description: str,
        current_round: int,
        rounds: list,
        rounds_total=4,
    ):
        self.t_id = t_id
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.current_round = current_round
        self.rounds_total = rounds_total
        self.rounds = rounds

        self.tournament_db = TinyDB("database/tournaments.json")

    def format_tournament(self):
        return {
            "id": self.t_id,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "current_round": self.current_round,
            "rounds_total": self.rounds_total,
            "rounds": self.rounds,
        }

    def save_tournament_db(self):
        db = self.tournament_db
        self.t_id = db.insert(self.format_tournament())
        db.update({"id": self.t_id}, doc_ids=[self.t_id])
