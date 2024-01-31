from models.player import Player
from models.tournament import Tournament
from views.rapport import Rapport


class ReportController:
    def __init__(self):
        self.players = Player.get_player_db()
        self.tournaments = Tournament.load_tournament_db()
        self.view = Rapport()

    def generate_players_report(self):
        sorted_players = sorted(self.players, key=lambda x: (x.last_name, x.first_name))
        self.view.display_players_list(sorted_players)

    def generate_tournaments_report(self):
        self.view.display_tournaments_list(self.tournaments)

    def generate_tournament_info_report(self, tournament):
        self.view.display_tournament_info(tournament)

    def generate_players_tournament_report(self, players):
        sorted_players = sorted(players, key=lambda x: (x.last_name, x.first_name))
        self.view.display_players_list_tournament(sorted_players)

    def generate_tour_info_report(self, tour):
        self.view.display_tour_info(tour)

    def export_players_to_csv(self, filename):
        players_data = [("Last Name", "First Name")]
        for player in self.players:
            players_data.append((player.last_name, player.first_name))
        self.view.export_to_csv(filename, players_data)

    def export_tournaments_to_csv(self, filename):
        tournaments_data = [("Name", "Date")]
        for tournament in self.tournaments:
            tournaments_data.append((tournament.name, tournament.date))
        self.view.export_to_csv(filename, tournaments_data)
