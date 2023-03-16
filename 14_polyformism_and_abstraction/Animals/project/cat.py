from abc import ABC

from project.animal import Animal


class Cat(Animal, ABC):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)

    @property
    def type_sound(self):
        return "Meow meow!"
