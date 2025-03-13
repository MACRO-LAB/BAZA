"""#26. Коллекция __slots__ | Объектно-ориентированное программирование Python
это - коллекция, которая позволяет ограничить доступ к атрибутам класса. __dict__ отсутствует
так же уменьшается память и ускоряется производительность
__sizeof__ - размер объекта проверить
"""
import timeit

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        """Пример как замерить скорость"""
        self.x += 1
        del self.y
        self.y = 0


class Point2D:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc(self):
        self.x += 1
        del self.y
        self.y = 0


p1 = Point(1, 2)
p2 = Point2D(10, 20)
# print(p1.__sizeof__() + p1.__dict__.__sizeof__(), p2.__sizeof__())

t1 = timeit.timeit(p1.calc)
t2 = timeit.timeit(p2.calc)
print(t1, t2)
