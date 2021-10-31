import Color


class Figure:
    color = Color.Color.RED

    def print(self):
        pass

    @property
    def perimeter(self):
        return 0

    def __lt__(self, other):
        return self.perimeter < other.perimeter

    def __eq__(self, other):
        return self.perimeter == other.perimeter
