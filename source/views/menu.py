from consolemenu import *
from consolemenu.items import *
from consolemenu.screen import *
import time



class MenuView:
    MENU_TITLE = """\
      _______ ______________  __  ____  _______
     / ___/ // / __/ __/ __/ /  |/  / |/ / ___/
    / /__/ _  / _/_\ \_\ \  / /|_/ /    / (_ / 
    \___/_//_/___/___/___/ /_/  /_/_/|_/\___/  """

    MAIN_MENU_TITLE = "Welcome manager!"

    def __init__(self):
        pass

    def get_tournament_info(self, name):
        location = input(f"Please enter {name} location: ")
        description = input(f"Please enter {name} description: ")
        return [name, location, description]

    def get_player_info(self, lastname):
        firstname = input(f"Please enter {lastname} first name: ")
        birthdate = input(f"Please enter {lastname} {firstname} date of birth (dd/mm/yyyy): ")
        gender = input(f"Please enter {lastname} {firstname} sex (M/F): ")
        return [lastname, firstname, birthdate, gender]

    def create_tournament(self):
        name = input("Please enter the tournament name: ")
        tournament_info = self.get_tournament_info(name)
        clear_terminal()
        print(f"The tournament {name} successfully created.")
        time.sleep(2)
        return tournament_info

    def create_player(self):
        lastname = input("Please enter the new player last name: ")
        player_info = self.get_player_info(lastname)
        clear_terminal()
        print(f"The player {lastname} {player_info[1]} has been successfully created.")
        time.sleep(2)
        return player_info

    def show_main_menu(self):
        menu = ConsoleMenu(self.MENU_TITLE, self.MAIN_MENU_TITLE)
        create_tournament_item = FunctionItem("Create Tournament", self.create_tournament)
        create_player_item = FunctionItem("Create New Player", self.create_player)
        menu.append_item(create_player_item)
        menu.append_item(create_tournament_item)
        menu.show()