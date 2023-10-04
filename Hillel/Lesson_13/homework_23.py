# Homework 23 by Polskoi Yuri

import math
from task_02 import Point


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return 'Circle' + super().__str__()[5:-1] + f', radius={self.radius})'

    def __add__(self, other):
        new = super().__add__(other)
        return Circle(self.radius + other.radius, new.x, new.y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        radius = abs(self.radius - other.radius)
        return Circle(radius, x, y) if radius != 0 else Point(x, y)


a = Circle(6, 1)
b = Circle(5, 4, 7)
c = Circle(5, 3, 8)

print(a - b)
print(b - c)
