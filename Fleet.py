from Robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []

    def robot_fleet(self):
        robot1 = Robot("Wall-E")
        robot2 = Robot("Optimus")
        robot3 = Robot("Ultron")

        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)