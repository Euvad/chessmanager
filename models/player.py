from tinydb import TinyDB


# mettre tinydb player db plus global
class Player:
    def __init__(
        self,
        id: int,
        last_name: str,
        first_name: str,
        birthday: str,
        gender: str,
        score: float,
    ):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.gender = gender
        self.score = score

        self.player_db = TinyDB("database/players.json")

    def format_player(self):
        return {
            "id": self.id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "date_of_birth": self.birthday,
            "gender": self.gender,
            "score": self.score,
        }

    def save_player_db(self):
        self.id = self.player_db.insert(self.format_player())
        self.player_db.update({"id": self.id}, doc_ids=[self.id])

    @staticmethod
    def filter_players_by_id(player_ids):
        all_players = Player.get_player_db()
        filtered_players = [player for player in all_players if player.id in player_ids]
        return filtered_players

    @staticmethod
    def get_player_db():
        players_db = TinyDB("database/players.json")

        # Retrieve all documents
        all_players_data = players_db.all()

        # Convert data to Player objects
        all_players = [
            Player(
                player_data["id"],
                player_data["last_name"],
                player_data["first_name"],
                player_data["date_of_birth"],
                player_data["gender"],
                player_data["score"],
            )
            for player_data in all_players_data
        ]

        return all_players
