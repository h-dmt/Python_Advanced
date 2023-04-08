from project.services.base_service import BaseService


class MainService(BaseService):
    MAX_CAPACITY = 30

    def __init__(self, name: str, capacity: int = MAX_CAPACITY):
        super().__init__(name, capacity)

    def details(self) -> str:
        result = [f"{self.name} Main Service:"]
        names = "Robots:"
        if self.robots:
            for robot in self.robots:
                names += " " + str(robot.name)
        else:
            names += " none"

        result.append(names)
        return '\n'.join(result)
