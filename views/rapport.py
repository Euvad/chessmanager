import csv
import os
from prettytable import PrettyTable
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem


class Rapport:
    def __init__(self):
        self.csv_folder = "csv"
        self.create_csv_folder()

    def report_exit(self):
        user_input = input(
            "Tapez 'exit' pour retourner au menu principal ou appuyez sur Entrée pour continuer: "
        )
        if user_input.lower() == "exit":
            return

    def create_csv_folder(self):
        if not os.path.exists(self.csv_folder):
            os.makedirs(self.csv_folder)

    def display_players_list(self, players):
        table = PrettyTable(["Last Name", "First Name"])
        for player in players:
            table.add_row([player.last_name, player.first_name])
        print(table)

    def display_tournaments_list(self, tournaments):
        table = PrettyTable(["Name", "Start Date", "End Date"])

        # Vérifie si tournaments est une instance d'un type itérable (par exemple, list, tuple)
        if isinstance(tournaments, (list, tuple)):
            for tournament in tournaments:
                table.add_row(
                    [tournament.name, tournament.start_date, tournament.end_date]
                )
            print(table)
        else:
            table.add_row(
                [tournaments.name, tournaments.start_date, tournaments.end_date]
            )
            print(table)
            self.report_exit()

    def display_tournament_info(self, tournaments, display_method):
        tournament_menu = ConsoleMenu("Select Tournament")
        for tournament in tournaments:
            tournament_menu.append_item(
                FunctionItem(
                    tournament.name,
                    lambda t=tournament: display_method(t),
                )
            )
        tournament_menu.show()

    def display_players_list_tournament(self, players):
        table = PrettyTable(["Last Name", "First Name"])
        for player in players:
            table.add_row([player.last_name, player.first_name])
        print(table)
        self.report_exit()

    def display_tour_info(self, tour):
        table = PrettyTable(["Player 1", "Player 2", "Result"])
        for round in tour.rounds:
            for match in round.matches:
                table.add_row(
                    [match.player1.last_name, match.player1.first_name, match.result]
                )
        print(table)
        self.report_exit()

    def export_to_csv(self, filename, data):
        file_path = os.path.join(self.csv_folder, filename)
        with open(file_path, mode="w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(data)
        print(f"Data exported to {filename}")
