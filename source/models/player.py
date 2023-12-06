from tinydb import TinyDB


class Player:
    def __init__(
        self,
        p_id: int,
        last_name: str,
        first_name: str,
        birthday: str,
        gender: str,
    ):
        self.p_id = p_id
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.gender = gender
        self.score = 0.0

        self.player_db = TinyDB("database/players.json")

    def format_player(self):
        return {
            "id": self.p_id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "date_of_birth": self.birthday,
            "gender": self.gender,
            "score": self.score,
        }

    def save_player_db(self):
        players_db = self.player_db
        self.p_id = players_db.insert(self.format_player())
        players_db.update({"id": self.p_id}, doc_ids=[self.p_id])
