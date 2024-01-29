from views.player import PlayerView
from models.player import Player
import time


class PlayerController:
    def __init__(self):
        pass

    def new_player(self):
        player_view = PlayerView()
        player_data = player_view.get_player_info()

        player_model = Player(
            id=0,
            last_name=player_data["lastname"],
            first_name=player_data["firstname"],
            birthday=player_data["birthdate"],
            score=0.0,
            gender=player_data["gender"],
        )
        player_model.save_player_db()
