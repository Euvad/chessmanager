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
        selected_doc_ids = set()

        player_count = 0

        while player_count < max_players:
            # Afficher la liste des joueurs avec leurs "doc_id"
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

            # Récupérer le "doc_id" du joueur sélectionné
            selected_doc_id = player_selections[selected_index]["doc_id"]

            # Vérifier si le "doc_id" est valide et n'a pas déjà été sélectionné
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

            time.sleep(0.2)  # Ajouter un délai si nécessaire

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
