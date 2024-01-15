import time
from consolemenu import *
from consolemenu.items import *
from dateutil import parser
import re


class TournamentView:
    def __init__(self):
        pass

    DATE_FORMAT = re.compile(r"^\d{2}/\d{2}/\d{4}$")

    def get_valid_input(self, prompt, validation_function):
        while True:
            try:
                user_input = input(prompt)
                return validation_function(user_input)
            except ValueError as e:
                print(f"Invalid input. {e}")

    def validate_date(self, date_string):
        if not re.match(self.DATE_FORMAT, date_string):
            raise ValueError("Invalid date format. Please use DD-MM-YYYY.")
        return parser.parse(date_string).isoformat()

    def validate_positive_int(self, value):
        int_value = int(value)
        if int_value <= 0:
            raise ValueError("Value must be greater than 0.")
        return int_value

    def validate_date_range(self, start_date, end_date):
        if start_date > end_date:
            raise ValueError("End date must be after start date.")

    def get_tournament_info(self, players):
        name = input("Please enter the tournament name: ")
        location = input(f"Please enter {name} location: ")
        description = input(f"Please enter {name} description: ")

        start_date = self.get_valid_input(
            f"Please enter the start date of {name} (DD-MM-YYYY): ", self.validate_date
        )
        end_date = self.get_valid_input(
            f"Please enter the end date of {name} (DD-MM-YYYY): ", self.validate_date
        )

        # Vérification de la relation entre start_date et end_date
        self.validate_date_range(start_date, end_date)

        rounds_total = self.get_valid_input(
            f"Please enter how much round {name} will have (must be greater than 0): ",
            self.validate_positive_int,
        )

        max_players = self.get_valid_input(
            f"Please enter how much players will play in this tournament (must be greater than 0): ",
            self.validate_positive_int,
        )

        player_data = self.get_player_list(players, max_players)
        tournament_data = {
            "name": name,
            "location": location,
            "description": description,
            "start_date": start_date,
            "end_date": end_date,
            "rounds_total": rounds_total,
            "max_players": max_players,
            "players": player_data,
        }
        return tournament_data

    def get_player_list(self, players, max_players):
        player_ids = []
        selected_doc_ids = set()

        player_count = 0

        while player_count < max_players:
            player_selections = [
                {
                    "doc_id": player.doc_id,
                    "name": f"Player {player.doc_id}: {player['last_name']} {player['first_name']}",
                }
                for player in players
            ]

            selected_index = SelectionMenu.get_selection(
                [player["name"] for player in player_selections],
                f"Please select player {player_count + 1}/{max_players}.",
                show_exit_option=False,
            )
            selected_doc_id = player_selections[selected_index]["doc_id"]
            if selected_doc_id not in selected_doc_ids:
                player_ids.append(selected_doc_id)
                selected_doc_ids.add(selected_doc_id)
                player_count += 1
                selected_player = players[selected_index]
                print(
                    f"Selected player: {selected_player['last_name']} {selected_player['first_name']}"
                )
            else:
                print("Invalid selection or player already selected. Please try again.")

            time.sleep(0.2)

        return player_ids

    def print_success(self, tournament_data):
        print(f"The tournament {tournament_data['name']} successfully created.")
        time.sleep(2)

    def select_tournament(self, tournament_list):
        selection = SelectionMenu.get_selection(tournament_list)
        selected_tournament = tournament_list[selection]
        return selected_tournament

    def draw_tournament(self, tournament_data):
        menu = ConsoleMenu(
            f"{tournament_data['name']} | {tournament_data['description']}",
            f"{tournament_data['location']} | Started: {tournament_data['start_date']} | Rounds: {tournament_data['current_round']}/{tournament_data['rounds_total']}",
            show_exit_option=False,
        )
        roundIsOver = FunctionItem(
            "This round is over.",
        )
        menu.append_item(roundIsOver)
        menu.show()
