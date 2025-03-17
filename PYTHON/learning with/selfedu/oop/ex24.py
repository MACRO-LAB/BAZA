"""#24. Полиморфизм и абстрактные методы | Объектно-ориентированное программирование Python

"""
import inspect


class Geom:
    def get_pr(self):
        # method_name = inspect.currentframe().f_code.co_name
        # return f"в {self.__class__.__name__} нет абстрактных методов {method_name}"
        raise NotImplementedError("Метод get_pr должен быть переопределен в подклассе")


class Rectangle(Geom):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_pr(self):
        return 2 * (self.width * self.height)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4 * self.a


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        pass
        # return self.a + self.b + self.c


geom = [
    Rectangle(1, 2), Rectangle(3, 4),
    Square(10), Square(20),
    Triangle(1, 2, 3),
    Triangle(4, 5, 6)
]
for g in geom:
    print(g.get_pr())

# print(r1.get_rect_pr(),r2.get_rect_pr())
# print(s1.get_sq_pr(),s2.get_sq_pr())
