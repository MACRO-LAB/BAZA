"6. Режимы доступа public, private, protected. Сеттеры и геттеры | ООП Python | Инкапсуляция"
"*attr (без подчеркиваний) - public - публичные атрибуты"
"*_attr (с подчеркиваний) - protected - приватные атрибуты/ по факту ограничений нет, просто некая пометка что это защищенный атрибут"
"*__attr (с двумя подчеркиваний) - private - защищенные атрибуты ? "
"dir() выводит список всех свойст с подчеркиваниями / вывести можно через print(p._Point__z)"
"accessify - модуль  pip install accessify . "

from accessify import private, protected

class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = self._y = self.__z = 0
        if self.__check_value(z) and self.__check_value(x) and self.__check_value(y):
            self.x = x
            self._y = y
            self.__z = 0.98

    "Более сильная защита accessify >"
    @private
    def check_value2(cls, z):
        return type(z) in [int, float]

    "Приват метод через класс метод"
    @classmethod
    def __check_value(cls, z):
        return type(z) in [int, float]

    "сеттеры"
    def set_coord(self, x, y, z):
        if self.__check_value(z) and self.__check_value(x) and self.__check_value(y):
            self.__z = z
        else:
            raise ValueError("значение должно быть числом")

    "геттеры"
    def get_coord(self):
        return self.__z


p = Point(1, 2)
p.x = 200
p.y = "coord_y"
print(p.x, p._y)

p.set_coord(1, 2, 3)
print(p.get_coord())

print(dir(p))
print(p._Point__z)

p.check_value2(2)

