from math import sqrt


class Vector:
    x = 0
    y = 0


    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def calc_from_reflect(x1, x2, y1, y2):
        x = x2 - x1
        y = y2 - y1
        magnitude = sqrt(x**2 + y**2)
        x /= magnitude
        y /= magnitude

        return Vector(x, y)
