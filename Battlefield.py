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
        self.show_robot_opponent_options()
        robot_pick = int(input("Which robot will attack?"))
        self.show_dino_opponent_options()
        dino_pick = int(input("Which dinosaur will defend?"))
        self.fleet.robots[robot_pick].attack(
            self.herd.dinosaurs[dino_pick])
        if self.herd.dinosaurs[dino_pick].health <= 0:
            print("${self.herd.dinosaurs[dino_pick].name} has died!")
            self.herd.dinosaurs.remove(self.herd.dinosaurs[dino_pick])

    def show_dino_opponent_options(self):
        print("Pick your dinosaur!")
        index = 0
        for robot in self.herd.dinosaurs:
            print("Press ${index} for ${dinosaur.name} with ${dinosaur.health} health")
            index += 1

    def show_robot_opponent_options(self):
        print("Pick your robot!")
        index = 0
        for robot in self.fleet.robots:
            print("Press ${index} for ${robot.name} with ${robot.health} health")
            index += 1

    def display_winners(self):
        if len(self.fleet.robots) > len(self.herd.dinosaurs):
           print ('Robots Win!')
        else:
            print('Dinosaurs Win!')
