import math
import settings


class Point:
    x = 0
    y = 0

    def __init__(self):
        pass

    def __init__(self, _x, _y):
        self.__init__()
        self.x = _x
        self.y = _y

    @staticmethod
    def distance(a, b):
        return math.sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y))

    def print(self):
        settings.fout.write(f"({self.x}, {self.y})")
