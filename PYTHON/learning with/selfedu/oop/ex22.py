"""#22. Наследование. Функция super() и делегирование | ООП Python

"""


class Geom:
    name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        print(f"Инициализатор ГЕом для {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print("Рисование линии")


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        # Geom.__init__(self,x1,y1,x2,y2)
        super().__init__(x1, y1, x2, y2)  # аналог строки выше #Делинирование
        self.fill = fill
        print("инициация Rect")

    def draw(self):
        print("Рисование Rect")


l = Line(0, 0, 10, 20)
r = Rect(1, 2, 3, 4)
print(l.__dict__, r.__dict__, sep="\n")
