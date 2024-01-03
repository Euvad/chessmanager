class Round:
    def __init__(self, matches, number, start_date=None, end_date=None):
        self.matches = matches
        self.number = number
        self.start_date = start_date
        self.end_date = end_date

    def __call__(self):
        return self
