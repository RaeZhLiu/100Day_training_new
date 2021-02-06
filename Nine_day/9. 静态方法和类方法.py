import math


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c & a + c > b & b + c > a

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self._a + self._b + self._c
        return math.sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))


if __name__ == '__main__':
    x, y, z = 3, 4, 5
    if Triangle.is_valid(x, y, z):
        t = Triangle(x, y, z)
        print("三角形周长为：", t.perimeter())
        print("三角形面积为：", t.area())
    else:
        print("三边长度有误，构不成三角形")

