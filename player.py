class Player:
    def __init__(self, name):
        self.name = name
        self.credits = 0
        self.skills = []

    def add_credits(self, amount):
        self.credits += amount

    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)


class Game:
    def __init__(self, player_name):
        self.player = Player(player_name)
        self.missions_completed = 0

    def complete_mission(self, reward):
        self.player.add_credits(reward)
        self.missions_completed += 1
