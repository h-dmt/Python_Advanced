import math
from abc import abstractmethod, ABC
from typing import List


class Shape(ABC):
    # Create a Shape class in order not to violate the Single Responsibility Principle
    @abstractmethod
    def find_area(self):
        ...


class Rectangle(Shape):

    def __init__(self, width, height):
        self.w = width
        self.h = height

    def find_area(self):
        return self.w * self.h


class Triangle(Shape):

    def __init__(self, b, h):
        self.b = b
        self.h = h

    def find_area(self):
        return self.b * self.h / 2


class Circle(Shape):

    def __init__(self, r):
        self.r = r

    def find_area(self):
        return self.r ** 2 * math.pi


class AreaCalculator:
    # Every Shape has a dedicated method for finding area and this is passed to
    # AreaCalculator in order to satisfy the Open/Closed Principle.
    def __init__(self, shapes):

        self.shapes: List[Shape] = shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.__shapes = value

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.find_area()

        return total


rectangle_1 = Rectangle(2, 3)
rectangle_2 = Rectangle(1, 6)
circle = Circle(3)
triangle = Triangle(3, 2)
shapes = [rectangle_1, rectangle_2, circle, triangle]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
