from source.views.player import PlayerView
from source.models.player import Player


class PlayerController:
    def __init__(self):
        pass

    def new_player(self):
        player_view = PlayerView()
        player_data = player_view.get_player_info()

        player_model = Player(
            p_id=0,
            last_name=player_data["lastname"],
            first_name=player_data["firstname"],
            birthday=player_data["birthdate"],
            gender=player_data["gender"],
        )

        player_model.save_player_db()
