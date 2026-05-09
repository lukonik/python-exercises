from __future__ import annotations


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, point: Point):
        return Point(self.x + point.x, self.y + point.y)

    def __str__(self):
        return f"({self.x},{self.y})"


p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)
