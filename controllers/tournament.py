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
            players_base = Player.get_player_db()
            self.tournament_view.tournament_end(tournament_data, players_base)

    def add_round(self, tournament, round):
        tournament.rounds.append(round)

    def first_round(self, tournament, players):
        round_number = tournament.current_round
        current_round = Round(round_number)
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
        self.calculate_scores(tournament, players)
        players.sort(key=lambda player: player.score, reverse=True)

        played_rounds = tr.rounds[:-1]
        played_pairs = self.get_played_pairs(played_rounds)

        for i in range(0, len(players), 2):
            player1 = players[i]
            player2 = players[i + 1]
            while (player1.id, player2.id) in played_pairs or (
                player2.id,
                player1.id,
            ) in played_pairs:
                random.shuffle(players)
                player1 = players[i]
                player2 = players[i + 1]

            match = Match(player1, player2)
            current_round.add_match(match)
            played_pairs.add((player1.id, player2.id))

        self.tournament_view.play_round(current_round)
        self.add_round(tr, current_round)

    def get_played_pairs(self, played_rounds):
        played_pairs = set()
        for round in played_rounds:
            for match in round.matches:
                player1_id = match.player1.id
                player2_id = match.player2.id
                played_pairs.add((player1_id, player2_id))
                played_pairs.add((player2_id, player1_id))
        return played_pairs

    def calculate_scores(self, tournament, players):
        for round_data in tournament.rounds:
            for match in round_data.matches:
                player1 = next(
                    player for player in players if player.id == match.player1.id
                )
                player2 = next(
                    player for player in players if player.id == match.player2.id
                )

                if match.result == 1:
                    player1.score += 1
                elif match.result == 2:
                    player2.score += 1
                elif match.result == 3:
                    player1.score += 0.5
                    player2.score += 0.5
