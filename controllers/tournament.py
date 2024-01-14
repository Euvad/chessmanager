from views.tournament import TournamentView
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from models.player import Player
import time
from prettytable import PrettyTable
from datetime import datetime


class TournamentController:
    def __init__(self):
        self.tournament_view = TournamentView()

    def new_tournament(self):
        tournament_data = self.tournament_view.get_tournament_info(
            players=Player.get_player_db()
        )
        tournament_model = Tournament(
            id=0,
            name=tournament_data["name"],
            location=tournament_data["location"],
            start_date=tournament_data["start_date"],
            end_date=tournament_data["end_date"],
            description=tournament_data["description"],
            current_round=0,
            rounds_total=4,
            players=tournament_data["players"],
            max_players=tournament_data["max_players"],
            rounds=[],
        )
        tournament_model.save_tournament_db()

    def draw_tournament(self):
        tournaments = Tournament.load_tournament_db()
        final_players = []
        tournament_names = [tournament["name"] for tournament in tournaments]
        selected_tournament = self.tournament_view.select_tournament(tournament_names)
        players = Player.get_player_db()
        for tournament in tournaments:
            if selected_tournament == tournament["name"]:
                found_tournament = tournament
                found_players = found_tournament["players"]
                for player in players:
                    if player.doc_id in found_players:
                        final_players.append(player)
                break 
        else:
            print("not found")
            return
        self.start_tournament(found_tournament, final_players)

    def start_tournament(self, tournament, players):
        tournament_data = Tournament(
            id=tournament["id"],
            name=tournament["name"],
            location=tournament["location"],
            start_date=tournament["start_date"],
            end_date=tournament["end_date"],
            description=tournament["description"],
            current_round=tournament["current_round"],
            rounds_total=tournament["rounds_total"],
            players=tournament["players"],
            max_players=tournament["max_players"],
            rounds=["rounds"],
        )
        tournament_data.update_attribute(
            "start_date", datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        while tournament_data.current_round <= tournament_data.rounds_total:
            if tournament_data.current_round == 1:
                self.first_round(tournament_data, players)
            else:
                self.next_round(tournament_data, players)

            tournament_data.current_round += 1
            tournament_data.update_tournament_db()

        if tournament_data.current_round > 1:
            tournament_data.update_attribute(
                "end_date", datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            self.tournament_end(tournament)

    def add_round(self, tournament, round):
        tournament.rounds.append(round)

    def first_round(self, tournament, players):
        round_number = tournament.current_round
        current_round = Round(round_number)
        tr = tournament
        # Shuffle the players for pairing
        import random

        random.shuffle(players)

        for i in range(0, len(players), 2):
            match = Match(players[i], players[i + 1])
            current_round.add_match(match)

        self.play_round(current_round)
        self.add_round(tr, current_round.to_serializable())

    def next_round(self, tournament, players):
        tr = tournament
        round_number = tr.current_round
        current_round = Round(round_number)
        for i in range(0, len(players), 2):
            match = Match(players[i], players[i + 1])
            current_round.add_match(match)

        self.play_round(current_round)
        self.add_round(tr, current_round.to_serializable())

    def play_round(self, current_round):
        print(f"-------- Round {current_round.round_number} --------")
        for match in current_round.matches:
            result = input(
                f"Enter the result for {match.player1["last_name"]} vs {match.player2["last_name"]} (e.g., 1-0, 0-1, 1/2-1/2): "
            )
            match.play_match(result)

    def tournament_end(self, tournament):
        print("Tournament ended. Results and winners can be determined here.")

