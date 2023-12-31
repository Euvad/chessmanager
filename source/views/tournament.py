import time
from consolemenu import *
from consolemenu.items import *
from dateutil import parser


class TournamentView:
    def __init__(self):
        pass

    def get_valid_input(self, prompt, input_type, min_value=None):
        while True:
            try:
                user_input = input(prompt)
                if input_type == "date":
                    # Parse date and return a formatted string
                    parsed_date = parser.parse(user_input)
                    return parsed_date.isoformat()
                elif input_type == "int":
                    value = int(user_input)
                    if min_value is not None and value <= 0:
                        raise ValueError("Value must be greater than 0.")
                    return value
                else:
                    print("Invalid input type.")
            except ValueError as e:
                print(f"Invalid {input_type} format. {e}")

    def get_tournament_info(self, players):
        name = input("Please enter the tournament name: ")
        location = input(f"Please enter {name} location: ")
        description = input(f"Please enter {name} description: ")
        # Obtenez des dates valides
        start_date = self.get_valid_input(
            f"Please enter the start date of {name} (YYYY-MM-DD): ", input_type="date"
        )
        end_date = self.get_valid_input(
            f"Please enter the end date of {name} (YYYY-MM-DD): ", input_type="date"
        )
        round_total = self.get_valid_input(
            f"Please enter how much round {name} will have (must be greater than 0): ",
            input_type="int",
            min_value=1,
        )

        max_players = self.get_valid_input(
            f"Please enter how much players will play in this tournament (must be greater than 0): ",
            input_type="int",
            min_value=1,
        )

        player_data = self.get_player_list(players, max_players)
        tournament_data = {
            "name": name,
            "location": location,
            "description": description,
            "start_date": start_date,
            "end_date": end_date,
            "round_total": round_total,
            "max_players": max_players,
            "players": player_data,
        }
        return tournament_data

    def get_player_list(self, players, max_players):
        player_ids = []
        selected_indices = set()

        player_count = 0

        while player_count < max_players:
            selected_index = SelectionMenu.get_selection(
                [
                    f"Player: {player['last_name']} {player['first_name']}"
                    for player in players
                ],
                f"Please select player {player_count + 1}/{max_players}.",
                show_exit_option=False,
            )

            # Check if the index is valid and hasn't been selected already
            if (
                0 <= selected_index < len(players)
                and selected_index not in selected_indices
            ):
                player_ids.append(selected_index)
                selected_indices.add(selected_index)
                player_count += 1
                selected_player = players[selected_index]
                print(
                    f"Selected player: {selected_player['last_name']} {selected_player['first_name']}"
                )
            else:
                print("Invalid selection or player already selected. Please try again.")

            time.sleep(0.2)  # Add a delay if necessary

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
        roundIsOver = FunctionItem("This round is over.", print("hello world"))
        menu.append_item(roundIsOver)
        menu.show()
