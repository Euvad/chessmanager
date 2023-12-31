from source.views.tournament import TournamentView
from source.models.tournament import Tournament
from source.models.player import Player
import time


class TournamentController:
    def __init__(self):
        self.tournament_view = TournamentView()

    def new_tournament(self):
        tournament_data = self.tournament_view.get_tournament_info(
            players=Player.get_player_db()
        )

        # Utilisez directement les clés du dictionnaire pour accéder aux données
        tournament_model = Tournament(
            t_id=0,  # revoir id
            name=tournament_data["name"],
            location=tournament_data["location"],
            start_date=tournament_data["start_date"],
            end_date=tournament_data["end_date"],
            description=tournament_data["description"],
            current_round=0,
            rounds_total=4,
            players=tournament_data["players"],
            max_players=tournament_data["max_players"],
            rounds=[1],
        )

        tournament_model.save_tournament_db()

    def load_tournament(self):
        tournaments = Tournament.load_tournament_db()
        tournament_names = [tournament["name"] for tournament in tournaments]
        selected_tournament = self.tournament_view.select_tournament(tournament_names)
        for tournament in tournaments:
            if selected_tournament == tournament["name"]:
                found_tournament = tournament
                TournamentView.draw_tournament(self, found_tournament)
            else:
                print("not found")
                time.sleep(5)