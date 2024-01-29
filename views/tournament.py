import time
from consolemenu import *
from consolemenu.items import *
from dateutil import parser
import re
from prettytable import PrettyTable


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

    def validate_positive_int(self, value):
        int_value = int(value)
        if int_value <= 0:
            raise ValueError("Value must be greater than 0.")
        return int_value

    def get_tournament_info(self, players):
        name = input("Please enter the tournament name: ")
        location = input(f"Please enter {name} location: ")
        description = input(f"Please enter {name} description: ")

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
            "rounds_total": rounds_total,
            "max_players": max_players,
            "players": player_data,
        }
        return tournament_data

    def get_player_list(self, players, max_players):
        player_ids = []
        selected_doc_ids = set()
        print(players)
        player_count = 0

        while player_count < max_players:
            player_selections = [
                {
                    "id": player.id,
                    "name": f"Player {player.id}: {player.last_name} {player.first_name}",
                }
                for player in players
            ]

            selected_index = SelectionMenu.get_selection(
                [player["name"] for player in player_selections],
                f"Please select player {player_count + 1}/{max_players}.",
                show_exit_option=False,
            )
            selected_doc_id = player_selections[selected_index]["id"]
            if selected_doc_id not in selected_doc_ids:
                player_ids.append(selected_doc_id)
                selected_doc_ids.add(selected_doc_id)
                player_count += 1
                selected_player = players[selected_index]
                print(
                    f"Selected player: {selected_player.last_name} {selected_player.first_name}"
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

    def tournament_end(self, tournament, player_base):
        user_input = input(
            "Tapez 'exit' pour retourner au menu principal ou appuyez sur Entrée pour continuer: "
        )
        if user_input.lower() == "exit":
            return

    def play_round(self, current_round):
        for index, match in enumerate(current_round.matches):
            menu_items = [
                match.player1.last_name,
                match.player2.last_name,
                "Draw",
            ]
            winner_menu = SelectionMenu(
                menu_items,
                title="Choose the winner:",
                subtitle=f"Round {current_round.round_number + 1} | Match {index + 1}",
            )
            winner_menu.show(show_exit_option=False)
            result_index = winner_menu.selected_option + 1

            match.play_match(result_index)

            # if match.result == 1 or match.result == 2:
            #     winner_id = match.player1 if match.result == 1 else match.player2
            #     player_data[winner_id]["score"] += 1
            # elif match.result == 3:  # Draw
            #     player_data[match.player1]["score"] += 0.5
            #     player_data[match.player2]["score"] += 0.5
