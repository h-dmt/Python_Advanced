from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str) -> str:
        valid_types = {"MainService": MainService, "SecondaryService": SecondaryService}

        if service_type not in valid_types:
            raise Exception("Invalid service type!")

        service = valid_types[service_type](name)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> str:
        valid_types = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}
        if robot_type not in valid_types:
            raise Exception("Invalid robot type!")

        robot = valid_types[robot_type](name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str) -> str:
        service = next(filter(lambda s: s.name == service_name, self.services))
        robot = next(filter(lambda r: r.name == robot_name, self.robots))
        if service.capacity == 0:
            raise Exception("Not enough capacity for this robot!")

        if (robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ == "MainService") or \
                (robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ == "SecondaryService"):
            return "Unsuitable service."

        self.robots.remove(robot)
        service.robots.append(robot)
        service.capacity -= 1
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str) -> str:
        service = next(filter(lambda s: s.name == service_name, self.services))

        robot = [r for r in service.robots if r.name == robot_name]
        if not robot:
            raise Exception("No such robot in this service!")

        self.robots.append(robot[0])
        service.robots.remove(robot[0])
        service.capacity += 1
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str) -> str:
        service = next(filter(lambda s: s.name == service_name, self.services))
        n_robots = len(service.robots)
        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {n_robots}."

    def service_price(self, service_name: str) -> str:
        service = next(filter(lambda s: s.name == service_name, self.services))
        price = 0
        for r in service.robots:
            price += r.price

        return f"The value of service {service_name} is {price:.2f}."

    def __str__(self):
        result = [service.details() for service in self.services]
        return "\n".join(result)
