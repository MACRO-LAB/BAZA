"""21. Функция issubclass(). Наследование от встроенных типов и от object | ООП Python"""
"""issubclass - проврка на наследование, только КЛАССОВ!, при проверке объектов возвращает ошибку"""
"""isinstance - проврка на наследование,экземляров """

from ex20 import Rect


class Geom:
    pass


class Line(Geom):
    pass


g = Geom()
l = Line()
print(g, l)
print(l.__class__)
print(issubclass(Line, Geom))
print(isinstance(l, Geom))

print(issubclass(int, object)) #True
"""Доказательство того , что стандартные методы это классы / и есть возможность переопределить их"""
