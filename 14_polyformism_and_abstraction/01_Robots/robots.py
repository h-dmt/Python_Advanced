class Robot:
    def __init__(self, name):
        self.name = name

    def sensors_amount(self):
        return 1


class MedicalRobot(Robot):
    
    def sensors_amount(self):
        return 6


class ChefRobot(Robot):
    
    def sensors_amount(self):
        return 4


class WarRobot(Robot):

    def sensors_amount(self):
        return 12

"""
def number_of_robot_sensors(Robot):
    print(robot.sensors_amount())
    print(robot.medical_robot_sensors_amount())
    print(robot.chef_robot_sensors_amount())
    print(robot.war_robot_sensors_amount())

"""

basic_robot = Robot('Robo')
print(basic_robot.sensors_amount())
da_vinci = MedicalRobot('Da Vinci')
print(da_vinci.sensors_amount())
moley = ChefRobot('Moley')
print(moley.sensors_amount())
griffin = WarRobot('Griffin')
print(griffin.sensors_amount())

