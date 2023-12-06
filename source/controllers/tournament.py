from source.views.tournament import TournamentView
from source.models.tournament import Tournament


class TournamentController:
    def __init__(self):
        pass

    def new_tournament(self):
        tournament_view = TournamentView()
        tournament_data = tournament_view.get_tournament_info()

        # Utilisez directement les clés du dictionnaire pour accéder aux données
        tournament_model = Tournament(
            t_id=0,
            name=tournament_data["name"],
            location=tournament_data["location"],
            start_date="Not started",
            end_date="TBD",
            description=tournament_data["description"],
            current_round=1,
            rounds=[],
        )

        tournament_model.save_tournament_db()
