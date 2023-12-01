
class Tournament:

    def __init__(
            self,
            t_id: int,
            name: str,
            location: str,
            start_date: str,
            end_date: str,
            description: str,
            time_control: str,
            current_round: int,
            players: list,
            rounds: list,
            rounds_total=4
    ):
        self.t_id = t_id
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.time_control = time_control
        self.current_round = current_round
        self.rounds_total = rounds_total
        self.players = players
        self.rounds = rounds
