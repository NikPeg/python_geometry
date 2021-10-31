import Figure
import Point
import Color
import settings
import math


class Circle(Figure.Figure):
    centre = None
    radius = 0

    def __init__(self, _x, _y, _radius, _color):
        self.centre = Point.Point(float(_x), float(_y))
        self.radius = float(_radius)
        self.color = eval(f"Color.Color.{_color}")

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    def print(self):
        settings.fout.write("Circle(")
        self.centre.print()
        settings.fout.write(f", {self.radius}) ")
        settings.fout.write(f"Perimeter: {self.perimeter}\n")
