from models.player import Player
from models.tournament import Tournament
from views.rapport import Rapport
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem


class ReportController:
    def __init__(self):
        self.players = Player.get_player_db()  # data not sync!!!
        self.tournaments = Tournament.load_tournament_db()
        self.view = Rapport()

    def new_report(self):
        menu = ConsoleMenu("Select Report Type")

        menu.append_item(
            FunctionItem("All Player Report", self.generate_players_report)
        )
        menu.append_item(
            FunctionItem("All Tournaments Report", self.generate_tournaments_report)
        )
        menu.append_item(
            FunctionItem(
                "Single Tournament Report",
                self.generate_tournament_info_report,
            )
        )
        menu.append_item(
            FunctionItem(
                "Single Tournament Players Report",
                self.generate_players_tournament_report,
            )
        )
        menu.append_item(
            FunctionItem("Tour Info Report", self.generate_tour_info_report)
        )
        menu.append_item(
            FunctionItem("Export Players to CSV", self.export_players_to_csv)
        )
        menu.append_item(
            FunctionItem("Export Tournaments to CSV", self.export_tournaments_to_csv)
        )

        menu.show()

    def generate_players_report(self):
        sorted_players = sorted(self.players, key=lambda x: (x.last_name, x.first_name))
        self.view.display_players_list(sorted_players)
        self.view.report_exit()

    def generate_tournaments_report(self):
        self.view.display_tournaments_list(self.tournaments)
        self.view.report_exit()

    def generate_tournament_info_report(self):
        self.view.display_tournament_info(
            self.tournaments, self.view.display_tournaments_list
        )

    def simple_display_method(self, tourn):
        players = Player.filter_players_by_id(tourn.players)
        sorted_players = sorted(players, key=lambda x: (x.last_name, x.first_name))
        self.view.display_players_list_tournament(sorted_players)

    def generate_players_tournament_report(self):
        self.view.display_tournament_info(self.tournaments, self.simple_display_method)

    def generate_tour_info_report(self):
        self.view.display_tournament_info(self.tournaments, self.view.display_tour_info)

    def export_players_to_csv(self, filename):
        players_data = [("Last Name", "First Name")]
        for player in self.players:
            players_data.append((player.last_name, player.first_name))
        self.view.export_to_csv(filename, players_data)
        self.view.report_exit()

    def export_tournaments_to_csv(self, filename):
        tournaments_data = [("Name", "Date")]
        for tournament in self.tournaments:
            tournaments_data.append((tournament.name, tournament.date))
        self.view.export_to_csv(filename, tournaments_data)
        self.view.report_exit()
