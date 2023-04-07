from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    SPEED_INCREASE = 2

    def train(self):
        self.speed = self.speed + self.SPEED_INCREASE if self.speed + self.SPEED_INCREASE < self.MAX_SPEED \
            else self.MAX_SPEED
