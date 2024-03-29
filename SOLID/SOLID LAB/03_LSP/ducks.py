from abc import abstractmethod, ABC


class Duck(ABC):

    def __init__(self):
        self.height = 0

    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def land(self):
        pass


class RubberDuck(Duck):
    def quack(self):
        return "Squeek"

    def walk(self):
        """Rubber duck can walk only if you move it"""
        raise Exception('I cannot walk by myself')

    def fly(self):
        """Rubber duck can fly only if you throw it"""
        raise Exception('I cannot fly by myself')

    def land(self):
        pass


class RobotDuck(Duck):
    HEIGHT = 50

    def quack(self):
        return 'Robotic quacking'

    def walk(self):
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0
