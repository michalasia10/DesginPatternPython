from enum import Enum
from math import cos, sin


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


# class Point:
#     def __init__(self,a,b,system=CoordinateSystem.CARTESIAN):
#         if system == CoordinateSystem.CARTESIAN:
#             self.x = a
#             self.y = b
#         elif system == CoordinateSystem.POLAR:
#             self.x = a *cos(b)
#             self.y = a *sin(b)

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'


class PointFactory:
    @staticmethod
    def new_cartehsian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


if __name__ == '__main__':
    p = PointFactory.new_cartehsian_point(2, 3)
    p2 = PointFactory.new_polar_point(1, 2)
    print('carthesian point', p, 'polar point', p2)
