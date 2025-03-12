"""7. Магические методы __setattr__, __getattribute__, __getattr__ и __delattr__ | ООП Python"""


class Point:
    MAX_COORD = 90
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    """Пример того , что создается новай атрибут,  а не меняется атрибут КЛАССА"""
    # def set_bound(self, left):
    #     self.MIN_COORD = left
    """как правильно делать"""

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left

    def __getattribute__(self, item):
        """То-есть как только идет обращение к атрибуту через экземпляр класса, то вызывается этот метод"""
        print("__getattribute__")
        if item == "x":
            raise ValueError("x не может быть изменен")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        """Вызывается при изменении атрибута"""
        print("__setattr__")
        if key == "z":
            raise ValueError("z не может быть изменен")
        else:
            """так делать нельзя , это рекурсия"""
            # self.x = value  200
            """Лучше выбрать жти варианты"""
            return object.__setattr__(self, key, value)
            # self.__dict__[key] = value

    def __getattr__(self, item):
        """Вызывается при обращении к несуществующему атрибуту"""
        """как вариант чтобы вместо ошибок выводилось что нибудь другое"""
        return  False

    def __delattr__(self, item):
        """Вызывается при удалении атрибута"""
        print("__delattr__")
        object.__delattr__(self, item)

pt_1 = Point(1, 2)
pt_2 = Point(10, 20)
pt_1.y = 100
print(pt_1.b)

del pt_1.x
print(pt_1.__dict__)


""" Магические методы __setattr__, __getattribute__, __getattr__ и __delattr__"""
