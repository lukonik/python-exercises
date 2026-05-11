import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area():
        pass


class Circle(Shape):
    def __init__(self, r: int):
        self.r = r

    def area(self):
        return math.pi * (self.r**2)


class Square(Shape):
    def __init__(self, length: int):
        self.length = length

    def area(self):
        return self.length**2


shapes = [Circle(5), Square(4)]

for shape in shapes:
    print(shape.area())
