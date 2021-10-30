import Figure
import Point


class Rectangle(Figure.Figure):
    left_up = None
    right_down = None

    def __init__(self):
        left_up = Point.Point()
        right_down = Point.Point()

    def __init__(self, _left_up, _right_down, _color):
        left_up = _left_up
        right_down = _right_down
        color = _color

    @property
    def perimeter(self):
        return 2 * (abs(self.left_up.x - self.right_down.x) + abs(self.left_up.y - self.right_down.y))

    def read(self):
        char color_char;
        scanf("%d %d %d %d %s", &left_up.x, &left_up.y, &right_down.x, &right_down.y, &color_char)
        color = stringToColor(color_char)

    void print() override {
        printf("Rectangle(");
        left_up.print();
        printf(", ");
        right_down.print();
        printf(") ");
        printf("Perimeter: %f\n", perimeter());
    }
};

#endif //GEOMETRY_RECTANGLE_H
