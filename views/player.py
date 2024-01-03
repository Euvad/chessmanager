import re
import time


class PlayerView:
    DATE_FORMAT = re.compile(r"^\d{2}/\d{2}/\d{4}$")
    GENDER_OPTIONS = {"M", "F"}

    def __init__(self):
        pass

    def get_valid_input(self, prompt, validator):
        while True:
            user_input = input(prompt)
            if validator(user_input):
                return user_input
            else:
                print("Invalid input. Please try again.")

    def get_player_info(self):
        lastname = self.get_valid_input(
            "Please enter the new player last name: ", lambda x: x.isalpha()
        )
        firstname = self.get_valid_input(
            f"Please enter {lastname} first name: ", lambda x: x.isalpha()
        )
        birthdate = self.get_valid_input(
            f"Please enter {lastname} {firstname} date of birth (dd/mm/yyyy): ",
            lambda x: bool(self.DATE_FORMAT.match(x)),
        )
        gender = self.get_valid_input(
            f"Please enter {lastname} {firstname} sex (M/F): ",
            lambda x: x.upper() in self.GENDER_OPTIONS,
        )
        player_data = {
            "lastname": lastname,
            "firstname": firstname,
            "birthdate": birthdate,
            "gender": gender,
        }
        return player_data

    def print_success(self, player_data):
        print(
            f"The player {player_data['lastname']} {player_data['firstname']} has been successfully created."
        )
        time.sleep(2)
