# game.py

from player import Player
from mission import Mission

class Game:
    def __init__(self, player_name):
        self.player = Player(player_name)
        self.missions = []
        self.current_mission_index = 0

    def add_mission(self, mission):
        self.missions.append(mission)

    def get_current_mission(self):
        if self.current_mission_index < len(self.missions):
            return self.missions[self.current_mission_index]
        return None

    def complete_current_mission(self):
        self.current_mission_index += 1

