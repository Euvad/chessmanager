from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem
from controllers.tournament import TournamentController
from controllers.player import PlayerController
from controllers.rapport import ReportController

MENU_TITLE = """\
      _______ ______________  __  ____  _______
     / ___/ // / __/ __/ __/ /  |/  / |/ / ___/
    / /__/ _  / _/_\ \_\ \  / /|_/ /    / (_ / 
    \___/_//_/___/___/___/ /_/  /_/_/|_/\___/  """

MAIN_DESC = "Welcome manager!"


def main():
    menu = ConsoleMenu(MENU_TITLE, MAIN_DESC)

    def new_tournament_func():
        tournament_controller = TournamentController()
        tournament_controller.new_tournament()

    def new_player_func():
        player_controller = PlayerController()
        player_controller.new_player()

    def load_tournament_func():
        tournament_controller = TournamentController()
        tournament_controller.draw_tournament()

    def new_report_func():
        report_controller = ReportController()
        report_controller.new_report()

    # Add menu options with modified function items
    new_tournament = FunctionItem("Create a new tournament", new_tournament_func)
    new_player = FunctionItem("Create a new player", new_player_func)
    load_tournament = FunctionItem("Load a tournament", load_tournament_func)
    new_report = FunctionItem("Generate reports", new_report_func)

    # Append the new options into MenuCls
    menu.append_item(new_tournament)
    menu.append_item(load_tournament)
    menu.append_item(new_player)
    menu.append_item(new_report)
    menu.show()


if __name__ == "__main__":
    main()
