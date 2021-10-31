import Figure
import Point
import Color
import settings


class Triangle(Figure.Figure):
    a = None
    b = None
    c = None

    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y, _color):
        self.a = Point.Point(float(a_x), float(a_y))
        self.b = Point.Point(float(b_x), float(b_y))
        self.c = Point.Point(float(c_x), float(c_y))
        self.color = eval(f"Color.Color.{_color}")

    @property
    def perimeter(self):
        return Point.Point.distance(self.a, self.b) + Point.Point.distance(self.b, self.c) + Point.Point.distance(
            self.c, self.a)

    def print(self):
        settings.fout.write("Triangle(")
        self.a.print()
        settings.fout.write(", ")
        self.b.print()
        settings.fout.write(", ")
        self.c.print()
        settings.fout.write(") ")
        settings.fout.write(f"Perimeter: {self.perimeter}\n")
