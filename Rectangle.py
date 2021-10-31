import Figure
import Point
import Color
import settings


class Rectangle(Figure.Figure):
    left_up = None
    right_down = None

    def __init__(self, _left_up_x, _left_up_y, _right_down_x, _right_down_y, _color):
        self.left_up = Point.Point(int(_left_up_x), int(_left_up_y))
        self.right_down = Point.Point(int(_right_down_x), int(_right_down_y))
        self.color = eval(f"Color.Color.{_color}")

    @property
    def perimeter(self):
        return 2 * (abs(self.left_up.x - self.right_down.x) + abs(self.left_up.y - self.right_down.y))

    def print(self):
        settings.fout.write("Rectangle(")
        self.left_up.print()
        settings.fout.write(" ")
        self.right_down.print()
        settings.fout.write(") ")
        settings.fout.write(f"Perimeter: {self.perimeter}\n")
