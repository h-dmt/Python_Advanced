import math
from abc import ABC, abstractmethod


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    @abstractmethod
    def available_processors(self):
        ...

    @property
    @abstractmethod
    def max_ram(self):
        ...

    @property
    @abstractmethod
    def computer_type(self):
        ...

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    @staticmethod
    def valid_ram(ram):
        value = math.log(ram, 2)
        return math.floor(value) == math.ceil(value)

    def configure_computer(self, processor: str, ram: int):
        # • Every type of computer should be configurable
        # • Valid types: "Laptop", "Desktop Computer"
        if processor not in self.available_processors:
            raise ValueError(f"{processor} is not compatible with "
                             f"{self.computer_type} {self.manufacturer} {self.model}!")

        if not self.valid_ram(ram) or ram > self.max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with "
                             f"{self.computer_type} {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price += int(math.log(ram, 2)) * 100
        self.price += self.available_processors[processor]

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
