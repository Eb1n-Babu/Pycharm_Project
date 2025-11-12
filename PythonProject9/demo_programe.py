class FootballPlayer:
    best = "real madrid"
    def __init__(self, name, nationality, club):
        self.name = name
        self.nationality = nationality
        self.club = club

    def display(self):
        return f"{self.name} {self.nationality} {self.club}"

    @classmethod
    def display2(cls):
        print(cls.best)\

    @staticmethod
    def display3():
        print(FootballPlayer.best)


class Club(FootballPlayer):
    def __init__(self, goals, trophies, name, nationality, club):
        super().__init__(name, nationality, club)
        self.goals = goals
        self.trophies = trophies

    def display(self):
        return f"{self.name} {self.nationality} {self.club} {self.goals} {self.trophies}"


f1 = FootballPlayer("CR7","PORTUGAL","ALNAZAR")
print(f1.display())
f1.display2()
f1.display3()


f2 = Club(1000,50,"CR7","PORTUGAL","ALNAZAR")
print(f2.display())
print(f2.name)