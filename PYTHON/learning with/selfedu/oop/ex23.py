"""23. Наследование. Атрибуты private и protected | Объектно-ориентированное программирование Python

"""
class Geom:
    __name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        print(f"Инициализатор ГЕом для {self.__class__}")
        self.__verify_coord(x1)
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._name = self.__name

    def __verify_coord(self, coord):
        return  0 <= coord <100



class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)  # аналог строки выше #Делинирование
        # self.__verify_coord(x1)
        self._fill = fill

    def get_coords(self):
        return (self._x1, self._y1)


r = Rect(1, 2, 3, 4)
r.get_coords()
print(r._name)