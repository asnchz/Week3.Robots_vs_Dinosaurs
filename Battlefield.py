from Fleet import Fleet
from Herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.run_game()

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winners()
    
    def display_welcome(self):
        print("Welcome to the battle!")

    def battle(self):
        pass

    def dino_turn(self, dinosaur):
        pass
    
    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass