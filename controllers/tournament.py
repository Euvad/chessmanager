from views.tournament import TournamentView
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from models.player import Player
import time
from prettytable import PrettyTable
from datetime import datetime
import random


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
            start_date="NOT STARTED",
            end_date="NOT ENDED",
            description=tournament_data["description"],
            current_round=0,
            rounds_total=tournament_data["rounds_total"],
            players=tournament_data["players"],
            max_players=tournament_data["max_players"],
            rounds=[],
        )
        tournament_model.save_tournament_db()

    def draw_tournament(self):
        tournaments = Tournament.load_tournament_db()
        final_players = []
        tournament_names = [tournament.name for tournament in tournaments]
        selected_tournament_name = self.tournament_view.select_tournament(
            tournament_names
        )
        players = Player.get_player_db()

        for tournament in tournaments:
            if selected_tournament_name == tournament.name:
                found_tournament = tournament
                found_players = found_tournament.players
                for player in players:
                    if player.id in found_players:
                        final_players.append(player)
                break
        else:
            print("Tournament not found")
            return
        self.start_tournament(found_tournament, final_players)

    def start_tournament(self, tournament_data, players):
        tournament_data.update_attribute(
            "start_date", datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        while tournament_data.current_round < tournament_data.rounds_total:
            if tournament_data.current_round == 0:
                self.first_round(tournament_data, players)
                tournament_data.current_round += 1
                tournament_data.update_tournament_db()
            else:
                self.next_round(tournament_data, players)
                tournament_data.current_round += 1
                tournament_data.update_tournament_db()

        if tournament_data.current_round > 1:
            tournament_data.update_attribute(
                "end_date", datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            players_base = Player.get_player_db()  # Get the player database
            self.tournament_view.tournament_end(tournament_data, players_base)

    def add_round(self, tournament, round):
        tournament.rounds.append(round)

    def first_round(self, tournament, players):
        round_number = tournament.current_round
        current_round = Round(round_number)
        # Shuffle the players for pairing
        random.shuffle(players)
        for i in range(0, len(players), 2):
            player1 = players[i]
            player2 = players[i + 1]
            match = Match(player1, player2)
            current_round.add_match(match)
        self.tournament_view.play_round(current_round)
        self.add_round(tournament, current_round)

    def next_round(self, tournament, players):
        tr = tournament
        round_number = tr.current_round
        current_round = Round(round_number)

        players.sort(key=lambda player: player.score, reverse=True)

        used_pairs = set()  # method to fill player who already played

        for i in range(0, len(players), 2):
            player1 = players[i]
            player2 = players[i + 1]
            while (player1.id, player2.id) in used_pairs or (
                player2.id,
                player1.id,
            ) in used_pairs:
                random.shuffle(players)
                player1 = players[i]
                player2 = players[i + 1]

            match = Match(player1, player2)
            current_round.add_match(match)
            used_pairs.add((player1.id, player2.id))
        self.tournament_view.play_round(current_round)
        self.add_round(tr, current_round)
