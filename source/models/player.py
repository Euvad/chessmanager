class Player:

    def __init__(
            self,
            p_id: int,
            last_name: str,
            first_name: str,
            birthday: str,
            gender: str,
    ):
        self.p_id = p_id
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.gender = gender
        self.score = 0.0
        self.opponents = []