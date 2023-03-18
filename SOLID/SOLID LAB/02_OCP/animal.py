from abc import abstractmethod
from typing import List


class Animal:
    def __init__(self, species):
        self.species = species  # [animals...]

    @staticmethod
    @abstractmethod
    def make_sound():
        ...


class Cat(Animal):
    @staticmethod
    def make_sound():
        return 'meow'


class Dog(Animal):
    @staticmethod
    def make_sound():
        return 'woof-woof'


class Human(Animal):
    @staticmethod
    def make_sound():
        return 'bla-bla'


def animal_sound(animals: List[Animal]):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat, Dog, Human]
animal_sound(animals)

