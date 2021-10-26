from Weapon import Weapon

class Robot:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power
        self.weapon = Weapon('Machine Gun', 50)

    def attack(self, dino):
        dino.health = dino.health - self.attack_power