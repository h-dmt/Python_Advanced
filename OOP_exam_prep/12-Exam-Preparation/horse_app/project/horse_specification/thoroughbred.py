from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    SPEED_INCREASE = 3

    def train(self):
        self.speed = self.speed + self.SPEED_INCREASE if self.speed + self.SPEED_INCREASE < self.MAX_SPEED \
            else self.MAX_SPEED

