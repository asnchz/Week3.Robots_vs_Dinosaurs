from Weapon import Weapon

class Robot:
    def __init__(self, robot_name, health, robot_weapon, attack_power):
        self.robot_name = robot_name
        self.health = health
        self.robot_weapon = Weapon()
        self.attack_power = attack_power