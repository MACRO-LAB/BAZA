"""#27. Как работает __slots__ с property и при наследовании | ООП Python
в наследовании там свои примочки, дочерний класс не наследует __slots__, выводить создавать и dict работаеют
если прописаать в дочернем к примеру  __slots__ = "z",    то  что та там будет, не понял
"""


class Point2D:
    __slots__ = ("x", "y" , "__length")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = (x * x + y * y) ** 0.5

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

pt = Point2D(1, 2)
print(pt.length)
"""Итог __slots__ запрещает только локальные, length - это уже атрибуты самого класса"""