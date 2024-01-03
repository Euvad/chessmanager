from views.tournament import TournamentView
from models.tournament import Tournament
from models.round import Round
from models.player import Player
import time
from prettytable import PrettyTable
from datetime import datetime


class TournamentController:
    def __init__(self):
        self.tournament_view = TournamentView()
        self.time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def new_tournament(self):
        tournament_data = self.tournament_view.get_tournament_info(
            players=Player.get_player_db()
        )

        # Utilisez directement les clés du dictionnaire pour accéder aux données
        tournament_model = Tournament(
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

    def draw_tournament(self):
        tournaments = Tournament.load_tournament_db()
        tournament_names = [tournament["name"] for tournament in tournaments]
        selected_tournament = self.tournament_view.select_tournament(tournament_names)
        players = Player.get_player_db()
        for tournament in tournaments:
            if selected_tournament == tournament["name"]:
                found_tournament = tournament
                found_players = found_tournament["players"]
                for player in players:
                    if player.doc_id in found_players:
                        print(player)
                        time.sleep(2)
                TournamentView.draw_tournament(self, found_tournament)
            else:
                print("not found")

    def start_tournament(self, tournament):
        tournament.start_date = self.time
        tournament.update_time(tournament.start_date, "start_date")

        while tournament.current_round <= tournament.rounds_total:
            if tournament.current_round == 1:
                self.first_round(tournament)
            else:
                self.next_round(tournament)

            tournament.current_round += 1
            tournament.update_tournament_db()

        if tournament.current_round > 1:
            tournament.end_date = self.time
            tournament.update_timer(tournament.end_date, "end_date")
            self.tournament_end(tournament)
