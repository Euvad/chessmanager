import time


class PlayerView:
    def __init__(self):
        pass

    def get_player_info(self):
        lastname = input("Please enter the new player last name: ")
        firstname = input(f"Please enter {lastname} first name: ")
        birthdate = input(
            f"Please enter {lastname} {firstname} date of birth (dd/mm/yyyy): "
        )
        gender = input(f"Please enter {lastname} {firstname} sex (M/F): ")
        player_data = {
            "lastname": lastname,
            "firstname": firstname,
            "birthdate": birthdate,
            "gender": gender,
        }
        self.print_success(player_data)
        return player_data

    def print_success(self, player_data):
        print(
            f"The player {player_data['lastname']} {player_data['firstname']} has been successfully created."
        )
        time.sleep(2)
