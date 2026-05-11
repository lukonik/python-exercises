import math


class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    @property
    def area(self):
        return math.pi * (self.radius**2)


circle = Circle(10)

print(f"{circle.area:.2f}")


circle.radius = 20

print(f"{circle.area:.2f}")
