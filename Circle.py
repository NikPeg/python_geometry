import Figure
import Point
import Color
import settings
import math


class Circle(Figure):
    centre = None
    radius = 0

    def __init__(self, _x, _y, _radius, _color):
        self.centre = Point.Point(_x, _y)
        self.radius = _radius
        self.color = eval(f"Color.Color.{_color}")

    @property
    def perimeter(self):
        return 2 * math.pi * self._radius

    def print(self):
        settings.fout.write("Circle(")
        self._centre.print()
        settings.fout.write(f", {self._radius}) ")
        settings.fout.write(f"Perimeter: {self.perimeter}\n")
