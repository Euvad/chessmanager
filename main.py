from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem
from source.controllers.tournament import TournamentController
from source.controllers.player import PlayerController

MENU_TITLE = """\
      _______ ______________  __  ____  _______
     / ___/ // / __/ __/ __/ /  |/  / |/ / ___/
    / /__/ _  / _/_\ \_\ \  / /|_/ /    / (_ / 
    \___/_//_/___/___/___/ /_/  /_/_/|_/\___/  """

MAIN_DESC = "Welcome manager!"


def main():
    menu = ConsoleMenu(MENU_TITLE, MAIN_DESC)

    # Instance creation
    tournament_controller = TournamentController()
    player_controller = PlayerController()
    # Add items to the menu
    new_tournament = FunctionItem(
        "Create a new tournament", tournament_controller.new_tournament
    )
    new_player = FunctionItem("Create a new player", player_controller.new_player)
    load_tournament = FunctionItem(
        "Load a tournament", tournament_controller.load_tournament
    )
    menu.append_item(new_tournament)
    menu.append_item(load_tournament)
    menu.append_item(new_player)
    menu.show()


if __name__ == "__main__":
    main()
