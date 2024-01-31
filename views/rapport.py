from prettytable import PrettyTable
import csv
import os


class Rapport:
    def __init__(self):
        self.csv_folder = "csv"
        self.create_csv_folder()

    def create_csv_folder(self):
        if not os.path.exists(self.csv_folder):
            os.makedirs(self.csv_folder)

    def display_players_list(self, players):
        table = PrettyTable(["Last Name", "First Name"])
        for player in players:
            table.add_row([player.last_name, player.first_name])
        print(table)

    def display_tournaments_list(self, tournaments):
        table = PrettyTable(["Name", "Date"])
        for tournament in tournaments:
            table.add_row([tournament.name, tournament.date])
        print(table)

    def display_tournament_info(self, tournament):
        print(f"Tournament Name: {tournament.name}")
        print(f"Tournament Dates: {tournament.date}")

    def display_players_list_tournament(self, players):
        table = PrettyTable(["Last Name", "First Name"])
        for player in players:
            table.add_row([player.last_name, player.first_name])
        print(table)

    def display_tour_info(self, tour):
        table = PrettyTable(["Player 1", "Player 2", "Result"])
        for match in tour.matches:
            table.add_row(
                [match.player1.last_name, match.player1.first_name, match.result]
            )
        print(table)

    def export_to_csv(self, filename, data):
        file_path = os.path.join(self.csv_folder, filename)
        with open(file_path, mode="w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(data)
        print(f"Data exported to {filename}")
