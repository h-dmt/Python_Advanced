from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    INIT_WEIGHT = 7

    def __init__(self, name: str, kind: str, price: float, weight: int = INIT_WEIGHT):
        super().__init__(name, kind, price, weight)

    def eating(self):
        self.weight += 1
