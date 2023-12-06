import time


class TournamentView:
    def __init__(self):
        pass

    def get_tournament_info(self):
        name = input("Please enter the tournament name: ")
        location = input(f"Please enter {name} location: ")
        description = input(f"Please enter {name} description: ")

        tournament_data = {
            "name": name,
            "location": location,
            "description": description,
        }
        self.print_success(tournament_data)
        return tournament_data

    def print_success(self, tournament_data):
        print(f"The tournament {tournament_data['name']} successfully created.")
        time.sleep(2)
