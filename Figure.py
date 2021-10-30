import Color


class Figure:
    color = Color.Color.RED
    perimeter = 0

    def print(self):
        pass

    def __lt__(self, other):
        return self.perimeter < other.perimeter

    def __eq__(self, other):
        return self.perimeter == other.perimeter
